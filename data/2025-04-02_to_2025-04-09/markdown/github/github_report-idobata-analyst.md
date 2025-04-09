# GitHub レポート: digitaldemocracy2030/idobata-analyst

期間: 2025-04-02 から 2025-04-09 まで

## Issues

### 過去7日間に完了されたissue (1件)

### [Biomeをrootで実行できるようにする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/90)

**作成者:** takker99  
**作成日:** 2025-03-31T04:09:52Z  
**内容:**

## 解決・改善したいこと

[VS codeのBiome拡張機能](https://marketplace.visualstudio.com/items?itemName=biomejs.biome)でformatしようとしたら、biomejsがないと警告が出てしまいました。
[![Image from Gyazo](https://i.gyazo.com/9582ed8fd457ebbde8b53a7c389ec247.png)](https://gyazo.com/9582ed8fd457ebbde8b53a7c389ec247)
コードを見てみると、`packages/*/package.json`には`@biomejs/biome`が入っているものの、ルートには入っていないため、ルートでbiomeを探せずエラーが出ていたみたいです。
[![Image from Gyazo](https://i.gyazo.com/c46bf0183bbf4de9223b7f4b80566cdd.png)](https://gyazo.com/c46bf0183bbf4de9223b7f4b80566cdd)

初めての人でも躓かないよう、(vscode限定ですが)biomeをすぐ動かせるような状態にしたいです。

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

- npm workspaceを導入し、root directoryで`@biomejs/biome`を入れる
- すべてのpackagesのlintとformatを実行するnpm scriptsをroot directoryに導入
- 開発に使う拡張機能を`extensions.json`に入れる

**コメント:** なし

---

### 過去7日間に作成されたissue (5件)

### [プロジェクトレポートの分析に失敗したとき、失敗理由を表示したい](https://github.com/digitaldemocracy2030/idobata-analyst/issues/105)

**作成者:** takker99  
**作成日:** 2025-04-06T06:51:58Z  
**内容:**

## 解決・改善したいこと

「プロジェクトレポートの分析に失敗しました」などと出ますが、理由が示されていなくて戸惑いがちです。

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

- 失敗理由を出せるなら出したい
  - APIの認証が通らなかった
  - ネットワークがつながらなかった
  - frontend/backendのコードのバグ
  - etc.
- 失敗理由を出せないなら、よくある失敗例みたいなのを出して、開発者のガイドとなるようにしたい

**コメント:** なし

---

### [動作確認用サンプルデータの改善](https://github.com/digitaldemocracy2030/idobata-analyst/issues/100)

**作成者:** spinute  
**作成日:** 2025-04-05T17:11:31Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->

https://github.com/digitaldemocracy2030/idobata-analyst/pull/93 と https://github.com/digitaldemocracy2030/idobata-analyst/pull/94 でサンプルデータを簡単に入れられるようにした。

しかし、サンプルデータが適当過ぎて、分析結果画面のリアリティがあまりない（立場のグラフや抽出された意見の多様性が乏しい等）

またサンプルデータをランダムに作っているが、ランダムだとキャッシュが当たらず https://github.com/digitaldemocracy2030/idobata-analyst/issues/63 の恩恵をあまり受けられない

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

リアリティあるシナリオを想定し、それっぽいコメントデータを作成し、テストデータとして使えるようにする

適当な LLM に想定シナリオを伝えてそれっぽいデータを作ってもらうと良さそう（例えば安野さんの動画ピックし、その内容を伝えて、論点と立場をたくさん列挙してもらった上で、各論点各立場とノイズが入り乱れたコメントを AI に指示して作らせる等）

**コメント:** なし

---

### [コメント一覧を出力できるようにすることで、自前でテストできるようにする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/98)

**作成者:** itoma-aikon  
**作成日:** 2025-04-04T12:13:18Z  
**内容:**

## 解決・改善したいこと

コメント一覧を出力できるようにしたら、何かと自前でできて便利そう


## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### [deep search的な機能によってファクトチェックする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/97)

**作成者:** Ina299  
**作成日:** 2025-04-02T10:05:56Z  
**内容:**

## 解決・改善したいこと

discourse上でファクトを確かめるための機能の実装

**コメント:** なし

---

### [ビジュアル分析のモバイル表示対応](https://github.com/digitaldemocracy2030/idobata-analyst/issues/96)

**作成者:** spinute  
**作成日:** 2025-04-02T08:33:22Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->

ビジュアル分析タブのレポートがモバイル端末の横幅が狭い画面で表示することをおそらく表示しておらず、読みにくい。

今の日本のインターネット利用は PC よりスマホが中心で、スマホで快適に閲覧できることは重要。

![Image](https://github.com/user-attachments/assets/00325e8f-03a3-4f6b-9446-a173b1e70ff2)

https://github.com/digitaldemocracy2030/idobata-analyst/pull/89 で余白を詰めてみたが、まだまだレイアウト的に見づらい。

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

ビジュアル分析のレポートをモバイル端末での表示を意識してリデザインし、実装する。

表面的なところでは、字下げと2カラム表示が縦長で横幅の狭いスマホ表示には向いていない気がする。ただ、別のやり方も色々ありそう。

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(8件)

### [ビジュアル分析をシェアしやすいUIにすることで、良い分析をみた参加者が画像とURLをSNSで共有しやすくする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/81)

**作成者:** itoma-aikon  
**作成日:** 2025-03-27T06:35:38Z  
**内容:**

## 解決・改善したいこと
投稿:314 いいね数5の投稿の分割
- XなどSNSで投稿しやすいように、画像としてダウンロードするボタンを作る:
   - 一定の長さで縦n分割にしてダウンロードするボタンを作るとさらに良さそう

https://large-scale-conversation-sandbox.discourse.group/t/topic/45/50

## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### [チャットの履歴を保存できるようにすることで、参加者がより継続的に深く論点に対しての理解を深められるようにする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/77)

**作成者:** itoma-aikon  
**作成日:** 2025-03-27T01:55:47Z  
**内容:**

## 解決・改善したいこと
投稿:mango いいね数3の投稿
チャットでAIと議論してみました。
議論に終わりがないので中断して翌日再開、が出来ると良いと思いました。現状ではブラウザを開いたまま残すしかなさそうです。
マイページ(自分の投稿)から履歴呼び出せるといいですね。
https://large-scale-conversation-sandbox.discourse.group/t/topic/45/30
投稿:mango いいね数0の投稿
一晩経ったら画面の接続が切れ、仕方なく再読み込みしたら会話履歴が消えてしまいました。また1から話すのは辛いです。
https://large-scale-conversation-sandbox.discourse.group/t/topic/45/37
投稿:akinori いいね数2の投稿の分割
ブラウザ操作での再読み込みは禁止する方法があってもいいかもしれないですね。
https://large-scale-conversation-sandbox.discourse.group/t/topic/45/38


## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### [GitHub Actions で test, linter を実行するようにすることで、開発者が安心してコードの品質を高く保てるようにする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/71)

**作成者:** spinute  
**作成日:** 2025-03-23T12:11:05Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->

CI で test, linter を実行し、スタイルやコード品質のベースラインをキープできるようにしたい。

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

- PR に対し、frontend, backend, chat-bot それぞれについて、linter を走らせ、テストを実行する GitHub Actions を定義する

**コメント:** なし

---

### [AIのレスポンスをキャッシュするようにすることで、開発時の動作確認で AI 費用がなるべくかからないようにする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/63)

**作成者:** spinute  
**作成日:** 2025-03-23T06:21:16Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->

開発中に繰り返し動作確認することになるが、OpenRouter API 叩くたびに課金され、お財布に優しくないかも。

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

ref: https://w1740803485-clv347541.slack.com/archives/C08FL58M3D3/p1742708110238619

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

実現方法は例えば以下：

- OpenRouter のレスポンスをキャッシュする仕組みを作る
    - ⭕️汎用な仕組みなので動作確認以外の場所でも恩恵を受けられる
    - ❌️費用はゼロにはならない
- 動作確認用の小さなデータを作る
    - ⭕️データ量と費用が概ね比例するので、小さいデータなら単価が安くなる
    - ❌️データが小さいと結果が面白くなくなったり動作確認力が下がったりする
    - ❌️リクエストのたびに小さいながらコストは発生する
- 動作確認用のデータだけは事前に取得済みのデータを埋め込んでおいて、OpenRouter API をバイパスして元々あるデータを使ってしまうようにする
    - ⭕️（動作確認の範囲では）コスト0になる
    - ⭕️キーなしでも最小限動かせるようになる（フロントエンドだけ触る人とかの入門ハードルが下がる）
    - ❌️データ更新やバイパス処理が入ってメンテナンス性が下がる

おそらく1つ目のものがメリット大きく負債にもなりにくそうで筋が良さそう。

https://github.com/digitaldemocracy2030/idobata-analyst/blob/main/packages/backend/src/services/openRouterService.ts に OpenRouter へのリクエストは集約されているので、ここにキャッシュ機構をうまく挟めば良さそう。

副次的なメリットとして、API 叩く回数が減れば処理もかなり早くなるので開発効率も良くなる。

**コメント:** なし

---

### [extractionフェーズで過度な捨象が発生してしまうのを避けたい](https://github.com/digitaldemocracy2030/idobata-analyst/issues/39)

**作成者:** blu3mo  
**作成日:** 2025-03-17T00:40:13Z  
**内容:**

## 解決・改善したいこと
- extractionフェーズで過度な捨象が発生してしまうのを避けたい。
例：
![Image](https://github.com/user-attachments/assets/30ac4f8d-ba41-4ea6-baec-c57a9114dd7d)
> 安野貴博
  9:28 AM
extractionフェーズで過度に捨象されている例。このぐらいの文量ならまるめなくてもいいようなきがする


## 具体的な実現方法・実装方法の概要（未記入でも構いません）
- プロンプトを修正して過度な捨象を避ける
  - 「適切なextraction」の定義が難しいが、少なくとも現状は捨象しすぎだと思う。特に、主張を抽象化してしまうことで元投稿が言ってないことまでextraction後に書かれてしまうのは望ましくないと思う。

**コメント:** なし

---

### [コメント数が0件の論点について、0件である旨を表示することで、ユーザーが無駄に読み込みを待ってしまうことを防ぐ](https://github.com/digitaldemocracy2030/idobata-analyst/issues/20)

**作成者:** blu3mo  
**作成日:** 2025-03-12T02:15:59Z  
**内容:**

https://large-scale-conversation-sandbox.discourse.group/t/topic/76/34

これはそもそも論点にヒットしているコメントが0件なのが問題ですね。
コメントが存在しないのでグラフも当然表示されない。

コメント数0件の時に円グラフを空っぽにするのではなく、「コメント数が0件です」と表示する、あるいは論点をそもそも表示しないようにしたい。後者の方が良いかも？

**コメント:** なし

---

### [コメントの左側のバーの色を、各立場（スタンス）に対応する円グラフの色と一致させることで、読み手が理解しやすくする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/15)

**作成者:** blu3mo  
**作成日:** 2025-03-12T02:08:13Z  
**内容:**

---
• <https://delib.takahiroanno.com/projects/67c7c8cd858bc4c6ea297050/analytics|論点ごとの分析ページ>にて、「円グラフの色」と「コメントの左についているバーの色」を一致させられると見やすそう。
    ◦ 今は「コメントの左についているバーの色」は全部青になっているが、これを「円グラフの色」の青緑橙と一致させたい。
    ◦ フロントエンドだけ触れば対応できる

![Image](https://github.com/user-attachments/assets/b11cf0e2-c381-411a-9fb2-3ff1d56e97b0)

**コメント:** なし

---

### [全体レポートにmarkdownと出てしまうのを修正し、読み手の違和感を防ぐ](https://github.com/digitaldemocracy2030/idobata-analyst/issues/10)

**作成者:** blu3mo  
**作成日:** 2025-03-12T01:36:49Z  
**内容:**

markdownって出ちゃう
https://delib.takahiroanno.com/projects/67b88d408b236a3238bb11a7/overall

![Image](https://github.com/user-attachments/assets/d43bb596-6ac8-4e7f-9ca8-d785a86f9c92)

これの問題は、LLMが

<img width="146" alt="Image" src="https://github.com/user-attachments/assets/96c5c1b4-e464-4357-95ac-a86bf2d89805" />

という文章を生成した時に、自動的に``` ```の部分だけ排除して、"markdown"の部分を排除してくれないこと。
markdownという文字も出力されてしまったパターンにも対応できるようにregexとかを調整できると良さそう。あるいはgeminiのapiで出力フォーマットを指定できるっぽいので、それを導入すべきかもしれない。

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (7件)

### [CSV プレビューの小さなバグ修正](https://github.com/digitaldemocracy2030/idobata-analyst/pull/95)

**作成者:** spinute  
**作成日:** 2025-04-02T08:03:07Z  
**変更:** +10 -3 (1ファイル)  
**マージ日:** 2025-04-02T12:52:05Z  
**内容:**

# 変更の概要
CSV のプレビュー時に出るデータ件数表示が変だったので修正した
- 常に1件と表示されてしまっていた
    - preview: 1 が付いていて、1行しかデータを読み出していないにも関わらず、データの件数を表示していたので変になっていた
    - CSVのパースには100万行〜規模のデータでもなければ今どきの PC では大した時間はかからないはずなので、preview: 1 を外してしまうことにした
- CSV を読み込む際に、末尾の空行が含まれてデータの件数が1件ずれてしまうことがあった（CSV ファイルの作り方によって、末尾に空行が入ることと入らないことがあり、末尾に空行が入る時のみ問題が発生する）
    - 空行はフィルタリングするようにして、実際のデータ数と表示数がずれないようにした

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [開発環境でサンプル CSV を読み込めるボタンを置いた](https://github.com/digitaldemocracy2030/idobata-analyst/pull/94)

**作成者:** spinute  
**作成日:** 2025-04-02T07:55:39Z  
**変更:** +373 -0 (2ファイル)  
**マージ日:** 2025-04-02T12:53:40Z  
**内容:**

# 変更の概要
- 開発環境でプロジェクト作成時に、サンプル CSV を読み込めるボタンを置いた
- サンプル CSV ファイルを作成して置いた
    - Slack で動作確認用に置いてあったダミーデータをレポジトリに置いていいかどうか少し迷ったので、ChatGPT にダミーデータを作らせた https://chatgpt.com/share/67ececb7-a83c-8006-9b6e-e9daf3a22722
    - https://github.com/digitaldemocracy2030/idobata-analyst/pull/93 で出てくるテーマと関連するテーマのコメントを生成している

![Screenshot 2025-04-02 at 17 09 49](https://github.com/user-attachments/assets/839b05bd-1dd2-4861-b53d-7f6449d875af)

件数表示が変だけどこれは既存のバグっぽいので https://github.com/digitaldemocracy2030/idobata-analyst/pull/95 で修正

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [開発環境で、プロジェクト作成ページにサンプルデータを入れるボタンを置いた](https://github.com/digitaldemocracy2030/idobata-analyst/pull/93)

**作成者:** spinute  
**作成日:** 2025-04-02T07:09:33Z  
**変更:** +28 -0 (1ファイル)  
**マージ日:** 2025-04-02T12:53:41Z  
**内容:**

# 変更の概要
- 開発環境で、プロジェクト作成ページにサンプルデータを入れるボタンを置いた

# 変更の背景
- 開発時に動作確認のために適当なデータを毎回入力するのが面倒だった
- ボタンクリックするとサンプルデータが入るようにした
- 
![Screenshot 2025-04-02 at 16 09 11](https://github.com/user-attachments/assets/661369eb-09d2-4a6b-be99-8b6d3f003da5)

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Enable to run biome at the root directory](https://github.com/digitaldemocracy2030/idobata-analyst/pull/91)

**作成者:** takker99  
**作成日:** 2025-03-31T04:23:57Z  
**変更:** +13636 -7489 (11ファイル)  
**マージ日:** 2025-04-02T12:56:35Z  
**内容:**

# 変更の概要
Fix #90
- rootで`npm install`すればbiomeの拡張機能に認識してもらえるようにする (https://github.com/digitaldemocracy2030/idobata-analyst/pull/91/commits/20d1fe15456042e68e69e77b10bdb04c9aeb8557)
- すべてのpackagesとルートにあるファイルをformat & lintするコマンドを追加 (https://github.com/digitaldemocracy2030/idobata-analyst/pull/91/commits/c54eec53af02e3b6576647f33808f992f538f7f1)
  - この過程で`mongo-init.js`がformatされてないことに気づいたのでやっておきました (https://github.com/digitaldemocracy2030/idobata-analyst/pull/91/commits/521b2b593a8464e84d1a2bb2cef3e6f618c05f98)
- biomeの拡張機能をinstallするよう促す (https://github.com/digitaldemocracy2030/idobata-analyst/pull/91/commits/52c71399b7ae85ef9a149d63f6439a3d7d281721)

本当は`npm install`も拡張機能を入れるのも自動で済ませたいところですが、devcontainerを導入しないとそこまではできないので、いったんこれでPRします。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [make containers-start の微修正](https://github.com/digitaldemocracy2030/idobata-analyst/pull/88)

**作成者:** spinute  
**作成日:** 2025-03-29T06:49:37Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-04-02T12:54:40Z  
**内容:**

# 変更の概要

- https://github.com/digitaldemocracy2030/idobata-analyst/pull/66 で makefile を追加したが、make containers-start を実行したときに `docker compose watch` を実行するようにしていたが、これだとコンソールにログが出ないので、`docker compose up --watch` を実行するように修正した

# 変更の背景
- ここに変更が必要となった背景を記載してください

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [improve copy-env.sh](https://github.com/digitaldemocracy2030/idobata-analyst/pull/64)

**作成者:** spinute  
**作成日:** 2025-03-23T11:29:12Z  
**変更:** +15 -3 (1ファイル)  
**マージ日:** 2025-04-02T12:55:21Z  
**内容:**

# 変更の概要
- https://github.com/digitaldemocracy2030/idobata-analyst/pull/48 で導入された copy-env.sh を改善した

# 変更の背景
- .env を既に作っているとき、copy-env.sh を実行すると既存のファイルが上書きされてしまう問題があった
- 既に .env があるときはおそらく copy-env.sh の実行はミスの可能性が高いので、上書きはせずに警告を表示するようにした

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [修正：issues19(コメント種類分布の追加)の解決](https://github.com/digitaldemocracy2030/idobata-analyst/pull/62)

**作成者:** itoma-aikon  
**作成日:** 2025-03-23T06:05:47Z  
**変更:** +27 -0 (1ファイル)  
**マージ日:** 2025-04-02T12:55:36Z  
**内容:**

# 変更の概要
- issues19(コメント種類分布の追加)の解決

# 変更の背景
- (https://github.com/digitaldemocracy2030/idobata-analyst/issues/19)の解決

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### 過去7日間に作成されたPR (5件)

### [Run lint and test on push and pull request](https://github.com/digitaldemocracy2030/idobata-analyst/pull/104)

**作成者:** takker99  
**作成日:** 2025-04-06T06:25:53Z  
**変更:** +43 -18 (3ファイル)  
**内容:**

# 変更の概要
- Fix #71

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [[WIP] コメントが過度に捨象されてしまう問題を緩和した](https://github.com/digitaldemocracy2030/idobata-analyst/pull/103)

**作成者:** spinute  
**作成日:** 2025-04-05T19:08:43Z  
**変更:** +100 -30 (9ファイル)  
**内容:**

# 変更の概要
- XXX: 実装途中
- https://github.com/digitaldemocracy2030/idobata-analyst/issues/39#issuecomment-2781040496 の実装
- stance-analysis 時に、論点・立場に関するコメントを改めて抽出させるようプロンプトを変更した
- 「論点ごとの分析」「コメントの一覧」に表示しているコメントを、このコメントに置き換えた
- コメントが加工されたものであることがより明確になるよう、「原文を表示」というボタンを置いた
    - 元の hover で原文が表示される機能も残している。hover だけだと気づきにくく、またスマホで操作しづらいのでボタンも置くのが良さそう

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [ディスプレイの大きさに合わせてページ幅を広げるようにした](https://github.com/digitaldemocracy2030/idobata-analyst/pull/102)

**作成者:** spinute  
**作成日:** 2025-04-05T19:01:54Z  
**変更:** +8 -8 (6ファイル)  
**内容:**

# 変更の概要
- 最大コンテンツ幅 4xl で固定されていたが、ディスプレイが大きいときに余白が無駄に広くなってしまうため、ディスプレイ幅の90%を最大コンテンツ幅に定義し直した

before

![Screenshot 2025-04-06 at 4 01 30](https://github.com/user-attachments/assets/b25c33b1-b443-48f8-ba1c-673d94ebcaa3)

after

![Screenshot 2025-04-06 at 4 00 43](https://github.com/user-attachments/assets/a6ca6a32-2843-421c-a021-c1e7cbf7aab6)

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [[WIP] implement cacheService and use it in openRouterService](https://github.com/digitaldemocracy2030/idobata-analyst/pull/101)

**作成者:** spinute  
**作成日:** 2025-04-05T18:54:56Z  
**変更:** +122 -1 (2ファイル)  
**内容:**

# 変更の概要
- https://github.com/digitaldemocracy2030/idobata-analyst/issues/63 を実装した
- cacheService を追加した。KVS 的なインターフェース read, write, fetch を実装し、Mongo DB をキャッシュサーバーとして使えるようにした
- openRouterService のリクエストパラメータの digest をキーにして、レスポンスをキャッシュするようにした

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [コメントの左側のバーの色を、各立場（スタンス）に対応する円グラフの色と一致させた](https://github.com/digitaldemocracy2030/idobata-analyst/pull/99)

**作成者:** spinute  
**作成日:** 2025-04-04T16:04:33Z  
**変更:** +50 -22 (2ファイル)  
**内容:**

# 変更の概要
- https://github.com/digitaldemocracy2030/idobata-analyst/issues/15 を実装した
- 円グラフ上の色と、コメントに添える色を一致させるようにした
- 「その他」用の色を導入し、「その他」は常にその色になるようにした

![Screenshot 2025-04-05 at 0 59 54](https://github.com/user-attachments/assets/2bfd9cfa-4db2-4124-ac15-02fc528cae8e)

# 変更の背景

- https://github.com/digitaldemocracy2030/idobata-analyst/pull/37 で同 issue に PR を立てていただいていたが、https://github.com/digitaldemocracy2030/idobata-analyst/pull/37#issuecomment-2743121886 が解消されておらず、まだマージできなさそうな状態であった
- 先週の定例の際に状況確認したい旨話が出たので https://github.com/digitaldemocracy2030/idobata-analyst/issues/15#issuecomment-2763375494 や https://w1740803485-clv347541.slack.com/archives/C08FF5MM59C/p1743256551200759 でメンションしてみたものの、お忙しいのか返信いただけていないので、こちらの PR で改めて実装することにした

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(3件)

### [ビジュアル分析タブの余白を調整した](https://github.com/digitaldemocracy2030/idobata-analyst/pull/89)

**作成者:** spinute  
**作成日:** 2025-03-29T13:06:55Z  
**変更:** +43 -32 (4ファイル)  
**内容:**

# 変更の概要
- https://github.com/digitaldemocracy2030/idobata-analyst/issues/72 の対応

# 変更の背景
- ビジュアル分析タブにおいて、特にモバイル端末からの閲覧で横幅が狭く、可読性が非常に低かった
- div の階層を減らしたり、余白を減らしたりした
- ビジュアルレポート本体がそもそもモバイル表示厳しそう（おそらく主に①ネストで余白が深くなっていくのと②2カラム表示の2点）なところもあり、それについてはこの PR では対応しない方針とした
    - https://github.com/digitaldemocracy2030/idobata-analyst/issues/96 に切り出した
- TODO: もう少し動作確認してこの PR を review ready にする

before

![Screenshot 2025-03-29 at 22 04 49](https://github.com/user-attachments/assets/e518affc-8bb1-4d54-b643-8214012b20c0)

after

![Screenshot 2025-03-29 at 22 05 11](https://github.com/user-attachments/assets/a4e45c86-3d1c-4401-9bdb-69a461c0eb20)

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [OpenRouter のクレジットが少なくなってきたらアラートを表示するようにした](https://github.com/digitaldemocracy2030/idobata-analyst/pull/60)

**作成者:** spinute  
**作成日:** 2025-03-22T13:17:14Z  
**変更:** +123 -4 (5ファイル)  
**内容:**

# 変更の概要
- https://github.com/digitaldemocracy2030/idobata-analyst/issues/22 を途中まで実装した
- https://openrouter.ai/docs/api-reference/get-credits を利用し、残クレジットを取得する
- 残りクレジットを取得し、100クレジットを切ったら console.log
    - アラートは1時間に1回までに制限している
    - 多分最終形は Slack 通知になりそうなので、一旦雑なものを出している
- ↑ の console.log を Slack への send に置き換えたい（が、多分 Slack workspace の適切な権限が必要そうなので一旦ここまで）
    - @blu3mo ここ進め方相談したいです！（webhook URL 発行していただき、環境変数経由で入れる→それを受け取って叩くコードを書いておく等...？）

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [コメントの左側のバーの色を、各立場（スタンス）に対応する円グラフの色と一致させることで、読み手が理解しやすくする](https://github.com/digitaldemocracy2030/idobata-analyst/pull/37)

**作成者:** javasparrows  
**作成日:** 2025-03-16T15:03:36Z  
**変更:** +47 -43 (2ファイル)  
**内容:**

# 変更の概要
- コメントの左側のバーの色を各立場（スタンス）に対応する円グラフの色と一致させた

# 変更の背景
- [論点ごとの分析ページにて、グラフとコメントの色をあわせる](https://github.com/takahiroanno2024/idobata-analyst/issues/15)

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ x] CLAの内容を読み、同意しました


**コメント:** なし

---

