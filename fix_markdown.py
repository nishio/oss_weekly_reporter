import os
from datetime import datetime, timedelta, timezone
import json

jst = timezone(timedelta(hours=9), name='JST')

start_date = datetime(2025, 4, 11, tzinfo=jst)
end_date = datetime(2025, 4, 18, 23, 59, 59, tzinfo=jst)

start_date_str = start_date.strftime('%Y年%m月%d日')
end_date_str = end_date.strftime('%Y年%m月%d日')

content = f'# {start_date_str}～{end_date_str}のSlack活動まとめ\n\n'

with open('./data/2025-04-11_to_2025-04-18/raw/slack/summary.json', 'r') as f:
    summary = json.load(f)
    channels = len(summary['channels'])
    messages = sum(channel['message_count'] for channel in summary['channels'])
    
    content += f'今週は **{channels}個**のチャンネルで合計**{messages}件**のメッセージがやり取りされました。\n\n'
    content += '## チャンネル別アクティビティ\n\n'
    
    for channel in sorted(summary['channels'], key=lambda x: x['message_count'], reverse=True):
        content += f'- **#{channel["name"]}**: {channel["message_count"]}件のメッセージ\n'

os.makedirs('./data/2025-04-11_to_2025-04-18/markdown/slack/', exist_ok=True)

with open('./data/2025-04-11_to_2025-04-18/markdown/slack/all_summary.md', 'w') as f:
    f.write(content)

print("4/11~4/18のSlackまとめMarkdownを正しい日付範囲で生成しました")
