# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-05-20T13:35:53.007615+09:00 から 2026-05-27T13:35:53.007615+09:00 まで

## Issues

### 過去7日間に完了されたissue (30件)

### [Windows実機での Docker Desktop セットアップ検証手順を整備する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/860)

**作成者:** nishio  
**作成日:** 2026-05-22T11:56:31Z  
**内容:**

## 概要

Windows 実機で `setup_win.bat` と Docker Desktop (`Linux containers`) を使ったセットアップを検証するための手順を整備する。

## 背景

`windows-latest` hosted runner では、Docker Desktop + Linux containers の実セットアップを完全自動化しにくい。そこで、軽量 CI は別 issue で扱い、この issue では **Windows 実機または self-hosted runner 上で AI / 人間が再実行できる手順** をまとめる。

## スコープ

- Windows 実機テストで確認すべき観点を整理
- 実行前提（Docker Desktop, WSL2, 再起動, API key, 展開手順）を明文化
- AI エージェント向けの再実行手順と観測ポイントをまとめる
- 必要なら docs や workflow comment に落とす

## 非スコープ

- `windows-latest` で回す軽量 regression test の追加

こちらは別 issue で扱う。


**コメント:** なし

---

### [Windows環境向け setup_win.bat の軽量 regression test を作る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/859)

**作成者:** nishio  
**作成日:** 2026-05-22T11:53:09Z  
**内容:**

## 概要

Windows 環境向け `setup_win.bat` の軽量 regression test を GitHub Actions (`windows-latest`) に追加する。

## スコープ

- `setup_win.bat` が文字化けせず読めることを確認
- `chcp 65001` を前提にした Windows バッチの基本実行が壊れていないことを確認
- Docker 未起動時に想定メッセージを出して停止することを確認
- API key 入力と `.env` 生成の基本分岐を確認
- 実 Docker Desktop / Linux containers の起動までは行わない

## 非スコープ

- Windows 実機での Docker Desktop + Linux containers の end-to-end 検証
- 実機テスト用の運用手順整備

これらは別 issue に分離して扱う。


**コメント:** なし

---

### [CSP / remote asset policy for public-IP HTTP access on current apps/* tree](https://github.com/digitaldemocracy2030/kouchou-ai/issues/846)

**作成者:** nishio  
**作成日:** 2026-05-21T12:44:38Z  
**内容:**

## Summary

`Issue #685` / `#833` で混ざっていた論点のうち、CSP と remote asset loading policy を current `apps/*` tree 向けに切り出す。

対象は主に次。

- public IP + HTTP で self-host したときの CSP violation
- `apps/public-viewer` / `apps/admin` が API / image / font 等をどこまで許可するか
- hardcoded host を入れずに current config (`API_BASEPATH`, `NEXT_PUBLIC_API_BASEPATH`, `NEXT_PUBLIC_SITE_URL`) と整合する policy をどう作るか

## Why split from #833

`#833` は UUID fallback / CSP / LocalLLM auto-fetch を 1 本に束ねていて review 単位が大きすぎる。
UUID fallback は別 branch で独立着手できたため、CSP / remote asset policy は別 issue として切り出す。

## Scope

- current `apps/public-viewer` / `apps/admin` tree を前提にする
- stale な `client/` / `client-admin/` patch は revive しない
- security header と asset loading policy を review 可能な単位で再設計する

## Related

- original report: #685
- umbrella follow-up: #833
- adjacent docs issue: #820
- adjacent PNG/CSP issue: #818


**コメント:** なし

---

### [LocalLLM model auto-fetch UX on current apps/admin create flow](https://github.com/digitaldemocracy2030/kouchou-ai/issues/845)

**作成者:** nishio  
**作成日:** 2026-05-21T12:44:37Z  
**内容:**

## Summary

`Issue #685` / `#833` で混ざっていた論点のうち、LocalLLM の model auto-fetch UX を current `apps/admin` create flow 向けに切り出す。

旧 `PR #735` では CSP や UUID fix と同時に扱われていたが、UX 改善としては別レビュー単位にした方がよい。

## Scope

- `apps/admin/app/create/hooks/useAISettings.ts` まわりの LocalLLM model fetch UX
- provider が `local` のときに、接続済み endpoint から model list をどう取得・表示するか
- current admin flow に乗る範囲で扱い、CSP / secure-context 問題とは分離する

## Why split from #833

`#833` の主要な bug fix（UUID fallback, CSP policy）とは性質が違い、review でも判断軸が異なる。
そのため current-tree follow-up として個別 issue に分離する。

## Related

- original report: #685
- umbrella follow-up: #833


**コメント:** なし

---

### [テストの共通モック/fixture 重複を整理する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/842)

**作成者:** nishio  
**作成日:** 2026-05-20T19:10:51Z  
**内容:**

## 背景

PR #840 (`workflow default化の土台を整備`) の review で、次の test file に重複した test double / mock setup が多いという指摘があった。

- `apps/api/tests/services/test_report_launcher.py`
- `apps/api/tests/routers/test_get_current_step.py`

指摘自体は妥当だが、PR #840 の本筋は workflow default 化の互換性確認であり、この cleanup は release blocker ではないため分離する。

## やりたいこと

### 1. `test_report_launcher.py`

- `DummyPopen`
- `ImmediateThread` / `DummyThread`
- sync recorder (`calls`, `syncs`)
- `subprocess.Popen` / `threading.Thread` monkeypatch

の重複を helper / fixture に寄せる。

### 2. `test_get_current_step.py`

- `settings.REPORT_DIR` の patch
- `builtins.open` の patch
- `json.load` の patch
- status file exists mock

の重複を helper / fixture に寄せる。

## ゴール

- test の意図を変えずに、mock setup の重複だけを減らす
- workflow default 化の挙動確認テストを保ちつつ、今後の更新時の drift を減らす

## スコープ外

- production code の挙動変更
- workflow / API status semantics の追加変更
- PR #840 に含まれる互換性修正の再設計


**コメント:** なし

---

### [Document filesystem-based usage for analysis-core CLI](https://github.com/digitaldemocracy2030/kouchou-ai/issues/836)

**作成者:** nishio  
**作成日:** 2026-05-19T08:00:28Z  
**内容:**

## Background

`#721` originally targeted the legacy `server/broadlistening/...` path, but the canonical CLI path is now `packages/analysis-core/` via:

- `python -m analysis_core`
- `kouchou-analyze`

We need current documentation for filesystem-based usage that matches the actual maintained entrypoint.

## Scope

- document current CLI usage for filesystem-based execution
- explain config path, input path, output path, and `--output-dir` / `--input-dir`
- explain `--dry-run` and `--without-html`
- avoid documenting deprecated `hierarchical_main.py` as the recommended path
- place or link the doc from the current canonical location

## Non-goals

- adding new validation logic
- reviving legacy `server/broadlistening/...` docs

## Parent

- part of #721


**コメント:** なし

---

### [Add config and input preflight validation to analysis-core CLI](https://github.com/digitaldemocracy2030/kouchou-ai/issues/837)

**作成者:** nishio  
**作成日:** 2026-05-19T08:00:28Z  
**内容:**

## Background

`#721` identified a real need for preflight validation, but the implementation should target the current `analysis-core` CLI rather than the deprecated pipeline shim.

## Scope

- design and implement preflight validation for current `analysis-core` config and input data
- decide whether this should be exposed as explicit CLI flags, subcommands, or integrated into normal startup
- validate config structure against current canonical config shape
- validate input file presence / shape before expensive pipeline execution
- ensure behavior and messaging are compatible with the maintained CLI path

## Questions to settle

- should this be `--validate-config` / `--validate-input`, or a separate command shape?
- how much should `--dry-run` cover versus explicit validation?
- which validations are safe and cheap enough to run by default?

## Non-goals

- output artifact validation
- legacy `server/broadlistening/...` compatibility work

## Parent

- part of #721


**コメント:** なし

---

### [Admin UUID fallback for public-IP HTTP access on current apps/* tree](https://github.com/digitaldemocracy2030/kouchou-ai/issues/833)

**作成者:** nishio  
**作成日:** 2026-05-18T15:55:00Z  
**内容:**

## Summary

`Issue #685` / 旧 `PR #735` で報告されていた論点のうち、current `apps/*` tree でまず独立対応できる `apps/admin` の `crypto.randomUUID()` 依存を扱う。

public IP + HTTP など non-secure context では `crypto.randomUUID()` が使えず、create / reuse 画面が即死しうる。ここを current-tree fix として先に分離する。

## Scope

- `apps/admin` create / reuse flow の UUID 生成
- `crypto.randomUUID()` が無い環境での fallback
- helper / unit test を含む current-tree fix

## Out of scope

- CSP / remote asset loading policy → `#846`
- LocalLLM model auto-fetch UX → `#845`

## Related

- original report: #685
- stale patch discussion: #735
- branch in progress: `feature/issue-833-admin-uuid`


**コメント:** なし

---

### [静的エクスポート環境向けのCSP設定ガイドをドキュメントに追加する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/820)

**作成者:** tokoroten  
**作成日:** 2026-03-29T12:44:22Z  
**内容:**

## 背景

PR #819 で、Plotly の PNG ダウンロードが CSP の `img-src` に `blob:` が含まれていないためブロックされる問題が報告されました。

https://www.broadlistening-hiroshima.com/ の本番環境では、Azure Static Web Apps 側で以下の CSP ヘッダーが付与されています：

```
content-security-policy: default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://js.monitor.azure.com; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self' https://js.monitor.azure.com https://*.applicationinsights.azure.com https://*.azurestaticapps.net; font-src 'self' data:; frame-ancestors 'none';
```

`next.config.ts` の `headers()` は `output: 'export'`（静的ビルド）時には無効（Next.js の仕様で no-op）のため、アプリケーション側での対応だけでは不十分です。

## やりたいこと

リバースプロキシ / CDN / 静的ホスティング環境での CSP 設定ガイドをドキュメントに追加する。

具体的には：
- `img-src` に `blob:` を含める必要がある旨の説明（Plotly の PNG エクスポートに必要）
- Azure Static Web Apps（`staticwebapp.config.json`）での設定例
- その他のホスティング環境（Nginx、Cloudflare 等）での設定例

## 関連
- #819

**コメント:** なし

---

### [PNGでダウンロードボタンが死んでいる可能性がある。](https://github.com/digitaldemocracy2030/kouchou-ai/issues/818)

**作成者:** tokoroten  
**作成日:** 2026-03-29T08:52:54Z  
**内容:**

PNGでダウンロードボタンが死んでいる可能性がある。
要調査
<img width="1241" height="740" alt="Image" src="https://github.com/user-attachments/assets/02137572-8913-4872-85be-e8219c6b3fc7" />

コンソールには次のエラーが出てきた
```
Loading the image 'blob:https://www.broadlistening-hiroshima.com/f28317b7-2c10-4b7b-8534-1ef4a988968b' violates the following Content Security Policy directive: "img-src 'self' data:". The action has been blocked.
```

**コメント:** なし

---

### [#813 の coderabbit, github workflow についての議論](https://github.com/digitaldemocracy2030/kouchou-ai/issues/815)

**作成者:** shingo-ohki  
**作成日:** 2026-03-09T01:36:31Z  
**内容:**

https://github.com/digitaldemocracy2030/kouchou-ai/pull/813 にて、以下のポイントは（一旦マージしてしまいましたが）議論すべきと思ったので 一旦 Issue にしました。

コメントがある方はぜひお願いします。

> .coderabbit.yaml と .github/workflows/codeql.yml は本PRの主題（空コメントフィルタ）とは無関係な変更です。元PR https://github.com/digitaldemocracy2030/kouchou-ai/pull/796 に含まれていたものをそのまま含めていますが、別PRに分離すべきか検討をお願いします

> 
Configuration & CI/CD Setup.coderabbit.yaml, .github/workflows/codeql.yml | CodeRabbit の自動レビュー設定とドラフト機能の有効化、および GitHub Actions による CodeQL セキュリティ分析ワークフローを新たに追加。
-- | --




**コメント:** なし

---

### [fix: ローカル開発環境でのReactバージョン不一致によるdev overlay クラッシュ](https://github.com/digitaldemocracy2030/kouchou-ai/issues/799)

**作成者:** tokoroten  
**作成日:** 2026-02-22T01:13:47Z  
**内容:**

## 問題

`make client-dev` でローカル開発環境を起動すると、以下のエラーが発生する。

```
TypeError: Cannot read properties of null (reading 'useReducer')
    at process.env.NODE_ENV.exports.useReducer (react.development.js:1215:33)
    at useErrorOverlayReducer (react-dev-overlay/shared.js:126:34)
    at usePagesDevOverlay (pages/hooks.js:18:66)
    at PagesDevOverlay (pages/pages-dev-overlay.js:19:71)
    at ReactDevOverlay (next-dev-server.js:103:12)
```

## 原因

pnpm ワークスペース環境で React のバージョンが2箇所に存在し、インスタンスが一致しない。

| 場所 | React バージョン |
|---|---|
| ルート `node_modules/react` | **19.1.0** |
| `apps/public-viewer/node_modules/react` | **19.2.3** |

`pnpm --filter @kouchou-ai/public-viewer dev`（`make client-dev`）をルートから実行すると、Next.js の開発インフラ（dev overlay 等）はルートの React 19.1.0 を使い、アプリ本体は React 19.2.3 を使う。2つの React インスタンスでディスパッチャーが共有されないため、`useReducer` 呼び出し時に `ReactCurrentDispatcher.current` が null になる。

## 回避策

現時点での回避策：

- **Docker 使用**（推奨）: `docker compose up` はコンテナ内で完結するため問題なし
- **直接実行**: `cd apps/public-viewer && pnpm dev` で実行するとルートの React が介在しない

## 恒久対応案

ルートの `package.json` の React/React-DOM を 19.2.3 に揃える、または pnpm の `overrides` で統一する。

```json
// package.json (root)
{
  "pnpm": {
    "overrides": {
      "react": "19.2.3",
      "react-dom": "19.2.3"
    }
  }
}
```

**コメント:** なし

---

### [レポート一覧取得時にslugフィールドの欠落によるValidationErrorが発生する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/740)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-12-27T14:09:44Z  
**内容:**

## 概要

レポート一覧画面でレポートの取得に失敗し、「レポートの取得に失敗しました」というエラーメッセージが表示される問題が発生しています。

## 原因

`report_status.json` に保存されている既存のレポートデータに `slug` フィールドが欠落しているため、Pydanticのバリデーションエラーが発生しています。

## エラーログ

```
pydantic_core._pydantic_core.ValidationError: 1 validation error for Report
slug
  Field required [type=missing, input_value={'status': 'ready', 'titl...token_usage_output': 70}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
```

## 再現手順

1. `docker compose up` でアプリケーションを起動
2. http://localhost:3000 または http://localhost:4000 にアクセス
3. レポート一覧を取得しようとすると、上記のエラーが発生

## 影響範囲

- レポート閲覧画面（client）のレポート一覧
- 管理画面（client-admin）のレポート一覧

## 関連コード

- `server/src/services/report_status.py` の `load_status_as_reports()` 関数
- `server/src/schemas/report.py` の `Report` スキーマ

## 提案される修正方法

1. 既存の `report_status.json` データに `slug` フィールドを追加するマイグレーションスクリプトを作成
2. または、`load_status_as_reports()` 関数で `slug` フィールドが欠落している場合のフォールバック処理を追加

**コメント:** なし

---

### [ファイルシステムベース実行方式の明確化と検証テスト追加](https://github.com/digitaldemocracy2030/kouchou-ai/issues/721)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-10-23T07:29:00Z  
**内容:**

# kouchou-ai ファイルシステムベース実行方式の明確化と検証テスト追加プラン

## 現状分析

### 既存の実装状況

kouchou-aiには既にファイルシステムベースでパイプラインを実行する機能が実装されています：

1. **エントリーポイント**: `server/broadlistening/pipeline/hierarchical_main.py`
   - CLIとして直接実行可能
   - APIサーバーを起動せずにパイプライン処理が可能

2. **入力ファイル配置場所**:
   - CSVファイル: `server/broadlistening/pipeline/inputs/`
   - 設定JSONファイル: `server/broadlistening/pipeline/configs/`

3. **出力ファイル配置場所**:
   - `server/broadlistening/pipeline/outputs/{dataset}/`
   - 最終結果: `hierarchical_result.json`
   - 中間ファイル: `args.csv`, `embeddings.pkl`, `hierarchical_clusters.csv` など

4. **パイプライン処理ステップ** (8段階):
   - extraction → embedding → hierarchical_clustering → hierarchical_initial_labelling
   - → hierarchical_merge_labelling → hierarchical_overview → hierarchical_aggregation
   - → hierarchical_visualization

### 不明確な点

1. **入力CSVフォーマット**:
   - 必須カラムの仕様
   - 文字エンコーディング要件
   - データ型の制約

2. **設定JSONフォーマット**:
   - 必須フィールドとオプションフィールド
   - 各パラメータの意味と有効な値の範囲
   - LLMプロバイダー設定方法

3. **出力フォーマット**:
   - `hierarchical_result.json`の構造
   - 各中間ファイルの役割と構造

4. **実行方法**:
   - コマンドラインオプションの詳細
   - 環境変数の設定方法
   - エラー時の対処方法

## 実装計画

### 1. ドキュメント作成

#### 1.1 ファイルシステムベース実行ガイド
**ファイル**: `server/broadlistening/FILESYSTEM_USAGE.md`

内容:
- パイプラインの概要説明
- 入力CSVフォーマット仕様
- 設定JSONフォーマット仕様
- 実行コマンドと各オプションの説明
- 出力ファイルの構造説明
- トラブルシューティング

#### 1.2 入出力スキーマ定義
**ファイル**: `server/broadlistening/pipeline/schemas/`

- `input_csv_schema.py` - 入力CSV検証用Pydanticモデル
- `config_schema.py` - 設定JSON検証用Pydanticモデル
- `output_schema.py` - 出力JSON検証用Pydanticモデル

### 2. テスト実装

#### 2.1 入力検証テスト
**ファイル**: `server/tests/broadlistening/test_input_validation.py`

テスト項目:
- ✅ 正常なCSVファイルの読み込み
- ✅ 必須カラムの存在確認
- ✅ 文字エンコーディング検証（UTF-8, Shift-JIS, CP932）
- ✅ データ型の検証
- ❌ 不正なCSVフォーマットの検出
- ❌ 空ファイルの検出
- ❌ 必須カラム欠損の検出

#### 2.2 設定JSON検証テスト
**ファイル**: `server/tests/broadlistening/test_config_validation.py`

テスト項目:
- ✅ 正常な設定JSONの読み込み
- ✅ 必須フィールドの存在確認
- ✅ デフォルト値の適用確認
- ✅ LLMプロバイダー設定の検証
- ❌ 不正なJSONフォーマットの検出
- ❌ 必須フィールド欠損の検出
- ❌ 無効なパラメータ値の検出

#### 2.3 出力検証テスト
**ファイル**: `server/tests/broadlistening/test_output_validation.py`

テスト項目:
- ✅ 出力ディレクトリの作成確認
- ✅ 必須出力ファイルの存在確認
- ✅ `hierarchical_result.json`の構造検証
- ✅ 中間ファイルの構造検証
- ✅ ステータスファイル（`hierarchical_status.json`）の検証

#### 2.4 エンドツーエンドテスト
**ファイル**: `server/tests/broadlistening/test_pipeline_e2e.py`

テスト項目:
- ✅ 小規模データセットでの完全パイプライン実行
- ✅ 各ステップの正常完了確認
- ✅ 出力ファイルの整合性確認
- ✅ トークン使用量の記録確認
- ✅ エラー時のステータス更新確認

### 3. テストデータ準備

#### 3.1 テスト用入力ファイル
**ディレクトリ**: `server/tests/broadlistening/fixtures/`

- `valid_input.csv` - 正常なCSVファイル（10件程度の小規模データ）
- `invalid_input_missing_column.csv` - 必須カラム欠損
- `invalid_input_empty.csv` - 空ファイル
- `invalid_input_encoding.csv` - 不正なエンコーディング

#### 3.2 テスト用設定ファイル
- `valid_config.json` - 正常な設定
- `minimal_config.json` - 最小限の設定（必須フィールドのみ）
- `invalid_config_missing_field.json` - 必須フィールド欠損
- `invalid_config_wrong_type.json` - 不正なデータ型

#### 3.3 期待される出力ファイル
- `expected_output/` - 正常実行時の期待される出力ファイル一式

### 4. バリデーション機能の実装

#### 4.1 入力バリデーター
**ファイル**: `server/broadlistening/pipeline/validators/input_validator.py`

機能:
- CSVファイルの読み込みと検証
- 必須カラムの確認
- データ型の検証
- エンコーディングの検出と変換

#### 4.2 設定バリデーター
**ファイル**: `server/broadlistening/pipeline/validators/config_validator.py`

機能:
- 設定JSONの読み込みと検証
- 必須フィールドの確認
- パラメータ値の範囲チェック
- デフォルト値の適用

#### 4.3 出力バリデーター
**ファイル**: `server/broadlistening/pipeline/validators/output_validator.py`

機能:
- 出力ファイルの存在確認
- JSON構造の検証
- データ整合性の確認

### 5. CLIツールの改善

#### 5.1 バリデーションコマンド追加
**ファイル**: `server/broadlistening/pipeline/hierarchical_main.py`

新規オプション:
- `--validate-input` - 入力ファイルのみ検証
- `--validate-config` - 設定ファイルのみ検証
- `--validate-output` - 出力ファイルのみ検証
- `--dry-run` - 実行せずに計画のみ表示

## 実装順序

1. **Phase 1: ドキュメント作成**
   - [ ] `FILESYSTEM_USAGE.md` の作成
   - [ ] 既存のサンプルファイルの整理

2. **Phase 2: スキーマ定義**
   - [ ] Pydanticモデルの作成
   - [ ] バリデーション関数の実装

3. **Phase 3: テストデータ準備**
   - [ ] テスト用フィクスチャの作成
   - [ ] 期待される出力の準備

4. **Phase 4: テスト実装**
   - [ ] 入力検証テスト
   - [ ] 設定検証テスト
   - [ ] 出力検証テスト
   - [ ] E2Eテスト

5. **Phase 5: バリデーター実装**
   - [ ] 入力バリデーター
   - [ ] 設定バリデーター
   - [ ] 出力バリデーター

6. **Phase 6: CLI改善**
   - [ ] バリデーションオプション追加
   - [ ] ヘルプメッセージの改善

7. **Phase 7: 統合とドキュメント更新**
   - [ ] 全テストの実行と確認
   - [ ] ドキュメントの最終更新
   - [ ] README.mdへのリンク追加

## 成果物

### ドキュメント
1. `server/broadlistening/FILESYSTEM_USAGE.md` - ファイルシステムベース実行ガイド
2. 更新された `server/broadlistening/README.md`

### コード
1. `server/broadlistening/pipeline/schemas/` - スキーマ定義
2. `server/broadlistening/pipeline/validators/` - バリデーター実装
3. 改善された `hierarchical_main.py`

### テスト
1. `server/tests/broadlistening/test_input_validation.py`
2. `server/tests/broadlistening/test_config_validation.py`
3. `server/tests/broadlistening/test_output_validation.py`
4. `server/tests/broadlistening/test_pipeline_e2e.py`
5. `server/tests/broadlistening/fixtures/` - テストデータ

## 期待される効果

1. **明確性の向上**
   - ファイルシステムベースでの実行方法が明確になる
   - 入出力フォーマットが文書化される

2. **品質保証**
   - 入力データの妥当性が事前に検証できる
   - 出力データの整合性が保証される

3. **開発効率の向上**
   - APIサーバーなしでパイプラインのテストが可能
   - 問題の早期発見が可能

4. **保守性の向上**
   - テストによる回帰防止
   - ドキュメントによる理解促進


**コメント:** なし

---

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

### [[BUG]url情報のある散布図で点をクリックしてもリンク先にジャンプできない現象](https://github.com/digitaldemocracy2030/kouchou-ai/issues/710)

**作成者:** nishio  
**作成日:** 2025-09-24T08:36:35Z  
**内容:**

### 概要

url情報のある散布図で点をクリックしてもリンク先にジャンプできない

### 再現手順

1. url情報のある散布図で点をクリック 
2. 何も起きない

### 期待する動作

新しいタブでリンク先が開く


### その他

displayModeBar: "hover"を削除すれば筆者環境では直ったが、PRを作成する上での再現性が微妙なので他の人の環境で再現するまで保留中
https://github.com/digitaldemocracy2030/kouchou-ai/blob/40d228c8f791d269fd69eae7aed33320c0f241d9/client/components/charts/ScatterChart.tsx#L385

**コメント:** なし

---

### [[BUG]APIが利用可能であってもAPI接続チェックが失敗する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/707)

**作成者:** nishio  
**作成日:** 2025-09-22T08:18:37Z  
**内容:**

### 概要
APIが利用可能であってもAPI接続チェックが失敗する
<img width="478" height="371" alt="Image" src="https://github.com/user-attachments/assets/f27a182d-116c-48ea-b91e-4ba2e5b3e859" />

表示されるエラーメッセージは事実に反するものである。

>エラーが見つかりました。
>内容をご確認ください。
>APIキーが無効または期限切れです。.envファイルを確認し修正してください。APIキーを改めて取得し直した場合も再設定が必要です。

### 再現手順

1. Azure環境で正しくセットアップした後で接続チェックをする

### その他

この環境&設定で問題なくレポートが作れるので、おそらくAzure環境などの条件を正しくチェックしないでAPI接続チェックをしているのだと思う。

**コメント:** なし

---

### [[BUG] リモート環境でのHTTPアクセス時に発生するCSPおよびJavaScriptエラーについて](https://github.com/digitaldemocracy2030/kouchou-ai/issues/685)

**作成者:** ivan-stout  
**作成日:** 2025-08-01T05:47:15Z  
**内容:**

### 概要

リモートサーバーにデプロイしたアプリケーションに、HTTP経由でパブリックIPアドレスを使用してアクセスすると、複数のエラーが発生して正常に動作しないようです。主な原因として、非セキュアなコンテキストで`crypto.randomUUID`関数が無効になることによるJavaScriptエラーと、厳格なContent Security Policy (CSP)により必要なリソースの読み込みがブロックされる問題が考えられます。また、画像URLの生成ロジックにも不具合があるようです。

### 再現手順

1. `docker compose` を使用して、リモートサーバーにアプリケーションをデプロイする。
2. `.env` ファイルに、サーバーのパブリックIPアドレスを `NEXT_PUBLIC_API_BASEPATH` と `NEXT_PUBLIC_SITE_URL` に設定する。
3. ウェブブラウザからパブリックIPアドレス (`http://<your_server_ip>:3000` または `http://<your_server_ip>:4000`) を使用してアプリケーションにアクセスする。
4. ブラウザの開発者コンソールを開き、エラーを確認する。

### 期待する動作

アプリケーションが、設定されたパブリックIPアドレスを介してHTTPでアクセスされた場合でも、JavaScriptエラーやCSP違反を発生させることなく、正常に読み込まれ、機能すること。

### スクリーンショット・ログ

発生した主なエラーは以下の通りです。

**1. JavaScriptのクラッシュを引き起こす`crypto.randomUUID`エラー**
```
Uncaught TypeError: crypto.randomUUID is not a function
    at ec (page-e894ce97fa4cefba.js:1:18309)
    ...
```

**2. Content Security Policy違反によるリソース読み込みエラー**
```
Refused to load the image 'http://18.233.19.158:8000/meta/icon.png' because it violates the following Content Security Policy directive: "img-src 'self' data:".
```

### ご参考：動作確認のための修正案 (git diff)

```diff
diff --git a/client-admin/app/layout.tsx b/client-admin/app/layout.tsx
index 1fb5a81..89e892e 100644
--- a/client-admin/app/layout.tsx
+++ b/client-admin/app/layout.tsx
@@ -21,6 +21,23 @@ export default function RootLayout({ children }: Readonly<{ children: React.Reac
   return (
     <html suppressHydrationWarning lang={"ja"}>
       <head>
+        <script
+          dangerouslySetInnerHTML={{
+            __html: `
+              if (typeof window !== 'undefined' && !window.crypto) {
+                window.crypto = {};
+              }
+              if (typeof window !== 'undefined' && !window.crypto.randomUUID) {
+                window.crypto.randomUUID = () => {
+                  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
+                    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
+                    return v.toString(16);
+                  });
+                };
+              }
+            `,
+          }}
+        />
         <link rel="preconnect" href="https://fonts.googleapis.com" />
         <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
         <link href="https://fonts.googleapis.com/css2?family=BIZ+UDPGothic&display=swap" rel="stylesheet" />
diff --git a/client-admin/next.config.ts b/client-admin/next.config.ts
index a481870..3f280a4 100644
--- a/client-admin/next.config.ts
+++ b/client-admin/next.config.ts
@@ -4,6 +4,19 @@ const nextConfig: NextConfig = {
   experimental: {
     optimizePackageImports: ["@chakra-ui/react"],
   },
+  async headers() {
+    return [
+      {
+        source: '/:path*',
+        headers: [
+          {
+            key: 'Content-Security-Policy',
+            value: "default-src 'self'; script-src 'self' 'unsafe-eval' 'unsafe-inline' https://fonts.googleapis.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; img-src 'self' data: http://18.233.19.158:8000; font-src 'self' https://fonts.gstatic.com; connect-src 'self' http://18.233.19.158:8000;",
+          },
+        ],
+      },
+    ];
+  },
 };
 
 export default nextConfig;
diff --git a/client/app/utils/image-src.ts b/client/app/utils/image-src.ts
index aefa36e..a7af5a7 100644
--- a/client/app/utils/image-src.ts
+++ b/client/app/utils/image-src.ts
@@ -62,7 +62,7 @@ export const getImageFromServerSrc = (src: string): string => {
     }
 
     // パスが / で始まることを確認
-    const normalizedSrc = src.startsWith("/") ? src : `/${src}`;
-    return `${basePath}${normalizedSrc}`;
+    const normalizedSrc = src.startsWith("/") ? src.substring(1) : src;
+    return `${basePath}/${normalizedSrc}`;
   }
 };
```

### 修正に関する注意点

上記の修正案は、今回の環境で問題の回避を確認できたものですが、あくまでご参考としてお考え下さい。恒久的な対策としては、セキュリティリスクを導入しないよう、より詳細な調査が必要になる可能性があります。 

**コメント:** なし

---

### [[BUG] 静的ファイル出力時に公開状態のレポートがない場合にエラーとなる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/683)

**作成者:** shingo-ohki  
**作成日:** 2025-07-31T01:14:24Z  
**内容:**

### 概要

<!-- バグの簡潔な説明をお願いします -->
公開状態のレポートがない状態で、[静的ファイル出力](https://github.com/digitaldemocracy2030/kouchou-ai?tab=readme-ov-file#%E9%9D%99%E7%9A%84%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%87%BA%E5%8A%9B)を行うとエラーが出る。


### 再現手順

1. レポートを生成する
2. すべてのレポートを「公開」以外の状態にする
3. [静的ファイル出力](https://github.com/digitaldemocracy2030/kouchou-ai?tab=readme-ov-file#%E9%9D%99%E7%9A%84%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%87%BA%E5%8A%9B)を行う

または、レポートがない状態で 3 を行う。

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->
例えば以下などが考えられるが、どうすべきかは議論が必要そう
- 適切なエラー（「公開状態のレポートがないためレポートを静的出力できません」etc.）を表示する
- 公開状態にかかわらず静的レポートを出力できるようにする

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

```
❯ make client-build-static
rm -rf out
docker compose up -d --wait api
[+] Running 1/1
 ✔ Container kouchou-ai-api-1  Healthy                                                                                        0.5s 
docker compose run --rm -e BASE_PATH= -e NEXT_PUBLIC_OUTPUT_MODE=export -v /home/tizze/program/digital-democracy/kouchou-ai/server:/server -v /home/tizze/program/digital-democracy/kouchou-ai/out:/app/dist client sh -c "npm run build:static && cp -r out/* dist && touch dist/.nojekyll"
[+] Creating 1/1
 ✔ Container kouchou-ai-api-1  Running                                                                                        0.0s 

> kouchou-ai-client@0.1.0 prebuild:static
> npm run copy-image && NEXT_PUBLIC_OUTPUT_MODE=export npm run rename-file


> kouchou-ai-client@0.1.0 copy-image
> node scripts/copy-image.mjs

Copied from default: icon.png
Copied from default: reporter.png
Copied from default: ogp.png
✅ All images copied successfully.

> kouchou-ai-client@0.1.0 rename-file
> node scripts/rename-file.mjs rename

Renamed: app/[slug]/opengraph-image.tsx → _opengraph-image.tsx

> kouchou-ai-client@0.1.0 build:static
> NEXT_PUBLIC_OUTPUT_MODE=export next build

   ▲ Next.js 15.2.3

   Creating an optimized production build ...
 ✓ Compiled successfully
 ✓ Linting and checking validity of types    

> Build error occurred
[Error: Page "/[slug]/opengraph-image.png" is missing "generateStaticParams()" so it cannot be used with "output: export" config.]
npm notice
```
### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->
[BUG] scripts/fetch_reports.pyでは「限定公開」「非公開」状態のレポートがバックアップできない #629 
も似た話

**コメント:** なし

---

### [[FEATURE] APIの接続チェック機能でユーザー入力APIキーもチェックできるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/681)

**作成者:** shingo-ohki  
**作成日:** 2025-07-27T10:39:32Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
現状、API接続チェックはユーザーが入力したAPIキー(https://github.com/digitaldemocracy2030/kouchou-ai/issues/633) については有効性の確認ができない

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->


**コメント:** なし

---

### [[BUG] Windows 環境で api の build error が出る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/666)

**作成者:** shingo-ohki  
**作成日:** 2025-07-15T22:23:03Z  
**内容:**

### 概要

<!-- バグの簡潔な説明をお願いします -->
Windows 環境で api の build 時に build error になる
 
### 再現手順

1. Windows 環境で docker compose up を実行

```
--------------------
  19 |     # WITH_GPU=false の場合は、不要なパッケージがインストールされないように CPU版の PyTorch を先にインストール
  20 | >>> RUN if [ "$WITH_GPU" = "false" ]; then \
  21 | >>>     echo "Installing PyTorch (CPU version)" && \
  22 | >>>     uv pip install --no-cache --system -r requirements-torch.txt --index-url https://download.pytorch.org/whl/cpu; \
  23 | >>>     fi
  24 |
--------------------
target api: failed to solve: process "/bin/sh -c if [ \"$WITH_GPU\" = \"false\" ]; then     echo \"Installing PyTorch (CPU version)\" &&     uv pip install --no-cache --system -r requirements-torch.txt --index-url https://download.pytorch.org/whl/cpu;     fi" did not complete successfully: exit code: 1
View build details: docker-desktop://dashboard/build/default/default/6az53xylwvpj196tnuhralrob
```

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->

dockerfileを以下のように書き換えたところ動きました。
```
# ---- 1. ベースイメージ --------------------------------------------------
    FROM python:3.12-slim
    WORKDIR /app
    # ---- 2. ビルド引数 -------------------------------------------------------
    ARG ENVIRONMENT=production   # development / production
    ARG WITH_GPU=false           # true / false
    # ---- 3. 共通ビルドツール ------------------------------------------------
    RUN apt-get update \
     && apt-get install -y --no-install-recommends curl build-essential \
     && rm -rf /var/lib/apt/lists/*
    RUN pip install --no-cache-dir uv
    # ---- 4. Poetry / pip の依存関係 -----------------------------------------
    COPY pyproject.toml requirements.lock requirements-dev.lock requirements-torch.txt README.md ./
    #
    # 4-A. PyTorch 系 (GPU か CPU かで分岐)
    #
    RUN if [ "${WITH_GPU}" = "false" ]; then \
            echo ">> Installing PyTorch (CPU version)" && \
            uv pip install --no-cache-dir --system -r requirements-torch.txt \
                --index-url https://download.pytorch.org/whl/cpu ; \
        else \
            echo ">> Installing PyTorch (GPU version)" && \
            uv pip install --no-cache-dir --system -r requirements-torch.txt ; \
        fi
    #
    # 4-B. アプリ依存 (dev / prod で分岐)
    #
    RUN if [ "${ENVIRONMENT}" = "development" ]; then \
            echo ">> Installing development dependencies" && \
            uv pip install --no-cache-dir --system -r requirements-dev.lock ; \
        else \
            echo ">> Installing production dependencies" && \
            uv pip install --no-cache-dir --system -r requirements.lock ; \
        fi
    # ---- 5. アプリケーション本体 --------------------------------------------
    COPY . .
    EXPOSE 8000
    CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

**コメント:** なし

---

### [[BUG]  scripts/fetch_reports.pyでは「限定公開」「非公開」状態のレポートがバックアップできない](https://github.com/digitaldemocracy2030/kouchou-ai/issues/629)

**作成者:** shingo-ohki  
**作成日:** 2025-07-03T01:10:52Z  
**内容:**

### 概要

scripts/fetch_reports.pyでは「公開」状態のレポートのバックアップは行われるが、「限定公開」「非公開」状態のレポートがバックアップできない

### 再現手順

1. レポートを限定公開にする
2.   scripts/fetch_reports.py を実行する

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->

レポートの公開状態に関わらず、レポートのバックアップが行われる
```
Fetching reports from https://api.wittyisland-cc57c95f.japaneast.azurecontainerapps.io...
Sending request to https://api.wittyisland-cc57c95f.japaneast.azurecontainerapps.io/reports with API key: xxx...
Found 1 reports
Processing report: 17dd4a5a-3b6b-4468-adfa-3c4c5e434228 - サンプルレポート
Saved report result for 17dd4a5a-3b6b-4468-adfa-3c4c5e434228 to /workspace/server/broadlistening/pipeline/outputs/17dd4a5a-3b6b-4468-adfa-3c4c5e434228/hierarchical_result.json
Updated report status in /workspace/server/data/report_status.json
Successfully processed 1 reports
```

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

make azure-update-deployment の内部で `scripts/fetch_reports.py` が実行されており、その際に気がつきました。
```
$ make azure-update-deployment
...
Fetching reports from https://api.wittyisland-cc57c95f.japaneast.azurecontainerapps.io...
Sending request to https://api.wittyisland-cc57c95f.japaneast.azurecontainerapps.io/reports with API key: xxx...
Found 0 reports
No reports were successfully processed
```

もっと言うと、以下でレポートの内容が取得できないことに起因するようでした。
```
$ curl -H 'x-api-key: xxxx' https://api.wittyisland-cc57c95f.japaneast.azurecontainerapps.io/reports
[]
$ curl -H 'x-api-key: xxxx' https://api.wittyisland-cc57c95f.japaneast.azurecontainerapps.io/reports
[{"slug":"17dd4a5a-3b6b-4468-adfa-3c4c5e434228","title":"サンプルレポート","description":"動作確認用のレポート","status":"ready","visibility":"public","isPubcom":true,"createdAt":"2025-07-01T10:39:54.599708+00:00","tokenUsage":280860,"tokenUsageInput":260160,"tokenUsageOutput":20700,"estimatedCost":0.051444,"provider":"openai","model":"gpt-4o-mini"}]
$ 
```

### その他

特に、Azure 環境で 

```
make azure-update-deployment
```

を実行する際に、`scripts/fetch_reports.py` が実行されますが、その際に「限定公開」「非公開」状態のレポートがバックアップできないため、「公開」状態のレポートのみが復元されるという状態になっています。

<!-- 追加で伝えておきたいことがあれば記入してください -->

**コメント:** なし

---

### [[FEATURE] フォームから入力された API Key を使ってレポートを生成できる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/613)

**作成者:** shingo-ohki  
**作成日:** 2025-06-24T11:19:25Z  
**内容:**

# 背景
- 現状の広聴AIは、セットアップのためにある程度のテクニカルスキル(git, コマンドライン操作など)が必要であり、
利用にはこの部分が一定のハードルになっている。
- DD2030 のドメインで Azure 環境に動作確認やデモ環境を準備しようという動きがある。
- フォームから入力したAPI Key を使ってレポート生成ができるようになれば、上記のデモ環境でユーザーがセットアップ作業なしに広聴AIを試すことができる

# 提案内容
フォームから入力された API Key を使ってレポートを生成できるようにする

**コメント:** なし

---

### [[BUG] レポート編集、意見グループ編集を行うと、トークン使用量や推定コストが0になる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/584)

**作成者:** shingo-ohki  
**作成日:** 2025-05-29T12:25:46Z  
**内容:**

### 概要
タイトル通り

### 再現手順

1. Azure デプロイした環境でレポート生成する（このときトークン使用量、推定コストには値が入っている）
2. 生成したレポートの「レポート編集」「意見グループ編集」を行う
3.該当のレポートのトークン使用量、推定コストが 0 になる

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

#### 「レポート編集」「意見グループ編集」前
![Image](https://github.com/user-attachments/assets/015ccaed-61e2-406e-9616-93ce36ce9dfa)
#### 「レポート編集」「意見グループ編集」後
![Image](https://github.com/user-attachments/assets/ab1c1370-8944-48d8-b62d-d02abce87ccd)

### その他
個々の意見データから url を紐づけてリンクしていた場合、リンクも消える（スクリーンショット取り忘れました）

<!-- 追加で伝えておきたいことがあれば記入してください -->

**コメント:** なし

---

### [[BUG]セットアップ時の「requirements.txt」の追加の必要性(windows環境)](https://github.com/digitaldemocracy2030/kouchou-ai/issues/530)

**作成者:** neetfreeter  
**作成日:** 2025-05-17T16:58:15Z  
**内容:**

### 概要
windows環境でver2を初めてセットアップした際のエラー(ver1のセットアップは過去にあり)
requirements.txtが必要


●chatgptによる解決方法

✅ 今やるべきこと：requirements.txt が無い or azure 系が無い場合
server ディレクトリの中に requirements.txt がない or azure 関連が入っていないため、Dockerビルド時に Python モジュールが不足してクラッシュしています。

---
🛠 対処方法：server/requirements.txt を新規作成 or 追記

以下の内容を使って kouchou-ai/server/requirements.txt を新規作成するか、追記してください。
↓ここから
fastapi
uvicorn
pydantic
httpx
openai

# Azure Storage の依存
azure-core
azure-storage-blob

# その他の可能性あるもの
python-dotenv
↑ここまで
---

🧪 作成後にやること

PowerShell でルート（kouchou-ai/）に戻って以下を実行：

docker compose down
docker compose build --no-cache
docker compose up

これで api コンテナ内で ModuleNotFoundError: No module named 'azure' は解消されるはず。

---

✅ 追加で確認しておきたいこと
Dockerfile または docker-compose.yml 内で server/requirements.txt をインストールするステップがあるか

.env ファイルに最低限以下があるか：

OPENAI_API_KEY=sk-xxx...
ADMIN_API_KEY=admin-xxx
PUBLIC_API_KEY=public-xxx

---
🧾 回答の根拠
Python で Azure Blob Storage を使う場合、必ず azure-core / azure-storage-blob の pip モジュールが必要

ModuleNotFoundError: No module named 'azure' は requirements 未記載によるものがほとんど



---

🧩 回答に対する多角的な反証

1. FastAPIだけならazure不要じゃ？
　→ 広聴AIの report_launcher で Azure Blob を使ってる


2. requirements.txt 無くても Dockerfileで入れてるかも？
　→ 今回は ModuleNotFoundError 出ているため不足している

3. .env が未設定の可能性も？
　→ ただし azure モジュールのエラーが出てるのでまずそちらを優先

**コメント:** なし

---

### [[DOCUMENT] メンテナー向けのマージ基準についてドキュメント化する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/456)

**作成者:** nasuka  
**作成日:** 2025-05-07T12:02:40Z  
**内容:**

# 現在の問題点
何がクリアされていればマージしてよいのか、基準が明文化されていないため、レビュー時にメンテナーが判断に迷う場面がある

# 提案内容
以下を記載したガイドラインを作成する

* 何がクリアされていればOKか
* 何は妥協してよいのか/妥協してはよくないのか


**コメント:** なし

---

### [[FEATURE] 環境確認機能を作る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/400)

**作成者:** tokoroten  
**作成日:** 2025-04-30T05:13:14Z  
**内容:**

# 背景
OpenAIのAPIKeyが正しくセットされているのかどうかが、実際にレポートの作成を始めるまで分からない


# 提案内容
管理画面、クライアント画面に以下の機能を付けたい

管理画面
- APIサーバが生きているかどうか
- ~~OpenAIのkeyが正しいか~~ 、疎通できるかどうか（Azureも）
  - API Key の有効性の確認は、https://github.com/digitaldemocracy2030/kouchou-ai/pull/421 で対応済み
  - 以下の検証については未対応
    - 残高不足の確認
    - RateLimitの確認
- クライアント用のフロントサーバが立っているかどうか
- ローカルLLM用のLM Studioが生きているかどうか

## デザインの検討
#447 



**コメント:** なし

---

### [Devin とのうまい協働方法を考える](https://github.com/digitaldemocracy2030/kouchou-ai/issues/398)

**作成者:** shingo-ohki  
**作成日:** 2025-04-30T03:14:27Z  
**内容:**

（広聴AIに限った話ではないですが、一旦ここに）
# 現在の問題点
Devin が活用され始めたが、それによる弊害があるのではないか？
あるとすれば、それを軽減し、人間と Devin のうまい協働方法はないか？

あくまで仮説です

> Shingo OHKI
  今日 11:10
Devin が大活躍してくれるのは嬉しい反面、なんとなく人間がPRを出しにくくなりそうな気がするのですが、これは気のせいですかね。
>Shingo OHKI
  [29分前](https://w1740803485-clv347541.slack.com/archives/C08FL58M3D3/p1745980862512019?thread_ts=1745979009.909629&cid=C08FL58M3D3)
ChatGPT が少し言語化を手伝ってくれました（最初の回答の解決策にはピンと来ていませんが）
https://chatgpt.com/share/68118c77-ca60-800c-9998-987c5fe25f37
「AI導入による文化の摩擦」が起きている自然な状態です。
なるほど、成長痛なんですかね。
気にならない人も多いと思いますし、決して Devin 活用にブレーキを踏みたい訳ではないです（どちらかというと人間が気持ちよく Devin と協働できるうまい活用方法を探したい） （編集済み） 
>ChatGPTChatGPT
[ChatGPT - Devin 活用と参加感](https://chatgpt.com/share/68118c77-ca60-800c-9998-987c5fe25f37)
Shared via ChatGPT (9 kB)
https://chatgpt.com/share/68118c77-ca60-800c-9998-987c5fe25f37
>Shingo OHKI
>3. 「Devinタスクを投げる場所」を整備
[#devin部屋](https://w1740803485-clv347541.slack.com/archives/C08PRQVQWSE) を作ったのは正しそう
>NISHIO Hirokazu
>11:51
>2030年のデジタル民主主義を考える上で、そもそも2030年にはOSS開発の形がだいぶ変わってそう
誰もAIエージェントと一緒にOSS活動をしていくことの知見をもってないので、この場が世界最先端の実験場の一つとして日々いろいろな観測と考察が生まれていくのだと思う

<!-- 現在のコードの何が問題なのか、どのような技術的負債があるかを説明してください -->

# 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->


**コメント:** なし

---

### [管理画面の基本e2eテスト計画](https://github.com/digitaldemocracy2030/kouchou-ai/issues/396)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-30T01:43:59Z  
**内容:**

# 管理画面の基本e2eテスト計画

## テストの目的

このテストの目的は、ユーザーが管理画面にアクセスし、CSVファイルをアップロードして新しいレポートを作成するという基本的なワークフローが正常に機能することを確認することです。

## テストの前提条件

1. 管理画面にアクセスするための認証情報が設定されていること
2. テスト用のサンプルCSVファイルが用意されていること
3. APIレスポンスをモックするための設定が完了していること

## テストのステップ

### 1. 管理画面へのアクセスとログイン

- Basic認証を使用して管理画面にアクセス
- 管理画面のトップページが正しく表示されることを確認

### 2. レポート作成ページへの移動

- 「新しいレポートを作成する」ボタンをクリックしてレポート作成ページに移動
- ページタイトル「新しいレポートを作成する」が表示されることを確認

### 3. 基本情報の入力

- レポートIDフィールドに一意のIDを入力（例：`test-report-{timestamp}`）
- 質問フィールドにテスト用の質問を入力（例：「これはテスト質問です」）
- イントロダクションフィールドにテスト用の説明を入力（例：「これはテスト説明です」）

### 4. CSVファイルのアップロード

- CSVファイルタブが選択されていることを確認
- テスト用のサンプルCSVファイルをアップロード
- ファイルが正常にアップロードされ、ファイル名が表示されることを確認
- コメント列が自動的に選択されていることを確認（「comment」列がある場合）

### 5. レポート作成の実行

- 「レポート作成を開始」ボタンをクリックしてフォームを送信
- APIリクエストが正しいパラメータで送信されることを確認（モックAPIを使用）
- 成功メッセージが表示されることを確認
- ダッシュボードページにリダイレクトされることを確認

## モックの設定

テストでは以下のAPIエンドポイントをモックします：

1. レポート作成API（`/admin/reports`）
   - 成功レスポンス：`{ success: true, slug: 'test-report' }`

## テストコードの構造

テストコードは以下の構造で実装します：

```typescript
import { test } from '@playwright/test';
import { CreateReportPage } from '../../pages/admin/create-report';
import { setupBasicAuth } from '../../utils/auth';
import { mockReportCreation } from '../../utils/mock-api';

test.describe('レポート作成ページ', () => {
  test('CSVファイルをアップロードしてレポートを作成する', async ({ page }) => {
    // 認証設定
    await setupBasicAuth(page);
    
    // APIモック設定
    await mockReportCreation(page);
    
    // ページオブジェクトの初期化
    const createReportPage = new CreateReportPage(page);
    
    // レポート作成ページにアクセス
    await createReportPage.goto();
    
    // 基本情報の入力
    await createReportPage.fillBasicInfo(
      'test-report-' + Date.now(),
      'これはテスト質問です',
      'これはテスト説明です'
    );
    
    // CSVファイルのアップロード
    await createReportPage.uploadCsvFile('../../fixtures/sample.csv');
    
    // フォームの送信
    await createReportPage.submitForm();
    
    // リダイレクト先の確認
    await page.waitForURL('**/');
  });
});
```

## 実装上の注意点

1. テストの安定性を確保するため、固定のタイムアウト値ではなく、要素の表示を待つ方法を使用する
2. モックAPIレスポンスは実際のAPIレスポンスと同じ構造にする
3. テスト間の独立性を確保し、テスト順序に依存しないようにする
4. 既存のページオブジェクトとユーティリティを活用して効率的なテストを実装する

## 関連Issue

- #395 管理画面のe2eテスト拡張ケース（APIキーエラーやクレジット不足などのエラーケース）


**コメント:** なし

---

### [[FEATURE]ローカルLLM / embedding を利用できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/385)

**作成者:** nasuka  
**作成日:** 2025-04-29T03:57:58Z  
**内容:**

# 背景
* 現在はOpenAI/Azure OpenAI のLLMのみをサポートしているが、アカウント登録・契約のハードルがあり、利用できないユーザーがいる
* 特に個人のユーザーではなく、自治体などの組織においては最初のアカウント作成がボトルネックになるケースがある
  * 出力の品質は下がるが、ローカルLLMの出力でもある程度参考になるアウトプットを出せる可能性がある
    * また、どのようなアウトプットが出るのかイメージできると、本格導入の話も進みやすくなる


# 提案内容
* ローカルLLMおよびembeddingを利用できるようにする
  * 事前に実験を行ったうえで、利用するLLM/embeddingを選定する
    * 要件としては、[こちら](https://gist.github.com/nishio/469b5dc420c77b359ef43f3bdfb11526) に記載されているスペックのマシンで動作すると良さそう（メモリ16GB以内）
* UIとしては、管理画面の「AIモデル」のセレクトボックスにローカルLLMのモデル名を追加する 
  * embeddingの選択フォームは現状存在しないので新設する

![Image](https://github.com/user-attachments/assets/f1cbd478-be65-4dfa-93fb-f980e598c39f)

**コメント:** なし

---

### 過去7日間に作成されたissue (4件)

### [[FEATURE] スマホ環境では散布図と別ビューを提供する方針を検討する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/872)

**作成者:** nishio  
**作成日:** 2026-05-26T10:43:46Z  
**内容:**

## 背景

現状の散布図 UI は desktop / mouse hover 前提が強く、スマホ相当の狭い viewport では使い勝手がかなり落ちる。

直近の再観測では、以下が確認できた。

- `#121`: portrait では annotation は bounds 内に収まるが、249px 幅ラベルが画面に対して大きく、散布図の余白がかなり圧迫される
- `#121`: `390x844` portrait で tap 相当の操作をすると tooltip 幅が `363-366px` となり、plot 幅 `390px` の大半を覆って散布図を読み続けにくい
- `#283`: mobile-sized viewport 上で desktop hover を当てると、一般的なスマホ幅相当でも `fullScreenButtons` と hover text の overlap が起こりうる

このため、「散布図をスマホでもそのまま成立させる」方向だけでなく、**スマホ環境では別ビューを出す** 選択肢を検討したい。

## 検討したいこと

- スマホ判定時に、散布図の代わりに別ビューを既定表示するか
- 別ビュー候補として何が良いか
  - 画像化した散布図（インタラクティブ性なし）
  - クラスタ一覧 + 要約文 + 件数のカード表示
  - 階層一覧ビュー
  - 上位クラスタだけの簡略図 + 詳細はリスト
- 「スマホでは散布図を隠す」のではなく、明示的に切り替え可能な導線を残すか
- viewport 幅だけで切るか、pointer/coarse など入力デバイス特性でも切るか
- public-viewer の report schema / build pipeline に、モバイル専用アセット（画像など）を追加する必要があるか

## 期待する成果

- スマホ環境での既定表示方針を決める
- 既存散布図の responsive 調整だけで粘るのか、モバイル専用ビューを導入するのかを決める
- 実装に入るなら、最初の最小スコープ（例: スマホでは静的画像 + クラスタ一覧を出す）を切る

## 関連 Issue

- `#121` [BUG] 縦長画面での散布図の表示がおかしい
- `#283` [BUG] ScatterChart の全画面表示で要約文が「全画面終了」ボタンの後ろに隠れないようにする処理が不安定
- `#266` [FEATURE] クラスタ数が増えた場合に散布図上でクラスタラベルが被ってしまう
- `#52` [FEATURE] チャート表示に連動した文章表示

## メモ

スマホでの使いづらさは、`#121` や `#283` の局所修正だけでは消えない可能性が高い。desktop と同じ可視化責務を mobile にそのまま持ち込むのではなく、**mobile では情報の見せ方を変える** 前提で設計し直した方がよいかもしれない。


**コメント:** なし

---

### [[REFACTOR] fetch_reports.py を migration / 緊急救済専用へ降格し、通常運用から外す](https://github.com/digitaldemocracy2030/kouchou-ai/issues/870)

**作成者:** nishio  
**作成日:** 2026-05-26T06:35:56Z  
**内容:**

## 背景

`tools/scripts/fetch_reports.py` は、ストレージ機能が無かった頃に「サーバをアップデートしたらローカルのレポートが消える」問題を回避するために入った退避策としては理解できます。

ただし current main では、生成後の成果物は `ReportSyncService` で Azure Blob Storage に同期され、起動時も `initialize_from_storage()` で復元する設計が本線です。この状態で `fetch_reports.py` を通常運用の safety net として残すと、設計上の canonical store が API scrape なのか Blob なのか曖昧になります。

## 現在の問題

- script の責務が「通常運用の backup」なのか「migration / 緊急救済」なのか曖昧
- current implementation は `PUBLIC_API_KEY` + public `/reports` 前提で、private / unlisted を扱えない
- workflow / docs に残っていると、Blob sync / restore 本線より script の方が重要に見えてしまう

## やりたいこと

`fetch_reports.py` を通常の deploy / update 手順から外し、migration または緊急救済時だけ使う補助ツールとして位置づけ直す。

## 受け入れ条件

- `fetch_reports.py` が通常の Azure deploy / update workflow の必須手順から外れている
- script を残す場合は、用途が migration / 緊急救済であることが docs / help text で明記されている
- 現行 contract で public reports しか取れないなら、その制約が明記されている
- もし private / unlisted も取れるように残す方針なら、public endpoint 依存ではない別実装方針が整理されている

## 関連

- 旧 issue: #629
- deploy safety 側の再設計: 別 issue で Blob Storage health check へ切り替えを扱う


**コメント:** なし

---

### [[BUG] Azure deploy の safety を fetch_reports 依存から Blob Storage health check に切り替える](https://github.com/digitaldemocracy2030/kouchou-ai/issues/871)

**作成者:** nishio  
**作成日:** 2026-05-26T06:35:56Z  
**内容:**

## 背景

現状の `.github/workflows/azure-deploy.yml` は deploy 前に `python3 tools/scripts/fetch_reports.py --api-url https://$API_DOMAIN` を実行し、既存 API からレポートを吸い出してから image build に進んでいます。

しかし current main では、レポート生成後の成果物は `ReportSyncService` により Azure Blob Storage に同期され、起動時も `initialize_from_storage()` で Blob から復元する構成が本線になっています。にもかかわらず deploy workflow だけが、ストレージ機能が無かった頃の `fetch_reports.py` ベースの退避策に依存したままです。

その結果、限定公開・非公開レポートを含む current contract と workflow の前提がずれています。

## 現在の問題

- `tools/scripts/fetch_reports.py` は `PUBLIC_API_KEY` で public `/reports` を読むだけなので、private / unlisted を backup できない
- current の canonical backing store は API scrape ではなく Azure Blob sync / restore 側
- deploy の安全性確認が「API から見えている public reports を吸い出せるか」に寄っており、本来確認したい storage の健全性を見ていない

## やりたいこと

Azure deploy の pre-check / safety を `fetch_reports.py` 依存から切り離し、Blob Storage が current report artifacts を read/write できることを軽く確認する health check に置き換える。

## 受け入れ条件

- `.github/workflows/azure-deploy.yml` で deploy 前に `fetch_reports.py` を常設バックアップ手段として実行しない
- 代わりに、Azure Blob Storage に対して最低限の read/write を確認する health check がある
- 可能なら `report_status.json` または report artifact の read-back も確認対象に含める
- private / unlisted report の visibility に依存せず deploy safety を評価できる
- なぜ API scrape ではなく Blob health check を deploy safety の基準にするのか docs / issue 上で説明されている

## 関連

- 旧 issue: #629
- `fetch_reports.py` の位置づけ整理: developer-wiki の `fetch-reports-deprecation-and-storage-health-2026-05-26`


**コメント:** なし

---

### [[analysis-core] label refinement PR化までの残作業整理](https://github.com/digitaldemocracy2030/kouchou-ai/issues/869)

**作成者:** nishio  
**作成日:** 2026-05-25T10:24:00Z  
**内容:**

## 背景

実験差分から、先に以下を独立 PR として切り出しました。

- #866: LLM grouping 分析モード
- #867: `--reuse-from`
- #868: 実行時 user API key plumbing

残りの WIP は退避ブランチ `codex/remaining-experiment-wip` に snapshot しました。

- commit: `47008bc` `Snapshot remaining experiment work`
- 目的: 残り作業を失わないための退避。PR そのものではない。
- 注意: 生成 outputs と実験用 config は commit していない。企業名由来の旧 prefix を含むローカルファイルも、そのまま PR に含めない。

## 目的

label refinement を、他の実験差分と混ぜずに PR 化できる状態へ整理する。

## 残作業

- #866 / #867 / #868 の merge 後、またはそれらを前提にした clean worktree 上で label refinement だけを再構成する。
- 既に切り出した LLM grouping / `--reuse-from` / user API key plumbing を label refinement PR に再混入させない。
- 実験用 config / generated outputs / judge 結果 JSON を PR から外す。必要な fixture だけ最小化して、旧 prefix も使わない名前にする。
- `hierarchical_label_refinement` の public contract を決める。
  - default は `mode = none` のままでよいか。
  - `setwise_refine` / `setwise_refine_short` / prompt variant のうち、PR に入れる mode をどこまでにするか。
  - `hierarchical_merge_labels.csv` を上書きする設計でよいか、`hierarchical_refined_labels.csv` を downstream artifact として渡す設計に寄せるか。
  - `hierarchical_merge_labels.original.csv` を永続 artifact として残すか。
- #868 の `user_api_key` plumbing が refinement step まで届くことを regression test で確認する。
- test coverage を label refinement に限定して整える。
  - step unit test
  - plugin adapter test
  - workflow/spec/orchestration test
  - prompt default test
  - full `packages/analysis-core` pytest
- PR body では「label refinement は label set の見出し編集であり、grouping 本体とは別」と明記する。

## 完了条件

- label refinement だけを含む draft PR が作られている。
- 生成 outputs と実験用 config が含まれていない。
- 企業名由来の旧 prefix が新規 PR 差分に出ない。
- `packages/analysis-core` の ruff と pytest が通っている。

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(5件)

### [[BUG] main ブランチへのマージ時に実行される Azure への deploy が失敗する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/741)

**作成者:** shingo-ohki  
**作成日:** 2025-12-27T14:53:28Z  
**内容:**

### 概要

表題通り。

- 失敗したときの事例
https://github.com/digitaldemocracy2030/kouchou-ai/actions/runs/20540103407/attempts/1

- リトライで直った
https://github.com/digitaldemocracy2030/kouchou-ai/actions/runs/20540103407

### 再現手順

1. main ブランチに更新を入れる
2. GitHub Actions で Azure への deploy 処理が動く
3. たまに失敗する

### 期待する動作

毎回 deploy が成功する
<!-- 本来どう動作すべきかを記入してください -->

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

### その他

AIによると、原因はこんな感じ
```
発生箇所: Azure デプロイの Docker ビルド中、client イメージの Dockerfile:14 の RUN npm ci で npm ERR! code ECONNRESET により失敗。内容は npm レジストリへの接続リセットで、依存関係の不整合ではありません。
文脈: azure-deploy.yml:53-90 で API/client/client-admin/client-static-build の 4 イメージを並列ビルド。複数の npm ci が同時に走るため、GitHub ホストランナー上でレジストリへの接続がまれに途切れる典型的なネットワーク起因の失敗です。
他のステージ (Python 依存、client-admin ビルドなど) は完走しており、恒常的な依存問題ではなく一時的な接続切れが原因と考えられます。

対応案（優先度順）

1. まずはリトライ実行: ワークフローを再実行すれば通る可能性が高いです。
2. npm ci にリトライとタイムアウトを付与 (各 Dockerfile の npm 実行直前で):
例: npm config set fetch-retries 5 && npm config set fetch-retry-mintimeout 20000 && npm config set fetch-retry-maxtimeout 120000 && npm config set registry https://registry.npmjs.org/
あるいは npm ci --fetch-retries=5 --fetch-retry-mintimeout=20000 --fetch-retry-maxtimeout=120000 --network-timeout=600000
対象: Dockerfile:14, Dockerfile:17, Dockerfile:5 と同ファイル内 2 回目の npm ci.
3. 並列度を下げる: ワークフローで Docker ビルドを直列にする、または client 系をまとめて後段にずらすことでレジストリへの同時接続を減らす。
4. npm キャッシュ活用: Docker BuildKit のキャッシュマウントや npm ci --cache /tmp/npm-cache を併用し、外部アクセス回数を削減。
まずは 1) を試し、再発するようなら 2) を反映、それでも改善しなければ 3)/4) を検討するのが現実的です。
```

**コメント:** なし

---

### [[BUG] Windows環境でインストールしようとすると文字化けが発生して中断する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/731)

**作成者:** Puni-Pon  
**作成日:** 2025-11-23T10:05:48Z  
**内容:**

### 概要

Windows環境でインストールしようとすると文字化けが発生して中断する

### 再現手順

1. 配布ファイルをダウンロード
2. Dockerを起動
3. setup_win.batを実行

### 期待する動作

APIを入力するとビルドがはじまり、管理画面にアクセスできるようになる

### スクリーンショット・ログ

```
kouchou-ai-3.0.0>echo Kouchou-AI Setup Tool
Kouchou-AI Setup Tool
kouchou-ai-3.0.0>echo =====================
=====================
kouchou-ai-3.0.0>REM Check if Docker Desktop is running
kouchou-ai-3.0.0>docker info  1>nul 2>&1
kouchou-ai-3.0.0>if 0 NEQ 0 (
echo Docker Desktop is not running.
 echo Please start Docker Desktop and try again.
 echo 豕ｨ諢・ Docker縺ｮ繧､繝ｳ繧ｹ繝医・繝ｫ逶ｴ蠕後・蜀崎ｵｷ蜍輔′蠢・ｦ√↑蝣ｴ蜷医′縺ゅｊ縺ｾ縺吶・
 pause
 exit /b
)
kouchou-ai-3.0.0>REM Enter OpenAI API key
kouchou-ai-3.0.0>echo OpenAI API繧ｭ繝ｼ繧貞・蜉帙＠縺ｦ縺上□縺輔＞縲・
OpenAI API繧ｭ繝ｼ繧貞・蜉帙＠縺ｦ縺上□縺輔＞縲・
kouchou-ai-3.0.0>∝承繧ｯ繝ｪ繝・け縺励※縲瑚ｲｼ繧贋ｻ倥￠縲阪ｒ驕ｸ謚槭＠縺ｦ縺上□縺輔＞縲・
'∝承繧ｯ繝ｪ繝・け縺励※縲瑚ｲｼ繧贋ｻ倥￠縲阪ｒ驕ｸ謚槭＠縺ｦ縺上□縺輔＞縲・' は、内部コマンドまたは外部コマンド、
操作可能なプログラムまたはバッチ ファイルとして認識されていません。
kouchou-ai-3.0.0>set /p OPENAI_API_KEY=Enter your OpenAI API key:
Enter your OpenAI API key:
```

APIキーを入力しても以下の表示になり強制終了

```
kouchou-ai-3.0.0>if 0 NEQ 0 (
echo 隴ｦ蜻・ 蜈･蜉帙＆繧後◆API繧ｭ繝ｼ縺ｮ蠖｢蠑上′豁｣縺励￥縺ｪ縺・庄閭ｽ諤ｧ縺後≠繧翫∪縺吶・
 ｼ縺ｯ縲茎k-縲阪〒蟋九∪繧翫∪縺吶・
 陦後＠縺ｾ縺吶°・・(Y/N
)

kouchou-ai-3.0.0>set /p CONTINUE=
```

### その他

WSL越しにsetup_linux.shを使って手順通りにセットアップすることで、Windows環境でも広聴aiの起動には成功しました。
ノンエンジニア向けにWindows環境でも使えるようにする、という目的を踏まえると、「setup_win.batを改修する」というアプローチのほかにも「WSLのインストールを促す」というアプローチも考えられるかなとは思います。

**コメント:** なし

---

### [[BUG] Clientの意見の説明が禁則処理ができていない](https://github.com/digitaldemocracy2030/kouchou-ai/issues/478)

**作成者:** tokoroten  
**作成日:** 2025-05-11T05:10:48Z  
**内容:**

### 概要

Plotlyの内部はSVGであり、SVGにおける改行はユーザが自前で行わなければならない。

現在は、30文字ごとに機械的に改行を差し込んでいるので、禁則処理に失敗するケースがある

https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/client/components/charts/ScatterChart.tsx#L81
> `<b>${cluster.label}</b><br>${arg.argument.replace(/(.{30})/g, "$1<br />")}`,

![image](https://github.com/user-attachments/assets/0ca3f6b2-c155-4cc1-954f-67019d41d13b)

### 期待する動作

禁則処理がうまく動いていること

### その他

禁則処理は以下を参照
https://ja.wikipedia.org/wiki/%E7%A6%81%E5%89%87%E5%87%A6%E7%90%86


**コメント:** なし

---

### [[BUG]ScatterChartの全画面表示で要約文が「全画面終了」ボタンの後ろに隠れないようにする処理が不安定](https://github.com/digitaldemocracy2030/kouchou-ai/issues/283)

**作成者:** masatosasano2  
**作成日:** 2025-04-12T18:36:39Z  
**内容:**

### 概要
Issue #278 が PR #282 で修正されたが、以下の課題が残ったため本Issueに切り出された。

PR #282 の修正内容
![Image](https://github.com/user-attachments/assets/a7a1bd58-febe-4993-a49a-2612b1c90ec9)

残課題
![Image](https://github.com/user-attachments/assets/3d080c1d-1502-4b09-8aca-fb2c1fdb9e52)

### 再現手順

1. 「全体図」または「濃い意見グループ」モードを選択する
2. 「全画面表示」ボタンを押す
3. ブラウザのサイズを極力小さくする
4. 画面上部の、右端より少し左側あたりでマウスを動かし続ける

### 期待する動作

要約文が「全画面終了」ボタンの後ろに隠れない（正確には、隠れたままにならない）ようにする


**コメント:** なし

---

### [[BUG]縦長画面での散布図の表示がおかしい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/121)

**作成者:** nishio  
**作成日:** 2025-03-21T15:32:58Z  
**内容:**

### 概要

<img width="453" alt="Image" src="https://github.com/user-attachments/assets/c20dbff2-454c-4b23-bf8b-973bcc6c96fd" />


横長の時の表示:
<img width="1512" alt="Image" src="https://github.com/user-attachments/assets/1b7a062a-5413-4d24-b5f3-91cb81059d07" />

<!-- バグの簡潔な説明をお願いします -->

### 再現手順

1. 縦長画面で見る

### 期待する動作

- 理論的な理想を言うと、そもそもアスペクト比は1:1であるべき
- 一方でそれにこだわって徹底した場合にみやすさが損なわれるのも問題がある
- 縦長画面で見た場合はラベルの幅との干渉でアスペクト比が大きく狂っているのでそこだけでも直すか？

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (19件)

### [[codex] legacy pipeline と refactoring phase docs を cleanup](https://github.com/digitaldemocracy2030/kouchou-ai/pull/865)

**作成者:** nishio  
**作成日:** 2026-05-23T12:57:58Z  
**変更:** +96 -4428 (32ファイル)  
**マージ日:** 2026-05-23T15:03:37Z  
**内容:**

## 概要
- `apps/api/broadlistening/pipeline` に残っていた legacy Python 実装を削除
- `docs/refactoring` の phase planning artifacts を source repo から除去
- API / tests / docs / skill を `analysis_core` 前提の current path に更新

## 変更内容
- 削除:
  - `apps/api/broadlistening/pipeline/hierarchical_main.py`
  - `apps/api/broadlistening/pipeline/hierarchical_utils.py`
  - `apps/api/broadlistening/pipeline/services/*`
  - `apps/api/broadlistening/pipeline/steps/*`
  - `docs/refactoring/phase0_investigation.md`
  - `docs/refactoring/phase2_5_plan.md`
  - `docs/refactoring/phase3_plan.md`
- 更新:
  - `apps/api/src/routers/admin_report.py` の API key verify が `analysis_core.services.llm` を参照するよう修正
  - 旧 pipeline service を参照していた API / experiment / test を `analysis_core` へ移行
  - `skills/kouchou-ai-architecture/SKILL.md` と `apps/api/broadlistening/README.md` を current architecture に合わせて整理
  - `report.html` の説明を `CLI ローカル確認用 HTML` に統一
  - `apps/api/pyproject.toml` から legacy file 向け Ruff 例外を削除

## 背景
`analysis-core` / workflow が canonical path になったあとも、deprecated な旧 pipeline 実装と planning artifact が source tree に残っていました。
今回の cleanup で、「current に使うコード」と「歴史として Wiki に残すもの」を分けます。

## 影響
- API の current 実行経路は変わりません。`report_launcher.py` は引き続き `python -m analysis_core` を起動します。
- `apps/api/broadlistening/pipeline/` は runtime data (`configs`, `inputs`, `outputs`) の置き場としては残ります。
- `report.html` は引き続き CLI 側だけで使うローカル確認用 HTML で、Web canonical artifact にはしません。

## テスト
- `ruff check src/routers/admin_report.py tests/services/test_llm.py tests/services/test_parse_json_list.py tests/routers/test_admin_report.py tests/services/test_report_sync.py`
- `ENV_FILE=.env.test uv run --with pytest --with pytest-asyncio --with pytest-cov --with-editable ../../packages/analysis-core pytest tests/services/test_llm.py tests/services/test_parse_json_list.py tests/routers/test_admin_report.py tests/services/test_report_sync.py -q`


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Refactor**
  * Consolidated pipeline execution through the analysis-core package; deprecated internal pipeline modules removed to streamline architecture.
  * Updated import paths for shared analysis services.

* **Documentation**
  * Clarified that `hierarchical_result.json` is the canonical pipeline output for distribution.
  * Clarified that `report.html` is a local helper artifact for preview purposes only, not for sharing.
  * Updated quickstart and architecture guides to reflect the current execution flow.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/865?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[codex] report_launcher の subprocess smoke と path cleanup を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/864)

**作成者:** nishio  
**作成日:** 2026-05-23T04:41:04Z  
**変更:** +747 -85 (12ファイル)  
**マージ日:** 2026-05-23T12:34:23Z  
**内容:**

## 変更内容
- `apps/api -> subprocess -> analysis_core` の境界を本物の subprocess で踏む manual smoke test を追加
- その smoke を、通常の `launch_report_generation()` フロー全体まで拡張し、`hierarchical_result.json`、`hierarchical_status.json`、`report_status.json` まで確認
- workflow plugin から legacy step へ渡す input/output path の配線を修正し、相対 `inputs/` / `outputs/` に落ちないようにした
- 共通の legacy config 組み立てを `_legacy_config.py` に集約し、extraction の path 解決に regression test を追加

## 背景
- 既存 repo には `analysis-core` 単体の e2e と、API 側の mock ベース service test はあったが、本番で使っている `apps/api -> subprocess -> analysis_core` の境界を手元で再現可能な形で踏むテストがなかった
- 通常フロー smoke を追加して初めて、workflow plugin 側が `--input-dir` / `--output-dir` を十分に legacy step へ渡しておらず、cwd 相対の `inputs/` / `outputs/` に依存していることが分かった
- path 修正を個別 plugin に散らしたままにすると再発しやすいため、共通化と回帰テストまで同じ PR に含めた

## 影響
- launcher や workflow path を触る変更の前に、production に近い API 実行経路を手元で 1 回踏めるようになる
- workflow 経由の実行でも、設定された report/input directory をより一貫して尊重するようになる
- extraction plugin について、comments artifact を使った path 解決の regression coverage が追加される

## 根本原因
workflow plugin 層が、解決済みの input/output base dir を legacy step 関数へ一貫して渡していなかった。そのため、API からの実 subprocess 実行でも `inputs/<slug>.csv` を current working directory 基準で探してしまう経路が残っていた。

## 動作確認
- `cd packages/analysis-core && ./.venv/bin/ruff check src/analysis_core/plugins/builtin tests/test_builtin_plugins.py`
- `cd packages/analysis-core && ./.venv/bin/pytest tests/test_builtin_plugins.py tests/test_workflow_engine.py -q`
- `cd apps/api && ADMIN_API_KEY=dummy PUBLIC_API_KEY=dummy OPENAI_API_KEY=dummy ./.venv/bin/pytest tests/services/test_report_launcher.py -q`
- `cd apps/api && ADMIN_API_KEY=dummy PUBLIC_API_KEY=dummy OPENAI_API_KEY=dummy ./.venv/bin/pytest tests/manual/report_launcher_subprocess_smoke.py -q -s`

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Added a manual smoke-testing capability to validate end-to-end report generation with a simulated local LLM to ensure subprocess-driven workflows produce expected outputs.

* **Tests**
  * Added manual smoke tests covering full report generation and aggregation flows.
  * Added regression tests verifying extraction step input selection and artifact outputs.

* **Refactor**
  * Consolidated legacy runtime configuration construction across multiple plugins; now includes consistent input location resolution and token-usage tracking.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/864?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[codex] Windows setup の実機 E2E と軽量 CI を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/862)

**作成者:** nishio  
**作成日:** 2026-05-22T12:43:25Z  
**変更:** +502 -72 (8ファイル)  
**マージ日:** 2026-05-22T14:15:14Z  
**内容:**

## 概要

- `setup_win.bat` に CI / self-hosted runner 向けの非対話モードを追加しました
- `windows-latest` で文字コード、Docker 未起動時の停止パス、`.env` 生成を確認する軽量 regression workflow を追加しました
- `kouchou-ai-e2e` ラベル付き self-hosted Windows runner で `setup_win.bat` + Docker Desktop の実機 E2E を走らせる workflow を追加しました
- Windows 実機セットアップ検証手順を docs に追加し、Windows セットアップガイドと MkDocs nav から辿れるようにしました

## 背景

Fixes #860

Issue コメントの方針に合わせて、単なるドキュメント化ではなく、以下の層に分けました。

- Hosted Windows: `setup_win.bat` の文字化け・構文・入力分岐・`.env` 生成を検出
- Self-hosted Windows: Docker Desktop + Linux containers で実セットアップ E2E
- Docs: 人間 / AI エージェントが実機で再実行する観測手順

## 確認

- `setup_win.bat --non-interactive --skip-docker-start --openai-api-key sk-test --gemini-api-key AIza-test` が exit 0 で `.env` を生成することを確認
- `setup_win.bat --non-interactive` が Docker 未起動時に exit 1 で停止することを確認
- `rg -n "[^\x00-\x7F]" setup_win.bat .github/workflows/windows-setup-script.yml` で ASCII-only を確認
- `python -m mkdocs build --strict`
- workflow YAML parse 確認
- `git diff --check`

## 補足

この PR 作成時点で、Windows 実機側に self-hosted runner は起動済みです。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Added automated Windows real-machine E2E workflow (manual trigger, environment checks, startup/wait/logging)
  * Introduced non‑interactive Windows setup with API key flags and optional Docker start/validation

* **Documentation**
  * Added comprehensive Windows real‑machine setup verification guide
  * Updated Windows setup guide to reference verification procedure

* **Chores**
  * Added Windows setup script validation workflow
  * Ensured runtime images include shared package contents

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/862?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [散布図の source link クリックが modebar に阻害される問題を修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/857)

**作成者:** nishio  
**作成日:** 2026-05-22T10:09:45Z  
**変更:** +106 -27 (2ファイル)  
**マージ日:** 2026-05-22T10:20:08Z  
**内容:**

## 概要
散布図で source link を有効にしている時、`displayModeBar: "hover"` の modebar overlay が点クリックを奪い、リンク先を開けない問題を修正します。

## 変更内容
- `ScatterChart` の DOM override を helper 化
- hover modebar の container を `pointer-events: none`、実 toolbar のみ `pointer-events: auto` にして、点クリックを妨げないように変更
- fullscreen ボタンとの重なり回避ロジックは維持
- ScatterChart の DOM helper に対する unit test を追加

## 確認
- `pnpm --filter @kouchou-ai/public-viewer test -- --runInBand components/charts/__tests__/ScatterChart.test.ts`
- `pnpm exec biome check apps/public-viewer/components/charts/ScatterChart.tsx apps/public-viewer/components/charts/__tests__/ScatterChart.test.ts`

Closes #710


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## Release Notes

* **Bug Fixes**
  * Fixed scatter chart modebar positioning to prevent overlap with adjacent UI elements.
  * Improved event listener cleanup and management for better reliability.

* **Tests**
  * Added comprehensive test coverage for scatter chart DOM interactions and positioning adjustments.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/857?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [legacy report_status の slug 欠落を吸収する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/856)

**作成者:** nishio  
**作成日:** 2026-05-22T09:05:49Z  
**変更:** +44 -0 (2ファイル)  
**マージ日:** 2026-05-22T09:10:28Z  
**内容:**

## 概要
legacy な `report_status.json` に `slug` フィールドが無い場合でも、レポート一覧取得で落ちないようにします。

## 変更内容
- `convert_old_format_status()` で `slug` 欠落時は status key から補完
- 一覧読み出し (`load_status_as_reports`) で legacy データを読めることをテスト追加
- `is_public` → `visibility` の既存 migration 互換コードと同じ層で吸収

## 確認
- `uv run --project apps/api ruff check apps/api/src/services/report_status.py apps/api/tests/services/test_report_status.py`
- `ADMIN_API_KEY=test PUBLIC_API_KEY=test OPENAI_API_KEY=test apps/api/.venv/bin/python -m pytest apps/api/tests/services/test_report_status.py`

Closes #740


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Improved legacy report format conversion to ensure all required identifying information is properly populated when migrating report data from older formats.

* **Tests**
  * Added comprehensive test coverage for format conversion, including validation of identifying field handling and status assignment during legacy data transformation.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/856?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [reuse画面の Biome warning を解消する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/855)

**作成者:** nishio  
**作成日:** 2026-05-22T05:16:57Z  
**変更:** +41 -38 (1ファイル)  
**マージ日:** 2026-05-22T06:37:35Z  
**内容:**

## 概要
`apps/admin/app/reuse/[slug]/page.tsx` の既存 Biome warning を解消します。

## 変更内容
- import 順を Biome の期待に合わせて整理
- 設定反映処理を `useEffectEvent` に切り出し
- `slug` 変更時の設定ロード effect から mutable handler 群を分離し、`useExhaustiveDependencies` warning を解消

## 確認
- `pnpm exec biome check 'apps/admin/app/reuse/[slug]/page.tsx'`
- `pnpm --filter @kouchou-ai/admin test -- --runInBand 'app/create/components/EnvironmentCheckDialog/EnvironmentCheckDialog.test.tsx'`


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Refactor**
  * Improved configuration synchronization in the admin reuse page so loaded settings are applied consistently across the UI — including AI provider and model selections, worker and cluster-level settings, prompt fields, and source-link preferences — reducing state mismatch and improving reliability when switching or loading reuse configurations.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/855?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [API テストの重複 mock/fixture を整理する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/854)

**作成者:** nishio  
**作成日:** 2026-05-22T05:06:56Z  
**変更:** +105 -265 (2ファイル)  
**マージ日:** 2026-05-22T05:42:36Z  
**内容:**

## 概要
API テストで繰り返していた subprocess / status JSON のモックを共通 helper に寄せ、fixture 重複を減らします。

## 変更内容
- `test_report_launcher.py` に `make_report_input()` と `patch_subprocess_launch()` を追加
- report launcher 系テストで重複していた `DummyPopen` / `DummyThread` / `ReportInput` 構築を共通化
- `test_get_current_step.py` に `mock_status_response()` を追加
- status JSON 読み出しテストで重複していた `Path` / `open` / `json.load` モックを共通化

## 確認
- `ADMIN_API_KEY=test PUBLIC_API_KEY=test OPENAI_API_KEY=test apps/api/.venv/bin/python -m pytest apps/api/tests/services/test_report_launcher.py apps/api/tests/routers/test_get_current_step.py`
- `uv run --project apps/api ruff check apps/api/tests/services/test_report_launcher.py apps/api/tests/routers/test_get_current_step.py`

Closes #842


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Tests**
  * Improved test infrastructure with reusable mocking utilities to reduce code duplication and enhance test maintainability.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/854?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [ユーザー入力 API キーでも接続チェックできるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/853)

**作成者:** nishio  
**作成日:** 2026-05-22T04:51:53Z  
**変更:** +90 -20 (8ファイル)  
**マージ日:** 2026-05-22T05:42:49Z  
**内容:**

## 概要
- 環境確認ダイアログの API 接続チェックでも、ユーザーが入力した API キーを使えるようにしました
- `x-user-api-key` を `/admin/environment/verify` へ渡し、backend 側で `request_to_chat_ai(..., user_api_key=...)` に接続しました
- create / reuse の両画面から同じ挙動になるように揃えました

## 背景
Issue #681 の通り、現状の API 接続チェックはサーバー側の環境変数に入っている API キーしか確認できず、画面上で入力した独自 API キーの有効性は事前確認できませんでした。

この PR では、実際のレポート生成時と同じ `x-user-api-key` 経路を環境確認ダイアログにも通し、ユーザー入力 API キーの接続チェックができるようにしています。

Closes #681

## 変更内容
- `apps/api/src/routers/admin_report.py`
  - `/admin/environment/verify` で `x-user-api-key` を受け取り、LLM verify 呼び出しへ渡す
- `apps/admin/app/create/components/EnvironmentCheckDialog/*`
  - `verifyApiKey()` が `x-user-api-key` を送れるように変更
  - `EnvironmentCheckDialog` に `userApiKey` prop を追加
- `apps/admin/app/create/page.tsx`
- `apps/admin/app/reuse/[slug]/page.tsx`
  - AI 設定で入力した API キーを接続チェックダイアログへ渡す

## 動作確認
- `pnpm --filter @kouchou-ai/admin test -- --runInBand app/create/components/EnvironmentCheckDialog/verifyApiKey.test.ts app/create/components/EnvironmentCheckDialog/EnvironmentCheckDialog.test.tsx`
- `ADMIN_API_KEY=test PUBLIC_API_KEY=test OPENAI_API_KEY=test apps/api/.venv/bin/python -m pytest apps/api/tests/routers/test_admin_report.py`
- `pnpm exec biome check apps/admin/app/create/components/EnvironmentCheckDialog/verifyApiKey.ts apps/admin/app/create/components/EnvironmentCheckDialog/EnvironmentCheckDialog.tsx apps/admin/app/create/components/EnvironmentCheckDialog/verifyApiKey.test.ts apps/admin/app/create/components/EnvironmentCheckDialog/EnvironmentCheckDialog.test.tsx apps/admin/app/create/page.tsx`

## 補足
- `apps/admin/app/reuse/[slug]/page.tsx` には今回差分と無関係の既存 `useExhaustiveDependencies` 警告があるため、この PR ではそこまでは解消していません

## CLAへの同意
- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Added support for custom API key verification. Users can now provide their own API keys during environment verification in report creation and management workflows, enabling validation with user-specific credentials instead of relying solely on provider defaults.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/853?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [管理画面でレポート生成失敗時のエラーログを確認できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/852)

**作成者:** nishio  
**作成日:** 2026-05-21T15:51:46Z  
**変更:** +436 -120 (8ファイル)  
**マージ日:** 2026-05-21T16:27:54Z  
**内容:**

## 概要
- closes #716
- レポート生成失敗時に、管理画面から失敗理由と実行ログの抜粋を確認できるようにします
- analysis-core 実行ログを各レポート配下に保存し、API 経由で admin UI に表示します

## 変更内容
- `apps/api/src/services/report_launcher.py`
  - `analysis.log` を各レポート配下に保存するよう変更
  - subprocess が non-zero exit した時に `hierarchical_status.json` へ `error` / `error_log_path` / `error_log_excerpt` を補完
- `apps/api/src/routers/admin_report.py`
  - `/admin/reports/{slug}/status/step-json` が `error_message` と `error_log_excerpt` を返すよう変更
- `apps/admin/app/_components/ReportCard/ProgressSteps/*`
  - polling hook で error detail を保持
  - 進捗表示の下にエラーメッセージとログ抜粋を表示

## 確認
- `pnpm --filter @kouchou-ai/admin test -- --runInBand apps/admin/app/_components/ReportCard/ProgressSteps/useReportProgressPolling.test.ts`
- `cd apps/api && set -a && source .env.test && set +a && .venv/bin/python -m pytest tests/routers/test_get_current_step.py tests/services/test_report_launcher.py`
- `cd apps/api && uv run ruff check src/routers/admin_report.py src/services/report_launcher.py tests/routers/test_get_current_step.py tests/services/test_report_launcher.py`
- `pnpm exec biome check apps/admin/app/_components/ReportCard/ProgressSteps/ProgressSteps.tsx apps/admin/app/_components/ReportCard/ProgressSteps/useReportProgressPolling.ts apps/admin/app/_components/ReportCard/ProgressSteps/useReportProgressPolling.test.ts`

## 補足
- まずは失敗時にユーザーが状況を把握できることを優先し、Web UI ではログ全文ではなく抜粋を表示しています
- reviewer request はまだ送っていません


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Enhanced error reporting: user-facing error messages and truncated log excerpts are shown when report generation fails.
  * Improved progress UI: progress tracker displays a clearer error panel with message and log snippet when applicable.
  * Consistent failure messaging: a clearer user-facing error text is shown after retries are exhausted.

* **Tests**
  * Extended test coverage for error response fields, log excerpt handling, and error UI/display.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/852?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Azure deploy で shared CSP helper を取り込む](https://github.com/digitaldemocracy2030/kouchou-ai/pull/851)

**作成者:** nishio  
**作成日:** 2026-05-21T14:27:47Z  
**変更:** +2 -0 (2ファイル)  
**マージ日:** 2026-05-21T14:42:30Z  
**内容:**

## 概要

`Azure Deployment` が `main` push で失敗していたため、web app Docker build に `apps/shared` を含めるようにします。

## 原因

`#848` で `apps/admin/next.config.ts` と `apps/public-viewer/next.config.ts` が `../shared/csp` を import するようになりましたが、各 Dockerfile の builder stage が `apps/shared` を copy していませんでした。

そのため Azure deploy の admin image build 中に `next build` が `Cannot find module ../shared/csp` で落ちていました。

## 変更内容

- `apps/admin/Dockerfile` に `COPY apps/shared apps/shared` を追加
- `apps/public-viewer/Dockerfile` に `COPY apps/shared apps/shared` を追加

## 確認

この環境では Docker daemon が起動しておらず `docker build` 自体は実行できませんでした。
代わりに、host 側で次を実行し、少なくとも `next.config.ts` の `../shared/csp` import 解決で落ちないことを確認しました。

- `pnpm --filter @kouchou-ai/admin build`
- `pnpm --filter @kouchou-ai/public-viewer build`

どちらも `MODULE_NOT_FOUND: ../shared/csp` では落ちていません。

## 関連

- failing workflow: `Azure Deployment`
- failing run example: `26230264389`
- failing step: `Azure環境のデプロイ`


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Chores**
  * Updated Docker build configurations for the admin and public viewer applications to properly include shared resources in the build context, improving dependency management during the deployment process.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/851?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [LocalLLM モデル一覧の auto-fetch UX を改善](https://github.com/digitaldemocracy2030/kouchou-ai/pull/850)

**作成者:** nishio  
**作成日:** 2026-05-21T14:14:57Z  
**変更:** +278 -31 (5ファイル)  
**マージ日:** 2026-05-21T14:20:56Z  
**内容:**

## 概要
- LocalLLM を選択した時にモデル一覧の自動取得を試みるようにしました
- LocalLLM アドレス変更時も debounce 付きで自動再取得し、失敗時は既存の手動ボタンで再試行できます
- create flow の案内文と validation 文言を、自動取得前提の UX に合わせて更新しました

## 変更内容
- `useAISettings` に LocalLLM モデル一覧の debounce 付き auto-fetch を追加
- 手動の `モデル取得` は retry 用に残し、成功時 toast は従来どおり維持
- `validation.test.ts` と `useAISettings.test.ts` を追加し、auto-fetch / manual retry を検証

## 確認
- `pnpm --filter @kouchou-ai/admin test -- --runInBand app/create/hooks/useAISettings.test.ts app/create/utils/validation.test.ts`
- `pnpm exec biome check apps/admin/app/create/hooks/useAISettings.ts apps/admin/app/create/hooks/useAISettings.test.ts apps/admin/app/create/components/AISettingsSection.tsx apps/admin/app/create/utils/validation.ts apps/admin/app/create/utils/validation.test.ts`

Closes #845


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * LocalLLM models are now automatically fetched when you select the LocalLLM provider, streamlining the setup process.

* **Bug Fixes**
  * Improved error messaging when LocalLLM model retrieval fails, providing clearer guidance to retry model fetching via the dedicated button.

* **Documentation**
  * Updated LocalLLM connection settings helper text for better clarity and improved user guidance.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/850?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Add static hosting CSP deployment guide](https://github.com/digitaldemocracy2030/kouchou-ai/pull/849)

**作成者:** nishio  
**作成日:** 2026-05-21T13:36:54Z  
**変更:** +149 -1 (6ファイル)  
**マージ日:** 2026-05-21T13:51:12Z  
**内容:**

## Summary

Adds deployment documentation for static-exported `public-viewer` when a hosting layer applies Content Security Policy headers.

Closes #820

## Changes

- add `docs/deployment/static-hosting-csp.md`
- document why `img-src blob:` is required for Plotly PNG download
- add Azure Static Web Apps / Cloudflare Pages / Nginx examples
- link the new guide from GitHub Pages, Azure, quickstart, docs index, and README
- clarify that GitHub Pages is not a good fit when CSP headers must be controlled precisely

## Verification

- `git diff --check`
- `python3 -m mkdocs build --strict` could not be run in this environment because `mkdocs` is not installed

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Documentation**
  * Added comprehensive CSP configuration guide for static hosting deployments
  * Updated deployment documentation for Azure and GitHub Pages with CSP requirements
  * Clarified that `img-src` must include `blob:` to enable Plotly PNG downloads
  * Provided platform-specific CSP setup examples (Azure Static Web Apps, Cloudflare, Nginx)

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/849?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [web apps に env-aware CSP header を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/848)

**作成者:** nishio  
**作成日:** 2026-05-21T13:11:22Z  
**変更:** +163 -2 (4ファイル)  
**マージ日:** 2026-05-21T13:31:51Z  
**内容:**

## 概要

public IP + HTTP の self-host 環境で、API / icon / reporter image などの remote asset を current config から安全に許可できるよう、`apps/admin` と `apps/public-viewer` に env-aware な CSP header を追加します。

Closes #846

## 変更内容

- `apps/shared/csp.ts` に共通の CSP helper を追加
- `API_BASEPATH` / `NEXT_PUBLIC_API_BASEPATH` / `NEXT_PUBLIC_SITE_URL` から許可 origin を抽出
- `apps/admin/next.config.ts` に動的 `Content-Security-Policy` header を追加
- `apps/public-viewer/next.config.ts` に動的 `Content-Security-Policy` header を追加
- Google Fonts と、GA が有効な場合の Google Analytics origin を許可
- `public-viewer` の static export (`output: export`) では header を配れないため、この経路では `headers()` を空にする
- helper の targeted test を追加

## 確認

- `pnpm --filter @kouchou-ai/admin test -- --runInBand app/utils/__tests__/csp.test.ts`
- `pnpm exec biome check apps/shared/csp.ts apps/admin/app/utils/__tests__/csp.test.ts apps/admin/next.config.ts apps/public-viewer/next.config.ts`

## スコープ外

- static export 配信先での CSP 設定ガイド: #820
- Plotly PNG download / `blob:` まわりの個別確認: #818
- LocalLLM model auto-fetch UX: #845


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Implemented Content Security Policy headers across applications to enhance security and protect against code injection vulnerabilities.
  * Added conditional Google Analytics integration with configurable security policies.

* **Tests**
  * Added comprehensive test suite validating security policy configuration and header generation.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/848?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [admin create/reuse flow の UUID fallback を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/847)

**作成者:** nishio  
**作成日:** 2026-05-21T12:47:23Z  
**変更:** +142 -16 (6ファイル)  
**マージ日:** 2026-05-21T12:53:49Z  
**内容:**

## 概要

public IP + HTTP など non-secure context で `crypto.randomUUID()` が使えない場合でも、admin の create / reuse 画面が即死しないように UUID fallback を追加します。

Closes #833

## 変更内容

- `apps/admin/app/utils/uuid.ts` に `createUUID()` helper を追加
- `crypto.randomUUID()` がある環境ではそれを優先使用
- 無い場合は `crypto.getRandomValues()`、さらに無ければ `Math.random()` で RFC4122 v4 形式 UUID を生成
- `useBasicInfo` と `EnvironmentCheckDialog` の直接 `crypto.randomUUID()` 呼び出しを helper 経由に置換
- helper / hook / dialog の targeted test を追加

## 確認

- `pnpm --filter @kouchou-ai/admin test -- --runInBand app/utils/__tests__/uuid.test.ts app/create/hooks/useBasicInfo.test.ts app/create/components/EnvironmentCheckDialog/EnvironmentCheckDialog.test.tsx`
- `pnpm exec biome check apps/admin/app/utils/uuid.ts apps/admin/app/utils/__tests__/uuid.test.ts apps/admin/app/create/hooks/useBasicInfo.ts apps/admin/app/create/hooks/useBasicInfo.test.ts apps/admin/app/create/components/EnvironmentCheckDialog/EnvironmentCheckDialog.tsx apps/admin/app/create/components/EnvironmentCheckDialog/EnvironmentCheckDialog.test.tsx`

## スコープ外

- CSP / remote asset policy: #846
- LocalLLM model auto-fetch UX: #845


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Refactor**
  * Implemented centralized UUID generation utility with fallback compatibility for environments where standard crypto APIs may be unavailable.
  * Migrated internal UUID generation across components and hooks to use the new centralized utility.

* **Tests**
  * Added comprehensive test coverage for UUID generation, including fallback scenarios.
  * Updated test suites to verify proper usage of centralized UUID generation.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/847?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [analysis-core CLI に preflight validation を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/844)

**作成者:** nishio  
**作成日:** 2026-05-21T10:44:28Z  
**変更:** +228 -5 (6ファイル)  
**マージ日:** 2026-05-21T11:42:09Z  
**内容:**

## 概要
- `analysis-core` CLI に config / input の preflight validation を追加
- filesystem-based usage を current canonical path に合わせて整理
- output artifact validation は runtime block ではなく developer/test concern として位置づけを明記

## 変更内容
- `--validate-config` と `--validate-input` を追加
- `--dry-run` を cheap preflight 兼 plan 表示として整理
- current plan で input CSV が本当に必要な場合だけ、`comment-id` / `comment-body` / `extraction.properties` を検証
- `docs/user-guide/cli-quickstart.md` に filesystem path 解決、validation-only コマンド、output validation の位置づけを追記
- CLI / orchestration テストを追加

## 方針
- `#836` と `#837` は current `analysis-core` CLI に対する fail-fast 改善として同一 PR にまとめる
- `#838` については、post-run output validation を runtime success 条件には入れず、schema test / e2e / viewer 側で担保する方針を docs に明記する

## 確認
- `./.venv/bin/ruff check src tests`
- `./.venv/bin/pytest tests/test_cli.py tests/test_orchestration.py`
- `./.venv/bin/pytest tests/test_imports.py`

Closes #836
Closes #837
Refs #838


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Added --validate-config and --validate-input standalone validation modes.
  * Dry-run now performs a cheap preflight (prints validated config/input info) and shows the execution plan.
  * Preflight verifies config, input file existence, and required CSV headers; validation-only modes exit after success.

* **Documentation**
  * Updated CLI quickstart and options: default input/output paths, --input-dir/--output-dir, --without-html, artifact roles (HTML is sidecar; canonical JSON), preflight vs post-run guidance.

* **Tests**
  * Added/updated CLI and orchestration tests covering dry-run and validation behaviors.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/844?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [analysis-core の optional dependency を extras に分離](https://github.com/digitaldemocracy2030/kouchou-ai/pull/843)

**作成者:** nishio  
**作成日:** 2026-05-21T07:31:55Z  
**変更:** +145 -49 (11ファイル)  
**マージ日:** 2026-05-21T09:50:34Z  
**内容:**

## 概要
- `analysis-core` の重い依存を base `dependencies` から `embeddings` / `clustering` extras に分離
- base install でも `import analysis_core` が落ちないように step / orchestrator の import を lazy 化
- README / quickstart を extras 前提の導線に更新

## 変更内容
- `packages/analysis-core/pyproject.toml` に `embeddings` / `clustering` / `full` extras を追加
- `analysis_core.steps` と `PipelineOrchestrator` の built-in step 解決を lazy import 化
- local embedding / hierarchical clustering 実行時に、optional dependency 不足なら説明的な `RuntimeError` を返すよう変更
- `README.md` と `docs/user-guide/*quickstart.md` の install コマンドを更新
- lockfile を再生成し、import 契約向けのテストを追加

## 背景
Task 2.5.6 で想定されていた extras 分割が未実施だったため、`analysis-core` の base install が不要に重くなっていました。
一方で単純に `pyproject.toml` だけ直すと、`analysis_core.steps` の eager import により base install でも import error が起きうるため、その部分をあわせて整理しています。

## 確認
- `./.venv/bin/ruff check src tests`
- `./.venv/bin/pytest tests/test_imports.py tests/test_hierarchical_clustering.py tests/test_cli.py`


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Documentation**
  * Clarified installation in CLI/import quickstarts and core README, recommending optional extras for embeddings, clustering, and Gemini support.

* **New Features**
  * Optional extras enable modular installs for embeddings, clustering, and full tooling; runtime errors now give actionable install guidance when extras are missing.

* **Refactor**
  * Core components now lazily load optional features to avoid importing optional dependencies at startup.

* **Tests**
  * Added tests verifying lazy-loading behavior and import-time cleanliness.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/843?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[codex] legacy API step imports を Ruff に合わせる](https://github.com/digitaldemocracy2030/kouchou-ai/pull/841)

**作成者:** nishio  
**作成日:** 2026-05-20T09:04:23Z  
**変更:** +4 -8 (5ファイル)  
**マージ日:** 2026-05-20T09:12:53Z  
**内容:**

# 変更内容

`apps/api/` の pre-push hook が legacy `broadlistening/pipeline/steps/` の import 並びだけで止まっていたので、Ruff の指摘に合わせて import block を整えます。

変更は import 順の修正のみで、実行ロジックには触れていません。

# 背景

workflow default 化の branch で push するたびに、今回の変更とは無関係な legacy step 群の `api-ruff-check` が失敗していました。

hook と同じコマンドを `apps/api/` ルートで再現すると、次の 5 ファイルだけが `I001` で止まっていました。

- `broadlistening/pipeline/steps/embedding.py`
- `broadlistening/pipeline/steps/extraction.py`
- `broadlistening/pipeline/steps/hierarchical_initial_labelling.py`
- `broadlistening/pipeline/steps/hierarchical_merge_labelling.py`
- `broadlistening/pipeline/steps/hierarchical_overview.py`

# 動作確認

```bash
cd apps/api
rye run ruff check .
rye run ruff format . --check
```

どちらも通過しています。


**コメント:** なし

---

### [[codex] workflow default化の土台を整備](https://github.com/digitaldemocracy2030/kouchou-ai/pull/840)

**作成者:** nishio  
**作成日:** 2026-05-20T03:17:17Z  
**変更:** +2479 -160 (33ファイル)  
**マージ日:** 2026-05-21T04:44:26Z  
**内容:**

# 概要

`analysis-core` の workflow 経路 (`run_workflow()`) を、将来の標準実行経路として使える状態へ近づける PR です。

この PR でやったことは次の 4 点です。

- workflow の初期入力・`without_html` / `without-html`・`report.html` 契約のずれを修正
- workflow 実行中も `hierarchical_status.json` を更新し、`status` / `current_job` / `completed_jobs` / token usage / failure 情報を残すようにした
- `from_dict()` / `from_config()` から前回 status と既存成果物を読んで rerun plan を作り、step skip と `previously_completed_jobs` を扱えるようにした
- CLI / API の入口を workflow default path 前提へ寄せ、通常実行・config rerun・aggregation rerun・duplicate/reuse・failure step status API まで確認した

# 背景

`analysis-core` には legacy `.run()` と新しい `.run_workflow()` が共存していましたが、実運用で必要な責務は長く `.run()` 側にありました。

この PR は、
- 入力の受け渡し
- status の永続化
- 前回結果を使った再実行判断
- CLI / API 入口との接続

を workflow 側へ段階的に移すためのものです。

# まだ残っていること

ここまでで入口確認、rerun、duplicate/reuse、failure semantics、real workflow rerun e2e までは進みました。まだ残っているのは次です。

- 実データバリエーションを増やした e2e / 運用系検証
- `hierarchical_status.json` の意味論が legacy path と完全互換かの最終確認
- README / deprecated README / refactoring docs を含む説明の整理

# 動作確認

analysis-core:

```bash
work/kouchou-ai/packages/analysis-core/.venv/bin/python -m pytest \
  work/kouchou-ai/packages/analysis-core/tests/test_workflow_engine.py \
  work/kouchou-ai/packages/analysis-core/tests/test_orchestration.py \
  work/kouchou-ai/packages/analysis-core/tests/test_builtin_plugins.py \
  work/kouchou-ai/packages/analysis-core/tests/test_hierarchical_visualization.py \
  work/kouchou-ai/packages/analysis-core/tests/test_cli.py \
  work/kouchou-ai/packages/analysis-core/tests/test_integration.py \
  work/kouchou-ai/packages/analysis-core/tests/test_pipeline_paths_integration.py \
  work/kouchou-ai/packages/analysis-core/tests/e2e/test_pipeline_e2e.py -q
```

apps/api (`.venv` / Python 3.12):

```bash
ADMIN_API_KEY=test PUBLIC_API_KEY=test OPENAI_API_KEY=test \
work/kouchou-ai/apps/api/.venv/bin/python -m pytest \
  work/kouchou-ai/apps/api/tests/services/test_report_launcher.py \
  work/kouchou-ai/apps/api/tests/services/test_report_duplicate.py \
  work/kouchou-ai/apps/api/tests/services/test_report_sync.py \
  work/kouchou-ai/apps/api/tests/routers/test_get_current_step.py -q
```

補足:
- system Python 3.10 では `apps/api` 側の既存 `datetime.UTC` import により一部テスト基盤が起動しません
- API 側の検証は repo 同梱の `.venv` (Python 3.12) を基準にしています

# CLAへの同意

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Default execution mode now uses workflow-based engine for improved step resumption and rerun efficiency.
  * Workflow engine supports step lifecycle callbacks and skip lists for granular execution control.
  * HTML report generation now uses pure Python instead of npm-based build.
  * Support for report duplication with artifact reuse.

* **Bug Fixes**
  * Configuration keys `without_html` and legacy `without-html` are now synchronized consistently.

* **Documentation**
  * Updated CLI/import guides, plugin documentation, and READMEs to reflect new execution defaults.

* **Deprecated**
  * `PipelineOrchestrator.run()` method now emits deprecation warning; use `run_default()` instead.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/840?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[codex] ignore apps/api uv lockfile](https://github.com/digitaldemocracy2030/kouchou-ai/pull/839)

**作成者:** nishio  
**作成日:** 2026-05-20T02:53:11Z  
**変更:** +1 -0 (1ファイル)  
**マージ日:** 2026-05-20T02:55:09Z  
**内容:**

## What changed
- ignore `apps/api/uv.lock` in the repo root `.gitignore`

## Why
- `apps/api` uses `requirements.lock` and `requirements-dev.lock` as the tracked lock artifacts
- `uv.lock` is a local byproduct in the current setup and was repeatedly dirtying worktrees

## Impact
- local `uv` usage in `apps/api` no longer creates accidental untracked noise
- no runtime or build behavior changes

## Validation
- confirmed the only code change is the `.gitignore` entry


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Chores**
  * Updated git configuration to ignore additional build artifacts.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/839?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (8件)

### [[codex] semantic island layout 生成を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/874)

**作成者:** nishio  
**作成日:** 2026-05-26T14:00:12Z  
**変更:** +1040 -19 (17ファイル)  
**内容:**

## 変更内容

- aggregation と visualization の間に `hierarchical_layout_generation` step を追加
- `arguments[].x/y` は既存の embedding 由来座標のまま残しつつ、`hierarchical_result.json.layouts` に名前付き layout を追加
- 全 run で `embedding_umap` を生成し、`llm_grouping` 出力では既定で `semantic_island_map` も生成
- self-contained HTML viewer が `default_layout_id` / `layouts` を読めるよう更新
- workflow、legacy config normalization、plugin registration、orchestration、compat spec を新 step に追従
- 新 step、workflow integration、CLI rerun、visualization fallback をカバーする回帰テストを追加

## 背景

`llm_grouping` では cluster-first な主図が欲しい一方で、既存の `x/y` を置き換えると WebUI を含む既存 consumer を壊すリスクがあります。そこで、既存の `arguments[].x/y` はそのまま canonical な座標として残し、CLI HTML などが段階的に採用できる追加 layout 層として `semantic_island_map` を導入しました。

## 影響

- `arguments[].x/y` だけを読んでいる既存 consumer とは後方互換
- CLI が生成する `report.html` では `llm_grouping` に対して `semantic_island_map` を既定 layout として使える
- 今後 `layouts` / `default_layout_id` を読む viewer を段階的に追加しやすくなる

## 確認

- `PYTHONPATH=packages/analysis-core/src .venv-analysis312/bin/pytest packages/analysis-core/tests/test_hierarchical_layout_generation.py packages/analysis-core/tests/test_builtin_plugins.py packages/analysis-core/tests/test_hierarchical_visualization.py packages/analysis-core/tests/test_imports.py packages/analysis-core/tests/test_integration.py packages/analysis-core/tests/test_compat.py packages/analysis-core/tests/test_pipeline_paths_integration.py packages/analysis-core/tests/test_cli.py -q`
- 実データ `jigsaw_sample_comments_400_config` のコピー上で `hierarchical_layout_generation` と `hierarchical_visualization` を実行し、`arguments[].x/y` が不変なまま `report.html` を再生成できることを確認


**コメント:** なし

---

### [[codex] Azure deploy を直列化して更新競合を避ける](https://github.com/digitaldemocracy2030/kouchou-ai/pull/873)

**作成者:** nishio  
**作成日:** 2026-05-26T12:43:44Z  
**変更:** +4 -0 (1ファイル)  
**内容:**

## 概要

- `Azure Deployment` workflow に `concurrency` を追加し、`main` 向け deploy を 1 本ずつ流すようにしました
- `cancel-in-progress: false` とし、先行 deploy を途中で止めず順番待ちさせます

## 背景

issue #741 の recent run を見ると、直近の failure は `npm` の一時的な fetch error というより、`ContainerAppOperationInProgress` による Azure Container Apps 更新競合でした。

短時間に `main` へ複数 merge が入ると、前の deploy が Azure 側で provisioning 中の間に次の deploy が `az containerapp update` を叩き、後続 run が失敗します。

まずは workflow 単位で deploy を直列化し、更新競合を起こしにくくします。

## 確認

- ローカルでは workflow YAML の差分確認のみ実施
- 実際の有効性確認は、この PR の merge 後または branch 上での GitHub Actions 実行が必要

Closes #741


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Chores**
  * Enhanced Azure deployment process to prevent interruption of ongoing deployments when multiple deployments are queued simultaneously.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/873?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[codex] 実行時ユーザーAPIキーの受け渡しを直す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/868)

**作成者:** nishio  
**作成日:** 2026-05-25T08:59:13Z  
**変更:** +94 -9 (12ファイル)  
**内容:**

## 概要
- `USER_API_KEY` を `analysis-core` の初期 API key 検証で使えるようにしました。
- workflow の `StepContext` と built-in plugin の legacy runtime config に、実行時の user API key を伝播するようにしました。
- 既存の legacy step でも `config["user_api_key"]` を優先し、なければ従来通り `USER_API_KEY` env を参照するようにしました。

## 意図
- Web/API 側は `x-user-api-key` を subprocess の `USER_API_KEY` に渡していますが、core 側の fail-fast validation や plugin 経由の step 実行で一貫して扱えていませんでした。
- user API key は `initialization()` の戻り config や status JSON に保存しないようにしています。

## スコープ
- API key plumbing の修正のみです。
- LLM grouping / label refinement / `--reuse-from` の実装は含めていません。

## 確認
- `rye run ruff check src tests/test_builtin_plugins.py tests/test_compat.py tests/test_orchestration.py tests/test_pipeline_paths_integration.py`
- `rye run python -m pytest tests/test_builtin_plugins.py tests/test_compat.py tests/test_orchestration.py tests/test_pipeline_paths_integration.py -q`
- `OPENAI_API_KEY=dummy rye run python -m pytest -q`

**コメント:** なし

---

### [[codex] 既存出力を再利用して再実行できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/867)

**作成者:** nishio  
**作成日:** 2026-05-25T08:18:47Z  
**変更:** +334 -17 (5ファイル)  
**内容:**

## 概要
- CLI に `--reuse-from` を追加し、既存の出力ディレクトリ名またはパスを指定できるようにしました。
- 指定元に存在する中間成果物を新しい出力ディレクトリへ seed し、対応するステップを `nothing changed` として skip できるようにしました。
- `extraction` では `args.csv` とあわせて `relations.csv` も再利用し、`report` のようなディレクトリ成果物もコピーできるようにしています。

## スコープ
- このPRは `--reuse-from` のみです。
- LLM grouping と label refinement の実装は含めていません。

## 確認
- `rye run ruff check src tests/test_cli.py tests/test_orchestration.py`
- `rye run python -m pytest tests/test_cli.py tests/test_orchestration.py tests/test_pipeline_paths_integration.py -q`
- `OPENAI_API_KEY=dummy rye run python -m pytest -q`

補足: `OPENAI_API_KEY` なしの全体 pytest は、既存の prompt テスト2件が環境変数未設定で失敗しました。ダミー値を入れると `181 passed` です。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Added a --reuse-from CLI option to reuse intermediate outputs from a prior run so completed pipeline stages can be skipped and only downstream work executed.
  * CLI help now documents the new flag and dry-run shows seeded/skipped steps.

* **Tests**
  * Added tests covering CLI behavior and orchestration seeding to ensure reused outputs are detected and downstream steps run as expected.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/867?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[codex] LLM grouping 分析モードを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/866)

**作成者:** nishio  
**作成日:** 2026-05-25T07:57:39Z  
**変更:** +882 -16 (16ファイル)  
**内容:**

## 概要

- `analysis_mode=llm_grouping` で LLM による意見グルーピング workflow を選べるようにしました
- `analysis.llm_grouping` plugin / step / specs / workflow を追加し、既存 viewer 互換の `hierarchical_clusters.csv` と `hierarchical_merge_labels.csv` を出力します
- discovery / assignment 用の default prompt と config normalization を追加し、`from_config` / `from_dict` の両方で mode に応じた specs と workflow を選ぶようにしました

## 意図

散布図互換を保ったまま、embedding によるクラスタリングではなく raw argument を LLM で top-level group に割り当てる実験用の入口を先に切り出します。label refinement は別論点なので、この PR には含めていません。

## 確認

- `rye run ruff check src tests/test_llm_grouping.py tests/test_compat.py tests/test_imports.py tests/test_prompts.py`
- `rye run python -m pytest tests/test_llm_grouping.py tests/test_compat.py tests/test_imports.py tests/test_prompts.py tests/test_integration.py tests/test_orchestration.py -q`
- `rye run python -m pytest tests/test_cli.py tests/test_pipeline_paths_integration.py -q`
- `rye run python -m pytest -q`

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## Release Notes

* **New Features**
  * Added LLM-based grouping workflow as an alternative to hierarchical clustering for analyzing opinions
  * Configuration now supports selecting analysis modes to choose between different grouping strategies
  * Implemented automated group discovery and assignment with customizable AI-powered prompts

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/866?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[codex] Windows setup の日本語案内を PowerShell に分離](https://github.com/digitaldemocracy2030/kouchou-ai/pull/863)

**作成者:** nishio  
**作成日:** 2026-05-22T14:28:07Z  
**変更:** +233 -154 (3ファイル)  
**内容:**

## 概要

- `setup_win.bat` を ASCII だけの薄いランチャーに縮小し、本体処理を `setup_win.ps1` へ分離しました
- API キー入力、形式確認、Docker 未起動時の案内、完了案内を PowerShell 側の日本語ダイアログで扱うようにしました
- Windows セットアップ手順のドキュメントを、新しい PowerShell 起動フローに合わせて更新しました

## 背景

Fixes #731

issue #731 の症状は、単なる表示崩れではなく、`setup_win.bat` 内の日本語行が `cmd.exe` で別コマンドとして解釈されて停止するものでした。`cmd.exe` / `.bat` 単体ではコードページ差異の影響を受けやすいため、バッチ本体は ASCII のみに保ち、日本語メッセージと入力処理は PowerShell へ逃がす方針に切り替えています。

## 確認

- `rg -n "[^\\x00-\\x7F]" setup_win.bat setup_win.ps1` で、バッチ本体と PowerShell 本体が ASCII のみで構成されていることを確認
- `git diff --check` 実行済み
- `pwsh` がローカル環境に無いため、PowerShell の実行確認は未実施

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Added interactive GUI prompts and a non‑interactive setup mode with options to skip Docker startup or API-key validation; automated local environment file creation and clearer success/error dialogs.

* **Refactor**
  * Windows setup launcher simplified to delegate setup logic to a centralized script for more consistent behavior.

* **Documentation**
  * Updated Windows setup and troubleshooting guidance to reflect the new prompts, paste workaround, and standardized Docker message.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/863?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Windows 向け setup_win.bat の軽量 CI を追加する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/861)

**作成者:** nishio  
**作成日:** 2026-05-22T11:59:42Z  
**変更:** +199 -9 (3ファイル)  
**内容:**

## 概要
Windows 向け `setup_win.bat` の軽量 regression test を `windows-latest` で回せるようにします。

## 変更内容
- `setup_win.bat` に non-interactive test hook を追加し、CI から `pause` で止まらずに検証できるようにした
- fake `docker.bat` を使って `docker info` / `docker compose` を模擬する PowerShell テストを追加
- `windows-latest` で上記テストを回す GitHub Actions workflow を追加
- 検証観点は以下に絞った
  - UTF-8 / `chcp 65001` 前提の文字化け検知
  - Docker 未起動時の想定メッセージ
  - API key 入力後の `.env` 生成
  - 不正な API key 入力時の abort 分岐

## 確認
- ローカル macOS 環境では `cmd.exe` / Windows PowerShell 実行環境が無いため、Windows 実行自体は未検証
- `#859` の目的どおり、最終確認は GitHub Actions の `windows-latest` で行う

Closes #859


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Enhanced Windows setup: optional non-interactive mode, centralized pause behavior, explicit success/fail exit codes, and ability to skip starting Docker Compose.

* **Tests**
  * Added automated Windows test suite validating script encoding, Docker-unavailable handling, env file generation, and user-abort flows.

* **Chores**
  * Added a Windows setup validation workflow to run these checks on push/PR and via manual trigger.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/861?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[codex] Windows setup の文字化け耐性を改善](https://github.com/digitaldemocracy2030/kouchou-ai/pull/858)

**作成者:** nishio  
**作成日:** 2026-05-22T11:14:13Z  
**変更:** +19 -34 (1ファイル)  
**内容:**

## 概要

- `setup_win.bat` のユーザー向け実行メッセージを ASCII のみにして、Windows のコードページ差異で文字化けしてもセットアップが中断しないようにしました
- API キー形式チェックの重複を削除し、`findstr` パイプではなく prefix 比較に整理しました
- Docker 未起動/未インストール時は明示的に exit code 1 で終了するようにしました

## 背景

Fixes #731

Issue #731 では、Windows で配布 zip の `setup_win.bat` を実行した際に日本語メッセージが mojibake し、一部がコマンドとして解釈されてセットアップが止まる症状が報告されています。バッチファイル本体は利用者の端末コードページに左右されやすいため、実行に必要な案内は ASCII に寄せました。詳しい日本語手順は既存の `docs/getting-started/windows-setup.md` に残っています。

## 確認

- `cmd /c "echo. | setup_win.bat"` を Docker CLI が無い環境で実行し、Docker Desktop 未起動/未インストール時の停止パスが英語メッセージで表示されることを確認
- `rg -n "[^\x00-\x7F]" setup_win.bat` でバッチファイル内に非 ASCII 文字が残っていないことを確認
- `git diff --check` 実行済み（CRLF 変換 warning のみ）

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## Release Notes

* **Chores**
  * Improved Windows setup script robustness with enhanced Docker environment validation
  * Simplified API key input handling with clearer validation for OpenAI and Gemini keys
  * Enhanced error messaging throughout the setup process with improved user guidance and confirmation prompts

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/858?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

