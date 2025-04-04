# GitHub レポート: digitaldemocracy2030/idobata-analyst

期間: 2025-03-05 から 2025-04-04 まで

## Issues

### 過去30日間に完了されたissue (24件)

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

### [新規改善提案がProjectに自動で追加されるかテスト](https://github.com/digitaldemocracy2030/idobata-analyst/issues/87)

**作成者:** jujunjun110  
**作成日:** 2025-03-29T05:23:47Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### [ビジュアル分析のリンク追加](https://github.com/digitaldemocracy2030/idobata-analyst/issues/83)

**作成者:** itoma-aikon  
**作成日:** 2025-03-27T06:38:35Z  
**内容:**

## 解決・改善したいこと
投稿:314 いいね数5の投稿の分割
- そのトピックの論点整理モジュールへのリンクをフッターに入れる:
  - QRコードでも良い
  - 論点整理モジュールはトピックのタイトルをネットで検索しても出てこないので導線を作る
  
https://large-scale-conversation-sandbox.discourse.group/t/topic/45/50
## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### [意図しない要約の防止](https://github.com/digitaldemocracy2030/idobata-analyst/issues/76)

**作成者:** itoma-aikon  
**作成日:** 2025-03-27T01:39:59Z  
**内容:**

## 解決・改善したいこと

投稿:akinori いいね数1の投稿
ダウンロードに「 論点整理モジュール」と話した内容も含んでほしいです。または、「AI と議論した内容もAI レポートに反映される」とのことなので、反映の有無と可能であれば反映する内容を指定したいです。意見を所有したいわけではないですが、意図しない文言での反映が行われるのを避けたいです。
https://large-scale-conversation-sandbox.discourse.group/t/topic/45/12
投稿:akinori いいね数1の投稿の分割
![Image](https://github.com/user-attachments/assets/46e2cdd6-a0bf-4c0c-993a-d5f55cacb404)
また、要約時の編集によって、意図していない内容に変わる可能性もあります。「同時に多様な学び方に触れる必要があります」と記載したのですが、「同一人物であっても多様な学び方に触れる機会を提供する必要がある」となって記録されました。

論理的な漏れや異なる意図に解釈できる場合には、念のため確認してくれる方が嬉しいかもしれません。また、本返信の時に実施してもらえると、より解釈が割れないような返信にできるのかもしれません。

こうあるべきだ、とお伝えしているわけではありません。何かの参考になりましたら嬉しいです。
https://large-scale-conversation-sandbox.discourse.group/t/topic/45/13

## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### [レポートの用途解説](https://github.com/digitaldemocracy2030/idobata-analyst/issues/74)

**作成者:** itoma-aikon  
**作成日:** 2025-03-27T01:10:27Z  
**内容:**

## 解決・改善したいこと

投稿:westcoaster いいね数1の投稿の分割
AI教育のところでレポートが投稿されたが、このレポートで示された新しい論点しか議論しちゃいけないわけじゃないんですよね？このレポートをどう使ってほしいかもうちょっと説明があった方が親切な気がしました（論点の整理・議論を深めたいポイントの提示だけど、元々の論点についても引き続きコメントしていいんですよね）
https://large-scale-conversation-sandbox.discourse.group/t/topic/45/5

## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### [lint, test が入っていないディレクトリにも lint, test を入れたい](https://github.com/digitaldemocracy2030/idobata-analyst/issues/54)

**作成者:** spinute  
**作成日:** 2025-03-20T11:30:00Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

開発効率やコード品質上げるために lint, test を入れたい

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

lint, test が入っていないディレクトリに lint, test を入れる

何を入れるべきかは諸説あるが、frontend に eslint、chat-bot に jest が入っているので、ファーストチョイスはそれで良い気がする（個人的には biome にしても良い気もするが、そのへんは reasonable な範囲でやる人の好みで決めて良さそう）

余裕があれば CI でも動かしたい（PR としては分けたほうが良さそう）

**コメント:** なし

---

### [Devcontainerを導入することで、lint/auto formatの設定をしやすくする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/50)

**作成者:** takker99  
**作成日:** 2025-03-20T05:32:01Z  
**内容:**

## 解決・改善したいこと

自分がNode.jsに不慣れだった点もありますが、Node.jsでlint & formatするのにどのvscode拡張機能を入れればいいか少し迷いました。
- dbaeumer.vscode-eslintとvscode.typescript-language-featuresを使えばいいみたい？

editorがvscodeに限られてしまいますが、Devcontainerを設定すれば、開発環境回りのトラブルを減らせると思います。
Github Codespaceでも動かせるので、手元で開発環境を用意できなくても、クラウド上ですぐに作業することができます。

ただ、monorepo相手だと設定がややこしいみたい？です。
- https://engineering.nifty.co.jp/blog/24158
- https://zenn.dev/izm/articles/3651766774c877
- https://product.st.inc/entry/2024/12/27/133252
- https://qiita.com/re_2osushi8888/items/e9df614f7b5182ae284d

一応提案としてissue立てておきますが、あんまり旨味ないかもです。


## 具体的な実現方法・実装方法の概要（未記入でも構いません）



**コメント:** なし

---

### [OpenRouter APIを使っている説明をREADME.mdに入れる](https://github.com/digitaldemocracy2030/idobata-analyst/issues/49)

**作成者:** takker99  
**作成日:** 2025-03-20T04:58:51Z  
**内容:**

## 解決・改善したいこと

一応`.env.example`中の文字列から察せますが、OpenRouter API経由でGemini APIを使っていることをREADME.mdに追加したいです。
どのLLM APIを使えばいいのかすぐにわからなかったので……。

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

README.mdに`OPENROUTER_API_KEYに各自で発行したGemini API keyを設定してください。`と追加すれば十分かな？

**コメント:** なし

---

### [envファイルの準備を少し楽にする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/47)

**作成者:** takker99  
**作成日:** 2025-03-20T04:12:56Z  
**内容:**

## 解決・改善したいこと

`README.md`の`開発環境のセットアップ`→`依存関係のインストール`に環境変数をコピーするコードがありますが、現状だとそれを毎回コピーして実行しないといけないので、少々手間です。
あらかじめrepoにshell scriptとして用意しておき、one linerで実行できるようにしたいです。

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

以下のコードを`copy-env.sh`としてrepoのルートに用意する。

```bash
# ルートディレクトリ
cp .env.example .env

# バックエンド
cp packages/backend/.env.example packages/backend/.env

# フロントエンド
cp packages/frontend/.env.example packages/frontend/.env
```

**コメント:** なし

---

### [論点分析レポートのクオリティを上げたい](https://github.com/digitaldemocracy2030/idobata-analyst/issues/44)

**作成者:** blu3mo  
**作成日:** 2025-03-17T09:41:26Z  
**内容:**

## 解決・改善したいこと
- 論点分析レポートの質を上げたい
  - 抽象度の高いタスクとして書いておきます。
- 例
  - https://delib.takahiroanno.com/projects/67d76376c29091a5f2fb8aa4/overall
  - https://w1740803485-clv347541.slack.com/archives/C08FF5MM59C/p1742203099858229
    - <img width="633" alt="Image" src="https://github.com/user-attachments/assets/1e4bfd8f-bbdc-4718-a44e-347f741190e7" />

## 具体的な実現方法・実装方法の概要（未記入でも構いません）
- パイプラインの各所で色々な改善が考えられる。サブイシューに分割していきたい
- 何か改善案があればどなたでも提案/実装ぜひ

**コメント:** なし

---

### [モバイルで論点タブが崩れるのを修正する](https://github.com/digitaldemocracy2030/idobata-analyst/issues/42)

**作成者:** 101ta28  
**作成日:** 2025-03-17T07:09:40Z  
**内容:**

## モバイルでレイアウトが崩れるのを修正する

![Image](https://github.com/user-attachments/assets/17fdca51-9f32-4b71-a055-421f019cfc3e)

## 修正方法の概要（未記入でも構いません）

#18 と同じ方法で修正する

**コメント:** なし

---

### [開発時のhot reloadに対応](https://github.com/digitaldemocracy2030/idobata-analyst/issues/40)

**作成者:** blu3mo  
**作成日:** 2025-03-17T01:39:47Z  
**内容:**

## 解決・改善したいこと

> Pin
  [Yesterday at 11:10 PM](https://w1740803485-clv347541.slack.com/archives/C08FF5MM59C/p1742134255623839)
環境構築スムーズにできるかもなところメモ：
> - build しないと変更反映されない（？）の開発不便そう。hot reload あるといいな（vite が入ってる気がするのでそうなっていないの不思議）

## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### [issueテスト（agent）](https://github.com/digitaldemocracy2030/idobata-analyst/issues/33)

**作成者:** jujunjun110  
**作成日:** 2025-03-15T13:14:57Z  
**内容:**

内容テスト
URL: 
by: @Jun Ito（エディ）

**コメント:** なし

---

### [てすと](https://github.com/digitaldemocracy2030/idobata-analyst/issues/32)

**作成者:** jujunjun110  
**作成日:** 2025-03-15T13:14:56Z  
**内容:**

てすと
URL: 
by: @Jun Ito（エディ）

**コメント:** なし

---

### [idobata-agentへのバグ報告](https://github.com/digitaldemocracy2030/idobata-analyst/issues/27)

**作成者:** jujunjun110  
**作成日:** 2025-03-12T15:58:22Z  
**内容:**

idobata-agentへのバグ報告
URL: idobata-agentへのバグ報告
by: @Jun Ito（エディ）

**コメント:** なし

---

### [x](https://github.com/digitaldemocracy2030/idobata-analyst/issues/26)

**作成者:** jujunjun110  
**作成日:** 2025-03-12T15:55:36Z  
**内容:**

x
URL: x
by: @Jun Ito（エディ）

**コメント:** なし

---

### [コメント一覧で日付に加えて時刻も表示したい](https://github.com/digitaldemocracy2030/idobata-analyst/issues/24)

**作成者:** javasparrows  
**作成日:** 2025-03-12T09:35:31Z  
**内容:**

[コメント一覧](https://delib.takahiroanno.com/projects/67c7c8cd858bc4c6ea297050/comments)

![Image](https://github.com/user-attachments/assets/b76278ed-9cc5-4449-bae3-d16abb4caf9b)

**コメント:** なし

---

### [READMEのフロントエンド環境変数がない](https://github.com/digitaldemocracy2030/idobata-analyst/issues/23)

**作成者:** javasparrows  
**作成日:** 2025-03-12T09:04:49Z  
**内容:**

`packages/frontend/.env.example`がそもそも無いようで、
```
# フロントエンド
cp packages/frontend/.env.example packages/frontend/.env
```
の部分がエラーになってしまう

**コメント:** なし

---

### [全体レポートのどこかに情報源の分布を追加する](https://github.com/digitaldemocracy2030/idobata-analyst/issues/19)

**作成者:** blu3mo  
**作成日:** 2025-03-12T02:13:16Z  
**内容:**

これ全体レポートのどこかに情報源の分布をかいておけるとよいかと
xが12件(xx%)、formがxx件(xx%)、みたいな

<img width="486" alt="Image" src="https://github.com/user-attachments/assets/528c8920-d24b-4cd2-a88f-f718ac18843a" />


**コメント:** なし

---

### [モバイルでレイアウトが崩れるのを修正する](https://github.com/digitaldemocracy2030/idobata-analyst/issues/18)

**作成者:** blu3mo  
**作成日:** 2025-03-12T02:10:08Z  
**内容:**

---
モバイルでレイアウトが崩れるのをなおしたい。タブがはみ出ている。

https://github.com/user-attachments/assets/acaf26c3-3d11-447f-896a-f39417008907

**コメント:** なし

---

### [全体レポートのタイトルの周りに[]がついてしまうのを直す](https://github.com/digitaldemocracy2030/idobata-analyst/issues/17)

**作成者:** blu3mo  
**作成日:** 2025-03-12T02:08:49Z  
**内容:**

----
• <https://delib.takahiroanno.com/projects/67c7c8cd858bc4c6ea297050/overall|全体レポート>のタイトルの周りに[]がついてしまうのを直したい（添付画像参照）
    ◦ これはプロンプトが悪いだけだと思う
    ◦ プロンプトはバックエンドの/config/prompt-templatesにあります

![Image](https://github.com/user-attachments/assets/cd67ec5f-de85-4cdb-90cd-860beb57d234)

**コメント:** なし

---

### [チャット機能から来たコメントのtypeを「チャット」にする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/14)

**作成者:** blu3mo  
**作成日:** 2025-03-12T02:07:59Z  
**内容:**

- チャット機能から吸われたコメントの種類は、「その他」ではなく「チャット」と表示されてほしい
- 前提：チャット機能については <https://x.com/blu3mo/status/1897382669945856071> を参照
- 現状：今はyoutube, x, form, otherの4種しか受け付けていない。（backend/src/models/comments.tsを参照）
- やりたいこと：
  - ここに5種目としてchatを追加したい。
  - その上で、フロントエンドでチャット由来のコメントの種類は「チャット」と表示されてほしい
  - 添付スクショに表示されているファイルはコメントの種類を扱っているので修正必要そう
  - 加えて、chat-botサーバーからバックエンドapiを呼んでいるところも修正必要そう
- これはフロントエンド、バックエンド、chat-botサーバー全部絡むのでややこしいかもしれない

**コメント:** なし

---

### [コメント一覧に日付も表示するようにする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/13)

**作成者:** blu3mo  
**作成日:** 2025-03-12T02:07:09Z  
**内容:**

• <https://delib.takahiroanno.com/projects/67c7c8cd858bc4c6ea297050/comments|コメント一覧>、日付に加えて時刻も表示したい
    ◦ データはあるのでフロントエンドをいじるだけ

[Slack Message](https://annyotakagmailcom.slack.com/archives/C0858TLQSAY/p1741241395008489?thread_ts=1741240865.781019&cid=C0858TLQSAY)

**コメント:** なし

---

### [GoogleAnalyticsを導入する](https://github.com/digitaldemocracy2030/idobata-analyst/issues/11)

**作成者:** blu3mo  
**作成日:** 2025-03-12T02:06:15Z  
**内容:**

どっから来ていてどれくらい見られているのか？（コメント率どれくらいか）
を見るためにもGoogle Analyticsなどを入れたほうがよいのではないか

[Slack Message](https://annyotakagmailcom.slack.com/archives/C0858TLQSAY/p1741259594329899?thread_ts=1741254139.990899&cid=C0858TLQSAY)

**コメント:** なし

---

### 過去30日間に作成されたissue (20件)

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

### [議論の粒度をGoogleマップのズームのように行き来できるようにすることで、利用者が議論の全体像と詳細を両方理解できるようにする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/85)

**作成者:** itoma-aikon  
**作成日:** 2025-03-27T07:23:53Z  
**内容:**

## 解決・改善したいこと
type:改善要望
summary: 
投稿:samo いいね数0の投稿の分割
- グーグルマップ式のズーム機能を導入
  - 全体像把握（10,000ft view）→ テーマ別クラスター → 個別意見の3段階表示
- 視覚的階層表現（色分け/サイズ調整による重要度表示）

※意見の誘導をしたのは投稿者だが、詳細を考えたのはAIとのこと
url: https://large-scale-conversation-sandbox.discourse.group/t/topic/45/52
投稿:itoma_aikon いいね数の投稿0の分割
ちょうどデジタル民主主義2030プロジェクトの広聴AI(ブロードリスニングのAI)にてズーム機能が実装されつつあるので、転用すると良さそうです。
url: https://large-scale-conversation-sandbox.discourse.group/t/topic/45/56
投稿:samo いいね数0の投稿の分割
私のイメージ的には、以下の様な感じです。（中略）
### 解像度自動調整機能
ボタン操作一つでAIが即座に内容理解を最適化します：
- **タップするだけで深度調整**：一度のタップでAIが自動的に解釈を変更し、その人に合った詳細度に調整
- **3段階表示**：全体俯瞰（マクロ）→テーマ別（メソ）→個別意見（マイクロ）を直感的に行き来
- **自動要約エンジン**：複雑な意見でも簡潔な要点として表示、必要に応じて詳細表示
### 馴染みのGUIパターン活用
既に使い慣れたインターフェースを応用し、学習負荷を最小化：
- **地図アプリ的ズーム感覚**：ピンチイン・アウトの感覚で意見の深さを調整
- **SNSライクなカード表示**：馴染みのある形式で意見を閲覧
- **絵文字・リアクション機能**：日常的に使うコミュニケーション方法を踏襲
このアプローチにより、スマホやタブレットの基本操作さえできれば、誰でも直感的に使えるシステムを実現。AIによる自動解釈と既存GUIパターンの組み合わせで、複雑な操作学習なしに多様な都民の意見を効果的に収集できます。

https://large-scale-conversation-sandbox.discourse.group/t/topic/45/57


## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### [他のAIとの連携性を深めるため、サイト全体の情報をテキストでコピー可能にする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/84)

**作成者:** itoma-aikon  
**作成日:** 2025-03-27T07:14:02Z  
**内容:**

## 解決・改善したいこと

投稿:samo いいね数2の投稿
### 現状の課題
論点整理モジュールを長く使用していると、以下のような問題を感じています:
- 回答がだんだんパターン化していく印象がある
- 使い込むほど似たような回答が繰り返され、ストレスになる
- 質問の仕方にも改善の余地があるが、システム側にも課題がある
### 提案内容
サイト上の論点すべての進捗状況を他のAI（PerplexityやノートブックLMなど）に取り込み、論点整理モジュールとは別のAIとのやり取りを通じて思考を深める仕組みを作りたいと考えています。

#### 期待されるメリット:
- 都政改善のための新しいアイデア発掘の可能性が広がる
- 既出アイデアとの重複を回避しやすくなる
- 既出アイデアが到達した地点から議論を発展させやすくなる

## 具体的な実現方法・実装方法の概要（未記入でも構いません）
### 具体的な実装希望
このサイトで扱われている論点は多岐にわたるため、各論点のまとめを一つずつ開いてコピー＆ペーストする作業は非効率です。そこで次のような機能を希望します:

- 現在のすべての論点についての議論内容
- それぞれの論点に関するコメント
- 各論点の進捗状況

これらを網羅したページを作成していただきたいです。そうすれば、そのページの内容を一括でコピーしてテキストファイルに保存し、普段使用しているAIに取り込むことができます。

#### 最終的な活用イメージ:
別のAIとのやり取りを通じて深めた考察を整理し、再度「東京井戸端会議」の論点整理モジュールに還元することで、より充実した都政の議論が可能になると考えています。

url:https://large-scale-conversation-sandbox.discourse.group/t/topic/45/51


**コメント:** なし

---

### [ビジュアル分析のフッダーに名称追記](https://github.com/digitaldemocracy2030/idobata-analyst/issues/82)

**作成者:** itoma-aikon  
**作成日:** 2025-03-27T06:37:22Z  
**内容:**

## 解決・改善したいこと

投稿:314 いいね数5の投稿の分割
- デジタル民主主義2030の論点整理モジュールであることをフッターに明記する:
  - デジタル民主主義2030のロゴがあるのであればそれを入れるとか

https://large-scale-conversation-sandbox.discourse.group/t/topic/45/50

## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

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

### [AIチャットが、会話内容をDiscourseに投稿しやすいような文章に整形してくれて、投稿を促す機能をつけると投稿ハードルが下がるのではないか](https://github.com/digitaldemocracy2030/idobata-analyst/issues/80)

**作成者:** jujunjun110  
**作成日:** 2025-03-27T02:06:09Z  
**内容:**

## 解決・改善したいこと

いま、privateチャットは結構使われるが、Discourseへの投稿ハードルは高いという事実がある
ここをうまく接続することで、Discourseが盛り上がるのではないか。

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

一定以上チャットを進めると、AIが意見をまとめスレッドへの投稿をサジェストする発言を行うようになる

**コメント:** なし

---

### [意見まとめで、円グラフと散布図を両方表示できるようにすることで、より包括的に意見のばらつきを理解できるようにする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/79)

**作成者:** itoma-aikon  
**作成日:** 2025-03-27T02:04:08Z  
**内容:**

## 解決・改善したいこと

投稿:314 いいね数0の投稿
「AIによる意見まとめ」では、出た意見の量的割合が円グラフで示されていますが、意見の割合を示すよりも、TTTCの意見の散布図のようなものの方が良いと思います
散布図の方が分析コストが高くなってしまうかもしれませんが、円グラフでどの意見が多いかを知ることにはあまり意味がないように感じました
https://large-scale-conversation-sandbox.discourse.group/t/topic/45/40

## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### [コメント一覧での情報源を常時表示可能にする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/78)

**作成者:** itoma-aikon  
**作成日:** 2025-03-27T02:00:46Z  
**内容:**

## 解決・改善したいこと

投稿:akinori いいね数0の投稿
「論点整理モジュール」の「コメント一覧」や「論点ごとの分析」下の各意見の「派」以下に表示されるコメントの情報源「その他」について、吹き出し表示される部分を常時表示可能＜にも＞選択できるようにしてほしい。

要約が表示されるのは嬉しいのですが、詳細をマウスオーバーして閲覧するのが、少し煩雑です。また、小さい表示でもコメントの記録時刻(または日付)表示があると登録順に表示されるなら、遡る範囲が特定できて嬉しいです。
https://large-scale-conversation-sandbox.discourse.group/t/topic/45/35


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

### [分析時に投稿をユニークなユーザーIDでカウントすることで、多重投稿した人の意見の重みが過剰に出ないようにする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/75)

**作成者:** itoma-aikon  
**作成日:** 2025-03-27T01:13:14Z  
**内容:**

## 解決・改善したいこと

投稿:westcoaster いいね数2の投稿
暇人なのでめっちゃコメントしまくっているのですが、複数回コメントしたときに、「自分一人の意見なのに、投稿が分かれているせいでこれが◯件とまとめられてしまうのが申し訳ない…」という気持ちに。
レポートにも「 本分析で使用した情報ソースでは、一人のユーザーが複数の意見を投稿できる仕様となっているため、数値はあくまで参考情報としてご認識ください。」とありますが、分析にかける前にIDごとにgroup byするみたいなことは難しいのでしょうか？

（ちなみに、投稿一発目がたたき台の提示となってかなり意見を考えやすくなりました！）

https://large-scale-conversation-sandbox.discourse.group/t/topic/45/9


## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### [ビジュアル分析タブの余白を調整し、スマホで表示した際にも快適に内容を理解できるようにする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/72)

**作成者:** spinute  
**作成日:** 2025-03-25T07:47:25Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->

ビジュアル分析タブをスマホで表示すると、横方向に過度に余白があって見にくい

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

![Image](https://github.com/user-attachments/assets/3f9efec6-454b-45d5-919f-20a9d08bb10c)

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

レポートが4重の入れ子 div の中に入っているが、外の3つは不要そう

スマホだと画面幅が狭く特に見づらいが、PC でも無駄なスペースを使っているので、そもそも div の入れ子を減らして良い気がする

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

### [バックエンド のテストを導入することで、開発者が継続的にコード品質をキープしやすくする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/70)

**作成者:** spinute  
**作成日:** 2025-03-23T12:06:57Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->

/packages/backend のテストがない

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

jest を使って簡単なテストを導入する

/package/chat-bot には既に導入済みなので、それを参考にすると良いかもしれない

**コメント:** なし

---

### [frontend のテストを導入することで、開発者が継続的にコード品質をキープしやすくする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/69)

**作成者:** spinute  
**作成日:** 2025-03-23T12:06:36Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->

/packages/frontend のテストがない

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

jest を使って簡単なテストを導入する

/package/chat-bot には既に導入済みなので、それを参考にすると良いかもしれない

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

### [論点抽出の仕組みを改善することで、議論に対して的を得ていて、より活発な議論をもたらす論点をAIが抽出できるようにする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/58)

**作成者:** blu3mo  
**作成日:** 2025-03-21T11:23:43Z  
**内容:**

今のパイプラインには2つのステップがある
  - 1 大量の意見から、論点と、各論点における派閥を抽出する
  - 2 各コメントに対して、各論点の派閥をラベル付けする
 **このうち、1（論点抽出）の仕組みを改善したい**

## 現状
  - Geminiに全コメントを放り込んで、雑に論点を5個抽出させている
    - https://github.com/digitaldemocracy2030/idobata-analyst/blob/main/packages/backend/src/config/prompt-templates/question-generation.txt
    - Geminiのコンテキスト幅の長さに甘えている
    - ベースラインとしては良いが、もっと良い方法があると思う

## 目指したい方向
  - 目的：「論点を抽出しつつ各コメントの立場を整理すること」によって、「DiscourseやSNSで①議論が深まり②参加者が増えるようなレポート/エージェントを動作させたい」
    - そのためにできると嬉しいことの例
      - 「マイナーだけど重要な論点」を発見したい
      - 新しい議論を生み出すような論点を発見したい
      - アテンションを集められるような賛否両論がある論点を発見したい
      - 存在する論点を全て網羅したい
      - 他にも色々ありそう
  - その他のnice-to-haveなこと
    - 分析結果の説明可能性が高い
    - コストが低い

## 試してみたいこと
  - 下手にbefore-LLMの手法を参考にするより、LLMを使ったら何ができるかをゼロベースで考えた方が良いものが作れそう
    - よっぽどのことをやらない限り、LLMのコストがボトルネックにはならなさそう。
      - 「全コメントをgemini-2.0-flashに放り込んで立場を分析させる」とか今やっているが全然コストは許容範囲
      - 線形のオーダーのことをやっている限りは大丈夫そう
  - コメントをバッチに分けて論点を生成させた上で最後にまとめた方が細部の論点も拾えそう
    - 例えば、
    - 1: 1000件のコメントを、50件のバッチ20個に分ける
    - 2: 各バッチから5個の論点を抽出する
      - ここは今までと同じようにLLMに全部放り
      - 合計5*20=100個の論点が抽出される。中には似たものも多いと思う。
    - 3: 100個の論点をLLMに放り込んで、渾身の5個の論点を作らせる
    - これは結構さくっと試せそう
  - 「100個の論点を作って、派閥のラベル付けをやって、そのデータを元に論点を5個選ぶ」みたいなやり方もありそう
    - 「100個の論点から5個の論点を選ぶ部分」の仕組みが色々探索できそう
    - n個のコメントがある時に各論点をn次元のベクトルとして捉えて、もっとも直交している五個のベクトルを選ぶ、とか
      - PolisやRemeshが近いアプローチの分析をやっている
        - https://pol.is/
        - https://arxiv.org/html/2503.01769v2
      - これは、分析結果の説明可能性が高い点が良いと思う

## (イシューのスコープ外だが)前提を疑う話
  - 今の「1 論点抽出 → 2 派閥をラベル付け」という設計より良い方法がある？
  - 今の設計の良いところ:
    - 1さえ何とかできれば、2の部分はいくらでもスケール可能
      - 100億件のコメントが来てもこのシステムは同じように動作する
      - コストは線形に伸びていくが、、
    - 新しいコメントが追加された時には2だけやればいいので、低コスト/一瞬でそれを分析結果に組み込める
    - そもそも「論点を抽出してコメントを整理すること」が「DiscourseやSNSで①議論が深まり②参加者が増えるようなレポート/エージェントを作ること」の役にたつのか？

**コメント:** なし

---

### [ビジュアルレポートのタイトルに作成日時が被っているのを改善することで閲覧者が読みやすくする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/57)

**作成者:** nishio  
**作成日:** 2025-03-21T02:25:08Z  
**内容:**

## 解決・改善したいこと

<img width="807" alt="Image" src="https://github.com/user-attachments/assets/b6f050dd-607f-4db4-9e1d-0dd3dec04e7c" />


<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### [分析開始前に、分析にかかるAPI費用を計算して表示することで事前に影響が分かるようにする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/56)

**作成者:** blu3mo  
**作成日:** 2025-03-21T00:07:30Z  
**内容:**

## 解決・改善したいこと

CSVアップロードの画面にてファイルをアップロードした後、分析を開始する前に「合計〇〇USDかかります」と表示されてほしい。
抽出フェーズと論点分析フェーズの合計費用がわかると良さそう。

## 具体的な実現方法・実装方法の概要（未記入でも構いません）
CSVのデータさえあれば、いくらかかるのか概算できるはず。
OpenRouterのGemini費用: https://openrouter.ai/google/gemini-2.0-flash-001
概算できればニーズは満たせると思うで、「全コメントの合計文字数 x 係数」みたいな計算でも良さそう。

**コメント:** なし

---

### [ビジュアルレポートの生成プロンプトを改善することで、SNS上などで見た人が論点やプロジェクトについて理解したり興味を持ちやすくする](https://github.com/digitaldemocracy2030/idobata-analyst/issues/46)

**作成者:** blu3mo  
**作成日:** 2025-03-19T01:11:50Z  
**内容:**

## 解決・改善したいこと

https://large-scale-conversation-sandbox.discourse.group/t/topic/45/50
論点整理モジュールのビジュアル分析についてです。
ビジュアル分析はかなり分かりやすく、かつ、柔らかいデザインで良いと思います。拡散してもらいやすくするために、

XなどSNSで投稿しやすいように、画像としてダウンロードするボタンを作る:
一定の長さで縦n分割にしてダウンロードするボタンを作るとさらに良さそう
デジタル民主主義2030の論点整理モジュールであることをフッターに明記する:
デジタル民主主義2030のロゴがあるのであればそれを入れるとか
そのトピックの論点整理モジュールへのリンクをフッターに入れる:
QRコードでも良い
論点整理モジュールはトピックのタイトルをネットで検索しても出てこないので導線を作る
というのはどうでしょうか

## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### 過去30日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去30日間にマージされたPR (29件)

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

### [Add: issue2project automation](https://github.com/digitaldemocracy2030/idobata-analyst/pull/86)

**作成者:** jujunjun110  
**作成日:** 2025-03-29T05:23:13Z  
**変更:** +47 -0 (1ファイル)  
**マージ日:** 2025-03-29T05:23:22Z  
**内容:**

# 変更の概要
- イシューをプロジェクトに自動追加するAutomationを追加

# 変更の背景
- Project側のautomationだとリポジトリ数に限界があったため

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Add: GA Tracking Code](https://github.com/digitaldemocracy2030/idobata-analyst/pull/73)

**作成者:** jujunjun110  
**作成日:** 2025-03-26T13:12:08Z  
**変更:** +13 -1 (1ファイル)  
**マージ日:** 2025-03-26T14:01:28Z  
**内容:**

# 変更の概要
- #11 
- GAのタグを導入した。これでpageviewなどは取れるようになるはず。

# 変更の背景
- どのようなユーザーに見られているか知りたい。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [biome の警告が出るようになっていたので修正した](https://github.com/digitaldemocracy2030/idobata-analyst/pull/68)

**作成者:** spinute  
**作成日:** 2025-03-23T12:01:23Z  
**変更:** +62 -62 (3ファイル)  
**マージ日:** 2025-03-26T02:02:08Z  
**内容:**

# 変更の概要
- biome の警告を修正した

# 変更の背景
- https://github.com/digitaldemocracy2030/idobata-analyst/pull/55 以後入った変更で新たに biome の警告がでるようになっていたので修正した
- https://github.com/digitaldemocracy2030/idobata-analyst/issues/54 を CI に入れて自動でチェックしてくれるようになるので、そのうちこういう手動対応は不要になる予定

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [improve readme](https://github.com/digitaldemocracy2030/idobata-analyst/pull/67)

**作成者:** spinute  
**作成日:** 2025-03-23T11:57:33Z  
**変更:** +12 -21 (1ファイル)  
**マージ日:** 2025-03-24T01:08:55Z  
**内容:**

# 変更の概要
- readme を更新した

# 変更の背景
- https://github.com/digitaldemocracy2030/idobata-analyst/pull/66 の変更を踏まえて readme を更新した
    - シンプルになったはず
- https://github.com/digitaldemocracy2030/idobata-analyst/issues/49 の内容をふまえて readme を更新した

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [add makefile](https://github.com/digitaldemocracy2030/idobata-analyst/pull/66)

**作成者:** spinute  
**作成日:** 2025-03-23T11:55:41Z  
**変更:** +44 -1 (4ファイル)  
**マージ日:** 2025-03-24T01:08:45Z  
**内容:**

# 変更の概要
- makefile を追加した

# 変更の背景
- 初期設定、起動、lint, test などを一発で実行できる makefile を置いた
    - test 未実装の backend, frontend ではその旨表示する echo を書いた
    - chat-bot では test コマンドはあるもののテストケースが一つも実行されずエラーが出ていたので、jest コマンドに --passWithNoTests オプションを付けた
- 対応する readme の更新は https://github.com/digitaldemocracy2030/idobata-analyst/pull/67 でやっている

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [fix frontend lint and its warnings](https://github.com/digitaldemocracy2030/idobata-analyst/pull/65)

**作成者:** spinute  
**作成日:** 2025-03-23T11:49:38Z  
**変更:** +142 -133 (14ファイル)  
**マージ日:** 2025-03-26T02:03:32Z  
**内容:**

# 変更の概要
- https://github.com/digitaldemocracy2030/idobata-analyst/pull/55 で biome を入れたが、frontend の設定が不十分だったので直した
- また、その結果露呈した frontend の lint error を一通り修正した

# 変更の背景
- frontend だけ biome のバージョンが何故か古かったので、backend, chat-bot に合わせてバージョンを上げた https://github.com/digitaldemocracy2030/idobata-analyst/compare/main...spinute:fix/frontend-lint?expand=1#diff-8571ecd91584b00015b23695d3a6a164282636bb47bfbe46dca243bf9b4db773R25
- lint, format で走らせているのが frontend だけなぜか lint, format コマンドになっていたので、check コマンドで統一した https://github.com/digitaldemocracy2030/idobata-analyst/compare/main...spinute:fix/frontend-lint?expand=1#diff-8571ecd91584b00015b23695d3a6a164282636bb47bfbe46dca243bf9b4db773R9-R10
    - biome では check が lint, format 含む色々やってくれるコマンド。--write を付けると修正可能なものを修正してくれる https://github.com/biomejs/biome?tab=readme-ov-file#usage
- その後 npm run format を実行して、検出されるようになったエラーを一通り修正した
    - 自動修正不可なものもあったので、そこは手動で修正した（主に https://biomejs.dev/linter/rules/no-label-without-control/ ）

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

### [起動に失敗するようになっていたので compose.yaml を修正した](https://github.com/digitaldemocracy2030/idobata-analyst/pull/61)

**作成者:** spinute  
**作成日:** 2025-03-22T20:41:06Z  
**変更:** +2 -1 (1ファイル)  
**マージ日:** 2025-03-26T02:03:55Z  
**内容:**

# 変更の概要
- 起動に失敗するようになっていたので compose.yaml を修正した
- https://github.com/digitaldemocracy2030/idobata-analyst/pull/45#issuecomment-2745619619 の問題を修正した

# 変更の背景
- https://github.com/digitaldemocracy2030/idobata-analyst/pull/45#issuecomment-2745619619 を参照

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [微修正: .env.example の設定の補足説明を正しくなるように変更 を更新](https://github.com/digitaldemocracy2030/idobata-analyst/pull/59)

**作成者:** itoma-aikon  
**作成日:** 2025-03-21T12:58:12Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-03-21T14:32:12Z  
**内容:**

# 変更の概要
- .env.example の設定の補足説明を正しくなるように変更

# 変更の背景
- 必要なキーがgeminiキーからOPENROUTERキーに変更されているのにも関わらず、説明にgeminiキーと書かれているため

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [biome を入れようとしてみる](https://github.com/digitaldemocracy2030/idobata-analyst/pull/55)

**作成者:** spinute  
**作成日:** 2025-03-20T18:36:10Z  
**変更:** +3247 -2982 (75ファイル)  
**マージ日:** 2025-03-21T05:16:10Z  
**内容:**

# 変更の概要
- https://github.com/digitaldemocracy2030/idobata-analyst/issues/54 の一部として biome を導入した

# 変更の背景
- chat-bot や backend に linter がなく、frontend では eslint が一部設定されていた
- 全パッケージに biome を導入し、lint エラーを一通り修正
    - frontend にはもともと eslint が入っていたため削除
- すべてのパッケージで同じ biome のルールを適用し、`npm run lint` でチェック、`npm run format` で自動整形できるようにした
- PR の規模が大きいため、自動フォーマット + lint エラーを cursor を使って大まかに修正
    - もう少し慎重に導入するのもありかも（例: https://zenn.dev/dev_commune/articles/ab57b866d84a3e）。やや慎重すぎるかも

## やったこと

- .vscode/settings.json：VS Code の自動フォーマッタ設定
- biome.json：biome のルール設定等。基本的に細かいルールはほとんど設定していない（recommended というので概ねいい感じになるのが biome の良いところ）
- package.json：`npm run lint` で `biome check`が、`npm run format` で `biome check --write` が走るようにした。また biome をインストールした（frontend では eslint 関係のものをアンインストールした）
- それ以外の変更は `npm run format` して自動でルール適用しつつ、unsafe のため自動で修正できないものは、そのログを Cursor に見せながら個別に修正して回った

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [チャット機能から来たコメントのtypeを「チャット」にする](https://github.com/digitaldemocracy2030/idobata-analyst/pull/53)

**作成者:** 101ta28  
**作成日:** 2025-03-20T11:28:57Z  
**変更:** +12 -4 (6ファイル)  
**マージ日:** 2025-03-20T23:36:08Z  
**内容:**

close #14 
# 変更の概要

- frontend
  - コメントのタイプに「チャット」を追加しました。
- backend
  -  コメントのタイプに「チャット」を追加しました。
- chat-bot
  - backendへの送信時ソースタイプをチャットに変更しました。

CSVアップロード画面での表示

![Screenshot from 2025-03-20 20-14-32](https://github.com/user-attachments/assets/3b0dfd38-9f30-4a88-bf37-fb31ef0695e0)

論点ごとの分析での表示

![Screenshot from 2025-03-20 20-16-34](https://github.com/user-attachments/assets/6b44ff2a-af36-44b3-a9be-9d4c25329ff4)

コメント一覧での表示

![Screenshot from 2025-03-20 20-14-03](https://github.com/user-attachments/assets/171793db-dd02-423f-8c65-12aad7bba31d)


# 変更の背景
- #14 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Update: セルフアサインできるワークフローを追加](https://github.com/digitaldemocracy2030/idobata-analyst/pull/52)

**作成者:** jujunjun110  
**作成日:** 2025-03-20T11:10:43Z  
**変更:** +50 -3 (2ファイル)  
**マージ日:** 2025-03-20T11:12:15Z  
**内容:**

# 変更の概要
- issueコメントで、 /assign と入力するとセルフアサインできる機能を追加

# 変更の背景
- リポジトリに権限がないとアサインを変更できない状態が、現在の状態に適していないため

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [introduce openRouterService](https://github.com/digitaldemocracy2030/idobata-analyst/pull/51)

**作成者:** spinute  
**作成日:** 2025-03-20T11:10:36Z  
**変更:** +267 -400 (11ファイル)  
**マージ日:** 2025-03-21T06:17:23Z  
**内容:**

# 変更の概要
- OpenAI を使った OpenRouter の呼び出し（とそれに付随する入出力処理・リトライ・ロギング・例外処理）が色々なところに書かれていたので、packages/backend/src/services/openRouterService.ts に集約した
- 基本的には過去のものと同様の処理を保ちつつ、リトライ回数やバックオフ、エラー処理など、あまり拘りがなさそうなところはシンプルにするために統一のものにした

# 変更の背景
- https://github.com/takahiroanno2024/idobata-analyst/issues/22#issuecomment-2727598833 のもの

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [envファイルの準備を少し楽にする](https://github.com/digitaldemocracy2030/idobata-analyst/pull/48)

**作成者:** takker99  
**作成日:** 2025-03-20T04:22:32Z  
**変更:** +18 -0 (2ファイル)  
**マージ日:** 2025-03-20T06:56:52Z  
**内容:**

# 変更の概要
- Fixes #47

# 変更の背景
- See #47

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [開発時のhot reloadに対応](https://github.com/digitaldemocracy2030/idobata-analyst/pull/45)

**作成者:** 101ta28  
**作成日:** 2025-03-17T14:04:20Z  
**変更:** +168 -20 (6ファイル)  
**マージ日:** 2025-03-21T07:10:53Z  
**内容:**

close #40 
# 変更の概要
- 開発時の Hot Reload に対応
  - frontend: 開発用の Dockerfile (Dockerfile.dev) を編集
  - chat-bot: 開発用の Dockerfile (Dockerfile.dev) を作成
  - backend: 開発用の Dockerfile (Dockerfile.dev) を編集
- docker-compose.yml の編集
  - mongodb に healthcheck を追加し、MongoDB が正常に稼働しているかチェックするようにした
  - backend に Dockerfile.dev を追加・コードの変更をリアルタイムに反映するようにした
  - frontend でホットリロードに対応
  - chat-bot でホットリロードに対応 (フロント側ではブラウザのリロードが必要)
- docker-compose.prod.yml の作成
  - 本番環境用の compose ファイルです
  - mongodb に healthcheck を追加し、MongoDB が正常に稼働しているかチェックするようにした
  - 全コンテナに自動再起動を行うようにした -> 一時的なダウンや障害時に、手動で再起動しなくても自動復旧させるため

# 変更の背景
- [開発時のhot reloadに対応](https://github.com/digitaldemocracy2030/idobata-analyst/issues/40)

# レビュアーの方への確認・相談
開発・本番環境に手を加えているため、複数人で確認していただけると非常にありがたいです。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [論点タブがはみ出る問題を修正](https://github.com/digitaldemocracy2030/idobata-analyst/pull/43)

**作成者:** 101ta28  
**作成日:** 2025-03-17T07:12:48Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-03-17T08:51:29Z  
**内容:**

close #42 
# 変更の概要
- 論点タブを横スクロールで触れるようにしました
- デスクトップでの見た目に変更はありません

# 変更の背景
- [モバイルで論点タブが崩れるのを修正する](https://github.com/takahiroanno2024/idobata-analyst/issues/42)

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Update CLA.md](https://github.com/digitaldemocracy2030/idobata-analyst/pull/41)

**作成者:** takahiroanno  
**作成日:** 2025-03-17T05:55:48Z  
**変更:** +9 -9 (1ファイル)  
**マージ日:** 2025-03-17T06:58:49Z  
**内容:**

# 変更の概要
- ここに変更の概要を記載してください

# 変更の背景
- ここに変更が必要となった背景を記載してください

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました


**コメント:** なし

---

### [add issue templates](https://github.com/digitaldemocracy2030/idobata-analyst/pull/38)

**作成者:** spinute  
**作成日:** 2025-03-16T19:41:42Z  
**変更:** +30 -0 (2ファイル)  
**マージ日:** 2025-03-16T22:06:24Z  
**内容:**

# 変更の概要
- issue テンプレートを追加した

# 変更の背景
- https://w1740803485-clv347541.slack.com/archives/C08FF5MM59C/p1742137557334459?thread_ts=1742134255.623839&cid=C08FF5MM59C で GitHub に慣れている人は GitHub で issue を作って構わないと聞いたので、いただいたフォームの内容を元にバグ報告・改善提案用のテンプレートを作ってみた
    - 内容はとりあえず何も無いより着実に良くなりそうなシンプルなものに絞っている

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [モバイルでタブがはみ出る問題を修正](https://github.com/digitaldemocracy2030/idobata-analyst/pull/36)

**作成者:** 101ta28  
**作成日:** 2025-03-16T11:02:23Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-03-16T22:40:33Z  
**内容:**

close #18 

# 変更の概要
- モバイルでレイアウトが崩れる問題を修正
- タブを横スクロールで触れるようにしました
- デスクトップでの見た目に変更はありません

https://github.com/user-attachments/assets/3daf27f9-ede5-4719-8f9f-ed0cd1d8ba82

# 変更の背景
- [モバイルでレイアウトが崩れるのを修正する](https://github.com/takahiroanno2024/idobata-analyst/issues/18)

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [全体レポートのタイトルの周りに[]がついてしまうのを直す #17のプロンプトエンジニアリング](https://github.com/digitaldemocracy2030/idobata-analyst/pull/35)

**作成者:** DarthReidar-jp  
**作成日:** 2025-03-16T10:11:56Z  
**変更:** +14 -9 (1ファイル)  
**マージ日:** 2025-03-16T17:50:29Z  
**内容:**

# 変更の概要
- /config/prompt-templates/project-report.txtのプロンプトエンジニアリング
- より明示的に[]を生成しないように指示するようにした
- 20回程度E2Eで生成を試したが、[]がうまく消えているようだったためPRを出します。
(しかし、[]が出力されてしまう可能性は完全には消えてないと思います。)

# 変更の背景
[- 全体レポートのタイトルの周りに[]がついてしまうのを直す](https://github.com/takahiroanno2024/idobata-analyst/issues/17)

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Update README.md](https://github.com/digitaldemocracy2030/idobata-analyst/pull/29)

**作成者:** jujunjun110  
**作成日:** 2025-03-15T12:01:52Z  
**変更:** +4 -5 (1ファイル)  
**マージ日:** 2025-03-15T12:02:01Z  
**内容:**

# 変更の概要
- ここに変更の概要を記載してください

# 変更の背景
- ここに変更が必要となった背景を記載してください

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](/takahiroanno2024/policy-repository/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Add: Contribution Settings](https://github.com/digitaldemocracy2030/idobata-analyst/pull/28)

**作成者:** jujunjun110  
**作成日:** 2025-03-15T11:56:01Z  
**変更:** +675 -283 (4ファイル)  
**マージ日:** 2025-03-15T11:56:07Z  
**内容:**

内容なし

**コメント:** なし

---

### [日付を日本形式にし、時刻も日本時間で表示](https://github.com/digitaldemocracy2030/idobata-analyst/pull/25)

**作成者:** javasparrows  
**作成日:** 2025-03-12T10:54:35Z  
**変更:** +14 -1 (1ファイル)  
**マージ日:** 2025-03-13T05:28:20Z  
**内容:**

![Screenshot 2025-03-12 at 19 36 48](https://github.com/user-attachments/assets/5181c881-270f-445c-9452-5ef1b00d5f22)


**コメント:** なし

---

### 過去30日間に作成されたPR (4件)

### [他のAIとの連携性を深めるため、サイト全体の情報をテキストでコピー可能にする機能を追加](https://github.com/digitaldemocracy2030/idobata-analyst/pull/92)

**作成者:** blu3mo  
**作成日:** 2025-04-01T00:42:49Z  
**変更:** +498 -1 (7ファイル)  
**内容:**

## 概要
LLMs.txt形式でプロジェクトの分析結果をダウンロードできる機能を追加しました。

## 変更内容
- バックエンド: LLMs.txtを生成するためのサービスとAPIエンドポイントを追加
- フロントエンド: LLMs.txtをダウンロードするためのUIコンポーネントを追加
- プロジェクト詳細ページの「全体の分析」タブにLLMs.txtダウンローダーを表示

## 動作確認方法
1. プロジェクト詳細ページの「全体の分析」タブを開く
2. 「AI連携用LLMs.txtダウンロード」セクションから「LLMs.txt」または「LLMs-full.txt」をダウンロード

## 関連Issue
#84 他のAIとの連携性を深めるため、サイト全体の情報をテキストでコピー可能にする

**コメント:** なし

---

### [ビジュアル分析タブの余白を調整した](https://github.com/digitaldemocracy2030/idobata-analyst/pull/89)

**作成者:** spinute  
**作成日:** 2025-03-29T13:06:55Z  
**変更:** +41 -32 (3ファイル)  
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

### 過去30日間に更新されたPR（作成・マージを除く）(2件)

### [Feature/better embed](https://github.com/digitaldemocracy2030/idobata-analyst/pull/8)

**作成者:** jujunjun110  
**作成日:** 2025-03-04T15:33:20Z  
**変更:** +19 -5 (2ファイル)  
**内容:**

内容なし

**コメント:** なし

---

### [Feature/accept empty row in csv](https://github.com/digitaldemocracy2030/idobata-analyst/pull/3)

**作成者:** jujunjun110  
**作成日:** 2025-02-21T15:26:47Z  
**変更:** +2 -1 (1ファイル)  
**内容:**

@blu3mo 
空行が許容されないのが作業上手間が大きかったので変更しました！

**コメント:** なし

---

