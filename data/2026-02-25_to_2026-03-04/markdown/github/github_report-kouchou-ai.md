# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-02-25T12:50:27.609769+09:00 から 2026-03-04T12:50:27.609769+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (1件)

### [[FEATURE] UMAPを並列化したい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/809)

**作成者:** tokoroten  
**作成日:** 2026-02-28T18:58:44Z  
**内容:**

# 背景

現在はrandom_stateが有効化されており、再現性があるコードになっているが、
random_stateを有効化すると、並列化が効かなくなる

packages/analysis-core/src/analysis_core/steps/hierarchical_clustering.py（59行目）
umap_model = UMAP(random_state=42, n_components=2, n_neighbors=n_neighbors)

公式ドキュメントにもその記述がある

https://umap-learn.readthedocs.io/en/latest/reproducibility.html

既に入力データに再現性が無いので、後段が再現性が必要ではないと考える。
LLMが前段に噛まされており、random seedを有効化しても、ハードウェアの揺らぎ（計算するノードによって浮動小数点の精度が異なる）や計算順序の揺らぎによって、出力データが異なる傾向にある。

# 提案内容

random_stateをNoneにして、並列化を有効にするオプションを提供する

# 懸念事項

現在の広聴AIはエンベディングの再利用が可能になってるので、umapの再現性オプションは必要かもしれない



**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(1件)

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

## Pull Requests

### 過去7日間にマージされたPR (3件)

### [feat: 散布図のデータポイントホバー時にクラスタラベルを非表示にする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/812)

**作成者:** tokoroten  
**作成日:** 2026-03-01T00:29:11Z  
**変更:** +105 -4 (1ファイル)  
**マージ日:** 2026-03-02T10:58:29Z  
**内容:**

## Summary
- 散布図でデータポイント（標本）にマウスホバーすると、そのポイントが所属するクラスタのラベル（Plotly annotation）がフェードアウトし、ラベル下のポイントが見やすくなる
- 別のクラスタのポイントに移動すると、前のラベルが復帰し新しいクラスタのラベルが非表示になる
- マウスがポイントから離れると300msの遅延後に全ラベルが復帰する

<img width="1162" height="663" alt="image" src="https://github.com/user-attachments/assets/1841bf5e-8aa3-4250-8e0a-366831f88c06" />



## Implementation
- Plotly の `gd.on("plotly_hover" / "plotly_unhover")` イベントを `onUpdate` コールバック内で直接登録（react-plotly.js の `onHover` prop は scattergl トレースで発火しないため）
- `customdata.arg_id` → クラスタ → アノテーションインデックスのマッピングを `useMemo` + ref で管理し、該当ラベルのみ `opacity` を切り替え
- `onHover` prop のクロージャキャプチャ問題を ref で回避

## Test plan
- [ ] 散布図の標本にホバーし、そのクラスタのラベルが消えることを確認
- [ ] 別のクラスタの標本に移動し、前のラベルが復帰・新しいラベルが消えることを確認
- [ ] 標本から離れた後、300ms程度で全ラベルが復帰することを確認
- [ ] 全画面モードでも同様に動作することを確認
- [ ] フィルター適用時にも正常に動作することを確認

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

## リリースノート

* **新機能**
  * 散布図チャートのホバー挙動を強化しました。マウスオーバー時に関連するクラスター注釈ラベルを自動的に非表示にし、マウスアウト後に適切な遅延で復帰させます。

* **改善 / クリーンアップ**
  * ホバーリスナーの確実な登録・解除と、表示復帰タイマーのクリア処理を追加してメモリリークや不要な振る舞いを防止するようにしました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [refactor: 属性フィルタロジックの統合とstale closureバグ修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/811)

**作成者:** tokoroten  
**作成日:** 2026-02-28T23:41:25Z  
**変更:** +222 -369 (4ファイル)  
**マージ日:** 2026-03-02T07:45:19Z  
**内容:**

## Summary
- フィルタロジックが3箇所（`attributeFilterUtils.ts`、`ClientContainer.tsx`、`Chart.tsx`）に重複していたものを `attributeFilterUtils.ts` に一元化
- `ClientContainer.tsx` の `updateFilteredResult` 関数がstale closureにより古いstate値を参照していたバグを、`useMemo` による派生計算に置き換えて修正
- `attributeMetas` を `useEffect + setState` から `useMemo` に変更し、不要な再レンダリングを解消
- 死コード（`filterSamples`、`getFilteredArgumentIds`、`samples`、`filteredSamples`、未使用の型定義）を削除

## Changes
- **attributeFilterUtils.ts**: 型定義・フィルタロジック・メタデータ計算を集約。`filterArgumentIds`、`computeAttributeMetas`、`hasActiveFilters`、`countActiveFilters` を提供
- **AttributeFilterDialog.tsx**: 重複型定義を削除し `attributeFilterUtils` からインポート。未使用の `attributeNames` を削除
- **ClientContainer.tsx**: `updateFilteredResult` を廃止し `filteredResult` を `useMemo` で派生計算。ハンドラを大幅簡素化（-312行 / +217行 → 152行の純減）
- **Chart.tsx**: 55行の重複フィルタ計算を完全削除。`filterState` propを廃止し `result.filteredArgumentIds` を直接使用

## Test plan
- [ ] 属性フィルタダイアログでカテゴリフィルタを設定し、scatter/treemap/hierarchyList各チャートで正しくフィルタリングされることを確認
- [ ] 数値レンジフィルタ（有効化トグル、空値含める）が正しく動作することを確認
- [ ] テキスト検索が正しく動作することを確認
- [ ] 密度フィルタ（scatterDensityモード）が正しく動作することを確認
- [ ] フィルタバッジの数値が正しく表示されることを確認
- [ ] フィルタクリアが正しく動作することを確認

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

## リリースノート

* **Refactor**
  * フィルタリングロジックと型定義を整理して一元化し、保守性とパフォーマンスを向上しました。
  * コンポーネントの状態管理をメモ化された派生データに切り替え、描画やフィルター適用の挙動を簡潔化しました。

* **New Features**
  * フィルターのメタ情報取得やアクティブフィルター数の集約表示を追加し、UIバッジやフィルターインジケータが正確になります。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix: override minimatch to ^10.2.1 to fix CVE-2026-26996 (ReDoS)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/808)

**作成者:** shingo-ohki  
**作成日:** 2026-02-24T13:12:53Z  
**変更:** +26 -44 (2ファイル)  
**マージ日:** 2026-02-25T12:48:40Z  
**内容:**

# 変更の概要
- `pnpm.overrides` を使用して、推移的依存関係の `minimatch` を `^10.2.1` に強制解決し、ReDoS 脆弱性（CVE-2026-26996）に対応
- 対象: minimatch@3.1.2, minimatch@5.1.6, minimatch@9.0.5 → minimatch@10.2.2
- 関連する依存関係（brace-expansion 1.x/2.x → 5.0.3, balanced-match 1.0.2 → 4.0.4）も自動的にアップグレード
- バージョン指定は `^10.2.1`（v10 系内に制限）を使用し、将来のメジャーバージョンを自動的に取り込むリスクを回避

# スクリーンショット
- UIの変更なし

# 変更の背景
- Dependabot alert #109 により、minimatch < 10.2.1 に ReDoS 脆弱性（CVE-2026-26996、severity: high）が報告された
- glob パターンに連続する `*` ワイルドカードが含まれる場合、正規表現のバックトラッキングにより O(4^N) の計算量が発生する
- minimatch は glob@7.2.3（jest経由）、glob@10.5.0、readdir-glob@1.1.3、test-exclude@6.0.0 の推移的依存として使用されている

# 関連Issue
- https://github.com/digitaldemocracy2030/kouchou-ai/security/dependabot/109
- https://github.com/isaacs/minimatch/security/advisories/GHSA-3ppc-4f35-3m26

# 動作確認の結果
- `pnpm install` 後に lockfile 内の minimatch がすべて 10.2.2 に解決されることを確認
- 既存の lint エラーは main ブランチにも存在する既知の問題であり、本変更による新規エラーは発生していない
- **jest テスト**（minimatch@10 と glob@7 の互換性検証）:
  - admin: 13 test suites, 96 tests → 全てパス
  - public-viewer: 5 test suites, 83 tests → 全てパス
- **Node.js バージョン要件**: minimatch@10.2.2 は `node: 20 || >=22` を要求 → プロジェクトの全 Dockerfile で `node:22-alpine` を使用しており要件を満たすことを確認

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


## ⚠️ レビュー時の注意点
- **メジャーバージョンジャンプ**: minimatch が 3.x/5.x/9.x から 10.x にアップグレードされます。jest テストは全てパスしていますが、glob@7.2.3 は本来 minimatch@^3.1.1 を期待しているため、テストでカバーされていない glob/minimatch の使用パターンで問題が発生する可能性があります
- **推移的依存関係の変更**: brace-expansion (1.x/2.x → 5.0.3) と balanced-match (1.0.2 → 4.0.4) もメジャーバージョンアップされています
- **Node.js バージョン要件**: minimatch@10.2.2 は `node: 18 || 20 || >=22` を要求します。プロジェクトは node:22-alpine を使用しているため問題ありません

---

Link to Devin run: https://app.devin.ai/sessions/749dd488c9e74e1aa14a768d1fb824b7
Requested by: @shingo-ohki

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

## リリースノート

* **Chores**
  * 依存解決の調整を行い、特定のライブラリについてインストール時に指定範囲のバージョンが優先されるよう設定を追加しました。これによりビルドやインストール時のバージョン整合性が向上します。その他の依存関係やスクリプトに変更はありません。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
<!-- devin-review-badge-begin -->

---

<a href="https://app.devin.ai/review/digitaldemocracy2030/kouchou-ai/pull/808" target="_blank">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://static.devin.ai/assets/gh-open-in-devin-review-dark.svg?v=1">
    <img src="https://static.devin.ai/assets/gh-open-in-devin-review-light.svg?v=1" alt="Open with Devin">
  </picture>
</a>
<!-- devin-review-badge-end -->

**コメント:** なし

---

### 過去7日間に作成されたPR (3件)

### [Show clear Japanese error on static build with no published reports](https://github.com/digitaldemocracy2030/kouchou-ai/pull/814)

**作成者:** Copilot  
**作成日:** 2026-03-02T11:06:09Z  
**変更:** +16 -2 (1ファイル)  
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

**コメント:** なし

---

### [fix: filter out empty/whitespace-only comments before LLM processing (#583) - conflict resolved](https://github.com/digitaldemocracy2030/kouchou-ai/pull/813)

**作成者:** nishio  
**作成日:** 2026-03-02T07:52:54Z  
**変更:** +154 -0 (4ファイル)  
**内容:**

# 変更の概要
- PR #796 (by @yasumorishima) の内容を main とのコンフリクト解消した上で取り込むPRです
- CSV入力の `comment-body` カラムに空文字列・空白のみ・null の値が含まれている場合、LLM処理前にフィルタで除外する機能を追加
- フィルタされた行数を logging で出力
- 全件が空だった場合、`RuntimeError` で明確に停止
- 既存関数に docstring を追加

# スクリーンショット
なし（コード・ロジック変更のみ）

# 変更の背景
- 分析対象カラムに空文字列や空白のみの値が含まれていると、そのままLLM APIに送信され大量のエラーが発生する問題があった (#583)
- 元PR #796 が main とコンフリクトしていたため（main側で `extract_batch` / `extract_arguments` に `timeout_seconds` パラメータが追加された変更と、PR側の docstring 追加が衝突）、コンフリクトを解消して再作成

## コンフリクト解消の内容
`extraction.py` の `extract_batch` と `extract_arguments` 関数で、main側の `timeout_seconds` パラメータ追加（複数行フォーマット含む）と PR側の docstring 追加の両方を統合

## レビュー時の注意点
- `.coderabbit.yaml` と `.github/workflows/codeql.yml` は本PRの主題（空コメントフィルタ）とは無関係な変更です。元PR #796 に含まれていたものをそのまま含めていますが、別PRに分離すべきか検討をお願いします
- テストファイルで `filter_empty_comments` を `_filter_empty_comments` としてエイリアスインポートしている点がやや紛らわしいです

# 関連Issue
Closes #583
Supersedes #796

# 動作確認の結果
- `test_extraction_filter.py` の7件のテストケースが本番コード (`filter_empty_comments`) を直接テストしていることを確認
  - 空文字列のフィルタ
  - 空白のみ（スペース、タブ、改行）のフィルタ
  - null値のフィルタ
  - 正常データが除外されないこと（ID・内容の保持も検証）
  - 全件空の場合に RuntimeError が発生すること
  - 全件 null の場合に RuntimeError が発生すること
  - 空・正常が混在するデータの正しいフィルタ

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。
- [ ] `.coderabbit.yaml` と `codeql.yml` のスコープ外変更を許容するか、別PRに分離するか判断

---

Link to Devin Session: https://app.devin.ai/sessions/7fbd6c1a5c2744548c4cb1988ee36808  
Requested by: @nishio

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **New Features**
  * コメント分析で空または空白のみのコメントを自動的にフィルタリングする機能を追加しました。

* **Chores**
  * コード品質向上のため、自動コードレビューおよびセキュリティ分析ワークフローを設定しました。

* **Tests**
  * コメントフィルタリング機能の包括的なテストを追加しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

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

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [fix: filter out empty/whitespace-only comments before LLM processing (#583)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/796)

**作成者:** yasumorishima  
**作成日:** 2026-02-20T22:07:25Z  
**変更:** +154 -0 (4ファイル)  
**内容:**

# 変更の概要
- CSV入力の`comment-body`カラムに空文字列や空白のみの値が含まれている場合、フィルタで除外するようにした
- フィルタされた行数をloggingで出力するようにした
- 全件が空だった場合、明確なエラーメッセージで停止するようにした

# スクリーンショット
なし（コード・ロジック変更のみ）

# 変更の背景
分析対象カラムに空文字列や空白のみの値が含まれていると、それがそのままLLM APIに送信され、大量のエラーが発生する問題があった（#583）。

# 関連Issue
Closes #583

# 動作確認の結果
- `test_extraction_filter.py` に5件のテストケースを追加し、全て通過することを確認した
  - 空文字列のフィルタ
  - 空白のみ（スペース、タブ、改行）のフィルタ
  - 正常データが除外されないこと
  - 全件空の場合にRuntimeErrorが発生すること
  - 空・正常が混在するデータの正しいフィルタ

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

## リリースノート

* **新機能**
  * 自動コードレビューの設定を追加（ドラフトの自動作成を有効化）。
  * CodeQL による自動セキュリティ解析ワークフローを追加。
  * 抽出処理で空または空白のみのコメントを自動除外し、全件が空の場合はエラーを返す挙動を導入。

* **テスト**
  * コメントフィルタリングの包括的なテストを追加しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

