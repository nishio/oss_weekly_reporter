
"""
Slack履歴をJSONファイルに抽出するスクリプト
"""

import os
import json
import argparse
import time
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Generator, Any, Union
from pathlib import Path

from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from ..config import Config
from ..utils.date_utils import get_date_range, get_date_range_dir
from ..utils.file_utils import ensure_dir, write_json_file

load_dotenv()


class SlackExtractor:
    """Slackからデータを抽出するクラス"""

    def __init__(self, token: str, auto_join: bool = True, skip_channels: Optional[List[str]] = None):
        """
        初期化
        
        Args:
            token: Slack APIトークン
            auto_join: 公開チャンネルに自動的に参加するかどうか
            skip_channels: スキップするチャンネルIDまたは名前のリスト
        """
        self.client = WebClient(token=token)
        self.auto_join = auto_join
        self.skip_channels = skip_channels or []
        self.skip_channel_ids = []  # チャンネルIDのリスト
        self.users = {}
        self._load_users()
        self._resolve_channel_names()  # チャンネル名をIDに解決

    def _load_users(self) -> None:
        """ユーザー情報を読み込む"""
        try:
            response = self.client.users_list()
            for user in response["members"]:
                self.users[user["id"]] = {
                    "name": user.get("name", ""),
                    "real_name": user.get("real_name", ""),
                    "display_name": user.get("profile", {}).get("display_name", "")
                }
        except SlackApiError as e:
            print(f"ユーザー情報の取得に失敗しました: {e}")
            
    def _resolve_channel_names(self) -> None:
        """チャンネル名をチャンネルIDに解決する"""
        try:
            response = self.client.conversations_list(types="public_channel")
            channels = response["channels"]
            
            while response.get("response_metadata", {}).get("next_cursor"):
                cursor = response["response_metadata"]["next_cursor"]
                response = self.client.conversations_list(
                    cursor=cursor, types="public_channel"
                )
                channels.extend(response["channels"])
            
            channel_map = {channel["name"]: channel["id"] for channel in channels}
            
            # skip_channelsの各項目がIDかチャンネル名かを判断し、IDのリストを作成
            for item in self.skip_channels:
                if item in channel_map:  # チャンネル名の場合
                    self.skip_channel_ids.append(channel_map[item])
                else:  # IDの場合またはマッチしない場合
                    self.skip_channel_ids.append(item)
            
            print(f"チャンネル名をIDに解決しました: {len(self.skip_channel_ids)}件")
        except SlackApiError as e:
            print(f"チャンネル一覧の取得に失敗しました: {e}")

    def get_username(self, user_id: Optional[str]) -> str:
        """ユーザーIDからユーザー名を取得"""
        if not user_id:
            return ""
        
        user = self.users.get(user_id, {})
        return user.get("real_name") or user.get("display_name") or user.get("name") or user_id

    def _process_text(self, text: Optional[str]) -> str:
        """テキスト内のユーザーIDなどを読みやすい形式に変換"""
        if not text:
            return ""
        
        for user_id, user_info in self.users.items():
            name = user_info.get("name") or user_id
            text = text.replace(f"<@{user_id}>", f"@{name}")
        
        text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
        
        return text

    def get_channels(self) -> Generator[Dict[str, Any], None, None]:
        """
        公開チャンネルの一覧を取得
        
        Yields:
            Dict[str, Any]: チャンネル情報（id, name, is_member等を含む）
        """
        cursor = None
        
        while True:
            try:
                response = self.client.conversations_list(
                    cursor=cursor,
                    types="public_channel"
                )
                
                for channel in response["channels"]:
                    if channel["id"] in self.skip_channel_ids or channel["name"] in self.skip_channels:
                        print(f"チャンネル {channel['name']} ({channel['id']}) をスキップします")
                        continue
                    
                    if (self.auto_join and 
                        not channel.get("is_member") and 
                        not channel.get("is_private") and 
                        not channel.get("is_archived")):
                        try:
                            self.client.conversations_join(channel=channel["id"])
                            channel["is_member"] = True
                            yield channel
                        except SlackApiError as e:
                            print(f"チャンネル {channel['name']} への参加に失敗しました: {e}")
                    elif channel.get("is_member"):
                        yield channel
                
                cursor = response.get("response_metadata", {}).get("next_cursor")
                if not cursor:
                    break
                    
            except SlackApiError as e:
                print(f"チャンネル一覧の取得に失敗しました: {e}")
                break

    def get_replies(self, channel_id: str, thread_ts: str) -> List[Dict[str, Any]]:
        """
        スレッド返信を取得
        
        Args:
            channel_id: チャンネルID
            thread_ts: スレッドの親メッセージのタイムスタンプ
            
        Returns:
            List[Dict[str, Any]]: スレッド返信のリスト（user_name, text_readable等を含む）
        """
        replies = []
        cursor = None
        
        while True:
            try:
                response = self.client.conversations_replies(
                    channel=channel_id,
                    ts=thread_ts,
                    cursor=cursor
                )
                
                for message in response["messages"]:
                    if message["ts"] != thread_ts:  # 親メッセージは除外
                        message["parent_ts"] = thread_ts
                        replies.append(message)
                
                cursor = response.get("response_metadata", {}).get("next_cursor")
                if not cursor:
                    break
                    
            except SlackApiError as e:
                print(f"スレッド返信の取得に失敗しました: {e}")
                break
                
        return replies

    def get_history(
        self, 
        channel_id: str, 
        oldest: str, 
        latest: Optional[str] = None
    ) -> Generator[Dict[str, Any], None, None]:
        """
        チャンネル履歴を取得
        
        Args:
            channel_id: チャンネルID
            oldest: 取得開始タイムスタンプ（Unix時間）
            latest: 取得終了タイムスタンプ（Unix時間、指定しない場合は現在まで）
            
        Yields:
            Dict[str, Any]: メッセージ情報（ts, user_name, text_readable等を含む）
        """
        cursor = None
        
        while True:
            try:
                params = {
                    "channel": channel_id,
                    "cursor": cursor,
                    "oldest": oldest
                }
                if latest:
                    params["latest"] = latest
                
                response = self.client.conversations_history(**params)
                messages = response["messages"]
                
                for i in range(len(messages) - 1, -1, -1):
                    msg = messages[i]
                    
                    if latest and float(latest) < float(msg["ts"]):
                        cursor = None
                        break
                    
                    msg["user_name"] = self.get_username(msg.get("user"))
                    msg["text_readable"] = self._process_text(msg.get("text"))
                    
                    yield msg
                    
                    if msg.get("reply_count"):
                        for reply in self.get_replies(channel_id, msg["ts"]):
                            reply["user_name"] = self.get_username(reply.get("user"))
                            reply["text_readable"] = self._process_text(reply.get("text"))
                            yield reply
                
                cursor = response.get("response_metadata", {}).get("next_cursor")
                if not cursor:
                    break
                    
            except SlackApiError as e:
                print(f"チャンネル履歴の取得に失敗しました: {e}")
                break

    def extract_to_json(
        self, 
        output_dir: Union[str, Path], 
        year: Optional[int] = None, 
        month: Optional[int] = None, 
        last_days: Optional[int] = None, 
        period: Optional[str] = None, 
        timezone_str: str = "UTC"
    ) -> Dict[str, Any]:
        """
        Slackデータを抽出してJSONファイルに保存
        
        Args:
            output_dir: 出力ディレクトリ
            year: 年（指定しない場合は現在の2ヶ月前）
            month: 月（指定しない場合は現在の2ヶ月前）
            last_days: 過去何日分を取得するか（指定した場合はyear, monthは無視）
            period: 期間（YYYY-MM-DD_to_YYYY-MM-DD形式、指定した場合はyear, month, last_daysは無視）
            timezone_str: タイムゾーン名
            
        Returns:
            Dict[str, Any]: 抽出結果の概要（期間情報とチャンネル一覧を含む）
        """
        if year is None and month is None and not last_days and not period:
            now = datetime.now(timezone.utc)
            target_date = now - timedelta(days=60)
            year = target_date.year
            month = target_date.month
        
        oldest, latest = get_date_range(
            year=year,
            month=month,
            last_days=last_days,
            period=period,
            timezone_str=timezone_str
        )
        
        oldest_ts = str(oldest.timestamp())
        latest_ts = str(latest.timestamp())
        
        date_range_dir = get_date_range_dir(oldest, latest)
        
        ensure_dir(Path(output_dir))
        date_range_path = Path(output_dir) / date_range_dir
        ensure_dir(date_range_path)
        
        slack_raw_dir = date_range_path / "raw" / "slack"
        ensure_dir(slack_raw_dir)
        
        start_date_str = oldest.strftime("%Y-%m-%d")
        end_date_str = latest.strftime("%Y-%m-%d")
        print(f"期間 {start_date_str} から {end_date_str} のデータを抽出します")
        print(f"データを {date_range_path} に保存します")
        
        result = {
            "period": {
                "start": oldest.isoformat(),
                "end": latest.isoformat()
            },
            "channels": []
        }
        
        for channel in self.get_channels():
            channel_id = channel["id"]
            channel_name = channel["name"]
            print(f"チャンネル {channel_name} のデータを抽出中...")
            
            messages = []
            for msg in self.get_history(channel_id, oldest_ts, latest_ts):
                messages.append(msg)
                if len(messages) % 100 == 0:
                    print(f"  {len(messages)}件のメッセージを取得しました")
            
            if messages:
                # JSONファイルに保存
                channel_file = slack_raw_dir / f"{channel_name}.json"
                write_json_file(messages, channel_file)
                
                relative_path = Path(date_range_dir) / "raw" / "slack" / f"{channel_name}.json"
                result["channels"].append({
                    "id": channel_id,
                    "name": channel_name,
                    "message_count": len(messages),
                    "file": str(relative_path)
                })
                
                print(f"  {len(messages)}件のメッセージを {channel_file} に保存しました")
            else:
                print(f"  メッセージが見つかりませんでした")
        
        summary_file = slack_raw_dir / "summary.json"
        write_json_file(result, summary_file)
        
        print(f"抽出結果の概要を {summary_file} に保存しました")
        return result


def main() -> int:
    """メイン関数"""
    parser = argparse.ArgumentParser(description='Slackの履歴をJSONファイルに抽出するツール')
    parser.add_argument('--token', help='Slack APIトークン', default=os.environ.get('SLACK_TOKEN'))
    parser.add_argument('--output-dir', help='出力ディレクトリ')
    parser.add_argument('--year', type=int, help='抽出する年（指定しない場合は現在の2ヶ月前）')
    parser.add_argument('--month', type=int, help='抽出する月（指定しない場合は現在の2ヶ月前）')
    parser.add_argument('--last-days', type=int, help='過去何日分を取得するか（指定した場合はyear, monthは無視）')
    parser.add_argument('--period', help='期間（YYYY-MM-DD_to_YYYY-MM-DD形式、指定した場合はyear, month, last_daysは無視）')
    parser.add_argument('--auto-join', action='store_true', help='公開チャンネルに自動的に参加する')
    parser.add_argument('--no-auto-join', action='store_false', dest='auto_join', help='公開チャンネルに自動的に参加しない')
    parser.add_argument('--skip-channels', help='スキップするチャンネルIDまたは名前のカンマ区切りリスト')
    parser.add_argument('--config', help='設定ファイルのパス')
    
    args = parser.parse_args()
    
    cli_args = {
        "slack.token": args.token,
        "output.default_dir": args.output_dir,
        "slack.auto_join": args.auto_join if args.auto_join is not None else None
    }
    
    # skip_channelsが指定されている場合は追加
    if args.skip_channels:
        cli_args["slack.skip_channels"] = args.skip_channels.split(',')
    
    config = Config(config_file=args.config, cli_args=cli_args)
    
    token = config.get("slack.token")
    output_dir = config.get("output.default_dir")
    auto_join = config.get("slack.auto_join")
    skip_channels = config.get("slack.skip_channels", [])
    
    if not token:
        print("エラー: Slack APIトークンが指定されていません。--tokenオプションまたはSLACK_TOKEN環境変数で指定してください。")
        return 1
    
    if skip_channels:
        print(f"スキップするチャンネル: {', '.join(skip_channels)}")
    
    extractor = SlackExtractor(
        token=token,
        auto_join=auto_join,
        skip_channels=skip_channels
    )
    
    timezone_str = config.get("output.timezone", "UTC")
    
    extractor.extract_to_json(
        output_dir=output_dir,
        year=args.year,
        month=args.month,
        last_days=args.last_days,
        period=args.period,
        timezone_str=timezone_str
    )
    
    return 0


if __name__ == "__main__":
    exit(main())
