# Slackデータの抽出と週次レポート生成
SLACK_TOKEN=$(grep SLACK_TOKEN .env | cut -d'=' -f2)
python -m src.slack_logger.slack_report --token "${SLACK_TOKEN}" --last-days 7 --weekly

# GitHubデータの抽出とレポート生成
# 広聴AI
python -m src.github_logger.github_report --repo "digitaldemocracy2030/kouchou-ai" --markdown --last-days 7

python -m src.github_logger.github_report --repo "digitaldemocracy2030/idobata" --markdown --last-days 7

# website
python -m src.github_logger.github_report --repo "digitaldemocracy2030/website" --markdown --last-days 7

# polimoney
python -m src.github_logger.github_report --repo "digitaldemocracy2030/polimoney" --markdown --last-days 7

# OpenAI APIを使用したレポート要約
# Slackレポートの要約
python -m src.call_openai_api slack --all-summary

# GitHubレポートの要約
python -m src.call_openai_api github --repo "digitaldemocracy2030/kouchou-ai" --prompt-file "./prompts/kouchou_prompt.txt"
python -m src.call_openai_api github --repo "digitaldemocracy2030/idobata" --prompt-file "./prompts/idobata_prompt.txt"
python -m src.call_openai_api github --repo "digitaldemocracy2030/website" --prompt-file "./prompts/website_prompt.txt"
python -m src.call_openai_api github --repo "digitaldemocracy2030/polimoney" --prompt-file "./prompts/polimoney_prompt.txt"
