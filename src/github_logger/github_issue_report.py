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


def extract_github_data(repo, output_dir="./data", last_days=7, include_prs=True):
    """
    GitHubからissueとPRデータを抽出してJSONファイルに保存
    
    Args:
        repo: リポジトリ名（owner/repo形式）
        output_dir: 出力ディレクトリ
        last_days: 過去何日分を取得するか
        include_prs: PRも含めるかどうか
    
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
    github_file = os.path.join(date_range_path, f"{repo_name}.json")
    with open(github_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    
    print(f"{len(all_issues)}件のissueと{len(all_prs)}件のPRを {github_file} に保存しました")
    
    summary_file = os.path.join(date_range_path, f"github_summary_{repo_name}.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"抽出結果の概要を {summary_file} に保存しました")
    
    return result


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(description='GitHubのissueとPRデータを抽出するツール')
    parser.add_argument('--repo', help='リポジトリ名（owner/repo形式）', required=True)
    parser.add_argument('--output-dir', help='出力ディレクトリ', default='./data')
    parser.add_argument('--last-days', type=int, help='過去何日分を取得するか', default=7)
    parser.add_argument('--no-prs', action='store_true', help='PRを含めない')
    
    args = parser.parse_args()
    
    extract_github_data(
        repo=args.repo,
        output_dir=args.output_dir,
        last_days=args.last_days,
        include_prs=not args.no_prs
    )
    
    return 0


if __name__ == "__main__":
    exit(main())
