import datetime
import os
import json
import argparse


def format_issue(issue):
    """
    issueデータをMarkdown形式に変換
    
    Args:
        issue: issueデータ
        
    Returns:
        Markdown形式のissue
    """
    issue_title = issue["title"]
    issue_url = issue["html_url"]
    issue_body = issue.get("body", "").replace("\r\n", "\n") if issue.get("body") else "内容なし"
    issue_user = issue["user"]
    issue_created_at = issue["created_at"]
    
    md = f"### [{issue_title}]({issue_url})\n\n"
    md += f"**作成者:** {issue_user}  \n"
    md += f"**作成日:** {issue_created_at}  \n"
    md += f"**内容:**\n\n{issue_body}\n\n"
    
    if "comments" in issue and issue["comments"]:
        md += "**コメント:**\n\n"
        for comment in issue["comments"]:
            comment_user = comment["user"]
            comment_date = comment["created_at"]
            comment_body = comment["body"].replace("\r\n", "\n") if comment.get("body") else ""
            md += f"- **{comment_user}** ({comment_date}):\n\n{comment_body}\n\n"
    else:
        md += "**コメント:** なし\n\n"
    
    md += "---\n\n"
    return md


def generate_markdown(json_file, output_file=None):
    """
    JSONファイルからMarkdownレポートを生成
    
    Args:
        json_file: JSONファイルのパス
        output_file: 出力ファイル名（指定しない場合はリポジトリ名から自動生成）
        
    Returns:
        生成されたMarkdown
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        issues = json.load(f)
    
    if not issues:
        print(f"{json_file} にissueが見つかりませんでした")
        return None
    
    if issues and "html_url" in issues[0]:
        repo_url = issues[0]["html_url"]
        repo = "/".join(repo_url.split("/")[3:5])
    else:
        repo = "unknown-repo"
    
    today = datetime.date.today()
    one_week_ago = today - datetime.timedelta(days=7)
    
    markdown_report = f"# GitHub Issue レポート: {repo}\n\n"
    markdown_report += f"期間: {one_week_ago.isoformat()} から {today.isoformat()} まで\n\n"
    
    closed_issues = [issue for issue in issues if issue.get("state") == "closed"]
    created_issues = [issue for issue in issues if issue.get("state") == "created"]
    updated_issues = [issue for issue in issues if issue.get("state") == "updated"]
    
    markdown_report += f"## 過去1週間に完了されたissue ({len(closed_issues)}件)\n\n"
    for issue in closed_issues:
        markdown_report += format_issue(issue)
    
    markdown_report += f"## 過去1週間に作成されたissue ({len(created_issues)}件)\n\n"
    for issue in created_issues:
        markdown_report += format_issue(issue)
    
    markdown_report += f"## 過去1週間に更新されたissue（作成・クローズを除く）({len(updated_issues)}件)\n\n"
    for issue in updated_issues:
        markdown_report += format_issue(issue)
    
    if not output_file:
        repo_name = repo.split("/")[1]
        output_file = f"github_issue_report-{repo_name}.md"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_report)
    
    print(f"レポートは {output_file} に保存されました。")
    return markdown_report


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(description='GitHubのissueデータからMarkdownレポートを生成するツール')
    parser.add_argument('--json-file', help='JSONファイルのパス', required=True)
    parser.add_argument('--output', help='出力ファイル名（指定しない場合はリポジトリ名から自動生成）')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.json_file):
        print(f"エラー: JSONファイルが見つかりません: {args.json_file}")
        return 1
    
    generate_markdown(
        json_file=args.json_file,
        output_file=args.output
    )
    
    return 0


if __name__ == "__main__":
    exit(main())
