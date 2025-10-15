# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-10-08T12:23:30.907589+09:00 から 2025-10-15T12:23:30.907589+09:00 まで

## Issues

### 過去7日間に完了されたissue (3件)

### [[BUG] client でロゴなどの画像が表示されない](https://github.com/digitaldemocracy2030/kouchou-ai/issues/717)

**作成者:** shingo-ohki  
**作成日:** 2025-10-10T08:08:05Z  
**内容:**

### 概要

<!-- バグの簡潔な説明をお願いします -->
現状の main ブランチ https://github.com/digitaldemocracy2030/kouchou-ai/commit/5f343c8018a08fa05d1970e09c2b71b0d4afdf49 で client でロゴなどの画像が表示されない

### 再現手順

1. docker compuse up などで client を起動する
2. http://localhost:3000 にアクセスする

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->

### スクリーンショット・ログ
以下のように、左上のロゴなどが表示されない
<img width="1136" height="961" alt="Image" src="https://github.com/user-attachments/assets/00cb992e-7a3f-4cb3-93de-d46dafef4f0a" />

<img width="755" height="150" alt="Image" src="https://github.com/user-attachments/assets/8a68d93e-87b6-4ac8-9504-652e30262ae4" />

<img width="508" height="116" alt="Image" src="https://github.com/user-attachments/assets/a9b99856-46fa-4312-8518-73aa6b318021" />

ロゴなどの画像をAPI経由で取得しようとしている
http://localhost:8000/images/logo.svg 

### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->
関連してそうなPR https://github.com/digitaldemocracy2030/kouchou-ai/pull/709

**コメント:** なし

---

### [[BUG] Windows用のsetupスクリプトが文字化けする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/714)

**作成者:** AkioPonkotu  
**作成日:** 2025-10-07T08:37:56Z  
**内容:**

### 概要

Windows用のsetupスクリプトが文字化けする

### 再現手順



### 期待する動作


### スクリーンショット・ログ


### その他


**コメント:** なし

---

### [[FEATURE] Azure に動作確認環境・デモ環境を作る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/622)

**作成者:** shingo-ohki  
**作成日:** 2025-06-29T08:25:09Z  
**内容:**

# 背景
- 現状、新しい機能の開発やソフトウェア改善を行った場合の動作確認は、エンジニアの手元の開発環境で行っているが、UI/UX の改善を行う際などはデザイナーなどエンジニア以外の方にも確認してもらいたいがその環境がない
- ユーザーが広聴AIを試すには環境構築をする必要があるが、これは多少のエンジニアリングスキルを必要とするため、簡単に試すことができない

<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->


# 提案内容
上記を解決するために、dd2030 が管理する Azure 環境に常に広聴AIがデプロイされているような環境を用意する

<!-- 実装案やデザイン案があれば記入してください -->

- 動作確認環境
  - [x] Azure 環境にセットアップする
  - [x]  #642 
  - [x] #688 
- デモ環境
  - [x] #633
  - ~~client-admin のパスワードなしでアクセスできるようにする~~ （未対応）
  - ~~dd2030.org ドメインでアクセスできるようにする~~ （未対応）

**コメント:** なし

---

### 過去7日間に作成されたissue (1件)

### [[FEATURE] レポート作成時のエラーログを web application 上から確認できない](https://github.com/digitaldemocracy2030/kouchou-ai/issues/716)

**作成者:** shingo-ohki  
**作成日:** 2025-10-09T03:14:25Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

現状ではエラーログは docker コンテナのログを確認する必要があるため、レポート作成時に何らかのエラーが出てレポート作成が失敗した場合、docker に不慣れなユーザーには対応が難しく、また原因や対応について Slack コミュニティーで質問することも難しくなっている。

> 統合ラベリング中にこけた模様。
> 原因がわからないので知りたい…
> win11
> GPT-4o使用（クレジットは余裕で残ってる）
> 1570件（たぶん）
> もしかして：Tier1なのでそれが原因？

from `#2_開発_広聴ai` slack チャンネル

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
- ログをダウンロードできる
- ログをアプリケーション上で表示できる

などの何らかの形で、web application 上からエラーログを確認できるようにできるとよい

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (2件)

### [fix [BUG] client でロゴなどの画像が表示されない](https://github.com/digitaldemocracy2030/kouchou-ai/pull/718)

**作成者:** shingo-ohki  
**作成日:** 2025-10-10T11:04:26Z  
**変更:** +5 -27 (2ファイル)  
**マージ日:** 2025-10-11T01:08:24Z  
**内容:**

# 変更の概要
- client でロゴなどの画像が表示されない問題を解消します

# スクリーンショット
- 変更前
<img width="1136" height="961" alt="Screenshot from 2025-10-10 16-55-53" src="https://github.com/user-attachments/assets/b95119d3-e6a6-42d6-be59-18b73f7ec483" />

- 変更後
<img width="1420" height="911" alt="Screenshot from 2025-10-10 19-57-48" src="https://github.com/user-attachments/assets/58bfc6cc-644a-4658-972a-3264b7e9e53d" />


# 変更の背景
- #709 で静的ファイルエクスポート時に画像のパスが適切に調整されるようにする修正がなされた際に、通常の client 表示時の画像表示に影響が出ていた

# 関連Issue
#717 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->
- 通常の client 表示時の画像表示が適切なこと
- [静的ファイルエクスポート](https://shingo-ohki.github.io/kouchou-ai-reports/) 時の画像表示が適切なこと

をそれぞれ確認しました


# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- バグ修正
  - 画像の相対パス解決を簡素化し、ベースパス有無に応じた先頭スラッシュの扱いを調整。静的アセットの読み込みがより安定・一貫化。
- ドキュメント
  - 画像取得ロジックに関する説明を最新の挙動に合わせて更新。
- スタイル
  - 軽微なコード整形（末尾カンマの追加）。動作への影響はありません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[BUG] Windows用のsetupスクリプトが文字化けする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/715)

**作成者:** AkioPonkotu  
**作成日:** 2025-10-07T08:42:07Z  
**変更:** +36 -8 (1ファイル)  
**マージ日:** 2025-10-12T00:25:25Z  
**内容:**

# 変更の概要
- 文字化けしていたWindows用のsetupスクリプトの文字コードを設定
- GeminiのAPIキーを正しくチェックできるように

# 変更の背景
- Slackで報告いただいた

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/714

# 動作確認の結果
スクリプトを実行し、APIキーのチェックや環境構築が文字化けせずに実行されることを確認しました。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - コンソールをUTF-8に統一してUnicodeをサポート。
  - Docker Desktopの利用可否を事前にチェック。
  - OpenAI/GeminiのAPIキー入力を案内（貼り付け方法のヒントを含む）。
- **改善**
  - APIキーは設定されている場合のみ形式検証し、不備は集約してユーザーに報告。
  - エラー時はY/Nで続行可否を対話的に確認。
  - 検証後に環境生成とコンテナ起動を実行する制御フローに改良。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (1件)

### [E2Eテストの実装（管理画面とクライアント画面）](https://github.com/digitaldemocracy2030/kouchou-ai/pull/719)

**作成者:** nishio  
**作成日:** 2025-10-13T18:35:13Z  
**変更:** +137832 -91 (27ファイル)  
**内容:**

## 概要

広聴AIアプリケーションの管理画面（client-admin）とクライアント画面（client）に対するPlaywright E2Eテストを実装しました。

文脈: Playwrightが公式のMCPを出した。[世の中的にもAIを使ったTDDが一般的になってきている](https://x.com/hillbig/status/1977321505664237931)。以前Devinにやらせようとしたe2eテストが以前よりやりやすくなったはずなので再挑戦した。
結果: 管理画面およびユーザ向け画面のテストを生成することができた。テストの管理に関するドキュメントも生成され、今後のテスト作成・更新がやりやすくなると思う。


### CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

以下Claude Code作成(nishioが読んでおかしいところはないと思います)

## 主な変更内容

### 1. E2Eテスト計画書
- **TEST_PLAN.md** - 管理画面のテスト計画（レポート作成フロー）
- **CLIENT_TEST_PLAN.md** - クライアント画面のテスト計画（レポート表示機能）

### 2. 管理画面（Admin）のE2Eテスト
- **tests/admin/create-report.spec.ts** - レポート作成機能の包括的なテスト
  - CSVアップロード
  - パイプライン設定
  - レポート名入力
  - 各種フォームバリデーション

### 3. クライアント画面（Client）のE2Eテスト
- **tests/client/reports.spec.ts** - レポート一覧表示のテスト
- **tests/client/report-detail.spec.ts** - レポート詳細表示のテスト
  - 正常系・異常系のテスト
  - レスポンシブデザイン検証（デスクトップ、タブレット、モバイル）
  - パフォーマンステスト（初期読み込み時間）

### 4. ダミーAPIサーバーの実装
Clientテスト用に`utils/dummy-server`（Next.js）を拡張：
- **middleware.ts** - `/meta/metadata.json` エンドポイント
- **app/reports/route.ts** - レポート一覧API
- **app/reports/[slug]/route.ts** - レポート詳細API
- 環境変数 `E2E_TEST=true` でテストモードに切り替え

### 5. 検証テスト（推奨実行）
- **tests/verify-dummy-server.spec.ts** - ダミーサーバーが期待通りにテストフィクスチャを返すことを確認
- **tests/verify-environment.spec.ts** - 必要なサーバーが正しい環境変数で起動していることを確認

### 6. テストフィクスチャ
- **fixtures/client/metadata.json** - Meta情報
- **fixtures/client/reports.json** - レポート一覧データ
- **fixtures/client/report-test-report-1.json** - レポート詳細データ（実際の本番データ構造を使用）

### 7. デバッグ用テスト
- **tests/simple.spec.ts** - 接続確認テスト
- **tests/debug.spec.ts** - 要素確認テスト

### 8. 設定ファイルとドキュメント
- **playwright.config.ts** - 3つのプロジェクト（verify, admin, client）
- **README.md** - 詳細な実行手順とデバッグ方法

## テスト実行方法

### 管理画面テスト
```bash
cd client-admin && npm run dev  # port 4000
cd test/e2e && npx playwright test --project=admin
```

### クライアント画面テスト
```bash
# ターミナル1: ダミーAPIサーバー
cd utils/dummy-server
PUBLIC_API_KEY=public E2E_TEST=true npx next dev -p 8002

# ターミナル2: クライアント
cd client
NEXT_PUBLIC_API_BASEPATH=http://localhost:8002 \
API_BASEPATH=http://localhost:8002 \
NEXT_PUBLIC_PUBLIC_API_KEY=public \
npm run dev

# ターミナル3: テスト実行（検証テスト推奨）
cd test/e2e
npx playwright test tests/verify-dummy-server.spec.ts --project=verify
npx playwright test tests/verify-environment.spec.ts --project=verify
npx playwright test --project=client
```

## テスト結果

- **管理画面テスト**: 動作確認済み
- **クライアント画面テスト**: 17/17 テスト成功
  - レポート一覧: 7/7 成功
  - レポート詳細: 10/10 成功
- **検証テスト**: 7/7 成功
  - ダミーサーバー検証: 4/4 成功
  - 環境設定検証: 3/3 成功

## 重要な注意事項

1. **Next.jsのハイドレーション待機が必須**  
   すべてのテストで `await page.waitForLoadState("networkidle")` を使用しています。

2. **検証テストの実行を推奨**  
   Clientテストが失敗する場合、まず検証テストを実行して環境設定を確認してください。

3. **実際の本番データ構造を使用**  
   `fixtures/client/report-test-report-1.json` は実際のパイプライン処理結果（hierarchical_result.json）をコピーしており、テストが本番データ構造を正確に検証できます。

4. **ダミーサーバーは既存のutils/dummy-serverを拡張**  
   新しいサーバーを作成せず、既存のNext.jsダミーサーバーを活用しています。

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- テスト
  - Playwright を用いた包括的なE2E環境を追加し、管理画面とクライアントの検証、レスポンシブ／パフォーマンス／エラーケースを網羅するテスト群と実行スクリプトを追加。
  - ダミーAPIとテスト用フィクスチャを導入し、検証・デバッグ用の専用テスト群を整備。
- ドキュメント
  - E2E ガイド、複数のテスト計画、フィクスチャ/実行/デバッグ手順を大幅に追記。
- チョア
  - バージョン管理の ignore ルールを拡充し、CI ワークフローを更新してクライアントとダミーAPIのセットアップを反映。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

