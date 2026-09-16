# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-09-09T17:27:04.095181+09:00 から 2026-09-16T17:27:04.095181+09:00 まで

## Issues

### 過去7日間に完了されたissue (2件)

### [[FEATURE] shell配布物にレポート別title・noindexを反映する（#935由来）](https://github.com/digitaldemocracy2030/kouchou-ai/issues/939)

**作成者:** nishio  
**作成日:** 2026-09-09T07:30:23Z  
**内容:**

## 背景・出典

#935「データ非依存な静的出力 (shell ビルド)」由来の後続課題です。PR作者が「把握している制約（このPRでは対応していません）」に挙げた、レポート別の`<title>`とunlistedの`noindex`を切り出します。

#935は、画面を一度ビルドし、レポート出力時にはHTMLのコピーとJSON同梱で済ませることで、利用者環境のNode依存を減らす基盤です。共通HTMLを使うため、現状のshellモードはタイトルが「広聴AI」で固定され、レポートごとの検索除外設定を含みません。

従来の静的exportは`apps/public-viewer/app/[slug]/page.tsx`の`generateMetadata`でタイトルを設定し、`visibility === unlisted`の場合に`noindex, nofollow`を設定します。shellモードはその前で共通metadataを返します。

## 対応したいこと

- 実データからshell配布物を作る段階で、レポート別タイトルを反映する方法を決めて実装する。
- Web公開するunlistedレポートについて、配布HTMLに検索除外設定を含める。ブラウザでJavaScriptを実行した後だけの設定に依存しない。
- ローカル閲覧とWeb公開の用途を区別し、#885の配布物生成の実装と接続する。レポートごとのNodeビルドは復活させない。

## 完了条件

- 異なる2レポートの配布HTMLに、それぞれのタイトルが正しく入り、引用符・日本語等を含む場合もHTMLを壊さない。
- unlistedレポートの配布HTMLには`noindex`が含まれ、公開レポートには意図しない検索除外が付かない。
- ブラウザで詳細を直接開く場合と、一覧から移動する場合のタイトルが整合する。
- 共通assetsは再利用され、レポート追加のたびにNext/Nodeによるビルドが不要なことを維持する。
- テストで配布HTMLとブラウザの両方を確認する。

## 範囲外

- OGP画像の生成は別の既存課題（#936は説明訂正）。
- 今回別途修正したhydrationエラーとは別件。

関連: #935 / #936 / #885


**コメント:** なし

---

### [[FEATURE] OpenAIのAPIをFlex-Processingにしてコストを半額にする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/916)

**作成者:** tokoroten  
**作成日:** 2026-09-07T20:08:48Z  
**内容:**

# 背景

OpenAIのAPIのコストを下げるために、Flex-Processingの採用を検討する。

https://developers.openai.com/api/docs/guides/flex-processing?api-mode=responses

レイテンシーが悪くなる代わりにコストが半額になるプラン

#374 の時点では、Flex-Processingは高級なモデルにしかサポートされておらず、汎用的に使える機能ではなかったため採用を見送った。

# 提案内容

現在は、GPT6、GPT5.6、GPT5.5の主要なモデルがFlexとサポートしているので、OpenAIを利用するのであれば、Flexオプションを有効にしても良いと考えられる


**コメント:** なし

---

### 過去7日間に作成されたissue (0件)

### 過去7日間に更新されたissue（作成・クローズを除く）(7件)

### [[FEATURE] Windows単一実行ファイル配布に向けて Web UI の Node runtime 依存をなくす](https://github.com/digitaldemocracy2030/kouchou-ai/issues/885)

**作成者:** nishio  
**作成日:** 2026-05-31T05:57:44Z  
**内容:**

## 背景

Slack で「Windows ユーザ的には実行バイナリがいっこあるだけが嬉しい」という話が出ました。以前の `#289` では、広聴AIを exe 配布するには Python/FastAPI と Next.js/Node の両方を抱える必要があり、完全単体化は重いという整理で止まっていました。

ただし current main を見ると、runtime の Node サーバ層はかなり薄くなっています。

- `apps/api` は既に FastAPI で、分析実行・レポート状態・管理 API・公開 API を持っている
- `apps/public-viewer` は `NEXT_PUBLIC_OUTPUT_MODE=export` / `build:static` を持ち、静的出力経路がある
- `apps/static-site-builder` は Express で `pnpm run build:static` を実行して `out/` を zip するだけ
- `apps/admin` の Node runtime 依存は、初期レポート一覧 fetch、11 個の Server Actions、3 個の Route Handlers (`/api/download`, `/api/admin/reports/[slug]/config`, `/api/healthcheck`)、Next の headers/CSP にほぼ限られる

つまり「Node をバイナリに同梱する」のではなく、Web UI を SPA/static assets に寄せ、必要な server-side wrapper を Python/FastAPI に寄せれば、**runtime は Python exe + 静的 assets** に近づけられる可能性があります。

さらに、単一実行ファイル配布の価値は「Docker なし」だけではなく **API 契約なしで local 完結** できる点にもあります。したがって MVP scope は外部 API route だけに固定せず、軽量モデルを同梱する offline route や、Chrome / Windows の native local AI runtime を使う route も比較対象に入れます。

## 提案

Windows 単一実行ファイル配布の前提タスクとして、Web UI の Node runtime 依存をなくす方針を検討・実装したいです。

想定する方向:

1. `apps/admin` を static export / SPA 化できるようにする
   - `app/page.tsx` の server-side fetch を client-side fetch に寄せる
   - `"use server"` の Server Actions を client fetch + shared API client に置き換える
   - `app/api/*/route.ts` の薄い proxy は FastAPI 側へ移すか、直接 API 呼び出しに変える
   - Next の `headers()` に依存している CSP は、Python 側 static serving または desktop/local 前提の配信設定へ移す

2. `apps/public-viewer` の runtime Node 依存を整理する
   - live viewer を static assets + client fetch で動かすか、local desktop MVP では admin から開く閲覧画面だけを対象にするかを決める
   - `revalidateTag` / ISR 前提の `/api/revalidate` は、Node runtime なしでは使わない設計にする
   - OGP 画像生成など Next 固有機能は、static fallback か別タスクへ分ける

3. `apps/static-site-builder` を FastAPI/Python へ寄せる
   - 現状の Express サーバは `pnpm run build:static` + zip だけなので、Python 側で同等 API を持てる
   - ただし「レポートごとの静的 HTML 出力」に Node build を runtime 実行し続けるなら、単一 exe には Node 同梱が戻ってくる
   - runtime Node なしを本気で狙うなら、public-viewer の事前ビルド済み assets で完結する方式、または Python 側の静的レポート生成方式を検討する

4. FastAPI で admin / public-viewer の静的 assets を serve する
   - 1 port (`localhost:8000` など) に寄せる
   - API と static assets の URL / base path / CORS / CSP を再整理する

5. Windows 配布 spike を作る
   - PyInstaller / Nuitka 等で FastAPI + analysis-core + static assets を固める
   - まずは次の 2 route を比較する
     - **API route**: OpenAI/Gemini API 利用、local storage、CPU、Docker なし。小さい artifact と品質を優先
     - **offline route**: local storage、CPU、Docker なし、API 契約なし。local 完結を優先
       - direct bundled-model option: 軽量 LLM / embedding model と推論 runtime を配布物に含める、または初回 download + local cache にする
       - platform-managed native runtime option: Foundry Local / Chrome Prompt API / Windows AI APIs などを provider として使う

## 実現可能性メモ

これは「数行でできる」話ではありませんが、current main の構造を見る限り **段階的には実現可能** です。特に admin 側の Node runtime 責務は、既存 FastAPI endpoint の薄い wrapper が多く、置換対象が見えています。

一方で、完全単体 exe の難所は残ります。

- Python 側の依存 (`torch`, `numba`, `scipy`, `umap-learn` 等) はバイナリサイズ・hidden import・Windows AV 誤検知のリスクがある
- Next.js static export では、Node server が必要な dynamic logic / headers / ISR / request-dependent route handlers は使えない
- admin API key を static client に載せてよいかは local desktop 前提の threat model を明示する必要がある
- on-demand の「静的 HTML zip 出力」を Node build なしで維持するには別設計が要る
- bundled-model route は API 契約不要になる一方、モデルファイルのサイズ・ライセンス・品質・推論速度・初回ロード時間・更新方法を product scope として抱える
- current code には `provider="local"` の OpenAI 互換 local LLM 経路と `is_embedded_at_local` / SentenceTransformer local embedding 経路があるが、現状は Ollama / LM Studio / Hugging Face cache など外部 runtime や初回 download に寄っている。offline route では、モデルファイルを同梱するのか、初回 download + local cache にするのか、platform runtime に任せるのかを決める必要がある
- Chrome Prompt API は Gemini Nano を browser 内で使えるが、広聴AIの Python/FastAPI batch pipeline から直接呼べない。browser tab / user activation / 長時間 batch 実行の lifecycle が risk なので、primary backend より client-side 補助や browser-only 実験向きに見える
- Microsoft Foundry Local は Python SDK、OpenAI-compatible local endpoint、embeddings、model download/cache 管理、Windows ML integration があり、current `provider="local"` に最も接続しやすい native runtime 候補
- Phi Silica / Windows AI APIs は Copilot+ PC / NPU 向けで方向性は合うが、supported device と experimental API 制約があるため、当面は future option / benchmark 対象として扱う

したがってこの issue は `#289` の直接再開ではなく、`#289` を現実的に再評価するための前提 issue として扱いたいです。local model の標準選定・推奨スペックは `#471`、embedding model 選択は `#450`、PLaMo-Embedding 実験は `#573` と接続します。

## 完了条件

- Web UI の runtime Node 依存一覧がドキュメント化されている
- `apps/admin` を static assets として serve するための最小方針が決まっている
- `apps/static-site-builder` の責務を FastAPI へ移すか、Node build を残す範囲が明示されている
- local desktop MVP の scope が 2 route で比較されている
  - API route: OpenAI/Gemini API、local storage、CPU、localhost、Docker なし
  - offline route: API 契約なし、local storage、CPU、localhost、Docker なし
  - 共通 out of scope 初期案: GPU acceleration 必須化、Ollama 依存、コード署名、自動更新、組織配布ポリシー対応
- offline route について、最低限以下を決める
  - direct bundled-model option の chat model / embedding model 候補とライセンス
  - モデルファイルを package に同梱するか、初回起動時 download にするか、platform runtime に任せるか
  - Foundry Local / Chrome Prompt API / Windows AI APIs を比較し、first spike 対象を決める
  - どのデータ量なら CPU / NPU / GPU なし環境で現実的に待てるか
  - API route との品質差を許容する UX / warning
- 可能なら prototype branch で以下を確認する
  - FastAPI が prebuilt admin assets を配信する
  - レポート一覧取得・作成・進捗 polling・削除/編集の主要 flow が Node server なしで動く
  - Windows で `python -m ...` または PyInstaller/Nuitka artifact から起動できる
  - offline route ではネットワークなし、または初回 model acquisition 後のネットワークなしで、小さな sample report を生成できる

## 参考

- related: `#289` [FEATURE]exe形式での配布によるインストール簡略化
- related: `#471` [DOCUMENT] ローカルLLMのベンチマーク、推奨スペックの決定
- related: `#450` [FEATURE]エンベデッドモデルを選択可能にする
- related: `#573` [ALGORITHM] PLaMo-Embedding-1Bの動作実験
- related: `#877` Windows セットアップガイドの前提条件整理
- Chrome Prompt API docs: https://developer.chrome.com/docs/ai/prompt-api
- Microsoft Foundry Local docs: https://learn.microsoft.com/en-us/azure/foundry-local/what-is-foundry-local
- Microsoft Foundry Local embeddings: https://learn.microsoft.com/en-us/azure/foundry-local/how-to/how-to-generate-embeddings
- Phi Silica platform card: https://learn.microsoft.com/en-us/windows/ai/cards/phi-silica-platform-card
- current code: `apps/api`, `apps/admin`, `apps/public-viewer`, `apps/static-site-builder`, `packages/analysis-core/src/analysis_core/services/llm.py`


**コメント:** なし

---

### [[FEATURE] Azure OpenAI Service 利用時のエラーハンドリングをよりユーザーフレンドリーにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/592)

**作成者:** shingo-ohki  
**作成日:** 2025-06-06T10:19:59Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

自治体でセットアップ時にハマったところ

> ここまででハマったことなんですが、今回Azure OpenAI Serviceを用いて構築していますが、APIバージョンとモデルバージョンを誤って.envに記述していました。（本来はAPIバージョンを記述する必要があります）
> そこで、[https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/server/broadlistening/pipeline/services/llm.py](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/server/broadlistening/pipeline/services/llm.py%E3%81%AE)のrequest_to_azure_chatcompletionメソッドで、エンドポイントに接続できない旨のエラーになっていましたが、例外がキャッチされていなく原因を特定するまでに時間が掛かりました。

from #2_開発_広聴ai より

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

## 2026-09-09 進捗

PR #945（未マージ）で、管理画面の接続確認が不明エラーになった場合、Azureを選択していればAPIバージョンとモデルバージョンの違い、同じリソースの設定を確認する案内を表示するようにしました。サーバー側の確認APIと、管理画面の2つの確認ダイアログを対象にしています。

バックエンド23件・関連UI27件の単体テストとCIが成功しています。実際のAzureリソースへの接続試験は行っていません。解析パイプライン全体の例外処理整理はこのPRの対象外のため、Issueは継続します。


**コメント:** なし

---

### [最新のコードでstatic exportしたページを確認できるようにしたい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/518)

**作成者:** nasuka  
**作成日:** 2025-05-15T04:06:11Z  
**内容:**

# 背景
* static exportしたページに問題がないかを確認するには、現状手動でexportして確認する必要がある
* 毎回手動でexportするのは大変なので自動化したい

# 提案内容
上記の自動化を実現する。

実現方針の案
* main branchにコミットがあったタイミングで github actionsを用いてstatic exportを実行する
* exportしたページをgithub pagesにホスティングする

deep research
https://chatgpt.com/c/6825654d-6bc4-800f-840a-b8e2ff3531f3

現在使えるリソースがgithubくらいなのでgithub pagesでホスティングする案を記載しているが、他に良さそうな選択肢があればそちらでもOK。

## 2026-09-09 確認用artifactの実装（PR #942、未マージ）

既存client buildで作った静的viewerを、コミットSHA付きのartifactとして7日間保存する変更を追加しました。CIが成功し、成果物の取得とローカルHTTPサーバーでの一覧表示を確認しています。

PR: https://github.com/digitaldemocracy2030/kouchou-ai/pull/942

常設URLへの公開は後続です。通常static出力の閲覧ではReact #418を観測したため、保存処理の成功と画面の実行時エラーを区別して記録します。今回はviewer/build方式を変更していません。


**コメント:** なし

---

### [管理画面のe2eテスト拡張ケース](https://github.com/digitaldemocracy2030/kouchou-ai/issues/395)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-30T01:41:40Z  
**内容:**

# 管理画面のe2eテスト拡張ケース

## 追加テストケース

1. Googleスプレッドシートからのデータインポート
   - スプレッドシートURLの入力と取得テスト
   - データ列の選択と表示確認

2. 入力バリデーションのテスト
   - 必須フィールドが空の場合のエラー表示
   - 無効なレポートIDの検証
   - 文字数制限の検証

3. AI詳細設定の変更とその反映
   - モデル選択の変更
   - ワーカー数の調整
   - PubComモードの切り替え
   - プロンプト設定の変更

4. エラーケースのテスト
   - **APIキーが間違っている場合のエラー処理**
   - **クレジットが入っていない場合のエラー処理**
   - ネットワークエラー時の処理
   - サーバーエラー時の処理

## 実装優先度

特に優先度が高いのは:
- APIキーエラーの適切な処理と表示
- クレジット不足時のエラー処理と表示

## 関連ファイル

- `test/e2e/tests/admin/create-report.spec.ts`
- `test/e2e/utils/mock-api.ts`
- `client-admin/app/create/page.tsx`


---

## 2026-09-09 現状と残作業

E2Eの導入自体は済んでいるため、上位計画 #379 の残ケースをこちらで追跡します。

現行mainにはCSV作成、確認画面の1280px/375px、複製時の要約プロンプト引継ぎのテストがあります。API認証・quota・rate limit・通信失敗は単体試験がありますが、`create-report.spec.ts` のAPIエラーE2Eは現在 `test.skip` です。「単体試験あり」を「ブラウザ経路まで確認済み」と扱わないようにします。

優先する残作業:
- [ ] ダミーAPIで認証失敗・quota不足・通信失敗を再現し、確認画面→設定へ戻る→再確認のE2Eを有効化する（実キー不要）。
- [ ] Spreadsheetの取得と列選択をタブ切替だけでなく通して検証する。
- [ ] モデル・ワーカー・PubCom・各プロンプトが最終送信内容に反映されることを検証する。

根拠: https://github.com/digitaldemocracy2030/kouchou-ai/blob/2dd5adc21103e880bf0250f29511f99a05c52590/test/e2e/tests/admin/create-report.spec.ts / https://github.com/digitaldemocracy2030/kouchou-ai/blob/2dd5adc21103e880bf0250f29511f99a05c52590/test/e2e/tests/admin/duplicate-report.spec.ts


## 2026-09-09 エラー復帰E2Eの実装（PR #943、未マージ）

認証・quota・rate limit・HTTP 503・通信切断の5ケースで、確認画面→設定へ戻る→キー変更→再確認のブラウザテストを追加しました。実キー不要、ダミーAPIのリクエスト単位の応答で再現します。ローカルでは事前検証4件、新規5件、既存作成・複製15件が成功しています。

PR: https://github.com/digitaldemocracy2030/kouchou-ai/pull/943

残作業はCI・マージ確認、Spreadsheetの取得と列選択、AI詳細設定の最終送信内容の検証です。Issue全体は完了扱いにしません。


**コメント:** なし

---

### [プラポリURL等をhowtoに記載すると良さそう](https://github.com/digitaldemocracy2030/kouchou-ai/issues/393)

**作成者:** nasuka  
**作成日:** 2025-04-29T13:13:43Z  
**内容:**

## 要望内容
改善案
metaデータ以外の変更箇所（フッターのプラポリ・利用規約、テスト環境のページへ）について、howtoもしくはReadMeに記載する。

改善する
変更することを忘れやすく、デバック時も気づかれない可能性がある。
ドキュメントに記載することで、公開前のチェックリストとなる。

---
こちらのイシューはGoogle Form経由で投稿されたものです

**コメント:** なし

---

### [[DOCUMENT]ソースコードの実装以外での貢献方法がもっと言語化されるとよい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/130)

**作成者:** nishio  
**作成日:** 2025-03-22T14:31:29Z  
**内容:**

# 現在の問題点
非エンジニアが何をしたらいいかわからない

# 提案内容

例えば
- GitHubのissuesをみて「その問題が解決されると自分も助かる！」と思ったものに:+1:をつけるのはタスクの優先付の参考になるので貢献
- 質問をするのは言語化のきっかけになるので貢献
- 将来的に「AのレポートとBのレポートのどっちがいいですか？」をやる可能性がある、そう言うのに回答してくれるのは貢献

他に思いついたら下にコメントつけてください

---

## 2026-09-09 現状と残作業

コード以外の貢献の入口として、現在のcontributingにはIssueへのリアクションは記載されていますが、ここに集まった利用感想・質問・事例・比較評価等を初見で選べる案内はまだ不足しています。

次の具体的な掲載先は `docs/development/contributing.md` と #876 の入口ページ。最初の一歩を「レポートを読んで分からなかった点を記録」「#564へ出典付き事例」「#912 / #913等の明示された確認作業」「同じ根拠から作ったA/B案の比較」のように、成果の残し先とセットで記載する案です。個人への依頼や役割割当は今回行っていません。


**コメント:** なし

---

### [[FEATURE] 濃いクラスタのしきい値のデフォルト値をレポートごとに設定できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/55)

**作成者:** nanocloudx  
**作成日:** 2025-03-16T03:55:36Z  
**内容:**

# 背景
現在の濃いクラスタのしきい値のデフォルト値はレポートごとに一律で固定値（上位20%・最小5件以上）となっている。
レポート出力者が、出力結果を確認した上で、しきい値のデフォルト値を変更できると良い

# 提案内容
- client-admin にて、出力済みのレポートに対して、デフォルトのしきい値を追加保存できるようにする
- client では濃いクラスタの初期表示が、レポート出力者の指定したしきい値になるようにする

---

## 2026-09-09 現状と残作業

現行viewerは `visualizationConfig.params.scatterDensity.maxDensity / minValue` を初期値として読めます。しかし管理画面の可視化設定ダイアログでは、表示チャート・初期チャートを選べるだけで、この閾値を編集する入力欄はありません。後半だけ実装済みとしてopenを維持します。

残作業: 既存の設定保存APIへ閾値の編集を接続し、値の検証・保存後の再読込・公開viewer初期表示まで確認する。他の可視化設定を保存時に落とさないことも検査します。

根拠: https://github.com/digitaldemocracy2030/kouchou-ai/blob/2dd5adc21103e880bf0250f29511f99a05c52590/apps/admin/app/_components/ReportCard/VisualizationConfigDialog/VisualizationConfigDialog.tsx / https://github.com/digitaldemocracy2030/kouchou-ai/blob/2dd5adc21103e880bf0250f29511f99a05c52590/apps/public-viewer/components/report/ClientContainer.tsx


**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (6件)

### [feat: shell配布物にレポート別title・noindexを反映](https://github.com/digitaldemocracy2030/kouchou-ai/pull/940)

**作成者:** nishio  
**作成日:** 2026-09-09T08:33:42Z  
**変更:** +560 -96 (15ファイル)  
**マージ日:** 2026-09-09T09:07:54Z  
**内容:**

## 解決する問題

#935の共通shellではタイトルが「広聴AI」に固定され、限定公開レポートの初期HTMLに検索除外設定がありませんでした。配布物を組み立てる際に「質問 - レポーター」とrobotsを挿入し、JavaScriptを実行しない場合にも反映します。

Closes #939（#935作者が挙げた制約への対応）

## 変更

- Python標準ライブラリのみの組立関数・CLIを追加。事前ビルドした共通assetsと公開API形式のJSONから出力し、レポートごとのNodeビルドを不要にします。
- タイトルをHTMLエスケープし、限定公開は`noindex, nofollow`、公開は`index, follow`を設定。限定公開は一覧から除外し、private・状態不整合・出力先衝突を拒否します。
- 一覧・詳細の画面遷移でも同じメタデータを更新し、限定公開の検索除外が公開ページに残らないようにします。
- E2Eの組立アダプターからも同じPython実装を呼び、利用方法を開発ドキュメントに追加しました。

既存の`/build`は変更していません。今回のCLI／関数が#885で利用する組立処理となり、FastAPIのダウンロード経路への接続は後続作業です。ローカル閲覧はHTTPサーバー経由、Web公開は配布物全体の配置を想定します。OGPは範囲外です。

## 検証

- Python: 10件成功（生HTML、エスケープ、公開状態、assets再利用、アプリ依存のないCLI実行等）。
- 本番shellビルド成功。Chromiumのshell E2E: 8件成功（JavaScript無効の公開／限定公開、直接表示、一覧遷移、再読み込み、hydration回帰）。
- viewer Jest: 12 suites / 123件成功。
- Ruff lint / format、変更TSのBiome、diff check成功。

既存の「HTMLに質問がない」E2Eは、仕様変更に合わせ、共通テンプレートと配布後の本文・RSCには質問がなく、配布HTMLのtitleだけに入ることを検証します。


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **New Features**
  - Added static shell packaging that creates standalone report pages from prebuilt assets and public API data, without requiring Node.js or a live API connection.
  - Report pages now display accurate titles and robots metadata, including `noindex, nofollow` for unlisted reports.
  - Shell navigation keeps page metadata synchronized when moving between reports and the report list.

- **Documentation**
  - Added developer guidance for building, serving, and publishing static shell distributions.

- **Tests**
  - Expanded automated coverage for metadata, navigation, validation, and generated static output.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix(public-viewer): shell一覧のhydrationエラーを解消](https://github.com/digitaldemocracy2030/kouchou-ai/pull/938)

**作成者:** nishio  
**作成日:** 2026-09-09T07:13:21Z  
**変更:** +38 -3 (5ファイル)  
**マージ日:** 2026-09-09T07:30:11Z  
**内容:**

## 変更の概要

#935で追加したshell出力の一覧を初めて開くと、React #418（hydration mismatch）が発生し、ブラウザ側で画面を作り直していました。`build:shell`だけを`next build --webpack`へ切り替え、同じ操作でエラーが出ないようにします。

表示が回復すると既存の描画テストだけでは検出できないため、一覧の初回表示→詳細→一覧の操作中に`pageerror`がないことを確認するE2Eを追加します。viewerだけの変更でもE2Eが走るようworkflowのpathsも補います。

既存の静的exportのモバイルテストも、初期表示の階層リストで「全体」→「子要素を表示」を操作してからクラスタ名を確認するよう更新します。折りたたみ中の子クラスタが最初から見えるという前提をなくします。

## 変更の背景

元のTurbopack出力では5回中5回、一覧初回表示でエラーを再現。Reactがdivを期待した箇所にEmotionの`style data-emotion="css-global ..."`があることを確認しました。[Chakra UI公式の同症状の回避策](https://chakra-ui.com/docs/get-started/frameworks/next-app#hydration-errors-turbopack)に沿った変更です。Webpack出力では同じ5回の操作でエラーがありませんでした。

通常のbuild / build:static / devは変更しません。レポート別title・unlistedのnoindexは別の後続Issueで扱います。

## スクリーンショット

画面デザインの変更はありません。初期表示時の内部エラーを修正します。

## 関連Issue・PR

- #935 の検証で発見したエラーの修正
- 関連する配布方針: #885

## 動作確認の結果

- viewer Jest: 12 suites / 123 tests passed。
- shellビルド成功（Webpack、APIキー・API接続なし）。
- 同梱fixtureとローカルHTTP配信を使ったChromiumのshell E2E: 5 passed（既存4件＋追加1件）。ローカル用設定でshellだけを実行。
- 追加テストは元のTurbopack出力でReact #418を検出して失敗し、変更後のWebpack出力で成功することを確認。
- 通常static exportのモバイルE2E（root / subdir）: 2 passed。変更前のテストは階層リストが折りたたまれているため失敗し、操作追加後に成功。
- dummy-server事前検証: 4 passed。ローカルではworkspaceのNext 16.2.6を使用（dummy-server指定版はローカルキャッシュになし）。
- CIの全体E2E・通常ビルドはPRのチェックで確認します。

## CLAへの同意

- [ ] CLAの内容を読み、同意しました

## マージ前のチェック

- CIの成功を確認してからマージする。
- 実APIへのリクエストは行っていない。


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Improved mobile report-detail testing to verify list view selection and hierarchy expansion before displaying cluster information.
  * Added coverage to detect hydration errors while navigating between report lists and detail pages.

* **Tests**
  * Expanded end-to-end test coverage for public viewer changes.
  * Updated static shell builds to use the Webpack-based Next.js build process.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [chore(deps): bump next from 16.2.11 to 16.3.3 in /utils/dummy-server](https://github.com/digitaldemocracy2030/kouchou-ai/pull/937)

**作成者:** dependabot[bot]  
**作成日:** 2026-09-09T07:11:32Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2026-09-09T09:07:49Z  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 16.2.11 to 16.3.3.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v16.3.3</h2>
<p>This release contains security fixes for the following advisories:</p>
<p>Critical:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-p293-qw3h-jr36">Unauthenticated Remote Code Execution on windows-hosted servers</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-2xp9-vwfh-vxw4">Unauthenticated Remote Code Execution in Image Optimization API when AVIF files are used</a></li>
</ul>
<h2>v16.3.2</h2>
<blockquote>
<p>[!NOTE]
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>[backport] Scope app-entry export validation to files inside the app directory (<a href="https://redirect.github.com/vercel/next.js/issues/97357">#97357</a>)</li>
<li>[backport] Fix catch-all index page being served for every other slug (<a href="https://redirect.github.com/vercel/next.js/issues/97416">#97416</a>)</li>
<li>[16.3] Turbopack: don't trace embedded WASM loader helpers (<a href="https://redirect.github.com/vercel/next.js/issues/97353">#97353</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/97463">#97463</a>)</li>
<li>[16.3] Turbopack: retain conditions when replacing resolve request keys (<a href="https://redirect.github.com/vercel/next.js/issues/97453">#97453</a>)</li>
<li>[16.3.x] Fix Turbopack worker chunk loading with asset prefix (<a href="https://redirect.github.com/vercel/next.js/issues/97419">#97419</a>)</li>
<li>[16.3.x] Authenticate Turborepo remote caching with OIDC instead of a static PAT (<a href="https://redirect.github.com/vercel/next.js/issues/97603">#97603</a>)</li>
</ul>
<h3>Credits</h3>
<p>Huge thanks to <a href="https://github.com/lubieowoce"><code>@​lubieowoce</code></a>, <a href="https://github.com/unstubbable"><code>@​unstubbable</code></a>, <a href="https://github.com/timneutkens"><code>@​timneutkens</code></a>, <a href="https://github.com/mischnic"><code>@​mischnic</code></a>, and <a href="https://github.com/eps1lon"><code>@​eps1lon</code></a> for helping!</p>
<h2>v16.3.1</h2>
<h2>What's Changed</h2>
<ul>
<li>[16.x] Turbopack: don't strip async-module runtime from shared runtime chunks by <a href="https://github.com/lukesandberg"><code>@​lukesandberg</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/96653">vercel/next.js#96653</a></li>
<li>[16.x] [turbopack] Add <code>turbopack_ecmascript</code> and <code>turbopack_wasm</code>'s embeded FS to <code>internal_assets_conditions</code> by <a href="https://github.com/lukesandberg"><code>@​lukesandberg</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/96655">vercel/next.js#96655</a></li>
<li>[16.x] [turbopack] Collapse nested promises in the analyzer by <a href="https://github.com/sampoder"><code>@​sampoder</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/96675">vercel/next.js#96675</a></li>
<li>[16.x] fix(next/image): preserve image response after optimization by <a href="https://github.com/styfle"><code>@​styfle</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/96733">vercel/next.js#96733</a></li>
<li>[16.3.x] Default deploy e2e tests to the repo next version by <a href="https://github.com/eps1lon"><code>@​eps1lon</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/96900">vercel/next.js#96900</a></li>
<li>[backport] Bump <code>@​swc/helpers</code> by <a href="https://github.com/mischnic"><code>@​mischnic</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/96885">vercel/next.js#96885</a></li>
<li>[backport] [turbopack] Raise registration calls in hoisted modules to the top by <a href="https://github.com/lukesandberg"><code>@​lukesandberg</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/97308">vercel/next.js#97308</a></li>
<li>[backport] Fix missing styled-jsx styles in Pages Router SSR on adapter builds by <a href="https://github.com/lukesandberg"><code>@​lukesandberg</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/97302">vercel/next.js#97302</a></li>
<li>[backport] [turbopack] Fix HMR for dynamic imports evaluated from layouts by <a href="https://github.com/lukesandberg"><code>@​lukesandberg</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/97317">vercel/next.js#97317</a></li>
<li>[backport] Restore the live <code>headers()</code> view of the incoming request by <a href="https://github.com/unstubbable"><code>@​unstubbable</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/97311">vercel/next.js#97311</a></li>
<li>[backport] Allow literal exports in <code>'use cache'</code> files by <a href="https://github.com/unstubbable"><code>@​unstubbable</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/97312">vercel/next.js#97312</a></li>
<li>[backport] Keep the dev validation worker alive across HMR updates by <a href="https://github.com/unstubbable"><code>@​unstubbable</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/97315">vercel/next.js#97315</a></li>
<li>[backport] Discard only cache entries that predate a tag revalidation, and reuse completed entries by <a href="https://github.com/unstubbable"><code>@​unstubbable</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/97314">vercel/next.js#97314</a></li>
<li>[backport] Encode the cache item name built by <code>unstable_cache</code> by <a href="https://github.com/unstubbable"><code>@​unstubbable</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/97313">vercel/next.js#97313</a></li>
<li>[16.3] [ci] Use OIDC tokens to read private preview builds by <a href="https://github.com/eps1lon"><code>@​eps1lon</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/97258">vercel/next.js#97258</a></li>
<li>[backport] [test] Compile the middleware redirect routes up front in dev by <a href="https://github.com/lukesandberg"><code>@​lukesandberg</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/97328">vercel/next.js#97328</a></li>
<li>[backport] Fix Nav Inspector request loop on repeat captures by <a href="https://github.com/acdlite"><code>@​acdlite</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/97326">vercel/next.js#97326</a></li>
<li>[backport] Fix: Optimistic routing bugs leading to repeated prefetch loops by <a href="https://github.com/acdlite"><code>@​acdlite</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/97325">vercel/next.js#97325</a></li>
<li>[backport] Retain fewer stale cache versions and use a TTL, plus the mtime fallback by <a href="https://github.com/lukesandberg"><code>@​lukesandberg</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/97304">vercel/next.js#97304</a></li>
<li>[backport] Revert i18n localization change for dynamic Pages API routes (<a href="https://redirect.github.com/vercel/next.js/issues/94905">#94905</a>) by <a href="https://github.com/gaojude"><code>@​gaojude</code></a> in <a href="https://redirect.github.com/vercel/next.js/pull/97330">vercel/next.js#97330</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/vercel/next.js/compare/v16.3.0...v16.3.1">https://github.com/vercel/next.js/compare/v16.3.0...v16.3.1</a></p>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/a9a1cb7859f178f830ad3773b303130c21b19586"><code>a9a1cb7</code></a> v16.3.3</li>
<li><a href="https://github.com/vercel/next.js/commit/968b9fcb26bdeb8e0a861a9df05361474666d51b"><code>968b9fc</code></a> [16.3.x] Fix ISR misses with backslashes in segments when deployed on Windows</li>
<li><a href="https://github.com/vercel/next.js/commit/3a15b4ac6ac8e70b1a9b18ecc18e8434462899b3"><code>3a15b4a</code></a> [16.3.x] [next/image]: disable avif image optimization</li>
<li><a href="https://github.com/vercel/next.js/commit/7378b51ea05a6745d3676bee00cb4c63aac3dd16"><code>7378b51</code></a> Backport/docs fixes 16.3 (<a href="https://redirect.github.com/vercel/next.js/issues/97649">#97649</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/528c1cdfc36bdf8051992febdafe45f17f042010"><code>528c1cd</code></a> [16.3.x] Stop generating error codes (<a href="https://redirect.github.com/vercel/next.js/issues/97780">#97780</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/d0ac8828c2fe6026dd7d700488bfd8289711fde6"><code>d0ac882</code></a> v16.3.2</li>
<li><a href="https://github.com/vercel/next.js/commit/81deb92859e26f8435cc0f37e244573c6638a955"><code>81deb92</code></a> [16.3.x] Authenticate Turborepo remote caching with OIDC instead of a static ...</li>
<li><a href="https://github.com/vercel/next.js/commit/cd714d9fceae7aec9d467598792b0c844f710607"><code>cd714d9</code></a> [16.3.x] Fix Turbopack worker chunk loading with asset prefix (<a href="https://redirect.github.com/vercel/next.js/issues/97419">#97419</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/5ac2327e62784eacdf6ab7db8629fd05c5f5fcdf"><code>5ac2327</code></a> [16.3] Turbopack: retain conditions when replacing resolve request keys (<a href="https://redirect.github.com/vercel/next.js/issues/97453">#97453</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/0ccb3e7f5d6b55c5c9e215248b264a428aee7dcb"><code>0ccb3e7</code></a> [16.3] Turbopack: don't trace embedded WASM loader helpers (<a href="https://redirect.github.com/vercel/next.js/issues/97353">#97353</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/97463">#97463</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/vercel/next.js/compare/v16.2.11...v16.3.3">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=16.2.11&new-version=16.3.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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

### [docs: export ビルドで OGP 画像が生成されない点を訂正 (#885)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/936)

**作成者:** yasumorishima  
**作成日:** 2026-09-09T02:30:35Z  
**変更:** +6 -3 (1ファイル)  
**マージ日:** 2026-09-09T07:10:09Z  
**内容:**

# 変更の概要

`docs/development/web-ui-node-runtime-dependencies.md`（#903 で追加）の記述を訂正します。

同ドキュメントは「export 時は `app/[slug]/opengraph-image.png/route.ts` がビルド時に静的 PNG を書き出す」と書いていましたが、実際には **export ビルドではレポートごとの OGP 画像は生成されません**。

`apps/public-viewer/scripts/rename-file.mjs` は `NEXT_PUBLIC_OUTPUT_MODE=export` のとき、`app/[slug]/opengraph-image.tsx` と `app/[slug]/opengraph-image.png`（route ディレクトリ）の**両方**を `_` 付きへ改名し、Next の private folder 規約でビルド対象から外します（`prebuild:static` で改名し `postbuild:static` で復元）。

その結果、`app/[slug]/page.tsx` が export 時にだけ設定する `openGraph.images: ["${slug}/opengraph-image.png"]` は、生成されないファイルを指しています。

このドキュメントを書いたのは私（#903）で、実挙動を確かめずに route の存在から推測して書いてしまいました。誤った前提が残ると #885 の判断材料として害になるため訂正します。

# スクリーンショット

UI の変更はありません。

# 変更の背景

#885 の作業で export の挙動を追っていた際に、記述と実挙動の食い違いに気付きました。

# 関連Issue

- #885
- #903（この訂正の対象を追加した PR）

# 動作確認の結果

`apps/public-viewer` の複製に対して改名スクリプトを実際に実行し、除外されるファイルを確認しました。

```
$ NEXT_PUBLIC_OUTPUT_MODE=export node scripts/rename-file.mjs rename
Renamed: app/[slug]/opengraph-image.tsx → _opengraph-image.tsx
Renamed: app/[slug]/opengraph-image.png → _opengraph-image.png
```

改名後の `app/[slug]/` には `_opengraph-image.png` / `_opengraph-image.tsx` が残り、ルーティング対象の OGP 生成経路が無くなります。あわせて `opengraph` を含む参照をリポジトリ全体で検索し、他に PNG を生成する経路が無いことも確認しました（`rename-file.mjs` / `page.tsx` の `openGraph.images` / 当該ドキュメントのみ）。

ドキュメントのみの変更のため、アプリの動作確認は行っていません。

# CLAへの同意

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

🤖 Generated with [Claude Code](https://claude.com/claude-code)


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Documentation**
  * Corrected documentation describing OGP image handling for public viewer pages.
  * Clarified that OGP images are not generated in export builds.
  * Updated runtime and route details to accurately reflect Node-specific behavior.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat(public-viewer): データ非依存な静的出力 (shell ビルド) を追加 (#885)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/935)

**作成者:** yasumorishima  
**作成日:** 2026-09-09T02:25:57Z  
**変更:** +829 -50 (17ファイル)  
**マージ日:** 2026-09-09T07:10:04Z  
**内容:**

# 変更の概要

静的出力をレポートに依存しない形にする **shell ビルド**（オプトイン）を追加します。

現在の static export は、ビルド時に API からレポート一覧と本文を取得して HTML に焼き込みます。そのためレポートが増減するたび `next build` が必要で、`apps/static-site-builder` が `POST /build` のたびに `pnpm run build:static` を子プロセス起動しています。

shell ビルドでは、レポートに依存しない HTML を **1 ルート（`__shell__`）だけ**出力します。配布時にはその 1 枚を各レポートの slug へコピーし、本文は `data/*.json` として並べます。ページは実行時に URL から slug を求めて JSON を読むため、静的アセットは**リリース時に一度ビルドすれば済み**、パッケージング（コピー＋JSON 書き出し＋zip）は Node を使わずに実装できます。

- `NEXT_PUBLIC_STATIC_SHELL=1`（`NEXT_PUBLIC_OUTPUT_MODE=export` を含意）でのみ有効
- shell 時は `generateStaticParams` / `generateMetadata` / ページ本体が API を参照しません
- レポート詳細・一覧の JSX は `ReportView` / `ReportListView` に切り出し、既存のサーバー版と shell 版で共有しています（画面が乖離しないように）
- E2E に `client-static-shell` プロジェクトを追加し、**コピーした HTML を実ブラウザで開いて描画されること**まで確認しています

issue #885 の方向 2・3 の土台にあたる部分です。段階的に進める想定で、この PR は public-viewer のみを対象にしています（次段は FastAPI 側のパッケージング、その次に `static-site-builder` の退役）。

# スクリーンショット

shell ビルドの出力を各 slug へコピーして配信したときの実画面です（E2E の `client-static-shell` プロジェクトで撮影）。既存モードの画面は変更していません。

**レポート詳細**（shell 出力を `/test-report-1/` へコピーして配信し、`data/reports/test-report-1.json` から描画）

![レポート詳細](https://raw.githubusercontent.com/yasumorishima/oss-contributions/main/assets/kouchou-ai-885/shell-report-detail.png)

**レポート一覧**（`data/reports.json` から描画）

![レポート一覧](https://raw.githubusercontent.com/yasumorishima/oss-contributions/main/assets/kouchou-ai-885/shell-report-list.png)

**同梱データの無い slug**（`/test-report-2/`）

![見つかりません](https://raw.githubusercontent.com/yasumorishima/oss-contributions/main/assets/kouchou-ai-885/shell-not-found.png)

# 変更の背景

issue #885 では「runtime Node なしを本気で狙うなら、public-viewer の事前ビルド済み assets で完結する方式、または Python 側の静的レポート生成方式を検討する」と整理されています。

現状の構造を追うと、単一実行ファイル配布で Node が実行時に残る主因は **静的出力がビルド時にデータと結合していること**でした。

- `app/[slug]/page.tsx` の `generateStaticParams` が `fetch(${getApiBaseUrl()}/reports)` でレポート一覧を取得し、`getStaticBuildReportSlugs` が `status === "ready"` の slug を列挙する
- `generateMetadata` とページ本体も `/meta/metadata.json` と `/reports/<slug>` を参照する
- したがって出力はその時点のレポート集合に固有になり、増減のたびに再ビルドが必要になる
- そのために `apps/static-site-builder/src/index.ts` がリクエストごとに `execAsync("pnpm run build:static")` を実行している

ここを切れば、実行時の Node だけでなく「ビルドに API 到達が必要」という制約も外れます。

# 関連Issue

- #885

# 動作確認の結果

fork の GitHub Actions で実行しました（すべて自動テスト・secrets 不要）。

1. **shell ビルドがレポートに依存しないこと**（`client build` ワークフロー）
   - 既存の static export と**同じフィクスチャ API に到達できる状態**で `build:shell` を実行し、`out/__shell__/index.html` が出力される一方で `out/example`（フィクスチャのレポート由来ルート）が生成されないことを確認
   - さらに `out/index.html` と `out/__shell__/index.html` にフィクスチャのレポート本文が含まれないことを確認（API を見せない状態で通しても検査にならないため、到達可能な状態で確認しています）
2. **既存モードが壊れていないこと**
   - 同ワークフローの通常ビルド（`build`）、static export（`build:static`）、Docker ビルドがいずれも成功
   - E2E 全体で **77 passed / 0 failed**（`client` / `client-static-root` / `client-static-subdir` / `admin` を含む）
3. **配布物が実ブラウザで動くこと**（E2E `client-static-shell`）
   - shell 出力を各 slug へコピーして http-server で配信し、`/test-report-1/` で当該レポートが描画されること
   - 生成された HTML にビルド時のレポート本文が焼き込まれていないこと
   - 同梱データの無い slug（`/test-report-2/`）で「ページが見つかりませんでした」が表示されること
   - トップページが `data/reports.json` からレポート一覧を描画すること
4. **単体テスト**（`Client Tests`）
   - URL からの slug 導出（basePath 付き・`index.html` 付き・前方一致だけの basePath を剥がさないこと）、同梱データ URL の組み立て、404 と通信失敗の切り分け、オプトイン判定を追加

## 把握している制約（この PR では対応していません）

- **OGP 画像**: shell では個別レポートの OGP 画像は付きません。もっとも export ビルドでは現在も生成されていません（`scripts/rename-file.mjs` が `opengraph-image.tsx` と `opengraph-image.png` の両方を除外するため）。この点は別途 docs の訂正 PR を出します。
- **`<title>` と `noindex`**: shell では HTML がレポート非依存になるため、レポートごとの `title` と unlisted の `noindex` が付きません。配布時に head を差し替えるか、実行時に注入するかは次段の課題と考えています。
- **client bundle**: `NEXT_PUBLIC_STATIC_SHELL` 未設定時も shell 用コンポーネントがバンドルに含まれる可能性があります（挙動は変わらないことを E2E で確認済み。バンドルサイズの実測はしていません）。
- **E2E の発火条件**: `e2e-tests.yml` の `paths` に `apps/public-viewer/**` が無いため、viewer だけを変更した PR では shell の E2E が走りません。この PR では workflow の発火条件は変更していません。
- basePath 付きの shell 配布と、レポート間のクライアント遷移は E2E で未検証です。

# CLAへの同意

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

🤖 Generated with [Claude Code](https://claude.com/claude-code)


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Added a static shell build that renders report lists and details from bundled data at runtime.
  * Added loading, not-found, and data-error states with clearer failed-data URL reporting.
  * Added support for bundled reporter metadata and images.
  * Added reusable report list and detail rendering across standard and shell views.

* **Tests**
  * Added end-to-end coverage for shell navigation, rendering, missing data, and build-time data isolation.
  * Added validation that shell output excludes report-specific content.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix(llm): make OpenAI Flex Processing work for GPT-5/6 and harden it (#917 follow-up)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/934)

**作成者:** tokoroten  
**作成日:** 2026-09-08T21:52:05Z  
**変更:** +417 -43 (5ファイル)  
**マージ日:** 2026-09-09T06:41:25Z  
**内容:**

## 概要

#917 (OpenAI Flex Processing) の検証で見つかった問題を修正した版です。#917 のコミット 2 件を含んでいるので、本 PR をマージすれば #917 は不要になります（Closes #916 / #917 を置き換え）。

## 背景（#917 検証で見つかった問題）

1. **GPT-5/6 系・o 系は `temperature=0` を 400 で拒否する**
   `Unsupported value: 'temperature' does not support 0 with this model.`
   カタログにある `gpt-5.6-terra` / `gpt-5.6-luna` / `o3-mini` は、Flex 以前に呼び出し自体が失敗していました（#912 の内容）。
2. `"gpt-5" in model` の部分一致なので、Flex 非対応の `gpt-5-pro` / `gpt-5-chat-latest` / `gpt-5-codex` 等にも Flex が付いていた。
3. OpenAI が Flex に推奨する約 15 分のタイムアウトに対し、既定 300 秒のままだった。Flex 混雑時の 429 (`resource_unavailable`) への対処もなかった。
4. 新規テストが開発環境の `OPENAI_USE_FLEX` に影響される。
5. `OPENAI_USE_FLEX` がドキュメント・`.env.example` に無い。

## 変更

- GPT-5/6 系と o1/o3/o4 系では `temperature` を送らない（`seed` は送る。実 API で受理を確認）。
- Flex 対象を `gpt-5*` / `gpt-6*` の基本モデルと `o3` / `o4-mini` に限定し、`pro` / `chat` / `codex` / `realtime` / `audio` / `search` / `transcribe` / `tts` / `image` を含む派生は除外。
- Flex 利用時は `OPENAI_FLEX_TIMEOUT_SECONDS`（既定 900 秒）と `LLM_REQUEST_TIMEOUT_SECONDS` の大きい方を使う。
- Flex で 429 が返ったら `service_tier=auto` で 1 回だけ再送してから、従来のリトライに委ねる。
- `request_to_openai` のペイロード構築を `_build_openai_chat_payload` に集約（通常 / `beta.parse` の両経路で同じ挙動）。
- テスト: 環境変数を隔離する fixture を追加し、モデル判定・env 上書き・Pydantic 経路・タイムアウト・フォールバックを追加（`test_llm.py` 70 件 pass）。
- ドキュメント: `docs/development/openai-flex-processing.md` を新設、`.env.example` と `llm-timeout.md` に追記。

Azure / OpenRouter 経路は変更していません。

## 検証

- `apps/api` pytest: `test_llm.py` 70 passed。API 全体 255 passed / 2 failed（失敗 2 件は Windows 固有のパス・cp932 問題で本 PR と無関係、main でも同様）。
- 実 API（修正後の `request_to_openai` 経由）:

| model | 経路 | 結果 |
|---|---|---|
| gpt-5.6-terra | plain / json_object / Pydantic | OK, response.service_tier = `flex`, timeout 900 |
| gpt-5-mini | Pydantic | OK, `flex` |
| o3-mini | plain | OK, `default`（temperature 省略） |
| gpt-4o-mini | Pydantic | OK, `default`, temperature=0 のまま |

修正前は gpt-5.6-terra / o3-mini が全経路で 400 でした。

Closes #916
Refs #912 #917

🤖 Generated with [Claude Code](https://claude.com/claude-code)


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **New Features**
  - Added OpenAI Flex Processing support for compatible models, with automatic selection or environment-based control.
  - Added configurable Flex-specific request timeouts.
  - Added fallback to standard processing when Flex capacity is unavailable.

- **Bug Fixes**
  - Improved handling of reasoning-model requests by omitting unsupported temperature settings.

- **Documentation**
  - Documented Flex Processing behavior, configuration, timeout handling, model support, and fallback and retry behavior.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (6件)

### [feat: レポート別に濃いクラスタの初期値を保存する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/946)

**作成者:** nishio  
**作成日:** 2026-09-09T09:47:24Z  
**変更:** +236 -7 (6ファイル)  
**内容:**

# 変更の概要
管理画面の可視化設定に、濃いクラスタの上位割合（%）と最小サンプル数の入力欄を追加しました。既存の設定保存APIへ接続し、レポートを開いたときのviewer初期値に反映します。

# 変更の背景
viewerはレポート別の閾値を読めましたが、管理画面から編集できませんでした。他の可視化設定を保持して保存し、割合の範囲外・負数・件数の小数・空欄を拒否します。取得失敗時に既存設定をデフォルトで上書きすることも防ぎます。狭い画面ではダイアログ内をスクロールできます。

# 関連Issue
Closes #55

# 動作確認の結果
- 管理画面Jest: 24 suites / 163件成功。新規9件は保存・再表示、他設定の保持、入力検証、未設定・取得失敗を検証。
- API統合テスト6件成功。PATCH→管理APIで再読込→公開APIでの反映と、不正値で保存内容が変わらないことを確認。
- ローカルの実形状fixture APIで、ブラウザから35%・7件を保存→再表示→公開viewerの設定に35%・7件が出ることを確認。375px幅の保存操作も確認。API永続化は上記の実ルーター統合テストで別途検証しています。
- Ruff、Biome、diff check成功。

通常staticは再出力、shellは更新後の公開JSONによる再組立が必要です。閲覧中に変えた値を管理設定へ自動保存する変更ではありません。


**コメント:** なし

---

### [fix: Azure接続確認の失敗時に設定の確認先を案内](https://github.com/digitaldemocracy2030/kouchou-ai/pull/945)

**作成者:** nishio  
**作成日:** 2026-09-09T09:43:39Z  
**変更:** +60 -2 (7ファイル)  
**内容:**

# 変更の概要
AzureのAPI接続確認が失敗した場合に、APIバージョンとモデルバージョンの違い、およびエンドポイント・デプロイ名・キーの確認先を表示します。作成前確認とAI詳細設定の接続チェックの両画面を対応させました。

# 変更の背景
Azure設定を誤ったときに「設定や接続を確認」の一般的な案内だけでは、どこを直せばよいか分かりませんでした。原因をAPIバージョンの誤りと断定せず、確認する項目を示します。認証・quota・rate limitの既存の専用表示は維持します。例外の生の内容や設定値は返しません。

# 関連Issue
Refs #592。管理画面の事前接続確認を改善するPRです。分析実行中の例外の扱いやAzure実環境での確認は残件のため、Issueは閉じません。

# 動作確認の結果
- APIルーターテスト23件成功。Azureの400・404・接続失敗・設定例外に対する案内と、例外詳細を返さないことを確認。
- 画面の単体テスト27件成功。両方の接続確認でAzure向け案内が表示されることを確認。
- Ruff、Biome、diff check成功。実Azureには接続していません。


**コメント:** なし

---

### [docs: 公開前に確認する作成者・規約リンクを案内](https://github.com/digitaldemocracy2030/kouchou-ai/pull/944)

**作成者:** nishio  
**作成日:** 2026-09-09T09:42:39Z  
**変更:** +39 -0 (1ファイル)  
**内容:**

# 変更の概要
公開前の確認表を使い方ガイドに追加しました。作成者・プライバシーポリシー・利用規約・メニュー・フッターの現在の設定場所と表示条件、配布済み静的サイトへの反映方法を案内します。

# 変更の背景
リンクを変更し忘れたまま公開しないよう、metadataで変更できる項目とソース中のリンクを区別しました。現在の標準メニューにはテスト環境へのリンクがないため、古いIssueの前提をそのまま案内せず、独自追加分の確認として扱います。

# 関連Issue
Closes #393

# 動作確認の結果
- 現行のmeta router、ReporterContent、Footer、GlobalNavigationと案内を照合。
- customファイルの実パス、default時のリンク非表示、isDefaultはAPI側で付与する挙動を確認。
- diff check成功。ドキュメントbuildはCIで確認します。


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **Documentation**
  - Added a user guide section explaining how to verify links before publishing reports.
  - Documented configuration locations for reporter details, introductory text, web pages, policies, menus, and footer links.
  - Explained fallback behavior between custom and default metadata.
  - Added a JSON configuration example and a pre-publication checklist covering metadata, link accessibility, mobile menus, and static exports.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [test: 作成前のAPI接続エラーから復帰するE2Eを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/943)

**作成者:** nishio  
**作成日:** 2026-09-09T09:20:21Z  
**変更:** +91 -24 (5ファイル)  
**内容:**

# 変更の概要
作成前確認でAPI接続に失敗したとき、エラーを表示し、設定へ戻って入力を修正し、再確認できるE2Eを5ケース追加しました。従来の実行されないAPIエラーテストを置き換えています。

# 変更の背景
#395の優先課題は、認証失敗・残高不足・通信失敗を単体テストだけでなくブラウザの操作経路で確認することでした。Server Actionからのリクエストはpage.routeでは捕捉できないため、ダミーAPIでリクエストごとにエラーを返します。

- テスト専用キーで認証・quota・rate limit・HTTP 503・ストリーム切断を再現。E2E_TEST=true限定で、実LLMへの通信はありません。
- 確認画面のエラー表示、設定とCSVの保持、キー変更後の未確認状態へのリセット、再確認の成功までを検証。
- dummy-server変更でもE2Eが発火するようworkflowのpathsを補足。

# 関連Issue
Refs #395。優先のエラー復帰経路を実装しました。Spreadsheetの取得・列選択とAI詳細設定の最終送信内容の検証は後続のため、Issueは閉じません。

# 動作確認の結果
- dummy-serverの事前検証4件成功。
- 新しいブラウザE2E5件成功。ストリーム切断時にはServer Actionのfetchが実際にSocketErrorで失敗することを確認。
- 変更TSのBiome・diff check成功。
- 全体CI成功。E2Eは86 passed / 2 skipped。

画面の実装変更はありません。実プロバイダーでの認証・残高検出自体はこのE2Eの範囲外です。


## ローカル回帰確認

新規5ケースに加え、既存の作成・複製E2E15件も成功しました。


**コメント:** なし

---

### [ci: 静的viewerの確認用成果物をダウンロード可能にする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/942)

**作成者:** nishio  
**作成日:** 2026-09-09T09:17:53Z  
**変更:** +45 -0 (3ファイル)  
**内容:**

# 変更の概要
client buildの静的exportを、コミットSHA付きのダウンロード成果物として7日間保存します。Nodeで再ビルドせずにローカルHTTPサーバーで閲覧できるよう、取得・閲覧手順を追加しました。

# 変更の背景
静的exportのCIビルドは既にありますが、成果物が残らず、画面を確認するには手元でビルドし直す必要がありました。既存のfixtureだけを使い、実環境のデータやAPIへ接続しません。workflow自身の変更でもCIが起動するようpathsを追加しています。

# 関連Issue
Refs #518。自動ビルド済み成果物の取得を先に実装します。GitHub Pages等の常設URLへの公開は後続のため、Issueは閉じません。

# 動作確認の結果
- 出力のindex.htmlとexample/index.htmlの存在を確認してからアップロードします。
- artifactにはBUILD_COMMIT.txtを同梱し、PRの検証用merge commitと先端SHAの違いもドキュメントに記載。
- diff check成功。CI実行後にartifactを取得して内容を確認します。


## CI・成果物の確認結果

CI成功。artifactを実際に取得し、BUILD_COMMIT.txt（検証merge commit 39c9183）、HTTP配信での一覧→詳細とタイトル表示を確認しました。通常static出力では一覧初回にReact #418を1件観測しています。表示・遷移は成功していますが、実行時エラーなしとはしていません。本PRはviewerやbuild方式の変更を含みません。


**コメント:** なし

---

### [docs: コードを書かない人の貢献方法と投稿先を案内](https://github.com/digitaldemocracy2030/kouchou-ai/pull/941)

**作成者:** nishio  
**作成日:** 2026-09-09T09:17:50Z  
**変更:** +32 -1 (3ファイル)  
**内容:**

# 変更の概要
コードを書かずに参加したい人が、感想・質問・事例共有・動作確認・A/B比較などの最初の一歩と投稿先を選べる表を追加しました。感想の記入例と、README・ドキュメントトップからの入口も追加しています。

# 変更の背景
Issueに集まった貢献方法がガイドへ反映されておらず、非エンジニアが具体的に何をすればよいか分かりにくい状態でした。CONTRIBUTING.mdを編集元とし、公開docsは既存の生成処理で反映します。

# 関連Issue
Closes #130

# 動作確認の結果
- 既存Issueの提案と案内の対応、投稿先、相対リンク、diff checkを確認。
- UIコードの変更なし。公開ドキュメントのビルドはCIで確認します。


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **Documentation**
  - Added guidance for non-code contributions, including feedback, questions, use cases, testing, comparisons, and experience sharing.
  - Added templates and submission advice covering privacy and API-key precautions.
  - Updated contributor and documentation guides with links to the new participation guidance.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

