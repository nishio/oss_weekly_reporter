# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-02-18T12:53:14.529103+09:00 から 2026-02-25T12:53:14.529103+09:00 まで

## Issues

### 過去7日間に完了されたissue (2件)

### [[FEATURE] Dockerイメージが重たい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/805)

**作成者:** tokoroten  
**作成日:** 2026-02-22T02:40:27Z  
**内容:**

利用者から、PCの空き容量が少ないため、Dockerを入れることができないという相談があった。

# 背景
- kouchou-ai-api 34.11 GB
- kouchou-ai-admin 1.33 GB
- kouchou-ai-static-site-builder 1.6 GB
- kouchou-ai-public-viewer 1.58 GB

<img width="953" height="510" alt="Image" src="https://github.com/user-attachments/assets/ec7bc29f-addb-4b0f-9386-fe83804982fb" />

# 提案内容
apiサーバの容量が大きすぎるので、減らしたい


**コメント:** なし

---

### [[BUG] 巨大なCSVを分析にかけると、分析開始のボタンのアイコンがぐるぐる回ったまま帰ってこなくなる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/803)

**作成者:** tokoroten  
**作成日:** 2026-02-22T02:21:26Z  
**内容:**

### 概要

2MB程度の巨大なCSVを分析にかけると、分析開始のボタンのアイコンがぐるぐる回ったまま帰ってこなくなる。

### 再現手順

1. このgistからサンプルデータをダウンロードして使う   https://gist.github.com/tokoroten/0115947bc25a53caa53d2f1e55a0b1df
2. 
 
### 期待する動作

すぐに画面遷移してレポート一覧画面に遷移する。

### スクリーンショット・ログ

<img width="896" height="429" alt="Image" src="https://github.com/user-attachments/assets/c76a0937-a996-4957-b473-966fe0bdeac0" />

### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->

**コメント:** なし

---

### 過去7日間に作成されたissue (2件)

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

### 過去7日間に更新されたissue（作成・クローズを除く）(1件)

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

## Pull Requests

### 過去7日間にマージされたPR (4件)

### [fix: shrink Docker images (api ~34GB→~2.7GB, admin/viewer smaller) and clean up api deps](https://github.com/digitaldemocracy2030/kouchou-ai/pull/807)

**作成者:** tokoroten  
**作成日:** 2026-02-22T07:31:26Z  
**変更:** +234 -502 (10ファイル)  
**マージ日:** 2026-02-23T01:35:20Z  
**内容:**

## Summary

- **apps/api/Dockerfile**: merge all `pip install` layers into one RUN command; use CPU-only PyTorch index (`https://download.pytorch.org/whl/cpu`) when `WITH_GPU!=true`; install `analysis-core` in the same layer to avoid torch duplication across layers
- **apps/api/pyproject.toml**: remove unused dependencies (litellm, plotly, joblib, umap-learn, scipy, llvmlite, janome, sentence-transformers, hf_xet, pytest); add actually-used deps (requests, httpx); regenerate lock files (121 → 48 packages)
- **apps/api/requirements-torch.txt**: delete (no longer referenced)
- **apps/admin/Dockerfile**: use root-level `tsc` for report-schema build; enable Next.js standalone mode
- **apps/admin/next.config.ts**: add `output: "standalone"`
- **apps/public-viewer/Dockerfile**: use root-level `tsc`; remove per-package `node_modules` in runner stage to fix `Cannot find module .../node_modules/next/dist/bin/next` crash caused by broken pnpm shim under `shamefully-hoist=true`
- **apps/static-site-builder/Dockerfile**: use root-level `tsc`; selective COPY of only needed files

## Image sizes (measured locally, CPU build)

| Image | Before | After |
|---|---|---|
| api | ~34 GB | ~4.6 GB |
| admin | ~1.33 GB | ~80 MB |
| public-viewer | — | ~711 MB |

## Test plan

- [x] `docker compose build` completes without errors (CPU mode, `WITH_GPU=false`)
- [x] All 4 containers start and remain healthy
- [x] public-viewer serves pages without `Cannot find module` crash
- [x] admin UI accessible
- [x] api health endpoint responds

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **チョアー**
  * Dockerイメージを再構成して実行時に含めるファイルを限定し、イメージサイズとメモリ使用を削減しました。
  * ビルド手順を簡素化して不要なビルドループを排除、依存性インストールを統一しました。
  * 開発時のGPUフラグ説明を拡充して環境設定が分かりやすくなりました。

* **新機能**
  * 実行環境のデフォルトポートを4000に設定し、起動コマンドを簡略化しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Fix infinite spinner when submitting large CSV for analysis](https://github.com/digitaldemocracy2030/kouchou-ai/pull/804)

**作成者:** Copilot  
**作成日:** 2026-02-22T02:21:40Z  
**変更:** +37 -25 (2ファイル)  
**マージ日:** 2026-02-22T07:49:36Z  
**内容:**

Submitting a ~2MB CSV caused the submit button to spin indefinitely. The parsed CSV is serialized as JSON (with repeated field names per row) and passed through a Next.js Server Action — this payload routinely exceeds Next.js's default 1MB server action body limit. The framework rejects the request silently before the handler runs, the uncaught rejection skips `setLoading(false)`, and the button never recovers.

## Changes

- **`apps/admin/next.config.ts`**: Raise `serverActions.bodySizeLimit` to `100mb`
  ```ts
  serverActions: {
    bodySizeLimit: "100mb",
  },
  ```

- **`apps/admin/app/create/page.tsx`**: Wrap the `createReport` call in `try/catch` so `setLoading(false)` is always reached on any error path; on success, `return` early before reaching it to avoid a state update on an unmounting component
  ```ts
  try {
    const result = await createReport({ ... });
    if (result.success) {
      router.replace("/");
      return;  // skip setLoading — navigating away
    }
    toaster.create({ type: "error", ... });
  } catch (e) {
    toaster.create({ type: "error", description: "送信データが大きすぎるか、通信エラーが発生しました" });
  }
  setLoading(false);
  ```

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>[BUG] 巨大なCSVを分析にかけると、分析開始のボタンのアイコンがぐるぐる回ったまま帰ってこなくなる</issue_title>
> <issue_description>### 概要
> 
> 2MB程度の巨大なCSVを分析にかけると、分析開始のボタンのアイコンがぐるぐる回ったまま帰ってこなくなる。
> 
> ### 再現手順
> 
> 1. このgistからサンプルデータをダウンロードして使う   https://gist.github.com/tokoroten/0115947bc25a53caa53d2f1e55a0b1df
> 2. 
>  
> ### 期待する動作
> 
> すぐに画面遷移してレポート一覧画面に遷移する。
> 
> ### スクリーンショット・ログ
> 
> <img width="896" height="429" alt="Image" src="https://github.com/user-attachments/assets/c76a0937-a996-4957-b473-966fe0bdeac0" />
> 
> ### その他
> 
> <!-- 追加で伝えておきたいことがあれば記入してください --></issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes digitaldemocracy2030/kouchou-ai#803

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/digitaldemocracy2030/kouchou-ai/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.


**コメント:** なし

---

### [feat: 散布図に「詳細クラスタ」タブを追加、クラスタの凸包を表示するオプションを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/798)

**作成者:** tokoroten  
**作成日:** 2026-02-21T23:30:20Z  
**変更:** +227 -40 (10ファイル)  
**マージ日:** 2026-02-22T04:09:36Z  
**内容:**

## Summary

- 散布図のタブバーに「詳細クラスタ」（`scatterDetail`）タブを「全体」の隣に追加
- 「詳細クラスタ」選択時は、密度フィルタなしで最深レベルの**全クラスター**を色分け・ラベル表示する
- 「全体」・「詳細クラスタ」表示時に各クラスターの**凸包（境界線）**を表示する
- 凸包にマウスホバーするとクラスター名が表示される
- タブ切り替え時にズーム・パン状態が保持されるよう `uirevision` を設定
- 設定画面から凸包の表示/非表示を切り替え可能

<img width="1217" height="903" alt="image" src="https://github.com/user-attachments/assets/2e255c95-7e07-4a3e-8c6d-903b22a5014c" />

<img width="1239" height="902" alt="image" src="https://github.com/user-attachments/assets/ade8b423-1d6f-4680-b028-595578ac4501" />

<img width="1233" height="978" alt="image" src="https://github.com/user-attachments/assets/3e327edf-c4da-47e8-b4d8-1c90530a0394" />

## 凸包を表示
<img width="1204" height="899" alt="image" src="https://github.com/user-attachments/assets/e255a6ed-5726-4706-ad4f-43e69a484d7d" />

<img width="1226" height="977" alt="image" src="https://github.com/user-attachments/assets/65c79b2e-e6a2-40fd-bf60-845c188bf58e" />



## 変更ファイル

| ファイル | 変更内容 |
|---|---|
| `apps/public-viewer/components/icons/ViewIcons.tsx` | `DetailViewIcon`（3×3グリッドの9ドット）を追加 |
| `apps/public-viewer/components/charts/plugins/scatter.tsx` | `scatterDetail` モード追加、凸包表示を context から制御 |
| `apps/public-viewer/components/charts/plugins/types.ts` | `ChartRenderContext` に `showConvexHull` フィールドを追加 |
| `apps/public-viewer/type.ts` | `ChartType` に `"scatterDetail"` を追加 |
| `apps/public-viewer/components/charts/SelectChartButton.tsx` | `DEFAULT_ENABLED_CHARTS` に `scatterDetail` を追加 |
| `apps/public-viewer/components/charts/ScatterChart.tsx` | 凸包（gift wrapping アルゴリズム）実装、ホバー時クラスター名表示 |
| `apps/public-viewer/components/report/Chart.tsx` | `showConvexHull` prop を追加し render context に伝播 |
| `apps/public-viewer/components/report/ClientContainer.tsx` | `scatterDetail` の状態管理・フィルタ処理、`showConvexHull` state 追加 |
| `apps/public-viewer/components/report/DisplaySettingDialog.tsx` | 「意見グループの境界線を表示」トグルを追加 |

## チャートモード比較

| モード | targetLevel | 密度フィルタ | 凸包 | 用途 |
|---|---|---|---|---|
| 全体 (scatterAll) | 1（最上位） | なし | あり | 上位クラスターを俯瞰 |
| **詳細クラスタ (scatterDetail)** | max（最深） | **なし** | **あり** | 全サブクラスターを確認 |
| 濃い意見 (scatterDensity) | max（最深） | あり | なし | 密集クラスターに注目 |

## 実装方針

既存のプラグインアーキテクチャ（`ChartPlugin` / `chartRegistry`）に従い、`scatter.tsx` プラグインの `modes` 配列に `scatterDetail` を追加した。凸包は Plotly の scatter trace（`fill: "toself"`, `hoveron: "fills"`）で実装し、gift wrapping アルゴリズムで計算する。

## Test plan

- [ ] タブバーに「詳細クラスタ」が「全体」と「濃い意見」の間に表示される
- [ ] 「詳細クラスタ」クリック時に最深レベルの全クラスターが色分け・ラベル表示される
- [ ] 「全体」・「詳細クラスタ」でクラスター境界の凸包が表示される
- [ ] 凸包にホバーするとクラスター名が表示される
- [ ] 設定画面の「意見グループの境界線を表示」トグルで凸包の表示/非表示が切り替わる
- [ ] 「濃い意見」では凸包が表示されない
- [ ] 「全体」と比較して「詳細クラスタ」ではより多くのクラスターが色分けされる
- [ ] 「全体」↔「詳細クラスタ」切り替え時にズーム・パン状態が保持される
- [ ] 属性フィルタが「詳細クラスタ」表示中にも正常動作する
- [ ] フルスクリーン表示でも正常動作する

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

## Summary by CodeRabbit

* **新機能**
  * 散布図に「詳細クラスタ」表示モードを追加し、既定チャートセットへ含めました。
  * 「詳細クラスタ」用の新アイコンを追加しました。
  * 表示設定に「意見グループの境界線を表示」トグルを追加し、クラスタの凸包（境界）を表示／非表示できます。
* **改善**
  * 凸包は散布点の背後に表示され、描画が整理されます。
  * データ更新後もズーム／パン状態が保持されます。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Increase analysis-core timeout defaults to 300 seconds](https://github.com/digitaldemocracy2030/kouchou-ai/pull/795)

**作成者:** nishio  
**作成日:** 2026-02-16T12:22:25Z  
**変更:** +48 -17 (3ファイル)  
**マージ日:** 2026-02-24T13:27:10Z  
**内容:**

# 変更の概要
- analysis-core の LLM リクエストタイムアウト既定値を 300 秒に引き上げました
- `hierarchical_overview` で使う LLM リクエストに 300 秒タイムアウトを明示的に指定しました
- `extraction` のバッチ待機タイムアウトを 300 秒に変更し、`config["extraction"]["timeout_seconds"]` で上書き可能にしました

# スクリーンショット
- UI変更なし

# 変更の背景
- `hierarchical_overview` で `Request timed out.` が発生し、分析パイプライン全体が失敗するケースが継続的に発生していました
- 既存の 30 秒タイムアウトでは外部 LLM 応答遅延時に失敗しやすいため、分析系のタイムアウトを 300 秒へ統一しました
- レポートの再利用によって今までのようにextractionからスタートしないケースが増えたため、後半のLLM呼び出しでcold startを踏むケースが増えたのだと思われます

# 関連Issue
- なし

# 動作確認の結果
- `python3 -m py_compile packages/analysis-core/src/analysis_core/services/llm.py packages/analysis-core/src/analysis_core/steps/extraction.py packages/analysis-core/src/analysis_core/steps/hierarchical_overview.py`
  - 成功
- `python3 -m ruff check ...`
  - 実行環境に `ruff` が未インストールのため未実施

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **新機能**
  * LLM関連リクエストに共通のタイムアウト設定を導入しました。デフォルトは300秒で、抽出処理や階層的概要生成を含むすべてのAI呼び出しで一貫して適用されます。長時間処理やローカル/外部プロバイダ間でのタイムアウト挙動が統一され、設定可能になりました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (6件)

### [fix: override minimatch to ^10.2.1 to fix CVE-2026-26996 (ReDoS)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/808)

**作成者:** shingo-ohki  
**作成日:** 2026-02-24T13:12:53Z  
**変更:** +26 -44 (2ファイル)  
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

### [Fix: Shrink all Docker images (api ~34GB→~3GB, admin ~1.33GB→~200-400MB) by eliminating layer duplication and using standalone mode](https://github.com/digitaldemocracy2030/kouchou-ai/pull/806)

**作成者:** Copilot  
**作成日:** 2026-02-22T02:40:53Z  
**変更:** +31 -26 (5ファイル)  
**内容:**

All four Docker images were larger than necessary due to layer bloat and inefficient runner stages.

## Root causes and fixes

### kouchou-ai-api (34 GB → expected ~3-4 GB)

`torch` was being installed **three times in separate `RUN` commands**, and Docker layers never delete files from previous layers — so all three copies persisted.

**Three separate torch installs across three layers:**
1. `uv pip install /packages/analysis-core` → `sentence-transformers` → `torch 2.9.1` CUDA from PyPI (~3GB)
2. `uv pip install -r requirements-torch.txt` → `torch 2.7.0` CPU (~500MB), masks layer 1 at runtime but layer 1 is still in the image
3. `uv pip install -r requirements.lock` → `torch 2.9.1` CUDA from PyPI again (~3GB), same problem

- **`apps/api/Dockerfile`** — Collapse all pip install steps into a **single `RUN`** command. For CPU mode (default), pass `--index-url https://download.pytorch.org/whl/cpu --extra-index-url https://pypi.org/simple/` so torch resolves to the CPU-only wheel from the primary index; all other packages fall back to PyPI. GPU mode continues to use PyPI directly.

```dockerfile
RUN set -- /packages/analysis-core && \
    if [ "$ENVIRONMENT" = "development" ]; then \
        set -- "$@" -r requirements-dev.lock; \
    else \
        set -- "$@" -r requirements.lock; \
    fi && \
    if [ "$WITH_GPU" != "true" ]; then \
        set -- --index-url https://download.pytorch.org/whl/cpu \
               --extra-index-url https://pypi.org/simple/ "$@"; \
    fi && \
    uv pip install --no-cache --system "$@"
```

- **`apps/api/requirements-torch.txt`** — Remove unused `torchvision` and `torchaudio` (not imported anywhere in the codebase); align `torch` version to `2.9.1` matching `requirements.lock`. Note: `requirements-torch.txt` is no longer consumed by the Dockerfile — torch is already pinned in both lock files as a transitive dep of `sentence-transformers`.

---

### kouchou-ai-admin (1.33 GB → expected ~200-400 MB)

The runner stage was doing `COPY --from=builder /repo /repo`, copying the entire repository tree including all dev dependencies and build tools.

- **`apps/admin/next.config.ts`** — Add `output: "standalone"`. Next.js creates `.next/standalone/` containing a minimal server with only the required runtime production dependencies.
- **`apps/admin/Dockerfile`** — Runner stage now copies only `.next/standalone/` (minimal server + runtime deps), `.next/static/` (compiled assets), and `public/` instead of the full `/repo` tree. Removed `corepack`/pnpm from the runner (standalone output is self-contained). Changed `CMD` from `pnpm start` to `node apps/admin/server.js` and set `ENV PORT=4000`.

---

### kouchou-ai-static-site-builder (1.6 GB — limited saving)

The runner stage was doing `COPY --from=builder /repo /repo`, pulling in TypeScript source, `tsconfig.json`, and `pnpm-lock.yaml` that are not needed at runtime.

- **`apps/static-site-builder/Dockerfile`** — Replace the wholesale `COPY --from=builder /repo /repo` with selective COPY instructions that exclude TypeScript source, tsconfig, and lock files. The node_modules cannot be pruned because this service builds public-viewer at request time and requires all build-time dependencies.

---

### kouchou-ai-public-viewer (1.58 GB — no change)

This service intentionally builds at container startup so it can fetch live data from the API server before serving. This requires all devDependencies (TypeScript, Next.js build tools, etc.) to be present at runtime. The runner stage already uses selective copies. No meaningful reduction is possible without architectural changes.

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>[FEATURE] Dockerイメージが重たい</issue_title>
> <issue_description>利用者から、PCの空き容量が少ないため、Dockerを入れることができないという相談があった。
> 
> # 背景
> - kouchou-ai-api 34.11 GB
> - kouchou-ai-admin 1.33 GB
> - kouchou-ai-static-site-builder 1.6 GB
> - kouchou-ai-public-viewer 1.58 GB
> 
> <img width="953" height="510" alt="Image" src="https://github.com/user-attachments/assets/ec7bc29f-addb-4b0f-9386-fe83804982fb" />
> 
> # 提案内容
> apiサーバの容量が大きすぎるので、減らしたい
> </issue_description>
> 
> <agent_instructions>dockerのセットアップファイルを読んで、何が問題かを考えて。
> </agent_instructions>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes digitaldemocracy2030/kouchou-ai#805

<!-- START COPILOT CODING AGENT TIPS -->
---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.

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

### [feat: 散布図に「詳細クラスタ」タブを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/797)

**作成者:** tokoroten  
**作成日:** 2026-02-21T15:20:50Z  
**変更:** +30 -7 (6ファイル)  
**内容:**

## Summary

- 散布図のタブバーに「詳細クラスタ」（`scatterDetail`）タブを「全体」の隣に追加
- 「詳細クラスタ」選択時は、密度フィルタなしで最深レベルの**全クラスター**を色分け・ラベル表示する
- タブ切り替え時にズーム・パン状態が保持されるよう `uirevision` を設定
- `Reporter.tsx` の `API_BASEPATH` 未設定時に発生する `TypeError: Invalid URL` を修正

<img width="1155" height="846" alt="image" src="https://github.com/user-attachments/assets/c489c570-57cf-43b4-a94f-3cd3ace17714" />

<img width="1154" height="846" alt="image" src="https://github.com/user-attachments/assets/5a0a7253-c71c-49ef-9a87-d70ce2244203" />

結局、広聴AIのユーザは、手を動かして考える人は細かく切り刻んでみたいので、このビューがあったほうがよさそう

## 変更ファイル

| ファイル | 変更内容 |
|---|---|
| `client/components/icons/ViewIcons.tsx` | `DetailViewIcon`（3×3グリッドの9ドット）を追加 |
| `client/components/charts/SelectChartButton.tsx` | `scatterDetail` タブを追加、タブ幅を4分割に変更 |
| `client/components/report/Chart.tsx` | `scatterDetail` を ScatterChart 描画条件に追加 |
| `client/components/report/ClientContainer.tsx` | `scatterDetail` の状態管理・フィルタ処理を追加 |
| `client/components/charts/ScatterChart.tsx` | `uirevision` を設定してズーム・パン状態を保持 |
| `client/components/reporter/Reporter.tsx` | `API_BASEPATH` 未設定時の Invalid URL エラーを修正 |

## チャートモード比較

| モード | targetLevel | 密度フィルタ | 用途 |
|---|---|---|---|
| 全体 (scatterAll) | 1（最上位） | なし | 上位クラスターを俯瞰 |
| **詳細クラスタ (scatterDetail)** | max（最深） | **なし** | 全サブクラスターを確認 |
| 濃い意見 (scatterDensity) | max（最深） | あり | 密集クラスターに注目 |

## Test plan

- [ ] タブバーに「詳細クラスタ」が4番目のタブとして表示される
- [ ] 「詳細クラスタ」クリック時に最深レベルの全クラスターが色分け・ラベル表示される
- [ ] 「全体」と比較してより多くのクラスターが色分けされる
- [ ] 「濃い意見」と比較して密度フィルタで除外されるクラスターも表示される
- [ ] 「全体」↔「詳細クラスタ」切り替え時にズーム・パン状態が保持される
- [ ] 属性フィルタが「詳細クラスタ」表示中にも正常動作する
- [ ] フルスクリーン表示でも正常動作する

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **新機能**
  * 散布図に「詳細クラスタ」表示オプションを追加
  * 散布図のテキスト検索と属性フィルタリング機能に対応

* **バグ修正**
  * 散布図データ更新後のズーム・パン状態を保持するよう改善
  * API設定不足時の画像読み込み処理を堅牢化

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

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

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

