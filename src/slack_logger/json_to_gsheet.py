
"""
JSONファイルからGoogle Spreadsheetにデータをアップロードするスクリプト
"""

import os
import json
import argparse
import time
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any, Union

import google.auth
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleSheetUploader:
    """JSONデータをGoogle Spreadsheetにアップロードするクラス"""

    def __init__(self, client_email: str, private_key: str, folder_id: str):
        """
        初期化
        
        Args:
            client_email: Google Service Accountのメールアドレス
            private_key: Google Service Accountの秘密鍵
            folder_id: Google Driveのフォルダーid
        """
        credentials = service_account.Credentials.from_service_account_info(
            {
                "type": "service_account",
                "project_id": "slack-logger",
                "private_key_id": "key-id",
                "private_key": private_key,
                "client_email": client_email,
                "client_id": "client-id",
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_x509_cert_url": f"https://www.googleapis.com/robot/v1/metadata/x509/{client_email.replace('@', '%40')}"
            },
            scopes=['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        )
        
        self.sheets_service = build('sheets', 'v4', credentials=credentials)
        self.drive_service = build('drive', 'v3', credentials=credentials)
        self.folder_id = folder_id

    def create_spreadsheet(self, name: str, timezone: str = 'UTC') -> Dict[str, Any]:
        """
        新しいスプレッドシートを作成
        
        Args:
            name: スプレッドシートの名前
            timezone: タイムゾーン
            
        Returns:
            作成されたスプレッドシートの情報
        """
        try:
            spreadsheet = self.sheets_service.spreadsheets().create(
                body={
                    'properties': {
                        'title': name,
                        'timeZone': timezone
                    }
                }
            ).execute()
            
            file_id = spreadsheet['spreadsheetId']
            self.drive_service.files().update(
                fileId=file_id,
                addParents=self.folder_id,
                body={'name': name}
            ).execute()
            
            return {
                'id': file_id,
                'name': name,
                'url': f"https://docs.google.com/spreadsheets/d/{file_id}"
            }
            
        except HttpError as error:
            print(f"スプレッドシートの作成に失敗しました: {error}")
            raise

    def get_latest_file(self) -> Optional[Dict[str, Any]]:
        """
        'latest'という名前のスプレッドシートを検索
        
        Returns:
            スプレッドシートの情報（見つからない場合はNone）
        """
        try:
            results = self.drive_service.files().list(
                q="name='latest' and mimeType='application/vnd.google-apps.spreadsheet'",
                fields="files(id, name)"
            ).execute()
            
            files = results.get('files', [])
            if files:
                return {
                    'id': files[0]['id'],
                    'name': files[0]['name'],
                    'url': f"https://docs.google.com/spreadsheets/d/{files[0]['id']}"
                }
            return None
            
        except HttpError as error:
            print(f"最新ファイルの検索に失敗しました: {error}")
            return None

    def copy_spreadsheet(self, file_id: str, new_name: str) -> Dict[str, Any]:
        """
        スプレッドシートをコピー
        
        Args:
            file_id: コピー元のスプレッドシートID
            new_name: 新しいスプレッドシートの名前
            
        Returns:
            コピーされたスプレッドシートの情報
        """
        try:
            copied_file = self.drive_service.files().copy(
                fileId=file_id,
                body={'name': new_name}
            ).execute()
            
            return {
                'id': copied_file['id'],
                'name': new_name,
                'url': f"https://docs.google.com/spreadsheets/d/{copied_file['id']}"
            }
            
        except HttpError as error:
            print(f"スプレッドシートのコピーに失敗しました: {error}")
            raise

    def rename_file(self, file_id: str, new_name: str) -> None:
        """
        ファイル名を変更
        
        Args:
            file_id: ファイルID
            new_name: 新しい名前
        """
        try:
            self.drive_service.files().update(
                fileId=file_id,
                body={'name': new_name}
            ).execute()
            
        except HttpError as error:
            print(f"ファイル名の変更に失敗しました: {error}")
            raise

    def create_sheet(self, spreadsheet_id: str, title: str) -> int:
        """
        スプレッドシート内に新しいシートを作成
        
        Args:
            spreadsheet_id: スプレッドシートID
            title: シートのタイトル
            
        Returns:
            作成されたシートのID
        """
        try:
            result = self.sheets_service.spreadsheets().batchUpdate(
                spreadsheetId=spreadsheet_id,
                body={
                    'requests': [
                        {
                            'addSheet': {
                                'properties': {
                                    'title': title
                                }
                            }
                        }
                    ]
                }
            ).execute()
            
            return result['replies'][0]['addSheet']['properties']['sheetId']
            
        except HttpError as error:
            print(f"シートの作成に失敗しました: {error}")
            raise

    def get_sheet_id_by_name(self, spreadsheet_id: str, sheet_name: str) -> Optional[int]:
        """
        シート名からシートIDを取得
        
        Args:
            spreadsheet_id: スプレッドシートID
            sheet_name: シート名
            
        Returns:
            シートID（見つからない場合はNone）
        """
        try:
            spreadsheet = self.sheets_service.spreadsheets().get(
                spreadsheetId=spreadsheet_id,
                fields='sheets.properties'
            ).execute()
            
            for sheet in spreadsheet['sheets']:
                if sheet['properties']['title'] == sheet_name:
                    return sheet['properties']['sheetId']
            
            return None
            
        except HttpError as error:
            print(f"シート情報の取得に失敗しました: {error}")
            return None

    def format_cell(self, value: Any, is_date: bool = False) -> Dict[str, Any]:
        """
        セルの値を適切な形式に変換
        
        Args:
            value: セルの値
            is_date: 日付かどうか
            
        Returns:
            Google Sheets API用のセルデータ
        """
        if value is None:
            return {'userEnteredValue': {'stringValue': ''}}
        
        if isinstance(value, str):
            return {'userEnteredValue': {'stringValue': value}}
        
        if isinstance(value, bool):
            return {'userEnteredValue': {'boolValue': value}}
        
        if isinstance(value, (int, float)):
            if is_date:
                date_value = (float(value) / 86400) + 25569  # 1970-01-01からの日数 + Excel基準日
                return {
                    'userEnteredValue': {'numberValue': date_value},
                    'userEnteredFormat': {
                        'numberFormat': {
                            'type': 'DATE_TIME',
                            'pattern': 'yyyy-mm-dd hh:mm'
                        }
                    }
                }
            return {'userEnteredValue': {'numberValue': value}}
        
        return {'userEnteredValue': {'stringValue': str(value)}}

    def batch_update(self, spreadsheet_id: str, sheet_id: int, rows: List[List[Dict[str, Any]]]) -> None:
        """
        シートにデータをバッチ更新
        
        Args:
            spreadsheet_id: スプレッドシートID
            sheet_id: シートID
            rows: 行データのリスト
        """
        if not rows:
            return
        
        try:
            self.sheets_service.spreadsheets().batchUpdate(
                spreadsheetId=spreadsheet_id,
                body={
                    'requests': [
                        {
                            'updateCells': {
                                'rows': [{'values': row} for row in rows],
                                'fields': 'userEnteredValue,userEnteredFormat',
                                'start': {
                                    'sheetId': sheet_id,
                                    'rowIndex': 0,
                                    'columnIndex': 0
                                }
                            }
                        }
                    ]
                }
            ).execute()
            
        except HttpError as error:
            if error.resp.status == 429:  # Rate limit exceeded
                print("API制限に達しました。1秒待機します...")
                time.sleep(1)
                self.batch_update(spreadsheet_id, sheet_id, rows)
            else:
                print(f"バッチ更新に失敗しました: {error}")
                raise

    def upload_json_to_sheet(self, json_file: str, spreadsheet_id: str, sheet_name: str) -> int:
        """
        JSONファイルのデータをシートにアップロード
        
        Args:
            json_file: JSONファイルのパス
            spreadsheet_id: スプレッドシートID
            sheet_name: シート名
            
        Returns:
            アップロードされたメッセージ数
        """
        with open(json_file, 'r', encoding='utf-8') as f:
            messages = json.load(f)
        
        if not messages:
            print(f"  {json_file} にメッセージが見つかりませんでした")
            return 0
        
        sheet_id = self.get_sheet_id_by_name(spreadsheet_id, sheet_name)
        if sheet_id is None:
            sheet_id = self.create_sheet(spreadsheet_id, sheet_name)
        
        rows = [[
            self.format_cell("スレッド"),
            self.format_cell("タイムスタンプ"),
            self.format_cell("ユーザー"),
            self.format_cell("テキスト"),
            self.format_cell("詳細")
        ]]
        
        for msg in messages:
            thread_mark = "+" if msg.get("reply_count") else ">" if msg.get("parent_ts") else ""
            
            ts = float(msg.get("ts", 0))
            
            row = [
                self.format_cell(thread_mark),
                self.format_cell(ts, is_date=True),
                self.format_cell(msg.get("user_name", "")),
                self.format_cell(msg.get("text_readable", "") or msg.get("text", "") or 
                               (msg.get("attachments", [{}])[0].get("fallback", "") if msg.get("attachments") else "")),
                self.format_cell(json.dumps({k: v for k, v in msg.items() if k not in ["ts", "user", "text", "user_name", "text_readable"]}))
            ]
            rows.append(row)
        
        batch_size = 100  # 一度に更新する行数
        for i in range(0, len(rows), batch_size):
            batch_rows = rows[i:i+batch_size]
            self.batch_update(spreadsheet_id, sheet_id, batch_rows)
            print(f"  {i+len(batch_rows)}/{len(rows)} 行をアップロードしました")
            if i + batch_size < len(rows):
                time.sleep(1)  # API制限を避けるために待機
        
        return len(messages)

    def upload_from_directory(self, json_dir: str, timezone: str = 'Asia/Tokyo', 
                             use_latest_file: bool = False, backup_with_date: bool = False) -> Dict[str, Any]:
        """
        ディレクトリ内のJSONファイルをGoogle Spreadsheetにアップロード
        
        Args:
            json_dir: JSONファイルのディレクトリ
            timezone: タイムゾーン
            use_latest_file: 'latest'という名前のファイルを使用するかどうか
            backup_with_date: 日付付きのバックアップを作成するかどうか
            
        Returns:
            アップロード結果の概要
        """
        summary_file = os.path.join(json_dir, "summary.json")
        if not os.path.exists(summary_file):
            raise FileNotFoundError(f"サマリーファイルが見つかりません: {summary_file}")
        
        with open(summary_file, 'r', encoding='utf-8') as f:
            summary = json.load(f)
        
        period_start = summary.get("period", {}).get("start", "")
        period_end = summary.get("period", {}).get("end", "")
        
        now = datetime.now(timezone.utc)
        date_str = now.strftime("%Y-%m-%d")
        
        spreadsheet_info = None
        
        if use_latest_file:
            latest_file = self.get_latest_file()
            
            if latest_file:
                spreadsheet_info = latest_file
                print(f"既存の'latest'ファイルを使用します: {spreadsheet_info['url']}")
                
                if backup_with_date:
                    backup_name = f"slack-log-{date_str}"
                    backup_info = self.copy_spreadsheet(spreadsheet_info['id'], backup_name)
                    print(f"バックアップを作成しました: {backup_info['url']}")
            else:
                spreadsheet_info = self.create_spreadsheet('latest', timezone)
                print(f"新しい'latest'ファイルを作成しました: {spreadsheet_info['url']}")
        else:
            if period_start and period_end:
                try:
                    start_date = datetime.fromisoformat(period_start).strftime("%Y-%m")
                    end_date = datetime.fromisoformat(period_end).strftime("%Y-%m")
                    sheet_name = f"slack-log-{start_date}-to-{end_date}"
                except ValueError:
                    sheet_name = f"slack-log-{date_str}"
            else:
                sheet_name = f"slack-log-{date_str}"
            
            spreadsheet_info = self.create_spreadsheet(sheet_name, timezone)
            print(f"新しいスプレッドシートを作成しました: {spreadsheet_info['url']}")
        
        total_messages = 0
        for channel_info in summary.get("channels", []):
            channel_name = channel_info.get("name", "unknown")
            json_file = channel_info.get("file")
            
            if json_file and os.path.exists(json_file):
                print(f"チャンネル {channel_name} のデータをアップロード中...")
                message_count = self.upload_json_to_sheet(json_file, spreadsheet_info['id'], channel_name)
                total_messages += message_count
                print(f"  {message_count}件のメッセージをアップロードしました")
            else:
                print(f"チャンネル {channel_name} のJSONファイルが見つかりません")
        
        result = {
            'spreadsheet_id': spreadsheet_info['id'],
            'spreadsheet_name': spreadsheet_info['name'],
            'spreadsheet_url': spreadsheet_info['url'],
            'total_messages': total_messages,
            'channels': len(summary.get("channels", [])),
            'period': {
                'start': period_start,
                'end': period_end
            }
        }
        
        print(f"合計 {total_messages} 件のメッセージを {len(summary.get('channels', []))} チャンネルからアップロードしました")
        print(f"スプレッドシートURL: {spreadsheet_info['url']}")
        
        return result


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(description='JSONファイルからGoogle Spreadsheetにデータをアップロードするツール')
    parser.add_argument('--client-email', help='Google Service Accountのメールアドレス', 
                        default=os.environ.get('GOOGLE_CLIENT_EMAIL'))
    parser.add_argument('--private-key', help='Google Service Accountの秘密鍵', 
                        default=os.environ.get('GOOGLE_PRIVATE_KEY'))
    parser.add_argument('--folder-id', help='Google Driveのフォルダーid', 
                        default=os.environ.get('GOOGLE_FOLDER_ID'))
    parser.add_argument('--json-dir', help='JSONファイルのディレクトリ', default='./slack_data')
    parser.add_argument('--timezone', help='タイムゾーン', default='Asia/Tokyo')
    parser.add_argument('--use-latest-file', action='store_true', 
                        help="'latest'という名前のファイルを使用する")
    parser.add_argument('--backup-with-date', action='store_true', 
                        help="日付付きのバックアップを作成する（--use-latest-fileと共に使用）")
    
    args = parser.parse_args()
    
    if not args.client_email:
        print("エラー: Google Service Accountのメールアドレスが指定されていません。--client-emailオプションまたはGOOGLE_CLIENT_EMAIL環境変数で指定してください。")
        return 1
    
    if not args.private_key:
        print("エラー: Google Service Accountの秘密鍵が指定されていません。--private-keyオプションまたはGOOGLE_PRIVATE_KEY環境変数で指定してください。")
        return 1
    
    if not args.folder_id:
        print("エラー: Google Driveのフォルダーidが指定されていません。--folder-idオプションまたはGOOGLE_FOLDER_ID環境変数で指定してください。")
        return 1
    
    if not os.path.exists(args.json_dir):
        print(f"エラー: JSONディレクトリが見つかりません: {args.json_dir}")
        return 1
    
    uploader = GoogleSheetUploader(
        client_email=args.client_email,
        private_key=args.private_key,
        folder_id=args.folder_id
    )
    
    uploader.upload_from_directory(
        json_dir=args.json_dir,
        timezone=args.timezone,
        use_latest_file=args.use_latest_file,
        backup_with_date=args.backup_with_date
    )
    
    return 0


if __name__ == "__main__":
    exit(main())
