import requests
import datetime
import os
import subprocess
import time

def get_github_token():
    try:
        result = subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"GitHub CLIからトークンを取得できませんでした: {e}")
        return None

def get_issue_comments(repo, issue_number):
    url_comments = f'https://api.github.com/repos/{repo}/issues/{issue_number}/comments'
    response_comments = requests.get(url_comments, headers=headers)
    return response_comments.json()

def format_issue_with_comments(issue, comments):
    issue_title = issue['title']
    issue_url = issue['html_url']
    issue_number = issue['number']
    issue_body = issue.get('body', '').replace('\r\n', '\n') if issue.get('body') else '内容なし'
    issue_user = issue['user']['login']
    issue_created_at = issue['created_at']
    
    md = f"### [{issue_title}]({issue_url})\n\n"
    md += f"**作成者:** {issue_user}  \n"
    md += f"**作成日:** {issue_created_at}  \n"
    md += f"**内容:**\n\n{issue_body}\n\n"
    
    if comments:
        md += "**コメント:**\n\n"
        for comment in comments:
            comment_user = comment['user']['login']
            comment_date = comment['created_at']
            comment_body = comment['body'].replace('\r\n', '\n') if comment.get('body') else ''
            md += f"- **{comment_user}** ({comment_date}):\n\n{comment_body}\n\n"
    else:
        md += "**コメント:** なし\n\n"
    
    md += "---\n\n"
    return md

GITHUB_TOKEN = get_github_token()
REPO = 'digitaldemocracy2030/kouchou-ai'

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

today = datetime.date.today()
one_week_ago = today - datetime.timedelta(days=7)
one_week_ago_str = one_week_ago.isoformat()

markdown_report = f"# GitHub Issue レポート: {REPO}\n\n"
markdown_report += f"期間: {one_week_ago_str} から {today.isoformat()} まで\n\n"

query_closed = f'repo:{REPO} is:issue closed:>={one_week_ago_str}'
url_search = 'https://api.github.com/search/issues'
params_closed = {'q': query_closed}
response_closed = requests.get(url_search, headers=headers, params=params_closed)
closed_issues = response_closed.json()

markdown_report += f"## 過去1週間に完了されたissue ({len(closed_issues.get('items', []))}件)\n\n"
for issue in closed_issues.get('items', []):
    comments = get_issue_comments(REPO, issue['number'])
    markdown_report += format_issue_with_comments(issue, comments)
    time.sleep(0.5)

query_created = f'repo:{REPO} is:issue created:>={one_week_ago_str}'
params_created = {'q': query_created}
response_created = requests.get(url_search, headers=headers, params=params_created)
created_issues = response_created.json()

markdown_report += f"## 過去1週間に作成されたissue ({len(created_issues.get('items', []))}件)\n\n"
for issue in created_issues.get('items', []):
    comments = get_issue_comments(REPO, issue['number'])
    markdown_report += format_issue_with_comments(issue, comments)
    time.sleep(0.5)

query_updated = f'repo:{REPO} is:issue updated:>={one_week_ago_str} -created:>={one_week_ago_str} -closed:>={one_week_ago_str}'
params_updated = {'q': query_updated}
response_updated = requests.get(url_search, headers=headers, params=params_updated)
updated_issues = response_updated.json()

markdown_report += f"## 過去1週間に更新されたissue（作成・クローズを除く）({len(updated_issues.get('items', []))}件)\n\n"
for issue in updated_issues.get('items', []):
    comments = get_issue_comments(REPO, issue['number'])
    markdown_report += format_issue_with_comments(issue, comments)
    time.sleep(0.5)

print(markdown_report)

with open('github_issue_report.md', 'w', encoding='utf-8') as f:
    f.write(markdown_report)
print("\nレポートは github_issue_report.md に保存されました。")
