# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-03-04T12:50:58.983330+09:00 から 2026-03-11T12:50:58.983330+09:00 まで

## Issues

### 過去7日間に完了されたissue (1件)

### [[BUG]分析対象のカラムにから文字列が含まれているとエラーになる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/583)

**作成者:** shingo-ohki  
**作成日:** 2025-05-29T09:25:11Z  
**内容:**

### 概要

> 中山心太（tokoroten）
  16:45
分析対象のカラムに空文字が入っていると、大量のエラーが出ますね。
自由記述アンケートの分析をやろうとしたら、死にました。
中山心太（tokoroten）
  [16:58](https://dd2030.slack.com/archives/C08F7JZPD63/p1748505525503179)
空行（改行だけとか、スペースだけとか）が入ってもダメなのかも。この辺要検討です。 （編集済み） 
中山心太（tokoroten）
  17:05
属性フィルタ、カテゴリ値で値がnullの場合がケア出来てないので、空白の選択肢を用意する

### 再現手順

1. <!-- バグが再現する手順をステップごとに記入してください -->
2. 
3. 

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->

**コメント:** なし

---

### 過去7日間に作成されたissue (1件)

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

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (2件)

### [fix: filter out empty/whitespace-only comments before LLM processing (#583) - conflict resolved](https://github.com/digitaldemocracy2030/kouchou-ai/pull/813)

**作成者:** nishio  
**作成日:** 2026-03-02T07:52:54Z  
**変更:** +154 -0 (4ファイル)  
**マージ日:** 2026-03-09T01:32:46Z  
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

### [fix: filter out empty/whitespace-only comments before LLM processing (#583)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/796)

**作成者:** yasumorishima  
**作成日:** 2026-02-20T22:07:25Z  
**変更:** +154 -0 (4ファイル)  
**マージ日:** 2026-03-09T01:32:48Z  
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

### 過去7日間に作成されたPR (2件)

### [誤混入したCI設定を見直し、CodeQL定期実行とCodeRabbit設定を調整](https://github.com/digitaldemocracy2030/kouchou-ai/pull/817)

**作成者:** shingo-ohki  
**作成日:** 2026-03-10T14:38:54Z  
**変更:** +16 -1 (2ファイル)  
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

### [Make UMAP n_neighbors configurable in hierarchical clustering (default: 15)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/816)

**作成者:** Copilot  
**作成日:** 2026-03-09T11:42:40Z  
**変更:** +7 -4 (4ファイル)  
**内容:**

`n_neighbors` for UMAP was hardcoded to `15` with no way to override it per-report. This exposes it as an optional config field while preserving the existing default.

## Changes

- **Schema** (`HierarchicalClusteringConfig`): added `n_neighbors: int | None = None`
- **`apps/api` + `analysis-core` step implementations**: read `n_neighbors` from config via `.get("n_neighbors", 15)` instead of a local constant
- **`analysis-core` plugin**: passes `n_neighbors` through to the legacy config dict; updated docstring

## Usage

```json
{
  "hierarchical_clustering": {
    "cluster_nums": [3, 6, 12],
    "n_neighbors": 30
  }
}
```

Omitting `n_neighbors` retains the previous behavior.

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/digitaldemocracy2030/kouchou-ai/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.


**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

