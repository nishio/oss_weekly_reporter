# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-09-02T17:00:57.716135+09:00 から 2026-09-09T17:00:57.716135+09:00 まで

## Issues

### 過去7日間に完了されたissue (30件)

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

### [[BUG] ラベル生成の部分失敗を正常完了扱いしない（#905の残件）](https://github.com/digitaldemocracy2030/kouchou-ai/issues/915)

**作成者:** nishio  
**作成日:** 2026-09-07T19:09:51Z  
**内容:**

# 背景

#905の意見抽出については、PR #910（merge済み）でAPI例外・timeout・不正応答を正常な「抽出0件」と区別し、失敗件数・回答ID・エラー種別を伴うerrorとして中断するよう修正した。

元Issueで併せて報告された、詳細クラスタに「エラーでラベル名が取得できませんでした」が残ったまま生成が完了するケースは未対応。この残件を本Issueへ移す。

# 対応範囲・完了条件

- [ ] 初期ラベリング・統合ラベリング等の例外処理を調べ、失敗を正常なラベルとして返す経路を特定する。
- [ ] API例外・timeout・不正応答と正常結果を区別し、失敗した工程・件数・対象クラスタを検知できるようにする。
- [ ] エラー文を通常のラベルとして含むレポートを正常完了扱いしない。抽出段階と同様のerror中断を基本案とする。
- [ ] 失敗した場合に後段が進まないこと、正常時のラベル生成に回帰がないことをテストする。
- [ ] 失敗時のtoken・費用集計の扱いを確認し、取得できていない分を完全な総額として表示しない。

# 元報告の未確認事項

194回答中49回答が抽出0件になった元の事象について、APIエラーログはなく、並列数30→5で改善したことしか分かっていない。PR #910で実データを再実行したわけではないため、原因特定済みとは扱わない。再発時は新しい失敗情報から原因を切り分ける。

警告付き部分完了や失敗分だけの再実行は追加機能案であり、このIssueの必須完了条件には含めない。

関連：#905、PR #910


**コメント:** なし

---

### [[FEATURE] LLMモデル一覧・料金情報を更新しやすい構造にする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/909)

**作成者:** shingo-ohki  
**作成日:** 2026-09-06T02:14:03Z  
**内容:**

# 背景

OpenAI / Azure OpenAI / Gemini / OpenRouter などのLLMモデルは更新頻度が高く、現在利用可能なモデルと広聴AI上で選択できるモデルに差が出やすい。

今回、新しいOpenAI / Geminiモデルへの対応を検討したところ、モデル一覧だけでなく、料金情報や説明文など複数箇所の更新が必要になることが分かった。

また、Azure OpenAIについては、OpenAIと同じモデル一覧を表示している一方で、実際のLLM呼び出しでは環境変数で指定したdeploymentが利用されており、モデル一覧の管理方法自体を整理する必要も見えてきた。

今後も各プロバイダーでモデルの追加・廃止が続くことを考えると、個別モデルを都度追加するだけでなく、モデル一覧・料金情報・説明文などを更新しやすい構造にしたい。

# 現状

現在、プロバイダーごとのモデル情報が複数箇所で管理されている。

例:

- OpenAIモデル一覧
- Azure OpenAIモデル一覧
- Geminiモデル一覧
- OpenRouterモデル一覧
- モデルごとの説明文
- モデルごとの料金情報

管理画面側ではOpenAI / Gemini / OpenRouter等のモデル一覧がコード上に定義されている。

一方、API側にもモデル一覧取得処理があり、

- OpenAI: 固定リスト
- Azure OpenAI: OpenAIと同じ固定リスト
- Gemini: APIキーがある場合はAPIから取得
- OpenRouter: APIから取得
- Local LLM: 接続先APIから取得

と、プロバイダーごとに管理方法が異なっている。

また、料金情報は別途provider / modelごとに定義されており、モデル追加時に複数箇所を更新する必要がある。

# 提案内容

モデルに関する情報を、できるだけ一箇所または明確な責務で管理できるように整理する。

例えば以下の情報をまとめて扱えるようにしたい。

- provider
- model id
- 表示名
- 説明文
- 入力料金
- 出力料金
- 利用可否
- deprecated / 提供終了情報
- Structured Outputs等、広聴AIで必要な機能への対応状況

あわせて以下も検討する。

- APIから取得可能なモデル一覧をどこまで動的に利用するか
- プロバイダー上で利用可能な全モデルを表示するのか、広聴AIで動作確認済みのモデルだけを表示するのか
- モデル追加・廃止時にフロントエンド / API / 料金情報 / 説明文を個別に修正しなくても済む構造にできないか
- Azure OpenAIについて、OpenAIと同じモデル一覧を共有するのが適切か
- Azure OpenAIのdeploymentとモデル情報をどのように管理するか
- 提供終了したモデルをUI上でどのように扱うか

# 完了条件案

- モデル追加・削除時に修正すべき箇所が整理されている
- 管理画面とAPI側でモデル一覧の不整合が起きにくい
- 料金情報・説明文もモデル情報と合わせて管理しやすくなっている
- OpenAI / Azure OpenAI / Gemini / OpenRouterそれぞれのモデル管理方法が整理されている
- 新しいモデルを追加する際の手順が分かる
- Azure OpenAIについて、管理画面上の選択肢と実際に利用されるdeploymentの関係が明確になっている

# 関連Issue

- #906 GPT-5.6 Terra / Luna を選択できるようにする
- #907 Gemini 3.8 Flash / 3.5 Flash-Lite を選択できるようにする
- #908 Azure OpenAI 選択時にモデル選択が実際のLLM呼び出しに反映されない

**コメント:** なし

---

### [[BUG] Azure OpenAI 選択時にモデル選択が実際のLLM呼び出しに反映されない](https://github.com/digitaldemocracy2030/kouchou-ai/issues/908)

**作成者:** shingo-ohki  
**作成日:** 2026-09-06T02:12:39Z  
**内容:**

### 概要

Azure OpenAI をLLMプロバイダーとして選択した場合、管理画面ではOpenAIと同じモデル一覧からモデルを選択できますが、実際のLLM呼び出しには選択したモデルが反映されていません。

現在、Azure OpenAI の呼び出しでは管理画面で指定した `model` ではなく、環境変数 `AZURE_CHATCOMPLETION_DEPLOYMENT_NAME` に設定されたdeploymentが常に使用されます。

そのため、管理画面上のモデル選択と実際に利用されるAzure OpenAIのdeploymentが一致しない可能性があります。

### 再現手順

1. LLMプロバイダーとして `Azure OpenAI` を選択する
2. 管理画面で任意のモデル（例: `gpt-4o-mini`）を選択する
3. レポート生成を実行する
4. Azure OpenAIへのLLM呼び出しを確認する
5. 管理画面で選択したモデルではなく、`AZURE_CHATCOMPLETION_DEPLOYMENT_NAME` に設定されたdeploymentが利用されることを確認する

### 期待する動作

管理画面で表示・選択されている内容と、実際にAzure OpenAIで使用されるdeploymentが一致していること。

Azure OpenAIではAPI呼び出し時にdeployment nameを指定するため、例えば以下のいずれかの形が考えられます。

- Azure OpenAIの場合は、利用可能なdeploymentを選択できるようにする
- Azure OpenAIのdeploymentを環境変数で固定する場合は、通常のモデル選択UIを表示せず、実際に利用されるdeploymentを明示する

### スクリーンショット・ログ

API側のAzure OpenAIモデル一覧は、現在OpenAIと同じ一覧を返しています。

```python
async def get_azure_models() -> list[dict[str, str]]:
    """Azureのモデルリストを取得（OpenAIと同じ）"""
    return [model.to_dict() for model in OPENAI_MODELS]
```

一方、Azure OpenAIのLLM呼び出しでは、管理画面で選択された model は渡されていません。

```
if provider == "azure":
    return request_to_azure_chatcompletion(
        messages,
        is_json,
        json_schema,
        user_api_key,
        timeout_seconds,
    )
```

実際に利用されるdeploymentは、以下の環境変数から取得されています。
```
deployment = os.getenv("AZURE_CHATCOMPLETION_DEPLOYMENT_NAME")
```

### その他

Azure OpenAIでは、OpenAI APIと同じモデル一覧をそのまま共有するより、Azure側のdeploymentとの対応を考慮した扱いが必要そうです。

今後、新しいOpenAIモデルへの対応を行う際にも、Azure OpenAIについてはモデル選択UIと実際のdeployment指定の整合性を整理する必要があります。

関連:

#906 GPT-5.6 Terra / Luna をOpenAIモデルとして選択できるようにする

**コメント:** なし

---

### [[FEATURE] Gemini 3.8 Flash / 3.5 Flash-Lite を選択できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/907)

**作成者:** shingo-ohki  
**作成日:** 2026-09-06T02:04:54Z  
**内容:**

# 背景

現在、Geminiモデルとして選択できるモデルが以下に限られている。

- `gemini-2.5-flash`
- `gemini-1.5-flash`
- `gemini-1.5-pro`

このうち `gemini-1.5-flash` / `gemini-1.5-pro` はすでに提供終了しているため、現在利用可能なモデルへ更新したい。

また、実データでLLMモデルを比較したところ、モデルによってクラスタラベルの読みやすさや処理の安定性などに違いが見られたため、Geminiについても新しいモデルを広聴AIで比較できるようにしたい。

まずは以下の安定版モデルを追加したい。

- `gemini-3.8-flash`
- `gemini-3.5-flash-lite`

`gemini-3.8-flash` は最新のFlash系モデル、`gemini-3.5-flash-lite` は低レイテンシ・低コスト・高スループット用途向けのモデルとなっており、広聴AIの意見抽出・ラベリングで比較してみたい。

# 提案内容

- Geminiのモデル選択肢に `gemini-3.8-flash` / `gemini-3.5-flash-lite` を追加する
- 提供終了している `gemini-1.5-flash` / `gemini-1.5-pro` の扱いを見直す
- 現在の抽出・ラベリング処理で正常に利用できることを確認する
- Structured Outputs等、現在利用しているAPI機能との互換性を確認する
- モデルごとの料金情報・説明文を更新する

必要に応じて `gemini-3.5-flash` なども比較対象として検討する。

**コメント:** なし

---

### [[FEATURE] GPT-5.6 Terra / Luna を選択できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/906)

**作成者:** shingo-ohki  
**作成日:** 2026-09-05T23:02:24Z  
**内容:**

# 背景

現在、OpenAIモデルとして選択できるモデルが `gpt-4o-mini` / `gpt-4o` / `o3-mini` に限られている。

実データでモデルを比較したところ、モデルによってクラスタラベルの読みやすさや処理の安定性などに違いが見られたため、現在のOpenAI APIで利用可能なモデルも比較・選択できるようにしたい。

`gpt-5.6-terra` は性能とコストのバランス、`gpt-5.6-luna` はコスト重視・高ボリューム用途向けとされているため、まずは以下のモデルを追加して広聴AIで比較してみたい。

- `gpt-5.6-terra`
- `gpt-5.6-luna`

必要に応じて `gpt-5.6-sol` なども比較対象として検討する。

# 提案内容

- OpenAIのモデル選択肢に `gpt-5.6-terra` / `gpt-5.6-luna` を追加する
- 現在の抽出・ラベリング処理で正常に利用できることを確認する
- Structured Outputs等、現在利用しているAPI機能との互換性を確認する
- モデルごとの料金情報を更新する

将来的には、モデル追加・廃止時に選択肢と料金情報を更新しやすい構造も検討したい。

**コメント:** なし

---

### [[BUG] LLM呼び出し失敗時に一部回答が欠落したままレポート生成が完了する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/905)

**作成者:** shingo-ohki  
**作成日:** 2026-09-05T22:56:08Z  
**内容:**

### 概要

LLMによる意見抽出処理の一部が失敗した際、その回答が「抽出0件」として扱われたままレポート生成が完了するケースを確認しました。

実データ194回答をGPT-4oで処理したところ、49回答が抽出0件となっていましたが、レポート自体はエラーにならず生成されました。

同じ入力データ・同じプロンプトで並列数を30から5に下げて再実行すると、抽出0件は0回答になりました。

原因はまだ特定できていません。

### 再現手順

1. 194回答の同一入力データを、GPT-4o・標準の意見抽出プロンプト・`workers=30` でレポート生成する
2. 生成された `relations.csv` を元回答単位で集計する
3. 194回答中49回答が抽出0件になっていることを確認する
4. 同じ入力データ・プロンプトで、`workers=5` に変更して再実行する
5. 再実行では194回答すべてから1件以上抽出されることを確認する

確認時の抽出結果：

- GPT-4o / workers=30：482意見、抽出0件 49回答
- GPT-4o / workers=5：666意見、抽出0件 0回答
- 参考：GPT-4o-mini / workers=30：681意見、抽出0件 0回答

入力CSVはSHA-1が一致しており、同一データであることを確認済みです。

### 期待する動作

LLM呼び出しに失敗した場合、それを通常の「抽出0件」として扱わず、失敗したことを検知できるようにしたいです。

少なくとも、一部回答の処理に失敗した状態でレポート生成を完了する場合には、利用者が「何件の処理に失敗したか」を確認できる状態になっていることを期待します。

可能であれば、LLM呼び出し失敗時のretry / backoffも検討したいです。

### スクリーンショット・ログ

現時点では原因となったAPIエラー等のログまでは確認できていません。

確認できた出力結果：

```text
GPT-4o / workers=30
回答数: 194
抽出数: 482
抽出0件: 49回答

GPT-4o / workers=5
回答数: 194
抽出数: 666
抽出0件: 0回答

GPT-4o-mini / workers=30
回答数: 194
抽出数: 681
抽出0件: 0回答

###その他
現在の extract_batch() では、個別のLLM呼び出しが例外になった場合、その回答の結果を空配列 [] として処理を継続するため、処理失敗と「意見が1件も抽出されなかった回答」を区別できません。

今回、GPT-4oの並列数を30→5に下げることで一旦解消しましたが、並列数が直接の原因かどうかまでは未確認です。

また別の処理段階でも、生成された詳細クラスタに「エラーでラベル名が取得できませんでした」が残るケースを確認しました。LLM処理の部分失敗をレポート生成完了時にまとめて検知・通知できる仕組みも検討できるとよさそうです。

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


---

## 2026-09-09 現状と残作業

Windows案内の作業窓口をこのIssueに集約し、旧 #287 / #254 はここへの統合としてcloseします。過去の本文・コメントは調査記録として残します。

- 現行の正本は `docs/getting-started/windows-setup.md`。PR #929 が対象環境・キー要件・起動前後の確認・失敗時の分岐を修正しています（CI成功、未merge）。
- ZIP配布とsetup_win.batを使うユーザー経路、Gitからcloneして開発する経路を混同しない。Git/PATH・改行・envの置き場等は該当する開発経路へ案内する。
- 非Docker/nativeの経路選択とREADME全体の整理は #876、単一実行ファイル化は #885 / draft PR #891 で追跡する。
- 古いコメント内の環境依存の回避策を、検証済みの標準手順として扱わない。Windows実機の全経路検証が済んだとはしない。


**コメント:** なし

---

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

### [[FEATURE] 広聴AIで作成したレポートを誤って解釈をしないようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/696)

**作成者:** shingo-ohki  
**作成日:** 2025-08-21T08:09:56Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

[広聴AI開発定例 2025/8/20](https://docs.google.com/document/d/1plggszRTxEEYUcZuCLiHkPrBsMtxr3RQpctKtZe5y4M/edit?tab=t.0#heading=h.yyt1ivvnrs0q) 内でレポートの解釈の仕方について話題になり、その辺りの説明が必要ではないか？という話になった

> 中山心太（tokoroten）
  [21:11](https://dd2030.slack.com/archives/C08F7JZPD63/p1755691873351029)
[【参院選】「AI分析で民意を可視化」の落とし穴…“数”は無意味？“サイエンス風”に惑わされないために｜アベヒル](https://www.youtube.com/watch?v=0_wIbDMvpMg)
公聴AIを使う場合、どういうふうなデータが得られて、どういうふうに偏っているのかはこの動画が詳しいので、おすすめです。
NISHIO Hirokazu
  [21:14](https://dd2030.slack.com/archives/C08F7JZPD63/p1755692086840979)
いっそおすすめ動画として広聴AIのWebサイトに載せたらいいのかも
中山心太（tokoroten）
  [21:29](https://dd2030.slack.com/archives/C08F7JZPD63/p1755692945671519)
良くも悪くも、中核メンバーがデータ分析者すぎるので、クセを分かってたわけだけど、
そこから一般に広がっていく過程で、その暗黙の前提知識が失われたせいで、誤った分析がなされるというのが起こっているので、なんとかしたいですね。 （編集済み） 
中山心太（tokoroten）
  [00:04](https://dd2030.slack.com/archives/C08F7JZPD63/p1755702294919739)
広聴AIの性質と、データの読み方、何が得られるのか、追加調査の考え方、みたいなのが整理できるといいな
[00:05](https://dd2030.slack.com/archives/C08F7JZPD63/p1755702301469099)
当たり前すぎて気づいてなかった
[21:31](https://dd2030.slack.com/archives/C08F7JZPD63/p1755693063767919)
書籍化するなら、↑の動画の二人に寄稿してもらえんかなー、公聴AIの限界やクセと言う話で。
[ブロードリスニングはノイジーマイノリティを積極的に拾ってしまうので、選挙に使う場合は注意が必要](https://scrapbox.io/dd2030/%E3%83%96%E3%83%AD%E3%83%BC%E3%83%89%E3%83%AA%E3%82%B9%E3%83%8B%E3%83%B3%E3%82%B0%E3%81%AF%E3%83%8E%E3%82%A4%E3%82%B8%E3%83%BC%E3%83%9E%E3%82%A4%E3%83%8E%E3%83%AA%E3%83%86%E3%82%A3%E3%82%92%E7%A9%8D%E6%A5%B5%E7%9A%84%E3%81%AB%E6%8B%BE%E3%81%A3%E3%81%A6%E3%81%97%E3%81%BE%E3%81%86%E3%81%AE%E3%81%A7%E3%80%81%E9%81%B8%E6%8C%99%E3%81%AB%E4%BD%BF%E3%81%86%E5%A0%B4%E5%90%88%E3%81%AF%E6%B3%A8%E6%84%8F%E3%81%8C%E5%BF%85%E8%A6%81)
書いておきました。
youkiti
  [今日 10:29](https://dd2030.slack.com/archives/C08F7JZPD63/p1755739749894699?thread_ts=1755738362.393659&cid=C08F7JZPD63)
理論的な基盤としてはこういうのがありますね
「ブロードリスニング」は、質的な調査
https://www.jstage.jst.go.jp/article/hokenshikyouiku/5/1/5_7/_pdf/-char/ja
中山心太（tokoroten）
  [今日 10:44](https://dd2030.slack.com/archives/C08F7JZPD63/p1755740657846419?thread_ts=1755738362.393659&cid=C08F7JZPD63)
データ分析を生業にしている人は、ブロードリスニングは質的調査、定性分析ツールだというのが分かっているんですが、
そこから一般に広がるにあたって「なんとなく説得力を産むツール」に変貌してしまっていて、そこで問題が起きてる感じですね
Shingo OHKI
  [今日 10:48](https://dd2030.slack.com/archives/C08F7JZPD63/p1755740894940289?thread_ts=1755738362.393659&cid=C08F7JZPD63)
「課題発見ツールです」と言い切ってしまった方がよいのかも？
[10:51](https://dd2030.slack.com/archives/C08F7JZPD63/p1755741075506609?thread_ts=1755738362.393659&cid=C08F7JZPD63)
可視化ツールに見えるから、説得力を持たせたくなる？
中山心太（tokoroten）
  [今日 10:51](https://dd2030.slack.com/archives/C08F7JZPD63/p1755741119292499?thread_ts=1755738362.393659&cid=C08F7JZPD63)
画像になるから説得力を利用者が感じてしまって、それが「良い分析である」と勘違いしてしまっていることですね
Shingo OHKI
  [今日 11:11](https://dd2030.slack.com/archives/C08F7JZPD63/p1755742305951539?thread_ts=1755738362.393659&cid=C08F7JZPD63)
クラスタをすべて同じ形と大きさの領域で表すようにしてそれをただ並べただけの画像にしたらミスリードは少なくなりそうな気がしました
[11:13](https://dd2030.slack.com/archives/C08F7JZPD63/p1755742412988739?thread_ts=1755738362.393659&cid=C08F7JZPD63)
それがこれなのかな
[11:14](https://dd2030.slack.com/archives/C08F7JZPD63/p1755742454819579?thread_ts=1755738362.393659&cid=C08F7JZPD63)
ラベルのところだけの羅列でもよさそうな
Shingo OHKI
  [今日 11:26](https://dd2030.slack.com/archives/C08F7JZPD63/p1755743196948079?thread_ts=1755738362.393659&cid=C08F7JZPD63)
ただ、なんとなく見栄えがいいから興味を持つということもありそうなので、難しいですね
中山心太（tokoroten）
  [今日 11:29](https://dd2030.slack.com/archives/C08F7JZPD63/p1755743349725199?thread_ts=1755738362.393659&cid=C08F7JZPD63)
なので、言い方が悪いですが、有権者へのアピールと、内部利用の分析は方針を分けないといけないわけですが、それを混同するから問題が起こるわけです。
ここら辺の注意書き、誰かに清書してもらって、プロダクトの中に組み入れてほしい。

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
やり方はいろいろありそう
- README などのドキュメントに入れる
- プロダクトの中に組み入れる
- 事例とともに website に載せる
- 解説記事を書く、書籍化する

**コメント:** なし

---

### [[REFACTOR] ts-node-dev はメンテナンスされなくなっているようなので別パッケージに変えたほうがいいかもしれない](https://github.com/digitaldemocracy2030/kouchou-ai/issues/690)

**作成者:** noritaka1166  
**作成日:** 2025-08-05T10:06:06Z  
**内容:**

# 現在の問題点
client-static-build で使用している [ts-node-dev](https://www.npmjs.com/package/ts-node-dev) ですが、  
最終更新から 3年以上経過しています。  
メンテナンスされているかを issue で確認している方がいて、ownerが別のパッケージを勧めているように見えるため、別パッケージに変えたほうがいいかもしれません。
<https://github.com/wclr/ts-node-dev/issues/348>

# 提案内容
個人的には [nodemon](https://www.npmjs.com/package/nodemon) を使用するのがいいのではないかと思っていますが、  
ts-node-dev の owner がおすすめしている [tsx](https://www.npmjs.com/package/tsx) を使うのもいいかもしれません。


**コメント:** なし

---

### [[FEATURE]タイトルや概要空欄の状態でCSVをD&Dしたときファイル名を入れる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/639)

**作成者:** nishio  
**作成日:** 2025-07-08T09:03:05Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
たくさんのCSVを分析処理するときに、CSVの名前に合わせて間違えない様に同じ名前をタイトルに入れる作業が手間

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
タイトルや概要空欄の状態でCSVをD&Dしたときファイル名から.csvを除いたものを空欄のところに入れる、空欄でないなら何もしない

**コメント:** なし

---

### [[FEATURE] データの有無に応じた UI のパターンを確認しやすくする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/566)

**作成者:** shgtkshruch  
**作成日:** 2025-05-23T09:39:49Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

- データの有無に応じた UI のパータンが増えてきた
  - #428
      - レポートが0件 or 1件以上
  - #438
    - metadata.json のデータの有無
- 自分はこれらの UI パターンを実装する際に、サーバーから取得するデータを変更したり、コード上で条件分岐を変えたりしているのですが、これが少し手間だなと思っています
- デザイナーがデータの有無で表示が切り替わる UI を確認する際にも、データを作ったり or 消したりする必要がありそうです
  - 例えばレポート一覧画面の Empty State を確認する場合は、レポートを0件にするなど


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
- [Storybook](https://storybook.js.org/) でデータがある場合の UI・データない場合の UI を登録して、サーバーのデータを変更することなくそれぞれの UI を確認できるようにする
   - 他にも UI をパターンごとに登録できるツールがあれば、そちらでも良いと思います
   - こういったツールがあると、エンジニアは手軽に手元で UI のパターンを確認できるようになりそうです
   - 導入する場合でも Storybook の実装・メンテナンスコストは多少かかるので、コストとメリットの比較は必要だと思います

# その他
- デザイナーがデータの有無に応じた UI を確認できるようにする場合は、Storybook など UI をカタログ化したものをホスティング環境もあると良さそうです
  - この場合はこの issue の解決が前提になるので、この issue が対応できてから必要があれば別 issue を切るでも良いかなと思いました
   - Chromatic (5000 snapshot まで無料), GitHub Pages, Netlify, etc...

**コメント:** なし

---

### [[design]レポート詳細>階層図にてグラフ下の説明文を階層図の内容に変更](https://github.com/digitaldemocracy2030/kouchou-ai/issues/528)

**作成者:** nanaueki  
**作成日:** 2025-05-17T09:55:02Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
目的：UXの向上
全体図、濃い意見グループで内容が切り替わるが、階層図は全体図の内容が表示される。
グラフの内容とグラフ下の説明文の文脈が異なる、グラフと説明の不一致でユーザーが混乱するため、
グラフホバー時に表示される、各階層の解説が表示される方が望ましい。

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
デザイン案は後日追加

該当画面
https://kouchou-ai.dd2030.org/5f0b335c-e07c-40e2-bce8-eca275da44ca/

表示内容
- タイトル
- 件数
- 全体に対する割合
- 詳細テキスト 

期待する動作
- テキストリンクタップで、該当する第二階層グラフに遷移（全体図の動作も変更する必要あり）


**コメント:** なし

---

### [[FEATURE] Extructionで並列実行した結果をソートしてから保存する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/514)

**作成者:** tokoroten  
**作成日:** 2025-05-14T00:38:18Z  
**内容:**

# 背景

同じ入力データを用いても、実行するたびに結果が異なる。

機械学習関連はSeed値が利用されているため、機械学習関連の問題である可能性は低い。

LLMはseedが固定されている。
```python
            payload = {
                "model": model,
                "messages": messages,
                "temperature": 0,
                "n": 1,
                "seed": 0,
                "timeout": 30,
            }
            if response_format:
                payload["response_format"] = response_format

            response = openai.chat.completions.create(**payload)
```


UMAPはrandom_stateでseedが固定されている。
`umap_model = UMAP(random_state=42, n_components=2, n_neighbors=n_neighbors)`

k-meansも同じ
`  kmeans_model = KMeans(n_clusters=initial_cluster_num, random_state=42)`


残っている可能性としては、LLMに対するリクエストの並列実行の結果、応答順序が異なり、結果の順序が変わることだと考えられる。
そして、UMAPに対する入力データの順序が毎回変わっているのだと思われる。結果として、Umapの結果が毎回異なる、ということになっていると考えられる。

# 提案内容

並列実行された結果が帰ってくる順序によって、データの並びが異なると考えられる。
コードはおそらくこの辺
https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/server/broadlistening/pipeline/steps/extraction.py


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

### [[REFACTOR] Azureのモデル選択の不整合の修正](https://github.com/digitaldemocracy2030/kouchou-ai/issues/477)

**作成者:** nasuka  
**作成日:** 2025-05-11T00:28:46Z  
**内容:**

# 現在の問題点
* 通常のOpenAIと異なり、Azure OpenAI を使う場合は事前にリソース（LLM・embedding）をデプロイしておく必要があり、APIを呼び出す際にモデル名だけでなくリソースに紐づく情報を渡す必要がある
  * [このあたり](https://github.com/digitaldemocracy2030/kouchou-ai/blob/a167a548ecba9b7b9fd279e5ea9a4f745bb3c550/.env.example#L63-L71) の環境変数でセットしている情報
* 現在のモデル作成時のUIでは、リソースの有無にかかわらず一律で3つのモデルが表示されるようになっている
   * ここで選択されたモデルは実際には使われず、環境変数で指定したモデルが使われるため利用モデルの不整合が起きている

![Image](https://github.com/user-attachments/assets/aab703d5-bc48-4055-a27f-5726bceb6d94)

# 提案内容
* （ライトに解決する案）Azure利用の場合はAdmin上ではモデルを選択できないようにする
  * モデル選択のセレクトボックスをグレーアウトし、Azure利用の場合は環境変数でセットしたモデルが使われる旨を表示する
* （ちゃんとやる案） LLMのdeployments の一覧をAPI経由で取得し、モデル選択肢のセレクトボックスで選択できるようにする
  * API自体はありそう
    * https://chatgpt.com/c/681fed08-3be4-800f-aca0-3ebaac6fed6f




**コメント:** なし

---

### [[FEATURE] 環境検証ページに、Azure、OpenRouter、LocalLLMを付ける](https://github.com/digitaldemocracy2030/kouchou-ai/issues/473)

**作成者:** tokoroten  
**作成日:** 2025-05-10T15:31:10Z  
**内容:**

# 背景

Client-adminの環境検証ページは、LLMプロバイダーの選択肢を作る前に作成されたものなので、ChatGPTしか対応していない。

![Image](https://github.com/user-attachments/assets/53ef974a-7cae-4be4-a43d-f62b7999833e)

# 提案内容

- Azureの環境確認
- OpenRouterの環境確認
- LocalLLMの環境確認


**コメント:** なし

---

### [[FEATURE]LLM呼び出しのタイムアウトを変更できるようにしてほしい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/452)

**作成者:** take365  
**作成日:** 2025-05-07T10:17:06Z  
**内容:**

# 背景
ローカルLLM（ためにOpenaaiのAPIでも）API呼び出しでタイムアウトしてしまうことがあるので、現状の３０秒固定から変更できるようにしてほしい


# 提案内容
案
１．作成画面（詳細設定）で変更できるようにする
２．.envで変更できるようにする


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

### [E2Eテスト導入計画 (E2E Testing Implementation Plan)](https://github.com/digitaldemocracy2030/kouchou-ai/issues/379)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-25T10:56:23Z  
**内容:**

# E2Eテスト導入計画 (E2E Testing Implementation Plan) - 更新

## 概要 (Overview)
レポート作成時に編集したプロンプトが反映されないバグのような状態管理の問題を早期に検出するため、E2Eテストを導入します。コスト効率と保守性を考慮した段階的なアプローチを取ります。

## 目的 (Goals)
- 重要なユーザーフローの動作を自動的に検証する
- リファクタリングによる回帰バグを早期に発見する
- 開発者の負担を最小限に抑えつつ、品質を向上させる

## アプローチ (Approach)
- Playwrightを使用したE2Eテスト
- 重要なフローに絞ったテスト作成
- 1日1回の全テスト実行 + PRラベルによる選択的実行
- Devinによるテストメンテナンス自動化

## 実装計画 (Implementation Plan)

### 現在進行中のサブイシュー
- [#380 基本的なE2Eテスト環境構築](https://github.com/digitaldemocracy2030/kouchou-ai/issues/380)

### 将来の実装メモ（サブイシューではなく参考情報として）
以下の項目は、最初のステップ（#380）で得られる知見を元に、必要に応じて調整・実装していきます。

#### 2. プロンプト編集テスト実装
- プロンプト編集の永続性テスト
- ページ内ナビゲーション後のプロンプト保持テスト
- エラー発生時のプロンプト保持テスト

#### 3. 基本的なユーザーフローテスト実装
- CSVファイルによるレポート作成テスト
- スプレッドシートによるレポート作成テスト

#### 4. テストメンテナンス自動化
- テスト失敗の自動検出
- Devinによる修正PR作成ワークフロー
- テスト結果レポート自動化

#### 5. 開発者ガイドライン作成
- E2Eテスト実行方法ドキュメント
- テスト追加・修正ガイドライン
- テスト失敗時のトラブルシューティング

## 実装順序 (Implementation Order)
1. 基本環境構築（最小限のテストで検証）- 進行中 #380
2. プロンプト編集テスト（今回のバグ対策）
3. 基本フローテスト（主要機能の保護）
4. メンテナンス自動化（持続可能性の確保）
5. ドキュメント整備（開発者体験の向上）

## 注意点 (Considerations)
- テストの安定性を重視（不安定なテストは無効化）
- セレクタは壊れにくい方法で指定（ID属性など）
- テスト失敗時の詳細なレポート生成
- コントリビュータへの影響を最小化

## 関連Issue
- #375 （プロンプト編集バグ）
- #377 （リファクタリングのrevert）
- #380 （基本的なE2Eテスト環境構築）


**コメント:** なし

---

### [[DOCUMENT] 元データの特徴に合わせたextractionプロンプトのガイドライン](https://github.com/digitaldemocracy2030/kouchou-ai/issues/367)

**作成者:** mtane0412  
**作成日:** 2025-04-23T13:46:14Z  
**内容:**

# 背景
extractionで「意見を抽出するプロンプト」で「意見」を抽出できなかったときに、few-shotの文が出てきたり意見を作ってしまう現象が既知の問題としてある。
2025/4/23 段階ではプロンプトよって改善可能であるという意見が多かった。
システムが自動で消してしまうのもよくないという意見があった。

ユーザーがプロンプトを改善できるガイドラインのようなものがあってもいいという発言があったと思い、同じ意見なのでissueにしておく

> extractionの品質の管理は課題として認識していたりします。
> 多くの利用者の信頼感を高めるうえでは大事になりそう。
> 
> なるほど、意見のないものから意見を抽出しようとしているのか...(nishio)
> クレンジングか、few-shot promptですね
> 意見抽出ツールを意見抽出でないことに使おうとしてるので汎用的に品質向上は難しいからユーザのブロンプトを調節するのがいちばん筋だと思う
> システムとして自動的に消すのはよくないのではという議論、そうだと思う、何がゴミで何が取りたいものかを決めるのは受け取り手が決めるものなので我々が決めることではない
> パンプキンパイのレシピが混ざってたら、たくさんの意見として抽出された(tanenobu)
> 不思議な出力を選択して元コメントを調べたり、それらをログ的に出力できると改善にまわせそう
> 私も標準でやったときに結構盛られましたわ。(kitaro)

![](https://i.gyazo.com/3e07293e28f06c3e3404b8db045774a6.png)

> こういう入力が来るなら、few-shotでキーワードを抽出するように指示すればいいと思う(nishio)
> いまはサンプルとして「意見のリスト」を返すように指示しているから、意見が生成される。キーワードのリストを返せと例示すればキーワードのリストが返る。

> アプローチはプロンプトだけなのか、など相談できれば。
> (nasuka)デフォルトのプロンプトで上記の事象が発生してるんでしょうか？基本的にはプロンプト改善 or  モデルの変更で> 対処するのが良さそうで、ルールベースで弾く機能を入れるのも案としてはあると思います
> 元のコメントよりも明らかに文字数が増えている場合は弾くなど
> （LLMでチェックするプロセスを入れることも可能だが、解決策としてはオーバーな気がする）
> (nishio)デフォルトのプロンプトで、十分賢いモデルならこうはならないのではという気もするが、とはいえ起きてるのであれば、ごく短い入力に関してはもっと「空リストを返す」という振る舞いをするようにプロンプトを変えてもいいかもですね
> ブロンプトの試行錯誤がやりやすくなる機能はあるとベターではある
> うまくいってない入力と出力のペアが集まると色々やりやすくはなると思います(nishio)
> たとえば上記CSVをo3にぶちこんで不適切な抽出だと思うものを取り出してもらうとか


# 提案内容
うまくいっていない例を収集する仕組みや活動が必要
> 不思議な出力を選択して元コメントを調べたり、それらをログ的に出力できると改善にまわせそう
> うまくいってない入力と出力のペアが集まると色々やりやすくはなると思います(nishio)

収集したものをもとにガイドライン的なドキュメントにまとめる。
(UIにも組み込むとよいと思いましたが、まずはドキュメント化が先かなと思いました。)

**コメント:** なし

---

### [[FEATURE] 意見を抽出できなかったときのエラーハンドリング](https://github.com/digitaldemocracy2030/kouchou-ai/issues/318)

**作成者:** mtane0412  
**作成日:** 2025-04-17T02:28:08Z  
**内容:**

# 背景
XのポストやSteamのレビューなどで試しているときに、extractionの段階で大量の `ERROR:root:Task <Future at 0xffff7d57f470 state=finished raised RuntimeError> failed with error: JSON list not found` が出ます。
おそらくコメントの中から意見を抽出できないことが多いと推測。(違ったら教えて下さい。)

実運用ではまとまった意見のデータが使われると思いますが、レポート作成者が「抽出段階でよくわからないエラーが出ている」という体験がありそうかなと思いました。

#315 が実装された場合に向けてログのノイズを減少させる。

# 提案内容
意見が抽出できなかった場合、元コメントと併記して意見が抽出できなかったことをログ出力する。

**コメント:** なし

---

### [[FEATURE]CSVアップロード時にタイトルや説明文を自動で埋めてほしい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/305)

**作成者:** masatosasano2  
**作成日:** 2025-04-13T07:45:30Z  
**内容:**

# 背景
入力の一手間を減らしたい
入力漏れでエラーにならないでほしい

# 提案内容
- タイトルと説明文を optional にする
- 空の場合にCSVの内容から自動生成する　※説明文は必須でないかも

**コメント:** なし

---

### [[FEATURE]ラベルが多い時の重なりの問題](https://github.com/digitaldemocracy2030/kouchou-ai/issues/294)

**作成者:** nishio  
**作成日:** 2025-04-13T00:59:47Z  
**内容:**

## 課題

広聴AIのレポート画面に表示されるプロットグラフにおいて、分析によって生成されたクラスタ（意見グループ）の数が多い場合に、各クラスタを示すラベルが互いに重なり合ってしまい、判読が困難になるという問題があります。

特に、自治体での利用など、詳細な分析のためにクラスタを細かく分ける傾向がある場合に、この見にくさが顕著になります。
> 「自治体的には、クラスタを細かく分ける方向の議論が強い。」
> 「UIの観点で、プロットグラフがそれに対応していけるとよさそう。」
> 「ラベルは重なって見にくくならないようにできるとか」

現状のままでは、せっかく詳細に分類された意見グループの内容を、グラフ上で直感的に把握することが難しくなっています。

## 解決策案

グラフ上でのラベルの重なりを軽減し、視認性を向上させるために、以下のいずれか、または組み合わせによる改善策を検討します。

*   **ラベル表示の選択的ON/OFF:** ユーザーが表示したいラベルを選択したり、一定数以上のラベルはデフォルトで非表示にする機能を追加する。
    > 「ラベル全部は表示しない設定」
*   **重なり回避アルゴリズムの導入:** ラベルの位置を自動的に調整し、重なりを最小限に抑えるアルゴリズムを実装する。
*   **インタラクティブなラベル操作:** ユーザーがグラフ上でラベルをドラッグ＆ドロップして任意の位置に移動できるようにする。
*   **ズームレベルに応じた表示制御:** グラフの拡大率に応じて、表示するラベルの数を調整する（例: 縮小時は主要なラベルのみ表示）。

**コメント:** なし

---

### [[DOCUMENT]Windows向けのセットアップ手順](https://github.com/digitaldemocracy2030/kouchou-ai/issues/287)

**作成者:** nishio  
**作成日:** 2025-04-13T00:02:52Z  
**内容:**

# 現在の問題点
<!-- 現在のコードの何が問題なのか、どのような技術的負債があるかを説明してください -->

## 課題

現在の `README.md` は主にUNIX系（Linux, macOS）環境を前提としており、Windowsユーザーが広聴AIをセットアップする際に特有の課題に直面することが多いです。

*   **必須ツールのインストールと設定:** Docker DesktopやGit for Windowsのインストール、特に環境変数Pathの設定 (`'git' は、内部コマンドまたは外部コマンド...`) やWSL連携で躓く可能性がある。
*   **改行コードの問題:** クローン時に適切に対応しないと、シェルスクリプト (`entrypoint.sh`) 実行時にエラーが発生する。
*   **コマンドの違い:** `cp` コマンドなど、コマンドプロンプトとPowerShellでの違いに戸惑う可能性がある。
*   **隠しファイル:** `.env` ファイルがデフォルトで非表示のため、作成・編集時に混乱が生じやすい。
*   **Docker関連のエラー:** `npm ci` エラー、ポート競合 (`port is already allocated`)、証明書エラーなど、Windows環境固有または頻出する可能性のあるエラーへの対処法が不明確。

これらの問題により、特に非エンジニアやITスキルに不安のあるWindowsユーザーにとって、導入のハードルが高くなっています。「WindowsユーザーはDocker Desktopのダウンロードからはじまる」「GithubのREADMEは現在UNIX系前提?」「'git' は、内部コマンドまたは外部コマンド...」「パスを通すという困難な作業」「entrypoint.shの5行目でエラー。改行コードの関係」「.env見つからない」「Powershellでないとないかも。cmdではない」

## 提案

Windowsユーザー向けの専用セットアップガイドを `README.md` に追記、または別ドキュメントとして作成する。

**含めるべき内容:**

1.  **必要なソフトウェア:**
    *   Docker Desktop (インストール方法、wingetコマンド例、注意点: セキュリティポリシー、WSL/ログインエラー)
    *   Git for Windows (インストール方法、wingetコマンド例、**Path設定の重要性**、確認方法)
    *   (推奨) テキストエディタ (VSCodeなど)
2.  **セットアップ手順:**
    *   リポジトリのクローン (**`--config core.autocrlf=false`** オプションの明記)
    *   `.env` ファイルの作成 (Windowsコマンド: `copy` / `cp`、**隠しファイル問題**とVSCodeでの編集推奨)
    *   アプリケーションの起動 (**`docker compose up`** コマンドの明記、初回ビルド時間について)
3.  **よくある問題と対処法 (Windows向け):**
    *   `git` コマンドが見つからない → Path設定の確認
    *   `entrypoint.sh` エラー → 改行コード問題の確認と再クローン
    *   `npm ci` エラー → (現状考えられる原因や再試行)
    *   証明書エラー → セキュリティソフトの確認
    *   ポート競合エラー → 他コンテナ停止 or ポート変更
    *   `.env` ファイルが見つからない → 隠しファイル設定 or VSCode利用
    *   コマンドの違い (`cp` vs `copy`)
4.  **トラブルシューティングTips:**
    *   エラーメッセージをLLMに質問するなどの自助努力の方法提示

これにより、Windowsユーザーがスムーズにセットアップを完了できるよう支援し、利用者の裾野を広げることを目指します。

# 仮原稿
## はじめに
このドキュメントは、Windows環境で広聴AIのセットアップを行うユーザー向けの手順と注意点をまとめたものです。現在の公式READMEは主にUNIX系（Linux, macOS）環境を前提としているため、Windows特有の考慮事項があります。

## 必要なソフトウェア
セットアップには以下のソフトウェアが必要です。事前にインストールしてください。

1.  **Docker Desktop:**
    *   公式サイトからダウンロードしてインストールします。
    *   `winget install -e --id Docker.DockerDesktop` コマンドでもインストール可能です。
    *   インストール後、Docker Desktopを起動し、必要な初期設定（WSL連携など）を完了させてください。
    *   **注意:** 自治体PCなどでは、セキュリティポリシーによりインストールが許可されていない場合があります。情報システム部門にご確認ください。
    *   **注意:** Googleアカウントでのログイン時やWSLアップデート時にエラーが発生することが報告されています。エラーメッセージに従って対処するか、IT管理者に相談してください。「Docker、Googleアカウントにてログイン時にエラー。」「wsl update failed: update failed: updating wsl: exit code: 1...」

2.  **Git for Windows:**
    *   公式サイトからインストーラーをダウンロードしてインストールします。「Git for Windows Portable」ではなく、通常のインストーラー版を使用してください。
    *   `winget install -e --id Git.Git` コマンドでもインストール可能です。
    *   **重要:** インストール中に「Adjusting your PATH environment」の項目で、「Git from the command line and also from 3rd-party software」を選択することを推奨します。これにより、コマンドプロンプトやPowerShellから `git` コマンドが利用可能になります。
    *   **パス設定確認:** インストール後、コマンドプロンプトまたはPowerShellを開き、`git --version` を実行してバージョン情報が表示されればOKです。表示されない場合（「'git' は、内部コマンドまたは外部コマンド...として認識されていません。」エラー）、環境変数のPathにGitの実行ファイルパス（例: `C:\Program Files\Git\cmd`）を手動で追加する必要があります。「パスを通すという困難な作業」 - 不明な場合はChatGPT等で「Windows 環境変数 パス 通し方」などで検索・質問してください。

3.  **(推奨) テキストエディタ:**
    *   VSCodeなどのテキストエディタがあると、設定ファイルの編集に便利です。

## セットアップ手順

1.  **リポジトリのクローン (改行コード問題対策):**
    *   コマンドプロンプトまたはPowerShellを開き、作業したいディレクトリに移動します。
    *   以下のコマンドを実行して、リポジトリをクローンします。`--config core.autocrlf=false` オプションは、WindowsとLinux/macOS間の改行コードの違いによるエラー (`entrypoint.sh` 関連など) を防ぐために重要です。
        ```bash
        git clone --config core.autocrlf=false https://github.com/digitaldemocracy2030/kouchou-ai.git
        ```
    *   クローンした `kouchou-ai` ディレクトリに移動します。
        ```bash
        cd kouchou-ai
        ```

2.  **環境設定ファイルの作成:**
    *   `example.env` ファイルをコピーして `.env` ファイルを作成します。PowerShellでは以下のコマンドで実行できます。
        ```powershell
        cp example.env .env
        ```
        (コマンドプロンプトの場合は `copy example.env .env`)
    *   **注意:** `.env` は隠しファイル属性が付くことがあります。Windowsのエクスプローラーで表示されない場合は、「表示」タブ -> 「隠しファイル」にチェックを入れるか、VSCodeなどのエディタで `kouchou-ai` フォルダを開いて `.env` ファイルを編集してください。「.env見つからない」「隠しファイルをfinderで開こうとしていた」
    *   `.env` ファイルを開き、OpenAI APIキーなどの必要な設定値を記述します。

3.  **アプリケーションの起動:**
    *   Docker Desktopが起動していることを確認します。
    *   `kouchou-ai` ディレクトリ内で、以下のコマンドを実行します。**ハイフンなしの `docker compose up` を使用してください。**
        ```bash
        docker compose up
        ```
    *   初回起動時は、Dockerイメージのダウンロードとビルドに時間がかかります（数分～十数分程度）。「Docker imageがない状態でdocker compose upすると500s以上かかる」
    *   ビルドと起動が正常に完了すると、ログの最後に `Application startup complete.` のようなメッセージが表示され、Webブラウザで `http://localhost:3000` (Admin Dashboard) と `http://localhost:5173` (レポート画面) にアクセスできるようになります。

## よくある問題と対処法

*   **`git` コマンドが見つからない:**
    *   Git for Windowsのインストール時にパス設定が適切に行われなかった可能性があります。上記「必要なソフトウェア」のGitの項目を確認し、環境変数Pathを修正してください。
*   **`entrypoint.sh` 関連のエラー:**
    *   改行コードの問題である可能性が高いです。上記「リポジトリのクローン」の手順に従い、`--config core.autocrlf=false` オプション付きでクローンし直してください。
*   **`docker compose up` 中の `npm ci` エラー:**
    *   `[client-admin builder ... ] RUN npm ci` でエラーが発生する場合があります。(ログ参照) 根本的な解決策はログに記載されていませんが、ネットワーク環境やDockerのリソース割り当てなどが影響している可能性があります。時間をおいて再試行するか、Docker Desktopの設定を見直してください。
*   **`docker compose up` 中の証明書エラー (`uv` など):**
    *   会社のセキュリティソフトなどがDocker内の通信をブロックしている可能性があります。「自治体のセキュリティによってuvのインストール時に証明書エラーがおきた」一時的にセキュリティソフトを無効にするか、Docker関連の通信を許可する設定を行ってください。
*   **`Bind for 0.0.0.0:3000 failed: port is already allocated` エラー:**
    *   ポート3000が他のアプリケーション（他のDockerコンテナ等）によって既に使用されています。「原因：3000ポートをすでに使っているdocker containerが立ち上がっていた」他のアプリケーションを停止するか、`.env` ファイルで `APP_PORT` を別の番号（例: `3001`）に変更してください。
*   **`.env` ファイルが見つからない/編集できない:**
    *   隠しファイルになっている可能性があります。上記「環境設定ファイルの作成」の注意点を確認してください。VSCodeでフォルダを開くのが確実です。
*   **コマンドプロンプトで `cp` コマンドが使えない:**
    *   `cp` はPowerShellのコマンドです。コマンドプロンプトでは `copy` を使用してください。もしくはPowerShellを起動して作業してください。「Powershellでないとないかも。cmdではない」

## トラブルシューティングTips
*   エラーが発生した場合、表示されたエラーメッセージ全体をコピーし、ChatGPTなどのLLMに貼り付けて「このエラーの原因と解決策を教えてください」と質問すると、具体的な解決策が見つかることがあります。「エラーが出たら内容張り付けて「エラーでた助けて」といえばほぼほぼ解決もしてくれます。」


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

### 過去7日間に作成されたissue (4件)

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

### [ブラウザ版（kouchou-ai-serverless）を広聴AIの本流とするかの議論](https://github.com/digitaldemocracy2030/kouchou-ai/issues/921)

**作成者:** nishio  
**作成日:** 2026-09-08T08:05:28Z  
**内容:**

## 背景

広聴AI×いどばた合同ミーティングの[事前まとめドキュメント](https://docs.google.com/document/d/1Wl5xCUkv2U8MkhW8-wLWr5TuLcDIpY2SFAnneKYL6Rk/)（2026年8月〜）で、次の提案が出ました。

- @tokoroten さんが広聴AIをペライチのHTMLにした [kouchou-ai-serverless](https://tokoroten.github.io/kouchou-ai-serverless/) を公開
  - 設定画面から OpenAI API Key を差し込むだけで動く
  - Chrome 内蔵の Gemini Nano を使えば無料で動作する
- tokorotenさん「これを広聴AIの本流とするのが良いんじゃないかなぁと思っている」
- 西尾も「研究者やデータサイエンティストでないライトなユーザにとってはこの方向性が良いと思う（インストールのトラブルがなくなるので）」と同意

ただしこれは2人の意見が一致しただけで、広聴AIチームとしての意思決定はまだ行われていません。このIssueを非同期の議論の場として立てます。

## 論点

1. **「本流」の意味を定義する**: README等の導線でブラウザ版を第一に案内する / 開発リソースの重心を移す / リポジトリ統合する、のどこまでを指すか
2. **既存版（Docker / Azure デプロイ）のポジション**: 大規模データ・自治体イントラ（LGWAN）・API Keyをエンドユーザに渡せない運用など、ブラウザ版でカバーできないケースの整理
3. **プラグインシステム構想との関係**: v5.0で進めている「コンポーネント間インターフェイスの明確化・部品の交換可能性」とブラウザ版の関係をどう設計するか
4. **手法の使い分け**: 事前まとめでは「小規模データは long-context LLM に全部入れる方が一般人に理解しやすい結果が出る」「制約のあるユーザには embedding ベースの価値が残る」という整理も出ており、ブラウザ版がどちらをどこまで担うか

## 提案

- まずこのIssueで非同期に意見を集める
- 鈴木健さんから提案されている広聴AIの戦略会議（9月以降）の議題に載せる

---
*この Issue は合同ミーティング事前まとめの議論を前に進めるため、西尾がAIエージェントの支援で作成しました。*


---

## 2026-09-09 現状と残作業

判断材料を更新します。チームとしての本流化・移管の結論は未決のままです。

- 入力と失敗検知: 本体PR #923（main済み）とServerless PR #23でCSVの判定を揃え、本体PR #928とServerless PR #26で抽出失敗・正常0件・原文付き診断の公開範囲を整理しました。
- 閲覧と根拠: 本体PR #927 / #933、Serverless PR #25 / #26で階層図・スマホ・日本語表示を同期。元コメント参照の正確さはServerless PR #22、公開用と再分析用の契約は #56 が次の候補です。これらの新PRは未mergeです。
- 選択の入口: #876で目的と制約から利用経路を案内し、#79 / #11で費用・時間の不安を減らす。両版を使い分ける方針も検証仮説として扱います。

次に集めたい判断材料は、サンプル閲覧→CSV分析→持ち出し→別の人が読み、元の声を確かめて対話や判断に使うところまで、どこで支援が必要かという利用観測です。Issue件数や機能数だけを成果指標にしません。


**コメント:** なし

---

### [[TEST] Gemini 3.8 Flash / 3.5 Flash-Liteの実API動作を検証する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/913)

**作成者:** nishio  
**作成日:** 2026-09-07T16:02:06Z  
**内容:**

# 目的
#907 / #909で`gemini-3.8-flash` / `gemini-3.5-flash-lite`を「動作未確認」のまま選択肢へ追加する。実APIを使う動作検証と、カタログの検証済みフラグ更新をこのIssueで追跡する。未検証フラグは一覧追加を妨げない。

# 完了条件
- [ ] current mainの参照commit・SDK版・モデルID・日付と、匿名の固定小規模入力を記録する
- [ ] 抽出、初期ラベリング、統合ラベリング、概要の実schema / promptで応答を確認する
- [ ] 送信パラメーター（temperature、seed、reasoning/thinking等）とStructured Outputs互換性を確認する
- [ ] 空応答、refusal、安全フィルター、timeoutなどを正常な0件と混同しないことを確認する
- [ ] 入出力・思考tokenと料金推定の対応を確認する
- [ ] モデルごとの成功・失敗・制約を記録し、必要なadapter修正を行う
- [ ] 合格したモデルだけcatalogのverifiedをtrueにし、検証結果へのリンクを残す

実行前に利用アカウント・件数・費用上限を決める。API keyや個人データはIssueへ貼らない。ラベル品質の優劣比較は、この互換性試験の合否とは分ける。

# 実施担当

2026-09-08の西尾の指示により、実APIでの検証は人間が実施する。具体的な担当者は未定。Codexでの実API試験や、そのための認証情報の共有は求めない。検証結果が記録されるまではカタログの未検証フラグを維持する。


**コメント:** なし

---

### [[TEST] GPT-5.6 Terra / Lunaの実API動作を検証する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/912)

**作成者:** nishio  
**作成日:** 2026-09-07T16:02:04Z  
**内容:**

# 目的
#906 / #909で`gpt-5.6-terra` / `gpt-5.6-luna`を「動作未確認」のまま選択肢へ追加する。実APIを使う動作検証と、カタログの検証済みフラグ更新をこのIssueで追跡する。未検証フラグは一覧追加を妨げない。

# 完了条件
- [ ] current mainの参照commit・SDK版・モデルID・日付と、匿名の固定小規模入力を記録する
- [ ] 抽出、初期ラベリング、統合ラベリング、概要の実schema / promptで応答を確認する
- [ ] 送信パラメーター（temperature、seed、reasoning/thinking等）とStructured Outputs互換性を確認する
- [ ] 空応答、refusal、安全フィルター、timeoutなどを正常な0件と混同しないことを確認する
- [ ] 入出力・思考tokenと料金推定の対応を確認する
- [ ] モデルごとの成功・失敗・制約を記録し、必要なadapter修正を行う
- [ ] 合格したモデルだけcatalogのverifiedをtrueにし、検証結果へのリンクを残す

実行前に利用アカウント・件数・費用上限を決める。API keyや個人データはIssueへ貼らない。ラベル品質の優劣比較は、この互換性試験の合否とは分ける。

# 実施担当

2026-09-08の西尾の指示により、実APIでの検証は人間が実施する。具体的な担当者は未定。Codexでの実API試験や、そのための認証情報の共有は求めない。検証結果が記録されるまではカタログの未検証フラグを維持する。


**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(17件)

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

---

## 2026-09-09 現状と残作業

PR #925でAI補助開発の入口は整備されましたが、これはこのIssue全体の完了ではありません。README、quickstart、CLIの利用モードを横断するcanonicalな入口は引き続き必要です。

次の完了範囲は、初めての利用者が「既存レポートを読む／CSVを分析する／組織で運用する／Web UIを開発する／分析手法を実験する」から経路を選べる1ページを作り、READMEとdocs入口から辿れることです。Serverlessも候補に含めますが、本流化や移管の正式決定を前提にしません（#921）。

#877 / PR #929 はWindowsの標準経路、#496 はDockerを使えない場合の入口として接続します。旧草案の固定的な件数閾値・OS順位を無条件に採用せず、測定済みの範囲と未確認を明記します。


**コメント:** なし

---

### [活用事例を集めて公開する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/564)

**作成者:** shingo-ohki  
**作成日:** 2025-05-23T03:27:56Z  
**内容:**

（[website の Issue](https://github.com/digitaldemocracy2030/website/issues) には存在せず、website は現段階では定例が存在しないため、一旦、広聴AI側で Issue を立ててみる）

# 目的
これから広聴AIを利用しようとするユーザーからすると、様々な活用事例があると導入ハードルが下がる
事例を集めて公開する




---

## 2026-09-09 現状と残作業

次に集める事例の単位を「レポートが作れた」から「どの問いに使い、その後の対話・判断がどう変わったか」へ広げたいです。

公開事例には、対象の問い／収集方法と偏り／利用した版・分析方法／元の声との照合／読者が取った次の行動／うまくいかなかった点／出典と公開範囲を揃える案です。全項目が観測できていない事例も、未確認を区別して整理します。

#696の読み方ガイドはmain済み（PR #924）。#542の責任所在、#56の元コメント、#921の入口選択に接続します。公開ページがあることだけでこの継続的な収集・再利用の課題を完了扱いにはしません。


**コメント:** なし

---

### [[FEATURE] 再現性を選べる分析設定と比較条件を整理する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/513)

**作成者:** tokoroten  
**作成日:** 2025-05-14T00:18:23Z  
**内容:**

# 背景

同じデータを入力しても同じ結果にならない

# 提案内容

ランダムシードを設定する

---

## 2026-09-09 現状と残作業

現行main `2dd5adc` を再確認した結果、以前の「全箇所seed設定済み」を現在の完了根拠にはできません。

- 通常クラスタリングのUMAP・KMeans、LLM groupingのUMAPに固定random_stateはありません。固定seedの除去はcommit 8fa8ee71358b0705859b02d0ab2064a6aac260deによる意図的変更です。
- #809 は並列性と再現性の選択を扱っています。担当者の作業と重複して既定値を戻すのではなく、こちらでは「保存済みargs/embeddingsを比較する時に何を固定・記録するか」を詰めます。
- 残作業: 再現性が必要な利用場面、seedの入力・出力記録、版と依存関係、再利用artifactを定義し、同じ入力で比較できる回帰試験を設計する。LLM出力までの完全一致は保証対象にしません。

根拠: https://github.com/digitaldemocracy2030/kouchou-ai/blob/2dd5adc21103e880bf0250f29511f99a05c52590/packages/analysis-core/src/analysis_core/steps/hierarchical_clustering.py / https://github.com/digitaldemocracy2030/kouchou-ai/blob/2dd5adc21103e880bf0250f29511f99a05c52590/packages/analysis-core/src/analysis_core/steps/llm_grouping.py


**コメント:** なし

---

### [[DOCKER] なしでも動かせるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/496)

**作成者:** masatosasano2  
**作成日:** 2025-05-13T02:11:36Z  
**内容:**

# 課題

- Docker Desktop の会社PCへのインストールが以下の事情で禁止されることがある
    - 2022/02 以降、一定以上の売上または従業員数のある組織の「非営利のOSS開発」以外に対してDockerの利用が有償になった
    - 具体的にどの条件を満たすと「利用」と判定されるかは定かでなく、ダウンロード時に登録されたメールアドレスやIPが会社のものかどうかで判定される可能性がある
    - そのため、防御的な判断としてDocker Desktopの利用がNGになった

- このようなケースでは現状、公聴AIが使えないので、Dockerなしで動かせるようにしたい

# 実現手段

- ビルド/デプロイの時間あたりを犠牲にしてDockerをOFFにできないか？
- または、RancherやPodmanなど他の手段で動かせないか？

---

## 2026-09-09 現状と残作業

「Dockerなしでは使えない」という当初の前提は変わっています。current mainにはAPI/adminをnative起動する手順とanalysis-core CLIがあり、Serverlessにもブラウザで使う経路があります。

ただし、組織PCの制約に合う経路を初見で選べる案内は未整理です。残作業は #876 の利用モード入口へ「Docker Desktopが利用できない」分岐を統合し、必要なソフト・モデルへのデータ送信・キー管理の条件を明記することです。Windows実行ファイル化 #885 と同一視せず、Podman等を未検証のまま動作保証しません。

現行の非Docker手順: https://github.com/digitaldemocracy2030/kouchou-ai/blob/2dd5adc21103e880bf0250f29511f99a05c52590/docs/getting-started/quickstart.md


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

---

## 2026-09-09 現状と残作業

PR #933のスマホ向けリスト初期表示は関連改善ですが、デスクトップで散布図上をスクロールすると拡大縮小される問題は未解決です。現行mainのScatterChartは `scrollZoom: true` のためopenを維持します。

残る焦点はPCのwheel操作です。過去に支持された短い待機と視覚フィードバックの案を出発点に、ページを読み進める操作と図を拡大する操作を同じレポートで比較します。スマホの初期ビュー検討 #872 を重ねてやり直さず、利用者が散布図を選んだ後の挙動も確認します。


**コメント:** なし

---

### [[FEATURE]エンベデッドモデルを選択可能にする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/450)

**作成者:** tokoroten  
**作成日:** 2025-05-07T07:13:48Z  
**内容:**

# 背景
LLMのプロバイダが選択可能になったので、 text-embedding-3-small の決め打ちでは対応できなくなってきている。
SentenseTransformerによるローカル埋め込みもあるので、選択式にしたい。
SentenseTransformerのほうがtext-embedding-3-small よりも性能が高いというレポートがあるので、text-embedding-3-largeを選択可能にしたい

# 提案内容
リストボックスを設置して、そのAIプロバイダーが提供可能な、エンベデッドモデルの一覧を表示するようにする



---

## 2026-09-09 現状と残作業

チャットモデル選択と、埋め込みをローカルにする切替はありますが、埋め込みモデルをprovider別に選ぶリストは現行AI設定画面にありません。チャットモデル一覧の更新 #909 をこのIssueの完了とは扱いません。

残作業: チャットと埋め込みを別の設定として、選択可能モデル・接続先・local/API・設定保存・実際の埋め込み呼出まで確認する。Serverlessではチャットと埋め込みが別スロットなので、同じ入力とモデル選択の確認例を使います。対応一覧と実モデルでの動作確認フラグは分けます。

根拠: https://github.com/digitaldemocracy2030/kouchou-ai/blob/2dd5adc21103e880bf0250f29511f99a05c52590/apps/admin/app/create/components/AISettingsSection.tsx / https://github.com/digitaldemocracy2030/kouchou-ai/blob/2dd5adc21103e880bf0250f29511f99a05c52590/packages/analysis-core/src/analysis_core/steps/embedding.py


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


**コメント:** なし

---

### [[FEATURE]利用可能なLLMを増やす](https://github.com/digitaldemocracy2030/kouchou-ai/issues/285)

**作成者:** nishio  
**作成日:** 2025-04-12T23:50:46Z  
**内容:**

# 背景
現在OpenAI APIのみ対応しており、Gemini無料枠やLocalLLMなど他の選択肢を利用できない。

from 4/12 meetup
>「Geminiの無料枠をOpen AI互換で使えたりする？」
「他LLM対応はうれしい（LocalLLMなど）」
「Local LLM(OpenAI互換)、embeddingなどで開発はケチりたい」
「idobataの方ではopenrouterが使われているのに対して、kouchouではopenaiが使われているのが不便に思った。統一してくれるとありがたいと思う。」


<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
>Gemini API、OpenRouter API、OpenAI互換のLocalLLMなど、複数のLLMに対応する。

(nishioコメント) OpenRouter APIには追加で対応してもいいかもしれない、ただし「統一」はありえない(OpenRouterを使えないユーザを締め出すことになるから)

---

## 2026-09-09 現状と残作業

「OpenAI APIだけに対応」という当初の前提は古く、現行mainにはGemini・Azure・OpenAI互換LocalLLMの経路があります。モデルカタログは #909、実モデル検証は #912 / #913 へ分離済みです。

残件は、OpenRouterの接続方式・構造化応答・対応モデルを確認する #537 と、対応可能／動作確認済みを混同しない案内です。#537の実装仮説は現在のLLMクライアントで再検証する必要があります。OpenRouterへ統一することや、未確認の無料・データ利用条件を保証することはこのIssueの結論にしません。


**コメント:** なし

---

### [[FEATURE]クラスタ数が増えた場合に散布図上でクラスタラベルが被ってしまう](https://github.com/digitaldemocracy2030/kouchou-ai/issues/266)

**作成者:** nasuka  
**作成日:** 2025-04-08T14:20:10Z  
**内容:**

# 背景
* クラスタ数が増えた場合に散布図上でクラスタラベルが被ってしまう
  * 添付画像は40件で出力したケース。多くのクラスタラベルが被ってしまっている。
![Image](https://github.com/user-attachments/assets/c8e61e43-ef60-4054-91d0-4b8f3e6f4847)

* この問題により、現在は第一階層のクラスタ数を大きな数値に設定できない
  * 現在は上限を20としているが、TTTCの過去事例では30件を表示していたケースもあるため、上限をもう少し大きくしたい

# 提案内容
解決するアプローチは幾つかありそう。

## 対策方針（Claudeによる案）
1. ラベル表示の選択的制限

- 重要度ベースの選択：クラスタサイズなどに基づき重要なラベルのみ表示
- 最大表示数の制限：表示するラベル数に上限を設定（例: 最大15個）
- ユーザー選択型表示：選択されたクラスタのみラベル表示

2. ラベルの視覚的最適化

- フォントサイズの縮小：ラベルのフォントサイズを小さくして占有面積を減らす
- 可変フォントサイズ：クラスタの重要度に応じてフォントサイズを調整
- ラベル省略表示：長いラベルを省略形で表示（例: "長いラベル名" → "長いラ..."）

3. インタラクティブ手法

- 凡例コンポーネントの追加：画面端に凡例を設け、クラスタ一覧を表示
- ホバー/クリック表示：マウスホバーやクリック時のみラベルを表示
- ハイライト機能：選択クラスタを強調し他を半透明化

4. レイアウト最適化

- ラベル位置の調整：ラベル同士の衝突を検出し位置を最適化
- クラスタのグルーピング：近接するクラスタを階層的に表示

---

## 2026-09-09 現状と残作業

#294 と重複するラベルの重なり問題を、このIssueへ集約します。

現行viewerにはラベル非表示の回避手段がありますが、ラベルを表示したままの重なりは未解決です。PR #933 の日本語禁則・スマホのリスト初期表示も、ラベル衝突そのものの解消ではありません。

残作業は、同じレポートで「表示したままグループ名を読めるか」を比較し、位置調整・省略等の案を選ぶこと。全ラベルを把握したいという既存議論と、#294 の可変表示・手動調整案を維持します。単にラベルを隠せることを完了条件にはしません。


**コメント:** なし

---

### [[FEATURE]階層図で一番下まで到達した時には原文を見せても良いのではないか](https://github.com/digitaldemocracy2030/kouchou-ai/issues/250)

**作成者:** takahiroanno  
**作成日:** 2025-04-08T02:23:21Z  
**内容:**

# 背景

より情報量を増やしたい。原文を確認できるとより情報量が増えるなと思った。
![Image](https://github.com/user-attachments/assets/52f7591f-1d06-419b-97a3-2e0e382c2d46)

↑ご覧のように画面がスパースになる

- Xなど、利用規約的に出すことができないものはその旨を表示すると良いと思う

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

---

## 2026-09-09 現状と残作業

PR #927 / Serverless PR #25で階層図から個別の抽出済み意見は見られるようになりますが、「抽出済み意見」と「元コメント」は別です。このIssueはそのPRだけでは完了しません。

元コメントの公開可否・多対多参照・原文なしJSONの扱いは #56 で共通化し、このIssueは階層図末端の表示として追跡します。残る確認条件は、長文1件からN意見が抽出されても長文をN回並べないこと、公開できない／データがない場合の表示が分かることです。


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

---

## 2026-09-09 現状と残作業

PR #922 / #926 で作成前確認と選択モデルの接続チェックはmainに入りましたが、費用は現在「目安なし」です。このIssueは未解決として維持します。

次の実装単位は、入力件数・文字量と選択されたチャット／埋め込みモデルから概算を出し、既知部分と単価不明を分けて表示することです。Serverlessの `src/lib/estimate.ts` / `WizardPage.tsx` にはモデル別・処理別の見積もりがあるため、同じ合成入力と期待値で両版を比較して再利用可能なルールを揃えます。単価不明を0円にしないこと、実料金の保証ではないことを確認条件に含めます。

時間の推定は #11 で別に追跡します。Serverlessの実行後の概算表示も、請求額の確認とは区別します。

参考: https://github.com/tokoroten/kouchou-ai-serverless/blob/4579cae7a90a9162a3129db28bc8fefca207abef/src/lib/estimate.ts


**コメント:** なし

---

### [[FEATURE] 元コメントの表示機能](https://github.com/digitaldemocracy2030/kouchou-ai/issues/56)

**作成者:** nanocloudx  
**作成日:** 2025-03-16T04:00:23Z  
**内容:**

# 背景
現在表示されている文言は、AIが要約した文章(arguments または clusters)である
arguments の生成元となった comments も参照できると良い
（全て表示すると視認性が下がるため、オプションとして表示する項目があると望ましい）

# 提案内容
- hierarchical_result.json に comment を追加する
  - 元コメントは引用がNGの場合があるので、引用元の規約に注意する必要がある
- レポート表示に元コメントを表示するオプションを追加する

---

## 2026-09-09 現状と残作業

次の開発候補として、両版の「要約から元の声へ戻る」契約をここで整理します。現行本体の公開JSONへ元コメントを自動追加する判断はしていません。

最初の完了範囲案:
- [ ] 公開可否が不明・不可の元コメントを公開出力へ含めない。公開用ファイルと再分析用データを区別する。
- [ ] 意見と元コメントの多対多参照を保持し、文字列ID・先頭ゼロ・数値精度外のIDでも誤対応しない（Serverless PR #22の確認例を共有）。
- [ ] 元コメントを含まない既存JSONも読める。不在を架空のIDや本文で補わない。
- [ ] 原文が複数の抽出意見から参照されるとき、UIで同じ長文を不必要に重複表示しない（#250）。

表示できるデータの範囲と確認例を先に固定し、その後に公開UIへ接続します。#921のrepo移管判断を待たずに検討できます。


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

### [[FEATURE] チャート表示に連動した文章表示](https://github.com/digitaldemocracy2030/kouchou-ai/issues/52)

**作成者:** nanocloudx  
**作成日:** 2025-03-16T03:43:03Z  
**内容:**

# 背景
レポートはチャートとクラスター文章から成っている
現在はチャート表示を切り替えたりしても、クラスター文章は初期表示のままである

# 提案内容
表示範囲の更新に合わせて、チャート下部にあるクラスター内容文章(cluster.takeaway)も更新する

---

## 2026-09-09 現状と残作業

階層図と説明の連動は #528 のPR #927で実装・ブラウザ確認済み、CI成功です。ただし未mergeなので、このIssueもまだcloseしません。

merge後は「全体／詳細／濃い意見の説明」「階層移動と戻る」「属性で絞った件数」「0件からの復帰」を照合して完了判断します。Serverless側はPR #25で同じ現在位置・件数・割合を扱います。元コメントを表示する要望 #56 / #250 は別の公開・参照契約であり、抽出済み意見の表示で完了扱いにしません。


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


---

## 2026-09-09 現状と残作業

作成前確認パネルはPR #922でmainに入りましたが、時間の欄は現在「目安なし」です。従来の「数分〜数十分」という一般案内だけでは入力に応じた目安を満たさないため、openを維持します。

次は同意のある公開／合成サンプルの測定で、件数・文字量・モデル・並列数・実行方式（本体／Serverless）・ステップ別時間を揃えて記録し、初回利用者へ幅のある目安を示せるか判断します。過去コメントの単発実測を全利用者へ外挿しません。精密な残り時間表示は別段階とし、費用の #79 と入力情報だけを共有します。


**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (24件)

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

### [fix: 日本語・全画面・スマホの閲覧を改善し状態カタログを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/933)

**作成者:** nishio  
**作成日:** 2026-09-08T15:33:37Z  
**変更:** +863 -108 (22ファイル)  
**マージ日:** 2026-09-08T17:20:10Z  
**内容:**

# 変更の概要

レポートを読む際の表示上の障害を修正し、同じ状態を再現できる開発用カタログとブラウザ回帰試験を追加しました。

- 日本語の結合文字を分断せず、句読点・括弧の禁則を考慮してPlotlyの文を折り返します。
- 全画面の終了ボタン専用の領域を確保し、ホバー表示との重なりを防ぎます。
- 静的出力をfile://で開くと、Next.jsの起動を待たずHTTP配信の案内を表示します。
- 幅600px以下では階層リストを初期表示します。明示的なvisualizationConfigを優先し、ユーザーの切替をリサイズで上書きしません。
- 開発専用の /dev/viewer-states/ で、通常・空一覧・メタデータなし・接続エラー・属性なし・空の意見・明示設定を切り替えられます。実コンポーネントと公開の仮想アンケート由来の12意見を使い、APIやデータ変更は不要です。本番では404です。

Serverless側も同じ折り返し関数・サンプル・スマホ初期表示へ揃えています（https://github.com/tokoroten/kouchou-ai-serverless/pull/26）。本体の静的出力とServerlessの単一HTMLの配布形式は区別しています。

# 関連Issue

Closes #478
Closes #283
Closes #253
Closes #872
Closes #566

# 動作確認の結果

- Jest 102件成功
- ブラウザ回帰試験4件成功：状態切替、全画面レイアウト、390pxでの初期表示と明示設定、file://の案内
- Next.js本番build（webpack）成功、本番カタログURLのHTTP 404を確認、厳密MkDocs build成功
- 状態カタログのE2EをClient Testsへ追加

# CLAへの同意

- [ ] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **New Features**
  - Added a development viewer catalog for previewing report, empty, error, and configuration states.
  - Added guidance when reports are opened directly from a local file.
  - Narrow screens now open reports with a readable hierarchical list when no default view is configured.

- **Improvements**
  - Improved Japanese text wrapping in charts while preserving punctuation, emoji, and complete characters.
  - Improved fullscreen chart layout and scrolling behavior.
  - Added an accessible label to the chart fullscreen control.

- **Documentation**
  - Added guidance for narrow-screen viewing and extraction prompt design.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix: static-site-builderの開発起動をtsxに移行](https://github.com/digitaldemocracy2030/kouchou-ai/pull/932)

**作成者:** nishio  
**作成日:** 2026-09-08T15:27:40Z  
**変更:** +314 -131 (2ファイル)  
**マージ日:** 2026-09-08T17:11:16Z  
**内容:**

# 変更の概要

ts-node-devをtsxに置き換え、存在しないsrc/server.tsへの参照を実際のsrc/index.tsに修正しました。

# 関連Issue

Closes #690

# 動作確認の結果

凍結lockfileでinstall、TypeScript build、dev起動後のhealthcheck、ソース更新による再起動後のhealthcheckが成功。

# CLAへの同意

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト

- [ ] CIが全て通過している
- [ ] 変更内容と検証範囲を確認した


**コメント:** なし

---

### [feat: 完成レポートの参照整合性を任意で検査する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/931)

**作成者:** nishio  
**作成日:** 2026-09-08T15:27:14Z  
**変更:** +164 -0 (4ファイル)  
**マージ日:** 2026-09-08T17:11:10Z  
**内容:**

# 変更の概要

完成artifactの検査を、分析成功の必須条件ではなく読み取り専用の診断コマンドとして追加します。ID重複、親の参照切れ・循環、階層パス、座標・件数の不正値を検査し、未知の追加フィールドは許容します。状態ファイルと分析内容の品質判定は範囲外です。

# 関連Issue

Closes #838

# 動作確認の結果

12テスト・Ruff・strict docs build成功。serverless同梱sample-report.jsonの検査は問題0件。実LLM API未使用。

# CLAへの同意

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト

- [ ] CIが全て通過している
- [ ] 変更内容と検証範囲を確認した


**コメント:** なし

---

### [docs: 入力特性に応じた抽出プロンプトの比較手順を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/930)

**作成者:** nishio  
**作成日:** 2026-09-08T15:18:20Z  
**変更:** +69 -0 (2ファイル)  
**マージ日:** 2026-09-08T17:14:45Z  
**内容:**

# 変更の概要

短文・意見でない入力・否定条件などの失敗を分類し、入力と出力の対応を収集する書式と比較手順を追加します。例は仮想データで動作未検証と明記し、標準プロンプトは変更しません。本体とserverlessで同じ入力・モデル・プロンプトを比較する手順を揃えます。

# 関連Issue

Closes #367

# 動作確認の結果

MkDocs strict build成功。例示プロンプトの実モデル評価は未実施で、改善を確認済みとはしていません。

# CLAへの同意

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト

- [ ] CIが全て通過している
- [ ] 変更内容と検証範囲を確認した


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **Documentation**
  - Added Japanese guidance for adjusting extraction prompts to different input types, including opinions, keywords, factual statements, irrelevant content, negations, and conditions.
  - Documented a workflow for collecting failure cases, comparing results with a baseline, and recording verification outcomes.
  - Added the new guidance to the developer documentation navigation.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [docs: Windows導入の対象環境と失敗時の確認順を明確化](https://github.com/digitaldemocracy2030/kouchou-ai/pull/929)

**作成者:** nishio  
**作成日:** 2026-09-08T15:07:58Z  
**変更:** +38 -7 (1ファイル)  
**マージ日:** 2026-09-08T17:11:01Z  
**内容:**

# 変更の概要

標準経路をDocker DesktopのLinux containersが起動できる環境とし、組織端末の制約・別環境・serverlessへの分岐を追加しました。APIキーはどちらか一方でよいこと、セットアップは形式確認であり実API確認ではないこと、起動後のモデル接続確認を明記します。

# 関連Issue

Closes #877

# 動作確認の結果

current mainのsetup_win.ps1と照合し、MkDocs strict build成功。文書変更のみ。Windows実機の新たな実行確認はしていません。

# CLAへの同意

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト

- [ ] CIが全て通過している
- [ ] 変更内容と検証範囲を確認した


**コメント:** なし

---

### [fix: 抽出失敗と正常0件の原文付き診断を残す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/928)

**作成者:** nishio  
**作成日:** 2026-09-08T15:07:54Z  
**変更:** +60 -0 (5ファイル)  
**マージ日:** 2026-09-08T17:10:54Z  
**内容:**

# 変更の概要

抽出時に、回答ID・原文・empty/error・例外の種類をJSONLで記録します。公開outputsの隣のdiagnosticsへ分離し、API例外本文を保存しません。失敗時の分析中断を維持し、正常0件を失敗と混同しないようにします。保存場所と削除方法を文書化しました。

# 関連Issue

Closes #318

# 動作確認の結果

抽出失敗の回帰テスト9件、Ruff、MkDocs strict build成功。実LLM APIは使用していません。

# CLAへの同意

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト

- [ ] CIが全て通過している
- [ ] 変更内容と検証範囲を確認した


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Added diagnostics for opinion-extraction failures and empty results, including the affected comment and failure status.
  * Diagnostics are stored separately from published reports with restricted file access.

* **Documentation**
  * Added developer documentation explaining extraction diagnostics, failure states, file handling, and cleanup guidance.
  * Added the diagnostics guide to the developer documentation navigation.

* **Chores**
  * Excluded generated extraction diagnostics and related artifacts from version control.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix: 階層図の現在位置と説明一覧を連動させる](https://github.com/digitaldemocracy2030/kouchou-ai/pull/927)

**作成者:** nishio  
**作成日:** 2026-09-08T14:50:08Z  
**変更:** +252 -13 (8ファイル)  
**マージ日:** 2026-09-08T17:10:13Z  
**内容:**

# 変更の概要

階層図で下の階層へ移動しても第1階層の説明が残る問題を修正します。現在のグループと直下のグループのタイトル・件数・全意見に対する割合・説明を表示し、説明から階層図へ移動できます。個別意見・一つ上に戻る・パンくずによる移動も同じ状態で更新します。

フィルター中は件数と分母を絞り込み後の意見に揃え、説明文自体は全意見から生成したものだと明示します。図内の割合も全意見を分母に統一しました。階層図が無効なレポートでは既存の説明アンカーを維持します。

# スクリーンショット

同梱の仮想アンケートを使い、女性フィルターの下で第1階層へ移動した画面です。

![階層と説明の連動](https://raw.githubusercontent.com/digitaldemocracy2030/kouchou-ai/codex/issue-528-treemap-context/docs/images/treemap/context.png)

# 変更の背景

説明一覧がtreemapLevelを参照していませんでした。また、通常のclickで取得したノードIDでは親へ戻る操作を追跡できないため、plotly_treemapclickのnextLevelを使いReactで移動先を管理します。

# 関連Issue

Closes #528

serverlessにも同じ表示・件数計算・回帰テストを移植: https://github.com/tokoroten/kouchou-ai-serverless/pull/25

# 動作確認の結果

- public-viewer: 101テスト成功（階層・個別意見・戻る・フィルター・ゼロ件・不正IDの回帰テストを含む）。変更ファイルのBiome成功。
- public-viewerの本番build成功（Next.js 16.2.6、webpack）。全体のtsc単独実行には既存validation.test.tsのfixture型不整合4件が残っています。
- 実ブラウザで説明リンク、図クリック、個別意見、戻るボタン、パンくず、属性フィルター、ゼロ件からの復帰を確認。
- 両版に同じserverless同梱サンプルを読み込み、女性フィルターで3,013件中460件・15.27%が一致することを確認。確認時だけdummy-serverのfixtureを差し替え、差分には含めていません。

# CLAへの同意

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）

- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 変更箇所と影響範囲の動作確認が適切か


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **New Features**
  - Added interactive treemap details for selected clusters and opinions, including counts, percentages, takeaways, and child groups.
  - Added navigation between hierarchy levels, return-to-root controls, and links from cluster summaries to the treemap.
  - Added filtering-aware treemap details and navigation to relevant arguments.

- **Bug Fixes**
  - Improved treemap click and pathbar navigation behavior.
  - Corrected percentage calculations and parent relationships for argument nodes.
  - Improved handling of empty treemap panels and zero-count results.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [選択したprovider・モデル・ローカル接続先でチャット接続を確認する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/926)

**作成者:** nishio  
**作成日:** 2026-09-08T13:08:35Z  
**変更:** +621 -66 (16ファイル)  
**マージ日:** 2026-09-08T14:17:39Z  
**内容:**

# 変更の概要
API接続チェックに選択モデルとローカルLLMの接続先を渡します。Azureは既存のサーバー設定済みデプロイ、OpenRouter・OpenAI・Geminiは選択モデル、LocalLLMは選択モデルと入力した接続先で短いチャットを確認します。

**PR #922に続く変更です。先に #922をマージする想定です。** 現時点の差分には#922の作成前確認が含まれます。このPR固有の変更はcommit `2319967`です。

# スクリーンショット
![local接続確認（ダミーAPI）](https://raw.githubusercontent.com/digitaldemocracy2030/kouchou-ai/codex/issue-473-provider-check/docs/images/provider-connection-check.png)

# 変更の背景
Azure・OpenRouterの呼出経路は既にありましたが、接続確認では固定モデルを使用し、LocalLLMの選択接続先も渡していませんでした。新規作成の確認画面と再利用画面を修正します。

- HTTPエラー、successなし、空のチャット応答を成功扱いにしません。確認リクエストはキャッシュしません。
- LocalLLMのモデル・接続先が空なら呼出前に拒否。SDK呼出のタイムアウトは30秒（リトライを含む全体の上限ではありません）。
- 成功表示はチャット接続の範囲に限定。埋め込み・構造化出力・残高・レポート全体の動作確認とは区別します。
- serverlessには選択endpoint/modelを使う応答テストが既にあるため、今回は本体の挙動を揃えています。

# 関連Issue
Closes #473
Related #391, #884, #922

# 動作確認の結果
- 管理画面全136テスト、型検査、変更TSのBiome成功。
- API admin_report関連19テスト、変更PythonのRuff成功。Azure/OpenRouter/localへの設定引渡し、入力不備、空応答、例外情報非公開を検証。
- E2E事前確認1件成功後、作成フロー14件成功・既存skip1件。1280px/375pxの接続確認・戻る操作を含みます。
- 実ブラウザでLocalLLM選択→作成前確認→ダミーAPIでの確認成功を表示。
- mkdocs build --strict成功。
- 実LLM APIは未使用。#912 / #913の人間による動作確認は完了扱いにしていません。

# CLAへの同意
- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト
- [ ] CIが全て通過している
- [ ] 適切な動作確認が行われている


**コメント:** なし

---

### [AIエージェントのIssue着手からPRまでの作業導線を集約する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/925)

**作成者:** nishio  
**作成日:** 2026-09-08T12:58:44Z  
**変更:** +62 -36 (5ファイル)  
**マージ日:** 2026-09-08T14:21:30Z  
**内容:**

# 変更の概要
AIエージェント向けの読む順番・タスク別ガイド・担当確認からPRまでの流れを既存のai-assistantsページに集約します。CONTRIBUTINGとCLAUDEの入口、MkDocsナビゲーションを接続し、CONTRIBUTINGをdocsへコピーする際のリンクも変換します。

# 変更の背景
skillsのセットアップ説明だけでは、作業開始時に何を読み、何を確認すればよいか分かりませんでした。各文書の役割、人間の明示指示が必要な対人操作、serverlessと関係する変更の相互PR・対応テストの確認を記載しました。
Codexはファイルパス指定を最小構成とし、任意のスキル登録を現在の公式案内に沿った.agents/skillsへ更新しました。

# 関連Issue
Closes #878

# 動作確認の結果
- mkdocs build --strict成功。
- CONTRIBUTINGから生成されたdocsページのリンク先がai-assistants.mdへ変換されることを確認。
- 差分チェック成功。文書・ナビゲーションのみの変更です。

# CLAへの同意
- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト
- [ ] CIが全て通過している
- [ ] 適切な動作確認が行われている


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Documentation**
  * Updated contributor guidance to direct AI-assisted contributors to the AI agent workflow documentation.
  * Reworked the AI agent documentation with reading order, task navigation, contribution procedures, repository guidance, and human-approval boundaries.
  * Clarified that the contributor guidance file remains a concise skills index.
  * Renamed the documentation navigation label and improved links to the AI agent workflow documentation.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [レポートに読み方ガイドを表示し、件数の誤解釈を防ぐ](https://github.com/digitaldemocracy2030/kouchou-ai/pull/924)

**作成者:** nishio  
**作成日:** 2026-09-08T12:55:17Z  
**変更:** +55 -0 (4ファイル)  
**マージ日:** 2026-09-08T14:18:05Z  
**内容:**

# 変更の概要
レポートのグラフの前に、件数を社会全体の支持率と混同しない説明を常時表示します。詳細を開くと収集の偏り、人数と意見数、図の解釈、AI出力の照合、追加調査の読み方を確認できます。公開viewerの静的出力とCLI生成report.htmlにも含まれます。

# スクリーンショット
![読み方ガイド](https://raw.githubusercontent.com/digitaldemocracy2030/kouchou-ai/codex/issue-696-reading-guide/docs/images/report-reading-guide.png)

# 変更の背景
AI分析の図を社会全体の支持率や合意の証明と誤解することを防ぎ、論点発見から対話・追加調査につなげます。[serverless PR #24](https://github.com/tokoroten/kouchou-ai-serverless/pull/24)にも同じ文言を適用しています。

# 関連Issue
Closes #696

# 動作確認の結果
- public-viewer全94テスト、CLI HTML関連14テスト成功、変更TSのBiome成功。
- 実ブラウザで既存ダミーレポートを表示し、常時説明と詳細の開閉を確認。
- 全体tscは既存validation.test.tsの型不整合4件で失敗。同じ4件が未変更mainでも再現し、この変更で増加していません。

# CLAへの同意
- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト
- [ ] CIが全て通過している
- [ ] 適切な動作確認が行われている


**コメント:** なし

---

### [CSVの形式エラーを修正方法付きで表示し、古い入力の再利用を防ぐ](https://github.com/digitaldemocracy2030/kouchou-ai/pull/923)

**作成者:** nishio  
**作成日:** 2026-09-08T09:19:43Z  
**変更:** +243 -50 (6ファイル)  
**マージ日:** 2026-09-08T14:18:01Z  
**内容:**

# 変更の概要
CSVの引用符不整合や列数不一致がPapa Parseの`complete`側に報告されても無視していたため、壊れたデータが解析対象になっていました。原因と修正方法を入力欄の下に表示し、列名の重複・空欄、データなしも拒否します。正常な1列CSVの区切り文字推定警告は許容します。

ファイルが読み込めた後だけ作成用入力に採用します。失敗時は以前の列・属性設定を破棄し、削除や再選択より前に始まった読み込みが後から入力を復活させないようにしました。既存の文字コード変換・列推定・ID補完は維持します。

# スクリーンショット
![CSVエラー表示](https://raw.githubusercontent.com/digitaldemocracy2030/kouchou-ai/codex/issue-97-csv-errors/docs/images/csv-format-error.png)

# 変更の背景・関連Issue
Closes #97

#884 / PR #922の作成前確認に対し、こちらは実行前のCSVパースエラーを扱います。[serverless PR #23](https://github.com/tokoroten/kouchou-ai-serverless/pull/23)にも同じ欠落があり、同じ判定・日本語メッセージ・CSV検証ケースで対応しています。repoの統合や本流化の判断を前提としません。

# 動作確認の結果
- 管理画面全21スイート・128テスト成功。引用符、列の過不足、空/重複ヘッダー、ヘッダーのみ、正常な1列、BOM、引用符内カンマ・改行、Shift_JISを検証。
- 失敗後の正常ファイル再選択、削除後の遅延完了をコンポーネントテストで確認。
- TypeScript検査、変更TSファイルのBiome検査成功。
- ローカルブラウザで壊れたCSVのエラー表示→削除→修正済みCSVの列選択表示を確認。解析実行・実API呼び出しはしていません。

# CLAへの同意
- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト
- [x] GitHub Actionsが全て通過している（E2Eを含む。CodeRabbitレビューは進行中）
- [x] 単体テストが実装されている
- [x] 入力エラー表示と再選択を確認した


**コメント:** なし

---

### [レポート作成前に入力とAPI接続状態を確認できる画面を追加する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/922)

**作成者:** nishio  
**作成日:** 2026-09-08T08:07:05Z  
**変更:** +458 -43 (7ファイル)  
**マージ日:** 2026-09-08T14:16:54Z  
**内容:**

# 変更の概要
CSV / Spreadsheet / pluginからレポートを作成する際、共通の「作成前の確認」を通るようにします。画面を開くだけでは作成やAPI接続チェックは実行せず、確認画面の開始操作で初めて、表示した内容を送信します。

入力元・選択コメント列・件数（非空件数）・属性列・クラスタ数・provider/model・並列数を表示します。非空コメント数がクラスタ数を下回る場合や空行がある場合は警告し、設定に戻って修正できます。費用と時間は初期段階として「目安なし」を表示します。

API接続チェックを確認画面へ統合し、未確認・確認中・OK・認証エラー・残高/quota不足・rate limit・不明エラーを区別します。検証用モデルの結果を選択モデルや必要残高の保証として扱いません。ローカルLLMの選択接続先を既存APIでは検証できないため、未対応と明示します。

# 関連Issue
Closes #884

# 動作確認の結果
- 管理画面: 21 suites / 128 tests passed、TypeScript型検査と変更ファイルBiome成功
- 3入力経路で確認前の送信なし、戻って修正した内容の反映、作成の二重送信防止を回帰テスト
- APIのエラー分類・未確認・確認中・成功、再表示時の結果リセット、空入力の開始抑止をテスト
- ローカル実ブラウザでCSVから確認画面、件数警告、ダミーAPIの接続成功表示を確認
- E2E事前確認4件成功、作成フロー13件成功（既存skip1件）。追加確認画面は1280px / 375pxの2ケースとも成功。スクリーンショットをPlaywrightレポートに添付

# 後続の範囲
#884に記載された最初の実装単位です。#11 / #79の数値見積もり、#221のsample-first/reuse導線、#292の課金設定の詳しいガイド、#391の全provider・選択モデルでの検証、#97の詳細なCSVエラー改善は今回完了扱いにしません。自動で入力件数を削減することもありません。

# テスト環境の補修
実ブラウザ検証に必要なため、ダミーAPIのモデル一覧にCORS応答を追加し、接続確認の成功fixtureを追加しています。有料の実APIは使用していません。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト
- [x] GitHub Actionsが全て通過している
- [x] 単体・回帰・E2Eテストが実装されている

GitHub Actions成功を確認済み。CodeRabbitは利用制限によりレビュー未実施です。


**コメント:** なし

---

### [LLM呼び出しのタイムアウトを環境変数で設定できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/920)

**作成者:** nishio  
**作成日:** 2026-09-08T07:58:35Z  
**変更:** +121 -5 (11ファイル)  
**マージ日:** 2026-09-08T14:17:55Z  
**内容:**

# 変更の概要
LLM呼び出しの待ち時間を `.env` の `LLM_REQUEST_TIMEOUT_SECONDS` で指定できるようにします。例: `600` なら600秒、未指定は従来どおり300秒です。OpenAI / Azure / Gemini / OpenRouter / ローカルLLMに共通で適用します。

抽出工程の `extraction.timeout_seconds` がworkflow pluginで落ちる問題も修正しました。工程設定 → 環境変数 → 既定値の順で採用し、正の整数以外を拒否します。仕様上の設定項目とドキュメント・環境変数サンプルも追加しています。

# 関連Issue
Closes #452

# 動作確認の結果
- analysis-core: 221 tests passed
- API LLMサービス: 40 tests passed
- 新規回帰テストで環境変数が全providerの呼び出し既定値・抽出・概要へ届くこと、workflow経由の上書き値が実際のLLM呼び出しへ届くこと、値の検証を確認
- Ruff / diffチェック成功。実APIは呼び出していません。

# 補足
API再起動が必要です。Docker Composeでは環境変数を再読込するためAPIコンテナを再作成します。SDKリトライ等を含む分析全体の制限時間ではありません。抽出では既存のバッチ待機期限（キュー内の処理も含む）も同じ値を使用します。embeddingは対象外です。ローカルLLMでの並列数1の案内も追記しました。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト
- [x] GitHub Actionsが全て通過している
- [x] 単体・回帰テストが実装されている

GitHub Actions成功を確認済み。CodeRabbitは利用制限によりレビュー未実施です。


**コメント:** なし

---

### [ラベル生成の失敗を検知して後続処理を停止する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/919)

**作成者:** nishio  
**作成日:** 2026-09-08T07:39:52Z  
**変更:** +316 -69 (7ファイル)  
**マージ日:** 2026-09-08T14:17:51Z  
**内容:**

# 変更の概要
初期・統合ラベル生成でAPI呼び出しや応答検証に失敗した場合、エラー文をラベルとして保存せず、その工程を失敗にして後続処理を止めます。たとえば2クラスタで失敗した場合、工程名・2件という件数・クラスタID・失敗種別をエラーとして報告します。

- API例外、タイムアウト、不正なJSON／欠落・空欄・型不正のラベルを検出。同じバッチの結果を回収して失敗一覧を作成します。
- 正常なラベル生成と、子クラスタが1つのときのラベル引き継ぎを維持します。
- 並列worker間のトークン集計を排他制御し、不正応答でも返されたusageを保持します。
- パイプライン失敗時はstatusに `token_usage_complete=false` / `estimated_cost=null` を保存。管理画面では残存する数値を合計として表示せず「不明（処理失敗・集計不完全）」と表示します。

# 変更の背景
従来は例外を握りつぶし「エラーでラベル名が取得できませんでした」という値で処理を続け、欠落があるレポートを正常完了にできました。

# 関連Issue
Closes #915

# 動作確認の結果
- analysis-core全体: 231 tests passed。その後追加した2ケースを含め、ラベル回帰テスト22件も成功。
- 旧実行経路・workflow経路の両方でerror status、後続停止、失敗工程の出力非生成、費用無効化を確認。
- 管理画面: 19 suites / 117 tests passed、TypeScript型検査成功。
- Ruff / Biome / diffチェック成功。
- 実API呼び出しは行わず、API例外・タイムアウト・不正応答をモックで再現。

# 補足
失敗したAPIリクエストのusageが取得できないことがあるため、失敗時の完全な課金額は復元しません。workflowでは失敗工程のusageは成功工程の合計に含まれず、不完全な集計として扱います。失敗分だけの再試行や警告付き正常完了は対象外です。

概要生成も確認し、API例外は既に伝播しています。既存のthinkタグ除去・テキスト応答互換は変更していません。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト
- [ ] CIが全て通過している
- [x] 単体・回帰テストが実装されている


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Failed analysis runs now clearly report incomplete token usage and estimated costs instead of presenting partial totals.
  * Pipeline processing now stops safely after labelling failures, preventing downstream steps and incomplete output files.
  * Labelling failures are classified consistently, including timeouts and invalid responses, while protecting sensitive error details.

* **Improvements**
  * Token usage tracking is now preserved more reliably, including when responses are malformed.
  * Single-item merges reuse existing labels without making an unnecessary API request.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [CSVファイル名から未入力のタイトルと調査概要を補完する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/918)

**作成者:** nishio  
**作成日:** 2026-09-08T07:36:51Z  
**変更:** +37 -1 (3ファイル)  
**マージ日:** 2026-09-08T14:17:45Z  
**内容:**

# 変更の概要
CSV選択時に、タイトル・調査概要が空欄なら拡張子を除いたファイル名で補完します。例: `調査.v2.csv` → `調査.v2`。各項目を独立して判定し、入力済みの値やレポートIDは維持します。

ファイル選択とドラッグ＆ドロップの共通イベントに適用します。ファイル削除・再選択でも入力済みの値は変更しません。

# 関連Issue
Closes #639

# 動作確認の結果
- 管理画面 Jest: 19 suites / 121 tests passed（空欄・片側入力済み・両側入力済み・再選択・削除・大文字拡張子を含む）
- TypeScript `tsc --noEmit`: 成功
- 変更ファイルの Biome: 成功
- レイアウト変更なし。実ブラウザでの操作確認は未実施。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト
- [ ] CIが全て通過している
- [x] 単体テストが実装されている


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Selecting a CSV file now automatically fills blank question and introduction fields using the file name.
  * Existing question and introduction text is preserved when already provided.
* **Bug Fixes**
  * Report identifiers remain unchanged when the CSV filename does not match the report title.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [モデルカタログを統一し新モデルを動作未確認で選択可能にする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/914)

**作成者:** nishio  
**作成日:** 2026-09-07T16:18:12Z  
**変更:** +1023 -649 (27ファイル)  
**マージ日:** 2026-09-07T17:36:12Z  
**内容:**

# 変更の概要
モデル一覧・説明・料金の重複をサーバーカタログへ集約し、新規作成と複製画面が同じAPIから読むようにしました。未検証でも選択可能にし、GPT-5.6 Terra / LunaとGemini 3.8 Flash / 3.5 Flash-Liteを「動作未確認」で追加します。

# 変更の背景
#909の[確定した判断](https://github.com/digitaldemocracy2030/kouchou-ai/issues/909#issuecomment-5573140968)に沿った実装です。
- verifiedとavailableを分離。動的一覧の未登録モデルも「動作未検証」で選択可能。既存モデルも検証記録を移入していないためverified=falseから開始します。
- 提供終了モデルは無効化し、保存済み設定を無言で置換せず再選択を案内します。
- 不明価格はnull。Gemini名のprefixを正規化してから検索し、期限切れ単価は不明に戻します。過去の保存済み推定額は書き換えません。
- Azureは固定表示を維持し、実モデル名と契約単価をサーバー設定で明示。OpenAIの一覧・料金にfallbackしません。
- Gemini/OpenRouterの動的一覧取得失敗時は、登録済み一覧と警告を返します。API自体の取得失敗時は再取得を案内します。

`docs/development/model-catalog.md` に追加・廃止・検証フラグ・料金・Azure設定の更新手順を記載しました。通常単価は概算で、GPT-5.6の長文料金は累積入力272,000token超の場合に保守的に不明とします。

# 関連Issue
Fixes #909
Fixes #906
Fixes #907

実APIによる互換性・思考トークン/料金集計の確認は別Issue #912 / #913へ移しました。未検証のまま一覧へ追加することは今回の指示に含まれます。

**関連PR：#911。** CIがmain向けPRのみを検査するためbaseはmainです。現在は#911のAzure UI修正も含み、#911を先にmergeするとその重複差分が消えます。

# 動作確認の結果
- 管理画面19スイート116テスト、型検査成功。保存済み廃止モデル、新モデルの選択、複製画面、Azureから他providerへの切替、取得失敗からの再試行を確認。
- APIのcatalog・価格・report statusテスト成功。分析処理の関連54テスト成功。
- Biome / Ruff / diff検査成功。
- ローカルの実APIへ接続した新規作成画面で、新モデルのラベルと選択、旧Geminiの無効化を確認。
- E2Eのダミーサーバーも同じcatalog JSONを参照します。
- 有料LLMの実API生成試験は未実施（#912 / #913で追跡）。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **New Features**
  - Added a shared AI model catalog with provider-specific descriptions, availability, verification status, deprecation indicators, and pricing.
  - Model selectors now identify unverified or unavailable models and support refreshing the catalog.
  - Azure model selection uses the server-configured deployment and pricing settings.
  - Newly discovered provider models can be displayed alongside catalog entries.

- **Bug Fixes**
  - Deprecated saved models are preserved while prompting users to select a replacement.
  - Unknown or unavailable pricing is now shown as unknown instead of zero.
  - Model-fetch failures now provide a warning and reload option.

- **Documentation**
  - Added guidance for maintaining the model catalog and configuring provider pricing.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Azure利用時のモデル選択を無効化し、サーバー設定の利用を明示する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/911)

**作成者:** nishio  
**作成日:** 2026-09-07T15:02:55Z  
**変更:** +108 -9 (3ファイル)  
**マージ日:** 2026-09-07T17:35:56Z  
**内容:**

# 変更の概要
Azureを選んだとき、実際の呼び出し先を変えられないモデル選択欄を無効化し、「サーバー設定を使用」と表示します。保存済みのモデル名やOpenAI用の性能・料金説明もAzureでは表示しません。OpenAIなど他のプロバイダーでは従来どおり選択できます。

# 変更の背景
Azureではサーバー側の設定で呼び出し先が決まるため、画面でモデルを選べる表示が実動作と食い違っていました。#477の既存コメントにある選択無効化の案に沿ったUIの修正です。
既存の保存設定・APIリクエストの形式は維持しています。モデルカタログや料金計算の再設計は含めません。

# 関連Issue
Fixes #908
Fixes #477

# 動作確認の結果
- 管理画面の全18スイート・114テスト成功。保存済みAzure設定の復元、OpenAI→Azure→OpenAIの切替、Geminiのモデル選択を追加検証。
- TypeScript型検査、変更3ファイルのBiome検査成功。
- ローカルの実画面でAzureの固定表示・disabled属性、OpenAIに戻した場合のモデル選択を確認。
- 実際のAzure APIを使ったレポート生成は未実施。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Azure AI configurations now use the model selected by the server.
  * Model selection is disabled when Azure is selected, with a clear indication that server settings are being used.
  * OpenAI and Gemini continue to support selectable models with provider-specific descriptions.

* **Tests**
  * Added coverage for provider switching, Azure model behavior, and model selection states.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix: 意見抽出の部分失敗を検知して分析を中断する (#905)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/910)

**作成者:** nishio  
**作成日:** 2026-09-07T12:45:40Z  
**変更:** +188 -79 (4ファイル)  
**マージ日:** 2026-09-07T17:35:59Z  
**内容:**

# 変更の概要

意見抽出で一部のLLM呼び出しが失敗しても正常な「抽出0件」として処理が続くため、回答が欠落したままレポートが完成していました。抽出バッチに失敗があれば既存のerror状態で分析を中断し、失敗件数・回答ID・エラー種別を表示するようにします。

- API例外とbatch timeoutを検知し、成功した空リストと区別します。
- 不正JSON、キー欠落、リスト以外や文字列以外の要素を含む応答をエラーにします。dict応答にも同じ検証を適用します。
- 生の回答本文・応答・APIエラーをエラーメッセージへ含めません。
- 失敗時は後段へ進まず、抽出の部分成果物も新規出力しません。

# 変更の背景

#905の実データ報告を受け、抽出の部分失敗を正常完了にしない最初の修正です。並列数が直接の原因だったかは未確定で、既存retryやworkersのデフォルトは変更していません。

実行中のfutureはcancelで強制終了できないため、timeout検知後もexecutor終了待ちが生じます。また、失敗したworkflowの費用・token集計の完全性は保証しません（batch内で取得済みの成功分は保持しますが、workflowの失敗step集計は別途課題です）。

# 関連Issue

Refs #905

ラベル生成のエラー文を含めた全工程の部分失敗検知、警告付き完了、失敗分のみ再実行は後続の検討とし、このPRでIssueを自動closeしません。

# 動作確認の結果

- analysis-core全体: `PYTHONPATH=src OPENAI_API_KEY=dummy GEMINI_API_KEY=dummy python -m pytest tests -q --disable-warnings` — 210 passed
- API parser: `PYTHONPATH=../../packages/analysis-core/src ADMIN_API_KEY=test PUBLIC_API_KEY=test OPENAI_API_KEY=dummy python -m pytest tests/services/test_parse_json_list.py -q --disable-warnings` — 19 passed
- 変更ファイルのRuff、`git diff --check` — 成功
- 回帰テスト: 正常な0件と入力順、部分失敗の件数と成功分token、未完了future、形式不正、legacy / 標準workflowでerror保存・後段未実行・部分CSV未出力。
- 外部LLMを呼ぶ実データ再実行は未実施。UI変更はありません。

# CLAへの同意

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）

- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **Bug Fixes**
  - Extraction responses are now validated for the expected JSON structure and list contents.
  - Invalid or malformed responses produce clear errors instead of silently returning empty results.
  - Error messages no longer expose the original response content.
  - Failed or timed-out batch tasks are reported, preventing incomplete results from being published.
  - Legitimate empty extraction results continue to be supported.
  - Batch results preserve ordering and associated comment references.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Bump next from 16.2.6 to 16.2.11 in /utils/dummy-server](https://github.com/digitaldemocracy2030/kouchou-ai/pull/904)

**作成者:** dependabot[bot]  
**作成日:** 2026-07-28T03:17:55Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2026-09-08T14:19:29Z  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 16.2.6 to 16.2.11.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v16.2.11</h2>
<p>This release contains security fixes for the following advisories:</p>
<p>High:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-m99w-x7hq-7vfj">Denial of Service in App Router using Server Actions</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-6gpp-xcg3-4w24">Middleware / Proxy bypass in App Router applications using Turbopack and single locale</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-p9j2-gv94-2wf4">Server-Side Request Forgery in rewrites via attacker-controlled destination hostname</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-89xv-2m56-2m9x">Server-Side Request Forgery in Server Actions on custom servers</a></li>
</ul>
<p>Moderate:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-68g3-v927-f742">Cache confusion of response bodies for requests with bodies</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-4633-3j49-mh5q">Cache confusion of response bodies for requests with bodies containing invalid UTF-8 byte sequences</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-q8wf-6r8g-63ch">Denial of Service in the Image Optimization API using SVGs</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-955p-x3mx-jcvp">Unauthenticated disclosure of internal Server Function endpoints</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-4c39-4ccg-62r3">Unbounded Server Action payload in Edge runtime</a></li>
</ul>
<h2>v16.2.10</h2>
<p>Contains no changes except publishing <code>@next/swc-wasm-web</code> which was accidentally not published since 16.2.4.</p>
<h2>v16.2.9</h2>
<p>Empty release to ensure <code>next@latest</code> points at a stable release. Next.js only allows publishing with Trusted Publishing enabled. In order to fix NPM dist-tags, we have to release a new version. Updating dist-tags is not possible with Trusted Publishing.</p>
<h2>v16.2.8</h2>
<p>Release with no changes in an attempt to fix <code>next@latest</code> pointing at a prerelease version.</p>
<h2>v16.2.7</h2>
<blockquote>
<p>[!NOTE]
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>Backport documentation fixes for v16.2 (<a href="https://redirect.github.com/vercel/next.js/issues/93804">#93804</a>)</li>
<li>[backport] Patch <code>playwright-core</code> to resolve <code>_finishedPromise</code> on <code>requestFailed</code> (<a href="https://redirect.github.com/vercel/next.js/issues/93920">#93920</a>)</li>
<li>[backport] Fix dev mode hydration failure when page is served from HTTP cache (<a href="https://redirect.github.com/vercel/next.js/issues/93492">#93492</a>)</li>
<li>[backport] Fix catch-all <code>router.query</code> corruption with <code>basePath</code> + <code>rewrites</code> (<a href="https://redirect.github.com/vercel/next.js/issues/93917">#93917</a>)</li>
<li>[backport] Encode non-ASCII characters in cache tags at construction (<a href="https://redirect.github.com/vercel/next.js/issues/93918">#93918</a>)</li>
<li>[backport] Fix server action forwarding loop with middleware rewrites (<a href="https://redirect.github.com/vercel/next.js/issues/93919">#93919</a>)</li>
<li>[backport] Turbopack: switch from base40 to base38 hash encoding (<a href="https://redirect.github.com/vercel/next.js/issues/93932">#93932</a>)</li>
<li>[ci] Disable hanging node 24 typescript tests on 16.2 backport branch (<a href="https://redirect.github.com/vercel/next.js/issues/94164">#94164</a>)</li>
<li>[backport] Fix &quot;type: module&quot; in project dir when using standalone or adapters (<a href="https://redirect.github.com/vercel/next.js/issues/94050">#94050</a>)</li>
<li>[backport] Propagate adapter preferred regions (<a href="https://redirect.github.com/vercel/next.js/issues/94200">#94200</a>)</li>
<li>[16.2.x] Don't drop <code>FormData</code> entries (<a href="https://redirect.github.com/vercel/next.js/issues/94240">#94240</a>)</li>
<li>[backport] feat(turbopack): add LocalPathOrProjectPath PostCSS config resolution (<a href="https://redirect.github.com/vercel/next.js/issues/94284">#94284</a>)</li>
</ul>
<h3>Credits</h3>
<p>Huge thanks to <a href="https://github.com/eps1lon"><code>@​eps1lon</code></a>, <a href="https://github.com/icyJoseph"><code>@​icyJoseph</code></a>, <a href="https://github.com/unstubbable"><code>@​unstubbable</code></a>, <a href="https://github.com/mischnic"><code>@​mischnic</code></a>, <a href="https://github.com/bgw"><code>@​bgw</code></a>, <a href="https://github.com/timneutkens"><code>@​timneutkens</code></a>, and <a href="https://github.com/lukesandberg"><code>@​lukesandberg</code></a> for helping!</p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/9beca0821cf4606ae33466ed6f4fc75f2887a4da"><code>9beca08</code></a> v16.2.11</li>
<li><a href="https://github.com/vercel/next.js/commit/3c48c7af78f2c01691065cb303da1b107a2c8617"><code>3c48c7a</code></a> [16.x] Fix Turbopack middleware matcher with i18n single locale</li>
<li><a href="https://github.com/vercel/next.js/commit/ac1eff3f7a7285176396ecc69c3b160a3d6ad1a2"><code>ac1eff3</code></a> [16.x] Improve performance of checking valid MPA form submissions</li>
<li><a href="https://github.com/vercel/next.js/commit/9a4651e754f70b12e397694ffc41f44c3ba8cc17"><code>9a4651e</code></a> [16.x] Enforce <code>serverActions.bodySizeLimit</code> for Server Actions in Edge runtime</li>
<li><a href="https://github.com/vercel/next.js/commit/b51206321854193208c0805ba42acc49287f942b"><code>b512063</code></a> [16.x] Set correct origin for internal redirects in custom server</li>
<li><a href="https://github.com/vercel/next.js/commit/d3033266c6dff23f7be71e19341fe3a8c6e2c599"><code>d303326</code></a> [16.x] Ensure exotic rewrite param values are properly encoded</li>
<li><a href="https://github.com/vercel/next.js/commit/73b94872bc343d09494b50394d8c08eb9fc8e56a"><code>73b9487</code></a> [16.x] fix(fetch-cache): key fetch(Request, init) by the effective request</li>
<li><a href="https://github.com/vercel/next.js/commit/bf9d17fb30501829f6fd7c0ee8e44e2794565742"><code>bf9d17f</code></a> [16.x] fix(incremental-cache): byte-exact fetch cache key for binary bodies</li>
<li><a href="https://github.com/vercel/next.js/commit/fe28768f533582ea8f6ee7d7a7498715927d45f5"><code>fe28768</code></a> [16.x] fix(next/image): improve performance of detectContentType()</li>
<li><a href="https://github.com/vercel/next.js/commit/d8afb8d550ac4ac5c106ea1410c3af43eaf1d469"><code>d8afb8d</code></a> [16.x] Performance improvements when decoding React Server function payloads</li>
<li>Additional commits viewable in <a href="https://github.com/vercel/next.js/compare/v16.2.6...v16.2.11">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=16.2.6&new-version=16.2.11)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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

### [docs: Web UI の Node runtime 依存インベントリを追加 (#885)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/903)

**作成者:** yasumorishima  
**作成日:** 2026-06-27T09:38:54Z  
**変更:** +113 -0 (1ファイル)  
**マージ日:** 2026-09-08T14:19:25Z  
**内容:**

## 概要

#885 の完了条件 第1項「Web UI の runtime Node 依存一覧のドキュメント化」に向けて、current `main` を精読し、`apps/admin` / `apps/public-viewer` / `apps/static-site-builder` の Node.js runtime 依存を棚卸しした docs を追加します。

- 追加: `docs/development/web-ui-node-runtime-dependencies.md`（`mkdocs.yml` は `nav:` 明示なし＝自動ナビなので追加だけで反映されます）
- **ドキュメントのみの変更で、挙動への影響はありません。**

## 主な発見

- **admin**: Node runtime 依存はほぼ「FastAPI への薄い proxy（Server Action 15本）」と「static export 阻害設定」だけ。Node 固有処理（ファイル生成 / zip / build）は 0。
- **public-viewer**: 既に `NEXT_PUBLIC_OUTPUT_MODE=export` モードを持ち、runtime の Node 依存（ISR / `connection()` / server fetch）は export ビルドで build 時処理に倒れて解決済み。残るのは「export ビルド自体に Node + Next + API 到達が必要」という build 時依存のみ。
- **static-site-builder**: ⭐ 単一exe化の最大の障壁。`POST /build` のたびに runtime で `next build`（`pnpm run build:static`）を子プロセス実行し、生成した `out/` を zip 返却する設計。「静的ファイルを生成する行為そのもの」が runtime の Node/Next build に依存しています。

## ひとつ伺いたい設計判断

admin の Server Action 14本は既に `NEXT_PUBLIC_ADMIN_API_KEY`（client 露出可）+ `getApiBaseUrl()` を使うだけの proxy なので、`"use server"` を外せば機械的に client fetch 化できます。ただしこれは **standalone（hosted）モードのネットワークモデルも「ブラウザ→Next サーバ経由」から「ブラウザ→FastAPI 直 + CORS」へ変える**ことを意味します。

- **(A)** export / local desktop モードのみ client 直叩きにし、standalone は現状の Server Action proxy を維持（モード分岐を持つ）
- **(B)** 両モードとも client 直叩きに寄せて Server Action を廃し、hosted では FastAPI 側に CORS / 認証を持たせる

どちらの方針が好ましいでしょうか。これが決まれば prototype（admin の export 化）を進めます。`ADMIN_API_KEY`（真にサーバ専用）を使う `duplicateReport` と `config` route handler だけは、local desktop の threat model（client にキーを載せてよいか）を別途決める必要があります。

## 補足

- 配置パス・粒度・ファイル名はご希望に合わせて調整します（不要であれば close いただいて構いません）。


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Documentation**
  * Added a new reference documenting Node.js runtime dependencies across the web UI apps.
  * Clarified which apps still rely on build-time Node.js tasks versus those that can run without runtime Node.js.
  * Summarized current blockers and next steps for moving toward export-based builds and simpler deployment.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (2件)

### [chore(deps): bump next from 16.2.11 to 16.3.3 in /utils/dummy-server](https://github.com/digitaldemocracy2030/kouchou-ai/pull/937)

**作成者:** dependabot[bot]  
**作成日:** 2026-09-09T07:11:32Z  
**変更:** +1 -1 (1ファイル)  
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

### [Enable OpenAI Flex Processing for GPT-5/6 models](https://github.com/digitaldemocracy2030/kouchou-ai/pull/917)

**作成者:** Copilot  
**作成日:** 2026-09-07T20:09:35Z  
**変更:** +63 -9 (2ファイル)  
**内容:**

OpenAI costs were leaving the standard service tier enabled even for models that support Flex Processing, which means we were not taking advantage of the lower-cost option when it was available. Flex trades latency for lower pricing, and the current generation of GPT-5/6 models makes that tradeoff worthwhile.

- Summary
  - Add Flex Processing automatically for OpenAI models in the GPT-5/6 family.
  - Keep legacy models on their default service tier to avoid changing behavior for unsupported or older generations.
  - Allow explicit opt-out via `OPENAI_USE_FLEX=false` for environments that need to force the standard path.

- Changes
  - Added a centralized `OpenAI` request guard in the shared LLM helper that detects supported Flex models and sets `service_tier="flex"`.
  - Applied the same logic to both standard chat completion requests and structured-output (`response_format` / Pydantic schema) requests.
  - Left GPT-4 and other non-Flex-supported models unchanged so we do not regress compatibility or latency-sensitive workloads.
  - Added focused regression coverage to confirm the Flex flag is attached for supported models and omitted otherwise.

```python
if _should_use_openai_flex(model):
    payload["service_tier"] = "flex"
```

- Impact
  - Lower OpenAI spend for the current GPT-5/6 family without broadening the change surface beyond the actual cost-optimization path.
  - No behavior change for older model families that do not support Flex Processing.

<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes #916

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

