# 2026年05月21日～2026年05月27日のSlack活動まとめ

今週は **14個**のチャンネルで合計**130件**のメッセージがやり取りされました。

## チャンネル別アクティビティ

- **#2_開発_広聴ai**: 63件のメッセージ
- **#2_コアループ_process**: 17件のメッセージ
- **#2_開発_広聴ai_アルゴリズム開発**: 13件のメッセージ
- **#2_broad-listening-book**: 7件のメッセージ
- **#dd_prance_event2026**: 4件のメッセージ
- **#2_開発_polimoney**: 4件のメッセージ
- **#0_全体お知らせ**: 4件のメッセージ
- **#7_雑談**: 4件のメッセージ
- **#2_コアループ_tech**: 3件のメッセージ
- **#2_開発_いどばた**: 3件のメッセージ
- **#3_ボードメンバーロール**: 3件のメッセージ
- **#8_人数推移**: 2件のメッセージ
- **#2_コミュニティ運営**: 2件のメッセージ
- **#2_新しいプロジェクトの種**: 1件のメッセージ

## チャンネル別詳細

### #2_開発_広聴ai (63件のメッセージ)

#### 05月21日(Thu) - 12件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-21 00:02:17_

なるほど、それはその通りですね。
Web版を「広聴AI」、コア部分を「広聴AIの分析エンジン」とか呼ぶとわかりやすいのかも？

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-21 00:02:34_

車のエンジンのメタファー

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-21 00:03:44_

エンジンの研究をする人はエンジンが露出しててすぐいじれる方が良いが、車に乗りたい人にとってはエンジンが露出してると危なっかしいので安全に運転できるように乗り物の形にする必要がある

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-21 02:43:56_

<https://github.com/digitaldemocracy2030/kouchou-ai/pull/840>
review readyにしているのはcode rabbitにreviewさせるためであって、まだ作業中です。
> 「*4つの blocker は片付け、CLI / API 入口の test 網も張った。あとは実データ通しと docs の整理を残すだけ*」というのが現在地です。
だいぶできたけども今日中に完了しなさそうなので報告しときました

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-21 02:47:38_

上記の現在地の解説もClaude Codeが書いてくれてて、ほんと助かる

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-21 04:15:30_

<https://github.com/digitaldemocracy2030/kouchou-ai/pull/840>
作業完了して、CodeRabbitのレビューもCIテストも全部OKなので一晩寝て明日マージしたいと思います

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-21 04:17:31_

CLIのワークフローをWeb版も使うようにし、その時にWeb版の機能が壊れないようにテストで確認しながら挙動の違いがないように擦り合わせていった、というPRです

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-21 23:18:39_

Codexにぼちぼち重要そうな方から実装してもらっていて、ちょっと色気を出して3並列にしたら他のスレッドが実行中のIssueを「次はこれが重要！」と言い出して面倒なことになった(苦笑)

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-21 23:20:48_

なおCodexが勝手にtokorotenにレビュー依頼する事案が発生したので叱っておきました

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-21 23:55:41_

ところでWikiは前回Mkdocsで作ってObsidian形式のリンクがリンク切れになってたのでQuartzで作り直しました
<https://nishio.github.io/kouchou-ai-developer-wiki>

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-21 23:56:39_

index.mdがAI向けの全ページINDEXになってて、人間のコントリビュータ向けではない問題、AI用のINDEXを別に作るのがいいのかもな…

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-21 23:58:42_

おっとリンクが切れている


#### 05月22日(Fri) - 23件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 00:08:57_

直った

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 19:06:42_

Codexはほんとモリモリ実装してくれるけどUI系のものはどの程度任せて大丈夫なのかな。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 19:26:11_

Codexくんの見積もりだと1〜3週間で大きな問題は片付くのでは、数ヶ月あれば全Issueが片付くのでは、というノリで、本当に全部片付くかはわからないけども(最後の1割にとても時間かかるとかありそう)書籍リリースまでに今までに堆積したIssueを一旦全部今の視点で見直すこと自体は十分できそうな気がしています

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 19:26:55_

なので一旦どんどん進めてどこまで行けるか試してみたい

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 19:32:15_

あー、でも優先順位で次のIssueはWindows環境の話だな…、まずWindowsの開発環境を作るか…

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 19:47:55_

それ自体をCodexにチャレンジさせたらいいのではと思った

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 20:19:24_

生Windows、茨の道だな… gitもないしpythonもない、PowerShellのencodingがcp932…

### **中山心太（tokoroten）** in #2_開発_広聴ai _2026-05-22 20:25:04_

生Windows、Gitpullしてきて、Claudeにセットアップしろで終わりです。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 20:29:39_

我々のようなAIに課金している人はいいんだけどさ

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 20:30:03_

<https://github.com/digitaldemocracy2030/kouchou-ai/pull/858>
Codex on WindowsからPRが出ました

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 20:32:41_

とりあえずASCIIになったけど、どうすんのがいいのかなぁ
誰かがユーザに親切にしようとして日本語のメッセージを出すようにし、それがユーザ環境の文字コードとミスマッチでこける

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 20:34:52_

<https://nishio.github.io/kouchou-ai-developer-wiki/analyses/codex-windows-environment-memo>
> *Open Questions*
> • Windows 用 setup script は、長期的には`.bat`のまま維持するべきか、PowerShell script へ寄せるべきか。
> • 非専門家向けの Windows 導線は、native Windows を厚く支えるより、Docker Desktop / WSL2 のどちらを正規入口として前面に出すべきか。


### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 20:35:58_

とりあえず今後CodexにWindowsユーザ役として色々操作してもらってトラブルシュートしてもらうことはできそう

### **中山心太（tokoroten）** in #2_開発_広聴ai _2026-05-22 20:37:28_

実験で、３つのレポジトリを起動しなくちゃならんのがしんどいのよなぁ

### **中山心太（tokoroten）** in #2_開発_広聴ai _2026-05-22 20:37:58_

コアに軽量フロントオプションを作って、FastAPIにHTMLを返してもらう方向とか無いかしら。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 20:49:07_

ChatGPTいわく「Windowsマシンをself-hosted GitHub Actions runnerにするのはどう？」とのことw

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 20:49:34_

365日24時間やるのはいやだけど、とりあえずやってみるかw

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 21:47:47_

CodexがPRトリガーで僕のマシンでのself-hosted runnerが動くように実装してて、それはダメではと思ったw

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 22:21:58_

Azure環境へのdeployがsuccessしてるのになんでWindows環境でのビルドがコケるんだ…

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 22:22:34_

しかしとりあえずself-host runnerでDocker Desktopを使う経路を試すテストを走らせるのは有用だということがわかった

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 23:11:32_

実機e2eテスト環境構築の話
<https://nishio.github.io/kouchou-ai-developer-wiki/analyses/windows-real-machine-e2e-lessons>

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 23:13:07_

Azure Deployはテストが足りてないので正常でなくてもsuccessするとCodexは主張している、今後要検証
<https://nishio.github.io/kouchou-ai-developer-wiki/analyses/windows-real-machine-e2e-lessons#why-existing-success-did-not-catch-it>

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-22 23:55:21_

setup_win.batの文字化け問題、Codexいわく「*.batでは無理だからPowerShellに追い出そう」とのことで、Windows 10/11 なら標準搭載とのことですけど、どう思います？
<https://nishio.github.io/kouchou-ai-developer-wiki/analyses/windows-setup-encoding-decision>


#### 05月23日(Sat) - 14件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-23 11:07:49_

今まで色々あちこちで書いていたことが簡潔にまとまった:

embeddingを前提としない分析様式(例: SenseMaker)を可能にしたい。しかし、embeddingを前提としている散布図は、見た目のインパクトが強く、ユーザが欲しがるので簡単には捨てられない。そこで互換のために一時的に “embeddingを前提としない分析様式” でもembeddingを併用して、散布図互換 にする案 と、長期的に 散布図が必須なビュー をやめる案の二段構えで進むのが良い。

#### スレッド返信

**Shingo OHKI** _2026-05-23 13:59:51_

ここについては、
• なぜ現状の散布図が人間には受け入れられやすいのか
• 広聴結果の公開UIに求められるものは何なのか？
みたいな議論が改めてできるといいのかもしれないなと思いました。

**Shingo OHKI** _2026-05-23 14:22:13_

（自治体での利用の文脈で）自分で投げた問いに少し答えてみると、
現状の散布図が受け入れられやすいのは、散布図そのものが本質というより、
• 大量の意見が扱われていることが一目で分かる
• 似た意見ごとに整理されているように見える
• 全体像を探索できる
• 要約やラベルだけでなく、個別意見にも戻れる
• 行政側が恣意的にまとめたのではなく、一定の透明性をもって公開しているように見える
という要素を、一画面で出しやすいからなのかなと思いました。

一方で、広聴結果の公開UIに求められるものは、単に分析結果をきれいに見せることではなく、
「集まった声がどう受け止められ、どう整理され、何が論点として見えてきたのか」を、
住民や職員が確認できることなのかなと。

そのためには、
• どのような声をどれくらい扱ったのか
• どういう観点で整理されたのか
• 主要な論点は何か
• 元の個別意見まで辿れるのか
• 少数意見や分類しにくい声が埋もれていないか
• 行政側が恣意的にまとめたように見えないか
• 次に何を議論・深掘りすべきかが見えるか
といったことが大事になってくるのかもしれません。

そう考えると、散布図が担っていた「広聴結果の公開UIとしての役割」を、
別のUIでどう担保するかを考えられるとよさそうだなと思いました。

また、これは元の「分析方式と view を独立にする」という話とも矛盾せず、
むしろ view 側が満たすべき要件を整理しておくと、
散布図以外の view も検討しやすくなりそうだなと思いました。

「多くの声を丁寧に扱い、整理の根拠や元の意見まで確認できる」
という体験が出せるなら、必ずしも現状の散布図である必要はないのかもしれません。

**Shingo OHKI** _2026-05-23 14:29:14_

公開UIとしては、embedding がやっているような「意味的に近いものを距離で精密に表すこと」自体が必ずしも本質ではなく、どの声がどの論点に整理されたのか、元の個別意見に戻れるのか、分類の根拠や限界が分かるのか、
といったことが確認できる方が重要なのかもしれません。

同じ意見グループに入ったものについても、グループ内の点同士の距離を厳密に表現するというより、
同じまとまりとして自然に近く表示されていれば、広聴結果の公開UIとしては十分成立しそうな気がしました。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-23 11:09:13_

LLM Wikiでねりねりした結果、これが重要な言語化なのにわかりやすく記載されていないのが問題だよねとわかってきた

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-23 12:31:07_

Windows PCが起動しなくなってしまった…
今回の作業が原因なのかWindows Updateで再起動したのが原因かは不明だが、せっかく作ったWindows開発環境が使えないからPRの動作確認もできない…

#### スレッド返信

**小野翔太** _2026-05-23 13:45:05_

winを普段使ってます。経験談で書いておきます。参考になれば

電源ボタン押してうんともすんとも→
デスクトップならワンチャン、電源コード抜いた状態で電源ボタンを長押し（数秒）後、電源コードを繋いで電源ボタンで起動したことあります（RAMの帯電？かなにかが原因だった）

一瞬立ち上がるが落ちる→
BIOS画面やセーフモードで立ち上げる方法が合ったはず…起動後すぐにF2キーとかがありがち

### **Shingo OHKI** in #2_開発_広聴ai _2026-05-23 13:46:31_

LLM Wiki について思ったこと

#### スレッド返信

**Shingo OHKI** _2026-05-23 13:47:42_

LLW Wiki とてもいいですね！
過去のSlack・GitHub・議事録などからここまで整理されているのは、すごいなと思いました。

一点、私の名前の漢字が違っていました（笑）
<https://nishio.github.io/kouchou-ai-developer-wiki/entities/ohki-shingo>

これ自体は大勢に影響ないのですが、これについて考えていて、LLM Wikiの設計上は結構大事な論点かもと思いました。

おそらく Shingo OHKI という表記から、AIが自然そうな漢字として漢字名を推測したのかなと思います。

ただ、人名・所属・役割・発言の帰属・意思決定の経緯のような情報でこういう補完が入ると、気づかないところで少しずつ間違った履歴が積み上がってしまう可能性がありそうです。

生成されたWikiが次の要約や検索の入力になると、小さな誤りが記録された事実のように扱われてしまうのが怖いですね。

なので、人物・組織・役割・発言帰属・決定事項まわりは、

•  原文にある事実
•  AIが推定した情報
•  人間が確認した情報
•  正式に決定された情報
などを分けて扱えると、安心して使えそうだと思いました。
今回であれば、確認できていない漢字名は記録しない方が安全そうだなと思いました。

**Shingo OHKI** _2026-05-23 13:48:56_

AIの推測じゃなくて、どこかで誰かが間違えて書いたとかもあるのかな

**NISHIO Hirokazu** _2026-05-23 20:10:48_

すみません、正しい表記は何ですか？（念のため）

**Shingo OHKI** _2026-05-23 22:11:32_

大木真吾です！

### **Shingo OHKI** in #2_開発_広聴ai _2026-05-23 13:59:51_

ここについては、
• なぜ現状の散布図が人間には受け入れられやすいのか
• 広聴結果の公開UIに求められるものは何なのか？
みたいな議論が改めてできるといいのかもしれないなと思いました。


#### 05月24日(Sun) - 3件

### **Shingo OHKI** in #2_開発_広聴ai _2026-05-24 08:27:32_

SusHi Tech Tokyo で接点ができた<https://www.ashisuto.co.jp/|株式会社アシスト>さんと、先日情報交換しました。

アシストさんはソフトウェア専門商社／パッケージインテグレーターで、
今年から公共領域への取り組みを強化されているとのことです。
こちらからは DD2030 と広聴AIの概要、自治体活用事例などの話を共有しました。

先方からは、広聴AIを「自治体に既にあるアンケート自由記述・チャットボットログ・庁内に眠る定性データから、
課題仮説やインサイトを得る入口」として活用できそうだという反応がありました。
また、OSSコミュニティと役割分担しながら、社会実装や顧客適用の部分で貢献できる可能性があるのでは、
という話も出ました。

まだ具体的な連携が決まったわけではなく、先方で社内検討いただく段階ですが、
DD2030／広聴AIにとって良い連携相手になる可能性があるかもしれないので、共有です。
進展があればまた共有します。


#### 05月25日(Mon) - 9件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-25 00:48:55_

もはや経緯をみんな忘れているかもしれない大リファクタリングが完了したので議事録に経緯とセットでまとめておきました

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-25 10:30:13_

LLMグルーピング実験
>`extraction する前提` なら、`LLM grouping` の追加コストは「+16% でラベル品質改善」
>散布図の見え方は従来法が圧勝
>ラベル品質は逆でした。OpenAI judge では`LLM grouping` の方が「読みやすい・具体的・代表性が高い」と判定されました。差は大勝ではないですが、*数点の改善は出ている*。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-25 11:20:29_

実験詳細
<https://nishio.github.io/kouchou-ai-developer-wiki/sources/jigsaw-llm-grouping-experiment-output-2026-05-25|https://nishio.github.io/kouchou-ai-developer-wiki/sources/jigsaw-llm-grouping-experiment-output-2026-05-25>

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-25 11:28:24_

自動で選ばれたK=8の実験ではLLMグルーピングの方がラベルの品質が良かったが、K=20では個別のラベルに関しては従来手法の方が良い
LLMグルーピングではKを増やすことでコストが増えてるのに品質が下がるという逆効果が起きている

これは興味深いな
細かい大量のクラスタができることを許容するなら従来手法の方がむしろ良いのだとすると、細かく分析する人向けには従来手法が良いかも？ざっくり観察に使うのが筋悪で、ドキュメントで「数十件に細かく割って分析する用です」とかガイドした方がよい可能性。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-25 11:34:05_

ここまでレベル1段階でやってるので[8, 40]のパターンもやって比較してみよう、その方が今の広聴AIのアルゴリズムに近い。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-25 11:54:21_

単発K=8のグルーピングよりK＝40をやってから8にまとめる方法だと「`一貫性` と `網羅性` は上がり、`区別性` は少し下がっています」とのことらしい。前2つが上がってるのは興味深い。隣のクラスタとの区別がわからないという話は今までにもユーザからちらほら聞こえてきてた気がしていて、今回の実験で解くべき問題がよりシャープに絞り込まれたかもしれない。つまり、現状の広聴AIに対する分析性能の向上って、実はトップレベルラベルの区別が明瞭でなくなりやすい問題の解決が必要ということなのかも。この辺、初期にnasukaさんが新しいアルゴリズムを試そうとしてた(入れた？入れてない？)記憶があるな…

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-25 11:56:12_

>ラベル集合全体をまとめて見せた direct judge は `llm_grouping_k8` 勝ちでした。理由は「読みやすく、重複が少なく、粒度が揃っている」です。つまり今回の差は、`[8,40]` が負けたのではなく、`[8,40]` は representative だが見出しが長く説明的になりやすい、ということです。

ここの観点を踏まえたアグリゲーションステップのプロンプトとかアルゴリズムの改善があると良さそう。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-25 12:30:44_

Codex君がノリノリでアルゴリズムの改善をして複数のプロンプトで比較実験してる、捗る〜

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-25 17:08:20_

Codexに「現在のコードベースと比較して完了済みのIssuesは閉じて」と言ってみた


#### 05月26日(Tue) - 2件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-26 15:06:10_

kouchou-ai-developer-wikiの整理が終わったのでREADMEも生成してもらいました。
AI用のindex.txtと人間用のindex.mdを分離するルールにしたことで、人間にとっての見方が少しマシになったはず
<https://github.com/nishio/kouchou-ai-developer-wiki/blob/main/README.md>

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-05-26 15:14:54_

entityはトップページに書くほどの重要度だろうか... 人間向けindexは「広聴AIの開発に必要な知識」という観点からもっとしっかりキュレートした方がいいかも



### #2_コアループ_process (17件のメッセージ)

#### 05月21日(Thu) - 6件

### **U0A67RK86BH** in #2_コアループ_process _2026-05-21 14:10:09_

<@U09C3J7V960> <@U0A6CE44B2S>
アリスからの連絡について、#2,4は今晩送付よていですかね？
#1、4は私から返信するか、あるいは明日の定例に＃1～4まとめてお話しますか？

＃1：
スタンフォード側にSODPセットアップは依頼したい点を伝える（費用交渉が先がいいでしょうか？）
現時点での当日の動きExcelを共有してコメントをもらう
#4：我々のスタンスとしては、協力いただける限りはDPとして進めて、結果として要件を満たせなかった場合はinspired by DPとして対外的に説明したい、と伝える

#### スレッド返信

**U09C3J7V960** _2026-05-21 15:57:40_

<@U0A67RK86BH> ありがとうございます。2,4について書きますのでまとめて送っていただけると助かります。10分以内に展開します。（価格交渉については、そのあと私から縄田さんのメールに書き足す形でお送りします）

**U09C3J7V960** _2026-05-21 16:08:32_

```Dear Alice,

Thank you so much for your detailed message — no need to apologize at all, it was very helpful. Let me respond to items #2, #3, and #4.

#1 Learning to use the Stanford Online Deliberation Platform

Thank you for the kind and thoughtful offer. We would gratefully like to take you up on it: please go ahead and have Stanford set up the deliberation for us this time, and we would very much appreciate your assistance in running it together. Given the limited time, we agree that having Stanford lead the setup is the most reliable path for June 21st. For a future deliberation, we would be very happy to be onboarded and learn to use the platform ourselves.

#2 Advisory Committee for the briefing materials

Thank you. Our advisory committee is as follows:

- Yuno Shibuya, Associate Professor, Interfaculty Initiative in Information Studies, The University of Tokyo
- Masahiro Sogabe, Professor, Public Law, Graduate School of Law, Kyoto University
- Yusuke Zennyo, Professor, Graduate School of Business Administration, Kobe University
- Eijiro Mizutani, Associate Professor, Institute for Media and Communications Research
- Masako Wakui, Professor, Law and Politics, Graduate School of Law, Osaka Metropolitan University

We have already been receiving advice on the briefing materials from this committee.

One question: within the SODP process, is there a defined procedure for how the advisory committee should review the materials (e.g., review criteria, format, or steps we should follow)? If so, we would appreciate your guidance.

As for the briefing materials, we will send a draft to Alice and Shinya late tonight (JST). If we can confirm at tomorrow's regular meeting that the materials are broadly in good shape, we plan to ask the advisory committee to begin their content review right after.

#3 Pre-deliberation survey - T1 - Launch date

The launch date for T1 is May 25th.

Based on Shinya's email, we understand that the survey structure as follows:

- T1: Items needed for stratified sampling (attributes) + survey on the discussion themes
- T2: Survey on the discussion themes(i.e. same as T1)
- T3: Survey on the discussion themes(i.e. same as T1, T2) + items measuring participation satisfaction

On this basis, we will send the survey (questionnaire) over tonight as well, so we would be grateful if we could review it together at tomorrow's regular meeting.

#4 DP vs. deliberation-inspired by DP

Thank you for the thoughtful advice. On our side, we intend to hold firm to the June 21st milestone while doing our best to meet the SODP standard. Of course, we fully understand that if it turns out we were unable to meet the standard in some respects, it would then become a "deliberation inspired by DP."

We look forward to discussing everything further at tomorrow's meeting.

Best regards,
Eiko```

**U09C3J7V960** _2026-05-21 16:08:44_

<@U0A67RK86BH> こちらで確認の上送付ください！

**U0A67RK86BH** _2026-05-21 17:30:05_

ありがとうございます、送付しました！

**U09C3J7V960** _2026-05-21 17:37:19_

<@U0A67RK86BH> ありがとうございます！　明日機嫌よく議論してもらったほうがよいので価格交渉は明日の定例終わった後に連絡します！（案文作っておきました）
=====
```Dear Alice,

Thank you for the discussion today — this is Naofumi, following up on one separate matter that I didn't want to take up too much of our meeting time with.

By way of context: I serve as Secretary-General of PRANCE (Plurality Research and Nameraka Center of Excellence), a newly established research center at Keio University, founded by Ken Suzuki. PRANCE is co-hosting this particular event together with DD2030. Going forward, it is PRANCE that intends to lead citizen deliberations in Japan — running them repeatedly and accumulating know-how over time. Our hope is to make deliberative democracy a recurring, established practice here, with PRANCE as the driving force.

With that long-term picture in mind, I wanted to ask about pricing. PRANCE is fundamentally an academic, non-profit, and largely pro-bono endeavor. We are still in the early stage of fundraising — donations have not yet come together, and our crowdfunding campaign has unfortunately been slow (<https://camp-fire.jp/projects/930941/view>).

Given this academic and non-profit positioning, I wanted to ask whether there might be room for a discount on the platform cost. Candidly, if a grassroots, citizen-led movement like ours has to cover this level of cost for every single deliberation, it will be difficult to sustain and scale the practice across Japan in the way we envision. A more accessible arrangement would make an enormous difference to whether deliberative democracy can truly take root here.

I would be very grateful for any sense you can share of whether an academic / non-profit rate might be possible — whether for this event, or as an ongoing arrangement as PRANCE continues this work. Since our timeline is tight, an early indication would be especially helpful as we finalize our budget for June 21st.

Thank you very much for considering this.

Best regards,
Naofumi Nishida
Secretary-General, PRANCE (Plurality Research and Nameraka Center of Excellence), Keio University```


#### 05月22日(Fri) - 9件

### **U09C3J7V960** in #2_コアループ_process _2026-05-22 11:25:45_

```Dear Professor Wakao and Alice（Japanese text follows below）
Nice to meet you. My name is Ogura, and I am a member of the Digital Democracy 2030 team.
I share the briefing materials I have prepared. I would highly appreciate it if you could take a look and share your comments.
Additionally, regarding the survey questions designed to align with the key points in the briefing, I am currently considering a 5-point scale. However, looking at the "DP Japan past T1 text" you shared previously, a 10-point scale (0–10) was used. I would love to get your feedback on what range/scale would be most appropriate for these questions.
Below are the draft survey questions:
Demographic Information (To be used for stratified sampling)
Age
Gender
Region/Location
Questions Common to T2
1. Should ad platform operators require official identity verification for all advertisers as a mandatory prerequisite for running ads?
2. Should ad platform operators be required to mandate labels on advertisements generated or optimized by AI?
3. Should ad platform operators bear a social responsibility to remove advertisements confirmed as fraudulent within a specific timeframe (e.g., 24 hours)?
4. Should ad platform operators bear liability, such as financial compensation, for damages caused by fraudulent advertisements hosted on their platforms?
5. Should a unified end-to-end system be developed and operated to handle the reporting, fact-checking, and removal requests of fraudulent ads? If so, should the operating body be the government, a third-party organization, or a government-affiliated agency?
6. Should the government require ad platform operators to submit and execute a damage-reduction plan—aiming for results equal to or better than Taiwan's achievements (where government measures reduced the total financial damage of scam ads to approximately 1/30)—and actively monitor its implementation?
7. Should large-scale platforms be mandated to provide free API access so that external experts can obtain data to monitor and analyze fraudulent ads in real-time?
8. Should all general social media users, not just advertisers, be required to verify that they are a "real individual" (KYC), even if they do not use their real names?
9. Large-scale ad platform operators should, in high-risk areas such as investment, crypto assets, and side-hustle solicitations, prioritize damage prevention over freedom of expression, and implement AI-driven pre-screening and pre-blocking as a general rule.
10. Should a mechanism similar to the one introduced on X (formerly Twitter), where general users collaborate to add context or flag misinformation on ads, be mandated across all platforms?
11. If a fraudulent ad is quickly spotted and reported, and subsequently confirmed as a scam, should the reporting user be given incentives such as rewards or loyalty points?
General Behavior & Perceptions(I would also like to consult with you on whether including this section is necessary)
12. I feel that I frequently view social media or video-sharing sites on my PC or smartphone throughout the day.
13. I often come across advertisements that appear to be fraudulent.
14. I believe platform operators are responding appropriately to counter fraudulent advertisements.
15. As an entity responsible for tackling fraudulent ads, platform operators are trustworthy.
16. I believe the government is responding appropriately to counter fraudulent advertisements.
17. As an entity responsible for tackling fraudulent ads, the government is trustworthy.
18. Someone close to me has fallen victim to a scam.
19. I have personally fallen victim to a scam.
20. I frequently visit external websites via advertisements on social media and other platforms.
Thank you very much for your time and guidance. I look forward to hearing your thoughts.
Best regards,
Ogura
-----
若尾先生

初めまして、デジタル民主主義2030メンバーの小倉と申します。
ブリーフィング資料を作成しましたので送付します。コメントいただけると幸いです。
また、ブリーフィング資料の論点と合わせる形でアンケートでは以下の質問をについて、５段階を想定していますが、以前いただいたDP Japan past T1 textを見ると、0~10の１０段階評価でしたので、選択の幅がどの程度が適切かについてもご意見をいただきたいです。

基礎情報（層化抽出にも用いる指標）
・年齢
・性別
・地域

T2と共通のアンケート
1.広告プラットフォーム事業者は、すべての広告主に対して公的な身元確認を広告掲載の必須要件とすべきか。
2.広告プラットフォーム事業者は、AIによって生成・最適化された広告に対し、ラベル表示を必須要件とすべきか。
3.広告プラットフォーム事業者は、詐欺だと判明した広告について、一定時間（例：24時間）以内に削除する社会的責任を負うべきか。
4.広告プラットフォーム事業者は、掲載された詐欺広告による被害に対して、賠償等の責任を負うべきか
5.詐欺広告の通報・事実確認・事業者への削除依頼を一気通貫で行うためのシステムを開発・運用すべきか。また、その実施主体は政府か、第三者機関・政府外郭団体か。
6.政府は、広告プラットフォーム事業者に対し、台湾の実績（政府による対策で詐欺広告被害額が約30分の1まで減少した）と同等以上の実績を目指した被害削減の実行計画を提出させ、その実行をモニタリングすべきか。
7.大規模プラットフォームに対し、外部の専門家が詐欺広告をリアルタイムで監視・分析できる用にデータを取得するための仕組み（API）の無償公開を義務付けるべきか
8.広告主だけでなく、SNSを利用するすべての一般ユーザーに対し、実名ではなくとも「実在する個人であること」の確認（KYC）を求めるべきか。
9.広告主だけでなく、SNSを利用するすべての一般ユーザーに対し、実名ではなくとも「実在する個人であること」の確認（KYC）を求めるべきか。
10.大規模広告プラットフォーム事業者は、投資・暗号資産・副業勧誘などの高リスク分野については、表現の自由よりも被害防止を優先し、AIを活用した事前審査・事前遮断を原則とすべきである。
11.X（旧Twitter）で導入されているような、一般ユーザーが協力して広告の背景情報や誤情報への指摘を追記できる仕組みを、全プラットフォームに義務付けるべきか
12.詐欺広告をいち早く発見・通報し、実際にそれが詐欺だと認定された場合、通報したユーザーに報奨金やポイントなどのインセンティブを付与するべきか。

（その他普段の行動等）※こちらは必要性についてもご相談したい
13. 1日の間にPCやスマホでSNSや動画サイトなどを見る頻度が高いと思う
14. 詐欺広告だと思うような広告をよく目にする
15.プラットフォーム事業者は、詐欺広告対策について適切に対応していると思う。
16. 詐欺広告対策の主体として、プラットフォーム事業者は信頼できる
17. 政府は、詐欺広告対策について適切に対応していると思う。
18.詐欺広告対策の主体として、政府は信頼できる
19.身近に詐欺にかかった人がいる
20.自分が詐欺にかかったことがある
21.SNSなどの広告から外部サイトを閲覧する頻度が高い```

### **U0A67RK86BH** in #2_コアループ_process _2026-05-22 11:29:07_

すみません改めて確認しましたが、若尾先生から過去アンケートは特に共有してもらってないですね…
何かのタイミングにてお尋ねいただければ幸いです

#### スレッド返信

**U09C3J7V960** _2026-05-22 11:29:42_

<@U0A67RK86BH> 本日必要なのでこの後メール出せますか？

**U09C3J7V960** _2026-05-22 11:34:47_

メールありがとうございます！

### **U09C3J7V960** in #2_コアループ_process _2026-05-22 11:42:46_

<@U0A67RK86BH> 何か補足ございましたらお願いします。
======================================================
Aliceと若尾先生（＋DD2030縄田さん / 西田）打ち合わせ要旨
■ブリーフィング資料について
• 先週から提示したものから劇的によくなった。SODP基準になっている。構成も問題ない
• テーマが「①台湾モデル」「②日本モデル」となっているほうがわかりやすい、問題なし
• 1テーマあたりトピックは6-8個で問題ない。（さくっと終わるトピックもあるため、Aliceの感覚的に1時間で消化できる）
• 本日は台湾モデルのトピックを説明したが以下フィードバック（フィードバックないやつについては修正必要なし）
    ◦ トピック5（通報サイトについて）：メインできく質問を運営主体は誰にすべきか？ということにすべき。
    ◦ トピック6：これはマストで聞く必要があるものか？（計画提出を求めるのは全員OKというだけではないか）。違う意図であるのであれば表現見直す必要がある。
■ブリーフィング資料のレビュープロセスについて
• SODPで共通のevaluation formatのようなものはない。
• ただブリーフィング資料について専門家レビューを通していることが大事。
• レビューのさせ方だが、全文を通読させるのではなくて、分担させて問題ない
• ただし分担については、1パートを2以上に見させる必要がある。
====
■T1/T2/T3について
• 若尾先生とAliceの認識が違っていたことに気づく。
    ◦ 若尾先生（T1/T2/T3）をやるべき。
    ◦ Alice（T1とT3）だけでいい。T2はOptional
        ▪︎ なんでOptional？　=>T1で聞ききれなかったものについて補足的にT2で聞くんだよね。（by Alice）=>それだとT1は知識なし時点でT2は知識あり時点だから意味がないのでは？=>まぁそうなんだけどいいのよデータが多ければ多いほど（by Alice）　的な回答。
    ◦ minimumでやるのであればじゃぁT1時点のアンケートは不要で、T2, T3だけでいい？ => データは多いほど多いほどがいいし、知識なしとあり時点の経過も見たほうが良いのでは？（Alice）
    ◦ 結論として、以下でよいとのこと。
        ▪︎ T1：層化抽出に必要な項目＋総務省等でSNS利用に関してとっている質問を参考にしたpreference（これは分析に必要なためのもの）の質問＋台湾モデルのディスカッショントピックに関しての質問（6つ）
        ▪︎ T2：台湾モデルのディスカッションに関しての質問＋日本モデルのディスカッションに関しての質問
        ▪︎ T3：T2の質問＋満足度調査
• T1のアンケート項目については25日にリリースする必要があるから、送り次第、若尾先生＋Aliceのほうが週末にかけてレビューしてくれるとのこと。【西田サポート＋小倉さん】
====
■SODP運用に関して
（縄田さんより）

#### スレッド返信

**U0A67RK86BH** _2026-05-22 11:46:07_

ありがとうございます。相違ないです。こちらにも詳細メモ入れてます。
メモはこちらに入れました。
<https://docs.google.com/document/d/1isqRSUvvympiNp8uKBWYHIAI8-CGNjePriZUfrN4qig/edit?tab=t.1pri05nn1e8d#bookmark=kix.tqs6ckd79pay>

T1について、厳密に20問と言われている訳ではないので、調整の余地はあると思います。必要であればT1に日本モデルのディスカッションに関しての質問を入れても大丈夫です。

**U09C3J7V960** _2026-05-22 14:07:04_

ありがとうございます、T1には日本モデルのディスカッションいれる予定です

### **U09C3J7V960** in #2_コアループ_process _2026-05-22 14:42:23_

```縄田さん、

どれを以前お送りしたか覚えていませんが、2012年に日本で行ったDPのT1、T2、T3の質問票をお送りします。
各DPによって事情が違うためこのDPでは個人属性をT2で聞いています。これはこのDPがオンラインでなく直接東京に集まって行ったものであり、T1で負担が増えると参加者が減る可能性があること、また電話アンケートだったという時間的制限もあったと思います。今回このような属性の質問はT1で聞いても問題ないと思います。

討論資料もお送りしたと思いますが再度お送りします。

若尾```


#### 05月25日(Mon) - 1件

### **U0A67RK86BH** in #2_コアループ_process _2026-05-25 11:28:26_

T1はこちらで調査会社に送付します


#### 05月27日(Wed) - 1件

### **U0A67RK86BH** in #2_コアループ_process _2026-05-27 12:19:36_

小グループ体験の簡単な記録です。明日は運営サイドでオブザーバーとして参加させてもらう予定です。



### #2_開発_広聴ai_アルゴリズム開発 (13件のメッセージ)

#### 05月25日(Mon) - 5件

### **NISHIO Hirokazu** in #2_開発_広聴ai_アルゴリズム開発 _2026-05-25 14:44:11_

要件として
・たくさんの意見があることが点群として表示されて欲しい、1つの点が1つの意見に対応するなど
・embeddingして2D UMAPした場合、空間配置を尊重したクラスタリングをしたら意味的なまとまりがベストではなく、意味的なまとまりでクラスタリングしたら2D UMAPで明瞭に分離しなくて理解が困難
・良い感じの可視化が欲しい

という積年の課題ですけど

・クラスタ内の距離ベースで全域木を作る
・クラスタまたぎのエッジを短い方から順に、明瞭分離を壊さない程度追加する(ここは少しずつ足しながらイテラティブにやる、二分探索でも良い)

ってのはどうでしょう

### **NISHIO Hirokazu** in #2_開発_広聴ai_アルゴリズム開発 _2026-05-25 14:45:59_

この方法の良いところは、追加したクラスタまたぎのエッジが示唆を与えるものとしてフォーカスして良いところ

### **NISHIO Hirokazu** in #2_開発_広聴ai_アルゴリズム開発 _2026-05-25 14:48:06_

---

関連した別の話、
100件未満くらいの小規模ケースで10000件超えを想定したツールをそのまま使うのはそもそもおかしいので
LLMでN:Nの類似関係を抽出し、関係の強い方から繋いで全域木にする

### **NISHIO Hirokazu** in #2_開発_広聴ai_アルゴリズム開発 _2026-05-25 21:00:01_

@shinta.nakayama <https://scrapbox.io/nishio/Hypothetical_Document_Embeddings>

### **中山心太（tokoroten）** in #2_開発_広聴ai_アルゴリズム開発 _2026-05-25 21:05:08_

条文とか計画をベースとしたHyDEはやってもよさそう。


#### 05月26日(Tue) - 8件

### **NISHIO Hirokazu** in #2_開発_広聴ai_アルゴリズム開発 _2026-05-26 18:52:07_

今気づいたのだが、実験は生成されたデータとかを永続化して後から確認できるようにしたいから根本的に別のリポジトリでやるべきだな(気づくのが遅い)

### **NISHIO Hirokazu** in #2_開発_広聴ai_アルゴリズム開発 _2026-05-26 19:40:14_

うーん

### **NISHIO Hirokazu** in #2_開発_広聴ai_アルゴリズム開発 _2026-05-26 19:51:52_

いっぽうSupervised UMAP

### **NISHIO Hirokazu** in #2_開発_広聴ai_アルゴリズム開発 _2026-05-26 20:00:13_

明瞭に分かれた上で他のグループに混ざって見えるのでダメ

### **NISHIO Hirokazu** in #2_開発_広聴ai_アルゴリズム開発 _2026-05-26 22:21:11_

結論、自分で考えるよりChatGPT ProにサーベイさせてそれをCodexに投げつけるといい可視化ができる()

#### スレッド返信

**Shingo OHKI** _2026-05-26 22:57:13_

見た目的にはこれで十分そうな気がしますね

**NISHIO Hirokazu** _2026-05-26 23:47:34_

ですよね

### **Shingo OHKI** in #2_開発_広聴ai_アルゴリズム開発 _2026-05-26 22:57:13_

見た目的にはこれで十分そうな気がしますね



### #2_broad-listening-book (7件のメッセージ)

#### 05月24日(Sun) - 4件

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-05-24 11:40:07_

@nishio.hirokazu <!here>

明日の20時から、ブロードリスニング本の編集会議を行いたいです。
インプレスさんとの打ち合わせをします。

TODO:
タイトルどーするのよ問題、現状は以下
「政治・自治体・企業に広がるブロードリスニング　～生成AIによる民意の可視化と分析」
「実践ブロードリスニング」や「実践入門ブロードリスニング」は敷居が上がりすぎている。

印税契約の人と、原稿料支払いの人を決定する。
私、西尾、角野、が印税契約、その他の人を原稿料支払いの予定だけど、異論があるかどうか。
原稿料の人は、2万部程度でた際の印税相当額をお支払いする、というかたちになるとおもいます。
印税契約者が増えることによる、改定時の契約更新リスクが主です。

図表画像はCMYKにしてほしい、黒＋赤の2色で刷る。
プログラムで出している画像は黒とシアンで出力してほしい。シアンを赤に置換する
これは、Web公開版とコンフリクトするので、ちょっと方針を考えたほうがよさそう。

#### スレッド返信

**小野翔太** _2026-05-24 15:26:31_

いつものmeetだと録画→公開フォルダに共有されてしまうので、問題がある場合は別でリンクを作った方がいいかもです。
必要があれば、録画されるが公開されないmeet発行します。

**NISHIO Hirokazu** _2026-05-24 18:09:41_

@shinta.nakayama 了解ですが、特に異論はないです

**NISHIO Hirokazu** _2026-05-24 18:13:21_

議題に挙げて異論が出なかったという議事録を残すことは有益なのでやったら良いと思う


#### 05月25日(Mon) - 2件

### **Slackbot** in #2_broad-listening-book _2026-05-25 19:00:15_

リマインダー : <!here> 本日20時より、ブロードリスニング本執筆会議を開催します！:mega: :clock9: 20:00-21:00 :link: <https://meet.google.com/feh-cnpt-nhq> :memo: <https://docs.google.com/document/d/1plggszRTxEEYUcZuCLiHkPrBsMtxr3RQpctKtZe5y4M> • ブロードリスニング本執筆にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！ • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-05-25 20:00:32_

@nishio.hirokazu 来れますか？


#### 05月26日(Tue) - 1件

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-05-26 18:06:33_

<https://docs.google.com/spreadsheets/d/1Nw-yeksF0pHLAH0otXkXUsBIgTyWL6OqO_9SoP-IRE8/edit?gid=1407163555#gid=1407163555>
現状の貢献量、こんな感じです。



### #dd_prance_event2026 (4件のメッセージ)

#### 05月25日(Mon) - 1件

### **U09C3J7V960** in #dd_prance_event2026 _2026-05-25 16:39:02_

<@U0B553CL9HA> さんありとうございます！　健さんからこちらのチャネルでコミュニケーションしたいということで、再掲します！
```皆様

お世話になっております。尹です。
先日はブレストありがとうございました。
運営を詰める中で、5点ご相談させていただければと存じます。

### 1. 会場決定について
石井さんより下記の選択肢をご提示いただきました。現地をご存知の方にご判断いただけると助かります。特に駒村先生・西田さん、ご意見いただけますと幸いです。

- 並行セッション（100名規模）：G-Lab（北館と動線が近い）または東館8階
- スピーカー控室：北館B1会議室3(静けさ・動線に懸念有り）または東館4階オープンラボ（石井さんが仮押さえ済）

### 2. ラウンジエリアについて
セッション間の休憩・ネットワーキングのため、ソフトドリンク（コーヒー・お茶・水等）を提供するラウンジエリアを設けたいと考えております。日中のアルコール提供は不要と考えています。

### 3. ランチについて
8月2日は日曜で三田周辺の飲食店に限りがあるため、事前に設計しておきたいところです。どんなプランがよさそうか、ご意見いただけますと幸いです。

### 4. イベントサイトについて
CFPをアナウンスしていきたく、イベントサイトのたたき台を作成いたしました。

<https://dd2026.socious.io>

AIで生成したドラフトのため、内容が正確ではない部分が含まれる可能性があります。ご確認の上、できるだけ早くフィードバックをいただけますと幸いです。5月29日（金）公開を目指したいと考えております。

併せて、使用可能なドメイン（PRANCE関連等）がございましたらご教示ください。

### 5. プログラムタイムラインについて
8/2から逆算で、下記を目安と考えております。

- ~5月末：オードリーさんの参加形態確定
- 6月上旬：CFP募集開始
- 6月中旬（~6/15）：最終プログラム確定・登録開始
- 7月下旬：現地最終確認
- 8/2：本番

200名規模の集客には6週間以上のプロモーション期間が必要と考え、このスケジュールを提案させていただきます。ご意見いただけますと幸いです。

---

引き続きよろしくお願い致します。

尹世羅（ゆんせら）
ソーシャス株式会社 代表取締役
<mailto:yun@socious.io|yun@socious.io>```


#### 05月26日(Tue) - 1件

### **U0B553CL9HA** in #dd_prance_event2026 _2026-05-26 16:00:46_

ありがとうございます。
追加で質問なのですが、オードリーさんから許可をいただいていると写真とプロフィール紹介文はございますでしょうか？

また去年のイベント写真素材もご共有頂けると幸いです。
ウェブサイトをアップデート致します。

何卒宜しくお願い致します。


#### 05月27日(Wed) - 2件

### **U09C3J7V960** in #dd_prance_event2026 _2026-05-27 11:53:06_

<@U0B553CL9HA> せっかく進めてくださっているのに返信遅れてごめんなさい！
> ```### 1. 会場決定について
> 石井さんより下記の選択肢をご提示いただきました。現地をご存知の方にご判断いただけると助かります。特に駒村先生・西田さん、ご意見いただけますと幸いです。
> 
> - 並行セッション（100名規模）：G-Lab（北館と動線が近い）または東館8階
> - スピーカー控室：北館B1会議室3(静けさ・動線に懸念有り）または東館4階オープンラボ（石井さんが仮押さえ済）```
私も現地わかっておらず、ただ石井さんからおすすめいただたいのでこちらでいいかなと思っております。

> ```### 2. ラウンジエリアについて```
よろしいかと思います。

> ```### 3. ランチについて```
予算の兼ね合いもあると思うので健さんどうでしょうか？@kensuzuki
個人的には、例えば近隣で食べられるランチスポットの一覧を書いた資料（慶應関係者なら詳しそう）を配っておく程度でいいかなと思っております。

> ```### 4. イベントサイトについて
> CFPをアナウンスしていきたく、イベントサイトのたたき台を作成いたしました。```
こちらすいません、明日まとめてみてます。
ただ、西田に限らず他の方も見ていただけると助かります！
ぱっとみたところ、
・まだリキタスやポリポリには声をかけていないため書けないかなと思いました。

> ```- ~5月末：オードリーさんの参加形態確定```
現時点ではプロボノでの依頼のため、講演・トークセッションなしとはいわれています。
ただ日付は抑えてあるので、for profitに切り替え前提で交渉しなおすというのはありです。
@kensuzuki さんどうでしょうか。

### **U09C3J7V960** in #dd_prance_event2026 _2026-05-27 11:53:40_

> ただ、西田に限らず他の方も見ていただけると助かります！<!here>



### #2_開発_polimoney (4件のメッセージ)

#### 05月23日(Sat) - 4件

### **U099TAD6RKL** in #2_開発_polimoney _2026-05-23 18:59:38_

数分遅れます！

### **Slackbot** in #2_開発_polimoney _2026-05-23 19:00:24_

リマインダー : <#C08FL5L6GSH> :mega:Polimoney開発会議を開催します！:mega: :clock7:19:00-20:00（毎週土曜日） :link:<http://meet.google.com/myy-ptwx-rsu|meet.google.com/myy-ptwx-rsu> :memo:<https://docs.google.com/document/d/19Kn6ekK3twMVcVaSyUgptvmfzrXEJezA6GXTbPXjm9M/edit?tab=t.0>  • 開発にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！  • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！

### **小野翔太** in #2_開発_polimoney _2026-05-23 19:48:03_

@shumizu418128 <@U099TAD6RKL>
hubのsupabase見てみたら、「その他の支出」がないかもです。
その他の収入はある。

#### スレッド返信

**小野翔太** _2026-05-23 19:57:55_

`account_codes`に一覧があり、`ledger_type`カラムに選挙か政治か両方かが書かれている。
…が、人件費は両方に使えるでいいはずなのに２つに分かれてたりする。

`account_codes` を分解して選挙と政治で別テーブルにするか、`ledger_type`カラムに`both` を使わないようにするかしないと、後で大変な気がしてきている。。。



### #0_全体お知らせ (4件のメッセージ)

#### 05月22日(Fri) - 1件

### **小野翔太** in #0_全体お知らせ _2026-05-22 19:48:53_

  毎週土曜日 19:00 , 日本標準時 にこのチャンネルでこれをリマインドするよう設定しました : “!here :mega: 1時間後より、全体定例会を開催します！
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


#### 05月23日(Sat) - 2件

### **小野翔太** in #0_全体お知らせ _2026-05-23 15:29:46_

<!here>
*コミュニケーションツールをSlackからDiscordへ移行する案について（ご意見募集：5月30日まで）*

みなさん、こんにちは！モアイです。
デジタル民主主義2030の一般社団法人化などの展開を見据え、より円滑で持続可能なコミュニティ運営を行うため、*メインのコミュニケーションツールを現在の「Slack」から「Discord」へ移行すること*を検討しています。

つきましては、みなさまからのご意見やご懸念を伺いたく、本日から1週間（5月30日まで）フィードバック期間を設けさせていただきます。特に致命的な問題や強い反対がなければ、1週間後にDiscordサーバーを立ち上げ、具体的な移行プロセスを開始する予定です。

以下に、移行を検討している理由と懸念点への対応方針をまとめましたので、ご一読いただけますと幸いです。

---

:bulb: *移行を検討している理由*

*1. 過去ログが残る環境の確保*
• 現在のSlackの無料プランでは、一定期間が経つと過去のメッセージやファイルが非表示（削除）になってしまいます。有償プランは月額コストが非常に高額なため導入が難しい状況です。
• Discordであれば、*無料のまま過去ログが残り*、いつでも検索・閲覧が可能です。
*2. 新メンバーが参加しやすい環境づくり（オンボーディングの改善）*
• Slackでは新しく入ったメンバーが自分でチャンネルを探して追加する必要がありますが、Discordでは「サーバーに参加した時点で主要なチャンネルに自動で入る（デフォルトイン）」仕組みや、コミュニティ向けのチュートリアル機能が充実しています。
• これにより、新しく参加したメンバーが迷わず活動に参加しやすくなります。
*3. コミュニティ運営の効率化*
 - 運営の自動化や整理に必要な機能がDiscordでは無料で豊富に提供されており、コミュニティの活発化や管理コストの削減に繋がります。

---

:warning: *懸念点とこれからの対応について*

*## Slackのメンバーや過去ログの扱いについて ##*
Slackの1,600人以上のメンバーアセットや過去のやり取りを完全に切り捨てるわけではありません。*移行後も、当面の間はSlackを残します*。
これまでの議論の資産を守るため、すでにGitHub上に専用のリポジトリ（<https://github.com/digitaldemocracy2030/slack-logs|slack-logs>）を作成し、*過去ログを本格的に抽出してアーカイブとして保存する作業を開始しています*。
移行後は、しばらく「Discordを中心」とした運用に切り替えますが、過去ログの参照や連絡用にSlackも併存させます。

*## ツールの使い方の違い（スレッドやUIなど）##*
SlackとDiscordでは画面デザインやスレッドの仕様（Discordはフォーラムや独自スレッド機能があります）が少し異なります。移行にあたっては、基本的な使い方ガイドを用意し、慣れるまでのサポートを行います。

*## メンバーの移行負荷 ##*
SlackからDiscordへスムーズに移動できるよう、アカウント作成方法などの案内と、移行用リンクを順次共有いたします。ROM（閲覧のみ）の方も含め、ぜひ一緒に移行していただければ嬉しいです。

---

:date: *今後のスケジュール（予定）*

• 5月23日（土）〜 5月30日（土）：本投稿に対するご意見・リアクションの受付期間
• 5月30日（土）以降：特にご意見がなければDiscordサーバーを開設し、移行の案内を開始
• 移行完了までの期間：しばらくの間はSlackとDiscordを併用しますが、*「新しいやり取りやアクティブな議論はDiscord」*を基本とします。Slackは過去の会話の参照や過渡期の連絡用として残す予定です。
---

:speech_balloon: *みなさまへのお願い*

この移行について、ご質問や「Discordになるとここが困る」「こういう懸念がある」といったご意見がありましたら、*この投稿のスレッド、またはリアクションにて*お気軽にお知らせください。

コミュニティがより活動しやすく、情報が蓄積されやすい環境にするための前向きな移行として考えております。ご協力のほど、どうぞよろしくお願いいたします！

:question:FAQ等を載せたページを用意しました。こちらも貼っておきます。
<https://dd2030.org/discord-migration/>

### **Slackbot** in #0_全体お知らせ _2026-05-23 19:00:03_

リマインダー : <!here> :mega: 1時間後より、全体定例会を開催します！ :clock8: 時刻 20:00-21:00 :link: Google Meet <https://meet.google.com/fhn-rcoj-sci> :memo: 議事録 <https://docs.google.com/document/d/1tBhaer67U9LbASfqPrg0rpmv0Tt4K7zFUTTzscKXj_I>  • プロジェクトにまつわる進捗報告・相談・TODOの決定を行う会です • どなたでも参加歓迎です！興味ある方はぜひ覗きに来てください  :open_file_folder:過去の録画格納先 <https://drive.google.com/drive/folders/1H55HTB0_rwargUwUJvEPg76Wz13i2-bp?usp=sharing>


#### 05月27日(Wed) - 1件

### **小野翔太** in #0_全体お知らせ _2026-05-27 13:02:38_

【注意喚起】
先ほど削除致しましたが、スパムととれる求人情報がこのチャンネルに投稿されました。
• 当団体の目的にそぐわない内容でしたので削除しました。スパムでなくても求人情報の投稿は基本NGとさせていただきます。
• 投稿がありましても、応募しないでください。
• 投稿だけでなく、DMにもご注意ください。
• 被害にあった、もしくはあいそうな場合、一人で悩まず、警察などにご連絡ください。



### #7_雑談 (4件のメッセージ)

#### 05月22日(Fri) - 2件

### **NISHIO Hirokazu** in #7_雑談 _2026-05-22 17:31:10_

The Synthetic PartyのAsker Bryld Staunæsから
> the web edition of the broad listening book is awesome and beautiful
というコメントが来ました cc <@U0AQQN267H7>

### **NISHIO Hirokazu** in #7_雑談 _2026-05-22 17:32:58_

チームみらいに関する論文の原稿も共有してもらいました
<https://docs.google.com/document/d/14IUKoACYjGpwrmAVqRQSCzSTSW4jJl6Q/edit>
GPTの要約:
> *Broad listening expands what the party can hear, but not what citizens can decide.*
> つまり、ブロードリスニングは「政党が聞ける範囲」を広げるが、「市民が決定できる範囲」を広げているとは限らない、という整理です。
現状まったくその通りだな〜〜と思いました


#### 05月24日(Sun) - 1件

### **U0A77QV20BF** in #7_雑談 _2026-05-24 12:54:04_

Project Coreloop「オンライン広告詐欺対策」の関連情報として、御参考までに（既にご存じの方も多いと思いますが）：
<https://slownews.com/m/m107a19587ef2>
上記のリンクは、同プロジェクトに関する以下の記事に含まれています：
<https://slownews.com/n/n56e0610bba18>
記事の続編はこちら：
<https://slownews.com/n/n47ec24c81322>


#### 05月26日(Tue) - 1件

### **NISHIO Hirokazu** in #7_雑談 _2026-05-26 10:08:33_

青山さんが自分で宣伝しなさそうだから僕が勝手にやりますw
<https://cybozushiki.cybozu.co.jp/articles/m006320.html>



### #2_コアループ_tech (3件のメッセージ)

#### 05月22日(Fri) - 3件

### **U0AEWLLPE8H** in #2_コアループ_tech _2026-05-22 17:38:53_

@yuki.kawabe (cc: @shutaro.aoyama)
本日定例はありますか？20時から研究費のMTGが重なっており、遅れて参加できそうであれば入ります:man-bowing:

#### スレッド返信

**Ryoma Kawabe Yuki** _2026-05-22 17:41:09_

あ、すいません。出張中でしてキャンセルでお願いします。全然できてない…

**U0AEWLLPE8H** _2026-05-22 17:42:33_

@yuki.kawabe 承知しました！来週は予定通り入れそうです。



### #2_開発_いどばた (3件のメッセージ)

#### 05月23日(Sat) - 2件

### **岩永淳志** in #2_開発_いどばた _2026-05-23 17:44:34_

Wakayama Talkですが、地元新聞社への記者会見を無事終えました
今朝時点で
2026/05/23段階の実績
ユーザー数：533ユーザー
チャットスレッド総数：973 ラリー
課題として抽出：439 意見、431の対策案
です

#### スレッド返信

**岩永淳志** _2026-05-23 17:45:26_

@foino74 初の囲み取材で気合いが入る柴崎さん


#### 05月25日(Mon) - 1件

### **岩永淳志** in #2_開発_いどばた _2026-05-25 22:40:13_

<https://hidakashimpo.co.jp/?p=107348|https://hidakashimpo.co.jp/?p=107348> 



### #3_ボードメンバーロール (3件のメッセージ)

#### 05月27日(Wed) - 3件

### **Hal Seki** in #3_ボードメンバーロール _2026-05-27 08:40:45_

<@U09C3J7V960> スパムメッセージ来てますね

#### スレッド返信

**U09C3J7V960** _2026-05-27 10:33:26_

@oscar.gaddress ご対応よろしくお願いします！

**小野翔太** _2026-05-27 12:52:39_

削除、DMで注意しました。続く場合はBANします。



### #8_人数推移 (2件のメッセージ)

#### 05月21日(Thu) - 1件

### **dd-bot** in #8_人数推移 _2026-05-21 09:05:03_

:bar_chart: *2026-05-21* メンバー数: 1592人（前日比: 1人）


#### 05月24日(Sun) - 1件

### **dd-bot** in #8_人数推移 _2026-05-24 09:05:03_

:bar_chart: *2026-05-24* メンバー数: 1593人（前日比: 1人）



### #2_コミュニティ運営 (2件のメッセージ)

#### 05月22日(Fri) - 2件

### **Slackbot** in #2_コミュニティ運営 _2026-05-22 19:00:10_

リマインダー : <!here> 本日20時より、コミュニティ運営定例会議を開催します！:mega: :clock9: 20:00-21:00 :link: <https://meet.google.com/deb-krky-zxx> :memo: <https://docs.google.com/document/d/1dn9R9WLaGNMDO-t1w7m8-2gZRSrgZI4glDvSIr101J4/edit?usp=sharing> • コミュニティ運営にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！ • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！

### **Slackbot** in #2_コミュニティ運営 _2026-05-22 20:00:02_

リマインダー : <!here> 只今より、コミュニティ運営定例会議を開催します！:mega: :clock9: 20:00-21:00 :link: <https://meet.google.com/deb-krky-zxx> :memo: <https://docs.google.com/document/d/1dn9R9WLaGNMDO-t1w7m8-2gZRSrgZI4glDvSIr101J4/edit?usp=sharing> • コミュニティ運営にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！ • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！



### #2_新しいプロジェクトの種 (1件のメッセージ)

#### 05月23日(Sat) - 1件

### **Ken Suzuki** in #2_新しいプロジェクトの種 _2026-05-23 20:11:54_

コアループ週次レポート(5/23)
• 全体: 6/19に自民党PTの提言が正式に承認され、そこで「ストップ広告詐欺」が言及されました。引き続き6/21のDP（熟議付き世論調査）　に向けて準備を進めています。また警察庁に訪問をし、連携について協議がはじまっています。（鈴木）
• Process: DPの準備をスタンフォードと調査会社と進めています。6/21のDP（なりすましオンライン広告詐欺対策に関する討論型世論調査）に向けたマイルストーンも明確になったので、スケジュール通りに粛々と準備を行います。来週は、スタンフォードチームにSODPについてのブリーフィングを受ける予定です。
• Tech: DPに向けてSODPの運用について来週からProcessチームと準備を進めていきます。(Ryoma) 
• Policy: DPに向けたアンケート、事前ブリーフィング資料作成を進めています。内容については、ワークショップにも参加いただいた専門家の皆さんとの協議を進めています、（小倉）
• Reference Product: 警察庁の組織犯罪対策の課の方々との連携のお話や各事業者との連携が本格化するので、そのための準備を進めています。これまでは市民からの通報のみでしたが、データの登録や活用に色々な広がりが出てきました。（赤澤）
• Communication: 警察庁の組織犯罪対策の課の方との打ち合わせに同席し、「ストップ詐欺広告を毎日見ている、これに基づいて今後プラットフォーマーに対しての削除通知申請もしていく」という力強い言葉を受けました。引き続きプロダクト開発のための連携、また、6/21の市民熟議に向けた全体サポートを行っていきます。また、クラウドファンディングについてもテコ入れを図っていきます（いくつかX企画をポストしていきます）。ご協力のほどよろしくお願いいたします。（西田）



