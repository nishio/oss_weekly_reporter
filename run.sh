# 4/4
# python -m slack_logger.slack_to_json --output-dir "./data" --last-days 30
# python -m slack_logger.json_to_markdown --json-dir "./data/2025-03-04_to_2025-04-03" --weekly --all --output "./data/2025-03-04_to_2025-04-03/all_summary.md"

# python -m github_logger.github_report --repo "digitaldemocracy2030/kouchou-ai" --markdown --last-days 30
# python -m github_logger.github_report --repo "digitaldemocracy2030/idobata-analyst" --markdown --last-days 30
# python -m github_logger.github_report --repo "digitaldemocracy2030/idobata-discourse-agent" --markdown --last-days 30
# python -m github_logger.github_report --repo "digitaldemocracy2030/idobata-sns-agent" --markdown --last-days 30
# python -m github_logger.github_report --repo "digitaldemocracy2030/idobata-infra" --markdown --last-days 30
# python -m github_logger.github_report --repo "digitaldemocracy2030/website" --markdown --last-days 30

python -m src.call_openai_api github --repo "digitaldemocracy2030/kouchou-ai"