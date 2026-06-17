# GitHub レポート: digitaldemocracy2030/idobata

期間: 2026-06-10T13:37:20.372832+09:00 から 2026-06-17T13:37:20.372832+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (0件)

### 過去7日間に作成されたPR (1件)

### [トップページ表示と GitHub App 秘密鍵設定を改善](https://github.com/digitaldemocracy2030/idobata/pull/497)

**作成者:** 101ta28  
**作成日:** 2026-06-16T05:53:02Z  
**変更:** +229 -118 (12ファイル)  
**内容:**

## 概要

この PR は、ホスティングサービスに依存しない範囲で、トップページ表示、API 取得、GitHub App 秘密鍵の扱い、idea-discussion のデータ型を改善します。

特定のデプロイ先に合わせた設定は含めていないため、既存の開発環境や本番環境の選択肢を狭めずに取り込める内容です。

## 変更内容

- 最新の質問がない場合でも、最新テーマを使ってトップページを表示・遷移できるようにしました
- 質問カード・テーマカード・一覧で `href` を受け取れるようにし、リンク先指定を柔軟にしました
- frontend の共通 HTTP client で GET リクエストに `cache: "no-store"` を指定し、古いレスポンスが表示されるリスクを下げました
- GitHub App の秘密鍵を、環境変数・base64 環境変数・設定可能なファイルパスから読めるようにしました
- 起動時に GitHub 関連の環境変数を出力していた debug log を削除しました
- `idea-discussion` の `Problem` / `Solution` / `SharpQuestion` の schema と TypeScript 型を拡張しました

## 含めていないもの

- Vercel 固有の rewrite 設定
- Railway 固有の Dockerfile 調整
- デプロイ環境専用の entrypoint script
- production container で frontend 静的ファイルを配信するための変更

## レビュー観点

- `idea-discussion` の schema/type 変更は既存データや API 利用箇所に影響し得るため、フィールド名と required 指定が意図どおりか確認したいです
- GET 全体に `cache: "no-store"` を付ける方針が、パフォーマンスより最新性を優先する判断として妥当か確認したいです
- GitHub App 秘密鍵の読み込み順序が運用上扱いやすいか確認したいです

## 検証

以下を実行し、すべて成功しています。

- `npm run typecheck --workspace=idobata-frontend`
- `npm run typecheck --workspace=idobata-idea-discussion-backend`
- `npm run typecheck --workspace=idobata-policy-editor-backend`
- `npm run typecheck --workspace=github-contribution-mcp`
- `npm run test --workspace=idobata-frontend`
- `npm run test --workspace=idobata-idea-discussion-backend`
- `npm run test --workspace=idobata-policy-editor-backend`
- `npm run test --workspace=github-contribution-mcp`
- `npm run lint --workspace=idobata-frontend`
- `npm run lint --workspace=idobata-idea-discussion-backend`
- `npm run lint --workspace=idobata-policy-editor-backend`
- `npm run lint --workspace=github-contribution-mcp`

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

