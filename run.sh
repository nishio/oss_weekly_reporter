# Slackデータの抽出と週次レポート生成
python -m src.slack_logger.slack_report --token "${SLACK_TOKEN}" --last-days 7 --weekly

# GitHubデータの抽出とレポート生成
# 広聴AI
python -m src.github_logger.github_report --repo "digitaldemocracy2030/kouchou-ai" --markdown --last-days 7

# いどばた系
python -m src.github_logger.github_report --repo "digitaldemocracy2030/idobata-analyst" --markdown --last-days 7
python -m src.github_logger.github_report --repo "digitaldemocracy2030/idobata-discourse-agent" --markdown --last-days 7
python -m src.github_logger.github_report --repo "digitaldemocracy2030/idobata-sns-agent" --markdown --last-days 7
python -m src.github_logger.github_report --repo "digitaldemocracy2030/idobata-infra" --markdown --last-days 7
python -m src.github_logger.github_report --repo "digitaldemocracy2030/2025_ai_idobatakaigi_output" --markdown --last-days 7
python -m src.github_logger.github_report --repo "digitaldemocracy2030/idobata-policy-editor" --markdown --last-days 7

# website
python -m src.github_logger.github_report --repo "digitaldemocracy2030/website" --markdown --last-days 7

# polimoney
python -m src.github_logger.github_report --repo "digitaldemocracy2030/polimoney" --markdown --last-days 7

# OpenAI APIを使用したレポート要約
# Slackレポートの要約
python -m src.call_openai_api slack --all-summary

# GitHubレポートの要約
python -m src.call_openai_api github --repo "digitaldemocracy2030/kouchou-ai"
python -m src.call_openai_api github --repo "digitaldemocracy2030/idobata-analyst"
python -m src.call_openai_api github --repo "digitaldemocracy2030/idobata-discourse-agent"
python -m src.call_openai_api github --repo "digitaldemocracy2030/idobata-sns-agent"
python -m src.call_openai_api github --repo "digitaldemocracy2030/idobata-infra"
python -m src.call_openai_api github --repo "digitaldemocracy2030/2025_ai_idobatakaigi_output"
python -m src.call_openai_api github --repo "digitaldemocracy2030/idobata-policy-editor"
python -m src.call_openai_api github --repo "digitaldemocracy2030/website"
python -m src.call_openai_api github --repo "digitaldemocracy2030/polimoney"