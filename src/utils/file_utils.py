"""
ファイル操作ユーティリティ

ファイル操作に関する共通処理を提供するモジュール
"""

import os
import json
import glob
from pathlib import Path
from typing import Dict, List, Any, Optional, Union, Generator, Tuple

from .date_utils import get_date_range_dir


def ensure_dir(directory: Union[str, Path]) -> Path:
    """
    ディレクトリが存在することを確認し、存在しない場合は作成する

    Args:
        directory: 確認/作成するディレクトリのパス

    Returns:
        Path: 作成されたディレクトリのPathオブジェクト
    """
    dir_path = Path(directory)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def get_date_range_path(
    base_dir: Union[str, Path],
    start_date_str: str,
    end_date_str: str
) -> Path:
    """
    日付範囲ディレクトリのパスを取得

    Args:
        base_dir: ベースディレクトリ
        start_date_str: 開始日（YYYY-MM-DD形式）
        end_date_str: 終了日（YYYY-MM-DD形式）

    Returns:
        Path: 日付範囲ディレクトリのパス
    """
    date_range = f"{start_date_str}_to_{end_date_str}"
    return Path(base_dir) / date_range


def get_latest_data_folder(base_dir: Union[str, Path] = "./data") -> str:
    """
    最新のデータフォルダを取得する

    Args:
        base_dir: データディレクトリのベースパス

    Returns:
        str: 最新のデータフォルダのパス
    """
    base_path = Path(base_dir)
    if not base_path.exists():
        raise FileNotFoundError(f"ディレクトリが見つかりません: {base_dir}")

    date_dirs = [d for d in base_path.iterdir() if d.is_dir() and "_to_" in d.name]
    
    if not date_dirs:
        raise FileNotFoundError(f"日付範囲ディレクトリが見つかりません: {base_dir}")
    
    latest_folder = str(max(date_dirs, key=lambda d: d.stat().st_ctime))
    return latest_folder


def read_json_file(file_path: Union[str, Path]) -> Dict[str, Any]:
    """
    JSONファイルを読み込む

    Args:
        file_path: JSONファイルのパス

    Returns:
        Dict[str, Any]: JSONデータ
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"JSONデコードエラー: {file_path} - {e}")
        return {}
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
        return {}


def write_json_file(
    data: Dict[str, Any],
    file_path: Union[str, Path],
    ensure_directory: bool = True
) -> None:
    """
    JSONファイルに書き込む

    Args:
        data: 書き込むデータ
        file_path: 書き込み先ファイルパス
        ensure_directory: ディレクトリが存在しない場合に作成するかどうか
    """
    file_path = Path(file_path)
    
    if ensure_directory:
        ensure_dir(file_path.parent)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def read_text_file(file_path: Union[str, Path]) -> str:
    """
    テキストファイルを読み込む

    Args:
        file_path: テキストファイルのパス

    Returns:
        str: ファイルの内容
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
        return ""


def write_text_file(
    content: str,
    file_path: Union[str, Path],
    ensure_directory: bool = True
) -> None:
    """
    テキストファイルに書き込む

    Args:
        content: 書き込む内容
        file_path: 書き込み先ファイルパス
        ensure_directory: ディレクトリが存在しない場合に作成するかどうか
    """
    file_path = Path(file_path)
    
    if ensure_directory:
        ensure_dir(file_path.parent)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def find_files(
    directory: Union[str, Path],
    pattern: str = "*",
    recursive: bool = True
) -> Generator[Path, None, None]:
    """
    ディレクトリ内のファイルを検索

    Args:
        directory: 検索対象ディレクトリ
        pattern: 検索パターン（glob形式）
        recursive: サブディレクトリも検索するかどうか

    Yields:
        Path: 見つかったファイルのパス
    """
    directory = Path(directory)
    
    if recursive:
        for file_path in directory.glob(f"**/{pattern}"):
            if file_path.is_file():
                yield file_path
    else:
        for file_path in directory.glob(pattern):
            if file_path.is_file():
                yield file_path


def find_json_files(
    directory: Union[str, Path],
    recursive: bool = True
) -> Generator[Path, None, None]:
    """
    ディレクトリ内のJSONファイルを検索

    Args:
        directory: 検索対象ディレクトリ
        recursive: サブディレクトリも検索するかどうか

    Yields:
        Path: 見つかったJSONファイルのパス
    """
    yield from find_files(directory, "*.json", recursive)


def find_markdown_files(
    directory: Union[str, Path],
    recursive: bool = True
) -> Generator[Path, None, None]:
    """
    ディレクトリ内のMarkdownファイルを検索

    Args:
        directory: 検索対象ディレクトリ
        recursive: サブディレクトリも検索するかどうか

    Yields:
        Path: 見つかったMarkdownファイルのパス
    """
    yield from find_files(directory, "*.md", recursive)
