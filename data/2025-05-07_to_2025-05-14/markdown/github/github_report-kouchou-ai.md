# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-05-07T17:36:45.597823+09:00 から 2025-05-14T17:36:45.597823+09:00 まで

## Issues

### 過去7日間に完了されたissue (22件)

### [[REFACTOR] npm run lint のエラー対応](https://github.com/digitaldemocracy2030/kouchou-ai/issues/502)

**作成者:** shingo-ohki  
**作成日:** 2025-05-13T09:10:37Z  
**内容:**

# 現在の問題点
client, client-admin で npm run lint すると大量のエラーが出る

```
$ cd client-admin
$ npm run lint
...
Skipped 1 suggested fixes.
If you wish to apply the suggested (unsafe) fixes, use the command biome check --fix --unsafe

The number of diagnostics exceeds the number allowed by Biome.
Diagnostics not shown: 29.
Checked 51 files in 35ms. No fixes applied.
Found 49 errors.
check ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✖ Some errors were emitted while running checks.
```

```
$ cd client
$ npm run lint
Checked 58 files in 26ms. No fixes applied.
Found 14 errors.
check ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✖ Some errors were emitted while running checks.
```

# 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->


**コメント:** なし

---

### [[FEATURE] ScatterChartの領域をわかりやすくする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/491)

**作成者:** mtane0412  
**作成日:** 2025-05-12T14:15:02Z  
**内容:**

# 背景
- ScatterChartの範囲がスクロールで拡大できたり移動できたりする
- グリッドラインが消えたことでScatterChartの領域がわからず、下にスクロールしたら図が拡大されたりして一瞬わからなくなることがあった
  - グリッドラインがあったころから見えづらくはあった

![Image](https://github.com/user-attachments/assets/7d4541b2-1b43-473e-bc6e-27df8f19ed34)

# 提案内容
ScatterChartとそうでない領域をユーザーが見分けられるようにする

**コメント:** なし

---

### [[CLIENT][DESIGN] ScatterChartのグリッドを非表示にする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/488)

**作成者:** masatosasano2  
**作成日:** 2025-05-12T13:28:23Z  
**内容:**

# 背景

縦軸横軸に意味はないが、グリッドがあることによって意味があると感じさせかねない。

# 提案内容

グリッドを非表示にする

**コメント:** なし

---

### [[BUG]LocalLLMがOllama apiサーバーと疎通しない?](https://github.com/digitaldemocracy2030/kouchou-ai/issues/483)

**作成者:** gorira-tatsu  
**作成日:** 2025-05-12T03:31:14Z  
**内容:**

### 概要

<!-- バグの簡潔な説明をお願いします -->
LocalLLMをREADME.mdに従って設定し、環境を構築したがOllama APIサーバーとの疎通がうまくいっていない。しかしながら、curlでDockerのHost環境からアクセスしてみると、きちんと返されている。
LLMサーバーの関連するipは一通り検証済み(ollama:11434, 127.0.0.1:11434, docker networkで設定されているip?など)

```bash
curl -X POST http://127.0.0.1:11434/v1/completions \
        -H "Content-Type: application/json" \
        -d '{
          "model": "hf.co/elyza/Llama-3-ELYZA-JP-8B-GGUF",
          "prompt": "Hello, world!",
          "max_tokens": 32
        }'
{"id":"cmpl-787","object":"text_completion","created":1747016694,"model":"hf.co/elyza/Llama-3-ELYZA-JP-8B-GGUF","system_fingerprint":"fp_ollama","choices":[{"text":"Hello!","index":0,"finish_reason":"stop"}],"usage":{"prompt_tokens":26,"completion_tokens":3,"total_tokens":29}}
```

<img width="1426" alt="Image" src="https://github.com/user-attachments/assets/12c61bbe-e0fd-4b0d-b844-4ee67e2a7edb" />

### 再現手順

1. 環境変数をwith_gpu=trueに設定する
2. sudo docker compose --profile ollama up
3. 管理画面にアクセスし、詳細設定からAPIがホストされているIPを選択しモデル取得する

### 期待する動作

モデル取得でOllamaの管理しているLLMが取得できる

### その他
環境はLinux, GPUはV100 * 8枚の環境です。

**コメント:** なし

---

### [[BUG] クライアントで、プロットを最大化したときに、コマンドパレットと最大化終了が被る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/479)

**作成者:** tokoroten  
**作成日:** 2025-05-11T05:27:51Z  
**内容:**

### 概要

クライアントで、プロットを最大化したときに、コマンドパレットと最大化終了が被る

### 再現手順

クライアントでplotlyを最大化する 。

### 期待する動作

いかのいずれかが欲しい
- 最大化を終了するためのボタンを別の場所にする
- Plotlyのコマンドパレットを別の位置に表示する

### スクリーンショット・ログ

![Image](https://github.com/user-attachments/assets/735bb04d-f010-45a6-ad09-fc3e79003098)

### その他

Plotlyをドラッグやズームで動かせるようにしたときに発生したバグだと思われる

**コメント:** なし

---

### [[FEATURE] Admin管理画面から、clientの静的ページをダウンロード可能にする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/472)

**作成者:** tokoroten  
**作成日:** 2025-05-10T15:27:43Z  
**内容:**

# 背景
原状は静的ファイルを作成するのに、エンジニアリングの知識が要り、少々難易度が高い。

# 提案内容

- 管理画面に静的ファイルのダウンロード機能を付ける
- nice to have: 管理画面から、vercelや、netflyにアップロードしてホスティングする機能を付ける

**コメント:** なし

---

### [[FEATURE] CodeRabbitの導入](https://github.com/digitaldemocracy2030/kouchou-ai/issues/466)

**作成者:** mtane0412  
**作成日:** 2025-05-08T04:17:20Z  
**内容:**

# 背景
#417
CodeRabbitはOSSだと無料なのでとりあえず入れてみることになった(2025/5/7定例)


# 提案内容
CodeRabbitを導入する

**コメント:** なし

---

### [[BUG]apiのビルド時に依存関係でエラーが起きる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/462)

**作成者:** nasuka  
**作成日:** 2025-05-08T01:18:43Z  
**内容:**

### 概要
apiのbuild時に以下のエラーが起きる


 > [api 7/8] RUN if [ "production" = "development" ]; then     echo "Installing development dependencies" &&     uv pip install --no-cache --system -r requirements-dev.lock;     else     echo "Installing production dependencies" &&     uv pip install --no-cache --system -r requirements.lock;     fi:
0.106 Installing production dependencies
0.156 Using Python 3.12.10 environment at: /usr/local
1.244   × No solution found when resolving dependencies:
1.244   ╰─▶ Because only server==0.1.0 is available and server==0.1.0 depends on
1.244       openai>=1.77.0, we can conclude that all versions of server depend on
1.244       openai>=1.77.0.
1.244       And because you require openai==1.63.2 and server, we can conclude that
1.244       your requirements are unsatisfiable.
------
failed to solve: process "/bin/sh -c if [ \"$ENVIRONMENT\" = \"development\" ]; then     echo \"Installing development dependencies\" &&     uv pip install --no-cache --system -r requirements-dev.lock;     else     echo \"Installing production dependencies\" &&     uv pip install --no-cache --system -r requirements.lock;     fi" did not complete successfully: exit code: 1
make: *** [up] Error 17

### 再現手順
`make build` を実施

### 期待する動作

エラーが起きず正常にビルドできること


**コメント:** なし

---

### [テスト起票](https://github.com/digitaldemocracy2030/kouchou-ai/issues/455)

**作成者:** masatosasano2  
**作成日:** 2025-05-07T11:56:09Z  
**内容:**

内容から不具合修正であることを判定してラベルが付与されるか？

**コメント:** なし

---

### [[GITHUB_ACTIONS] ラベル判定用のプロンプトの改善](https://github.com/digitaldemocracy2030/kouchou-ai/issues/444)

**作成者:** masatosasano2  
**作成日:** 2025-05-06T16:17:00Z  
**内容:**

# 現在の問題点

ラベル判定が不適切なことがある

# 提案内容

以下の方針に従ってプロンプトを変更する
- [ラベルの説明文](https://github.com/digitaldemocracy2030/kouchou-ai/labels)を踏まえ、適宜修正・補足する
- 内容とマッチすれば何でもいいのではなく、解決すべき課題の分類になっているべきであることを明示する
- 明らかにその分類になると確信できない限り付与しない
- 画像は無視する
- 以下のラベルは定義上実装を見ないとわからないので、タイトルのキーワードマッチだけ残してLLM判定候補から外す
    - dependencies, javascript, python

# 検証結果

直近20件について概ね意図通り改善することと、重大な過不足がないことを確認済み
https://docs.google.com/spreadsheets/d/1XqtM7-eEbcjku2OWjHeD9js-1nHtlNXQY2UMM83ziJo

**コメント:** なし

---

### [[design] デザインシステムの設計](https://github.com/digitaldemocracy2030/kouchou-ai/issues/443)

**作成者:** UtkNggc  
**作成日:** 2025-05-06T13:04:56Z  
**内容:**

デザインシステムの組み方を考える。
（実際の構築作業は本Issueには含まれません。）

### 目的
・UIエンハンスの効率化
・UIブレを防いで一貫したUXを担保
・デザイン資産化

### やること
Figmaのvariables、styles、components、を駆使したシステム設計。
chakraUIを使用してるので、そこも踏まえて設計する。←ここが悩みどころ。

### 将来
これをやりたいのです。
https://zenn.dev/ubie_dev/articles/f927aaff02d618

**コメント:** なし

---

### [[FEATURE][design] headerにプロダクト名を表示する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/441)

**作成者:** UtkNggc  
**作成日:** 2025-05-06T11:13:43Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
現在、header左の部分が「デジタル民主主義2030」になっている。
デジタル民主主義2030は、複数プロダクトを含むプロジェクト名なので、
プロダクト内のheaderではプロダクト名を表記したい。

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
・メイン「広聴AI」
・サブ「part of project デジタル民主主義2030」
で画像作成しました。こちらに変えていただくのはいかがでしょう。

▼Figma
https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=176-458&t=PgvCDEqVEw2sn016-11

■設計意図
・ロゴ制作するには時間がかかるので、現時点では取り急ぎフラットなフォントで作成。
・現在のロゴサイズと同じサイズで作成したので、画像のリンク先を変えていただくだけで実装完了いただける見込み。

# ご相談したいこと
「part of project」がしっくりきてない気がする。。もっとふさわしいものがないか。

![Image](https://github.com/user-attachments/assets/9df3d50f-5945-4f6b-a2c7-f4b582b4151e)

**コメント:** なし

---

### [[FEATURE][design]見出し文言変更](https://github.com/digitaldemocracy2030/kouchou-ai/issues/437)

**作成者:** UtkNggc  
**作成日:** 2025-05-06T09:29:26Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
①見出しが英語表記されている
「Report」「About」「Admin Dashboard Report」「Analysis」
わかりやすい日本語の見出しにして、ユーザーの認知負荷を下げたい。

②About情報の位置はfooterが適切そう
ページ下部のデジ民を案内するAbout情報は、footer内にあるのが適切だと思いました。
footerにまとめるならここの「About」見出しも不要かなと。
本Issueでは見出しのみ整えて、別Issueでfooter改善したいです！

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
①は日本語表記にする
②はトルツメする

▼具体的にはFigmaのVDをご覧ください
https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=166-14&t=kOSSvTCqdQUPUdMZ-11

# ご相談したいこと
「Analysis」を何に訳すのがいいか迷っています。
「分析結果」「分析要約」など？

**コメント:** なし

---

### [セットアップに時間がかかる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/432)

**作成者:** shingo-ohki  
**作成日:** 2025-05-05T07:25:55Z  
**内容:**

>Macでセットアップをしているのですが、セットアップにはどれくらいかかるものでしょうか？
10分以上この画面のままなのですが、順調に進んでる認識で良いのでしょうか？

from #2開発_広聴AI より

![Image](https://github.com/user-attachments/assets/13b6aad6-8667-49ac-8c32-f387565a37af)

**コメント:** なし

---

### [[BUG][design]管理画面：スプレッドシートURLのinput欄がスマホ時のみ高さがつぶれてる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/431)

**作成者:** UtkNggc  
**作成日:** 2025-05-05T05:02:04Z  
**内容:**

### 概要

<!-- バグの簡潔な説明をお願いします -->
スマホビューでGoogleスプレッドシートURLのinput欄の高さが潰れている。
![Image](https://github.com/user-attachments/assets/a890fcae-dc5c-4902-8344-b10345d75203)

### 再現手順

1. スマホビュー環境の管理画面を開く
2. 入力データのスイッチをGoogleスプレッドシートにする

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->
PC・タブレットビューの時と同じようにしてほしい
![Image](https://github.com/user-attachments/assets/f7c89a70-d7bc-472a-9f43-ba9e065c1924)

よろしくお願いします！！

**コメント:** なし

---

### [[FEATURE] ローカルLLMを簡単に動かすために、OllamaのDockerを追加する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/430)

**作成者:** tokoroten  
**作成日:** 2025-05-05T04:33:13Z  
**内容:**

# 背景
#422 でローカルLLMが実装された（まだレビュー中）
しかし、ollamaやLM Studioを手動でインストールしないと、ローカルLLMを利用することができない

# 提案内容
- OllamaのDockerイメージを追加し、オプションで起動可能にする
- デフォルトで適切なモデルを起動時にロードするようにしておく

公式イメージ
https://hub.docker.com/r/ollama/ollama

いい感じの起動スクリプトを組む


**コメント:** なし

---

### [[design]ブランドコンパス制定](https://github.com/digitaldemocracy2030/kouchou-ai/issues/416)

**作成者:** UtkNggc  
**作成日:** 2025-05-02T07:37:24Z  
**内容:**

UI/UX/ワーディング/トンマナ、などを考える際の意思決定材料を制定したい。

### 作成場所
▼Figma Brand Compass スライドファイル
https://www.figma.com/slides/0B55u8rxDjjjpRJbNUEP0Z/%F0%9F%A7%AD-Brand-Compass?node-id=1-42&t=LFrlwNUh5bLJE7rA-1
スライドにした理由は、外部に広報する際にもリンク渡すだけでいいので便利だから

### 具体的には
・Vision Mission Values
・Brand Personality
・Brand Promise
・Design Principles
・Do & Don't
など。意思決定の材料になりそうなもの。

### 必要なもの
・現時点で固まってる指針（ふわっとでもok）
・先にジョインされてるメンバーさんたちが感じる本プロダクトの特性
・なんとなく共通認識になってるもの
などを、slackを漁ったりヒアリングをしたりして集めたい。
↑このヒアリングに広聴AIを利用したいです！！！（当事者としてUXを体験したい）

### 予定している手法
①上記の必要なものを集める
②集めた内容をもとに各内容に落とし込んで整えていく
③Figmaスライドにまとめる
④共通認識になるように全体に共有

### NEXT STEP
ブランドコンパスがあれば、ロゴ制作も可能です。

**コメント:** なし

---

### [[FEATURE] レポートがデフォルトで公開されないようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/365)

**作成者:** mtane0412  
**作成日:** 2025-04-23T13:24:06Z  
**内容:**

# 背景

> そもそもデフォルトpublicでlistedだったら公開したくないものも作成した瞬間公開されてしまう問題があるのでは

サーバーを公開している状態で、作成直後にpublicとして出力される問題がある。
現在の仕様だと、isPublic = falseなレポートは管理者でも表示ができない。

2025/4/23 定例
> レポートの限定公開ステータスの需要が少し気になってます！
> boolから型を変えるので後方互換もあるので、思ったより面倒かもしれないので。
> YouTubeのunlistedみたいなもの
> Clientのトップに単一のリストがあって自動的にそこに入って公開されてしまう(nishio)
> そもそもデフォルトpublicでlistedだったら公開したくないものも作成した瞬間公開されてしまう問題があるのでは
> YouTubeみたいにデフォルトprivateかせめてunlistedじゃないといけないのでは
> 管理画面同様にBASIC認証をかける？(nasuka)
> レポートごとに個別のパスワードを設定できればいいのでは(nishio)
> 複数のシリーズレポートのシェアで不便になりそう(aruga)
> そういう意味ではそもそもリストが複数作れないといけないのでは(nishio)

# 提案内容
デフォルトで非公開、もしくは限定公開( #341 )のようにアクセスできないようにする。
非公開であっても管理者が作成されたレポートを確認できるようにする。

**コメント:** なし

---

### [[FEATURE] レポートの限定公開](https://github.com/digitaldemocracy2030/kouchou-ai/issues/341)

**作成者:** mtane0412  
**作成日:** 2025-04-19T14:49:51Z  
**内容:**

# 背景
- レポートの公開ステータスは公開と非公開で、非公開にした場合、管理者であってもレポートページを参照することができない
- 面白いレポートができたので他人に共有したいが、一般に広く公開したいわけではないものがある。既に作成したデータも公開しているので、部分公開しようと思うと手間がかかる。


# 提案内容
- Youtubeの限定公開のように、URLを知っている人だけがアクセスできるレポートページの状態を作る
- 単純にトップページからリンクされないように出力すればできる？

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

### [（実験）LLMによるクラスタ品質の自動評価](https://github.com/digitaldemocracy2030/kouchou-ai/issues/144)

**作成者:** nasuka  
**作成日:** 2025-03-25T03:36:54Z  
**内容:**

# 背景
https://github.com/digitaldemocracy2030/kouchou-ai/issues/143

* こちらのイシューは上記のサブイシュー


# 提案内容
* LLMによるクラスタ品質の自動評価の実験を行う
  * 出力されたクラスタタイトル・説明文・所属データ点の情報に基づいて、LLMでクラスタの品質を評価する
* どのようなアプローチで評価するかは、assigneeの方におまかせする
  * 例としては、例えば以下のような評価項目のスコアをLLMで出力するようなアプローチがある
    * クラスタ内部の一貫性評価
      * クラスタタイトル・説明文・所属データのテキストを入力し、一貫性を100点満点でスコアリングする
    * クラスタ外部との分離度の評価
      * クラスタAの情報（タイトルや所属データ等）と、重心の距離が最もAに近いクラスタBの情報をLLMに入力し、分離度を出力する


**コメント:** なし

---

### [[FEATURE] コード以外の貢献も可視化する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/122)

**作成者:** shingo-ohki  
**作成日:** 2025-03-21T22:56:37Z  
**内容:**

プロジェクト固有の話題ではないですが、一旦こちらに

# 背景

現在、GitHub リポジトリへのコードのマージのみがコントリビューションとして可視化されています。しかし、プロジェクトの進行には以下のようなコード以外の重要な貢献もあります。

- Slack やオンラインミーティングでの議論・調整
- PR や Issue に対するレビューコメント・フィードバック
- #デジタル民主主義2030 のハッシュタグをつけた Twitter（X）での発信
- その他、プロジェクトの前進に貢献する活動

これらの貢献も適切に可視化することで、より多くの人が参加しやすくなり、
現在の「手が足りない」問題の解消や「属人化をなくす」ことにつながるのではないかと考えました。

# 提案内容

コード以外の貢献を記録・可視化する仕組みを検討するのはどうでしょうか？ 例えば、以下のような方法が考えられます。

- Slack や Twitter（X）での貢献を記録する仕組み（例: GitHub Actions で定期的に収集）
- コントリビューションログを作成し、定期的にレポートを公開

また、「プロジェクト本体のコードには手を出しづらいけど、このような形なら参加しやすい」という人が貢献しやすくなるという効果も期待できます。

参考: https://chatgpt.com/share/67ddda49-b6b8-800c-96c3-0a02a62b8839

また、いどばた の仕組みを一部流用できる可能性も考えられ、
熟議への参加や政策提案・法案成立へのコントリビューション可視化にもつながるかもしれません。

**コメント:** なし

---

### 過去7日間に作成されたissue (22件)

### [[FEATURE] 別のレポートのUMAPを使い回す](https://github.com/digitaldemocracy2030/kouchou-ai/issues/515)

**作成者:** nasuka  
**作成日:** 2025-05-14T02:44:06Z  
**内容:**

# 背景
* UMAPの実行結果がレポート出力毎に異なる
* これにより、同じデータを入力しても見た目がかなり変わるレポートが出力されてしまうためユーザー側の解釈が難しくなる

参考:
https://dd2030.slack.com/archives/C08F7JZPD63/p1747176858166689


# 提案内容
別のレポートのUMAPを使い回せるようにする。これにより、過去出力したレポートと同一の平面上にテキスト（=extraction結果）をプロットできるようになるため、時系列による傾向の変化等を比較しやすくなる。

## 実装案
api
* レポート出力時にUMAPのモデルを保存するようにする
  * 既存のレポートのUMAPを使い回す場合は、保存したUMAPをコピーして利用する
* レポートごとの実行パラメータ（config）を取得するendpointを実装する
  * admin側で、利用しているembedding等の情報を取得するため

admin
AI詳細設定内で以下の設定項目を新設する。
* UMAPのモデルを新規作成するか既存のレポートのものを使い回すかを選択できるようにする
* 既存のレポートのものを使い回す場合に、利用元のレポートを選択できるようにする

**コメント:** なし

---

### [[FEATURE] Extructionで並列実行した結果をソートしてから保存する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/514)

**作成者:** tokoroten  
**作成日:** 2025-05-14T00:38:18Z  
**内容:**

# 背景

同じ入力データを用いても、実行するたびに結果が異なる。

機械学習関連はSeed値が利用されているため、機械学習関連の問題である可能性は低い。

LLMはseedが固定されている。
```python
            payload = {
                "model": model,
                "messages": messages,
                "temperature": 0,
                "n": 1,
                "seed": 0,
                "timeout": 30,
            }
            if response_format:
                payload["response_format"] = response_format

            response = openai.chat.completions.create(**payload)
```


UMAPはrandom_stateでseedが固定されている。
`umap_model = UMAP(random_state=42, n_components=2, n_neighbors=n_neighbors)`

k-meansも同じ
`  kmeans_model = KMeans(n_clusters=initial_cluster_num, random_state=42)`


残っている可能性としては、LLMに対するリクエストの並列実行の結果、応答順序が異なり、結果の順序が変わることだと考えられる。
そして、UMAPに対する入力データの順序が毎回変わっているのだと思われる。結果として、Umapの結果が毎回異なる、ということになっていると考えられる。

# 提案内容

並列実行された結果が帰ってくる順序によって、データの並びが異なると考えられる。
コードはおそらくこの辺
https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/server/broadlistening/pipeline/steps/extraction.py


**コメント:** なし

---

### [[FEATURE] 確率的挙動がある箇所にはランダムシードを設定して結果を固定する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/513)

**作成者:** tokoroten  
**作成日:** 2025-05-14T00:18:23Z  
**内容:**

# 背景

同じデータを入力しても同じ結果にならない

# 提案内容

ランダムシードを設定する

**コメント:** なし

---

### [[FEATURE]windows直環境での起動手順・構成を整備する（python仮想環境＋npm 対応）](https://github.com/digitaldemocracy2030/kouchou-ai/issues/509)

**作成者:** take365  
**作成日:** 2025-05-13T14:28:44Z  
**内容:**

### 🔍 概要
現在の `kouchou-ai` プロジェクトは Linux/Mac 環境での実行を前提にしている部分があり、Windows 環境での手動起動・開発がやや煩雑です。  
この Issue では、Windows 上で仮想環境（Python venv）や npm を活用しながら、直接実行できる構成を整備することを目的とします。

---

### 🧭 背景
- #496 で求められている「すぐに動かせる構成」の一環。
- Windowsユーザーが詰まりやすい起動手順の改善。
- bash系スクリプトを使わずに、`cmd` / `PowerShell` で起動できる手順の整備。

---

### ✅ 対応内容（予定）
- `dev_win_direct.bat` の整備
  - 仮想環境 (`venv`) の `activate` による Python 実行
- `.env` の読み込み自動化（`python-dotenv` などを検討）
- README への起動手順（Windows向け）追記

---

### 🔗 関連PR
- draft: [PR #499](https://github.com/digitaldemocracy2030/kouchou-ai/pull/499)  
  → 本 Issue をもとに今後ブラッシュアップ予定

---



**コメント:** なし

---

### [[REFACTOR] report_status.jsonの互換性を担保するためのコードの削除](https://github.com/digitaldemocracy2030/kouchou-ai/issues/507)

**作成者:** nasuka  
**作成日:** 2025-05-13T12:51:01Z  
**内容:**

# 現在の問題点
* report_status.jsonの形式が変わったため、互換性を担保するための一時的なコードが実装されている

# 提案内容
* メジャーバージョンをアップデートした段階でコードを削除する
  * ver2.0 -> ver3.0のタイミングで削除する


**コメント:** なし

---

### [[design] デザインシステム構築／数値環境](https://github.com/digitaldemocracy2030/kouchou-ai/issues/506)

**作成者:** UtkNggc  
**作成日:** 2025-05-13T12:14:28Z  
**内容:**

https://github.com/digitaldemocracy2030/kouchou-ai/issues/443 で全体の設計ができたので、構築開始できます。
1つ1つのタスクが重いのでIssue分散してます。

このIssueでは、spacing、radius、border、effect、max.min-sizeなどの数値周りの環境を整備します。

## 手順
作業は広聴AIのFigmaファイルで行います。

1. chakraUIの数値情報すべてvariablesで定義
2. 使うものだけ洗い出して作業パネルで呼び出せるように設定
3. そのtokenを使用してstylesに登録
4. Figmaファイル内にガイドライン作成（ブランド思想用ではなくデザイナ&エンジニアが見る用に一覧性のあるもの）

### 期待できる効果

- デザイナーが容易に数値選定できるようになる（エンハンス時の数値の迷いを大幅に削減）
- chakraUI範囲内の数値を使用するため実装がやりやすいのではないか
- 将来的にchakraUIをはがして独自サイズを使うことになったとしてもVariablesの変更ですべて置き換わる

### 留意点
ブランドコンパス内に明記されてるブランドパーソナリティのデザイントンマナを叶える設計にする。
https://www.figma.com/slides/0B55u8rxDjjjpRJbNUEP0Z/%F0%9F%A7%AD-Brand-Compass?t=yLYyNEeIO9pprmn3-6

**コメント:** なし

---

### [[design] デザインシステム構築／Typography環境](https://github.com/digitaldemocracy2030/kouchou-ai/issues/505)

**作成者:** UtkNggc  
**作成日:** 2025-05-13T12:05:53Z  
**内容:**

https://github.com/digitaldemocracy2030/kouchou-ai/issues/443 で全体の設計ができたので、構築開始できます。
1つ1つのタスクが重いのでIssue分散してます。

このIssueではタイポグラフィに関わる環境を整備します。

## 手順
作業は広聴AIのFigmaファイルで行います。

1. chakraUIのタイポ情報すべてvariablesで定義
2. 使うものだけ洗い出してsemantic定義
3. そのtokenを使用してstylesに登録
4. Figmaファイル内にタイポグラフィガイドライン作成（ブランド思想用ではなくデザイナ&エンジニアが見る用に一覧性のあるもの）

### 検討が必要なこと

- 日本語family優先順位の検討（Noto sans, Hiragino Kaku Gothic ProN, YuGothic, Meiryo、など
- 英数字family変える変えない
- size, line-heightの取捨選択

### 期待できる効果

- デザイナーが容易にタイポ選定できるようになる（エンハンス時の色の迷いを大幅に削減）
- chakraUI範囲内の数値を使用するため実装がやりやすいのではないか
- 将来的にchakraUIをはがして独自タイポを使うことになったとしてもVariablesの変更ですべて置き換わる

### 留意点
ブランドコンパス内に明記されてるブランドパーソナリティの「ボイス」を叶える設計にする。
https://www.figma.com/slides/0B55u8rxDjjjpRJbNUEP0Z/%F0%9F%A7%AD-Brand-Compass?t=yLYyNEeIO9pprmn3-6

**コメント:** なし

---

### [[design] デザインシステム構築／color環境](https://github.com/digitaldemocracy2030/kouchou-ai/issues/504)

**作成者:** UtkNggc  
**作成日:** 2025-05-13T11:57:14Z  
**内容:**

https://github.com/digitaldemocracy2030/kouchou-ai/issues/443 で全体の設計ができたので、構築開始できます。
1つ1つのタスクが重いのでIssue分散してます。

このIssueではカラーに関わる環境を整備します。

## 手順

作業は広聴AIのFigmaファイルで行います。

1. chakraUIのカラーたちをすべてPrimitiveにいれる
2. Primitiveから選定してSemanticで定義（実質上のプロダクトカラー）
3. stylesに登録
4. Figmaファイル内にカラーガイドライン作成（ブランド思想用ではなくデザイナ&エンジニアが見る用に一覧性のあるもの）

### 期待できる効果

- デザイナーが容易に色選定できるようになる（エンハンス時の色の迷いを大幅に削減）
- chakraUI範囲内のカラーのため実装がやりやすいのではないか
- 将来的にchakraUIをはがして独自カラーを使うことになったとしてもPrimitiveの変更ですべて置き換わる

### 留意点
ブランドコンパス内のブランドパーソナリティとデザイントンマナを叶える設計にする
https://www.figma.com/slides/0B55u8rxDjjjpRJbNUEP0Z/%F0%9F%A7%AD-Brand-Compass?t=yLYyNEeIO9pprmn3-6

**コメント:** なし

---

### [個人情報生成と除去率測定の機能追加](https://github.com/digitaldemocracy2030/kouchou-ai/issues/503)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-05-13T09:31:39Z  
**内容:**

# 個人情報生成と除去率測定の機能追加

## 概要
傾聴AIシステムにおいて、以下の機能を追加する必要があります：

1. LLMに架空の個人情報を生成させ、既存の文章にうまく埋め込むコードの作成
2. 個人情報の抽出プロンプトを改善し、個人情報の除去率を測定する機能の実装

## 詳細

### 1. 架空の個人情報生成と埋め込み
- LLMを使用して架空の個人情報を生成するコードを作成
- 生成した個人情報を既存の文章に自然に埋め込む機能の実装
- 対象となる個人情報の種類：
  - 投稿者本人の情報（年齢、職業、氏名、性別、家族構成、人間関係など）
  - 批判対象となる第三者の個人情報
- 注意点：政治家などの公人の公開されている個人情報は除去対象としない

### 2. 個人情報除去率の測定
- 現在の抽出プロンプトを改善し、個人情報の検出・除去精度を向上
- 個人情報の除去率を定量的に測定する方法の実装
  - 個人情報をインジェクションした文章と通常の文章を比較
  - LLMを使用して個人情報が適切に除去されているかを判定
  - 判定プロセス自体もLLMで実装
- 測定結果を基にプロンプトの継続的な改善

## 期待される成果物
- 架空の個人情報生成と埋め込みのためのコード
- 改善された個人情報抽出プロンプト
- 個人情報除去率の測定機能と評価方法

## 参考情報
このIssueは2025年5月13日のSlackチャンネル #8_devinと人間たちの部屋 での会話に基づいています。


**コメント:** なし

---

### [[DOCKER] なしでも動かせるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/496)

**作成者:** masatosasano2  
**作成日:** 2025-05-13T02:11:36Z  
**内容:**

# 課題

- Docker Desktop の会社PCへのインストールが以下の事情で禁止されることがある
    - 2022/02 以降、一定以上の売上または従業員数のある組織の「非営利のOSS開発」以外に対してDockerの利用が有償になった
    - 具体的にどの条件を満たすと「利用」と判定されるかは定かでなく、ダウンロード時に登録されたメールアドレスやIPが会社のものかどうかで判定される可能性がある
    - そのため、防御的な判断としてDocker Desktopの利用がNGになった

- このようなケースでは現状、公聴AIが使えないので、Dockerなしで動かせるようにしたい

# 実現手段

- ビルド/デプロイの時間あたりを犠牲にしてDockerをOFFにできないか？
- または、RancherやPodmanなど他の手段で動かせないか？

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

### [[REFACTOR] Azureのモデル選択の不整合の修正](https://github.com/digitaldemocracy2030/kouchou-ai/issues/477)

**作成者:** nasuka  
**作成日:** 2025-05-11T00:28:46Z  
**内容:**

# 現在の問題点
* 通常のOpenAIと異なり、Azure OpenAI を使う場合は事前にリソース（LLM・embedding）をデプロイしておく必要があり、APIを呼び出す際にモデル名だけでなくリソースに紐づく情報を渡す必要がある
  * [このあたり](https://github.com/digitaldemocracy2030/kouchou-ai/blob/a167a548ecba9b7b9fd279e5ea9a4f745bb3c550/.env.example#L63-L71) の環境変数でセットしている情報
* 現在のモデル作成時のUIでは、リソースの有無にかかわらず一律で3つのモデルが表示されるようになっている
   * ここで選択されたモデルは実際には使われず、環境変数で指定したモデルが使われるため利用モデルの不整合が起きている

![Image](https://github.com/user-attachments/assets/aab703d5-bc48-4055-a27f-5726bceb6d94)

# 提案内容
* （ライトに解決する案）Azure利用の場合はAdmin上ではモデルを選択できないようにする
  * モデル選択のセレクトボックスをグレーアウトし、Azure利用の場合は環境変数でセットしたモデルが使われる旨を表示する
* （ちゃんとやる案） LLMのdeployments の一覧をAPI経由で取得し、モデル選択肢のセレクトボックスで選択できるようにする
  * API自体はありそう
    * https://chatgpt.com/c/681fed08-3be4-800f-aca0-3ebaac6fed6f




**コメント:** なし

---

### [[REFACTOR] envのUSE_AZUREを剥がす](https://github.com/digitaldemocracy2030/kouchou-ai/issues/475)

**作成者:** tokoroten  
**作成日:** 2025-05-10T15:35:37Z  
**内容:**

# 現在の問題点
LLMプロバイダが選択できるようになったので、Azureを使うかどうかの判断をenvを経由して行う必要はなくなった

# 提案内容
env から USE_AZURE を消す、関連するif文を剥がしていく


**コメント:** なし

---

### [[ALGORITHM] bonsaiの検証をする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/474)

**作成者:** tokoroten  
**作成日:** 2025-05-10T15:33:22Z  
**内容:**

# 背景

bonsaiという面白そうなツリークラスタリングのアルゴリズムが登場したので実験したい

![Image](https://github.com/user-attachments/assets/5f193a78-4101-4c44-bd07-ed6a2339d813)
https://x.com/DucheneJohan/status/1920819010221769022


https://github.com/dhdegroot/Bonsai-data-representation

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

# 対象データ
<!-- 実験に用いるデータについて記入してください。検討中の場合はその旨を記載してください。 -->


# 実験結果について（実験を実施される方向け）
* 実験結果はこちらの[Google Docs](https://docs.google.com/document/d/1GK4Arh8ZyJmQjQ4iW1CRMruEUPicKAAUZEZi2TpAo4w/edit?tab=t.0#heading=h.j72jxw32gila)に記載してください

**コメント:** なし

---

### [[FEATURE] 環境検証ページに、Azure、OpenRouter、LocalLLMを付ける](https://github.com/digitaldemocracy2030/kouchou-ai/issues/473)

**作成者:** tokoroten  
**作成日:** 2025-05-10T15:31:10Z  
**内容:**

# 背景

Client-adminの環境検証ページは、LLMプロバイダーの選択肢を作る前に作成されたものなので、ChatGPTしか対応していない。

![Image](https://github.com/user-attachments/assets/53ef974a-7cae-4be4-a43d-f62b7999833e)

# 提案内容

- Azureの環境確認
- OpenRouterの環境確認
- LocalLLMの環境確認


**コメント:** なし

---

### [[DOCUMENT] ローカルLLMのベンチマーク、推奨スペックの決定](https://github.com/digitaldemocracy2030/kouchou-ai/issues/471)

**作成者:** tokoroten  
**作成日:** 2025-05-10T13:18:48Z  
**内容:**

# 現在の問題点

- ローカルLLMがどれくらいの速度で動作するのかが分かっていない。
- どれくらいのマシンであれば動作するのかが分かっていない
- 標準のLLMモデルを何にするのかという議論は出来ていない

# 提案内容

- LLMのベンチマーク用のスクリプトの作成
- 様々なPCで動作確認を行い、ベンチマークを行う
  - サンプルのデータが何分で処理でき、1件あたり何秒で処理できるか？というのが出るとよい
- NPUによるアクセラレーションをいい感じに効かせる
  - AMD、Apple、Intelのアクセラレータが効くようにする
  - Arm Windowsはターゲット外でいいと思う

# 最終的なゴール

- 自治体向けにどのようなPCを買えば快適に動作するのか？という案内を出す。
  - 理想はMSのCopilot+PC基準のスペックで動くような提案をする

**コメント:** なし

---

### [[ALGORITHM]　extractフェーズで、個人情報の除去を行う](https://github.com/digitaldemocracy2030/kouchou-ai/issues/470)

**作成者:** tokoroten  
**作成日:** 2025-05-10T01:48:01Z  
**内容:**

# 背景
個人情報が含まれているデータをもとに、現在の公聴aiを走らせ、結果をウェブ公開する場合、下手をすると入力された個人情報がそのまま漏れる可能性がある

現状は人間が事前の除去をしなければならず、前処理の負担がおおきい

# 提案内容

extractフェーズもしくはその前段で、個人情報やプライバシー情報のマスキングや除去をLLMで行う

# 対象データ
<!-- 実験に用いるデータについて記入してください。検討中の場合はその旨を記載してください。 -->


# 実験結果について（実験を実施される方向け）
* 実験結果はこちらの[Google Docs](https://docs.google.com/document/d/1GK4Arh8ZyJmQjQ4iW1CRMruEUPicKAAUZEZi2TpAo4w/edit?tab=t.0#heading=h.j72jxw32gila)に記載してください

**コメント:** なし

---

### [エネルギー庁パブコメのpdf -> csv化](https://github.com/digitaldemocracy2030/kouchou-ai/issues/467)

**作成者:** nasuka  
**作成日:** 2025-05-08T07:24:34Z  
**内容:**

# 背景
パブコメデータを入手できたがpdf形式のため、csvなどの扱いやすい形式に変換する必要がある。

データはこちら
https://w1740803485-clv347541.slack.com/archives/C08PX74S5T4/p1746688643277269


nishioさんが以前別のパブコメ向けに作成していたスクリプトはあるが、恐らくそのまま適用することは難しい
```
PDFからCSVを生成するプログラムは文化庁バブコメの時に作ったものがあります
https://github.com/nishio/aipubcom-data
[16:18](https://w1740803485-clv347541.slack.com/archives/C08PX74S5T4/p1746688728888009)
が、そのまま使えることはないと思うので試してみて正規表現を直したりすることが必要です
16:19
僕は17時から出かけるので作業できないですが、これをCSVに変換するところをできる人がいればお任せしたい
New
16:21
作りかけていたツールはこちらにあります
https://github.com/nishio/pubcom-seiri
単純一致を検知してフィルタするとか、embeddingで距離を計算するとかはtool1.pyで大体実装済み
このパブコメデータでまともに動くかどうかが今後検証が必要なところです
```

# 実施内容
・パブコメをpdf -> csvに変換する
・広聴AIへのPRは不要。独立したスクリプトを実装する。

**コメント:** なし

---

### [OpenAI APIキーの確保](https://github.com/digitaldemocracy2030/kouchou-ai/issues/464)

**作成者:** nasuka  
**作成日:** 2025-05-08T01:53:19Z  
**内容:**

# 現在の問題点
* OpenAIのAPIキーを使ってイシューにラベリングする仕組みがあるが、現状APIキーがないため動作しなくなっている
https://w1740803485-clv347541.slack.com/archives/C08FL58LK8V/p1746668461239949?thread_ts=1746662038.867129&cid=C08FL58LK8V

# 対策
1. 何らかの方法でAPIキーを確保する（ボードメンバーに打診する等）
2. （無料のものがあれば） OpenAI API以外のLLM APIを使って分類する
3. LLMによる分類は廃止する



**コメント:** なし

---

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

### 過去7日間に更新されたissue（作成・クローズを除く）(11件)

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

### [[FEATURE]レポート一覧画面：レポート0件時のエンプティ表現をする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/428)

**作成者:** UtkNggc  
**作成日:** 2025-05-04T17:07:41Z  
**内容:**

# 現状
エンジニアさんに調べていただいたところ、
・管理画面（client-admin）では「レポートがありません」が表示される
・ユーザー向け（client）の一覧画面では何も表示されない
<img width="1471" alt="Image" src="https://github.com/user-attachments/assets/dc103f60-8421-4079-b7a3-e09e1887195a" />
<img width="1477" alt="Image" src="https://github.com/user-attachments/assets/f0eeed4d-3dad-4816-ac18-f6d40dc48353" />

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
エンプティには
・現状を知らせる（ユーザーを迷子にしない）
・次のアクションの誘導（行動促進）
・プロダクトに対する信頼獲得
などの役割があります。

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
具体的にはデザイン時に検討したいですが、少なくとも、
・現状を伝える
・エンプティを解消するために何をしたらいいかを伝える
を満たすUIにはしたい。

# 担当デザイナーへ
かけられる開発工数や、ここに到達するユーザーの背景次第で、どれだけリッチにするかが変わります。
なのでそれを踏まえたうえで、
・文字のみ
・文字 + イメージイラスト
・参照できるものがあればそこへのリンク
・ユーザーにとっては使い方の学習の機会にもなるかもしれないため、その観点でデザインにできることがないか
などを検討していただけるといいかも。

**コメント:** なし

---

### [コードレビューの効率化](https://github.com/digitaldemocracy2030/kouchou-ai/issues/417)

**作成者:** shingo-ohki  
**作成日:** 2025-05-02T08:08:24Z  
**内容:**

# 背景
Devin の活用が進むに伴い、開発のボトルネックが PR レビューに移りつつある

# 対応策の案

> Shingo OHKI
>   12:00
> 次なるボトルネックはPRレビュー（嬉しい悲鳴） （編集済み） 
> Screenshot from 2025-05-02 11-54-20.png
> NISHIO Hirokazu
>   [12:43](https://w1740803485-clv347541.slack.com/archives/C08FL58M3D3/p1746157384711949)
> Devinに辛口レビューさせよう()
> haruki shimizu
> これ、レビューはお金かかってしまうのですが、サマリーは無料だそうです
> https://www.coderabbit.ai/
> coderabbit.aicoderabbit.ai
> AI Code Reviews | CodeRabbit | Try for Free
> Most advanced AI code reviews that catches 95%+ bugs. Free your devs to ship code faster. (139 kB)
> https://www.coderabbit.ai/
> TakateTomoki
>   13:28
> コードラビット、パプリックリポジトリならレビューも無料です
> コードラビットからdevinに指摘させて更に書き直させるみたいなことできるはず （編集済み） 

from #雑談 チャンネル
https://w1740803485-clv347541.slack.com/archives/C08FL58M3D3/p1746154812918109

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



**コメント:** なし

---

### [[FEATURE] 「全体図」と「階層図」の意見グループの色を揃える](https://github.com/digitaldemocracy2030/kouchou-ai/issues/337)

**作成者:** shingo-ohki  
**作成日:** 2025-04-19T05:17:29Z  
**内容:**

# 背景
「全体図」から「階層図」に切り替えた時に、注目していた意見グループを見失いがち（もちろん文字を読めば分かる）

from 2025.4.19 広聴AIもくもく会


# 提案内容
「全体図」と「階層図」の意見グループの色を揃えてはどうか？

**コメント:** なし

---

### [[FEATURE] LLMが出力した結果の手動修正機能（編集機能）がほしい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/310)

**作成者:** nasuka  
**作成日:** 2025-04-15T05:38:53Z  
**内容:**

# 背景
* LLMが出力したクラスタ名や説明、argumentが適切でない場合がある
  * e.g.
    * 公開するのに不適切な単語や表現がクラスタ名に含まれている
    * 他のクラスタと同一の内容がクラスタ名に含まれている
* このようなケースにおいては、LLMのアウトプットを見た後に人間が手動で文言を修正したい

# 提案内容
LLMが出力したテキスト（クラスタタイトル・説明・概要・argument）について、手動で編集する画面をadminに設け、レポートに編集内容を反映する


(admin)
* 上記の編集画面を設ける
  * 編集後のデータを編集用のendpointに送る

(api)
* 編集用のendpointを実装する
  * リクエストで受け取ったデータを各種中間ファイル（args.csv等）に保存
  * hierarchical_aggregation.pyを再度実行し、更新後のデータでhierarchical_result.jsonを保存する

そもそも全要素を編集できるようにするかというのは議論の余地がある。やるとしても、まずはクラスタ名のみを対象にするなど、部分的に始めていくのが良さそう。
また、透明性担保のために編集履歴を残すようにするかも議論の余地がある。

**コメント:** なし

---

### [[FEATURE]exe形式での配布によるインストール簡略化](https://github.com/digitaldemocracy2030/kouchou-ai/issues/289)

**作成者:** nishio  
**作成日:** 2025-04-13T00:24:58Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
現状の広聴AIはDockerとGitの知識・インストールが前提となっており、特にITスキルやセキュリティ制限のある自治体ユーザーにとっては導入のハードルが高い。

>「Dockerのインストールが認められてない（情シス部門の理解が必要）」「自治体関係者の中でのアーリーアダプターたちが試す際に、最初の①リポジトリをクローン」段階で既にかなり大きなハードルになっている。」

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

(解決策案) アプリケーションを単一の実行ファイル（.exe形式）にパッケージ化し、DockerやGitのインストール、コマンドライン操作を不要にすることを検討する。

>「exe化は難しいだろうか？(たねのぶ)」。

これにより、ダブルクリック等で簡単に起動でき、非エンジニアやセキュリティ制限のある環境でも利用しやすくなる可能性がある。ただし、技術的な実現可能性や配布ファイルサイズなどの課題も考慮する必要がある。


(nishioコメント) DockerやGitを「インストールできるが難しい」のケースには有効かも。「Dockerのインストールが認められてない」の場合、広聴AI.exeが作られたところでそれのインストールが認められないのではという気がする。

**コメント:** なし

---

### [[BUG]ScatterChartの全画面表示で要約文が「全画面終了」ボタンの後ろに隠れないようにする処理が不安定](https://github.com/digitaldemocracy2030/kouchou-ai/issues/283)

**作成者:** masatosasano2  
**作成日:** 2025-04-12T18:36:39Z  
**内容:**

### 概要
Issue #278 が PR #282 で修正されたが、以下の課題が残ったため本Issueに切り出された。

PR #282 の修正内容
![Image](https://github.com/user-attachments/assets/a7a1bd58-febe-4993-a49a-2612b1c90ec9)

残課題
![Image](https://github.com/user-attachments/assets/3d080c1d-1502-4b09-8aca-fb2c1fdb9e52)

### 再現手順

1. 「全体図」または「濃い意見グループ」モードを選択する
2. 「全画面表示」ボタンを押す
3. ブラウザのサイズを極力小さくする
4. 画面上部の、右端より少し左側あたりでマウスを動かし続ける

### 期待する動作

要約文が「全画面終了」ボタンの後ろに隠れない（正確には、隠れたままにならない）ようにする


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

### [[REFACTOR] 濃いクラスタのアイコン変更](https://github.com/digitaldemocracy2030/kouchou-ai/issues/113)

**作成者:** nishio  
**作成日:** 2025-03-20T12:20:30Z  
**内容:**

# 現在の問題点

<img width="249" alt="Image" src="https://github.com/user-attachments/assets/bc626d04-e7c0-4245-9b01-e762d433a434" />

濃いクラスタのアイコンは特に意味はなくこれになっている


# 提案内容

多分叩き台の案がないとどう変えたらいいかの議論もできないと思うので雑に描いておく

![Image](https://github.com/user-attachments/assets/9e46dfd6-71d4-4c2b-bbd5-1c79220c8d80)

アイコンとしてデザインできるかは度外視して描くとこんな感じで「全体像」は全体にたくさんの点が散らばっており、「濃いクラスタ」はぎゅっとした「濃い」「密度の高い」塊がいくつかある感じ

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (23件)

### [Fix/biome lint errors](https://github.com/digitaldemocracy2030/kouchou-ai/pull/511)

**作成者:** shingo-ohki  
**作成日:** 2025-05-13T15:29:57Z  
**変更:** +921 -1862 (67ファイル)  
**マージ日:** 2025-05-13T15:33:01Z  
**内容:**

# 変更の概要
- #510 に伴い lint error がでていたので npm run format で機械的に修正しました

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- ざっとレポート生成、レポート表示の一連の操作を行い、問題ないことを確認しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [x] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **スタイル**
  - 複数行で記述されていたインポート文、関数宣言、JSX要素、配列やオブジェクトリテラルなどを単一行にまとめ、コードの可読性と一貫性を向上しました。
  - ReactコンポーネントのforwardRef宣言や型注釈も、より簡潔な1行スタイルに統一しました。
  - CSSのグラデーション指定や辞書データも1行表記に変更されています。
- **ドキュメント**
  - 表示や動作には影響ありませんが、全体的にコードのフォーマットが整理されました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [biomeのlineWidthを120まで引き上げる](https://github.com/digitaldemocracy2030/kouchou-ai/pull/510)

**作成者:** nasuka  
**作成日:** 2025-05-13T14:58:08Z  
**変更:** +2 -1 (1ファイル)  
**マージ日:** 2025-05-13T15:03:00Z  
**内容:**

# 変更の概要
* biomeのlineWidthをデフォルトの80 -> 120に引き上げた

# 変更の背景
80だと不自然な箇所で切れてしまうケースがあったので120まで引き上げた
参考: https://github.com/digitaldemocracy2030/kouchou-ai/pull/508#discussion_r2086898542

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

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **スタイル**
  - フォーマッターの設定に最大行幅（120文字）が追加され、コードの整形方法が変更されました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [フロントのlint errorを修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/508)

**作成者:** nasuka  
**作成日:** 2025-05-13T13:43:45Z  
**変更:** +741 -594 (39ファイル)  
**マージ日:** 2025-05-13T14:18:59Z  
**内容:**

# 変更の概要
* client/client-adminのlint errorを修正
  * npm run formatで機械的に修正
  * 機械的に修正できないものは一部手動で修正

# 変更の背景
* lint errorが大量に出ていた

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/502

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->
基本的な動作ができるかは確認しました。

* csvファイルからレポートが生成できる
* client/client-adminの各画面がエラーなく閲覧できる

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [ ] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **スタイル**
  - インポート文や文字列リテラルのクォートをシングルからダブルへ統一
  - トレーリングカンマや改行、インデントの調整など、コードの可読性向上のためのフォーマット修正
  - 型専用インポート（import type）の導入と型注釈の明示化
  - JSXや関数パラメータの整形、空白行の整理

- **リファクタリング**
  - 一部関数や変数の型注釈の明確化や引数リストの整形
  - エラーハンドリングや条件分岐の記述スタイルの統一

- **ドキュメント**
  - ファイル末尾への改行追加

- **テスト**
  - テストコード・設定ファイルのクォート統一やインポートの型指定化

※本リリースは機能や挙動の変更はありません。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [client, client-admin の見出しを変更](https://github.com/digitaldemocracy2030/kouchou-ai/pull/501)

**作成者:** shingo-ohki  
**作成日:** 2025-05-13T08:54:14Z  
**変更:** +8 -14 (5ファイル)  
**マージ日:** 2025-05-13T10:41:38Z  
**内容:**

# 変更の概要
- client, client-admin の見出しを日本語に変更します
- About 見出しを削除します (footter にまとめるのは #438 にあるので今回は未対応です）

# スクリーンショット
- client-admin
  - 変更前
![Screenshot From 2025-05-13 17-50-12](https://github.com/user-attachments/assets/150fbe14-0314-44ce-8934-f7ad4eba4ce1)

  - 変更後
![Screenshot From 2025-05-13 17-50-31](https://github.com/user-attachments/assets/28f2fb53-4b4c-4d1f-abdf-f0608650858c)


- client（レポート一覧）
  - 変更前
![Screenshot From 2025-05-13 17-50-48](https://github.com/user-attachments/assets/58cb8505-f229-4f52-aa52-988a58c3562a)

  - 変更後
![Screenshot From 2025-05-13 17-51-00](https://github.com/user-attachments/assets/c24e7a51-6100-479f-971e-db8ee81ebbaf)

- client(個別のレポート）
  -  変更前
![Screenshot From 2025-05-13 17-51-11](https://github.com/user-attachments/assets/c0cbdf48-c2a2-4bef-8b56-a1e0fece6b42)

  -  変更後
![Screenshot From 2025-05-13 17-51-29](https://github.com/user-attachments/assets/2d2c9ad8-7b34-4551-ab49-14ae757a280c)

# 関連Issue
#437 

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

- [x] CLAの内容を読み、同意しました



<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **スタイル**
  - 各ページおよびコンポーネントの見出しを日本語に変更し、テキストの位置揃えを中央から左寄せに調整しました。
  - 見出しの下部マージンを拡大し、レイアウトの余白を改善しました。
  - 「About」ページの見出しを削除しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [限定公開機能を実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/500)

**作成者:** nasuka  
**作成日:** 2025-05-13T08:30:08Z  
**変更:** +458 -90 (10ファイル)  
**マージ日:** 2025-05-13T12:57:05Z  
**内容:**

# 変更の概要
* 従来の公開/非公開に加えて、限定公開（unlisted）を実装
* 「限定公開」にセットされたレポートは以下の挙動になる
  * adminの一覧画面では表示される
  * clientにおいて、
      * **一覧画面では表示されない**
      * レポートの詳細画面（ `/{slug}`） では閲覧できる
        * つまり、管理者などのURLを知っているユーザーのみが閲覧できる
* **作成直後のレポートは「限定公開」状態となる**
  * 実用上、作成されたレポートはすぐに公開したくないケースが多いと思われるため
    * 例えばAzure上で広聴AIをホスティングしている場合、作成したレポートを内部で確認し、問題なければ公開という手順を踏むことが多いと思われる

# スクリーンショット
公開方式の切り替えはドロップダウン方式で実装した（従来のラジオカードだと幅が足りなかったため）
![image](https://github.com/user-attachments/assets/2cc0ea37-a171-4474-84d2-6eb6dff28926)


# 変更の背景
前述したように、外部には広く公開したくないが、内部ではレポートを共有したいというニーズがあるため実装した

# 関連Issue
Close https://github.com/digitaldemocracy2030/kouchou-ai/issues/365
Close https://github.com/digitaldemocracy2030/kouchou-ai/issues/341

# 動作確認の結果
* 作成直後のレポートが限定公開状態になる
* 限定公開のレポートがadminの一覧画面に表示される
* 限定公開のレポートがclientの一覧画面に表示されない
* 限定公開のレポートの詳細画面にアクセスできる

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
  - レポートの公開範囲設定が「公開」「限定公開」「非公開」の3種類から選択可能に拡張されました。
  - 管理画面の公開範囲切り替えUIがラジオボタンからドロップダウン形式に変更され、操作性が向上しました。

- **バグ修正**
  - レポートの公開範囲判定ロジックが厳密化され、非公開レポートの誤表示を防止します。

- **テスト**
  - 公開範囲変更APIの動作確認や旧フォーマットからのデータ変換処理に関するテストが追加され、品質が強化されました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Chart に枠線をつける](https://github.com/digitaldemocracy2030/kouchou-ai/pull/497)

**作成者:** masatosasano2  
**作成日:** 2025-05-13T03:14:35Z  
**変更:** +8 -2 (1ファイル)  
**マージ日:** 2025-05-13T04:56:39Z  
**内容:**

# 変更の概要
- 全画面表示でない場合のChartに枠線をつけました
- これに伴い、枠線内部のChartが描画されないmargin-bottom領域が不自然になったため、無くしました

# スクリーンショット
<img width="1324" alt="image" src="https://github.com/user-attachments/assets/fed88bf1-d057-4f36-ab29-3bfae6f68f2b" />
<img width="1302" alt="image" src="https://github.com/user-attachments/assets/47795d24-6b84-4e26-adc7-38817df46af8" />


# 変更の背景
- 枠線がないことで描画領域が曖昧だった
  - ScatterChartの範囲がわかりにくい
  - TreemapChartの「全体」パネルの背景色が白なので、気づきにくい
- Issue 488 でScatterChartのグリッドを非表示にしたことでより分かりにくくなった

# 関連Issue
#491 

# 動作確認の結果
- 上記キャプチャの通り
- 全画面表示には枠線は付与されない
- Treemapの内側に追加のmarginが付与されてしまうが、無くし方がわからなかった。必要であれば別Issueで対応する。

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **スタイル**
  - チャートコンテナに薄い枠線を追加し、チャート周辺の余白を調整しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [ScatterChartの全画面表示でボタンが重ならないようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/495)

**作成者:** masatosasano2  
**作成日:** 2025-05-13T00:11:42Z  
**変更:** +109 -78 (1ファイル)  
**マージ日:** 2025-05-13T01:18:14Z  
**内容:**

# 変更の概要
ScatterChartの全画面表示で「全画面終了」ボタンとその他のボタンが重ならないよう、その他のボタンのエリアを下方向に移動する

# スクリーンショット
<img width="455" alt="image" src="https://github.com/user-attachments/assets/e810d116-cc76-461b-830b-767d2144f2b6" />

# 関連Issue
#479 

# 動作確認の結果
- 全画面の場合は上記キャプチャの通り重ならないようになった
- 全画面でない場合は従来通り↓
<img width="361" alt="image" src="https://github.com/user-attachments/assets/a877b5e5-4d97-495a-9d1f-a5f1d3979dba" />

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [x] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **バグ修正**
  - Plotlyのモードバーが全画面ボタンと重ならないようにUIを調整しました。

- **スタイル**
  - コードのフォーマットとインデントを改善し、可読性を向上させました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Update README.md `docker compose up` の時間短縮](https://github.com/digitaldemocracy2030/kouchou-ai/pull/492)

**作成者:** masatosasano2  
**作成日:** 2025-05-12T14:24:37Z  
**変更:** +1 -0 (1ファイル)  
**マージ日:** 2025-05-12T14:37:33Z  
**内容:**

# 変更の概要
docker compose up の時間を短縮する方法をREADMEに追記

# 変更の背景
docker compose up に時間がかかるため、
UIの軽微な修正を確認したい時など煩雑。

# 関連Issue
なし

# 動作確認の結果
up, down ともに数分かかっていたのが、up が約30秒、　downが1-2秒まで縮まりました。

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [x] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **ドキュメント**
  - 開発者向けセットアップ手順に、`docker compose up` で特定サービスのみを `--no-deps` オプション付きで起動する方法に関する注意書きを追加しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [hide ScatterChart grid lines](https://github.com/digitaldemocracy2030/kouchou-ai/pull/490)

**作成者:** masatosasano2  
**作成日:** 2025-05-12T13:35:18Z  
**変更:** +2 -0 (1ファイル)  
**マージ日:** 2025-05-12T14:09:06Z  
**内容:**

# 変更の概要
ScatterChartのグリッドを非表示にします

# スクリーンショット
<img width="1017" alt="image" src="https://github.com/user-attachments/assets/6d3c3ec9-d4eb-4db9-927f-3acb29a14c8b" />

# 変更の背景
縦軸と横軸に意味があると勘違いさせないため

# 関連Issue
#488 

# 動作確認の結果
上記キャプチャの通りになりました。

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [x] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **スタイル**
  - 散布図チャートのX軸およびY軸のグリッド線が非表示になりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [LocalLLM 接続先の例を修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/485)

**作成者:** shingo-ohki  
**作成日:** 2025-05-12T05:33:37Z  
**変更:** +2 -2 (1ファイル)  
**マージ日:** 2025-05-12T07:01:05Z  
**内容:**

# 変更の概要
- ローカルLLMの接続先の例を修正します

# スクリーンショット
- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください
## 変更前
![Screenshot From 2025-05-12 14-30-38](https://github.com/user-attachments/assets/6374d60b-5de1-4120-8f87-8b051c1dc276)

## 変更後
![Screenshot From 2025-05-12 14-29-54](https://github.com/user-attachments/assets/f2f4e18d-cad7-49c4-8108-c1f5fc4c5a36)


# 変更の背景
#483 を見ると説明がミスリードしているため

# 関連Issue
#483 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->
意図通りに画面上の説明が修正されていることを確認した（上記のスクリーンショット）

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

- **スタイル**
  - LocalLLM接続アドレス入力欄のプレースホルダーを「127.0.0.1:1234」から「ollama:11434」に変更しました。
  - ヘルパーテキストを、OpenAI互換のLLMサーバー（例：ollamaやLM Studio）を指定する詳細な説明に更新し、dockerセットアップ時のアドレス例「ollama:11434」を追加しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [GitHub Pagesで公開する手順のドキュメントを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/480)

**作成者:** mtane0412  
**作成日:** 2025-05-11T06:33:00Z  
**変更:** +98 -0 (2ファイル)  
**マージ日:** 2025-05-11T07:01:23Z  
**内容:**

# 変更の概要
- ホスティングのドキュメント docs/github-pages-hosting.md を追加
- README.mdからドキュメントへのリンクを追加

# 変更の背景
- 静的ホスティングのドキュメントがない
- Github Pagesへのデプロイが可能になった

# 関連Issue
#235
#413 

# 動作確認の結果
検証用リポジトリを新規に作成し、ドキュメント通りにデプロイできることを確認した。
すでにビルドしている場合は再ビルドが必要なのでドキュメントに追加した。

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [x] 単体テストが実装されているか
  - (追記)docsオンリーなので特に実装していないです
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Plotlyのクラスタ名のラベルを改行するように設定した](https://github.com/digitaldemocracy2030/kouchou-ai/pull/476)

**作成者:** tokoroten  
**作成日:** 2025-05-10T16:15:06Z  
**変更:** +79 -9 (1ファイル)  
**マージ日:** 2025-05-11T09:51:17Z  
**内容:**

# 変更の概要
- plotlyで表示されるラベルの横幅を設定可能にした

# スクリーンショット

## Before
![image](https://github.com/user-attachments/assets/551c1795-57d2-4b7a-8369-5ebde2de3db9)

## After

![image](https://github.com/user-attachments/assets/5973c83c-39aa-49ea-8e0b-bfba77ffa020)

# 変更の背景
- ラベルが横長で、クラスタをはみ出してラベルが伸びているせいで「クラスタ感」が出にくかった

# 関連Issue

#121


# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [x] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - 散布図チャートのクラスタラベルに最大幅を指定できるオプションを追加し、ラベルの自動改行表示に対応しました。
  - クラスタラベルの注釈に半透明背景と整ったスタイルを適用し、視認性を向上させました。
  - クラスタラベルの背景角を丸くするなど、注釈の見た目をさらに改善しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [ローカルLLMを利用するための ollama コンテナを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/468)

**作成者:** shingo-ohki  
**作成日:** 2025-05-09T00:09:36Z  
**変更:** +77 -4 (5ファイル)  
**マージ日:** 2025-05-09T13:22:28Z  
**内容:**

# 変更の概要
- ローカルLLM用に ollama コンテナをオプションで起動可能にします（docker compose up 実行時に、 --profile ollama を指定したときのみ起動)
- 起動時にデフォルトでモデル `hf.co/elyza/Llama-3-ELYZA-JP-8B-GGUF`を読み込むようにしました（ここは全く知見がないので、適切なものがあればご指摘下さい）
- README に手順を追加

# 変更の背景
#422  でローカルLLMを使用可能にする機能が実装され、その機能を簡単に利用するためには、その実行環境を簡単に構築できた方がよい

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/430

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - GPU搭載マシン向けのローカルLLM（Ollama）サービスをDocker Composeに追加しました。
  - ローカルLLM利用方法の詳細な手順をREADMEに追記しました。

- **ドキュメント**
  - READMEにローカルLLMの利用方法や必要環境、注意事項などを追加しました。
  - メタデータファイル設定の説明文の表記を一部調整しました。

- **その他**
  - ローカルLLMサーバーのデフォルトアドレスを「localhost:11434」から環境変数対応の「ollama:11434」に変更しました。
  - 環境変数 `NEXT_PUBLIC_LOCAL_LLM_ADDRESS` を `.env.example` とテスト用 `.env.example` に追加しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [client-build-static実行時にルートに.nojekyllファイルを追加する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/465)

**作成者:** mtane0412  
**作成日:** 2025-05-08T04:13:15Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-05-08T09:24:12Z  
**内容:**

# 変更の概要
- client-build-static実行時にルートに.nojekyllファイルを追加する

# 変更の背景
- Github Pagesにデプロイする際にjeykllで処理されてしまうのを防ぐために.nojekyllが必要
- .nojekyll ファイルをユーザーに手動で追加させるよりもビルド時に作成したほうが罠を踏むのを減らせる
- .nojekyll ファイルがあることで他のホスティングへのデプロイに特に影響はない(はず)
- #235 の着手に先立って.nojekyllをルートに追加する

# 関連Issue
#235 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [APIの依存関係エラーを解決](https://github.com/digitaldemocracy2030/kouchou-ai/pull/463)

**作成者:** nasuka  
**作成日:** 2025-05-08T01:21:36Z  
**変更:** +136 -173 (3ファイル)  
**マージ日:** 2025-05-08T04:34:45Z  
**内容:**

# 変更の概要
* APIビルド時に依存関係でエラーが起きていたので解決
* tenacityがなぜか消えていたので追加

# 関連Issue
close https://github.com/digitaldemocracy2030/kouchou-ai/issues/462

# 動作確認結果
- [x] apiが正常にビルドできることを確認
- [x] 正常にレポート生成ができることを確認

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [fix json import and str format for labeling](https://github.com/digitaldemocracy2030/kouchou-ai/pull/458)

**作成者:** masatosasano2  
**作成日:** 2025-05-07T12:44:22Z  
**変更:** +2 -2 (1ファイル)  
**マージ日:** 2025-05-07T12:47:07Z  
**内容:**

何度も申し訳ありません。#444 の追加修正です。
動作確認後に変更したところでバグを仕込んでしまいました。
改めて最新コードで意図通り動作することを確認いたしました。


**コメント:** なし

---

### [レビューのガイドラインを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/457)

**作成者:** nasuka  
**作成日:** 2025-05-07T12:27:49Z  
**変更:** +26 -0 (2ファイル)  
**マージ日:** 2025-05-09T13:24:09Z  
**内容:**

# 変更の概要
* メンテナー向けのレビューガイドラインを追加
* レビューのトータルコストを下げるために、PRテンプレートに以下を追加
  * レビュー前のチェックリスト
  * `動作確認の結果 ` の項目を追加

# 変更の背景
何がクリアされていればマージしてよいのか、基準が明文化されていないため、レビュー時にメンテナーが判断に迷う場面があった

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/456

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **Documentation**
  - Enhanced the pull request template with sections for documenting test results and a pre-merge checklist to ensure thorough verification.
  - Updated review guidelines to emphasize system improvement over perfection and clarified when to request changes or approve pull requests.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Update review_issue.py: cast issue_number to int](https://github.com/digitaldemocracy2030/kouchou-ai/pull/453)

**作成者:** masatosasano2  
**作成日:** 2025-05-07T10:34:56Z  
**変更:** +1 -0 (1ファイル)  
**マージ日:** 2025-05-07T10:36:27Z  
**内容:**

すみません、 #446 にマージもれがありました。
これがないとactionsが型エラーで落ちてしまい、LLMでのラベル判定がされません。

**コメント:** なし

---

### [事前の合意が必須でない旨を追記](https://github.com/digitaldemocracy2030/kouchou-ai/pull/451)

**作成者:** nasuka  
**作成日:** 2025-05-07T08:01:14Z  
**変更:** +1 -0 (1ファイル)  
**マージ日:** 2025-05-07T08:32:21Z  
**内容:**

# 変更の概要
Issueの仕様策定について、事前の合意が必須でない旨を追記

# 変更の背景
以下の議論を踏まえて反映
https://w1740803485-clv347541.slack.com/archives/C08PTG6QB0V/p1746602668665029

```
コントリビューションのMDを読んでたんですが、
[https://github.com/digitaldemocracy2030/kouchou-ai/blob/5a4754d8cb8e36cefcc33724eb973cdc0800eeaf/CONTRIBUTING.md#%E3%82%B3%E3%83%[…]3%82%BB%E3%82%B9](https://github.com/digitaldemocracy2030/kouchou-ai/blob/5a4754d8cb8e36cefcc33724eb973cdc0800eeaf/CONTRIBUTING.md#%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E8%B2%A2%E7%8C%AE%E3%83%97%E3%83%AD%E3%82%BB%E3%82%B9)
コードの貢献プロセス
数行以上のコードを提供する場合は、実装に着手する前に以下のステップをお願いします：

関連するIssueがない場合は、まず新たにIssueを作成してください
実装計画を投稿し、メンテナや他の開発者からの賛同（リアクション）を得てから着手してください
特に、軽微なバグやUIの修正ではなく、新機能の追加や大規模なアーキテクチャの変更を行う場合には、メンテナーのリアクションを得てから開発に着手してください
AIがコードを吐き出してくれる時代になると、これは何か違うなぁとなってる。これは手でコードを書いている時代の価値観だと思う。
ドラフト状態ではメンテナは自発的なレビューはしない、というのを明言したうえで、AIが吐き出したコードを投げ込んでくれてもいいんじゃないかと思う。

中山心太（tokoroten）
  [16:38](https://w1740803485-clv347541.slack.com/archives/C08PTG6QB0V/p1746603525596589)
この手のルールは、こういう現象↓を防ぐためのものなわけですが、
- クソデカパッチを送ってくる
- 設計方針とあわないので、rejectされる
- パッチを送った人が労力が報われなかったことでアンチになって、燃える
AIで作られたコードの場合、「労力が報われなかった」という感覚にはなりにくいと思うんですよね


Shingo OHKI
  [16:43](https://w1740803485-clv347541.slack.com/archives/C08PTG6QB0V/p1746603796996229)
概ね同意ですが、PR送る側の「労力が報われなかった」という感覚以外に、そのPRをレビューするリソースは必要になるので、「Issue 化されて賛同が得られているものがあればそれが優先される」というのはあってもいいのかもしれません。
```

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [ところてんさんをメンテナーに追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/449)

**作成者:** nasuka  
**作成日:** 2025-05-07T06:35:52Z  
**変更:** +1 -0 (1ファイル)  
**マージ日:** 2025-05-07T06:36:02Z  
**内容:**

# 変更の概要
ところてんさんをメンテナーとして追加

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Feat/evaluation report](https://github.com/digitaldemocracy2030/kouchou-ai/pull/448)

**作成者:** take365  
**作成日:** 2025-05-07T04:30:03Z  
**変更:** +1584 -0 (8ファイル)  
**マージ日:** 2025-05-07T12:23:23Z  
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

### [Labeling prompt improvement](https://github.com/digitaldemocracy2030/kouchou-ai/pull/446)

**作成者:** masatosasano2  
**作成日:** 2025-05-07T01:35:12Z  
**変更:** +45 -34 (1ファイル)  
**マージ日:** 2025-05-07T06:18:21Z  
**内容:**

# 変更の背景
ラベルの自動付与処理のうち、LLMに判定させる箇所の精度が低い。

# 変更の概要
Promptを改善した。

# 検証結果
https://docs.google.com/spreadsheets/d/1XqtM7-eEbcjku2OWjHeD9js-1nHtlNXQY2UMM83ziJo
修正前のpromptと加えて改善傾向にある。

# 関連Issue
#444

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Add provider selection to LLM integration](https://github.com/digitaldemocracy2030/kouchou-ai/pull/422)

**作成者:** shinta.nakayama+Devin  
**作成日:** 2025-05-03T14:54:30Z  
**変更:** +900 -156 (25ファイル)  
**マージ日:** 2025-05-08T00:43:31Z  
**内容:**

# LLM統合へのプロバイダー選択機能の追加

このPRは広聴AIアプリケーションにプロバイダー選択機能を追加し、異なるLLMプロバイダー間で動的に切り替えることを可能にします。

## 変更内容

### バックエンド
- `admin_report.py`スキーマにproviderとlocal_llm_addressフィールドを追加
- `report_launcher.py`にプロバイダー情報を含めるよう更新
- `llm.py`を更新し、環境変数の代わりにproviderパラメータを使用するように変更
- サーバーサイドでのモデル取得機能を追加
- OpenAI SDKを使用したLocalLLMサポートを実装
- パイプラインステップでproviderとlocal_llm_addressパラメータを渡すように修正

### フロントエンド
- プロバイダー選択ドロップダウンを追加
- プロバイダーごとのモデルリストを動的に管理
- LocalLLM用の「モデル取得」ボタンを実装
- WebStorage (localStorage) を使用して設定を保存・読み込み
- LocalLLMプロバイダー選択時にisEmbeddedAtLocalを自動的にチェックし無効化
- **「埋め込み処理をサーバ内で行う」チェックボックスの位置をAIモデルの下に移動**

## Devinセッションへのリンク
https://app.devin.ai/sessions/6ccb4a9b82d7428289074993f6a64371

## リクエスト元
shinta.nakayama@gmail.com


**コメント:** なし

---

### 過去7日間に作成されたPR (10件)

### [[GITHUB_ACTIONS] アサイン状況に合わせてステータスを更新する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/512)

**作成者:** masatosasano2  
**作成日:** 2025-05-13T16:10:53Z  
**変更:** +366 -2 (6ファイル)  
**内容:**

# 変更の概要
GitHub IssuesとGitHub Projectsのステータスフィールドを以下の条件とイベントに基づいて自動的に更新します。
| **条件**  | **トリガー** | **変更後のstatus** |
| ------------- | ------------- | ------------- |
| Status in [`No Status`, `Cold List`, `Need Refinement`, `Ready`]  | Assign | `In Progress` |
| Status = `In Progress` | Unassign | `Ready` |

# 変更の背景
kouchou-ai のIssue数が多く、statusの管理コストが高いため、一部の変更を自動化したい。

# 関連Issue
#425
(後続Issue：#454, #459)

# 実装詳細
- 既存の処理への追加
    - `.github/workflows/assign_bot.yml`：スラッシュコマンドでassign/unassignされたときの設定
- GitHub Actionsワークフローを作成：
    - `.github/workflows/assign_manually.yml`：GitHubのUI上でassign/unassignされたときの設定
    - `.github/workflows/assign_status_sync.yml`：assign/unassignの場合にステータス更新を蹴る設定
    - `.github/scripts/assign_status_sync.py` : 冒頭の条件通りにステータスを更新する処理
    - `.github/scripts/sync_status.py` : ステータス更新の共通処理（#454, #459 で再利用予定）
- GraphQL API でProjectsやIssueの情報を取得　※ REST API はProjectV2に未対応のため
- Tokenは手動発行ではなく GitHub Apps 経由で発行　※ ProjectV2 x GitHub Actions では手動設定で権限付与できないため

# 必要な設定

### OrganizationのGitHub Apps を作成する
- 手順：https://docs.github.com/ja/apps/creating-github-apps/registering-a-github-app/registering-a-github-app
- WebhookはOFF
- Permissions > Organization permissions > Projects > Read and write を指定
- Permissions > Repository permissions > Metadata > Read only を指定
- Permissions > Repository permissions > Actions > Read only を指定
    - 確認メールが届いたら、リンク先でリポジトリを指定して許可
- Install only on this account

### Private Key の発行
- 作成完了画面の指示に従い、続けてGitHub Apps のインストール準備としてprivate keyを発行する
- 手順：https://docs.github.com/ja/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps
- 発行すると、ローカルに秘密鍵（pemファイル）がダウンロードされる

### OrganizationのGitHub Apps をインストールする
- 手順：https://docs.github.com/ja/apps/using-github-apps/installing-your-own-github-app
- General > Generate a new client secret
- Install App > Install (to organization)

### Organization secrets の設定
- Organization の設定ページを開く
- Repository > Settings > General > Security > Secrets and variables > Actions > Organization secrets
- PJ_APP_ID : AppのGeneralタブのApp ID
- PJ_APP_PEM : private key を発行した際にローカルにダウンロードされたpemファイルの内容（テキスト全体）
    - Repository を指定する

# 補足：

- `.github/scripts/sync_status.py` l.10-22 について
    - `digitaldemocracy2030/kouchou-ai` に特化したID等になっている
    - 機密情報ではない
    - 本来は環境設定に持たせる方が綺麗だが、どうせ後続処理もこのリポジトリ独自のルールに則った処理なので、このままにしている
        - もし将来的に他のリポジトリで使い回すようであれば環境変数へ移植するのが望ましい
- **PROJECT_ID** (PVT_xxxx) と **STATUS_FIELD** (PVTSSF_xxxx) の取得方法：
    - https://docs.github.com/ja/graphql/overview/explorer にアクセス
    - Githubアカウントでログイン ※ `digitaldemocracy2030` のメンバである必要がある
    - 以下のクエリを実行:
```
{
  organization(login: "digitaldemocracy2030") {
    projectV2(number: 3) {
      id
      fields(first: 20) {
        nodes {
          ... on ProjectV2SingleSelectField {
            id
            name
          }
        }
      }
    }
  }
}
```

# スクリーンショット

No Status + assigned -> In Progress
<img width="579" alt="image" src="https://github.com/user-attachments/assets/276cb071-900b-4a42-89c8-b514b2c944ae" />

Cold List + assigned -> In Progress
<img width="598" alt="image" src="https://github.com/user-attachments/assets/3fc89e15-5ff1-425c-be73-13ed789ed318" />

In Progress + unassigned -> Ready
<img width="533" alt="image" src="https://github.com/user-attachments/assets/b294c6c9-6a78-4a0b-90f6-4cb096343f82" />

Done + unassigned -> Done
<img width="452" alt="image" src="https://github.com/user-attachments/assets/122d4150-a3f7-4195-9981-c66fbeceb2eb" />

In Progress + assigned -> In Progress
<img width="402" alt="image" src="https://github.com/user-attachments/assets/14bccb34-361e-4046-81e9-5909fea18732" />

assign-bot > assign-status-sync
![image](https://github.com/user-attachments/assets/c5a64086-241c-40b9-b13f-9650630e8cb0)

# 動作確認の結果

- Organization(sasa-test-org)とAppsを作成
- kouchou-aiと同じ名称のステータスをもつプロジェクト（kouchou-ai-copy）を用意
- Assign/unassign に対するステータス変更結果は上記のとおり
    - ログにある通りにステータス値が変わり、カンバンも移動することを確認
    - assign / unassign は手動設定もスラッシュコマンドも両方通ることを確認

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - Issueのアサイン・アサイン解除に連動して、GitHub Project上のステータスを自動で同期する機能を追加しました。
  - 新しいワークフロー「Sync Project Status with Assignees」「Update Issue Status」を追加し、アサインイベント発生時に自動的にステータス更新が実行されるようになりました。
  - アサイン操作に応じてステータスを「in progress」や「ready」に切り替える自動同期スクリプトを導入しました。

- **その他**
  - 必要なPython依存パッケージ（requests 2.25.0以上）を追加しました。
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

### [軸の表示機能を導入: PR:481をベースに本番実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/489)

**作成者:** shinta.nakayama+Devin  
**作成日:** 2025-05-12T13:31:24Z  
**変更:** +433 -19 (11ファイル)  
**内容:**

# 軸の表示機能の導入

PR:481をベースとして、UMAPで次元圧縮されたデータの軸の意味を解析し表示する機能を本番実装しました。

## 変更内容

### サーバーサイド
- `hierarchical_main.py`に新しいステップ`generate_axis`を追加
- 軸生成ロジックを`hierarchical_aggregation.py`から抽出し、`hierarchical_generate_axis.py`として独立させた
- エラーハンドリングとロギングを強化し、本番環境での安定性を向上

### クライアントサイド
- 「LLMが推定した軸を表示」オプションを設定ダイアログに追加
- 軸データが存在する場合のみオプションを表示（後方互換性の確保）
- 軸の表示/非表示を切り替える機能を実装

## テスト方法
1. 新しいパイプラインを実行し、`axis_labels.json`が生成されることを確認
2. クライアント側で軸の表示/非表示が正しく機能することを確認
3. 軸データがない場合、オプションが表示されないことを確認

## 注意点
- PR:481の実験的実装を本番品質に改善
- 警告を修正し、エラーハンドリングを強化
- 後方互換性を確保

Link to Devin run: https://app.devin.ai/sessions/5c5a0406bea940e0aa0a14a4ac6cf01c
Requested by: shinta.nakayama@gmail.com


**コメント:** なし

---

### [デザイン変更: セグメントビューでの全体・濃い意見・階層の切り替え機能](https://github.com/digitaldemocracy2030/kouchou-ai/pull/487)

**作成者:** nsk.smn+Devin  
**作成日:** 2025-05-12T06:27:57Z  
**変更:** +178 -71 (5ファイル)  
**内容:**

# デザイン変更: セグメントビューでの全体・濃い意見・階層の切り替え機能

## 変更内容
- セグメントビューを使用して全体・濃い意見・階層のビュー切り替え機能を実装
- 新しいカスタムアイコンを作成（全体、濃い意見、階層）
- Chakra UIのカラーパレット（gray.100, gray.200, gray.500）を使用
- モバイル表示では縦積みレイアウトに対応
- デスクトップ表示では横並びレイアウトに対応

## デザイン意図
- 「ビューの切り替え機能」だと伝えるためにセグメントビューに変更
- 「当たり前に押す機能」としてアピールするため中央配置 & やや大きめサイズ
- 本プロダクトのキモとなる機能のため1つ1つを主張させるためアイコンで表現

## 実装詳細
- Chakra UIのsegmented-controlコンポーネントを使用
- カスタムアイコンを新規作成
- レスポンシブデザインに対応（モバイルでは縦積み、デスクトップでは横並び）

Link to Devin run: https://app.devin.ai/sessions/8b3acd70772247219783e236a211bc16
Requested by: nsk.smn@gmail.com


**コメント:** なし

---

### [[FEATURE] OpenRouterを使えるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/486)

**作成者:** takumi19910112  
**作成日:** 2025-05-12T06:04:35Z  
**変更:** +477 -50 (11ファイル)  
**内容:**

# 変更の概要
- LLMプロバイダー（OpenRouter）の切り替え・設定機能の追加
- OpenRouter利用時、クライアント側でgpt-4o, 4o-mini、gemini2.5系を選択肢として表示し、ラベルも分かりやすく整理

# スクリーンショット
- OpenAIのAPIキーを一旦抜いて、OpenRouterで確実に動いていることを確認
- レポート出力も、OpenRouter経由であることを明記されている
- 選択肢も、ISSUEに載っているモデルが載っていること
<img width="1199" alt="スクリーンショット 2025-05-12 10 49 12" src="https://github.com/user-attachments/assets/9ed66338-2910-4823-9b06-eaf2be85efa2" />

<img width="1077" alt="スクリーンショット 2025-05-12 10 50 28" src="https://github.com/user-attachments/assets/35a4572e-205f-4865-897e-ab6e88ca6ab6" />

<img width="1066" alt="スクリーンショット 2025-05-12 16 47 43" src="https://github.com/user-attachments/assets/837c587e-612e-4e92-ad6f-59a115e98b55" />

<img width="1252" alt="スクリーンショット 2025-05-12 21 20 53" src="https://github.com/user-attachments/assets/3e6551fd-871c-41f8-8986-62a7dea9d05c" />



# 変更の背景
- OpenAIのみ依存ではなく、複数のLLMプロバイダーを柔軟に選択できるようにすることで、利用制限やコスト、用途ごとの最適化に対応するため


# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/402

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->
- レポート作成画面で、OpenRouterのAPIが使用できることを確認
- （念の為OpenAIのAPIキーを無効にした状態で）OpenRouterのAPI経由でモデルを呼び出して分析するように設定
- レポートの作成をする
- クライアント側の画面で、分析詳細を確認して、OpenRouterで分析していることを確認
- OpenAIのAPIキーを使って、OpenAIによる分析も、問題なくできることを確認
- （レビューしてくださる方へ）
- OpenRouterの検証の際に、私が開発で使ったAPIキーが、あと数ドル分残っています。もし検証時にAPIキーがない場合は、私のAPIキーを共有しますのでご連絡ください。（APIキーは上限金額を設定して、共有可能なものです）

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
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
  - OpenRouterを含む複数のLLMプロバイダー（OpenAI、Azure、Local LLM、OpenRouter）のサポートを追加しました。
  - 管理画面からAIプロバイダーやモデルを選択できるようになりました。
  - OpenRouter用のAPIキーやエンドポイント設定が可能になりました。
  - LLMプロバイダー接続確認用の管理APIエンドポイントを追加しました。

- **改善**
  - AI設定画面のアクセシビリティが向上しました（ラベルや説明の追加）。
  - モデル選択時、OpenRouterのモデル名が分かりやすく表示されます。
  - プロバイダーごとに利用可能なモデル一覧が取得・表示されるようになりました。
  - 処理結果の説明文に利用プロバイダー名が動的に反映されます。
  - 設定情報の受け渡しやプロバイダー指定の一貫性を強化しました。
  - JSONレスポンスのバリデーションが強化され、余分なフィールドが禁止されました。

- **バグ修正**
  - 設定情報の受け渡しやプロバイダー指定の一貫性を改善しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Feature/openrouter llm main202406](https://github.com/digitaldemocracy2030/kouchou-ai/pull/484)

**作成者:** takumi19910112  
**作成日:** 2025-05-12T04:20:24Z  
**変更:** +510 -173 (17ファイル)  
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

**コメント:** なし

---

### [[FEATURE] OpenRouterを使えるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/482)

**作成者:** takumi19910112  
**作成日:** 2025-05-12T03:06:14Z  
**変更:** +510 -173 (17ファイル)  
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

**コメント:** なし

---

### [[WIP] [実験]軸の性質を推定し、プロット時に軸情報を表示する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/481)

**作成者:** tokoroten  
**作成日:** 2025-05-11T16:32:03Z  
**変更:** +268 -18 (6ファイル)  
**内容:**

これは実験です、現状の設計を無理くり改造して実装しているので、絶対にマージしてはいけません。

# 変更の概要
TTCの時も、横軸と縦軸は何なのか？というのを尋ねられることが多かった。
いっそのこと、LLMに横軸と縦軸が何なのかを推定させてしまえばよいじゃないか、という実験

# スクリーンショット
![](https://github.com/user-attachments/assets/47654f82-d0e8-4f8a-8873-d90a358abb36)


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - 散布図チャートにX軸・Y軸の名称および最小・最大ラベルが表示されるようになりました。
  - 軸ラベルや最小・最大値ラベルがチャート内に明示的に表示され、軸の可読性が向上しました。

- **改善**
  - チャートの余白が拡大され、軸ラベルの表示が見やすくなりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [自動静的ファイル生成機能の実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/469)

**作成者:** shinta.nakayama+Devin  
**作成日:** 2025-05-10T01:17:09Z  
**変更:** +561 -1 (12ファイル)  
**内容:**

# 自動静的ファイル生成機能の実装

## 概要
レポート生成完了時に自動的に静的ファイルを生成し、管理画面からダウンロードおよび外部サービスへのデプロイを可能にする機能を実装しました。

## 変更内容
1. **自動静的ファイル生成**
   - レポート生成完了時に入力データサイズを確認し、10,000件以下の場合は自動的に静的ファイルを生成
   - 10,000件を超える場合は手動での生成が必要（リソース消費を抑制するため）

2. **管理画面からのダウンロード機能**
   - 個別レポートの静的ファイルをダウンロードするボタンを追加
   - 全レポートのエクスポート機能は既存のまま維持

3. **外部ホスティングサービスとの連携**
   - Netlifyへのワンクリックデプロイ機能
   - Vercelへのワンクリックデプロイ機能
   - **セキュリティ強化**: 外部ホスティング環境変数が設定されている場合のみデプロイボタンを表示

## 技術的な詳細
- `report_launcher.py`に入力データサイズに基づく条件分岐を追加
- `client-static-build`サービスに個別レポート生成エンドポイントを追加
- 管理画面に静的ファイルダウンロードボタンとデプロイボタンを追加
- Netlify/Vercel APIとの連携機能を実装
- セキュリティ対策として、環境変数が設定されている場合のみデプロイボタンを表示

## 環境変数
以下の環境変数を追加しました：
- `NETLIFY_AUTH_TOKEN`: Netlifyへのデプロイに必要なAPIトークン
- `VERCEL_AUTH_TOKEN`: Vercelへのデプロイに必要なAPIトークン

## ドキュメント
- 外部ホスティングサービスとの連携方法について詳細なドキュメントを追加しました: [docs/external-hosting.md](https://github.com/digitaldemocracy2030/kouchou-ai/blob/devin/1746839287-auto-static-file-generation/docs/external-hosting.md)
- README.mdに静的ファイルの自動生成と外部ホスティングに関する情報を追加しました

## テスト方法
1. レポートを生成し、完了後に自動的に静的ファイルが生成されることを確認
2. 管理画面から個別レポートの静的ファイルをダウンロードできることを確認
3. Netlify/Vercelへのデプロイ機能をテスト（APIトークンの設定が必要）

## セキュリティに関する注意点
- 外部ホスティング機能は、環境変数（NETLIFY_AUTH_TOKEN、VERCEL_AUTH_TOKEN）が設定されている場合のみ表示されます
- これにより、機密性の高い環境（行政機関など）での利用時に情報漏洩の懸念を防止します
- APIエンドポイントでも環境変数のチェックを行い、未設定の場合はエラーを返します

Link to Devin run: https://app.devin.ai/sessions/72e098f3de7a4fbc997537a270e2fb9a
Requested by: shinta.nakayama@gmail.com


**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(3件)

### [Client-AdminにChatGPTのAPIKeyの確認画面の追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/421)

**作成者:** tokoroten  
**作成日:** 2025-05-03T13:19:34Z  
**変更:** +216 -4 (3ファイル)  
**内容:**

# 変更の概要
- 管理画面の追加
- とりあえずOpenAIのAPIを一発叩いてみて、動作確認
- エラーが出たら、エラーを分かりやすく表示

# スクリーンショット
![image](https://github.com/user-attachments/assets/f4e0a02b-3fb1-4e3d-9eed-c624273ec0cb)
![image](https://github.com/user-attachments/assets/5193c5bc-5ea3-4740-aeca-22ab50a27dce)
![image](https://github.com/user-attachments/assets/e6c4a57d-86fa-4bce-809e-3e59aee058af)


# 変更の背景
- envでAPIKeyが正しく設定されているか分からない
- APIのデポジットに正しくチャージされているか分からない

# 関連Issue

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [管理画面の基本e2eテスト実装の簡素化](https://github.com/digitaldemocracy2030/kouchou-ai/pull/407)

**作成者:** NISHIO Hirokazu+Devin  
**作成日:** 2025-05-01T06:00:01Z  
**変更:** +224 -746 (15ファイル)  
**内容:**

## 概要
Issue #396 に関連する管理画面の基本e2eテスト実装を簡素化しました。

## 変更内容
- 複雑なセレクタ戦略を単純化し、より信頼性の高いセレクタを使用
- h1セレクタをh2セレクタに修正（実際の要素に合わせて）
- introFieldセレクタの問題を修正
- デバッグコードとエラーハンドリングを簡素化
- テストコードの可読性を向上

## テスト方法
```bash
cd test/e2e
npm install
npx playwright install
npx playwright test
```

## 関連Issue/PR
- Issue #396: 管理画面の基本e2eテスト計画
- PR #397: 以前の実装

## Link to Devin run
https://app.devin.ai/sessions/53ea0979f0964bd8bd60bed07ff7fe12

## Requested by
NISHIO Hirokazu (nishio.hirokazu@gmail.com)


**コメント:** なし

---

### [Issue #396: 管理画面の基本e2eテストを実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/397)

**作成者:** NISHIO Hirokazu+Devin  
**作成日:** 2025-04-30T01:58:00Z  
**変更:** +657 -13 (2ファイル)  
**内容:**

# 管理画面の基本e2eテスト実装

Issue #396 に基づいて、管理画面の基本的なエンドツーエンドテストを実装しました。このテストでは、以下の基本的なワークフローをテストします：

1. 管理画面へのアクセスとログイン（Basic認証）
2. レポート作成ページへの移動
3. 基本情報の入力
4. CSVファイルのアップロード
5. レポート作成の実行と成功確認

## 変更内容
- `test/e2e/tests/admin/create-report.spec.ts` ファイルを更新し、テストを実装
- 既存のページオブジェクトとユーティリティを活用

## テスト方法
テストを実行するには以下のコマンドを使用します：
```
cd test/e2e
npm test
```

Link to Devin run: https://app.devin.ai/sessions/1883f9aaaede4ddab11a25bbbde4d8bc
Requested by: NISHIO Hirokazu (nishio.hirokazu@gmail.com)


**コメント:** なし

---

