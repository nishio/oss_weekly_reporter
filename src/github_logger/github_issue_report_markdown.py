import datetime
import os
import json
import argparse


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
    
    markdown_report = f"# GitHub レポート: {repo}\n\n"
    markdown_report += f"期間: {one_week_ago.isoformat()} から {today.isoformat()} まで\n\n"
    
    issues = [item for item in items if item.get("type") == "issue"]
    prs = [item for item in items if item.get("type") == "pr"]
    
    if issues:
        markdown_report += f"## Issues\n\n"
        
        closed_issues = [issue for issue in issues if issue.get("state") == "closed"]
        created_issues = [issue for issue in issues if issue.get("state") == "created"]
        updated_issues = [issue for issue in issues if issue.get("state") == "updated"]
        
        markdown_report += f"### 過去1週間に完了されたissue ({len(closed_issues)}件)\n\n"
        for issue in closed_issues:
            markdown_report += format_item(issue)
        
        markdown_report += f"### 過去1週間に作成されたissue ({len(created_issues)}件)\n\n"
        for issue in created_issues:
            markdown_report += format_item(issue)
        
        markdown_report += f"### 過去1週間に更新されたissue（作成・クローズを除く）({len(updated_issues)}件)\n\n"
        for issue in updated_issues:
            markdown_report += format_item(issue)
    
    if prs:
        markdown_report += f"## Pull Requests\n\n"
        
        merged_prs = [pr for pr in prs if pr.get("state") == "merged"]
        created_prs = [pr for pr in prs if pr.get("state") == "created"]
        updated_prs = [pr for pr in prs if pr.get("state") == "updated"]
        
        markdown_report += f"### 過去1週間にマージされたPR ({len(merged_prs)}件)\n\n"
        for pr in merged_prs:
            markdown_report += format_item(pr)
        
        markdown_report += f"### 過去1週間に作成されたPR ({len(created_prs)}件)\n\n"
        for pr in created_prs:
            markdown_report += format_item(pr)
        
        markdown_report += f"### 過去1週間に更新されたPR（作成・マージを除く）({len(updated_prs)}件)\n\n"
        for pr in updated_prs:
            markdown_report += format_item(pr)
    
    if not output_file:
        repo_name = repo.split("/")[1]
        output_file = f"github_report-{repo_name}.md"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(markdown_report)
    
    print(f"レポートは {output_file} に保存されました。")
    return markdown_report


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(description='GitHubのデータからMarkdownレポートを生成するツール')
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
