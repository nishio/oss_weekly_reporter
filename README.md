# OSS Weekly Reporter

Open Source Software (OSS) Weekly Reporterは、OSSプロジェクトの週次報告を省力化するためのツールです。SlackのログとGitHubのログを抽出し、LLMに渡すためのMarkdown形式に変換します。

## 機能

- **slack_to_json.py**: Slackからデータを抽出してJSONファイルに保存
  - 日付範囲ごとにフォルダを作成し、チャンネルごとのJSONファイルを保存
  - 各ログフォルダにREADME.mdを自動生成（期間、チャンネル数、メッセージ数などの情報を含む）
- **json_to_gsheet.py**: JSONファイルからGoogle Spreadsheetにデータをアップロード
  - Google Driveの指定フォルダにスプレッドシートを作成
  - チャンネルごとにシートを分けて保存
- **json_to_markdown.py**: JSONデータをLLM用のMarkdown形式に変換
  - 日次または週次のサマリーを生成
  - LLMによる「今日はこんな議論が行われた」という解説作成に適したフォーマット
- **github_report.py**: GitHubからissueとPRのデータを抽出してレポート作成
  - 指定したリポジトリの最近のアクティビティ（issue、PR）を取得
  - JSON形式でデータを保存し、オプションでMarkdownレポートも生成
- **call_openai_api.py**: OpenAI O1 APIを使用してMarkdownを処理
  - SlackやGitHubから生成されたMarkdownレポートをLLMで分析
  - 重要なポイントや活動の要約を自動生成

## インストール

```bash
# リポジトリをクローン
git clone https://github.com/nishio/oss_weekly_reporter.git
cd oss_weekly_reporter

# 依存パッケージをインストール
pip install -e .
```

## 設定

### 環境変数

`.env`ファイルを作成して必要な環境変数を設定します（`.env.template`をコピーして使用）：

```
# Slack API関連
SLACK_TOKEN=xoxb-your-token-here

# Google API関連
GOOGLE_CLIENT_EMAIL=your-service-account@example.iam.gserviceaccount.com
GOOGLE_PRIVATE_KEY=your-private-key-here
GOOGLE_FOLDER_ID=your-folder-id-here
```

### 設定ファイル

`config.yaml`ファイルで追加設定を行います（`config.yaml.template`をコピーして使用）：

```yaml
# スキップするチャンネル
skip_channels:
  - general
  - random

# 公開チャンネルに自動参加するかどうか
auto_join: true

# 出力設定
output:
  default_dir: ./data
  timezone: Asia/Tokyo
```

## 使用方法

### 1. Slackからデータを抽出

```bash
python -m slack_logger.slack_to_json --token "xoxb-your-token" --output-dir "./data" --last-days 7
```

#### オプション

- `--token`: Slack APIトークン（必須、または`SLACK_TOKEN`環境変数で指定）
- `--output-dir`: 出力ディレクトリ（デフォルト: `./data`）
- `--year`: 抽出する年（指定しない場合は現在の2ヶ月前）
- `--month`: 抽出する月（指定しない場合は現在の2ヶ月前）
- `--last-days`: 過去何日分を取得するか（指定した場合はyear, monthは無視）
- `--auto-join`: 公開チャンネルに自動的に参加する（デフォルト: True）
- `--no-auto-join`: 公開チャンネルに自動的に参加しない
- `--skip-channels`: スキップするチャンネルIDのカンマ区切りリスト

### 2. Google Spreadsheetにアップロード

(この機能は未テストです)

```bash
python -m slack_logger.json_to_gsheet --json-dir "./data"
```

#### オプション

- `--client-email`: Google Service Accountのメールアドレス（必須、または`GOOGLE_CLIENT_EMAIL`環境変数で指定）
- `--private-key`: Google Service Accountの秘密鍵（必須、または`GOOGLE_PRIVATE_KEY`環境変数で指定）
- `--folder-id`: Google Driveのフォルダーid（必須、または`GOOGLE_FOLDER_ID`環境変数で指定）
- `--json-dir`: JSONファイルのディレクトリ（デフォルト: `./data`）
- `--timezone`: タイムゾーン（デフォルト: `Asia/Tokyo`）
- `--use-latest-file`: 'latest'という名前のファイルを使用する
- `--backup-with-date`: 日付付きのバックアップを作成する（`--use-latest-file`と共に使用）

#### Google Sheets APIのセットアップ

Google Sheetsへのアップロードを利用するには、以下のセットアップが必要です：

1. [Google Cloud Platform](https://console.cloud.google.com/)でプロジェクトを作成
2. プロジェクトで以下のAPIを有効化：
   - Google Drive API
   - Google Sheets API
3. Service Accountを作成：
   - Google Cloud Consoleで「IAM & 管理」→「サービスアカウント」→「サービスアカウントを作成」
   - 必要な権限を付与（Sheets編集権限、Drive ファイル作成権限）
   - JSONキーをダウンロード
4. ダウンロードしたJSONから必要な情報を`.env`ファイルに設定：
   ```
   GOOGLE_CLIENT_EMAIL=your-service-account@example.iam.gserviceaccount.com
   GOOGLE_PRIVATE_KEY=your-private-key-here
   ```
5. アップロード先のGoogle Driveフォルダを作成し、そのフォルダIDを取得：
   - フォルダのURLが `https://drive.google.com/drive/folders/1AbCdEfGhIjKlMnOpQrStUvWxYz` の場合、
   - フォルダIDは `1AbCdEfGhIjKlMnOpQrStUvWxYz`
   - このIDを`.env`ファイルの`GOOGLE_FOLDER_ID`に設定

### 3. LLM用のMarkdownに変換

```bash
python -m slack_logger.json_to_markdown --json-dir "./data" --weekly --output "./weekly_summary.md"
```

#### オプション

- `--json-dir`: JSONファイルのディレクトリ（デフォルト: `./data`）
- `--output`: 出力ファイル名（指定しない場合は標準出力）
- `--timezone`: タイムゾーン（デフォルト: `Asia/Tokyo`）
- `--daily`: 日次サマリーを生成
- `--weekly`: 週次サマリーを生成
- `--days-ago`: 何日前のデータを対象とするか（日次サマリー用、デフォルト: 0）
- `--weeks-ago`: 何週間前のデータを対象とするか（週次サマリー用、デフォルト: 0）

### 4. GitHubのデータを抽出してレポートを生成

```bash
python -m github_logger.github_report --repo "owner/repo" --markdown
```

#### オプション

- `--repo`: 対象リポジトリ（'owner/repo'形式、またはカンマ区切りで複数指定可能）
- `--org`: 組織名（`--repo`で指定したリポジトリ名の前に付与される）
- `--output-dir`: 出力ディレクトリ（デフォルト: `./data`）
- `--last-days`: 過去何日分を取得するか（デフォルト: 7）
- `--no-prs`: PRを含めない
- `--markdown`: Markdownレポートも生成する
- `--output`: Markdownレポートの出力ファイル名（指定しない場合はリポジトリ名から自動生成）
- `--json-file`: 既存のJSONファイルからMarkdownレポートを生成する場合に指定

#### 使用例

1. 単一リポジトリのデータ抽出とMarkdownレポート生成:
```bash
python -m github_logger.github_report --repo "owner/repo" --markdown
```

2. 複数リポジトリの同時処理:
```bash
python -m github_logger.github_report --repo "owner/repo1,owner/repo2,owner/repo3" --markdown
```

3. 組織名を指定して複数リポジトリを処理:
```bash
python -m github_logger.github_report --org "organization-name" --repo "repo1,repo2,repo3" --markdown
```

4. データ抽出のみ行う:
```bash
python -m github_logger.github_report --repo "owner/repo"
```

5. 既存のJSONファイルからMarkdownレポートを生成する:
```bash
python -m github_logger.github_report --json-file "./data/yyyy-MM-dd_to_yyyy-MM-dd/repo-name.json"
```

### 5. OpenAI O1 APIを使用してMarkdownを処理

```bash
# Slackデータの処理（最新のフォルダのweekly_summary.mdを使用）
python -m src.call_openai_api slack

# Slackデータの処理（all_summary.mdを使用）
python -m src.call_openai_api slack --all-summary

# 特定の期間を指定してSlackデータを処理
python -m src.call_openai_api slack --period "2025-03-01_to_2025-03-31"

# GitHubデータの処理
python -m src.call_openai_api github --repo "owner/repo"
```

#### オプション

- `--data-dir`: データディレクトリ（指定しない場合は最新のフォルダを使用）
- `--output-dir`: 出力ディレクトリ（指定しない場合はデータディレクトリと同じ）
- `slack`: Slackデータを処理するコマンド
  - `--all-summary`: weekly_summary.mdの代わりにall_summary.mdを使用
  - `--period`: 期間（YYYY-MM-DD_to_YYYY-MM-DD形式）
- `github`: GitHubデータを処理するコマンド
  - `--repo`: リポジトリ名（owner/repo形式、必須）

#### 環境変数

`.env`ファイルに以下の環境変数を追加する必要があります：

```
# OpenAI API関連
OPENAI_API_KEY=your-openai-api-key-here
```

## 自動化

このリポジトリには、GitHub Actionsを使用して週に2回（月曜日と木曜日）自動的にSlackログを抽出するワークフローが含まれています。抽出されたデータは`data`ブランチに保存されます。

### ワークフロー設定

`.github/workflows/extract-logs.yml`ファイルで設定されています：

- 実行スケジュール: 月曜日と木曜日の午前3時（UTC）
- 抽出期間: 過去7日間
- 出力先: `data`ブランチ

### 必要な設定

GitHub Secretsに以下の値を設定する必要があります：

- `SLACK_TOKEN`: SlackのAPIトークン

また、GitHub Actionsがデータブランチにプッシュするために、以下の権限設定が必要です：

1. リポジトリの「Settings」→「Actions」→「General」
2. 「Workflow permissions」で「Read and write permissions」を選択
3. 「Save」をクリック

この設定がない場合、GitHub Actionsがデータブランチにプッシュする際に権限エラーが発生します。

## 開発

### セットアップ

開発用にリポジトリをセットアップするには：

```bash
# リポジトリをクローン
git clone https://github.com/nishio/oss_weekly_reporter.git
cd oss_weekly_reporter

# 開発モードでインストール
pip install -e .

# テスト用の環境変数を設定
cp .env.template .env
# .envファイルを編集して適切な値を設定

# 設定ファイルを作成
cp config.yaml.template config.yaml
# 必要に応じてconfig.yamlを編集
```
