# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-10-14T17:25:26.041241+09:00 から 2026-10-21T17:25:26.041241+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (2件)

### [[FEATURE] AnthoropicのAPIに対応する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/1042)

**作成者:** tokoroten  
**作成日:** 2026-10-20T16:27:50Z  
**内容:**

# 背景

ClaudeCodeのMAXを契約していると、AnthoropicのAPIクレジットが無償配布されるようになったため、Anthoropicのクレジットが余っている開発者が増えている。
エンジニアの利用者を増やすのであれば、AnthoropicのAPIに対応するのが有効だと考える。

これまでも、AnthoropicのAPIKeyをOpenRouterに提供すれば、OpenRouter経由で利用することはできた。
しかし現在はOpenRouterでAPIKeyの漏洩の事故が起きているので、OpenRouterは使いづらくなっている。

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

**コメント:** なし

---

### [散布図: 全点フィルタ済みクラスタのラベルを薄くするか（効いていない dimming 分岐の挙動決定）](https://github.com/digitaldemocracy2030/kouchou-ai/issues/1023)

**作成者:** nishio  
**作成日:** 2026-10-16T11:49:39Z  
**内容:**

## 背景・現象

散布図（detail / density ビュー、クラスタラベル表示ON）で、フィルタ（注目度・テキスト検索など）を掛けて **ある最深クラスタの点が全部フィルタで消える** とき、そのクラスタの中心ラベル（名前ボックス）を薄くして「現在のフィルタに該当なし」を示す意図のコードがあります（`apps/public-viewer/components/charts/ScatterChart.tsx` の注釈ラベル）。

しかし実際には **薄くなりません**。全消えクラスタのラベルも、点が残っているクラスタのラベルも同じ濃さ（不透明度 0.8）で表示され、見分けがつきません。

## 比較（スクリーンショット）

全点フィルタで「防災・防犯」クラスタが 0 件になったときのラベル表示。**左＝現状 (b)** / **右＝選択肢 a（0.4 に薄く）**。

![現状(b) と 選択肢a の比較](https://raw.githubusercontent.com/nishio/kouchou-ai-developer-wiki/main/assets/review-2026-10-16/h-ab.png)

透明度の候補（白文字の読みやすさ ↔ 区別しやすさ のトレードオフ）:

![透明度サンプル 1.0〜0.3](https://raw.githubusercontent.com/nishio/kouchou-ai-developer-wiki/main/assets/review-2026-10-16/h-alpha.png)

> スクショは実コードの注釈スタイル（白太字 14px・borderpad 10・背景 rgba・SOFT_COLORS・フィルタ点は半透明グレー）を再現したモックです。実プロットの背景は白。

## 原因

ラベル背景色 `clusterColorMapA` は `SOFT_COLORS[i]`（`#RRGGBB`）＋ `Math.floor(0.8*255)=204=0xcc` ＝ **`#RRGGBBcc`**（末尾 `cc` が不透明度 0.8）。

dimming 分岐は末尾2桁（`cc`）を `"cc"` に置換しており、**`cc → cc` の no-op**。つまり `isAllFiltered` の分岐が背景色を何も変えていません。

```ts
const bgColor = isAllFiltered
  ? clusterColorMapA[id].replace(/[0-9a-f]{2}$/i, "cc") // ← 末尾 cc を cc に置換（無変化）
  : clusterColorMapA[id];
```

さらに同じ箇所に **互いに矛盾するコメント** があります:

- 「フィルターされていても背景色を維持（…ラベルは元の色で表示）」← *元の色を保つ*
- 「クラスター全体がフィルターされた場合も薄くする」← *薄くする*

どちらが本来の意図か不明なため、挙動を決めたいです。

## 質問：どちらを採用しますか？

いずれも挙動は **どちらか一方だけ採用** する想定です（2 つの候補 PR は択一。採用しない方は close します）。

- **(a) 薄くする** — 全消えクラスタのラベル背景を実際に薄く（不透明度 0.8 → 0.4）して「該当なし」を視覚化する。候補 PR: **#1024**
  - 留意点: ラベル文字は白なので、背景を薄くしすぎると白地に白文字で読みにくくなります。上のサンプルを見ると 0.4 は白文字がやや薄く、**0.5〜0.6** が「薄いと分かる」かつ「読める」のバランスが良さそうです（PR #1024 は現状 `66`=0.4。値は調整可能）。
- **(b) 元の色を維持** — 「背景色を維持」というコメントの意図を正とし、効いていない分岐・不要になった `@ts-ignore`・誤解を招くコメントを削除してシンプルにする（見た目は現状維持）。候補 PR: **#1025**

どちらがよいか（または第3案）をご指定ください。候補 PR: **#1024（選択肢 a）** / **#1025（選択肢 b）**。

---

（2026-10-16 のソースコードレビューで発見した軽微な表示バグ。データ・解析結果には影響しません。）


**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (29件)

### [test(api): 再利用の実行計画テストで、偽のステップが spec の成果物をすべて書くようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1047)

**作成者:** nishio  
**作成日:** 2026-10-21T02:36:13Z  
**変更:** +3 -3 (1ファイル)  
**マージ日:** 2026-10-21T02:38:35Z  
**内容:**

## 概要

#1043 と #1044 が両方入った main で、`apps/api/tests/services/test_report_duplicate.py` の llm_grouping の 2 ケースが失敗していたので、テストの前提を直します。本番のコードは変えていません。

## 原因

- #1043 で、llm_grouping の `hierarchical_merge_labels.csv` が spec の `extra_files` に入り、再実行判定で「前回の成果物がある」かを確かめる対象になりました。
- #1044 で足したテストは、複製元の status を本物の書き込み処理で作るときに、各ステップの代わりの偽ステップで成果物を書きます。この偽ステップは `filename` と抽出の `relations.csv` しか書いていませんでした。
- そのため、両方が入った main では、偽の複製元に merge labels が無く、llm_grouping が「previous data not found」で再実行され、テストの期待（overview と aggregation だけが再実行される）と食い違っていました。2 本はそれぞれ単独では CI を通っていました。

## 変更

- 偽ステップが、本物のステップと同じく spec の `filename` と `extra_files` をすべて書くようにしました（抽出の `relations.csv` の特別扱いはこれに含まれます）。

## テスト

- `apps/api` の `pytest tests --ignore=tests/manual`: 389 passed（修正前の main では 2 failed, 387 passed）
- `ruff check` / `ruff format --check`: 通過

🤖 Generated with [Claude Code](https://claude.com/claude-code)


**コメント:** なし

---

### [fix(public-viewer): 濃い意見が 0 件のときの切り替え先を有効な表示から選ぶ](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1046)

**作成者:** nishio  
**作成日:** 2026-10-21T02:18:00Z  
**変更:** +62 -6 (2ファイル)  
**マージ日:** 2026-10-21T02:25:33Z  
**内容:**

## 概要
公開ページで「濃い意見」の抽出結果が 0 件になったときの切り替え先を、管理者が有効にしている表示（`enabledCharts`）の中から選ぶようにします。

## 問題（再現条件）
1. 管理画面の「可視化設定」で、「表示するチャート」から「散布図（全体）」を外す（例: `enabledCharts: ["scatterDensity", "treemap"]`、デフォルト表示は `scatterDensity`）
2. 意見が少ないレポートや、最小件数を大きめにした設定などで、最深階層に条件を満たすクラスタが無い
3. 公開ページを開く（または表示設定で抽出条件を変えて 0 件にする）

この場合、選択ボタンは「濃い意見」「階層」の 2 つだけなのに、どちらも選ばれていない状態になります。そのうえ、管理者が外した「全体」の散布図（第 1 階層）と、第 1 階層のクラスタ一覧が表示されます。

## 原因
#1039 で、濃い意見の抽出結果が 0 件のときに一つ上の階層を濃い意見として表示しないよう、`ClientContainer` の `useEffect` で `scatterAll` へ切り替える処理を入れました。この切り替え先は固定で、`enabledCharts` を見ていませんでした。選択ボタン（`SelectChartButton`）は `enabledCharts` で絞り込みますが、`Chart` は `selectedChart` のプラグインをそのまま描画します。そのため、ボタンに無い表示が出ていました。

## 変更
- 切り替え先を、選択ボタンと同じ判定で選べる表示の中から選びます。判定には `resolveChartModes` を使い、`enabledCharts`、`chartOrder`、濃い意見を無効にする上書きを渡します。
  - 「全体」が選べれば、これまでどおり「全体」へ戻します
  - 「全体」が無ければ、表示順で先頭の選べる表示へ戻します
  - 他に選べる表示が無ければ切り替えません。濃い意見のまま、最深階層の散布図を該当クラスタなしで表示します。#1039 の「一つ上の階層を濃い意見として出さない」は保たれます

## テスト
- `apps/public-viewer/components/report/ClientContainer.test.tsx` に 3 件を追加しました
  - 「全体」を外した設定: 「階層」が選ばれ、ツリーマップを表示する（散布図は出ない）
  - `chartOrder` を指定した設定: 表示順で先頭の「リスト」を選ぶ
  - 「濃い意見」だけの設定: 「濃い意見」が選ばれたまま最深階層の散布図を表示し、第 1 階層のクラスタは一覧に出さない
- 修正前のコードでは、追加した 3 件がすべて失敗することを確認しました。修正前は、どのラジオも未選択のまま、第 1 階層の散布図と第 1 階層のクラスタ 7 件の一覧が表示されていました
- `npx jest`（public-viewer）: 160 passed（修正前の 157 件に 3 件を追加）
- `pnpm exec biome ci apps/public-viewer`、`npx tsc --noEmit -p .`: エラーなし

🤖 Generated with [Claude Code](https://claude.com/claude-code)

**コメント:** なし

---

### [fix(admin): レポート生成の完了後も管理画面のカードが「作成中」のまま止まる問題を直す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1045)

**作成者:** nishio  
**作成日:** 2026-10-21T02:17:58Z  
**変更:** +254 -11 (5ファイル)  
**マージ日:** 2026-10-21T02:25:29Z  
**内容:**

## 概要
レポート生成が終わっても、管理画面の一覧でカードが「AIによるレポート作成中です」のまま止まることがあります。その間は、手動で再読み込みするまで公開リンクや操作メニューが出ません。この問題を直します。成果物のアップロードに失敗して error になったときに、エラー表示とその理由が出ない問題も直します。

## 問題（再現条件）
- `STORAGE_TYPE=azure_blob` の環境で、管理画面の一覧を開いたままレポートを作成（または再利用・複製）すると起きる。
- 進捗のステップがすべて完了になっても、カードは「AIによるレポート作成中です」のまま変わらない。その後は step-json も一覧も問い合わせないので、再読み込みするまでリンク・公開設定・メニューが出ない。
- 成果物のアップロードに失敗して error になった場合も、作成中の表示のまま変わらない。エラー表示もエラー理由も出ない。
- ローカル保存（`STORAGE_TYPE=local`）でも、ときどき（1 割程度）同じように止まる。analysis-core が completed を書いてからプロセスが終わるまでに 1〜2 秒かかるため。

## 原因
- 進捗ポーリング（`useReportProgressPoll`）は、`hierarchical_status.json` が completed / error になった時点で止まる。その後 `ProgressSteps` は 1 秒後に `router.refresh()` を 1 回だけ呼んでいた。
- 一方、カードの表示を決める一覧の status（`report_status`）が ready / error になるのは、API が analysis-core の終了を待ち、成果物をストレージへ同期した後になる。
- #1034 で、ready にするのは成果物・入力・設定のアップロードがすべて成功した後になった。アップロードに失敗したレポートを ready にしないためで、この方針は維持する。
  - その結果、Azure Blob 運用では completed から ready までの間にアップロードの時間がまるごと入るようになった。1 回だけの取り直しでは processing を受け取りやすい（大きめのレポートではほぼ毎回）。
  - 取り直しが 1 回だけという作り自体は #1034 より前からある。そのため、ローカル保存でもこの間隔が 1 秒を超えると止まっていた。
- アップロードに失敗して error になった場合、`ProgressSteps` は completed の状態のまま残る。そのためエラー理由が表示されなかった。

## 変更
- `ProgressSteps`: completed / error を受けた後も、カードの status が processing の間は一覧を取り直し続ける。
  - 最初は従来どおり 1 秒後、その後は 3 秒おきに取り直し、最大 40 回（約 2 分）で打ち切る。
  - 上限を設けたのは、一覧 API が ready の全レポートの結果ファイルを読むため。
- error のカードにも `ProgressSteps` は残る。そこで `ReportCard` からレポートの status を渡し、取り直しは processing の間に限った。error のカードでは取り直さない。
- カードが ready になっても、`ProgressSteps` は退場アニメーションの間だけ古い props（processing）のまま残る。非表示のタブではアニメーションが進まず長く残るので、`useIsPresent` を使ってその間は取り直さない。
- completed を受けた後にカードが error になったときは、step-json を取り直してエラー理由（例: 成果物のアップロード失敗）を表示する。このため `useReportProgressPoll` に `restartPolling` を追加した。
- API は変更していない。

## テスト
### 追加したテスト
router の mock は、Next と同じく refresh の前後で同じ 1 つのオブジェクトにしている。
- `apps/admin/app/_components/ReportCard/ReportCard.test.tsx`（5 件）
  - step-json が completed でも、一覧が processing の間は取り直しを続け、ready になったら止める（退場アニメーション中も取り直さない）
  - step-json が error でも、一覧が processing の間は取り直しを続け、error になったら止める
  - 一覧が processing のまま変わらなくても、取り直しは上限で止まる
  - completed の後に一覧が error になったら step-json を取り直し、アップロード失敗の理由を表示する
  - error のカードでは一覧を取り直さない
- `apps/admin/app/_components/ReportCard/ProgressSteps/useReportProgressPolling.test.ts`（1 件）
  - completed で止まった後も、`restartPolling` で step-json を取り直せる

### 修正前に失敗することの確認
修正前のコード（fca42699）では、追加した 6 件がすべて失敗する。既存のテストは通過する。失敗の内容は次のとおり。
- 取り直しが 1 回で止まる
- error に切り替わっても step-json を取り直さない
- error のカードでも 1 回取り直す
- `restartPolling` が無い

### 修正後
apps/admin で次がすべて通過した。
- `npx jest`（186 件）
- `pnpm exec biome ci apps/admin`
- `npx tsc --noEmit -p .`

### 実ブラウザでの確認
admin を `next build` → `next start` で起動した。completed から一覧が ready / error になるまでの時間を変えられる偽 API と headless Chromium で、修正前後を比べた。
- completed の 4.5 秒後に ready
  - 修正前: 1 回の取り直しで processing を受け取り、40 秒たっても作成中のまま。
  - 修正後: 2 回目の取り直しで ready に切り替わり、リンクが出る。その後の要求は止まる。
- completed の 4.5 秒後に error
  - 修正前: 作成中のまま。
  - 修正後: error に切り替わった直後に step-json を取り直し、エラー表示と「Failed to upload report artifacts to storage」が出る。その後の要求は止まる。
- completed の 0.3 秒後に ready
  - 修正後も、従来どおり 1 回の取り直しで切り替わる。

🤖 Generated with [Claude Code](https://claude.com/claude-code)

**コメント:** なし

---

### [fix(api): 再利用での複製で完了記録の入力名を新しい slug に読み替え、抽出からの全段再実行を防ぐ](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1044)

**作成者:** nishio  
**作成日:** 2026-10-21T02:17:55Z  
**変更:** +231 -6 (2ファイル)  
**マージ日:** 2026-10-21T02:32:39Z  
**内容:**

## 概要

管理画面の「再利用」でレポートを複製すると、設定を何も変えなくても抽出から全段が再実行されていました。そのため中間成果物が再利用されていませんでした。この PR では、複製時に引き継ぐ完了記録の入力名（`global_params.input`）を新しい slug に読み替えて、変えていないステップの成果物をそのまま使うようにします。

## 問題（再現条件）

1. 現在の main でレポートを作成する（ラベルを手で直していてもよい）。
2. レポートカードの「再利用」から、設定を変えずに（またはクラスタ数だけ変えて）開始する。
3. analysis.log に `(!) extraction global parameter 'input' changed from '<元slug>' to '<元slug>-copy-YYYYMMDD'` が出る。hierarchical では extraction から hierarchical_merge_labelling まで、llm_grouping では extraction・embedding・llm_grouping がすべて再実行される。

影響は次のとおりです。

- 全コメント分の抽出（LLM 呼び出し）と埋め込みに、費用と時間がもう一度かかる。
- 抽出結果・クラスタ・ラベルが複製元と変わる。そのため「同じ意見のままクラスタ数だけ変えて比べる」という使い方ができない。
- 複製元で手直ししたラベル（`hierarchical_merge_labels.csv`）は、複製先では再生成で置き換わり、引き継がれない。

`global_params` の無い記録しか持たないレポート（#1033 より前に実行したもの）を複製した場合は、従来どおり再利用されます。

## 原因

- #1033 で、analysis-core は各ステップの完了記録に `global_params`（input・question・intro・is_pubcom・enable_source_link）を残すようになりました。再実行の判定では、これを config と比べます。extraction は `input` に依存します。
- API の複製は、入力 CSV を `inputs/<新slug>.csv` にそのままコピーし、config の `input` を新しい slug に書き換えます。一方で、複製元の `completed_jobs` / `previously_completed_jobs` は `global_params` ごとそのまま引き継いでいました。#1034 で status の引き継ぎを `_write_reuse_status` にまとめた後も、この点は同じです。
- その結果、中身が同じ入力でも名前が違うだけで「input が変わった」と判定されます。さらに依存関係により、下流のステップもすべて再実行になっていました。#1033 では、API の複製（`reuse_from` を使わない経路）が status を引き継いで再利用している点が考慮されていませんでした。

## 変更

`apps/api/src/services/report_duplicate.py` を変更しました。

- `_write_reuse_status` に `renamed_input=(複製元の入力名, 複製先の入力名)` を追加しました。`global_params.input` が複製元の slug になっている記録だけを、新しい slug に書き換えます。
  - 対象は `completed_jobs` と `previously_completed_jobs` の両方です。ラベル編集の後は、上流の記録が `previously_completed_jobs` 側にあるためです。
- 書き換えるのは、入力 CSV をそのままコピーした場合だけです。複製元の入力が無く、`hierarchical_result.json` の arguments から入力を作り直した場合は中身が違うので書き換えず、抽出からやり直します。
- 次のものには触れません。
  - `global_params` の無い古い形式の記録
  - input 以外の値（question など。変更は従来どおり analysis-core が検知します）

## テスト

`apps/api/tests/services/test_report_duplicate.py` を更新・追加しました。

- **既存テストの見直し:** これまでのテストは、`global_params` の無い手書きの status を使っていたため、この回帰を検出できませんでした。現在の analysis-core が書く形（`global_params` 付き）の記録と、古い形式の記録を混ぜるように変えました。そのうえで、input だけが新しい slug に読み替わり、ほかの値と古い形式の記録は変わらないことを確かめます。
- **追加したテストの流れ:**
  1. API の書き出し処理（`save_config_file` / `save_input_file`）で複製元を作る。
  2. analysis-core の本物の `initialization` / `run_step` / `termination` で status を書く。各ステップの中身だけは、成果物ファイルを書く偽物にする。
  3. `duplicate_report` で複製する。
  4. 複製後の config で `initialization(persist_status=False)` を呼び、実行計画を確かめる。
- **確かめる内容:**
  - 変更なしの場合、hierarchical では extraction〜hierarchical_merge_labelling が skip され、llm_grouping では extraction・embedding・llm_grouping が skip される。run になるのは overview と aggregation だけ。
  - クラスタ数だけ変えた場合、run になるのは hierarchical_clustering 以降だけ。
  - 上の各ケースは、ラベル編集後の複製元でも同じ結果になる。ラベル編集後とは、aggregation だけを再実行して、上流の記録が `previously_completed_jobs` に移った状態を指す。
  - arguments から入力を作り直した場合は、extraction が `some parameters changed: input` で run になる（書き換えすぎを防ぐ確認）。
- **修正前の失敗:** 修正前のコードでは、既存テスト 1 件と、追加した実行計画のテスト 6 件が失敗することを確認しました。いずれも extraction が `some parameters changed: input` で run になっていました。修正後は、このファイルの 9 件すべてが通ります。
- **全体の結果:**
  - `apps/api` の `pytest tests --ignore=tests/manual`: 389 passed（修正前は 382 passed で、追加分が 7 件）
  - `packages/analysis-core` の `pytest tests`: 406 passed（変更なし）
  - ruff check / format --check: 通過
- **本番に近い経路での確認:** 本物の API（作成 → ラベル編集 → 再利用での複製）と `python -m analysis_core` を通して確かめました。偽物にしたのは LLM と埋め込みの呼び出しだけです。
  - 変更なしの複製: LLM 呼び出しは overview の 1 回だけでした。`args.csv` と `embeddings.pkl` は複製元と一致し、手直ししたラベルも複製先に引き継がれました。
  - クラスタ数の変更: 再実行されたのはクラスタリング以降だけでした。
  - llm_grouping: 再実行されたのは overview と aggregation だけでした。

## 今後の案

根本的には、analysis-core 側で入力の名前ではなく入力 CSV の内容のハッシュ（例: `input_sha256`）を完了記録に残して比べる方法があります。

- API での読み替えが不要になります。
- CLI の `--reuse-from` でも同じ比較を共有できます。
- 同じ名前のまま入力 CSV の中身だけが差し替わった場合も検知できます。

ただし、次の対応が必要になるため、今回は入れていません。

- 名前しか持たない既存の記録との互換を保つこと。
- 「input 名の変更で extraction が再実行される」既存テストを、内容の違う CSV で確かめる形に見直すこと。

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

<!-- coderabbit-ai-generated:v1 -->

## Summary by CodeRabbit

- **Bug Fixes**
  - Improved report duplication with reused processing status so directly copied inputs retain accurate completion information.
  - Ensured rebuilt inputs rerun extraction instead of incorrectly inheriting completion status from the original report.
  - Preserved compatibility with older or incomplete status records without valid input details.
- **Tests**
  - Added coverage for status preservation, input renaming, report duplication, and selective step reruns.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix(analysis-core): --reuse-from の成果物の複製と、再実行時のトークン引き継ぎの不具合を直す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1043)

**作成者:** nishio  
**作成日:** 2026-10-21T02:17:53Z  
**変更:** +422 -34 (9ファイル)  
**マージ日:** 2026-10-21T02:32:35Z  
**内容:**

## 概要

CLI の `--reuse-from` と、再実行時に前回分のトークン数を引き継ぐ処理（#1031）にあった 3 つの不具合を直します。

1. llm_grouping モードで `--reuse-from` を使うと `hierarchical_merge_labels.csv` が複製されず、集計が必ず失敗する
2. 強制終了された実行を `--reuse-from` の複製元にすると、ステップの古い記録を採用し、新しい成果物を古いパラメータのものとして再利用する
3. 再実行時に引き継ぐトークン数が、途中失敗の後の再実行やステップの無効化で実際と食い違う

## 問題（再現条件）

### 1. llm_grouping の `--reuse-from` で集計が失敗する

1. `analysis_mode=llm_grouping` のジョブ A を完了する
2. 同じ設定のジョブ B（または intro・hidden_properties・sampling_num など集計側の設定だけを変えたジョブ）を `--reuse-from A` で実行する
3. extraction / embedding / llm_grouping / overview が SKIP、集計が RUN の計画になり、集計が `Step 'aggregation' validation failed: Missing required input: merge_labels` で失敗する（exit 1）。overview の prompt / model だけを変えた場合は、overview が同じ理由で失敗する

- `--dry-run` の計画には兆候が出ません。失敗した出力ディレクトリには status が残るため、同じコマンドで再実行しても同じ失敗を繰り返していました
- API / 管理画面の複製は `--reuse-from` を使わず、merge labels も明示的にコピーしているので影響しません

### 2. 強制終了された複製元の古い記録を採用する

1. A を `hierarchical_clustering.cluster_nums = [2, 4]` で完了する
2. A を `[3, 6]` に変えて再実行し、クラスタリングの完了後に OOM / SIGKILL などで強制終了される（status は running のまま、clustering の新旧の記録が並ぶ）
3. B を `[2, 4]` で `--reuse-from A` として実行すると、B にコピーされる `hierarchical_clusters.csv` は `[3, 6]` の結果なのに seed される記録は `[2, 4]` なので、clustering と initial_labelling が「nothing changed」で SKIP され、クラスタとラベルが食い違ったレポートが黙ってできる

### 3. 引き継ぐトークン数が実際と食い違う

各 LLM ステップが 100 トークンを使う場合:

- 途中失敗の後の再実行: 全段を完了（400）→ overview の prompt を変えて再実行し overview で失敗（error、300）→ 同じ設定で再実行して成功すると 300 になる（成果物の記録の合計は 400）
- ステップの無効化: opinion_classification を有効にして実行（500）→ 無効にして `--force` で再実行しても 500 のまま（正しくは 400）。analysis_mode を同じ出力先で切り替えた場合も、使われなくなったステップの分が持ち越される

API の「集計だけ再実行」（ラベル編集・設定編集）は正しく動いており、影響しません。

## 原因

1. `_seed_reused_outputs` と `decide_what_to_run` は、各ステップの spec の `filename` しか複製・存在確認していませんでした（extraction の `relations.csv` だけ特別扱い）。llm_grouping は `hierarchical_clusters.csv` と `hierarchical_merge_labels.csv` の 2 つを書き、overview と集計は後者を読みます。この欠落は llm_grouping モード（#866）と `--reuse-from`（#867）が入った時点からあり、当時は overview だけを変えた場合に限って表に出ていました。#1033 で集計を複製せず常に再実行するようにしたため、llm_grouping を再実行しないすべての reuse で失敗するようになりました
2. #1033 から、実行中の status に `completed_jobs`（新しい記録）と `previously_completed_jobs`（前回までの記録）が並びます。`_seed_reused_outputs` はこの 2 つを連結して dict 内包表記でまとめていたため、後ろにある古い記録が勝っていました。再実行判定は #1033 で `collect_previous_jobs` により新しい記録を優先するよう直っていましたが、seed 側は古い記録を優先したままでした
3. #1031 の `carried_over_token_usage` は「前回の合計 − 今回再実行するステップの最新記録」で引き継ぎ分を求めていました。途中で失敗した実行の合計は開始時に再実行予定のステップ分を差し引き済みなのに、完了できなかったステップの最新記録は古いままなので、二重に差し引かれます。また run=False のステップは差し引かれないため、無効化したステップや計画に無いステップの分が持ち越されていました

## 変更

- spec に `extra_files` を設け、extraction の `relations.csv` と llm_grouping の `hierarchical_merge_labels.csv` を宣言しました。`--reuse-from` の複製と、再実行判定の「前回の成果物がある」の確認を `filename` と `extra_files` の全部で行います（extraction の `relations.csv` の特別扱いはこれに置き換え）。片方でも欠けていれば、そのステップを再実行します
  - 既に上記 1 の失敗で止まっている出力ディレクトリも、同じコマンドの再実行で llm_grouping からやり直して完了します（複製元の成果物は使われません。複製元を使いたい場合は出力ディレクトリを消して再実行してください）
- `_seed_reused_outputs` で、再実行判定と同じ `collect_previous_jobs` によりステップごとに最新の記録を採ります
- `carried_over_token_usage` は、今回実行せず成果物を残すステップ（計画にあり run=False で、設定で無効化されていないもの）の最新記録を足し合わせて引き継ぎ分とします。入出力の内訳がない古い記録は、従来どおり前回合計の比率で按分します
  - 前回の合計は上限として残しました。管理画面の複製では複製元の記録がそのまま写されますが、複製先の合計には数えていないためです（上限が無いと、複製したレポートでラベルを編集するとトークン数が複製元の分だけ増えます）
  - そのため、既に食い違った合計が記録されている status は自動では直りません（`--force` で数え直せます）
- 無効化の判定（without-html の可視化、無効の opinion_classification）を `_disabled_reason` にまとめ、`decide_what_to_run` と `carried_over_token_usage` で共有しました
- 前回の成果物を模した既存テストのフィクスチャ（args.csv だけを置いていたもの）に `relations.csv` を足しました。extraction は args.csv と relations.csv を必ず続けて書き、API の複製・ストレージ同期も relations.csv を保持しています

## テスト

追加した回帰テスト（上限の確認を除き、すべて修正前に失敗し、修正後に通ることを確認しました）:

- `test_rerun_decisions.py::TestSecondaryArtifacts`
  - `test_reuse_from_seeds_llm_grouping_merge_labels`: llm_grouping の複製元から merge labels が seed され、`--dry-run` 相当でも llm_grouping が SKIP になる（修正前: merge labels が無い）
  - `test_reused_llm_grouping_job_runs_aggregation`: `PipelineOrchestrator.from_config(..., reuse_from=...).run_default()` を実物の WorkflowEngine と集計ステップで通す（修正前: `Missing required input: merge_labels`）
  - `test_missing_secondary_artifact_reruns_step`（llm_grouping の merge labels / extraction の relations.csv）: 欠けていれば「previous data not found」で再実行する（修正前: nothing changed）
- `test_rerun_decisions.py::TestReuseFromInterruptedSource::test_reuse_from_uses_latest_record_of_each_step`: 強制終了された複製元で clustering が「cluster_nums changed」で RUN になる（修正前: SKIP）
- `test_orchestration.py::TestTokenUsageCarryOver`
  - `test_carried_over_token_usage_after_failed_partial_rerun`（修正前: 700 のところ 400）
  - `test_carried_over_token_usage_skips_steps_no_longer_in_the_report`（無効化 + `--force`、無効化 + 集計だけ、analysis_mode の切り替え）
  - `test_cli_retry_after_failed_partial_rerun_counts_every_kept_step`: from_config + run_default の CLI 経路で 400 → 失敗 300 → 再実行 400（修正前: 300）
  - `test_cli_force_after_disabling_a_step_drops_its_tokens`: 500 → 無効化 + `--force` で 400（修正前: 500）
  - `test_carried_over_token_usage_never_exceeds_previous_totals`: 複製したレポートの集計だけの再実行で合計が増えない（上限の確認。修正前から通る）

実行結果:

- `packages/analysis-core`: `pytest tests` 416 passed（変更前 406 + 追加 10）、`ruff check .` 通過
- `apps/api`: `pytest tests --ignore=tests/manual` 382 passed（変更前と同数）
- 手元で実物の CLI 経路（LLM と埋め込みの呼び出しだけ差し替え）で llm_grouping のジョブ A を作り、`--reuse-from A` で「同一設定」「intro だけ変更」「overview の prompt だけ変更」「group_count を変更」の 4 通りを実行して、すべて完了し、結果の output_dir と intro が新しいジョブの値になることを確認しました。同一設定と intro 変更では LLM・埋め込みの呼び出しが 0 回でした

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

<!-- coderabbit-ai-generated:v1 -->

## Summary by CodeRabbit

- **New Features**
  - Improved workflow reruns by recognizing primary and additional step artifacts.
  - Added support for relation and grouping-label files in pipeline outputs.
  - Rerun selection now uses the latest available step status, including interrupted runs.

- **Bug Fixes**
  - Improved token carryover accuracy by excluding disabled or out-of-plan steps and preventing duplicate historical counts.
  - Ensured missing secondary artifacts trigger the appropriate reruns.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix(admin): 再利用ページで分析方式を変更不可にし、レポート作成エラーの詳細を表示する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1041)

**作成者:** nishio  
**作成日:** 2026-10-18T18:21:40Z  
**変更:** +169 -28 (6ファイル)  
**マージ日:** 2026-10-19T03:58:30Z  
**内容:**

## 概要
管理画面の 2 つの不具合を直します。1 つは、再利用ページで分析方式を変えても反映されない点です。もう 1 つは、レポート作成に失敗したときにエラーの詳細が表示されない点です。

## 問題
- 再利用ページ（`app/reuse/[slug]`）では分析方式の select を操作できました。しかし duplicate API の override（`ReportDuplicateOverrides`）は `analysis_mode` を受け付けないため、変更は送信されず、元レポートの方式で黙って実行されていました。
- `createReport`（Server Action）は失敗時に `response.statusText` だけを返していました。そのため API が返す `detail`（例: `Invalid slug format`、422 の検証エラー）が捨てられ、トーストには `Bad Request` などの HTTP 理由句しか出ませんでした。再利用ダイアログでは `detail` を表示しており、作成だけ扱いが違っていました。

## 変更
- `AISettingsSection` に任意 prop `analysisModeLocked` を追加しました。true のときは分析方式を `Field.Root disabled` で無効にし、「再利用元レポートの分析方式を引き継ぎます（再利用時は変更できません）」と表示します。再利用ページでのみ有効にしています。
- `createReport` は失敗時にレスポンス本文を読みます。`detail` が文字列ならそのまま、配列なら `loc: msg` の形に整形して返し、読めない場合だけ `statusText` に戻します。

## テスト
- 新規 `app/reuse/[slug]/page.test.tsx`: 再利用元の分析方式が表示され、変更できないことを確認します。
- `AISettingsSection.test.tsx`: 固定時は選択不可、通常時は選択可のテストを追加しました。
- 新規 `app/create/api/createReport.test.ts`: detail が文字列の場合、422 の配列の場合、JSON でない本文の場合を確認します。
- 新規テストは修正前に失敗することを確認済みです。`pnpm test`（26 suites / 178 tests）、`biome ci`、`tsc --noEmit` はすべて通ります。

## 補足
レポートのライフサイクル修正の PR と `createReport.test.ts` が衝突します。後から merge する側で解消してください（テストの追加箇所が重なるだけです）。

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * When reusing a report, the analysis mode is shown as inherited from the source report and cannot be changed.
  * API error messages now include details returned by the server, with a fallback when no usable details are available.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix(public-viewer): 静的ビルドのメタ画像を API から取得し、default の reporter.png を混ぜない](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1040)

**作成者:** nishio  
**作成日:** 2026-10-18T18:21:34Z  
**変更:** +196 -27 (4ファイル)  
**マージ日:** 2026-10-19T03:51:10Z  
**内容:**

## 概要
static-site-builder で作る静的 HTML 出力に、古いメタ画像や default のテスト用 reporter.png が入らないようにします。

## 問題
static-site-builder の Dockerfile は、イメージ作成時点の `apps/api/public` をコピーしてイメージに含めます。ボリュームの共有はありません。そのため、ビルド後に `apps/api/public/meta/custom` へ画像を追加・更新し、再ビルドせずに起動すると、静的出力の icon.png / ogp.png / reporter.png は古いコピーになります（初期状態なら default のテスト画像）。
一方、reporter 画像を表示するかどうかは live API（custom の有無）で判定します。このため custom/reporter.png を置いた環境では、default のテスト用 reporter.png が表示されていました。

## 変更
- `apps/public-viewer/scripts/copy-image.mjs`
  - ビルドのたびに `API_BASEPATH`（なければ `NEXT_PUBLIC_API_BASEPATH`）の `/meta/{icon,ogp,reporter}.png` を取得し、取得できた画像を優先して使います
  - `/meta/reporter.png` が 204（custom なし）の時は、前回のビルドで残った reporter.png も出力から消します
  - API に届かない時はローカルの custom → default の順にフォールバックします。ただし default のテスト用 reporter.png はコピーしません
  - `copyImages` を export し、直接実行された時だけ動くようにしました
- `apps/public-viewer/package.json`: `test` で node:test の回帰テストも実行します
- `.github/workflows/client-jest.yml`: `*.mjs` の変更でもテストが走るよう paths に追加しました

## テスト
- 回帰テスト `scripts/copy-image.test.mjs`（4 件）を追加しました。修正前のスクリプトでは 4 件とも失敗し、修正後は 4 件とも通ります
- `pnpm --filter @kouchou-ai/public-viewer test`: jest 142 passed、node:test 4 passed
- `pnpm exec biome ci apps/public-viewer`、`tsc --noEmit`: 問題なし

🤖 Generated with [Claude Code](https://claude.com/claude-code)

**コメント:** なし

---

### [fix(public-viewer): OGP 画像と表示まわりの不具合を直す（濃い意見 0 件・フォントキャッシュ・params の Promise・/meta 画像・ビルド失敗時の改名・4xx リトライ・metadataBase）](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1039)

**作成者:** nishio  
**作成日:** 2026-10-18T18:21:31Z  
**変更:** +520 -65 (23ファイル)  
**マージ日:** 2026-10-19T03:50:59Z  
**内容:**

## 概要
公開ビューア（apps/public-viewer）の OGP 画像生成と表示まわりの不具合 7 件を直します。

## 問題
- 「濃い意見」モードで抽出結果が 0 件になると、フィルタ後の result から最深階層を計算していたため、一つ上の階層の全クラスタを「濃い意見」として表示していた
- OGP のフォント取得に失敗した Promise がキャッシュに残り、Google Fonts が一度失敗するとプロセスを再起動するまで OGP 生成が失敗し続けていた
- Next 16 では opengraph-image に渡る params が Promise になったのに同期で読んでいたため、SSR のすべてのレポートで OGP 画像が失敗していた（/reports/undefined を取りに行っていた）
- fetchApiWithRetry が、4xx で自分が投げた例外を同じ catch で拾い、リトライしないはずの 404/401 でも 6 回（約 5 秒）アクセスしていた
- build / build:static / build:shell が失敗すると post スクリプトが走らず、改名した opengraph-image のルートが作業ツリーに残っていた
- サーバーモードでは public/meta がコピーされないため、/meta/icon.png（favicon）・/meta/reporter.png・/meta/ogp.png が 404 になっていた
- 静的書き出しでは metadataBase を設定していなかったため、og:image が http://localhost:3000/... に解決され、ベースパスも付かなかった

## 変更
- 最深階層はフィルタ前の result で決める（ChartRenderContext に modeResult を追加）。抽出結果が 0 件になったら全体表示に戻す
- フォント取得が失敗したらキャッシュを消す。res.ok も確認する
- opengraph-image で `await params` する
- リトライ判定を整理し、catch するのは fetch の例外（ネットワークエラー）だけにした。4xx は 1 回で失敗させる
- `scripts/with-renamed-files.mjs` を追加し、改名 → ビルド → 復元を try/finally で必ず実行する。build 系の pre/post の改名・復元は削除した
- サーバーモードでは next.config の rewrites で `/meta/*` を API に転送する
- `getMetadataBase()`（NEXT_PUBLIC_SITE_URL とベースパスから作る）を追加し、静的書き出しでも metadataBase を設定する。未設定ならビルド時に警告する。og:image のパスはベースパスなしの絶対パスにした
- `apps/public-viewer/.gitignore` に `tsconfig.tsbuildinfo` を追加した（ビルドキャッシュを追跡しない）。docs/development/web-ui-node-runtime-dependencies.md の og:image の記述を新しいパスに合わせて更新した

## テスト
- 各指摘に回帰テストを追加した（jest 15 件）。修正前のコードではいずれも失敗することを確認した
- `pnpm exec biome ci apps/public-viewer`、`tsc --noEmit`、`pnpm --filter @kouchou-ai/public-viewer test`（24 suites / 157 tests passed）
- API がない状態で `pnpm run build:static` を実行し、ビルドが失敗しても OGP 画像ルートが元の名前に戻ることを確認した

🤖 Generated with [Claude Code](https://claude.com/claude-code)

**コメント:** なし

---

### [fix(api): ローカル LLM のモデル一覧取得をパイプラインと同じ接続先にし、Gemini 接続確認のエラー分類を直す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1038)

**作成者:** nishio  
**作成日:** 2026-10-18T18:21:27Z  
**変更:** +90 -13 (5ファイル)  
**マージ日:** 2026-10-19T03:50:49Z  
**内容:**

## 概要
API 側のプロバイダ処理で見つかった2件の不具合を直します。

## 問題
1. `/admin/models` のローカル LLM（`get_local_llm_models`）が、パイプラインの `_resolve_local_llm_base_url` とは別に自前でアドレスを解析し、api_key も `not-needed` に固定していました。
   - `https://host` → `http://https://host/v1` という不正な URL になる
   - `https://host:port` → unpack の ValueError で 400
   - ポート省略の `ollama` → 80 番に接続
   - `LOCAL_LLM_API_KEY` が送られない
   その結果、パイプラインなら動く HTTPS ゲートウェイ構成でも、管理画面ではモデルを選べませんでした。
2. 管理画面の接続確認（`/admin/environment/verify`）が Gemini のエラーを `google.api_core.exceptions` で判定していましたが、本番の依存に google-api-core は無く、実際に投げられるのは `google.genai.errors.ClientError`（または 429 のリトライを使い切った後の `RuntimeError`）です。そのため無効なキーでもレート制限でも「不明なエラー」と表示されていました。

## 変更
- analysis-core: `_resolve_local_llm_base_url` を `resolve_local_llm_base_url` として公開化（旧名は alias で残す）
- api: `get_local_llm_models` は `resolve_local_llm_base_url` と `LOCAL_LLM_API_KEY`（既定 `not-needed`）を使い、パイプラインと同じ接続先・認証でモデル一覧を取得する
- api: 接続確認で `google.genai.errors.APIError` の `code` を見て分類する（400 の `API_KEY_INVALID`・401・403 → `authentication_error`、429 → `rate_limit_error`）。Gemini で 429 のリトライを使い切った `RuntimeError` も `rate_limit_error` とする

## テスト
- `apps/api/tests/services/test_model_catalog.py::test_local_models_use_pipeline_address_resolution`（4ケース。修正前は全件失敗）
- `apps/api/tests/routers/test_admin_report.py::TestVerifyApiKey::test_verify_api_key_gemini_classifies_errors`（6ケース。修正前は5件失敗）
- apps/api: 343 passed、packages/analysis-core: 330 passed、変更ファイルは ruff check / format --check 通過

🤖 Generated with [Claude Code](https://claude.com/claude-code)

**コメント:** なし

---

### [fix(analysis-core): LLM プロバイダまわりの不具合修正（Flex のタイムアウト、Gemini の思考トークン、Gemini 埋め込みの 429、local アドレスの解析、overview の代替処理）](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1037)

**作成者:** nishio  
**作成日:** 2026-10-18T18:21:23Z  
**変更:** +393 -95 (11ファイル)  
**マージ日:** 2026-10-19T03:50:38Z  
**内容:**

## 概要
analysis-core の LLM プロバイダまわりで見つかった不具合を 5 件直します。

## 問題
1. **バッチ待機タイムアウトで、遅れて成功した応答を捨てていた**: 意見抽出と意見分類では、1 リクエストの timeout と同じ値でバッチ側も `concurrent.futures.wait` していました。そのため、Flex（最大 900 秒）や SDK 内部の再試行で timeout を超えてから成功した応答も TimeoutError として扱われ、分析全体が中断していました。実行中の future は cancel できず、executor を抜けるときに結局待つので、この待機上限は所要時間を短くする役にも立っていませんでした。
2. **Gemini の思考トークンを集計していなかった**: gemini-2.5 系は既定で thinking が有効です。しかし出力トークンに `candidates_token_count` だけを使っていたため、`thoughts_token_count` が集計にも概算費用にも入っていませんでした。
3. **Gemini 埋め込みが 429 で止まっていた**: 1 テキストにつき 1 リクエストを順番に送り、429 を再試行していませんでした。件数が多いと埋め込みステップ全体が失敗していました。
4. **local LLM のアドレスを黙って差し替えていた**: `host:port` の解析に失敗すると（末尾のスラッシュ、IPv6、数値でないポート）、警告を出すだけで `localhost:11434` に接続先を差し替えていました。
5. **overview の代替処理が JSON 文字列をそのまま公開していた**: JSON のパースに失敗すると think タグを除くだけで、think の後ろに付いた JSON や途中で切れた JSON がそのまま `hierarchical_overview.txt` に書かれていました。応答が None のときは TypeError で落ちていました。

## 変更
1. `extract_batch` / `classify_batch` からバッチ側の待機上限を外しました。1 リクエストの上限は SDK に渡す timeout に任せます。遅れて完了した応答のトークンも集計されます。
2. Gemini の出力トークンに `thoughts_token_count` を加えました。
3. Gemini 埋め込みは 100 件（batchEmbedContents の上限）ずつまとめて送ります。429 は chat 経路と同じ指数バックオフで最大 5 回まで再試行し、返ってきた埋め込みの件数が入力と合わなければエラーにします。
4. local LLM のアドレスは `urlsplit` で解析します。末尾の `/` と角括弧付きの IPv6 は受け付け、それ以外の解析できないアドレスは `ValueError` にします。
5. overview は、think タグを除いた後に JSON を取り出し直して `summary` を使います。summary を取り出せない JSON、空の応答、None は失敗として扱い、ファイルを書きません。JSON を返さずに要約文だけを返すモデルの本文は、これまでどおり使います。

## テスト
- 各修正に回帰テストを追加し、修正前のコードでは失敗することを確認しました（21 件が失敗）。
- analysis-core で `pytest -q tests` を実行し、353 passed。
- apps/api で `pytest -q tests --ignore=tests/manual` を実行し、333 passed。
- 変更したファイルに `ruff check` を実行し、問題なし。

## 補足
apps/api の `llm_models.py`（モデル一覧の取得）は、local アドレスを別の方法で解析しています。今回は analysis-core 側だけを直したので、そちらは手を入れていません。

🤖 Generated with [Claude Code](https://claude.com/claude-code)

**コメント:** なし

---

### [fix(api): スプレッドシート取り込みで comment-id の型と属性値の先頭ゼロを保つ](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1036)

**作成者:** nishio  
**作成日:** 2026-10-18T18:21:20Z  
**変更:** +49 -2 (4ファイル)  
**マージ日:** 2026-10-19T03:50:28Z  
**内容:**

## 概要
スプレッドシートを取り込むとき、CSV の全列を文字列として読むようにしました。これで comment-id が数値でもレポートを作成でき、属性値の先頭の 0 も消えなくなります。

## 問題
- `fetch_public_spreadsheet`（`services/spreadsheet_service.py`）と `get_spreadsheet_data`（`routers/spreadsheet.py`）が、型推論ありで `pl.read_csv` を呼んでいました。
- そのため comment-id が数値のシートでは、`id` が JSON の int で返ります。admin 画面はこの値をそのまま `POST /admin/reports` に送り、`Comment.id: str` が数値を受け付けないため 422 で失敗していました。
- 属性列も数値として読まれたあとに `str()` で文字列に戻すため、`'01'` が `'1'` になり、先頭の 0 が何の警告もなく消えていました。
- CSV アップロード経路はフロント側の `parseCsv` で `String()` しているため、この問題は起きません。

## 変更
- 2 か所の `pl.read_csv` に `infer_schema_length=0` を指定し、全列を文字列で読むようにしました。

## テスト
- `tests/routers/test_spreadsheet.py`: 取り込み済み CSV に数値の comment-id と先頭 0 つきの属性値を入れ、`id` が文字列で返ること、属性値の先頭 0 が残ることを確認します。
- `tests/services/test_spreadsheet_service.py`: `fetch_public_spreadsheet` の結果で、comment-id 列が Utf8 になり、値が元のまま残ることを確認します。
- どちらも修正前に失敗することを確認しました。修正後、api テストは 335 passed、ruff check / format --check も通っています。

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Spreadsheet data now preserves values such as IDs and ZIP codes as strings, retaining leading zeros and preventing numeric-looking IDs from being converted to numbers.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix(api): llm_grouping レポートのラベル一覧取得・編集で CSV を壊さないようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1035)

**作成者:** nishio  
**作成日:** 2026-10-18T18:21:16Z  
**変更:** +135 -49 (5ファイル)  
**マージ日:** 2026-10-19T03:50:16Z  
**内容:**

## 概要
llm_grouping（LLM 直接グルーピング）で作ったレポートでは、管理画面のラベル編集が使えません。API を直接呼ぶと hierarchical_merge_labels.csv の中身が消えます。この PR はその修正です。

## 問題
- llm_grouping が出力する `hierarchical_merge_labels.csv` には `density` / `density_rank` 列がありません。そのため `ClusterRepository.read_from_csv` が全行を KeyError としてスキップし、`GET /admin/reports/{slug}/cluster-labels` が常に空を返していました
- `PATCH /admin/reports/{slug}/cluster-label` は、その空の読み込み結果を固定の列リストで書き戻します。その結果、CSV がヘッダーだけに切り詰められていました
- 存在しない id を指定しても成功として扱われ、ファイルが書き直されていました

## 変更
- `read_from_csv`: density 系の列を `row.get()` で任意扱いにしました（`ClusterResponse` 側は既に Optional）
- `update_csv`: 元ファイルの列構成と行をそのまま保ち、対象 id の label / description だけを書き換えるようにしました
- `update_csv`: 読み込めた行が 0 件のときは書き込まずに失敗を返します
- `update_csv`: 対象 id が無いときは `ClusterNotFound` を送出します。ルーターは 404 を返し、集計は実行しません
- 使われなくなった `ClusterRepository.FIELDS` を削除しました

## テスト
- llm_grouping 形式の CSV（実ファイル）で、読み込み・列を保った更新・未知 id・空ファイルを確認する回帰テストを追加しました（4 件）
- ルーターについて、未知 id で 404 を返し集計を呼ばないことを確認するテストを追加しました
- 既存の更新テストは、実ファイルを使う形に書き換えました
- 追加した 5 件は修正前に失敗し、修正後に通ることを確認しました
- `pytest -q tests --ignore=tests/manual`（apps/api）: 338 passed。ruff check / format --check も問題ありません

🤖 Generated with [Claude Code](https://claude.com/claude-code)

**コメント:** なし

---

### [fix: レポートのライフサイクルの不具合をまとめて修正（設定編集での項目消失・既存 slug の上書き・再起動で processing 固着・アップロード失敗で ready・複製直後のポーリング停止）](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1034)

**作成者:** nishio  
**作成日:** 2026-10-18T18:21:12Z  
**変更:** +539 -36 (13ファイル)  
**マージ日:** 2026-10-19T03:50:05Z  
**内容:**

## 概要
レポートの作成・編集・複製・完了処理・サーバー再起動の各段階で見つかった、データ整合性と状態遷移の不具合を直します。

## 問題
1. **タイトル・説明の編集で config の項目が消える**: `PATCH /admin/reports/{slug}/config` が `ReportConfig` を通して config を書き戻すため、`ReportConfig` に定義のない `enable_source_link` と `embedding.model` が落ちていました。その後の再集計で、出典リンクや埋め込みモデルの指定が黙って失われます。
2. **既存 slug でのレポート作成が上書きになる**: `POST /admin/reports` は既存（削除済みを含む）の slug を拒否していませんでした。そのため全ステップが skip されて旧成果物が新レポートとして残ったり、既存レポートの status（visibility・created_at）が黙って上書きされたりしていました。管理画面の ID 欄は既定で UUID なので、起きるのは ID を手で既存のものに書き換えたときです。
3. **サーバー再起動で processing のまま固まる**: analysis-core を監視するスレッドはサーバーと一緒に失われるため、再起動前に processing だったレポートは processing のまま残り、再実行も複製もできませんでした。
4. **成果物のアップロードが失敗しても ready になる**: 完了処理は ready にしてから各ファイルをアップロードしており、成否を見ていませんでした。一部が失敗するとリモートには ready の status だけが残り、揮発ディスクで再起動すると、結果ファイルの無い ready レポートになります。
5. **reuse 付き複製の直後に進捗ポーリングが止まる**: 元レポートの completed な `hierarchical_status.json` がそのままコピーされていました。analysis-core が running に書き換えるまでの約 1 秒の間に初回 poll が当たると completed を受け取り、ポーリングが止まったままになります。

## 変更
- `ConfigRepository.update_json`: `configs/<slug>.json` があれば生の dict を読み、更新するフィールドだけを差し替えます。config が結果ファイルに埋め込まれた旧レポートの経路は従来どおりです。
- `POST /admin/reports`: 既存の slug（status。削除済みを含む）、`configs/<slug>.json`、`outputs/<slug>/` のいずれかがあれば 409 を返します。duplicate と同じ判定（`slug_exists_anywhere`）を `include_input=False` で使います。`inputs/<slug>.csv` は作成画面のスプレッドシート・プラグイン取り込みが作成前に書き出し、`launch_report_generation` が `report.comments` から書き直すため、衝突として扱いません。admin の作成画面は 409 のとき ID の重複を伝えるメッセージを表示します。
- `ReportSyncService.sync_*` が成否を返すようにしました。完了処理は、成果物・入力・config の同期が全て成功したときだけ ready にし、失敗時は理由つきの error にしてから status を同期します。
- 起動時（lifespan）の `recover_interrupted_reports`: processing のエントリを走査します。ワークフローが completed で結果ファイルがあれば同期して ready に、それ以外は error（ログ抜粋つき）にします。
- reuse 付き複製: 複製先の status ファイルには `completed_jobs` / `previously_completed_jobs` だけを引き継ぎ、`status: pending` にします。running にすると、元レポートの `lock_until` がまだ有効な場合に analysis-core の判定にかかるため、pending にしました。

## テスト
- 各指摘に回帰テストを追加し、修正前のコードで失敗することを確認しました（取り込み済みの `inputs/<slug>.csv` だけがある slug で作成が 409 にならないことのテストを含みます）。
- api: `pytest -q tests --ignore=tests/manual` → 343 passed
- analysis-core: `pytest -q tests` → 330 passed
- admin: biome ci・tsc --noEmit は通過。jest の `app/create` は 86 passed
- ruff check / format --check: 変更ファイルはすべて通過

## 補足
- サーバープロセスだけが再起動して analysis-core のサブプロセスが動き続ける場合（開発用の `uvicorn --reload` でのコード変更、ストレージを共有する複数インスタンスなど）も、実行中のジョブは起動時の回収で error になり、その後完了しても error のまま残ります。本番相当の単一インスタンスの起動では発生しません（docstring に明記）。

🤖 Generated with [Claude Code](https://claude.com/claude-code)

**コメント:** なし

---

### [fix: 再実行判定と CLI オプション（--only / --dry-run / --reuse-from）の不整合を修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1033)

**作成者:** nishio  
**作成日:** 2026-10-18T18:21:08Z  
**変更:** +608 -48 (10ファイル)  
**マージ日:** 2026-10-19T03:49:54Z  
**内容:**

## 概要
analysis-core の再実行判定（decide_what_to_run）と、CLI の --only / --force / --dry-run / --reuse-from まわりの不整合を直します。あわせて hierarchical_status.json をアトミックに書き込むようにし、admin の進捗ポーリングが書き込み途中のファイルを読んで止まる問題も直します。

## 問題
1. input・question・intro・is_pubcom・enable_source_link・extraction.properties・hidden_properties・sampling_num を変えても再実行判定が検知しない。--reuse-from では複製元の hierarchical_result.json / report がそのまま使われる。
2. 上流のパラメータを変えた実行が下流で失敗した後に同じ config で再実行すると、全段が skip され、古い結果のまま completed になる（--only で上流の 1 段だけ再実行した後も同じ）。
3. kill や Ctrl+C で中断すると status ファイルに previous が入れ子で残り、次の実行が最も古い previous まで遡って判定するため、中断した実行が上書きした成果物を見落とす。
4. hierarchical_status.json を切り詰めてから書くので、get_current_step が空や書きかけのファイルを読むと status:error を返し、admin UI が実行中のレポートを「失敗」と表示してポーリングを止める。
5. --only に存在しないステップ名（workflow 側の ID や typo）や disabled のステップを渡すと、何も実行せずに exit 0 で終わる。--force と併用すると --only が無視される。
6. --dry-run / --validate-config / --validate-input でも --reuse-from の成果物コピーと status 書き込みが走る。そのため、以後に別の --reuse-from を指定しても警告なしで無視される。

影響は主に CLI を使う場合です（API のレポート生成・複製は reuse_from を使いません）。4 は API / admin でも起きます。

## 変更
- specs の dependencies に `global_params` を追加し、完了記録に `global_params`（トップレベル設定の値）を保存して比較する。global_params がない古い記録では比較しないので、既存のジョブがアップグレードで全段再実行になることはない。extraction に `properties`、aggregation に `sampling_num` / `hidden_properties` を追加する（古い記録にキーがなく、現在値が既定値と同じなら変更なし扱い）。
- --reuse-from では、自ジョブの config を埋め込む hierarchical_aggregation / hierarchical_visualization を複製しない。
- 依存ステップの完了時刻が自分より新しい場合は再実行する。
- status ファイルに previous を入れ子で書かず、履歴は previously_completed_jobs に残す。判定では最新の記録を優先する（旧形式の入れ子 previous も読める）。run_workflow は KeyboardInterrupt なども捕まえて status を error にしてから再送出する。
- status の書き込みを一時ファイル + os.replace にする。API の get_current_step は JSON の解析に失敗したら loading を返す。
- --only を specs のステップ名と照合し、実行されないステップを指定したらエラーにする。--force との併用では --only の範囲だけを実行する。
- persist_status=False（--dry-run / --validate-*）のときは複製も status 書き込みもせず、計画はメモリ上の seed で出す。既存の status と食い違う --reuse-from には警告を出す。

## テスト
- 新規: `packages/analysis-core/tests/test_rerun_decisions.py`（23 件）、`apps/api/tests/routers/test_get_current_step.py` に 2 件
- 更新: `test_cli.py`（dry-run で宛先に何も残らないことを確認）、`test_orchestration.py`（visualization を複製しない）
- analysis-core `pytest -q tests`: 353 passed。api `pytest -q tests --ignore=tests/manual`: 335 passed
- origin/main の実装に対して新しいテストを実行すると、互換性テストを除いて失敗することを確認した

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Bug Fixes**
  * Status polling continues to show a run as loading when its status file is empty or incomplete, instead of returning an error.
  * Interrupted runs now record an error status and retain the history of previously completed steps.
* **Improvements**
  * Rerun decisions account for relevant setting changes and newer dependency outputs, while reusing eligible prior results.
  * Reuse checks no longer reuse aggregation or visualization outputs, and dry runs do not write files to the destination.
  * The `--force` help text clarifies that `--only` limits reruns to the selected step; invalid or skipped steps are rejected.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix(analysis-core): 集計結果のデータ欠落を修正（comment-id の型、同じ文面の意見の帰属、古い意見分類、分析対象件数）](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1032)

**作成者:** nishio  
**作成日:** 2026-10-18T18:21:04Z  
**変更:** +244 -13 (8ファイル)  
**マージ日:** 2026-10-19T03:43:50Z  
**内容:**

## 概要
hierarchical_aggregation 周辺で、属性・URL・ラベル・件数が黙って欠けたり誤ったりする問題を 4 件直します。

## 問題
1. **comment-id の型推論**: relations.csv を型推論で読んでいたため、`001` のような先頭ゼロ付き ID が数値 `1` に変わっていました。入力 CSV は文字列で読むので照合できず、`arguments[].attributes` / `url` / `comment_id` が黙って失われていました。
2. **同じ文面の意見の帰属**: extraction が抽出意見の文面だけで重複をまとめていました。そのため、別々の回答から同じ文面の意見が出ると arg-id が 1 つになり、集計では最後の回答の属性・URL しか残りませんでした。属性フィルタをかけると、他の回答者の分が表示から漏れていました。
3. **古い意見分類のマージ**: `opinion_classifications.csv` があれば無条件にマージしていました。そのため、無効化した後や分類が失敗した後でも、古いラベルが結果に入っていました。また optional ステップなので、`enabled: true` で要求した分類が失敗しても exit 0 で完了していました。
4. **分析対象件数**: custom intro の「分析対象となったデータの件数」は、空コメントを除く前の行数をもとにしていたため、実際の処理件数より多く表示されていました。

## 変更
- `hierarchical_aggregation`: relations.csv を読むときに `comment-id` を `Utf8` に固定しました。
- `extraction`: 重複判定のキーを `(comment-id, 文面)` にしました。同じ文面でも回答ごとに別の arg-id になり、意見 1 件は常に 1 つの回答に対応します。
  - **挙動の変化**: 別の回答から完全に同じ文面の意見が出た場合、これまでは 1 件にまとめていましたが、今後は回答ごとに 1 件ずつ数えます。そのため、args の件数とクラスタの件数が増えることがあります。
- `hierarchical_aggregation`: `opinion_classification.enabled` が真のときだけ分類ラベルをマージします。
- `opinion_classification`: 開始時に前回の CSV / summary を削除します。
- workflow: `opinion_classification` を optional から外しました。無効時は condition でスキップされます。有効時に分類が失敗すると、パイプラインが失敗します。
- `create_custom_intro`: extraction と同じ `filter_empty_comments` をかけてから limit と比べます。
- docs: `plugin-output-data-structures.md`（relations.csv の説明）と `opinion-classification.md`（マージ条件と失敗時の扱い）を更新しました。

## テスト
- 新規: `packages/analysis-core/tests/test_aggregation_data_integrity.py`（6 件）、`test_opinion_classification.py::TestStep::test_failure_removes_previous_run_output`
- 既存の `test_workflow_and_registry_include_step` の assertion を `optional is False` に変えました。
- 新規テストが修正前のコードで失敗することを確認しました。
- analysis-core `pytest -q tests`: 337 passed
- api `pytest -q tests --ignore=tests/manual`: 333 passed
- 変更ファイルに `ruff check` / `ruff format --check` を実行し、問題なし

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Identical opinions from different comments now remain linked to their respective comments.
  * Comment IDs with leading zeros are preserved, and opinion labels are applied only when classification is enabled.
  * Failed classification runs no longer leave previous results behind, and enabled classification failures stop the pipeline.
  * Custom-intro comment counts now account for filtered empty comments and extraction limits.

* **Documentation**
  * Clarified how opinion labels, comment-to-opinion relationships, and classification failures are handled.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix(analysis-core): 一部ステップのみ再実行してもトークン使用量を 0 に戻さない](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1031)

**作成者:** nishio  
**作成日:** 2026-10-18T13:03:50Z  
**変更:** +300 -13 (3ファイル)  
**マージ日:** 2026-10-19T03:43:39Z  
**内容:**

## 概要
管理画面でラベル編集・設定編集を行うと、レポートのトークン数と推定コストが 0 / $0 に戻ってしまう問題を修正します。

## 原因
編集後、API は `execute_aggregation` で `--only hierarchical_aggregation` を実行します。analysis-core は実行開始時に `total_token_usage` / `token_usage_input` / `token_usage_output` を 0 で初期化し、終了時に「今回実行したステップの合計」（集約のみなので 0）で上書きしていました。API の `_monitor_process` はこの値をそのまま `update_token_usage()` に渡すため、report_status の値が 0 になっていました。

## 変更内容
- `carried_over_token_usage()` を追加。前回 status の合計から、今回再実行するステップの前回分を差し引いた値を引き継ぐ
  - スキップされたステップ（成果物が残るステップ）のトークンは、レポートの費用として残す
  - 再実行したステップは新しいトークン数で置き換える（二重に数えない）
  - `--force` など全ステップを再実行する場合は、従来どおり 0 から数える
- `initialization()`（CLI / 旧 run() 経路）と `run_workflow()` の開始時、および終了時の合計に引き継ぎ値を反映
- `completed_jobs` の各 job に `token_input` / `token_output` を記録。内訳のない旧 status は、前回合計の入出力比で按分する
- API 側は status の値を転記するだけなので変更なし

## 設計判断（レビュー時に見てほしい点）
「合計」は **現在の成果物を作ったステップのトークン数**（＝レポート自体のコスト）と定義しました。再実行を含む累積支出ではありません。累積支出を表示したい場合は、ヘルパーで再実行ステップを差し引かないようにする 1 行の変更で対応できます。
すでに 0 と表示されている既存レポートは status に 0 が保存されているため、この修正では復元されません（今後のリセットを防ぐのみ）。

## テスト
- `tests/test_orchestration.py` に `TestTokenUsageCarryOver` を追加（集約のみの再実行で合計を維持、再実行ステップの置き換え、`--only` の初期化時に 0 を書かない、ヘルパー単体）
- 修正前は追加テスト 6 件が失敗、修正後は analysis-core 全 336 件が pass

🤖 Generated with [Claude Code](https://claude.com/claude-code)


**コメント:** なし

---

### [fix(analysis-core): hierarchical_aggregation の失敗を握りつぶさず伝播させる](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1030)

**作成者:** nishio  
**作成日:** 2026-10-18T13:02:34Z  
**変更:** +102 -1 (2ファイル)  
**マージ日:** 2026-10-19T03:43:29Z  
**内容:**

## 概要
`hierarchical_aggregation` は関数全体を `try/except Exception` で包み、失敗時に `False` を返して例外を握りつぶしていました。そのため集約に失敗してもパイプラインが成功扱いになっていました。この問題を修正します。

## 問題
- plugin は戻り値の bool を `metadata["success"]` に入れるだけで、workflow engine は例外が出ない限り step を成功扱いする
- その結果、`hierarchical_result.json` が欠けていたり古いままでも、CLI は exit 0 で終わり、API はレポートを `ready` にしていた（例: hidden_properties で指定したカラムが無い、translations / overview が無い）
- JSON 書き出し後の `create_custom_intro` / `add_original_comments` が失敗した場合は、pubcom 用 CSV が黙って欠落していた

## 変更
- `except` 節で `return False` をやめて re-raise する（diff を小さくするため try ブロックとインデントは維持）
- 例外は engine / legacy orchestrator の既存経路で処理される。run は失敗になり、`hierarchical_status.json` は `status: "error"`、CLI は exit 1 になる（extraction / labelling の失敗伝播と同じ規約）
- 成功時の `True` 返却は互換のため維持

## 影響（レビュー時に見てほしい点）
管理画面のラベル編集・設定編集で走る aggregation-only 実行が失敗した場合、これまでは「成功扱い・古い JSON のまま ready」でしたが、今後は error として表に出ます。失敗を正しく検知するための変更です。一方で、編集後の集計失敗で READY だったレポートの status が落ちる挙動について、別途扱いを検討する余地があります（aggregation-only の失敗を report status とは別に記録する、など）。

## テスト
- `tests/test_aggregation_failures.py` を追加: 成功時は従来どおり / 入力欠損・hidden_properties の欠損カラム・JSON 書き出し後の失敗が伝播する / workflow で run が失敗扱いになる
- 修正前は 4 件が失敗（workflow は `success=True` を返していた）、修正後は全件 pass。analysis-core 全体 335 passed、ruff OK

🤖 Generated with [Claude Code](https://claude.com/claude-code)



**コメント:** なし

---

### [fix(analysis-core): cluster_nums を正規化してから最大クラスタ数を決める](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1029)

**作成者:** nishio  
**作成日:** 2026-10-18T13:02:30Z  
**変更:** +121 -2 (2ファイル)  
**マージ日:** 2026-10-19T03:43:18Z  
**内容:**

## 概要
`hierarchical_clustering_embeddings` は `cluster_nums.sort()` より前に `cluster_nums[-1]` を取り、初期 KMeans のクラスタ数として使っていました。そのため CLI config で `cluster_nums = [50, 5]` のように降順で指定すると KMeans(5) が実行され、50 の階層が警告なしに失われていました。また in-place sort が呼び出し元の config を書き換えるため、params diff や再実行判定に影響しうる状態でした。

## 変更内容
- `normalize_cluster_nums()` を追加し、cluster_nums のコピーを一度だけ正規化する
  - 正の整数以外（0・負数・float・文字列・bool・空リスト）は `ValueError`
  - 意見件数を超えるクラスタ数は件数に clamp して warning を出す（`calculate_recommended_cluster_nums` や LLM grouping の件数上限と同じ扱い）。従来は抽出・埋め込みの後で KMeans が落ちていた
  - 昇順ソートと重複除去
- 初期 KMeans のクラスタ数は、正規化後の最大値から取る
- `hierarchical_clustering` では UMAP の前に検証し、不正値は早めにエラーにする。config 自体は書き換えない

## テスト
- `tests/test_hierarchical_clustering.py` に回帰テストを追加（fake KMeans で n_clusters を記録）。修正前は降順入力・config 非破壊・件数超過の 3 件が失敗
- analysis-core 全体 342 passed、ruff check / format --check OK

## 対象外（別 PR 候補）
- API schema（`apps/api/src/schemas/admin_report.py`）での `cluster` の昇順・正の整数チェックと `workers >= 1` の validation

🤖 Generated with [Claude Code](https://claude.com/claude-code)


**コメント:** なし

---

### [fix(api): async エンドポイント内の同期 I/O を threadpool に逃がしイベントループのブロックを防ぐ](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1028)

**作成者:** nishio  
**作成日:** 2026-10-18T13:02:27Z  
**変更:** +127 -7 (5ファイル)  
**マージ日:** 2026-10-19T03:43:08Z  
**内容:**

## 概要
FastAPI の `async def` エンドポイントが同期 I/O を直接呼んでいました。その間はイベントループ全体が止まり、他のすべてのリクエスト（公開ビューアの SSR fetch を含む）が待たされます。この問題を修正します。

## 変更内容
- `/admin/environment/verify`: `request_to_chat_ai`（30 秒 timeout + tenacity リトライ）を `run_in_threadpool` で実行
- `/admin/spreadsheet/import`: `process_spreadsheet_url` を `run_in_threadpool` で実行。あわせて `requests.get` に timeout（接続 10 秒 / 読み取り 60 秒）を追加。従来は timeout 未指定で、無期限に待つことがあった。timeout 時は既存のエラーハンドリングで 400 を返す
- Next.js revalidate の同期 `requests.post`（最大 3 秒）を含む `update_report_visibility_state` / `update_report_config` / `invalidate_report_cache` を、visibility・config・cluster-label・visualization-config の各 async エンドポイントから `run_in_threadpool` 経由で呼ぶ

エンドポイントのシグネチャ（`async def`）と既存テストの patch 対象は変えず、呼び出し箇所だけを最小限変更しています。

## テスト
- 対象関数がイベントループ外で呼ばれることを検証するテストを追加（verify / visibility / spreadsheet import）。修正前のコードでは失敗することを確認済み
- `requests.get` に timeout が渡ること、Timeout が `ValueError` に変換されることを検証
- `pytest tests`: 338 passed / `ruff check`・`ruff format --check` 通過

🤖 Generated with [Claude Code](https://claude.com/claude-code)


**コメント:** なし

---

### [fix(api): プラグイン取込とスプレッドシート取得のファイル名を検証しパストラバーサルを防止](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1027)

**作成者:** nishio  
**作成日:** 2026-10-18T13:02:23Z  
**変更:** +112 -2 (4ファイル)  
**マージ日:** 2026-10-19T03:42:56Z  
**内容:**

## 概要
`POST /admin/plugins/{plugin_id}/import` の `fileName` と `GET /admin/spreadsheet/data/{file_name}` の `file_name` を検証しないまま、`INPUT_DIR / f"{name}.csv"` のパス組み立てに使っていました。そのためパストラバーサルが可能でした（#1020 と同種）。

## 問題
- プラグイン取込: `fileName` に `../outputs/<slug>/args` のような値を渡すと、`plugin.save_to_csv` が `INPUT_DIR` の外に CSV を書き込める（既存レポートの中間ファイル上書きなど）
- スプレッドシートデータ取得: `file_name` が検証されないまま読み込みパスに使われる（`/` はルーティングで弾かれるが、`%2E%2E`・改行・バックスラッシュなどは通っていた）
- `SLUG_PATTERN` は `match` と末尾 `$` の組み合わせなので、`"name\n"` のような末尾改行付きの値が通っていた

## 変更内容
- `routers/plugins.py`: `import_data` に `validate_slug(request.fileName)` を追加。広い except に握りつぶされないよう、try の外（`fetch_data` の前）で検証して 400 を返す
- `routers/spreadsheet.py`: `get_spreadsheet_data` に `validate_slug(file_name)` を追加
- `utils/slug_utils.py`: `match` を `fullmatch` に変更し、末尾改行を拒否
- `validate_slug` を採用した理由: 取込ファイル名は後続の `create_report` で `report.input` として同じ `validate_slug` で検証されるため（既存の英大文字・アンダースコアを含む名前も壊さない）

## テスト
- `tests/routers/test_input_file_name_validation.py` を追加。修正前は 12 failed / 3 passed、修正後は 15 passed
- api テスト全体: 348 passed、`ruff check` / `ruff format --check` 通過

🤖 Generated with [Claude Code](https://claude.com/claude-code)


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Invalid file names are now rejected before plugin imports or spreadsheet data are accessed, preventing malformed names from reaching file operations.
  * File-name validation now checks the entire name, including trailing characters and newlines.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix(analysis-core): ローカル埋め込み失敗時に別モデルへ暗黙 fallback せず fail-fast する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1022)

**作成者:** nishio  
**作成日:** 2026-10-16T11:37:19Z  
**変更:** +74 -2 (2ファイル)  
**マージ日:** 2026-10-16T12:26:40Z  
**内容:**

# 変更の概要
- `request_to_local_llm_embed`（provider=local の OpenAI 互換ローカルLLM埋め込み）が、呼び出し失敗時に**別モデルへ暗黙 fallback していた**のをやめ、原因の分かる `RuntimeError` で **fail-fast** します。

# スクリーンショット
- UI 変更なし（analysis-core 内部ロジックの修正）。

# 変更の背景
- 従来は `client.embeddings.create(...)` が失敗すると、`except Exception:` で `request_to_local_embed`（sentence-transformers の mpnet, 768 次元）へ**暗黙に切り替え**ていました。埋め込みは 1000 件バッチ単位で呼ばれるため、この fallback は**バッチ単位で埋め込み次元を変え**ます。
- その結果:
  - **一部バッチだけ失敗**（エンドポイントが断続的に落ちる）→ 次元が混在し、`embedding.pkl`（`list[dict]` 保存）は書けても、下流 `steps/hierarchical_clustering.py` の `np.asarray([...])` が **pinned `numpy>=1.26` で `ValueError: inhomogeneous shape`** を投げてクラッシュします（実測 numpy 2.5.4 で確認）。落ちる場所が真因（埋め込み途中の fallback）から遠く、原因が追いにくい失敗になります。
  - **全バッチ失敗** → 次元は揃うのでクラッシュしませんが、**設定と異なるモデル（mpnet）で silent に完走**し、意図と違うベクトル空間の成果物が出ます（wrong model）。
- 問題の本質は「黙って別モデルに swap する」ことなので、**fail-fast**（失敗したモデル名・アドレス・元エラーを含む `RuntimeError`）に変更します。サーバー内蔵の埋め込みモデル（mpnet）を使いたい場合は、従来どおり `is_embedded_at_local` を明示的に有効化する経路があります。
- （2026-10-16 のソースレビュー backlog「D」。当初は data-loss と分類していましたが、実挙動は上記のとおり「部分失敗＝クラッシュ / 全失敗＝silent wrong-model」で、correctness/robustness の問題です。）

# 関連Issue
- （レビューで発見。対応する既存 Issue なし）

# 動作確認の結果
- `request_to_local_llm_embed` に対し回帰テスト（新規 `tests/test_local_embed_failfast.py`）を追加：
  - 正常時は OpenAI 互換エンドポイントの埋め込みをそのまま返す。
  - 失敗時は `request_to_local_embed`（mpnet への swap）を**呼ばず**、失敗モデル名と元エラーを含む `RuntimeError` を送出する。
- **修正前のコードでは失敗系テストが fail**（旧挙動は "Falling back to local embedding" で swap）することを確認。修正後は pass。
- `test_llm.py` ＋新テストで全 pass（隔離 venv・PYTHONPATH で独立再実行）、ruff / format クリーン。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。
- [ ] UI（`apps/public-viewer` / `apps/admin`）の変更で利用方法・表示が変わる場合、`docs/user-guide/how-to-use.md` を更新したか（→ 内部ロジックのみ。更新不要）

🤖 Generated with [Claude Code](https://claude.com/claude-code)


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Local embedding requests now report an error when the configured embedding API fails, rather than silently switching to a different embedding method.
  * The error message includes the model, API address, original error, and configuration guidance to help diagnose the issue.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix(api): report_status.json の読み書きを lock + atomic 保存で保護](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1021)

**作成者:** nishio  
**作成日:** 2026-10-16T09:14:25Z  
**変更:** +142 -21 (2ファイル)  
**マージ日:** 2026-10-16T12:26:35Z  
**内容:**

# 変更の概要
- `report_status.json` の読み書きを `_lock` で保護し、書き込みを一時ファイル + `os.replace` で atomic 化します。バックグラウンドの status 更新と `GET /admin/reports` の競合で、一瞬 0 件表示や取りこぼしが起こる不具合を防ぎます。

# スクリーンショット
- UI 変更なし（API の永続化処理の修正）。

# 変更の背景
- `load_status` と `load_status_as_reports` は、`STATE_FILE` を読んでモジュールグローバル `_report_status` を再代入する処理を **`_lock` を取らずに**行っていました。一方で mutator 群（`set_status` / `update_token_usage` / `save_status` 等）は `_lock` を保持し、`save_status` は `open(STATE_FILE, "w")`（truncate → 書き直し）で**非 atomic** に書いていました。
- そのため、writer が `save_status` で truncate 中の瞬間に `GET /admin/reports`（→ `load_status_as_reports`）が走ると、半分書かれたファイルを読んで `json.JSONDecodeError` → `_report_status = {}` → **一覧が一瞬 0 件**になる、あるいは writer と read-modify のレースが起こりえます。
- 修正:
  1. `load_status` / `load_status_as_reports` の「読み込み + グローバル再代入（+ 一覧構築）」を `with _lock:` で囲む（`_lock` は RLock なので再入可能で安全）。
  2. `save_status` を atomic 化: 同一ディレクトリの一時ファイルに書いてから `os.replace` で差し替え（POSIX で atomic）。失敗時は一時ファイルを掃除して既存ファイルを温存。
- 留意点: `os.replace` はプロセス内の truncate レースを解消しますが、ハード電源断に対する durability（fsync）までは扱いません（別論点）。

# 関連Issue
- （レビューで発見。対応する既存 Issue なし）

# 動作確認の結果
- 事前に有効な `STATE_FILE` を用意し、書き込みを途中で失敗させた場合に**元ファイルが truncate されず温存される**こと（旧実装の `open("w")` では壊れる）、および `save_status` → `load_status` の round-trip を検証する回帰テストを `test_report_status.py` に追加。読み込みが `_lock` を取ることも確認。
- 修正前は atomicity テストが fail することを確認。`test_report_status.py` 全 14 件 pass、ruff / format クリーン。隔離 venv で独立に再実行して確認。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。
- [ ] UI（`apps/public-viewer` / `apps/admin`）の変更で利用方法・表示が変わる場合、`docs/user-guide/how-to-use.md` を更新したか（→ 内部の永続化処理のみ。更新不要）

🤖 Generated with [Claude Code](https://claude.com/claude-code)


**コメント:** なし

---

### [fix(api): create_report で report.input を slug 検証しパストラバーサルを防ぐ](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1020)

**作成者:** nishio  
**作成日:** 2026-10-16T09:14:23Z  
**変更:** +54 -0 (2ファイル)  
**マージ日:** 2026-10-16T12:26:30Z  
**内容:**

# 変更の概要
- `create_report`（POST /admin/reports）で `report.input` を `validate_slug` で検証し、パストラバーサルを防ぎます。他の admin エンドポイントと一貫させる最小修正です。

# スクリーンショット
- UI 変更なし（API の入力検証の追加）。

# 変更の背景
- 他の admin エンドポイント（duplicate / delete / visibility / config / cluster-label / download 等）はすべて `validate_slug(...)`（`^[A-Za-z0-9_-]+$` 以外なら HTTPException(400)）を通しますが、**作成経路だけ `report.input` を検証していません**でした。`ReportInput.input` にも field_validator はありません。
- `report.input` はその後 `report_launcher` でファイルパス構成に直接使われます（`CONFIG_DIR/f"{input}.json"`、`INPUT_DIR/f"{input}.csv"`、`REPORT_DIR/slug`、いずれも `parents=True` で mkdir）。そのため `"../../.."` を含む値は管理下のデータディレクトリの外にファイルを作成・上書きしうる、かつ他エンドポイントが弾く値がここだけ素通りして不整合なレポートエントリを生みます。admin API キー保持が前提の認証済み経路ですが、他と一貫した防御を入れます。
- 配置は `try` の**外**（`launch_report_generation` の前）にしています。`create_report` の `try` は広い `except Exception` を持ち、`try` 内に置くと `validate_slug` の `HTTPException(400)` がそれに握りつぶされて 500 になるためです（他の slug 検証は duplicate のように `except HTTPException: raise` を持つ経路に限り try 内に置かれています）。

# 関連Issue
- （レビューで発見。対応する既存 Issue なし）

# 動作確認の結果
- POST /admin/reports に `input="../../etc/pwn"`（他は有効な body）を送ると **400（Invalid slug format）** を返し `launch_report_generation` が呼ばれないこと、有効な input では slug 検証を通過して launch に到達することを検証する回帰テストを `test_admin_report.py` に追加（launch は mock）。
  - 補足: 成功時はハンドラが自前の `ORJSONResponse` を返すため実ステータスは 200（ルートの `status_code=202` が上書きされる既存挙動）。本 PR はこの 202→200 の不整合には手を入れていません。
- 修正前はトラバーサルのテストが fail（400 にならない）することを確認。`test_admin_report.py` 全 25 件 pass、ruff / format クリーン。隔離 venv で独立に再実行して確認。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。
- [ ] UI（`apps/public-viewer` / `apps/admin`）の変更で利用方法・表示が変わる場合、`docs/user-guide/how-to-use.md` を更新したか（→ API 内部の検証追加のみ。更新不要）

🤖 Generated with [Claude Code](https://claude.com/claude-code)


**コメント:** なし

---

### [fix(analysis-core): from_dict 経路で hierarchical の cluster_nums 既定を None にそろえる](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1019)

**作成者:** nishio  
**作成日:** 2026-10-16T09:14:20Z  
**変更:** +68 -1 (3ファイル)  
**マージ日:** 2026-10-16T12:26:25Z  
**内容:**

# 変更の概要
- dict 経路（`from_dict` → `normalize_config`）でも `hierarchical_clustering.cluster_nums` の既定を `None` にそろえ、`cluster_nums` 未指定の hierarchical 実行がクラッシュしないようにします。

# スクリーンショット
- UI 変更なし（analysis-core の config 正規化の修正）。

# 変更の背景
- デフォルトの hierarchical workflow（`workflows/hierarchical_default.py`）の clustering ステップは `${config.hierarchical_clustering.cluster_nums}` を参照します。engine の変数解決（`WorkflowEngine._resolve_step_config`）は、**親 dict が存在するのに参照先の入れ子キーが無い**場合に `WorkflowExecutionError` を送出します。
- ファイル経路（`from_config` → `initialization`）は `hierarchical_specs.json` の `"cluster_nums": null` から `None` を埋める（＝「自動計算」の意味）一方、dict 経路（`from_dict` → `normalize_config`）は `cluster_nums` を未設定のままにしていました。そのため `from_dict` + `run_default()` を hierarchical モードで `cluster_nums` 省略実行すると、テンプレート解決で例外になり `PipelineResult(success=False, ...)` に落ちます。
- 事前に次を確認済み: (1) `steps/hierarchical_clustering.py` は `cluster_nums` の falsy（None/未指定）を `calculate_recommended_cluster_nums` による自動計算として扱う、(2) ファイル経路が None を入れている、(3) `from_dict` が `normalize_config` を通る。したがって**最小で一貫する修正は dict 経路でも None を既定にすること**です。

# 関連Issue
- （レビューで発見。対応する既存 Issue なし）

# 動作確認の結果
- `normalize_config` が `hierarchical_clustering.cluster_nums = None` を出すこと、および engine（`_resolve_step_config`、`run` が使うのと同じ解決）が `create_hierarchical_workflow()` の clustering テンプレートを**例外を出さずに** `{"cluster_nums": None}` に解決することを検証する回帰テスト（`tests/test_from_dict_cluster_nums.py`）を追加。
- 既存の `test_fills_clustering_defaults`（`cluster_nums` 不在を pin していた契約）を、`cluster_nums is None` を pin する正しい契約へ更新。
- 修正前は engine 解決テストが `WorkflowExecutionError` で fail することを確認。`test_compat.py` + 新テストで 15 件 pass、ruff / format クリーン。隔離 venv で独立に再実行して確認。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。
- [ ] UI（`apps/public-viewer` / `apps/admin`）の変更で利用方法・表示が変わる場合、`docs/user-guide/how-to-use.md` を更新したか（→ 内部ロジックのみ。更新不要）

🤖 Generated with [Claude Code](https://claude.com/claude-code)


**コメント:** なし

---

### [fix(analysis-core): Azure 推論モデルデプロイに temperature を送らない](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1018)

**作成者:** nishio  
**作成日:** 2026-10-16T09:14:18Z  
**変更:** +122 -10 (2ファイル)  
**マージ日:** 2026-10-16T12:26:20Z  
**内容:**

# 変更の概要
- Azure チャット補完（`request_to_azure_chatcompletion`）が、推論モデル（o 系 / GPT-5,6 系）のデプロイに対しても `temperature=0` を送っていた不具合を修正します。OpenAI 経路と同様に、推論モデルでは temperature を送りません。

# スクリーンショット
- UI 変更なし（analysis-core 内部ロジックの修正）。

# 変更の背景
- OpenAI 経路（`_build_openai_chat_payload`）は、GPT-5/6・o 系の推論モデルが temperature 指定を拒否するため、`if not _is_openai_reasoning_model(model): payload["temperature"] = 0` で temperature を省いています（既存のガード）。
- しかし `request_to_azure_chatcompletion` には同じガードが無く、`beta.chat.completions.parse` 経路と通常の `create` 経路の両方で `temperature=0` を**ハードコード**していました。そのため o3 / gpt-5 等の Azure デプロイを使うと Azure が 400（Unsupported value: 'temperature'）を返し、該当のパイプラインステップが失敗します。
- 判定キーは Azure の `deployment` 名です。Azure のデプロイは通常モデル名に合わせて命名される前提で、推論モデル名に見える場合のみ temperature を外します（それ以外のデプロイでは挙動は従来どおり）。この方針はレビュー時の finding に沿っています。

# 関連Issue
- （レビューで発見。対応する既存 Issue なし）

# 動作確認の結果
- 推論デプロイ（`o3` / `gpt-5` / `o4-mini` / `GPT-6-Astra`）では Azure クライアントに渡る kwargs に `temperature` が**含まれない**こと、通常デプロイ（`gpt-4o`）では `temperature=0` が渡ることを、create 経路・parse 経路の両方について検証する回帰テストを `test_llm.py` に追加。`seed`/`n` 等の他パラメータは維持されることも確認。
- 修正前は推論デプロイのテストが fail（temperature が渡る）することを確認。`test_llm.py` 全件 pass、ruff / format クリーン。隔離 venv で独立に再実行して確認。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。
- [ ] UI（`apps/public-viewer` / `apps/admin`）の変更で利用方法・表示が変わる場合、`docs/user-guide/how-to-use.md` を更新したか（→ 内部ロジックのみ。更新不要）

🤖 Generated with [Claude Code](https://claude.com/claude-code)


**コメント:** なし

---

### [fix(api,admin): 埋め込みモデル機能(#450)の後始末 — 複製時のモデル引き継ぎ + 作成時のバリデーション接続](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1017)

**作成者:** nishio  
**作成日:** 2026-10-16T09:14:15Z  
**変更:** +93 -0 (5ファイル)  
**マージ日:** 2026-10-16T12:26:14Z  
**内容:**

# 変更の概要
#450（埋め込みモデルをチャットと独立に選択）の後続不具合 2 件をまとめて修正します。
- **(api) 複製時にソースの埋め込みモデルが落ちる**: `report_duplicate.py` の embedded-config フォールバック経路で `embedding.model` を引き継ぐ。
- **(admin) 埋め込みモデルの検証エラーが送信をブロックしない**: `embeddingModelError` を `validateFormValues` に接続する。

# スクリーンショット
- UI 表示自体の変更はなし（admin は「必ず失敗する組合せ」を送信前に止めるバリデーション追加のみ）。

# 変更の背景
**(api) 複製時の埋め込みモデル欠落**
`_build_analysis_core_config_from_embedded_config` は `ReportConfig(**embedded_config).model_dump()` で config を再生成しますが、`ReportConfig` に `embedding` フィールドが無く extra は ignore されるため、ソース config の `embedding` セクションが落ちます（`enable_source_link` だけは同じ理由で手動再付与されていた）。その結果、config ファイルが無くこのフォールバック経路で複製し、かつ `embedding_model` を override しない場合、複製先が既定モデル（text-embedding-3-small）で embeddings を再生成し、**ソースと異なるベクトル空間**（＝クラスタリング・散布図座標が別物）になります。`model` のみ再付与し、normalize 済みの `source_code` サブフィールドは再導入しません（analysis-core の step 別オプション検証で弾かれるため）。

**(admin) 埋め込みバリデーションの非接続**
`useAISettings` は `embeddingModelError`（例: OpenRouter では選択可能な埋め込みモデルが無い等）を算出しますが、`page.tsx` の `validateFormValues` には `modelError` しか渡しておらず、**必ず失敗する組合せ（OpenRouter × 非ローカル埋め込み）がそのまま送信**できていました。レポートは起動し、抽出ステップ（＝LLM コスト発生済み）の後に埋め込みステップで失敗します。`modelError` と同じ扱いで検証ゲートに接続します（有効な組合せでは空文字なので正常系はブロックしません）。

# 関連Issue
- Refs #450

# 動作確認の結果
- **(api)** `_build_analysis_core_config_from_embedded_config` に `embedding: {model, source_code}` を渡し、戻り config の `embedding == {"model": "text-embedding-3-large"}`（model 保持・source_code 非再導入）を検証する回帰テストを追加。修正前は `KeyError: 'embedding'` で fail することを確認。`test_report_duplicate.py` 全 2 件 pass。
- **(admin)** `embeddingModelError` 設定時に `{isValid:false, errorMessage}`、空の時はそれを理由にブロックしない、の 2 ケースを `validation.test.ts` に追加。`validation.test.ts` 全 18 件 pass、`biome check` クリーン。
- いずれも隔離した uv venv / worktree で独立に再実行して確認。ruff / biome もクリーン。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。
- [ ] UI（`apps/public-viewer` / `apps/admin`）の変更で利用方法・表示が変わる場合、`docs/user-guide/how-to-use.md` を更新したか（→ 送信前バリデーションの追加のみで表示・操作手順は不変。更新不要）

🤖 Generated with [Claude Code](https://claude.com/claude-code)


**コメント:** なし

---

### [fix(analysis-core): 指定カテゴリ変更時に llm_grouping を確実に再実行する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1016)

**作成者:** nishio  
**作成日:** 2026-10-16T08:38:17Z  
**変更:** +19 -1 (2ファイル)  
**マージ日:** 2026-10-16T12:26:07Z  
**内容:**

# 変更の概要
- #996 で追加した指定カテゴリ分類（supervised）の `predefined_groups` / `other_group_label` を、`llm_grouping` ステップの再実行判定（rerun invalidation）対象に加えます。
- これにより、分類カテゴリ集合や「その他」ラベルを変えた再実行が確実に反映されるようになります。

# スクリーンショット
- UI 変更はありません（`analysis-core` の spec 定義とテストのみ）。

# 変更の背景
- `predefined_groups`（分類する枠の集合）と `other_group_label`（catch-all「その他」のラベル）は出力を決定する要因ですが、`llm_grouping_specs.json` の `dependencies.params` に登録されていませんでした。
- `decide_what_to_run()` / `different_params()`（`core/orchestration.py`）は `dependencies.params`（+ use_llm の `prompt`/`model`）に挙がったキーしか前回実行と比較しません。そのため、**同じ `output_dir` への増分再実行（`-f` なし）** では、カテゴリ集合を変更しても「nothing changed」と判定されて `llm_grouping` がスキップされ、`hierarchical_clusters.csv` / `hierarchical_merge_labels.csv` が**古いカテゴリ・古い割当のまま**残ります（新カテゴリは生成されず、該当意見は「その他」に寄ったまま）。`other_group_label` のリネームも同様に反映されません。
- これは `discovery_prompt` / `assignment_prompt` に対して既存のガードテストが守っている契約（出力決定オプションは `dependencies.params` に入れる）が、#996 の supervised オプションに対して適用漏れしていたものです。

# 関連Issue
- Refs #996（#996 で追加した指定カテゴリ分類の後続不具合）

# 動作確認の結果
- `dependencies.params` に `predefined_groups` / `other_group_label` を追加。`different_params` は `!=` による等価比較のため、list/dict 値（カテゴリ定義の配列）でも差分検知が機能します。「前回未追跡 → 今回設定あり」も差分として検知され、安全側（再実行する方向）に倒れます。
- 既存の prompt ガードテスト `test_llm_grouping_specs_treat_prompt_changes_as_dependencies` に倣い、supervised オプションが `dependencies.params` に含まれることを検証する回帰テスト `test_llm_grouping_specs_treat_supervised_options_as_dependencies` を追加。
- **回帰検証**: 修正前の spec に対して追加テストが fail（AssertionError）し、修正後は pass することを確認。
- `packages/analysis-core/tests/test_llm_grouping.py` 全 12 件 pass（`[clustering]` extra 導入環境）。変更ファイルに対し `ruff check` / `ruff format` も pass。JSON の妥当性も確認済み。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。
- [ ] UI（`apps/public-viewer` / `apps/admin`）の変更で利用方法・表示が変わる場合、`docs/user-guide/how-to-use.md` を更新したか（→ 本修正は内部ロジックのみで UI 変更なし。更新不要）

🤖 Generated with [Claude Code](https://claude.com/claude-code)


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * The grouping workflow now accounts for predefined groups and the label used for other items when handling its settings, helping ensure these options are recognized consistently.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix(analysis-core): Gemini 埋め込みレスポンスの .embeddings(複数) 形式を解釈する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1015)

**作成者:** nishio  
**作成日:** 2026-10-16T08:34:12Z  
**変更:** +33 -1 (2ファイル)  
**マージ日:** 2026-10-16T12:26:01Z  
**内容:**

# 変更の概要
- Gemini provider の埋め込み呼び出し（`request_to_gemini_embed`）が実質まったく機能していなかった不具合を修正します。
- `extract_embedding_values` に、新しい統合 `google-genai` SDK (>=1.0) の `EmbedContentResponse`（`.embeddings` 複数形）を解釈するブランチを追加しました。

# スクリーンショット
- UI 変更はありません（`analysis-core` / API 内部ロジックの修正のみ）。

# 変更の背景
- #450 でチャットモデルとは独立に埋め込みモデル（Gemini の `gemini-embedding-001` など）を選択できるようにしましたが、`services/llm.py` の `request_to_gemini_embed` は新しい統合 SDK の `client.models.embed_content()` を使用しています。
- この SDK の戻り値 `EmbedContentResponse` は `.embedding`（単数）ではなく **`.embeddings`（複数・各 `ContentEmbedding.values`）** を持ちます。しかし `extract_embedding_values` は「単数 `.embedding` 属性を持つ object」か「dict 系」しか扱っておらず、実 SDK オブジェクトに対しては常に `None` を返していました。
- その結果 `request_to_gemini_embed` が最初のテキストで `RuntimeError("Gemini embedding response did not contain a 'values' list ...")` を送出し、Gemini 埋め込みが完全に使えない状態でした（埋め込みステップは hierarchical / llm_grouping いずれのワークフローでも必須のため、抽出ステップ実行後に失敗します）。
- 既存テスト `test_request_to_embed_use_gemini` は `embed_content` を dict（`{"embedding": [...]}`）で mock しており、実 SDK の戻り形状と乖離していたため、このバグを検知できていませんでした。

# 関連Issue
- Refs #450（#450 で追加した Gemini 埋め込み選択の後続不具合）

# 動作確認の結果
- lock 固定版の `google-genai==1.62.0` の実型を introspect し、`EmbedContentResponse.model_fields` が `embeddings`（複数）であること、実レスポンス object が `.embedding` 属性を持たず dict でもないことを確認。修正前の `extract_embedding_values` は実レスポンス object に対し `None` を返す（= `RuntimeError` 経路）ことを確認しました。
- 実 SDK と同じ object 形状（`SimpleNamespace(embeddings=[SimpleNamespace(values=[...])])`）で mock するよう `test_request_to_embed_use_gemini` を更新し、回帰ユニットテスト `test_extract_embedding_values_genai_embeddings_object` を追加しました。
- **回帰検証**: 修正前の `llm.py` に対して更新後の 2 テストを実行し、当該 `RuntimeError: ... (shape=SimpleNamespace)` で fail することを確認（テストがバグを確実に捕捉することを検証）。修正適用後は pass します。
- `apps/api/tests/services/test_llm.py` 全 77 件 pass。変更 2 ファイルに対し `ruff check` / `ruff format` も pass。
- 注記: 実 API キーを用いた実通信確認は本環境では未実施です（SDK 実型検証 + mock による回帰テストで代替）。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。
- [ ] UI（`apps/public-viewer` / `apps/admin`）の変更で利用方法・表示が変わる場合、`docs/user-guide/how-to-use.md` を更新したか（→ 本修正は内部ロジックのみで UI 変更なし。更新不要）

🤖 Generated with [Claude Code](https://claude.com/claude-code)


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Improved compatibility with Google Gemini embedding responses. The app can now read embedding values from responses that contain a list of embedding objects, including cases where no singular embedding field is present. Empty lists or entries without a values list do not produce an embedding. Existing response formats continue to be supported.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix(ci): 公開処理と定期 E2E テストを本家リポジトリのみに限定](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1014)

**作成者:** shingo-ohki  
**作成日:** 2026-10-14T11:07:12Z  
**変更:** +13 -4 (3ファイル)  
**マージ日:** 2026-10-14T15:01:24Z  
**内容:**

## 概要

fork でも本家と同じ公開・定期実行ジョブが動く問題を防ぐため、以下の処理を `digitaldemocracy2030/kouchou-ai` のみに限定しました。

- **ドキュメント公開（`docs.yml`）**：GitHub Pages 用アーティファクトのアップロードとデプロイを本家に限定
- **PyPI 公開（`publish-analysis-core.yml`）**：PyPI への公開ステップを本家に限定
- **E2E Tests（`e2e-tests.yml`）**：スケジュール実行のジョブを本家に限定

fork でのビルド・テスト、および Pull Request 時の CI は維持します。

## 背景

fork の `main` でも GitHub Pages へのデプロイが試行され、ドキュメントのビルドは成功しているのに Pages のデプロイで HTTP 404 になっていました。

発生例：https://github.com/shingo-ohki/kouchou-ai/actions/runs/38535269204

また、fork でも E2E Tests の定期実行が毎日行われていました。

実行例：https://github.com/shingo-ohki/kouchou-ai/actions/runs/38489085357

PyPI 公開ワークフローも従来はリポジトリの限定条件がありませんでした。公開用認証情報の有無に依存せず、公開処理自体を本家に限定します。

## 変更後の動作

| 処理 | 本家 | fork |
| --- | --- | --- |
| ドキュメントのビルド | 実行 | 実行 |
| GitHub Pages への公開（`main` push） | 実行 | スキップ |
| analysis-core のビルド・テスト（対象タグ push／手動実行） | 実行 | 実行 |
| PyPI への公開 | 実行 | スキップ |
| E2E Tests の定期実行 | 実行 | スキップ |
| E2E Tests の PR 実行 | 実行 | 実行 |

## 確認内容

- 変更対象は `.github/workflows/docs.yml`、`.github/workflows/publish-analysis-core.yml`、`.github/workflows/e2e-tests.yml` の3ファイルのみです。
- fork 側では公開処理や定期 E2E テストのジョブがスキップされる条件であることを定義上確認しました。
- 実際の GitHub Actions の結果は PR のチェックで確認します。

※ 定期実行イベント自体は fork でも発生しますが、E2E テストのジョブはスキップされます。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Chores**
  * Restricted documentation deployment, scheduled end-to-end test runs, and package publishing to the designated project repository. Pull-request end-to-end tests continue to run.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (6件)

### [test(api): モデルカタログのテストが 2027-01-01 以降に必ず落ちる問題を直す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1050)

**作成者:** nishio  
**作成日:** 2026-10-21T06:35:35Z  
**変更:** +34 -1 (1ファイル)  
**内容:**

## 概要
api のテスト `tests/services/test_model_catalog.py::test_requested_models_are_selectable_but_unverified` は、2027-01-01 以降はコードを変えなくても必ず落ちます。年明けに main の CI が突然赤くなるので、テストを実行日に依存しないように直します。

## 問題（再現条件）
- `src.services.model_catalog.date.today()` を 2027-01-01 にして api のテストを実行すると、このテストだけが `TypeError`（`row["price"]` が None）で落ちる。2026-12-31 までは通る。
- 日付を 2027-01-01 にして api のテスト全体（389 件）を回し、落ちるのはこの 1 件だけであることを確かめた。

## 原因
- このテストは、gemini-3.8-flash などの 4 モデルが「選べるが動作未確認」であることに加えて、単価（`price["source"]`）があることも確かめている。
- `model_catalog.json` の gemini-3.8-flash の単価には `"valid_until": "2026-12-31"` がある（b84434bf で導入）。
- `price_for_model` は、`valid_until` を過ぎた単価を None にする。期限切れの単価を表示しないための仕様で、`test_expired_price_is_unknown` で確かめている。
- そのため、このテストは実行日だけで結果が変わっていた。

## 変更
- `test_requested_models_are_selectable_but_unverified`：`src.services.model_catalog.date` を差し替え、日付を単価の確認日（`checked_at` の 2026-09-08）に固定した。
- `test_model_stays_selectable_after_price_expires` を追加した。差し替えたカタログで、期限の当日は単価があり、翌日は単価が None になってもモデルは選べたまま（`available: True`）であることを確かめる。実際のカタログの期限の値には依存させていない。
- 本体のコードとカタログは変更していない。gemini-3.8-flash の単価を確認し直して `valid_until` を延ばすかどうかは、別に判断が要る。

## テスト
- `apps/api` で `pytest`：390 件すべて通過した（実行日 2026-10-21）。
- `test_model_catalog.py`（18 件）を、`model_catalog.date.today()` を 2027-01-01 にする pytest plugin を付けて実行した。修正前は 1 件失敗し、修正後はすべて通過した。
- `ruff check` / `ruff format --check`：通過した。

🤖 Generated with [Claude Code](https://claude.com/claude-code)


**コメント:** なし

---

### [fix(analysis-core): .env をパッケージの置き場所ではなく作業ディレクトリから探す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1049)

**作成者:** nishio  
**作成日:** 2026-10-21T06:31:41Z  
**変更:** +63 -7 (5ファイル)  
**内容:**

## 概要
CLI クイックスタート（`docs/user-guide/cli-quickstart.md`）の手順どおりに `pip install` して作業ディレクトリに `.env` を置いても、`kouchou-analyze` がその `.env` を読まずに `OPENAI_API_KEY environment variable is not set` で終了します。この問題を直します。

## 問題（再現条件）
- `pip install kouchou-ai-analysis-core`（editable ではない通常のインストール）をする。
- 作業ディレクトリに `config.json`・`inputs/`・`.env`（`OPENAI_API_KEY=...`）を置き、環境変数は設定せずに `kouchou-analyze --config config.json` を実行する。
- `.env` があるのに `Error: OPENAI_API_KEY environment variable is not set.` で exit=1 になる。
- 逆に、リポジトリを editable install して使う開発環境では、どの作業ディレクトリで実行しても、リポジトリ直下の `.env` が読まれる。`env -u OPENAI_API_KEY` で外しても、`.env` から読み直される。テストが開発者の実キーで LLM に要求を送っていた件（#1048）は、この経路でキーが入っていた。

## 原因
- `services/llm.py`・`services/timeouts.py`（import 時）と `core/orchestration.py` の `validate_api_keys` は、引数なしで `load_dotenv()` を呼んでいた。
- 引数なしの `load_dotenv()` は `find_dotenv()` を使い、呼び出し元のファイル（インストールされた `analysis_core` の .py）の場所から親をさかのぼって `.env` を探す。作業ディレクトリは見ない。
  - pip で入れた場合は site-packages の親をさかのぼるので、ユーザーの `.env` は見つからない。
  - editable install では `packages/analysis-core/src/...` の親をさかのぼるので、リポジトリ直下の `.env` が見つかる。
- `llm.py` のコメントは「Look in current directory first, then parent directories」で、作業ディレクトリから探す意図だった。
- なお `python -c` や対話環境では python-dotenv が作業ディレクトリから探すので、そこでは問題が見えない。

## 変更
- `analysis_core/env_file.py` に `load_env_file()` を追加した。`find_dotenv(usecwd=True)` で作業ディレクトリとその親から `.env` を探して読み込む。
  - `services` 配下に置くと `core/orchestration.py` の import で openai まで読み込まれるようになるので、パッケージ直下に置いた。
- `llm.py`・`timeouts.py`・`validate_api_keys` の `load_dotenv()` をこれに置き換えた。`override` の扱いは変えていない（既存の環境変数が優先）。
- 影響
  - リポジトリ内で作業する開発者：作業ディレクトリから親をさかのぼるので、従来どおりリポジトリ直下の `.env` が読まれる。
  - Docker の API：環境変数は compose から渡されるので変わらない（`apps/api/src/config.py` は元から作業ディレクトリ基準）。
  - リポジトリの外で editable install した CLI を使う場合：リポジトリ直下の `.env` は読まれなくなる。作業ディレクトリの `.env` か環境変数で渡す。

## テスト
### 追加したテスト
`packages/analysis-core/tests/test_env_file.py`（2 件）。CLI と同じくスクリプトファイルとして別プロセスで実行し、作業ディレクトリの親に置いた `.env` が読まれることを確かめる。
- import 時：`LLM_REQUEST_TIMEOUT_SECONDS` と `OPENAI_API_KEY` が `.env` から入る
- `validate_api_keys("openai")` が `.env` のキーで通る

### 修正前に失敗することの確認
本体の 3 ファイルを main（c57e0bfa）に戻すと、追加した 2 件はどちらも失敗する（`OPENAI_API_KEY environment variable is not set`）。

### 修正後
- `packages/analysis-core` で `pytest`：418 件すべて通過した。
- `ruff check`：通過した。
- 非 editable で入れた CLI での確認：作業ディレクトリに偽キーと記録用ローカルサーバーを書いた `.env` を置いて `kouchou-analyze --config config.json` を実行した。
  - 修正前：`OPENAI_API_KEY environment variable is not set` で exit=1。
  - 修正後：キーの検査を通り、`.env` のキーを付けた `/v1/chat/completions` の要求が記録用サーバーに届いた。

🤖 Generated with [Claude Code](https://claude.com/claude-code)


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

<!-- coderabbit-ai-generated:v1 -->

## Summary by CodeRabbit

- **New Features**
  - Environment configuration can now be loaded from a `.env` file located in a parent directory, making settings available when running tools from nested folders.
  - Existing environment variables remain unchanged by default when loading configuration.

- **Bug Fixes**
  - Improved consistency when loading API keys and timeout settings across analysis and language-model services.

- **Tests**
  - Added coverage verifying configuration discovery from nested working directories and validation of API-key settings.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [test(analysis-core): テストが .env のキーで実際に LLM へ要求を送らないようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1048)

**作成者:** nishio  
**作成日:** 2026-10-21T06:27:43Z  
**変更:** +68 -8 (2ファイル)  
**内容:**

## 概要
analysis-core の pytest を回すと、リポジトリ直下に `.env` がある開発環境では、その API キーを付けて OpenAI の `/v1/chat/completions` に実際に要求が送られていました。テストは失敗を握りつぶすので、通過したまま課金・送信が起きます。この問題を直します。

## 問題（再現条件）
- リポジトリ直下に `OPENAI_API_KEY` を書いた `.env` を置き、`packages/analysis-core` で `pytest` を実行する（環境変数の `OPENAI_API_KEY` は未設定でよい）。
- `tests/test_pipeline_paths_integration.py::TestPipelinePathsIntegration::test_extraction_step_uses_config_paths` が、`.env` のキーで `/v1/chat/completions`（gpt-4o-mini）に要求を送る。
  - 偽キーと記録用のローカルサーバーを `.env` に書いて確かめた。テストのコメント本文（`This is a test comment about AI`）が届き、テストは 9 件とも passed。
- `.env` が無くても、`OPENAI_API_KEY` が設定されていれば api.openai.com:443 に接続する。

## 原因
- このテストは LLM を mock せずに `extraction()` を呼び、`except Exception: pass  # Expected - we're not mocking LLM` で失敗を握りつぶしていた。キーが無効でも、接続できなくても passed になる。
- `analysis_core/services/llm.py` は import 時に `load_dotenv()` を呼ぶ。python-dotenv はこのとき呼び出し元のファイルの場所から親をさかのぼって `.env` を探すので、editable install ではリポジトリ直下の `.env` が読まれる。

## 変更
- `test_extraction_step_uses_config_paths`：`request_to_chat_ai` を mock し、`try/except` をやめた。抽出が最後まで進み、`args.csv` が書かれることも確かめるようにした。
- `packages/analysis-core/tests/conftest.py` を追加した。
  - 自動で適用される fixture で、loopback 以外への socket 接続を遮断する。
  - 接続を試みたテストは、コード側が例外を握りつぶしても teardown で失敗する。今回のような mock 漏れを今後も検出するため。
  - 実 API を呼ぶ e2e（`e2e` マーク）は対象外。
- 本体のコードは変更していない。`load_dotenv()` がパッケージの場所から `.env` を探す件は別の PR で扱う。

## テスト
### 修正前のテストを検出できることの確認
修正前の `test_pipeline_paths_integration.py` に、追加した conftest だけを当てて実行した。`OPENAI_API_KEY=sk-dummy` で、テストは api.openai.com への接続の試み（12 回）を理由に error になった。

### 修正後
- `packages/analysis-core` で `pytest`：416 件すべて通過した。追加したガードに引っかかる既存のテストは無い。
- 偽キーと記録用サーバーを書いた `.env` を置いて実行した。記録用サーバーへの要求は 0 件だった。
- `pytest tests/e2e`：キーが無いので skip。e2e はガードの対象外のまま。
- `ruff check`：通過した。

🤖 Generated with [Claude Code](https://claude.com/claude-code)


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

<!-- coderabbit-ai-generated:v1 -->

## Summary by CodeRabbit

- **Tests**
  - Improved test isolation by preventing non-end-to-end tests from making external network connections.
  - Updated pipeline integration coverage to use controlled AI request responses instead of real external requests.
  - Added verification that the expected number of AI requests is made and that the CSV output is generated successfully.
  - Test suites now fail clearly when unexpected external network access or connection failures occur.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix(analysis-core): 集計結果の出力内容を整理（取り下げ）](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1026)

**作成者:** nishio  
**作成日:** 2026-10-18T12:54:46Z  
**変更:** +92 -1 (2ファイル)  
**内容:**

一旦取り下げます。内容を整理して改めて提出します。


**コメント:** なし

---

### [fix(public-viewer): [選択肢b] 散布図ラベルの効いていない dimming 分岐を削除 (#1023)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1025)

**作成者:** nishio  
**作成日:** 2026-10-16T11:50:41Z  
**変更:** +4 -8 (1ファイル)  
**内容:**

# 変更の概要
散布図ラベルの、**効いていない** dimming 分岐を削除し、ラベル背景を常に元のクラスタ配色にします（＝「背景色を維持」というコメントの意図を正とする）。これは #1023 の **選択肢 (b)** です（(a)＝実際に薄くする。**どちらか一方のみ採用**想定で、採用しない方は close）。

# スクリーンショット
見た目は現状維持（効いていない分岐の削除のため表示は変わりません）。下の比較の **左（現状 b）** が本 PR 後の表示です（右は選択肢 a＝ #1024）。

![現状(b) と 選択肢a の比較](https://raw.githubusercontent.com/nishio/kouchou-ai-developer-wiki/main/assets/review-2026-10-16/h-ab.png)

> スクショは実コードの注釈スタイルを再現したモックです（実プロット背景は白）。

# 変更の背景
`clusterColorMapA` は `#RRGGBBcc`（不透明度 0.8）で、従来の dimming 分岐は末尾を `"cc"` に置換する no-op のため何も変えていませんでした。加えて隣接コメントは「背景色を維持（元の色で表示）」と、分岐の意図（薄くする）と矛盾していました（詳細は #1023）。本 PR は「元の色を維持」を正とし、死んだ分岐・不要になった `@ts-ignore`・誤解を招くコメントを削除してシンプルにします（`separateDataByFilter` / `allFiltered` は他箇所で使用のため温存）。

# 関連Issue
- #1023（選択肢 b。採否はそちらで議論）

# 動作確認の結果
- `biome check` クリーン、`tsc --noEmit` エラーなし（削除した `@ts-ignore` に依存する箇所が残っていないことを確認）、`components/charts` の jest **89 件 pass**（隔離 worktree で実行）。挙動は現状維持（デッドコード削除）。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか（→ デッドコード削除で挙動不変のため新規テストなし。tsc / biome / 既存 chart テストで確認）
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。
- [ ] UI の変更で利用方法・表示が変わる場合、`docs/user-guide/how-to-use.md` を更新したか（→ 見た目・操作とも不変。更新不要）

🤖 Generated with [Claude Code](https://claude.com/claude-code)


**コメント:** なし

---

### [fix(public-viewer): [選択肢a] 全点フィルタ済みクラスタのラベル背景を実際に薄くする (#1023)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/1024)

**作成者:** nishio  
**作成日:** 2026-10-16T11:50:38Z  
**変更:** +5 -2 (1ファイル)  
**内容:**

# 変更の概要
散布図ラベルの「全点フィルタ済みクラスタを薄くする」挙動を**実際に効く**ようにします。これは #1023 の **選択肢 (a)** です（(b)＝効いていない分岐の削除。**どちらか一方のみ採用**想定で、採用しない方は close）。

# スクリーンショット
全点フィルタで「防災・防犯」が 0 件になったときのラベル表示（**左＝現状 b / 右＝本 PR a**）。本 PR では右のように薄く表示され、「該当なし」が分かります。

![現状(b) と 本PR(a) の比較](https://raw.githubusercontent.com/nishio/kouchou-ai-developer-wiki/main/assets/review-2026-10-16/h-ab.png)

透明度の候補（白文字の読みやすさ ↔ 区別しやすさ。値は調整可能・議論は #1023）:

![透明度サンプル 1.0〜0.3](https://raw.githubusercontent.com/nishio/kouchou-ai-developer-wiki/main/assets/review-2026-10-16/h-alpha.png)

> スクショは実コードの注釈スタイルを再現したモックです（実プロット背景は白）。

# 変更の背景
`clusterColorMapA` は `#RRGGBB` ＋ `Math.floor(0.8*255)=0xcc` ＝ `#RRGGBBcc`（不透明度 0.8）。従来の dimming 分岐は末尾 2 桁（`cc`）を `"cc"` に置換する **no-op** で、全点フィルタ済みクラスタのラベルが薄くなりませんでした（詳細は #1023）。末尾アルファを `66`（0.4）に下げて実際に薄くし、「現在のフィルタに該当なし」を視覚化します。矛盾していた隣接コメントも整理しました。
- 留意: ラベル文字は白なので、薄くしすぎると白地で白文字が読みにくくなります。まず 0.4 にしていますが、値は調整可能です。

# 関連Issue
- #1023（選択肢 a。採否はそちらで議論）

# 動作確認の結果
- `biome check` クリーン、`components/charts` の jest **89 件 pass**（隔離 worktree で実行）。純粋に表示（背景アルファ）の変更で、型・データ・クラスタリング結果には影響しません。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか（→ Plotly 注釈内の表示色のため専用 unit test は未追加。biome / 既存 chart テスト / 目視で確認）
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。
- [ ] UI の変更で利用方法・表示が変わる場合、`docs/user-guide/how-to-use.md` を更新したか（→ 全点フィルタ済みクラスタのラベルが薄くなる見た目変更のみ。操作手順は不変で更新不要）

🤖 Generated with [Claude Code](https://claude.com/claude-code)


**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

