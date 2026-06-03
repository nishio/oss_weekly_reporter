# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-05-27T13:36:48.015427+09:00 から 2026-06-03T13:36:48.015427+09:00 まで

## Issues

### 過去7日間に完了されたissue (4件)

### [[BUG] 以前のバージョンで作成したレポートの散布図の表示時に "WebGL is not supported" というメッセージが出る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/886)

**作成者:** shingo-ohki  
**作成日:** 2026-05-31T22:52:17Z  
**内容:**

### 概要
以前の version で作成したレポートの散布図が表示されずに、
`WebGL is not supported by your browser...`
というメッセージが出る。

https://public-viewer.wittyisland-cc57c95f.japaneast.azurecontainerapps.io/6120b19e-56c4-4248-a374-9370f0e96944/
<!-- バグの簡潔な説明をお願いします -->

### 期待する動作
散布図が表示される

### スクリーンショット・ログ

<img width="810" height="838" alt="Image" src="https://github.com/user-attachments/assets/0502a93e-3766-4a46-a1f1-c32ffa5cea6f" />

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->

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

~`fetch_reports.py` を通常の deploy / update 手順から外し、migration または緊急救済時だけ使う補助ツールとして位置づけ直す。~

話がややこしくなるので削除でいいのではないか

別途、環境構築後にAzure Blob Storageの読み書きが正しく動いているかをテストで検証すべき

## 関連

- 旧 issue: #629
- deploy safety 側の再設計: 別 issue で Blob Storage health check へ切り替えを扱う


**コメント:** なし

---

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

### 過去7日間に作成されたissue (9件)

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

### [[FEATURE] レポート作成前に入力・コスト・API状態を確認できるパネルを追加する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/884)

**作成者:** nishio  
**作成日:** 2026-05-29T10:51:42Z  
**内容:**

## 背景

`#221` の「試行錯誤の負担を減らす」を、実装可能な単位へ落とすための tracking issue です。

現状の作成画面には、CSV / Spreadsheet / plugin から送信前に `comments` を組み立てる処理があり、コメント数が第2階層クラスタ数を下回る場合だけ `window.confirm` で確認しています。一方で、ユーザーが本当に知りたい「この入力をこの設定で実行して大丈夫か」は、入力件数、コメント列、クラスタ数、概算時間、概算コスト、API key / billing / quota の状態が分散していて、作成開始前に判断しにくい状態です。

## 目的

作成開始前に、ユーザーが次の不安をまとめて確認できるようにします。

- 入力データは意図した列・件数で読めているか
- 現在のクラスタ数は入力件数に対して無理がないか
- API key / billing / quota は実行できる状態か
- 実行時間と費用は大まかにどの程度か
- 大きい入力では、いきなり全件実行せず sample-first / reuse を検討すべきか

## 下位 Issue の整理

この issue は次の issue を束ねます。ただし PR で自動 close するかは、各 issue の完了条件を満たした時点で個別に判断します。

| Issue | 扱い |
|---|---|
| #221 | 親テーマ。試行錯誤負担削減の umbrella として残す |
| #11 | 作成前・実行中の時間目安。まずは粗い時間帯を作成前確認に入れる |
| #79 | CSV / Spreadsheet / plugin 入力の概算コスト表示。最初は精密計算ではなく粗い費用帯でよい |
| #292 | OpenAI API 課金設定 / ChatGPT Plus との混同。作成前確認内で billing / quota check と docs 導線を出す |
| #391 | API key / quota / rate limit の preflight。既存 `/admin/environment/verify` を作成前フローへ統合する |
| #97 | CSV フォーマット・コメント列・件数の不安。作成前確認で選択列、非空件数、クラスタ数との関係を見せる |
| #19 | 既に close 済み。再利用機能は存在するため、大規模入力や再実行時の導線として活用する |
| #877 | 隣接テーマ。Windows setup の導入摩擦であり、この issue の主対象である「アプリ起動後の分析実行前確認」とは分ける |

## Tracking checklist

- [ ] #11 時間目安を作成前確認へ入れる
- [ ] #79 費用帯を作成前確認へ入れる
- [ ] #292 API課金設定の混同を UI / docs 導線で減らす
- [ ] #391 API key / quota / rate limit preflight を作成前フローへ統合する
- [ ] #97 入力列・非空件数・クラスタ数との関係を作成前に確認できるようにする
- [ ] #221 sample-first / reuse 導線を検討する

## 最初の実装スライス

まずは `apps/admin/app/create/page.tsx` の既存 `window.confirm` を、作成前確認パネル / ダイアログに置き換えます。

最小要件:

- CSV / Spreadsheet / plugin のどの入力経路でも、送信前に同じ確認パネルを通る
- コメント件数、選択コメント列、選択属性列、クラスタ数、provider / model を表示する
- 既存の「コメント数 < 第2階層クラスタ数」警告を、パネル内の警告として表示する
- API接続チェックの状態を表示する
  - 未確認
  - OK
  - 認証エラー
  - 残高不足 / quota 不足
  - rate limit
  - 不明なエラー
- コスト / 時間見積もり欄を用意する
  - 最初は「目安なし」でもよい
  - 入れる場合は、精密な金額ではなく粗い帯にする

## 後続スライス

- `#11/#79`: コメント件数・文字数・model から coarse time / cost bucket を出す
- `#292/#391`: `/admin/environment/verify` を作成前確認パネルから呼び出し、失敗時に actionable message を出す
- `#97`: 非空コメント数、短すぎる行、コメント列推定の信頼度など、入力確認を増やす
- `#221`: 大規模入力時の sample-first / reuse 導線を設計する

## 非目標

- 初回から精密な費用予測を作ること
- 自動で勝手にサンプリングして実行件数を減らすこと
- Windows setup guide の整理までこの issue に含めること
- すべての provider の pricing を完全に最新化すること

## 完了条件

- 作成開始前に、入力・クラスタ数・AI設定・API状態・費用/時間目安を一箇所で確認できる
- 既存の `window.confirm` より情報量が多く、キャンセルして設定を直す理由が分かる
- 下位 issue のうち、どこまでがこの issue の PR で満たされたかをコメントで整理できる

## 参考

- #221
- #11
- #79
- #292
- #391
- #97


**コメント:** なし

---

### [[EXPERIMENT] KJ法的プロンプトがラベル品質に効くか比較実験する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/882)

**作成者:** nishio  
**作成日:** 2026-05-29T08:49:08Z  
**内容:**

## 背景

広聴AIでは、KJ法や「表札」の考え方をラベリング prompt に取り入れると品質が上がるのではないか、という議論がある。

ただし、KJ法的な言葉を prompt に入れることが本当にラベル品質を改善しているのかは、まだ比較実験として切り分けられていない。方法論としての KJ法が有用であることと、prompt に KJ法的な指示を書くことが有効であることは別問題なので、採用判断の前に比較したい。

## 提案内容

同一のクラスタリング結果・同一の入力データを使い、KJ法的プロンプトの有無でラベル品質を比較する。

比較候補:

- baseline: 現行の `hierarchical_initial_labelling` / `hierarchical_merge_labelling` prompt
- KJ prompt: 「表札」「KJ法的に、混沌から意味を立ち上げる」などの指示を入れた prompt
- neutral structured prompt: KJ法という語は使わず、代表性・カバレッジ・短さ・隣接クラスタとの差別化だけを明示した prompt
- optional: KJ prompt + label refinement の組み合わせ

## 固定したい条件

- clustering / hierarchy は同一にする
- sampling 条件を固定する。可能なら `sampling_num=10` と全件投入の両方で見る
- model / temperature / seed 相当の条件を揃える
- コストと token 量も記録する
- OpenAI judge だけに依存せず、Claude judge または人間 judge 用の bundle を作る

## 評価観点

- クラスタ内の主要 2〜3 軸を落とさずカバーしているか
- 代表意見本文とラベルが噛み合っているか
- 隣接クラスタと区別しやすいか
- 短く読みやすいが、抽象化しすぎていないか
- 「整ったが中身とずれたラベル」を増やしていないか

## 完了条件

- baseline / KJ prompt / neutral structured prompt の比較結果が残っている
- KJ法的プロンプトが有効だったのか、単に構造化された指示が効いたのか、不明だったのかを結論として書ける
- 有効だった場合は prompt 更新または experimental mode としての扱いを提案する
- 有効でなかった場合は、KJ法は prompt 技法ではなく product 設計原則として扱う、という整理を残す

## 関連

- #881: ラベル品質改善の実験・議論を追跡可能にする

**コメント:** なし

---

### [[analysis-core] ラベル品質改善の実験・議論を追跡可能にする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/881)

**作成者:** nishio  
**作成日:** 2026-05-29T08:48:48Z  
**内容:**

## 背景

ラベル品質の改善について、実験・judge・人間判断・設計論点が Slack / developer-wiki / WIP branch / Issue に散らばっている。

既存の `#869` は label refinement を PR 化するための作業整理だが、品質改善として何を検証し、何を採用判断の根拠にするかは別途追跡できるようにしたい。

## 現在の論点

- label refinement は現状 `current_label / current_description / children labels` を polish する step で、代表意見本文を見ていない。上流ラベルが誤っている場合、綺麗な誤ラベルを固定化するリスクがある。
- `none / setwise / contrast / balanced` の比較では、読みやすさが改善しても代表性やカバレッジが落ちるケースがあり、OpenAI judge だけでは判断しにくい。
- 人間判断としては、ラベルは「目次」ではなく「クラスタ要約」として扱い、短さよりも主要 2〜3 軸のカバレッジを優先する方向が出ている。
- 上流の `hierarchical_initial_labelling` / `hierarchical_merge_labelling` は `sampling_num=10` のランダムサンプリングを使っており、大規模クラスタではラベルがクラスタ全体ではなくランダム 10 件に引っ張られる可能性がある。
- まずは `sampling_num` を実質無効化して全件をラベリング LLM に渡す比較を行い、改善しない・context window が厳しい場合に max coverage / FPS / k-medoids などの sampling 戦略比較へ進むのがよさそう。
- title 候補 embedding と各要素 embedding の cosine 類似度総和を最大化する案も、代表性あるラベル選択の候補として検証対象になる。

## 関連 issue / 作業

- #869: label refinement PR 化までの残作業整理
- KJ法的プロンプトの有効性比較は別 issue として追跡する

## やりたいこと

この issue を、ラベル品質改善に関する実験・議論の上位トラッキング issue にする。

- 現在走っている、または直近で議論しているラベル品質改善実験をこの issue から辿れるようにする
- 実験ごとに「比較対象」「固定条件」「judge 方法」「採用判断」を明記する
- OpenAI judge の単独評価に寄せず、Claude / 人間 judge / 代表意見との照合を含める
- PR 化するものと、研究・実験ログに留めるものを分ける

## 完了条件

- label refinement、sampling、label candidate selection、KJ法 prompt 比較などの関連 issue / PR がこの issue から辿れる
- 少なくとも 1 つの実験について、固定条件つきの比較結果と採用判断が issue comment または developer-wiki に残っている
- default-on / default-off / 不採用の判断が、単なる印象ではなく比較結果に基づいて説明できる

**コメント:** なし

---

### [[FEATURE] [8, 64] の分析をマンダラートで可視化したい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/880)

**作成者:** nishio  
**作成日:** 2026-05-29T08:41:19Z  
**内容:**

# 背景

分析結果を一覧的に読むだけでなく、中心テーマから 8 個の観点、さらに各観点から 8 個の詳細へ展開するような構造で眺められると、論点の全体像と掘り下げ先を把握しやすくなる可能性がある。

特に [8, 64] のように、少数の主要観点と、その下位に広がる詳細観点を扱う分析では、マンダラート形式が探索的な可視化として適しているかもしれない。

# 提案内容

[8, 64] の分析結果をマンダラートで可視化する案を検討する。

- 中央: 分析対象または中心テーマ
- 周囲 8 マス: 主要クラスタ、主要論点、または上位観点
- 各主要観点の周囲: 関連する下位論点や代表コメント

検討したいこと:

- 主要 8 観点をどの基準で選ぶか
- 64 個の下位要素をクラスタ、ラベル、代表コメントのどれとして見せるか
- レポート閲覧者にとって、通常のクラスタ表示や散布図より分かりやすい用途があるか
- スマホ表示や印刷・共有時に破綻しないレイアウトにできるか

まずは既存分析結果を使ったプロトタイプまたはモックで、読みやすさを確認したい。

**コメント:** なし

---

### [[FEATURE] クラスタと時刻の掛け合わせでヒートマップ表示したい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/879)

**作成者:** nishio  
**作成日:** 2026-05-29T08:41:04Z  
**内容:**

# 背景

分析結果を見るときに、クラスタごとの量や特徴だけでなく、それがどの時刻・期間に集中しているかを把握できると、議論や関心の変化を追いやすくなる。

現在の散布図やクラスタ表示だけでは、時間方向の偏りやピークが見えにくい場面がある。

# 提案内容

クラスタと時刻を掛け合わせたヒートマップ表示を追加する。

- 縦軸: クラスタ
- 横軸: 時刻または期間バケット
- 色: 投稿数、コメント数、代表度、またはその他の集計値

想定したい確認観点:

- 特定クラスタがどの時間帯に盛り上がったか
- 複数クラスタの盛り上がり順や同時発生があるか
- レポート上で、時間変化の説明に使えるビューになるか

詳細な集計粒度、対象データ、UI 上の配置は別途検討する。

**コメント:** なし

---

### [[DOCUMENT] AI エージェントを使うコントリビュータ向けの作業導線を 1 か所にまとめる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/878)

**作成者:** nishio  
**作成日:** 2026-05-28T18:12:47Z  
**内容:**

## 背景

AI エージェントを使ってこの repo に貢献するための情報は、現在いくつかの場所に分散しています。

- `CLAUDE.md`: Claude Code 向けの入口
- `docs/development/ai-assistants.md`: Claude Code / Codex と `skills/` の使い方
- `CONTRIBUTING.md`: issue / assignee / PR の基本ルール
- `test/e2e/CLAUDE.md`: Playwright E2E の追加ルール

それぞれ個別には有用ですが、AI-assisted contribution を始める人にとっては「まずどのファイルを読めばよいか」「どの作業でどのガイドを参照するのか」が 1 ページで分かりません。

特に、次の情報はまとまっていると使いやすいはずです。

- `skills/` のどれを何に使うか
- Codex / Claude Code での最低限のセットアップ
- issue 着手前の assignee ルール
- E2E を触る時に `test/e2e/CLAUDE.md` を読む必要があること
- AI が独断でやらないほうがよい対人操作の境界

## 提案

AI エージェント利用者向けに、1 本の「作業導線ページ」を docs 側へ追加したいです。

候補内容:

- 最初に読む順番（`CONTRIBUTING.md` → `CLAUDE.md` / `docs/development/ai-assistants.md` → 必要に応じて各 skill / E2E ガイド）
- 典型タスク別の参照先
  - 構造把握
  - ローカル起動
  - フロント変更
  - API 変更
  - E2E 変更
- issue 着手から PR までの最小フロー
- 人間レビューや assignee まわりの注意点

## 完了条件

- AI エージェント利用者が「最初に何を読むか」「作業ごとに何を追加で読むか」を迷わない
- `CLAUDE.md`、`docs/development/ai-assistants.md`、`CONTRIBUTING.md` の役割分担が明確になる
- AI-assisted contribution の最低限の運用ルールが docs サイトから辿れる

## 参考

- `CLAUDE.md`
- `docs/development/ai-assistants.md`
- `CONTRIBUTING.md`
- `test/e2e/CLAUDE.md`


**コメント:** なし

---

### [[DOCUMENT] Windows セットアップガイドの前提条件と失敗時の分岐を current main に合わせて整理する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/877)

**作成者:** nishio  
**作成日:** 2026-05-28T18:12:32Z  
**内容:**

## 背景

`docs/getting-started/windows-setup.md` はユーザー向けの入口として重要ですが、前提条件と実際の入力要件に少しズレがあります。

たとえば現状の記述では:

- 前提条件に `OpenAI APIキー` と `Gemini APIキー` の両方が並んでいる
- 一方でセットアップ手順では「どちらか一方でも可」と書かれている
- Docker Desktop / WSL2 / メモリ不足 / 貼り付け不能など、詰まりやすい箇所はあるが、どの症状なら何を確認すべきかの分岐が弱い

開発者向けの実機検証手順は `docs/development/windows-real-machine-setup-verification.md` にありますが、一般ユーザー向けガイドから見ると「自分が満たすべき最小条件」と「失敗時に次に見る場所」がまだ少し分かりにくいです。

なお、`#860` では実機検証手順の整備が進みましたが、今回の論点はそれを踏まえたうえでの **ユーザー向けセットアップ文書の明確化** です。

## 提案

Windows ガイドを、次の観点で整理したいです。

- API キー要件を「OpenAI または Gemini のどちらか一方で可」と明示する
- Docker Desktop の起動確認、WSL2 初回セットアップ、メモリ不足時の確認順をチェックリスト化する
- `setup_win.bat` 実行前に確認すること / 実行後にアクセス確認することを分ける
- 一般ユーザー向けガイドと、開発者向け実機検証ガイドの役割分担を明確にする

可能なら、症状別の短い分岐表があると初回セットアップで詰まりにくくなるはずです。

## 完了条件

- Windows の初見ユーザーが「最低限何が必要か」を誤解しない
- `setup_win.bat` 実行前後の確認ポイントが明確になる
- Docker Desktop / WSL2 / メモリ不足 / API キー入力ミスの切り分け導線が分かる
- 開発者向け検証手順との住み分けが明示される

## 参考

- `docs/getting-started/windows-setup.md`
- `docs/development/windows-real-machine-setup-verification.md`
- closed issue `#860`


**コメント:** なし

---

### [[DOCUMENT] README / docs の開発者向け導線を current main に合わせて整理する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/876)

**作成者:** nishio  
**作成日:** 2026-05-28T18:12:16Z  
**内容:**

## 背景

開発者向けの入り口が `README.md`、`docs/index.md`、`docs/getting-started/quickstart.md`、`docs/user-guide/cli-quickstart.md` に分散しており、どの起動モードを選べばよいかが初見では分かりにくいです。

現状少なくとも次の 4 つの経路があります。

- Docker Compose で Web アプリ一式を起動する
- `make client-dev` + dummy-server でフロントエンドだけ触る
- Docker を使わず `apps/api` / `apps/admin` を個別起動する
- `packages/analysis-core` / CLI として使う

しかし README には長い説明が残り、docs 側にも別の quickstart があり、どれが最初に読むべき正本なのかが曖昧です。結果として、環境変数の置き場所、`.env` 変更後の再 build 要否、`analysis-core` の editable install のような重要注意が経路ごとに散っています。

## 提案

開発者向けの導線を「利用モード別」に整理し、1 本の canonical な入口ページを決めたいです。

たとえば:

- `README.md` は概要 + docs サイトへの導線に絞る
- docs 側に「開発者向けスタートガイド」を置き、以下のモード分岐を最初に提示する
  - まず動かしたい: Docker Compose
  - UI だけ触りたい: dummy-server + `make client-dev`
  - API / admin を個別デバッグしたい: native 起動
  - CLI / analysis-core を使いたい: CLI quickstart
- 各モードごとに必要な環境変数、起動コマンド、確認 URL、よくある落とし穴を 1 ページで完結させる

## 完了条件

- 新規開発者が「自分はどの起動モードを使うべきか」を最初の 1 ページで判断できる
- README と docs の役割分担が明確になる
- `.env` の置き場所、再 build が必要な条件、`analysis-core` の追加セットアップなどの重要注意が見落とされにくくなる

## 参考

- `README.md`
- `docs/index.md`
- `docs/getting-started/quickstart.md`
- `docs/user-guide/cli-quickstart.md`

---

## 2026-05-31 更新: 新方針 (PR #883 撤回後)

PR #883 を撤回し、当初の 4 モード分岐に加えて以下を盛り込む方向で再着手します。詳細と全文草案は下記リンク先 + 撤回時コメント参照。

### 追加要件

- **「開発者」を 3 サブ役割に分解**: 組織内デモ役 (橋渡し役・非エンジニア) / WebUI 開発者 (エンジニア) / 分析者・研究者 (DS 素養) は動機も推奨 Mode も違う
- **読者像 5 像を冒頭で明示**: 一般ユーザ / 自治体担当本人 / 組織内デモ役 / WebUI 開発者 / 分析者・研究者
- **「Mode 1 が default」を廃止**: 目的別に Mode 2/3/4 を直接推す。Mode 1 はデバッガ / ホットリロードが効きにくく開発作業に不向き
- **環境構築の前提を Mode 選択前に確認**: 利用主体 (個人 / 大組織) → OS の順。Docker Desktop license と platform 安定性ティア (Linux > Mac > Windows) を明示
- **構造把握スタンスを 1 段落で紹介**: 「広聴 AI は構造把握のためのツールであって、定量分析のためのツールではない」
- **Mode 4 にデータ量前提を明記**: 数百件以上、数十件未満は手作業 KJ 法へ
- **代替ルートを独立節に**: WSL2 + Docker Engine / SaaS ホスト型待ち / 動かせる人を探す

### 完了条件 (追加)

- 自治体担当の評価役 (技術者でないが組織で導入検討する人) が「自分はどの像か」を判断できる
- 大組織所属で Docker Desktop ライセンスが取れない人が、行き止まりではなく代替ルートに案内される
- Windows ユーザに「Windows は実機検証が薄い」期待値が伝わる
- Mode 1 が「default 推奨」ではなく「全体動作確認用」と位置づけられる
- Mode 4 (CLI) を小規模データで実行して失望する読者が減る

### 草案・参考リンク

- 再構成方針: https://nishio.github.io/kouchou-ai-developer-wiki/analyses/pr-883-restructuring-2026-05-31/
- developer-quickstart.md 全文草案: https://nishio.github.io/kouchou-ai-developer-wiki/analyses/pr-883-developer-quickstart-draft-2026-05-31/
- 設計判断の core stance (構造把握スタンス): https://nishio.github.io/kouchou-ai-developer-wiki/concepts/analysis-stance/
- エコシステムビジョン (Web UI = simple / CLI = 実験 / コミュニティ): https://nishio.github.io/kouchou-ai-developer-wiki/analyses/broadlistening-tool-ecosystem-vision/
- PR #883 撤回時のコメント (撤回理由詳細): https://github.com/digitaldemocracy2030/kouchou-ai/pull/883#issuecomment-4585915650

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(7件)

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

### [レポート作成時にAPIが正常でない場合にわかりやすいエラーを出す](https://github.com/digitaldemocracy2030/kouchou-ai/issues/391)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-29T12:10:49Z  
**内容:**

# レポート作成時にAPIが正常でない場合にわかりやすいエラーを出す

## 概要
現在、OpenAI APIキーが無効または期限切れの場合、レポート作成プロセスが途中で失敗し、ユーザーにとって原因がわかりにくい状態になっています。APIの状態に問題がある場合に、より明確なエラーメッセージを表示する機能が必要です。

## 背景
Windows環境セットアップガイドの改善（PR #387）の議論中に、APIキーの有効性チェックについて検討されました。セットアップスクリプト（setup_win.bat）での実装は複雑さを増すため見送られましたが、アプリケーション本体でのエラーハンドリング改善は有用と判断されました。

参考: https://chatgpt.com/share/68107163-fecc-8009-b2a3-125f8c8d8310

## 提案される改善点
1. レポート作成開始時にAPIの健全性チェックを行う
2. APIキーが無効または期限切れの場合、わかりやすいエラーメッセージを表示
3. APIサーバーに接続できない場合のネットワークエラー処理
4. エラーメッセージは技術的な詳細ではなく、ユーザーが取るべき行動を明確に示す

## 実装案
- APIリクエスト前に簡単な健全性チェック（例: `/v1/models`エンドポイントへのリクエスト）
- エラーコードに応じた適切なメッセージ表示
  - 401: APIキーが無効または期限切れ
  - 429: レート制限に達した
  - その他: ネットワーク接続の問題など

## 期待される効果
- ユーザー体験の向上
- トラブルシューティングの簡素化
- サポート負担の軽減


**コメント:** なし

---

### [[DOCUMENT]OpenAI APIの課金設定に関する混乱](https://github.com/digitaldemocracy2030/kouchou-ai/issues/292)

**作成者:** nishio  
**作成日:** 2025-04-13T00:52:56Z  
**内容:**

# 現在の問題点
非エンジニアにとって、OpenAI APIキーの取得と課金設定（クレジット購入）が必要であることが分かりにくく、ChatGPT Plusと混同しやすい。設定不備によりQuota超過エラー (429) が発生する。

「OpenAIの課金の設定してなかった」
「Error code: 429 - 'You exceeded your current quota, please check your plan and billing details.'」
「非エンジニアの場合、環境を設定した際にOpenAI APIに課金するというステップがわからない(たねのぶ)」
「OpenAIに課金=ChatGPT Plusだと思う人もいる」

# 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->
(解決策) READMEに、OpenAI APIキーの取得手順と、ChatGPT Plusとは別にAPI利用のためのクレジット購入（支払い方法登録）が必要であることを明記する。Quota超過エラーの意味と対処法も説明する。


**コメント:** なし

---

### [(情報整理)試行錯誤の負担を減らす](https://github.com/digitaldemocracy2030/kouchou-ai/issues/221)

**作成者:** nishio  
**作成日:** 2025-04-02T11:45:10Z  
**内容:**

とりあえず立てて、あとで詳細化します

from 4/2定例
>使うまでの準備工数に認識のギャップがある
>プロンプトやクラスタ数等、様々なチューニングを行う必要があるが、その認識がない
>試行錯誤の負担を減らす必要がある(& ドキュメント？)

>自治体の典型的な使い方がわかったら型を示せる

>100件、1000件とサンプリングする？→黙ってやると有害、確認ダイアログがあるといい

- クラスタ数の変更はextraction, embeddingが終わった後のデータでスピーディにできる 関連: https://github.com/digitaldemocracy2030/kouchou-ai/issues/19
- extractionの試行錯誤の負担を減らす仕組みが必要

- いきなり1万件入れて1時間くらい待たされる →　https://github.com/digitaldemocracy2030/kouchou-ai/issues/11

- https://github.com/digitaldemocracy2030/kouchou-ai/issues/241

**コメント:** なし

---

### [[FEATURE]CSVのフォーマットのエラーをわかりやすくする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/97)

**作成者:** nishio  
**作成日:** 2025-03-19T02:43:19Z  
**内容:**

# 背景
>従来のフォーマット(comment-body)の物をいれると画面遷移せずにトースターでエラーが表示されるがエラーの詳細はないので解決方法が分からなさそう、ここはカラム名の間違い、文字コードがSJIS、BOMがついてる、などなどいろんなハマりバターンが予想されるのでケアできると良さそう


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

**コメント:** なし

---

### [[FEATURE]CSVアップロード時にそれを処理した場合のコストを表示](https://github.com/digitaldemocracy2030/kouchou-ai/issues/79)

**作成者:** nishio  
**作成日:** 2025-03-18T03:19:29Z  
**内容:**

# 背景

>安野貴博: ファイルアップロードすると解析掛ける前にコストを教えてくれるの良さそうですね
>ほづみゆうき: ついにレポート出力まで漕ぎ着けたのですがAPI料金がどれくらいになるのかまったく感覚的に分からずドキドキだったので素人にはあると嬉しいと思います！

# 提案内容

これを実現するためには2つの要素が必要

- 1: done( ~~いまCSVアップロード即処理開始になっているが、一旦確認ダイアログを挟む必要がある~~ )
- 2: どのくらいのデータだとどれくらいの費用になるのかの見積もり関数が必要

## (2)の真面目な作り方

(1)は @nanocloudx さんが詳しいと思うが、(2)の部分がわからなくて着手できないと思う。
UI改善に着手する前に、この関数を作るためのデータ自体を集めていないのでそこからやる必要がある。

- a: extraction
- b: embedding
- c: その後のレポート作成

(a)がO(N)でgpt4oなので大きく、(b)はO(N)だがembedding modelなので安く、cはクラスタ数のオーダー(階層モデルなど今回いろいろ追加したから読めない)という感じで、このそれぞれに分けて料金を出せるようにしてデータ量違いでデータを集めればよい。

## (2)の雑な作り方

ユーザのペインは「すごい高額だったらどうしよう」だと思うので、まず「100円未満っすね」「100~1000円くらい」「これはでかいから1000円以上かかるよ」の3段階でいいのでは説

**コメント:** なし

---

### [[FEATURE]レポート出力にかかる時間の目安を記載する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/11)

**作成者:** nasuka  
**作成日:** 2025-03-04T10:59:48Z  
**内容:**

# 背景
* レポート出力までに何分程度かかるのかがユーザー目線でわからない


# 提案内容
* 実行時間の目安を記載する


**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (13件)

### [[codex] CodeQL Action を v4 に更新](https://github.com/digitaldemocracy2030/kouchou-ai/pull/893)

**作成者:** nishio  
**作成日:** 2026-06-01T15:53:46Z  
**変更:** +3 -3 (1ファイル)  
**マージ日:** 2026-06-01T16:04:41Z  
**内容:**

## 概要

CodeQL Action v3 が 2026 年 12 月に deprecated 予定であるため、`.github/workflows/codeql.yml` 内の CodeQL Action 参照を v4 に更新しました。

## 変更内容

- `github/codeql-action/init@v3` を `@v4` に更新
- `github/codeql-action/autobuild@v3` を `@v4` に更新
- `github/codeql-action/analyze@v3` を `@v4` に更新

workflow の trigger、permissions、対象言語、job 構成は変更していません。

## 確認

- `.github` 配下に `github/codeql-action/*@v3` が残っていないことを確認
- `git diff --check HEAD~1..HEAD`
- Ruby 標準 YAML parser で `.github/workflows/codeql.yml` の構文確認

**コメント:** なし

---

### [[codex] Code scanning alerts の指摘を修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/892)

**作成者:** nishio  
**作成日:** 2026-06-01T15:45:44Z  
**変更:** +141 -68 (18ファイル)  
**マージ日:** 2026-06-01T16:05:02Z  
**内容:**

## Summary
- admin の API fetch で URL path/query に入る入力値をエンコード
- static-site-builder の build endpoint に rate limit を追加し、build 失敗時の外部返却メッセージを固定化
- API key verify endpoint の例外詳細をレスポンスへ返さないよう変更し、回帰テストを追加

## Validation
- pnpm exec biome check --write <touched TypeScript files>
- pnpm --filter @kouchou-ai/static-site-builder build
- pnpm --filter @kouchou-ai/admin test -- --runInBand <related tests>
- ruff check apps/api/src/routers/admin_report.py apps/api/tests/routers/test_admin_report.py
- ENV_FILE=.env.test PYTHONPATH=src:../../packages/analysis-core/src uv run --with pytest --with pytest-asyncio pytest tests/routers/test_admin_report.py::TestVerifyApiKey

## Notes
- pnpm --filter @kouchou-ai/admin lint は今回触っていない既存の formatting/import/dependency 指摘で失敗します。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Fixed handling of special characters in report names, cluster labels, and identifiers across admin operations to prevent malformed URLs

* **Improvements**
  * Standardized API error responses to hide internal implementation details from users
  * Added rate limiting to the build endpoint to prevent abuse and improve stability

* **Tests**
  * Added verification test to ensure error responses properly conceal internal details

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Azure Deployment の readiness 確認を latest revision 基準にする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/890)

**作成者:** nishio  
**作成日:** 2026-06-01T15:15:20Z  
**変更:** +130 -19 (1ファイル)  
**マージ日:** 2026-06-01T16:04:49Z  
**内容:**

## 概要
- Azure Deployment の job timeout を 30 分に延長
- `az containerapp update` 後、全 Container App の `latestRevisionName == latestReadyRevisionName` を script 側 timeout 付きで確認
- timeout / smoke failure 時に revision status と recent logs を出して fail
- stable URL の root smoke に加え、public-viewer の representative report smoke を追加
- runtime build 時代の古い public-viewer コメントを削除

## 確認
- `ruby -e 'require "yaml"; YAML.load_file(ARGV[0])' .github/workflows/azure-deploy.yml`\n- `bash -n` on extracted deploy confirmation script\n- `python3 -m py_compile` on extracted representative report smoke script\n- `git diff --check`\n- live Azure CLI output shape for latest/ready/provisioning query\n\n## 注意\n- Azure Deployment workflow は push to main / workflow_dispatch 専用なので、この PR 上では本番 deployment 自体は走らない

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Chores**
  * Enhanced deployment automation with improved timeout handling and stricter error detection.
  * Added comprehensive health verification for cloud services during deployment to ensure stability before marking releases complete.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[codex] Dependabot npm alerts に対応する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/889)

**作成者:** nishio  
**作成日:** 2026-06-01T14:59:56Z  
**変更:** +83 -61 (2ファイル)  
**マージ日:** 2026-06-01T15:28:41Z  
**内容:**

## 概要

Dependabot alerts で検出されている npm transitive dependency を、root `pnpm.overrides` と `pnpm-lock.yaml` 更新で GitHub Security Advisory / Dependabot alert の patched range に寄せます。

この PR の目的は npm latest への全面更新ではなく、現時点の Dependabot alerts を閉じるための最小限の transitive dependency pinning です。公開 PR 本文には alert の詳細内容は転記せず、依存更新の範囲だけを記載します。

## 変更内容

- `pnpm.overrides` に advisory patched range を満たす version を明示
- `pnpm-lock.yaml` を再生成
- 既存の `minimatch` override を patched version に更新

## 検証

- `pnpm audit --json` → vulnerabilities 0
- `pnpm --filter @kouchou-ai/public-viewer test -- --runInBand` → 94 passed
- `pnpm --filter @kouchou-ai/admin test -- --runInBand` → 111 passed
- `pnpm --filter @kouchou-ai/static-site-builder build` → passed
- `git diff --check` → passed

## 補足

- `pnpm lint` は今回の差分外の既存 formatting / import / hook dependency 指摘で失敗するため、この PR では触っていません。
- open PR #888 / #863 は `package.json` / `pnpm-lock.yaml` を触っていないため、差分上の干渉は小さいです。
- CodeRabbit の指摘を受け、この PR が「latest への更新」ではなく「Dependabot / advisory range に対する patched version への更新」であることを明記しました。

**コメント:** なし

---

### [public-viewer の build と startup を分離する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/888)

**作成者:** nishio  
**作成日:** 2026-06-01T14:08:59Z  
**変更:** +115 -13 (7ファイル)  
**マージ日:** 2026-06-01T14:58:13Z  
**内容:**

## 概要
- dynamic hosting の `next build` が API を読まないようにし、API fetch を request-time に寄せる
- static export は fixture API ありの build として CI で維持する
- Docker image build 時に `.next` を作り、container 起動時の `pnpm run build` を撤去する

## 確認
- `pnpm --filter @kouchou-ai/public-viewer test -- --runInBand`
- `env -u API_BASEPATH -u NEXT_PUBLIC_API_BASEPATH -u NEXT_PUBLIC_PUBLIC_API_KEY pnpm --filter @kouchou-ai/public-viewer build`
- fixture API あり `pnpm --filter @kouchou-ai/public-viewer build:static`
- runtime smoke: `/`, `/faq/`, `/example/` が 200、API 接続エラー文字列なし
- PR #888 CI `client build`: API-less dynamic build、static export build、Docker build が success

## メモ
- `[slug]` に `connection()` を入れると `/example` が `DYNAMIC_SERVER_USAGE` で落ちたため、non-export は `generateStaticParams() => []` と runtime env 読みで対応

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Chores**
  * Expanded CI triggers and added a local fixture-based build/test flow for static exports.
  * Optimized container build (telemetry disabled, explicit package build) and simplified startup to skip in-container builds.

* **Performance**
  * Conditional metadata and connection behavior to skip remote calls during non-static-export builds.
  * Safer environment-variable handling to avoid build-time inlining.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[codex] Fix Plotly scattergl CSP](https://github.com/digitaldemocracy2030/kouchou-ai/pull/887)

**作成者:** 101ta28  
**作成日:** 2026-06-01T04:28:18Z  
**変更:** +31 -16 (5ファイル)  
**マージ日:** 2026-06-01T08:24:45Z  
**内容:**

close #886 

## 概要

本修正では、production 環境で Plotly の `scattergl` が初期化できるように、public viewer の CSP を修正しました。

## 根本原因

ブラウザは WebGL に対応しており、Plotly のデータも有効でしたが、production の CSP では `script-src 'self' 'unsafe-inline'` のみが許可されていました。

Plotly の `scattergl` は内部で regl を使用しており、regl は WebGL の描画コマンドを生成する際に runtime eval を必要とします。`'unsafe-eval'` がない場合、Plotly は `.no-webgl` オーバーレイを表示したままにし、WebGL 対応ブラウザでも `WebGL is not supported...` と表示します。

## 変更内容

* 共有 CSP ビルダーに明示的な `allowUnsafeEval` オプションを追加しました。
* Plotly の `scattergl` が使用される `public-viewer` で、そのオプションを有効化しました。
* その他の呼び出し元については、明示的に opt-in しない限り、デフォルトの CSP 挙動を変更しないようにしました。
* opt-in 挙動に対する CSP ヘルパーテストを追加しました。
* 静的ホスティング向けの CSP ドキュメントと README の注記を更新し、Plotly `scattergl` 用に `script-src 'unsafe-eval'` を含めるようにしました。

## 検証

* `./node_modules/.bin/biome check apps/shared/csp.ts apps/public-viewer/next.config.ts apps/admin/app/utils/__tests__/csp.test.ts`
* `./node_modules/.bin/jest app/utils/__tests__/csp.test.ts --runInBand`
* `git diff --check`


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Added support for Plotly's scattergl visualization with proper Content Security Policy configuration.
  * Enabled PNG download functionality with updated CSP blob requirements.

* **Documentation**
  * Updated deployment guides with CSP requirements for scattergl and PNG downloads.
  * Added configuration examples for Azure Static Web Apps, Cloudflare Pages, and Nginx.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[codex] fetch_reports.py を通常運用から外す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/875)

**作成者:** nishio  
**作成日:** 2026-05-28T18:01:24Z  
**変更:** +429 -338 (14ファイル)  
**マージ日:** 2026-05-29T04:47:25Z  
**内容:**

## 概要
- `tools/scripts/fetch_reports.py` を削除
- `azure-update-deployment` から deploy 前の API scrape バックアップ処理を削除
- Azure Blob Storage の運用ドキュメントを、Blob sync / restore を本線とする説明へ更新
- 環境構築後の確認手順を `apps/api/scripts/test_storage.py` ベースに更新

## 背景
- current main では `ReportSyncService` による Blob sync と `initialize_from_storage()` による復元が本線
- `fetch_reports.py` は public `/reports` scrape 前提で private / unlisted を扱えず、canonical store としても不適切
- deploy / update 手順に残っていると Blob Storage より script の方が重要に見えてしまう

Fixes #870

## 確認
- `rg -n "fetch_reports\.py|fetch_reports" .`
- `git diff --check`

## 未実施
- テストは未実施（Makefile / docs / script 削除のみ）

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Documentation**
  * Added a storage-snapshot operations guide, updated deployment/migration docs, and clarified that report sync is storage-backed (no manual fetch).
* **New Features / Tools**
  * Added a restore-from-storage utility and enhanced upload-from-storage workflow.
* **Chores**
  * Removed the manual report-fetch/backup step from the deployment flow and added a storage connectivity check during deploy.
* **Tests**
  * Added tests covering storage download/upload failure behavior.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/875?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[codex] semantic island layout 生成を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/874)

**作成者:** nishio  
**作成日:** 2026-05-26T14:00:12Z  
**変更:** +981 -13 (8ファイル)  
**マージ日:** 2026-05-28T16:26:55Z  
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


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Added hierarchical layout generation step with support for embedding UMAP layouts and semantic island mapping (auto-enabled for LLM grouping mode)
  * Added MST (Minimum Spanning Tree) visualization controls to HTML reports for enhanced cluster visualization and tree-based layout options

* **Documentation**
  * Updated documentation to reference "standard analysis steps" instead of specific step count

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/874?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[codex] Azure deploy を直列化して更新競合を避ける](https://github.com/digitaldemocracy2030/kouchou-ai/pull/873)

**作成者:** nishio  
**作成日:** 2026-05-26T12:43:44Z  
**変更:** +4 -0 (1ファイル)  
**マージ日:** 2026-05-28T05:46:59Z  
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
**マージ日:** 2026-05-28T16:23:38Z  
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
**マージ日:** 2026-05-28T16:26:37Z  
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
  * Added a --reuse-from CLI option to reuse intermediate outputs from a prior run, seed those outputs into the current run, and skip already-completed upstream stages.
  * CLI help documents the new flag and dry-run displays seeded/skipped steps.

* **Tests**
  * Added tests validating CLI behavior, seeded outputs, and orchestration initialization to ensure correct skipping and downstream execution.

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
**マージ日:** 2026-05-28T16:26:47Z  
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
**マージ日:** 2026-06-01T16:06:15Z  
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

### 過去7日間に作成されたPR (2件)

### [feat(packaging): Windows スタンドアロン（embeddable Python + 静的 viewer）](https://github.com/digitaldemocracy2030/kouchou-ai/pull/891)

**作成者:** tokoroten  
**作成日:** 2026-06-01T15:39:45Z  
**変更:** +1861 -28 (47ファイル)  
**内容:**

# 変更の概要
広聴AIを **Windows スタンドアロン**（embeddable Python に同梱）で動かすための土台を追加します。システム Python 不要で、FastAPI バックエンド + 分析パイプラインを embeddable CPython 上で起動し、public-viewer を静的 SPA として FastAPI から配信します。LM Studio（OpenAI 互換のローカル LLM）と組み合わせれば、API コストなしで「とりあえず試す」用途を想定しています（torch 不要）。

主な追加:
- `packaging/windows-standalone/`
  - `build.ps1`: embeddable Python の取得 → site-packages 有効化 → pip ブートストラップ → `analysis-core[clustering,gemini]`（torch 除外）+ apps/api 依存をインストール → アプリ一式を**空のレポートデータ**で同梱 → public-viewer を standalone ビルドして `dist/viewer` に同梱
  - `run-server.py` / `start.bat`: ランチャー。**UTF-8 モード(`-X utf8`) 必須**（日本語 Windows の cp932 で `json.load` がクラッシュするため）。viewer を `/viewer` にマウントしブラウザを開く
  - `README.md` / `env.sample` / `.gitignore`
- public-viewer のスタンドアロン SPA 化（`NEXT_PUBLIC_STANDALONE=1` で分岐。**ホスト版 SSR と static-site-builder の挙動は不変**）
  - `ReportView`（slug を実行時に取得して描画）、`/report?slug=` universal ページ、クライアント一覧、`[slug]` は output:export 用 sentinel、`ReporterClient`
  - 実行時に作成したレポートが**再ビルドなしで**表示できる
- `tmp-embeddable-poc/`: 検証記録（`FINDINGS.md`）・検証スクリプト・スクショ

> Draft。`apps/admin` はまだ含めていません（Server Actions のため要 Node もしくは SPA 化が必要）。現状は「レポート閲覧」までで、作成 UI は今後対応します。

# スクリーンショット
スタンドアロン（静的 viewer + embeddable API）での実機描画:
- 一覧 → カードクリック → レポート（概要 + Plotly クラスタ散布図・日本語ラベル）まで描画

（`tmp-embeddable-poc/FINAL-list.png` / `FINAL-report.png` を参照）

# 変更の背景
Windows でローカルに「とりあえず使ってみる」人の導入コスト（Docker / クラウド API 等）を大幅に下げるため。embeddable Python + LM Studio で、インストーラ一つで完結できる構成を目指す第一歩。

# 関連Issue
- なし（探索的な基盤追加）

# 動作確認の結果
embeddable ランタイム上で以下を実機確認:
- numba/UMAP のクラスタリングステップ（UMAP→KMeans→ward）が完走
- 実 API アプリ（`src.main:app`）が `-X utf8` で起動、`/openapi.json` `/meta/metadata.json` `/admin/reports` が 200
- `build.ps1` で空データ・viewer 同梱の **644MB** バンドルが手動介入なしに再現
- Playwright で **一覧 → クリック → レポート描画**（概要・Plotly チャート）を確認。すべて静的ファイル + embeddable API から実行時取得、Node 不要
- 詳細は `tmp-embeddable-poc/FINDINGS.md`

既知の軽微事項（非致命）: 初回描画で React #418 ハイドレーション警告のログ（描画は正常）、静的配信下で Next の RSC プリフェッチ `.txt` が 404（フルナビゲーションにフォールバックし動作）。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


**コメント:** なし

---

### [[codex] 開発者向け導線を利用モード別に整理する (closes #876)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/883)

**作成者:** nishio  
**作成日:** 2026-05-29T08:59:00Z  
**変更:** +284 -257 (5ファイル)  
**内容:**

## Summary

- `docs/development/developer-quickstart.md` を新規追加し、開発者向けの canonical 入口に。Docker Compose / dummy-server + frontend dev / native (apps/api・apps/admin) / CLI (analysis-core) の 4 モードへ「最初の 1 ページ」で分岐できるようにした。
- 各モードで必要な環境変数・起動コマンド・確認 URL・よくある落とし穴を 1 ページに集約。`.env` の置き場所がモードごとに異なる点、Docker 環境変数のビルド時埋め込み、`analysis-core` の editable install といった見落としやすい注意点を明示。
- `README.md` を概要 + docs サイト導線に絞り、長い setup 説明・ローカル LLM / GA / メタデータ / 静的出力の詳細はドキュメントサイトへ集約。
- `docs/index.md` / `docs/getting-started/quickstart.md` / `mkdocs.yml` を新ページに合わせて整理（重複削除、nav 追加）。

closes #876

## Test plan

- [ ] `mkdocs build --strict` がローカルでクリーン pass することを確認済み（CI でも回す）
- [ ] レンダリング後の `developer-quickstart` ページで 4 モードの anchor (#mode-1-docker-compose 等) が機能する
- [ ] `docs/getting-started/quickstart.md` → 開発者向けスタートガイドへの導線リンクが click 可能
- [ ] `README.md` の最短手順 (`docker compose up`) で localhost:3000 / 4000 / 8000 が起動する（既存挙動の維持確認）

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Documentation**
  * Major README rewrite: concise project overview, launch shortcuts, links to docs, and simplified warnings/credit text.
  * Added developer quickstart with four startup modes (Docker Compose, UI-only mock, native apps, and CLI/data mode).
  * Reworked getting-started to favor Docker Compose quickstart.
  * Updated docs index and site navigation to include the new developer-start guide.

<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/kouchou-ai/pull/883?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

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

