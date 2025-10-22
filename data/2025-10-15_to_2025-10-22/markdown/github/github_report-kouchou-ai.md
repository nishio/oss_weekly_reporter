# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-10-15T12:27:09.640380+09:00 から 2025-10-22T12:27:09.640380+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (2件)

### [静的HTML出力（GitHub Pages等）のE2Eテストを実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/720)

**作成者:** nishio  
**作成日:** 2025-10-15T16:46:15Z  
**変更:** +1023 -11 (12ファイル)  
**マージ日:** 2025-10-17T06:37:27Z  
**内容:**

## 概要

静的ホスティング環境（GitHub Pagesなど）での動作を検証するE2Eテストを実装しました。

## 背景

静的ビルド（`output: "export"`）を使用して生成されたHTMLファイルが、実際にホスティング環境で正しく動作するかを自動テストで検証する必要がありました。特に以下の2つのホスティングパターンを検証する必要がありました:

1. **Rootドメインホスティング**: `https://example.com/` 形式
2. **サブディレクトリホスティング**: `https://example.com/kouchou-ai/` 形式（basePathあり）

## 実装内容

### 📋 テスト計画

- `test/e2e/CLIENT_STATIC_TEST_PLAN.md` を作成
- Rootホスティングとサブディレクトリホスティングの違いを文書化
- 各ホスティングパターンで検証すべきシナリオを定義

### 🔧 自動ビルドプロセス

#### 1. ビルドスクリプト (`scripts/build-static.sh`)
- Rootホスティング用とサブディレクトリホスティング用の静的ビルドを生成
- 環境変数で動作を制御:
  - Root: `NEXT_PUBLIC_STATIC_EXPORT_BASE_PATH=""`
  - Subdir: `NEXT_PUBLIC_STATIC_EXPORT_BASE_PATH="/kouchou-ai"`
- 出力先:
  - Root → `client/out/`
  - Subdir → `client/out-subdir/`

#### 2. グローバルセットアップ (`scripts/global-setup.ts`)
- テスト実行前に自動的に静的ビルドを生成
- `SKIP_STATIC_BUILD=true` で既存ビルドを使用可能
- ビルド順序を最適化（subdir → rootの順で実行）

### 🧪 テストスイート

#### client-static-root (15テスト)
- Rootドメインホスティングを検証
- basePathなしでの動作を確認
- http://localhost:3001 でテスト

#### client-static-subdir (16テスト)
- サブディレクトリホスティングを検証
- basePath="/kouchou-ai" での動作を確認
- http://localhost:3002/kouchou-ai でテスト
- 静的リソースが `/kouchou-ai/_next/...` から正しく読み込まれることを検証

#### テストカバレッジ
- ✅ レポート一覧の表示
- ✅ レポート詳細の表示
- ✅ クラスタ情報の表示
- ✅ ナビゲーション（戻るボタン）
- ✅ レスポンシブデザイン（デスクトップ/タブレット/モバイル）
- ✅ パフォーマンス（初期読み込み時間）
- ✅ 404エラーハンドリング

### 🔨 修正内容

#### 1. `client/scripts/rename-file.mjs`
静的エクスポート時に `opengraph-image.png` ディレクトリを除外するように修正:

```javascript
if (process.env.NEXT_PUBLIC_OUTPUT_MODE === "export") {
  ignoreFiles = [
    "app/[slug]/opengraph-image.tsx",
    "app/[slug]/opengraph-image.png"  // 追加
  ];
}
```

**理由**: Next.jsの静的エクスポートでは、動的ルート内のOGP画像生成が `generateStaticParams()` を要求するため、ビルド時に一時的に除外する必要があります。

#### 2. `client/.gitignore`
静的ビルド出力ディレクトリを追加:

```
out
out-subdir  # 追加
public/meta
```

#### 3. `test/e2e/playwright.config.ts`
- `globalSetup` を追加
- 2つの新しいプロジェクトを追加:
  - `client-static-root`
  - `client-static-subdir`
- 各プロジェクト用のwebServerを設定（http-serverでポート3001と3002）

## テスト結果

```bash
$ SKIP_STATIC_BUILD=true npx playwright test --project=client-static-root --project=client-static-subdir

✓ client-static-root: 15 passed
✓ client-static-subdir: 16 passed
✓ Total: 31 passed in 23.9s
```

### 検証項目
- ✅ Rootホスティング（`basePath=""`）が正常に動作
- ✅ サブディレクトリホスティング（`basePath="/kouchou-ai"`）が正常に動作
- ✅ 静的リソースが正しいパスから読み込まれる
- ✅ ナビゲーションがbasePathを考慮して動作
- ✅ レスポンシブデザインが全デバイスで動作
- ✅ パフォーマンス基準を満たしている

## 使用方法

### 全テストを実行（ビルドから）
```bash
cd test/e2e
npx playwright test --project=client-static-root --project=client-static-subdir
```

### 既存ビルドを使用してテスト
```bash
cd test/e2e
SKIP_STATIC_BUILD=true npx playwright test --project=client-static-root --project=client-static-subdir
```

### Rootホスティングのみテスト
```bash
cd test/e2e
npx playwright test --project=client-static-root
```

### サブディレクトリホスティングのみテスト
```bash
cd test/e2e
npx playwright test --project=client-static-subdir
```

## 技術的な詳細

### ビルド順序の重要性
`build-static.sh subdir` は `out/` を `out-subdir/` に**移動**するため、以下の順序で実行する必要があります:

1. `build-static.sh subdir` → `out/` を `out-subdir/` に移動
2. `build-static.sh root` → 新しい `out/` を生成

この順序により、両方のディレクトリが同時に存在します。

### http-serverの使用
playwright.config.tsで各静的ビルドを別々のポートでホスト:

- Port 3001: `client/out/` (Root)
- Port 3002: `client/out-subdir/` (Subdir)

### basePath設定の検証
サブディレクトリテストでは、以下を確認:

1. URLが `/kouchou-ai` プレフィックスを持つ
2. 静的リソース（JS/CSS）が `/kouchou-ai/_next/...` から読み込まれる
3. ページ間ナビゲーションがbasePathを保持する

## ドキュメント

詳細な情報は以下を参照:
- テスト計画: `test/e2e/CLIENT_STATIC_TEST_PLAN.md`
- 実行手順: `test/e2e/README.md`

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- 新機能: なし
- 変更
  - 動的ページのOpen Graph画像生成を削除。共有時のOG画像配信が行われなくなります。
- ドキュメント
  - クライアント静的ビルド向けE2Eテスト手順・運用ガイドを追記（ルート配置／サブディレクトリ配置の両方に対応）。
- テスト
  - 静的ビルド（ルート／サブディレクトリ）向けのE2Eテスト一式を追加（表示、ナビゲーション、レスポンシブ、パフォーマンス、静的アセット検証）。
- 雑務
  - 静的出力の追加ディレクトリを無視対象に追加。
  - テスト前に静的ビルドを自動生成するセットアップとサーバー起動設定を追加。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [E2Eテストの実装（管理画面とクライアント画面）](https://github.com/digitaldemocracy2030/kouchou-ai/pull/719)

**作成者:** nishio  
**作成日:** 2025-10-13T18:35:13Z  
**変更:** +137832 -91 (27ファイル)  
**マージ日:** 2025-10-15T08:59:11Z  
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

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

