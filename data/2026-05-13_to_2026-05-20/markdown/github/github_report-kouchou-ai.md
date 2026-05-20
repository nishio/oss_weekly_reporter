# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-05-13T13:31:53.893108+09:00 から 2026-05-20T13:31:53.893108+09:00 まで

## Issues

### 過去7日間に完了されたissue (3件)

### [[FEATURE] CLI / analysis-core で cluster_nums を省略可能にし、argument 数ベースで推奨値を自動計算する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/830)

**作成者:** nishio  
**作成日:** 2026-05-18T14:34:33Z  
**内容:**

## 背景

議事録で、デフォルトのクラスタ数が少なすぎるため、コメント数が多いデータでもまとめすぎの設定が使われやすい、という指摘がありました。

特に CLI / `kouchou-ai-analysis-core` の導線では、`cluster_nums: [3, 6]` がサンプル・デフォルトとして露出しており、それをそのまま参考にした結果、300件前後のデータでも粗すぎる階層で分析されやすくなっています。

現状確認:
- `docs/user-guide/cli-quickstart.md` に `"cluster_nums": [3, 6]` の例がある
- `docs/user-guide/import-quickstart.md` にも同様の例がある
- `packages/analysis-core/src/analysis_core/compat/config_converter.py` が `cluster_nums` のデフォルトを `[3, 6]` にしている
- `packages/analysis-core/src/analysis_core/specs/hierarchical_specs.json` でも `cluster_nums: [3, 6]` を持っている
- 一方で `docs/user-guide/how-to-use.md` では、Admin 画面では「コメント数に基づいたおすすめクラスタ数設定」が初期値として設定されると書かれている

## 問題

- CLI / `analysis-core` 利用者は、小さすぎる固定値をそのまま採用しやすい
- コメント数が多いケースでも `3 -> 6` のような粗い設定になりやすく、クラスタがまとまりすぎる
- 「ドキュメントの記述を直す」だけだと、固定デフォルト自体が残り続ける

## 提案

`hierarchical_clustering.cluster_nums` を省略可能にし、未指定時は extraction 後の argument 数から「おすすめのクラスタ数」を自動計算する。

計算式の方向性:
- 基準はコメント数ではなく extraction 後の `argument` 数とする
- `argument` 数が 1000 件のときに `[10, 100]` になる計算式にする
- Admin 画面ですでに使っている「おすすめクラスタ数」ロジックがあるなら共通化して CLI / `analysis-core` でも使う
- 自動計算値はログや出力に明示し、利用者が採用されたクラスタ数を確認できるようにする
- 明示指定された `cluster_nums` は従来どおり優先する
- 実装後に CLI / import quickstart の `[3, 6]` 例も追従させる

## 受け入れ条件の案

- [ ] `cluster_nums` を設定しなくても CLI / `analysis-core` が実行できる
- [ ] 未指定時に、extraction 後の `argument` 数に応じたクラスタ数が自動計算される
- [ ] `argument` 数 1000 件のときに `[10, 100]` となる
- [ ] 自動計算されたクラスタ数をユーザーが確認できる
- [ ] 明示的に `cluster_nums` を指定した場合はその値を使う
- [ ] `docs/user-guide/cli-quickstart.md` / `docs/user-guide/import-quickstart.md` が新仕様に一致する

## 関連

- #577 自動クラスタ数調整機能のベータ評価と継続判断
- `docs/user-guide/cli-quickstart.md`
- `docs/user-guide/import-quickstart.md`
- `packages/analysis-core/src/analysis_core/compat/config_converter.py`
- `packages/analysis-core/src/analysis_core/specs/hierarchical_specs.json`


**コメント:** なし

---

### [fix: Overview コンポーネントで result.config が undefined の場合にクラッシュする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/800)

**作成者:** tokoroten  
**作成日:** 2026-02-22T01:45:29Z  
**内容:**

## 概要

`Overview.tsx` の16行目で `result.config.question` にアクセスする際、`result.config` が `undefined` の場合に TypeError が発生しアプリがクラッシュする。

## エラー内容

```
TypeError: Cannot read properties of undefined (reading 'question')
    at Overview (components\report\Overview.tsx:16:24)
```

## 再現条件

- レポートデータのロード前にコンポーネントがレンダリングされる
- または `result.config` を持たないレポートデータが渡される

## 期待される動作

`result.config` が未定義の場合でもクラッシュせず、適切なフォールバック（ローディング表示やデフォルト値）を表示する。

## 修正案

`result.config` の存在チェックを追加するか、optional chaining (`result.config?.question`) を使用する。

**コメント:** なし

---

### [[BUG]公開状態にしたレポートがない状態で静的HTML出力をしたときのエラーメッセージがわかりにくい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/726)

**作成者:** nishio  
**作成日:** 2025-10-27T16:41:06Z  
**内容:**

### 概要

```
client-static-build-1  |     '[Error: Page "/[slug]/opengraph-image.png" is missing "generateStaticParams()" so it cannot be used with "output: export" config.]\n' +
```

### 再現手順

1. 恐らく公開状態にしたレポートがない状態で静的HTML出力をすると発生する

### 期待する動作

エラーメッセージがわかりにくい。公開状態にしたレポートがない状態で静的HTML出力をしたときには早い段階でわかりやすい日本語のメッセージを出すべきである。


**コメント:** なし

---

### 過去7日間に作成されたissue (4件)

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

### [Evaluate output artifact validation for analysis-core CLI](https://github.com/digitaldemocracy2030/kouchou-ai/issues/838)

**作成者:** nishio  
**作成日:** 2026-05-19T08:00:28Z  
**内容:**

## Background

Output validation was bundled into `PR #722`, but it is separable from config/input preflight checks and should be evaluated on its own for the current `analysis-core` path.

## Scope

- clarify whether post-run output validation is needed for current `analysis-core`
- if yes, define the validation surface for generated artifacts such as `hierarchical_result.json` and status files
- decide whether this belongs in the CLI, a helper command, or tests only

## Questions to settle

- is this primarily a developer/test concern rather than an end-user CLI concern?
- should output validation block success, or be an opt-in diagnostic tool?
- which artifacts are stable enough to validate strictly?

## Non-goals

- legacy pipeline shim improvements
- duplicating existing test coverage without a clear runtime use case

## Parent

- part of #721


**コメント:** なし

---

### [Issue #685 follow-up: reimplement remote HTTP/CSP/UUID fixes on current apps/* tree](https://github.com/digitaldemocracy2030/kouchou-ai/issues/833)

**作成者:** nishio  
**作成日:** 2026-05-18T15:55:00Z  
**内容:**

## Summary

`PR #735` tried to address `Issue #685`, but it is no longer mergeable as-is.

As of 2026-05-19:

- `PR #735` is still a draft
- it is `CONFLICTING`
- checks were failing (`build` x2, `e2e-tests`)
- the patch targets the old `client/` and `client-admin/` frontend tree
- current `main` uses `apps/public-viewer/` and `apps/admin/`

So the issue is still worth fixing, but the old patch should not be revived by conflict resolution alone. It should be reimplemented from current `main`.

## Why `PR #735` should not be merged

- The changed paths are stale relative to current `main`
- Security-related changes (CSP) and UX changes (LocalLLM auto-fetch) are bundled together, which makes review harder
- `crypto.randomUUID()` usage still exists on current `main`, but the old polyfill patch needs to be reconsidered against the current code structure and browser support policy

## Next actions

- [ ] Reproduce `Issue #685` on current `main` with the current `apps/*` frontend layout
- [ ] Decide support policy for public-IP HTTP access in self-hosted environments
- [ ] Implement a current-tree fix for `crypto.randomUUID()` usage in `apps/admin`
- [ ] Implement and review CSP / remote asset loading policy for `apps/public-viewer` and `apps/admin`
- [ ] Decide whether LocalLLM model auto-fetch should be included in the same fix or split into a separate UX issue/PR
- [ ] Open a fresh PR from current `main` instead of rebasing `PR #735`

## Related

- Fix target: #685
- Supersedes stale patch discussion in: #735


**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(2件)

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

### [[FEATURE] レポートページを見ようとスクロールすると図が拡大縮小される](https://github.com/digitaldemocracy2030/kouchou-ai/issues/493)

**作成者:** mtane0412  
**作成日:** 2025-05-12T14:26:32Z  
**内容:**

# 背景
ScatterChartの領域でスクロールで拡大縮小できるようになった。
このことにより「レポートページを見るためにスクロールする→図が拡大/縮小される」というユーザーが意図しない動作がほぼ発生する。

![](https://i.gyazo.com/00394aa1f859e933dc6f293ba1605361.gif)


# 提案内容
何らかの方法でユーザー操作を直感的にする

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (15件)

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

### [Improve static build error handling for public viewer](https://github.com/digitaldemocracy2030/kouchou-ai/pull/835)

**作成者:** nishio  
**作成日:** 2026-05-19T06:30:42Z  
**変更:** +132 -26 (3ファイル)  
**マージ日:** 2026-05-19T07:47:13Z  
**内容:**

## Summary
- centralize static export report validation in a helper used by `generateStaticParams()`
- fail fast with a clear message when there are no ready reports for static export
- distinguish the `BUILD_SLUGS` mismatch case from the "no ready reports" case
- add unit tests for the static build validation helpers

## Verification
- `pnpm test -- --runInBand app/utils/__tests__/static-build.test.ts app/utils/__tests__/api.test.ts`
- `API_BASEPATH=http://127.0.0.1:8999 NEXT_PUBLIC_API_BASEPATH=http://127.0.0.1:8999 pnpm run build:static` and confirm it fails with the new ready-report error
- `API_BASEPATH=http://127.0.0.1:8002 NEXT_PUBLIC_API_BASEPATH=http://127.0.0.1:8002 NEXT_PUBLIC_PUBLIC_API_KEY=public pnpm run build:static` and confirm it succeeds against `utils/dummy-server`


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Tests**
  * Added comprehensive test suite for static build utilities.

* **Chores**
  * Refactored static build parameter generation with improved error handling for static exports.
  * Enhanced validation and error messages for missing or unmatched build configurations.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/835?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix: validate public report payload before serving](https://github.com/digitaldemocracy2030/kouchou-ai/pull/834)

**作成者:** nishio  
**作成日:** 2026-05-18T16:10:50Z  
**変更:** +53 -2 (3ファイル)  
**マージ日:** 2026-05-19T01:53:28Z  
**内容:**

## 概要

`/reports/{slug}` が返す `hierarchical_result.json` について、public-viewer が前提にしている最小契約を API 側で検証するようにします。

- `config.question` を含まない壊れた report payload は返さず、`500 Invalid report data` を返す
- `config` 欠損 report に対する回帰テストを追加する

## なぜ `#802` では足りなかったか

`#800` の切り分けで、`config` を欠いた `hierarchical_result.json` を API が返すと viewer が落ちること自体は再現できました。

ただし根本原因は `Overview.tsx` の 1 箇所だけではありません。

- `PR #802` は `Overview.tsx` の `result.config.question` を optional chaining に変えるだけだった
- しかし current `public-viewer` では metadata 生成や OGP 画像生成など、他にも `result.config.*` を前提にしている箇所がある
- そのため `Overview` だけを null-safe にしても、壊れた payload が API から来る限り viewer 全体の契約不整合は残る

実際の問題は、`apps/api` の `/reports/{slug}` が保存済みの `hierarchical_result.json` を shape validation せず、そのまま public API として返している点にあります。

## この PR でやること

- `/reports/{slug}` の返却前に、public-viewer が最低限必要とする shape を検証する
- 具体的には `overview`, `clusters`, `arguments`, `config.question` を持たない payload を invalid として扱う
- invalid な report data は viewer に流さず、API 境界で失敗させる

これにより、viewer 側で個別に握りつぶすのではなく、契約違反を API 側で止められます。

## テスト

- `ADMIN_API_KEY=dummy PUBLIC_API_KEY=dummy OPENAI_API_KEY=dummy uv run python -m pytest tests/routers/test_report.py -q`
- `uv run ruff check src/routers/report.py src/schemas/public_report_result.py tests/routers/test_report.py`

Closes #800
Supersedes #802


**コメント:** なし

---

### [feat: auto-calculate cluster counts in analysis-core when omitted](https://github.com/digitaldemocracy2030/kouchou-ai/pull/832)

**作成者:** nishio  
**作成日:** 2026-05-18T14:47:03Z  
**変更:** +93 -21 (13ファイル)  
**マージ日:** 2026-05-18T15:56:42Z  
**内容:**

## 概要
- `cluster_nums` 未指定時に、extraction 後の argument 数から推奨クラスタ数を自動計算するように変更
- 固定デフォルト `[3, 6]` を CLI / analysis-core の compat, specs, plugin fallback から除去
- quickstart と関連テストを新仕様へ更新

## 変更内容
- `analysis_core.steps.hierarchical_clustering` に推奨クラスタ数計算を追加
- 計算式は Admin 側の既存ロジックに合わせて `lv1 = round(cuberoot(argument_count))`, `lv2 = lv1^2` をベースに使用
- `argument_count=1000` で `[10, 100]` になることをテストで保証
- `cluster_nums` 省略時は実行ログに採用値を出力し、config にも反映
- `docs/user-guide/cli-quickstart.md` / `docs/user-guide/import-quickstart.md` から `[3, 6]` の例を削除

## テスト
- `packages/analysis-core/.venv-ci/bin/python -m pytest packages/analysis-core/tests/test_hierarchical_clustering.py packages/analysis-core/tests/test_compat.py packages/analysis-core/tests/test_orchestration.py packages/analysis-core/tests/test_pipeline_paths_integration.py -q`

## CLAへの同意
- [x] CLAの内容を読み、同意しました

Closes #830


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Hierarchical clustering `cluster_nums` parameter is now optional and automatically calculated based on extracted argument count when omitted.

* **Documentation**
  * Updated quickstart guides to reflect optional `cluster_nums` configuration and auto-calculation behavior.

* **Tests**
  * Added tests validating automatic cluster number calculation and updated existing tests for new optional parameter behavior.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/832?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Add analysis-core publish workflow](https://github.com/digitaldemocracy2030/kouchou-ai/pull/831)

**作成者:** nishio  
**作成日:** 2026-05-18T14:40:35Z  
**変更:** +53 -5 (2ファイル)  
**マージ日:** 2026-05-18T14:41:56Z  
**内容:**

# Summary
- add `publish-analysis-core.yml` for PyPI release automation
- trigger publishes only on `analysis-core-v*` tags
- update the PyPI release playbook to match the new tag convention

# Background
- the package-specific CI is already in `main`, but the publish workflow was committed after the previous PR was merged
- `PYPI_API_TOKEN` is now configured in repository secrets
- release tags for this package should use the dedicated `analysis-core-v*` namespace rather than the repo-wide `v*`

# Verification
- workflow definition reviewed locally
- release docs updated to use `analysis-core-v0.1.1`

# Notes
- this workflow runs `ruff`, `pytest`, `build`, then `pypa/gh-action-pypi-publish`
- actual publish execution will occur only when an `analysis-core-v*` tag is pushed

# Related
- follow-up to the merged CI groundwork from #826

**コメント:** なし

---

### [[codex] remove fixed random seeds from hierarchical clustering](https://github.com/digitaldemocracy2030/kouchou-ai/pull/829)

**作成者:** nishio  
**作成日:** 2026-05-18T14:33:44Z  
**変更:** +4 -4 (2ファイル)  
**マージ日:** 2026-05-19T02:37:13Z  
**内容:**

## Summary
- remove fixed `random_state=42` from hierarchical clustering in both `apps/api` and `packages/analysis-core`
- add a regression test that checks the analysis-core step source no longer hardcodes `random_state=42`
- intentionally do not add any new UI or config flag

## Why
The discussion on #810 concluded that a reproducibility toggle is unnecessary in both the Web UI and CLI. The smaller and current fix is to stop hardcoding the seed instead of introducing a new `enable_reproducibility` flag and propagating it across layers.

## Validation
- `ruff check packages/analysis-core/tests/test_hierarchical_clustering_random_seed.py packages/analysis-core/src/analysis_core/steps/hierarchical_clustering.py apps/api/broadlistening/pipeline/steps/hierarchical_clustering.py`
- `python3.12` AST check confirming `UMAP` / `KMeans` no longer receive `random_state=42`

## Notes
- supersedes #810
- keeps the change surface limited to clustering behavior


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Updated clustering algorithms to use variable random seeds instead of fixed values, resulting in non-deterministic behavior across runs.

* **Tests**
  * Added regression test to ensure clustering randomization behavior is maintained.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/829?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[codex] fix public-viewer reporter API URL fallback](https://github.com/digitaldemocracy2030/kouchou-ai/pull/828)

**作成者:** nishio  
**作成日:** 2026-05-18T04:48:43Z  
**変更:** +61 -2 (3ファイル)  
**マージ日:** 2026-05-18T14:03:53Z  
**内容:**

## What changed
- add `getApiUrl()` to `apps/public-viewer/app/utils/api.ts`
- switch `Reporter` image probing to use the same API base URL fallback as the rest of `public-viewer`
- add unit tests for server-side URL construction and missing-env handling

## Why
`Reporter` was using `process.env.API_BASEPATH` directly via `new URL(...)`, while the rest of `public-viewer` uses `getApiBaseUrl()` and falls back to `NEXT_PUBLIC_API_BASEPATH` when `API_BASEPATH` is unset.

That mismatch meant the root page could fail prerender with `ERR_INVALID_URL` even in environments where the app otherwise had a valid API base URL.

## Impact
- `public-viewer` build behavior is more predictable across CI and local environments
- root page prerender no longer has a stricter env requirement than the rest of the app
- missing or invalid API base URL now degrades to "reporter image absent" instead of throwing during prerender

## Validation
- `pnpm test -- --runInBand app/utils/__tests__/api.test.ts`
- `NEXT_PUBLIC_API_BASEPATH=http://127.0.0.1:18000 NEXT_PUBLIC_PUBLIC_API_KEY=test pnpm build` with a minimal mock API


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## Release Notes

* **New Features**
  * Added improved API URL construction utility for better consistency across the application.

* **Bug Fixes**
  * Enhanced reporter image URL handling with more robust error management.
  * Better support for different server-side and client-side configuration scenarios.

* **Tests**
  * Added comprehensive test coverage for API URL construction with various environment configurations.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/828?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [docs: add plan for llm grouping and capability auto-detection](https://github.com/digitaldemocracy2030/kouchou-ai/pull/827)

**作成者:** nishio  
**作成日:** 2026-05-18T04:02:20Z  
**変更:** +286 -0 (1ファイル)  
**マージ日:** 2026-05-18T14:06:55Z  
**内容:**

## Summary
- add initial implementation plan document for LLM grouping and capability auto-detection
- clarify short-term compatibility approach and long-term capability-driven visualization gating

## Notes
- this PR is intended as a base branch to stack follow-up commits
- unrelated local files are intentionally excluded

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Documentation**
  * Added planning documentation outlining future enhancements to analysis capabilities and visualization features.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/827?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Add analysis-core CI and test fixes](https://github.com/digitaldemocracy2030/kouchou-ai/pull/826)

**作成者:** nishio  
**作成日:** 2026-05-16T23:49:43Z  
**変更:** +113 -43 (16ファイル)  
**マージ日:** 2026-05-18T14:09:50Z  
**内容:**

# Summary
- add a dedicated GitHub Actions workflow for `packages/analysis-core`
- fix `analysis_core` tests so they are CI-safe and path-independent
- allow CLI `--dry-run` to skip early API key validation and harden empty-comment filtering

# Background
- `analysis-core` had no package-specific CI even though it is published separately to PyPI
- `tests/test_cli.py` depended on a local absolute path and `--dry-run` still failed before plan display
- the extraction filter crashed on all-`None` comment bodies with a Polars schema error instead of the intended runtime error

# Verification
- `ruff check .`
- `OPENAI_API_KEY=dummy GEMINI_API_KEY=dummy .venv-ci/bin/pytest -q`
- result: `120 passed, 1 warning`

# Notes
- the remaining UMAP warning is known and currently acceptable; seed/parallelism can be revisited when that option is added

# Related
- no linked issue

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Dry-run mode now skips early API key validation and avoids persisting run status, making plan-generation faster and side-effect free.

* **Chores**
  * Added continuous checks and test runs via a new CI workflow.
  * Cleaned and consolidated test imports for more reliable, portable tests.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/826?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat(visualization): self-contained HTML report (replaces broken npm step) + fix `--without-html` default](https://github.com/digitaldemocracy2030/kouchou-ai/pull/825)

**作成者:** nishio  
**作成日:** 2026-05-15T10:52:18Z  
**変更:** +742 -34 (4ファイル)  
**マージ日:** 2026-05-18T14:11:55Z  
**内容:**

## 動機

CLI / Coding Agent ユーザーが `kouchou-analyze --config X.json` を走らせても、視覚的なレポートが出ない状態になっています。原因は 2 点:

1. **`packages/analysis-core/src/analysis_core/steps/hierarchical_visualization.py` が壊れている** — `subprocess.Popen("npm run build", cwd="../report")` を呼び出していますが、`../report` ディレクトリは新パッケージ構造には存在しません (リファクタで `apps/public-viewer/` 配下に移動)。step は黙って no-op になり、HTML は生成されません
2. **`--without-html` フラグが常に True** — `argparse` で `action="store_true", default=True` の組み合わせのため、フラグを渡しても渡さなくても True (= HTML スキップ)。`kouchou-analyze --dry-run` で `[SKIP] hierarchical_visualization: skipping html output` が必ず出る

CLI / Agent から散布図を見るには docker compose で admin UI + public-viewer + api をフルスタックで立ち上げて、admin にレポート登録 → public-viewer で閲覧、という重い経路しかありませんでした。

## 変更内容

### 1. `hierarchical_visualization` を Python self-contained HTML 生成に書き換え

`outputs/{run}/hierarchical_result.json` を読んで `outputs/{run}/report.html` を同じディレクトリに書く Python 実装に置換。

- **単一ファイル** (~500 KB for ~300 args)。Plotly は CDN 参照、JSON データは `<script id=\"report-data\" type=\"application/json\">` で inline。Node も pnpm も docker も api サーバも不要、`file://` でも動く
- **デザインは `apps/public-viewer` を踏襲**:
  - 750-px 1 カラムのヘッダー (質問 / argument 件数 / overview)
  - 散布図は軸無し + `apps/public-viewer/components/charts/ScatterChart.tsx` の `softColors` 40 色パレット + クラスタ重心アノテーション (per-character-width の `wrapLabelText` を JS に port)
  - クラスタ詳細リストは `apps/public-viewer/components/report/ClusterOverview.tsx` のスタイル踏襲、下層クラスタは折りたたみ `<details>` に
- **library API**: `build_html(data, title=None, url_pattern=None) -> str` を export。pipeline orchestrator を経由せず、既存の `hierarchical_result.json` から直接 HTML 文字列を得る用途で使える
- **`report_url_pattern` config キー (任意)** — `str.format` style の URL テンプレート (例: `\"https://example.com/r/{comment_id}\"`)。設定すると散布図の点クリックで元コメントが新タブで開き、ホバーに 🔗 ヒントが付く。public-viewer の `enable_source_link` 相当
- **standalone CLI**: `python -m analysis_core.steps.hierarchical_visualization hierarchical_result.json -o report.html [--url-pattern ...]`

### 2. `--without-html` の default を False に flip

`packages/analysis-core/src/analysis_core/__main__.py` で `action=\"store_true\", default=False` に変更。これで:

- デフォルトで HTML が生成される
- `--without-html` を明示的に渡したときだけスキップされる (= フラグが本来の opt-out として機能する)

`PipelineOrchestrator.from_config(without_html=True)` の library API 既定値は変えていないので library 利用者への影響なし。CLI のみの挙動変更です。

## テスト

新規 `packages/analysis-core/tests/test_hierarchical_visualization.py` (11 ケース):

- `build_html` の出力が valid HTML / `<title>` precedence / overview の paragraph 分割 / クラスタラベル埋め込み
- URL pattern の per-arg URL 注入と `ENABLE_SOURCE_LINK` フラグ切り替え
- 40 色パレットが inline されているか
- step 関数: 正常系 (`hierarchical_result.json` から `report.html` 生成) + missing input → `FileNotFoundError`
- step 関数: config の `report_url_pattern` が末端まで流れるか

```
$ pytest packages/analysis-core/tests/test_hierarchical_visualization.py -v
============================== 11 passed in 3.39s ==============================
```

`ruff check` も touched files で clean。

## 互換性

**破壊的変更なし**。

- 既存 `hierarchical_visualization` は `cwd=\"../report\"` を要求していたが、その path は新パッケージ構造には存在しないため事実上 **no-op** だった (HTML は出ていない)。本 PR の新実装は strict superset
- `--without-html` フラグはこれまでも値が常に True で flag を渡しても変化しなかった (= フラグが事実上機能していなかった) ため、観測される動作は「default が False で HTML が出るようになる」だけ
- `PipelineOrchestrator.from_config(without_html=...)` の library API default は維持

## スクリーンショット

300 件規模の `hierarchical_result.json` で生成した `report.html` の見た目:

- ヘッダー: 質問 + arguments 件数 + overview 段落
- 散布図: クラスタ重心に色付きアノテーション、ホバーで argument 本文 + クラスタ名
- クラスタ詳細: level 1 はフラットに列挙、下層は `<details>` で折りたたみ
- 階層レベル切替セレクター + クラスタラベル ON/OFF トグル
- `--url-pattern` ON 時: 点クリックで元コメントへ + マーカーが白枠 + ホバーに 🔗

(ローカルで `python -m analysis_core.steps.hierarchical_visualization /path/to/hierarchical_result.json -o report.html` で再現可能)

## 関連

なし (issue 化前に PR 提出)。

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## Release Notes

* **New Features**
  * Interactive HTML reports featuring scatter plots and hierarchical cluster visualizations
  * Clickable scatter points that open source code comments in the browser
  * Self-contained report files generated automatically with zero external dependencies

* **Improvements**
  * HTML report generation is now enabled by default; use `--without-html` to opt out

* **Documentation**
  * Updated CLI quickstart guide with instructions for viewing reports in the browser

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/825)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat(local-llm): accept full URL in `address`, support `LOCAL_LLM_API_KEY`](https://github.com/digitaldemocracy2030/kouchou-ai/pull/824)

**作成者:** nishio  
**作成日:** 2026-05-15T07:12:30Z  
**変更:** +117 -58 (3ファイル)  
**マージ日:** 2026-05-18T14:00:00Z  
**内容:**

## 動機

`local` provider は Ollama / LM Studio を念頭に `address` を `"host:port"` 形式で受け取り、内部で `f"http://{host}:{port}/v1"` を組み立てています。このため、**OpenAI 互換の HTTPS gateway** (ポート省略 + TLS 終端、自前ホストや組織内ゲートウェイなど) を `local` provider 経由で叩く運用ができません。

例: `local_llm_address: "https://my-gateway.example.com"` を渡すと `int(port_str)` で `ValueError` → fallback で `localhost:11434` に接続失敗。

外部 API を使えない・使いたくない環境で広聴AI を `local` provider で動かそうとした際に発覚した制約です。

## 変更内容

### 1. `_resolve_local_llm_base_url(address)` ヘルパを追加

両ファイル (`apps/api/broadlistening/pipeline/services/llm.py` と `packages/analysis-core/src/analysis_core/services/llm.py`) に同じヘルパを追加し、URL 解決ロジックを 1 箇所に集約。

対応する `address` 形式:

| 入力 | 解決後の `base_url` | 互換性 |
|---|---|---|
| `"localhost:11434"` | `"http://localhost:11434/v1"` | 既存 (Ollama デフォルト) |
| `"127.0.0.1:1234"` | `"http://127.0.0.1:1234/v1"` | 既存 (LM Studio など) |
| `"localhost"` | `"http://localhost:11434/v1"` | 既存 (port 省略時の fallback) |
| `"https://my-gateway.example.com"` | `"https://my-gateway.example.com/v1"` | **新規** (HTTPS + ポート省略) |
| `"https://my-gateway.example.com/v1"` | 同上 | **新規** (`/v1` 既に付与済) |
| `"http://my-gateway:8000/openai"` | `"http://my-gateway:8000/openai/v1"` | **新規** (path 付き gateway) |

### 2. `LOCAL_LLM_API_KEY` 環境変数で API key を渡せるよう拡張

`request_to_local_llm` / `request_to_local_llm_embed` の両方で `os.environ.get(\"LOCAL_LLM_API_KEY\", \"not-needed\")` を参照。未設定なら従来通り `"not-needed"` がそのまま Bearer に乗るので、**Ollama / LM Studio 利用者には挙動変更なし**。認証付き gateway を使う場合のみ env で渡せる。

### 3. リファクタ

`request_to_local_llm` / `request_to_local_llm_embed` が同じ URL パースロジックを 4 箇所で重複していたのを helper 1 つに集約。

### 4. テスト

`packages/analysis-core/tests/test_local_llm_base_url.py` に parametrized 単体テストを追加 (11 ケース、後方互換 + 新規対応 + malformed fallback)。

```
$ pytest packages/analysis-core/tests/test_local_llm_base_url.py -v
============================== 11 passed in 7.06s ==============================
```

## 互換性

**破壊的変更なし**。

- 既存の `"host:port"` 形式は完全に同一の `base_url` を返す
- `LOCAL_LLM_API_KEY` 未設定時は従来通り `"not-needed"` を使う
- ドキュメンテーション: docstring の `address` 説明を「`"127.0.0.1:1234"` または `"https://..."`」に更新

## 動作確認

OpenAI 互換の HTTPS gateway 経由で `provider=local` のフルパイプライン (extraction / hierarchical_initial_labelling / hierarchical_merge_labelling / hierarchical_overview の各 LLM ステップ + ローカル embedding) を完走できることを確認済み。

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Enhanced local LLM configuration to support multiple address formats including full URLs and HTTPS gateways
  * Added environment variable support for local LLM API key configuration

* **Improvements**
  * Automatic OpenAI-compatible URL normalization with `/v1` path handling
  * Updated documentation for address format requirements

* **Tests**
  * Added test coverage for address format validation and normalization

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/824)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [chore(deps): bump next from 16.2.3 to 16.2.6](https://github.com/digitaldemocracy2030/kouchou-ai/pull/823)

**作成者:** dependabot[bot]  
**作成日:** 2026-05-13T00:14:10Z  
**変更:** +171 -143 (3ファイル)  
**マージ日:** 2026-05-18T05:50:48Z  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 16.2.3 to 16.2.6.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v16.2.6</h2>
<blockquote>
<p>[!NOTE]
This release contains security fixes and backported bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Security Fixes</h3>
<p>The following advisories have been addressed:</p>
<p><strong>High:</strong></p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj">GHSA-8h8q-6873-q5fj: Denial of Service with Server Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f">GHSA-267c-6grr-h53f: Middleware / Proxy bypass in App Router applications via segment-prefetch routes</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-26hh-7cqf-hhc6">GHSA-26hh-7cqf-hhc6: Middleware / Proxy bypass in App Router applications via segment-prefetch routes - <strong>Incomplete Fix Follow-Up</strong></a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx">GHSA-mg66-mrh9-m8jx: Denial of Service via connection exhaustion in applications using Cache Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-492v-c6pp-mqqv">GHSA-492v-c6pp-mqqv: Middleware / Proxy bypass through dynamic route parameter injection</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-c4j6-fc7j-m34r">GHSA-c4j6-fc7j-m34r: Server-side request forgery in applications using WebSocket upgrades</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-36qx-fr4f-26g5">GHSA-36qx-fr4f-26g5: Middleware / Proxy bypass in Pages Router applications using i18n</a></li>
</ul>
<p><strong>Moderate:</strong></p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-ffhc-5mcf-pf4q">GHSA-ffhc-5mcf-pf4q: Cross-site scripting in App Router applications using CSP nonces</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-gx5p-jg67-6x7h">GHSA-gx5p-jg67-6x7h: Cross-site scripting in beforeInteractive scripts with untrusted input</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-h64f-5h5j-jqjh">GHSA-h64f-5h5j-jqjh: Denial of Service in the Image Optimization API</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-wfc6-r584-vfw7">GHSA-wfc6-r584-vfw7: Cache poisoning in React Server Component responses</a></li>
</ul>
<p><strong>Low:</strong></p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-vfv6-92ff-j949">GHSA-vfv6-92ff-j949: Cache poisoning via collisions in React Server Component cache-busting</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-3g8h-86w9-wvmq">GHSA-3g8h-86w9-wvmq: Middleware / Proxy redirects can be cache-poisoned</a></li>
</ul>
<h3>Core Changes</h3>
<ul>
<li>fix: preserve HTTP access fallbacks during prerender recovery (<a href="https://redirect.github.com/vercel/next.js/issues/92231">#92231</a>)</li>
<li>Fix fallback route params case in app-page handler (<a href="https://redirect.github.com/vercel/next.js/issues/91737">#91737</a>)</li>
<li>Fix invalid HTML response for route-level RSC requests in deployment adapter (<a href="https://redirect.github.com/vercel/next.js/issues/91541">#91541</a>)</li>
<li>Patch setHeader for direct route handlers (<a href="https://redirect.github.com/vercel/next.js/issues/93101">#93101</a>)</li>
<li>Include deployment id in <code>cacheHandlers</code> keys (<a href="https://redirect.github.com/vercel/next.js/issues/93453">#93453</a>)</li>
<li>Fix double-encoding of URL pathname parts in client param parsing (<a href="https://redirect.github.com/vercel/next.js/issues/93491">#93491</a>)</li>
</ul>
<h2>v16.2.5</h2>
<blockquote>
<p>[!NOTE]
This release contains security fixes and backported bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Security Fixes</h3>
<p>The following advisories have been addressed:</p>
<p><strong>High:</strong></p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj">GHSA-8h8q-6873-q5fj: Denial of Service with Server Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f">GHSA-267c-6grr-h53f: Middleware / Proxy bypass in App Router applications via segment-prefetch routes</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx">GHSA-mg66-mrh9-m8jx: Denial of Service via connection exhaustion in applications using Cache Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-492v-c6pp-mqqv">GHSA-492v-c6pp-mqqv: Middleware / Proxy bypass through dynamic route parameter injection</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-c4j6-fc7j-m34r">GHSA-c4j6-fc7j-m34r: Server-side request forgery in applications using WebSocket upgrades</a></li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/ee6e79b1792a4d401ddf2480f40a83549fe8e722"><code>ee6e79b</code></a> v16.2.6</li>
<li><a href="https://github.com/vercel/next.js/commit/afa053d9eb9c2a68c7eba43e84fe6bed8babcd45"><code>afa053d</code></a> Turbopack: Match proxy matchers with webpack implementation (<a href="https://redirect.github.com/vercel/next.js/issues/93594">#93594</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/97a154e5bbee0cb1ac3fb8aa4db66ac36e796e3d"><code>97a154e</code></a> Turbopack: Fix middleware matcher suffix (<a href="https://redirect.github.com/vercel/next.js/issues/93590">#93590</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/83899bc89103d4df1479e065c7c1e09d4698a7b6"><code>83899bc</code></a> [backport] Disable build caches for production/staging/force-preview deploys ...</li>
<li><a href="https://github.com/vercel/next.js/commit/7b222b90954d607fc28a34e9b360a9b1636bc206"><code>7b222b9</code></a> [backport][test] Pin package manager to patch versions (<a href="https://redirect.github.com/vercel/next.js/issues/93595">#93595</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/a8dc24f1fe23d4a22d24fac734837f7c824138f7"><code>a8dc24f</code></a> [backport] Turbopack: more strict vergen setup (<a href="https://redirect.github.com/vercel/next.js/issues/93587">#93587</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/766148f9cd48c0e218acafcd0f15defc14871bf4"><code>766148f</code></a> v16.2.5</li>
<li><a href="https://github.com/vercel/next.js/commit/0dd94836a8b43209fcfefa448c141683c22c1a27"><code>0dd9483</code></a> fix: add explicit checks for RSC header (<a href="https://redirect.github.com/vercel/next.js/issues/83">#83</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/98">#98</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/d166096c399c4fc4e09cd2d1bf26dca6579a855d"><code>d166096</code></a> fix proxy matching for segment prefetch URLs (<a href="https://redirect.github.com/vercel/next.js/issues/89">#89</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/96">#96</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/9d50c0b7190f59c470308578e12882788819f14c"><code>9d50c0b</code></a> Strip next-resume header from incoming requests (<a href="https://redirect.github.com/vercel/next.js/issues/92">#92</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/vercel/next.js/compare/v16.2.3...v16.2.6">compare view</a></li>
</ul>
</details>
<details>
<summary>Maintainer changes</summary>
<p>This version was pushed to npm by <a href="https://www.npmjs.com/~GitHub%20Actions">GitHub Actions</a>, a new releaser for next since your current version.</p>
</details>
<br />


**コメント:** なし

---

### [chore(deps): bump next from 16.1.5 to 16.2.6 in /utils/dummy-server](https://github.com/digitaldemocracy2030/kouchou-ai/pull/822)

**作成者:** dependabot[bot]  
**作成日:** 2026-05-12T08:03:37Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2026-05-18T05:43:13Z  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 16.1.5 to 16.2.6.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v16.2.6</h2>
<p>This release contains security fixes for the following advisories:</p>
<p>High:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj">GHSA-8h8q-6873-q5fj: Denial of Service with Server Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f">GHSA-267c-6grr-h53f: Middleware / Proxy bypass in App Router applications via segment-prefetch routes</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-26hh-7cqf-hhc6">GHSA-26hh-7cqf-hhc6: Middleware / Proxy bypass in App Router applications via segment-prefetch routes - Incomplete Fix Follow-Up</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx">GHSA-mg66-mrh9-m8jx: Denial of Service via connection exhaustion in applications using Cache Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-492v-c6pp-mqqv">GHSA-492v-c6pp-mqqv: Middleware / Proxy bypass through dynamic route parameter injection</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-c4j6-fc7j-m34r">GHSA-c4j6-fc7j-m34r: Server-side request forgery in applications using WebSocket upgrades</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-36qx-fr4f-26g5">GHSA-36qx-fr4f-26g5: Middleware / Proxy bypass in Pages Router applications using i18n</a></li>
</ul>
<p>Moderate:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-ffhc-5mcf-pf4q">GHSA-ffhc-5mcf-pf4q: Cross-site scripting in App Router applications using CSP nonces</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-gx5p-jg67-6x7h">GHSA-gx5p-jg67-6x7h: Cross-site scripting in beforeInteractive scripts with untrusted input</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-h64f-5h5j-jqjh">GHSA-h64f-5h5j-jqjh: Denial of Service in the Image Optimization API</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-wfc6-r584-vfw7">GHSA-wfc6-r584-vfw7: Cache poisoning in React Server Component responses</a></li>
</ul>
<p>Low:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-vfv6-92ff-j949">GHSA-vfv6-92ff-j949: Cache poisoning via collisions in React Server Component cache-busting</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-3g8h-86w9-wvmq">GHSA-3g8h-86w9-wvmq: Middleware / Proxy redirects can be cache-poisoned</a></li>
</ul>
<h2>v16.2.5</h2>
<p>This release contains security fixes for the following advisories:</p>
<p>High:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj">GHSA-8h8q-6873-q5fj: Denial of Service with Server Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f">GHSA-267c-6grr-h53f: Middleware / Proxy bypass in App Router applications via segment-prefetch routes</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx">GHSA-mg66-mrh9-m8jx: Denial of Service via connection exhaustion in applications using Cache Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-492v-c6pp-mqqv">GHSA-492v-c6pp-mqqv: Middleware / Proxy bypass through dynamic route parameter injection</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-c4j6-fc7j-m34r">GHSA-c4j6-fc7j-m34r: Server-side request forgery in applications using WebSocket upgrades</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-36qx-fr4f-26g5">GHSA-36qx-fr4f-26g5: Middleware / Proxy bypass in Pages Router applications using i18n</a></li>
</ul>
<p>Moderate:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-ffhc-5mcf-pf4q">GHSA-ffhc-5mcf-pf4q: Cross-site scripting in App Router applications using CSP nonces</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-gx5p-jg67-6x7h">GHSA-gx5p-jg67-6x7h: Cross-site scripting in beforeInteractive scripts with untrusted input</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-h64f-5h5j-jqjh">GHSA-h64f-5h5j-jqjh: Denial of Service in the Image Optimization API</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-wfc6-r584-vfw7">GHSA-wfc6-r584-vfw7: Cache poisoning in React Server Component responses</a></li>
</ul>
<p>Low:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-vfv6-92ff-j949">GHSA-vfv6-92ff-j949: Cache poisoning via collisions in React Server Component cache-busting</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-3g8h-86w9-wvmq">GHSA-3g8h-86w9-wvmq: Middleware / Proxy redirects can be cache-poisoned</a></li>
</ul>
<h2>v16.2.4</h2>
<blockquote>
<p>[!NOTE]
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>chore: Bump reqwest to 0.13.2 (Fixes Google Fonts with Turbopack for Windows on ARM64) (<a href="https://redirect.github.com/vercel/next.js/issues/92713">#92713</a>)</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/ee6e79b1792a4d401ddf2480f40a83549fe8e722"><code>ee6e79b</code></a> v16.2.6</li>
<li><a href="https://github.com/vercel/next.js/commit/afa053d9eb9c2a68c7eba43e84fe6bed8babcd45"><code>afa053d</code></a> Turbopack: Match proxy matchers with webpack implementation (<a href="https://redirect.github.com/vercel/next.js/issues/93594">#93594</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/97a154e5bbee0cb1ac3fb8aa4db66ac36e796e3d"><code>97a154e</code></a> Turbopack: Fix middleware matcher suffix (<a href="https://redirect.github.com/vercel/next.js/issues/93590">#93590</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/83899bc89103d4df1479e065c7c1e09d4698a7b6"><code>83899bc</code></a> [backport] Disable build caches for production/staging/force-preview deploys ...</li>
<li><a href="https://github.com/vercel/next.js/commit/7b222b90954d607fc28a34e9b360a9b1636bc206"><code>7b222b9</code></a> [backport][test] Pin package manager to patch versions (<a href="https://redirect.github.com/vercel/next.js/issues/93595">#93595</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/a8dc24f1fe23d4a22d24fac734837f7c824138f7"><code>a8dc24f</code></a> [backport] Turbopack: more strict vergen setup (<a href="https://redirect.github.com/vercel/next.js/issues/93587">#93587</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/766148f9cd48c0e218acafcd0f15defc14871bf4"><code>766148f</code></a> v16.2.5</li>
<li><a href="https://github.com/vercel/next.js/commit/0dd94836a8b43209fcfefa448c141683c22c1a27"><code>0dd9483</code></a> fix: add explicit checks for RSC header (<a href="https://redirect.github.com/vercel/next.js/issues/83">#83</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/98">#98</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/d166096c399c4fc4e09cd2d1bf26dca6579a855d"><code>d166096</code></a> fix proxy matching for segment prefetch URLs (<a href="https://redirect.github.com/vercel/next.js/issues/89">#89</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/96">#96</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/9d50c0b7190f59c470308578e12882788819f14c"><code>9d50c0b</code></a> Strip next-resume header from incoming requests (<a href="https://redirect.github.com/vercel/next.js/issues/92">#92</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/vercel/next.js/compare/v16.1.5...v16.2.6">compare view</a></li>
</ul>
</details>
<details>
<summary>Maintainer changes</summary>
<p>This version was pushed to npm by <a href="https://www.npmjs.com/~GitHub%20Actions">GitHub Actions</a>, a new releaser for next since your current version.</p>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=16.1.5&new-version=16.2.6)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>Dependabot commands and options</summary>
<br />

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/digitaldemocracy2030/kouchou-ai/network/alerts).

</details>

**コメント:** なし

---

### [誤混入したCI設定を見直し、CodeQL定期実行とCodeRabbit設定を調整](https://github.com/digitaldemocracy2030/kouchou-ai/pull/817)

**作成者:** shingo-ohki  
**作成日:** 2026-03-10T14:38:54Z  
**変更:** +16 -1 (2ファイル)  
**マージ日:** 2026-05-18T13:57:21Z  
**内容:**

# 変更の概要
#813 で混入した .coderabbit.yaml と codeql.yml は意図した追加ではありませんでしたが、#815 での議論を踏まえ、設定内容を見直して反映しました。

本PRでは以下を設定しています。

- CodeRabbit
  - Draft PR では自動レビューしない（drafts: false）
- CodeQL
  - main への push / main 向け PR で解析を実行
  - 週1回の定期実行（JST 月曜 03:00）
  - 手動実行（workflow_dispatch）を可能に
  - 同一refの重複実行を抑制（concurrency）
  - docs系変更のみの場合は実行しない（paths-ignore）

# 変更の背景
- #813 で coderabbit, codeql の設定が入る
- #815 で上記の変更が意図したものではなかったことが分かる
- せっかくなので適切な値にしようというのが本PR

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

* **Chores**
  * Refined code review automation configuration.
  * Enhanced security scanning workflow with improved path-based exclusions for non-code files.
  * Added scheduled scanning triggers and concurrency management for continuous integration processes.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Show clear Japanese error on static build with no published reports](https://github.com/digitaldemocracy2030/kouchou-ai/pull/814)

**作成者:** Copilot  
**作成日:** 2026-03-02T11:06:09Z  
**変更:** +19 -2 (1ファイル)  
**マージ日:** 2026-05-19T02:15:58Z  
**内容:**

When `generateStaticParams()` returns `[]` during a static export build (no published reports), Next.js emits a cryptic error: `Page "/[slug]/opengraph-image.png" is missing "generateStaticParams()"`. The actual cause — no published reports — is not surfaced.

## Changes

- **`apps/public-viewer/app/[slug]/page.tsx`** — `generateStaticParams()` now fails fast with a clear Japanese message when `NEXT_PUBLIC_OUTPUT_MODE=export`:
  - Empty report list → logs actionable message and `process.exit(1)` before Next.js hits the confusing error
  - API fetch failure → logs the raw error + a Japanese message, then exits

```
❌ 静的HTML出力エラー: 公開状態のレポートが見つかりません。
静的HTML出力を行うには、少なくとも1つのレポートを公開状態にしてください。
```

Non-export (SSR/dev) builds are unaffected — they continue to return `[]` silently on fetch errors.

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>[BUG]公開状態にしたレポートがない状態で静的HTML出力をしたときのエラーメッセージがわかりにくい</issue_title>
> <issue_description>### 概要
> 
> ```
> client-static-build-1  |     '[Error: Page "/[slug]/opengraph-image.png" is missing "generateStaticParams()" so it cannot be used with "output: export" config.]\n' +
> ```
> 
> ### 再現手順
> 
> 1. 恐らく公開状態にしたレポートがない状態で静的HTML出力をすると発生する
> 
> ### 期待する動作
> 
> エラーメッセージがわかりにくい。公開状態にしたレポートがない状態で静的HTML出力をしたときには早い段階でわかりやすい日本語のメッセージを出すべきである。
> </issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes digitaldemocracy2030/kouchou-ai#726

<!-- START COPILOT CODING AGENT TIPS -->
---

🔒 GitHub Advanced Security automatically protects Copilot coding agent pull requests. You can protect all pull requests by enabling Advanced Security for your repositories. [Learn more about Advanced Security.](https://gh.io/cca-advanced-security)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Improved build reliability with enhanced validation of required content during static exports. Builds now fail fast with clearer error messages when expected content is unavailable, preventing silent failures or incomplete deployments.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/814?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (1件)

### [[codex] Start workflow defaultization groundwork](https://github.com/digitaldemocracy2030/kouchou-ai/pull/840)

**作成者:** nishio  
**作成日:** 2026-05-20T03:17:17Z  
**変更:** +882 -76 (17ファイル)  
**内容:**

## What changed

This PR starts the workflow-defaultization refactor for `analysis-core`.

- seed the initial `comments` artifact in `WorkflowEngine` from `config["input"]`
- accept both `without_html` and legacy `without-html` when evaluating workflow visualization conditions
- keep both config key variants in sync during legacy initialization while both execution paths coexist
- align the built-in hierarchical visualization plugin with the current self-contained `report.html` contract
- add regression tests for workflow input seeding, legacy `without-html` handling, and visualization plugin output path

## Why

`run_workflow()` was not ready to become the default path because a few concrete integration gaps remained:

- the workflow engine had no initial artifact for extraction
- legacy CLI/config flags were not fully normalized for workflow conditions
- the visualization plugin still described and returned an older HTML output contract

This PR addresses those gaps first so the larger refactor can proceed in smaller stages.

## Impact

- workflow-based execution can now see the input CSV as a starting artifact
- visualization-step gating is less brittle while legacy and workflow paths coexist
- plugin metadata/output path now matches the current self-contained HTML implementation

## Validation

- `work/kouchou-ai/packages/analysis-core/.venv/bin/python -m pytest work/kouchou-ai/packages/analysis-core/tests/test_workflow_engine.py work/kouchou-ai/packages/analysis-core/tests/test_builtin_plugins.py work/kouchou-ai/packages/analysis-core/tests/test_hierarchical_visualization.py -q`

## Next steps

This is intentionally only the first slice. Remaining work for workflow defaultization still includes status persistence / rerun planning and other legacy execution-path responsibilities.


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Bug Fixes**
  * Fixed config flag handling to accept both underscore and dash variants for backward compatibility.

* **New Features**
  * Persisted hierarchical workflow status and progress across runs, including token totals and completed-step records.
  * Workflow engine: lifecycle hooks for step start/complete, ability to skip steps, and seeding of initial artifacts.
  * Visualization now generates a self-contained HTML report via pure-Python.

* **Tests**
  * Added regression and orchestration tests covering flag reconciliation, status persistence, callbacks, skipping, and artifact seeding.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/840?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(9件)

### [feat: Make UMAP random_state configurable to enable parallelization](https://github.com/digitaldemocracy2030/kouchou-ai/pull/810)

**作成者:** Copilot  
**作成日:** 2026-02-28T18:59:01Z  
**変更:** +88 -10 (15ファイル)  
**内容:**

UMAP's `random_state=42` was hardcoded, which silently disables parallelization per <a href="https://umap-learn.readthedocs.io/en/latest/reproducibility.html">UMAP's own docs</a>. Since LLM-generated embeddings upstream are already non-deterministic, strict reproducibility provides little practical value.

## Changes

- **Default behavior changed**: `random_state` now defaults to `None` (parallelization enabled) instead of `42`
- **New config option `enable_reproducibility`**: Set to `true` to restore `random_state=42` for reproducible runs (e.g., when reusing cached embeddings)
- **Admin UI toggle**: "UMAPの再現性を有効にする" checkbox added to the report generation settings panel, allowing users to opt into reproducible (non-parallel) mode from the frontend

### Affected files

**Analysis core / API pipeline**
- `steps/hierarchical_clustering.py` (both `packages/analysis-core` and `apps/api`) — reads `enable_reproducibility` from config
- `plugins/builtin/hierarchical_clustering.py` — forwards the option through the plugin layer
- `workflows/hierarchical_default.py` — wires `enable_reproducibility` from workflow config
- `apps/api/src/schemas/report_config.py` — adds `enable_reproducibility: bool = False`
- `packages/report-schema/src/index.ts` — adds `enable_reproducibility?: boolean`

**API request/response schemas**
- `apps/api/src/schemas/admin_report.py` — adds `enable_reproducibility` to `ReportInput` and `ReportDuplicateOverrides`
- `apps/api/src/services/report_launcher.py` — passes `enable_reproducibility` through `_build_config()`
- `apps/api/src/services/report_duplicate.py` — handles `enable_reproducibility` in `_apply_overrides()`

**Admin frontend**
- `apps/admin/app/create/hooks/useAISettings.ts` — adds `enableReproducibility` state with localStorage persistence
- `apps/admin/app/create/components/AISettingsSection.tsx` — adds checkbox UI for the reproducibility setting
- `apps/admin/app/create/api/createReport.ts` — passes `enable_reproducibility` to the API
- `apps/admin/app/create/page.tsx` — wires `enableReproducibility` from hook to API call and settings panel
- `apps/admin/app/reuse/[slug]/page.tsx` — loads `enable_reproducibility` from existing config, surfaces it in the UI, and includes it in overrides when changed
- `apps/admin/app/_components/ReportCard/DuplicateReportDialog/actions.ts` — adds `enable_reproducibility` to the duplicate overrides type

### Usage

```json
{
  "hierarchical_clustering": {
    "cluster_nums": [3, 6, 12],
    "enable_reproducibility": true
  }
}
```

Omitting `enable_reproducibility` (or setting it to `false`) enables parallelization. Setting it to `true` restores the previous deterministic behavior. The same toggle is available in the admin UI under "レポート生成設定".

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>[FEATURE] UMAPを並列化したい</issue_title>
> <issue_description># 背景
> 
> 現在はrandom_stateが有効化されており、再現性があるコードになっているが、
> random_stateを有効化すると、並列化が効かなくなる
> 
> packages/analysis-core/src/analysis_core/steps/hierarchical_clustering.py（59行目）
> umap_model = UMAP(random_state=42, n_components=2, n_neighbors=n_neighbors)
> 
> 公式ドキュメントにもその記述がある
> 
> https://umap-learn.readthedocs.io/en/latest/reproducibility.html
> 
> 既に入力データに再現性が無いので、後段が再現性が必要ではないと考える。
> LLMが前段に噛まされており、random seedを有効化しても、ハードウェアの揺らぎ（計算するノードによって浮動小数点の精度が異なる）や計算順序の揺らぎによって、出力データが異なる傾向にある。
> 
> # 提案内容
> 
> random_stateをNoneにして、並列化を有効にするオプションを提供する
> 
> # 懸念事項
> 
> 現在の広聴AIはエンベディングの再利用が可能になってるので、umapの再現性オプションは必要かもしれない
> 
> </issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes digitaldemocracy2030/kouchou-ai#809

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/digitaldemocracy2030/kouchou-ai/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.


**コメント:** なし

---

### [fix: prevent crash in Overview when result.config is undefined](https://github.com/digitaldemocracy2030/kouchou-ai/pull/802)

**作成者:** Copilot  
**作成日:** 2026-02-22T02:10:59Z  
**変更:** +1 -1 (1ファイル)  
**内容:**

`Overview.tsx` crashes with a `TypeError` when `result.config` is `undefined` — occurring before report data fully loads or when data lacking a `config` field is passed.

## Change

- **`components/report/Overview.tsx`**: Use optional chaining to guard against `undefined` config:

```tsx
// Before
{result.config.question}

// After
{result.config?.question}
```

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>fix: Overview コンポーネントで result.config が undefined の場合にクラッシュする</issue_title>
> <issue_description>## 概要
> 
> `Overview.tsx` の16行目で `result.config.question` にアクセスする際、`result.config` が `undefined` の場合に TypeError が発生しアプリがクラッシュする。
> 
> ## エラー内容
> 
> ```
> TypeError: Cannot read properties of undefined (reading 'question')
>     at Overview (components\report\Overview.tsx:16:24)
> ```
> 
> ## 再現条件
> 
> - レポートデータのロード前にコンポーネントがレンダリングされる
> - または `result.config` を持たないレポートデータが渡される
> 
> ## 期待される動作
> 
> `result.config` が未定義の場合でもクラッシュせず、適切なフォールバック（ローディング表示やデフォルト値）を表示する。
> 
> ## 修正案
> 
> `result.config` の存在チェックを追加するか、optional chaining (`result.config?.question`) を使用する。</issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes digitaldemocracy2030/kouchou-ai#800

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/digitaldemocracy2030/kouchou-ai/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.


**コメント:** なし

---

### [fix: resolve duplicate React instance crash in local dev (pnpm workspace)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/801)

**作成者:** Copilot  
**作成日:** 2026-02-22T02:10:53Z  
**変更:** +6 -0 (1ファイル)  
**内容:**

In a pnpm workspace, running `make client-dev` from the repo root caused Next.js dev overlay to load a different React instance (root `node_modules`, v19.1.0) than the app itself (`apps/public-viewer/node_modules`, v19.2.3). The mismatched dispatchers result in `ReactCurrentDispatcher.current` being `null` on `useReducer`, crashing the dev overlay.

## Changes

- **`package.json` (root)** — add `pnpm.overrides` to pin `react` and `react-dom` to `19.2.3` across the entire workspace, ensuring a single React instance regardless of where pnpm resolves the dependency

```json
"pnpm": {
  "overrides": {
    "react": "19.2.3",
    "react-dom": "19.2.3"
  }
}
```

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>fix: ローカル開発環境でのReactバージョン不一致によるdev overlay クラッシュ</issue_title>
> <issue_description>## 問題
> 
> `make client-dev` でローカル開発環境を起動すると、以下のエラーが発生する。
> 
> ```
> TypeError: Cannot read properties of null (reading 'useReducer')
>     at process.env.NODE_ENV.exports.useReducer (react.development.js:1215:33)
>     at useErrorOverlayReducer (react-dev-overlay/shared.js:126:34)
>     at usePagesDevOverlay (pages/hooks.js:18:66)
>     at PagesDevOverlay (pages/pages-dev-overlay.js:19:71)
>     at ReactDevOverlay (next-dev-server.js:103:12)
> ```
> 
> ## 原因
> 
> pnpm ワークスペース環境で React のバージョンが2箇所に存在し、インスタンスが一致しない。
> 
> | 場所 | React バージョン |
> |---|---|
> | ルート `node_modules/react` | **19.1.0** |
> | `apps/public-viewer/node_modules/react` | **19.2.3** |
> 
> `pnpm --filter @kouchou-ai/public-viewer dev`（`make client-dev`）をルートから実行すると、Next.js の開発インフラ（dev overlay 等）はルートの React 19.1.0 を使い、アプリ本体は React 19.2.3 を使う。2つの React インスタンスでディスパッチャーが共有されないため、`useReducer` 呼び出し時に `ReactCurrentDispatcher.current` が null になる。
> 
> ## 回避策
> 
> 現時点での回避策：
> 
> - **Docker 使用**（推奨）: `docker compose up` はコンテナ内で完結するため問題なし
> - **直接実行**: `cd apps/public-viewer && pnpm dev` で実行するとルートの React が介在しない
> 
> ## 恒久対応案
> 
> ルートの `package.json` の React/React-DOM を 19.2.3 に揃える、または pnpm の `overrides` で統一する。
> 
> ```json
> // package.json (root)
> {
>   "pnpm": {
>     "overrides": {
>       "react": "19.2.3",
>       "react-dom": "19.2.3"
>     }
>   }
> }
> ```</issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes digitaldemocracy2030/kouchou-ai#799

<!-- START COPILOT CODING AGENT TIPS -->
---

💬 We'd love your input! Share your thoughts on Copilot coding agent in our [2 minute survey](https://gh.io/copilot-coding-agent-survey).


**コメント:** なし

---

### [docs: add plan for llm grouping and capability auto-detection](https://github.com/digitaldemocracy2030/kouchou-ai/pull/794)

**作成者:** nishio  
**作成日:** 2026-02-12T06:58:07Z  
**変更:** +275 -0 (1ファイル)  
**内容:**

## Summary\n- add initial implementation plan document for LLM grouping and capability auto-detection\n- clarify short-term compatibility approach and long-term capability-driven visualization gating\n\n## Notes\n- this PR is intended as a base branch to stack follow-up commits\n- unrelated local files are intentionally excluded\n

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **Documentation**
  * AI搭載オピニオングループ化機能の今後の計画書を追加。今後の開発ロードマップを定義します。

**注:** この変更は内部計画ドキュメントであり、ユーザー向けの機能変更は含まれていません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Implement Content Security Policy (CSP) headers and add local model f…](https://github.com/digitaldemocracy2030/kouchou-ai/pull/735)

**作成者:** Devesh36  
**作成日:** 2025-12-05T15:55:58Z  
**変更:** +331 -12 (8ファイル)  
**内容:**

# PR: Issue #685 リモート環境でのHTTPアクセス時に発生するCSPおよびJavaScriptエラーを修正

## 変更の概要

このPRでは、Issue #685で報告されたリモート環境でのHTTPアクセス時に発生するCSP（Content Security Policy）エラーおよびJavaScriptエラーを以下の4つの変更で解決します：

### 1. **crypto.randomUUID ポリフィル追加**
- `window.crypto.randomUUID`がサポートされていない環境に対応するポリフィルを実装
- ブラウザ環境でのみ実行され、既に存在する場合は上書きしない（冪等性を確保）
- RFC 4122準拠のUUID v4を生成

**ファイル:**
- `client/app/polyfills/crypto-uuid.ts` (新規作成)
- `client-admin/app/polyfills/crypto-uuid.ts` (新規作成)
- `client/app/layout.tsx` (初期化処理追加)
- `client-admin/app/layout.tsx` (初期化処理追加)

### 2. **Content Security Policy（CSP）の動的設定**
- CSPヘッダーを環境変数ベースで動的に生成
- `NEXT_PUBLIC_SITE_URL`と`NEXT_PUBLIC_API_BASEPATH`から取得したドメイン/IPを許可リストに追加
- HTTP/HTTPS両方のアクセスと、WebSocket (ws/wss) をサポート
- localhost開発環境と公開IP環境の両方に対応

**ファイル:**
- `client/next.config.ts` (CSPヘッダー関数を追加)
- `client-admin/next.config.ts` (CSPヘッダー関数を追加)

### 3. **画像URL処理の強化**
- 新しい`getRemoteImageUrl()`ヘルパー関数を追加
- リモートHTTPアクセス時に正しいドメイン/IPを含むURLを生成
- 既存の`getImageFromServerSrc()`と`getRelativeUrl()`は変更なし

**ファイル:**
- `client/app/utils/image-src.ts` (新関数追加)

### 4. **LocalLLM プロバイダー選択時の自動フェッチ**
- LocalLLMプロバイダー選択時にモデルリストを自動取得
- ユーザーが手動で「モデル取得」ボタンをクリックする必要がなくなる
- 失敗時はコンソールに警告をログし、UIには表示しない

**ファイル:**
- `client-admin/app/create/hooks/useAISettings.ts` (useEffect追加)

---

## スクリーンショット

### 変更前
```
[LocalLLMプロバイダー選択]
  ↓
[ユーザーが「モデル取得」ボタンをクリック]
  ↓
[モデルリストが表示される]
```

### 変更後
```
[LocalLLMプロバイダー選択]
  ↓
[自動的にモデルリストを取得して表示] ✨ 自動化
  ↓
[またはユーザーが「モデル取得」ボタンで手動更新可能]
```

**CSP動作:**
- localhost: `img-src 'self' ... http://localhost:3000 ...`
- 公開IP: `img-src 'self' ... http://192.168.1.100:3000 ...`

---

## 変更の背景

### Issue #685の内容
- リモート環境（公開IP経由）でHTTPアクセス時にCSPエラーが発生
- `crypto.randomUUID`が一部環境で未定義
- ローカルLLMサーバー選択時にモデルリストが自動取得されない
- 画像やスクリプトが正しく読み込まれない

### 根本原因
1. **CSP設定が静的** - ローカルホストのみを許可、公開IP未対応
2. **ポリフィル欠落** - 古いブラウザ環境では`crypto.randomUUID`未提供
3. **自動フェッチなし** - LocalLLM選択時に手動で模型リストを取得する必要
4. **URL処理が不完全** - リモートアクセス時にドメイン/IPが正しく含まれない

### 解決方法
- 環境変数から動的にCSPを構築
- ポリフィルで互換性を確保
- `useEffect`で自動フェッチを実装
- URLビルダーヘルパーで正しいドメイン/IPを処理

---

## 関連Issue

- **Issue #685**: [BUG] リモート環境でのHTTPアクセス時に発生するCSPおよびJavaScriptエラーについて
  - https://github.com/digitaldemocracy2030/kouchou-ai/issues/685

---

## 動作確認の結果

### ✅ ローカル開発環境での確認
```
環境: http://localhost:3000, http://localhost:4000
- ブラウザコンソール: CSPエラーなし ✓
- 画像読み込み: 正常 ✓
- LocalLLMプロバイダー選択: モデル自動取得・表示 ✓
- UUID生成: 正常 ✓
```

### ✅ リモートHTTPアクセスでの確認
```
環境: NEXT_PUBLIC_SITE_URL=http://192.168.1.100:3000
- CSPヘッダー: img-src, connect-src, script-src に 192.168.1.100 を許可 ✓
- ブラウザコンソール: CSPエラーなし ✓
- 画像読み込み: http://192.168.1.100 からの読み込み成功 ✓
- WebSocket接続: ws://192.168.1.100 OK ✓
```

### ✅ LocalLLMプロバイダー動作確認
```
手順:
1. client-admin管理画面でレポート作成ページを開く
2. AIプロバイダーを「LocalLLM」に選択
3. (確認) モデルリストが自動的に取得・表示される
4. コンソール確認: エラーなし（またはサーバー接続失敗時のみ警告）
```

### ✅ ポリフィル動作確認
```
// 既存コードは変更不要
const id = crypto.randomUUID(); // 正常に動作
```

### ✅ 環境変数設定での確認
```bash
# ローカル環境
NEXT_PUBLIC_SITE_URL=http://localhost:3000
NEXT_PUBLIC_API_BASEPATH=http://localhost:8000
NEXT_PUBLIC_LOCAL_LLM_ADDRESS=ollama:11434
→ すべて正常に動作

# リモート環境
NEXT_PUBLIC_SITE_URL=http://192.168.1.100:3000
NEXT_PUBLIC_API_BASEPATH=http://192.168.1.100:8000
NEXT_PUBLIC_LOCAL_LLM_ADDRESS=192.168.1.50:11434
→ すべて正常に動作、CSP違反なし
```

### ✅ 後方互換性確認
```
- 既存の getImageFromServerSrc() は変更なし ✓
- 既存の getRelativeUrl() は変更なし ✓
- crypto.randomUUID() 呼び出しコードは変更不要 ✓
- LocalLLMモデル取得ボタンは引き続き使用可能 ✓
```

---

## CLAへの同意

- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

---

## マージ前のチェックリスト（レビュアーがマージ前に確認してください）

- [x] CIが全て通過している
- [ ] 単体テストが実装されているか
  - **注**: crypto ポリフィル、CSP ヘッダー、LocalLLM 自動フェッチのテストは別途追加予定
  - 現在: 手動確認で動作検証済み
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

### レビュー時の確認項目

1. **CSP設定の安全性**
   - [ ] `buildCSPHeader()` で環境変数から正しくドメイン/IPを抽出しているか
   - [ ] `'unsafe-inline'` や `'unsafe-eval'` は必要最小限か
   - [ ] WebSocket (ws/wss) のサポートは適切か

2. **ポリフィル実装**
   - [ ] `typeof window !== "undefined"` でSSR時の実行を防いでいるか
   - [ ] 冪等性が確保されているか（既存の関数を上書きしない）
   - [ ] UUID v4フォーマットが正しいか

3. **LocalLLM自動フェッチ**
   - [ ] 依存配列 `[provider, localLLMAddress]` が正しいか
   - [ ] 失敗時はコンソールのみログで、UIに表示されないか
   - [ ] 手動ボタンとの競合がないか

4. **画像URL処理**
   - [ ] `getRemoteImageUrl()` が新規追加で、既存関数に影響ないか
   - [ ] URL構築時の例外処理が適切か

5. **環境変数**
   - [ ] `.env.example` に新規変数の説明が記載されているか
   - [ ] デフォルト値（localhost）が適切か

6. **後方互換性**
   - [ ] 既存コードは変更不要か
   - [ ] リリースノートで既存ユーザーへの影響を記載する必要があるか

---

## 実装詳細

### ファイル一覧

| ファイル | 変更種別 | 詳細 |
|---------|--------|------|
| `client/app/polyfills/crypto-uuid.ts` | 新規作成 | crypto.randomUUID ポリフィル |
| `client-admin/app/polyfills/crypto-uuid.ts` | 新規作成 | crypto.randomUUID ポリフィル |
| `client/app/layout.tsx` | 修正 | ポリフィル初期化関数を呼び出し |
| `client-admin/app/layout.tsx` | 修正 | ポリフィル初期化関数を呼び出し |
| `client/next.config.ts` | 修正 | CSP 動的ビルド関数を追加 |
| `client-admin/next.config.ts` | 修正 | CSP 動的ビルド関数を追加 |
| `client/app/utils/image-src.ts` | 修正 | `getRemoteImageUrl()` ヘルパー追加 |
| `client-admin/app/create/hooks/useAISettings.ts` | 修正 | LocalLLM 自動フェッチ useEffect 追加 |

### コード例

**ポリフィル初期化（layout.tsx）:**
```typescript
import { initCryptoUUIDPolyfill } from "@/app/polyfills/crypto-uuid";
initCryptoUUIDPolyfill(); // モジュール読み込み時に実行
```

**CSP ビルド（next.config.ts）:**
```typescript
const buildCSPHeader = (): string => {
  const siteUrl = getSiteUrl(); // NEXT_PUBLIC_SITE_URL から取得
  const siteDomain = new URL(siteUrl).hostname; // "192.168.1.100" など
  
  return `img-src 'self' ... http://${siteDomain} ...`;
};
```

**LocalLLM 自動フェッチ（useAISettings.ts）:**
```typescript
useEffect(() => {
  if (provider === "local" && localLLMAddress) {
    fetchModelsFromServer("local", localLLMAddress)
      .then(models => setLocalLLMModels(models))
      .catch(error => console.warn("Auto-fetch failed:", error));
  }
}, [provider, localLLMAddress]);
```

---

## リリースノート（参考）

### 新機能
- ✅ リモート環境（公開IP）でのHTTPアクセス対応
- ✅ LocalLLMプロバイダー選択時の自動モデルフェッチ
- ✅ crypto.randomUUID ポリフィル

### 改善
- ✅ CSP設定を環境変数ベースで動的化
- ✅ UX向上：LocalLLM選択時のモデル自動読み込み

### 修正
- ✅ Issue #685: リモート環境でのCSPエラーを解決
- ✅ Issue #685: crypto.randomUUID 未定義エラーに対応

### 後方互換性
- ✅ すべての既存APIは互換性を保持
- ✅ ユーザーコードの変更は不要

---

## 質問・コメント

レビュー時にご質問やご指摘があればお知らせください。

/fix #685 

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **新機能**
  * ローカルLLM provider使用時に、利用可能なモデルリストが自動的に取得され、最初のモデルが自動選択されるようになりました。
  * 画像URL生成機能が追加されました。

* **セキュリティ改善**
  * Content Security Policy（CSP）ヘッダーが実装され、セキュリティが強化されました。

* **互換性改善**
  * UUID生成の互換性が向上しました。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat: integrate Biome for linting and formatting](https://github.com/digitaldemocracy2030/kouchou-ai/pull/734)

**作成者:** Devesh36  
**作成日:** 2025-12-04T05:31:40Z  
**変更:** +2172 -300 (11ファイル)  
**内容:**

<h1 style="line-height: normal; font-size: 19.994px; font-weight: 600; margin: 16px 0px 8px; font-family: -apple-system, &quot;system-ui&quot;, sans-serif; color: rgb(204, 204, 204); font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(24, 24, 24); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">Biome Integration Setup — Complete</h1><p style="margin: 0px 0px 16px; color: rgb(204, 204, 204); font-family: -apple-system, &quot;system-ui&quot;, sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(24, 24, 24); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong>What was done:</strong></p><p style="margin: 0px 0px 16px; color: rgb(204, 204, 204); font-family: -apple-system, &quot;system-ui&quot;, sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(24, 24, 24); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">Created a<span> </span><strong>unified Biome linting &amp; formatting toolchain</strong><span> </span>with 3-phase gradual adoption:</p><ul style="padding-inline-start: 24px; color: rgb(204, 204, 204); font-family: -apple-system, &quot;system-ui&quot;, sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(24, 24, 24); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><li><strong>Phase 1 (now):</strong><span> </span>Non-blocking setup; warnings only</li><li><strong>Phase 2 (weeks 3–6):</strong><span> </span>Gradual enforcement</li><li><strong>Phase 3 (weeks 7–10):</strong><span> </span>Strict mandatory checks</li></ul><p style="margin: 0px 0px 16px; color: rgb(204, 204, 204); font-family: -apple-system, &quot;system-ui&quot;, sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(24, 24, 24); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong>Files created/updated:</strong></p>
File | Purpose
-- | --
package.json | Updated npm scripts: lint, lint:check, lint:frontend, format
biome.json | Root config with Phase 1 rules (most disabled/warned)
biome.md | Full setup guide + 3-phase strategy
BIOME_SETUP_SUMMARY.md | 1-page executive summary
BIOME_QUICK_REFERENCE.md | Developer command cheatsheet
docs/BIOME_IMPLEMENTATION.md | Detailed rationale + migration roadmap
IMPLEMENTATION_CHECKLIST.md | Verification checklist
PR_BIOME_700.md | PR template for Issue #700
.github/workflows/biome-lint.yml | Report-only GitHub Actions workflow

<p style="margin: 0px 0px 16px; color: rgb(204, 204, 204); font-family: -apple-system, &quot;system-ui&quot;, sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(24, 24, 24); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong>Key features:</strong></p><p style="margin: 0px 0px 16px; color: rgb(204, 204, 204); font-family: -apple-system, &quot;system-ui&quot;, sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(24, 24, 24); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">✅ Targets:<span> </span><code style="font-family: &quot;SF Mono&quot;, Monaco, Menlo, Courier, monospace; font-size: 11.999px; color: rgb(208, 208, 208); background-color: rgb(60, 60, 60); padding: 1px 3px; border-radius: 4px; white-space: pre-wrap;">client/</code>,<span> </span><code style="font-family: &quot;SF Mono&quot;, Monaco, Menlo, Courier, monospace; font-size: 11.999px; color: rgb(208, 208, 208); background-color: rgb(60, 60, 60); padding: 1px 3px; border-radius: 4px; white-space: pre-wrap;">client-admin/</code>,<span> </span><code style="font-family: &quot;SF Mono&quot;, Monaco, Menlo, Courier, monospace; font-size: 11.999px; color: rgb(208, 208, 208); background-color: rgb(60, 60, 60); padding: 1px 3px; border-radius: 4px; white-space: pre-wrap;">client-build/</code><br>✅ Excludes:<span> </span><code style="font-family: &quot;SF Mono&quot;, Monaco, Menlo, Courier, monospace; font-size: 11.999px; color: rgb(208, 208, 208); background-color: rgb(60, 60, 60); padding: 1px 3px; border-radius: 4px; white-space: pre-wrap;">server/</code><span> </span>(Python),<span> </span><code style="font-family: &quot;SF Mono&quot;, Monaco, Menlo, Courier, monospace; font-size: 11.999px; color: rgb(208, 208, 208); background-color: rgb(60, 60, 60); padding: 1px 3px; border-radius: 4px; white-space: pre-wrap;">node_modules/</code>,<span> </span><code style="font-family: &quot;SF Mono&quot;, Monaco, Menlo, Courier, monospace; font-size: 11.999px; color: rgb(208, 208, 208); background-color: rgb(60, 60, 60); padding: 1px 3px; border-radius: 4px; white-space: pre-wrap;">.next/</code>, etc.<br>✅ Single config → replaces ESLint + Prettier<br>✅ Non-blocking in Phase 1 → no merge blocks<br>✅ Ready to open PR for Issue #700</p><br class="Apple-interchange-newline">Biome Integration Setup — Complete
What was done:

Created a unified Biome linting & formatting toolchain with 3-phase gradual adoption:

Phase 1 (now): Non-blocking setup; warnings only
Phase 2 (weeks 3–6): Gradual enforcement
Phase 3 (weeks 7–10): Strict mandatory checks
Files created/updated:

File	Purpose
[package.json](vscode-file://vscode-app/Applications/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html)	Updated npm scripts: lint, lint:check, lint:frontend, format
[biome.json](vscode-file://vscode-app/Applications/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-browser/workbench/workbench.html)	Root config with Phase 1 rules (most disabled/warned)
biome.md	Full setup guide + 3-phase strategy
BIOME_SETUP_SUMMARY.md	1-page executive summary
BIOME_QUICK_REFERENCE.md	Developer command cheatsheet
docs/BIOME_IMPLEMENTATION.md	Detailed rationale + migration roadmap
IMPLEMENTATION_CHECKLIST.md	Verification checklist
PR_BIOME_700.md	PR template for Issue #700
.github/workflows/biome-lint.yml	Report-only GitHub Actions workflow
Key features:

✅ Targets: client/, client-admin/, client-build/
✅ Excludes: server/ (Python), node_modules/, .next/, etc.
✅ Single config → replaces ESLint + Prettier
✅ Non-blocking in Phase 1 → no merge blocks
✅ Ready to open PR for Issue #700


/fix #700 
<h1 style="line-height: normal; font-size: 19.994px; font-weight: 600; margin: 16px 0px 8px; font-family: -apple-system, &quot;system-ui&quot;, sans-serif; color: rgb(204, 204, 204); font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(24, 24, 24); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">バイオーム統合設定 — 完了</h1><p style="margin: 0px 0px 16px; color: rgb(204, 204, 204); font-family: -apple-system, &quot;system-ui&quot;, sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(24, 24, 24); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong>実行内容:</strong></p><p style="margin: 0px 0px 16px; color: rgb(204, 204, 204); font-family: -apple-system, &quot;system-ui&quot;, sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(24, 24, 24); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">統一された Biome linting &amp; を作成しました。書式設定ツールチェーン</strong><span></span>、3 段階の段階的導入:</p><ul style="padding-inline-start: 24px; color: rgb(204, 204, 204); font-family: -apple-system, &quot;system-ui&quot;, sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(24, 24, 24); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><li><strong>フェーズ 1 (現在):</strong><span> </span>非ブロッキング セットアップ;警告のみ</li><li><strong>フェーズ 2 (3～6 週目):</strong><span> </span>段階的な強制</li><li><strong>フェーズ 3 (7～10 週目):</strong><span> </span>厳格な必須チェック</li></ul><p style="margin: 0px 0px 16px; color: rgb(204, 204, 204); font-family: -apple-system, &quot;system-ui&quot;, sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(24, 24, 24); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong>作成/更新されたファイル:</strong></p>
ファイル | 目的
-- | --
package.json | 更新された npm スクリプト: lint、lint:check、lint:frontend、format
biome.json | フェーズ 1 のルール（ほとんどの無効化/警告）を含むルート設定
biome.md | 完全なセットアップガイド + 3 フェーズ戦略
BIOME_SETUP_SUMMARY.md | 1 ページのエグゼクティブサマリー
BIOME_QUICK_REFERENCE.md | 開発者コマンドチートシート
docs/BIOME_IMPLEMENTATION.md | 詳細な根拠 + 移行ロードマップ
IMPLEMENTATION_CHECKLIST.md |検証チェックリスト
PR_BIOME_700.md | 問題番号 #700 の PR テンプレート
.github/workflows/biome-lint.yml |レポートのみの GitHub Actions ワークフロー

<p style="margin: 0px 0px 16px; color: rgb(204, 204, 204); font-family: -apple-system, &quot;system-ui&quot;, sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(24, 24, 24); text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;"><strong>主な特徴:</strong></p><p style="margin: 0px 0px 16px; color: rgb(204, 204, 204); font-family: -apple-system, &quot;system-ui&quot;, sans-serif; font-size: 13px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; white-space: normal; background-color: rgb(24, 24, 24); text-decoration-thickness: initial; text-decoration-style: initial; テキスト装飾色: initial;">✅ ターゲット:<span

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **新機能**
  * 統合的なコード検査・整形ツールを導入し、非ブロッキングのCI検査ワークフローを追加

* **ドキュメント**
  * セットアップガイド、クイックリファレンス、導入サマリ、実装チェックリスト、実装手順書など多数のドキュメントを追加

* **その他**
  * コード整形／リンター設定を更新し、開発用スクリプトを追加・調整しました

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [静的ビルド実行前に公開状態のレポートが存在するかを検証](https://github.com/digitaldemocracy2030/kouchou-ai/pull/727)

**作成者:** NISHIO+Devin  
**作成日:** 2025-10-27T16:49:22Z  
**変更:** +84 -1 (2ファイル)  
**内容:**

# 変更の概要
- 静的ビルド実行前に公開状態のレポートが存在するかを検証するスクリプトを追加
- 公開レポートが存在しない場合に、わかりやすい日本語のエラーメッセージを表示するように改善

# スクリーンショット
N/A（UIの変更なし）

# 変更の背景
Issue #726 で報告された問題を解決するための変更です。

現状では、公開状態のレポートがない状態で静的HTML出力を実行すると、Next.jsから以下のような分かりにくいエラーメッセージが表示されていました：

```
'[Error: Page "/[slug]/opengraph-image.png" is missing "generateStaticParams()" so it cannot be used with "output: export" config.]\n'
```

このエラーメッセージでは根本原因（公開レポートがない）が分からず、ユーザーが適切に対処できない問題がありました。

# 関連Issue
Fixes #726

# 実装の詳細

## 追加ファイル
- `client/scripts/validate-reports.mjs`: レポート検証スクリプト

## 変更ファイル  
- `client/package.json`: `prebuild:static` スクリプトに検証を追加

## 検証ロジック
1. 静的エクスポートモード時のみ実行（`NEXT_PUBLIC_OUTPUT_MODE === "export"`）
2. API エンドポイント `/reports` からレポート一覧を取得
3. `status === "ready"` のレポートが存在するかをチェック
4. 存在しない場合は、詳細な日本語エラーメッセージを表示してビルドを中断

## エラーメッセージの改善点
- APIサーバー未起動時とレポート未作成時で異なるエラーメッセージを表示
- 具体的な対処方法を箇条書きで提示
- 現在のレポート数と公開レポート数を表示

# 動作確認の結果
- APIサーバー未起動時に適切なエラーメッセージが表示されることを確認
- Biomeのlintチェックが通過することを確認

**⚠️ レビュアーへの注意事項:**
- テスト環境のAPI側に既存の不具合があったため、「公開レポートがない状態でAPIが正常に動作している」というシナリオの完全な動作確認は実施できていません
- 実際の環境で公開レポートがない状態での動作確認を推奨します

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか（※今回は検証スクリプトのため単体テスト未実装）
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する

## レビュー時の重点確認項目
- [ ] 公開レポートがない状態で `make client-build-static` を実行し、わかりやすい日本語エラーメッセージが表示されることを確認
- [ ] 公開レポートが存在する状態で静的ビルドが正常に完了することを確認
- [ ] エラーメッセージの内容が適切で、ユーザーが対処方法を理解できることを確認
- [ ] API レスポンスの形式が想定と異なる場合のエラーハンドリングが適切か確認

---

**Link to Devin run:** https://app.devin.ai/sessions/edece407fde44bd8935bd2d410bfbfc8  
**Requested by:** NISHIO (@nishio) - nishio.hirokazu@gmail.com

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **新機能**
  * 静的エクスポートビルド時に、レポートの可用性を事前検証するステップを追加しました。準備完了したレポートが存在しない場合、ビルドプロセスは停止され、詳細なエラーメッセージが表示されます。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Add filesystem-based usage documentation and validation tests](https://github.com/digitaldemocracy2030/kouchou-ai/pull/722)

**作成者:** NISHIO+Devin  
**作成日:** 2025-10-23T07:46:58Z  
**変更:** +2088 -3 (24ファイル)  
**内容:**

# 変更の概要
APIサーバーを起動せずに、ファイルシステムベースでパイプラインを実行するための機能を明確化し、入出力の検証機能とテストを追加しました。

**主な追加内容:**
- ファイルシステムベース実行の包括的なドキュメント（FILESYSTEM_USAGE.md、388行）
- Pydanticによる入力CSV、設定JSON、出力JSONのスキーマ定義と検証
- CLIバリデーションオプション（`--validate-input`, `--validate-config`, `--validate-output`, `--dry-run`）
- 54個のテストケースを含む包括的なテストスイート

# スクリーンショット
UIの変更はありません（CLI機能の追加のみ）

# 変更の背景
Issue #721で指摘された通り、kouchou-aiには既にファイルシステムベースでパイプラインを実行する機能がありましたが、以下の点が不明確でした：
- 入力CSVファイルの正確な形式
- 設定JSONファイルの詳細な仕様
- 出力ファイルの構造
- バリデーション方法

この変更により、開発者やパワーユーザーがAPIサーバーなしでパイプラインを実行し、入力データの妥当性を事前に検証できるようになります。

# 関連Issue
Resolves #721

# 動作確認の結果
以下のテストを実行し、すべて成功しました：

```bash
ENV_FILE=.env.test python -m pytest tests/broadlistening/test_input_validation.py -v
# 14 passed

ENV_FILE=.env.test python -m pytest tests/broadlistening/test_config_validation.py -v  
# 20 passed

ENV_FILE=.env.test python -m pytest tests/broadlistening/test_output_validation.py -v
# 11 passed

ENV_FILE=.env.test python -m pytest tests/broadlistening/test_pipeline_e2e.py -v
# 9 passed
```

**⚠️ 重要な注意点**: 
- テストは全てスキーマ検証とファイル構造の確認のみ
- 実際のAPIキーを使用したパイプライン実行は未テスト
- 新しいCLIオプション（`--validate-*`, `--dry-run`）の動作確認は手動テストが必要

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか → ✅ 54テスト実装済み
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する

## レビュー時に特に確認してほしい点

### 1. hierarchical_main.pyの変更（高リスク）
- 72-90行目: 新しいバリデーションフラグの処理ロジック
- 98行目: `--dry-run`フラグが`--skip-interaction`と組み合わせて使われている点
- 105-117行目: dry-runモードの実装
- **確認ポイント**: 既存の実行フローを壊していないか、早期returnが適切か

### 2. スキーマ定義の妥当性
- `server/broadlistening/pipeline/schemas/config_schema.py`: 設定のデフォルト値と制約
- `server/broadlistening/pipeline/schemas/input_csv_schema.py`: CSV検証ルール
- **確認ポイント**: バリデーションが厳しすぎないか、緩すぎないか

### 3. ドキュメントの正確性
- `server/broadlistening/FILESYSTEM_USAGE.md`: 388行の包括的なドキュメント
- **確認ポイント**: 実装と一致しているか、誤解を招く記述がないか

### 4. 手動動作確認の推奨
以下のコマンドで実際に動作確認することを推奨します：
```bash
# 設定ファイルのバリデーション
python hierarchical_main.py configs/dummy-comments-japan.json --validate-config

# 入力ファイルのバリデーション  
python hierarchical_main.py configs/dummy-comments-japan.json --validate-input

# Dry-run実行
python hierarchical_main.py configs/dummy-comments-japan.json --dry-run
```

---

**Devin実行セッション**: https://app.devin.ai/sessions/3c421325d5604e71ba8e800747f59e40  
**リクエスト元**: NISHIO (nishio.hirokazu@gmail.com / @nishio)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **新機能**
  * ファイルシステムベースでのパイプライン直接実行が可能に（APIサーバー不要）
  * 設定・入力・出力の検証オプション（--validate-config、--validate-input、--validate-output）を追加
  * パイプライン実行前の確認用ドライランモード（--dry-run）を実装

* **ドキュメント**
  * ファイルシステムベースでの使用方法に関する詳細ガイドを追加

* **テスト**
  * パイプライン検証機能の包括的なテストカバレッジを追加

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Feature/issue 493 レポート画面のスクロールイベント回避を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/597)

**作成者:** dentaro  
**作成日:** 2025-06-09T12:11:47Z  
**変更:** +141 -161 (2ファイル)  
**内容:**

# 変更の概要
client/components/chart.tsx
図の上にオーバーレイをかけることにより、レポートページを見ようとスクロールしても図が拡大縮小されないようにした。
1秒で自動解除。図内を出ると自動1秒でオーバーレイ復帰。
図の描画速度を向上させた。

# スクリーンショット
![image](https://github.com/user-attachments/assets/5d8d4190-239c-484b-bad0-3c2e8e81be15)
![image](https://github.com/user-attachments/assets/507f3cbc-2e45-4152-bf79-80e7c993bfdb)

# 変更の背景
ScatterChartの領域でスクロールで拡大縮小できるようになった。
このことにより「レポートページを見るためにスクロールする→図が拡大/縮小される」というユーザーが意図しない動作がほぼ発生する。何らかの方法でユーザー操作を直感的にする必要がある。

# 関連Issue
[FEATURE] レポートページを見ようとスクロールすると図が拡大縮小される #493

# 動作確認の結果
「親画面が一定時間（1秒）スクロールしていないこと」を拡大縮小のトリガーにする
親画面スクロール中にScatterChartにマウスオーバーしたら半透明のグレーのパネル（=操作無効）をChartに被せ、そのままスクロールで通り過ぎられるようにした
図内に入るとクリックしなくてもオーバーレイが解除される
意図しないスクロールによる拡大縮小を、オーバーレイのオン状態の時にキャンセルしている

以下の既存のエラー、警告は維持されているので、別のissueで対応すべき
・No label associated with a form field
・mg タグ、video タグ、canvas タグに overflow: visible を指定すると、要素の境界外にビジュアル コンテンツが作成される場合があります。https://github.com/WICG/shared-element-transitions/blob/main/debugging_overflow_on_images.md をご覧ください。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）]
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [] CIが全て通過している
- [] 単体テストが実装されているか
- [] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **ドキュメント**
  - READMEに「Windowsからプッシュ！！」という一文を追加しました。

- **リファクタ**
  - チャートのフィルタリング処理を効率化し、メモ化によるパフォーマンス向上を行いました。
  - チャートの描画ロジックを整理し、共通プロパティの管理を簡素化しました。

- **新機能**
  - チャート上にインタラクティブなオーバーレイを追加し、意図しない操作を防止できるようになりました。

- **スタイル**
  - フルスクリーンボタンやオーバーレイの表示位置・見た目を微調整しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

