
"""
Slack履歴をJSONファイルに抽出するスクリプト
"""

import os
import json
import argparse
import time
import yaml
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Generator, Any, Union
from pathlib import Path

from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()

def load_config() -> Dict[str, Any]:
    """設定ファイルを読み込む"""
    config_paths = [
        Path("config.yaml"),  # カレントディレクトリ
        Path(__file__).parent.parent.parent / "config.yaml",  # リポジトリルート
    ]
    
    for config_path in config_paths:
        if config_path.exists():
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    config = yaml.safe_load(f)
                print(f"設定ファイルを読み込みました: {config_path}")
                return config or {}
            except Exception as e:
                print(f"設定ファイルの読み込みに失敗しました: {e}")
                break
    
    print("設定ファイルが見つからないか、読み込めませんでした。デフォルト設定を使用します。")
    return {}


class SlackExtractor:
    """Slackからデータを抽出するクラス"""

    def __init__(self, token: str, auto_join: bool = True, skip_channels: List[str] = None):
        """
        初期化
        
        Args:
            token: Slack APIトークン
            auto_join: 公開チャンネルに自動的に参加するかどうか
            skip_channels: スキップするチャンネルIDのリスト
        """
        self.client = WebClient(token=token)
        self.auto_join = auto_join
        self.skip_channels = skip_channels or []
        self.users = {}
        self._load_users()

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
        """公開チャンネルの一覧を取得"""
        cursor = None
        
        while True:
            try:
                response = self.client.conversations_list(
                    cursor=cursor,
                    types="public_channel"
                )
                
                for channel in response["channels"]:
                    if channel["id"] in self.skip_channels:
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
        """スレッド返信を取得"""
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

    def get_history(self, channel_id: str, oldest: str, latest: Optional[str] = None) -> Generator[Dict[str, Any], None, None]:
        """チャンネル履歴を取得"""
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

    def extract_to_json(self, output_dir: str, year: Optional[int] = None, month: Optional[int] = None, 
                       last_days: Optional[int] = None) -> Dict[str, Any]:
        """
        Slackデータを抽出してJSONファイルに保存
        
        Args:
            output_dir: 出力ディレクトリ
            year: 年（指定しない場合は現在の2ヶ月前）
            month: 月（指定しない場合は現在の2ヶ月前）
            last_days: 過去何日分を取得するか（指定した場合はyear, monthは無視）
            
        Returns:
            抽出結果の概要
        """
        now = datetime.now(timezone.utc)
        
        if last_days:
            latest = now
            oldest = now - timedelta(days=last_days)
        else:
            if year is None or month is None:
                target_date = now - timedelta(days=60)
                year = target_date.year
                month = target_date.month
            
            oldest = datetime(year, month, 1, tzinfo=timezone.utc)
            
            if month == 12:
                latest = datetime(year + 1, 1, 1, tzinfo=timezone.utc)
            else:
                latest = datetime(year, month + 1, 1, tzinfo=timezone.utc)
        
        oldest_ts = str(oldest.timestamp())
        latest_ts = str(latest.timestamp())
        
        os.makedirs(output_dir, exist_ok=True)
        
        start_date_str = oldest.strftime("%Y-%m-%d")
        end_date_str = latest.strftime("%Y-%m-%d")
        date_range_dir = f"{start_date_str}_to_{end_date_str}"
        
        date_range_path = os.path.join(output_dir, date_range_dir)
        os.makedirs(date_range_path, exist_ok=True)
        
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
                channel_file = os.path.join(date_range_path, f"{channel_name}.json")
                with open(channel_file, 'w', encoding='utf-8') as f:
                    json.dump(messages, f, ensure_ascii=False, indent=2)
                
                relative_path = os.path.join(date_range_dir, f"{channel_name}.json")
                result["channels"].append({
                    "id": channel_id,
                    "name": channel_name,
                    "message_count": len(messages),
                    "file": relative_path
                })
                
                print(f"  {len(messages)}件のメッセージを {channel_file} に保存しました")
            else:
                print(f"  メッセージが見つかりませんでした")
        
        summary_file = os.path.join(date_range_path, "summary.json")
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        
        print(f"抽出結果の概要を {summary_file} に保存しました")
        return result


def main():
    """メイン関数"""
    config = load_config()
    
    default_output_dir = config.get('output', {}).get('default_dir', './data')
    default_auto_join = config.get('auto_join', True)
    
    config_skip_channels = config.get('skip_channels', [])
    
    parser = argparse.ArgumentParser(description='Slackの履歴をJSONファイルに抽出するツール')
    parser.add_argument('--token', help='Slack APIトークン', default=os.environ.get('SLACK_TOKEN'))
    parser.add_argument('--output-dir', help=f'出力ディレクトリ（デフォルト: {default_output_dir}）', default=default_output_dir)
    parser.add_argument('--year', type=int, help='抽出する年（指定しない場合は現在の2ヶ月前）')
    parser.add_argument('--month', type=int, help='抽出する月（指定しない場合は現在の2ヶ月前）')
    parser.add_argument('--last-days', type=int, help='過去何日分を取得するか（指定した場合はyear, monthは無視）')
    parser.add_argument('--auto-join', action='store_true', default=default_auto_join, 
                        help=f'公開チャンネルに自動的に参加する（デフォルト: {default_auto_join}）')
    parser.add_argument('--no-auto-join', action='store_false', dest='auto_join',
                        help='公開チャンネルに自動的に参加しない')
    parser.add_argument('--skip-channels', help='スキップするチャンネルIDのカンマ区切りリスト')
    parser.add_argument('--config', help='設定ファイルのパス', default='config.yaml')
    
    args = parser.parse_args()
    
    if not args.token:
        print("エラー: Slack APIトークンが指定されていません。--tokenオプションまたはSLACK_TOKEN環境変数で指定してください。")
        return 1
    
    skip_channels = config_skip_channels.copy()
    if args.skip_channels:
        skip_channels.extend(args.skip_channels.split(','))
    
    if skip_channels:
        print(f"スキップするチャンネル: {', '.join(skip_channels)}")
    
    extractor = SlackExtractor(
        token=args.token,
        auto_join=args.auto_join,
        skip_channels=skip_channels
    )
    
    extractor.extract_to_json(
        output_dir=args.output_dir,
        year=args.year,
        month=args.month,
        last_days=args.last_days
    )
    
    return 0


if __name__ == "__main__":
    exit(main())
