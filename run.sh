python -m src.slack_logger.slack_report --token "${SLACK_TOKEN}" --last-days 30 --weekly --all


python -m src.github_logger.github_report --repo "digitaldemocracy2030/kouchou-ai" --markdown --last-days 30
python -m src.github_logger.github_report --repo "digitaldemocracy2030/idobata-analyst" --markdown --last-days 30
python -m src.github_logger.github_report --repo "digitaldemocracy2030/idobata-discourse-agent" --markdown --last-days 30
python -m src.github_logger.github_report --repo "digitaldemocracy2030/idobata-sns-agent" --markdown --last-days 30
python -m src.github_logger.github_report --repo "digitaldemocracy2030/idobata-infra" --markdown --last-days 30
python -m src.github_logger.github_report --repo "digitaldemocracy2030/website" --markdown --last-days 30

python -m src.call_openai_api slack --all-summary
python -m src.call_openai_api github --repo "digitaldemocracy2030/kouchou-ai"
