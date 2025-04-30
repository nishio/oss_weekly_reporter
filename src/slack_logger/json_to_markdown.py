"""
SlackのJSONデータからLLM用のMarkdownを生成するスクリプト
"""

import os
import json
import argparse
import glob
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Any, Optional, Union, Tuple

from ..config import Config
from ..utils.file_utils import ensure_dir, read_json_file, write_text_file


class MarkdownGenerator:
    """SlackのJSONデータからMarkdownを生成するクラス"""

    def __init__(self, timezone_str: str = "Asia/Tokyo", skip_channels: Optional[List[str]] = None):
        """
        初期化

        Args:
            timezone_str: タイムゾーン
            skip_channels: スキップするチャンネルIDまたは名前のリスト
        """
        self.timezone_str = timezone_str
        self.jst = (
            timezone(timedelta(hours=9), name="JST")
            if timezone_str == "Asia/Tokyo"
            else None
        )
        self.skip_channels = skip_channels or []

    def _format_timestamp(self, ts: str) -> str:
        """
        タイムスタンプを読みやすい形式に変換

        Args:
            ts: Slackのタイムスタンプ

        Returns:
            フォーマットされた日時文字列
        """
        dt = datetime.fromtimestamp(float(ts), tz=self.jst or timezone.utc)
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def _should_skip_message(self, message: Any) -> bool:
        """
        スキップすべきメッセージかどうかを判定

        Args:
            message: メッセージデータ

        Returns:
            スキップする場合はTrue、そうでない場合はFalse
        """
        if not isinstance(message, dict):
            return False
            
        if message.get("subtype") == "channel_join":
            return True
            
        user_name = message.get("user_name", "").lower()
        if "devin" in user_name:
            return True
            
        return False

    def _format_message(self, message: Dict[str, Any], channel_name: str) -> str:
        """
        メッセージをMarkdown形式に変換

        Args:
            message: メッセージデータ
            channel_name: チャンネル名

        Returns:
            Markdown形式のメッセージ
        """
        user_name = message.get("user_name", "Unknown User")
        text = message.get("text_readable", message.get("text", ""))
        ts = message.get("ts", "")
        formatted_time = self._format_timestamp(ts)

        if message.get("parent_ts"):
            return f"**{user_name}** _{formatted_time}_\n\n{text}\n"

        return f"### **{user_name}** in #{channel_name} _{formatted_time}_\n\n{text}\n"

    def generate_daily_summary(
        self,
        json_dir: Union[str, Path],
        output_file: Optional[Union[str, Path]] = None,
        days_ago: int = 0,
        all_data: bool = False,
    ) -> str:
        """
        指定した日のメッセージをMarkdown形式で要約

        Args:
            json_dir: JSONファイルのディレクトリ
            output_file: 出力ファイル名（指定しない場合は標準出力）
            days_ago: 何日前のデータを対象とするか
            all_data: 全てのデータを出力するかどうか（Trueの場合、日付フィルタリングを行わない）

        Returns:
            生成されたMarkdown
        """
        now = datetime.now(self.jst or timezone.utc)

        if all_data:
            start_of_day = datetime.fromtimestamp(
                0, tz=self.jst or timezone.utc
            )  # UNIXエポック（1970年1月1日）
            end_of_day = now
            date_str = "全期間"
        else:
            target_date = now - timedelta(days=days_ago)
            start_of_day = datetime(
                target_date.year,
                target_date.month,
                target_date.day,
                tzinfo=self.jst or timezone.utc,
            )
            end_of_day = start_of_day + timedelta(days=1)
            date_str = start_of_day.strftime("%Y年%m月%d日")

        start_ts = start_of_day.timestamp()
        end_ts = end_of_day.timestamp()

        markdown = f"# {date_str}のSlack活動まとめ\n\n"

        channel_messages = {}
        json_files = list(Path(json_dir).glob("raw/slack/*.json"))

        for json_file in json_files:
            if json_file.name == "summary.json":
                continue

            channel_name = json_file.stem
            
            if channel_name in self.skip_channels:
                print(f"Markdownからチャンネル {channel_name} をスキップします")
                continue

            try:
                messages = read_json_file(json_file)

                day_messages = []
                for msg in messages:
                    if not isinstance(msg, dict):
                        continue
                        
                    ts = float(msg.get("ts", 0))
                    if (all_data or (start_ts <= ts < end_ts)) and not self._should_skip_message(msg):
                        day_messages.append(msg)

                if day_messages:
                    channel_messages[channel_name] = day_messages

            except Exception as e:
                print(f"ファイル {json_file} の読み込みに失敗しました: {e}")

        if not channel_messages:
            markdown += "この日のメッセージはありませんでした。\n"
        else:
            for channel_name, messages in sorted(channel_messages.items()):
                if messages:
                    markdown += (
                        f"\n## #{channel_name} ({len(messages)}件のメッセージ)\n\n"
                    )

                    messages.sort(key=lambda x: float(x.get("ts", 0)))

                    threads = {}
                    standalone_messages = []

                    for msg in messages:
                        parent_ts = msg.get("parent_ts")
                        if parent_ts:
                            if parent_ts not in threads:
                                threads[parent_ts] = []
                            threads[parent_ts].append(msg)
                        else:
                            standalone_messages.append(msg)

                    for msg in standalone_messages:
                        markdown += self._format_message(msg, channel_name) + "\n"

                        thread_ts = msg.get("ts")
                        if thread_ts in threads:
                            replies = sorted(
                                threads[thread_ts], key=lambda x: float(x.get("ts", 0))
                            )
                            markdown += "#### スレッド返信\n\n"
                            for reply in replies:
                                markdown += (
                                    self._format_message(reply, channel_name) + "\n"
                                )

        if output_file:
            output_path = Path(output_file)
            if "markdown/slack" in str(output_path):
                ensure_dir(output_path.parent)
            else:
                markdown_dir = output_path.parent / "markdown" / "slack"
                ensure_dir(markdown_dir)
                output_path = markdown_dir / output_path.name
            
            write_text_file(content=markdown, file_path=output_path)
            print(f"Markdownを {output_path} に保存しました")

        return markdown

    def generate_weekly_summary(
        self,
        json_dir: Union[str, Path],
        output_file: Optional[Union[str, Path]] = None,
        weeks_ago: int = 0,
        all_data: bool = False,
    ) -> str:
        """
        過去7日間のメッセージをMarkdown形式で要約

        Args:
            json_dir: JSONファイルのディレクトリ
            output_file: 出力ファイル名（指定しない場合は標準出力）
            weeks_ago: 何週間前のデータを対象とするか
            all_data: 全てのデータを出力するかどうか（Trueの場合、日付フィルタリングを行わない）

        Returns:
            生成されたMarkdown
        """
        now = datetime.now(self.jst or timezone.utc)

        if all_data:
            start_date = datetime.fromtimestamp(
                0, tz=self.jst or timezone.utc
            )  # UNIXエポック（1970年1月1日）
            end_date = now
            start_date_str = "全期間"
            end_date_str = now.strftime("%Y年%m月%d日")
        else:
            end_date = now - timedelta(days=7 * weeks_ago)
            start_date = end_date - timedelta(days=6)  # 過去7日間（当日を含む）

            start_date = datetime(
                start_date.year,
                start_date.month,
                start_date.day,
                tzinfo=self.jst or timezone.utc,
            )
            end_date = datetime(
                end_date.year,
                end_date.month,
                end_date.day,
                23,
                59,
                59,
                tzinfo=self.jst or timezone.utc,
            )

            start_date_str = start_date.strftime("%Y年%m月%d日")
            end_date_str = end_date.strftime("%Y年%m月%d日")

        start_ts = start_date.timestamp()
        end_ts = end_date.timestamp()

        markdown = f"# {start_date_str}～{end_date_str}のSlack活動まとめ\n\n"

        channel_messages = {}
        json_files = list(Path(json_dir).glob("raw/slack/*.json"))

        for json_file in json_files:
            if json_file.name == "summary.json":
                continue

            channel_name = json_file.stem
            
            if channel_name in self.skip_channels:
                print(f"Markdownからチャンネル {channel_name} をスキップします")
                continue

            try:
                messages = read_json_file(json_file)

                week_messages = []
                for msg in messages:
                    if not isinstance(msg, dict):
                        continue
                        
                    ts = float(msg.get("ts", 0))
                    if (all_data or (start_ts <= ts < end_ts)) and not self._should_skip_message(msg):
                        week_messages.append(msg)

                if week_messages:
                    channel_messages[channel_name] = week_messages

            except Exception as e:
                print(f"ファイル {json_file} の読み込みに失敗しました: {e}")

        if not channel_messages:
            markdown += "この週のメッセージはありませんでした。\n"
        else:
            total_messages = sum(len(msgs) for msgs in channel_messages.values())
            active_channels = len(channel_messages)

            markdown += f"今週は **{active_channels}個**のチャンネルで合計**{total_messages}件**のメッセージがやり取りされました。\n\n"
            markdown += "## チャンネル別アクティビティ\n\n"

            sorted_channels = sorted(
                channel_messages.items(), key=lambda x: len(x[1]), reverse=True
            )

            for channel_name, messages in sorted_channels:
                markdown += f"- **#{channel_name}**: {len(messages)}件のメッセージ\n"

            markdown += "\n## チャンネル別詳細\n"

            for channel_name, messages in sorted_channels:
                markdown += f"\n### #{channel_name} ({len(messages)}件のメッセージ)\n\n"

                messages.sort(key=lambda x: float(x.get("ts", 0)))

                daily_messages = {}

                for msg in messages:
                    ts = float(msg.get("ts", 0))
                    dt = datetime.fromtimestamp(ts, tz=self.jst or timezone.utc)
                    day_key = dt.strftime("%Y-%m-%d")

                    if day_key not in daily_messages:
                        daily_messages[day_key] = []

                    daily_messages[day_key].append(msg)

                for day, day_messages in sorted(daily_messages.items()):
                    dt = datetime.strptime(day, "%Y-%m-%d")
                    day_str = dt.strftime("%m月%d日(%a)")
                    markdown += f"#### {day_str} - {len(day_messages)}件\n\n"

                    threads = {}
                    standalone_messages = []

                    for msg in day_messages:
                        parent_ts = msg.get("parent_ts")
                        if parent_ts:
                            if parent_ts not in threads:
                                threads[parent_ts] = []
                            threads[parent_ts].append(msg)
                        else:
                            standalone_messages.append(msg)

                    count = 0
                    for msg in standalone_messages:
                        markdown += self._format_message(msg, channel_name) + "\n"
                        count += 1

                        thread_ts = msg.get("ts")
                        if thread_ts in threads:
                            replies = sorted(
                                threads[thread_ts], key=lambda x: float(x.get("ts", 0))
                            )
                            markdown += "#### スレッド返信\n\n"
                            for reply in replies:
                                markdown += (
                                    self._format_message(reply, channel_name) + "\n"
                                )

                    markdown += "\n"

        if output_file:
            output_path = Path(output_file)
            if "markdown/slack" in str(output_path):
                ensure_dir(output_path.parent)
            else:
                markdown_dir = output_path.parent / "markdown" / "slack"
                ensure_dir(markdown_dir)
                output_path = markdown_dir / output_path.name
            
            write_text_file(content=markdown, file_path=output_path)
            print(f"Markdownを {output_path} に保存しました")

        return markdown


def main() -> int:
    """メイン関数"""
    parser = argparse.ArgumentParser(
        description="SlackのJSONデータからLLM用のMarkdownを生成するツール"
    )
    parser.add_argument(
        "--json-dir", help="JSONファイルのディレクトリ"
    )
    parser.add_argument("--output", help="出力ファイル名（指定しない場合は標準出力）")
    parser.add_argument("--timezone", help="タイムゾーン")
    parser.add_argument("--daily", action="store_true", help="日次サマリーを生成")
    parser.add_argument("--weekly", action="store_true", help="週次サマリーを生成")
    parser.add_argument(
        "--days-ago",
        type=int,
        help="何日前のデータを対象とするか（日次サマリー用）",
    )
    parser.add_argument(
        "--weeks-ago",
        type=int,
        help="何週間前のデータを対象とするか（週次サマリー用）",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="全てのデータを出力する（日付フィルタリングを行わない）",
    )
    parser.add_argument("--skip-channels", help="スキップするチャンネルIDまたは名前のカンマ区切りリスト")
    parser.add_argument("--config", help="設定ファイルのパス")

    args = parser.parse_args()
    
    cli_args = {
        "output.default_dir": args.json_dir,
        "output.timezone": args.timezone
    }
    
    # skip_channelsが指定されている場合は追加
    if args.skip_channels:
        cli_args["slack.skip_channels"] = args.skip_channels.split(',')
    
    config = Config(config_file=args.config, cli_args=cli_args)
    
    json_dir = config.get("output.default_dir")
    timezone_str = config.get("output.timezone", "Asia/Tokyo")
    skip_channels = config.get("slack.skip_channels", [])
    
    days_ago = args.days_ago if args.days_ago is not None else 0
    weeks_ago = args.weeks_ago if args.weeks_ago is not None else 0

    generator = MarkdownGenerator(timezone_str=timezone_str, skip_channels=skip_channels)

    if args.weekly:
        markdown = generator.generate_weekly_summary(
            json_dir=json_dir,
            output_file=args.output,
            weeks_ago=weeks_ago,
            all_data=args.all,
        )
    else:  # デフォルトは日次サマリー
        markdown = generator.generate_daily_summary(
            json_dir=json_dir,
            output_file=args.output,
            days_ago=days_ago,
            all_data=args.all,
        )

    if not args.output:
        print(markdown)

    return 0


if __name__ == "__main__":
    exit(main())
