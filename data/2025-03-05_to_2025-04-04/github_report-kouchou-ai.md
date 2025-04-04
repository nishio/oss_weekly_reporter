# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-03-05 から 2025-04-04 まで

## Issues

### 過去30日間に完了されたissue (30件)

### [[FEATURE]CIでpytestを実行する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/205)

**作成者:** nasuka  
**作成日:** 2025-03-31T06:31:29Z  
**内容:**

# 背景
* 現状テスト/CIが整備されていないためにバグが発見しにくく、またレビュー/QAに時間がかかる

# 提案内容
* github actionsで、PR作成/pushのタイミングでpytestを実行し、failする場合はマージできないようにする
* 現状テストコードが全く整備されていないので、CI実施のためにまずは簡単なテストコードをいくつか実装する

**コメント:** なし

---

### [[DOCUMENT]コードの貢献プロセスの記載](https://github.com/digitaldemocracy2030/kouchou-ai/issues/201)

**作成者:** nasuka  
**作成日:** 2025-03-30T14:46:49Z  
**内容:**

# 現在の問題点
* コードの貢献プロセスについて、CONTRIBUTING.mdに記載されていない内容がある
  * e.g. 👍 の件数が優先度を決める上で参考にされる、など

# 提案内容
* CONTRIBUTING.mdに、上記のように明文化されていない内容を記載する


**コメント:** なし

---

### [[DOCUMENT] server開発時のコンテナ起動方法についてREADMEに明記する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/199)

**作成者:** ei-blue  
**作成日:** 2025-03-30T05:30:22Z  
**内容:**

# 現在の問題点
serverディレクトリでmake runを実行すると、config.pyで正しく.envが参照されずエラーになる。

# 提案内容
serverディレクトリのREADMEに記載されている内容を実行するとエラーになるので、serverコンテナだけを起動する方法を明記する。

**コメント:** なし

---

### [[BUG]静的HTML出力時の画像の 404 解消](https://github.com/digitaldemocracy2030/kouchou-ai/issues/196)

**作成者:** nishio  
**作成日:** 2025-03-28T15:41:33Z  
**内容:**

### 概要
see https://github.com/digitaldemocracy2030/kouchou-ai/pull/195
<!-- バグの簡潔な説明をお願いします -->

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

### [[DOCUMENT] 環境変数を書き換えた場合は docker compose up --build を実行するようにREADMEに追記する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/191)

**作成者:** nasuka  
**作成日:** 2025-03-28T06:16:48Z  
**内容:**

# 現在の問題点
* 環境変数を変更した場合はdocker imageをbuildしなおさないと動作しないケースがある
  * フロントでは、APIキーなどの一部の環境変数をimageのビルド時に埋め込んでいる
  * このため、フロント側はdocker compose upを実行すると初回に設定した環境変数のイメージのままコンテナが立て続けられてしまう（ビルド時に埋め込んでいる環境変数は、イメージをビルドし直さない限り.envを編集しても変更が反映されない）
    * これにより以下の様にapiとフロントのAPIキーが一致しないケースが発生してしまう

```
1: デプロイの作業をしてたディレクトリでそのまま新機能開発をしようとしてdocker-compose upしたら起動はしたけど管理画面がAPIサーバに繋がらなくてスピナーが回りっぱなし
2: 原因は401 unauthorized
3: docker-compose upすると、compose.yamlのclient-adminはAPIサーバに接続するためのAPIキーをargsでハードコードしているので管理画面には古いキーが環境変数として渡される、一方でserverの方はそれをしないで.envを渡しているのでこちらは新しいAPIキーが渡される、不一致なので繋がらない
```

# 提案内容
* 環境変数を書き換えた場合は `docker compose up --build` を実行するようにREADMEに追記する


**コメント:** なし

---

### [[FEATURE]スプレッドシートでデータを取得した後にレポートIDを変更して作成を実行するとコメントデータが二重に保管される](https://github.com/digitaldemocracy2030/kouchou-ai/issues/184)

**作成者:** nasuka  
**作成日:** 2025-03-26T06:42:10Z  
**内容:**

# 背景
* レポート作成画面において、スプレッドシートからデータを取得した後にレポートのIDを変更すると、コメントのデータが二重に保管されてしまう
  * スプレッドシート取得時のIDと、レポート作成ボタンを押した時点のIDでそれぞれコメントデータが保存される
  * ID変更前のデータはその後参照されず、APIサーバーのディスク容量を無駄に消費してしまう


# 提案内容
* データ取得後にレポートのIDを変更できないようにした上で、画面上でその旨を表示する
  * e.g. 「スプレッドシートからデータを取得した後はIDを変更できません」といった文言をIDの入力フォーム直下に表示する

ただ、容量の問題を解決するだけであれば、report_status.jsonに存在しないslugのデータがinputsに存在する場合に削除するような処理を走らせるようにしても良いかもしれない？ 妙案ある方はコメントいただけると助かります。




**コメント:** なし

---

### [[FEATURE]resultをローカル環境へ取得するscriptをつくる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/179)

**作成者:** nishio  
**作成日:** 2025-03-25T13:23:48Z  
**内容:**

# 背景

リモート環境で作成されたレポートのデータをローカルに持ってくることが現状少し不便

>1.既存のAPIに対して以下を実施
GET /reports を叩いて全レポートのslugを取得する
GET /reports/{slug}を叩いて個別のレポートのresultを取得する
2.新規に構築した環境に以下を実施
outputs配下に各slugの名称でディレクトリを作ってその配下にresultを置く
./server/data/配下のreport_status.jsonを手動で編集する（これを編集しないと一覧画面にレポートが表示されない）

from https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1742904758383619?thread_ts=1742889178.309719&cid=C08F7JZPD63


# 提案内容
これをやるscriptを作る


**コメント:** なし

---

### [[FEATURE]dependabotの導入](https://github.com/digitaldemocracy2030/kouchou-ai/issues/151)

**作成者:** nasuka  
**作成日:** 2025-03-25T05:54:10Z  
**内容:**

# 背景
* セキュリティの脆弱性に伴うパッケージのアップデートを行いたい
* 現状でもgithub上の `Security` でアラートはくるが、パッケージアップデートをする際は手作業が入る


# 提案内容
* dependabotを用いてパッケージアップデートのPR作成を自動化する

**コメント:** なし

---

### [[FEATURE]API呼び出し前にCSVファイル内の意見数を確認する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/147)

**作成者:** ei-blue  
**作成日:** 2025-03-25T05:27:30Z  
**内容:**

# 背景
CSVファイルのデータから最終的に抽出された意見の数が詳細設定で設定されたクラスタ数を下回っていると、クラスタリングの過程でエラーになり、無駄にAPIを呼び出すことになってしまう。

# 提案内容
「レポート作成を開始」ボタンを押した際にクラスタ設定の数とCSVファイルの行数を比較し、CSVファイルの行数の方が少ない場合に警告を出す。
コメント数（CSVファイルの行数）＝最終的な意見の数　ではないため、エラーにする必要はない。

**コメント:** なし

---

### [[BUG] Unknown event handler property `onFileRemove`. が出る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/142)

**作成者:** shingo-ohki  
**作成日:** 2025-03-25T03:25:55Z  
**内容:**

### 概要

https://github.com/digitaldemocracy2030/kouchou-ai/commit/685bb7c685e281ad3afb760bc8e7c9d649532d41

の状態のコードで localhost:4000/create にアクセスすると以下のエラーが出る。

`Unknown event handler property `onFileRemove`. It will be ignored.
`
### 再現手順

1. https://github.com/digitaldemocracy2030/kouchou-ai/commit/685bb7c685e281ad3afb760bc8e7c9d649532d41 を checkout
2. docker compose up
3. ブラウザで localhost:4000/create にアクセス

### 期待する動作
エラーが出ないこと

### スクリーンショット・ログ

![Image](https://github.com/user-attachments/assets/71256468-62ea-40fe-aa58-ccfbbe88199f)

![Image](https://github.com/user-attachments/assets/55429512-79dc-4dd6-8bbe-a6d0b5ee98a0)

### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->

**コメント:** なし

---

### [[FEATURE] OGPカードを魅力的なものにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/140)

**作成者:** takahiroanno  
**作成日:** 2025-03-25T02:49:25Z  
**内容:**

# 背景
SNSなどでシェアされることによって広聴AIの存在が広く知られる

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

**コメント:** なし

---

### [テスト](https://github.com/digitaldemocracy2030/kouchou-ai/issues/135)

**作成者:** nasuka  
**作成日:** 2025-03-23T02:33:21Z  
**内容:**

## 要望内容
テスト

---
こちらのイシューはGoogle Form経由で投稿されたものです

**コメント:** なし

---

### [テスト用イシューです](https://github.com/digitaldemocracy2030/kouchou-ai/issues/134)

**作成者:** nasuka  
**作成日:** 2025-03-23T02:33:18Z  
**内容:**

## 要望内容
テスト

---
こちらのイシューはGoogle Form経由で投稿されたものです

**コメント:** なし

---

### [[DOCUMENT]Azureのセットアップガイドに関する免責事項を記載する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/133)

**作成者:** nasuka  
**作成日:** 2025-03-23T02:11:50Z  
**内容:**

# 現在の問題点
- セットアップ手順に従った結果に対する責任範囲が明確に定義されていない
  - 利用者がトラブル発生時にプロジェクトに過度な責任を求める可能性がある

# 提案内容
以下のような免責事項を記載する

* 本ドキュメントは情報提供のみを目的としており、特定の環境でのデプロイを保証するものではありません。
* 本ガイドに従って実施されたデプロイや設定によって生じた問題、損害、セキュリティインシデントについて、作者および関連プロジェクト貢献者は一切の責任を負いません。
* 各組織のセキュリティポリシーやコンプライアンス要件に従って適切に評価・カスタマイズしてください。


**コメント:** なし

---

### [[FEATURE] 意見データの入力にGoogle スプレッドシートのデータを使えるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/132)

**作成者:** shingo-ohki  
**作成日:** 2025-03-23T01:31:08Z  
**内容:**

# 背景
- #124 とは別のルートとして、意見データとしてGoogle スプレッドシートのデータが使えると文字コードの問題を回避できる
- #105 のパブコメ自体を Google Form で集めるように標準化できると、それをそのまま広聴AIに流し込める

# 提案内容
Google スプレッドシートのURLを指定できるようにする

- [x] #182 
- [ ] 非公開のSpreadsheetにサービスアカウントをinviteしてもらってそれを読む

**コメント:** なし

---

### [[FEATURE] OpenRouterを用いて動くようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/128)

**作成者:** 101ta28  
**作成日:** 2025-03-22T14:07:01Z  
**内容:**

# 背景
[idobata-analyst](https://github.com/digitaldemocracy2030/idobata-analyst) では、AI呼び出しに[OpenRouter](https://openrouter.ai)を用いている。

環境構築時に共通プラットフォームのKeyを用いることができれば便利だと思うため。

また、(OpenAI以外の)複数モデルの切り替えがしやすいものが良いと思ったため。

# 提案内容

server ディレクトリ内の`config.py`や`hierarchical_utils.py`を変更すれば動くと思われます。

**コメント:** なし

---

### [[FEATURE]Shift-JISのcsvをUTF-8に変更する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/124)

**作成者:** yuneko1127  
**作成日:** 2025-03-22T04:56:29Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
ExcelなどでCSVを作成するとShift-JISになり、非エンジニアの利用を考えるのであれば、文字コードの変換は利用者側ではなくシステム側でやるべきだと考えるから。


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
最初にcsvを読んでいるところで、UTF-8でない場合は別の処理をする。

**コメント:** なし

---

### [[FEATURE]文字コードがSJISやBOMがついてるときPythonで変換する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/123)

**作成者:** nishio  
**作成日:** 2025-03-22T04:50:42Z  
**内容:**

# 背景
ExcelからCSVを書き出す時、だいたいSJISで書き出してしまうしUTF-8にするとしてもBOMをつけてしまったりする

# 提案内容
エラーにするより、しれっと変換したほうが説明コスト低いのではないか


**コメント:** なし

---

### [[FEATURE]サンプルデータの件数増加](https://github.com/digitaldemocracy2030/kouchou-ai/issues/120)

**作成者:** nasuka  
**作成日:** 2025-03-21T12:59:17Z  
**内容:**

# 背景
- 現在のサンプルは50件しかないため、濃いクラスタを表示しても全体図と描画が変わらず挙動のイメージがつかない


# 提案内容
- サンプルデータの件数を増やす
  - 200件程度あれば良さそう

**コメント:** なし

---

### [バグテスト](https://github.com/digitaldemocracy2030/kouchou-ai/issues/119)

**作成者:** nasuka  
**作成日:** 2025-03-21T11:20:59Z  
**内容:**

## バグの内容


---
こちらのイシューはGoogle Form経由で投稿されたものです

**コメント:** なし

---

### [[REFACTOR]レポート画面における「議論」という言葉がわかりにくい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/118)

**作成者:** nasuka  
**作成日:** 2025-03-21T08:20:23Z  
**内容:**

# 背景
* レポート表示画面で「議論」という単語が使われているが、日本語としてわかりにくい
  * 「33議論」といった表記はそもそも日本語として正しくないように思える
  * Analysis配下の「議論を抽出」といった表現も違和感がある
![Image](https://github.com/user-attachments/assets/d4068108-dc0c-4639-9dae-942ab870db3a)



![Image](https://github.com/user-attachments/assets/669b7198-8e0f-43ed-a4ad-dbbad40c5720)

# 提案内容
1. クラスタタイトル下の「33議論」等の表現は「33件」という表現に変える
2. Analysis内で使われている「議論」という単語は 「意見」に置き換える（実際に行っている処理としても意見の方がニュアンス的に正しい）


**コメント:** なし

---

### [バグテスト](https://github.com/digitaldemocracy2030/kouchou-ai/issues/117)

**作成者:** nasuka  
**作成日:** 2025-03-21T05:53:25Z  
**内容:**

## バグの内容


---
こちらのイシューはGoogle Form経由で投稿されたものです

**コメント:** なし

---

### [[FEATURE]クラスタ数5/50が分数に見える](https://github.com/digitaldemocracy2030/kouchou-ai/issues/114)

**作成者:** nishio  
**作成日:** 2025-03-20T12:24:41Z  
**内容:**

# 背景

<img width="817" alt="Image" src="https://github.com/user-attachments/assets/4adeaef8-77dc-4dbb-a8d9-44f7b2e2fe4c" />

実際には「一段階目5個、二段階目50個」の意味だが、まあこの表現では伝わらないか...


# 提案内容
たとえば「一段階目5件 / 二段階目50件」とか「大分類5 / 小分類50」とかの文字を補う

**コメント:** なし

---

### [[FEATURE]クラスタ見出しをanchorにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/112)

**作成者:** nishio  
**作成日:** 2025-03-20T12:12:16Z  
**内容:**

# 背景

<img width="832" alt="Image" src="https://github.com/user-attachments/assets/4f696633-40b9-47c4-924d-01ab50c0c50c" />

# 提案内容

展開表示するものは将来的には階層クラスタリングのデータから取れるかもしれないが、とりあえずanchorにしたら特定の見出しにリンクして言及できるようになって良いのではないか

**コメント:** なし

---

### [[REFACTOR] 「クラスタ」言い換え案](https://github.com/digitaldemocracy2030/kouchou-ai/issues/110)

**作成者:** nishio  
**作成日:** 2025-03-20T12:05:11Z  
**内容:**

# 現在の問題点
「クラスタ」という言葉がわかりにくい

# 提案内容
案出し
- 意見集団
- 意見グループ
- 意見チーム

**コメント:** なし

---

### [[FEATURE]apiのlint（ruff）をdocker環境でできるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/108)

**作成者:** nasuka  
**作成日:** 2025-03-20T08:34:36Z  
**内容:**

# 背景
* CIでruffによるlintを走らせているが、ローカル環境でruffによるcheck/formatを行うには、python環境の構築が必要
  * dockerがあるのに、lintのためにローカル環境にpython環境の構築が必要な情報状態となっている

# 提案内容
* docker環境でruffによるcheck/formatを実行できるようにする

**コメント:** なし

---

### [[FEATURE]ロゴから掛け算をなくす](https://github.com/digitaldemocracy2030/kouchou-ai/issues/106)

**作成者:** takahiroanno  
**作成日:** 2025-03-20T07:59:47Z  
**内容:**

# 背景

![Image](https://github.com/user-attachments/assets/df86ddf6-c54f-492c-b12d-4ee177281817)

- 上記ロゴの掛け算の右側はないほうがよいかと思います
  - 自治体、政党などがより使いやすくなる
  - ユーザーにとっても初見で情報が多すぎなくて済む

フッターの右下にデジ民の解説はあるので、ここに入れずに済むかと思います

# 提案内容
掛け算の右側の削除

**コメント:** なし

---

### [[FEATURE]パブコメ形式でレポート出力するようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/105)

**作成者:** takahiroanno  
**作成日:** 2025-03-20T07:47:45Z  
**内容:**

# 背景
具体的なユースケースとして、行政機関においてパブコメを分析することがありそう。
その際に、よく用いられている方式で意見のカタマリをexportできると、自治体のユーザーにとって使いやすくなる。

例
- https://www.mlit.go.jp/common/001034196.pdf
- https://www8.cao.go.jp/cstp/pubcomme/kihon4_toshin/kekka2.pdf

# 提案内容

- レポート出力、ボタンをおく（チャートの右上に並べるのが一案か）
- ３カラムでcsvを出力する
  - 大分類
  - 小分類（濃いクラスタのみ）

**コメント:** なし

---

### [[REFACTOR] 不要な.env.exampleの削除](https://github.com/digitaldemocracy2030/kouchou-ai/issues/101)

**作成者:** nasuka  
**作成日:** 2025-03-20T06:39:55Z  
**内容:**

# 現在の問題点
server配下に.env.exampleがあるが、使われていない

# 提案内容
./server/.env.exampleを削除する


**コメント:** なし

---

### [[FEATURE]CSVのアップロードが成功した際に成功メッセージを表示](https://github.com/digitaldemocracy2030/kouchou-ai/issues/100)

**作成者:** ei-blue  
**作成日:** 2025-03-20T06:36:54Z  
**内容:**

# 背景
新規レポート作成画面において、現状ではCSVをアップロードした際にファイルアップロードエリアの下にファイル名が表示されるが、操作画面のサイズによってはスクロールしないと見えない位置にあり、ファイルがアップロードできたかどうかわかりにくい。

![Image](https://github.com/user-attachments/assets/35d419bb-4685-4124-bb71-34d59235281c)


# 提案内容

やり方はいろいろありそうなのでこだわらないです。以下はパッと思いついた例。

- 「ファイルがアップロードされました」というフラッシュメッセージを出す
- ファイルアップロードエリアの縦幅を小さくする
- アップロード成功時にファイルアップロードエリアの文言を変える

**コメント:** なし

---

### 過去30日間に作成されたissue (23件)

### [[FEATURE]設定画面について](https://github.com/digitaldemocracy2030/kouchou-ai/issues/227)

**作成者:** nishio  
**作成日:** 2025-04-03T13:37:38Z  
**内容:**

# 背景

![Image](https://github.com/user-attachments/assets/bb76f174-3347-4e73-aeed-823e8f4272d1)
最小クラスタは2以上。上が10でいいかは少し微妙で、2,5,10,25,50,100くらいの選択式がいいかもという気持ち
閉じるボタンが文章に被んている件、見出しと説明が横並びなのを縦並びにすると良いかも
「濃いグループの設定しかないので中に入れたらどうか」という話が以前悪化が、この設定によって濃いグループを選択できるかどうかが変わるのでそとにあるべき、将来的にはカラーバレットの設定などもここにはいるのかなと思う

<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

**コメント:** なし

---

### [[BUG] ２回目以降、静的ファイル出力（static build）時 パーミッションエラーが発生する？](https://github.com/digitaldemocracy2030/kouchou-ai/issues/225)

**作成者:** naoyo4  
**作成日:** 2025-04-03T00:12:34Z  
**内容:**

### 概要

<!-- バグの簡潔な説明をお願いします -->
静的ファイル出力（static build） を行う際、最初は問題なく出力ディレクトリーが作成されるが、再度実行するとパーミッションエラーが発生する？

### 再現手順

1. README の手順に則り（ make client-build-static ）、静的ファイル生成（ out ディレクトリ出力 ）
2. 再度同じことを行うとMakefile手順の最初（ rm -rf out ）でパーミッションエラーが発生
3. （ Webサーバーにも、FTP でUP時、パーミッションエラーが発生 ）

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->
２回目以降もパーミッションエラーが発生せず、処理できる。
（ WebサーバーにFTPでUPできる ）

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->
(base) nao@d500:~/kouchou-ai$ make client-build-static
rm -rf out
rm: 'out/images/broadlistening.png' を削除できません: 許可がありません
rm: 'out/404.html' を削除できません: 許可がありません
rm: 'out/_next/static/chunks/polyfills-42372ed130431b0a.js' を削除できません: 許可がありません
：
：

### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->
Issue 上げること自体ほぼ初めてで、内容自体も自信ありませんが、アドバイスだけでもいただければ幸いです。
http-server による動作等は、問題ないことは確認済み。

**コメント:** なし

---

### [[FEATURE]クライアント開発用のresultを公開](https://github.com/digitaldemocracy2030/kouchou-ai/issues/223)

**作成者:** nishio  
**作成日:** 2025-04-02T16:36:49Z  
**内容:**

# 背景
クライアント開発用にAI処理済みのresultをどこかからダウンロードして配置できるようにしておけばAPIキーに課金しなくてもUIの開発に参加できる
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
data/statusも変更しないといけないのが少し面倒

**コメント:** なし

---

### [[FEATURE]クラスタ数変更を直接入力可能にする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/222)

**作成者:** nishio  
**作成日:** 2025-04-02T16:27:55Z  
**内容:**

# 背景

<img width="302" alt="Image" src="https://github.com/user-attachments/assets/257a3fed-faab-4e86-ba90-8fd6c3126f42" />

データが8000件とかある場合、20 > 400 とかにしたくなるわけだけど、現状では350回のクリックが必要では

# 提案内容

クラスタ数変更を直接入力可能にする

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

**コメント:** なし

---

### [[FEATURE] frontからstaticなHTMLファイルをexportしてDownloadできるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/220)

**作成者:** takahiroanno  
**作成日:** 2025-04-02T11:43:27Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

**コメント:** なし

---

### [[FEATURE]client/client-adminのテストをgithub actionsで実行する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/219)

**作成者:** nasuka  
**作成日:** 2025-04-02T10:36:50Z  
**内容:**

# 背景
* 現状テストコードが存在せず、実装変更した際に不具合が起きる可能性が高い/検証に工数がかかる


# 提案内容
* github actionsで、clientのテストを行うように設定する
  * 現在はそもそもテストコードが存在しないので、テストが容易な関数等をピックアップしてテストコードも合わせて実装する
  * 参考: https://github.com/digitaldemocracy2030/kouchou-ai/pull/206

**コメント:** なし

---

### [[FEATURE]レポート一覧に作成日時を追加する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/218)

**作成者:** ei-blue  
**作成日:** 2025-04-02T03:55:52Z  
**内容:**

# 背景
現状、レポート一覧ではレポート名でしか区別がつけられないが、
- 同じ内容で複数回レポートを作成と区別がつかない
- 作成したレポートがいつ時点までのアップデートを反映したものかわからない

ため、レポート作成日時があると便利なのではと思いました。

# 提案内容
以下は一案です。

- レポート作成時にreport_status.jsonに日時を追加
- レポート一覧ページでタイトルの下に日時を表示


**コメント:** なし

---

### [[FEATURE]Azureへのデプロイ時に手元のレポートを含めることを可能にする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/216)

**作成者:** nishio  
**作成日:** 2025-04-01T09:09:59Z  
**内容:**

# 背景
ストレージ連携ができていない状況でもAzureデプロイの更新時にレポートが維持される


# 提案内容

by Devin
APIサーバをビルドする際にローカルの結果ファイルを含める方法を提案します。

1. server/Dockerfileを修正して、ビルド時にローカルの結果ファイルをコンテナにコピーします：

```
# 既存のDockerfileに追加
COPY ./broadlistening/pipeline/outputs /app/broadlistening/pipeline/outputs
COPY ./data/report_status.json /app/data/report_status.json
```

2. Makefileのazure-buildターゲットを修正して、ビルド前にローカルの結果ファイルを一時的にserverディレクトリにコピーします：

```
azure-build-with-reports:
	$(call read-env)
	@echo ">>> レポートファイルをビルドディレクトリにコピー..."
	@mkdir -p ./server/broadlistening/pipeline/outputs
	@mkdir -p ./server/data
	@cp -r ./server/broadlistening/pipeline/outputs/* ./server/broadlistening/pipeline/outputs/ || true
	@cp ./server/data/report_status.json ./server/data/ || true
	@echo ">>> APIイメージをビルド..."
	docker build --platform linux/amd64 -t $(AZURE_ACR_NAME).azurecr.io/api:latest ./server
	docker build --platform linux/amd64 -t $(AZURE_ACR_NAME).azurecr.io/client:latest ./client
	docker build --platform linux/amd64 --no-cache -t $(AZURE_ACR_NAME).azurecr.io/client-admin:latest ./client-admin
```

この方法で、APIサーバをビルドする際にローカルの結果ファイルを含めることができます。



**コメント:** なし

---

### [[FEATURE]Azureのデプロイ更新作業をMakefileにまとめる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/214)

**作成者:** nishio  
**作成日:** 2025-04-01T08:22:16Z  
**内容:**

# 背景
作業が複雑なため

## chat log
nishio
最新版でAzureにデプロイされているものを更新しようとしたのですが、色々トラブって結局できませんでした。 makeでazure-login azure-build azure-acr-login-auto azure-push make azure-config-update make azure-fix-client-adminまでやったのですが見た目が変わらなくて、何がいけなかったのかなぁと思っています。
truego
上記だと、clien-admin コンテナは新しいもので起動しますが、client と api のコンテナは古いまま（イメージは新しくなったけどコンテナは古いもので起動したまま）になりそうですね。 azure-fix-client-admin の処理の中の以下の部分（古いイメージのコンテナを停止して、新しく push されたイメージでコンテナを起動する）と同様のことを client, api コンテナでもやる必要がありそうな気がしました。
```
az containerapp update --name client-admin --resource-group $(AZURE_RESOURCE_GROUP) --min-replicas 0 && \ echo '>>> 再度スケールアップ...' && \ sleep 5 && \ az containerapp update --name client-admin --resource-group $(AZURE_RESOURCE_GROUP) --min-replicas 1"
```

nishio
apiサーバを再起動したらレポートが全部消えたので無事コンテナの更新ができたようです:爆笑: Spreadsheetを読む機能が増えてたのでソースコードの更新は成功、問題はレポートの復元だけ


# 提案内容
Makefileにターゲットとしてまとめる


**コメント:** なし

---

### [[FEATURE]5→50の表記を50→5に変えるか？](https://github.com/digitaldemocracy2030/kouchou-ai/issues/213)

**作成者:** nishio  
**作成日:** 2025-04-01T08:10:37Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
>NISHIO Hirokazu
5→50の表示、実際の流れとしては50に分けてから5つに集約してますよね。50→5では？という気がしてきました 
Nasuka Sumino
これは確かに仰るとおりですね。
50 -> 5に表示を変えたほうが処理の実態に合っていて良さそうに思いました...！
https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1743489984598769

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
5→50の表記を50→5に変える

**コメント:** なし

---

### [[BUG]新しいレポートを作成してもclient一覧画面にレポートが表示されない](https://github.com/digitaldemocracy2030/kouchou-ai/issues/212)

**作成者:** nasuka  
**作成日:** 2025-04-01T06:03:27Z  
**内容:**

### 概要
* 新しいレポートを作成してもclient一覧画面にレポートが表示されない
  * もともとclientは即時反映ではなく、ISRを採用しているため、表示まで最大5分の遅延がある認識
    * https://github.com/digitaldemocracy2030/kouchou-ai/issues/61
  * 一方で、試した限りでは5分経過しても一覧画面に新規のレポートが表示されない

### 再現手順

1. 新規にレポートを作成する
2. 5分以上経過した後に、clientの一覧画面にアクセスする
3. 一覧画面上に新規レポートが表示されない

他に参考になりそうな情報を以下に記載
* 一覧画面には表示されないがレポートの詳細画面にはアクセスすることはできる
* 再度clientをビルドした場合は一覧画面に新規レポートが表示される


### 期待する動作

レポート作成から、最大でも5分経過した段階ではclientの一覧画面に新規のレポートが表示される

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->

**コメント:** なし

---

### [[FEATURE]OOMの事後処理](https://github.com/digitaldemocracy2030/kouchou-ai/issues/211)

**作成者:** nishio  
**作成日:** 2025-04-01T06:00:12Z  
**内容:**

# 背景
エラー時にはレポート一覧にその旨が出るが、Out of Memoryで死んだ場合にはエラー内容を書き込む前に死ぬので「処理中」の表示が続いてしまう


# 提案内容
良い解決方法を考えたい

案
- pidをstatusにもつ
-  レポート一覧APIが呼ばれた時に、未完了のレポートについてプロセスが生きてるか確認して、死んでるならstatusをエラーに変える


**コメント:** なし

---

### [[FEATURE]レポート一覧のクリック可能範囲を広げる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/207)

**作成者:** nishio  
**作成日:** 2025-03-31T10:28:45Z  
**内容:**

# 背景

<img width="1023" alt="Image" src="https://github.com/user-attachments/assets/01686efb-d5a0-4679-b456-435ca5e978d2" />

レポートを見るためにクリックするところか説明のない灰色の領域だけ
目の前で使ってもらったらどこをクリックしたらいいか戸惑っていた

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

ブロック全体に広げた方がいいのではと思った

**コメント:** なし

---

### [[FEATURE]1回のextractionで複数のcommentを処理する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/190)

**作成者:** nasuka  
**作成日:** 2025-03-28T02:12:39Z  
**内容:**

# 背景
* 現在のextraction処理は1リクエストに1件のコメントを処理しているため、実行に時間がかかる
  * リクエストそのものの並列化は行われているが、OpenAI APIのrate limitの関係で並列化による高速化も限界がある


# 提案内容
* 1回のextractionで複数のコメントを同時に処理する
  * 同時処理の件数が増えることで、rate limit(requests per minute)の問題が緩和される

プロンプトのイメージ
```
あなたは専門的なリサーチアシスタントで、整理された議論のデータセットを作成するお手伝いをする役割です。
人工知能に関する公開協議を実施した状況を想定しています。一般市民から寄せられた議論の例を提示しますので、それらをより簡潔で読みやすい形に整理するお手伝いをお願いします。必要な場合は2つの別個の議論に分割することもできますが、多くの場合は1つの議論にまとめる方が望ましいでしょう。
結果は出力例に記載したjson形式で出力して

## 入力例
- id1: AIは仕事の効率化に役立つ。人生の相談相手にもなってくれる。
- id2: AIは電力を消費しすぎる問題がある
- id3: AIには反対です

## 出力例
{
    "id1": [
        "AIは仕事の効率化に役立つ",
        "AIは人生の相談相手になる"
    ],
    "id2": [
        "AIは電力消費が大きい"
    ],
    "id3": [
        "AIには反対"
    ]
}
```

extraction実行時のLLMのresponse formatが変わるため、周辺の実装も変える必要がある。

## 進め方
* まずは、上記のようなプロンプト・出力フォーマットに変更して同時処理数を増やした場合にどのようにアウトプットの文言が変わるかを確認する
  * 入力データは、ツイートレベルの長さのケースと、aipubcomのように1コメントが長いケースの両方で確かめた方が良さそう
* 抽出結果が問題なさそうであればプロダクトに機能実装する


**コメント:** なし

---

### [[FEATURE]CSVをJSONに変換せずに送信したい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/186)

**作成者:** ei-blue  
**作成日:** 2025-03-26T08:36:06Z  
**内容:**

# 背景

- 現在、コメントデータはフロントエンドでCSVファイルを読み込んだ後、JSONに変換し、comments 配列としてAPIに送信している。
- しかし、これはデータ量が多い場合に通信サイズやメモリ使用量が増える原因となり、効率的ではない。
- また、バックエンド側でも最終的にはCSV形式に戻して処理しているため、変換処理が冗長。

# 提案内容

- CSVファイルをフロントエンドからそのままAPIに送信できるように変更し、サーバー側で直接ファイルを受け取って処理できるようにする。
- これにより、クライアント側の前処理やメモリ消費を削減でき、処理効率が向上。

想定される実装方法：

- フロントエンドでは FormData を使ってCSVファイルを直接送信
- バックエンドでは UploadFileなどを使ってCSVファイルを受け取り、既存の inputs/xxx.csv に保存する

## 留意事項

- 現在フロントエンドで簡単なバリデーションを行っているが、これは最終的にはなくし、フロントエンドの処理を軽くする
- コメントIDの生成もフロントエンドで行っているのでそれも必要に応じてサーバーに移す
- スプレッドシートを入力として受け取る #132 の動きも気にしておく


**コメント:** なし

---

### [[FEATURE]失敗したプロセスの詳細情報を得られるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/185)

**作成者:** nishio  
**作成日:** 2025-03-26T07:34:45Z  
**内容:**

# 背景

NISHIO Hirokazu
うーん、「成功して完了したレポートの結果」をローカルにコピーできるようにはなったけど、デプロイしてる本番環境をユーザが使ってなんかコケたというときに、どんなデータを入れてどこまで進んでどんな死に方をしたのかを確認できないと捗らないな。本番環境のコンテナに直接入ったりサーバのログを見たりすればなんとかなるとはいえ、さっと手元に落として確認したい。やっぱりzipしてダウンロードするAPIをつけるべきか？？
2 件の返信

Nasuka Sumino
あっても良いと思います！
他にもいくつかアプローチはある気がしつつ（ステータスを細分化する、外部ストレージ連携してストレージを見に行く等）、データを丸ごと落とせるようにするのが実装的にも比較的ライトで原因究明もしやすいように思います。 

NISHIO Hirokazu
今回、aipubcomの現時点で公開されてる7つのPDFから過去最大のデータセットを作って入れてみたんですけど、たくさん時間が掛かってから死んだので雰囲気的にembeddingは完了してからクラスタリング時に何か起きたのかなぁみたいな気持ちです

https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1742971649061709

# 提案内容

<img width="319" alt="Image" src="https://github.com/user-attachments/assets/78faf532-a481-4dbb-8279-17fe42cf258d" />

管理画面の...ボタンで出るメニューに中間データなどをまとめたzipをダウンロードする機能をつける

**コメント:** なし

---

### [[BUG]パスワードに&があるとそこでコマンドが分割される](https://github.com/digitaldemocracy2030/kouchou-ai/issues/177)

**作成者:** nishio  
**作成日:** 2025-03-25T08:44:36Z  
**内容:**

### 概要
`ADMIN_API_KEY=foo&bar` のようなときに実行されるコマンドが `command --ADMIN_API_KEY=foo&bar`になって、それは`ADMIN_API_KEY=foo` と `bar`が`&`で繋がれたものと認識されてしまう

### 期待する動作

`command --ADMIN_API_KEY="foo&bar"`になる

### その他

まあ、記号を使わないだけで回避できるので緊急というわけではない、気づいたときに書かないと忘れるので...

**コメント:** なし

---

### [[FEATURE]LLMベースの分類機能の実装](https://github.com/digitaldemocracy2030/kouchou-ai/issues/176)

**作成者:** nasuka  
**作成日:** 2025-03-25T08:30:43Z  
**内容:**

# 背景
* 既存の階層クラスタリングアルゴリズムは以下の課題がある
  * ある程度データの件数が存在することを前提としている（小規模データだとワークしにくい）
  * embeddingに基づいてデータをまとめているため、クラスタリングの品質がembedding（およびUMAP後の2次元ベクトル）の品質に依存する


# 提案内容
LLMベースの分類機能を実装する。これは以下の2つの方向性がある。

1. 分類するトピックをLLMで自動で構築するパターン
  a. データから、どのようなトピックがあるかを自動で推定し、各意見をトピックに分類する
  b. 参考: [sensemaking](https://medium.com/jigsaw/making-sense-of-large-scale-online-conversations-b153340bda55)
2. 分類するトピックを人間が付与するパターン
  a. 意見を所与のトピックに分類する
  b. あらかじめ決められたトピックに意見を分類したい場合に活用できる

あった方が良い機能であるように思う一方で、既存のクラスタリングベースのアルゴリズムとこの機能をどう同居させるかが悩ましい。
既存のレポートは見せ方も異なってくると思われるので、別形式のページを出力するのが一案。

# 進め方について
* いきなり機能を実装するのではなく、プロダクトとは独立して実験スクリプトを実装し、検証用のデータセットを使って結果の妥当性を評価する
* 問題なければプロダクトの機能として実装を進める
  * 一旦実験系のIssueだけ立てておき、機能することがわかった段階でプロダクトへの実装イシューを立てる

**コメント:** なし

---

### [[DOCUMENT] Azure である程度の期間運用する際に必要な項目を追加する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/175)

**作成者:** shingo-ohki  
**作成日:** 2025-03-25T08:21:14Z  
**内容:**

# 現在の問題点
- 最初に構築するときのことしかケアできていない
- 何らかの理由(環境変数を更新した、新機能が使いたくてコードを更新した、ロゴを設定した、など)でコンテナを作り直すときにはまりどころがある

> フルでmakeしちゃうと新しいACRが作られちゃうのか？→.env.azure.generatedに書き出されたACR名を.env.azureに転記していなかったので毎回生成されていた
from https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1742889861058199?thread_ts=1742886821.947769&cid=C08F7JZPD63

> コンテナを再起動して生成済みレポートが消える
> ソースコードが更新されて新機能が追加されたらみんな新機能を使いたくて作り直しをすると思いますけど、それでレポートが全部消えてたら泣かれるかもw
> 分析して「よし静的HTMLを生成して公開しよう、そのためにはロゴを入れて更新」で分析結果が消える
from https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1742889178309719

# 提案内容

> 環境変数を変更したい時とか、ソースコードをupdateしたい時のためのマニュアルがあればいい

**コメント:** なし

---

### [[FEATURE] 生成するレポートを永続化できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/174)

**作成者:** shingo-ohki  
**作成日:** 2025-03-25T08:17:16Z  
**内容:**

# 背景
（特に Azure 環境では）コンテナをつくり直すとそれまでに生成したレポートが消えてしまう
https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1742889178309719

# 提案内容
例えば、
1. レポート生成時に永続化できるようにする（Azure のストレージサービスや Google drive など?） 

**コメント:** なし

---

### [[FEATURE]グラウンディングの実験](https://github.com/digitaldemocracy2030/kouchou-ai/issues/173)

**作成者:** nasuka  
**作成日:** 2025-03-25T08:10:43Z  
**内容:**

# 背景
https://github.com/digitaldemocracy2030/kouchou-ai/issues/172
* 上記のイシューに記載しているグラウンディングの実験を行う


# 実施内容
以下を実施する想定

* グラウンディング処理を行う実験スクリプトを実装
* 検証データに対してグラウンディングされたクラスタ説明文を出力
* 結果を確認し、問題なければプロダクトの機能として実装する
  * 確認のプロセスについては要検討

**コメント:** なし

---

### [[FEATURE]クラスタ説明文におけるグラウンディングの実装](https://github.com/digitaldemocracy2030/kouchou-ai/issues/172)

**作成者:** nasuka  
**作成日:** 2025-03-25T08:07:39Z  
**内容:**

# 背景
* クラスタの説明文では所属する意見の内容を解説しているが、本当にそのような意見が存在するのか確認するのに手間がかかる
* レポートの説得力を増す上で、説明の根拠となる元データを簡単に参照できるようにしたい


# 提案内容
* クラスタ説明文において、その根拠となるargumentを紐づけたテキストを表示する
  *  参考: https://medium.com/jigsaw/making-sense-of-large-scale-online-conversations-b153340bda55
    * Groundings
    * 紐づけ方・紐づけた文章の生成のさせ方は様々なアプローチがあるので、アプローチを検討する部分からassigneeの方にお任せする

# 進め方について
* いきなり機能を実装するのではなく、プロダクトとは独立して実験スクリプトを実装し、検証用のデータセットを使って結果の妥当性を評価する
  * 問題なければプロダクトの機能として実装を進める
  * 一旦実験系のIssueだけ立てておき、機能することがわかった段階でプロダクトへの実装イシューを立てる



**コメント:** なし

---

### 過去30日間に更新されたissue（作成・クローズを除く）(2件)

### [[FEATURE]レポートの複製・再利用機能](https://github.com/digitaldemocracy2030/kouchou-ai/issues/19)

**作成者:** nasuka  
**作成日:** 2025-03-04T11:38:39Z  
**内容:**

# 背景
* 設定を少しだけ変えて実行したいケースがある
  * 例えばクラスタ数だけ変えるなど


# 提案内容
* レポートの設定複製機能を実装する


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

### 過去30日間にマージされたPR (30件)

### [クラスタ見出しをanchorにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/224)

**作成者:** shgtkshruch  
**作成日:** 2025-04-02T23:22:45Z  
**変更:** +20 -3 (1ファイル)  
**マージ日:** 2025-04-03T00:13:54Z  
**内容:**

# 変更の概要
-  レポートの詳細ページのクラスターの見出しにリンクをつけました

https://github.com/user-attachments/assets/a885796d-6fd5-44f5-b70e-49efdce7ff99

# 変更の背景
- リンクの href, id 属性は、URL から意味が把握しやすいと思ったので見出しの日本語の文字列を設定しています
  - レポートの個別ページに同じ見出しのクラスターは出てこないことを前提にしているので、認識違いがあればコメントいただけると :pray:
- クリックできるとわかりやすいように hover 時にアイコンを表示しました

# 関連Issue
- fix: #112

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [レポート出力の進捗を表示](https://github.com/digitaldemocracy2030/kouchou-ai/pull/217)

**作成者:** 101ta28  
**作成日:** 2025-04-01T10:25:00Z  
**変更:** +298 -143 (3ファイル)  
**マージ日:** 2025-04-03T04:16:20Z  
**内容:**

close #13 

# 変更の概要
- レポート出力の進捗をダッシュボード上で把握できるようにするため

![output](https://github.com/user-attachments/assets/e09a651e-ae4d-4eee-a099-43671adbcc8b)

# 変更の背景
#13 

# 関連Issue
#13 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x]  CLAの内容を読み、同意しました

**コメント:** なし

---

### [不要なターゲット(azure-acr-login)を削除](https://github.com/digitaldemocracy2030/kouchou-ai/pull/210)

**作成者:** shingo-ohki  
**作成日:** 2025-03-31T13:34:32Z  
**変更:** +0 -7 (1ファイル)  
**マージ日:** 2025-03-31T13:56:28Z  
**内容:**

# 変更の概要
- Makaefile中の不要なターゲットが残っていたので削除しました

# 変更の背景
> Makefileのazure-acr-loginターゲットってACR名を置き換えてないから一般的には動かないし、どこからも呼ばれてないように思いますが盲腸ですかね？
https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1743423114579229

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [レポートページの OGP カードのデザイン](https://github.com/digitaldemocracy2030/kouchou-ai/pull/209)

**作成者:** shgtkshruch  
**作成日:** 2025-03-31T11:48:58Z  
**変更:** +350 -16 (13ファイル)  
**マージ日:** 2025-03-31T16:12:08Z  
**内容:**

# 変更の概要
- `app/[slug]/` 以下のページについて、OGP 画像を生成できるようにしました
  - 通常のビルド（`next build`） の場合は、リクエスト時に生成
  - static build（`NEXT_PUBLIC_OUTPUT_MODE=export next build`）の場合は、ビルド時に生成

## 生成される OGP 画像
### タイトルが短い場合
![image](https://github.com/user-attachments/assets/55db4e75-4442-4af7-9224-718b3ffadf9c)

### タイトルが長い場合

Footer に被らない範囲で表示して、はみ出た部分は切り取っています。

![image](https://github.com/user-attachments/assets/b70cab6b-6b70-4411-ad18-5c8bf09a0f10)

3点リーダー入れると親切かなと思ったのですが、OGP を生成する環境が特殊で使用できる CSS に制限があるのと、JavaScript で文字数を削るのも英数と日本語でレンダリングされる幅が異なるので、単純に文字数でも切れないなと思ったので、一旦はシンプルな実装にしています。
ref: https://nextjs.org/docs/app/api-reference/functions/image-response#supported-css-properties


## meta タグ
### 通常のビルドの場合
![image](https://github.com/user-attachments/assets/16d3aec0-8ad9-4e8f-b5b8-bf1d4c1e5fe8)


### static build の場合
![image](https://github.com/user-attachments/assets/9b3bcd42-b0ec-4a4c-b80e-df6b77ec004f)

# 変更の背景
- OGP 画像の生成方法
  - 通常のビルドの場合は、[`opengraph-image`](https://nextjs.org/docs/app/api-reference/file-conventions/metadata/opengraph-image) でリクエストごとに生成します
  - static build の場合は上記の方法が使えないため、こちらの方法で実装しました
    - https://github.com/vercel/next.js/issues/51147#issuecomment-1842197049
    - 調べたところ他に良さそうな方法がなかったので、他の方法があればコメントいただけると :pray:
- この構成でビルドした場合の課題点
  - static build 時に `opengraph-image.tsx` があるとビルド時にエラーになる
  - （上記のエラーを解消してビルドできた場合）通常のビルド・static build 両方の OGP 画像生成処理が走り、1つのページに対して2つの OGP 画像が生成される
- 対策として、通常のビルドと static build でビルド対象のファイルを分ける対応をいれました
  - App Router では `_` から始まる Private folder はルーティングから除外される
    - https://nextjs.org/docs/app/getting-started/project-structure#private-folders
  - この仕組みを使って通常のビルドの際は static build 用の OGP 生成ファイルを除外、static build 時は通常のビルド用の OGP 生成ファイル（`opengraph-image.tsx`）を除外する処理を挟むようにしました
- static build したアプリケーションを動作確認していて、ページリロード時に `http://localhost:3000/example` から `http://localhost:3000/example/` に遷移すると 404 になっていたので、static build の場合のみ `trailingSlash` の設定を有効にしました

# 関連Issue
- fix: https://github.com/digitaldemocracy2030/kouchou-ai/issues/140

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [fix assertion position](https://github.com/digitaldemocracy2030/kouchou-ai/pull/208)

**作成者:** nishio  
**作成日:** 2025-03-31T10:48:50Z  
**変更:** +20 -2 (1ファイル)  
**マージ日:** 2025-03-31T15:27:11Z  
**内容:**

# 変更の背景
Azureのchat extractionの中でenvが不完全であるときに、チェックしてAssertionErrorを投げていたが、上流でcatchしてAPI呼び出しのエラーとして扱っていた

# 変更の概要
そもそも環境変数の正しさを毎回のAPI呼び出し時にチェックする必要はない、もっと早い段階でチェックすべき

何が間違っているのかも分かりやすくなった
```
kouchou-ai-dev-api-1           |     assert os.getenv("AZURE_EMBEDDING_API_KEY")
kouchou-ai-dev-api-1           |            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [pytestを追加 & github actionsでテストを実行](https://github.com/digitaldemocracy2030/kouchou-ai/pull/206)

**作成者:** nasuka  
**作成日:** 2025-03-31T08:14:14Z  
**変更:** +171 -32 (21ファイル)  
**マージ日:** 2025-04-01T05:56:17Z  
**内容:**

# 変更の概要
* pytestのコードを追加
  * CIでpytestを実行することが目的なため、今回はテストしやすい関数を一つピックアップして実装
* github actions でpytestを実行するように設定
* （本筋ではないがapi側でlint errorが出ていたファイルをいくつか修正）

# 変更の背景
* 現状テスト/CIが整備されていないためにバグが発見しにくく、またレビュー/QAに時間がかかる

# 関連Issue
Close https://github.com/digitaldemocracy2030/kouchou-ai/issues/205

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [パブコメモードについての説明をREADMEに追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/204)

**作成者:** ei-blue  
**作成日:** 2025-03-31T00:47:48Z  
**変更:** +75 -67 (4ファイル)  
**マージ日:** 2025-03-31T06:25:45Z  
**内容:**

# 変更の概要
- パブコメモードについての説明をhow_to_useのREADMEに追加
- AI詳細設定の画像をパブコメモード設定入りのものに変更
- レポート作成画面も、スプレッドシート入りのものに変更
- ブロードリスニングディレクトリ内のREADMEにもパブコメモードについての記載を追加
- Lint自動修正

# 変更の背景
- #194 によりパブコメモードが追加されたため

# 関連Issue
#105 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [server内のREADMEを最新の内容にアップデート](https://github.com/digitaldemocracy2030/kouchou-ai/pull/203)

**作成者:** ei-blue  
**作成日:** 2025-03-30T22:41:24Z  
**変更:** +45 -5 (1ファイル)  
**マージ日:** 2025-03-31T00:39:13Z  
**内容:**

# 変更の概要
- server内のREADMEをアップデート

# 変更の背景
- 現在のREADMEに記載されている内容だとサーバーが起動しないため、正確な内容に修正
- 各エンドポイントのテスト方法、APIキーについての説明を追加

# 関連Issue
Closes #199 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [CONTRIBUTING.mdを改善](https://github.com/digitaldemocracy2030/kouchou-ai/pull/202)

**作成者:** nasuka  
**作成日:** 2025-03-30T15:03:34Z  
**変更:** +69 -15 (2ファイル)  
**マージ日:** 2025-03-30T15:54:23Z  
**内容:**

# 変更の概要
* CONTRIBUTING.mdを改善
  * 👍 の件数が優先度を検討する上で参考にされる旨を記載
  * 「コードの貢献プロセス」を明文化
    * 大きな変更の場合は事前にイシューでコードオーナーのリアクションを待ってもらう
  * など
* READMEにバグ報告・改善要望のGoogle Formリンクを追記

CONTRIBUTING.mdについては、streamlitのコントリビューションガイドが良さそうだったのでそちらを参考に修正しています。
https://github.com/streamlit/streamlit/wiki/Contributing

# 変更の背景
* README/CONTRIBUTINGについて、最新の状況を反映できていない部分があった

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/201

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [階層図ホバー時にクラスタの概要説明を表示](https://github.com/digitaldemocracy2030/kouchou-ai/pull/200)

**作成者:** shgtkshruch  
**作成日:** 2025-03-30T06:47:03Z  
**変更:** +6 -1 (1ファイル)  
**マージ日:** 2025-03-30T15:54:53Z  
**内容:**

# 変更の概要
- 階層図にホバー時に表示される Tooltip にクラスタの概要（takeaway）を表示するようにしました
![image](https://github.com/user-attachments/assets/19d49dd4-3b7c-4f13-8e5f-db9960712f3f)

# 変更の背景
- issue 上では元々表示していた件数や割合は削除した方が見やすいという意見があったので、その方向で実装しました
> ツールチップには件数/割合があるとごちゃごちゃしている印象を抱いたので、個人的に件数/割合は省いた方が見やすいと感じました
> ref: https://github.com/digitaldemocracy2030/kouchou-ai/issues/14#issuecomment-2745205016
# 関連Issue
- fix: https://github.com/digitaldemocracy2030/kouchou-ai/issues/14
# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [static build の手順のドキュメントを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/198)

**作成者:** shgtkshruch  
**作成日:** 2025-03-29T11:24:44Z  
**変更:** +19 -7 (3ファイル)  
**マージ日:** 2025-03-29T13:07:52Z  
**内容:**

# 変更の概要
- static build について README にドキュメントを追加しました
- static build を Docker 内で完結することで、Node.js がホスト環境になくても build できるようにしました
- こちらで static build 関連の PR は一旦完了の認識です

# 変更の背景
- 以下の PR で static build が動作するようになったので、利用者向けの手順をまとめました
   - https://github.com/digitaldemocracy2030/kouchou-ai/pull/195
   - https://github.com/digitaldemocracy2030/kouchou-ai/pull/197

# 関連Issue
- fix: https://github.com/digitaldemocracy2030/kouchou-ai/issues/53

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [static build 時に画像が 404 になる不具合の解消](https://github.com/digitaldemocracy2030/kouchou-ai/pull/197)

**作成者:** shgtkshruch  
**作成日:** 2025-03-29T00:47:26Z  
**変更:** +66 -7 (7ファイル)  
**マージ日:** 2025-03-29T09:55:37Z  
**内容:**

# 変更の概要
- static build した際に server (API) から取得する画像が 404 になる課題を解決しました

## Before
![image](https://github.com/user-attachments/assets/796dcabc-f090-4da3-9cb9-8f69b1d74d34)


## After
![image](https://github.com/user-attachments/assets/4196b10e-7c35-4a88-89ab-58f6096c20ed)


# 変更の背景
- server でホストしている public/meta 以下の画像を client の public ディレクトリにコピーする script を追加
  - この辺りの画像が 404 になっていたので、これらのファイルをコピーする処理を追加しました
  https://github.com/digitaldemocracy2030/kouchou-ai/blob/7429106a54de66f6c541807e8bc6d4842f08a55c/README.md?plain=1#L37-L46
  - 画像を表示するコンポーネントが Server Component であれば Component 内でファイルをコピーする処理が書けるかもと思ったのですが、今回は Client Component 内で画像を表示していたので scirpt で解決する方法を取りました
  - static build のコマンド実行前に、上記コマンドを実行
- server から取得した画像のパスを切り替える関数を utils を追加 

# 関連Issue
- fix: https://github.com/digitaldemocracy2030/kouchou-ai/issues/196

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [client を static build できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/195)

**作成者:** shgtkshruch  
**作成日:** 2025-03-28T09:06:20Z  
**変更:** +271 -69 (8ファイル)  
**マージ日:** 2025-03-28T15:42:08Z  
**内容:**

# 変更の概要
- client アプリケーションを static build できるようにしました
  - `out/` に生成されるビルド成果物を Web サーバーでホストすることで、トップページやレポートページを表示することが可能
  - static build 用のコマンドを追加しました（Makefile, client/package.json）
  - static build したアプリケーションのローカルでの動作確認用に [http-server](https://www.npmjs.com/package/http-server) を devDependencies に追加しました

# やっていないこと
- static build 後に server (API) から配信しているロゴなどの画像が 404 になる課題の解決
  - static build した場合は、client のみで動かす必要があるので、何らかの方法で server でホストしている画像を client のビルド成果物に含める必要がある認識
  - 差分が大きくなりそうなので、別の PR に分けて対応予定です

![image](https://github.com/user-attachments/assets/45ed3608-ea94-4cf9-aeca-bbc08cd44f2b)

- static build の手順のドキュメンテーション
  - 実装が揃って動くことが確認でき次第、README などに手順を追加する PR を作成予定です

# 変更の背景
- report のデータ取得を `<ClientContainer>` 内の fetch から props で渡す形に変更しました https://github.com/digitaldemocracy2030/kouchou-ai/commit/f535425187de6b0c94efc0cae9449508da821d94
   https://github.com/digitaldemocracy2030/kouchou-ai/blob/d48b281afb70b832daa845ee1cd9e651b62c2041/client/components/report/ClientContainer.tsx#L52-L81
  - こちらがあると static build した後もクライアントからサーバーに問い合わせが発生するため
  - client で fetch する方法（現状の実装）
    - pros:
      - 重いデータの report に依存する処理をクライアントで実施することで DOMContentLoaded が早い
      - データ取得中もローディングが表示されるので、ユーザーに早く UI を返せる
    - cons:
      - クライアントで report のデータを fetch が終わるまでグラフが表示されない（ローディング表示になる）
      - サーバー・クライアントそれぞれで report のデータ fetch が実行される
        - revalidate が設定されているのでサーバーでは毎回実行されるわけでないですが、時間が来ると再度実行される認識です
  - props で渡す方法（この PR の実装）
    - pros:
      - データの取得がサーバーで完結するので、static build したらクライアントだけで動く
      - サーバーで report に依存したレンダリングが終わるので、グラフも含めてページ全体が完成する時間を短縮できる
    - cons:
      - HTML が大きくなるので、DOMContentLoaded が遅い

## レンダリング速度の比較

データの取得方法を変更したことで、どのくらい速度やレンダリングに影響があるか計測しました。
client fetch / props それぞれの実装について、npm run build && npm run start を実行して、ブラウザで表示確認しました。

**計測条件**
- Google Chrome（バージョン: 134.0.6998.118, Official Build, arm64）
- シークレットモード
- Network Cache を無効化
- Network Speed を Fast 4G に設定

| | DOMContentLoaded | Loaded | Finish |
|--------|--------|--------|--------|
| client fetch | 379ms | 985ms | 6.24s |
| props | 1.37s | 1.37s | 2.76s | 

client で fetch する方法は、DOMContentLoaded が早いですが、グラフが表示されるまでに 6.24s かかっています。
props で渡す方法は、HTML サイズが大きくなるので DOMContentLoaded が遅いですが、グラフが表示されるのは 2.76s です。

### client fetch

https://github.com/user-attachments/assets/a7068da0-9abd-4886-b68d-adc2d3fafa9a

### props

https://github.com/user-attachments/assets/a10dfd7b-a6af-4478-8e35-8a6bb2069a94

## 結論
client fetch・props どちらも pros / cons あるのですが、以下の点を考慮してこの PR では  props で渡す方法で実装しました。

- データの取得がサーバーで完結するので、static build しても動作する
- ユーザーにグラフを表示するまでの時間が短くなることでページ全体の情報を表示する時間が短縮されているので、トータルで見ると UX が良さそう

（この実装方針は個人的な意見をベースにしていて、優先順位の考え方が違ったり認識違いがあるかもしれないので、その場合はコメントいただけると嬉しいです :pray: ）


# 関連Issue
- https://github.com/digitaldemocracy2030/kouchou-ai/issues/53

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [パブコメモード（CSV形式出力・CSVにコメント原文を追加）](https://github.com/digitaldemocracy2030/kouchou-ai/pull/194)

**作成者:** ei-blue  
**作成日:** 2025-03-28T08:47:45Z  
**変更:** +399 -135 (23ファイル)  
**マージ日:** 2025-03-30T15:55:42Z  
**内容:**

# 変更の概要
- レポート作成画面に「パブコメモード」ボタンを追加。これを選択すると、元コメントつきのCSVファイルが作成され、レポート完成後の詳細画面からダウンロードができます。
- 最終的な一つのコメントから複数の議論が抽出されている場合、元コメントが複数の行に表示されます。
- 似たようなコメントが複数あって一つの議論が抽出されている場合は、元コメントが維持され、議論が複数の行に表示されます。
（mergeはhierarchical_aggregation.py内で実行しているので、特にここのロジックをチェックしてもらえると嬉しいです。）
- イシューと関係なく、フォーマットでWarningが出たのでnpx eslint . --fixを実行したら大量のファイルが修正されました。
- スプレッドシート対応はまだ試していませんが、サーバーサイドのロジックが同じなら問題ないはず。

<img width="1001" alt="Screenshot 2025-03-28 at 01 27 09" src="https://github.com/user-attachments/assets/a8897692-5535-447f-b0c7-134e955bad5c" />

<img width="1075" alt="Screenshot 2025-03-28 at 01 25 49" src="https://github.com/user-attachments/assets/2ad9d7be-1281-4bd4-8205-2ccb834cc694" />
<img width="1254" alt="Screenshot 2025-03-28 at 01 40 20" src="https://github.com/user-attachments/assets/57bfba14-516b-4197-8841-4d524580bca0" />

# 今後
以下のような可能性があるかなと思って、イシューをCloseにはしていません。
- パブコメモードの際はデフォルトのプロンプトをパブコメ用にしたい。ガワだけ作っていますが、今の段階でプロンプトを二種類作ると同期がめんどくさそうだなと思ってアクティブにはしていません。
- パブコメモードじゃない場合でも原文を見れるといいかもしれない

# 変更の背景
- 行政のユースケースの一つとして考えられるパブリックコメント対応においては、既存の公開形式に近いCSVファイルのニーズがある
- 元意見を提示することはアカウンタビリティの面からも重要

# 関連Issue
#105 #56 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [文言の変更（「議論」-> 「意見」、〇〇議論 -> 〇〇件）](https://github.com/digitaldemocracy2030/kouchou-ai/pull/193)

**作成者:** shingo-ohki  
**作成日:** 2025-03-28T07:07:58Z  
**変更:** +13 -13 (3ファイル)  
**マージ日:** 2025-03-28T07:19:59Z  
**内容:**

# 変更の概要
- クラスタタイトル下の「33議論」等の表現は「33件」という表現に変える
- Analysis内で使われている「議論」という単語は 「意見」に置き換える

## スクリーンショット
![Screenshot from 2025-03-28 15-57-22](https://github.com/user-attachments/assets/c6ec7fa2-d42e-41f6-8ece-0726b431da36)

# 関連Issue
#118 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [環境変数を編集した場合の起動手順を追記](https://github.com/digitaldemocracy2030/kouchou-ai/pull/192)

**作成者:** nasuka  
**作成日:** 2025-03-28T06:34:46Z  
**変更:** +8 -6 (2ファイル)  
**マージ日:** 2025-03-28T07:27:10Z  
**内容:**

# 変更の概要
* 環境変数を編集した場合の起動手順を追記
* compose.ymlのargsをハードコードした値ではなく、.envか読み込んだ環境変数で定義
  * 一部の環境変数がcompose.ymlのargsと二重で定義されており、compose.yml側にハードコードされた値が使われるようになっていたので、.envの環境変数を使うように修正
    * デフォルトでは.env内の環境変数がcomposeのファイル内で展開できる
      * 参考: https://docs.docker.jp/compose/environment-variables.html

# 変更の背景
* 環境変数を変更した場合はdocker imageをbuildしなおさないと動作しないケースがある
  * フロントでは、APIキーなどの一部の環境変数をimageのビルド時に埋め込んでいる
  * このため、フロント側はdocker compose upを実行すると初回に設定した環境変数のイメージのままコンテナが立て続けられてしまう（ビルド時に埋め込んでいる環境変数は、イメージをビルドし直さない限り.envを編集しても変更が反映されない）
    * これによりapiとフロントのAPIキーが一致しないケースが発生してしまう

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/191

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [サンプルのコメントデータのサンプルを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/189)

**作成者:** nasuka  
**作成日:** 2025-03-26T12:36:47Z  
**変更:** +400 -50 (1ファイル)  
**マージ日:** 2025-03-26T14:10:40Z  
**内容:**

# 変更の概要
* sample_comments.csvのコメントサンプルを50->400件に増加

# 変更の背景
* デフォルトの設定だと2層目のクラスタがまともに形成されなかった（50件のコメント -> 50件のクラスタとなる）ため、件数を追加した
  * 200件程度だと濃いクラスタのビューで2クラスタしか表示されなかったため、サンプルを400件まで増加

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/120

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [/を分数に見えなくするために→に変えた](https://github.com/digitaldemocracy2030/kouchou-ai/pull/188)

**作成者:** takahiroanno  
**作成日:** 2025-03-26T11:55:13Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-03-26T11:55:54Z  
**内容:**

# 変更の概要
- ここに変更の概要を記載してください

# 変更の背景
- ここに変更が必要となった背景を記載してください

# 関連Issue
関連するIssueのリンクをこちらに記載してください

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました

**コメント:** なし

---

### [「データをクリアして再入力」を押した時に、既に保存したデータがあれば削除](https://github.com/digitaldemocracy2030/kouchou-ai/pull/187)

**作成者:** shingo-ohki  
**作成日:** 2025-03-26T09:54:04Z  
**変更:** +133 -8 (4ファイル)  
**マージ日:** 2025-03-26T12:20:28Z  
**内容:**

# 変更の概要
- 「データをクリアして再入力」を押した時に、既に保存したデータがあれば削除するようにしました

# 変更の背景
- 現状では[不要なデータが残ってしまうことがある](https://github.com/digitaldemocracy2030/kouchou-ai/pull/182#discussion_r2013473586)

# 関連Issue
#184 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Shift JISのcsvがアップロードされた時にUTF-8に変更する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/183)

**作成者:** yuneko1127  
**作成日:** 2025-03-25T21:00:45Z  
**変更:** +64 -15 (3ファイル)  
**マージ日:** 2025-03-26T02:04:06Z  
**内容:**

# 変更の概要
Shift JISのcsvがアップロードされた時にUTF-8に変更する。
そのために、client-adminのparseCsv.tsに文字コードを変更する処理を記述した。

# 変更の背景
ExcelなどでCSVを作成するとShift-JISになり、非エンジニアの利用を考えるのであれば、文字コードの変換は利用者側ではなくシステム側でやるべきだと考えるから。

# 関連Issue
#124

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [公開設定された Google スプレッドシートを意見データとして扱えるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/182)

**作成者:** shingo-ohki  
**作成日:** 2025-03-25T14:52:38Z  
**変更:** +493 -71 (7ファイル)  
**マージ日:** 2025-03-26T06:31:39Z  
**内容:**

# 変更の概要
- 公開設定された Google スプレッドシートのURLを入力するフォームを追加
- 入力データ（CSVファイルアップロード/Google スプレッドシート）をタブで切り替えられるようにする

![Screenshot from 2025-03-25 23-51-37](https://github.com/user-attachments/assets/1d9acdec-b5eb-4f7a-b6e7-4dd78106d702)

# 変更の背景
以下のIssueのうち、まずはこちらを対応します。
- 公開のSpreadsheetを読む
 
# 関連Issue
#132 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Azure.mdにサンプル構成の注意事項を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/181)

**作成者:** nasuka  
**作成日:** 2025-03-25T14:39:30Z  
**変更:** +5 -0 (1ファイル)  
**マージ日:** 2025-03-25T14:44:58Z  
**内容:**

# 変更の概要
* サンプル構成でデプロイした場合、コンテナを停止するとレポートが消失する旨を追記

# 変更の背景
* 現状の構成に関する制限事項が記載できていなかった
  * 参考: https://github.com/digitaldemocracy2030/kouchou-ai/issues/175
  * 上記issueの他の内容は追って修正でも良いが、サンプル構成でレポートが消失する旨はトラブルに繋がりかねないので先行して追記

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/175

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [resultをローカル環境へ取得するscriptをつくる](https://github.com/digitaldemocracy2030/kouchou-ai/pull/180)

**作成者:** nishio  
**作成日:** 2025-03-25T13:45:11Z  
**変更:** +247 -0 (1ファイル)  
**マージ日:** 2025-03-25T15:17:59Z  
**内容:**

# 変更の概要
- [FEATURE]resultをローカル環境へ取得するscriptをつくる · Issue #179 
- リモートのAPIサーバURLを指定すると
  - GET /reports を叩いて全レポートのslugを取得する
  - GET /reports/{slug}を叩いて個別のレポートのresultを取得する
  - ローカル環境に適切に配置し、server/data/report_status.jsonを更新する

# 変更の背景
- 現状リモート環境で作成されたレポートを手元に取得したりバックアップしたりする手軽な手段がなく、再起動の際に成果が失われてしまうため

# 関連Issue
#179

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [リポートがない場合は 404 を返すように修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/178)

**作成者:** shgtkshruch  
**作成日:** 2025-03-25T10:34:24Z  
**変更:** +80 -62 (8ファイル)  
**マージ日:** 2025-03-25T11:16:25Z  
**内容:**

# 変更の概要
- リポートの個別ページで server が 404 を返した場合、Next.js 標準の [`notFound`](https://nextjs.org/docs/app/api-reference/functions/not-found) を使用して 404 を返すように修正しました
  - 404 用に`not-found.tsx`, エラー用に `error.tsx` を追加しました
  - 手元の環境で `next dev` と `make up` で動作することは確認しました
  - こちらの対応と合わせて既存のコードを修正しています（後述）

## Before
![image](https://github.com/user-attachments/assets/39f02b57-c6f3-409a-9a7c-77ae7d8ef22d)


## After
### 404 時 (`not-found.tsx`）
![image](https://github.com/user-attachments/assets/fc003abd-3e02-4924-8ab6-66e7ac4e4f6a)

### エラー時（`error.tsx`）
![image](https://github.com/user-attachments/assets/8a1980f7-4aa6-4aa1-82c6-bac3a5f7f755)


# 変更の背景

- Chakra UI を hydration error を回避するための `<ClientProvider>` コンポーネントを削除しました
  - `ssr: false` が設定されており、こちらがあると `notFound` API を使用しても 200 が返り 404 が返らなかったため
  - Chakra UI の公式では `next dev` の `--turbo` オプションを使わない対応を推奨しているようでした
    - issue: https://github.com/chakra-ui/chakra-ui/issues/9811#issuecomment-2729845766
    - 公式ドキュメント: https://chakra-ui.com/docs/get-started/frameworks/next-app#hydration-errors
    - 修正前のコマンドは `next dev --turbopack` ですが、`--turbopack`, `--turbo` 共に内部的に Turbopack 利用していて、Turbopack と現行の Chakra UI の相性が良くなさそうなので、このオプションを外すことで hydration error を回避する対応をしました
- 画像を参照するコンポーネントの `src` を client 側で参照できるパスに修正しました
  - `ssr: false` を外した影響で画像のパスが client から参照できなくなっていたため
  - 画像の取得は client（ブラウザ）から行われると思うので、client から参照できるパスを指定しました

# 関連Issue
- fix: #69

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [dependabotの定期更新を削除](https://github.com/digitaldemocracy2030/kouchou-ai/pull/171)

**作成者:** nasuka  
**作成日:** 2025-03-25T07:41:16Z  
**変更:** +0 -49 (1ファイル)  
**マージ日:** 2025-03-25T07:42:48Z  
**内容:**

# 変更の概要
- dependabotの設定ファイルを削除

# 変更の背景
- セキュリティアラートに関するPR作成はgithub上で設定できたため、こちらは削除
  - できればセキュリティアラート以外のアップデートも対応したいが、動作検証に時間がかかるため当面は必要に応じて手動でアップデートする

# 関連Issue
関連するIssueのリンクをこちらに記載してください

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Bump @types/react from 19.0.10 to 19.0.12 in /client](https://github.com/digitaldemocracy2030/kouchou-ai/pull/167)

**作成者:** dependabot[bot]  
**作成日:** 2025-03-25T06:13:58Z  
**変更:** +3 -3 (1ファイル)  
**マージ日:** 2025-03-25T07:29:14Z  
**内容:**

Bumps [@types/react](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/HEAD/types/react) from 19.0.10 to 19.0.12.
<details>
<summary>Commits</summary>
<ul>
<li>See full diff in <a href="https://github.com/DefinitelyTyped/DefinitelyTyped/commits/HEAD/types/react">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=@types/react&package-manager=npm_and_yarn&previous-version=19.0.10&new-version=19.0.12)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating it. You can achieve the same result by closing it manually
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)


</details>

**コメント:** なし

---

### [Bump @eslint/eslintrc from 3.3.0 to 3.3.1 in /client-admin](https://github.com/digitaldemocracy2030/kouchou-ai/pull/165)

**作成者:** dependabot[bot]  
**作成日:** 2025-03-25T06:13:50Z  
**変更:** +4 -3 (1ファイル)  
**マージ日:** 2025-03-25T07:30:43Z  
**内容:**

Bumps [@eslint/eslintrc](https://github.com/eslint/eslintrc) from 3.3.0 to 3.3.1.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/eslint/eslintrc/releases"><code>@​eslint/eslintrc</code>'s releases</a>.</em></p>
<blockquote>
<h2>v3.3.1</h2>
<h2><a href="https://github.com/eslint/eslintrc/compare/v3.3.0...v3.3.1">3.3.1</a> (2025-03-11)</h2>
<h3>Bug Fixes</h3>
<ul>
<li>correct <code>types</code> field in package.json (<a href="https://redirect.github.com/eslint/eslintrc/issues/184">#184</a>) (<a href="https://github.com/eslint/eslintrc/commit/2f4cf3fe36ee0df93c1c53f32c030c58db1816a2">2f4cf3f</a>)</li>
</ul>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/eslint/eslintrc/blob/main/CHANGELOG.md"><code>@​eslint/eslintrc</code>'s changelog</a>.</em></p>
<blockquote>
<h2><a href="https://github.com/eslint/eslintrc/compare/v3.3.0...v3.3.1">3.3.1</a> (2025-03-11)</h2>
<h3>Bug Fixes</h3>
<ul>
<li>correct <code>types</code> field in package.json (<a href="https://redirect.github.com/eslint/eslintrc/issues/184">#184</a>) (<a href="https://github.com/eslint/eslintrc/commit/2f4cf3fe36ee0df93c1c53f32c030c58db1816a2">2f4cf3f</a>)</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/eslint/eslintrc/commit/556e80029f01d07758ab1f5801bc9421bca4b072"><code>556e800</code></a> chore: release 3.3.1 (<a href="https://redirect.github.com/eslint/eslintrc/issues/185">#185</a>)</li>
<li><a href="https://github.com/eslint/eslintrc/commit/a34f97e9fb940fdac653cd90f63c2b7a8e4604f8"><code>a34f97e</code></a> docs: update readme to include bun install (<a href="https://redirect.github.com/eslint/eslintrc/issues/182">#182</a>)</li>
<li><a href="https://github.com/eslint/eslintrc/commit/2f4cf3fe36ee0df93c1c53f32c030c58db1816a2"><code>2f4cf3f</code></a> fix: correct <code>types</code> field in package.json (<a href="https://redirect.github.com/eslint/eslintrc/issues/184">#184</a>)</li>
<li>See full diff in <a href="https://github.com/eslint/eslintrc/compare/v3.3.0...v3.3.1">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=@eslint/eslintrc&package-manager=npm_and_yarn&previous-version=3.3.0&new-version=3.3.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating it. You can achieve the same result by closing it manually
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)


</details>

**コメント:** なし

---

### [Bump next from 15.1.6 to 15.2.3 in /client-admin](https://github.com/digitaldemocracy2030/kouchou-ai/pull/153)

**作成者:** dependabot[bot]  
**作成日:** 2025-03-25T06:10:50Z  
**変更:** +51 -41 (2ファイル)  
**マージ日:** 2025-03-25T06:12:00Z  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 15.1.6 to 15.2.3.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v15.2.3</h2>
<blockquote>
<p>[!NOTE]<br />
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.
This release contains a security patch for <a href="https://github.com/vercel/next.js/security/advisories/GHSA-f82v-jwr5-mffw">CVE-2025-29927</a>.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>Update default allowed origins list (<a href="https://redirect.github.com/vercel/next.js/issues/77212">#77212</a>)</li>
<li>unify allowed origin detection handling (<a href="https://redirect.github.com/vercel/next.js/issues/77053">#77053</a>)</li>
<li>Add dev warning for cross-origin and stabilize allowedDevOrigins (<a href="https://redirect.github.com/vercel/next.js/issues/77044">#77044</a>)</li>
<li>Ensure deploymentId is used for CSS preloads (<a href="https://redirect.github.com/vercel/next.js/issues/77210">#77210</a>)</li>
<li>Update middleware request header (<a href="https://redirect.github.com/vercel/next.js/issues/77201">#77201</a>)</li>
<li>[metadata] remove the default segement check for metadata rendering (<a href="https://redirect.github.com/vercel/next.js/issues/77119">#77119</a>)</li>
<li>[ts-hint] fix vscode type hint plugin enabling (<a href="https://redirect.github.com/vercel/next.js/issues/77099">#77099</a>)</li>
<li>[metadata] re-insert icons to head for streamed metadata (<a href="https://redirect.github.com/vercel/next.js/issues/76915">#76915</a>)</li>
</ul>
<h3>Credits</h3>
<p>Huge thanks to <a href="https://github.com/ijjk"><code>@​ijjk</code></a>, <a href="https://github.com/ztanner"><code>@​ztanner</code></a>, and <a href="https://github.com/huozhi"><code>@​huozhi</code></a> for helping!</p>
<h2>v15.2.2</h2>
<h3>Core Changes</h3>
<ul>
<li>[dev-overlay] fix styling on overflow error messages, add button hover state: <a href="https://redirect.github.com/vercel/next.js/issues/76771">#76771</a></li>
<li>Fix: respond 405 status code on OPTIONS request to SSG page: <a href="https://redirect.github.com/vercel/next.js/issues/76767">#76767</a></li>
<li>[dev-overlay] Always show relative paths: <a href="https://redirect.github.com/vercel/next.js/issues/76742">#76742</a></li>
<li>[metadata] remove the duplicate metadata in the error boundary: <a href="https://redirect.github.com/vercel/next.js/issues/76791">#76791</a></li>
<li>Upgrade React from <code>d55cc79b-20250228</code> to <code>443b7ff2-20250303</code>: <a href="https://redirect.github.com/vercel/next.js/issues/76804">#76804</a></li>
<li>[dev-overlay] Ignore animations on page load: <a href="https://redirect.github.com/vercel/next.js/issues/76834">#76834</a></li>
<li>fix: remove useless set-cookie in action-handler: <a href="https://redirect.github.com/vercel/next.js/issues/76839">#76839</a></li>
<li>Turbopack: handle task cancelation: <a href="https://redirect.github.com/vercel/next.js/issues/76831">#76831</a></li>
<li>Upgrade React from <code>443b7ff2-20250303</code> to <code>e03ac20f-20250305</code>: <a href="https://redirect.github.com/vercel/next.js/issues/76842">#76842</a></li>
<li>add types for <code>__next_app__</code> module loading functions: <a href="https://redirect.github.com/vercel/next.js/issues/74566">#74566</a></li>
<li>fix duplicated noindex when server action is triggered: <a href="https://redirect.github.com/vercel/next.js/issues/76847">#76847</a></li>
<li>fix: don't drop queued actions when navigating: <a href="https://redirect.github.com/vercel/next.js/issues/75362">#75362</a></li>
<li>[dev-overlay]: remove dependency on platform for focus trapping: <a href="https://redirect.github.com/vercel/next.js/issues/76849">#76849</a></li>
<li>Turbopack: Add <strong>turbopack_load_by_url</strong>: <a href="https://redirect.github.com/vercel/next.js/issues/76814">#76814</a></li>
<li>Add handling of origin in dev mode: <a href="https://redirect.github.com/vercel/next.js/issues/76880">#76880</a></li>
<li>[dev-overlay] Stop grouping callstack frames into ignored vs. not ignored: <a href="https://redirect.github.com/vercel/next.js/issues/76861">#76861</a></li>
<li>Upgrade React from <code>e03ac20f-20250305</code> to <code>029e8bd6-20250306</code>: <a href="https://redirect.github.com/vercel/next.js/issues/76870">#76870</a></li>
<li>[dev-overlay] Increase padding if no <code>x</code> button present: <a href="https://redirect.github.com/vercel/next.js/issues/76898">#76898</a></li>
<li>fix: prevent incorrect searchParams being applied on certain navs: <a href="https://redirect.github.com/vercel/next.js/issues/76914">#76914</a></li>
<li>[dev-overlay] Dim ignore-listed callstack frames when shown: <a href="https://redirect.github.com/vercel/next.js/issues/76862">#76862</a></li>
</ul>
<h3>Example Changes</h3>
<ul>
<li>chore(cna): update tailwind styles to be closer to non-tw cna: <a href="https://redirect.github.com/vercel/next.js/issues/76647">#76647</a></li>
</ul>
<h3>Misc Changes</h3>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/535e26d3c69de49df8bd17618a424cbe65ec897b"><code>535e26d</code></a> v15.2.3</li>
<li><a href="https://github.com/vercel/next.js/commit/2fcae1d7e3079874ff633b5b8311adb584c80ce6"><code>2fcae1d</code></a> Update default allowed origins list (<a href="https://redirect.github.com/vercel/next.js/issues/77212">#77212</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/adf5462b5f269963395b0a2ef12a1b66e8cadabc"><code>adf5462</code></a> unify allowed origin detection handling (<a href="https://redirect.github.com/vercel/next.js/issues/77053">#77053</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/5e59da1f5c8b9e8b3a759048bd371efcd77813ae"><code>5e59da1</code></a> Add dev warning for cross-origin and stabilize allowedDevOrigins (<a href="https://redirect.github.com/vercel/next.js/issues/77044">#77044</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/8151cb6ce921cb1b9faeab6fb88551146dc206b7"><code>8151cb6</code></a> Ensure deploymentId is used for CSS preloads (<a href="https://redirect.github.com/vercel/next.js/issues/77210">#77210</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/52a078da3884efe6501613c7834a3d02a91676d2"><code>52a078d</code></a> Update middleware request header (<a href="https://redirect.github.com/vercel/next.js/issues/77201">#77201</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/4698ad6478cc85a7283a8c41edfbba023dadf57d"><code>4698ad6</code></a> [metadata] remove the default segement check for metadata rendering (<a href="https://redirect.github.com/vercel/next.js/issues/77119">#77119</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/1e1ff403a28703b08e68758cfcbb7b6c97c4bd2a"><code>1e1ff40</code></a> [ts-hint] fix vscode type hint plugin enabling (<a href="https://redirect.github.com/vercel/next.js/issues/77099">#77099</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/88deb12b03c90f5146b1270cd7bea3517cf90083"><code>88deb12</code></a> [metadata] re-insert icons to head for streamed metadata (<a href="https://redirect.github.com/vercel/next.js/issues/76915">#76915</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/f4552826e1ed15fbeb951be552d67c5a08ad0672"><code>f455282</code></a> v15.2.2</li>
<li>Additional commits viewable in <a href="https://github.com/vercel/next.js/compare/v15.1.6...v15.2.3">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=15.1.6&new-version=15.2.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating it. You can achieve the same result by closing it manually
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/digitaldemocracy2030/kouchou-ai/network/alerts).

</details>

**コメント:** なし

---

### [dependabotを導入](https://github.com/digitaldemocracy2030/kouchou-ai/pull/152)

**作成者:** nasuka  
**作成日:** 2025-03-25T05:59:21Z  
**変更:** +49 -0 (1ファイル)  
**マージ日:** 2025-03-25T06:12:22Z  
**内容:**

# 変更の概要
* dependabotの設定ファイルを設置し、パッケージアップデートのPR作成が自動で行われるようにした

# 変更の背景
* セキュリティの脆弱性に伴うパッケージのアップデートを行いたいが、現状でもgithub上の Security でアラートはくるが、パッケージアップデートをする際は手作業が入る
  * -> dependabotで自動化する

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/151

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Bump next from 15.1.7 to 15.2.3 in /utils/dummy-server](https://github.com/digitaldemocracy2030/kouchou-ai/pull/150)

**作成者:** dependabot[bot]  
**作成日:** 2025-03-25T05:43:59Z  
**変更:** +41 -41 (2ファイル)  
**マージ日:** 2025-03-25T05:44:39Z  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 15.1.7 to 15.2.3.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v15.2.3</h2>
<blockquote>
<p>[!NOTE]<br />
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.
This release contains a security patch for <a href="https://github.com/vercel/next.js/security/advisories/GHSA-f82v-jwr5-mffw">CVE-2025-29927</a>.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>Update default allowed origins list (<a href="https://redirect.github.com/vercel/next.js/issues/77212">#77212</a>)</li>
<li>unify allowed origin detection handling (<a href="https://redirect.github.com/vercel/next.js/issues/77053">#77053</a>)</li>
<li>Add dev warning for cross-origin and stabilize allowedDevOrigins (<a href="https://redirect.github.com/vercel/next.js/issues/77044">#77044</a>)</li>
<li>Ensure deploymentId is used for CSS preloads (<a href="https://redirect.github.com/vercel/next.js/issues/77210">#77210</a>)</li>
<li>Update middleware request header (<a href="https://redirect.github.com/vercel/next.js/issues/77201">#77201</a>)</li>
<li>[metadata] remove the default segement check for metadata rendering (<a href="https://redirect.github.com/vercel/next.js/issues/77119">#77119</a>)</li>
<li>[ts-hint] fix vscode type hint plugin enabling (<a href="https://redirect.github.com/vercel/next.js/issues/77099">#77099</a>)</li>
<li>[metadata] re-insert icons to head for streamed metadata (<a href="https://redirect.github.com/vercel/next.js/issues/76915">#76915</a>)</li>
</ul>
<h3>Credits</h3>
<p>Huge thanks to <a href="https://github.com/ijjk"><code>@​ijjk</code></a>, <a href="https://github.com/ztanner"><code>@​ztanner</code></a>, and <a href="https://github.com/huozhi"><code>@​huozhi</code></a> for helping!</p>
<h2>v15.2.2</h2>
<h3>Core Changes</h3>
<ul>
<li>[dev-overlay] fix styling on overflow error messages, add button hover state: <a href="https://redirect.github.com/vercel/next.js/issues/76771">#76771</a></li>
<li>Fix: respond 405 status code on OPTIONS request to SSG page: <a href="https://redirect.github.com/vercel/next.js/issues/76767">#76767</a></li>
<li>[dev-overlay] Always show relative paths: <a href="https://redirect.github.com/vercel/next.js/issues/76742">#76742</a></li>
<li>[metadata] remove the duplicate metadata in the error boundary: <a href="https://redirect.github.com/vercel/next.js/issues/76791">#76791</a></li>
<li>Upgrade React from <code>d55cc79b-20250228</code> to <code>443b7ff2-20250303</code>: <a href="https://redirect.github.com/vercel/next.js/issues/76804">#76804</a></li>
<li>[dev-overlay] Ignore animations on page load: <a href="https://redirect.github.com/vercel/next.js/issues/76834">#76834</a></li>
<li>fix: remove useless set-cookie in action-handler: <a href="https://redirect.github.com/vercel/next.js/issues/76839">#76839</a></li>
<li>Turbopack: handle task cancelation: <a href="https://redirect.github.com/vercel/next.js/issues/76831">#76831</a></li>
<li>Upgrade React from <code>443b7ff2-20250303</code> to <code>e03ac20f-20250305</code>: <a href="https://redirect.github.com/vercel/next.js/issues/76842">#76842</a></li>
<li>add types for <code>__next_app__</code> module loading functions: <a href="https://redirect.github.com/vercel/next.js/issues/74566">#74566</a></li>
<li>fix duplicated noindex when server action is triggered: <a href="https://redirect.github.com/vercel/next.js/issues/76847">#76847</a></li>
<li>fix: don't drop queued actions when navigating: <a href="https://redirect.github.com/vercel/next.js/issues/75362">#75362</a></li>
<li>[dev-overlay]: remove dependency on platform for focus trapping: <a href="https://redirect.github.com/vercel/next.js/issues/76849">#76849</a></li>
<li>Turbopack: Add <strong>turbopack_load_by_url</strong>: <a href="https://redirect.github.com/vercel/next.js/issues/76814">#76814</a></li>
<li>Add handling of origin in dev mode: <a href="https://redirect.github.com/vercel/next.js/issues/76880">#76880</a></li>
<li>[dev-overlay] Stop grouping callstack frames into ignored vs. not ignored: <a href="https://redirect.github.com/vercel/next.js/issues/76861">#76861</a></li>
<li>Upgrade React from <code>e03ac20f-20250305</code> to <code>029e8bd6-20250306</code>: <a href="https://redirect.github.com/vercel/next.js/issues/76870">#76870</a></li>
<li>[dev-overlay] Increase padding if no <code>x</code> button present: <a href="https://redirect.github.com/vercel/next.js/issues/76898">#76898</a></li>
<li>fix: prevent incorrect searchParams being applied on certain navs: <a href="https://redirect.github.com/vercel/next.js/issues/76914">#76914</a></li>
<li>[dev-overlay] Dim ignore-listed callstack frames when shown: <a href="https://redirect.github.com/vercel/next.js/issues/76862">#76862</a></li>
</ul>
<h3>Example Changes</h3>
<ul>
<li>chore(cna): update tailwind styles to be closer to non-tw cna: <a href="https://redirect.github.com/vercel/next.js/issues/76647">#76647</a></li>
</ul>
<h3>Misc Changes</h3>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/535e26d3c69de49df8bd17618a424cbe65ec897b"><code>535e26d</code></a> v15.2.3</li>
<li><a href="https://github.com/vercel/next.js/commit/2fcae1d7e3079874ff633b5b8311adb584c80ce6"><code>2fcae1d</code></a> Update default allowed origins list (<a href="https://redirect.github.com/vercel/next.js/issues/77212">#77212</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/adf5462b5f269963395b0a2ef12a1b66e8cadabc"><code>adf5462</code></a> unify allowed origin detection handling (<a href="https://redirect.github.com/vercel/next.js/issues/77053">#77053</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/5e59da1f5c8b9e8b3a759048bd371efcd77813ae"><code>5e59da1</code></a> Add dev warning for cross-origin and stabilize allowedDevOrigins (<a href="https://redirect.github.com/vercel/next.js/issues/77044">#77044</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/8151cb6ce921cb1b9faeab6fb88551146dc206b7"><code>8151cb6</code></a> Ensure deploymentId is used for CSS preloads (<a href="https://redirect.github.com/vercel/next.js/issues/77210">#77210</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/52a078da3884efe6501613c7834a3d02a91676d2"><code>52a078d</code></a> Update middleware request header (<a href="https://redirect.github.com/vercel/next.js/issues/77201">#77201</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/4698ad6478cc85a7283a8c41edfbba023dadf57d"><code>4698ad6</code></a> [metadata] remove the default segement check for metadata rendering (<a href="https://redirect.github.com/vercel/next.js/issues/77119">#77119</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/1e1ff403a28703b08e68758cfcbb7b6c97c4bd2a"><code>1e1ff40</code></a> [ts-hint] fix vscode type hint plugin enabling (<a href="https://redirect.github.com/vercel/next.js/issues/77099">#77099</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/88deb12b03c90f5146b1270cd7bea3517cf90083"><code>88deb12</code></a> [metadata] re-insert icons to head for streamed metadata (<a href="https://redirect.github.com/vercel/next.js/issues/76915">#76915</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/f4552826e1ed15fbeb951be552d67c5a08ad0672"><code>f455282</code></a> v15.2.2</li>
<li>Additional commits viewable in <a href="https://github.com/vercel/next.js/compare/v15.1.7...v15.2.3">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=15.1.7&new-version=15.2.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating it. You can achieve the same result by closing it manually
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/digitaldemocracy2030/kouchou-ai/network/alerts).

</details>

**コメント:** なし

---

### 過去30日間に作成されたPR (5件)

### [Azure Blob Storage連携機能の実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/228)

**作成者:** nasuka  
**作成日:** 2025-04-03T16:01:04Z  
**変更:** +1223 -28 (18ファイル)  
**内容:**

# 変更の概要
Azure Blob Storageと連携する機能を実装し、データの永続化を実現
コードとしては以下の機能を実装している

* レポート作成完了時に当該レポートに関する生成物と、report_status.jsonをストレージにアップロードする
  * 生成物は中間ファイル・個別のレポートのstatusのjson・最終的なresultファイルなど全てアップする
* アプリ起動時にストレージから全レポートに関するファイルとreport_status.jsonをダウンロードする
  * レポートに関するファイルについては、jsonファイルのみダウンロードしている
    * 中間生成物までDLするとサイズが重く時間がかかり、また結果の描画にはresult等のjsonがあれば十分なため

また、Azureインフラ構築について、以下のプロセスを追加している

1. ストレージの作成（azure-create-storage）
2. api containerへのマネージドIDの付与(azure-assign-managed-identity)
2. api コンテナからストレージへのアクセス権限の付与(azure-assign-storage-access)

# 変更の背景
Azure環境において、Container Apssでアプリケーションを動かした場合にデータの永続化ができず、レポートが消失してしまう問題があった

# 関連Issue
Close https://github.com/digitaldemocracy2030/kouchou-ai/issues/46

# 動作確認結果

- [x] 作成されたレポート関連ファイルおよびreport_statusが外部ストレージにアップされる
- [x] apiのコンテナを停止 -> 再起動し、ストレージに保存されたファイルが再起動後のapiコンテナに同期されている

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました

**コメント:** なし

---

### [add column selection](https://github.com/digitaldemocracy2030/kouchou-ai/pull/226)

**作成者:** ei-blue  
**作成日:** 2025-04-03T06:57:26Z  
**変更:** +132 -31 (1ファイル)  
**内容:**

# 変更の概要
- csv/スプレッドシートのアップロード/取得時にカラム名の一覧を取得してドロップダウンを作成
- commentという名前を探し、ある場合はデフォルトでそれを選択（なければ「選択してください」が表示）
- /admin/reportsエンドポイントに渡すコメントデータはそこで指定されたカラムのデータが使われる
<img width="884" alt="Screenshot 2025-04-02 at 23 08 05" src="https://github.com/user-attachments/assets/7b9a7381-593f-444b-9bf3-e55864713c86" />
<img width="906" alt="Screenshot 2025-04-02 at 23 08 15" src="https://github.com/user-attachments/assets/c3ff9fe8-9a08-4730-a525-ce468937d442" />

# 変更の背景
- すでにあるデータを分析する際、カラム名を手動でcommentに変更する手間を省ける


# 関連Issue
- Close #116 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [(Draft)Azureの更新のためのターゲットを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/215)

**作成者:** nishio  
**作成日:** 2025-04-01T08:25:51Z  
**変更:** +42 -0 (1ファイル)  
**内容:**

# 変更の背景
https://github.com/digitaldemocracy2030/kouchou-ai/issues/214

# 変更の概要
- Azureの更新のためのターゲットを追加
- (未テストです、次に更新する時にテストします)


# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/214


# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Bump lucide-react from 0.474.0 to 0.483.0 in /client](https://github.com/digitaldemocracy2030/kouchou-ai/pull/169)

**作成者:** dependabot[bot]  
**作成日:** 2025-03-25T06:14:13Z  
**変更:** +5 -5 (2ファイル)  
**内容:**

Bumps [lucide-react](https://github.com/lucide-icons/lucide/tree/HEAD/packages/lucide-react) from 0.474.0 to 0.483.0.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/lucide-icons/lucide/releases">lucide-react's releases</a>.</em></p>
<blockquote>
<h2>Version 0.483.0</h2>
<h2>What's Changed</h2>
<ul>
<li>feat(ci): added <code>pix</code> to brand filter by <a href="https://github.com/jguddas"><code>@​jguddas</code></a> in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2908">lucide-icons/lucide#2908</a></li>
<li>fix(packages/lucide-angular): restore exporting prefixed and suffixed icon names by <a href="https://github.com/karsa-mistmere"><code>@​karsa-mistmere</code></a> in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2919">lucide-icons/lucide#2919</a></li>
<li>feat(icons): updates <code>filter</code> &amp; adds <code>filter-plus</code> icon by <a href="https://github.com/lukedukeus"><code>@​lukedukeus</code></a> in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2917">lucide-icons/lucide#2917</a></li>
</ul>
<h2>New Contributors</h2>
<ul>
<li><a href="https://github.com/lukedukeus"><code>@​lukedukeus</code></a> made their first contribution in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2917">lucide-icons/lucide#2917</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/lucide-icons/lucide/compare/0.482.0...0.483.0">https://github.com/lucide-icons/lucide/compare/0.482.0...0.483.0</a></p>
<h2>Version 0.482.0</h2>
<h2>What's Changed</h2>
<ul>
<li>fix(deps): CVE-2024-21538 by <a href="https://github.com/anupamme"><code>@​anupamme</code></a> in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2871">lucide-icons/lucide#2871</a></li>
<li>feat(icons): add <code>saudi-riyal</code> Symbol by <a href="https://github.com/Null78"><code>@​Null78</code></a> in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2827">lucide-icons/lucide#2827</a></li>
</ul>
<h2>New Contributors</h2>
<ul>
<li><a href="https://github.com/anupamme"><code>@​anupamme</code></a> made their first contribution in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2871">lucide-icons/lucide#2871</a></li>
<li><a href="https://github.com/Null78"><code>@​Null78</code></a> made their first contribution in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2827">lucide-icons/lucide#2827</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/lucide-icons/lucide/compare/0.481.0...0.482.0">https://github.com/lucide-icons/lucide/compare/0.481.0...0.482.0</a></p>
<h2>Version 0.481.0</h2>
<h2>What's Changed</h2>
<ul>
<li>feat(icons): added <code>clock-fading</code> icon by <a href="https://github.com/jguddas"><code>@​jguddas</code></a> in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2405">lucide-icons/lucide#2405</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/lucide-icons/lucide/compare/0.480.0...0.481.0">https://github.com/lucide-icons/lucide/compare/0.480.0...0.481.0</a></p>
<h2>Version 0.480.0</h2>
<h2>What's Changed</h2>
<ul>
<li>ci: added <code>bluesky</code> and <code>spotify</code> to brand list filter by <a href="https://github.com/jguddas"><code>@​jguddas</code></a> in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2857">lucide-icons/lucide#2857</a></li>
<li>fix(docs): grammatical inconsistencies by <a href="https://github.com/FOSS-VFX"><code>@​FOSS-VFX</code></a> in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2899">lucide-icons/lucide#2899</a></li>
<li>fix(docs): Resolves <a href="https://github.com/lucide-icons/lucide/tree/HEAD/packages/lucide-react/issues/2887">#2887</a> by <a href="https://github.com/briz123"><code>@​briz123</code></a> in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2889">lucide-icons/lucide#2889</a></li>
<li>fix(icons): arcified <code>newspaper</code> by <a href="https://github.com/karsa-mistmere"><code>@​karsa-mistmere</code></a> in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2885">lucide-icons/lucide#2885</a></li>
<li>ci(node): Use correct node version by <a href="https://github.com/ericfennis"><code>@​ericfennis</code></a> in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2877">lucide-icons/lucide#2877</a></li>
<li>fix(icons): changed <code>infinity</code> icon by <a href="https://github.com/jamiemlaw"><code>@​jamiemlaw</code></a> in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2868">lucide-icons/lucide#2868</a></li>
<li>feat(icons): added <code>shrimp</code> icon by <a href="https://github.com/jguddas"><code>@​jguddas</code></a> in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2319">lucide-icons/lucide#2319</a></li>
</ul>
<h2>New Contributors</h2>
<ul>
<li><a href="https://github.com/FOSS-VFX"><code>@​FOSS-VFX</code></a> made their first contribution in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2899">lucide-icons/lucide#2899</a></li>
<li><a href="https://github.com/briz123"><code>@​briz123</code></a> made their first contribution in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2889">lucide-icons/lucide#2889</a></li>
</ul>
<p><strong>Full Changelog</strong>: <a href="https://github.com/lucide-icons/lucide/compare/0.479.0...0.480.0">https://github.com/lucide-icons/lucide/compare/0.479.0...0.480.0</a></p>
<h2>Version 0.479.0</h2>
<h2>What's Changed</h2>
<ul>
<li>feat(<code>@​lucide/svelte</code>): Lucide svelte 5 package by <a href="https://github.com/ericfennis"><code>@​ericfennis</code></a> in <a href="https://redirect.github.com/lucide-icons/lucide/pull/2753">lucide-icons/lucide#2753</a></li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/lucide-icons/lucide/commit/07f9d3ea79208b1d3f7c389386fbb9e89d72e30b"><code>07f9d3e</code></a> ci(node): Use correct node version (<a href="https://github.com/lucide-icons/lucide/tree/HEAD/packages/lucide-react/issues/2877">#2877</a>)</li>
<li><a href="https://github.com/lucide-icons/lucide/commit/1787b82cfe02660207e0053b471ea7c56dac8fb8"><code>1787b82</code></a> build(deps-dev): bump vite from 5.4.13 to 5.4.14 in /packages/lucide (<a href="https://github.com/lucide-icons/lucide/tree/HEAD/packages/lucide-react/issues/2804">#2804</a>)</li>
<li><a href="https://github.com/lucide-icons/lucide/commit/b46927e510d93bc5020cad18240f63b05d4c8b0b"><code>b46927e</code></a> fix(lucide-react): Revert exports property package.json, fixing edge worker e...</li>
<li><a href="https://github.com/lucide-icons/lucide/commit/3ab6c373a0803514cfd037d1f399fb726f3cbba7"><code>3ab6c37</code></a> build(deps-dev): bump vite from 5.4.12 to 5.4.13 (<a href="https://github.com/lucide-icons/lucide/tree/HEAD/packages/lucide-react/issues/2798">#2798</a>)</li>
<li><a href="https://github.com/lucide-icons/lucide/commit/ba2c4b526fb8b2b45391aa30a3c5d328f50988f6"><code>ba2c4b5</code></a> build(deps-dev): bump vite from 5.1.8 to 5.4.12 (<a href="https://github.com/lucide-icons/lucide/tree/HEAD/packages/lucide-react/issues/2786">#2786</a>)</li>
<li><a href="https://github.com/lucide-icons/lucide/commit/50630b3aaf84f3bdbe2bb963f5235d4b99ad465a"><code>50630b3</code></a> ci: Improve build speeds (<a href="https://github.com/lucide-icons/lucide/tree/HEAD/packages/lucide-react/issues/2778">#2778</a>)</li>
<li>See full diff in <a href="https://github.com/lucide-icons/lucide/commits/0.483.0/packages/lucide-react">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=lucide-react&package-manager=npm_and_yarn&previous-version=0.474.0&new-version=0.483.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating it. You can achieve the same result by closing it manually
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)


</details>

**コメント:** なし

---

### [Bump @types/node from 20.17.19 to 22.13.13 in /client](https://github.com/digitaldemocracy2030/kouchou-ai/pull/168)

**作成者:** dependabot[bot]  
**作成日:** 2025-03-25T06:14:05Z  
**変更:** +9 -9 (2ファイル)  
**内容:**

Bumps [@types/node](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/HEAD/types/node) from 20.17.19 to 22.13.13.
<details>
<summary>Commits</summary>
<ul>
<li>See full diff in <a href="https://github.com/DefinitelyTyped/DefinitelyTyped/commits/HEAD/types/node">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=@types/node&package-manager=npm_and_yarn&previous-version=20.17.19&new-version=22.13.13)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating it. You can achieve the same result by closing it manually
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)


</details>

**コメント:** なし

---

### 過去30日間に更新されたPR（作成・マージを除く）(2件)

### [レイアウト修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/20)

**作成者:** nanocloudx  
**作成日:** 2025-03-04T11:53:29Z  
**変更:** +40 -24 (6ファイル)  
**内容:**

- メニューを上に移動
- 設定を右端に隔離
- ツリーマップを階層図にリネーム
<img width="903" alt="Screenshot 2025-03-04 at 20 51 34" src="https://github.com/user-attachments/assets/5fa0e548-f2d4-4fae-93c3-479426bbdbaf" />

- CSVアップロード時のID指定を任意に
- 既定値はUUIDv4
<img width="789" alt="Screenshot 2025-03-04 at 20 52 00" src="https://github.com/user-attachments/assets/607a969f-8534-4240-adfb-69c1e82105f1" />


**コメント:** なし

---

### [Docker化](https://github.com/digitaldemocracy2030/kouchou-ai/pull/8)

**作成者:** nasuka  
**作成日:** 2025-03-03T08:12:24Z  
**変更:** +543 -668 (28ファイル)  
**内容:**

それぞれのサービスのdocker化を実施。


**コメント:** なし

---

