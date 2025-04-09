# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-04-02 から 2025-04-09 まで

## Issues

### 過去7日間に完了されたissue (15件)

### [[FEATURE]Azure Blob Serviceにlocal file systemにあるレポートをuploadするスクリプト](https://github.com/digitaldemocracy2030/kouchou-ai/issues/260)

**作成者:** nishio  
**作成日:** 2025-04-08T10:51:40Z  
**内容:**

# 背景
- derived from #216 
- local file systemにあるレポートをビルドに含めるのではなく、Azure Blob Serviceにuploadするスクリプトがあるのが適切


# 提案内容



**コメント:** なし

---

### [[FEATURE]１層目のクラスタ数上限を緩和する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/257)

**作成者:** nasuka  
**作成日:** 2025-04-08T06:46:31Z  
**内容:**

# 背景
* 現在1層目のクラスタ数上限は最大で10個だが、これだと粒度が粗すぎる
  * 実用的には1層目でもより細分化して確認したいケースがある

# 提案内容
* 1層目のクラスタ数の上限を緩和する
  * 決め打ちだが一旦40個程度までは緩和しても良さそう
  * バックエンド側は対応できるようになっており、admin側でバリデーションを修正すればできるはず
* 2層目については、設定値の下限を1層目のクラスタ数の2倍程度にすると良さそう


**コメント:** なし

---

### [[FEATURE]Analysis内の「意見が含まれるコメント数」 を「コメント数」に変える](https://github.com/digitaldemocracy2030/kouchou-ai/issues/238)

**作成者:** nasuka  
**作成日:** 2025-04-06T02:09:30Z  
**内容:**

# 背景
* 実装の実態として、「意見が含まれるコメント数」ではなく元データ内の単純な「コメント数」を算出しており、文言と実態が合っていない
* また、件数を記載する上でも、全体として何件のデータが処理されたのかが表示されている方が自然
  * 「意見が含まれるコメント数」を記載するのであれば、「コメント数」と「抽出された意見数」の間に入れるべき
    * ここまで入れるべきかどうかは議論の余地があるが、個人的には複雑になりすぎるので表示しなくても良いように思う


<img width="881" alt="Image" src="https://github.com/user-attachments/assets/e2bab1c1-d1b9-4013-a87e-b3d9724ea29d" />


# 提案内容
「意見が含まれるコメント数」 -> 「コメント数」に文言を修正する

**コメント:** なし

---

### [[BUG] 散布図等・全体画面表示：背景HPの一部が重なって表示される](https://github.com/digitaldemocracy2030/kouchou-ai/issues/237)

**作成者:** naoyo4  
**作成日:** 2025-04-05T23:33:17Z  
**内容:**

### 概要

<!-- バグの簡潔な説明をお願いします -->
全体画面表示すると、元のHP、タイトルの文字・ボタン等（ 背景HP ）が重なって表示される。
（　スクロールすると背景HPも動いて表示される　）

### 再現手順

「全体図」・「濃い意見グループ」の散布図、および「階層図」で、**右の「全体画面表示」を押し、全体画面表示をする**

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->
全体画面表示をしても、背景HPの一部が重なって表示されることがないようにする。

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

![Image](https://github.com/user-attachments/assets/0b37672e-0655-4f3c-a836-7b3f3d8b1dbe)

![Image](https://github.com/user-attachments/assets/dddcfd73-2bd1-4bec-8f90-bba248d76324)

![Image](https://github.com/user-attachments/assets/1a4ffcb7-6a32-4e49-8fd7-6b6e9557b47e)

![Image](https://github.com/user-attachments/assets/7b070937-39b8-479b-9592-256681b0f24d)

### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->
以前は、このようなことはなかった。　どのタイミングで発生しだしたか不明。
最新の Build（ Commit 978b776 ： main #226 ）で確認。
（　↑ 表現の仕方がよく分からないけど・・・最新のもの　）

２日前（ 4/4 ）作成した、テストサイト（ https://naoyo4.xsrv.jp/ ）でも同様の現象が確認できる。
（　タイミング的に同じ最新 Build or 少し手前　）

**コメント:** なし

---

### [[FEATURE]レポートの削除機能](https://github.com/digitaldemocracy2030/kouchou-ai/issues/230)

**作成者:** nasuka  
**作成日:** 2025-04-04T07:56:05Z  
**内容:**

# 背景
* 広聴AIのレポート出力にあたっては、パラメータ/プロンプトを変えて何度もレポートを出力するケースが多い
  * 実験的に出力したレポートがclientの一覧画面にあるとノイズになることがあり、実験的に出力したレポートを削除したいケースがある
    * 公開/非公開を管理する( https://github.com/digitaldemocracy2030/kouchou-ai/issues/229 )ことでclient側の問題は解決できるが、admin側では非公開にしたとしても不要なレポートが残る


# 提案内容
レポートの削除機能を実装する

* client-admin
  * 一覧画面でレポートの削除が押された際に、削除のリクエストをapiに送信する
* api
  * report_statusの状態にdeletedを追加する  
  * 削除のendpointを作成し、対象のslugのレポートのstatusをdeletedにする
  * deletedなレポートをフィルタした上でclientに結果を返す
  
↑は保守的に論理削除にする想定で記載してますが、物理削除でもいいかも（ご意見ある方はぜひコメントしていただけると助かります）

![Image](https://github.com/user-attachments/assets/e16a27d5-ec5f-4a44-8a82-14e99cf8a47e)

**コメント:** なし

---

### [[FEATURE]レポートの公開/非公開状態の設定](https://github.com/digitaldemocracy2030/kouchou-ai/issues/229)

**作成者:** nasuka  
**作成日:** 2025-04-04T07:42:44Z  
**内容:**

# 背景
* 広聴AIのレポート出力にあたっては、パラメータ/プロンプトを変えて何度もレポートを出力するケースが多い
* 実験的に出力したレポートがclientの一覧画面にあるとノイズになることがある
  * client側では調整した後の最終的なレポートが閲覧できれば良く、実験過程のレポートは閲覧できなくても良い場合がある
    * e.g. 最終的なレポートを市民に向けてパブリックに公開するケース等

# 提案内容
adminに公開/非公開のトグルスイッチを設け、公開状態のもののみclient側で表示するようにする

改修内容のイメージ

* api
  * レポートごとに公開/非公開を管理する情報を追加する
    * report_status.jsonで管理する想定
  * `GET /reports` に対して公開中のレポートのみ返すようにする
  *  `GET /reports/{slug}` に対して、公開中のレポートのみ結果のjsonを返すようにする
* client-admin
  * 一覧画面においてレポートごとに公開/非公開を管理するトグルスイッチを足す
  * トグルスイッチが押された際にapi側にリクエストを送信し、公開/非公開の状態を変更する

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

### 過去7日間に作成されたissue (16件)

### [[FEATURE]クラスタ数が増えた場合に散布図上でクラスタラベルが被ってしまう](https://github.com/digitaldemocracy2030/kouchou-ai/issues/266)

**作成者:** nasuka  
**作成日:** 2025-04-08T14:20:10Z  
**内容:**

# 背景
* クラスタ数が増えた場合に散布図上でクラスタラベルが被ってしまう
  * 添付画像は40件で出力したケース。多くのクラスタラベルが被ってしまっている。
![Image](https://github.com/user-attachments/assets/c8e61e43-ef60-4054-91d0-4b8f3e6f4847)


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

**コメント:** なし

---

### [[REFACTOR] GitHub Actions で Biome の lint, format のチェックを実行する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/264)

**作成者:** shgtkshruch  
**作成日:** 2025-04-08T12:47:44Z  
**内容:**

# 現在の問題点
<!-- 現在のコードの何が問題なのか、どのような技術的負債があるかを説明してください -->

- #84 で Biome を導入しましたが、format, lint エラーがあるコードがプルリクエストに含まれていても気づく仕組みが現状では整っていません
- Biome の lint, format を適用しないコードが取り込まれると、コード全体の統一性が落ちるのと、Biome を適用した他のプルリクエストでコードの差分が出る可能性があります
  - 本来のプルリクエストとは関係のない差分が出ることで、レビューの負荷が上がりそう

# 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->

- client, client admin のコードの修正を含むプルリクエストを作成したら、CI で Biome の format, lint のチェックを実行する
  - [公式で提供している GitHub Actions と `biome ci`](https://biomejs.dev/recipes/continuous-integration/) コマンドが利用できるかもしれません

**コメント:** なし

---

### [(情報整理)OpenAIが使えないケースのケア](https://github.com/digitaldemocracy2030/kouchou-ai/issues/255)

**作成者:** nishio  
**作成日:** 2025-04-08T03:21:10Z  
**内容:**

# 背景

政党に売り込む上で「ChatGPTの政治利用NG」が障害になる可能性がある？→あるのでケアが必要

解決案
 - A: そもそもAzure OpenAI ServiceならOKなのでは説(=対処完了済み)
 - B: Geminiを叩けるように変える
   - B-1: 直接Geminiを叩く分岐を環境変数でやる
   - B-2: OpenRouter経由にすることでOpenAI API形式でGeminiを叩けるようにする
   - B-3: [LiteLLM Proxy](https://scrapbox.io/nishio/LiteLLM_Proxy) でやるマニュアルを作る


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

**コメント:** なし

---

### [(情報整理)Windows環境で試す人のためのガイドが必要](https://github.com/digitaldemocracy2030/kouchou-ai/issues/254)

**作成者:** nishio  
**作成日:** 2025-04-08T03:14:53Z  
**内容:**

Windows環境で試す人の踏みそうなトラブルシューティング

西尾も角野さんもMacなのでどんなトラブルが起きるのかを観測できてない感、issueでもslackでもガンガン書いてもらえるといいと思う

Windows環境で試すとなった時に、まずいきなり「生環境でやる」「WSLでやる」「Dockerでやる」の3つの選択肢があると思ってて、どれが一番スムーズなのかはよくわかってない、Windows環境のある人の協力があるとありがたいゾーン

関連Slack: https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1744081553571589

**コメント:** なし

---

### [[FEATURE]静的HTML出力してローカルファイルシステムで開いたときに詳細なエラー表示をする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/253)

**作成者:** nishio  
**作成日:** 2025-04-08T03:13:48Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

Q: 静的HTML出力してローカルファイルシステムで開いたとき読み込み中のまま進まない、バグ？
A: →ブラウザがデータをローカルファイルシステムから読めないことに起因する、GitHubPagesなどにデプロイしちゃえば動くと思う、手元でサーバを立てるてもある、解説があるとベター

関連Slack: https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1744080063900439

# 提案内容

この件は読み込み中のバーが回りっぱなしになるが裏では即座にエラーになってるはずで、エラーメッセージを出して解決策解説ページへのリンクを示すのが親切だと思う



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

**コメント:** なし

---

### [初期設定時のentrypoint.shエラー](https://github.com/digitaldemocracy2030/kouchou-ai/issues/243)

**作成者:** nasuka  
**作成日:** 2025-04-06T11:02:11Z  
**内容:**

## バグの内容
初期設定時にentrypoint.shエラーが出たため、ChatGPTに解決策を聞いたものとなります。
http://localhost:3000/　http://localhost:4000/のページは見れるようになりました。
環境がWindows10で、PowerShell 5.xです。

【エラー内容①】
client-1 exited with code 0
/entrypoint.sh: line 5: syntax error: unexpected "fi" (expecting "then")

●エラーの意味：
client（レポート表示画面）の起動時に、entrypoint.sh という起動スクリプトの中に文法ミスがあります

正確には：
if 文が書いてあるけど、その中に then がない
そのまま fi（if の終わり）に到達して、エラーになってる

●修正案１（？）
if [ "$NODE_ENV" = "production" ]; then
  npm run start
else
  npm run dev
fi

●修正案２（？）
#!/bin/sh
# 起動時に全て削除した上でbuildしなおす
if [ -d ".next" ]; then
  rm -rf .next
fi  

# build時にAPIサーバーを参照するため、APIサーバーの起動を待ってからbuildを行う
npm run build
exec npm run start

●修正案３（？）
Windowsメモ帳が改行コードをCRLF（\r\n）にしてしまうせいで、Docker内で「: not found」や syntax error: unexpected "fi" が出る。
✅ 対処方法（メモ帳ユーザーでもOK）
PowerShellで改行コードをLFに変換する（推奨）
以下を PowerShell で kouchou-ai フォルダ内で実行：
＜PowerShell＞
手順１（PowerShell 7.x対応）
cd ~\kouchou-ai
(Get-Content .\client\entrypoint.sh) -join "`n" | Set-Content -NoByteOrderMark -Encoding utf8 .\client\entrypoint.sh

手順１修正版コマンド（PowerShell 5.x対応）
(Get-Content .\client\entrypoint.sh) -join "`n" | Set-Content -Encoding UTF8 .\client\entrypoint.sh
手順２
docker-compose down
docker-compose up --build






【エラー内容②】
client-1 | ./entrypoint.sh: line 1: ﻿#!/bin/sh: not found
この「﻿」は見えないBOM文字。Windowsのメモ帳で保存した .sh ファイルはUTF-8 with BOMになりやすい。
手順１：entrypoint.sh の最初の行のBOMを完全に除去する
●修正案②ー１（PowerShell 7.x対応）
Get-Content .\client\entrypoint.sh | Out-File -Encoding ASCII -NoNewline .\client\entrypoint.sh
●修正案②ー２（PowerShell 7.x対応）
Get-Content .\client\entrypoint.sh | Set-Content -Encoding UTF8 -NoByteOrderMark .\client\entrypoint.sh
●修正案②ー３（PowerShell 5.x対応）
[System.IO.File]::WriteAllLines('.\client\entrypoint.sh', [System.IO.File]::ReadAllLines('.\client\entrypoint.sh'), (New-Object System.Text.UTF8Encoding($false)))


手順２：フルリセットして再起動
docker-compose down --volumes --remove-orphans
docker-compose build --no-cache
docker-compose up


---
こちらのイシューはGoogle Form経由で投稿されたものです

**コメント:** なし

---

### [[FEATURE]おすすめクラスタ数設定機能](https://github.com/digitaldemocracy2030/kouchou-ai/issues/241)

**作成者:** nishio  
**作成日:** 2025-04-06T03:54:15Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

>yuneko
意見グループ数(クラスタ数)をどのくらいで試せばいいのか、目安が知りたいです。この件数(列数)だとまずこれにするといいよというのがわかると、お試しで自分のデータを試したときに、うまく行ったなという感覚になりやすい気がします。
NISHIO Hirokazu
模索段階ではあるんですけど漠然と思ってることとしては、データが1000件あるなら10→100にするのが良さそうという感じです
8000件だったら20→400、125件だったら5→25
∛1000=10ということです。
その理屈でいうとサンプルの400件のデータは7→50がいい気がしましたが、今の5→50と7→50に変えたのとでどちらが良いのかを雰囲気ではなくちゃんと科学的根拠を持って言えるようになるといいなぁと思ってて、その研究の緊急度が低くて放置されていますw
yuneko
いいレポートを明らかに評価できると嬉しいですね。(嬉しいけど放置はされそう)
ヒューリスティクスでも少し評価できるなら、一定の初期値で固定しておくより、できるならコメントの件数によって勝手にクラスタ数を変更する(例えば∛の切り捨てとか)にした方がユーザーフレンドリーかもと思いました。もしくは、おすすめクラスタ数を選択したら、勝手にいい感じのクラスタ数に変更するなど。

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

案0: READMEに書く

案1: CSVアップロード後に「おすすめクラスタ数設定 7→50 [button: この設定にする]」みたいな表示を出す
 
問題点
- Google Spreadsheetから読むのってクライアントサイドだったかな... サーバサイドで読むまでデータ量がわからないのだとするとこの方法では無理
- 一旦Google Spreadsheetは無視すると言うのも手

案2: パラメータを変えて再分析する機能ができた後なら、前の分析の情報を使っておすすめを出すことができるかも？

**コメント:** なし

---

### [[FEATURE] パブコメモードに回答案を追加する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/236)

**作成者:** ei-blue  
**作成日:** 2025-04-05T09:48:05Z  
**内容:**

# 背景
- 実際のパブコメの運用においては、意見概要と、意見に対する考え方がセットになって公開されている。
- （あくまでも草案としての）回答案があらかじめ記入してあると、一から記載するよりも職員の負担が減るのではないか。
- 最初は一般論としての回答からはじめ、最終的にはRAGで公式文書を参照して回答できるようにしたい。

# 提案内容
- 回答案作成用プロンプトを用意する
- パブコメモードに「回答案作成」というオプションをつける
- CSVファイルに回答を追加

RAG対応の構成も追って考えていきたいので、意見・提案があればお願いします

**コメント:** なし

---

### [[DOCUMENT] README に GitHub Pages で公開する手順を記載する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/235)

**作成者:** shgtkshruch  
**作成日:** 2025-04-05T07:07:57Z  
**内容:**

# 現在の問題点
<!-- 現在のコードの何が問題なのか、どのような技術的負債があるかを説明してください -->

- client を static build して GitHub Pages で公開する場合、ビルドしたファイルをアップロードすると一部のコードが動かない
  - 原因: GitHub Pages で動いている Jekyll が `_` から始まるファイルやディレクトリを無視するため、static build 後の `_next` 以下のファイルが 404 になる
    - https://github.blog/news-insights/the-library/bypassing-jekyll-on-github-pages/
  - `.nojekyll` というファイルをルートに置くと動くようになるが、この挙動は知らない人が多そうで GitHub Pages で公開する人が同じ罠にハマる可能性がある

# 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->

- README の静的ファイル出力のセクションに、GitHub Pages で公開する場合の手順を記載する
  - ルートに `.nojekyll` ファイルを追加することもここに記載する

**コメント:** なし

---

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

- https://github.com/digitaldemocracy2030/kouchou-ai/issues/241

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

### 過去7日間に更新されたissue（作成・クローズを除く）(2件)

### [[REFACTOR] フロントエンドのコードを Biome でフォーマットをする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/84)

**作成者:** shgtkshruch  
**作成日:** 2025-03-18T03:59:30Z  
**内容:**

# 現在の問題点
<!-- 現在のコードの何が問題なのか、どのような技術的負債があるかを説明してください -->

- この issue のスコープとしては、フロントエンドに関わる client, client-admin, utils/dummy-server を想定しています
- コードの formatter が導入されていないため、開発者によってコードの書き方（ex. 改行、スペースの入れ方）に差分出てくる可能性がある

# 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->
- フロントエンドで広く利用されている [prettier](https://prettier.io/) を導入して、コードのフォーマットを自動化する
  - 一部 ESLint でフォーマットのチェックをしているところも prettier に寄せたい気持ちです
    https://github.com/digitaldemocracy2030/kouchou-ai/blob/c0a10e33f3f0ea458525a19a55a887b3f3f4792b/client/eslint.config.mjs#L16-L20
    https://github.com/digitaldemocracy2030/kouchou-ai/blob/c0a10e33f3f0ea458525a19a55a887b3f3f4792b/client-admin/eslint.config.mjs#L16-L20
  https://github.com/digitaldemocracy2030/kouchou-ai/blob/c0a10e33f3f0ea458525a19a55a887b3f3f4792b/utils/dummy-server/eslint.config.mjs#L16-L20
- pre-commit or pre-push hook などで prettier を実行する仕組みを導入して、フォーマットされたコードが GitHub に push されるようにする
  - これを実現するツールとしては [husky](https://github.com/typicode/husky) や [lefthook](https://github.com/evilmartians/lefthook) などがありますが、個人的には実行のパフォーマンスと設定のシンプルさから lefthook が良いかなと思っています

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

### 過去7日間にマージされたPR (21件)

### [第一階層のクラスタ数の上限を緩和](https://github.com/digitaldemocracy2030/kouchou-ai/pull/265)

**作成者:** nasuka  
**作成日:** 2025-04-08T13:24:30Z  
**変更:** +88 -35 (2ファイル)  
**マージ日:** 2025-04-08T14:03:13Z  
**内容:**

# 変更の概要
- (admin) 第一階層のクラスタ数上限を10 -> 20に緩和
  - これに合わせて、第二階層のクラスタ数下限を、`第一階層のクラスタ数 * 2` に変更
  - 条件に合致しない（下回る）場合は第二階層のクラスタ数が自動で下限に調整される & メッセージが表示される（gif参照）
- (client) 散布図のカラーバリエーションを8種類 -> 20種類まで追加

![acd132c150b21a9a813d7fe7f92e81e9](https://github.com/user-attachments/assets/71d995c8-e179-43b7-ba74-06a531a153b3)

20件のクラスタを可視化した例
![image](https://github.com/user-attachments/assets/d3d5467a-51c0-436e-87ee-50a4cbdf15ef)



# 変更の背景
* 第一階層のクラスタ数上限が10になっていたが、これだと少なすぎるケースがある
  * TTTCの過去事例だとクラスタ数を30に出力しているケースもある
    * 参考: https://broadlistening.seisakukikaku.metro.tokyo.lg.jp/20250131/index.html
  * 上限クラスタ数は出来ればもう少し緩和したかったが、クラスタ数が増えすぎると散布図が見にくくなる問題があるため、一旦今回のPRでは20に設定している

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/257

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
**マージ日:** 2025-04-08T13:36:26Z  
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
**マージ日:** 2025-04-09T01:02:00Z  
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

### [Azure Blob Storageにローカルのレポートをuploadするscript](https://github.com/digitaldemocracy2030/kouchou-ai/pull/261)

**作成者:** nishio  
**作成日:** 2025-04-08T11:13:03Z  
**変更:** +541 -0 (4ファイル)  
**マージ日:** 2025-04-08T12:23:08Z  
**内容:**

# 変更の概要
- Azure Blob Storageにローカルのレポートをuploadするscriptを追加した
- 実環境で動作確認済み

# 変更の背景
- Azure Blob Storage導入後に生成されたレポートは永続化されるが、それ以前のものは別途Azure Blob Storageに入れる必要があるため

# 関連Issue
- https://github.com/digitaldemocracy2030/kouchou-ai/issues/260

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Azure.mdに環境変数の説明を追記](https://github.com/digitaldemocracy2030/kouchou-ai/pull/259)

**作成者:** nasuka  
**作成日:** 2025-04-08T09:48:37Z  
**変更:** +71 -10 (1ファイル)  
**マージ日:** 2025-04-08T11:45:26Z  
**内容:**

# 変更の概要
* Azure.md内部に、Azure環境固有の環境変数について説明を追記
  * 概要、設定例、許容される命名規則（文字）について追記
* コンテナが停止するとレポートが削除される記載を削除 
  * ストレージ連携でデータの永続化が実現したため

# 変更の背景
* ユーザー側でどのような名称を設定すべきか・どのような命名規則が許容されるのかわからないことがある
  * 参考: https://github.com/digitaldemocracy2030/kouchou-ai/pull/228#issuecomment-2785746069
    * >  ここでnaming conventionが分からなかったので調べた>>>


# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Fix: 静的ビルド時のパーミッションエラー修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/258)

**作成者:** nishio  
**作成日:** 2025-04-08T07:20:09Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-04-08T13:42:37Z  
**内容:**

# 静的ビルド時のパーミッションエラー修正

## 問題
静的ファイル出力（static build）を行う際、2回目以降にパーミッションエラーが発生する問題を修正しました。
Dockerコンテナ内でrootユーザーとしてファイルが生成されるため、ホスト側の通常ユーザーが`rm -rf out`でファイルを削除できなくなっていました。

## 解決策
Dockerコンテナ起動時にホストと同じユーザーIDを指定する方法（ユーザー指定アプローチ）を実装しました。
`docker compose run`コマンドに`--user $(shell id -u):$(shell id -g)`オプションを追加することで、
生成されるファイルの所有者がホストユーザーになり、パーミッションエラーが発生しなくなります。

## メリット
- 根本的な解決策（原因を解決）
- 生成されるファイルの所有者が最初からホストユーザーになる
- セキュリティ的に優れている（最小権限の原則に従う）

Fixes #225

Link to Devin run: https://app.devin.ai/sessions/b996b4b929424c5788a064bcafebf242
Requested by: NISHIO Hirokazu (nishio.hirokazu@gmail.com)

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [「パブコメモード」という名称を「CSV出力モード」に変更](https://github.com/digitaldemocracy2030/kouchou-ai/pull/256)

**作成者:** ei-blue  
**作成日:** 2025-04-08T06:25:47Z  
**変更:** +19 -19 (4ファイル)  
**マージ日:** 2025-04-08T06:51:48Z  
**内容:**

# 変更の概要
- UI上及びコード上の説明において「パブコメモード」という言葉を「CSV出力モード」に変更
- page.tsxのその他の変更は自動フォーマットによるもの

# 変更の背景
- 旧パブコメモードは元コメントと合わせてCSVでデータを出力する機能であり、必ずしもパブリックコメント分析だけに用途が限られるわけではないため。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Fix issue #237: Add z-index to fullscreen chart container](https://github.com/digitaldemocracy2030/kouchou-ai/pull/252)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-08T02:46:13Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-04-08T08:14:59Z  
**内容:**

全画面表示モードで背景要素が重なって表示される問題を修正しました。z-indexの設定が不足していたため、全画面表示用のコンテナに高いz-index値を追加しました。

Fixes #237

Link to Devin run: https://app.devin.ai/sessions/9864e37baf8c414a882d0060f821be30
Requested by: annyotaka@gmail.com

**コメント:** なし

---

### [client に Biome を適用](https://github.com/digitaldemocracy2030/kouchou-ai/pull/249)

**作成者:** shgtkshruch  
**作成日:** 2025-04-07T12:21:33Z  
**変更:** +2070 -4995 (55ファイル)  
**マージ日:** 2025-04-08T11:41:37Z  
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

### [[FEATURE] client/client-adminのテストをGitHub Actionsで実行する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/247)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-07T10:05:13Z  
**変更:** +13142 -1633 (13ファイル)  
**マージ日:** 2025-04-08T11:59:59Z  
**内容:**

Issue #219 を解決します。

# 変更内容
- clientとclient-adminにJestのセットアップを追加
- ユーティリティ関数（getApiBaseUrl, getClusterNum）のテストを実装
- GitHub Actionsで自動テスト実行するためのワークフローを追加

# 検証方法
- ローカルでテストを実行し、パスすることを確認
- PR作成後、GitHub Actionsが正常に実行されることを確認

Close #219

Link to Devin run: https://app.devin.ai/sessions/e3d45689784648ae809350c5a927f2ee
Requested by: annyotaka@gmail.com

**コメント:** なし

---

### [[FEATURE] レポート一覧に作成日時を追加する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/245)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-07T10:00:47Z  
**変更:** +9 -0 (4ファイル)  
**マージ日:** 2025-04-09T01:09:47Z  
**内容:**

Issue #218 の対応: レポート一覧に作成日時を追加しました。\n\nLink to Devin run: https://app.devin.ai/sessions/b13628010677450a813d14ed748a51ca\nRequested by: annyotaka@gmail.com

**コメント:** なし

---

### [Biome の追加と dummy-server にフォーマットを適用](https://github.com/digitaldemocracy2030/kouchou-ai/pull/242)

**作成者:** shgtkshruch  
**作成日:** 2025-04-06T08:41:59Z  
**変更:** +566 -4291 (15ファイル)  
**マージ日:** 2025-04-06T22:19:16Z  
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

### [clientの一覧画面でISRを有効化](https://github.com/digitaldemocracy2030/kouchou-ai/pull/240)

**作成者:** nasuka  
**作成日:** 2025-04-06T03:30:36Z  
**変更:** +3 -0 (1ファイル)  
**マージ日:** 2025-04-06T22:18:01Z  
**内容:**

# 変更の概要
* clientの一覧画面でISRを有効化
  * 5分毎に更新を実施
  * これにより、作成した新規のレポートが一覧画面に表示されるようになった

# 変更の背景
* clientの一覧画面においては、ISRが設定されておらず、新規のレポートを作成してもbuildを再実行しないかぎり一覧画面に反映されなかった

# 関連Issue
Close https://github.com/digitaldemocracy2030/kouchou-ai/issues/212

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [「意見が含まれるコメント数」 -> 「コメント数」に文言を修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/239)

**作成者:** nasuka  
**作成日:** 2025-04-06T03:13:37Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-04-06T03:26:34Z  
**内容:**

# 変更の概要
Analysis上で、「意見が含まれるコメント数」 -> 「コメント数」に文言を修正

# 変更の背景
* 実装の実態として、「意見が含まれるコメント数」ではなく元データ内の単純な「コメント数」を計算しており、文言と実態が合っていない
* また、件数を表示するうえでも、入力データ全体の件数が表示されている方が自然

# 関連Issue
Close https://github.com/digitaldemocracy2030/kouchou-ai/issues/238

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [意見グループ（クラスタ）数の値の変更を直接入力でも可能にする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/234)

**作成者:** shingo-ohki  
**作成日:** 2025-04-05T03:14:43Z  
**変更:** +78 -21 (1ファイル)  
**マージ日:** 2025-04-06T00:09:11Z  
**内容:**

# 変更の概要
- タイトルの通り
- 並列実行数についても見た目を揃えるために同様に修正

# スクリーンショット
![Screenshot from 2025-04-05 12-06-44](https://github.com/user-attachments/assets/7ea283c1-f25d-405a-a30e-ba8a298ecd97)

# 変更の背景
現状では大きく値を変更しようとするとボタンをたくさん押す必要があってユーザーに負担がかかるため

# 関連Issue
#222 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [[FEATURE]レポートの公開/非公開状態の設定 (#229)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/233)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-04T10:14:57Z  
**変更:** +79 -10 (7ファイル)  
**マージ日:** 2025-04-07T07:25:13Z  
**内容:**

# [FEATURE]レポートの公開/非公開状態の設定 (#229)

このPRでは、広聴AIのレポートの公開/非公開状態を切り替える機能を実装しています。管理者はレポートごとにトグルスイッチで公開/非公開を設定でき、公開中のレポートのみがクライアント側で表示されます。

変更内容:
- レポートスキーマに公開/非公開フラグを追加
- APIエンドポイントで公開/非公開状態を切り替える機能を追加
- クライアント側のエンドポイントで公開レポートのみを返すよう修正
- 管理画面にトグルスイッチを追加

Link to Devin run: https://app.devin.ai/sessions/5934f18249994900886ec0abe2360456
Requested by: annyotaka


**コメント:** なし

---

### [Implement report deletion feature (issue #230)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/232)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-04T10:08:38Z  
**変更:** +57 -7 (4ファイル)  
**マージ日:** 2025-04-08T11:55:39Z  
**内容:**

This PR implements the report deletion feature as described in issue #230.

## Changes
- Added DELETED status to ReportStatus enum
- Created a new DELETE endpoint in admin_report.py
- Modified report_status.py to filter deleted reports
- Updated client-admin UI to enable report deletion

Fixes #230

Link to Devin run: https://app.devin.ai/sessions/dc95c7c8dabb4dd7b02bdf6a4544c1fc
Requested by: annyotaka@gmail.com

**コメント:** なし

---

### [Azure Blob Storage連携機能の実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/228)

**作成者:** nasuka  
**作成日:** 2025-04-03T16:01:04Z  
**変更:** +1460 -30 (20ファイル)  
**マージ日:** 2025-04-08T09:04:48Z  
**内容:**

# 変更の概要
* Azure Blob Storageと連携する機能を実装し、Azure Container Apps環境においてレポート等のデータの永続化を実現した
* アプリケーションコード・テストの実装と、Azureインフラ構築スクリプトの追加を実施した


## 実装概要

* レポート作成完了時に、当該レポートに関する生成物とreport_status.jsonをストレージにアップロードする
  * 中間ファイルや最終的なresultファイルなど、当該レポートのoutputsディレクトリの配下にある全てのファイルをアップする
* アプリ起動時にストレージから全レポートのファイル（outputs）とreport_status.jsonをダウンロードする
  * レポートに関するファイルについては、jsonファイルのみダウンロードしている
    * 中間生成物までDLするとサイズが重くなってしまい、結果の描画にはresult等のjsonがあれば十分なため


また、Azure Blob Storageの活用に伴って、Azureインフラ構築で以下のプロセスを追加している。
これにより `make azure-setup-all` でストレージの構築・連携を実現している。

1. ストレージの作成（azure-create-storage）
2. api containerへのマネージドIDの付与(azure-assign-managed-identity)
2. api コンテナからストレージへのアクセス権限の付与(azure-assign-storage-access)


Container Appsからストレージへの認証は2種類あるが、今回はセキュリティが堅牢なMicrosoft Entra ID（旧Azure AD）による認証を採用

参考:
https://claude.ai/share/c6c6521f-f2aa-4088-b227-2864afa5c6df

## 注意点
* 本機能の実装によって、機能搭載後に出力したレポートはストレージ上に保存されますが、それ以前に出力したレポートは保存されません
* 以前に出力したレポートを同期したい場合は以下の手順で同期することができます
  * 1.レポート・ステータスファイルを以下のスクリプトで既存のアプリからexportする
    * https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/scripts/fetch_reports.py
  * 2.ステータスファイル・レポートの生成物をAzure Blob Storageに配置する
    * 事前にストレージを作成しておく必要があります。`make azure-setup-all` で構築した場合は、一通り環境を構築した後に配置する必要があります。
    * ファイルは以下の様に配置する必要があります
      * レポートの関連ファイルは `outputs/{slug}` 配下に配置（ローカル環境と同じ）
      * ステータスファイルは `status/report_status.json` として配置
  * 3.apiコンテナの再起動
    * ストレージからのファイル同期はAPIの起動時にのみ行われているため、apiコンテナを再起動する必要があります
    * コンテナの再起動は `make azure-api-restart` で実行できます

![image](https://github.com/user-attachments/assets/676de31c-b8a4-4a00-8140-771ed2cdf2ef)


# 変更の背景
Azure環境において、Container Appsでアプリケーションを動かした場合にデータの永続化ができず、レポートが消失してしまう問題があった

# 関連Issue
Close https://github.com/digitaldemocracy2030/kouchou-ai/issues/46

# 動作確認結果

- [x] 作成されたレポート関連ファイルおよびreport_statusが外部ストレージにアップされる
- [x] apiのコンテナを停止 -> 再起動し、ストレージに保存されたファイルが再起動後のapiコンテナに同期されている
- [x] STORAGE_TYPEが `local` or 設定されていない場合に問題なくレポート出力が実行できる
- [x] `make azure-setup-all` で、Azure Blob Storage含めて全てのインフラが構築できる

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [add column selection](https://github.com/digitaldemocracy2030/kouchou-ai/pull/226)

**作成者:** ei-blue  
**作成日:** 2025-04-03T06:57:26Z  
**変更:** +132 -31 (1ファイル)  
**マージ日:** 2025-04-04T06:07:55Z  
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

### 過去7日間に作成されたPR (5件)

### [[FEATURE] GoogleAnalytics 対応 #54](https://github.com/digitaldemocracy2030/kouchou-ai/pull/251)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-08T02:32:53Z  
**変更:** +1000 -0 (11ファイル)  
**内容:**

GoogleAnalyticsを実装しました。

環境変数`NEXT_PUBLIC_GA_MEASUREMENT_ID`を追加し、client と client-admin の両方のアプリケーションでGoogleAnalytics 4のトラッキングコードを実装しました。

開発環境では自動的にGAが無効になるよう実装しています。

Link to Devin run: https://app.devin.ai/sessions/bf89d99cdeb94897a6a5085d8e34826e
Requested by: annyotaka@gmail.com

**コメント:** なし

---

### [[FEATURE] レポートの複製・再利用機能 (Issue #19)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/248)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-07T10:07:21Z  
**変更:** +231 -7 (5ファイル)  
**内容:**

このPRはIssue #19の実装です。レポートの設定を複製・再利用する機能を追加します。

## 変更内容
- 管理画面に「既存レポートの再利用」オプションを追加
- 既存レポートの設定を取得するAPIエンドポイントを追加
- レポート生成時に複製元のレポートの中間成果物をコピーする機能を追加

## リンク
- Issue: #19
- Link to Devin run: https://app.devin.ai/sessions/7f69c1c5eace4259828fdcd2cce6f06a

## 検証方法
1. 管理画面で「既存レポートの再利用」を選択
2. 既存レポートを選択して設定を読み込む
3. 設定を変更して新しいレポートを作成
4. レポートが正常に生成されることを確認

**コメント:** なし

---

### [[FEATURE] 1回のextractionで複数のcommentを処理する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/246)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-07T10:02:28Z  
**変更:** +360 -65 (5ファイル)  
**内容:**

# 複数コメントを1回のextraction処理で処理する

## 概要
Issue #190 の実装です。1回のLLMリクエストで複数のコメントを同時に処理できるようにしました。これにより、処理速度の向上とOpenAI APIのレート制限の問題の緩和が期待できます。

## 変更内容
- extractionPromptを更新し、複数コメントを一度に処理できるフォーマットに変更
- extraction.pyにバッチ処理のロジックを実装
- parse_json_list.pyを拡張し、新しいJSONレスポンス形式に対応

## テスト
- 短いコメント（ツイートレベル）と長いコメント（公開コメントレベル）の両方でテスト
- 従来の方法と比較して処理速度の向上を確認

Link to Devin run: https://app.devin.ai/sessions/c9d31459eaed4fe9bc2274aaf699d893
Requested by: annyotaka@gmail.com


**コメント:** なし

---

### [[FEATURE] おすすめクラスタ数設定機能の実装 (#241)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/244)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-07T10:00:36Z  
**変更:** +82 -1 (3ファイル)  
**内容:**

Issue #241 の実装を行いました。

- 案0: README.mdとhow_to_use/README.mdに推奨クラスタ数の情報を追加
- 案1: CSVアップロード後に推奨クラスタ数設定UIを追加
- 計算方法: コメント数の立方根(∛n)を基準に計算

Google Spreadsheetの部分は無視しています。

テスト手順:
1. CSVファイルをアップロード
2. 推奨クラスタ数が表示されることを確認
3. 「この設定にする」ボタンで設定が適用されることを確認

Link to Devin run: https://app.devin.ai/sessions/4edce5fbbb4241d3b2c60118e98d4b8d
Requested by: annyotaka@gmail.com

**コメント:** なし

---

### [Test PR: Dummy change for verification](https://github.com/digitaldemocracy2030/kouchou-ai/pull/231)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-04T09:52:59Z  
**変更:** +2 -0 (1ファイル)  
**内容:**

This is a test PR to verify access to the repository and PR creation functionality.

Link to Devin run: https://app.devin.ai/sessions/6da4c845527d479989142984f4c0e5b1
Requested by: annyotaka@gmail.com

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

