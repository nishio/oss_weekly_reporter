"""
SlackのJSONデータからLLM用のMarkdownを生成するスクリプト
"""

import os
import json
import argparse
import glob
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Any, Optional


class MarkdownGenerator:
    """SlackのJSONデータからMarkdownを生成するクラス"""

    def __init__(self, timezone_str: str = "Asia/Tokyo"):
        """
        初期化
        
        Args:
            timezone_str: タイムゾーン
        """
        self.timezone_str = timezone_str
        self.jst = timezone(timedelta(hours=9), name="JST") if timezone_str == "Asia/Tokyo" else None

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
            return f"    - **{user_name}**: {text} _{formatted_time}_"
        
        return f"- **{user_name}** in #{channel_name}: {text} _{formatted_time}_"

    def generate_daily_summary(self, json_dir: str, output_file: Optional[str] = None, 
                              days_ago: int = 0) -> str:
        """
        指定した日のメッセージをMarkdown形式で要約
        
        Args:
            json_dir: JSONファイルのディレクトリ
            output_file: 出力ファイル名（指定しない場合は標準出力）
            days_ago: 何日前のデータを対象とするか
            
        Returns:
            生成されたMarkdown
        """
        now = datetime.now(self.jst or timezone.utc)
        target_date = now - timedelta(days=days_ago)
        start_of_day = datetime(target_date.year, target_date.month, target_date.day, 
                               tzinfo=self.jst or timezone.utc)
        end_of_day = start_of_day + timedelta(days=1)
        
        start_ts = start_of_day.timestamp()
        end_ts = end_of_day.timestamp()
        
        date_str = start_of_day.strftime("%Y年%m月%d日")
        
        markdown = f"# {date_str}のSlack活動まとめ\n\n"
        
        channel_messages = {}
        json_files = glob.glob(os.path.join(json_dir, "*.json"))
        
        for json_file in json_files:
            if os.path.basename(json_file) == "summary.json":
                continue
                
            channel_name = os.path.splitext(os.path.basename(json_file))[0]
            
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    messages = json.load(f)
                    
                day_messages = []
                for msg in messages:
                    ts = float(msg.get("ts", 0))
                    if start_ts <= ts < end_ts:
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
                    markdown += f"\n## #{channel_name} ({len(messages)}件のメッセージ)\n\n"
                    
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
                            for reply in sorted(threads[thread_ts], key=lambda x: float(x.get("ts", 0))):
                                markdown += self._format_message(reply, channel_name) + "\n"
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown)
            print(f"Markdownを {output_file} に保存しました")
        
        return markdown

    def generate_weekly_summary(self, json_dir: str, output_file: Optional[str] = None, 
                               weeks_ago: int = 0) -> str:
        """
        指定した週のメッセージをMarkdown形式で要約
        
        Args:
            json_dir: JSONファイルのディレクトリ
            output_file: 出力ファイル名（指定しない場合は標準出力）
            weeks_ago: 何週間前のデータを対象とするか
            
        Returns:
            生成されたMarkdown
        """
        now = datetime.now(self.jst or timezone.utc)
        days_since_monday = now.weekday()
        start_of_week = now - timedelta(days=days_since_monday + 7 * weeks_ago)
        start_of_week = datetime(start_of_week.year, start_of_week.month, start_of_week.day, 
                                tzinfo=self.jst or timezone.utc)
        end_of_week = start_of_week + timedelta(days=7)
        
        start_ts = start_of_week.timestamp()
        end_ts = end_of_week.timestamp()
        
        start_date_str = start_of_week.strftime("%Y年%m月%d日")
        end_date_str = (end_of_week - timedelta(days=1)).strftime("%Y年%m月%d日")
        
        markdown = f"# {start_date_str}～{end_date_str}のSlack活動まとめ\n\n"
        
        channel_messages = {}
        json_files = glob.glob(os.path.join(json_dir, "*.json"))
        
        for json_file in json_files:
            if os.path.basename(json_file) == "summary.json":
                continue
                
            channel_name = os.path.splitext(os.path.basename(json_file))[0]
            
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    messages = json.load(f)
                    
                week_messages = []
                for msg in messages:
                    ts = float(msg.get("ts", 0))
                    if start_ts <= ts < end_ts:
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
            
            sorted_channels = sorted(channel_messages.items(), 
                                    key=lambda x: len(x[1]), reverse=True)
            
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
                        if count >= 10:
                            markdown += "...(省略)...\n\n"
                            break
                            
                        markdown += self._format_message(msg, channel_name) + "\n"
                        count += 1
                        
                        thread_ts = msg.get("ts")
                        if thread_ts in threads:
                            replies = sorted(threads[thread_ts], key=lambda x: float(x.get("ts", 0)))
                            for i, reply in enumerate(replies):
                                if i >= 3:
                                    markdown += f"    - _他 {len(replies) - 3} 件の返信_\n"
                                    break
                                markdown += self._format_message(reply, channel_name) + "\n"
                    
                    markdown += "\n"
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(markdown)
            print(f"Markdownを {output_file} に保存しました")
        
        return markdown


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(description='SlackのJSONデータからLLM用のMarkdownを生成するツール')
    parser.add_argument('--json-dir', help='JSONファイルのディレクトリ', default='./slack_data')
    parser.add_argument('--output', help='出力ファイル名（指定しない場合は標準出力）')
    parser.add_argument('--timezone', help='タイムゾーン', default='Asia/Tokyo')
    parser.add_argument('--daily', action='store_true', help='日次サマリーを生成')
    parser.add_argument('--weekly', action='store_true', help='週次サマリーを生成')
    parser.add_argument('--days-ago', type=int, default=0, help='何日前のデータを対象とするか（日次サマリー用）')
    parser.add_argument('--weeks-ago', type=int, default=0, help='何週間前のデータを対象とするか（週次サマリー用）')
    
    args = parser.parse_args()
    
    generator = MarkdownGenerator(timezone_str=args.timezone)
    
    if args.weekly:
        markdown = generator.generate_weekly_summary(
            json_dir=args.json_dir,
            output_file=args.output,
            weeks_ago=args.weeks_ago
        )
    else:  # デフォルトは日次サマリー
        markdown = generator.generate_daily_summary(
            json_dir=args.json_dir,
            output_file=args.output,
            days_ago=args.days_ago
        )
    
    if not args.output:
        print(markdown)
    
    return 0


if __name__ == "__main__":
    exit(main())
