import os
import json
import glob
from datetime import datetime, timedelta, timezone
import re

jst = timezone(timedelta(hours=9), name='JST')

start_date = datetime(2025, 4, 11, tzinfo=jst)
end_date = datetime(2025, 4, 18, 23, 59, 59, tzinfo=jst)

start_date_str = start_date.strftime('%Y年%m月%d日')
end_date_str = end_date.strftime('%Y年%m月%d日')

skip_channels = [
    "2_開発_いどばた_github",
    "2_開発_広聴ai_github"
]

content = f'# {start_date_str}～{end_date_str}のSlack活動まとめ\n\n'

with open('./data/2025-04-11_to_2025-04-18/raw/slack/summary.json', 'r') as f:
    summary = json.load(f)
    
    filtered_channels = [ch for ch in summary['channels'] if ch['name'] not in skip_channels]
    channels = len(filtered_channels)
    messages = sum(channel['message_count'] for channel in filtered_channels)
    
    content += f'今週は **{channels}個**のチャンネルで合計**{messages}件**のメッセージがやり取りされました。\n\n'
    content += '## チャンネル別アクティビティ\n\n'
    
    for channel in sorted(filtered_channels, key=lambda x: x['message_count'], reverse=True):
        content += f'- **#{channel["name"]}**: {channel["message_count"]}件のメッセージ\n'

content += '\n## チャンネル別詳細\n\n'

json_files = glob.glob('./data/2025-04-11_to_2025-04-18/raw/slack/*.json')
for json_file in sorted(json_files):
    channel_name = os.path.splitext(os.path.basename(json_file))[0]
    
    if channel_name in skip_channels or channel_name == 'summary':
        continue
    
    with open(json_file, 'r') as f:
        try:
            channel_data = json.load(f)
            
            if not channel_data:
                continue
                
            content += f'### #{channel_name}\n\n'
            
            sorted_messages = sorted(channel_data, key=lambda x: float(x.get('ts', '0')))
            
            for msg in sorted_messages:
                ts = float(msg.get('ts', '0'))
                dt = datetime.fromtimestamp(ts, jst)
                date_str = dt.strftime('%Y-%m-%d %H:%M:%S')
                
                user = msg.get('user_name', 'Unknown User')
                text = msg.get('text_readable', msg.get('text', ''))
                
                text = re.sub(r'<@([^>]+)>', r'@\1', text)
                
                content += f'**{date_str} {user}**:\n{text}\n\n'
                
                replies = msg.get('replies', [])
                if replies:
                    for reply in replies:
                        reply_ts = float(reply.get('ts', '0'))
                        reply_dt = datetime.fromtimestamp(reply_ts, jst)
                        reply_date_str = reply_dt.strftime('%Y-%m-%d %H:%M:%S')
                        
                        reply_user = reply.get('user_name', 'Unknown User')
                        reply_text = reply.get('text_readable', reply.get('text', ''))
                        
                        reply_text = re.sub(r'<@([^>]+)>', r'@\1', reply_text)
                        
                        content += f'> **{reply_date_str} {reply_user}**:\n> {reply_text}\n\n'
            
            content += '---\n\n'
        except json.JSONDecodeError:
            print(f"JSONデコードエラー: {json_file}")
            continue

os.makedirs('./data/2025-04-11_to_2025-04-18/markdown/slack/', exist_ok=True)

with open('./data/2025-04-11_to_2025-04-18/markdown/slack/all_summary.md', 'w') as f:
    f.write(content)

print("4/11~4/18のSlackまとめMarkdownを正しい日付範囲で生成し、チャンネル別詳細を追加しました")
