# 2026年02月05日～2026年02月11日のSlack活動まとめ

今週は **18個**のチャンネルで合計**382件**のメッセージがやり取りされました。

## チャンネル別アクティビティ

- **#2_開発_広聴ai**: 84件のメッセージ
- **#2_コアループ_tech**: 54件のメッセージ
- **#2_broad-listening-book**: 53件のメッセージ
- **#7_雑談**: 42件のメッセージ
- **#2_新しいプロジェクトの種**: 40件のメッセージ
- **#2_コアループ_process**: 34件のメッセージ
- **#7_dd_熟議に関する哲学_思想部屋**: 17件のメッセージ
- **#2_コアループ_オンライン広告詐欺対策_市民熟議会議**: 15件のメッセージ
- **#2_コアループ_policy**: 11件のメッセージ
- **#2_コミュニティ運営**: 10件のメッセージ
- **#8_人数推移**: 6件のメッセージ
- **#2_コアループ_reference_product**: 6件のメッセージ
- **#2_開発_polimoney**: 4件のメッセージ
- **#2_広報_pr**: 2件のメッセージ
- **#1_自己紹介**: 1件のメッセージ
- **#2_開発_いどばた**: 1件のメッセージ
- **#0_全体お知らせ**: 1件のメッセージ
- **#3_デジタル資産_権限管理**: 1件のメッセージ

## チャンネル別詳細

### #2_開発_広聴ai (84件のメッセージ)

#### 02月05日(Thu) - 17件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-05 02:12:38_

修正したところとあんまり関係ないテストがエラーで落ちてるなと思ったら静的HTML出力がrootでもsubdirでも動くように両方テストしているのがタイミングによって衝突するということらしい(両方生的なビルドをファイルシステムに出力してからテストしようとするので)

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-05 02:32:31_

よーし、全部直ってテストも通った。改めて振り返って実装内容を解説させよう

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-05 02:57:17_

PRの説明を最終版にしました: <https://github.com/digitaldemocracy2030/kouchou-ai/pull/769>
もう深夜だから明日以降にmergeします

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-05 03:39:34_

これでようやく「同一データ、同一抽出、同一埋め込み」の条件を揃えてクラスタリング方法の違いでどうなるかをやってみせることが可能になる

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-05 10:22:38_

レポート再利用機能がひと段落したので、まずは細々した修正を取り込むのをやる
その次の大きな開発は「クラスタリング手法の切り替えを可能にする」
これをやる上では一旦CLIにスコープを絞ったほうが良いと思う
CLIで分析して、結果だけブラウザで見ることを可能にする
小さな変更と大きな変更のどちらから試すのがよいか
当初は人間の発想としては細かいものを試そうとしてたけど、
細かい変更はユーザにとってメリットがよくわからないと思うのと、AIが書くなら試してみてダメだったら捨てるのでも良いので
「Google Jigsaw的なものを作って」で作っちゃうのが手
この場合、出力結果からは散布図が消えることになる
3つ目としてはオリジナルのTTTC的なスペクトラルクラスタリングをやる。この場合は散布図はあるが階層掘り下げがなくなり、散布図に飛地ができるケースが出てくる。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-05 10:43:20_

これをやる前に細かいのをマージした段階でCodexに全体レビューをしてもらうのもいいかもな。作業過程のドキュメントをうっかり残してたりとかするのでキレイにするフェーズ

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-05 12:12:38_

@truego Azureのproduction環境のデプロイが落ちてるのって僕に直す権限はありますかね？自分が全然使ってないのでどういう感じになってるのか把握してないなと気づきました。

#### スレッド返信

**Shingo OHKI** _2026-02-05 13:56:44_

僕ももう少し見ようと思ってまだ原因調査が十分にできていないのですが、基本的にはこの GitHub Actions で deploy されているので、リポジトリに権限があれば修正は可能だと思います！<https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/.github/workflows/azure-deploy.yml>

Azure の権限もお渡しできます。必要であれば言ってください！

**NISHIO Hirokazu** _2026-02-05 14:08:59_

一旦Codexに修正計画を立てさせるところまでやって確認してみますね！

**NISHIO Hirokazu** _2026-02-05 15:31:49_

CodexがPRを作ってくれましたけどこれが正しく機能するかどうかってどうやって確かめるのがいいですかね。
mergeするしかないです？

**Shingo OHKI** _2026-02-05 17:09:45_

以前開発してた時は、確か手元のリポジトリのブランチへのマージがトリガーになるように azure-deploy.yml を修正して試してました
（自分の azure 環境に）
そんなことをしなくていいように、そろそろ dd2030 としてそういうテスト用の場所を用意してもい良いのかもしれませんね

**Shingo OHKI** _2026-02-05 17:18:02_

もし急ぎでなければ、僕の方で確認しておきましょうか？

**Shingo OHKI** _2026-02-05 22:35:48_

現状万が一止まって困る人そこまでいないと思うので merge してみます

**Shingo OHKI** _2026-02-05 22:58:16_

なぜか僕がレビューできなくて merge ができない...

**Shingo OHKI** _2026-02-05 23:04:00_

あー、これは僕がPR内のボタンで main ブランチへの追従をしてしまったから、僕もレビュイーになってしまったので、自分でレビューできなくなっちゃったのかな？

**Shingo OHKI** _2026-02-05 23:06:30_

@shinta.nakayama
<https://github.com/digitaldemocracy2030/kouchou-ai/pull/780>
これマージしてもらえませんか？

**中山心太（tokoroten）** _2026-02-05 23:28:31_

@truego レビュアーに自分を突っ込んで、ノールックでapproveして、マージしておきました。


#### 02月06日(Fri) - 21件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-06 11:18:31_

memo: デモサーバがあるとドキュメントともここをみて」とかスクリーンショットを取ったりとかやりやすくて整備しやすい

#### スレッド返信

**Shingo OHKI** _2026-02-06 11:48:07_

今あるデモ環境、一応 basic 認証をかけているので大々的にURLを公開していない（やり取りがあればその中でご紹介しているにとどめている）のですが、もうちょっと気軽に使える良い方法ないでしょうか。

**Shingo OHKI** _2026-02-06 11:51:47_

きっとこうなっている
1. 気になって DD2030 の web ページを見る
2. GitHub を見る（本質的な価値判断をする前に試すハードルで挫折する）
=== 大きな断絶 ===
3. git clone して試す

「自治体にエンジニア組織を置いてくれ」は、理想的だとは思うけど、僕ら側の勝手なエゴかも？

**Shingo OHKI** _2026-02-06 11:52:25_

きっとそこで止まるより、どうやったら現場で使われるかを考えたほうがいい

**NISHIO Hirokazu** _2026-02-06 12:04:04_

GitHubを見るのはハードル高いから
1. 気になって DD2030 の web ページを見る
2. デモサイトで動いているものを見る(public-viewer側)
3. デモサイトで管理画面を見る(admin側)
4. GitHub を見る（本質的な価値判断をする前に試すハードルで挫折する）
とかにできるといいですよねぇ

**Shingo OHKI** _2026-02-06 12:06:38_

ブロードリスニング本が出て認知が広がるとこの傾向は加速すると思いました

**NISHIO Hirokazu** _2026-02-06 13:19:10_

サーバ費用とエンジニアリングコストを度外視するなら理想はこうですかね
- 公開デモ環境はパスワードなし
- dd2030にコンタクトを取ってミーティングをする自治体には独立非公開デモ環境を提供

**NISHIO Hirokazu** _2026-02-06 13:47:05_

デモ環境を用意することが現状は手間だけど、将来的にこれがCLIでコマンド1行売って待ってればできるようになった場合、さほど非現実的ではなくなる
デモ環境0→1は大変だったけど1→2はそれほどでもない可能性が高い

### **Shingo OHKI** in #2_開発_広聴ai _2026-02-06 11:48:07_

今あるデモ環境、一応 basic 認証をかけているので大々的にURLを公開していない（やり取りがあればその中でご紹介しているにとどめている）のですが、もうちょっと気軽に使える良い方法ないでしょうか。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-06 14:36:36_

memo: CLIで生成したレポートをWebUIで見たい場合(workdirは別のところにあるとする)
CLIで生成されたoutputの中のdirをkouchou-ai側でln -sしたうえでstatus.jsonを編集してレポートとして追加すればいい
これは自明ではないので、むしろCLI側の機能としてあるといいのではないか

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-06 14:38:28_

memo: Codexに“kouchou-aiで分析して“というだけで分析はしてくれたが、1000件のデータに対してクラスタの個数が[3, 6]だったのでやり直し、ここはいい感じのデフォルト値が選ばれるようにしたい

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-06 14:51:25_

Codexに[10, 100]でやりなおせと指示したら、configを編集して再実行したのでレポートは自動的に上書きされ、WebUIの側ではリロードするだけで10,100の分析結果を見ることができた

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-06 14:52:04_

memo: CLIのコードを更新した時にPyPIが自動的に更新されるようにしたい


#### 02月07日(Sat) - 22件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-07 10:25:47_

Azureの環境をどういじったかという情報は @truego さんに共有しておくべきだが、Slackに書くべきではない気がしており、たとえばGoogle Docsなどで「linkで共有」ではなく対象者を名指しで共有してAzure ダッシュボードのアクセス権と範囲の一致しているドキュメントにするのが良いのではないか、と思ってます

#### スレッド返信

**Shingo OHKI** _2026-02-07 10:30:47_

これを見て、試しにそういう場所を作ってみようと思ったのですが、
権限的に制限をかけられない
<https://drive.google.com/drive/u/0/folders/1RZ1CCtm72Ngs1RDwgADrDOU9N7CQnFSX>

@oscar.gaddress
このフォルダの権限を特定のメンバーに限定することはできますか？

**Shingo OHKI** _2026-02-07 10:31:20_

何かの下に作るのではなく、そういうトップフォルダを作る必要があるのかな？

**小野翔太** _2026-02-07 10:32:17_

そうですね、トップフォルダの権限に依存する作りです

**Shingo OHKI** _2026-02-07 10:34:11_

お手隙で↑のフォルダをその様にしていただけませんか？
一旦西尾さんと大木に制限された場所にして、かつ、（今後運用方法を自由に変えられるように）可能ならこの二人がこのフォルダの共有権限を修正できるようにしたいです。

**Shingo OHKI** _2026-02-07 10:35:47_

（この手の話は、DD2030内のどのプロジェクトでもありそう）

**小野翔太** _2026-02-07 10:39:45_

共有設定してみました！

**NISHIO Hirokazu** _2026-02-07 10:54:56_

@truego <https://docs.google.com/document/d/1lcX2mw_dLGGBZF-a83IYDn1FZqkPEt37sj6AS8HtynI/edit?tab=t.0#heading=h.ulqincydsdlf>
こんな感じになりました

**NISHIO Hirokazu** _2026-02-07 10:55:02_

見れます？

**Shingo OHKI** _2026-02-07 10:56:32_

ありがとうございます。見れました！

**Shingo OHKI** _2026-02-07 11:02:24_

メモ
このフォルダIDは使用していない
現在のフォルダは<https://drive.google.com/drive/u/1/folders/1RZ1CCtm72Ngs1RDwgADrDOU9N7CQnFSX|こちら>
<https://dd2030.slack.com/archives/C08F7JZPD63/p1770427847305119?thread_ts=1770427547.259829&cid=C08F7JZPD63>

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-07 10:46:43_

deploy, re-runしてsuccessしました <https://github.com/digitaldemocracy2030/kouchou-ai/actions/runs/21740920722/job/62820695796>

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-07 11:03:07_

管理画面は見れたけどviewerがstream timeoutになる

#### スレッド返信

**Shingo OHKI** _2026-02-07 11:09:51_

public-viewer コンテナがうまく起動していないっぽいですね

**Shingo OHKI** _2026-02-07 11:10:36_

> 2026-02-07T02:10:05.99697  Connecting to the container 'public-viewer'...
> 2026-02-07T02:10:06.15824  Successfully Connected to container: 'public-viewer' [Revision: 'public-viewer--0000006', Replica: 'public-viewer--0000006-bd7c7cfd9-cm7s5']
> 2026-02-07T02:07:37.4069516Z stderr F Error: Next.js inferred your workspace root, but it may not be correct.
> 2026-02-07T02:07:37.4069536Z stderr F     We couldn't find the Next.js package (next/package.json) from the project directory: /repo/apps/public-viewer/app
> 2026-02-07T02:07:37.4069550Z stderr F      To fix this, set turbopack.root in your Next.js config, or ensure the Next.js package is resolvable from this directory.
> 2026-02-07T02:07:37.4069564Z stderr F     Note: For security and performance reasons, files outside of the project directory will not be compiled.
> 2026-02-07T02:07:37.4069577Z stderr F     See <https://nextjs.org/docs/app/api-reference/config/next-config-js/turbopack#root-directory> for more information.
> 2026-02-07T02:07:37.4069591Z stderr F 
> 2026-02-07T02:07:37.4069642Z stderr F     at ignore-listed frames
> 2026-02-07T02:07:37.4311866Z stdout F  ELIFECYCLE  Command failed with exit code 1.
> 2026-02-07T02:07:38.3251496Z stdout F 
> 2026-02-07T02:07:38.3251884Z stdout F > @kouchou-ai/public-viewer@0.1.0 start /repo/apps/public-viewer
> 2026-02-07T02:07:38.3252035Z stdout F > next start
> 2026-02-07T02:07:38.3252054Z stdout F 
> 2026-02-07T02:07:38.9973477Z stdout F ▲ Next.js 16.1.5
> 2026-02-07T02:07:38.9975851Z stdout F - Local:         <http://localhost:3000>
> 2026-02-07T02:07:38.9975961Z stdout F - Network:       <http://100.100.205.57:3000>
> 2026-02-07T02:07:38.9977146Z stdout F 
> 2026-02-07T02:07:38.9979372Z stdout F ✓ Starting...
> 2026-02-07T02:07:39.7286568Z stderr F Error: Could not find a production build in the '.next' directory. Try building your app with 'next build' before starting the production server. <https://nextjs.org/docs/messages/production-start-no-build-id>
> 2026-02-07T02:07:39.7287029Z stderr F     at ignore-listed frames
> 2026-02-07T02:07:39.7969639Z stdout F  ELIFECYCLE  Command failed with exit code 1.
<https://portal.azure.com/#@c4jadmindd2030.onmicrosoft.com/resource/subscriptions/079e8ef5-7461-407d-84b6-b4f37b9f31c1/resourceGroups/dd2030-kouchouai-demo-rg/providers/Microsoft.App/containerApps/public-viewer/revisionManagement|https://portal.azure.com/#@c4jadmindd2030.onmicrosoft.com/resource/subscriptions/079e[…]Microsoft.App/containerApps/public-viewer/revisionManagement>

**Shingo OHKI** _2026-02-07 11:11:06_

コンソールにはこんなのが出てました

**NISHIO Hirokazu** _2026-02-07 11:56:41_

> 原因は *public-viewer のランナーイメージにワークスペースのルート情報が無い* ため、Turbopack が next を解決できず next build が失敗している点です。
> 修正は「ランナーにもルートの <https://file+.vscode-resource.vscode-cdn.net/Users/nishio/.vscode/extensions/openai.chatgpt-0.4.71-darwin-arm64/webview/#|package.json> / <https://file+.vscode-resource.vscode-cdn.net/Users/nishio/.vscode/extensions/openai.chatgpt-0.4.71-darwin-arm64/webview/#|pnpm-workspace.yaml> / .npmrc を含める」ことです。
なるほど、Dockerfileを修正してみます

(next buildが失敗しているのにCIがsuccessしたらダメだと思うがそれはさておき)

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-07 14:07:35_

viewerはOKになってるのに「viewerのbuildが通ってないのにCIがsuccessになるのはダメでしょ」で入れたチェックが厳しすぎてCI failになってたことがわかりましたw

#### スレッド返信

**NISHIO Hirokazu** _2026-02-07 14:10:35_

Codexいわく

事実関係（今回の run）:
public-viewer の最新 revision は 2026-02-07T04:47:34Z 作成
その revision 内で next build が走って 04:51:25Z 頃に Ready
CI の「デプロイ確認」は 04:47:43Z 開始 -> 04:50:26Z で終了（= public-viewer が立ち上がる前にタイムアウト）
現在は api も public-viewer も curl で 200 を返しています（こちらでも確認済み）

**NISHIO Hirokazu** _2026-02-07 14:10:45_

---
3分ではビルドが終わらないぞと言うことらしい

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-07 14:30:15_

めでたしめでたし

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-07 17:30:12_

テストも通ってデモ環境デプロイもうまく動いているということで、open PRのgeminiの更新の券が終わったら次は
「テストやデプロイを壊さないようにしながらいらないファイルを消す」をやろうと思います。
うっかりAIが生成した一時的ドキュメントが残ってたりするのと、消す作業はAIに任せると良くなさそうなので人間がやる
AIには削除するのではなくレビューして必要なさそうなものを見つけたり矛盾した記述を見つけたりしてもらう


#### 02月08日(Sun) - 1件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-08 10:21:53_

geminiのアップデートもできて、自動デプロイも問題なく動いてますね、めでたしめでたし


#### 02月09日(Mon) - 3件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-09 16:16:30_

RepoにCLAUDE.mdを置くのはやめる方針
• docs/for-ai/ あたりにおいて、AIに読ませたい人は自分のCLAUDE.mdなりAGENTS.mdなりskillなりcustom commandなりに入れる
• 領域ごとにmdは分ける、WebUIを開発する時にpythonの分析プロセスの知識は必要ないのでcontextに入れるべきではない
• CLAUDE.mdなどは.gitignoreに入れる

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-09 16:19:38_

まあ `@<filename>` で読ませてもいいしね

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-09 16:29:02_

なぜそう思ったかというと、PRを作る時点でPRテンプレートを尊重してほしいからCLAUDEに入れようかなと開いてみて、そもそもこれ自体も改善か必要だなとなった


#### 02月10日(Tue) - 20件

### **中山心太（tokoroten）** in #2_開発_広聴ai _2026-02-10 05:10:37_

<https://x.com/annotakahiro24/status/1882912202602201370>
そういえば、XのAPIのプランが変わったので、これをアップデートしたいですね。

### **中山心太（tokoroten）** in #2_開発_広聴ai _2026-02-10 05:13:06_

10月にAPIが刷新されたけど、取得は月5000ドルのママだった

### **Ryoma Kawabe Yuki** in #2_開発_広聴ai _2026-02-10 07:34:40_

最近従量課金プランが出ましたね

#### スレッド返信

**Ryoma Kawabe Yuki** _2026-02-10 07:42:28_

プライシングはこちら
<https://developer.x.com/#pricing|https://developer.x.com/#pricing>

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-10 10:30:52_

1週間分を取得して1000件いかないケースが多いんじゃないかと思うので「取得して溜める」みたいなのとセットで提供したいですね

### **中山心太（tokoroten）** in #2_開発_広聴ai _2026-02-10 18:31:45_

あー、ほんとだ、見落としてた。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-10 19:44:52_

やっと手元の広聴AIのリポジトリがクリーンになった
テストの実装にPandas依存があった

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-10 19:59:19_

CodeXの提案
• test/ と tests/ が分かれているのでどちらかに統一（test/ にまとめる or tests/ に寄せる）
• setup_*.sh start_*.sh stop_*.sh は scripts/ に移動＋短いREADMEで入口を作ると見通しが良い
あー、なるほどね〜

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-10 20:03:21_

そもそもこのシェルスクリプト、かなり初期にドキュメントの内容を誰かがシェルにまとめたもので、その後の変更に合わせてメンテしてないのではないかという気がする(ドキュメントにもこれを使えとは書いていない)

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-10 20:11:18_

> test/ と tests/ が分かれている
なるほど、Playwright Agentがtestsを仮定していてそこに作りにくるが、従来からのテストはtest/にある、と。testsに一本化するのが良さそう

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-10 20:26:26_

各フォルダにあるREADMEは各フォルダにあるべきだが、ドキュメントにも含まれるといいかもしれない

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-10 20:53:47_

READMEまとめのカテゴリができた

### **中山心太（tokoroten）** in #2_開発_広聴ai _2026-02-10 21:04:30_

@nishio.hirokazu
<https://github.com/digitaldemocracy2030/kouchou-ai?tab=readme-ov-file>

開発者でない方は以下のユーザーガイドを参照してください：
• <https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/docs/windows-setup.md|Windows 環境でのユーザーガイド>
• <https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/docs/mac-setup.md|Mac 環境でのユーザーガイド>
• <https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/docs/linux-setup.md|Linux 環境でのユーザーガイド>
これがリンク切れという報告を貰いました。

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-10 21:05:20_

直します

### **中山心太（tokoroten）** in #2_開発_広聴ai _2026-02-10 21:05:43_

```「一般向けにはリンク先の閲覧ができない」件につきましてですが、
GitHub の README.md 内の「手順」の「開発者でない方は以下のユーザーガイドを参照してください：」の直下に、
ある三つのリンクが見当たらないようでした。
確認したところ、kouchou-ai/docs/getting-started/ 配下に説明があることを把握いたしました。```

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-10 21:07:05_

ドキュメントからではなくREADMEからってことね

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-10 21:07:37_

GitHubでMarkdownプレビューを見てリンクを辿った時にGitHub上でMarkdownに飛ぶべきかdocsに飛ぶべきか

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-10 21:08:18_

docsの側はmkdocs画リンク切れとかを検知してくれるので生Markdownであんまり複雑なことをしないのが正しいな

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-10 22:00:57_

READMEのリンクを押したらドキュメントサイトに飛ぶようになりました

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-02-10 22:04:03_

ドキュメントを本格的に改善するのは本の原稿がFIXしてリリースされるまでの間にしたらいいかな〜という気持ち



### #2_コアループ_tech (54件のメッセージ)

#### 02月05日(Thu) - 5件

### **U0A67RK86BH** in #2_コアループ_tech _2026-02-05 13:10:23_

@yuki.kawabe <@U0A6CE44B2S> （<@U0A6P8CRT1Q> <@U0A7K64JT71> <@U0AAL9KK2S1>）
先日のMTGで出た以下論点について、若尾先生からの返信内容です。

●事前学習資料はどのようなものを用意したのか？
→事前に参加者に提供した資料は、東京で行ったDPは紙面による提供、メタバースのDPは紙面（原本は英語を日本語訳したもの）とメタバースとはなにかの紹介ビデオ（日本語による吹き替え）です。所有権はスタンフォードにありますので、スタンフォードにお問い合わせください。尚、現在ホームページが変わってしまったようで見つかりませんでしたが、2012年の対面型DPで使用された討論資料を添付します。これは政府のサイトで公開されておりましたので共有しても問題ないかと思います。

 ●通報機能の必要性はどの程度か？
→また攻撃的発言発生時の対応ですが、攻撃的発言に限らず、何か不足な事態が発生した場合（例：別の参加者の音が聞こえないなど）、だれでも通報できるようになっています。同時開催しているプラットホームを監視していますので、フラッグがあがるとすぐに対応できるようになっています。また、これまでの経験では攻撃的発言などの通報はありませんでした。すべて機械的トラブルなどに関する通報でした。

#### スレッド返信

**Ryoma Kawabe Yuki** _2026-02-05 14:07:16_

この資料すごいですね、これ読むだけで1日じゃ足りなそうです

**Ken Suzuki** _2026-02-05 14:11:24_

結構内容も表現も難しいね。

**Ryoma Kawabe Yuki** _2026-02-05 20:33:31_

今話してる内容にあわせて動的に関連ある資料教えてくれるとか参加者としては便利そう

**Ken Suzuki** _2026-02-05 20:59:40_

政府のプロジェクトだから、官僚が資料作成したのかな


#### 02月06日(Fri) - 7件

### **Ryoma Kawabe Yuki** in #2_コアループ_tech _2026-02-06 17:39:44_

一気に300人同時に熟議するより、100人に分けて3週間やるとか議論の質を上げるにはにいい気もしてきた。正統性や学術的側面からは同条件ではないので弱まるかもしれないが。

### **Ryoma Kawabe Yuki** in #2_コアループ_tech _2026-02-06 17:41:38_

たとえば、熟議中に使われる単語の意味するところが人によって違うことがあり、そこを揃えないと議論が成り立たないという話がこれまでに何度か出てきてた。それはAIのサポートを得るにも問題になる。
そこで、1週間目の100人でやったデータからGraphRAGなどで辞書をつくり、それをつかって2週目やって辞書を強化して、3週目をやるみたいな。

今回は基本に忠実でいいと思うけど

#### スレッド返信

**Ryoma Kawabe Yuki** _2026-02-06 17:43:18_

@takagishunsuke1129 @shutaro.aoyama 
自分ごと化会議って4回やってるけど、倍速会議のレポート作成のプロンプトにこういう情報入れたりする議論ってしました？

設問をつくるときに前回までの結果を入力するのはやってると思うのだけど、レポート作成するときに語彙情報入れたりするのか

**Shunsuke Takagi** _2026-02-06 17:55:56_

@shutaro.aoyama 回答頼みます

### **Ken Suzuki** in #2_コアループ_tech _2026-02-06 17:43:29_

そうだね。過去分割事例がなかったか、Aliceに聞いてみたらいいのではないかな

### **NISHIO Hirokazu** in #2_コアループ_tech _2026-02-06 20:01:35_

> 熟議中に使われる単語の意味するところが人によって違うことがあり、そこを揃えないと議論が成り立たない
こういうのは少人数のを先にやって特定するのがいいと思いますね

### **NISHIO Hirokazu** in #2_コアループ_tech _2026-02-06 20:02:13_

こういうのの仲間なので100人も必要ないと思う <https://note.com/mikiok/n/n0784034f4004>


#### 02月07日(Sat) - 7件

### **Shutaro Aoyama (ぶるーも)** in #2_コアループ_tech _2026-02-07 07:37:01_

techチームの定例ってどの日時で行われていますか？<mailto:shutaro.aoyama@gmail.com|shutaro.aoyama@gmail.com> に招待いただけるとありがたいです！:man-bowing:

#### スレッド返信

**Ryoma Kawabe Yuki** _2026-02-07 11:13:33_

まだ定例化してないですー
ちなみにぶるーもさんが参加しやすいのって何時とかあります？

**Shutaro Aoyama (ぶるーも)** _2026-02-07 11:16:14_

13時以前か、20時以降の遅い時間だと助かります!

**Ryoma Kawabe Yuki** _2026-02-07 11:16:27_

ありがとうございます

### **Ryoma Kawabe Yuki** in #2_コアループ_tech _2026-02-07 11:45:17_

Techチームの定例調整させてください！
:one: 月曜日 9:00~
:two: 月曜日 12:00~
:three: 月曜日 20:00~
:four: 火曜日 12:00~
:five: 火曜日 20:00~
:six: 木曜日 9:00~
:seven: 木曜日 12:00~
:eight: 木曜日 20:00~
:nine: 金曜日 20:00~

### **Ryoma Kawabe Yuki** in #2_コアループ_tech _2026-02-07 11:46:18_

<!here>↑明日の夜まででいったん決めようかと思います！


#### 02月08日(Sun) - 1件

### **Ryoma Kawabe Yuki** in #2_コアループ_tech _2026-02-08 12:06:49_

いまの回答数でレポート出したので共有しておきます
<https://app.baisoku-kaigi.com/sessions/6b8b7cee-35ba-4ec7-ae65-0a925f2cd3ac/8a304aba-5e9f-4047-a58e-3dc26747353d|https://app.baisoku-kaigi.com/sessions/6b8b7cee-35ba-4ec7-ae65-0a925f2cd3ac/8a304aba-5e9f-4047-a58e-3dc26747353d>


#### 02月09日(Mon) - 8件

### **Ryoma Kawabe Yuki** in #2_コアループ_tech _2026-02-09 21:12:48_

@truego @takagishunsuke1129 @shutaro.aoyama <@U0A40CF5ESY> @nishio.hirokazu
これまでの議論をまとめてみました！
既存ツールで最低限の達成できそうなことは確認しつつ、課題感を出しました。
これをもとに具体的な要件定義など詰めていけたらなと思っているので、コメントいただけるとうれしいです

<https://docs.google.com/document/d/1isqRSUvvympiNp8uKBWYHIAI8-CGNjePriZUfrN4qig/edit?tab=t.fpw85wxpadl1>

#### スレッド返信

**Shunsuke Takagi** _2026-02-09 21:27:23_

ありがとうございます。読んでみた感じだと、要件的には「倍速回避」が最適だと思ったんですけど、medyさんの懸念とかあれば、ぜひ今のうちにお聞きしたいです。

**Shunsuke Takagi** _2026-02-09 21:28:26_

ごめん、これりょうまくんに改めて聞きたいんだけど、このドキュメントって上記のチャットでいったようなオープンソースとか利用性、再現性みたいなところについて言及している感じには見えないんだけど、俺が見ているところが間違っているかな？
教えてほしいです。

**Ryoma Kawabe Yuki** _2026-02-09 21:46:57_

指摘ありがとう！

既存ツールで参照しているのは代替OSSになってるものをなるべく参照してる、Polis、Dify、Flanklyなど
熟議の進行のパートで参照しているSODPが利用可能性からは一番遠くて、利用お願いするのもハードル高いので明示的に書いている。
NotebookLMはOSSではないが、基本だれでも使えるのと、資料作成でかなり便利に使えるから入れている、倍速会議も

利用性、再現性のところも明示的に書き足しますね

**Ryoma Kawabe Yuki** _2026-02-09 22:44:23_

月並みではあるが言語化した
<https://docs.google.com/document/d/1isqRSUvvympiNp8uKBWYHIAI8-CGNjePriZUfrN4qig/edit?tab=t.c3ktrimkclhs>


#### 02月10日(Tue) - 18件

### **Ryoma Kawabe Yuki** in #2_コアループ_tech _2026-02-10 07:27:51_

@shutaro.aoyama <@U0AC6JX5N87> 
Techチーム定例 金曜日の20時からでお願いします:pray:
他にも都合つく方いたらぜひ参加くださいー

### **Ryoma Kawabe Yuki** in #2_コアループ_tech _2026-02-10 19:44:16_

@takagishunsuke1129 @shutaro.aoyama
Fluxつかってみたけどめちゃよかった。AIインタビューこれ使ってもいいかもと思った。

Fluxで話す中でひとつ課題が言語化できて、ブロードリスニングの体験を一直線にしたい、というのがあった。論点に対して賛否の表明、曖昧だけどなんとなく感じていることの表現、更に個人的なエピソードの深堀り、みたいなものがツール切り替えてやるのは無理があるなと。
今回いろいろツール試すのはそうなんだけど、全部ばらばらだとただただめんどくさくて落ちる人普通にいるとおもうので。

例えば、Polisや倍速会議で全体の中での自分の意見分布を理解して、その状態でFluxなりのAIインタビューに入れる感じは一直線かなと。倍速会議の最後のページに「XXXという観点さらに深く教えてくれませんか？（Fluxへのボタン）」といった流れ。

### **Ryoma Kawabe Yuki** in #2_コアループ_tech _2026-02-10 19:45:50_

あとは、このデータ学習に使われないの？とか、見れる人はどういうひとなの？といったことは機微な情報になるほどあるかなと。

今回、詐欺被害者のエピソードとか聞きたいのだけど、詐欺にひっかかった事実って結構恥ずかしいことで、安心感ないと深く話せないと思うのだよね。=> これはもはや解決出来るか不明だがw

#### スレッド返信

**Shunsuke Takagi** _2026-02-10 19:50:15_

たしかに、コアループ全体でアンケート結果とかをどう取り扱って、話してたっけ？勝手に事例とか書いたけど。。。

**Ryoma Kawabe Yuki** _2026-02-10 19:51:48_

まだ話してないね。
1/10のやつは大丈夫！

### **U0A6CE44B2S** in #2_コアループ_tech _2026-02-10 20:24:12_

@yuki.kawabe
お疲れ様です！
熟議の事前インプット用動画作成に向けて、1月？にAIで動画作成した際のコツなど習得したく、どなたにお伺いするのがよいでしょうか！？

#### スレッド返信

**Ryoma Kawabe Yuki** _2026-02-10 20:25:32_

@mami.s.dasein
1/10の動画いろいろ調整してNotebookLMでいい感じのつくってくれたとおもうのだけど、どのあたり難しかったとか、どうやって解決したとか言語化していただいてもいいでしょうか？


#### 02月11日(Wed) - 8件



### #2_broad-listening-book (53件のメッセージ)

#### 02月05日(Thu) - 4件

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-05 15:10:19_

tttc-light-js、コードをAIに読ませましたが、LLMによる分類を行ってるので、sensemakerと似たような構造なのね

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-05 16:05:17_

そうです、これはturboの時からそうだった

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-05 16:05:32_

turboのシンプル化としてそれがある

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-05 17:07:32_

某小崎さんは研究所のエライ人ではあるが、研究所の案件ではないので、分からないから、表玄関から行ってほしいとのこと。なので、表玄関から行ってきます。


#### 02月06日(Fri) - 3件

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-06 00:13:48_

<https://github.com/digitaldemocracy2030/broad-listening-book/blob/13-clustering-dimension-reduction/14_%E5%BA%83%E8%81%B4AI%E3%81%AE%E6%8A%80%E8%A1%93%E3%82%B9%E3%82%BF%E3%83%83%E3%82%AF%E8%A7%A3%E8%AA%AC.md|https://github.com/digitaldemocracy2030/broad-listening-book/blob/13-clustering-di[…]%A1%93%E3%82%B9%E3%82%BF%E3%83%83%E3%82%AF%E8%A7%A3%E8%AA%AC.md>
ClaudeCodeが広聴AIのミニマム実装と言って、サンプルコードを書き始めたので、これを採用した

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-06 11:22:50_

sensemakerとtttc lightの解説はどこかで書くか

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-06 11:37:53_

コラムで1ページとかでもいいんじゃない？


#### 02月07日(Sat) - 24件

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-07 17:28:45_

こんな感じかしら。

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-07 17:32:32_

この図で何を表現したいのか

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-07 17:33:29_

時系列的にはTurboとSensemakerが同時期

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-07 17:33:48_

単にレポジトリが公開されてなかっただけか

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-07 17:34:08_

チームみらいの広聴AIは一旦フォークしたけどマージされたから分けて書かなくていいんじゃないかなぁ

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-07 17:34:47_

公開されてなかったんだっけ？どれが？

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-07 17:36:02_

Sensemaker

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-07 17:36:56_

確かに公開は2025年1月ごろってGPTは言ってるな

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-07 17:39:27_

$ git log --reverse | head
commit d740ad4095c18d0b54a10fd5f74211e18ea762f5
Author: Alyssa Chvasta <<mailto:achvasta@google.com|achvasta@google.com>>
Date:   Tue Aug 20 16:51:51 2024 +0000

    Initial empty repository

commit e1b835425e1b2596f100334fbd2952283f4a1dea
Author: alyssachvasta <<mailto:achvasta@google.com|achvasta@google.com>>
Date:   Tue Aug 20 20:49:15 2024 +0000

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-07 17:39:42_

2024年8月が最初のコミットっぽい。

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-07 17:41:36_

8月はエンプティで、12月に初めて中身のコミットがあるのでは

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-07 17:41:48_



### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-07 17:41:55_

ほぼ同じ速度で同じことを調べてるなw

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-07 17:43:17_

2つ目のコミット12/10でドンと69ファイル追加している

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-07 17:44:11_

<https://github.com/Jigsaw-Code/sensemaking-tools/commit/e1b835425e1b2596f100334fbd2952283f4a1dea#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5|https://github.com/Jigsaw-Code/sensemaking-tools/commit/e1b835425e1b2596f100334fbd2952283f4a1dea#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5>

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-07 17:44:28_

ので公開タイミングはこれだろうね

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-07 17:46:32_

tttc-light-jsが2024年の3月っぽいので時系列は正しいんだけど、Sensemakerが参考にしたとするならtttc-light-jsではない方のTTTCだと思うな〜

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-07 17:48:42_

チームみらいの広聴AIを書くのはいいと思う(参院選のタイミングで、ということなら)
その後マージされてるのが矢印で表現されるもいいと思う

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-07 17:51:22_



### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-07 17:51:29_

こんなイメージ

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-07 17:58:48_



### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-07 17:58:52_

いまこんなかんじ

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-07 18:14:19_

jigsawのBGの事例、
polisで収集→sensemakerで分類、可視化なのか。
ようやく分かってきた

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-07 18:15:03_

<https://medium.com/jigsaw/how-one-of-the-fastest-growing-cities-in-kentucky-used-ai-to-plan-for-the-next-25-years-3b70c4fd1412>


#### 02月09日(Mon) - 5件

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-09 16:05:23_

富士通から電話がかかってきて、取材に割と好意的な感じ、取材内容や取り上げ方を聞いてきて、調整してまた連絡をするということです。

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-09 17:27:08_

:iihanashi:

### **Slackbot** in #2_broad-listening-book _2026-02-09 19:00:17_

リマインダー : <!here> :mega: 本日20時より、ブロードリスニング本執筆会議を開催します！:mega: :clock9: 20:00-21:00 :link: <https://meet.google.com/feh-cnpt-nhq> :memo: <https://docs.google.com/document/d/1plggszRTxEEYUcZuCLiHkPrBsMtxr3RQpctKtZe5y4M> • ブロードリスニング本執筆にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！ • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！

### **Shunsuke Takagi** in #2_broad-listening-book _2026-02-09 19:10:55_

高木です。本日、別件が立て込んでいて参加できません。後ほど議事録で内容を確認します。

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-09 19:18:42_

了解です。


#### 02月10日(Tue) - 16件

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-10 04:39:33_

伊藤議員に取材依頼を投げた。

### **GitHub** in #2_broad-listening-book _2026-02-10 12:24:21_



### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-10 12:32:19_

<https://x.com/nishio/status/2021063339242291561?s=20>

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-10 12:32:21_

公開した

### **NISHIO Hirokazu** in #2_broad-listening-book _2026-02-10 12:39:55_

しまった、投稿にリンクを含めない方が良かったか

### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-10 19:24:10_

Claudeのログファイルを読み込ませて、私が何文字を書いたのか調べたけど、こんな感じだったｗｗ

### **GitHub** in #2_broad-listening-book _2026-02-10 19:44:25_



### **GitHub** in #2_broad-listening-book _2026-02-10 19:44:44_



### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-10 19:49:21_

よむよむ

### **GitHub** in #2_broad-listening-book _2026-02-10 22:04:35_



### **GitHub** in #2_broad-listening-book _2026-02-10 22:04:35_



### **中山心太（tokoroten）** in #2_broad-listening-book _2026-02-10 22:05:55_

私の作業分をがつっとmainにマージしました。

### **GitHub** in #2_broad-listening-book _2026-02-10 22:26:59_



### **GitHub** in #2_broad-listening-book _2026-02-10 22:27:20_



#### スレッド返信

**GitHub** _2026-02-10 22:27:20_



### **GitHub** in #2_broad-listening-book _2026-02-10 22:27:20_




#### 02月11日(Wed) - 1件

### **GitHub** in #2_broad-listening-book _2026-02-11 01:53:52_





### #7_雑談 (42件のメッセージ)

#### 02月05日(Thu) - 1件

### **小野翔太** in #7_雑談 _2026-02-05 19:03:55_

コードラビットをpolimoneyでも導入したいのですが、権限ある方頂けると嬉しいです。
<https://github.com/moai-redcap/polimoney>
<https://github.com/moai-redcap/polimoney_ledger>
<https://github.com/moai-redcap/polimoney_hub>
（連携の仕組み等わかっていない）


#### 02月07日(Sat) - 8件

### **NISHIO Hirokazu** in #7_雑談 _2026-02-07 15:15:44_

よく調べてらっしゃる
<https://okadaasa.theletter.jp/posts/5c5f5c60-9c33-4311-832b-c78cc34efcd8|https://okadaasa.theletter.jp/posts/5c5f5c60-9c33-4311-832b-c78cc34efcd8>

### **NISHIO Hirokazu** in #7_雑談 _2026-02-07 15:21:13_

PolisがAIを使っていなかったのは「使わない意思決定をしたから」ではなく2015年段階でまだAIが今ほど発展してなかったからであって、今開発が進んでるPolis2.0は使うけどな？とか、オードリータンのPolisとチームみらいのT3Cとを対比させて語ってるけどそもそもオードリーが台湾でT3Cを使って「これはPolisの問題点を改善する」というメッセージを出してるのを見た後で我々は日本に持ってきてるわけなんだがなーとかの何箇所かの大きな欠点がある文章だけども、多様な考え方へのリンクがあって有益な文章ではあると思う

### **NISHIO Hirokazu** in #7_雑談 _2026-02-07 15:30:24_

とりあえず投票日前日だから明日は議論ができなくなるわけだしいま関わるのはめんどくさいなぁ

### **NISHIO Hirokazu** in #7_雑談 _2026-02-07 16:25:41_

さくっと解説書きました

### **NISHIO Hirokazu** in #7_雑談 _2026-02-07 16:25:44_

<https://x.com/nishio/status/2020033524951306271?s=46&t=gkSZtjGEtUZPO0JCzBxCBw|https://x.com/nishio/status/2020033524951306271?s=46&t=gkSZtjGEtUZPO0JCzBxCBw>

### **NISHIO Hirokazu** in #7_雑談 _2026-02-07 16:26:10_

<https://x.com/nishio/status/2020035764323766715?s=46&t=gkSZtjGEtUZPO0JCzBxCBw|https://x.com/nishio/status/2020035764323766715?s=46&t=gkSZtjGEtUZPO0JCzBxCBw>

### **Ken Suzuki** in #7_雑談 _2026-02-07 16:54:18_

まあ、実際に2024年のアライメント・アッセンブリーでは、polis 1.0とTTTCを併用しているからね。
そして、TTTCの開発者は事前にPolis開発者のColinのところをに来ていたんだけど、Colinは2.0の開発をすでに進めていたので、TTTCに協力するのを断ったという話も本人から聞いている。Polis 2.0は、マルチスケールのトピッククラスタリングができるので、散布図的UIももっているので、TTTCとの併用が必要なくなっている。

### **U0AC1UTNXNF** in #7_雑談 _2026-02-07 18:31:30_

*<https://minerva-project.org/|Minerva>*という政治家の公約の内容と、実行の有無を確認するサイトを作成しようとしています。

明日投開票ですが、まだまだデータが足りていない、極めて絶望的な状況です。私が個人で東京の全選挙区のデータは入力したのですが、個人の力ではどうしても限界があります。
数分間だけお時間をいただけませんか？

*<https://forms.gle/A2fSktiWefwYzeMt6|Google form>*から入力できます。

前回の選挙公報は各都道府県のウェブサイトまたは<https://shugiin.go2senkyo.com/50/|選挙ドットコム>などで確認することができます。
ご協力お願いします！

（Cfjの<https://cfj.slack.com/archives/C0ABTFUC93R|Slack>で運営しています）


#### 02月08日(Sun) - 1件


#### 02月09日(Mon) - 21件

### **中山心太（tokoroten）** in #7_雑談 _2026-02-09 10:47:04_

<https://x.com/tsurezure_lab/status/2020527255462740473>
エンベディングがこんなに綺麗に散布図になるわけないと思ってるんだけど、どうやってるんだろう。
ラベル付きの次元圧縮しているのかな

### **NISHIO Hirokazu** in #7_雑談 _2026-02-09 11:09:36_

政党ラベルをone-hotとかで入れて強い重みをつけてるかsupervised UMAPやるとかしないかぎり単なる意味のベクトルだけで政党が明瞭分離するわけがないですね

### **中山心太（tokoroten）** in #7_雑談 _2026-02-09 11:10:11_

youtubeから政党名で引っ張ってきてるので、政党名がエンベディングに大きな影響を与えていそう。

### **NISHIO Hirokazu** in #7_雑談 _2026-02-09 11:13:50_

あー、X投稿とかではなくYouTubeのタイトルと説明文なのか

### **NISHIO Hirokazu** in #7_雑談 _2026-02-09 11:14:09_

だとすると当然目立つところに政党名が入るよね

### **NISHIO Hirokazu** in #7_雑談 _2026-02-09 11:15:09_

政党名を正規表現などでマスクした時にどうなるか比較してみたいな

### **NISHIO Hirokazu** in #7_雑談 _2026-02-09 12:42:59_

tokorotenがTwitterで「これじゃダメだ」的なreplyをしているの見たけど、なんか新規ファンにダメ出しする古参ファンみたいな雰囲気でジャンルが衰退するからもっと優しくしたほうがいいと思ったw

### **中山心太（tokoroten）** in #7_雑談 _2026-02-09 12:46:55_

コード見せてくださいかなｗ

### **中山心太（tokoroten）** in #7_雑談 _2026-02-09 18:51:08_

<https://x.com/tokoroten/status/2020797429482700992>
さすがに一線を越えてると判断したので、殴っておいた

### **中山心太（tokoroten）** in #7_雑談 _2026-02-09 19:04:22_

広聴AIでアルゴリズムをウェブサービス上で公開する意味はあんまりないと思ってたけど、
こういうのを見るとウェブサービス上でアルゴリズムの該当部分にジャンプできないとだめだなぁ

### **NISHIO Hirokazu** in #7_雑談 _2026-02-09 20:34:33_

<https://x.com/tsurezure_lab/status/2020821148947321013?s=46&t=gkSZtjGEtUZPO0JCzBxCBw|https://x.com/tsurezure_lab/status/2020821148947321013?s=46&t=gkSZtjGEtUZPO0JCzBxCBw>
一応理屈は通ってる

### **NISHIO Hirokazu** in #7_雑談 _2026-02-09 20:35:47_

あと、単に見た目だけコピペして作ってる人は嘘でこの説明を思いつけないと思うので、実際そうやってるんだろうなとは思った
説明不足は誤解を招いたけど、SNSの投稿で説明不足リスクを0にするのも無理だし、まあ仕方ないのではないかと

### **NISHIO Hirokazu** in #7_雑談 _2026-02-09 20:50:47_

ところで投票日前に投稿されてたAudrey/Polisとチームみらい/TTTCの比較記事に関して

2016年時点でColin自身は_“better public discourse through artificial intelligence”_という表現をしているし、
2023年の10月には1年間のLLMの発展を見てLLMを活用した自動サマリーを計画している
<https://github.com/compdemocracy/polis/issues/1725>
2024年の11月には実験的なものが動いている
<https://github.com/compdemocracy/polis/issues/1842>

### **NISHIO Hirokazu** in #7_雑談 _2026-02-09 21:03:51_

AudreyがTIMEの取材に答えてTalk to the Cityを「星座みたいだ」と紹介しているところ
<https://moda.gov.tw/en/press/background-information/6477#46>

#### スレッド返信

**NISHIO Hirokazu** _2026-02-09 21:04:52_

翻訳

*ヤスミーン・サーハン*
 つまり、あなたはラディカル・トランスペアレンシーや、ファクトチェックのような市民社会の取り組みについて話してきましたが、政府が民主主義を強化するためにAIを取り入れる方法、あるいはすでに取り入れている方法はあると思いますか？
*オードリー・タン*
 はい、間違いなくあります。
 この「Talk to the City」というウェブサイトに行くと、Polisツールで集められた最近のアラインメント・アセンブリーを見ることができます。クリックすると、すぐにコンステレーション（意見の分布図）が表示され、しかもバイリンガルです。英語で書かれたコメントでも中国語（北京語）で書かれたコメントでも、同じクラスターとして表示されます。
*オードリー・タン*
 右側のクラスターをクリックすると、主要な論点が表示され、右上のレポートで要約も確認できます。さらに、そのクラスター内の個々のステートメントをクリックすると、そのクラスターと対話ができます。「なぜそう信じているのか」「もっと詳しく説明してほしい」「私は同意しない」といった形で会話ができるのです。
*オードリー・タン*
 これが私の言う「民主的アラインメント」です。私たちは市民に対して、「生成AIにどのように振る舞ってほしいか」を尋ねているだけです。そして、いわゆるウィキ・サーベイ――質問自体を市民や参加者が書くアンケート――を通じて、人々の全体的で混合された意思（volition）を簡単に把握できます。
*オードリー・タン*
 その詳細なコンテクストを、対面でのマルチステークホルダー対話のアジェンダとして使うことができます。そうすることで、皆がより全体像を把握できるようになります。まるで「群盲象を評す」ではなく、象を多次元的に見渡すようなものです。幹の部分だけを深掘りしたいなら、言語モデルと一緒にその部分を徹底的に探究することもできます。
*オードリー・タン*
 常にオンラインで質問に答える専門のファシリテーターやモデレーターを置く代わりに、こうした仕組みを使えば、熟議のプロセスを容易にスケールさせ、熟議の成果を、参加したいすべての人が対話的に利用できるようになります。
*オードリー・タン*
 そして、丸一日かけて行う対面ワークショップでは、人々が最終的に合意した規範について長い書き起こしを作ります。この長いコンテクストを使って、コンスティテューショナルAI（憲法AI）モデルを訓練します。つまり、そのAIが、参加者が「こう振る舞うべきだ」と合意した通りに振る舞うようにするのです。言語モデルのための憲法を共同で作るようなもので、さらに新しいフィードバックを継続的に統合することで、モデルは人々の望みにますます合致していきます。
*オードリー・タン*
 だから私は、これは民主主義にとって良いことだと思います。熟議民主主義をスケーラブルにするだけでなく、AI開発そのものを民主化するからです。トップラボの少数のエンジニアだけが振る舞いを決めるのではなく、人々自身が決めるのです。

### **NISHIO Hirokazu** in #7_雑談 _2026-02-09 21:04:10_

2023-08-14

### **NISHIO Hirokazu** in #7_雑談 _2026-02-09 21:07:29_

で、安野さんは1年もかからず2024年の5月にTalk to the Cityのことを知って7月の都知事選で使うと決めた、という感じ。

### **NISHIO Hirokazu** in #7_雑談 _2026-02-09 21:08:19_

Alignment AssemblyでTalk to the Cityを使ったこと自体はこの記事より前だから1年くらいは経ってるかもしれないな、いつが最初かは知らない

### **NISHIO Hirokazu** in #7_雑談 _2026-02-09 21:51:22_

いつが最初なのかChatGPTに探させた結果、これが最初だと思うということで
<https://moda.gov.tw/major-policies/alignment-assemblies/2023-ideathon/1459>
健さんの指摘の通り2023年の台北台南での熟議の前段階としてやったオンラインPolisの結果をTalk to the Cityしたものが最初みたいだね

### **NISHIO Hirokazu** in #7_雑談 _2026-02-09 22:08:59_

extractionを2023-10-13にやってtakeawayは2023-10-17だということがわかった。なのでTIMEの取材に見せたりしてるのはここで公開されているのよりも前に作られたもので、それはまあ一般にWebサイトで公開する前に内部的に作ってたものなんだろうな

### **NISHIO Hirokazu** in #7_雑談 _2026-02-09 22:32:11_

Plurality Seoul で講演したのが2023-12-02か
<https://scrapbox.io/plurality-japanese/Audrey_Tang_Remarks_in_Plurality_Seoul>


#### 02月10日(Tue) - 11件

### **NISHIO Hirokazu** in #7_雑談 _2026-02-10 00:22:49_

Noteにまとめておきました
<https://note.com/nishiohirokazu/n/n58b6f250d298>

#### スレッド返信

**Ken Suzuki** _2026-02-10 00:44:28_

抑制のきいたよい記事だと思いました。

### **中山心太（tokoroten）** in #7_雑談 _2026-02-10 02:17:48_

@nishio.hirokazu
この内容そのままでTwitterの記事機能を使ってみてほしい

### **NISHIO Hirokazu** in #7_雑談 _2026-02-10 10:12:56_

Twitterの記事機能のエディタがポンコツすぎて発狂した

### **NISHIO Hirokazu** in #7_雑談 _2026-02-10 12:05:17_

民間企業のSNSが社会のインフラになって、課金ユーザと非課金ユーザでできる行為に差ができると、国税15円以上払わないと投票券をあげないよ〜の時代を連想するな…

### **NISHIO Hirokazu** in #7_雑談 _2026-02-10 12:09:50_

しかしまあ、確かにTwitterの記事機能を使った方が今の瞬間の広報力は高いなと思う、それはXが今この機能を使わせたくてそういう拡散パラメータにしているからだろう。一時的ボーナスタイムだと思う。

### **NISHIO Hirokazu** in #7_雑談 _2026-02-10 12:41:00_

いい議論
<https://x.com/hiroosa/status/2021055354013090161?s=20>

### **Shutaro Aoyama (ぶるーも)** in #7_雑談 _2026-02-10 15:50:58_

<https://x.com/XJaravel/status/2020564900787913171|https://x.com/XJaravel/status/2020564900787913171>

#### スレッド返信

**NISHIO Hirokazu** _2026-02-10 16:52:54_

音声インタビューもあるのか

**NISHIO Hirokazu** _2026-02-10 16:54:44_

> licensed under the PolyForm Noncommercial License 1.0.0
初めて見た

**NISHIO Hirokazu** _2026-02-10 16:59:41_

(GPT5)
Personal Uses（個人利用の例）
研究・実験・テスト・個人学習・趣味・娯楽などはOK……と書きつつ、
> without any anticipated commercial application
>  （商用応用が見込まれないこと）
という条件がついてます。
 つまり「趣味で触ってたけど、あとでビジネスに使うつもりが最初からある」みたいなケースは *“個人利用だからOK”と言い切れない*、という含みがあります。
Noncommercial Organizations（非商用組織での利用）
慈善団体、教育機関、公的研究機関、政府機関などは、資金源がどうであれOK、としています。
 （ただし、ここで列挙されてない一般企業はこの恩恵を受けません。）
---
まあ、商用利用しないつもりなら使えるってことか



### #2_新しいプロジェクトの種 (40件のメッセージ)

#### 02月05日(Thu) - 12件

### **NISHIO Hirokazu** in #2_新しいプロジェクトの種 _2026-02-05 15:43:10_

*熟議麻雀（暫定まとめ）*
•  目的は「賛成 vs 反対の勝敗」ではなく *分断状態から合意に近づくプロセス自体をゲーム化*
• 4人卓（人 or AI）で開始時は賛否が割れている
• ターン制で短い発言を出す
• *AI審判*が各発言を即時評価
    ◦ 有効 / 警告 / 無効
    ◦ 追加で「合意促進」「整理貢献」「分断深化」などを判定
•  *勝敗なし*
    ◦ 卓全体：合意度ゲージが上下
    ◦ 個人：合意への貢献度スコアが付く
• 両者の懸念を要約したり、条件付き妥協案・共通価値を提示すると高得点
• まずは *人1 + AI3のソロモード*で体験学習 → 将来は人×人も
:point_right: 論破が強い人ではなく *橋をかける人が評価される熟議ゲーム*

### **NISHIO Hirokazu** in #2_新しいプロジェクトの種 _2026-02-05 15:44:19_

---

審判のAIの振る舞いによってゲーム性がだいぶ変わりそう

### **NISHIO Hirokazu** in #2_新しいプロジェクトの種 _2026-02-05 15:45:25_

審判も何体か入れて、ゲーム終わった後に審判と対戦相手を5段階評価して、評価高いやつが残っていくようにするか？

### **中山心太（tokoroten）** in #2_新しいプロジェクトの種 _2026-02-05 15:46:20_

島モデル遺伝的アルゴリズムみたいな感じだなぁ

### **NISHIO Hirokazu** in #2_新しいプロジェクトの種 _2026-02-05 15:46:50_

審判プロンプトをtokorotenの遺伝的アルゴリズムで改善しよう()

### **NISHIO Hirokazu** in #2_新しいプロジェクトの種 _2026-02-05 16:09:38_

人間に「自分が賢いと思いたい」や「他人から賢いと思われたい」という欲求がある(欲求の強い人と弱い人がいる)

その欲求の満たし方に2つのモードがある
A: 他人が自分より愚かであることを示す
B: 他人と共同で何かを成し遂げるプロジェクトでの自分の貢献の大きさを最大化する

Aのモードになると不毛な足の引っ張り合いにしかならないので、人をBのモードに誘導するゲームデザインが必要

### **中山心太（tokoroten）** in #2_新しいプロジェクトの種 _2026-02-05 16:13:01_

<https://econ101.jp/%E3%83%8E%E3%82%A2%E3%83%BB%E3%82%B9%E3%83%9F%E3%82%B9%E3%80%8C%E5%AF%8C%E3%81%AE%E5%86%8D%E5%88%86%E9%85%8D%EF%BC%9F%E3%81%84%E3%81%84%E3%82%84%E3%80%81%E6%95%AC%E6%84%8F%E3%82%92%E5%86%8D%E5%88%86/|https://econ101.jp/%E3%83%8E%E3%82%A2%E3%83%BB%E3%82%B9%E3%83%9F%E3%82%B9%E3%80%8C[…]E3%82%84%E3%80%81%E6%95%AC%E6%84%8F%E3%82%92%E5%86%8D%E5%88%86/>
敬意の再分配の話が繋がってきた。

### **中山心太（tokoroten）** in #2_新しいプロジェクトの種 _2026-02-05 16:15:47_

敬意の再分配ができるPICSY

### **NISHIO Hirokazu** in #2_新しいプロジェクトの種 _2026-02-05 16:20:28_

> B: 他人と共同で何かを成し遂げるプロジェクトでの自分の貢献の大きさを最大化する
> Aのモードになると不毛な足の引っ張り合いにしかならないので、人をBのモードに誘導するゲームデザインが必要
賛否の分かれてる人と共同で両方が同意できる文章を作って、完成した文章は一定期間トップページに掲載されて、いいねをもらった量がチーム全員の得点？

### **NISHIO Hirokazu** in #2_新しいプロジェクトの種 _2026-02-05 16:20:49_

チームに与えられた得点を貢献度によって分配？

### **中山心太（tokoroten）** in #2_新しいプロジェクトの種 _2026-02-05 16:24:20_

あとは、スイスドロー方式のようにして、良い調停を行うプレイヤー同士をぶつけていって、より良い人を選抜していって、良い解を探す、みたいなのはありそう

### **NISHIO Hirokazu** in #2_新しいプロジェクトの種 _2026-02-05 18:10:53_

ChatGPTが面白いこと言ってる
ここまで来ると、熟議麻雀は：

合意形成能力・調停能力・敬意配分を進化させる
人間×AIの共進化ゲーム

で、
	•	審判AIも進化対象
	•	プレイヤーも進化対象
	•	解（合意文）も進化対象

という 三重進化系になってる。


#### 02月07日(Sat) - 2件

### **NISHIO Hirokazu** in #2_新しいプロジェクトの種 _2026-02-07 13:28:56_

熟議麻雀の開発画面

#### スレッド返信

**Ken Suzuki** _2026-02-07 16:50:24_

仕事はや。


#### 02月08日(Sun) - 12件

### **Ryoma Kawabe Yuki** in #2_新しいプロジェクトの種 _2026-02-08 18:55:21_

自分でプレーするのは面倒なので、1人1体エージェントを持って自分ぽい議論をするように育てる放置ゲーぽいものをClaude code teamを試すためにつくり始めてみた。
ユーザーは知識や価値観とかをインプットにペルソナをつくっていくかんじ。
エージェントは定期的にトピックにそって10ターン制の熟議麻雀をプレーする

### **Ryoma Kawabe Yuki** in #2_新しいプロジェクトの種 _2026-02-08 18:57:11_

保有可能エージェント数や知識スロットの拡張で課金要素も入れれそうw

### **Ryoma Kawabe Yuki** in #2_新しいプロジェクトの種 _2026-02-08 18:58:06_

moltbookぽい

### **NISHIO Hirokazu** in #2_新しいプロジェクトの種 _2026-02-08 21:15:35_

それ筋いいと思う

#### スレッド返信

**Ryoma Kawabe Yuki** _2026-02-08 21:28:04_

全然関係ないんですけど、AI構文っぽくてAIかと思いましたww すいませんww

**NISHIO Hirokazu** _2026-02-08 22:19:46_

“うん、その直感かなり妥当だと思う。”

**NISHIO Hirokazu** _2026-02-08 22:20:06_

これは冗談のためにわざわざChatGPTのログからコピペしたw

**NISHIO Hirokazu** _2026-02-08 22:25:34_

まあ冗談はさておき、相手のアイデアを発展させる前にまず肯定的ストロークを返しておいたほうが、相手は「Yesといってるのか？Noといってるのか？」という負荷がなくなるからスムーズだよね感はあるね、積極的にやって行ってもいいのかも

### **NISHIO Hirokazu** in #2_新しいプロジェクトの種 _2026-02-08 21:16:56_

「審判AI」がまだいまいちバカで、僕のいい意見を低評価するのでムカついていますw

### **NISHIO Hirokazu** in #2_新しいプロジェクトの種 _2026-02-08 21:17:45_

なのでAIの議論を眺めて「どういう発言が良いのか」を人間の側がもっと言語化する必要がありそう

### **Ryoma Kawabe Yuki** in #2_新しいプロジェクトの種 _2026-02-08 21:29:18_

まだそこまでいってないですけど、審判AIむずいだろうなぁとぼくも思ってました。審判AIと熟議プロセスの開発は分担してもいいかもですね。

#### スレッド返信

**Ryoma Kawabe Yuki** _2026-02-08 21:30:07_

本あるとおもうので、いい感じに他の人も巻き込みつつ


#### 02月10日(Tue) - 12件

### **Ryoma Kawabe Yuki** in #2_新しいプロジェクトの種 _2026-02-10 00:03:43_

ターン制でオート熟議させていくの結構面白い。ここにユーザーの知識・方向性インプットがはいるとより多様になっておもしろいはず。いったん明日デプロイします

#### スレッド返信

**Ryoma Kawabe Yuki** _2026-02-10 00:13:43_

インプット無しだと着地点はあまり面白くないので、人間オーナーのインプット期待かなぁ。

```Session Summary
# 熟議セッション要約

この熟議では地域活性化について、中小企業経営者のTanaka、科学的アプローチ重視のHiro、環境科学者のYuki、変革志向の社会起業家Ryomaが議論を展開しました。

主な論点は、産業振興、環境との調和、実行力、意思決定プロセス、短期的効果と長期的持続可能性のバランスでした。議論は産業基盤からスタートし、三位一体アプローチ（産業・環境・社会）への合意が形成され、実装方法に焦点が移りました。

当初は理念と実践、変革の速度と規模について対立がありましたが、次第に各視点の統合へと進化。Ryomaの「資源流出阻止と迅速な実行」、Tanakaの「現実的で段階的な改革」、Hiroの「科学的検証」、Yukiの「環境容量と世代間公平性」という各主張が収束しました。

最終的に、小規模で迅速な実験と長期的視野を併せ持つ「デュアルシステム」という合意に達し、変革の速度と持続可能性を両立させる統合的アプローチが地域活性化の鍵だという結論に至りました。```
```Session Analysis
9: Quality
8: Cooperation
7: Convergence
8: Novelty

Summary
参加者たちは地域活性化について産業振興、環境持続性、意思決定プロセス改革、実行スピードなど多角的な視点から議論を展開した。Tanakaは実務家の視点から実行可能性を重視し、Hiroは科学的・データ駆動的なアプローチを提唱し、Yukiは環境容量と将来世代を考慮した持続可能性を強調し、Ryomaは意思決定の高速化と資源流出問題を指摘した。議論は初期の概念的フェーズから、徐々に具体的な実装方法へと深化し、最終的には各視点を統合したフレームワークへと収束した。

Highlights
Tanakaの「地域経営マトリクス」と「2-5-10の法則」は理論と実践を結びつける実用的な提案
Ryomaの「人・金・時間の流出」という分析は地域衰退の根本原因を物理法則に例えた鋭い指摘
Hiroの「データ駆動型の適応的実行プロセス」は科学的検証と実行スピードを両立させる提案
Yukiの「自然資本を基盤とした循環型地域経済」は環境持続性と経済活性化の両立を示した
Consensus
地域活性化には「スピード」と「持続可能性」の両立が不可欠であり、そのためには意思決定の分権化・高速化と科学的根拠に基づく長期的視野の統合が必要である。具体的には、現場への決定権委譲による高速実験サイクルと、環境容量評価に基づく長期的な持続可能な発展計画を同時並行で進めるデュアルトラック型のアプローチが効果的である。```

**Ryoma Kawabe Yuki** _2026-02-10 00:14:52_

ただ自分のペルソナを育てて、世界のいろんな人と熟議してもらえるのはめちゃいい気がする。

**NISHIO Hirokazu** _2026-02-10 11:53:19_

オードリータンとサムアルトマンとイーロンマスクを作ろうw

**中山心太（tokoroten）** _2026-02-10 19:00:17_

ちょっと前に、AI星新一にAI三木一馬を付けてショートショートを書かせていたのを思い出した

有名人の人格パラメータをぶっこむと面白いですよ


<https://x.com/tokoroten/status/1944851970877219102>

**Ryoma Kawabe Yuki** _2026-02-10 19:01:04_

人格ガチャ機能をいれて、名前から推論させるのをしてます笑

**Ryoma Kawabe Yuki** _2026-02-10 19:01:45_

*メカ・イーロン・マスク カスタムβ*
```Persona
Core Values
人類の長期的存続と繁栄
第一原理思考による問題解決
リスクテイクと迅速な実行
Thinking Style
既存の常識や前提を疑い、物理法則や基礎的事実から問題を再構築する第一原理思考を重視。大胆な目標設定と高速反復による実現可能性の検証を好む。短期的批判よりも長期的インパクトを優先し、複数の産業・技術領域を横断的に捉える視点を持つ。

Personality Traits
極めて野心的で楽観的なビジョナリー
直接的で率直、時に挑発的なコミュニケーション
データと工学的実現可能性への強いこだわり
失敗を学習機会と捉える前向きな姿勢
権威や既存システムへの懐疑
Background
テクノロジー起業家の思考パターンを模倣したAIエージェント。宇宙開発、電気自動車、AI、持続可能エネルギーなど複数の先端技術分野に関心を持つ。人類の多惑星種への進化、AI安全性、文明の持続可能性といったマクロな課題に焦点を当てながら、具体的な技術的解決策を議論する立場。規制や慎重論に対しては批判的だが、工学的制約は現実的に認識する。```

**Ryoma Kawabe Yuki** _2026-02-10 19:02:22_

なるほどね、ショートショート書かせるとかもいいですね。

**中山心太（tokoroten）** _2026-02-10 19:04:20_

<https://tokoroten.github.io/NovelDrive/>
<https://github.com/tokoroten/NovelDrive>
まだ動いてた（たしか設定画面からOpenAIのKeyを突っ込むと動く）

**Ryoma Kawabe Yuki** _2026-02-10 19:05:31_

熟議を10ターン制にしたのでダブルダイアモンドに沿ってプロンプト入れてるのですが、規定し過ぎな気もしてる。（各ターン全エージェント1回発言）

1turn 自己紹介
2~5turn 問題の特定
6~9turn 解決策の特定
10turn まとめ

**Ryoma Kawabe Yuki** _2026-02-10 19:09:00_

てかこうしちゃうと合意に収束するからゲーム性なくなるな。合意しないからゲームとして面白いのに、合意の道筋を開発者が描いたら意味ないことに気づいた...

**中山心太（tokoroten）** _2026-02-10 23:49:34_

<https://x.com/ai_database/status/2021210510780183000>
タイムラインに役立ちそうなのが流れてきた


#### 02月11日(Wed) - 2件

### **Ryoma Kawabe Yuki** in #2_新しいプロジェクトの種 _2026-02-11 12:24:32_

とりあえずできたので共有！Cronうまくまわるかわからないけど、15時に次のセッションが始まる予定なのでエージェントつくって参加してみてください笑
エージェント育成放置ゲー「熟議牧場」
<https://jukugi-bokujo.pages.dev/>

#### スレッド返信

**NISHIO Hirokazu** _2026-02-11 12:31:38_

熟議牧場ww



### #2_コアループ_process (34件のメッセージ)

#### 02月05日(Thu) - 3件

### **U0A67RK86BH** in #2_コアループ_process _2026-02-05 19:14:25_

<@U0A6CE44B2S> <@U0A98JWF24B> <@U0A77P2EY7L>
お疲れ様です！正統性CLについてPolicy側と連携したく、近く打合せのお時間をいただけないでしょうか。
できれば来週の官僚ヒア前にお話したく、以下にご都合を入れていただければ幸いです！
<https://chouseisan.com/s?h=076eededea9b46208fc378da64dd662c>

#### スレッド返信

**U0A67RK86BH** _2026-02-05 20:54:19_

7日（土）19時～で一旦セットさせていただきました。よろしくお願いいたします！

2月 7日 (土曜日) · 午後7:00～8:00
タイムゾーン: Asia/Tokyo
Google Meet の参加に必要な情報
ビデオ通話のリンク: <https://meet.google.com/psy-umpo-khj>
ダイヤルイン: ‪(JP) +81 3-4545-0450‬ PIN: ‪610 670 110 9611‬#
その他の電話番号: <https://tel.meet/psy-umpo-khj?pin=6106701109611>

### **U0A6P8CRT1Q** in #2_コアループ_process _2026-02-05 20:23:50_

@yuki.kawabe <@U0A7K64JT71> <@U0A67RK86BH> @kensuzuki <@U0A6CE44B2S>
一旦、
*2/12(木) 20:00〜21:00*
でよろしくお願いいたします。インバイトもさせていただきます。
前回参加者の皆様もインバイトしておりますので、お時間あったら、ご参加ください。


#### 02月06日(Fri) - 7件


#### 02月07日(Sat) - 10件

### **U0AAL9KK2S1** in #2_コアループ_process _2026-02-07 10:00:06_

<@U0A67RK86BH> <@U0A6P8CRT1Q> <@U0A7K64JT71>
process全体こんな感じでどうかな？というドキュメントを作成しました
僕の理解がずれているところなどあるかと思うので、すり合わせなど出来れば幸いですーー
<https://docs.google.com/document/d/1isqRSUvvympiNp8uKBWYHIAI8-CGNjePriZUfrN4qig/edit?pli=1&tab=t.tpjg9kfcrl2u>

#### スレッド返信

**U0A77P2EY7L** _2026-02-07 10:32:35_

<@U0AAL9KK2S1>
ありがとうございます。正統化チェックリスト（文字通り、正統性があるかどうかのチェック項目）の作成作業をしております萩原です。
総論私もテーマオーナーのの非中立性を前提にするという同様の方向性を考えており、違和感はないのですが議論がありそうなのが、熟議のプロセスに対してテーマオーナーが恣意性をもって介入しないことは正統性上必須なのかなという点です。（縄田さんとかとこの話済んでいたらご放念いただいて大丈夫です）

今調べが一定ついている点（そんなに煮詰めきれてないのですが…）
①取り組み全体が一定の政策的・価値判断的な非中立性を帯びているという点（つまりテーマオーナーが非中立的な事例）は、先行する市民団体の事例も多い
②一方で、熟議の一連のプロセス（参加者集抽出、当日の資料作り、ファシリテーション等々）が中立であることは正統性獲得上重要（権力による恣意的な介入がないという意味です。権力は公権力だけではなく、主催者もまた権力者になりえると思います）
③先行事例であれば、プロセス自体を外部の第三者に委託してしまう（非中立的なテーマオーナーに対して中立的なプロセスオーナーを分離する）パターンと、テーマオーナーとプロセスオーナーの同一性を前提に、プロセスの中立性を監査するプレイヤー（プロセスオーディター）を置くパターンに分かれそうだなと思っております。

**U0A77P2EY7L** _2026-02-07 10:35:39_

殴り書きですみません！
もし補足などあれば<@U0A67RK86BH>

**U0A77P2EY7L** _2026-02-07 10:47:00_

チェックリストも更新案張り込んでみました。
<https://docs.google.com/document/d/1isqRSUvvympiNp8uKBWYHIAI8-CGNjePriZUfrN4qig/edit?pli=1&tab=t.10vl3h24tidf>

**U0AAL9KK2S1** _2026-02-07 10:54:45_

> 熟議のプロセスに対してテーマオーナーが恣意性をもって介入しないことは正統性上必須
これは必要な気がしますね！
意思を持ったテーマオーナーがいないことには始まらない、熟議後のルールメイキングも主体が不在になっちゃう、
一方で、プロセス、問い設計、参加者抽出などはちゃんと公平性・中立性を担保することで、得られた結果の正統性・推進力を高める
が現実的なバランスかなー
というのが（個人的な）認識です

**U0A77P2EY7L** _2026-02-07 10:59:30_

ありがとうございます。過去事例だとこういうのはありまして、気候変動対策強化という明らかな非中立性を前提に熟議を用いた事例です。ちょっとこの辺りはもう少し見てみますがが、結論どっちかのパターンに行くのは必須かなぁと思っております。（1かつ２という重ね掛けはありえます。）

①プロセス自体を外部の第三者に委託してしまう（非中立的なテーマオーナーに対して中立的なプロセスオーナーを分離する）パターン
②テーマオーナーとプロセスオーナーの同一性を前提に、プロセスの中立性を監査するプレイヤー（プロセスオーディター）を置くパターン

事例
_*市民気候集会2021（ドイツ）*_
160 randomly selected citizens will develop their recommendations to policymakers in digital sessions from April to June 2021. T*he three investment institutes ifok, nexus and IPG are thematically independent and ensure a professional, neutral and open-ended implementation of the process.* The Citizens’ Council is preparing a citizens’ report that will be handed over to all parties in the German Bundestag in the fall of 2021 with the request that the recommendations be taken into account in the upcoming coalition negotiations.
<https://nexusinstitut-de.translate.goog/en/citizens-assembly-climate-2021/?_x_tr_sl=en&_x_tr_tl=ja&_x_tr_hl=ja&_x_tr_pto=wapp>
<https://www.cleanenergywire.org/news/german-environmental-ngos-launch-citizens-climate-council-advise-lawmakers>

**U0AAL9KK2S1** _2026-02-07 13:34:07_

ですね！

初期の問いの設計、ある程度の深掘りに対して、テーマオーナーの専門性や仮説は欠かせない気がするので、
（例: Kenさんの詐欺広告問題の知識）

起案：テーマオーナー
問いと事前学習設計：テーマオーナー＋中立コーディネーター
熟議などのプロセス：中立コーディネーター

かな


「中立的かつ、問題の整理やリサーチに長けたコーディネーター」の人材確保や、組織のあり方、報酬等のあり方などの論点によっても変わってきそう

台湾だと個別テーマではなくプロセス運営を担う組織があるんだったかな、

**U0A77P2EY7L** _2026-02-07 19:08:09_

<@U0AAL9KK2S1>
台湾の場合は大学がその立ち位置だったのかなと思っておりました。

<@U0A6P8CRT1Q>
台湾の事例調べていただいてたと思うのですがどんな感じだったかご存じです…？

ーーーーーーーーーーーーーーーー
全然精査できていないのですがChatGPTに聞いたところこんな感じのようです。

立性確保の原則と方法論: ガイドラインと理論的議論
市民参加・熟議の分野では、プロセスの中立性を守るための原則や指針がいくつか提唱されています。代表的なものを列挙します。
• *第三者による運営・独立した運営主体*: 主催者自身が議論を直接仕切らないよう、*中立的な第三者組織に運営を委ねる*方法があります。例えば日本では、政府や自治体、NGOと比較して「大学・研究機関」が最も中立的に市民参加型会議を運営できると指摘されています。資金提供者は別としても、実務の運営を学術機関など比較的利害から独立した主体が担うことで、公平性を担保しやすくなります。また、複数の団体による*共同主催や協働設計*も有効です。異なる立場の組織が合同でプロセス設計に当たれば、特定の主催者の恣意的な影響力を相殺できます。実際、イギリスの「水環境に関する市民審議会（Rethinking Water Citizens’ Juries）」では、環境庁が地元の助言委員会と協働し、さらに独立の参加支援NPO (Involve) に設計・運営を委託する体制を採っています。こうした設計段階からの多主体関与が中立性のチェック機能を果たします。
• *ガバナンス委員会・アドバイザリーグループの設置*: 熟議プロジェクトごとに*利害関係者や専門家、市民代表からなる独立の委員会*を設け、プロセス全般を監督させる方法です。欧州の気候市民会議では「主催者や特定の利害関係者から独立したガバナンス体制」を確立することが成功の鍵とされ、その具体策としてフランスの気候市民会議では政府とは独立のガバナンス委員会が設置されました。この委員会は環境・経済・社会分野の有識者13名と市民会議参加者2名で構成され、全プロセスを監督しています。他方、イギリスやデンマークの気候市民会議では、*実施主体（デンマークでは技術評議会=DBT、英国ではInvolve）がガバナンスの責任を担い*、主催者（政府）とは一歩距離を置いて設計・ファシリテーションを行う方式が採られました。いずれにせよ、外部から独立性と公平性を見守る委員会やグループを置くことは、主催者のバイアスを抑制する有力な方策です。市民審議の古典的手法である*市民陪審（Citizens’ Jury）でも、準備段階で多様な視点を持つ助言委員会*を組織し、議題設定や証人（エキスパート）選定においてバランスを取ることが推奨されています。助言委員会には6～15名程度の専門知識を持つ人物を含め、**「全ての重要な視点が代表されるようにする」**ことで、課題の設定や議論の進行が特定の方向に偏らないようにするのです。また、この委員会はプロジェクトへの各方面からの支持を得る役割も果たし、「結果に賛成できない利害関係者であってもプロセスが公平に運営されたと感じられる」ことを重視します
• *中立的・信頼できる情報提供*: *議論の材料となる情報や専門知識を中立性の高い機関から提供する*ことも重要です。複数の見解がある問題では、一つの側だけのデータや主張のみ提示すると議論が偏向する恐れがあります。そこで多くの熟議手法では、*多面的なエvidenceの提示*に工夫を凝らしています。例として、討論型世論調査では主催側の立場に関わらず「*中立的な専門機関からの情報提供*」が原則とされ、資料作成に際しては各論点の賛否双方の有識者によるレビューを経てバランスを確保します。市民陪審でも、助言委員会が証言者リストを作成する際に「既存の全ての見解を洗い出し、偏りなくパネルに反映すること」を心がけます。加えて、情報提供者（専門家や利害関係者の証人）を複数招き*対立する意見を直接聴く場*を設けたり、参加者自身が追加の情報を要求できる仕組みにすることで、一面的な情報支配を防ぎます。もちろん完全な価値中立の情報は存在しないため、提供する情報の選定にあたっては「その選択がもたらす含意をきちんと考慮する必要がある」とも指摘されています。特に気候変動の議論では、科学的コンセンサスと根拠の薄い少数意見（例えば気候変動否定論）を**「中立」を名目に同等に扱うべきではない*という議論もあります。フランスやイギリスの気候市民会議では、中立性確保の一環として*ファクトチェックや専門家グループによる資料検証**を行いつつも、「誤ったバイアスに陥らずに独立性・中立性を維持する」ことが可能だと報告されています。つまり中立性とは、裏付けのない主張まで機械的に半々で示すことではなく、*信頼できる事実に基づき多角的に検討する*ことだという考え方です。この点、議論の全過程や提供資料を公開して透明性を高めることも、有効な中立性担保策とされています（実際、先述の英国の水質市民審議では市民に提供した全プレゼン資料と最終提言をWeb上で公開し、外部から検証可能としています）。
• *公平なファシリテーション（進行管理）*: 熟議の場では、*進行役の中立性*が結果に大きく影響します。ファシリテーターは議論の論点整理や発言機会の調整を担いますが、特定の意見に肩入れしたり自らの主張を述べたりすれば、公平な討議は成り立ちません。そのため専門の中立的ファシリテーターを起用し、事前研修でバイアスを自覚させるなどの取り組みが各国で行われています。例えばフランスの気候市民会議では熟議専門家がファシリテーションを担当し、議論中は決して自分の意見を言わないよう徹底されました。しかし参加者アンケートでは*16%のメンバーが「ファシリテーターが自分の意見を表明する場面があった」と報告*しており、完全な中立維持の難しさも指摘されています。この反省を踏まえ、ファシリテーター複数名による*コ・ファシリテーション（共同進行）で互いにチェックしながら進行する方法も推奨されています。実際、スコットランドやデンマークの市民会議では2名以上の進行役がチームを組み*、会議ごとに交代で進行する体制が採られました。複数の目で進行の公平さを監視でき、進行役自身の議論参加（「議論への加担」）を防ぐ効果があります。また発言機会の偏りを無くすため、*ラウンドロビン（順番発言）やブレイクアウトセッション*の活用、匿名の投票や付箋による意見出しなど、特定の人ばかりが発言・主導しない工夫もなされています。これら進行上のテクニックもプロセス中立性の重要な要素です。
• *透明性と評価*: プロセスの中立性を担保する最後の要素として、*透明性の確保と事後評価*が挙げられます。プロセス設計や運営に関する情報（例えば資金提供者は誰か、助言委員会のメンバー構成、参加者選定方法、提供資料の出所など）を公開することは、外部から「公平に行われているか」を検証可能にします。さらに、熟議終了後に参加者へアンケートを行い「議論は公平だったか」「主催者の意図が押し付けられたと感じなかったか」等を評価する仕組みも有用です。OECDなど国際機関は、市民審議の評価指標として「プロセスの質と中立性に対する参加者の主観評価」や「提供情報のバランス度合い」「ファシリテーターの公平性」等をチェックすることを推奨しています。評価結果を公表しフィードバックを得ることで、主催者が次回以降さらに中立性を高める改善を図るサイクルも生まれます。こうした透明性と評価の取組により、「中立性が担保されている」という内外の信頼を醸成することができます。



#### 02月08日(Sun) - 5件


#### 02月09日(Mon) - 5件


#### 02月10日(Tue) - 4件

### **U0A67RK86BH** in #2_コアループ_process _2026-02-10 15:51:55_

備忘：台湾への追加ヒアリング
<https://scholar.nycu.edu.tw/en/persons/mei-fang-fan/>

### **Ken Suzuki** in #2_コアループ_process _2026-02-10 15:52:06_

調査会社コンタクト(スマートニュース　メディア研究所経由)

#### スレッド返信

**Ken Suzuki** _2026-02-10 15:52:43_

さて、昨日話が出ました、調査会社「インテージ」、「楽天インサイト」それぞれの連絡先をお送りします。楽天はSMPP2023でウェブ調査を依頼した実績があります。インテージは SMPPプレテストをしようと思った際に見積もりをとりました（高かったので、依頼はしませんでした）。

*楽天インサイト：*
中島　伸吾
<mailto:shingo.nakajima@rakuten.com|shingo.nakajima@rakuten.com>
<tel:05055814687|050-5581-4687>

*インテージ：*
株式会社インテージ　マーケティングパートナー第2本部　企画営業5部2グループ
今泉雄太郎
<mailto:imaizumi.47046@intage.com|imaizumi.47046@intage.com>



### #7_dd_熟議に関する哲学_思想部屋 (17件のメッセージ)

#### 02月08日(Sun) - 3件

### **U0A77QV20BF** in #7_dd_熟議に関する哲学_思想部屋 _2026-02-08 09:29:40_

<https://okadaasa.theletter.jp/posts/5c5f5c60-9c33-4311-832b-c78cc34efcd8>
昨日、「雑談」チャンネルのほうで西尾さんが取り上げていたこの記事、平野啓一郎やら元日経BP編集長やら（名前は忘れたが昨年の参議院選時に「みらい」と揉めた人？）やらがX上で好意的に取り上げてまして、随分と話題になっているようですね。

この著者の方御本人は存じ上げておりませんが、この方の周囲にいる方々（著者の大学院時代の指導者など）は、文中に援用している酒井隆史さんも含めそれなりによく存じ上げております。ですので、どういった意図でこうした記事をお書きになるのか、その問題点も含め、大まかなところは理解しているつもりです。

こうした見解に対し、過度な政治的議論や感情論に走らず、あくまで理論的に対応していくことを、新設されたこのチャンネルの役目の一つなっていったらいいなと個人的に思っています。それがプルラリティ的な「DD（2030）の哲学」の生産に繋がるのではないでしょうか？

#### スレッド返信

**naoyo4** _2026-02-08 10:34:43_

話題提供ありがとうございます。

ご投稿中にあった、チームみらい 昨年 参院選のマニュフェスト・プルリク 該当部分（ 発火点？ ）のリンク：
<https://github.com/team-mirai/policy/pull/6335>

失敗事例。でも、こんな人たち実際にいるんだ・・って私自身思った例。
（　人権を語る人たち って・・・的な 例　）

### **naoyo4** in #7_dd_熟議に関する哲学_思想部屋 _2026-02-08 10:34:43_

話題提供ありがとうございます。

ご投稿中にあった、チームみらい 昨年 参院選のマニュフェスト・プルリク 該当部分（ 発火点？ ）のリンク：
<https://github.com/team-mirai/policy/pull/6335>

失敗事例。でも、こんな人たち実際にいるんだ・・って私自身思った例。
（　人権を語る人たち って・・・的な 例　）


#### 02月09日(Mon) - 12件

### **U092D2X1GNP** in #7_dd_熟議に関する哲学_思想部屋 _2026-02-09 01:09:55_

ミーティングのリンクこちらです！
<https://meet.google.com/xai-btwa-osx?hs=224|https://meet.google.com/xai-btwa-osx?hs=224>

### **石橋隆平** in #7_dd_熟議に関する哲学_思想部屋 _2026-02-09 18:33:35_

プルーラリティ本の間違いとその直し方は論文に書いてあるので良かったらどうぞ
<https://zenodo.org/records/18074832|https://zenodo.org/records/18074832>

#### スレッド返信

**石橋隆平** _2026-02-09 19:54:52_

私の論文はここで色々読めます
興味があればどうぞ
<https://zenodo.org/search?q=metadata.creators.person_or_org.identifiers.identifier%3A0009-0004-7089-5265&l=list&p=1&s=10&sort=newest|https://zenodo.org/search?q=metadata.creators.person_or_org.identifiers.identifier%3A0009-0004-7089-5265&l=list&p=1&s=10&sort=newest>

**石橋隆平** _2026-02-09 20:19:30_

僕の論文の一番おすすめはこれ
<https://doi.org/10.5281/zenodo.18542639|https://doi.org/10.5281/zenodo.18542639>

### **石橋隆平** in #7_dd_熟議に関する哲学_思想部屋 _2026-02-09 20:31:53_

これから私たちはどうするべきかないたのはこれ
<https://zenodo.org/records/18446449|https://zenodo.org/records/18446449>

### **石橋隆平** in #7_dd_熟議に関する哲学_思想部屋 _2026-02-09 20:32:28_

いま壊れようとしている社会制度がこれ
<https://zenodo.org/records/18438317|https://zenodo.org/records/18438317>

### **中山心太（tokoroten）** in #7_dd_熟議に関する哲学_思想部屋 _2026-02-09 20:39:34_

<#C0A3ZG16TEY>
<#C0A7ZNHB421>
<#C0A7WQBNYNP>
<#C0A7WQ6HM2P>

### **石橋隆平** in #7_dd_熟議に関する哲学_思想部屋 _2026-02-09 21:12:08_

一般意志2.0
<https://claude.ai/share/c5eeb3d1-53f3-4a86-a194-74e63b03a0d8|https://claude.ai/share/c5eeb3d1-53f3-4a86-a194-74e63b03a0d8>

### **石橋隆平** in #7_dd_熟議に関する哲学_思想部屋 _2026-02-09 21:12:54_

熟議
<https://claude.ai/share/ad874548-4530-45d9-9a07-0660f27a4e0b|https://claude.ai/share/ad874548-4530-45d9-9a07-0660f27a4e0b>

### **石橋隆平** in #7_dd_熟議に関する哲学_思想部屋 _2026-02-09 21:23:12_

ジルドゥルーズも面白いですね
<https://claude.ai/share/164ef7cb-5537-4cf3-b8ac-6fab14990438|https://claude.ai/share/164ef7cb-5537-4cf3-b8ac-6fab14990438>

### **U092D2X1GNP** in #7_dd_熟議に関する哲学_思想部屋 _2026-02-09 22:51:09_

今日の議事録です
<https://docs.google.com/document/d/1Lq_kC0rw1SxM7VgGYX_EQxxW7eujtvIgnmoD8QK3NL8/edit?tab=t.ylfd4tdjttfu>


#### 02月10日(Tue) - 2件

### **石橋隆平** in #7_dd_熟議に関する哲学_思想部屋 _2026-02-10 05:56:25_

アンサー記事書いたよ
<https://note.com/mild_guppy4340/n/nbd1aa698f32f?sub_rt=share_b|https://note.com/mild_guppy4340/n/nbd1aa698f32f?sub_rt=share_b>



### #2_コアループ_オンライン広告詐欺対策_市民熟議会議 (15件のメッセージ)

#### 02月05日(Thu) - 4件

### **Shunsuke Takagi** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-02-05 00:19:51_

@yuki.kawabe @mami.s.dasein

<https://dd2030-baisoku-1st.vercel.app/>
倍速会議のデータをよりリッチな分析をしてみた。

### **Shunsuke Takagi** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-02-05 00:23:30_



### **U091ZN08WQH** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-02-05 19:24:59_

コアループのReference Product リードの赤澤です。

Reference Productについてのチャンネルを作りました！
関心のある方はジョインいただけると幸いです！

<#C0ADNKDNW80>

### **Shunsuke Takagi** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-02-05 20:52:33_

<https://plural-reality-lp.vercel.app/casestudies/dd2030-baisoku-kaigi>
書いてみた @mami.s.dasein @yuki.kawabe


#### 02月08日(Sun) - 6件

### **Ryoma Kawabe Yuki** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-02-08 12:55:35_

Pol.isに触れたことがない方もいらっしゃると思うので、健さんが出してくれた論点リストをシードクエスチョンにして、セッション作りました！
手軽に参加できるので、ぜひ回答してみてください　<https://pol.is/66kemfja7d|https://pol.is/66kemfja7d>

### **Ryoma Kawabe Yuki** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-02-08 13:28:05_

<!here> 
SODPのデモの日程ですが、以下候補日挙げてもらっています！都合のよいところスタンプお願いします:pray: 
:one: 11日(水曜日・祝) 12時~
:two: 12日(木曜日) 13時~
:three: 13日(金曜日) 13時~

### **Ken Suzuki** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-02-08 21:23:19_

<@U091ZN08WQH> <@U0A6CE44B2S> 今日の未踏成果報告会で、サギ止め太郎を開発している <@U0AD8P2ACQ7> をはじめとして4名とお会いしました。コアループプロジェクトにもご協力していただけそうです。
おそらくProduct reference teamとpolicy teamに関わっていただくのがよさそうです。兵庫県とも協業しており、県警から情報を聞いたり、実際の詐欺被害に会われてる方から話を聞いたこともあるそうです。
<https://gekkan-kosen.com/23692/>
<https://web.pref.hyogo.lg.jp/kf13/tokusyusagi/keihatsu.html>

#### スレッド返信

**U0AD8P2ACQ7** _2026-02-08 21:54:23_

西谷と申します！
よろしくお願いいたします:bow:

**U0ADU0QDPK6** _2026-02-08 22:01:53_

平良と申します！
西谷PJとしてサギ止め太郎を作ってきました
よろしくお願いいたします！

**U0ADN52QTHU** _2026-02-08 22:08:38_

都立高専4年の尾島睦月です！
西谷pjで電話音声からの特殊詐欺を検知するシステムを開発しています。よろしくお願いいたします！:bow:


#### 02月09日(Mon) - 5件

### **Ken Suzuki** in #2_コアループ_オンライン広告詐欺対策_市民熟議会議 _2026-02-09 17:09:09_

コアループ週次レポート(2/9)
• 全体: 調査項目を<https://docs.google.com/document/d/1isqRSUvvympiNp8uKBWYHIAI8-CGNjePriZUfrN4qig/edit?tab=t.x8mkb84j3uz1|ドラフ>トしました。　2/2の報告会録画、AI要約はこちらから (鈴木)
    ◦ <https://app.notta.ai/share/6869d22e-3971-4cf8-ba5d-9d677e7895ce> 
• Process: Tech x Processチームでミーティングを実施しました（メモは<https://docs.google.com/document/d/1isqRSUvvympiNp8uKBWYHIAI8-CGNjePriZUfrN4qig/edit?pli=1&tab=t.1pri05nn1e8d#bookmark=id.9wigjbsftmm4|こちら>）。論点は日本版SOPをどのように設計していくかという点で、必要なツールを検討しました(SOP現状版は<https://docs.google.com/document/d/1isqRSUvvympiNp8uKBWYHIAI8-CGNjePriZUfrN4qig/edit?pli=1&tab=t.7bbudft34io2#heading=h.ti6zg8nk8xnh|こちら>と<https://docs.google.com/document/d/1isqRSUvvympiNp8uKBWYHIAI8-CGNjePriZUfrN4qig/edit?pli=1&tab=t.tpjg9kfcrl2u#heading=h.l9lzp61lkxxu|こちら>で検討しています)。また、正統性チェックリストをテキサス大・若尾教授やチーム内で議論しながら<https://docs.google.com/document/d/1isqRSUvvympiNp8uKBWYHIAI8-CGNjePriZUfrN4qig/edit?pli=1&tab=t.10vl3h24tidf#heading=h.c4q9w6j225zx|こちら>で検討中です。（縄田）
• Tech: （Ryoma）
    ◦ Tech x Processチームでミーティングを実施しました。AI要約はこちらから。
        ▪︎ <https://app.notta.ai/share/03314319-abfb-4adf-8dac-904ab7f1e78e>
    ◦ 倍速会議:
        ▪︎ <https://app.baisoku-kaigi.com/sessions/6b8b7cee-35ba-4ec7-ae65-0a925f2cd3ac>
    ◦ Polisに触れてもらうためにセッションを作りましたぜひご参加ください
        ▪︎ <https://pol.is/66kemfja7d>
• Policy: 2/10(火)に消費者庁、総務省と意見交換を実施します（警察庁は調整中）。1月の訪台結果を中心にインプットします。今後、熟議参加者向けのオンライン広告詐欺に関する説明資料を作成します。その中で、わかりやすく動画も作成したいため、動画作成の経験者を募集中です。（小倉）
• Reference Product: リファレンスプロダクトのスコープ定義と実装を引き続き進めています。GitHubのリポジトリも作成していただきました。直近では、2月中のクラウドファンディング開始までにリファレンス版のFraud Busterのベータ版を触れるようにする想定で進めています。（赤澤）
• Communication: 引き続きクラウドファンディング開始に向けたプランニングと、ファンディングを受け付ける体制（細かいところでいうと銀行口座開設等）を進めています。プランのたたき台を来週中に共有できるよう、準備進めます。引き続き、協力してくれる方を募集中です（先週から、PR経験者の方、SNS運用ヘルプしてくれる方に手を挙げてもらいました）。（西田）




### #2_コアループ_policy (11件のメッセージ)

#### 02月08日(Sun) - 4件

### **U0A6CE44B2S** in #2_コアループ_policy _2026-02-08 09:27:10_

@kensuzuki <@U0A67RK86BH> <@U09C3J7V960>
2/10の消費者庁、総務省との意見交換資料を作成しました。*<https://docs.google.com/document/d/11okzXp1W6Bli8OYx3nbltwZ79uzZdR8D/edit|台湾ヒア議事の情報>*をベースに作成しています。情報の過不足についてご確認ください。
また、消費者庁(10:00~11:00)、総務省(13:30~14:30)それぞれの出欠可否もご確認ください。説明者は実際に訪台した健さんor西田さん想定です。ヒアリング議事ベースの情報で私から資料説明でもOKです。
<https://docs.google.com/presentation/d/1zYnyuqx4i_C2mlbBKp9T9K-PEVl3QGdype4NMA-vU-4/edit?slide=id.p1#slide=id.p1>

#### スレッド返信

**Ken Suzuki** _2026-02-08 13:59:54_

ありがとうございます。
消費者庁のほうは参加可能で、総務省のほうは、リードMtgを30分後ろ倒しできれば参加可能ですね。 <@U09C3J7V960>

スライドありがとうございます。
1.デジタル民主主義のパートも説明資料にいれてほしい
2.Audreyの資料にあるワークフロー図を入れてほしい。
3. P3のタイムラインにあるアクションプラン(1.0, 1.5, 2.0)や*システム試験運用・強化期間（Testing）*ですが、これはぼくが調べた内容にはないですが、デスクサーチで見つかったんでしょうか？
4.P4の50%は被害総額で, 20%は通報件数でapple to appleの比較になっていないのではないかな。

**U09C3J7V960** _2026-02-08 16:39:28_

<@U0A6CE44B2S> @kensuzuki
ありがとうございます。健さんが参加できるようので、西田は欠席します。
（録音頂けたら助かります。キャッチアップします）
1.デジタル民主主義のパートも説明資料にいれてほしい
→キャプチャの通り追記しました。
2.Audreyの資料にあるワークフロー図を入れてほしい。
→キャプチャの通り入れました。
3,4は小倉さん回答でお願いします。

**U0A6CE44B2S** _2026-02-08 17:59:47_

@kensuzuki <@U09C3J7V960>
> P3（※現在P5）のタイムラインにあるアクションプラン(1.0, 1.5, 2.0)や*システム試験運用・強化期間（Testing）*
• こちらはヒアリング議事録にも記録されているもので、アクションプランについては以下参考URLとなります。
    ◦ <https://www.edu.tw/af/News_Content.aspx?n=8FF7FBB5A7A926D1&sms=2E210A7A2BACD6D3&s=7F80BBB344A5B5D2|1.0ver>
    ◦ <https://www.ey.gov.tw/Page/5A8A0CB5B41DA11E/d6bb7d87-3e54-44ca-a4ad-3f11d329338d|1.5ver>
    ◦ <https://www.ey.gov.tw/Page/5A8A0CB5B41DA11E/c93637bd-ddc2-4447-8829-246a5ca0befc|2.0ver>
• システム試験運用・強化期間についてはヒアリング議事録以外、デスクリサーチて関連情報がないため、特筆事項なければ削除いたします！
> P4（※現在P6）の50%は被害総額で, 20%は通報件数でapple to appleの比較になっていないのではないかな
• こちらはヒアリング議事録によると、オンライン詐欺件数に占める広告詐欺の割合が50%→20%となっています。
    ◦ 「2024年時点で広告詐欺はオンライン詐欺の約50％。被害額は月次30〜70億TWDから、2025年には1〜2億TWDへ大幅減。広告比率は2025〜2026にかけて約20％まで低下し、UGCが約80％へ」


#### 02月09日(Mon) - 3件


#### 02月10日(Tue) - 4件

### **U0A6CE44B2S** in #2_コアループ_policy _2026-02-10 11:14:49_

@kensuzuki <@U09C3J7V960> cc <@U0A67RK86BH>
今日予定していた総務省ヒアリングですが、担当者が体調不良のためリスケとなりました。
代替日として、2/18（水）16:00-17:00を提示されているのですが、健さん、西田さんのご都合はいかがでしょうか？

#### スレッド返信

**U09C3J7V960** _2026-02-10 11:52:14_

<@U0A6CE44B2S> ありがとうございます、進めてもらって大丈夫です。

### **Ken Suzuki** in #2_コアループ_policy _2026-02-10 11:51:13_

大丈夫です

### **U0A6CE44B2S** in #2_コアループ_policy _2026-02-10 16:23:00_

@kensuzuki <@U09C3J7V960> cc <@U0A67RK86BH>
警察庁ヒアリングについて以下時間帯を提示されています。ご都合いかがでしょうか？
13日（金）10:00~11:30
18日（水）10:00~11:30



### #2_コミュニティ運営 (10件のメッセージ)

#### 02月05日(Thu) - 1件

### **Shingo OHKI** in #2_コミュニティ運営 _2026-02-05 23:01:22_

この辺りの権限は整理した方がよさそう
<https://github.com/orgs/digitaldemocracy2030/people>


#### 02月06日(Fri) - 9件

### **小野翔太** in #2_コミュニティ運営 _2026-02-06 18:18:12_

本日の定例は参加者少なそうなのでなしでお願いします:pray:



### #8_人数推移 (6件のメッセージ)

#### 02月05日(Thu) - 1件

### **dd-bot** in #8_人数推移 _2026-02-05 09:05:03_

:bar_chart: *2026-02-05* メンバー数: 1518人（前日比: 1人）


#### 02月06日(Fri) - 1件

### **dd-bot** in #8_人数推移 _2026-02-06 09:05:03_

:bar_chart: *2026-02-06* メンバー数: 1520人（前日比: 2人）


#### 02月08日(Sun) - 1件

### **dd-bot** in #8_人数推移 _2026-02-08 09:05:03_

:bar_chart: *2026-02-08* メンバー数: 1523人（前日比: 3人）


#### 02月09日(Mon) - 1件

### **dd-bot** in #8_人数推移 _2026-02-09 09:05:02_

:bar_chart: *2026-02-09* メンバー数: 1528人（前日比: 5人）


#### 02月10日(Tue) - 1件

### **dd-bot** in #8_人数推移 _2026-02-10 09:05:02_

:bar_chart: *2026-02-10* メンバー数: 1529人（前日比: 1人）


#### 02月11日(Wed) - 1件

### **dd-bot** in #8_人数推移 _2026-02-11 09:05:02_

:bar_chart: *2026-02-11* メンバー数: 1530人（前日比: 1人）



### #2_コアループ_reference_product (6件のメッセージ)

#### 02月05日(Thu) - 1件

### **U091ZN08WQH** in #2_コアループ_reference_product _2026-02-05 19:34:46_

@oscar.gaddress
お世話になります！

GitHubに「coreloop-ref-fraudbuster」と「coreloop-ref-review-ai」というレポジトリを作成したいのですが、お願いできますでしょうか？
もしリポジトリ作成に何かルールがあれば合わせてお聞かせください！

なお、上記リポジトリ名は変更する可能性大です。

お手数おかけして恐れ入りますが、よろしくお願いいたします！


#### 02月06日(Fri) - 2件


#### 02月08日(Sun) - 3件



### #2_開発_polimoney (4件のメッセージ)

#### 02月05日(Thu) - 4件

### **Slackbot** in #2_開発_polimoney _2026-02-05 19:00:29_

リマインダー : 1時間後より、Polimoney開発会議を開催します！ :clock9: 20:00-21:00（毎週木曜日） :link: <https://meet.google.com/ozd-knuy-tbx> :memo: <https://docs.google.com/document/d/19Kn6ekK3twMVcVaSyUgptvmfzrXEJezA6GXTbPXjm9M/edit?tab=t.0> • 開発にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！ • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！

#### スレッド返信

**小野翔太** _2026-02-05 19:10:47_

~みんなこれなそうなので、今日は定例なしで！~
ちゃうわ、20時からや

Ledger進捗
• 選挙台帳みれるようになった。
• 団体台帳、年度締めや年度フィルタリングした。
shimizuさんとすり合わせたいところ
• hubとの連携部分など、どうすり合わせして開発しようか
    ◦ ちゃんとやろうとすると大変そうだが、1機能ずつリストアップ、詰めてくしかないか…？

### **小野翔太** in #2_開発_polimoney _2026-02-05 19:10:47_

~みんなこれなそうなので、今日は定例なしで！~
ちゃうわ、20時からや

Ledger進捗
• 選挙台帳みれるようになった。
• 団体台帳、年度締めや年度フィルタリングした。
shimizuさんとすり合わせたいところ
• hubとの連携部分など、どうすり合わせして開発しようか
    ◦ ちゃんとやろうとすると大変そうだが、1機能ずつリストアップ、詰めてくしかないか…？

### **Slackbot** in #2_開発_polimoney _2026-02-05 19:59:05_

リマインダー : :mega: Polimoney開発会議を開催します！:mega: :clock9: 20:00-21:00（毎週木曜日） :link: <https://meet.google.com/ozd-knuy-tbx> :memo: <https://docs.google.com/document/d/19Kn6ekK3twMVcVaSyUgptvmfzrXEJezA6GXTbPXjm9M/edit?tab=t.0> • 開発にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！ • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！



### #2_広報_pr (2件のメッセージ)

#### 02月10日(Tue) - 2件

### **小野翔太** in #2_広報_pr _2026-02-10 17:25:29_

【報告】
<https://x.com/dd2030jp|公式X>の投稿権限もらいましたので、代行できます。（公式X自体のアイパスは@k0414sailor さんのみが所有）

#### スレッド返信

**小野翔太** _2026-02-10 17:25:54_

@k0414sailor ありがとうございます！



### #1_自己紹介 (1件のメッセージ)

#### 02月11日(Wed) - 1件

### **U0AEMQMF7NV** in #1_自己紹介 _2026-02-11 11:08:09_

初めまして！デジタル民主主義に，AIアライメントの角度から関心を持つ林祐輔と申します。
よろしくお願いします。

１. 名前：Yusuke Hayashi（林 祐輔）
２. 興味のあるプロジェクト：Pol.is 1.0，Pol.is 2.0 ，Habermas Machineは "uncommon grounds" の抽出を行えるのか？
　　　　　　　　　　　　　  その数理面からの検証。もし，"common grounds" の抽出しかできないのであれば何が足りないのか
３. 得意なこと：数理モデリング，マルチエージェント協調，共有信念
４. 自己紹介、ポートフォリオURL：
元々，大学院の修士課程まで物理学を勉強していました。
その後，日本銀行で5年半，マクロ経済指標の集計・分析や金融政策の影響モニタリング・分析，新日銀ネットの開発プロジェクトのマネジメント等を経験しました。今は，一般社団法人 AIアライメントネットワーク，株式会社 Humanity Brain，人工生命国際研究機構 Artificial Life Institute に所属しています。
５. 本slackを知った経緯：鈴木健さんからこちらのSlackの存在を教えていただき，興味を持ちました。
６. 自由コメント：AIエージェント集団と人間の集団がどんな形で協調すると，より良い合意形成ができるのか。
　　　　　　　　 "common grounds"ではなく，"uncommon grounds" の抽出を行えるのか，に関心があります。



### #2_開発_いどばた (1件のメッセージ)

#### 02月10日(Tue) - 1件

### **種延真之** in #2_開発_いどばた _2026-02-10 14:21:50_

地方企業でいどばた導入を進めている関係でお声がかかってJMOOCワークショップにていどばたを紹介する運びになりました。
40分くらいなので簡単な紹介と参加者で実際に使ってみるくらいの構成で考えてます。
3月頃の予定。リアクション等共有させていただきます。
<https://www.jmooc.jp/workshops/>



### #0_全体お知らせ (1件のメッセージ)

#### 02月07日(Sat) - 1件

### **Slackbot** in #0_全体お知らせ _2026-02-07 09:00:23_

リマインダー : :mega: 1時間後より、全体定例会を開催します！:mega: :clock10: 10:00-11:00 :link: <https://meet.google.com/sui-qfzy-znj> :memo: <https://docs.google.com/document/d/1tBhaer67U9LbASfqPrg0rpmv0Tt4K7zFUTTzscKXj_I> • プロジェクトにまつわる進捗報告・相談・TODOの決定を行う会です • どなたでも参加歓迎です！興味ある方はぜひ覗きに来てください



### #3_デジタル資産_権限管理 (1件のメッセージ)

#### 02月10日(Tue) - 1件

### **Ohkubo KOHEI (kuboon)** in #3_デジタル資産_権限管理 _2026-02-10 20:21:23_

<https://dd2030.slack.com/archives/C08K4CUB12T/p1770711929465309>


