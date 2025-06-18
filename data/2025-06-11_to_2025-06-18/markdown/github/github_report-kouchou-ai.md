# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-06-11T12:28:53.668659+09:00 から 2025-06-18T12:28:53.668659+09:00 まで

## Issues

### 過去7日間に完了されたissue (4件)

### [[FEATURE] デザインシステムの実装反映 / Button](https://github.com/digitaldemocracy2030/kouchou-ai/issues/599)

**作成者:** shgtkshruch  
**作成日:** 2025-06-10T09:09:51Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

- デザインシステムで Button が追加されたので、フロントエンドの実装にも取り込みたい
  - Figma: https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=931-3156&t=xo3pcMDDvEqaiV2b-4
- デザインシステムの置き場所が決まっていないので、この issue ではデザインシステムが反映されている client 内の共通コンポーネントとして実装します


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

- client に Button コンポーネントを実装すること
- client の以下の箇所のボタンが上記コンポーネントに置き換わること
  - レポーター情報
  - Footer 

**コメント:** なし

---

### [[FEATURE] デザインシステムの実装反映 / Typography](https://github.com/digitaldemocracy2030/kouchou-ai/issues/598)

**作成者:** shgtkshruch  
**作成日:** 2025-06-10T08:54:25Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

- https://github.com/digitaldemocracy2030/kouchou-ai/issues/505 で Typography が定義されたので、フロントエンドの実装として取り込みたい
  - Figma: https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=893-2217&t=xo3pcMDDvEqaiV2b-4
- 現状ではデザインシステムの実装を配置する場所が決まっていないのと、 デザインシステムが反映された実装が client のみのため、この issue では client の中に実装する
  - デザインシステムを配置する場所が決まったら、必要な定義を移動すれば良いので移行コストはそこまで高くない認識です

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

- client の中に Typography のパターンを定義する
- client に上記 Typography を適用する
  - 2025/06/10 時点で Typography が Figma 上反映されているのは、レポーターの表示と Footer の箇所なので、こちらが対象

**コメント:** なし

---

### [[FEATURE] admin のレポートについて、CSV ダウンロードを一律で可能にする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/596)

**作成者:** shgtkshruch  
**作成日:** 2025-06-09T09:51:37Z  
**内容:**

# 背景
- 現在は選択式の「CSV出力モード」について、一律で出力（ダウンロード）できる方が自然という議論があった
 ![Image](https://github.com/user-attachments/assets/99904665-62df-4e81-99f5-60461a0390bf)

## Slack

> ウタコ ノギグチ  19:48
【おしえてくださいー！】CSVダウンロード機能について。レポート作成時に「CSV出力モード」にチェックマークを入れてないとダウンロードできないっぽいと気づいたのですが、CSVダウンロードの可/不可を任意にした背景ありましたら教えてほしいですー！任意にせず一律で出力できるのが自然かなと思ったのですが、もしかしてCSVダウンロード可能にするにはコストがかかる感じでしょうか？？

> Nasuka Sumino 23:18
>> 任意にせず一律で出力できるのが自然かなと思ったのですが、もしかしてCSVダウンロード可能にするにはコストがかかる感じでしょうか？？
>
> こちらですが、当初はパブコメ用途を想定した機能だったので任意選択にしてましたが、ウタコさんが仰るとおり一律で出力できる方が自然だと思うのでその形にするでよいかと思います！

ref: https://dd2030.slack.com/archives/C08F7JZPD63/p1749293334276609

# 提案内容
- admin で作成するレポートについて、一律で CSV ダウンロードをできるようにする

**コメント:** なし

---

### [[BUG] OpenAI API以外のLLMを使っても、OpenAI APIを利用したと表示される](https://github.com/digitaldemocracy2030/kouchou-ai/issues/494)

**作成者:** tokoroten  
**作成日:** 2025-05-12T18:44:13Z  
**内容:**

### 概要

![Image](https://github.com/user-attachments/assets/02429b8b-1552-4189-94e2-a37d25a61195)

### 修正が必要な個所

> 分析対象となったデータの件数は{processed_num}件で、これらのデータに対してOpenAI APIを用いて{args_count}件の意見（議論）を抽出し、クラスタリングを行った。

https://github.com/digitaldemocracy2030/kouchou-ai/blob/ea4f8c02fe0741a1305deccc44e5eabe087841fd/server/broadlistening/pipeline/steps/hierarchical_aggregation.py#L94-L96

LLMのプロバイダー情報をconfigから取得して、表示をディスパッチする必要がある。場合によってはmodelも公開する必要があると思う。


**コメント:** なし

---

### 過去7日間に作成されたissue (1件)

### [[REFACTOR] 管理画面のレポート一覧画面をコンポーネント分割する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/604)

**作成者:** shgtkshruch  
**作成日:** 2025-06-16T10:58:09Z  
**内容:**

# 現在の問題点
<!-- 現在のコードの何が問題なのか、どのような技術的負債があるかを説明してください -->

- https://github.com/digitaldemocracy2030/kouchou-ai/issues/460 で管理画面のレポート一覧画面のリデザインが進んでいます
  - 今の所、既存の機能に変更はありませんが、一括編集のような機能が追加されたり、機能への動線が変わりそうです
- [今の管理画面のレポート一覧の実装](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/client-admin/app/page.tsx)は、コンポーネント分割がされていないので、このままデザインの変更を適用すると diff が大きくなる可能性が高い
  - デザインのみを変更したい場合でも、見た目とロジックが密結合しているので、ロジックのコードも移動する diff が発生しそう

# 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->

- 管理画面の一覧画面を機能単位でコンポーネント分割する
- ロジック部分はカスタムフックなどに切り出す
  - 新しい UI からも呼び出せるので実装がしやすくなりそう


**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(4件)

### [[REFACTOR] レポーター情報のデフォルト値を空にしたい（なってる?）](https://github.com/digitaldemocracy2030/kouchou-ai/issues/590)

**作成者:** UtkNggc  
**作成日:** 2025-06-05T16:09:40Z  
**内容:**

## 背景
https://github.com/digitaldemocracy2030/kouchou-ai/issues/438 にて、今までAbout情報だったものをレポーター情報としてまとめた。

## 問題点
metadata.jsonを見たところ、現在はデフォルトのレポーター情報にdd2030の情報が入ってるみたいで、初期値は何もない方が自然なので空にしたい。

<img width="1046" alt="Image" src="https://github.com/user-attachments/assets/7b8c31fe-8f71-4c0d-8614-43832f602e85" />


## 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->
初期値を空にする。
空にすると、「レポーター情報が未設定です。〜」という表示になるはず。
<img width="524" alt="Image" src="https://github.com/user-attachments/assets/93877486-6352-45ac-9879-9c22bc8832a1" />

※もしも私が見てるファイルがちがってて問題なかったら本Issueは閉じちゃってくださいー！！

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

### [[FEATURE]用語解説ページをつける](https://github.com/digitaldemocracy2030/kouchou-ai/issues/111)

**作成者:** nishio  
**作成日:** 2025-03-20T12:07:35Z  
**内容:**

# 背景
「プロンプト」「埋め込み」「濃い(クラスタ)」について、単語レベルで言い換えてもわかりやすくならない気がするので、やるとしたら用語解説ページをつけるとかかな

「縦軸・横軸はなんだろう」についても解説

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

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

### 過去7日間にマージされたPR (6件)

### [Revert "[FEATURE] admin のレポートについて、CSV ダウンロードを一律で可能にする"](https://github.com/digitaldemocracy2030/kouchou-ai/pull/606)

**作成者:** takumi19910112  
**作成日:** 2025-06-17T09:37:50Z  
**変更:** +37 -16 (7ファイル)  
**マージ日:** 2025-06-17T09:42:04Z  
**内容:**

Reverts digitaldemocracy2030/kouchou-ai#603

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - 「CSV出力モード」(csv出力モード)の設定がAI設定セクションに追加され、チェックボックスで切り替え可能になりました。これにより、レポート作成時にCSV出力の有無を選択できます。

- **改善**
  - レポートのCSVダウンロードボタンの表示条件がシンプルになりました。
  - レポートの「CSV出力モード」設定が動的に反映されるようになりました。

- **仕様変更**
  - レポートの「CSV出力モード」設定が必須項目となり、常に明示的に指定されるようになりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[FEATURE] admin のレポートについて、CSV ダウンロードを一律で可能にする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/603)

**作成者:** takumi19910112  
**作成日:** 2025-06-15T06:37:47Z  
**変更:** +16 -37 (7ファイル)  
**マージ日:** 2025-06-16T01:57:43Z  
**内容:**

# 変更の概要
- 関連ISSUEのディスカッションにあるように、CSV出力のチェックボックスにチェックがないとCSV出力されないという制御だったので、チェックボックスそのものをなくして一律で可能にしました。

# スクリーンショット
CSVダウンロードのチェックボックスがないこと
<img width="1329" alt="CSVダウンロードのチェックボックスがないこと" src="https://github.com/user-attachments/assets/a16685a2-bea4-41cc-b8db-9f2693a6e2de" />

チェックボックスはないが、CSVは既存機能を失っていないこと
<img width="1438" alt="チェックボックスはないが、CSVは既存機能を失っていないこと" src="https://github.com/user-attachments/assets/2758914f-a843-4242-b02a-9147dfc74861" />


CSVも閲覧できること
<img width="996" alt="CSVも閲覧できること" src="https://github.com/user-attachments/assets/e7f3c662-182d-40bd-8e97-a130ca5b992c" />

レポートも閲覧できること
<img width="1390" alt="レポートも閲覧できること" src="https://github.com/user-attachments/assets/139e7898-7976-4749-b33f-0106b77a5af9" />


# 変更の背景
- is_pubcomという、パブリックコメントかどうかという値があったのですが、それを削除してしまうと影響範囲も大きそうですし、いったんは常にTrueにするという方針で実装しました。もし、削除した方がよい場合はご指摘お願いします。

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/596

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->
上記のスクリーンショットに動作確認結果を載せております。


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

- **新機能の変更**
  - レポート作成時のCSV出力モードが常に有効となり、UI上での切り替え設定が削除されました。

- **UIの変更**
  - 「CSV出力モード」に関するチェックボックスや説明文が設定画面から削除されました。
  - レポートカードのポップオーバーが、レポートの状態が「ready」の場合に常に表示されるようになりました。

- **仕様変更**
  - レポートのCSV出力はデフォルトで有効となり、個別の切り替え操作が不要になりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client] デザインシステムの Button を適用する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/602)

**作成者:** shgtkshruch  
**作成日:** 2025-06-15T06:35:35Z  
**変更:** +188 -65 (5ファイル)  
**マージ日:** 2025-06-16T01:44:39Z  
**内容:**

# 変更の概要
- Figma で作成中のデザインシステムの Button コンポーネントを client に適用します
- Figma: https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=931-3156&t=dDDYeVZGk6s6vTGD-4
![image](https://github.com/user-attachments/assets/fce555ba-00af-4cf8-b34d-0c5a1902cb34)

# スクリーンショット
通常の表示はこれまでと同じです。

![localhost_3000_](https://github.com/user-attachments/assets/ca17074c-c5dc-4f6c-9fe2-47435ca21eb3)

hover 時に背景色が変わって box-shadow がつくようになりました。

![image](https://github.com/user-attachments/assets/64d1f5d5-db7a-4ac3-8e9d-e8e1b48baa06)

# 変更の背景
- Figma を参考に Button コンポーネントを追加しました
  - これまで独自にスタイリングしていたコードが共通コンポーネントになりました
- client の以下の要素に上記の Button コンポーネントを適用しました
  - レポーターの表示 UI
  - Footer

# 関連Issue
- fix: #599 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- client の画面で、レポーター UI と Footer にデザインシステムの Button コンポーネントが反映されていること

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
  - カスタムボタンコンポーネントを追加し、統一されたボタンスタイル（primary、secondary、tertiary、ghost）とサイズバリエーション（xs、md、xl）を導入しました。
  - ボタン用の新しいカラートークンを追加しました。

- **リファクタ**
  - 既存のボタンを新しいUIボタンコンポーネントに置き換え、スタイル指定を簡素化しました。
  - すべてのボタンのバリアント指定を標準化し、個別のカスタムスタイルを削除しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[BUG] OpenAI API以外のLLMを使っても、OpenAI APIを利用したと表示される](https://github.com/digitaldemocracy2030/kouchou-ai/pull/601)

**作成者:** takumi19910112  
**作成日:** 2025-06-14T23:26:50Z  
**変更:** +23 -2 (1ファイル)  
**マージ日:** 2025-06-15T07:03:06Z  
**内容:**

# 変更の概要
- `server/broadlistening/pipeline/steps/hierarchical_aggregation.py`にて、
`分析対象となったデータの件数は{processed_num}件で、これらのデータに対してOpenAI APIを用いて{args_count}件の意見（議論）を抽出し、クラスタリングを行った。`
このようにOpenAI APIが固定の文字列になっていたため、configのJSONに記載されているプロバイダ名およびモデル名を取得し、動的に表示するようにしました。

# スクリーンショット
OpenAIによる分析のときは、これまでの文言通りであること
<img width="1451" alt="OpenAI" src="https://github.com/user-attachments/assets/d99feb90-a216-41e5-a7d0-958ae17e0dbe" />


<img width="1010" alt="OpenAIテスト結果" src="https://github.com/user-attachments/assets/db2c8160-1090-4549-b663-33243578c9ab" />


プロバイダを動的に取得できていること

<img width="1160" alt="OpenRouter" src="https://github.com/user-attachments/assets/74e80fb1-7a89-48ef-b66d-20b26e08f13c" />

<img width="1088" alt="OpenRouterテスト結果" src="https://github.com/user-attachments/assets/b94115dd-c882-46b5-9936-d9a7e0f8727d" />



# 変更の背景
- 関連ISSUEにも記載の通りのバグ修正のためのPRになります

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/494

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
動作確認については、上にUIのスクリーンショットを添付していますので、そちらとさせてください


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - カスタム紹介文に実際に利用されているLLMプロバイダー名とモデル名が動的に表示されるようになりました。複数プロバイダーや環境変数による切り替えにも対応しています。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client] デザインシステムの Typography を適用する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/600)

**作成者:** shgtkshruch  
**作成日:** 2025-06-13T10:02:31Z  
**変更:** +1461 -135 (12ファイル)  
**マージ日:** 2025-06-13T14:28:13Z  
**内容:**

# 変更の概要
- デザインシステムで Typography の定義がされたので、client の画面に適用します
    - Figma: https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=893-2217&t=RD5Ds3wDIpwS4Hfo-4

![image](https://github.com/user-attachments/assets/ee8636ff-bb36-4470-a320-d71f4fa62386)


# スクリーンショット

## Before

![localhost_3000_](https://github.com/user-attachments/assets/a3ae3a07-84e7-4e75-93fb-edb7a3b17460)

## After

![localhost_3000_](https://github.com/user-attachments/assets/3cdfea78-801f-4b6b-955d-09f0623006fc)


# 変更の背景
- Typography は Figma で client の一部の要素にしか適用されていないため、以下の部分が適用対象です
  - レポーターの情報を表示するコンポーネント
  - Footert
- font-family に BIZ UDPGothic を適用
  - 特定の要素に Typography を適用するために、layout.tsx で Goole Fonts を読み込む形にしています
  - [Next.js に Web Font を最適化する機能](https://nextjs.org/docs/app/getting-started/fonts)がありますが、こちらを利用すると全ての要素に適用されて Figma の状態と差異が出るため、この方法は選択しませんでした
  - Figma でもすべての要素に Typograohy が適用されたら、上記の機能を使うのが良いと思っています
- TextStyle とそれに関連した  Semantic Token を定義
  - https://chakra-ui.com/docs/styling/text-styles
  - https://chakra-ui.com/docs/theming/semantic-tokens
- Link コンポーネントを追加
  - https://chakra-ui.com/docs/components/link
  - 複数の箇所で独自に実装していたので、共通コンポーネントに切り出してデザインシステムのトークンを当てました
- textStyle など独自に定義した token が VS Code で補完できるようにするために typegen:chakra コマンドを追加
  - https://chakra-ui.com/docs/get-started/cli#chakra-typegen

# 関連Issue
- fix: #598 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- client でレポート情報と Footer に Typography が適用されていること

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
  - Google Fonts「BIZ UDPGothic」を全体に適用し、Webフォントの一貫性を向上。
  - 独自のLinkコンポーネントと統一されたテキストスタイルシステムを導入。
  - セマンティックなカラートークンやテキストスタイル、フォント設定を集中管理するテーマシステムを追加。

- **スタイル**
  - フッターやレポーター画面などでテキストやボタンのスタイルを一貫化し、可読性とデザインの統一感を改善。

- **ドキュメント／開発環境**
  - Chakra UI CLIの型生成スクリプトを追加し、開発効率を向上。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client] レポーター画像が Docker 環境で取得できないエラーを修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/595)

**作成者:** shgtkshruch  
**作成日:** 2025-06-09T09:09:13Z  
**変更:** +40 -30 (3ファイル)  
**マージ日:** 2025-06-12T06:57:47Z  
**内容:**

# 変更の概要
- #581 で追加した Reporter コンポーネントで、レポーターの画像が  Docker Compose 起動時に取得できないエラーが出ていたので修正しました
```
Failed to fetch reporter image: TypeError: fetch failed
client-1               |     at async a (.next/server/chunks/296.js:1:399) {
client-1               |   [cause]: [AggregateError: ] { code: 'ECONNREFUSED' }
client-1               | }
```

# スクリーンショット
赤枠で囲った画像が今回の修正対象です

![スクリーンショット 2025-06-09 17 26 38](https://github.com/user-attachments/assets/e53c43c6-9981-4fd3-8b4e-cd47c9c14821)

# 変更の背景
- レポーターの画像オプショナルなので、server 側で画像があるかどうかを判定しています
  - client 側で判定すると、画像の有無によってレイアウトがガタつくので、client でレンダリングする前に判定できる server で処理をしています
  - 画像があれば client から取得できる URL を設定した Image コンポーネントを返すようにしました
  - 元の実装で使っていた `getImageFromServerSrc` は[サーバーサイドレンダリング時に `NEXT_PUBLIC_API_BASEPATH` を使っていて](https://github.com/shgtkshruch/kouchou-ai/blob/e9b403e844ddc4a7f33562f681149f28b6379c21/client/app/utils/image-src.ts#L56-L57)、こちらは [cilent rendering 用の `API_BASEPATH`](https://github.com/digitaldemocracy2030/kouchou-ai/blob/e9b403e844ddc4a7f33562f681149f28b6379c21/.env.example#L39-L40) で実装とコメントに差異があるので、一旦使用するのを避けました
- Biome のフォーマット漏れのコードがあったので、合わせて修正しました

# 関連Issue
- #581

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- Docker Comopse 環境でレポータの画像を設定したら、エラーなく表示されること
- Static Build をした場合にもレポーター画像が表示されること

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

- **スタイル**
  - インポート文やコードの整形、クォートやインデントの統一など、コードスタイルを改善しました。

- **バグ修正**
  - レポーター画像の取得方法を修正し、環境変数を利用したURL生成に変更しました。これにより、画像の取得がより安定します。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (1件)

### [Revert "[FEATURE] admin のレポートについて、CSV ダウンロードを一律で可能にする"](https://github.com/digitaldemocracy2030/kouchou-ai/pull/605)

**作成者:** shingo-ohki  
**作成日:** 2025-06-17T09:29:21Z  
**変更:** +37 -16 (7ファイル)  
**内容:**

Reverts digitaldemocracy2030/kouchou-ai#603

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - 設定セクションに「CSV出力モード」のチェックボックスを追加し、ユーザーがCSV出力機能の有効・無効を切り替え可能になりました。

- **改善**
  - レポート作成時にCSV出力モードの設定を反映できるようになりました。
  - レポート一覧でCSVダウンロードボタンの表示条件を簡素化しました。

- **変更**
  - レポートのCSV出力モード設定の初期値が「無効」になりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(3件)

### [Feature/issue 493 レポート画面のスクロールイベント回避を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/597)

**作成者:** dentaro  
**作成日:** 2025-06-09T12:11:47Z  
**変更:** +141 -161 (2ファイル)  
**内容:**

# 変更の概要
client/components/chart.tsx
図の上にオーバーレイをかけることにより、レポートページを見ようとスクロールしても図が拡大縮小されないようにした。
1秒で自動解除。図内を出ると自動1秒でオーバーレイ復帰。
図の描画速度を向上させた。

# スクリーンショット
![image](https://github.com/user-attachments/assets/5d8d4190-239c-484b-bad0-3c2e8e81be15)
![image](https://github.com/user-attachments/assets/507f3cbc-2e45-4152-bf79-80e7c993bfdb)

# 変更の背景
ScatterChartの領域でスクロールで拡大縮小できるようになった。
このことにより「レポートページを見るためにスクロールする→図が拡大/縮小される」というユーザーが意図しない動作がほぼ発生する。何らかの方法でユーザー操作を直感的にする必要がある。

# 関連Issue
[FEATURE] レポートページを見ようとスクロールすると図が拡大縮小される #493

# 動作確認の結果
「親画面が一定時間（1秒）スクロールしていないこと」を拡大縮小のトリガーにする
親画面スクロール中にScatterChartにマウスオーバーしたら半透明のグレーのパネル（=操作無効）をChartに被せ、そのままスクロールで通り過ぎられるようにした
図内に入るとクリックしなくてもオーバーレイが解除される
意図しないスクロールによる拡大縮小を、オーバーレイのオン状態の時にキャンセルしている

以下の既存のエラー、警告は維持されているので、別のissueで対応すべき
・No label associated with a form field
・mg タグ、video タグ、canvas タグに overflow: visible を指定すると、要素の境界外にビジュアル コンテンツが作成される場合があります。https://github.com/WICG/shared-element-transitions/blob/main/debugging_overflow_on_images.md をご覧ください。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）]
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [] CIが全て通過している
- [] 単体テストが実装されているか
- [] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **ドキュメント**
  - READMEに「Windowsからプッシュ！！」という一文を追加しました。

- **リファクタ**
  - チャートのフィルタリング処理を効率化し、メモ化によるパフォーマンス向上を行いました。
  - チャートの描画ロジックを整理し、共通プロパティの管理を簡素化しました。

- **新機能**
  - チャート上にインタラクティブなオーバーレイを追加し、意図しない操作を防止できるようになりました。

- **スタイル**
  - フルスクリーンボタンやオーバーレイの表示位置・見た目を微調整しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix: ollama コンテナの起動方法](https://github.com/digitaldemocracy2030/kouchou-ai/pull/591)

**作成者:** shingo-ohki  
**作成日:** 2025-06-06T05:31:53Z  
**変更:** +1 -1 (1ファイル)  
**内容:**

# 変更の概要
- ollama コンテナの起動方法に誤りがあったので修正しました

# 関連Issue
#587 

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
  - OllamaサービスをGPUサポートで起動するためのDocker Composeコマンドのオプション順序を修正しました。

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

