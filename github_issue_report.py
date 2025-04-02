import requests
import datetime
import os
import subprocess

def get_github_token():
    try:
        result = subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"GitHub CLIからトークンを取得できませんでした: {e}")
        return None

GITHUB_TOKEN = get_github_token()

REPO = 'digitaldemocracy2030/kouchou-ai'

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

today = datetime.date.today()
one_week_ago = today - datetime.timedelta(days=7)
one_week_ago_str = one_week_ago.isoformat()

query_closed = f'repo:{REPO} is:issue closed:>={one_week_ago_str}'
url_search = 'https://api.github.com/search/issues'
params_closed = {'q': query_closed}
response_closed = requests.get(url_search, headers=headers, params=params_closed)
closed_issues = response_closed.json()

print("【過去1週間に完了されたissue】")
for issue in closed_issues.get('items', []):
    print(f"- {issue['title']} ({issue['html_url']})")

query_created = f'repo:{REPO} is:issue created:>={one_week_ago_str}'
params_created = {'q': query_created}
response_created = requests.get(url_search, headers=headers, params=params_created)
created_issues = response_created.json()

print("\n【過去1週間に作成されたissue】")
for issue in created_issues.get('items', []):
    print(f"- {issue['title']} ({issue['html_url']})")

query_updated = f'repo:{REPO} is:issue updated:>={one_week_ago_str} -created:>={one_week_ago_str} -closed:>={one_week_ago_str}'
params_updated = {'q': query_updated}
response_updated = requests.get(url_search, headers=headers, params=params_updated)
updated_issues = response_updated.json()

print("\n【過去1週間に更新されたissue（作成・クローズを除く）】")
for issue in updated_issues.get('items', []):
    print(f"- {issue['title']} ({issue['html_url']})")

if closed_issues.get('items'):
    issue_number = closed_issues['items'][0]['number']
    url_comments = f'https://api.github.com/repos/{REPO}/issues/{issue_number}/comments'
    response_comments = requests.get(url_comments, headers=headers)
    comments = response_comments.json()

    print(f"\n【Issue #{issue_number} のコメント】")
    for comment in comments:
        print(f"- {comment['user']['login']} at {comment['created_at']}: {comment['body'][:80]}...")
