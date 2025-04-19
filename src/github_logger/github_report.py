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
    
    today = datetime.date.today()
    one_week_ago = today - datetime.timedelta(days=last_days)
    one_week_ago_str = one_week_ago.isoformat()
    
    os.makedirs(output_dir, exist_ok=True)
    
    start_date_str = one_week_ago.strftime("%Y-%m-%d")
    end_date_str = today.strftime("%Y-%m-%d")
    date_range_dir = f"{start_date_str}_to_{end_date_str}"
    
    date_range_path = os.path.join(output_dir, date_range_dir)
    os.makedirs(date_range_path, exist_ok=True)
    
    github_raw_dir = os.path.join(date_range_path, "raw", "github")
    os.makedirs(github_raw_dir, exist_ok=True)
    
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
    github_file = os.path.join(github_raw_dir, f"{repo_name}.json")
    with open(github_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    
    print(f"{len(all_issues)}件のissueと{len(all_prs)}件のPRを {github_file} に保存しました")
    
    summary_file = os.path.join(github_raw_dir, f"github_summary_{repo_name}.json")
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
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


def generate_markdown(items, repo, start_date, end_date, output_file=None):
    """
    データからMarkdownレポートを生成
    
    Args:
        items: GitHubデータのリスト
        repo: リポジトリ名
        start_date: 開始日
        end_date: 終了日
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
    
    if issues:
        markdown_report += f"## Issues\n\n"
        
        closed_issues = [issue for issue in issues if issue.get("state") == "closed"]
        created_issues = [issue for issue in issues if issue.get("state") == "created"]
        updated_issues = [issue for issue in issues if issue.get("state") == "updated"]
        
        markdown_report += f"### 過去{(datetime.date.fromisoformat(end_date) - datetime.date.fromisoformat(start_date)).days}日間に完了されたissue ({len(closed_issues)}件)\n\n"
        for issue in closed_issues:
            markdown_report += format_item(issue)
        
        markdown_report += f"### 過去{(datetime.date.fromisoformat(end_date) - datetime.date.fromisoformat(start_date)).days}日間に作成されたissue ({len(created_issues)}件)\n\n"
        for issue in created_issues:
            markdown_report += format_item(issue)
        
        markdown_report += f"### 過去{(datetime.date.fromisoformat(end_date) - datetime.date.fromisoformat(start_date)).days}日間に更新されたissue（作成・クローズを除く）({len(updated_issues)}件)\n\n"
        for issue in updated_issues:
            markdown_report += format_item(issue)
    
    if prs:
        markdown_report += f"## Pull Requests\n\n"
        
        merged_prs = [pr for pr in prs if pr.get("state") == "merged"]
        created_prs = [pr for pr in prs if pr.get("state") == "created"]
        updated_prs = [pr for pr in prs if pr.get("state") == "updated"]
        
        markdown_report += f"### 過去{(datetime.date.fromisoformat(end_date) - datetime.date.fromisoformat(start_date)).days}日間にマージされたPR ({len(merged_prs)}件)\n\n"
        for pr in merged_prs:
            markdown_report += format_item(pr)
        
        markdown_report += f"### 過去{(datetime.date.fromisoformat(end_date) - datetime.date.fromisoformat(start_date)).days}日間に作成されたPR ({len(created_prs)}件)\n\n"
        for pr in created_prs:
            markdown_report += format_item(pr)
        
        markdown_report += f"### 過去{(datetime.date.fromisoformat(end_date) - datetime.date.fromisoformat(start_date)).days}日間に更新されたPR（作成・マージを除く）({len(updated_prs)}件)\n\n"
        for pr in updated_prs:
            markdown_report += format_item(pr)
    
    if not output_file:
        repo_name = repo.split("/")[1]
        start_date_str = start_date.replace("-", "")
        end_date_str = end_date.replace("-", "")
        date_range_dir = f"{start_date}_to_{end_date}"
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(os.path.dirname(current_dir))  # リポジトリのルートディレクトリ
        data_dir = os.path.join(base_dir, "data")
        markdown_dir = os.path.join(data_dir, date_range_dir, "markdown", "github")
        os.makedirs(markdown_dir, exist_ok=True)
        output_file = os.path.join(markdown_dir, f"github_report-{repo_name}.md")
    else:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_report)
    
    print(f"レポートは {output_file} に保存されました。")
    return markdown_report


def generate_markdown_from_file(json_file, output_file=None):
    """
    JSONファイルからMarkdownレポートを生成
    
    Args:
        json_file: JSONファイルのパス
        output_file: 出力ファイル名（指定しない場合はリポジトリ名から自動生成）
        
    Returns:
        生成されたMarkdown
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        items = json.load(f)
    
    if not items:
        print(f"{json_file} にデータが見つかりませんでした")
        return None
    
    if items and "html_url" in items[0]:
        repo_url = items[0]["html_url"]
        repo = "/".join(repo_url.split("/")[3:5])
    else:
        repo = "unknown-repo"
    
    today = datetime.date.today()
    one_week_ago = today - datetime.timedelta(days=7)
    
    if not output_file:
        repo_name = repo.split("/")[1] if "/" in repo else repo
        date_range_dir = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(json_file))))
        if not '_to_' in date_range_dir:
            date_range_dir = f"{one_week_ago.strftime('%Y-%m-%d')}_to_{today.strftime('%Y-%m-%d')}"
        
        output_dir = os.path.dirname(json_file)
        output_dir_base = os.path.dirname(json_file).split(os.sep)
        base_path = os.sep.join(output_dir_base[:output_dir_base.index(date_range_dir)])
        markdown_dir = os.path.join(base_path, date_range_dir, "markdown", "github")
        os.makedirs(markdown_dir, exist_ok=True)
        output_file = os.path.join(markdown_dir, f"github_report-{repo_name}.md")
    
    return generate_markdown(
        items=items,
        repo=repo,
        start_date=one_week_ago.isoformat(),
        end_date=today.isoformat(),
        output_file=output_file
    )


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(description='GitHubのissueとPRデータを抽出してレポートを生成するツール')
    parser.add_argument('--repo', help='リポジトリ名（owner/repo形式）', required=True)
    parser.add_argument('--output-dir', help='出力ディレクトリ', default='./data')
    parser.add_argument('--last-days', type=int, help='過去何日分を取得するか', default=7)
    parser.add_argument('--no-prs', action='store_true', help='PRを含めない')
    parser.add_argument('--markdown', action='store_true', help='Markdownレポートも生成する')
    parser.add_argument('--output', help='Markdownレポートの出力ファイル名（指定しない場合はリポジトリ名から自動生成）')
    parser.add_argument('--json-file', help='既存のJSONファイルからMarkdownレポートを生成する場合に指定')
    
    args = parser.parse_args()
    
    if args.json_file:
        if not os.path.exists(args.json_file):
            print(f"エラー: JSONファイルが見つかりません: {args.json_file}")
            return 1
        
        generate_markdown_from_file(
            json_file=args.json_file,
            output_file=args.output
        )
    else:
        result, json_file = extract_github_data(
            repo=args.repo,
            output_dir=args.output_dir,
            last_days=args.last_days,
            include_prs=not args.no_prs
        )
        
        if result and args.markdown:
            repo_name = args.repo.split("/")[1]
            
            if not args.output:
                today = datetime.date.today()
                one_week_ago = today - datetime.timedelta(days=args.last_days)
                start_date_str = one_week_ago.strftime("%Y-%m-%d")
                end_date_str = today.strftime("%Y-%m-%d")
                date_range_dir = f"{start_date_str}_to_{end_date_str}"
                date_range_path = os.path.join(args.output_dir, date_range_dir)
                
                if json_file and os.path.exists(json_file):
                    output_dir = os.path.dirname(json_file)
                else:
                    output_dir = date_range_path
                    
                markdown_dir = os.path.join(args.output_dir, date_range_dir, "markdown", "github")
                os.makedirs(markdown_dir, exist_ok=True)
                args.output = os.path.join(markdown_dir, f"github_report-{repo_name}.md")
            
            items = []
            if json_file and os.path.exists(json_file):
                with open(json_file, 'r', encoding='utf-8') as f:
                    items = json.load(f)
            
            generate_markdown(
                items=items,
                repo=args.repo,
                start_date=result["period"]["start"],
                end_date=result["period"]["end"],
                output_file=args.output
            )
    
    return 0


if __name__ == "__main__":
    exit(main())
