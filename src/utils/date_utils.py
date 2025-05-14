"""
日付処理ユーティリティ

日付や時間に関する共通処理を提供するモジュール
"""

import os
from datetime import datetime, timedelta, timezone
from typing import Optional, Tuple, Dict, Any, Union


def get_jst_timezone() -> timezone:
    """
    日本標準時のタイムゾーンを取得

    Returns:
        timezone: 日本標準時のタイムゾーン
    """
    return timezone(timedelta(hours=9), name='JST')


def get_timezone_by_name(timezone_str: str = "Asia/Tokyo") -> timezone:
    """
    タイムゾーン名からタイムゾーンオブジェクトを取得

    Args:
        timezone_str: タイムゾーン名

    Returns:
        timezone: タイムゾーンオブジェクト
    """
    # 既知のタイムゾーン名の処理
    if timezone_str == "Asia/Tokyo" or timezone_str == "JST":
        return get_jst_timezone()
    elif timezone_str == "UTC":
        return timezone.utc
    
    try:
        # 環境変数TZを設定してタイムゾーンを取得
        os.environ['TZ'] = timezone_str
        tz = datetime.now().astimezone().tzinfo
        
        # tzinfoがNoneの場合はUTCを返す
        if tz is None:
            return timezone.utc
        
        # tzinfoをtimezoneにキャスト
        if hasattr(tz, 'utcoffset'):
            offset = tz.utcoffset(None) or timedelta(0)
            return timezone(offset)
        
        # デフォルトはUTCを返す
        return timezone.utc
    except Exception as e:
        print(f"タイムゾーンの取得に失敗しました: {e}")
        return timezone.utc


def format_timestamp(ts: Union[str, float], timezone_str: str = "Asia/Tokyo") -> str:
    """
    タイムスタンプを読みやすい形式に変換

    Args:
        ts: Unixタイムスタンプ（文字列または浮動小数点数）
        timezone_str: タイムゾーン名

    Returns:
        str: フォーマットされた日時文字列（YYYY-MM-DD HH:MM:SS）
    """
    tz = get_timezone_by_name(timezone_str)
    timestamp = float(ts) if isinstance(ts, str) else ts
    dt = datetime.fromtimestamp(timestamp, tz=tz)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def get_date_range(
    year: Optional[int] = None,
    month: Optional[int] = None,
    last_days: Optional[int] = None,
    period: Optional[str] = None,
    timezone_str: str = "Asia/Tokyo"
) -> Tuple[datetime, datetime]:
    """
    日付範囲を取得

    Args:
        year: 年（指定しない場合は現在の年）
        month: 月（指定しない場合は現在の月）
        last_days: 過去何日分を取得するか
        period: 期間（YYYY-MM-DD_to_YYYY-MM-DD形式）
        timezone_str: タイムゾーン名

    Returns:
        Tuple[datetime, datetime]: 開始日時と終了日時のタプル
    """
    tz = get_timezone_by_name(timezone_str)
    now = datetime.now(tz)
    
    if period:
        # 期間が指定されている場合
        try:
            start_date_str, end_date_str = period.split("_to_")
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").replace(tzinfo=tz)
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").replace(hour=23, minute=59, second=59, tzinfo=tz)
            return start_date, end_date
        except ValueError:
            print(f"期間の形式が不正です: {period}")
            # 不正な形式の場合はデフォルトの日付範囲を使用
    
    if last_days:
        # 過去N日間が指定されている場合
        end_date = now
        start_date = end_date - timedelta(days=last_days)
        return start_date, end_date
    
    if year and month:
        # 年月が指定されている場合
        start_date = datetime(year, month, 1, tzinfo=tz)
        if month == 12:
            end_date = datetime(year + 1, 1, 1, tzinfo=tz) - timedelta(seconds=1)
        else:
            end_date = datetime(year, month + 1, 1, tzinfo=tz) - timedelta(seconds=1)
        return start_date, end_date
    
    # デフォルト: 過去7日間
    end_date = now
    start_date = end_date - timedelta(days=7)
    return start_date, end_date


def get_date_range_dir(start_date: datetime, end_date: datetime) -> str:
    """
    日付範囲からディレクトリ名を生成

    Args:
        start_date: 開始日時
        end_date: 終了日時

    Returns:
        str: 日付範囲ディレクトリ名（YYYY-MM-DD_to_YYYY-MM-DD形式）
    """
    start_str = start_date.strftime("%Y-%m-%d")
    end_str = end_date.strftime("%Y-%m-%d")
    return f"{start_str}_to_{end_str}"


def get_weekly_date_range(weeks_ago: int = 0, timezone_str: str = "Asia/Tokyo") -> Tuple[datetime, datetime]:
    """
    週次の日付範囲を取得（月曜日から日曜日）

    Args:
        weeks_ago: 何週間前か
        timezone_str: タイムゾーン名

    Returns:
        Tuple[datetime, datetime]: 開始日時と終了日時のタプル
    """
    tz = get_timezone_by_name(timezone_str)
    now = datetime.now(tz)
    
    # 現在の週の日曜日を計算
    days_since_sunday = now.weekday() + 1  # 月曜日が0、日曜日が6
    if days_since_sunday == 7:
        days_since_sunday = 0
    
    end_date = now - timedelta(days=days_since_sunday) + timedelta(days=7 * (1 - weeks_ago))
    end_date = end_date.replace(hour=23, minute=59, second=59)
    
    start_date = end_date - timedelta(days=6)
    start_date = start_date.replace(hour=0, minute=0, second=0)
    
    return start_date, end_date


def get_daily_date_range(days_ago: int = 0, timezone_str: str = "Asia/Tokyo") -> Tuple[datetime, datetime]:
    """
    日次の日付範囲を取得

    Args:
        days_ago: 何日前か
        timezone_str: タイムゾーン名

    Returns:
        Tuple[datetime, datetime]: 開始日時と終了日時のタプル
    """
    tz = get_timezone_by_name(timezone_str)
    now = datetime.now(tz)
    
    target_date = now - timedelta(days=days_ago)
    
    start_date = target_date.replace(hour=0, minute=0, second=0)
    end_date = target_date.replace(hour=23, minute=59, second=59)
    
    return start_date, end_date
