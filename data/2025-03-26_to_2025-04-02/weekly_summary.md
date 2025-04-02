# 2025年03月31日～2025年04月06日のSlack活動まとめ

今週は **9個**のチャンネルで合計**126件**のメッセージがやり取りされました。

## チャンネル別アクティビティ

- **#2_開発_広聴ai**: 45件のメッセージ
- **#2_開発_いどばた**: 30件のメッセージ
- **#0412_1day_hackathon**: 28件のメッセージ
- **#1_雑談**: 10件のメッセージ
- **#2_開発_デジ民ウェブサイト**: 5件のメッセージ
- **#1_freetalk-in-english**: 3件のメッセージ
- **#1_自己紹介**: 2件のメッセージ
- **#0_全体お知らせ**: 2件のメッセージ
- **#2_新しいプロジェクトの種**: 1件のメッセージ

## チャンネル別詳細

### #2_開発_広聴ai (45件のメッセージ)

#### 03月31日(Mon) - 22件

- **truego** in #2_開発_広聴ai: この議論、長期的に影響ありそうなので進むといいなと思いました:pray:
<https://github.com/digitaldemocracy2030/kouchou-ai/issues/84|[REFACTOR] フロントエンドのコードを prettier でフォーマットをする> _2025-03-31 07:58:50_
    - **Furukawa**: ちなみにローカルでのフォーマット設定、みなさんどうされていますか…？
フォーマットされていないと結局PRがエラーになるので、その辺のルールやおすすめsettings.json内容もどこかに(というか、CONTRIBUTING.mdに？)書いてあるとありがたいなと思いました _2025-03-31 17:42:23_
    - **Nasuka Sumino**: api側については、ruffでcheck/formatを行うコマンドが用意されているので、その辺りを今送っているPRにも追記しておきました（今のmainだとdocker環境にruff等が入らないバグがあるのですが、このPRがマージされた後は `make lint/api-check` 等でローカルでもチェックできるようになるはずです
<https://github.com/digitaldemocracy2030/kouchou-ai/pull/206/commits/c3256ceccc6954412173295ee58d4cb377378f69>

一旦これでチェック/フォーマット自体はできるようになるはずですが、それとは別でsettings.jsonの内容も共有するようにしても良いかもしれませんね（自分もそのあたり整備できていないのですが :innocent: ） _2025-03-31 18:37:15_
    - **shgtkshruch**: formatter そろそろ入れたいですね。
今の Next.js では Biome はまだサポートされていないという理解なので、Prettier にするのが個人的には無難かなと思っています。

フォーマットについては、自分は client しか触っていないのですが、ESLint のルール違反で自動で修復できるもの（ex. シングルクオート or ダブルクオート、セミコロンの有無など）は `npm run lint -- --fix` で修正しています。コードの構造に起因するエラーは自分で直す必要がありますね。 _2025-03-31 19:53:09_
    - _他 1 件の返信_
- **今井 竜也** in #2_開発_広聴ai: ゆるゆるっとですが、ローカルマシンを用いた本番環境作成・更新のメモを作ってみました。
修正点やアドバイスがあれば大募集です～

<https://gist.github.com/101ta28/a0aae1ed56eaefc2719bc55e4cbdfcd1> _2025-03-31 15:57:55_
    - **Furukawa**: 素晴らしい！！ありがとうございます！！
1点気になったのですが、tempブランチはproductionから作って、そこにmainをマージしてみるのかなと思ったのですが、現在の書き方だとmainからtempを作成してそこにmainをマージしているように見えます。これは意図している書き方でしょうか？ _2025-03-31 16:10:57_
    - **今井 竜也**: 意図としては、最新の動作(main)をtempブランチで試してからマージという感じでした。

おっしゃる通り、分かりにくい表現だったので~変更かけてみます！~変更かけました！ _2025-03-31 16:14:59_
    - **Furukawa**: なるほど、確かに完全切り替えするパターンも差分だけ欲しいパターンもありますよね！変更後のドキュメントでよくわかりました！ありがとうございます！ _2025-03-31 16:30:10_
    - _他 3 件の返信_
- **Furukawa** in #2_開発_広聴ai: ちなみにローカルでのフォーマット設定、みなさんどうされていますか…？
フォーマットされていないと結局PRがエラーになるので、その辺のルールやおすすめsettings.json内容もどこかに(というか、CONTRIBUTING.mdに？)書いてあるとありがたいなと思いました _2025-03-31 17:42:23_
- **NISHIO Hirokazu** in #2_開発_広聴ai: Makefileのazure-acr-loginターゲットってACR名を置き換えてないから一般的には動かないし、どこからも呼ばれてないように思いますが盲腸ですかね？ _2025-03-31 21:11:54_
    - **truego**: ほんとだ。azure-acr-login-auto があってそっちを使っているからいらなそうですね！ _2025-03-31 22:20:58_
    - **truego**: PR出しておきました。
<https://github.com/digitaldemocracy2030/kouchou-ai/pull/210> _2025-03-31 22:35:03_
- **NISHIO Hirokazu** in #2_開発_広聴ai: うっ、Copilotくんがレビューしてくれて変更を提案してくれたので採用したらRuffがfailするようになってしまった、どうすればよかったのか… _2025-03-31 21:22:12_
    - **Nasuka Sumino**: <https://chatgpt.com/share/67eaa845-5c70-800f-b8b1-39af8c290ce8>
Deep Researchにかけてみましたが、linterの個別の設定内容を反映したレビューをするのはできなさそうな感じがしますね...。

> *現状、Copilotのコード提案やレビューコメントにプロジェクト固有のRuff設定を自動的に反映させる明確な方法は存在しません*。たとえば、`.editorconfig`や`pyproject.toml`に定義した最大行長（line-length=120）をCopilotが認識し、その範囲内の長い行を指摘しないようにする、といったことは標準では行われません。これはコミュニティからも指摘されており、Visual Studio版Copilotのプレビューで「*.editorconfigを考慮していない*」との報告もあります<http://developercommunity.visualstudio.com|developercommunity.visualstudio.com>
> 。GitHubが提供する*カスタムコーディングガイドライン機能*を使えば、「本プロジェクトでは行の長さ120文字まで許容し、PEP8のE501違反は無視する」といったルールを自然言語で記述してCopilotに遵守させることは可能ですが<http://docs.github.com|docs.github.com>
> 、この機能は前述のとおり限定的な提供状況です。また公式ドキュメントでも、「*リンターや静的解析ツールでカバーできるスタイル規約を、Copilotのガイドラインで強制しようとしないでください*」と注意されています<http://docs.github.com|docs.github.com>
> 。これは裏を返せば、*Copilot自体はリントツールがカバーする細かなスタイルには全面的には対応しておらず、現時点ではユーザーが明示的に指示しない限りモデルの汎用知識にもとづいて指摘してしまう*ことを意味します。残念ながら*Copilot専用の設定ファイル（例えばLintルールを教えるようなファイル）は提供されていません*。したがって、Ruffの設定をCopilotに完全に守らせる直接的な方法は今のところ無いと考えられます。
変更を反映した後にformatterで機械的にフォーマットをかけるか、もしくはCopilot側が参照しているスタイルにCI側を合わせるかという感じですかね。今の設定にそこまでこだわりはないので、Copilot Reviewがワークしそうであればそちらに合わせに行くでも良いかなと思いました（具体でどんなルールに基づいているか開示されてなさそう？なので、合わせに行くのもちょっと手間がかかりそうではありますが _2025-03-31 23:53:27_
- **NISHIO Hirokazu** in #2_開発_広聴ai: 今日はデプロイ環境と開発環境を分離して、最新版でAzureにデプロイされているものを更新しようとしたのですが、色々トラブって結局できませんでした。
前半部はenvが間違ってる時のエラーメッセージが適切ではないせいでハマってたことが原因でPRを作りました。ローカルで動くようにはなりました。
後半に関して、azure-login azure-build azure-acr-login-auto azure-push make azure-config-update make azure-fix-client-adminまでやったのですが見た目が変わらなくて、何がいけなかったのかなぁと思っています。
Devinいわく
> • ビルド: `make azure-build DOCKER_BUILD_ARGS="--no-cache --pull"` でキャッシュを無効化して確実に最新コードでビルド
> • デプロイ: `az containerapp update --name api --resource-group ${RESOURCE_GROUP} --image ${ACR_NAME}.<http://azurecr.io/api:latest|azurecr.io/api:latest> --force` で強制的に更新
が必要とのことですが、正しい指摘かどうかは分かりません。明日以降試してみるつもりです。 _2025-03-31 22:22:00_
    - **truego**: > azure-login azure-build azure-acr-login-auto azure-push make azure-config-update make azure-fix-client-adminまでやった
上記だと、clien-admin コンテナは新しいもので起動しますが、client と api のコンテナは古いまま（イメージは新しくなったけどコンテナは古いもので起動したまま）になりそうですね。
azure-fix-client-admin の処理の中の以下の部分（古いイメージのコンテナを停止して、新しく push されたイメージでコンテナを起動する）と同様のことを client, api コンテナでもやる必要がありそうな気がしました。
``` az containerapp update --name client-admin --resource-group $(AZURE_RESOURCE_GROUP) --min-replicas 0 && \
      echo '>>> 再度スケールアップ...' && \
      sleep 5 && \
      az containerapp update --name client-admin --resource-group $(AZURE_RESOURCE_GROUP) --min-replicas 1"``` _2025-03-31 22:55:12_
    - **NISHIO Hirokazu**: apiサーバを再起動したらレポートが全部消えたので無事コンテナの更新ができたようです:joy: _2025-03-31 23:25:40_
    - **NISHIO Hirokazu**: Spreadsheetを読む機能が増えてたのでソースコードの更新は成功、問題はレポートの復元だけ _2025-03-31 23:43:03_

#### 04月01日(Tue) - 22件

- **安野貴博** in #2_開発_広聴ai: @efu.eiouai
ごめんなさい！　新しくレポート作ってみたのですが、どこからパブコメデータDLできますっけ？
<https://admin.kouchou-ai.dd2030.org/> _2025-04-01 14:04:41_
    - **安野貴博**:  _2025-04-01 14:05:00_
    - **安野貴博**: この一番下は更新後に作ったやつなのですが、それっぽいボタンが見つからず _2025-04-01 14:05:12_
    - **安野貴博**: 見てるとこ違うのかも・？ _2025-04-01 14:05:16_
    - _他 5 件の返信_
- **NISHIO Hirokazu** in #2_開発_広聴ai: どういうシチュエーションで作成したレポートが消えるのかについて整理したい。理解を書くので間違ってたら突っ込んでください

• 手元の環境でdocker-compose upしている人はボリュームマウントされてるから大丈夫
• →どこに保存されてるのかに気づかないかもしれない。/server/broadlistening/pipeline/outputs/* が個別データで、server/data/report_status.jsonが一覧
• たとえばAzure Container Appsなどにコンテナをビルドしてデプロイしているようなケースにおいては、生成されたレポートがコンテナの中に保存されてるので、新しいソースコードをビルドしてデプロイすると「コンテナごと新しいものに置き換わる=既存のレポートは消える」という挙動になる
• →/scripts/fetch_reports.pyで手元に保存できるのでそれをするといい
• <https://admin.kouchou-ai.dd2030.org/> はCIで更新しているという話、レポートが消えない更新はどうやってやってます？
• →バックエンド側はデータを永続化するためにコンテナではなくVMで動かしている、CDはしていない
クリアになった _2025-04-01 14:06:56_
- **NISHIO Hirokazu** in #2_開発_広聴ai: 5→50の表示、実際の流れとしては50に分けてから5つに集約してますよね。50→5では？という気がしてきました _2025-04-01 15:46:24_
    - **Nasuka Sumino**: これは確かに仰るとおりですね。
50 -> 5に表示を変えたほうが処理の実態に合っていて良さそうに思いました...！ _2025-04-01 16:01:22_
    - **NISHIO Hirokazu**: issued _2025-04-01 17:11:05_
- **NISHIO Hirokazu** in #2_開発_広聴ai: 無事消えたレポートのローカルバックアップからの復元ができました
手段: Azure Container Appにファイルを送る手段がないのでDropboxにアップロードしてコンテナの中からcurlでダウンロード(酷い) _2025-04-01 16:39:06_
    - **NISHIO Hirokazu**: まったくおすすめできない解決手段なのでやっぱりストレージを繋ぐべきか〜〜 _2025-04-01 16:58:24_
- **NISHIO Hirokazu** in #2_開発_広聴ai: 整理Issueを整理し直しておきました
<https://github.com/digitaldemocracy2030/kouchou-ai/issues/80>
(Issueへのリンクにタイトルがつくときとつかない時の差がわからない) _2025-04-01 17:32:49_
    - **shgtkshruch**: マークダウンのリストの中に issue へのリンクを置くとタイトルが展開されますね :memo:

> If you reference an issue, pull request, or discussion in a list, the reference will unfurl to show the title and state instead.
> ref: <https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls#issues-and-pull-requests> _2025-04-01 17:44:46_
    - **NISHIO Hirokazu**: なるほど、更新しました！ _2025-04-01 17:52:32_
- **NISHIO Hirokazu** in #2_開発_広聴ai: とりあえず自分の脳内の混乱を整理して言語化し終わったのでひと段落しました _2025-04-01 18:14:30_

#### 04月02日(Wed) - 1件

- **Nasuka Sumino** in #2_開発_広聴ai: <!here>
本日20時からの広聴AI開発定例について、以下のドキュメントをベースに進めていきたいと思います！
作業内容の共有や質問など、なんでもご記載ください！
<https://docs.google.com/document/d/1plggszRTxEEYUcZuCLiHkPrBsMtxr3RQpctKtZe5y4M/edit?tab=t.0#heading=h.3z7ruicizjrm> _2025-04-02 17:58:52_


### #2_開発_いどばた (30件のメッセージ)

#### 03月31日(Mon) - 15件

- **石井拓都** in #2_開発_いどばた: creditを購入したのですが、依然`401 No auth credentials found` が出てしまいます。
問題を切り分けるために、OpenRouter APIを使った小規模なプログラムを作って確認しようと思います。 _2025-03-31 11:26:11_
- **石井拓都** in #2_開発_いどばた: `idobata-analyst/.env` も必要だったんですね……。
そちらにもAPIキーを通したら動きました！
ありがとうございます！ _2025-03-31 11:34:50_
- **石井拓都** in #2_開発_いどばた: format走らせようとしたらbiomejsがないと出てきたので、biomejsを入れたりしました。
globalにinstallされている環境前提みたいだったので、rootにpackage.jsonを置いて、そちらにbiomeを入れるようにしたいです。
~issue立てておきます~<https://github.com/digitaldemocracy2030/idobata-analyst/issues/90|立てました> _2025-03-31 12:53:52_

#### 04月01日(Tue) - 5件

- **Shutaro Aoyama (ぶるーも)** in #2_開発_いどばた: <https://github.com/digitaldemocracy2030/idobata-analyst/pull/92>
<http://all-hands.dev|all-hands.dev> を使ってPRを作ってみました。あとで自分でレビューします。 _2025-04-01 09:44:12_
- **Shutaro Aoyama (ぶるーも)** in #2_開発_いどばた: （もろもろidobata-analystのレビュー滞っていてすみません！明日対応します） _2025-04-01 09:44:36_
- **Nasuka Sumino** in #2_開発_いどばた: streamlitのコントリビューションガイドがかなり丁寧に書かれていて参考になりそうだったのでこちらでも共有しておきます。広聴AIの<https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CONTRIBUTING.md|コントリビューションガイド>でも内容を一部取り入れています。
<https://github.com/streamlit/streamlit/wiki/Contributing> _2025-04-01 12:12:45_
    - **安野貴博**: これは横展開してもよさそうね _2025-04-01 13:20:57_

#### 04月02日(Wed) - 10件

- **Slackbot** in #2_開発_いどばた: Reminder: i "<!here> :mega: 本日19時より、いどばた開発会議を開催します！:mega: :clock9: 19:00-20:00 :link: <https://meet.google.com/vno-mknp-aoo> • 開発にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！ • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！" _2025-04-02 09:00:18_
- **安野貴博** in #2_開発_いどばた: @yasu.umi.19910101
セルフホスティングのインフラ周りっていかがでしょ？ _2025-04-02 13:44:04_
    - **Yasu-umi Nishikawa**: 相変わらずDockerfile弄くり回してます…ただrailsのサーバー立てたいだけなのに……
<https://github.com/digitaldemocracy2030/idobata-infra/pull/3>
作業中のものはこのpull reqに置くようにしてます(面倒なのでwip commitをforce pushしちゃってますがあとでもうちょっと整理します) _2025-04-02 13:57:29_
- **安野貴博** in #2_開発_いどばた: いどばたの課題意識をおいておく。（あんままとまってなくてごめん）

• Layer1: SNS
    ◦ SNS上で巻き込んでゆくための実験をどんどん進めたい
• Layer2: いどばたAI
    ◦ 現状レポートを見る画面とBotと話す画面が分離しているが統一したい
        ▪︎ ChatGPTのCanvasと同様の形式で良いと思う
        ▪︎ 左に対話ログ / 右にレポート
            • 右のレポートは切替ボタンを押すことでグラフィカルになったり論点ごとになったり生データになったりすると良いと思う
    ◦ いどばたbotと話すことによって、新しくAIが受け取った（抽出した）意見には『ありがとう！』感を追加したい
        ▪︎ 自分の対話によってレポートが進化しているという自己効力感
        ▪︎ 特に『今までになかった視点』にはより大きく感謝できると良さそう
• Layer3: Discourse
    ◦ いどばたレポートなどを参照しながら複数人でより深い議論ができると良い
    ◦ もしかするとここもChatGPTやLayer2と同様の形にしてもいいのかもしれない
        ▪︎ 左側Discourse
        ▪︎ 右側Canvas
• Layer4: GitHub
    ◦ ここも左カラムがBot / Discourseが切り替わっていて、右側に具体案が書いてあればいいのかもしれない _2025-04-02 13:54:11_
- **安野貴博** in #2_開発_いどばた: いどばたUI試案を作りました
<https://docs.google.com/presentation/d/1VFtBdyeSO7e0V8ZZ2hBX_TeAwBbcUUWEoJ3iSXPIoV4/edit?usp=sharing> _2025-04-02 15:57:50_
- **小野翔太** in #2_開発_いどばた: いどばたの最初に見せる1枚絵
考えているんですが、考えるほどもっと多くのことを伝くなりますね… _2025-04-02 16:35:01_
    - **小野翔太**: 一旦作りました。
ズレてる部分や改善案など
いただけると幸いです！ _2025-04-02 17:18:06_
- **jujunjun110** in #2_開発_いどばた: <!here>
本日のいどばた開発定例に向けて、作業内容の共有や質問など、以下の議事録になんでも事前にご記載ください〜！
<https://docs.google.com/document/d/1cK5i3ATo1OXsy-oicllY6-YlI-q0AJVtqQW7a71V-AU/edit?tab=t.fax1253vkyvp> _2025-04-02 16:51:25_
- **小野翔太** in #2_開発_いどばた: 一旦作りました。
ズレてる部分や改善案など
いただけると幸いです！ _2025-04-02 17:18:06_
- **Slackbot** in #2_開発_いどばた: Reminder:  :mega: 1時間後より、いどばた開発会議を開催します！:mega: :clock9: 19:00-20:00 :link: <https://meet.google.com/vno-mknp-aoo> • 開発にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！ • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！ _2025-04-02 18:00:06_


### #0412_1day_hackathon (28件のメッセージ)

#### 03月31日(Mon) - 20件

- **Satoshi Takayama** in #0412_1day_hackathon: @satoshi.takayama has joined the channel _2025-03-31 12:34:47_
- **Michio Kawai** in #0412_1day_hackathon: 活用事例が増やすことがコミュニティの活性化につながると思うので、この日をきっかけに事例が生まれるようにサポートできたらと思いました。
導入相談とかどう使うかを相談するブース？みたいなのがあると良いのかもと思いましたが、意見もらいたいです _2025-03-31 13:05:41_
- **Michio Kawai** in #0412_1day_hackathon: @nanocloudx 1day_hackathonのチャンネルです！ブース的な形でウェブサイトや広報も設けて、議論したい人が議論できると良さそうと思いました！ _2025-03-31 13:50:35_
    - **石橋隆平**: アンカンファレンスのようなスタイルはどうですか？
<https://opendatahandbook.org/glossary/ja/terms/unconference/|https://opendatahandbook.org/glossary/ja/terms/unconference/> _2025-03-31 14:55:08_
    - **石橋隆平**: Scalamatsuri2019
<https://2019.scalamatsuri.org/ja/unconference/|https://2019.scalamatsuri.org/ja/unconference/> _2025-03-31 14:56:45_
    - **石橋隆平**: 話したいけどどう進めれば良いかわからない人にはファシリテーターとして誰がサポートに入っても良いです(自分はできます) _2025-03-31 14:59:47_
- **Syuhei Kobayashi (なのくろ)** in #0412_1day_hackathon: @nanocloudx has joined the channel _2025-03-31 13:50:39_

#### 04月01日(Tue) - 5件

- **LogExporter** in #0412_1day_hackathon: @logexporter has joined the channel _2025-04-01 09:40:04_

#### 04月02日(Wed) - 3件

- **石橋隆平** in #0412_1day_hackathon: すいません！12日現地に行けなくなってしまいました。裏方で出来る限りお手伝いしたいとは思っているので引き続きよろしくお願いします:bow: _2025-04-02 11:52:18_
    - **安野貴博**: 残念！　たぶんまたやるので次の機会にはぜひ！ _2025-04-02 12:15:09_


### #1_雑談 (10件のメッセージ)

#### 03月31日(Mon) - 3件

- **安野貴博** in #1_雑談: 広聴AI関連のYouTube動画をポストしました

【ゆる仮説】生成AIで量産したコメントをパブコメで送りまくる多数派攻撃の対処法を考えてみた
<https://youtu.be/hJPEV4POFZc> _2025-03-31 21:18:35_

#### 04月01日(Tue) - 5件

- **小野翔太** in #1_雑談: せっかくのエイプリルフール、なにかしかけるべきだったか… _2025-04-01 12:48:24_
    - **nao yo4**: 小生は、メールや Line 等を送る相手に、

_*「 本内容には、エイプリルフール的要素は含んでおりません。 」*_

って１文を添えるという、_*間接的な楽しみ方*_ をしておりました。
ＳＮＳ時代、コンプラも厳しき折、ちょっとリスキーでもあるので・・・ _2025-04-01 19:37:58_
- **nao yo4** in #1_雑談: 小生は、メールや Line 等を送る相手に、

_*「 本内容には、エイプリルフール的要素は含んでおりません。 」*_

って１文を添えるという、_*間接的な楽しみ方*_ をしておりました。
ＳＮＳ時代、コンプラも厳しき折、ちょっとリスキーでもあるので・・・ _2025-04-01 19:37:58_
- **小野翔太** in #1_雑談: コンプラ問題難しいですよね…w
SNS時代だからこそバズれたら強いですが、燃えると大変ですしね… _2025-04-01 20:57:12_

#### 04月02日(Wed) - 2件

- **nobumichi asai** in #1_雑談: イーロン・マスク率いるDOGEが6000万行ものCOBOLコードを含む社会保障局のシステムをコード生成AIでわずか数カ月の内に移行させようとしているようです。
重要なポイントは、行政システムにデジタル監視システムが導入されるということ。イーロン・マスクは兼ねてから政府内のお金の流れをブロックチェーンにより透明化すると語っていました。
政府内のお金が追跡可能で透明化されるのは、ポジティブな可能性を感じますね。
しかし同時に国民に対してこれが適用されるリスクは今後考えていく必要があるかもしれません。
日本のマイナンバーカードのあり方は注視していく必要があるかもしれませんね。
<https://gigazine.net/news/20250401-doge-plans-to-rebuild-ssa-cobol-database/?utm_source=facebook&utm_medium=sns&utm_campaign=facebook_post&utm_content=20250401-doge-plans-to-rebuild-ssa-cobol-database|https://gigazine.net/news/20250401-doge-plans-to-rebuild-ssa-cobol-database/?utm_so[…]&utm_content=20250401-doge-plans-to-rebuild-ssa-cobol-database> _2025-04-02 03:42:01_
- **nobumichi asai** in #1_雑談: （参考）
オンライン議論の中でAIのバイアスをどう回避するか？
-------------------------
AIのバイアスを相対化する実験的なGPTsでアプリ“MetaLogos”を公開しました。
政治的な議論をAIを使って行うとき、人々が気づかないバイアスが加算される可能性があります。
ChatGPTやClaudeの場合だと、西洋史観の偏りは避けることができませんし、時の政権の政治アジェンダの影響を強く受けています。
これは無意識的に人々の価値観に影響を与えます。
このことは、デジタル民主制でオンラインで熟議が行われるプロセス、
AIでサマリーやクラスター分析をするときにも重要な問題となる可能性があります。

AI自体は「可能性」の潜在空間であり、善でも悪でもありません。仏教的な「空」そのもの。
それゆえ、一歩間違えれば、AIは、教条的な神となり、神官政治となるリスクがあります。
また、うまく使えば、バイアスを相対化し、偏りのない議論を生み出し、
人間を覚醒させ共進化のための伴走者とすることもできます。
実際問題、現在ではAIはフェイクによる情報操作に大活躍？しています。

AIをどう使うかは、ユーザーが提供するコンテキスト次第。
MetaLogosでは、無自覚的なコンテキストを「問い」「メタ認知」によって可視化することでAIによるバイアスや認知操作を回避しています。
身近なニュースをネタに対話してみて下さい。

こうした発想から政治にAIを使う実践的なアプローチはいろいろあります。
・意図的に対立する立場から意見を生成させる。
・断片化する政治情報に対して、どんな経緯でその事象が起きたのかコンテキストを解説させる。
・関係するステークホルダーの立場から意味を捉え直して比較させる。
こうしたシステムプロンプトを組んで、AIを議論のファシリテーターにする、というのは有効かもしれません。

ちなみにボクが試したところでは、
一般的なテーマについては、システムプロンプトによるメタ認知で、
価値判断を相対化させることができましたが、
特定のセンシティブな政治テーマについては頑ななバイアスがかかっているようでした。
<https://chatgpt.com/g/g-67df8936bff081918ce4772c4a16cab5-metalogos> _2025-04-02 03:56:01_


### #2_開発_デジ民ウェブサイト (5件のメッセージ)

#### 04月01日(Tue) - 3件

- **小野翔太** in #2_開発_デジ民ウェブサイト: 皆さんの助言を参考にしつつ、とりあえず情報をぶっこんでいる途中です（ワイヤーフレーム）。
<https://www.figma.com/design/lkwDYHrjp8U7A5pg6E2OdM/web%E3%82%B5%E3%82%A4%E3%83%88?node-id=12-2&t=IQ0UQcgclFAjdwXj-1>

編集権限も付与可能ですが、確か無料版は人数制限があったと思うので～…どうしたものか。

@nanocloudx
なにか進め方などありましたらご指示ください。
また、暴走してたら止めて下さい:man-bowing: _2025-04-01 15:15:56_
    - **Syuhei Kobayashi (なのくろ)**: 最高です！ありがとうございます！！！
暴走頂けるぐらいが丁度いいと思っていますので、是非よろしくお願いします :heart: _2025-04-01 21:57:35_
    - **Kizaki**: 情報を整理いただきありがとうございます。

個人的に思っていたことなのですが、

• なぜデジタル民主主義なのか
• なぜ2030年なのか
詳しく説明するページがあると、ユーザーにとってより自分ごと化されやすくなり、共感する人が増えるのではないかと思います。

例えば、

なぜデジタル民主主義なのか
＝なぜテクノロジーを社会実装する必要があるのか？

について、都知事選における@annyotaka さんの演説を引用させていただくと、経済を発展させてくには、（これ以上人口を増やせず天然資源もない東京においては）「テクノロジーを活用することでしか実現できない」と説明されています。これは東京に限った話ではなく、日本という国全体にも言えることかと思います。

極論ですが、私たち現役世代は、テクノロジーを社会実装していくことで、経済の復興や暮らしの豊かさを得られる社会を目指すか、あるいは、このままゆるやかに衰退していくことを受け入れるのか、選択を迫られているように思います。

デジタル民主主義という取り組みは、閉塞感の漂う今の社会において、興味をもち、参加してみることで、「もしかしたら未来は変えられるかもしれない」と思え、そうした思いが少しずつ広がっていくことで、やがて「変えられるに違いない」という確信へと変わっていくような、そんな変化につながる運動になっていったらいいなと思います。

<https://youtu.be/pzZhq6-4QBk> _2025-04-01 22:02:39_

#### 04月02日(Wed) - 2件



### #1_freetalk-in-english (3件のメッセージ)

#### 03月31日(Mon) - 3件

- **Shunsuke Takagi (taka)** in #1_freetalk-in-english: <https://docs.google.com/presentation/d/1UTO0mEM-XHYWBPaK9bwJgTo6TwX4kfJDsJArYY3LEpc/edit?usp=sharing> _2025-03-31 14:06:04_
    - **Shunsuke Takagi (taka)**: I had a talk about digital democracy 2030 in japan on d/acc day in Taipei! thanks all

slide; <https://docs.google.com/presentation/d/1UTO0mEM-XHYWBPaK9bwJgTo6TwX4kfJDsJArYY3LEpc/edit#slide=id.g3465e9d4753_0_14> _2025-03-31 17:29:58_
- **Shunsuke Takagi (taka)** in #1_freetalk-in-english: I had a talk about digital democracy 2030 in japan on d/acc day in Taipei! thanks all

slide; <https://docs.google.com/presentation/d/1UTO0mEM-XHYWBPaK9bwJgTo6TwX4kfJDsJArYY3LEpc/edit#slide=id.g3465e9d4753_0_14> _2025-03-31 17:29:58_


### #1_自己紹介 (2件のメッセージ)

#### 03月31日(Mon) - 2件



### #0_全体お知らせ (2件のメッセージ)

#### 04月01日(Tue) - 2件

- **Kazuko Muto** in #0_全体お知らせ: 3/29のデジタル民主主義2030週次定例、メモも以下に共有いたします！
<https://docs.google.com/document/d/1adkIbAeCCI1BGMMqAqt041JDH5Gl5MPfG7N1AShz6rM/edit?usp=sharing> _2025-04-01 09:57:41_


### #2_新しいプロジェクトの種 (1件のメッセージ)

#### 04月02日(Wed) - 1件

- **NISHIO Hirokazu** in #2_新しいプロジェクトの種: まとめ
・オリジナルの実装は「Slackからの抽出」と「Google Spreadsheetへのアップロード」がセットになっていた。これはログを保存するという目的には合理的。1ヶ月に1回実行して2ヶ月前のログを保存する運用を想定
・毎週の更新レポートをLLMで作りたいという目的に使おうと思った時、Google Spreadsheetを経由するのは無駄に複雑では？となった、それはそう、目的が変わったから適切な構成も変わる
・「Slackからの抽出(JSONで保存)」「JSONからのMarkdown作成」「JSONからGoogle Spreadsheet」のコンポーネントに分けてそれぞれPython実装を作った
・今回は手作業でやるかもだけど将来的にMarkdownを入力として「週次レポートのMarkdown」をLLMが生成する
・JSONはGitHubでdataブランチを作ってそこに日付付きで保存していく予定 _2025-04-02 16:26:15_

