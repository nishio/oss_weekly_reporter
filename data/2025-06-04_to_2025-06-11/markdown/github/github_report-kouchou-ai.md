# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-06-04T12:29:47.506818+09:00 から 2025-06-11T12:29:47.506818+09:00 まで

## Issues

### 過去7日間に完了されたissue (2件)

### [[FEATURE] 複数のレポートに対する処理を簡単に行えるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/461)

**作成者:** shingo-ohki  
**作成日:** 2025-05-08T00:35:39Z  
**内容:**

# 背景
>複数チェック/全部チェックしてから一括で
公開/ダウンロード/複製/削除/リストにグルーピング/リストに追加/リストから削除
とかできてもいいですね

from https://github.com/digitaldemocracy2030/kouchou-ai/issues/460#issuecomment-2859230331

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
- 複数のレポートに対する処理を簡単に行えるようにする

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

### 過去7日間に作成されたissue (6件)

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

### [[FEATURE] .env 書き換えた際に Docker build を忘れやすい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/594)

**作成者:** shingo-ohki  
**作成日:** 2025-06-06T13:39:40Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
タイトル通り。既に複数人が経験しているため、何かできることはないか？

> 環境変数（.env）を編集した場合は、docker compose down を実行した後、 docker compose up --build を実行してアプリケーションを起動してください
一部の環境変数は Docker イメージのビルド時に埋め込まれているため、環境変数を変更した場合はビルドの再実行が必要となります

[README](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/README.md?plain=1#L62-L63
)にはすでに記載がある

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
例）.env のファイルハッシュを取得して差分検知し、差分があったら build するようにするとか？

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

**コメント:** なし

---

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

### 過去7日間に更新されたissue（作成・クローズを除く）(4件)

### [[DOCUMENT]ローカル LLM の使用時のdocker composeコマンドについて](https://github.com/digitaldemocracy2030/kouchou-ai/issues/587)

**作成者:** dentaro  
**作成日:** 2025-05-31T14:59:36Z  
**内容:**

# 現在の問題点
README.mdの「ローカル LLM の使用」の項で、通らないコマンドがありました。

# 提案内容
「広聴AI」のREADME.mdの

docker compose up -d --profile ollama

Docker の version v2.35.1-desktop.1で、WINとMACで試しましたが、どちらも通らないようです。

docker compose --profile ollama up -d

だと通るようになりました。

**コメント:** なし

---

### [[REFACTOR] フロントエンド共通で利用するデザインシステムの開発基盤を作る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/586)

**作成者:** shgtkshruch  
**作成日:** 2025-05-31T09:34:50Z  
**内容:**

# 現在の問題点
<!-- 現在のコードの何が問題なのか、どのような技術的負債があるかを説明してください -->

- デザイナーさんの方でデザインシステムの整備を進めていただいています
  - https://github.com/digitaldemocracy2030/kouchou-ai/issues/504
  - https://github.com/digitaldemocracy2030/kouchou-ai/issues/505
  - https://github.com/digitaldemocracy2030/kouchou-ai/issues/506
- このデザインシステムは client, client-admin で使う想定で作成されています
- フロントエンドの実装としてもデザインシステムを整備して、client, client-admin など複数のサービスから import して使えるようにしたいです
  - 2025/05/31 時点では、複数のサービスで共通して使うライブラリやモジュールを配置して他のサービスから import しつつ、その依存関係を管理する仕組みはない認識です
  - 現状は client, client-admin で同じコンポーネントがあってもそれぞれで二重に実装している (ex. `components/ui` 以下のコンポーネント）ので、このやり方で Design System も実装できなくはないですが、DRY に実装したいなと思っています

# 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->

- 今は package manager として npm を採用しているので、まずはミニマムで [npm workspaces](https://docs.npmjs.com/cli/v8/using-npm/workspaces) で対応できると良いかなと考えています
  - 対象: client, client-admin, client-static-build とこれから実装する design-system


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

### [[FEATURE][design] レポート管理画面：直感的に使いやすくしたい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/460)

**作成者:** UtkNggc  
**作成日:** 2025-05-07T16:09:28Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
現状の管理画面は直感的に使いにくいかもしれない。
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

## Pull Requests

### 過去7日間にマージされたPR (2件)

### [[client] Dialog を開いた際の Initial Focus を変更する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/593)

**作成者:** shgtkshruch  
**作成日:** 2025-06-06T10:28:03Z  
**変更:** +9 -5 (1ファイル)  
**マージ日:** 2025-06-06T13:10:04Z  
**内容:**

# 変更の概要
- client の Footer 内にある「謝辞」と「免責」の Dialog を開いた際に、閉じるボタンに foucs が当たるようにしました

# スクリーンショット
## 謝辞

![image](https://github.com/user-attachments/assets/e6184ccb-7b74-48d5-93bf-bcd62dfd45ec)

## 免責

![image](https://github.com/user-attachments/assets/dfcb1398-8d3c-4139-a3bb-016c58784d9b)

# 変更の背景
- 元の実装は Chakra UI のデフォルトの挙動で、Dialog 内に出現する Initial Focusable Element にフォーカスが当たるようになっていました
  - おそらくこちらの挙動を実施しているものと思われます
  > ダイアログを実装する際には、ユーザーのフォーカスを設定する場所として最も適切な場所を検討することが重要です。HTMLDialogElement.showModal() を用いて <dialog> を開いたとき、フォーカスは内部で最初のフォーカス可能な要素に設定されます。
ref: [<dialog>: ダイアログ要素 - HTML: ハイパーテキストマークアップ言語 | MDN](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/dialog#%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B7%E3%83%93%E3%83%AA%E3%83%86%E3%82%A3)
- この挙動によって、「謝辞」の Dialog を開いた際に「[AI Objectives Institute](https://ai.objectives.institute/)」の Link に対して Initial Focus が当たっていました
- 上記のリンクは参考情報を掲載したもので、ユーザーに MUST で閲覧してもらうことを期待した Link ではないので、Initail Focus が当たることは違和感がある
- W3C の Accecibiliy のガイドラインでは追加的な情報を表示する Dialog について最も頻繁に使われそうな要素に focus するのが望ましいという記述があるので、今回は「閉じる」ボタンに Initial Focus を当てるように変更しました
  > If a dialog is limited to interactions that either provide additional information or continue processing, it may be advisable to set focus to the element that is likely to be most frequently used, such as an OK or Continue button.
ref: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- Chakra UI で Initial Foucs を設定する方法: https://www.chakra-ui.com/docs/components/dialog#initial-focus

# 関連Issue
- https://github.com/digitaldemocracy2030/kouchou-ai/pull/589#issuecomment-2948651314

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- client で謝辞と免責の Dialog を開いて、閉じるボタンにフォーカスが当たっている

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
  - ダイアログ表示時に「閉じる」ボタンへ初期フォーカスが自動的に当たるようになりました。

- **改善**
  - フォーカス管理とアクセシビリティが向上しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client] Footer にプロジェクトの概要をまとめる](https://github.com/digitaldemocracy2030/kouchou-ai/pull/589)

**作成者:** shgtkshruch  
**作成日:** 2025-06-03T10:39:31Z  
**変更:** +459 -132 (8ファイル)  
**マージ日:** 2025-06-05T15:21:37Z  
**内容:**

# 変更の概要
- Footer を新しいデザインに合わせて実装しました
  - 広聴AI やデジタル民主主義2030 プロジェクトの概要の情報がこちらに配置されます
- Figma: https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=509-3935&t=ourvDYxYXZbZlZBY-4

# スクリーンショット
## 375px
### Footer
![sm](https://github.com/user-attachments/assets/89a43141-dc1d-47e0-8503-8239571f114a)

### 謝辞
![image](https://github.com/user-attachments/assets/6646a1b6-8aa3-4c24-ae0d-87802c629d69)


### 免責
![image](https://github.com/user-attachments/assets/45cdb71c-df24-41e9-93e3-f197b83dbaf6)


## 768px
### Footer
![md](https://github.com/user-attachments/assets/2d70a1ce-ad81-42e4-8fe6-153b74cd5ebd)

### 謝辞
![image](https://github.com/user-attachments/assets/208ecf50-5e75-4b35-8f48-805a901e0b40)

### 免責
![image](https://github.com/user-attachments/assets/510ecbd0-44a0-4c32-a311-fd6d5a2923a5)


## 1280px
### Footer

![lg](https://github.com/user-attachments/assets/61351dff-79cc-488b-9df5-43c567ef164d)

### Empty

metadata が未設定で、レポートが0件の場合。
レポート件数が少ない場合でも、Footer はページ下部に固定して配置しています。

![empty](https://github.com/user-attachments/assets/a6c280de-2132-4689-9793-912c8cfbd7af)


### レポート詳細画面

![report-detail](https://github.com/user-attachments/assets/18f6a1cd-e90c-48b9-af74-2a8688a1b616)


### インタラクション
※ スクリーンキャプチャのツールの影響でボタンに hover した際にカーソルが変わっていませんが、実際は pointer になります

**デザイナーへの確認事項**: 利用規約や免責のボタンは hover 時のインタラクションがわかりやすいように、plain -> ghost のボタンにしているがどうでしょう？
Chakra UI で定義されている Button の種類: https://chakra-ui.com/docs/components/button#variants

https://github.com/user-attachments/assets/e5be8468-b5e2-4bac-a6ee-b9b5a171fb08

# 変更の背景

- Footer のデザインが更新されたので、実装も追従しました
- まだデザインシステムが未整備なので、Typography（font-family, letterSpacing など）は取り込めていません
  - こちらの issue でフロントエンドのデザインシステムの開発基盤ができたら、そこに Typography の定義をした後に、client から読み込む形にできればと思っています
  - https://github.com/digitaldemocracy2030/kouchou-ai/issues/586

# 関連Issue
- fix: #438 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- client のレポート一覧、レポート詳細画面で Footer が適切に表示されていることを確認

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
  - フッターにSNS（X、Note、Slack、GitHub）アイコンを追加し、外部リンクボタンを拡充しました。
  - 「謝辞」「免責」などの情報をダイアログ形式で表示する新しいモーダルUIを導入しました。

- **デザイン・スタイル**
  - フッターのレイアウトとデザインを一新し、ブランドイメージや画像を強化しました。
  - 全体の余白や背景、ボタンデザインを調整し、より統一感のある見た目に改善しました。
  - ヘッダーに縦方向の余白を追加しました。

- **その他**
  - フッターは常に表示されるようになりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (3件)

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

### [[client] レポーター画像が Docker 環境で取得できないエラーを修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/595)

**作成者:** shgtkshruch  
**作成日:** 2025-06-09T09:09:13Z  
**変更:** +40 -30 (3ファイル)  
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
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


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

### 過去7日間に更新されたPR（作成・マージを除く）(13件)

### [Draft/221 auto cluster and skip](https://github.com/digitaldemocracy2030/kouchou-ai/pull/565)

**作成者:** take365  
**作成日:** 2025-05-23T03:45:03Z  
**変更:** +842 -169 (22ファイル)  
**内容:**

 #221 自動クラスタ設定＋スキップ設定＋省略タイトル補完
 のドラフト
 
 
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

**コメント:** なし

---

### [グラフ選択の UI を Figma と揃える](https://github.com/digitaldemocracy2030/kouchou-ai/pull/563)

**作成者:** shgtkshruch  
**作成日:** 2025-05-22T09:53:04Z  
**変更:** +2 -2 (1ファイル)  
**内容:**

# 変更の概要
- スマホサイズの SegmentControl の高さが Figma と異なっていたので、修正しました
- Figma: https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=48-14037&t=193sCKxfNOY0fQKb-0

# スクリーンショット
## before
![image](https://github.com/user-attachments/assets/18a75ad4-007b-42f0-8d75-a60d71094332)


## after

![image](https://github.com/user-attachments/assets/7044847e-c693-4168-a08a-35308924204e)


# 変更の背景
- https://github.com/digitaldemocracy2030/kouchou-ai/pull/531/ で、SegmentControl の高さがずれていた不具合を修正した際にスマホ時の高さがを考慮する指定がなくなったため

# 関連Issue
https://dd2030.slack.com/archives/C08F7JZPD63/p1747901201788969?thread_ts=1747883068.322639&cid=C08F7JZPD63

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

画面サイズをスマホサイズにして、Figma と同じ高さの SegmentControl になっていることを確認しました。

ここに関連する箇所の以前の PR で意図しないデザインの崩れがあったので、念の為レビュアーの方のローカルでも表示を確認していただけると嬉しいです :pray:

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
  - セグメントグループの高さがレスポンシブになり、小さい画面では80px、大きい画面では56pxに調整されました。
  - 内部アイテムの高さが親コンテナに合わせて自動調整されるようになりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

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

### [Add Windows manual startup support (venv/npm) - resolves #999](https://github.com/digitaldemocracy2030/kouchou-ai/pull/498)

**作成者:** take365  
**作成日:** 2025-05-13T05:37:10Z  
**変更:** +127 -2 (3ファイル)  
**内容:**

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
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - Windowsユーザー向けに、Dockerを使わずに開発環境をセットアップ・起動できる手順をREADMEに追加しました。
  - Windows用のバッチスクリプトを追加し、環境変数の設定や各サービス（サーバー、クライアント、管理画面）の自動起動をサポートしました。

- **改善**
  - レポート生成時に使用するPython実行ファイルを環境変数から動的に選択できるようになりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Feat/evaluation report](https://github.com/digitaldemocracy2030/kouchou-ai/pull/448)

**作成者:** take365  
**作成日:** 2025-05-07T04:30:03Z  
**変更:** +1584 -0 (8ファイル)  
**内容:**

# 変更の概要
- クラスタリング評価結果をCVS形式、HTML形式で出力するレポート生成機能を experimental/evaluation_report 以下に新規追加しました。
- LLM評価（明確さ、一貫性、多様性、代表性）とシルエットスコア（UMAP・Embeddingベース）を統合し、可視化可能なHTMLレポートとして出力します。
- 既存の本番コードには影響しない構成となっており、すべての変更は experimental/ ディレクトリに収まっています。
-タイトル・解説が「エラー」なのに低い評価ができていない、意見が１件の場合の意見のまとまり具合がアンバランスも対応

# 変更の背景
- 現在のクラスタリング評価はCSVやJSON形式が中心であり、利用者や開発者が結果を俯瞰して確認するのが難しい状況でした。
- 本変更により、評価結果を視覚的に確認でき、クラスタリング精度の比較や改善方針の立案が容易になります。
- 将来的に本機能を本体に統合することも視野に入れた、初期実装段階として experimental/ に追加しています。

# 関連Issue
（実験）LLMによるクラスタ品質の自動評価 #144
https://github.com/digitaldemocracy2030/kouchou-ai/issues/144 

# CLAへの同意
- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Windows 環境で Docker を使わずに手動でセットアップできるようにするためのスクリプトおよび手順](https://github.com/digitaldemocracy2030/kouchou-ai/pull/363)

**作成者:** take365  
**作成日:** 2025-04-23T09:55:11Z  
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

# CLAへの同意
- [x] コントリビューターライセンス契約（CLA）に同意します。

**コメント:** なし

---

### [改行コード混在の解消のため .gitattributes を追加（#243 対応）](https://github.com/digitaldemocracy2030/kouchou-ai/pull/314)

**作成者:** take365  
**作成日:** 2025-04-16T03:07:22Z  
**変更:** +2 -0 (1ファイル)  
**内容:**

# 変更の概要

- `.gitattributes` を追加し、改行コード（LF / CRLF）をファイル種別ごとに明示的に制御するようにしました。

# 変更の背景

- Windows環境での利用時、Git の自動変換（`core.autocrlf`）やエディタの設定により `.sh` ファイルが CRLF になってしまい、
  POSIXシェルで構文エラー（"unexpected 'fi' (expecting 'then')"）が発生するケースがありました。
- これは entrypoint.sh の構文の問題ではなく、改行コードが Windows形式（CRLF）で保存されたことが原因です。
- `.gitattributes` によって `*.sh` は LF、`*.bat` や `*.cmd` は CRLF に固定することで、OS間の不整合を防ぎます。

# 関連Issue

- https://github.com/digitaldemocracy2030/kouchou-ai/issues/243
- https://github.com/digitaldemocracy2030/kouchou-ai/issues/286
# CLAへの同意

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Windowsユーザの利用環境構築 #300　の調整](https://github.com/digitaldemocracy2030/kouchou-ai/pull/313)

**作成者:** take365  
**作成日:** 2025-04-16T02:49:17Z  
**変更:** +50 -20 (4ファイル)  
**内容:**

# 変更の概要
setup_win.bat の文言を英語化し、Docker起動時の挙動を --build に変更
起動・停止用の補助バッチファイル（start_win.bat, stop_win.bat）を追加
運用手順を含めたガイド（windows-setup.md）を追記

# 変更の背景
リンクが切れている部分があった(sample.envとずれていた）
日本語の影響で処理が異常になった。かといってSJISにするとwebで化ける
docker compose up -d では.env の変更が反映されないことがあるため、初回実行時から --build を使うように変更
コマンド操作が苦手な非エンジニアの利用者向けに、クリックだけで起動・停止できるバッチファイルを用意
その利用手順を windows-setup.md に明記し、運用しやすい形にしました

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/300


- [x ] CLAの内容を読み、同意しました

**コメント:** なし

---

### [frontend のコードを push する際に Biome の Lint を実行できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/270)

**作成者:** shgtkshruch  
**作成日:** 2025-04-09T09:53:33Z  
**変更:** +299 -47 (12ファイル)  
**内容:**

# 変更の概要
- [Lefthook](https://github.com/evilmartians/lefthook) を使って、Git Hooks の pre-push で Biome の Lint を実行できるようにしました
- CONTRIBUTING.md に client, client-admin のコードチェックに関する記載を追加しました
- 動作確認をしている際にフォーマット漏れのコードがあったので、Biome のフォーマットを適用しました

# 変更の背景
-  Lefthook はデフォルトでは off にしていて、設定ファイルを作成することで on になる設計にしています
    - 理由: 現状の Lefthook の設定は frontend のコードのみで、server 側の開発をする人にも有効にした場合に弊害が出る可能性を避けたかった
    - 最初は安全側に倒して、導入してみて良さそうであればデフォルトで on に変えても良いかもしれません
- pre-commit で毎回チェックすると少し煩雑かなと思ったので、pre-push でチェックするようにしました

# 関連Issue
- fix: #84 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [client の package-lock.json に差分が出る課題の修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/263)

**作成者:** shgtkshruch  
**作成日:** 2025-04-08T12:36:06Z  
**変更:** +320 -3292 (5ファイル)  
**内容:**

# 変更の概要
- `npm i` 実行後に client の package-lock.json で差分が出ないようにしました
- 新たに client に追加されたコードに Biome のフォーマットを適用しました

# 変更の背景
- https://github.com/digitaldemocracy2030/kouchou-ai/pull/247/commits/3a7ad517ed90b3a121dd835fbb93d6d1c00277f5 の commit で ESLint を削除する修正がデグレしていたのでもとに戻しました
- Biome のコードフォーマットをチェックする CI があっても良さそうなので、この後 issue だけ作ろうと思います 📝 

# 関連Issue
関連するIssueのリンクをこちらに記載してください

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [client-admin に Biome を適用](https://github.com/digitaldemocracy2030/kouchou-ai/pull/262)

**作成者:** shgtkshruch  
**作成日:** 2025-04-08T12:26:20Z  
**変更:** +1173 -4101 (32ファイル)  
**内容:**

# 変更の概要
- client-admin に Biome を適用しました

# 変更の背景
- 差分が大きいのでコミット単位でみていただけると良さそうです
  - https://github.com/digitaldemocracy2030/kouchou-ai/commit/4af790cd4bd43d37ea6ef118c9fad9b57fc33541 ESLint を削除
  - https://github.com/digitaldemocracy2030/kouchou-ai/commit/0e9e28da0793a9e2d03b6949caf5c632822e1f2b npm script に Biome のコマンドを追加
  - https://github.com/digitaldemocracy2030/kouchou-ai/commit/680a97801f1e5bef81c846ba4c3230627ce89869 Biome の format を適用（自動で修正できるもののみなので、コードの構造は変わっていない認識です）
  - https://github.com/digitaldemocracy2030/kouchou-ai/commit/d6bd0b4da71079b7437ad0f1082263f66a7bcc4c 自動で直せない format, lint エラーを修正（ここは手動で対応したので見てもらいたいところです）

# 関連Issue
- #84 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [client に Biome を適用](https://github.com/digitaldemocracy2030/kouchou-ai/pull/249)

**作成者:** shgtkshruch  
**作成日:** 2025-04-07T12:21:33Z  
**変更:** +2070 -4995 (55ファイル)  
**内容:**

# 変更の概要
- client に Biome の lint と format を適用しました

# 変更の背景
- 差分が大きいので、コミット単位で見ていただけると良さそうです
  - https://github.com/digitaldemocracy2030/kouchou-ai/commit/ba19407ed69f2ca7d31eecdcf20aabb37bb1be15 ESLint を削除 
  - https://github.com/digitaldemocracy2030/kouchou-ai/commit/6a641bfa8d9de8c97c6f4ddb15923fd40d482815 npm scirpt に Biome のコマンドを追加
  - https://github.com/digitaldemocracy2030/kouchou-ai/commit/f341c4db5bbc30e6744d937c3a1ebc8345304f38 Biome の format を適用（自動で修正できる分なので、コードの構造は変わっていない認識です）
  - https://github.com/digitaldemocracy2030/kouchou-ai/commit/3cae15cae82f203bb147a796eafd3af76371d1d8 自動で直せない format, lint エラーを修正（ここは手動でやっているので見てもらいたい部分です）
  - https://github.com/digitaldemocracy2030/kouchou-ai/commit/4cfbfb7d2ffb379ffa5f2f054d1ba564691ae24e プロジェクトルートに Biome を追加したので、setup script でもルートで `npm install` する処理を追加
- 動作確認したこと
  - `npm run dev` でブラウザで動作すること
  - `npm run build`, `npm run build:static` がエラーなく終了すること
  
# 関連Issue
- #84 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Biome の追加と dummy-server にフォーマットを適用](https://github.com/digitaldemocracy2030/kouchou-ai/pull/242)

**作成者:** shgtkshruch  
**作成日:** 2025-04-06T08:41:59Z  
**変更:** +566 -4291 (15ファイル)  
**内容:**

# 変更の概要
- Biome をプロジェクトルートにインストールしました
  - Biome の設定は [idobata-analyst](https://github.com/digitaldemocracy2030/idobata-analyst/blob/main/biome.json) を参考にしつつ、ベーシックなものを設定しています
- utils/dummy-server を ESLint -> Biome に置き換えてフォーマットを適用しました
- VS Code の workspace settings 用のファイルを追加しました

# 変更の背景
- client, client-admin, utils/dummy-server で共通した設定を使うために、プロジェクトルートに Biome をインストールしました
  - 既存の PR とコンフリクトしにくそうなのと、Biome の動作確認も兼ねて utils 以下にフォーマットを適用しました
  - client, client-admin は後続の PR で対応するので、一旦 biome.json の ignore に追加しています
  - server は Python のコードになるので ignore にしています
- npm workspace 化するか迷ったのですが、もとの issue からスコープが大きくなりそうかなと思ったので、一旦やめておきました（対応した方がよければ合わせて対応するのでコメントいただけると :pray: ）

# 関連Issue
- https://github.com/digitaldemocracy2030/kouchou-ai/issues/84

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

