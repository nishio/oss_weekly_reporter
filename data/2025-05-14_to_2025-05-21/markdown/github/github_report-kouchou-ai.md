# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-05-14T12:25:48.007939+09:00 から 2025-05-21T12:25:48.007939+09:00 まで

## Issues

### 過去7日間に完了されたissue (8件)

### [[FEATURE] 利用規約をoptionalにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/539)

**作成者:** nasuka  
**作成日:** 2025-05-19T05:40:41Z  
**内容:**

# 背景
* メタデータの設定において、現在は利用規約が必須になっているが、サービスの性質としてユーザー登録を伴うわけではないので利用規約は必須ではない


# 提案内容
* `metadata.json` において、termsLinkのデフォルト値をnullにする
* termsLinkがnullの場合は `利用規約` をフッターで表示しないようにする

![Image](https://github.com/user-attachments/assets/b5d6f894-7e57-4914-9fb6-e478283b1949)

**コメント:** なし

---

### [[BUG] 実装済みの機能の説明に「将来実装予定」という文言が残っている](https://github.com/digitaldemocracy2030/kouchou-ai/issues/532)

**作成者:** shingo-ohki  
**作成日:** 2025-05-18T01:22:31Z  
**内容:**

### 概要

Local LLM の対応はすでに実装済みだが、レポート生成ページ(client-admin)のUIの説明に将来実装予定という文言が残っている

### スクリーンショット・ログ

![Image](https://github.com/user-attachments/assets/a6a57289-8c64-4c6f-8a12-00214159a7c1)

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->


**コメント:** なし

---

### [エネルギー庁パブコメのpdf -> csv化](https://github.com/digitaldemocracy2030/kouchou-ai/issues/467)

**作成者:** nasuka  
**作成日:** 2025-05-08T07:24:34Z  
**内容:**

# 背景
パブコメデータを入手できたがpdf形式のため、csvなどの扱いやすい形式に変換する必要がある。

データはこちら
https://w1740803485-clv347541.slack.com/archives/C08PX74S5T4/p1746688643277269


nishioさんが以前別のパブコメ向けに作成していたスクリプトはあるが、恐らくそのまま適用することは難しい
```
PDFからCSVを生成するプログラムは文化庁バブコメの時に作ったものがあります
https://github.com/nishio/aipubcom-data
[16:18](https://w1740803485-clv347541.slack.com/archives/C08PX74S5T4/p1746688728888009)
が、そのまま使えることはないと思うので試してみて正規表現を直したりすることが必要です
16:19
僕は17時から出かけるので作業できないですが、これをCSVに変換するところをできる人がいればお任せしたい
New
16:21
作りかけていたツールはこちらにあります
https://github.com/nishio/pubcom-seiri
単純一致を検知してフィルタするとか、embeddingで距離を計算するとかはtool1.pyで大体実装済み
このパブコメデータでまともに動くかどうかが今後検証が必要なところです
```

# 実施内容
・パブコメをpdf -> csvに変換する
・広聴AIへのPRは不要。独立したスクリプトを実装する。

**コメント:** なし

---

### [[design]#400 #421 に関連したマスター反映 & マスターデザイン作成](https://github.com/digitaldemocracy2030/kouchou-ai/issues/447)

**作成者:** UtkNggc  
**作成日:** 2025-05-07T02:00:20Z  
**内容:**

・421で管理画面のボタン追加があるのでマスターに反映
・そのボタン押下後の画面がないのでマスター作成

https://github.com/digitaldemocracy2030/kouchou-ai/pull/400
https://github.com/digitaldemocracy2030/kouchou-ai/pull/421

**コメント:** なし

---

### [[design]ブランドコンパス制定](https://github.com/digitaldemocracy2030/kouchou-ai/issues/416)

**作成者:** UtkNggc  
**作成日:** 2025-05-02T07:37:24Z  
**内容:**

UI/UX/ワーディング/トンマナ、などを考える際の意思決定材料を制定したい。

### 作成場所
▼Figma Brand Compass スライドファイル
https://www.figma.com/slides/0B55u8rxDjjjpRJbNUEP0Z/%F0%9F%A7%AD-Brand-Compass?node-id=1-42&t=LFrlwNUh5bLJE7rA-1
スライドにした理由は、外部に広報する際にもリンク渡すだけでいいので便利だから

### 具体的には
・Vision Mission Values
・Brand Personality
・Brand Promise
・Design Principles
・Do & Don't
など。意思決定の材料になりそうなもの。

### 必要なもの
・現時点で固まってる指針（ふわっとでもok）
・先にジョインされてるメンバーさんたちが感じる本プロダクトの特性
・なんとなく共通認識になってるもの
などを、slackを漁ったりヒアリングをしたりして集めたい。
↑このヒアリングに広聴AIを利用したいです！！！（当事者としてUXを体験したい）

### 予定している手法
①上記の必要なものを集める
②集めた内容をもとに各内容に落とし込んで整えていく
③Figmaスライドにまとめる
④共通認識になるように全体に共有

### NEXT STEP
ブランドコンパスがあれば、ロゴ制作も可能です。

**コメント:** なし

---

### [[FEATURE] OpenRouterを使えるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/402)

**作成者:** nasuka  
**作成日:** 2025-04-30T08:55:15Z  
**内容:**

# 背景
* OpenAIが使えないユースケースがある
  * 政治的なキャンペーンでの利用ができない
    * 参考: https://github.com/digitaldemocracy2030/kouchou-ai/issues/255 
  * このため、用途によっては政党が利用できないケースがある
* そもそもOpenAIのみに依存している状況は好ましくないため、使えるLLMの選択肢は増やしたい
* また、OpenAI だと Rate Limit が厳しいという問題もある
  * https://github.com/digitaldemocracy2030/kouchou-ai/issues/295


# 提案内容
* OpenRouterを導入する

# 実装方針案
api
* 環境変数にOpenRouterのAPI Keyをセットできるようにする
* OpenRouterでAPIリクエストを投げられるようにする
  * すべてのモデルをサポートすると厳しそうなので、一旦以下をサポートできると良さそう
    * OpenAI（gpt-4o, 4o-mini）
      * 4.1系列もサポートしても良いかも？
    * Gemini（gemini2.5系列） 
  * 上記のモデルはstructured outputもサポートされているので実装が容易

client-admin
* 環境変数がセットされている場合にOpenRouterのモデルを選択肢に表示する 
  * あわせて、OpenAIのAPIキーがセットされている場合のみ、OpenAIのモデルを選択肢に表示するようにした方が良いかも（今はAPIキーがセットされていなくてもデフォルトで3つの選択肢が表示されている）
    * OpenAI APIキーで使うOpenAIのモデルとOpenRouterで使うOpenAIのモデルは区別できるようにしておいた方が良さそう（リクエストをapiに投げるときにどちらで投げるか判別できるようにするため）
      * e.g. `OpenAI gpt-4o` , `OpenRouter gpt-4o` のような表記にする？
* レポート作成時に選択されたモデルでapiにリクエストを送る
![Image](https://github.com/user-attachments/assets/dda0a3c7-ca57-4709-9c69-933f6eec3628)




**コメント:** なし

---

### [[BUG] 静的ファイルがGithub Pagesでうまく表示されない件](https://github.com/digitaldemocracy2030/kouchou-ai/issues/274)

**作成者:** keisuke-a  
**作成日:** 2025-04-10T06:52:19Z  
**内容:**

### 概要

静的ファイルをoutして、その中身をgithub pagesで公開すると、out/index.html自体は表示はされるが、画像要素がなかったりリンク先（個別ページ）が404になるなど、うまく表示されない。（参照が絶対パスになってることによる？）


**コメント:** なし

---

### [[REFACTOR] 濃いクラスタのアイコン変更](https://github.com/digitaldemocracy2030/kouchou-ai/issues/113)

**作成者:** nishio  
**作成日:** 2025-03-20T12:20:30Z  
**内容:**

# 現在の問題点

<img width="249" alt="Image" src="https://github.com/user-attachments/assets/bc626d04-e7c0-4245-9b01-e762d433a434" />

濃いクラスタのアイコンは特に意味はなくこれになっている


# 提案内容

多分叩き台の案がないとどう変えたらいいかの議論もできないと思うので雑に描いておく

![Image](https://github.com/user-attachments/assets/9e46dfd6-71d4-4c2b-bbd5-1c79220c8d80)

アイコンとしてデザインできるかは度外視して描くとこんな感じで「全体像」は全体にたくさんの点が散らばっており、「濃いクラスタ」はぎゅっとした「濃い」「密度の高い」塊がいくつかある感じ

**コメント:** なし

---

### 過去7日間に作成されたissue (19件)

### [[BUG] report_status.jsonが初期化される](https://github.com/digitaldemocracy2030/kouchou-ai/issues/553)

**作成者:** mtane0412  
**作成日:** 2025-05-21T01:54:38Z  
**内容:**

### 概要

一旦メモ

1. docker compose up後にlocalhost:4000が立ち上がる
2. localhost:4000を開くとレポートが読込中
3. このタイミングでブラウザ更新する
4. ログでslugに関して例外が出てレポートが表示されなくなる

手動でreport_status.jsonのtest-slugの情報を消すとレポートなしの状態で再び使えるようになる。
```report_status.json
{}
```

scripts/fetch_reports.py で作成されたレポートから復元できる？
やってみたけどなんかのAPIキーが必要そう(Azure限定?)

#549 作業中に発生して関連がないか調べる。
dockerのディスク空き容量で` No space left on device` が出ていたのでそっち関連かもしれない。
mainブランチで発生するかまだ調べていない。


### 再現手順
todo: 調べる
1. <!-- バグが再現する手順をステップごとに記入してください -->
2. 
3. 

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->

### スクリーンショット・ログ

report_status.jsonがこのデフォルトの状態になっている
```
{
    "test-slug": {
        "status": "ready",
        "title": "Test Report",
        "description": "Test Description",
        "visibility": "public",
        "is_pubcom": false,
        "created_at": "2023-01-01T00:00:00Z",
        "token_usage": 800,
        "token_usage_input": 350,
        "token_usage_output": 450,
        "provider": "openai",
        "model": "gpt-4o"
    }
}
```
この状態でtest-slugを取りに行くのでエラーが出る。
```
api-1 | 2025-05-20 14:21:10 [error ] Request URL: http://api:8000/reports - Exception: 1 validation error for Report
api-1 | slug
api-1 | Field required [type=missing, input_value={'status': 'ready', 'titl...nai', 'model': 'gpt-4o'}, input_type=dict]
```

### その他
report_status.json まわりの挙動をよく理解していない

**コメント:** なし

---

### [PR #531 レビュー：属性カラム選択とフィルタリング機能](https://github.com/digitaldemocracy2030/kouchou-ai/issues/552)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-05-21T00:38:16Z  
**内容:**

# PR #531 レビュー：属性カラム選択とフィルタリング機能

## 概要
このPRは広聴AIアプリケーションに属性カラム選択とフィルタリング機能を実装しています。ユーザーはCSV/スプレッドシートデータのインポート時に属性カラムを選択し、これらの属性に基づいてレポートの可視化をフィルタリングすることができます。

## フロントエンド変更点
- データインポート時に属性カラムを選択するための新しいコンポーネント `AttributeColumnsSelector.tsx` を追加
- 属性カラム選択を統合するために `CsvFileTab.tsx` と `SpreadsheetTab.tsx` を修正
- 属性に基づいてデータをフィルタリングするための `AttributeFilterDialog.tsx` コンポーネントを追加
- フィルタリングされたビューをサポートするために可視化コンポーネントを強化：
  - フィルターに基づいてポイントをハイライト/薄暗くするように `ScatterChart.tsx` を修正
  - 属性フィルタリングをサポートするように `TreemapChart.tsx` を更新
  - チャートコントロールに属性フィルターボタンを追加
- フィルタリングロジックのための `attributeFilterUtils.ts` にユーティリティ関数を追加

## バックエンド変更点
- "attribute_" プレフィックスを持つ属性フィールドを処理するために <ref_file file="/home/ubuntu/repos/kouchou-ai/server/src/services/report_launcher.py" /> を更新
- <ref_file file="/home/ubuntu/repos/kouchou-ai/server/broadlistening/pipeline/steps/hierarchical_aggregation.py" /> を強化：
  - レポート生成パイプラインで属性データを処理
  - NumPy型のJSONシリアル化を追加
  - CSV出力に属性カラムを含める

## 良い点
- 機能実装はフルスタック全体にわたって包括的
- 属性選択のUIは直感的で既存のワークフローとうまく統合されている
- フィルタリング機能はカテゴリ型と数値型の両方の属性タイプをサポート
- 可視化コンポーネントはフィルタリングされたデータを視覚的な区別で適切に処理
- バックエンド変更は後方互換性を維持

## 改善点
1. **エラー処理**：
   - 属性カラム選択の検証と特殊文字の処理の改善
   - フィルターの無効な数値範囲のエラー状態の追加

2. **パフォーマンスの考慮事項**：
   - 大きな属性リストには仮想スクロールが実装されていますが、多くの属性を持つデータセットには他の最適化が必要かもしれません
   - 非常に大きなデータセットに対する遅延読み込みまたはページネーションの検討

3. **コード構成**：
   - 一部のコンポーネント（`AttributeFilterDialog.tsx`など）はかなり大きく、さらに分割できる可能性があります
   - フィルタリングロジックは複数の場所で重複しており、さらに集中化できる可能性があります

4. **テスト**：
   - この機能のテスト更新は見つかりませんでした
   - 属性フィルタリングロジックの単体テストとUIコンポーネントの統合テストの追加を検討

5. **ドキュメント**：
   - 新しい属性フィルタリング機能のユーザードキュメントを追加
   - 複雑なフィルタリングロジックにコードコメントを追加することを検討

## 推奨事項
1. 異なる属性データ型のエッジケースのエラー処理に対応
2. 新機能の包括的なテストを追加
3. より良いメンテナンス性のために大きなコンポーネントのリファクタリングを検討
4. 属性フィルタリング機能のユーザードキュメントを強化


**コメント:** なし

---

### [PR #531 Review: Attribute Column Selection and Filtering Feature](https://github.com/digitaldemocracy2030/kouchou-ai/issues/551)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-05-21T00:37:42Z  
**内容:**

# PR #531 Review: Attribute Column Selection and Filtering Feature

## Overview
This PR implements attribute column selection and filtering functionality in the kouchou-ai application. It allows users to select attribute columns from CSV/spreadsheet data during import and then filter report visualizations based on these attributes.

## Frontend Changes
- Added new component `AttributeColumnsSelector.tsx` for selecting attribute columns during data import
- Modified `CsvFileTab.tsx` and `SpreadsheetTab.tsx` to integrate attribute column selection
- Added `AttributeFilterDialog.tsx` component for filtering data based on attributes
- Enhanced visualization components to support filtered views:
  - Modified `ScatterChart.tsx` to highlight/dim points based on filters
  - Updated `TreemapChart.tsx` to support attribute filtering
  - Added attribute filter button to chart controls
- Added utility functions in `attributeFilterUtils.ts` for filtering logic

## Backend Changes
- Updated <ref_file file="/home/ubuntu/repos/kouchou-ai/server/src/services/report_launcher.py" /> to handle attribute fields with "attribute_" prefix
- Enhanced <ref_file file="/home/ubuntu/repos/kouchou-ai/server/broadlistening/pipeline/steps/hierarchical_aggregation.py" /> to:
  - Process attribute data in the report generation pipeline
  - Add JSON serialization for NumPy types
  - Include attribute columns in CSV export

## Positive Aspects
- Feature implementation is comprehensive across the full stack
- UI for attribute selection is intuitive and integrates well with existing workflows
- Filtering functionality supports both categorical and numeric attribute types
- Visualization components properly handle filtered data with visual distinctions
- Backend changes maintain backward compatibility

## Areas for Improvement
1. **Error Handling**:
   - Better validation for attribute column selection and handling of special characters
   - Error states for invalid numeric ranges in filters

2. **Performance Considerations**:
   - Virtual scroll is implemented for large attribute lists, but other optimizations may be needed for datasets with many attributes
   - Consider lazy loading or pagination for very large datasets

3. **Code Organization**:
   - Some components (like `AttributeFilterDialog.tsx`) are quite large and could be broken down further
   - Filtering logic is duplicated in a few places and could be further centralized

4. **Testing**:
   - No test updates were found for this feature
   - Consider adding unit tests for attribute filtering logic and integration tests for the UI components

5. **Documentation**:
   - Add user documentation for the new attribute filtering functionality
   - Consider adding code comments for complex filtering logic

## Recommendations
1. Address error handling for edge cases with different attribute data types
2. Add comprehensive tests for the new functionality
3. Consider refactoring larger components for better maintainability
4. Enhance user documentation for the attribute filtering feature


**コメント:** なし

---

### [各ステップの中間ファイルをcsvではなくDBで管理する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/548)

**作成者:** coderabbitai[bot]  
**作成日:** 2025-05-20T08:56:34Z  
**内容:**

## 背景
* 現状は outputs/ 配下の CSV (例: args.csv) を中間ファイルとして保存し、最終成果物 hierarchical_result.json を再生成している。
* 手動編集を行った際にcsvを編集するが、csv管理だとデータの更新時に不整合が発生する可能性がある
* また、レポートの複製機能を実装する場合、新規にレコードを作成せず、作成済みのextraction結果を使い回せるようにな

複製機能のissue:
https://github.com/digitaldemocracy2030/kouchou-ai/issues/19


## 提案
ファイルベースの管理からデータベース（DB）ベースの管理へ移行することで、以下の利点が得られる。

- トランザクション管理によるアトミック性の確保
- 複数ユーザーによる同時編集時の競合管理の改善
- データの一貫性と整合性の向上
- バックアップと復元の容易化
- パフォーマンスの最適化（特に大量データ処理時）


懸念事項等のメモ:
https://github.com/digitaldemocracy2030/kouchou-ai/issues/310#issuecomment-2888243252


**コメント:** なし

---

### [[FEATURE] adminにおいて、APIルートを介してfastapiにリクエストを送る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/547)

**作成者:** nasuka  
**作成日:** 2025-05-20T08:25:30Z  
**内容:**

# 背景
* adminにおいて、 `process.env.NEXT_PUBLIC_ADMIN_API_KEY` でAPIキーを読んでリクエストをfastapiに送っているが、APIキーが漏洩するリスクがある
* APIキーの露出をさせられる（攻撃できる）のは、以下の状況に限定されるためリスクが高い訳ではないが、ゼロではない
  * 広聴AIをリモートでホスティングしている
  * 攻撃者が管理画面のURLを知っている
  * 攻撃者が管理画面にログインしている（id/passwordを知っている）

参考
https://github.com/digitaldemocracy2030/kouchou-ai/pull/545#discussion_r2097241946


# 提案内容
Next.jsのAPIルートをadminに用意したうえで、fastapiと疎通する
（一旦CodeRabbitの指摘内容をそのまま書いていますがこの方針が妥当か自信がないので、next.jsに詳しい方いたらコメントいただけると助かります）

**コメント:** なし

---

### [[REFACTOR] APIのエラーハンドリングの共通化](https://github.com/digitaldemocracy2030/kouchou-ai/issues/546)

**作成者:** nasuka  
**作成日:** 2025-05-20T08:00:54Z  
**内容:**

# 現在の問題点
* エラーハンドリングが各endpointのコード内に散逸している

# 提案内容
* FastAPI の例外ハンドラ（@app.exception_handler）を定義し、共通の HTTPException 処理を移譲
* 共通デコレータを作成して、エンドポイントごとの try–except を簡潔化

参考https://github.com/digitaldemocracy2030/kouchou-ai/pull/545#discussion_r2097241922


**コメント:** なし

---

### [[DOCUMENT・FEATURE] レポートに関する責任の所在について明記する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/542)

**作成者:** nasuka  
**作成日:** 2025-05-19T08:00:39Z  
**内容:**

# 現在の問題点
* レポートに関する責任の所在について、明記されていない
  * レポートのfooterにはdd2030の免責事項が記載されているが、上記の内容が記載されていない

参考: https://github.com/digitaldemocracy2030/kouchou-ai/issues/539#issuecomment-2890006194

# 提案内容
README/footerの免責事項に、レポートに関する責任の所在を明記する




**コメント:** なし

---

### [[FEATURE] OpenRouterの無料モデルを追加する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/537)

**作成者:** tokoroten  
**作成日:** 2025-05-18T14:39:16Z  
**内容:**

# 背景
OpenRouterの無料モデルを使えるようにして、無料で広聴AIを使えるようにしたい。

OpenRouterは、学習されるが代わりに無料に使えるという口を用意している。
ただし、オプトアウト設定をすれば、学習はされない。

# 提案内容

試しに実装してみた感じ、エラーを吐いて使えなかったので、原因をちょっと深堀する必要がある。
おそらく、OpenAIのライブラリを使って、ベータ版のAPI　client.beta.chat.completions.parse をコールしているのが原因ではないかと考えている。
local llmと同様のコードにすれば、何とかならんかと思ってるが、検証不足

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

### [[design]ブロードリスニングとは？の説明画像の更新](https://github.com/digitaldemocracy2030/kouchou-ai/issues/529)

**作成者:** nanaueki  
**作成日:** 2025-05-17T13:44:41Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
デザイン統一性の向上

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
修正前
<img width="863" alt="Image" src="https://github.com/user-attachments/assets/6efa55b4-97db-4684-b954-def838bf6427" />

修正後
後日決定案を添付

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

### [[FEATURE]限定公開のページにはnoindexオプションを付ける](https://github.com/digitaldemocracy2030/kouchou-ai/issues/520)

**作成者:** tokoroten  
**作成日:** 2025-05-15T09:24:45Z  
**内容:**

# 背景

限定公開のページであっても、過去に公開していたり、何らかのひょうしにURLが外部に漏れると、ウェブクローラが巡回して拾っていく可能性がある

# 提案内容

限定公開の時はnorobotを付けて、検索エンジン避けをしておく
```html

<meta name="robots" content="noindex" />
```

**コメント:** なし

---

### [[DOCUMENT]エネルギー庁パブコメの分析レポート公開](https://github.com/digitaldemocracy2030/kouchou-ai/issues/519)

**作成者:** nishio  
**作成日:** 2025-05-15T08:10:02Z  
**内容:**


- https://github.com/digitaldemocracy2030/kouchou-ai/issues/467#issuecomment-2865366585
- データはできたのでレポートを書く

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

**コメント:** なし

---

### [ウェルカムミーティングで募集すべき役割を具体化する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/517)

**作成者:** shingo-ohki  
**作成日:** 2025-05-14T11:51:15Z  
**内容:**

募集する役割を整理したほうがいいかも？

- PdM
- フロントエンジニア

>小野翔太
20:48
＞リクルーティングのはなし
コミュニティ運営で、ウェルカムミーティングを開催しようと思っています。そこでつかう資料に、募集をかけるスライドがあるので、そこに載せたいです

from 開発定例

**コメント:** なし

---

### [[ALGORITHM]クラスタ数、エンベディング、次元圧縮の違いのモデルの違いによるシルエットスコア（まとまり具合）の変化の調査](https://github.com/digitaldemocracy2030/kouchou-ai/issues/516)

**作成者:** take365  
**作成日:** 2025-05-14T10:27:15Z  
**内容:**

# 背景
エンベディングの選択や、クラスタ数自動決定、異なる次元圧縮などの可能性につなげる調査


# 提案内容
クラスタ数、エンベディング、次元圧縮の違いのモデルの違いによるシルエットスコア（まとまり具合）の変化の調査

# 対象データ
サンプルデータ（400件）
パブコメエネルギー政策（2170件）
パブコメ環境省（567件）
StackOverflow日本語版（4532件）



# 実験結果について（実験を実施される方向け）
* 実験結果はこちらの[Google Docs](https://docs.google.com/document/d/1GK4Arh8ZyJmQjQ4iW1CRMruEUPicKAAUZEZi2TpAo4w/edit?tab=t.0#heading=h.j72jxw32gila)に記載してください

**コメント:** なし

---

### [[FEATURE] 別のレポートのUMAPを使い回す](https://github.com/digitaldemocracy2030/kouchou-ai/issues/515)

**作成者:** nasuka  
**作成日:** 2025-05-14T02:44:06Z  
**内容:**

# 背景
* UMAPの実行結果がレポート出力毎に異なる
* これにより、同じデータを入力しても見た目がかなり変わるレポートが出力されてしまうためユーザー側の解釈が難しくなる

参考:
https://dd2030.slack.com/archives/C08F7JZPD63/p1747176858166689


# 提案内容
別のレポートのUMAPを使い回せるようにする。これにより、過去出力したレポートと同一の平面上にテキスト（=extraction結果）をプロットできるようになるため、時系列による傾向の変化等を比較しやすくなる。

## 実装案
api
* レポート出力時にUMAPのモデルを保存するようにする
  * 既存のレポートのUMAPを使い回す場合は、保存したUMAPをコピーして利用する
* レポートごとの実行パラメータ（config）を取得するendpointを実装する
  * admin側で、利用しているembedding等の情報を取得するため

admin
AI詳細設定内で以下の設定項目を新設する。
* UMAPのモデルを新規作成するか既存のレポートのものを使い回すかを選択できるようにする
* 既存のレポートのものを使い回す場合に、利用元のレポートを選択できるようにする

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

### [[FEATURE] 確率的挙動がある箇所にはランダムシードを設定して結果を固定する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/513)

**作成者:** tokoroten  
**作成日:** 2025-05-14T00:18:23Z  
**内容:**

# 背景

同じデータを入力しても同じ結果にならない

# 提案内容

ランダムシードを設定する

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(15件)

### [[FEATURE]windows直環境での起動手順・構成を整備する（python仮想環境＋npm 対応）](https://github.com/digitaldemocracy2030/kouchou-ai/issues/509)

**作成者:** take365  
**作成日:** 2025-05-13T14:28:44Z  
**内容:**

### 🔍 概要
現在の `kouchou-ai` プロジェクトは Linux/Mac 環境での実行を前提にしている部分があり、Windows 環境での手動起動・開発がやや煩雑です。  
この Issue では、Windows 上で仮想環境（Python venv）や npm を活用しながら、直接実行できる構成を整備することを目的とします。

---

### 🧭 背景
- #496 で求められている「すぐに動かせる構成」の一環。
- Windowsユーザーが詰まりやすい起動手順の改善。
- bash系スクリプトを使わずに、`cmd` / `PowerShell` で起動できる手順の整備。

---

### ✅ 対応内容（予定）
- `dev_win_direct.bat` の整備
  - 仮想環境 (`venv`) の `activate` による Python 実行
- `.env` の読み込み自動化（`python-dotenv` などを検討）
- README への起動手順（Windows向け）追記

---

### 🔗 関連PR
- draft: [PR #499](https://github.com/digitaldemocracy2030/kouchou-ai/pull/499)  
  → 本 Issue をもとに今後ブラッシュアップ予定

---



**コメント:** なし

---

### [[design] デザインシステム構築／color環境](https://github.com/digitaldemocracy2030/kouchou-ai/issues/504)

**作成者:** UtkNggc  
**作成日:** 2025-05-13T11:57:14Z  
**内容:**

https://github.com/digitaldemocracy2030/kouchou-ai/issues/443 で全体の設計ができたので、構築開始できます。
1つ1つのタスクが重いのでIssue分散してます。

このIssueではカラーに関わる環境を整備します。

## 手順

作業は広聴AIのFigmaファイルで行います。

1. chakraUIのカラーたちをすべてPrimitiveにいれる
2. Primitiveから選定してSemanticで定義（実質上のプロダクトカラー）
3. stylesに登録
4. Figmaファイル内にカラーガイドライン作成（ブランド思想用ではなくデザイナ&エンジニアが見る用に一覧性のあるもの）

### 期待できる効果

- デザイナーが容易に色選定できるようになる（エンハンス時の色の迷いを大幅に削減）
- chakraUI範囲内のカラーのため実装がやりやすいのではないか
- 将来的にchakraUIをはがして独自カラーを使うことになったとしてもPrimitiveの変更ですべて置き換わる

### 留意点
ブランドコンパス内のブランドパーソナリティとデザイントンマナを叶える設計にする
https://www.figma.com/slides/0B55u8rxDjjjpRJbNUEP0Z/%F0%9F%A7%AD-Brand-Compass?t=yLYyNEeIO9pprmn3-6

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

### [[FEATURE][design] レポート管理画面：直感的に使いやすくしたい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/460)

**作成者:** UtkNggc  
**作成日:** 2025-05-07T16:09:28Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
現状の管理画面は直感的に使いにくい。
あるていど機能がそろった現時点で管理画面を改善したい。

▼現状
![Image](https://github.com/user-attachments/assets/600f5c6f-4dda-4b0d-a272-75088588f063)

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
・機能の見出しを上部バーにまとめる
・各機能ボタンはアイコンやトグルなど直感的にわかるものにする
・新規作成ボタンを右上に移動
・作成日時の秒数トルツメ（もしかすると時間も？）
・レポートのURL表示トルツメ
![Image](https://github.com/user-attachments/assets/3777dc40-ec37-4dd7-ba76-db6323453f23)

# デザイン時に検討するもの
・全レポートをエクスポート機能の位置
・エラー、作成中、のstatesの表現どうするか
・エラー、作成中、のステップの要 / 不要 -> 要るならステップ数やプログレスバーも検討
・もしレポートのURLが必要なら「シェア」みたいな表現でもいいかも。

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/437：見出し文言&位置変更

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

### [[DOCUMENT] .github/copilot-instructions.md を設置したい。](https://github.com/digitaldemocracy2030/kouchou-ai/issues/445)

**作成者:** tokoroten  
**作成日:** 2025-05-07T01:18:45Z  
**内容:**

# 提案内容
Github Copilot Chatは、まず `.github/copilot-instructions.md` を必ず読み込み、そのうえで動作する。要するにこのファイルがシステムプロンプトとして振る舞う。

https://copilot-instructions.md/

そのため、傾聴AIに適合した、適切な copilot-instructions.md を設置することで、Github Copilot Chatを利用しているユーザの開発者体験を改善したい。

**コメント:** なし

---

### [[FEATURE][design] headerにプロダクト名を表示する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/441)

**作成者:** UtkNggc  
**作成日:** 2025-05-06T11:13:43Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
現在、header左の部分が「デジタル民主主義2030」になっている。
デジタル民主主義2030は、複数プロダクトを含むプロジェクト名なので、
プロダクト内のheaderではプロダクト名を表記したい。

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
・メイン「広聴AI」
・サブ「part of project デジタル民主主義2030」
で画像作成しました。こちらに変えていただくのはいかがでしょう。

▼Figma
https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=176-458&t=PgvCDEqVEw2sn016-11

■設計意図
・ロゴ制作するには時間がかかるので、現時点では取り急ぎフラットなフォントで作成。
・現在のロゴサイズと同じサイズで作成したので、画像のリンク先を変えていただくだけで実装完了いただける見込み。

# ご相談したいこと
「part of project」がしっくりきてない気がする。。もっとふさわしいものがないか。

![Image](https://github.com/user-attachments/assets/9df3d50f-5945-4f6b-a2c7-f4b582b4151e)

**コメント:** なし

---

### [[FEATURE][design] コンテンツ下部のAbout情報をFooterにまとめる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/438)

**作成者:** UtkNggc  
**作成日:** 2025-05-06T09:36:29Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
コンテンツエリア内はその画面独自のコンテンツのみにしたい。
About情報はプロジェクト情報なので、footerにまとめるのが適切。

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
Aboutの内容とFooterの内容を組み合わせたfooterを作成する。

※具体的なVDは担当デザイナーが作成します。

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

### [(実験) 同一の内容が大量に投稿される問題への対処法](https://github.com/digitaldemocracy2030/kouchou-ai/issues/346)

**作成者:** nasuka  
**作成日:** 2025-04-21T05:54:34Z  
**内容:**

# 背景
https://github.com/digitaldemocracy2030/kouchou-ai/issues/345
上記のIssueに紐づく実験のIssue

以下元Issueの背景を転載
* [パブコメの大量投稿](https://x.com/takahiroanno/status/1914151807443718381) によって、入力データの中に似通った内容が大量に含まれる場合がある
* これによって、以下の問題が起きる
  * 1.フロントの処理負荷が高くなる
    * 現在の設計では、数万件〜規模のデータは描画の負荷が高くPCによっては正常に表示できない可能性がある
  * 2.バックエンドの処理負荷・コストが高くなる
    * レポート出力処理の際のクラスタリングの計算負荷が高くなる・extraction処理にかかるLLM APIのコストが高くなる
  * 3.ユーザーの認知負荷が高くなる
    * 今の形式でクラスタリングや可視化を行うと、スパム的な意見が意見全体の大半を占めるために、本来着目したい意見が目立たなくなってしまう可能性がある


# 提案内容
* 類似する意見をあらかじめまとめたうえで、まとめた後の意見を広聴AIの分析にかける。
  * まとめた後の意見が表示されるようになることで、フロントの処理負荷が下がり、またユーザーの認知負荷も下がる
  クラスタよりもより細かい粒度で、「ほとんど同じことを言っている意見」がまとめられると良さそう？（あくまで一案で、この粒度でまとめるのがマストではない）
* まとめ方には幾つかのアプローチがありそう。
  * e.g. クラスタリングでまとめる、LLMでまとめる、そのハイブリッド等

↑は問題解決の一つのアプローチの案として記載していますが、他にアプローチがあれば随時コメントにご記載ください。

## 想定する進め方
* 実験データの選定（or 作成）
* 実験データに対して、アルゴリズムを適用し、アウトプットを確認
  * * @nishio , @nasuka （+ 時間があれば@takahiroanno も）あたりは確認しておけると良さそう
* 問題なさそうであれば機能実装の検討に移る




**コメント:** なし

---

### [（情報整理）同一の内容が大量に投稿される問題への対処法](https://github.com/digitaldemocracy2030/kouchou-ai/issues/345)

**作成者:** nasuka  
**作成日:** 2025-04-21T05:40:51Z  
**内容:**

# 背景
* [パブコメの大量投稿](https://x.com/takahiroanno/status/1914151807443718381) によって、入力データの中に似通った内容が大量に含まれる場合がある
* これによって、以下の問題が起きる
  * 1.フロントの処理負荷が高くなる
    * 現在の設計では、数万件〜規模のデータは描画の負荷が高くPCによっては正常に表示できない可能性がある
  * 2.バックエンドの処理負荷・コストが高くなる
    * レポート出力処理の際のクラスタリングの計算負荷が高くなる・extraction処理にかかるLLM APIのコストが高くなる
  * 3.ユーザーの認知負荷が高くなる
    * 今の形式でクラスタリングや可視化を行うと、スパム的な意見が意見全体の大半を占めるために、本来着目したい意見が目立たなくなってしまう可能性がある


# 進め方
* アルゴリズムの改善によって上記の問題を解決するかを検討する。
* いきなり機能を実装するのではなく、プロダクトとは独立して実験スクリプトを実装し、検証用のデータセットを使って結果の妥当性を評価する
* 問題なければプロダクトの機能として実装を進める
  * 一旦実験系のIssueだけ立てておき、機能することがわかった段階でプロダクトへの実装イシューを立てる

```
1: 独立したスクリプトとして機能するものを作れるが実験
2: それをapiサーバに統合するか検討
3: それをどんなGUIでユーザに見せるか検討
という流れがスムーズかなと思いました
```

**コメント:** なし

---

### [[FEATURE] LLMが出力した結果の手動修正機能（編集機能）がほしい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/310)

**作成者:** nasuka  
**作成日:** 2025-04-15T05:38:53Z  
**内容:**

# 背景
* LLMが出力したクラスタ名や説明、argumentが適切でない場合がある
  * e.g.
    * 公開するのに不適切な単語や表現がクラスタ名に含まれている
    * 他のクラスタと同一の内容がクラスタ名に含まれている
* このようなケースにおいては、LLMのアウトプットを見た後に人間が手動で文言を修正したい

# 提案内容
LLMが出力したテキスト（クラスタタイトル・説明・概要・argument）について、手動で編集する画面をadminに設け、レポートに編集内容を反映する


(admin)
* 上記の編集画面を設ける
  * 編集後のデータを編集用のendpointに送る

(api)
* 編集用のendpointを実装する
  * リクエストで受け取ったデータを各種中間ファイル（args.csv等）に保存
  * hierarchical_aggregation.pyを再度実行し、更新後のデータでhierarchical_result.jsonを保存する

そもそも全要素を編集できるようにするかというのは議論の余地がある。やるとしても、まずはクラスタ名のみを対象にするなど、部分的に始めていくのが良さそう。
また、透明性担保のために編集履歴を残すようにするかも議論の余地がある。

**コメント:** なし

---

### [[FEATURE]かかったコストの表示機能](https://github.com/digitaldemocracy2030/kouchou-ai/issues/284)

**作成者:** nishio  
**作成日:** 2025-04-12T23:42:45Z  
**内容:**

# 背景
実行ごとのトークン数やコストが表示されず、利用者がコスト感を把握しにくい。

from 4/12 meetup
>「clineのように実行のたびにトークン、コストが表示されるUIは確かによい(たねのぶ)」
>「使用者にコスト感覚がついていく」


# 提案内容
(解決策) UIに実行ごとのトークン数と推定コストを表示する機能を追加する。

(nishio補足) 実行前に推定費用を表示する案は過去にあった、これは実行後に実際にかかった費用を表示するところが新しい
 - https://github.com/digitaldemocracy2030/kouchou-ai/issues/79

**コメント:** なし

---

### [[FEATURE]レポートの複製・再利用機能](https://github.com/digitaldemocracy2030/kouchou-ai/issues/19)

**作成者:** nasuka  
**作成日:** 2025-03-04T11:38:39Z  
**内容:**

# 背景
* 設定を少しだけ変えて実行したいケースがある
  * 例えばクラスタ数だけ変えるなど


# 提案内容
* レポートの設定複製機能を実装する


# 機能の提供価値
* LLM APIコストの削減
  * レポート出力までのステップを途中から実行できるようになるためAPIのコストを削減できる
* レポート出力の高速化

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (16件)

### [npm run format](https://github.com/digitaldemocracy2030/kouchou-ai/pull/554)

**作成者:** nishio  
**作成日:** 2025-05-21T02:21:51Z  
**変更:** +38 -24 (1ファイル)  
**マージ日:** 2025-05-21T02:25:38Z  
**内容:**

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

- **スタイル**
  - コードの可読性向上のため、フォーマットやインデントを整理しました。機能や画面表示に変更はありません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [デザイン変更: セグメントビューでの全体・濃い意見・階層の切り替え機能](https://github.com/digitaldemocracy2030/kouchou-ai/pull/550)

**作成者:** shgtkshruch  
**作成日:** 2025-05-20T12:13:32Z  
**変更:** +177 -71 (3ファイル)  
**マージ日:** 2025-05-21T01:47:15Z  
**内容:**

# 変更の概要
- https://github.com/digitaldemocracy2030/kouchou-ai/pull/487 を引き継いで、チャートの切り替え UI を Figma のデザインをもとに実装しました

# スクリーンショット

figma のデザインにある画面幅に設定して、スクリーンショット撮っています 📷 
https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=171-2&t=GXKzpACguMXTJ59Z-0

## 375px
![image](https://github.com/user-attachments/assets/83f31382-fca2-4693-873e-4a18f3ed031c)

## 768px
![image](https://github.com/user-attachments/assets/1bbfcc29-fec9-4082-8062-012fcf86a095)

## 1280px
![image](https://github.com/user-attachments/assets/956398a3-c245-4840-85d8-b7165b39c394)


# 変更の背景
- Chakra UI の Segment Control コンポーネントを使いつつ、Figma のデザインに合わせて実装しています
  - Figma: https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=171-2&t=GXKzpACguMXTJ59Z-0
- ブレイクポイントは Chakra UI のデフォルトのものを使用しています
  - https://www.chakra-ui.com/docs/theming/breakpoints
- Chakra UI の styel props に配列を渡すと上記ブレイクポイントごとに切り替わるので、この機能を使ってレスポンシブ対応をしています
  - https://v2.chakra-ui.com/docs/styled-system/responsive-styles

# 関連Issue
- fix: https://github.com/digitaldemocracy2030/kouchou-ai/issues/113

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

Google Chrome でレポート詳細画面開いて、ブラウザ幅を変更して Figma のデザインように UI が切り替わることを確認しました。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [ ] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - チャートの表示切替ボタンに新しいセグメントコントロールUIを導入し、選択肢ごとにアイコンを追加しました。
  - 新しいアイコン（全体表示、密集表示、階層表示）を追加しました。

- **改善**
  - チャート切替UIのレイアウトと操作性を向上し、選択肢の動的生成やツールチップ表示に対応しました。
  - レイアウト調整により、チャート概要部分の余白を縮小しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [DeepWikiのバッジを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/544)

**作成者:** mtane0412  
**作成日:** 2025-05-19T14:40:41Z  
**変更:** +2 -0 (1ファイル)  
**マージ日:** 2025-05-20T01:09:51Z  
**内容:**

# 変更の概要
- READMEにask deepwikiのbadgeを追加

# 変更の背景
DeepWikiのバッジをREADME.mdに追加すると毎週自動でDeepWikiが更新されるようになる。
> Add a badge to this wiki in the repo's README file to auto refresh the wiki weekly with the latest code.

https://deepwiki.com/badge-maker?url=https%3A%2F%2Fdeepwiki.com%2Fdigitaldemocracy2030%2Fkouchou-ai

# 関連Issue

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

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

- **ドキュメント**
  - READMEにDeepWikiへのバッジリンクを追加しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [dd2030に関する説明を修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/541)

**作成者:** nasuka  
**作成日:** 2025-05-19T06:28:54Z  
**変更:** +11 -3 (2ファイル)  
**マージ日:** 2025-05-19T07:45:07Z  
**内容:**

# 変更の概要
フッター中のdd2030の説明において以下の追記を実施

* 広聴AIに関する説明を追記
* このレポートが広聴AIによって出力されたものである旨を追記


# スクリーンショット
`広聴AIについて` を追記

![image](https://github.com/user-attachments/assets/9bdb2274-88ff-4d5a-8a07-0e2404ede495)


変更前の内容は以下

![image](https://github.com/user-attachments/assets/3c5955e2-e929-461c-802d-4e5ffd998e5d)


# 変更の背景
* 元々の記述だと、デジタル民主主義2030プロジェクトに関する説明はなされているが、それとこのレポートとの関係性がわからなかった
* また、レポート出力者とdd2030との関係性も読み取りにくい構造になっていた

-> 当該レポートが、dd2030の成果物によって出力されたものであることを明示するように修正


# 動作確認の結果
前述のスクショの通り

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

- **新機能**
  - フッタードロワーに「広聴AIについて」と「デジタル民主主義2030プロジェクトについて」の2つのセクションを追加し、説明文を拡充しました。

- **その他**
  - 利用規約リンクが一時的に非表示になりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [利用規約のリンクのデフォルト値をnullに変更](https://github.com/digitaldemocracy2030/kouchou-ai/pull/540)

**作成者:** nasuka  
**作成日:** 2025-05-19T05:54:48Z  
**変更:** +2 -2 (1ファイル)  
**マージ日:** 2025-05-19T07:45:08Z  
**内容:**

# 変更の概要
* 利用規約のリンクのデフォルト値をnullに変更

# 変更の背景
利用規約については（実装的にもサービスとしても）必須ではないが、現状のデフォルト値が `/` になっており、optionalでないことがユーザーにとってわかりにくいのでデフォルト値をnullに変更した

# 関連Issue
Close https://github.com/digitaldemocracy2030/kouchou-ai/issues/539

# 動作確認の結果
利用規約がnullの場合はフッターに利用規約が含まれないことを確認した
![image](https://github.com/user-attachments/assets/2db1651f-039f-4009-b932-61220b53103b)


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

- **バグ修正**
  - 利用規約リンクが正しく表示されない問題を修正しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [トークン使用量追跡と表示機能の実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/536)

**作成者:** 種延真之+Devin  
**作成日:** 2025-05-18T14:30:09Z  
**変更:** +598 -65 (20ファイル)  
**マージ日:** 2025-05-20T05:09:18Z  
**内容:**

# トークン使用量追跡と表示機能の実装

## 変更内容
- LLMサービス関数（OpenAI、Azure、ローカルLLM）でトークン使用量を追跡するよう修正
- レポートスキーマにトークン使用量フィールドを追加
- パイプラインステップでトークン使用量を累積する機能を追加
- レポート一覧ページで各レポートのトークン使用量を表示するよう修正
- トークン情報がない場合は「情報なし」と表示

## テスト方法
- 新しいレポートを生成し、トークン使用量が正しく追跡・表示されることを確認
- 古いレポート（トークン情報なし）でも表示が問題ないことを確認

Link to Devin run: https://app.devin.ai/sessions/1b1d0ae947d94daa9303d0e0b980de15
Requested by: 種延真之 (mtane0412@gmail.com)


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - レポート進捗画面およびレポートカードに、トークン使用量（合計・入力・出力）の表示を追加しました。
  - トークン使用量の詳細がAPIレスポンスやレポート情報に含まれるようになりました。

- **バグ修正**
  - 進捗取得APIが常にトークン使用量情報を返すよう改善しました。

- **テスト**
  - トークン使用量の追跡・更新・表示に関する単体テストとエンドポイントテストを追加しました。

- **ドキュメント**
  - pytestのasyncioマーカー定義を追加しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [プルリクエストのテンプレートの項目の順番を修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/535)

**作成者:** shingo-ohki  
**作成日:** 2025-05-18T12:19:55Z  
**変更:** +7 -7 (1ファイル)  
**マージ日:** 2025-05-18T13:05:41Z  
**内容:**

# 変更の概要
- プルリクエスト時のテンプレートの項目が、コントリビュータに対するものとレビュアーに対するものが混在していたので、一部の項目の順番を入れ替え、以下の形で整理しました  
  - 前半の大部分がコントリビュータに対するもの
  - 後半をレビュアーに対するもの
  
具体的には、
- `CLAへの同意` を `マージ前のチェックリスト（レビュアーがマージ前に確認してください）` の前に移動しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **ドキュメント**
  - プルリクエストテンプレート内で、CLA同意セクションの位置を動作確認結果の直後に移動しました。内容自体の変更はありません。
  - レビュアーによる動作確認の表現を「歓迎します（必須ではありません）」に変更し、確認が推奨されることを明確化しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [LocalLLM の説明文を修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/534)

**作成者:** shingo-ohki  
**作成日:** 2025-05-18T12:05:37Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-05-18T13:03:24Z  
**内容:**

# 変更の概要
- #422 で LocalLLM 対応の実装が行われたが、client-admin のレポート作成ページの説明文にはまだ「将来実装予定」という文言が残っていたのでその文言を削除しました

# スクリーンショット
- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください
## 変更前
![Screenshot From 2025-05-18 10-19-55](https://github.com/user-attachments/assets/408b25e4-356f-49cf-838a-96d5ca1fee14)

## 変更後
![Screenshot From 2025-05-18 20-59-16](https://github.com/user-attachments/assets/a471cea5-3460-4d14-9db8-b699ad191966)

# 関連Issue
#532 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->
- スクリーンショットの通り、意図通り文言が修正できていることを確認しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **ドキュメント**
  - 「local」プロバイダー設定の説明文から「（将来対応予定）」の表記を削除しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Update CODE_REVIEW_GUIDELINES.md：デザインフェーズから開発フェーズへの移行プロセス](https://github.com/digitaldemocracy2030/kouchou-ai/pull/533)

**作成者:** masatosasano2  
**作成日:** 2025-05-18T01:57:12Z  
**変更:** +3 -1 (1ファイル)  
**マージ日:** 2025-05-18T05:43:34Z  
**内容:**

# 変更の概要
デザインフェーズから開発フェーズに移行するときのプロセスを追記しました。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **ドキュメント**
  - デザインに関するサブ課題の取り扱いについてガイドラインを明確化しました。レビュー担当者がサブ課題をクローズし、開発フェーズへ進めることが可能になりました。開発中に実現性の問題が発生した場合は、必要に応じてデザインフェーズへ戻ることができます。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [使われていないプロンプトファイルの削除](https://github.com/digitaldemocracy2030/kouchou-ai/pull/527)

**作成者:** tokoroten  
**作成日:** 2025-05-17T08:23:41Z  
**変更:** +0 -163 (8ファイル)  
**マージ日:** 2025-05-17T08:26:55Z  
**内容:**

# 変更の概要
- server/broadlistening/pipeline/prompts/ の下にある、プロンプトのdefault.txt を削除した
 
おそらくpipelineを単体で動かしていた時代の残骸？

# 変更の背景

- server/broadlistening/pipeline/prompts/ の下にある、プロンプトのdefault.txtは、現状ではどこからも参照されてない
  - https://github.com/search?q=repo%3Adigitaldemocracy2030%2Fkouchou-ai%20default.txt&type=code
- そのため、開発時の混乱を抑制するために、これらのプロンプトを削除したい

# 動作確認の結果
削除して正常動作

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [ ] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **削除**
  - 複数の日本語プロンプトテンプレートファイルを削除しました。これにより、AIによる要約、ラベリング、クラスタ統合、翻訳などの機能が利用できなくなります。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[FEATURE] OpenRouterを使えるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/526)

**作成者:** takumi19910112  
**作成日:** 2025-05-16T15:28:41Z  
**変更:** +225 -38 (12ファイル)  
**マージ日:** 2025-05-18T14:40:37Z  
**内容:**

# 変更の概要
- [こちらでPR](https://github.com/digitaldemocracy2030/kouchou-ai/pull/482)を作成していましたが、冗長な表現や余計な表現などが多かったので、刷新して実装しました。
- 変更内容としては、OpenRouterを経由してOpenAIとgeminiを使えるようにする実装です。

# スクリーンショット
OpenRouterが選択肢に表示されているところの画像
<img width="545" alt="スクリーンショット 2025-05-17 1 16 21" src="https://github.com/user-attachments/assets/1afcbef0-4736-464f-be56-369543855d9e" />

レポート分析（こちらは既存の機能である、OpenAIAPIを使っている様子の画像で、既存の実装に問題がないことのスクショです）
<img width="1506" alt="スクリーンショット 2025-05-17 1 16 56" src="https://github.com/user-attachments/assets/96806e5e-92c9-43c4-9215-2b4609058300" />

レポート分析
OpenRouter経由だと、画像のようになります。
<img width="1739" alt="スクリーンショット 2025-05-17 1 18 16" src="https://github.com/user-attachments/assets/93d91b50-ee1f-4185-b1f3-ce8737df2639" />




# 変更の背景
- OpenAIAPIだけでなく、OpenRouterAPIを使う実装でした。
- 従って既存のプロバイダに加えて、OpenRouterでの分析をするバックエンドの実装と、UIの調整が必要でした。

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/402

# 動作確認の結果
- 既存のプロバイダを使って今まで通り分析とレポートの作成ができること
- OpenRouter経由でOpenAIを呼び出して分析とレポート作成ができること
- OpenRouter経由でgeminiを呼び出して分析とレポート分析ができること

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
    - OpenRouterプロバイダーのAIモデルが選択可能になりました。
    - OpenRouter経由でのAIリクエストに対応しました。

- **改善**
    - OpenRouterのモデルリストが静的に設定され、即時選択が可能になりました。
    - AIリクエスト関数の名称を`request_to_chat_openai`から`request_to_chat_ai`に変更し統一しました。
    - READMEや環境変数例にOpenRouterのAPIキー設定方法を追加しました。

- **バグ修正**
    - OpenRouterの選択肢が無効化されていた問題を修正しました。

- **テスト**
    - OpenRouter対応に合わせてテストを追加・更新しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [biome fix](https://github.com/digitaldemocracy2030/kouchou-ai/pull/525)

**作成者:** masatosasano2  
**作成日:** 2025-05-16T06:32:49Z  
**変更:** +7 -28 (7ファイル)  
**マージ日:** 2025-05-16T06:35:38Z  
**内容:**

npm run format の実行結果です。
先日の一斉formatの後、行あたりの文字数が80から120に変わったことに伴う変化と思われます。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **Style**
  - コードや設定ファイルの複数行表記を単一行に統一し、可読性を向上しました。動作や機能に変更はありません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [windows直環境対応#](https://github.com/digitaldemocracy2030/kouchou-ai/pull/524)

**作成者:** take365  
**作成日:** 2025-05-15T16:39:27Z  
**変更:** +208 -0 (2ファイル)  
**マージ日:** 2025-05-20T22:29:35Z  
**内容:**

# 変更の概要
Windows 環境で Docker を使用せずに開発環境を構築・起動する手順をまとめた Markdown ファイルを新たに追加しました。
起動用のdirect_start_win.batを追加しました
検証・開発用途を想定しており、非推奨構成として experimental 配下に配置しています。
pdm を利用しつつ pyproject.toml に準拠したセットアップ手順を記載しています。
.env の分割処理や各サービスの依存ライブラリインストール方法を明記しました。


当初はご提案いただいたとおり、rye + make を使った構成に合わせようと検討しましたが、以下の理由から今回は断念し、代替手段として pdm ベースでの手順を採用しました。

rye の実行ファイルは、インストール時にセキュリティ警告を無視する必要があり、加えて Windows 環境での実行にはセキュリティ設定の調整が必要となる場面がありました。
make も別途 exe をダウンロードし、Path に追加する必要がありますが、最終的には rye に依存するため、初心者や非エンジニアにとっては敷居が高い構成になってしまうと判断しました。
.env の分割処理などもバッチスクリプトで補完する必要があり、結果的に純粋な make ベースの恩恵が限定的である点も考慮しました。
そのため、server 側では pyproject.toml を活かしつつも、pdm を使ったセットアップに調整しています。
また、report_launcher.pyの変更は起動時の仮想環境を引き継げていたため取り下げました。
なお、この手順は「非推奨手順」として kouchou-ai/experimental/direct_win に配置し、軽量な検証や個人開発向けの補助的な位置づけとして取り扱っています。


# スクリーンショット
- UIなし

# 変更の背景
- issu対応

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/509
https://github.com/digitaldemocracy2030/kouchou-ai/pull/499

# 動作確認の結果
pdm で作った仮想環境を使いつつ起動、レポート作成の完了。

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [x ] 単体テストが実装されているか
- [x ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。




- [x ] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **ドキュメント**
  - Windows環境でDockerを使わずに開発環境を構築するためのユーザーガイドを追加しました。

- **新機能**
  - Windows向けの環境構築・起動用バッチスクリプトを追加しました。複数サービスの起動や環境変数の自動設定が可能です。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [embeddingを使う際にproviderを適用する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/521)

**作成者:** nasuka  
**作成日:** 2025-05-15T14:53:23Z  
**変更:** +8 -7 (5ファイル)  
**マージ日:** 2025-05-15T15:51:28Z  
**内容:**

# 変更の概要
* embeddingを作成する際に、providerを考慮するように修正

# 変更の背景
* embedding作成時に、providerが考慮されておらず、デフォルトのOpenAIで作成されるようになっていた


# 動作確認の結果
![image](https://github.com/user-attachments/assets/aba89f39-ca1f-407e-8f26-055da6b019a5)

Azure OpenAIのembeddingが呼び出されていることを確認した

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。


# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **バグ修正**
  - 埋め込みリクエスト時にプロバイダー情報の指定が正しく反映されるようになりました。
  - プロバイダー設定が必須となり、未設定時にエラーが表示されるようになりました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[GITHUB_ACTIONS] アサイン状況に合わせてステータスを更新する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/512)

**作成者:** masatosasano2  
**作成日:** 2025-05-13T16:10:53Z  
**変更:** +381 -2 (7ファイル)  
**マージ日:** 2025-05-16T07:08:51Z  
**内容:**

# 変更の概要
GitHub IssuesとGitHub Projectsのステータスフィールドを以下の条件とイベントに基づいて自動的に更新します。
| **条件**  | **トリガー** | **変更後のstatus** |
| ------------- | ------------- | ------------- |
| Status in [`No Status`, `Cold List`, `Need Refinement`, `Ready`]  | Assign | `In Progress` |
| Status = `In Progress` | Unassign | `Ready` |

# 変更の背景
kouchou-ai のIssue数が多く、statusの管理コストが高いため、一部の変更を自動化したい。

# 関連Issue
#425
(後続Issue: #454 , #459 )

# 実装詳細
- 既存の処理への追加
    - `.github/workflows/assign_bot.yml`：スラッシュコマンドでassign/unassignされたときに`status_update.yml`を呼び出す設定
- GitHub Actionsワークフローを作成：
    - `.github/workflows/assign_manually.yml`：GitHubのUI上でassign/unassignされたときに`status_update.yml`を呼び出す設定
    - `.github/workflows/status_update.yml`：ステータス更新処理を蹴る設定。他のymlから呼び出される（Issues 454, 459で再利用予定）
    - `.github/scripts/status_update.py` : 冒頭の条件通りにステータスを更新する処理（Issues 454, 459で再利用予定）
    - `.github/scripts/status_update_common.py` : ステータス更新の共通処理（Issues 454, 459で再利用予定）
- GraphQL API でProjectsやIssueの情報を取得　※ REST API はProjectV2に未対応のため
- Tokenは手動発行ではなく GitHub Apps 経由で発行　※ ProjectV2 x GitHub Actions では手動設定で権限付与できないため

# 必要な設定

### OrganizationのGitHub Apps を作成する
- 手順：https://docs.github.com/ja/apps/creating-github-apps/registering-a-github-app/registering-a-github-app
- WebhookはOFF
- Permissions > Organization permissions > Projects > Read and write を指定
- Permissions > Repository permissions > Metadata > Read only を指定
- Permissions > Repository permissions > Actions > Read only を指定
    - 確認メールが届いたら、リンク先でリポジトリを指定して許可
- Install only on this account

### Private Key の発行
- 作成完了画面の指示に従い、続けてGitHub Apps のインストール準備としてprivate keyを発行する
- 手順：https://docs.github.com/ja/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps
- 発行すると、ローカルに秘密鍵（pemファイル）がダウンロードされる

### OrganizationのGitHub Apps をインストールする
- 手順：https://docs.github.com/ja/apps/using-github-apps/installing-your-own-github-app
- General > Generate a new client secret
- Install App > Install (to organization)

### Organization secrets の設定
- Organization の設定ページを開く
- Repository > Settings > General > Security > Secrets and variables > Actions > Organization secrets
- PJ_APP_ID : AppのGeneralタブのApp ID
- PJ_APP_PEM : private key を発行した際にローカルにダウンロードされたpemファイルの内容（テキスト全体）
    - Repository を指定する

# 補足：

- `.github/scripts/repo_config.py` について
    - `digitaldemocracy2030/kouchou-ai` に特化したID等になっている
    - 機密情報ではない
    - 本来は環境設定に持たせる方が綺麗だが、どうせ後続処理もこのリポジトリ独自のルールに則った処理なので、このままにしている
        - もし将来的に他のリポジトリで使い回すようであれば環境変数へ移植するのが望ましい
- **PROJECT_ID** (PVT_xxxx) と **STATUS_FIELD** (PVTSSF_xxxx) の取得方法：
    - https://docs.github.com/ja/graphql/overview/explorer にアクセス
    - Githubアカウントでログイン ※ `digitaldemocracy2030` のメンバである必要がある
    - 以下のクエリを実行:
```
{
  organization(login: "digitaldemocracy2030") {
    projectV2(number: 3) {
      id
      fields(first: 20) {
        nodes {
          ... on ProjectV2SingleSelectField {
            id
            name
          }
        }
      }
    }
  }
}
```

# スクリーンショット

No Status + assigned -> In Progress
<img width="579" alt="image" src="https://github.com/user-attachments/assets/276cb071-900b-4a42-89c8-b514b2c944ae" />

Cold List + assigned -> In Progress
<img width="598" alt="image" src="https://github.com/user-attachments/assets/3fc89e15-5ff1-425c-be73-13ed789ed318" />

In Progress + unassigned -> Ready
<img width="533" alt="image" src="https://github.com/user-attachments/assets/b294c6c9-6a78-4a0b-90f6-4cb096343f82" />

Done + unassigned -> Done
<img width="452" alt="image" src="https://github.com/user-attachments/assets/122d4150-a3f7-4195-9981-c66fbeceb2eb" />

In Progress + assigned -> In Progress
<img width="402" alt="image" src="https://github.com/user-attachments/assets/14bccb34-361e-4046-81e9-5909fea18732" />

assign-bot > assign-status-sync
![image](https://github.com/user-attachments/assets/c5a64086-241c-40b9-b13f-9650630e8cb0)

# 動作確認の結果

- Organization(sasa-test-org)とAppsを作成
- kouchou-aiと同じ名称のステータスをもつプロジェクト（kouchou-ai-copy）を用意
- Assign/unassign に対するステータス変更結果は上記のとおり
    - ログにある通りにステータス値が変わり、カンバンも移動することを確認
    - assign / unassign は手動設定もスラッシュコマンドも両方通ることを確認

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [ ] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - イシューのアサイン・アンサインに応じてプロジェクトのステータスを自動更新する機能を追加しました。
  - イシューのステータスが「進行中」や「準備完了」などに連動して自動変更されます。
  - アサイン操作に連動してステータス更新を行う新しいGitHub Actionsワークフローを複数導入しました。
- **その他**
  - ステータス更新処理に必要な依存パッケージを追加しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [デザイン変更: セグメントビューでの全体・濃い意見・階層の切り替え機能](https://github.com/digitaldemocracy2030/kouchou-ai/pull/487)

**作成者:** nsk.smn+Devin  
**作成日:** 2025-05-12T06:27:57Z  
**変更:** +178 -71 (5ファイル)  
**マージ日:** 2025-05-21T01:47:17Z  
**内容:**

# デザイン変更: セグメントビューでの全体・濃い意見・階層の切り替え機能

## 変更内容
- セグメントビューを使用して全体・濃い意見・階層のビュー切り替え機能を実装
- 新しいカスタムアイコンを作成（全体、濃い意見、階層）
- Chakra UIのカラーパレット（gray.100, gray.200, gray.500）を使用
- モバイル表示では縦積みレイアウトに対応
- デスクトップ表示では横並びレイアウトに対応

## デザイン意図
- 「ビューの切り替え機能」だと伝えるためにセグメントビューに変更
- 「当たり前に押す機能」としてアピールするため中央配置 & やや大きめサイズ
- 本プロダクトのキモとなる機能のため1つ1つを主張させるためアイコンで表現

## 実装詳細
- Chakra UIのsegmented-controlコンポーネントを使用
- カスタムアイコンを新規作成
- レスポンシブデザインに対応（モバイルでは縦積み、デスクトップでは横並び）

Link to Devin run: https://app.devin.ai/sessions/8b3acd70772247219783e236a211bc16
Requested by: nsk.smn@gmail.com


**コメント:** なし

---

### 過去7日間に作成されたPR (8件)

### [fix: report_status.jsonを上書きするテストを削除](https://github.com/digitaldemocracy2030/kouchou-ai/pull/555)

**作成者:** mtane0412  
**作成日:** 2025-05-21T02:51:59Z  
**変更:** +0 -64 (1ファイル)  
**内容:**

test-slug データが report_status.json に書き込まれる問題を修正しました。
実装内容
最新のmainブランチから新しいブランチ devin/fix-test-slug-leak-latest を作成し、`test_update_token_usage.py` に teardown_method を追加しました：
def teardown_method(self):
    """各テスト後に_report_statusをクリア"""
    _report_status.clear()
この修正により、テスト実行後に _report_status グローバル変数がクリアされ、テストデータが本番環境に漏れることを防ぎます。
実装状況
- 最新のmainブランチから新しいブランチを作成
- test_update_token_usage.py に teardown_method を追加
- 変更を devin/fix-test-slug-leak-latest ブランチにコミットしてプッシュ
- :x: PRの作成（コマンドが失敗）

次のステップ
GitHub上で手動でPRを作成していただくか、以下のURLから直接ブランチを確認できます：
https://github.com/digitaldemocracy2030/kouchou-ai/tree/devin/fix-test-slug-leak-latest
修正内容は test_update_token_usage.py に実装されています。
Devinセッション
この作業は https://app.devin.ai/sessions/7408ab9acf194f3eb709d0c7c5f844a0 で行われました。
[11:49](https://dd2030.slack.com/archives/C08PRQVQWSE/p1747795779395259?thread_ts=1747792798.579469&cid=C08PRQVQWSE)
追加の検証結果
コードベース全体を検索した結果、`_report_status` グローバル変数を操作しているのは test_update_token_usage.py のみであることを確認しました。また、`update_token_usage` 関数を呼び出しているのも同じファイルのみです。
これにより、今回実装した修正（`teardown_method` の追加）が問題を完全に解決することが確認できました。テスト実行後に _report_status がクリアされるため、test-slug データが本番環境に漏れることはなくなります。
修正内容は既に devin/fix-test-slug-leak-latest ブランチにプッシュされています。GitHub上でPRを作成していただければ、この修正をmainブランチにマージできます。

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

- **テスト**
  - `update_token_usage` 関連のテストスイートを削除しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [レポートページに推定コスト表示機能を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/549)

**作成者:** 種延真之+Devin  
**作成日:** 2025-05-20T11:32:07Z  
**変更:** +472 -15 (10ファイル)  
**内容:**

# レポートページに推定コスト表示機能を追加

## 概要
Issue #284 の実装として、レポートページにLLMの使用コスト（推定）を表示する機能を追加しました。トークン使用量と同様に、レポート作成中にリアルタイムで更新され、プロバイダーとモデル情報も合わせて表示されます。

## 変更内容

### バックエンド
- `LLMPricing`サービスを新規作成し、各プロバイダー・モデルの最新料金情報を定義
  - OpenAI (gpt-4o-mini, gpt-4o, o3-mini)
  - Azure OpenAI
  - OpenRouter
- レポートスキーマに推定コスト、プロバイダー、モデル情報のフィールドを追加
- レポート作成中にリアルタイムで推定コストを計算する機能を実装
- レポート作成過程でプロバイダーとモデル情報を保持する仕組みを追加
- `LLMPricing`サービスのユニットテストを実装

### フロントエンド
- レポートカードに推定コスト表示を追加（`$1.2345 (OpenAI GPT-4o-mini)`形式）
- レポート作成中のポーリングで推定コスト、プロバイダー、モデル情報を取得・表示
- レポート完了後も推定コストとプロバイダー・モデル情報を保持して表示

## 動作確認
- トークン使用量と同じくリアルタイムで更新されることを確認
- 推定コスト情報がないレポートは「情報なし」と表示
- OpenAI + GPT-4o-miniの組み合わせで正常に動作することを確認

## スクリーンショット
![推定コスト表示のスクリーンショット](https://github.com/user-attachments/assets/4d4fb551-d9f1-4af5-9143-8b682df5b0b4)

## 関連Issue
Closes #284

## Devinセッション
https://app.devin.ai/sessions/85a9f2748ead4343ba46d0795f960e3c


**コメント:** なし

---

### [意見グループのタイトル・説明を手動で編集できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/545)

**作成者:** nasuka  
**作成日:** 2025-05-20T04:31:31Z  
**変更:** +1468 -87 (16ファイル)  
**内容:**

# 変更の概要
* 出力済みのレポートに対して、意見グループのタイトル・説明を編集する機能を実装

# スクリーンショット
![60fead70df97d60ba2ff8cc81ecffbbd](https://github.com/user-attachments/assets/eedddfcb-bacc-4745-9727-6f2d4b82cf0c)


# 変更の背景
* LLMが出力したクラスタ名や説明、argumentが適切でない場合があるので、出力後に手動で修正したい
  * e.g.
    * 公開するのに不適切な単語や表現がクラスタ名に含まれているケース
    * 他のクラスタと同一の内容がクラスタ名に含まれているケース

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/310

# 動作確認の結果
* クラスタのタイトル・説明が編集できる
  * 第1階層・第2階層それぞれ確認
* レポート作成が実行できる
  * レポート作成に関連する関数も少し修正しているため確認

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。



# 実装方針に関する補足

実装方針および検討した内容の詳細は以下のコメントに記載。
最終的に、以下のような更新を実施するアプローチを採用している。

1. クラスタラベルの中間ファイル（hierarchical_merge_labelling.pyの成果物）を更新
2. そのうえで `hierarchical_result.json` （フロントで描画に使われるjsonファイル） を更新

ファイル更新なので、例えば複数のユーザーが同一のクラスタのタイトル・説明を同時に編集しているような場合は不整合が起きうる（後に更新した人の内容だけが反映される可能性がある）。
一方で、DB導入については上記のイシューにコメントしたようなハードルがあり、また上記のリスクがあるとしてもこの機能によって得られる便益が大きいので、今回はそのリスクを許容してでもこの機能をマージしたほうが良いと考えています。
https://github.com/digitaldemocracy2030/kouchou-ai/issues/310#issuecomment-2888243252

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
    - レポートカードのメニューに「意見グループを編集する」項目を追加し、クラスタのタイトル・説明を編集できるダイアログを実装しました。
    - 管理画面からクラスタ情報の取得・更新が可能となり、更新後は集計処理が自動で実行されます。

- **バグ修正**
    - ファイルパスの解決を絶対パスに統一し、ファイル操作の信頼性を向上しました。

- **ドキュメント**
    - クラスタ関連のAPI型定義とスキーマを新たに追加しました。

- **テスト**
    - クラスタ編集APIおよびリポジトリの包括的なユニットテストを新規追加しました。

- **リファクタ**
    - クラスタ処理に関する例外クラスを新設し、エラーハンドリングを強化しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [アドミン管理画面でリロードを抑制する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/543)

**作成者:** tokoroten  
**作成日:** 2025-05-19T14:34:06Z  
**変更:** +37 -22 (1ファイル)  
**内容:**

# 変更の概要
- 現在の管理画面では、完了やエラーになった項目も、何度もリロードしている
- フロントの判定を変えて、リロードを抑制する

# スクリーンショット

# 変更の背景
- 管理画面のリロードがひどくて、サーバのログが流れてしまって

# 関連Issue

# 動作確認の結果
処理中のレポートのみがリロードされていることを確認した。

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

- **バグ修正**
  - 完了またはエラー状態のレポートに対して不要なポーリングが行われないようになりました。
  - レポートの進捗が変化した際、ステータス更新が一度だけ行われるよう改善されました。
  - 完了やエラー時にページが自動リロードされなくなりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Refactor PR #531 attribute filtering feature](https://github.com/digitaldemocracy2030/kouchou-ai/pull/538)

**作成者:** shinta.nakayama+Devin  
**作成日:** 2025-05-19T03:24:34Z  
**変更:** +2158 -930 (23ファイル)  
**内容:**

# Refactor PR #531: Attribute Filtering Feature

## 変更の概要
PR #531 で実装された属性フィルタリング機能のリファクタリングを行いました。具体的には以下の改善を行っています：

1. TypeScript型の安全性向上
   - 暗黙的な `any` 型の排除
   - イベントハンドラーの型付け
   - コンポーネントプロップスの型定義の強化

2. コンポーネントの一貫性
   - `AttributeColumnsSelector` で生の HTML 要素の代わりに Chakra UI コンポーネントを使用
   - 一貫したコンポーネントパターンの適用

3. コード整理
   - 大きなコンポーネントを小さなサブコンポーネントに分割（`AttributeFilterDialog`）
   - ユーティリティ関数の最適化

4. Python 型の問題修正
   - `hierarchical_aggregation.py` の TypedDict 実装の修正
   - 型アノテーションの追加・修正

5. パフォーマンス最適化
   - React コンポーネントでの計算のメモ化
   - フィルタリング関数の最適化

## 関連 PR
#531

## 動作確認の結果
リファクタリング前後で機能が同じように動作することを確認しました。

## マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

## CLAへの同意
- [x] CLAの内容を読み、同意しました

Link to Devin run: https://app.devin.ai/sessions/93027cff3d3f48ffa8b62fcb1497a49b
Requested by: shinta.nakayama@gmail.com


**コメント:** なし

---

### [属性フィルタ機能の実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/531)

**作成者:** tokoroten  
**作成日:** 2025-05-17T22:10:05Z  
**変更:** +2158 -925 (23ファイル)  
**内容:**

# 変更の概要
- アップロード時に後でスライスするための属性カラムを指定できる
- サーバでの処理の最後に、もともとの属性カラムを結合する
- クライアントで属性カラムをフィルターをかけることを可能にする

## 属性フィルタ付きのサンプルデータ
https://gist.github.com/tokoroten/0115947bc25a53caa53d2f1e55a0b1df

# スクリーンショット
## アップロード時の分析用カラム
![image](https://github.com/user-attachments/assets/317badba-80a4-4eca-87e0-8110f7b477b2)


## クライアントでの属性スライサー
![image](https://github.com/user-attachments/assets/d488ff3f-c276-44f1-8493-07c24aeadbd0)

![image](https://github.com/user-attachments/assets/70d70bd7-ac4a-47cc-9fad-082188d9eee1)

## 属性スライス結果

![image](https://github.com/user-attachments/assets/702d26b0-337b-48bc-b1d0-e861e470f5bb)


# 変更の背景
- どのような属性の人がどこの意見にいるのかの分布を見たい
- 年齢・性別・職業・支持政党などでフィルターが行えると、政党は選挙キャンペーンの意思決定が行いやすくなる

# 関連Issue
#281

# 動作確認の結果
とりあえず動いている

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - CSVやスプレッドシートから複数の属性カラムを選択できる機能を追加しました。
  - 属性カラムでデータをフィルタリングできるダイアログとUIをレポート画面に追加しました。
  - 属性フィルターの適用により、散布図やツリーマップで対象外のデータがグレーアウト・非表示化されるようになりました。

- **改善**
  - 属性情報がコメントや引数データに付与され、レポートや可視化で利用可能になりました。
  - 属性フィルターと密度フィルターの組み合わせによる複合的なフィルタリングが可能になりました。

- **バグ修正**
  - NumPy型データのJSONシリアライズ互換性を強化しました。

- **その他**
  - ログ出力や関数定義のフォーマットを整理しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [windows直環境対応](https://github.com/digitaldemocracy2030/kouchou-ai/pull/523)

**作成者:** take365  
**作成日:** 2025-05-15T16:33:03Z  
**変更:** +195 -0 (2ファイル)  
**内容:**

ドラフト
# 変更の概要
Windows 環境で Docker を使用せずに開発環境を構築・起動する手順をまとめた Markdown ファイルを新たに追加しました。
起動用のdirect_start_win.batを追加しました
検証・開発用途を想定しており、非推奨構成として experimental 配下に配置しています。
pdm を利用しつつ pyproject.toml に準拠したセットアップ手順を記載しています。
.env の分割処理や各サービスの依存ライブラリインストール方法を明記しました。


当初はご提案いただいたとおり、rye + make を使った構成に合わせようと検討しましたが、以下の理由から今回は断念し、代替手段として pdm ベースでの手順を採用しました。

rye の実行ファイルは、インストール時にセキュリティ警告を無視する必要があり、加えて Windows 環境での実行にはセキュリティ設定の調整が必要となる場面がありました。
make も別途 exe をダウンロードし、Path に追加する必要がありますが、最終的には rye に依存するため、初心者や非エンジニアにとっては敷居が高い構成になってしまうと判断しました。
.env の分割処理などもバッチスクリプトで補完する必要があり、結果的に純粋な make ベースの恩恵が限定的である点も考慮しました。
そのため、server 側では pyproject.toml を活かしつつも、pdm を使ったセットアップに調整しています。
また、report_launcher.pyの変更は起動時の仮想環境を引き継げていたため取り下げました。
なお、この手順は「非推奨手順」として kouchou-ai/experimental/direct_win に配置し、軽量な検証や個人開発向けの補助的な位置づけとして取り扱っています。


# スクリーンショット
- UIなし

# 変更の背景
- issu対応

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/509
https://github.com/digitaldemocracy2030/kouchou-ai/pull/499

# 動作確認の結果
pdm で作った仮想環境を使いつつ起動、レポート作成の完了。

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [x ] 単体テストが実装されているか
- [x ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。




- [x ] CLAの内容を読み、同意しました

**コメント:** なし

---

### [windows直環境対応](https://github.com/digitaldemocracy2030/kouchou-ai/pull/522)

**作成者:** take365  
**作成日:** 2025-05-15T16:26:10Z  
**変更:** +195 -0 (2ファイル)  
**内容:**

ドラフト
# 変更の概要
- ここに変更の概要を記載してください

# スクリーンショット
- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください

# 変更の背景
- ここに変更が必要となった背景を記載してください

# 関連Issue
関連するIssueのリンクをこちらに記載してください

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [x ] 単体テストが実装されているか
- [x ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。




- [x ] CLAの内容を読み、同意しました

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [Add Windows manual startup support (venv/npm) - resolves #999](https://github.com/digitaldemocracy2030/kouchou-ai/pull/499)

**作成者:** take365  
**作成日:** 2025-05-13T05:38:24Z  
**変更:** +127 -2 (3ファイル)  
**内容:**

# 変更の概要
- Windows 環境で Docker を使わずに手動でセットアップできるようにするためのスクリプトおよび手順を追加しました。
- `.env` 設定、仮想環境の準備、依存ライブラリのインストール、実行用の補助スクリプトなどを含みます。

# スクリーンショット
- UIの変更はありません。

# 変更の背景
- Issue #254 の調査を進める中で、Windows 環境での実行手段として「生環境構築」も検証しました。
- 開発時には WSL2 や Docker を立ち上げることが比較的重いため、軽量な起動ができる選択肢として「生環境での実行」も許容していただければと思います（どちらかというと私自身の開発効率向上の観点からの提案です、他に使う人もいなそうなら私だけマージして使ってますので、却下でも大丈夫です）。
- 今後も Docker や WSL2 による環境構築の整備は継続される見込みのため、これは補助的な手段として捉えています。

# 関連Issue
- https://github.com/digitaldemocracy2030/kouchou-ai/issues/254
-https://github.com/digitaldemocracy2030/kouchou-ai/issues/496
# CLAへの同意
- [x] コントリビューターライセンス契約（CLA）に同意します。

**コメント:** なし

---

