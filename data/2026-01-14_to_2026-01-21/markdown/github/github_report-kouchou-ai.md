# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-01-14T12:38:27.768419+09:00 から 2026-01-21T12:38:27.768419+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (5件)

### [[FEATURE].envとshell envが食い違っている時にその旨を表示する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/750)

**作成者:** nishio  
**作成日:** 2026-01-21T01:11:33Z  
**内容:**

# 背景
adminサーバの起動の際、.envと異なった値(特にport番号)がshell envで指定されている場合、shell envが優先される。しかしこれは暗黙的に行われるので食い違いに気付きにくい(特にshell envの設定をAIエージェントがやっていて、しかもそのことを忘れている場合)

なので.envをshell envがoverrideしている場合にその旨がサーバ起動時のメッセージで出るようにする。

# 提案内容
```
[env-check] WARNING: Shell environment variables are overriding .env file values:
  API_BASEPATH:
    .env file:    http://localhost:8000
    shell env:    http://localhost:8001 (this value is used)
  ...

To fix this, either:
  1. Unset the shell environment variables: unset API_BASEPATH NEXT_PUBLIC_API_BASEPATH
  2. Or start in a new terminal session
  3. Or explicitly set correct values when starting: API_BASEPATH=http://localhost:8000 npm run dev
```


**コメント:** なし

---

### [[FEATURE]「レポートの取得に失敗しました」を親切にする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/749)

**作成者:** nishio  
**作成日:** 2026-01-21T00:46:59Z  
**内容:**

# 提案内容
admin画面がapiサーバからの
```
>  9 |     const response = await fetch(`${getApiBaseUrl()}/admin/reports`, {
```
に失敗した時に表示される

```
レポートの取得に失敗しました
エラー：データの取得に失敗しました
Error: fetch failed to http://localhost:8000.
```
について、もう少し親切なメッセージにする。
apiサーバからレポート一覧を取得しようとしたこと、サーバにそもそも接続できてないのか(=apiサーバが起動していない、addressやportが間違っている)、接続したけどパスワード違いでrejectされたのか、など。

<img width="897" height="330" alt="Image" src="https://github.com/user-attachments/assets/55e1ae1f-7f3f-410d-b527-441814affb3b" />

**コメント:** なし

---

### [[FEATURE]JSONダウンロード](https://github.com/digitaldemocracy2030/kouchou-ai/issues/748)

**作成者:** nishio  
**作成日:** 2026-01-21T00:37:22Z  
**内容:**

# 背景
サーバで広聴AIを動かしているケースで、分析後にJSONファイルを使って「広聴AI上での可視化」以外のことを可能にする(他のBIツールと連携するなど)ために、JSONをダウンロードするAPIとメニューをつける


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

`/reports/{slug}`が今までそれに近いことをしていたが、これは内部APIであり、管理画面でレポート表示パラメータを設定可能にするにあたって設定も含まれるようになった。
これとは別に、パイプラインが出力したJSONを取得するシンプルなAPIがあるべきである。
またUIもあるのがベター。

<img width="318" height="358" alt="Image" src="https://github.com/user-attachments/assets/9dd8da79-b79c-44bf-98f5-cccd82c34c37" />

**コメント:** なし

---

### [[DOCUMENT]ドキュメントをorganizeする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/747)

**作成者:** nishio  
**作成日:** 2026-01-21T00:22:30Z  
**内容:**

# 現在の問題点
色々なファイルがあるが目次などが整備されていない

# 提案内容
よくあるOSSのドキュメントみたいなものをMkDocs Material作り、CI+GitHub Pagesで公開する


**コメント:** なし

---

### [[FEATURE] バックエンドの pandas を polars に置換する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/745)

**作成者:** 101ta28  
**作成日:** 2026-01-20T05:24:37Z  
**内容:**

# 背景
パッケージを pandas から polars にすることで、処理の高速化が見込まれるため。


# 提案内容
- polars パッケージの導入
- pandas で処理している部分を polars の記法に置き換え

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (0件)

### 過去7日間に作成されたPR (2件)

### [安定運用したいコアと実験的な拡張を分離し、壊れにくい形に設計変更する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/746)

**作成者:** nishio  
**作成日:** 2026-01-20T23:48:34Z  
**変更:** +30635 -25349 (484ファイル)  
**内容:**

# 目的
安定運用したいコアと実験的な拡張（新しい解析手法・ビュー・入力ソース）を技術的に分離し、壊れにくい契約（API/manifest）を軸に拡張できる構造へリファクタすること。あわせて、CLI/PyPI での再利用や運用の整理（アプリ/パッケージ/プラグインの分離）を実現するのが狙い。

詳細: docs/M5_REFACTORING_PLAN.md

## 細部の変更
- リポジトリ構造の整理と命名統一
  - `server`→`apps/api`、`client`→`apps/public-viewer`、`client-admin`→`apps/admin`、`client-static-build`→`apps/static-site-builder` へ移行し、docker/CI/ドキュメントの参照を更新
  - `scripts`→`tools/scripts`、`experimental`→`experiments` へ移動
  - `pnpm-workspace.yaml` と `pnpm-lock.yaml` を追加してワークスペース化し、root の `.npmrc` を整備
- パイプラインのパッケージ化（analysis-core）
  - `packages/analysis-core` を新設し、ワークフローエンジン・互換レイヤ・CLI を実装
  - API 側は従来のパイプラインに依存せず `analysis_core` を subprocess で起動する構成に移行
  - テストや依存関係を整理
- 入力プラグイン機構の導入（API＋管理UI）
  - `apps/api/src/plugins` にプラグイン基盤（manifest/registry）を追加し、YouTube 取得プラグインを実装
  - 管理画面のレポート作成 UI にプラグインタブを追加し、検証・プレビュー・インポートのフローを統合
- 可視化プラグイン＋可視化設定の整備
  - `apps/public-viewer` にチャートのプラグインレジストリを導入（scatter/treemap/階層リスト）し、動的な表示切り替えに対応
  - `visualizationConfig` のスキーマと API を追加し、管理画面に可視化設定ダイアログを実装
  - 公開画面は設定値を優先し、既存の既定挙動と互換性を維持
- CI/運用・Docker/Azureの更新
  - GitHub Actions を pnpm 前提に変更し、パスやビルドコマンドを新構成に合わせて更新
  - `compose.yaml` と Azure デプロイのコンテナ名・ビルドパスを新しいアプリ構成に揃えた
  - `.dockerignore` を新規追加し、ビルド対象を整理
- ドキュメントと計画の追加・更新
  - `docs/PLUGIN_GUIDE.md` などプラグイン関連のドキュメントを拡充
  - `M5_REFACTORING_PLAN.md`、`M5_PLUGIN_SYSTEM_PLAN.md` など計画・背景文書を追加し、方向性を明文化

# スクリーンショット
> `apps/public-viewer` にチャートのプラグインレジストリを導入（scatter/treemap/階層リスト）し、動的な表示切り替えに対応
https://gyazo.com/af56999b44a99ee8e1497158086cdabe][https://gyazo.com/43ddac15c0ab52f89a54eb60512a9832

>`apps/api/src/plugins` にプラグイン基盤（manifest/registry）を追加し、YouTube 取得プラグインを実装

<img width="1000" height="331" alt="image" src="https://github.com/user-attachments/assets/81a5fbeb-9b16-4726-8308-71932b91d3e3" />

# 動作確認の結果

Result: All 167 tests now pass

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

**コメント:** なし

---

### [バックエンドの pandas を polars に変更](https://github.com/digitaldemocracy2030/kouchou-ai/pull/744)

**作成者:** 101ta28  
**作成日:** 2026-01-20T03:14:22Z  
**変更:** +298 -213 (11ファイル)  
**内容:**

close #745 

# 変更の概要
- server 側の DataFrame 処理（スプレッドシート取込・レポート入力保存・パイプライン各ステップ）を pandas から polars へ移行し、`pyproject.toml` の依存を polars に置き換えました。
- パイプライン各ステップ（extraction/embedding/hierarchical_*）は polars 用 API で再実装し、CSV/PKL の入出力や NaN 取扱いを polars ベースに統一しました。
- `hierarchical_initial_labelling.py` では polars 変換に伴う `cluster_id` 非存在時の例外を防ぐため、列存在チェックを追加しました。

# スクリーンショット
- UI 変更はありません。

# 変更の背景
- pandas から polars に一本化し、処理速度やメモリ効率の改善と依存関係の簡素化を図るため。

# 動作確認の結果
- `python server/broadlistening/pipeline/hierarchical_main.py configs/<slug>.json --skip-interaction --without-html` を実行し、各ステップが polars ベースで正常に完了することを確認しました。
- extraction や embedding の処理速度が向上しました。

## pandas実装でのログ
```md
[2026-01-20T02:07:30.434587] Pipeline started (force=False, only=None)
[2026-01-20T02:07:30.434656] Execution plan: extraction -> not trace of previous run, embedding -> not trace of previous run, hierarchical_clustering -> not trace of previous run, hierarchical_initial_labelling -> not trace of previous run, hierarchical_merge_labelling -> not trace of previous run, hierarchical_overview -> not trace of previous run, hierarchical_aggregation -> not trace of previous run, hierarchical_visualization (skip: skipping html output)
[2026-01-20T02:07:30.491381] Step 'extraction' started
[2026-01-20T02:08:00.566242] Step 'extraction' completed in 30.07s (token_usage=219804, cost=$0.0386)
[2026-01-20T02:08:00.566657] Step 'embedding' started
[2026-01-20T02:09:54.465461] Step 'embedding' completed in 113.90s (token_usage=0, cost=$0.0386)
[2026-01-20T02:09:54.470881] Step 'hierarchical_clustering' started
[2026-01-20T02:10:17.690810] Step 'hierarchical_clustering' completed in 23.22s (token_usage=0, cost=$0.0386)
[2026-01-20T02:10:17.691584] Step 'hierarchical_initial_labelling' started
[2026-01-20T02:10:25.716891] Step 'hierarchical_initial_labelling' completed in 8.03s (token_usage=41476, cost=$0.0477)
[2026-01-20T02:10:25.717396] Step 'hierarchical_merge_labelling' started
[2026-01-20T02:10:29.967746] Step 'hierarchical_merge_labelling' completed in 4.25s (token_usage=15450, cost=$0.0505)
[2026-01-20T02:10:29.968368] Step 'hierarchical_overview' started
[2026-01-20T02:10:33.520297] Step 'hierarchical_overview' completed in 3.55s (token_usage=1518, cost=$0.0508)
[2026-01-20T02:10:33.525990] Step 'hierarchical_aggregation' started
[2026-01-20T02:10:33.629066] Step 'hierarchical_aggregation' completed in 0.10s (token_usage=0, cost=$0.0508)
[2026-01-20T02:10:33.629110] Skipping step 'hierarchical_visualization' (skipping html output)
[2026-01-20T02:10:33.629686] Pipeline completed successfully in 183.19s
```

## polars実装でのログ
```md
[2026-01-20T02:46:20.192634] Pipeline started (force=False, only=None)
[2026-01-20T02:46:20.192672] Execution plan: extraction -> not trace of previous run, embedding -> not trace of previous run, hierarchical_clustering -> not trace of previous run, hierarchical_initial_labelling -> not trace of previous run, hierarchical_merge_labelling -> not trace of previous run, hierarchical_overview -> not trace of previous run, hierarchical_aggregation -> not trace of previous run, hierarchical_visualization (skip: skipping html output)
[2026-01-20T02:46:20.194132] Step 'extraction' started
[2026-01-20T02:46:44.269107] Step 'extraction' completed in 24.07s (token_usage=219789, cost=$0.0386)
[2026-01-20T02:46:44.269520] Step 'embedding' started
[2026-01-20T02:48:32.488457] Step 'embedding' completed in 108.22s (token_usage=0, cost=$0.0386)
[2026-01-20T02:48:32.493790] Step 'hierarchical_clustering' started
[2026-01-20T02:48:55.816983] Step 'hierarchical_clustering' completed in 23.32s (token_usage=0, cost=$0.0386)
[2026-01-20T02:48:55.817834] Step 'hierarchical_initial_labelling' started
[2026-01-20T02:49:02.517996] Step 'hierarchical_initial_labelling' completed in 6.70s (token_usage=41416, cost=$0.0477)
[2026-01-20T02:49:02.522667] Step 'hierarchical_merge_labelling' started
[2026-01-20T02:49:06.590521] Step 'hierarchical_merge_labelling' completed in 4.07s (token_usage=15159, cost=$0.0505)
[2026-01-20T02:49:06.594908] Step 'hierarchical_overview' started
[2026-01-20T02:49:10.318800] Step 'hierarchical_overview' completed in 3.72s (token_usage=1597, cost=$0.0508)
[2026-01-20T02:49:10.324562] Step 'hierarchical_aggregation' started
[2026-01-20T02:49:10.348322] Step 'hierarchical_aggregation' completed in 0.02s (token_usage=0, cost=$0.0508)
[2026-01-20T02:49:10.348372] Skipping step 'hierarchical_visualization' (skipping html output)
[2026-01-20T02:49:10.349008] Pipeline completed successfully in 170.16s
```

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **リファクタリング**
  * 全体的にデータ処理基盤をpandasからpolarsへ移行し、入出力と処理効率を改善
  * 埋め込みやクラスタリング、抽出〜集約〜ラベリングの各処理をpolarsベースで統一
  * スプレッドシート/レポート出力のCSV処理と列操作をpolarsに更新

* **バグ修正 / 安定性**
  * 埋め込み読み込みの形式検証、不整合検出、空結果や例外処理を強化

* **その他**
  * ビルド・依存設定を整理・拡充

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

