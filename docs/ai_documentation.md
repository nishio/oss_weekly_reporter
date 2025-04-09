# デジタル民主主義2030 Weekly Report 作成のためのAI向けドキュメント

このドキュメントは、デジタル民主主義2030プロジェクトのWeekly Reportを作成するためのAI向けガイドです。READMEに記載されていない追加情報や、AIがレポート生成を効率的に行うために必要な知識を提供します。

## プロジェクト概要

デジタル民主主義2030は、デジタル技術を活用して民主主義プロセスを強化・改善することを目指すプロジェクトです。このプロジェクトには複数のサブプロジェクトが含まれており、それぞれが異なる側面からデジタル民主主義の実現に貢献しています。

### 主要サブプロジェクト

1. **kouchou-ai**: 校長AIプロジェクト - 教育分野でのAI活用
2. **idobata-analyst**: データ分析コンポーネント
3. **idobata-discourse-agent**: 議論支援エージェント
4. **idobata-sns-agent**: SNS連携エージェント
5. **idobata-infra**: インフラストラクチャ管理
6. **website**: プロジェクト公式ウェブサイト

## データソース

Weekly Reportは主に2つのデータソースから情報を収集します：

### 1. Slack

Slackからは以下の情報を抽出します：
- チャンネルごとのメッセージ
- 投稿者情報
- 投稿日時
- スレッド情報
- リアクション情報

### 2. GitHub

GitHubからは以下の情報を抽出します：
- Issue（新規・更新・クローズ）
- Pull Request（新規・マージ・クローズ）
- コミット情報
- レビューコメント
- ディスカッション

## レポート生成プロセス

### 1. データ抽出

```bash
# Slackデータの抽出
python -m src.slack_logger.slack_to_json --output-dir "./data" --last-days 7

# GitHubデータの抽出（各リポジトリごとに実行）
python -m src.github_logger.github_report --repo "digitaldemocracy2030/kouchou-ai" --markdown --last-days 7
python -m src.github_logger.github_report --repo "digitaldemocracy2030/website" --markdown --last-days 7
python -m src.github_logger.github_report --repo "digitaldemocracy2030/idobata-analyst" --markdown --last-days 7
python -m src.github_logger.github_report --repo "digitaldemocracy2030/idobata-discourse-agent" --markdown --last-days 7
python -m src.github_logger.github_report --repo "digitaldemocracy2030/idobata-sns-agent" --markdown --last-days 7
python -m src.github_logger.github_report --repo "digitaldemocracy2030/idobata-infra" --markdown --last-days 7
```

### 2. データ変換

```bash
# SlackデータをMarkdownに変換
python -m src.slack_logger.json_to_markdown --json-dir "./data/[日付範囲]" --weekly --all --output "./data/[日付範囲]/all_summary.md"
```

### 3. AIレポート生成

```bash
# Slackデータに基づくAIレポート生成
python -m src.call_openai_api slack --all-summary

# GitHubデータに基づくAIレポート生成（各リポジトリごと）
python -m src.call_openai_api github --repo "digitaldemocracy2030/kouchou-ai"
python -m src.call_openai_api github --repo "digitaldemocracy2030/website"

# idobata系リポジトリは結合してからAIレポート生成
# （結合スクリプトは別途必要）
```

## ファイル構造

新しいフォルダ構造は以下の通りです：

```
data/
└── YYYY-MM-DD_to_YYYY-MM-DD/
    ├── raw/
    │   ├── slack/
    │   │   ├── [channel_name].json
    │   │   └── summary.json
    │   └── github/
    │       ├── [repo_name].json
    │       └── github_summary_[repo_name].json
    ├── markdown/
    │   ├── slack/
    │   │   ├── daily_summary_YYYY-MM-DD.md
    │   │   ├── weekly_summary.md
    │   │   └── all_summary.md
    │   └── github/
    │       └── github_report-[repo_name].md
    └── ai_reports/
        ├── slack_summary_YYYYMMDD_HHMMSS.md
        └── github_summary_[repo_name]_YYYYMMDD_HHMMSS.md
```

## レポート解釈のためのコンテキスト

### Slackデータの解釈

- **チャンネル活動**: チャンネルごとのメッセージ数は、そのトピックに関する活動レベルを示します
- **スレッド**: 深いディスカッションが行われている場所を示します
- **リアクション**: コミュニティの反応や合意を示します

### GitHubデータの解釈

- **Issue**: 新しい機能要求、バグ報告、タスク管理を示します
- **Pull Request**: 実際のコード変更と開発進捗を示します
- **レビューコメント**: コードの品質管理とチームコラボレーションを示します

## レポート作成のためのプロンプト

AIレポート生成時には、以下の点に注目してレポートを作成してください：

1. **進捗の要約**: 期間中の主要な進展や成果
2. **課題の特定**: 直面している問題や障害
3. **トレンドの分析**: 活動パターンや注目すべき変化
4. **重要なディスカッション**: 重要な決定や議論
5. **次のステップ**: 今後の予定や優先事項

## 特定のプロジェクトに関する追加コンテキスト

### kouchou-ai

校長AIは教育現場でのAI活用を目指すプロジェクトで、主に以下の機能開発に焦点を当てています：
- 学習コンテンツの自動生成
- 学習者の進捗管理
- パーソナライズされた学習体験の提供

### idobata系プロジェクト

idobataシリーズは相互に連携するコンポーネントで構成されており、全体として議論プラットフォームを形成しています：
- **analyst**: データ分析と可視化
- **discourse-agent**: 議論の促進と整理
- **sns-agent**: 外部SNSとの連携
- **infra**: システム全体のインフラ管理

### website

公式ウェブサイトはプロジェクトの対外的な窓口として機能し、以下の要素に焦点を当てています：
- プロジェクト概要の説明
- 成果物の公開
- コミュニティエンゲージメント

## レポート生成時の注意点

1. **機密情報の取り扱い**: APIキーやアクセストークンなどの機密情報は絶対にレポートに含めないでください
2. **バランスの取れた報告**: 技術的詳細と非技術者向けの説明のバランスを取ってください
3. **コンテキストの提供**: 単なる活動リストではなく、その意味や影響を説明してください
4. **一貫性**: 週ごとのレポート間で一貫した形式と用語を使用してください
5. **優先順位付け**: 最も重要な情報を強調し、詳細は補足情報として提供してください

## トラブルシューティング

レポート生成中に問題が発生した場合は、以下を確認してください：

1. **API認証**: Slack/GitHub APIトークンが正しく設定されているか
2. **データ範囲**: 正しい日付範囲が指定されているか
3. **ファイルパス**: 出力ディレクトリが存在し、書き込み権限があるか
4. **依存関係**: 必要なライブラリがすべてインストールされているか
5. **API制限**: API使用量制限に達していないか

---

このドキュメントは継続的に更新され、プロジェクトの進化に合わせて拡張されます。
