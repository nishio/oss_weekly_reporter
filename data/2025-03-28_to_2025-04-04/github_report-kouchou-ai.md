# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-03-28 から 2025-04-04 まで

## Issues

### 過去7日間に完了されたissue (14件)

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

### [[FEATURE] 単一ページの出力機能](https://github.com/digitaldemocracy2030/kouchou-ai/issues/53)

**作成者:** nanocloudx  
**作成日:** 2025-03-16T03:45:56Z  
**内容:**

# 背景
現在はサーバーを起動することで各レポート表示が実現されている
サーバーが用意できない（静的ファイルの配置ならできる）環境でもレポートの公開ができるようにしたい

# 提案内容
next export を用いて単一レポートだけのファイル出力ができる機能を追加する

**コメント:** なし

---

### [[FEATURE]階層図ホバー時にクラスタの概要説明を表示したい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/14)

**作成者:** nasuka  
**作成日:** 2025-03-04T11:30:25Z  
**内容:**

# 背景
階層図をホバーしても表示される情報が少なく、クラスタの内容を把握しにくい。


# 提案内容
ホバー時に「クラスタの説明文」をツールチップ表示する
例えば以下のようなクラスタ説明文をツールチップに表示するイメージ

> このクラスタは、生成AIの利用がクリエイターの権利や創作活動に与える影響に関する懸念を集約しています。参加者は、生成AIが著作権を侵害するリスクや、クリエイターの努力を無視することによる創作意欲の減退を指摘し、厳格な規制や法整備の必要性を強調しています。また、生成AIの悪用による名誉毀損や偽情報の拡散、文化的影響についても懸念が示されており、クリエイターとAIの共存を目指すための具体的な対策が求められています。


![Image](https://github.com/user-attachments/assets/c3ccf02e-7701-4ea6-941b-5f73cc15f42e)

**コメント:** なし

---

### [[FEATURE]レポート出力の進捗を知りたい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/13)

**作成者:** nasuka  
**作成日:** 2025-03-04T11:15:35Z  
**内容:**

# 背景
* レポート出力が現在どの程度進んでいるのかをダッシュボード上で把握したい


# 提案内容
* バックエンドの処理のステップ単位（extraction, clustering, etc）でダッシュボード上のステータス表示を変える
* 実現方法の案としては、ステップ毎にレポートの実行ステータスを更新する（processingの粒度を細分化する）のが比較的ライトに実現できそう？
  * この場合、以下の実装が必要
    * バックエンド側ではステップを実行する毎にステータスを更新する
    * client/client-admin側でステータスに応じて表示を変える


**コメント:** なし

---

### 過去7日間に作成されたissue (15件)

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

### 過去7日間に更新されたissue（作成・クローズを除く）(6件)

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

### [[FEATURE]「どのフィールドをcommentとするか」を指定できる機能](https://github.com/digitaldemocracy2030/kouchou-ai/issues/116)

**作成者:** nishio  
**作成日:** 2025-03-21T05:24:46Z  
**内容:**

# 背景
Shutaro Aoyama (ぶるーも)
昨日こうちょうAIを試して、csvフォーマットが絶妙に違うのがだるいなと思いました（ここはコミュニケーションとった方がよかったですね、、）
いどばたcsvのcontentをcommentに変えるとこうちょうAIに突っ込めるという認識


NISHIO Hirokazu
現状はまずはノンエンジニアが使えるようにWebUIを頑張ってますけど、将来的にはAPIでレポート生成をトリガーできるべきで、その時に「どのフィールドをcommentとするか」を指定できるのが理想だと思います 

# 提案内容

defaultが"comment"であるような"target-column"属性を受け取るようにし、そのカラムを分析対象とする。
アンケートのようなデータソースでは通常複数のカラムがあるので、個別にCSVを保存し直さなくても分析できるようになって楽。

**コメント:** なし

---

### [(情報整理)Azureについて](https://github.com/digitaldemocracy2030/kouchou-ai/issues/80)

**作成者:** nishio  
**作成日:** 2025-03-18T03:33:26Z  
**内容:**

自治体や大企業などを中心にAzureを使いたいというニーズがある。

これを分解整理する

- 1: ✅ OpenAIのAPIを直接叩くのではなくAzure OpenAI Serviceを使いたい( #89)
- 2: ✅ Azureでホストしたい(#94)
- 3: Azure Container Appsでホストしている場合にソースコードのアップデートをすると既存のレポートが消えてしまう問題の解決

- x: Azureでのセットアップガイド ( #133 #175)

## 3に関して

- https://github.com/digitaldemocracy2030/kouchou-ai/pull/180 で消失を防いでいるが部分的解決に過ぎない
- https://github.com/digitaldemocracy2030/kouchou-ai/issues/214 で更新時に自動的に保存する方針にした
- これらをビルドに含めることができれば実は解決なのでは？という気もする https://github.com/digitaldemocracy2030/kouchou-ai/issues/216

- 王道の解決方法はストレージ接続の #174 #46 だと思うが、デフォルトでONにしないなら「ストレージOFFで始めて試して、いいレポートができたので保存したくなったので更新しようとして消える」というバターンが発生することのケアが必要

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

**コメント:** なし

---

### [[FEATURE]ストレージ連携](https://github.com/digitaldemocracy2030/kouchou-ai/issues/46)

**作成者:** nasuka  
**作成日:** 2025-03-15T14:01:35Z  
**内容:**

# 変更の背景
* 現在、apiにおいて、各レポートのステータス（ready, etc）と出力されたレポートのファイルは、レポート出力を実行したマシンにのみ保存される
* このため、persistent volumeを持たない実行環境ではapiをホスティングできない
  * また、バックアップを取らない限り、実行環境が壊れた場合にデータが失われてしまう


# 提案内容
* レポートのステータスを記録するファイルと、出力されたレポートおよびその中間ファイルをストレージ（S3等）に連携する
  * 現在、Azureでインフラを構築できるスクリプトが組まれているので、まずはAzure Blob Storageと連携できるようにするのが良さそう？
* 具体的には、以下の処理を実装する
  * ステータスの更新時にステータスファイルをストレージにアップロードする
    * statusファイルは `./server/data/report_status.json` に配置されている
  * レポート出力完了時に、中間ファイル・resultをストレージにアップロードする
    * 中間ファイルは `./server/broadlistening/outputs` 配下に配置されている
      * outputs配下に、各レポートのslugでディレクトリが作成され、そのディレクトリ内にレポートの中間成果物（embeddingやクラスタリング結果など）と結果ファイル（hierarchical_result.json）が格納されている
  * アプリケーション起動時に、ストレージから各ファイルをダウンロードする
* ストレージ連携はオプショナルにする
  * ストレージ利用がオンになっている場合のみストレージ連携を行う



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


**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (16件)

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

### 過去7日間に作成されたPR (3件)

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

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [CSVファイル送信時にコメント数とクラスタ数設定を比較して警告を出す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/148)

**作成者:** ei-blue  
**作成日:** 2025-03-25T05:28:53Z  
**変更:** +11 -0 (1ファイル)  
**内容:**

# 変更の概要

- レポート作成ボタンクリック時にCSVファイルの行数とクラスタ数の設定を比較し、ファイルの行数が少ない場合に警告を出す。

![image](https://github.com/user-attachments/assets/8d0ff772-d758-4575-826a-4aebe8ea3b01)

# 変更の背景

- デフォルトのクラスタ数設定は[5, 50]。
- 登録されたCSVファイルの意見数が設定されたクラスタ数に満たない場合、クラスタリングの過程でエラーになる。
- これを防ぐため、APIを呼び出す前にCSVファイル内のコメント数（ファイルの行数）を確認する。
- コメント数＝意見数ではなく、一つのコメントから複数の意見が抽出される可能性もあるため、エラーではなく警告にとどめる。

# 関連Issue
Closes #147 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

