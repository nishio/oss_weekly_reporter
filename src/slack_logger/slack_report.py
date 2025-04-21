"""
Slackデータの抽出からMarkdown生成までを一括で行うスクリプト
"""

import os
import json
import argparse
import glob
import time
import yaml
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Generator, Any, Union, Tuple
from pathlib import Path

from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from .slack_to_json import SlackExtractor, load_config
from .json_to_markdown import MarkdownGenerator

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
    
    if last_days:
        now = datetime.now(timezone.utc)
        oldest = now - timedelta(days=last_days)
        latest = now
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
        generator = MarkdownGenerator(timezone_str=timezone_str)
        
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
    config = load_config()
    
    default_output_dir = config.get('output', {}).get('default_dir', './data')
    default_auto_join = config.get('auto_join', True)
    
    config_skip_channels = config.get('skip_channels', [])
    
    parser = argparse.ArgumentParser(description='Slackデータの抽出からMarkdown生成までを一括で行うツール')
    parser.add_argument('--token', help='Slack APIトークン', default=os.environ.get('SLACK_TOKEN'))
    parser.add_argument('--output-dir', help=f'出力ディレクトリ（デフォルト: {default_output_dir}）', default=default_output_dir)
    parser.add_argument('--year', type=int, help='抽出する年（指定しない場合は現在の2ヶ月前）')
    parser.add_argument('--month', type=int, help='抽出する月（指定しない場合は現在の2ヶ月前）')
    parser.add_argument('--last-days', type=int, default=7, help='過去何日分を取得するか（デフォルト: 7日）')
    parser.add_argument('--period', help='期間（YYYY-MM-DD_to_YYYY-MM-DD形式、指定した場合はyear, month, last_daysは無視）')
    parser.add_argument('--auto-join', action='store_true', default=default_auto_join, 
                        help=f'公開チャンネルに自動的に参加する（デフォルト: {default_auto_join}）')
    parser.add_argument('--no-auto-join', action='store_false', dest='auto_join',
                        help='公開チャンネルに自動的に参加しない')
    parser.add_argument('--skip-channels', help='スキップするチャンネルIDのカンマ区切りリスト')
    parser.add_argument('--timezone', help='タイムゾーン', default="Asia/Tokyo")
    parser.add_argument('--daily', action='store_true', help='日次サマリーを生成（デフォルトは週次サマリー）')
    parser.add_argument('--weekly', action='store_true', default=True, help='週次サマリーを生成（デフォルト）')
    parser.add_argument('--all', action='store_true', help='全てのデータを出力する（日付フィルタリングを行わない）')
    parser.add_argument('--no-markdown', action='store_false', dest='markdown', help='Markdownを生成しない')
    parser.add_argument('--output', help='Markdown出力ファイル名（指定しない場合は自動生成）')
    
    args = parser.parse_args()
    
    if not args.token:
        print("エラー: Slack APIトークンが指定されていません。--tokenオプションまたはSLACK_TOKEN環境変数で指定してください。")
        return 1
    
    skip_channels = config_skip_channels.copy()
    if args.skip_channels:
        skip_channels.extend(args.skip_channels.split(','))
    
    if skip_channels:
        print(f"スキップするチャンネル: {', '.join(skip_channels)}")
    
    result = slack_report(
        token=args.token,
        output_dir=args.output_dir,
        year=args.year,
        month=args.month,
        last_days=args.last_days,
        period=args.period,
        auto_join=args.auto_join,
        skip_channels=skip_channels,
        timezone_str=args.timezone,
        weekly=not args.daily,  # --dailyが指定されていない場合は週次サマリー
        all_data=args.all,
        markdown=args.markdown,
        output_file=args.output
    )
    
    print("処理が完了しました。")
    return 0


if __name__ == "__main__":
    exit(main())
