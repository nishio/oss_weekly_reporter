import requests
import datetime
import os
import subprocess
import json
import argparse
from pathlib import Path


def get_github_token():
    try:
        result = subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"GitHub CLIからトークンを取得できませんでした: {e}")
        return None


def extract_issues(repo, output_dir="./data", last_days=7):
    """
    GitHubからissueデータを抽出してJSONファイルに保存
    
    Args:
        repo: リポジトリ名（owner/repo形式）
        output_dir: 出力ディレクトリ
        last_days: 過去何日分を取得するか
    
    Returns:
        抽出結果の概要
    """
    GITHUB_TOKEN = get_github_token()
    
    if not GITHUB_TOKEN:
        print("GitHub CLIからトークンを取得できませんでした。")
        return None
    
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    
    today = datetime.date.today()
    one_week_ago = today - datetime.timedelta(days=last_days)
    one_week_ago_str = one_week_ago.isoformat()
    
    os.makedirs(output_dir, exist_ok=True)
    
    start_date_str = one_week_ago.strftime("%Y-%m-%d")
    end_date_str = today.strftime("%Y-%m-%d")
    date_range_dir = f"{start_date_str}_to_{end_date_str}"
    
    date_range_path = os.path.join(output_dir, date_range_dir)
    os.makedirs(date_range_path, exist_ok=True)
    
    print(f"データを {date_range_path} に保存します")
    
    result = {
        "period": {
            "start": one_week_ago.isoformat(),
            "end": today.isoformat()
        },
        "repo": repo,
        "issues": []
    }
    
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
    
    all_issues = []
    
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
            "body": issue.get("body", "")
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
            "body": issue.get("body", "")
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
            "body": issue.get("body", "")
        }
        all_issues.append(issue_data)
        result["issues"].append({
            "id": issue["id"],
            "number": issue["number"],
            "title": issue["title"],
            "state": "updated"
        })
    
    repo_name = repo.split("/")[1]
    issues_file = os.path.join(date_range_path, f"{repo_name}.json")
    with open(issues_file, 'w', encoding='utf-8') as f:
        json.dump(all_issues, f, ensure_ascii=False, indent=2)
    
    print(f"{len(all_issues)}件のissueを {issues_file} に保存しました")
    
    summary_file = os.path.join(date_range_path, f"github_summary_{repo_name}.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"抽出結果の概要を {summary_file} に保存しました")
    
    return result


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(description='GitHubのissueデータを抽出するツール')
    parser.add_argument('--repo', help='リポジトリ名（owner/repo形式）', required=True)
    parser.add_argument('--output-dir', help='出力ディレクトリ', default='./data')
    parser.add_argument('--last-days', type=int, help='過去何日分を取得するか', default=7)
    
    args = parser.parse_args()
    
    extract_issues(
        repo=args.repo,
        output_dir=args.output_dir,
        last_days=args.last_days
    )
    
    return 0


if __name__ == "__main__":
    exit(main())
