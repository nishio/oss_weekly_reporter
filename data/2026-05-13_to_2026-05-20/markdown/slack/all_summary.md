# 2026年05月14日～2026年05月20日のSlack活動まとめ

今週は **12個**のチャンネルで合計**167件**のメッセージがやり取りされました。

## チャンネル別アクティビティ

- **#2_開発_広聴ai**: 59件のメッセージ
- **#7_雑談**: 33件のメッセージ
- **#2_コアループ_process**: 30件のメッセージ
- **#2_コアループ_オンライン広告詐欺対策_市民熟議会議**: 19件のメッセージ
- **#0_全体お知らせ**: 7件のメッセージ
- **#2_コミュニティ運営**: 7件のメッセージ
- **#2_コアループ_tech**: 4件のメッセージ
- **#2_開発_polimoney**: 2件のメッセージ
- **#2_broad-listening-book**: 2件のメッセージ
- **#2_コアループ_communication**: 2件のメッセージ
- **#2_コアループ_policy**: 1件のメッセージ
- **#8_人数推移**: 1件のメッセージ

## チャンネル別詳細

### #2_開発_広聴ai (59件のメッセージ)

#### 05月15日(Fri) - 9件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-15 11:35:49_

新しいデータと環境でClaude Codeに「広聴AIで分析して」と丸投げして何に躓くかを記録させている
AIのAPIがHTTPSの時に広聴AIはHTTPとハードコードされていて問題だと早速躓いているw

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-15 11:47:17_

analysis-coreをlocal venvにeditableでインストールする経路で試してるみたいだ、なるほどな〜

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-15 12:42:21_

3つ修正点があるというので一旦PRを作らせて、それを後で僕がレビューします

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-15 17:24:47_

チケットが最適でないのは当然だと思うが、どうしていくのが良いのかは悩ましいところ
<https://techblog.technology-doctor.com/entry/2026/05/11/144722|https://techblog.technology-doctor.com/entry/2026/05/11/144722>

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-15 18:01:30_

> *`build:static` は build 時に API endpoint に fetch する設計* で、JSON ファイルを直接食わせるモードは入っていません。
これオプションとしてつけたらサーバを起動しなくても散布図HTMLが手に入るのでは

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-15 19:14:27_

AIに任せると300件のデータに対して「3 → 6 → 12 → 24」みたいなまとめすぎのパラメータにする傾向がある

#### スレッド返信

**Shingo OHKI** _2026-05-15 20:48:05_

それってなんでなんですかね？

**NISHIO Hirokazu** _2026-05-15 22:35:10_

うっ、こういうことか

**Shingo OHKI** _2026-05-15 22:57:15_

あー、なるほど！


#### 05月16日(Sat) - 3件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-16 20:53:52_

広聴AIの開発に関して、@truego さん @shinta.nakayama さんそれぞれPRとかがあるみたいですけど、月曜は集合しますか？それともDocsに現状の考えてることを書いといて的な感じにしますか？

### **中山心太（tokoroten）** in #2_開発_広聴ai _2026-05-16 21:00:17_

そうですね、久しぶりに開発ミーティングしましょうか。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-16 22:31:41_

:clock9: 20:00-21:00
:link: <https://meet.google.com/feh-cnpt-nhq>
:memo: <https://docs.google.com/document/d/1plggszRTxEEYUcZuCLiHkPrBsMtxr3RQpctKtZe5y4M>


#### 05月17日(Sun) - 7件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-17 00:31:37_

前回はdd2030を初めて訪れた人向けのWikiを生成したけど、今度は「広聴AIの開発者向け」でWiki生成を試してみる

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-17 01:32:59_

まだ全然完璧ではないので実際に開発しながら「ここは記載が間違ってる」とか指摘していかないといけない感じですがそれなりに形になりました。

リファクタリングってどこまでやったんだっけ〜とか
<https://github.com/nishio/kouchou-ai-developer-wiki/blob/main/wiki/analyses/refactoring-status.md>
はまりどころってどこ？とか
<https://github.com/nishio/kouchou-ai-developer-wiki/blob/main/wiki/analyses/gotchas.md>
議論が分かれてたのなんだっけ？とか
<https://github.com/nishio/kouchou-ai-developer-wiki/blob/main/wiki/analyses/open-decisions.md>

このWikiを踏まえて開発させればSlackや議事録の話を文脈理解しつつ開発してくれるはず…
開発者が「なんだっけ？」となったこともガンガン質問していけば解説がどんどん生えるはず

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-17 02:02:52_

ある程度この運用が安定してきたら過去のIssuesを読みにいかせて整理させたい。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-17 07:40:33_

Slackをあんまり読んでなさそうだったので明示的に指示を出してみたらいい感じにまとめてくれそうな気配

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-17 08:03:01_

PyPIの更新自動化をやらなければいけないことを思い出してきたのでCodexにWikiを見ながら実装してもらっている。そもそもコア部分用のテストが必要だよねという話になっている。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-17 08:54:40_

UMAPのseed固定警告以外はpass、seed固定に関してはtokorotenが何か検討してた気がする、デフォルトは固定なしで良いと思う、固定用オプションをつけるのはありだがYAGNIかなという気持ち

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-17 09:10:44_

Codex Mobileの導入により電車移動中にも開発が進む(無限労働編)


#### 05月18日(Mon) - 10件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-18 13:14:44_

Codexが賢いのかLLM Wikiを繋いだことによる効果なのか切り分けられてませんが、スマホで別の用事の待ち時間に「nishioのopenなPRってどんな状況？」と聞いたらcoderabbitのレビューコメントとかも読んで作業してくれたので格段に便利になりました。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-18 14:42:56_

dependabotのPRに関しては問題なさそうなのでmergeしますね

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-18 20:00:25_

<!here> 本日20時より、ブロードリスニング本執筆会議を開催します！:mega:
:clock9: 20:00-21:00
:link: <https://meet.google.com/feh-cnpt-nhq>
:memo: <https://docs.google.com/document/d/1plggszRTxEEYUcZuCLiHkPrBsMtxr3RQpctKtZe5y4M>
• ブロードリスニング本執筆にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-18 20:56:51_

@truego これの話を聞き忘れました、MergeしてOK？
<https://github.com/digitaldemocracy2030/kouchou-ai/pull/817>

#### スレッド返信

**Shingo OHKI** _2026-05-18 21:51:02_

はい、OKです！

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-18 21:14:25_

どうしてdriveに入ってないのかはさておき文字起こしは一部の人にだけ共有されてる状態になってた
<https://docs.google.com/document/d/1rA4xOFEj869wIehzJanYiHOADrMoY8F3Aamx_CwfP_Q/edit?usp=sharing>

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-18 21:16:27_

CodeQLってなんだろう(これもAIに聞いてみる)

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-18 23:06:58_

> openなPRから1つ選んでCIが通っていることを確認してmergeして
と書いたら
> open PR から #828 を選び、CI通過を確認して merge しました。checks は test, build, Analyze (python), Analyze (javascript), CodeQL, CodeRabbit がすべて pass でした。
と確認してからmergeすることに成功した。

ただしadmin mergeしたので「そうじゃなくてmergeしてOKだと判断した理由を書いてから通常のマージをすべきだよ」という教育をしたw

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-18 23:15:02_

deployがfailしたのに気づいたので原因調査中

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-18 23:56:20_

これはたまたまで、同じコードで再実行したら直った


#### 05月19日(Tue) - 25件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 00:02:12_

PyPI 0.1.2 がリリースされるところまで成功しました

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 00:07:52_

現状の実装は 「analysis-core-v* tag を push し、その workflow が最後まで success した時に PyPI release が発生する」 なのだけど、これでいいのかmainのupdateで勝手にどんどんリリースした方がいいのか、それとも1日1回くらい更新があったらリリースするってのがいいのか、は検討の余地がありそう

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 00:26:29_

<https://nishio.github.io/kouchou-ai-developer-wiki/analyses/codeql-introduction-context/>

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 00:30:20_

今試しているWikiつきのAgentに実装させるスタイルの解説も生成しときました
<https://nishio.github.io/kouchou-ai-developer-wiki/concepts/wiki-driven-workflow/>

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 00:44:16_

ちなみにこのWikiは以前作ったdd2030 wikiと違って「人間が読むためにAIが書いている」というよりは「人間も読める形でAIが自分の理解を書き留めている」という感じのものです。AIが読む想定。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 10:41:36_

@shinta.nakayama <https://github.com/digitaldemocracy2030/kouchou-ai/pull/834>
> `#800` の切り分けで、`config` を欠いた `hierarchical_result.json` を API が返すと viewer が落ちること自体は再現できました。
だけど、これを下流で回避するんじゃなくて、そもそももっと上流で止めるべきだよねということで
> `/reports/{slug}` が返す `hierarchical_result.json` について、public-viewer が前提にしている最小契約を API 側で検証するようにします。
という実装にしようと思っています。

### **中山心太（tokoroten）** in #2_開発_広聴ai _2026-05-19 10:48:38_

なるほど、よさそう。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 13:15:28_

Codexに「PRを見て」「これってマージできる？」と聞くと「これはいれたらいい」とか「これは深刻なレビューの指摘に答えないまま放置されているからcloseしよう」とか「もっとこう言う設計にした方がいいと思う」とか言ってくるのでメンテナのPR処理に対する心理的ハードルが激下がりします

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 13:19:06_

そしてそれがスマホからできるので電車移動とか病院の待ち時間とかにできる

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 13:23:28_



### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 13:23:55_

言語化助かる

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 15:49:39_

気づいてなかったがブロードリスニング本の原稿を元に、ユーザがどのような目的で使うかや期待などを抽出してWikiに入れると良さそう

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 16:55:36_

すべてのPRが解決されました、スッキリ！

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 16:58:21_

10月に自分がDevinにやらせて、CodeRabbitからいっぱいコメントが着いてたPRについて「このPRどう思う？」とCodexに聞いたら「CLI経路を作ったので前提が変わってますね、解決したかった問題の一部はすでに解決済み、残りをIssueにしてPRは閉じたらいいんじゃない？」と言われてすんなり解消しましたw
<https://github.com/digitaldemocracy2030/kouchou-ai/pull/722#issuecomment-4485587932|https://github.com/digitaldemocracy2030/kouchou-ai/pull/722#issuecomment-4485587932>

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 17:11:35_

特にAIに書かせてPRを作った時点でdoneのつもりでいたが、思ってなかった方向からCodeRabbitのレビューが付いたときに、タスクのサイズが急に想定より大きくなってしまう。
このときに、使える時間キャパをオーバーしてしまったりとかで「続きは今度やろう」ってすると、だいたい次までに忘れる(苦笑)
じゃあその場でPRをcloseするかというと「もったいない」的な気持ちが生じてしまい「とりあえずdraftにしとこ」となりがち。
一方で、「最初の実装案A」と「それに対するレビューコメントB」の両方がある状態で第三者的にCodexがレビューをすると「Bの指摘に合わせて修正すべきか」「そもそも最初の案Aが良くなかったのか」という思考が走って、いい感じの解決策が出てくることがしばしばある。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 17:22:08_

145件のOpen Issueを読んで分析することがあっさりできている、すごい

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 17:24:44_

解決したい課題を軸に整理させている、これが終わったら次はそれぞれの課題が現在の実装でも再現するのかを確認させて、再現するものに関して解決策を作っていく。Issueに書かれている解決策はあくまで一つの案に過ぎない、それを実装すべきかどうかはソースコードを踏まえた上で判断。

問題に対する解決の案だしには人間も議論に参加してワイワイした方がいいかもですね、やり方を考えてみます

### **Shingo OHKI** in #2_開発_広聴ai _2026-05-19 17:26:49_

議論した方がいいものは、ある程度の観点はAIに出してもらっといて、それを見ながら定例とかで話せるといいんですかねー

### **Shingo OHKI** in #2_開発_広聴ai _2026-05-19 17:27:54_

開発チームに超優秀な参謀が入った感:smile:

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 17:38:58_

全Issueを読んだ上で15個のカテゴリにまとめて、９月の書籍リリースまでの重要度順にしたトップ5

上から順にいうと、9 月前の優先順はこうです。
1. 正規の実行入口が分かりにくく、古い経路に迷い込みやすい
2. 実行前に防げる失敗を preflight できず、壊れてから気づく
3. Web UI / static export / self-hosted 公開が壊れやすい
4. provider / API / 認証設定が一貫せず、使える環境でも「使えない」と見える
5. 失敗したときに原因が見えず、自己解決もコミュニティ支援も難しい

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 17:48:02_

「誰のための経路か」をもっと明確にしていくべきだったんだな、いろんなユーザのいろんなニーズを聞いて入口をどんどん増やしていった結果、メリデメ判断のできない人は「どの入口が正解なんだ？」となってしまう

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 17:48:18_

Codexのまとめ:
• 研究者・データサイエンティスト
Mac / Linux の CLI を使える前提でよい。ここでは `analysis-core` ベースのカスタマイズ性の高い CLI パイプラインが正規入口。
• 非エンジニアの試行錯誤ユーザ
CLI 作業は最小限で、レポート作成から確認まで Web UI で閉じる必要がある。ここでは admin / api / public-viewer を含む Web 経路が正規入口。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 17:50:47_

前者でWindowsを使ってる場合には「WSL2かDockerを使ってください」というスタイルで良いと思う。
後者に関しては「Gitを使わずZipでダウンロードしてsetup.batを起動」とかで動くようになるべきなんだろうな〜

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-19 18:30:21_

<https://x.com/mtkn1xbt/status/2056615102120648973?s=46&t=gkSZtjGEtUZPO0JCzBxCBw|https://x.com/mtkn1xbt/status/2056615102120648973?s=46&t=gkSZtjGEtUZPO0JCzBxCBw>
Twitterを情報源としたブロードリスニングをやりたい場合X APIではなくこの経路もありかも


#### 05月20日(Wed) - 5件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-20 12:05:55_

Issuesを読んで再検討したRefactoring Statusを元に、このドキュメントの記述が現状のソースコードとマッチしているか検証して次にやるべきことを検討する
<https://nishio.github.io/kouchou-ai-developer-wiki/analyses/refactoring-status/>

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-20 12:19:48_

言語化
• 広聴AI的な分析(Talk to the CityやJigsaw Sensemaker、farbrainやdivconなどの新しい試行錯誤など)をやりやすくするためにCLI版を使いやすくしていく
    ◦ この目的は多種多様な試行錯誤を容易にすることである
    ◦ 試行錯誤が容易であることは、一時的に壊れることや選択肢が多くて混乱することを引き起こしうるが、それは新しいものが活発に生み出されるためのコストである
    ◦ しかしこの選択肢だけでは研究者やデータサイエンティストだけしか使うことができない
• Web UIは専門的な知識がないユーザにも分析や自然言語のプロンプトの工夫を試行錯誤できるようにするためのものである
    ◦ なのでCLIなどでの技術的な作業は最小限にしなければならない
    ◦ Web上で完結するのが重要
    ◦ CLIでできることの全てができる必要はない(し、その複雑さはこのツールにとってはむしろネガティブである)

### **Shingo OHKI** in #2_開発_広聴ai _2026-05-20 13:16:12_

CLI版 / 分析コア -> 広聴AIの分析基盤 analysis-core
WebUI + analysis-core -> いわゆる広聴AI

みたいな呼び分けにすると分かりやすいのかもしれませんね。



### #7_雑談 (33件のメッセージ)

#### 05月14日(Thu) - 10件

### **Ohkubo KOHEI (kuboon)** in #7_雑談 _2026-05-14 13:32:19_

discord は slack よりはマシな気がするが、私としてはどうせ移行するならなんらかの oss のセルフホストでやっていきたいという気持ちがあります。
まだ良いのを見つけてませんが。

#### スレッド返信

**小野翔太** _2026-05-14 15:25:22_

セルフホストわかります。
discordもいつ制限されるかわからない→また移行を考えるとセルフホスト考えちゃいます

**小野翔太** _2026-05-14 15:25:56_

スーパーテキトーにググったらmatrixがいいそうな
<https://hide.me/ja/blog/matrix%E3%83%97%E3%83%AD%E3%83%88%E3%82%B3%E3%83%AB%E3%81%A8%E3%81%AF%E4%BD%95%E3%81%8B%E3%80%81%E3%81%9D%E3%81%97%E3%81%A6%E3%81%9D%E3%82%8C%E3%81%AF%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8/>

**Ohkubo KOHEI (kuboon)** _2026-05-14 16:09:15_

matrix は私はかなり初期からwatchしていて結構詳しいし自鯖を立てたこともありますが、惜しい感じです、まあでも今ある中では一番良いかもしれないので、賛同者が多ければ試してみたいです

**Ohkubo KOHEI (kuboon)** _2026-05-14 16:11:37_

matrix はプロトコルの標準化なので、サーバもクライアントも複数あります。

**小野翔太** _2026-05-14 17:33:21_

Discordは
• 入会チュートリアル的な機能がある
    ◦ 「何に興味がありますか？」みたいな質問でチャンネルやロール分けができる
    ◦ はじめに読んでね　を提示できる？
• やり取りが残る
• ロールがあり権限管理が細かくできる
• チャンネルのカテゴリ分けができる
あたりがslack無料版と比べると良いところかなと思ってます。ボイスチャットは本件ではいらんかなと。
そのあたりを考えつつ、ちょっと私もmatrix含め調べたり触ったりしてみます。
聞いたこと無いツールに登録するハードルと、クライアントアプリ名とサービス名が違うところ、特にスマホで使うときに混乱がありそうというところがセルフホストで気になるところです。

**Ohkubo KOHEI (kuboon)** _2026-05-14 17:57:49_

試しに最新版を1つおうちサーバにまたセルフホストしてみるかなー
使ってみるのが一番なので。

### **Ohkubo KOHEI (kuboon)** in #7_雑談 _2026-05-14 17:59:57_

@nishio.hirokazu
Log Exporter ってアプリ、今も運用していますか？

#### スレッド返信

**NISHIO Hirokazu** _2026-05-14 19:12:41_

自信がないがそれがOSSWeeklyReporterのためのログを出力してたやつじゃないかな

**Ohkubo KOHEI (kuboon)** _2026-05-14 22:06:44_

単にAPIキーを使って slack rest api を叩くのに使ってるということか。


#### 05月15日(Fri) - 5件

### **Shingo OHKI** in #7_雑談 _2026-05-15 09:53:59_

オンライン広告詐欺ではないですが、浜松駅のあちこちで警察官がこれを配ってました。
パッと見20人くらいいて驚きました。
この領域、世の中に対する影響は思っているよりも大きいのかも知れませんね。

#### スレッド返信

**Shingo OHKI** _2026-05-15 09:57:55_

メディアもいたので、警察が張っている大々的なキャンペーンなのかも知れませんね。
あんまりこういうの見たことなかったので驚きました。


#### 05月16日(Sat) - 2件

### **NISHIO Hirokazu** in #7_雑談 _2026-05-16 20:52:18_

@kuboon (from全体定例)
とりあえずログの抽出やdd2030のGitHubに置くことに関して異論は出てないので予定通りガンガンやっていきましょうというという気持ち。
SlackかDiscordかの議論はまだ色々な意見がある名の状況で、Outlineは「試してみるのは良いこと」な感じ。僕はまだOutlineの嬉しさがよくわかっていないがSlackログの本格的な出力が進むとそれを活用できるようになるのかな？？


#### 05月17日(Sun) - 2件


#### 05月19日(Tue) - 7件

### **U0AAL9KK2S1** in #7_雑談 _2026-05-19 17:54:20_

良い本でした
<https://www.seidosha.co.jp/book/index.php?id=4079&status=published|https://www.seidosha.co.jp/book/index.php?id=4079&status=published> 


#### 05月20日(Wed) - 7件



### #2_コアループ_process (30件のメッセージ)

#### 05月14日(Thu) - 8件

### **U0A67RK86BH** in #2_コアループ_process _2026-05-14 14:11:43_

<@U0A98JWF24B> <@U0A6P8CRT1Q> <@U0A7K64JT71> <@U0AAL9KK2S1>
お疲れ様です。市民熟議（DP）の日程が６月21日（日）に確定しました。当日の運営や参加者からの問い合わせ対応をお手伝いいただきたいのですが、ご都合いかがでしょうか？1週間前～前日＋当日にかけて徐々にやることが増えそうなので、可能な範囲でご協力いただきたいです！

#### スレッド返信

**U0AAL9KK2S1** _2026-05-14 14:57:23_

:clap:
どこまで動けるか、まずドキュメント見てみますね

**U0A6P8CRT1Q** _2026-05-14 15:22:08_

ご連絡ありがとうございます！承知しました。
キャッチアップできていないので、まっつんさん同様docs確認しておきます！

**U0A67RK86BH** _2026-05-14 15:23:57_

SOPに最新の流れ入れてます。説明時間設けることも可能なので、とりあえず6/21を確保いただければありがたいです！

**U0A98JWF24B** _2026-05-14 20:49:32_

6/21の週末にカンファレンスがあり参加できませんが、事前の準備でできることには取り組みます！

### **U0A67RK86BH** in #2_コアループ_process _2026-05-14 16:43:14_

<@U0A98JWF24B>
だめ元ですが・・
クロスマーケティング社と月曜16時～に打合せするので、ご都合つけばご同席いただければとてもありがたいです！

Zoom ミーティングに参加する
<https://us06web.zoom.us/j/82283320114?pwd=IP4WsiTI2q21yt0WrN1Nh8eryMgmjK.1>
ミーティング ID: 822 8332 0114
パスコード: 714783

#### スレッド返信

**U0A98JWF24B** _2026-05-14 20:50:54_

ありがとうございます！その時間は移動中の予定で、出先からのiPhoneからの参加か、不参加になってしまうかもしれませんが、可能な限り参加できるようにします

**U0A67RK86BH** _2026-05-14 21:42:46_

助かりますー！ありがとうございます


#### 05月16日(Sat) - 17件

### **U0A6CE44B2S** in #2_コアループ_process _2026-05-16 12:37:20_

<@U0A67RK86BH> cc @kensuzuki <@U09C3J7V960>
ブリーフィング資料は作成中ですが、クロスマーケティングに依頼する上で不足しているものって現状あと何かあるでしょうか？
西田さんと先ほど話をしたところ、若尾先生たちとの議論の中でコントロールグループは今回不要なので、T1（参加者募集時の詳細なアンケート）はいらず、T2（熟議前のアンケート）T3（熟議後のアンケート）が必要ということだと理解したのですがあっていますかね？

### **U0A67RK86BH** in #2_コアループ_process _2026-05-16 12:44:13_

コントロールグループの有無に関わらず、T1は必要と認識してました！資料を読む前後でどんな変化があるかという点です。コントロールグループは熟議をやるやらないの違いという認識なので、そもそも母集団が違う認識です。ただ、昨日私が抜けた後に若尾先生とそういう話になったのであればご放念ください！

### **U0A67RK86BH** in #2_コアループ_process _2026-05-16 12:59:52_

@kensuzuki <@U09C3J7V960> 
SODPの費用について、アリスからメールもらいましたが、8000ドルなので、130万ぐらいですかね？on demand platformは使わずになったので、人件費などが削られて200万もかからなくなったのかなと思います。こちらの金額いかがでしょう？

### **U09C3J7V960** in #2_コアループ_process _2026-05-16 13:35:58_

<@U0A67RK86BH>いや、昨日はそもそもその話になっていないです。コントロール以外の目的があるとしたらT1って何のためにアンケートとる必要あるんでしょうか？　あとアンケートとる対象は、縄田さんの認識だと１５００人に対して？　それとも３３０人に対してですか？

#### スレッド返信

**U0A67RK86BH** _2026-05-16 13:38:11_

若尾先生が冒頭で資料の前後の変化を知るためとおっしゃってませんでしたか？また、T1のサンプルとして共有いただいたものに基本属性以外の設問もありませんか？認識違いましたらご指摘下さい

**U09C3J7V960** _2026-05-16 13:56:04_

<@U0A67RK86BH> （<@U0A6CE44B2S>）
冒頭の5分ぐらい出ていなかったのでそのタイミングかも。

そもそもT1でアンケートとる/とらないの話って、
1. 層化抽出のタイミングでとるのは負担重すぎるのでは？　（アンケートやっておいて、「層化抽出の結果、あなたは対象ではありません（なので謝礼もなしです）」というのは負担重い）って話がリード定例で出て、
2. そのあとの若尾先生/縄田さん/西田/Aliceの打ち合わせで、「アンケートはT2とT3の二回だけでいいです」（対象者330人に、SODPやる前とSODPやった後。熟議の効果を測るのは研究者目的のnice to haveで、今回の件では不要。）という話が出て、
3. リード定例で健さんに「上記のとおりです」と伝えたところ、「でも論文だとやるって書いてあるよね。若尾先生に確認しよう」（キャプチャ。<https://jasr.or.jp/wp/asr/asrpdf/asr11/asr11_090.pdf>）となり
4. そのあと若尾先生に縄田さんがメール（5/1）
```基本情報や希望日程を聞くT1では、テーマに関するアンケートは特に実施しないという理解で正しいでしょうか？いくつか過去の文献を見ていると、テーマに関するアンケート調査も実施していそうな取組もあるように思えたのでお伺いする次第です。あくまでも熟議の前後で取得するT2・T3の比較がメインと理解しておりますが認識が誤っておりましたらご教示ください。
P34→<https://tama.sfc.keio.ac.jp/sest/guideline-dp.pdf>
P139 →<https://jasr.or.jp/wp/asr/asrpdf/asr11/asr11_090.pdf>```
5. 若尾先生から返信
```まずT1の件ですが、過去の日本での二つのT1の質問項目をまとめましたのでご覧ください。
<https://docs.google.com/spreadsheets/d/1OOPa0XkZTseSjMrOyOfohpjAW7bLMVI7FddI-1Y3WcU/edit?usp=sharing>
これを見ていただくとお分かりいただけますが、数多くの問いをT1の時点で設けております。というのはT1は通常の世論調査と同じ扱いとなり、T2はそれに加えて資料を読んだ影響、T3はさらに熟議の影響を測ることになりますt。つまり、通常の世論調査と熟議の効果を測るためにはT1とT3の比較が必要となってきます。年齢や性別といった属性情報は、東京都民を対象にやったDPではいわゆるT0の時点で属性の質問を聞いていて、さらに年齢や性別は世論調査会社が把握していたのでそれとマッチングさせました。ですので、今回利用される世論調査がどの程度把握しているかによって属性質問項目は変ってくると思います。```
っていうところでメール上は途切れていて、
6. 5/15打ち合わせ（冒頭の話）
かなと思います。

それで西田がわかってないところに戻るのですが、
①このT1のアンケートってmustで必要？（若尾先生の文章読むとマストであるとは読めない。「つまり、通常の世論調査と熟議の効果を測るためにはT1とT3の比較が必要となってきます。」と書いてあるのだが、SODPとして成立するためのmustなのか研究目的でのnice to haveなのか）
②もしmustであるならば対象の集団は？（これが1500とか300とかの話。クロスマーケティング社のパネルは100,000、そのあと層化抽出で1500→300という話だったと思いますがどのタイミングでT1アンケートを実施？）
③このT1をやるってことはクロスマーケティング社に連携済？（費用増にならない？）。T1アンケートやったけど選ばれなかった（謝礼無し）の人に対しての対応ってどうなったんだっけ？

ということなんですがすいません、私がわかっていないだけでしょうか？

**U09C3J7V960** _2026-05-16 14:00:34_

> T1のサンプルとして共有いただいたものに基本属性以外の設問もありませんか？
<https://docs.google.com/spreadsheets/d/1OOPa0XkZTseSjMrOyOfohpjAW7bLMVI7FddI-1Y3WcU/edit?gid=1682592971#gid=1682592971>
属性以外のpreferenceについて確認する質問が多く入っているのは認識しています。世論調査として厳格にやるなら小倉さん一人だと手におえない（専門家入れないといけない）ので、本当にやらないといけないんでしたっけ？（と今更気づきました）

### **U09C3J7V960** in #2_コアループ_process _2026-05-16 13:56:04_

<@U0A67RK86BH> （<@U0A6CE44B2S>）
冒頭の5分ぐらい出ていなかったのでそのタイミングかも。

そもそもT1でアンケートとる/とらないの話って、
1. 層化抽出のタイミングでとるのは負担重すぎるのでは？　（アンケートやっておいて、「層化抽出の結果、あなたは対象ではありません（なので謝礼もなしです）」というのは負担重い）って話がリード定例で出て、
2. そのあとの若尾先生/縄田さん/西田/Aliceの打ち合わせで、「アンケートはT2とT3の二回だけでいいです」（対象者330人に、SODPやる前とSODPやった後。熟議の効果を測るのは研究者目的のnice to haveで、今回の件では不要。）という話が出て、
3. リード定例で健さんに「上記のとおりです」と伝えたところ、「でも論文だとやるって書いてあるよね。若尾先生に確認しよう」（キャプチャ。<https://jasr.or.jp/wp/asr/asrpdf/asr11/asr11_090.pdf>）となり
4. そのあと若尾先生に縄田さんがメール（5/1）
```基本情報や希望日程を聞くT1では、テーマに関するアンケートは特に実施しないという理解で正しいでしょうか？いくつか過去の文献を見ていると、テーマに関するアンケート調査も実施していそうな取組もあるように思えたのでお伺いする次第です。あくまでも熟議の前後で取得するT2・T3の比較がメインと理解しておりますが認識が誤っておりましたらご教示ください。
P34→<https://tama.sfc.keio.ac.jp/sest/guideline-dp.pdf>
P139 →<https://jasr.or.jp/wp/asr/asrpdf/asr11/asr11_090.pdf>```
5. 若尾先生から返信
```まずT1の件ですが、過去の日本での二つのT1の質問項目をまとめましたのでご覧ください。
<https://docs.google.com/spreadsheets/d/1OOPa0XkZTseSjMrOyOfohpjAW7bLMVI7FddI-1Y3WcU/edit?usp=sharing>
これを見ていただくとお分かりいただけますが、数多くの問いをT1の時点で設けております。というのはT1は通常の世論調査と同じ扱いとなり、T2はそれに加えて資料を読んだ影響、T3はさらに熟議の影響を測ることになりますt。つまり、通常の世論調査と熟議の効果を測るためにはT1とT3の比較が必要となってきます。年齢や性別といった属性情報は、東京都民を対象にやったDPではいわゆるT0の時点で属性の質問を聞いていて、さらに年齢や性別は世論調査会社が把握していたのでそれとマッチングさせました。ですので、今回利用される世論調査がどの程度把握しているかによって属性質問項目は変ってくると思います。```
っていうところでメール上は途切れていて、
6. 5/15打ち合わせ（冒頭の話）
かなと思います。

それで西田がわかってないところに戻るのですが、
①このT1のアンケートってmustで必要？（若尾先生の文章読むとマストであるとは読めない。「つまり、通常の世論調査と熟議の効果を測るためにはT1とT3の比較が必要となってきます。」と書いてあるのだが、SODPとして成立するためのmustなのか研究目的でのnice to haveなのか）
②もしmustであるならば対象の集団は？（これが1500とか300とかの話。クロスマーケティング社のパネルは100,000、そのあと層化抽出で1500→300という話だったと思いますがどのタイミングでT1アンケートを実施？）
③このT1をやるってことはクロスマーケティング社に連携済？（費用増にならない？）。T1アンケートやったけど選ばれなかった（謝礼無し）の人に対しての対応ってどうなったんだっけ？

ということなんですがすいません、私がわかっていないだけでしょうか？

### **U09C3J7V960** in #2_コアループ_process _2026-05-16 14:00:34_

> T1のサンプルとして共有いただいたものに基本属性以外の設問もありませんか？
<https://docs.google.com/spreadsheets/d/1OOPa0XkZTseSjMrOyOfohpjAW7bLMVI7FddI-1Y3WcU/edit?gid=1682592971#gid=1682592971>
属性以外のpreferenceについて確認する質問が多く入っているのは認識しています。世論調査として厳格にやるなら小倉さん一人だと手におえない（専門家入れないといけない）ので、本当にやらないといけないんでしたっけ？（と今更気づきました）

### **U0A67RK86BH** in #2_コアループ_process _2026-05-16 14:07:04_

整理いただきありがとうございます！

1-2はスタンフォードDPとしてOKかを聞く必要があるのでメールで尋ねてみます。3については連携済みです。スクリーニングの内容が変化することに伴う費用増は特にきいてません。選ばれなかった人には特にこちらからの手出しはなく、あるとしたら調査会社がパネルに提供しているポイント付与程度ではないでしょうか。

### **U0A67RK86BH** in #2_コアループ_process _2026-05-16 14:09:30_

プロセスの話は私から尋ねますが、preferenceなどの設問詳細については、西田さんか小倉さんから若尾先生にお尋ねいただけないでしょうか？今日夜まで仕事で…すみません:bow:

### **Ken Suzuki** in #2_コアループ_process _2026-05-16 20:10:39_

<@U0A67RK86BH>何を手伝ってほしいのかわからないので、皆さんにお伝えください

#### スレッド返信

**U0A67RK86BH** _2026-05-16 21:08:12_

修正しました

**小野翔太** _2026-05-16 21:23:55_

<@U0A67RK86BH>
本日の週次全体定例にて（参照：<https://docs.google.com/document/d/1tBhaer67U9LbASfqPrg0rpmv0Tt4K7zFUTTzscKXj_I/edit?usp=sharing|議事録>）、processチームでDPの準備等の人手が足りないことを知りました。
<#C090HUWBBNG> にて募集をかけたいのですが、修正いただいた募集内容がどこにあるのかわからず…（すみません）教えていただけると幸いです！

もしくは直接<#C090HUWBBNG> に書いていただいても問題ありません！

**U0A67RK86BH** _2026-05-16 22:11:04_

大変助かります、ありがとうございます！健さんから追って展開予定の週次レポートに詳細記載いたしましたが、教えていただいたチャンネルでも募集させていただきます！


#### 05月18日(Mon) - 3件

### **U09C3J7V960** in #2_コアループ_process _2026-05-18 16:43:53_

<@U0A67RK86BH> 割り込んですいません、私の方で直接聞きました！
```Dear Professor Wakao (cc: Alice),
(日本語は英文の後に続きます / Japanese text follows below.)

Thank you, as always, for your continued support. This is Naofumi from DD2030.

The DP date has been confirmed for Sunday, June 21st (JST). As we proceed with preparations, several methodological questions about the SODP have come up. We would be grateful for your guidance.
We have 5 questions in total.

■ On the T1 Survey (to Professor Wakao)

1. After reviewing your email from May 4th and the past T1 questionnaire spreadsheet you shared, we discussed the matter internally at DD2030. In your explanation, you noted that "comparing T1 and T3 is necessary to measure the effect of deliberation against a standard public opinion poll." We understand this to mean that the comparison is necessary for research purposes. Could you confirm whether this is correct? In other words, is conducting a T1 survey (including topic-specific questions) a mandatory requirement for the SODP to be methodologically valid? Or is it more accurately positioned as a "nice to have" for the research goal of verifying the deliberation effect?

2. If T1 is mandatory, which population should be the target? Our current flow is: Cross Marketing's panel of 100,000 → stratified sampling down to 1,500 → final participants of approximately 330. We would appreciate your advice on at which stage T1 should be administered (at the 1,500-person stage, or the 330-person stage) from a methodological standpoint.

3. If T1 is mandatory, on what basis should we design the T1 "opinion poll" (topic-specific questions)? Looking at the T1 questionnaire from the Tokyo solar power DP that you shared, we observed many questions on topic-linked specific preferences (e.g., "Should the current solar power target be maintained or raised?", "Trust in various organizations") and knowledge (e.g., the share of solar in Japan's energy mix), with the same questions repeated at T2 and T3 to measure change.

For our case, should we use the same specific propositions that will be asked at T2 and T3 (corresponding to topics a–j in the "Small Group Deliberation Topics" section below) for T1 as well? Or should T1 ask questions at one level of abstraction higher, capturing overall awareness and attitudes toward the theme (e.g., "the appropriate role of government in addressing online ad fraud," "general perceptions of platform operator responsibility")? We would appreciate your guidance.

The purpose of this DP is to report to the government: "After deliberation, the level of agreement with this proposal is X%." With June 21st approaching and our timeline becoming tight, we would like to clarify the minimum set of procedures necessary for the SODP to be valid. 
We apologize for the delay since our last set of questions, and appreciate your follow-up guidance on the above.

■ On the Small Group Deliberation Topics and Facilitation Protocol (to Alice, cc: Professor Wakao)

Alice,

Following up from our discussion last Friday — we wanted to share the topics we are currently considering for the small group deliberation, and ask for your guidance on two protocol-related points.

The topics we currently envision for small group deliberation are as follows (the exact wording will be refined):

a. Advertising platform operators should require official identity verification of all advertisers as a mandatory condition for ad placement.
b. Advertising platform operators should require labeling for ads generated or optimized by AI.
c. Advertising platform operators should bear a social responsibility to remove ads identified as fraudulent within a defined timeframe (e.g., 24 hours).
d. Advertising platform operators should bear liability, including compensation, for damages caused by fraudulent ads they have published.
e. The government should develop and operate an integrated system for reporting fraudulent ads, verifying facts, and requesting removal from operators — or alternatively, this should be carried out by a third-party body or quasi-governmental organization.
f. In Taiwan, government measures reduced damages from online ad fraud to roughly 1/30. When applying similar regulation in Japan, platform operators should be required to submit damage-reduction implementation plans, with the government monitoring execution.
g. Large advertising platforms should provide a free API enabling regulators and researchers to detect fraudulent ads in real time.
h. For high-risk categories such as investment, crypto assets, and side-job solicitations, harm prevention should take precedence over freedom of expression, with AI-based pre-screening and pre-blocking as the default.
i. Advertising platform operators should conduct identity-existence verification (KYC — verifying real-person existence, not real-name disclosure) for all general users, not only advertisers.
j. Large messenger services should be required to perform KYC on the creators of investment/asset-management groups above a certain size, and to register a domestic point of contact and responsible party.

With this in mind, we have two questions for you:

4. In our previous meeting, you indicated that 4–8 topics per session (60 minutes of discussion + 15 minutes for questionnaire selection = 75 minutes) is a reasonable guideline. Given the granularity of the topics above, how many topics would you realistically recommend (4? 6? Could we manage 8?)? Is there a standard guideline in the SODP methodology for how many minutes per topic per participant should be allocated?

5. What is the protocol for cases where discussion on a given topic becomes either highly animated or stagnant in a small group? For example, if we plan 6 topics in 60 minutes, is there a mechanism that automatically moves the group to the next topic at the 10-minute mark even if discussion is still active — or is pacing left to the group's discretion (or the moderator's judgment)?

Thank you very much for your time. We look forward to your guidance.

Best regards,
Nishida

---

若尾先生（cc: Alice）

いつも大変お世話になっております。DD2030の西田です。

DPの開催日が6月21日（日）に確定し、準備を進めるなかで、SODPの方法論に関わるご質問が出てきましたので、ご教示いただけますと幸いです。
合計で5つ質問がございます。

■ T1アンケートの取り扱いについて（若尾先生宛）

1. 先日いただいた5/4のメールおよび過去のT1質問項目シートを拝見し、DD2030内で論点を整理しておりました。先生のご説明では「通常の世論調査と熟議の効果を測るためにはT1とT3の比較が必要」とのことでしたが、
これは研究目的での比較分析にとって必要、という理解で正しいでしょうか。つまり、T1アンケート（テーマに関する設問を含むもの）の実施は、SODPとして成立させるための必須要件でしょうか。
それとも、熟議効果の検証という研究目的での実施が望ましい（nice to have）という位置づけでしょうか。

2. 仮に必須である場合、対象母集団はどの段階の集団を想定すべきでしょうか。今回のフローでは、クロス・マーケティング社のパネル10万人 → 層化抽出で1,500人 → 最終参加者約330人、という想定で進めており、
　T1をどの段階で実施するのが方法論上適切か（1,500人段階か、330人段階か）をご助言いただけますと助かります。

3. 仮に必須である場合、T1の「世論調査」（テーマに関する設問）は、どのような基準で設計すべきでしょうか。先日共有いただいた東京都太陽光発電DPのT1質問項目シートを拝見すると、
　テーマと連動した具体的な選好（例：「現在ある太陽光発電の達成目標を維持するか、引き上げるか」「各団体への信頼度」など）や知識（例：日本の電源構成に占める太陽光の割合）に関する設問が多数並んでおり、T2・T3でも同一設問を聞いて変化を測定する構造とお見受けしました。
　今回の場合、T2・T3で問う具体的な提言（下記「小グループ討論で扱うテーマ案」のa〜jに相当する設問）をT1でもそのまま援用してよいのか、
　それともT1では一段抽象度を上げたテーマ全体の認知・態度（例：「オンライン広告詐欺対策における政府の関与のあり方」「プラットフォーム事業者の責任に関する一般的な認識」など）を問うべきなのか、ご助言いただけますと助かります。

今回のDPの目的は、政府に対して「この提言についての熟議後の賛同率は●●%です」とお伝えすることです。6月21日開催に向けて時間がタイトになってきたこともあり、SODPとして成立させるために必要な最小限の実施手順を知りたく思っております。先日ご質問してから時間があいてしまって恐縮ですが、上記の通りフォローアップの質問をさせてください。

■ 小グループ討論で扱うテーマ案と進行プロトコルについて（Alice宛・若尾先生CC）

当日小グループで議論する内容については、現時点で以下のテーマを想定しています（質問文は今後ブラッシュアップ予定）。

a. 広告プラットフォーム事業者は、すべての広告主に対して公的な身元確認を広告掲載の必須要件とすべきである。
b. 広告プラットフォーム事業者は、AIによって生成・最適化された広告に対し、ラベル表示を必須要件とすべきである。
c. 広告プラットフォーム事業者は、詐欺だと判明した広告について、一定時間（例：24時間）以内に削除する社会的責任を負うべきである。
d. 広告プラットフォーム事業者は、掲載された詐欺広告による被害に対して、賠償等の責任を負うべきである。
e. 政府は、詐欺広告の通報・事実確認・事業者への削除依頼を一気通貫で行うためのシステムを開発・運用すべきである。あるいは、この実施主体は第三者機関・政府外郭団体であるべきである。
f. 台湾では政府による対策で詐欺広告被害額が約30分の1まで減少した。日本でも同様の規制を適用するにあたり、プラットフォーマーに被害削減の実行計画を提出させるべきである（プラットフォーマーが実行したかどうかを日本政府はモニタリングすべきである）。
g. 大規模広告プラットフォームは、規制当局や研究者が詐欺広告をリアルタイムで検知するためのAPIを無償で提供すべきである。
h. 投資・暗号資産・副業勧誘などの高リスク分野については、表現の自由よりも被害防止を優先し、AIを活用した事前審査・事前遮断を原則とすべきである。
i. 広告プラットフォーム事業者は、広告だけでなくすべての一般ユーザーに対して実在性確認（KYC、※実名ではなく実在性）を行うべきである。
j. 大規模なメッセンジャーサービスは、一定規模以上の「投資・資産運用を目的とするグループ」に対して、開設者の本人確認（KYC）義務および国内連絡先・責任者登録を義務付けるべきである。

これを踏まえて、以下2点ご教示ください。

4. 先日のミーティングでは、1セッション（60分の討論＋15分のアンケート選択 ＝ 75分）あたり4〜8テーマが目安とのお話がありました。上記のような粒度のテーマの場合、現実的に何個程度を想定するのが妥当でしょうか（4個？ 6個？ 8個まで可能？）。SODPの方法論上、1テーマあたりの参加者一人あたりの発話時間の目安は決められていますでしょうか。
5. 小グループの討論で、あるテーマで議論が盛り上がった場合、あるいは逆に議論が進まなかった場合の進行プロトコルはどうなっていますでしょうか。例えば60分で6テーマを想定する場合、1テーマ10分を超えても議論が継続しているときに、強制的に次のテーマへ移行する仕組みがあるのか、それともグループ内の判断に委ねられるのか、ご教示いただけますと幸いです。

お忙しいところ恐縮ですが、ご教示のほどよろしくお願いいたします。

西田```

#### スレッド返信

**U0A67RK86BH** _2026-05-18 17:24:50_

<@U09C3J7V960>
ありがとうございます。恐れ入ります！
調査会社ともちょうど打合せをしてきて、層化抽出のプロセスや今後のタイムラインを聞いてきました。以下にまとめているので御覧ください。もしT1アンケート（テーマに関する設問を含むもの）を実施するならば、25日（月）までにアンケート会社に内容を共有する必要があります。また、調査会社によれば1500人の段階（層化が終わったタイミング）でテーマに関する設問を実施する想定のようです。
<https://docs.google.com/document/d/1isqRSUvvympiNp8uKBWYHIAI8-CGNjePriZUfrN4qig/edit?nstoken=7SOY%2FFbMog3%2FTQb%2FYOdCufM%2FS5ick3VzTEWaurLsvKwJnToZN0npY9yTnZVt5XjFxVe6%2F9LhfYtXoro%2FPB%2BPzvnIZI5N8H%2B1ZJsFObeSSA85jtrjaof7LgjsYkovbw%2FXUry6rAVU%2FkwVBEi29DlXAiRfWpBOFvS3TCQfrz6luMsD%2FoQuY9oQ1sB%2BnMZrW52Qlghp10R%2Fbg72r18RrAUZaeqmEK0mpyJtahgf%2FFFJHGL9AzbRgxsey%2FbK5VvjlGd4RanxARlbNC8p6inM18fsauHzm%2FIJKuq2WpH3jrdaPSSrXfqr%2BLpYLPRpYhRl88GT%2FjylwtxT2EfsKImW3esZZztAp9MvvYPRtk9ISLGliWwxGZ7vvirSFDO10PeYO6ya3OGeE51MUEG6DCOv5votSFZukdaTh4Tl0lTITeICzIxgLim%2F1Yzy6exXXP%2BGRO4jq9DNU9J4fwPF2cb9K3D4d1oXcnvqUgssshJN9YoblYjn6KIt1IRRtZNtic6xyAnv6%2BBgPiiDjEnBQf5ql4LzfM9qkot2uC9rJQFm4BbHSiUzdqVqJbRxsu38n%2F2svDHxFKznN%2Fo4iSPBKMpPKnjZ2acO0wd9hXYqYJdDVyMFjZEPa1X5R1ap8LzhgMeXYDKXP%2BhmZ6Q7v572w%2FWzuJkE%2Bxw%3D&nscheck=oaJgezRr558D9yfEzNr7Gg%3D%3D&tab=t.1pri05nn1e8d#bookmark=id.hcej4pbpbpu1>


#### 05月19日(Tue) - 1件


#### 05月20日(Wed) - 1件

### **U09C3J7V960** in #2_コアループ_process _2026-05-20 08:40:42_

若尾先生からの回答
```西田さん、

ご連絡いただきありがとうございます。

（１）T1について
T１はサンプル＝330人の段階です。重要なのは、330人（つまりT1＝DP参加者でもある）の内訳が男女、年齢層、地域が母集団（日本人口）とマッチしている必要があります。

（２）＞今回の場合、T2・T3で問う具体的な提言（下記「小グループ討論で扱うテーマ案」のa〜jに相当する設問）をT1でもそのまま援用してよいのか、
　それともT1では一段抽象度を上げたテーマ全体の認知・態度（例：「オンライン広告詐欺対策における政府の関与のあり方」「プラットフォーム事業者の責任に関する一般的な認識」など）を問うべきなのか、ご助言いただけますと助かります。

T1に意味があるのはT2とT3と比較できるからであり、つまりT1の内容はT2、T3の内容でもあります。ですのでT1で質問したものがT2やT3に含まなかった場合、無駄になってしまいます。まとめますと

T1＝［属性の質問（職業、収入、持ち家）及び普段の行動（ネット使用頻度など）］＋T2
T2
T3＝T2＋T3のみの設問（参加満足度など）

となります。

（３）小グループでのテーマについて
これはテーマによって違ってきますので何とも言えませんし、主催者側がどこまで一つのテーマを掘り下げたいのかにもよります。また参加者が知らないテーマの場合、掘り下げるのが難しいので逆に多くのテーマを入れることができる、とも言えます。４～８は妥当だと思いますが、具体的にどんなテーマを話し合うのかを見てみないと、というのが正直な感想です。

プラットフォームでは一人の一回での発言時間は90秒だったと思います。90秒が過ぎると自動的に次の人に移動します。発言したい人は「発言する」をクリックすると発言者リストに登録されて自分の発言が来るのを待つという仕組みです。また、全く発言していない参加者には「発言してください」というメッセージがその人の画面だけに現れます。一人が発言できる回数の制限はありません。また、一定の参加者が「次のテーマに進む」というのをクリックすると次のテーマに移動します。誰も（またはごく少数者だけ）それをクリックしない場合は設定時間が過ぎたら自動的に次のテーマに移動します。

（４）その他
アンケートと資料の改定版ができましたらその都度お送りください。

また今後ブラッシュアップするということでしたが、例えば
＞g. 大規模広告プラットフォームは、規制当局や研究者が詐欺広告をリアルタイムで検知するためのAPIを無償で提供すべきである。

において、一般人がAPIを理解できているのかが気になります。

また、6月21日は父の日ですが、その影響は心配しなくても大丈夫でしょうか。


若尾信也```



### #2_コアループ_オンライン広告詐欺対策_市民熟議会議 (19件のメッセージ)

#### 05月16日(Sat) - 19件

### **NISHIO Hirokazu** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-05-16 09:58:25_

あと2分くらいで始まると思いますが入り口を発見できていないです

### **NISHIO Hirokazu** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-05-16 09:58:55_

あっみつけました

### **Shingo OHKI** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-05-16 09:59:14_

このようなエラーがでて参加できなかったです

5/16 10:00-12:00
Meeting chat link
<https://us06web.zoom.us/launch/jc/86240244788>

ミーティング ID: 862 4024 4788
パスコード: 756926

### **NISHIO Hirokazu** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-05-16 09:59:27_

> ホストの組織に属していないメンバーは、このミーティング チャットに参加できません。参加するにはホストに許可を求めてください。

### **NISHIO Hirokazu** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-05-16 09:59:30_

同じく

### **NISHIO Hirokazu** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-05-16 10:00:00_

スライドは発見したので読みます

### **中山心太（tokoroten）** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-05-16 10:03:11_

パスコード直打ちで入れそうなんですが、ホストが入室許可してくれません

### **U09C3J7V960** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-05-16 10:03:27_

すいません、いま対応中ですのでしばしおまちください。

### **Shingo OHKI** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-05-16 10:04:28_

先程来たメールのリンクで入れました。ありがとうございます！

### **U09C3J7V960** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-05-16 10:04:54_

すいませんでした！よろしくお願いします。

### **Shingo OHKI** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-05-16 12:16:44_

今日参加させていただいた感想です
とても面白かったです！

グループごとに（ファシリテーターによって？）議論のやり方に違いがありそうだなと感じました
- 全員の意見を幅広く扱おうとする方向のグループ
- 特定の意見について議論を深める方向で話をしているグループ

また、自分が参加していないグループの議論の様子も後から見ることができたら、議論の内容に触発されてさらにアイディアが出る可能性がありそうで、この少人数の同期した議論を元に、非同期でそれに参加することができれば300人の同時開催だけでなく、もっと多くの方からアイディアを集めることも出来そうだなと思いました

#### スレッド返信

**Shingo OHKI** _2026-05-16 17:53:26_

<https://docs.google.com/spreadsheets/d/1z3980f96Vt_6HNTefq2w-dCLNPwk2Ukj7ilFRMSGuIA/edit?gid=0#gid=0|グループ１>のシートを見ると、意見の上の方にそれぞれのアイディアがあり、下の方でそのアイディアに対して別の人が様々な人がコメントをしているように見えました。

これは非同期でも（ある程度）できるということだと思うので、スケールする可能性ありそう

というのと、グループごとにこの議論のやり方が微妙に違っているのだなと思いました。（バラバラがいいのか、優れたやり方に統一する方がいいのかは分かってませんが）

**Shingo OHKI** _2026-05-16 17:54:59_

議論の時間の大半が、個人で書いた意見を説明する時間になってしまっていたので、それはある程度事前にやっておいて、それを元に議論することにフォーカスできるとよさそうだなと思いました

**Shingo OHKI** _2026-05-16 17:55:47_

資料を読んで個人の意見をシートに書くところまでは、必ずしも同期的にやる必要はないのかもしれません

**Shingo OHKI** _2026-05-16 18:11:29_

あと、今日参加して少し感じたこととして、「この活動ならではのアイディアを出す」ことの意義は理解しつつ、オンライン詐欺広告の被害を減らすという目的から見ると、必ずしも新規性のあるアイディアが出ること自体が最重要なのかは少し気になりました。

### **NISHIO Hirokazu** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-05-16 12:17:10_

SNSで紹介しようかと思ってWebサイトを見てたんですけど
<https://coreloop.dd2030.org/online-ad-fraud-prevention>
> 落合陽一 ⽒〔 〇〇 〕
この肩書きがブレースホルダーのまま露出されちゃってるのはミスです？

#### スレッド返信

**U09C3J7V960** _2026-05-16 12:18:59_

ミスですので修正お願いします！（<@U091ZN08WQH> ）

**U09C3J7V960** _2026-05-16 12:19:22_

@nishio.hirokazu
<https://camp-fire.jp/projects/930941/view>
クラファンの案内もお願いします！

### **中山心太（tokoroten）** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-05-16 12:22:41_

こんな感じで最近はディープフェイクツールを仕事として作ってるので、作る側の技術で協力可能であれば、おっしゃってください。



### #0_全体お知らせ (7件のメッセージ)

#### 05月16日(Sat) - 7件

### **Slackbot** in #0_全体お知らせ _2026-05-16 19:00:03_

リマインダー : <#C08FL58LK8V> :mega: 1時間後より、全体定例会を開催します！ :clock8: 20:00-21:00 :link: <https://meet.google.com/fhn-rcoj-sci> :memo: <https://docs.google.com/document/d/1tBhaer67U9LbASfqPrg0rpmv0Tt4K7zFUTTzscKXj_I> • プロジェクトにまつわる進捗報告・相談・TODOの決定を行う会です • どなたでも参加歓迎です！興味ある方はぜひ覗きに来てください

#### スレッド返信

**Shingo OHKI** _2026-05-16 19:21:22_

最近あまり参加できていなかったので話の流れを追っかけようと思ったのですが、直近の会議の動画って以下とは別のところにあったりしますか？
<https://drive.google.com/drive/folders/1H55HTB0_rwargUwUJvEPg76Wz13i2-bp>

**小野翔太** _2026-05-16 19:41:53_

いえ、私がサボっててフォルダに移動してないだけです！
今、動画移動しました

**佐藤まみ** _2026-05-16 20:51:31_

完全に思いつきですが、その過去ログ格納リンク、毎週のリマインダーに追記してもいいかも…？

*▼例文*
> リマインダー : <#C08FL58LK8V> :mega: 1時間後より、全体定例会を開催します！
> :clock8: 時刻
> 20:00-21:00
> :link: Google Meet
> <https://meet.google.com/fhn-rcoj-sci>
> :memo: 議事録
> <https://docs.google.com/document/d/1tBhaer67U9LbASfqPrg0rpmv0Tt4K7zFUTTzscKXj_I>
> • プロジェクトにまつわる進捗報告・相談・TODOの決定を行う会です
> • どなたでも参加歓迎です！興味ある方はぜひ覗きに来てください
> :open_file_folder:過去の録画格納先は<https://drive.google.com/drive/folders/1H55HTB0_rwargUwUJvEPg76Wz13i2-bp|こちら>

**佐藤まみ** _2026-05-16 20:51:52_

（私も最近出れてなくて、格納フォルダ探してました）

**小野翔太** _2026-05-16 21:34:01_

@mami.s.dasein
ありがとうございます！設定してみました！

### **小野翔太** in #0_全体お知らせ _2026-05-16 21:32:29_

  毎週金曜日 19:00 , 日本標準時 にこのチャンネルでこれをリマインドするよう設定しました : “!here :mega: 1時間後より、全体定例会を開催します！
:clock8: 時刻
20:00-21:00
:link: Google Meet
https://meet.google.com/fhn-rcoj-sci
:memo: 議事録
https://docs.google.com/document/d/1tBhaer67U9LbASfqPrg0rpmv0Tt4K7zFUTTzscKXj_I

• プロジェクトにまつわる進捗報告・相談・TODOの決定を行う会です
• どなたでも参加歓迎です！興味ある方はぜひ覗きに来てください

:open_file_folder:過去の録画格納先
https://drive.google.com/drive/folders/1H55HTB0_rwargUwUJvEPg76Wz13i2-bp?usp=sharing” 



### #2_コミュニティ運営 (7件のメッセージ)

#### 05月15日(Fri) - 3件

### **Slackbot** in #2_コミュニティ運営 _2026-05-15 19:00:13_

リマインダー : <!here> 本日20時より、コミュニティ運営定例会議を開催します！:mega: :clock9: 20:00-21:00 :link: <https://meet.google.com/deb-krky-zxx> :memo: <https://docs.google.com/document/d/1dn9R9WLaGNMDO-t1w7m8-2gZRSrgZI4glDvSIr101J4/edit?usp=sharing> • コミュニティ運営にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！ • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！

#### スレッド返信

**tahashika（たはしか）** _2026-05-15 19:52:39_

度々すみません、、、今日も時間合わなそうです:bow:
来週こそ一度顔出します

### **Slackbot** in #2_コミュニティ運営 _2026-05-15 20:00:26_

リマインダー : <!here> 只今より、コミュニティ運営定例会議を開催します！:mega: :clock9: 20:00-21:00 :link: <https://meet.google.com/deb-krky-zxx> :memo: <https://docs.google.com/document/d/1dn9R9WLaGNMDO-t1w7m8-2gZRSrgZI4glDvSIr101J4/edit?usp=sharing> • コミュニティ運営にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！ • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！


#### 05月18日(Mon) - 3件

### **U0A77QV20BF** in #2_コミュニティ運営 _2026-05-18 10:47:36_

以下は、「Discordへの移行」に関する、全体定例会（5月16日・土、20:00～）での議論を受けての私見です。

①　鈴木さんのほうから、Slackでは過去ログが三か月しか保存されないことと、他の方々から有料版の値段をお聞きした時点で、「Discord一択だな」と思いました。私は過去ログを非常に頻繁に拝見させていただいておりますが、それを引っ張り出すのになんらかの手間が必要になったら見なくなるだろうと思います。そうなると（少なくとも私にとっての）ワークスペースの価値は半減するだろうとも。ましてや自分にDMして保存している過去ログまで３か月で見れなくなるようだと、DDについて色々と考えを巡らす上で大打撃です。

②　これも鈴木さんのほうからご指摘があった、「Slackへの加入の技術的困難」も、優秀なエンジニアである私の知人が加入する際、非常に苦労したという事実が証明済みです。こうしたことに長けているはずのこの知人が、あるコア・メンバーの方の手を借りなければ加入出来なかったとなると、多くの人が同じ理由で参加を断念しているのではないかと考えられます（この知人もコア・メンバーのサポートがなければ加入していなかったでしょう）。
	私は、1月12日に開催されたKickof Meetingへの申し込みフォームを鈴木さんのXで見つけ、それに応募したらいつの間にか入れるようになっていて、未だにどうしてそうなったのかは分かっていません（笑）。

③　Tokorotenさんから御指摘にあった「Slackにおける各コミュニティへのオンボーディングに纏わる困難」も、より多くのメンバーの積極参加の大きな障壁になっていると思われます。かれこれ４か月以上、頻繁にSlackを訪れている私でも、未だに路頭に迷うことがあります。ましてや、参加当初は右も左もわからない状態で、各コミュニティの定例会を含む種々のミーティングに頻繁に参加するなどすることで、徐々にコアメンバーの方々から様々な形でのサポートをいただくようになり、フェード・アウトせずに済んでいます。
	逆に言えば、新規メンバー側の加入当初からの積極的なコミットメントと、既存メンバーのマインドフルなサポートの両方がないと、積極参加どころか、メンバーシップ継続も儘ならないというのが現状であり、その原因の一つとして「Slack問題」があるように思われます。

④　私は、デジタル民主主義に関係する或るワークショップへの参加をきっかけにDiscordを頻繁に使用しておりましたが、上記のような問題は一切ございませんでした。このワークショップ参加者のマジョリティは、（多くの非エンジニアを含む）自治体の職員やコミュニティ活動家といった方々でしたが、私も含め、上記のようなSlackに纏わる問題は一切なく、多くの方々がワークスペース上で活発な交流をされておられました。

これらのことから、Discordへの移行が、中長期的には様々な面で2030の活性化に繋がるのではないかというのが、私の私見です。

#### スレッド返信

**Ohkubo KOHEI (kuboon)** _2026-05-18 14:53:58_

slack 問題については同意できる部分は多々あるのですが、 discord へ移行する事でそれらの問題がどの程度解決するのか？というのは少々疑問はあります。
私は日常的に discord も使ってますが、アレはアレでゲームの広告みたいなのとか 「Nitroを購入しよう！」みたいなのが随所に挟まってきます。そういうものだと知らない人には slack 以上に受け入れ難いのでは？という懸念もあります。

**Ohkubo KOHEI (kuboon)** _2026-05-18 15:00:45_

なお、過去ログについては slack 上からは消えますがデータは取得できるので、例えば '/log 台湾' のような slash command で検索できるようにする、といったようなことは無償プランの範囲内でやる気次第で可能です。AI を噛ませて自然言語で過去ログに対して質問する、みたいなことも可能性があります。


#### 05月19日(Tue) - 1件



### #2_コアループ_tech (4件のメッセージ)

#### 05月14日(Thu) - 1件

### **中山心太（tokoroten）** in #2_コアループ_tech _2026-05-14 13:00:26_

そういえば、仕事でディープフェイクツールを作ってるので、ディープフェイクのアルゴリズムはだいたい理解できるようになってきましたので、必要だったら解説します。
（InsightFaceのライセンス料が高すぎるので、だったら自分で作るわ、ってなってる）


#### 05月15日(Fri) - 2件

### **Ryoma Kawabe Yuki** in #2_コアループ_tech _2026-05-15 17:34:58_

非同期でできそうなことがおおいので、今週も定例スキップしましょうか。

#### スレッド返信

**Shutaro Aoyama (ぶるーも)** _2026-05-15 19:58:07_

了解です！


#### 05月16日(Sat) - 1件

### **中山心太（tokoroten）** in #2_コアループ_tech _2026-05-16 12:19:26_

最近仕事で作ってるディープフェイクツールはこんな感じ

左下が業界最高性能のInsightFaceのinswapper
右下が私が現在作っているバージョン
（交換先の顔は画像生成AIで作った適当な画像）

inswapperの商用ライセンスが高いので、１からディープラーニングをぶん回して自作で作ってます



### #2_開発_polimoney (2件のメッセージ)

#### 05月16日(Sat) - 1件

### **Slackbot** in #2_開発_polimoney _2026-05-16 19:00:06_

リマインダー : <#C08FL5L6GSH> :mega:Polimoney開発会議を開催します！:mega: :clock7:19:00-20:00（毎週土曜日） :link:<http://meet.google.com/myy-ptwx-rsu|meet.google.com/myy-ptwx-rsu> :memo:<https://docs.google.com/document/d/19Kn6ekK3twMVcVaSyUgptvmfzrXEJezA6GXTbPXjm9M/edit?tab=t.0>  • 開発にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！  • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！


#### 05月19日(Tue) - 1件

### **小野翔太** in #2_開発_polimoney _2026-05-19 11:51:46_

@shumizu418128 <@U099TAD6RKL>
きたかも



### #2_broad-listening-book (2件のメッセージ)

#### 05月15日(Fri) - 1件

### **U0A77QV20BF** in #2_broad-listening-book _2026-05-15 15:36:45_

現在、同書を序文から通して読ませていただいているところですが、00（「本書のよみかた」）から4-2（「国民民主の…」）までは「です・ます」調で、序文および4-3以降の半分強は「だ・である」調になっておりました。すでにお気づきかもしれませんが、一応ご報告させていただきます。


#### 05月18日(Mon) - 1件

### **Slackbot** in #2_broad-listening-book _2026-05-18 19:00:22_

リマインダー : <!here> 本日20時より、ブロードリスニング本執筆会議を開催します！:mega: :clock9: 20:00-21:00 :link: <https://meet.google.com/feh-cnpt-nhq> :memo: <https://docs.google.com/document/d/1plggszRTxEEYUcZuCLiHkPrBsMtxr3RQpctKtZe5y4M> • ブロードリスニング本執筆にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！ • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！



### #2_コアループ_communication (2件のメッセージ)

#### 05月15日(Fri) - 2件

### **U0A821PG3PA** in #2_コアループ_communication _2026-05-15 06:29:57_

<@U09C3J7V960> 
明日のワークショップ、井上さんは「欠席」となります。よろしくお願いします！
（参加申込シート、こちらで編集できなかったのでそのままです）

### **U0A821PG3PA** in #2_コアループ_communication _2026-05-15 06:35:36_

<@U091ZN08WQH> （ <@U09C3J7V960>）※急ぎません！

日テレ 井上さんより、
ストップ詐欺広告の通報数が1000を超えたので、これらの元データを共有いただけないでしょうか、とのことです。可能でしょうか:man-bowing:

前回共有した約300件だと、新しい分析、発見が得られなかったとのこと。



### #2_コアループ_policy (1件のメッセージ)

#### 05月14日(Thu) - 1件

### **Ken Suzuki** in #2_コアループ_policy _2026-05-14 14:00:58_

<@U0A6CE44B2S> 落合さんが前半1時間参加できるのですが、車の中からの参加になるので、事前に個人ワークアウトはやっておきたいそうです。西田さんと連携して、事前に落合さんにやっておいてもらえるようにできませんか。



### #8_人数推移 (1件のメッセージ)

#### 05月20日(Wed) - 1件

### **dd-bot** in #8_人数推移 _2026-05-20 09:05:02_

:bar_chart: *2026-05-20* メンバー数: 1591人（前日比: 1人）


