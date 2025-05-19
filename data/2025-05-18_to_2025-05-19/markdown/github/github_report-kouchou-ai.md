# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-05-18T16:13:25.293468+09:00 から 2025-05-19T16:13:25.293468+09:00 まで

## Issues

### 過去1日間に完了されたissue (4件)

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

### 過去1日間に作成されたissue (2件)

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

### 過去1日間に更新されたissue（作成・クローズを除く）(4件)

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

## Pull Requests

### 過去1日間にマージされたPR (4件)

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

### 過去1日間に作成されたPR (4件)

### [dd2030に関する説明を修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/541)

**作成者:** nasuka  
**作成日:** 2025-05-19T06:28:54Z  
**変更:** +11 -3 (2ファイル)  
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

### [Refactor PR #531 attribute filtering feature](https://github.com/digitaldemocracy2030/kouchou-ai/pull/538)

**作成者:** shinta.nakayama+Devin  
**作成日:** 2025-05-19T03:24:34Z  
**変更:** +2092 -915 (23ファイル)  
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

### [トークン使用量追跡と表示機能の実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/536)

**作成者:** 種延真之+Devin  
**作成日:** 2025-05-18T14:30:09Z  
**変更:** +189 -36 (12ファイル)  
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


**コメント:** なし

---

### 過去1日間に更新されたPR（作成・マージを除く）(1件)

### [[WIP]属性フィルタ機能の実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/531)

**作成者:** tokoroten  
**作成日:** 2025-05-17T22:10:05Z  
**変更:** +1998 -877 (22ファイル)  
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
  - 属性によるフィルタリング結果が散布図やツリーマップ上で強調表示・グレーアウトされるようになりました。

- **改善**
  - 属性情報がコメントや引数データに付与され、レポートや可視化で利用可能になりました。

- **バグ修正**
  - NumPy型データのJSONシリアライズ互換性を強化しました。

- **その他**
  - ログ出力や関数定義のフォーマットを整理しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

