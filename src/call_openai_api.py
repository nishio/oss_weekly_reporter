"""
OpenAI O1 APIを使用してMarkdownファイルを処理するスクリプト
"""

import os
import json
import argparse
import glob
from datetime import datetime
import time
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Union
import openai
from dotenv import load_dotenv

from .config import Config
from .utils.file_utils import ensure_dir, read_text_file, write_text_file, get_latest_data_folder

load_dotenv()

config = Config()






def call_openai_api(
    prompt: str, content: str, model: Optional[str] = None, temperature: Optional[float] = None
) -> Tuple[Optional[str], float]:
    """
    OpenAI APIを呼び出す

    Args:
        prompt: プロンプト
        content: 処理するコンテンツ
        model: 使用するモデル（指定しない場合は設定から取得）
        temperature: 温度パラメータ（指定しない場合は設定から取得）

    Returns:
        APIレスポンスと費用の見積もり
    """
    if model is None:
        model = config.get("openai.model", "o1")
    
    if temperature is None:
        temperature = config.get("openai.temperature", 0.7)
    
    openai.api_key = config.get("openai.api_key", os.getenv("OPENAI_API_KEY"))
    
    if not openai.api_key:
        print("エラー: OpenAI APIキーが設定されていません。")
        return None, 0.0
    
    start_time = time.time()

    try:
        try:
            params = {
                "model": model,
                "messages": [
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": content},
                ]
            }
            
            if model != "o1":
                params["temperature"] = temperature
                
            response = openai.chat.completions.create(**params)
            
            elapsed_time = time.time() - start_time

            input_tokens = response.usage.prompt_tokens
            output_tokens = response.usage.completion_tokens

            input_cost_per_token = 0.000015  # $0.015 / 1K tokens
            output_cost_per_token = 0.000060  # $0.060 / 1K tokens

            estimated_cost = (input_tokens * input_cost_per_token) + (
                output_tokens * output_cost_per_token
            )

            return response.choices[0].message.content, estimated_cost
            
        except AttributeError:
            params = {
                "model": model,
                "messages": [
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": content},
                ]
            }
            
            if model != "o1":
                params["temperature"] = temperature
                
            response = openai.ChatCompletion.create(**params)
            
            elapsed_time = time.time() - start_time

            input_tokens = response["usage"]["prompt_tokens"]
            output_tokens = response["usage"]["completion_tokens"]

            input_cost_per_token = 0.000015  # $0.015 / 1K tokens
            output_cost_per_token = 0.000060  # $0.060 / 1K tokens

            estimated_cost = (input_tokens * input_cost_per_token) + (
                output_tokens * output_cost_per_token
            )

            return response["choices"][0]["message"]["content"], estimated_cost

    except Exception as e:
        print(f"APIの呼び出しに失敗しました: {e}")
        return None, 0.0


def process_slack_data(
    data_dir: Optional[Union[str, Path]] = None,
    output_dir: Optional[Union[str, Path]] = None,
    use_all_summary: bool = False,
    period: Optional[str] = None,
    prompt_file: Optional[Union[str, Path]] = None,
) -> None:
    """
    Slackデータを処理する

    Args:
        data_dir: データディレクトリ
        output_dir: 出力ディレクトリ
        use_all_summary: all_summary.mdを使用するかどうか
        period: 期間（YYYY-MM-DD_to_YYYY-MM-DD形式）
        prompt_file: 使用するプロンプトファイルのパス（指定しない場合はデフォルト）
    """
    if not data_dir:
        try:
            data_dir = get_latest_data_folder()
        except FileNotFoundError as e:
            print(e)
            return

    if data_dir is None:
        print("データディレクトリが指定されていません")
        return
        
    if not output_dir:
        output_dir = data_dir

    data_path = Path(data_dir)
    output_path = Path(output_dir)
    
    ensure_dir(output_path)

    markdown_file = "all_summary.md" if use_all_summary else "weekly_summary.md"
    markdown_path = data_path / "markdown" / "slack" / markdown_file

    if not markdown_path.exists():
        print(f"Markdownファイルが見つかりません: {markdown_path}")
        return

    if not prompt_file:
        prompt_file = Path(__file__).parent.parent / "src" / "slack_logger" / "prompt.txt"
    elif not Path(prompt_file).exists():
        print(f"プロンプトファイルが見つかりません: {prompt_file}")
        return
        
    prompt = read_text_file(prompt_file)
    content = read_text_file(markdown_path)

    if period:
        prompt += f"\n\n対象期間: {period}"

    print(f"Slackデータを処理中: {markdown_path}")
    response, cost = call_openai_api(prompt, content)

    if response:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ai_reports_dir = output_path / "ai_reports"
        ensure_dir(ai_reports_dir)
        output_file = ai_reports_dir / f"slack_summary_{timestamp}.md"

        write_text_file(response, output_file)

        print(f"レスポンスを保存しました: {output_file}")
        print(f"推定費用: ${cost:.6f}")


def process_github_data(
    repo: str, 
    data_dir: Optional[Union[str, Path]] = None, 
    output_dir: Optional[Union[str, Path]] = None,
    prompt_file: Optional[Union[str, Path]] = None,
    org: Optional[str] = None,
) -> None:
    """
    GitHubデータを処理する

    Args:
        repo: リポジトリ名（owner/repo形式）またはカンマ区切りのリポジトリ名リスト
        data_dir: データディレクトリ
        output_dir: 出力ディレクトリ
        prompt_file: 使用するプロンプトファイルのパス（指定しない場合はデフォルト）
        org: 組織名（指定した場合、repoはowner/なしのリポジトリ名のリストとして扱う）
    """
    if not data_dir:
        try:
            data_dir = get_latest_data_folder()
        except FileNotFoundError as e:
            print(e)
            return

    if data_dir is None:
        print("データディレクトリが指定されていません")
        return
        
    if not output_dir:
        output_dir = data_dir

    data_path = Path(data_dir)
    output_path = Path(output_dir)
    
    ensure_dir(output_path)

    repos = repo.split(",")
    
    for single_repo in repos:
        single_repo = single_repo.strip()
        
        if org:
            full_repo = f"{org}/{single_repo}"
        else:
            full_repo = single_repo
            
        repo_name = full_repo.split("/")[1]
        markdown_file = f"github_report-{repo_name}.md"
        markdown_path = data_path / "markdown" / "github" / markdown_file

        if not markdown_path.exists():
            print(f"Markdownファイルが見つかりません: {markdown_path}")
            continue

        if not prompt_file:
            prompt_file = Path(__file__).parent.parent / "src" / "github_logger" / "prompt.txt"
        elif not Path(prompt_file).exists():
            print(f"プロンプトファイルが見つかりません: {prompt_file}")
            return
            
        prompt = read_text_file(prompt_file)
        content = read_text_file(markdown_path)

        print(f"GitHubデータを処理中: {markdown_path}")
        response, cost = call_openai_api(prompt, content)

        if response:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            ai_reports_dir = output_path / "ai_reports"
            ensure_dir(ai_reports_dir)
            output_file = ai_reports_dir / f"github_summary_{repo_name}_{timestamp}.md"

            write_text_file(response, output_file)

            print(f"レスポンスを保存しました: {output_file}")
            print(f"推定費用: ${cost:.6f}")


def main() -> int:
    """メイン関数"""
    parser = argparse.ArgumentParser(
        description="OpenAI O1 APIを使用してMarkdownファイルを処理するツール"
    )
    parser.add_argument(
        "--data-dir", help="データディレクトリ（指定しない場合は最新のフォルダを使用）"
    )
    parser.add_argument(
        "--output-dir",
        help="出力ディレクトリ（指定しない場合はデータディレクトリと同じ）",
    )
    parser.add_argument(
        "--model", help="使用するOpenAIモデル"
    )
    parser.add_argument(
        "--temperature", type=float, help="OpenAI APIの温度パラメータ"
    )
    parser.add_argument(
        "--config", help="設定ファイルのパス"
    )

    subparsers = parser.add_subparsers(dest="command", help="コマンド")

    slack_parser = subparsers.add_parser("slack", help="Slackデータを処理")
    slack_parser.add_argument(
        "--all-summary",
        action="store_true",
        help="weekly_summary.mdの代わりにall_summary.mdを使用",
    )
    slack_parser.add_argument("--period", help="期間（YYYY-MM-DD_to_YYYY-MM-DD形式）")
    slack_parser.add_argument("--prompt-file", help="使用するプロンプトファイルのパス")

    github_parser = subparsers.add_parser("github", help="GitHubデータを処理")
    github_parser.add_argument(
        "--repo", required=True, help="リポジトリ名（owner/repo形式またはカンマ区切りのリスト）"
    )
    github_parser.add_argument("--org", help="組織名（指定した場合、repoはowner/なしのリポジトリ名のリストとして扱う）")
    github_parser.add_argument("--prompt-file", help="使用するプロンプトファイルのパス")

    args = parser.parse_args()
    
    cli_args = {
        "output.default_dir": args.data_dir,
        "openai.model": args.model,
        "openai.temperature": args.temperature
    }
    
    global config
    config = Config(config_file=args.config, cli_args=cli_args)
    
    data_dir = args.data_dir
    output_dir = args.output_dir or data_dir
    
    if not args.command:
        parser.print_help()
        return 1

    if args.command == "slack":
        process_slack_data(
            data_dir=data_dir,
            output_dir=output_dir,
            use_all_summary=args.all_summary,
            period=args.period,
            prompt_file=args.prompt_file,
        )
    elif args.command == "github":
        process_github_data(
            repo=args.repo, 
            data_dir=data_dir, 
            output_dir=output_dir,
            prompt_file=args.prompt_file,
            org=args.org,
        )

    return 0


if __name__ == "__main__":
    exit(main())
