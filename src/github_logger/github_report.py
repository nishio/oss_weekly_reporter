import requests
import datetime
import os
import subprocess
import json
import argparse
import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Union, Tuple

from ..config import Config
from ..utils.date_utils import get_date_range, get_date_range_dir
from ..utils.file_utils import ensure_dir, write_json_file, read_json_file


def get_github_token():
    try:
        result = subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"GitHub CLIからトークンを取得できませんでした: {e}")
        return None


def extract_username_from_email(email_or_name):
    """
    メールアドレスからユーザー名部分を抽出する
    
    Args:
        email_or_name: メールアドレスまたは名前
        
    Returns:
        ユーザー名（GitHubアカウント名に近い形式）
    """
    if not email_or_name:
        return None
        
    email_match = re.search(r'([^@\s]+)@', email_or_name)
    if email_match:
        return email_match.group(1)
    
    return email_or_name.strip()

def extract_github_data(
    repo: str, 
    output_dir: str = "./data", 
    last_days: int = 7, 
    include_prs: bool = True,
    timezone_str: str = "UTC"
) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    """
    GitHubからissueとPRデータを抽出してJSONファイルに保存
    
    Args:
        repo: リポジトリ名（owner/repo形式）
        output_dir: 出力ディレクトリ
        last_days: 過去何日分を取得するか
        include_prs: PRも含めるかどうか
        timezone_str: タイムゾーン名
    
    Returns:
        抽出結果の概要とJSONファイルのパス
    """
    GITHUB_TOKEN = get_github_token()
    
    if not GITHUB_TOKEN:
        print("GitHub CLIからトークンを取得できませんでした。")
        return None, None
    
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    
    start_date, end_date = get_date_range(last_days=last_days, timezone_str=timezone_str)
    one_week_ago_str = start_date.date().isoformat()
    
    output_path = Path(output_dir)
    ensure_dir(output_path)
    
    date_range_dir = get_date_range_dir(start_date, end_date)
    
    date_range_path = output_path / date_range_dir
    ensure_dir(date_range_path)
    
    github_raw_dir = date_range_path / "raw" / "github"
    ensure_dir(github_raw_dir)
    
    print(f"データを {date_range_path} に保存します")
    
    result = {
        "period": {
            "start": start_date.isoformat(),
            "end": end_date.isoformat()
        },
        "repo": repo,
        "issues": [],
        "prs": []
    }
    
    all_issues = []
    
    query_closed = f"repo:{repo} is:issue closed:>={one_week_ago_str}"
    url_search = "https://api.github.com/search/issues"
    params_closed = {"q": query_closed}
    response_closed = requests.get(url_search, headers=headers, params=params_closed)
    closed_issues = response_closed.json()
    
    query_created = f"repo:{repo} is:issue created:>={one_week_ago_str}"
    params_created = {"q": query_created}
    response_created = requests.get(url_search, headers=headers, params=params_created)
    created_issues = response_created.json()
    
    query_updated = f"repo:{repo} is:issue updated:>={one_week_ago_str} -created:>={one_week_ago_str} -closed:>={one_week_ago_str}"
    params_updated = {"q": query_updated}
    response_updated = requests.get(url_search, headers=headers, params=params_updated)
    updated_issues = response_updated.json()
    
    for issue in closed_issues.get("items", []):
        issue_data = {
            "id": issue["id"],
            "number": issue["number"],
            "title": issue["title"],
            "state": "closed",
            "html_url": issue["html_url"],
            "user": issue["user"]["login"],
            "created_at": issue["created_at"],
            "closed_at": issue.get("closed_at"),
            "body": issue.get("body", ""),
            "type": "issue"
        }
        all_issues.append(issue_data)
        result["issues"].append({
            "id": issue["id"],
            "number": issue["number"],
            "title": issue["title"],
            "state": "closed"
        })
    
    for issue in created_issues.get("items", []):
        if any(i["id"] == issue["id"] for i in all_issues):
            continue
        
        issue_data = {
            "id": issue["id"],
            "number": issue["number"],
            "title": issue["title"],
            "state": "created",
            "html_url": issue["html_url"],
            "user": issue["user"]["login"],
            "created_at": issue["created_at"],
            "body": issue.get("body", ""),
            "type": "issue"
        }
        all_issues.append(issue_data)
        result["issues"].append({
            "id": issue["id"],
            "number": issue["number"],
            "title": issue["title"],
            "state": "created"
        })
    
    for issue in updated_issues.get("items", []):
        if any(i["id"] == issue["id"] for i in all_issues):
            continue
        
        issue_data = {
            "id": issue["id"],
            "number": issue["number"],
            "title": issue["title"],
            "state": "updated",
            "html_url": issue["html_url"],
            "user": issue["user"]["login"],
            "created_at": issue["created_at"],
            "updated_at": issue["updated_at"],
            "body": issue.get("body", ""),
            "type": "issue"
        }
        all_issues.append(issue_data)
        result["issues"].append({
            "id": issue["id"],
            "number": issue["number"],
            "title": issue["title"],
            "state": "updated"
        })
    
    all_prs = []
    
    if include_prs:
        query_merged = f"repo:{repo} is:pr merged:>={one_week_ago_str}"
        params_merged = {"q": query_merged}
        response_merged = requests.get(url_search, headers=headers, params=params_merged)
        merged_prs = response_merged.json()
        
        query_pr_created = f"repo:{repo} is:pr created:>={one_week_ago_str}"
        params_pr_created = {"q": query_pr_created}
        response_pr_created = requests.get(url_search, headers=headers, params=params_pr_created)
        created_prs = response_pr_created.json()
        
        query_pr_updated = f"repo:{repo} is:pr updated:>={one_week_ago_str} -created:>={one_week_ago_str} -merged:>={one_week_ago_str}"
        params_pr_updated = {"q": query_pr_updated}
        response_pr_updated = requests.get(url_search, headers=headers, params=params_pr_updated)
        updated_prs = response_pr_updated.json()
        
        for pr in merged_prs.get("items", []):
            pr_url = f"https://api.github.com/repos/{repo}/pulls/{pr['number']}"
            pr_response = requests.get(pr_url, headers=headers)
            pr_detail = pr_response.json()
            
            commits_url = f"https://api.github.com/repos/{repo}/pulls/{pr['number']}/commits"
            commits_response = requests.get(commits_url, headers=headers)
            commits = commits_response.json()
            
            co_author = None
            requester = None
            
            if commits and len(commits) > 0:
                for commit in commits:
                    commit_message = commit.get("commit", {}).get("message", "")
                    match = re.search(r'Co-Authored-By:\s*([^<]+)', commit_message)
                    if match:
                        co_author = extract_username_from_email(match.group(1).strip())
                        break
            
            pr_body = pr_detail.get("body", "")
            if pr_body:
                match = re.search(r'Requested by:\s*([^\n]+)', pr_body)
                if match:
                    requester = extract_username_from_email(match.group(1).strip())
            
            pr_data = {
                "id": pr["id"],
                "number": pr["number"],
                "title": pr["title"],
                "state": "merged",
                "html_url": pr["html_url"],
                "user": pr["user"]["login"],
                "created_at": pr["created_at"],
                "merged_at": pr_detail.get("merged_at"),
                "body": pr.get("body", ""),
                "additions": pr_detail.get("additions"),
                "deletions": pr_detail.get("deletions"),
                "changed_files": pr_detail.get("changed_files"),
                "co_author": co_author,
                "requester": requester,
                "type": "pr"
            }
            all_prs.append(pr_data)
            result["prs"].append({
                "id": pr["id"],
                "number": pr["number"],
                "title": pr["title"],
                "state": "merged"
            })
        
        for pr in created_prs.get("items", []):
            if any(p["id"] == pr["id"] for p in all_prs):
                continue
            
            pr_url = f"https://api.github.com/repos/{repo}/pulls/{pr['number']}"
            pr_response = requests.get(pr_url, headers=headers)
            pr_detail = pr_response.json()
            
            commits_url = f"https://api.github.com/repos/{repo}/pulls/{pr['number']}/commits"
            commits_response = requests.get(commits_url, headers=headers)
            commits = commits_response.json()
            
            co_author = None
            requester = None
            
            if commits and len(commits) > 0:
                for commit in commits:
                    commit_message = commit.get("commit", {}).get("message", "")
                    match = re.search(r'Co-Authored-By:\s*([^<]+)', commit_message)
                    if match:
                        co_author = extract_username_from_email(match.group(1).strip())
                        break
            
            pr_body = pr_detail.get("body", "")
            if pr_body:
                match = re.search(r'Requested by:\s*([^\n]+)', pr_body)
                if match:
                    requester = extract_username_from_email(match.group(1).strip())
            
            pr_data = {
                "id": pr["id"],
                "number": pr["number"],
                "title": pr["title"],
                "state": "created",
                "html_url": pr["html_url"],
                "user": pr["user"]["login"],
                "created_at": pr["created_at"],
                "body": pr.get("body", ""),
                "additions": pr_detail.get("additions"),
                "deletions": pr_detail.get("deletions"),
                "changed_files": pr_detail.get("changed_files"),
                "co_author": co_author,
                "requester": requester,
                "type": "pr"
            }
            all_prs.append(pr_data)
            result["prs"].append({
                "id": pr["id"],
                "number": pr["number"],
                "title": pr["title"],
                "state": "created"
            })
        
        for pr in updated_prs.get("items", []):
            if any(p["id"] == pr["id"] for p in all_prs):
                continue
            
            pr_url = f"https://api.github.com/repos/{repo}/pulls/{pr['number']}"
            pr_response = requests.get(pr_url, headers=headers)
            pr_detail = pr_response.json()
            
            commits_url = f"https://api.github.com/repos/{repo}/pulls/{pr['number']}/commits"
            commits_response = requests.get(commits_url, headers=headers)
            commits = commits_response.json()
            
            co_author = None
            requester = None
            
            if commits and len(commits) > 0:
                for commit in commits:
                    commit_message = commit.get("commit", {}).get("message", "")
                    match = re.search(r'Co-Authored-By:\s*([^<]+)', commit_message)
                    if match:
                        co_author = extract_username_from_email(match.group(1).strip())
                        break
            
            pr_body = pr_detail.get("body", "")
            if pr_body:
                match = re.search(r'Requested by:\s*([^\n]+)', pr_body)
                if match:
                    requester = extract_username_from_email(match.group(1).strip())
            
            pr_data = {
                "id": pr["id"],
                "number": pr["number"],
                "title": pr["title"],
                "state": "updated",
                "html_url": pr["html_url"],
                "user": pr["user"]["login"],
                "created_at": pr["created_at"],
                "updated_at": pr["updated_at"],
                "body": pr.get("body", ""),
                "additions": pr_detail.get("additions"),
                "deletions": pr_detail.get("deletions"),
                "changed_files": pr_detail.get("changed_files"),
                "co_author": co_author,
                "requester": requester,
                "type": "pr"
            }
            all_prs.append(pr_data)
            result["prs"].append({
                "id": pr["id"],
                "number": pr["number"],
                "title": pr["title"],
                "state": "updated"
            })
    
    repo_name = repo.split("/")[1]
    
    all_data = all_issues + all_prs
    github_file = github_raw_dir / f"{repo_name}.json"
    write_json_file(all_data, github_file)
    
    print(f"{len(all_issues)}件のissueと{len(all_prs)}件のPRを {github_file} に保存しました")
    
    summary_file = github_raw_dir / f"github_summary_{repo_name}.json"
    write_json_file(result, summary_file)
    
    print(f"抽出結果の概要を {summary_file} に保存しました")
    
    return result, github_file


def format_item(item):
    """
    issueまたはPRデータをMarkdown形式に変換
    
    Args:
        item: issueまたはPRデータ
        
    Returns:
        Markdown形式のデータ
    """
    item_title = item["title"]
    item_url = item["html_url"]
    item_body = item.get("body", "").replace("\r\n", "\n") if item.get("body") else "内容なし"
    item_user = item["user"]
    item_created_at = item["created_at"]
    item_type = item.get("type", "issue")
    
    if item_user == "devin-ai-integration[bot]" and (item.get("co_author") or item.get("requester")):
        human_name = item.get("co_author") or item.get("requester")
        item_user = f"{human_name}+Devin"
    
    md = f"### [{item_title}]({item_url})\n\n"
    md += f"**作成者:** {item_user}  \n"
    md += f"**作成日:** {item_created_at}  \n"
    
    if item_type == "pr":
        if "additions" in item and "deletions" in item and "changed_files" in item:
            md += f"**変更:** +{item['additions']} -{item['deletions']} ({item['changed_files']}ファイル)  \n"
        if "merged_at" in item and item["merged_at"]:
            md += f"**マージ日:** {item['merged_at']}  \n"
    
    md += f"**内容:**\n\n{item_body}\n\n"
    
    if "comments" in item and item["comments"]:
        md += "**コメント:**\n\n"
        for comment in item["comments"]:
            comment_user = comment["user"]
            comment_date = comment["created_at"]
            comment_body = comment["body"].replace("\r\n", "\n") if comment.get("body") else ""
            md += f"- **{comment_user}** ({comment_date}):\n\n{comment_body}\n\n"
    else:
        md += "**コメント:** なし\n\n"
    
    md += "---\n\n"
    return md


def generate_markdown(
    items: List[Dict[str, Any]], 
    repo: str, 
    start_date: str, 
    end_date: str, 
    output_file: Optional[Union[str, Path]] = None
) -> Optional[str]:
    """
    データからMarkdownレポートを生成
    
    Args:
        items: GitHubデータのリスト
        repo: リポジトリ名
        start_date: 開始日（ISO形式）
        end_date: 終了日（ISO形式）
        output_file: 出力ファイル名（指定しない場合はリポジトリ名から自動生成）
        
    Returns:
        生成されたMarkdown
    """
    if not items:
        print("データが見つかりませんでした")
        return None
    
    markdown_report = f"# GitHub レポート: {repo}\n\n"
    markdown_report += f"期間: {start_date} から {end_date} まで\n\n"
    
    issues = [item for item in items if item.get("type") == "issue"]
    prs = [item for item in items if item.get("type") == "pr"]
    
    start_date_str = start_date.split('T')[0] if 'T' in start_date else start_date
    end_date_str = end_date.split('T')[0] if 'T' in end_date else end_date
    days_diff = (datetime.date.fromisoformat(end_date_str) - datetime.date.fromisoformat(start_date_str)).days
    
    if issues:
        markdown_report += f"## Issues\n\n"
        
        closed_issues = [issue for issue in issues if issue.get("state") == "closed"]
        created_issues = [issue for issue in issues if issue.get("state") == "created"]
        updated_issues = [issue for issue in issues if issue.get("state") == "updated"]
        
        markdown_report += f"### 過去{days_diff}日間に完了されたissue ({len(closed_issues)}件)\n\n"
        for issue in closed_issues:
            markdown_report += format_item(issue)
        
        markdown_report += f"### 過去{days_diff}日間に作成されたissue ({len(created_issues)}件)\n\n"
        for issue in created_issues:
            markdown_report += format_item(issue)
        
        markdown_report += f"### 過去{days_diff}日間に更新されたissue（作成・クローズを除く）({len(updated_issues)}件)\n\n"
        for issue in updated_issues:
            markdown_report += format_item(issue)
    
    if prs:
        markdown_report += f"## Pull Requests\n\n"
        
        merged_prs = [pr for pr in prs if pr.get("state") == "merged"]
        created_prs = [pr for pr in prs if pr.get("state") == "created"]
        updated_prs = [pr for pr in prs if pr.get("state") == "updated"]
        
        markdown_report += f"### 過去{days_diff}日間にマージされたPR ({len(merged_prs)}件)\n\n"
        for pr in merged_prs:
            markdown_report += format_item(pr)
        
        markdown_report += f"### 過去{days_diff}日間に作成されたPR ({len(created_prs)}件)\n\n"
        for pr in created_prs:
            markdown_report += format_item(pr)
        
        markdown_report += f"### 過去{days_diff}日間に更新されたPR（作成・マージを除く）({len(updated_prs)}件)\n\n"
        for pr in updated_prs:
            markdown_report += format_item(pr)
    
    if not output_file:
        repo_name = repo.split("/")[1]
        date_range_dir = f"{start_date}_to_{end_date}"
        
        current_dir = Path(__file__).parent.absolute()
        base_dir = current_dir.parent.parent  # リポジトリのルートディレクトリ
        data_dir = base_dir / "data"
        
        markdown_dir = data_dir / date_range_dir / "markdown" / "github"
        ensure_dir(markdown_dir)
        output_file = markdown_dir / f"github_report-{repo_name}.md"
    else:
        ensure_dir(Path(output_file).parent)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_report)
    
    print(f"レポートは {output_file} に保存されました。")
    return markdown_report


def generate_markdown_from_file(
    json_file: Union[str, Path], 
    output_file: Optional[Union[str, Path]] = None,
    timezone_str: str = "UTC"
) -> Optional[str]:
    """
    JSONファイルからMarkdownレポートを生成
    
    Args:
        json_file: JSONファイルのパス
        output_file: 出力ファイル名（指定しない場合はリポジトリ名から自動生成）
        timezone_str: タイムゾーン名
        
    Returns:
        生成されたMarkdown
    """
    items = read_json_file(json_file)
    
    if not items:
        print(f"{json_file} にデータが見つかりませんでした")
        return None
    
    if items and "html_url" in items[0]:
        repo_url = items[0]["html_url"]
        repo = "/".join(repo_url.split("/")[3:5])
    else:
        repo = "unknown-repo"
    
    start_date, end_date = get_date_range(last_days=7, timezone_str=timezone_str)
    
    if not output_file:
        repo_name = repo.split("/")[1] if "/" in repo else repo
        json_file_path = Path(json_file)
        
        try:
            date_range_dir = json_file_path.parent.parent.parent.name
            if not '_to_' in date_range_dir:
                date_range_dir = get_date_range_dir(start_date, end_date)
                
            base_path = json_file_path.parent
            while base_path.name != date_range_dir and str(base_path) != '/':
                base_path = base_path.parent
            
            if str(base_path) == '/':
                base_path = json_file_path.parent.parent.parent
            else:
                base_path = base_path.parent
                
            markdown_dir = base_path / date_range_dir / "markdown" / "github"
            ensure_dir(markdown_dir)
            output_file = markdown_dir / f"github_report-{repo_name}.md"
        except (IndexError, ValueError):
            date_range_dir = get_date_range_dir(start_date, end_date)
            markdown_dir = Path(json_file).parent.parent / "markdown" / "github"
            ensure_dir(markdown_dir)
            output_file = markdown_dir / f"github_report-{repo_name}.md"
    
    return generate_markdown(
        items=items,
        repo=repo,
        start_date=start_date.date().isoformat(),
        end_date=end_date.date().isoformat(),
        output_file=output_file
    )


def main() -> int:
    """
    メイン関数
    
    Returns:
        int: 終了コード（0: 成功, 1: 失敗）
    """
    config = Config()
    
    parser = argparse.ArgumentParser(description='GitHubのissueとPRデータを抽出してレポートを生成するツール')
    
    repo_group = parser.add_argument_group('リポジトリ指定')
    repo_group.add_argument('--repo', help='リポジトリ名（owner/repo形式、またはカンマ区切りで複数指定可能）', required=True)
    repo_group.add_argument('--org', help='組織名（--repo で指定したリポジトリ名の前に付与される）')
    
    parser.add_argument('--output-dir', help='出力ディレクトリ', default=config.get("output.default_dir", "./data"))
    parser.add_argument('--last-days', type=int, help='過去何日分を取得するか', default=7)
    parser.add_argument('--no-prs', action='store_true', help='PRを含めない')
    parser.add_argument('--markdown', action='store_true', help='Markdownレポートも生成する')
    parser.add_argument('--output', help='Markdownレポートの出力ファイル名（指定しない場合はリポジトリ名から自動生成）')
    parser.add_argument('--json-file', help='既存のJSONファイルからMarkdownレポートを生成する場合に指定')
    parser.add_argument('--timezone', help='タイムゾーン', default=config.get("output.timezone", "UTC"))
    parser.add_argument('--config', help='設定ファイルのパス')
    
    args = parser.parse_args()
    
    if args.config:
        config = Config(config_file=args.config)
    
    timezone_str = args.timezone or config.get("output.timezone", "UTC")
    
    # 既存のJSONファイルからMarkdownレポートを生成
    if args.json_file:
        if not Path(args.json_file).exists():
            print(f"エラー: JSONファイルが見つかりません: {args.json_file}")
            return 1
        
        generate_markdown_from_file(
            json_file=args.json_file,
            output_file=args.output,
            timezone_str=timezone_str
        )
        return 0
    
    repos = []
    raw_repos = [repo.strip() for repo in args.repo.split(',')]
    
    for repo in raw_repos:
        if '/' in repo:
            repos.append(repo)  # すでに owner/repo 形式の場合はそのまま
        elif args.org:
            repos.append(f"{args.org}/{repo}")  # 組織名を付与
        else:
            print(f"エラー: リポジトリ '{repo}' に組織名が指定されていません。--org オプションを使用するか、owner/repo 形式で指定してください。")
            return 1
    
    print(f"処理対象リポジトリ: {repos}")
    
    output_dir = args.output_dir or config.get("output.default_dir", "./data")
    
    start_date, end_date = get_date_range(last_days=args.last_days, timezone_str=timezone_str)
    date_range_dir = get_date_range_dir(start_date, end_date)
    
    all_results = []
    all_items = []
    
    for repo in repos:
        result, json_file = extract_github_data(
            repo=repo,
            output_dir=output_dir,
            last_days=args.last_days,
            include_prs=not args.no_prs,
            timezone_str=timezone_str
        )
        
        if result:
            all_results.append(result)
            
            if args.markdown:
                repo_name = repo.split("/")[1]
                
                if not args.output:
                    markdown_dir = Path(output_dir) / date_range_dir / "markdown" / "github"
                    ensure_dir(markdown_dir)
                    output_file = markdown_dir / f"github_report-{repo_name}.md"
                else:
                    if len(repos) > 1:
                        output_path = Path(args.output)
                        base, ext = output_path.stem, output_path.suffix
                        output_file = output_path.with_name(f"{base}-{repo_name}{ext}")
                    else:
                        output_file = args.output
                
                # JSONファイルからデータを読み込み
                items = []
                if json_file and Path(json_file).exists():
                    items = read_json_file(json_file)
                    all_items.extend(items)
                
                generate_markdown(
                    items=items,
                    repo=repo,
                    start_date=result["period"]["start"],
                    end_date=result["period"]["end"],
                    output_file=output_file
                )
    
    if len(repos) > 1 and all_items and args.markdown:
        markdown_dir = Path(output_dir) / date_range_dir / "markdown" / "github"
        ensure_dir(markdown_dir)
        combined_output = markdown_dir / "github_report-combined.md"
        
        repo_names = [r.split("/")[1] for r in repos]
        combined_repo_name = ", ".join(repo_names)
        
        generate_markdown(
            items=all_items,
            repo=combined_repo_name,
            start_date=start_date.date().isoformat(),
            end_date=end_date.date().isoformat(),
            output_file=combined_output
        )
        
        print(f"まとめレポートは {combined_output} に保存されました。")
    
    return 0


if __name__ == "__main__":
    exit(main())
