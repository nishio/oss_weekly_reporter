"""
Slackデータの抽出からMarkdown生成までを一括で行うスクリプト
"""

import os
import json
import argparse
import glob
import time
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Generator, Any, Union, Tuple
from pathlib import Path

from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from .slack_to_json import SlackExtractor
from .json_to_markdown import MarkdownGenerator
from ..config import Config

load_dotenv()


def slack_report(
    token: str,
    output_dir: str = "./data",
    year: Optional[int] = None,
    month: Optional[int] = None,
    last_days: Optional[int] = 7,
    period: Optional[str] = None,
    auto_join: bool = True,
    skip_channels: Optional[List[str]] = None,
    timezone_str: str = "Asia/Tokyo",
    weekly: bool = True,
    all_data: bool = False,
    markdown: bool = True,
    output_file: Optional[str] = None
) -> Dict[str, Any]:
    """
    Slackデータの抽出からMarkdown生成までを一括で行う

    Args:
        token: Slack APIトークン
        output_dir: 出力ディレクトリ
        year: 年（指定しない場合は現在の2ヶ月前）
        month: 月（指定しない場合は現在の2ヶ月前）
        last_days: 過去何日分を取得するか（指定した場合はyear, monthは無視）
        period: 期間（YYYY-MM-DD_to_YYYY-MM-DD形式、指定した場合はyear, month, last_daysは無視）
        auto_join: 公開チャンネルに自動的に参加するかどうか
        skip_channels: スキップするチャンネルIDのリスト
        timezone_str: タイムゾーン
        weekly: 週次サマリーを生成するかどうか（Falseの場合は日次サマリー）
        all_data: 全てのデータを出力するかどうか（Trueの場合、日付フィルタリングを行わない）
        markdown: Markdownを生成するかどうか
        output_file: Markdown出力ファイル名（指定しない場合は自動生成）

    Returns:
        処理結果の概要
    """
    extractor = SlackExtractor(
        token=token,
        auto_join=auto_join,
        skip_channels=skip_channels
    )
    
    result = extractor.extract_to_json(
        output_dir=output_dir,
        year=year,
        month=month,
        last_days=last_days,
        period=period
    )
    
    if period:
        date_range_dir = period
        try:
            start_date_str, end_date_str = period.split("_to_")
            oldest = datetime.strptime(start_date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
            latest = datetime.strptime(end_date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
            latest = latest.replace(hour=23, minute=59, second=59)
        except ValueError as e:
            print(f"期間の形式が正しくありません: {e}")
            print("YYYY-MM-DD_to_YYYY-MM-DD形式で指定してください")
            raise
    elif last_days:
        now = datetime.now(timezone.utc)
        oldest = now - timedelta(days=last_days)
        latest = now
        start_date_str = oldest.strftime("%Y-%m-%d")
        end_date_str = latest.strftime("%Y-%m-%d")
        date_range_dir = f"{start_date_str}_to_{end_date_str}"
    else:
        if year is None or month is None:
            target_date = datetime.now(timezone.utc) - timedelta(days=60)
            year = target_date.year
            month = target_date.month
        
        oldest = datetime(year, month, 1, tzinfo=timezone.utc)
        
        if month == 12:
            latest = datetime(year + 1, 1, 1, tzinfo=timezone.utc)
        else:
            latest = datetime(year, month + 1, 1, tzinfo=timezone.utc)
        
        start_date_str = oldest.strftime("%Y-%m-%d")
        end_date_str = latest.strftime("%Y-%m-%d")
        date_range_dir = f"{start_date_str}_to_{end_date_str}"
    date_range_path = os.path.join(output_dir, date_range_dir)
    
    if markdown:
        generator = MarkdownGenerator(timezone_str=timezone_str, skip_channels=skip_channels)
        
        if not output_file:
            if weekly:
                output_file = os.path.join(date_range_path, "all_summary.md")
            else:
                output_file = os.path.join(date_range_path, "daily_summary.md")
        
        if weekly:
            markdown_content = generator.generate_weekly_summary(
                json_dir=date_range_path,
                output_file=output_file,
                all_data=all_data
            )
        else:
            markdown_content = generator.generate_daily_summary(
                json_dir=date_range_path,
                output_file=output_file,
                all_data=all_data
            )
        
        result["markdown_file"] = output_file
    
    return result


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(description='Slackデータの抽出からMarkdown生成までを一括で行うツール')
    parser.add_argument('--token', help='Slack APIトークン', default=os.environ.get('SLACK_TOKEN'))
    parser.add_argument('--output-dir', help='出力ディレクトリ')
    parser.add_argument('--year', type=int, help='抽出する年（指定しない場合は現在の2ヶ月前）')
    parser.add_argument('--month', type=int, help='抽出する月（指定しない場合は現在の2ヶ月前）')
    parser.add_argument('--last-days', type=int, help='過去何日分を取得するか（デフォルト: 7日）')
    parser.add_argument('--period', help='期間（YYYY-MM-DD_to_YYYY-MM-DD形式、指定した場合はyear, month, last_daysは無視）')
    parser.add_argument('--auto-join', action='store_true', help='公開チャンネルに自動的に参加する')
    parser.add_argument('--no-auto-join', action='store_false', dest='auto_join', help='公開チャンネルに自動的に参加しない')
    parser.add_argument('--skip-channels', help='スキップするチャンネルIDまたは名前のカンマ区切りリスト')
    parser.add_argument('--timezone', help='タイムゾーン')
    parser.add_argument('--daily', action='store_true', help='日次サマリーを生成（デフォルトは週次サマリー）')
    parser.add_argument('--weekly', action='store_true', help='週次サマリーを生成（デフォルト）')
    parser.add_argument('--all', action='store_true', help='全てのデータを出力する（日付フィルタリングを行わない）')
    parser.add_argument('--no-markdown', action='store_false', dest='markdown', help='Markdownを生成しない')
    parser.add_argument('--output', help='Markdown出力ファイル名（指定しない場合は自動生成）')
    parser.add_argument('--config', help='設定ファイルのパス')
    
    args = parser.parse_args()
    
    cli_args = {
        "slack.token": args.token,
        "output.default_dir": args.output_dir,
        "slack.auto_join": args.auto_join if args.auto_join is not None else None,
        "output.timezone": args.timezone
    }
    
    # skip_channelsが指定されている場合は追加
    if args.skip_channels:
        cli_args["slack.skip_channels"] = args.skip_channels.split(',')
    
    config = Config(config_file=args.config, cli_args=cli_args)
    
    token = config.get("slack.token")
    output_dir = config.get("output.default_dir")
    auto_join = config.get("slack.auto_join")
    skip_channels = config.get("slack.skip_channels", [])
    timezone_str = config.get("output.timezone", "Asia/Tokyo")
    
    if not token:
        print("エラー: Slack APIトークンが指定されていません。--tokenオプションまたはSLACK_TOKEN環境変数で指定してください。")
        return 1
    
    if skip_channels:
        print(f"スキップするチャンネル: {', '.join(skip_channels)}")
    
    if args.last_days is None:
        args.last_days = 7
    
    result = slack_report(
        token=token,
        output_dir=output_dir,
        year=args.year,
        month=args.month,
        last_days=args.last_days,
        period=args.period,
        auto_join=auto_join,
        skip_channels=skip_channels,
        timezone_str=timezone_str,
        weekly=not args.daily,  # --dailyが指定されていない場合は週次サマリー
        all_data=args.all,
        markdown=args.markdown,
        output_file=args.output
    )
    
    print("処理が完了しました。")
    return 0


if __name__ == "__main__":
    exit(main())
