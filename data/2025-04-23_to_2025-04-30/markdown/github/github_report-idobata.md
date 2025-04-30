# GitHub レポート: digitaldemocracy2030/idobata

期間: 2025-04-23T18:03:13.595970+09:00 から 2025-04-30T18:03:13.595970+09:00 まで

## Issues

### 過去7日間に完了されたissue (6件)

### [テーマ一覧のタップ可能エリアが小さすぎる](https://github.com/digitaldemocracy2030/idobata/issues/95)

**作成者:** jujunjun110  
**作成日:** 2025-04-29T23:39:38Z  
**内容:**

内容なし

**コメント:** なし

---

### [/frontend buildエラー（win）](https://github.com/digitaldemocracy2030/idobata/issues/88)

**作成者:** moai-redcap  
**作成日:** 2025-04-29T15:10:33Z  
**内容:**

## 問題

下記エラーにより /frontend のnpm build が失敗する。
```
src/components/chat/FloatingChat.tsx:1:8 - error TS6133: 'React' is declared but its value is never read.
src/components/chat/FloatingChat.tsx:3:3 - error TS6133: 'useEffect' is declared but its value is never read.
src/components/chat/FloatingChat.tsx:4:3 - error TS6133: 'useRef' is declared but its value is never read.
src/components/chat/FloatingChat.tsx:8:10 - error TS6133: 'ExtendedMessage' is declared but its value is never read.
src/ThemeContext.tsx:10:1 - error TS6133: 'Theme' is declared but its value is never read.
```
少なくともwin環境ではbuildに失敗してfrontendが表示されない。

## 修正方法の概要
buildコマンド内の`tsc -b`（tsのコンパイル）が前述のエラーによって止まってしまっている。
上記箇所の削除でこの問題はクリアできそう。

## 補足
npm dev はなんなく成功してしまうので気づきずらいかも。

**コメント:** なし

---

### [利用者がキークエスチョンを一目で理解できるように文章を簡潔にする](https://github.com/digitaldemocracy2030/idobata/issues/37)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-26T11:52:25Z  
**内容:**

# キークエスチョンの文章を簡潔にする

## 背景
現在のキークエスチョンは一文が長すぎて頭に入ってこないという指摘があります。例えば、「現状は、過去の政策の失敗経験や、特定分野への集中、国営企業の提案などに対する疑念、他党との類似性、国政で活動する理由の不明確さなどから、提案されている政策ビジョンの独自性や実現可能性、そして新党としての存在意義に対する国民の納得感が十分に得られていない。それを、過去の教訓を踏まえつつ、具体的で実現可能、かつ他とは明確に異なる独自のアプローチであることが国民に明確に伝わり、そのビジョンへの期待と信頼を集めるには、どうすればよいだろうか？」のような長文です。

## 改善内容
- キークエスチョンを簡潔な一文にまとめる
- 詳細な課題と解決の方向性は別項目として整理する
- 例：「現状はビジョンの納得感が低いが、期待と信頼を集めるにはどうすべきか？」のような形式に変更

## 期待される効果
利用者がキークエスチョンを一目で理解でき、レポートの可読性が向上します。

## 参考
Slackスレッド: https://app.slack.com/client/T0123456789/C0123456789/thread/C0123456789-1234567890.123456


**コメント:** なし

---

### [CI/CDを整備することでコードPush時に改変に問題あるコードが入り込みにくくする](https://github.com/digitaldemocracy2030/idobata/issues/24)

**作成者:** jujunjun110  
**作成日:** 2025-04-23T13:55:50Z  
**内容:**

内容なし

**コメント:** なし

---

### [読みやすさに特化したレポートを作成できるようにし、初めてそテーマを訪問した人の興味を満たせるようにする](https://github.com/digitaldemocracy2030/idobata/issues/15)

**作成者:** jujunjun110  
**作成日:** 2025-04-23T13:42:59Z  
**内容:**

内容なし

**コメント:** なし

---

### [プロジェクトをコンテナでビルドできるようにすることで、誰でも手元でデバッグ・開発ができるようにする](https://github.com/digitaldemocracy2030/idobata/issues/13)

**作成者:** jujunjun110  
**作成日:** 2025-04-23T13:35:15Z  
**内容:**

内容なし

**コメント:** なし

---

### 過去7日間に作成されたissue (23件)

### [各ホスティング主体が、サイト名や、aboutの文章を、管理画面から好きに変更できるようにする](https://github.com/digitaldemocracy2030/idobata/issues/91)

**作成者:** jujunjun110  
**作成日:** 2025-04-29T22:45:18Z  
**内容:**

内容なし

**コメント:** なし

---

### [現在のざっくりデザインを、デザインファイル通りのFineなデザインにアップデートする](https://github.com/digitaldemocracy2030/idobata/issues/85)

**作成者:** jujunjun110  
**作成日:** 2025-04-29T11:05:14Z  
**内容:**

https://www.figma.com/design/Td64AEvdk42ov6t6IPEvTN/DD2030?node-id=1465-1673&t=0RrmGA2O7ZC95tqH-4

**コメント:** なし

---

### [ワイヤフレームに存在する画面を一通り揃え、開発者がイメージを持ちやすくしつつ、開発を行う際の雛形を作成する(管理画面)](https://github.com/digitaldemocracy2030/idobata/issues/84)

**作成者:** jujunjun110  
**作成日:** 2025-04-29T10:46:28Z  
**内容:**

内容なし

**コメント:** なし

---

### [ホスティングの担当者が簡単にホスティングをできるように、クラウド環境で環境を構築するための仕組みを構築する](https://github.com/digitaldemocracy2030/idobata/issues/83)

**作成者:** jujunjun110  
**作成日:** 2025-04-29T10:42:05Z  
**内容:**

基本的にはIaaCを使うのが良いと思うがあえてHowを絞る必要はないかなと思ったので指定していない
GCPでまず動かせると良い


**コメント:** なし

---

### [issue test](https://github.com/digitaldemocracy2030/idobata/issues/80)

**作成者:** jujunjun110  
**作成日:** 2025-04-29T06:29:48Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### [ホスティング主体者が議論の段階に応じた適切なフィードバックを得られるように確信度レバーを実装する](https://github.com/digitaldemocracy2030/idobata/issues/57)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-27T13:32:12Z  
**内容:**

# 議論の確信度に応じたAI反論レベルの調整機能

## 概要
いどばた政策での議論において、運営側がAIの反論レベルを調整できる「確信度レバー」機能の追加を提案します。これにより、議論の段階や確信度に応じて、AIの反応を適切に調整することができます。

## 背景
現在のシステムでは、AIの反論レベルが固定されており、議論の段階や運営側の確信度に関わらず同じ反応をします。しかし、議論の初期段階では幅広い提案を集めたい場合と、ある程度方向性が定まってきた段階では反論を強めたい場合があります。

## 提案内容
- 運営者が調整できる「確信度レバー」UIを追加
- 確信度が低い設定：AIはより多くの提案を受け入れ、反論を控えめにする
- 確信度が高い設定：AIはより積極的に反論し、提案の問題点を指摘する

## 期待される効果
- 議論の段階に応じた適切なAI反応の調整が可能になる
- 初期段階では多様なアイデアを収集しやすくなる
- 後期段階では提案の問題点をより深く検討できるようになる

## Slackスレッド参照
このアイデアは以下のSlackスレッドで提案されました：
https://digitaldemocracy2030.slack.com/archives/C08FZDRQVS1/p1714307458000019

```
安野貴博 (U08FZDRRY8Z): • アイデアとして、いどばた政策で議論があった時に、どれだけ反論するか？　それともすぐに提案を作り始めるか？　の確信度レバーがあると良さそう
    ◦ あんまり確信度ない段階ではなるべく提案を広く集める　→　運営側の確信度が高くなってきたら比較的強めにAIに反論させるようにする
```


**コメント:** なし

---

### [ホスティング主体者がPRの可読性を高めるためにPR作成時の不要な改行や区切りを削除する](https://github.com/digitaldemocracy2030/idobata/issues/56)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-27T13:32:07Z  
**内容:**

# PRの最後に不要な改行や区切りが挿入される問題

## 問題の概要
いどばたが作成するPRの最後に、不要な改行や区切り（例：`---`）が挿入される傾向があります。これにより、PRの可読性が低下し、レビュー時に余計な注意が必要になっています。

## 再現例
以下のPRで問題が確認できます：
https://github.com/takahiroanno2024/2025_ai_idobatakaigi_output/pull/124/files

このPRでは、ファイルの最後に不要な改行と `---` が挿入されています。

## Slackスレッド
この問題は以下のSlackスレッドで報告されました：
https://digitaldemocracy2030.slack.com/archives/C06FZDRV0DP/p1714307430000000

## 期待される動作
PRを作成する際に、ファイルの最後に不要な改行や区切りが挿入されないようにする。


**コメント:** なし

---

### [シャープな問いの生成前にreasoningを入れることで、問いのクオリティを高めたい](https://github.com/digitaldemocracy2030/idobata/issues/50)

**作成者:** blu3mo  
**作成日:** 2025-04-27T09:33:58Z  
**内容:**

## 解決・改善したいこと

シャープな問いのクオリティを最大限高めるためにLLMを頑張らせたい。
LLMがシャープな問いを生成する前に、
- 10個候補を出させて、そのうちの5個を選ばせる
- 質問本文に加えて、詳細な課題説明とか詳細な理想像説明とかを書かせる
など

**コメント:** なし

---

### [利用者が正確な情報を得られるようにプレースホルダーの表示を修正する](https://github.com/digitaldemocracy2030/idobata/issues/41)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-26T11:54:05Z  
**内容:**

# プレースホルダーの表示を修正する

## 背景
現在のAIレポートでは、「計M個の提案」のように、プレースホルダーがそのまま表示されてしまう問題があります。

## 改善内容
- プレースホルダーを実際の数値に置き換える処理を実装する
- 数値が取得できない場合の代替表示を用意する

## 期待される効果
利用者が正確な情報を得られ、レポートの信頼性が向上します。

## 参考
Slackスレッド: https://app.slack.com/client/T0123456789/C0123456789/thread/C0123456789-1234567890.123456


**コメント:** なし

---

### [利用者が問題点の詳細に簡単にアクセスできるようにリンク機能を追加する](https://github.com/digitaldemocracy2030/idobata/issues/40)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-26T11:53:25Z  
**内容:**

# 問題点へのリンク機能を追加する

## 背景
現在のAIレポートでは、問題点にナンバーが振られているのは良いが、リンクが貼られていないという指摘があります。

## 改善内容
- 問題点の番号にリンクを追加する
- リンク先は該当する問題点の詳細情報や元のデータソースとする

## 期待される効果
利用者が問題点の詳細に簡単にアクセスでき、レポートの利便性が向上します。

## 参考
Slackスレッド: https://app.slack.com/client/T0123456789/C0123456789/thread/C0123456789-1234567890.123456


**コメント:** なし

---

### [利用者が重要な部分を視覚的に認識できるように太字フォーマットを修正する](https://github.com/digitaldemocracy2030/idobata/issues/39)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-26T11:53:15Z  
**内容:**

# 太字フォーマットの修正

## 背景
現在のAIレポートでは、「**共通の方向性（合意点）**」のように、太字がかっこつきだと適用されない問題があります。

## 改善内容
- Markdownの太字フォーマットが正しく適用されるように修正する
- かっこを含む場合でも太字が適用されるようにする

## 期待される効果
利用者が重要な部分を視覚的に認識しやすくなり、レポートの可読性が向上します。

## 参考
Slackスレッド: https://app.slack.com/client/T0123456789/C0123456789/thread/C0123456789-1234567890.123456


**コメント:** なし

---

### [利用者が具体的な行動指針を理解できるように曖昧な表現を具体的な提案に置き換える](https://github.com/digitaldemocracy2030/idobata/issues/38)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-26T11:53:05Z  
**内容:**

# 曖昧な表現を具体的な提案に置き換える

## 背景
現在のAIレポートでは、「多様な角度からの検証が必要です」「二元論を超えることが重要です」といった曖昧な表現で多くのイシューがまとめられています。具体的にどういうことなのかが分からないという指摘があります。

## 改善内容
- 「多様な角度から云々」をNGワードとして設定する
- 具体的なスタンスや提案を明確に示すようにする
- コンサルティング会社のように、敢えてスタンスを取る方針を採用する

## 期待される効果
利用者が具体的な行動指針を理解でき、レポートの実用性が向上します。

## 参考
Slackスレッド: https://app.slack.com/client/T0123456789/C0123456789/thread/C0123456789-1234567890.123456


**コメント:** なし

---

### [利用者がキークエスチョンの違いを明確に理解できるように差別化を強化する](https://github.com/digitaldemocracy2030/idobata/issues/36)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-26T11:52:16Z  
**内容:**

# キークエスチョンの差別化を強化する

## 背景
現在のAIレポートでは、キークエスチョンごとの差別化が弱く、意味的に重なっている部分が多いという指摘があります。課題と解決策を共有している度合いが大きいキークエスチョンは重なりを見てオミットしてもよいのではないかという提案もあります。

## 改善内容
- キークエスチョン間の重複を分析し、意味的に重なっている部分を特定する
- 重複度の高いキークエスチョンを統合または削除する判断基準を設ける
- 各キークエスチョンの独自性を明確にする

## 期待される効果
利用者がキークエスチョンの違いを明確に理解でき、レポートの価値が向上します。

## 参考
Slackスレッド: https://app.slack.com/client/T0123456789/C0123456789/thread/C0123456789-1234567890.123456


**コメント:** なし

---

### [レビュアーが効率的にレビューできるように差分を最小化する](https://github.com/digitaldemocracy2030/idobata/issues/35)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-26T11:41:58Z  
**内容:**

# 概要
いどばた政策のPRを見ていてのフィードバックとして、以下の点が指摘されています：
- 差分が大きいものが多い
- 中には無駄な差分もある気がする
- なるべく差分を最小化したいなと思った（レビューのためにも）
- 元の文をリスペクトする度合いをあげるようなプロンプトを考えてもよいかも

# 背景
レビューの効率化と品質向上のため、PRの差分を最小限に抑えることが重要です。現状では、必要以上に大きな差分が発生しているケースがあり、レビューの負担が増加しています。

# 提案
1. 元の文章をより尊重するようなプロンプトの改善
2. 不要な差分を生成しないようなロジックの見直し
3. 差分の最小化を意識した実装方針の策定

# 期待される効果
- レビュー時間の短縮
- レビュー品質の向上
- 元の文章の意図をより適切に保持
Slackスレッドのリンク: [#2_開発_いどばた](https://slack.com/app_redirect?channel=2_開発_いどばた)

このissueはSlackでの議論から作成されました。元の文脈を理解するために上記のスレッドを参照してください。


**コメント:** なし

---

### [PR作成についての挙動が不安定な部分を解消し、確実にPR Draftが保存されるようにする](https://github.com/digitaldemocracy2030/idobata/issues/23)

**作成者:** jujunjun110  
**作成日:** 2025-04-23T13:55:44Z  
**内容:**

内容なし

**コメント:** なし

---

### [参加者のチャットログを保存するようにして、どのような会話がされているかを運営者が理解できるようにする](https://github.com/digitaldemocracy2030/idobata/issues/22)

**作成者:** jujunjun110  
**作成日:** 2025-04-23T13:55:40Z  
**内容:**

内容なし

**コメント:** なし

---

### [レポートに対して貢献を紐づけ表示する機能を作ることで、参加者が議論に参加した意味を強く感じられるようにする](https://github.com/digitaldemocracy2030/idobata/issues/21)

**作成者:** jujunjun110  
**作成日:** 2025-04-23T13:55:36Z  
**内容:**

内容なし

**コメント:** なし

---

### [Googleログイン（OAuth）をつけることで、貢献などをユーザーに紐づけられるようにする](https://github.com/digitaldemocracy2030/idobata/issues/20)

**作成者:** jujunjun110  
**作成日:** 2025-04-23T13:55:32Z  
**内容:**

内容なし

**コメント:** なし

---

### [OGP画像を設定し、SNSでシェアしたときにサイトの魅力が閲覧者に伝わりやすくする](https://github.com/digitaldemocracy2030/idobata/issues/19)

**作成者:** jujunjun110  
**作成日:** 2025-04-23T13:55:28Z  
**内容:**

内容なし

**コメント:** なし

---

### [大量のPRが来た際に、適切にRejectする文言をAIが生成することで、PRマージ担当者が気まずい雰囲気なくRejectできるようにする](https://github.com/digitaldemocracy2030/idobata/issues/18)

**作成者:** jujunjun110  
**作成日:** 2025-04-23T13:55:20Z  
**内容:**

内容なし

**コメント:** なし

---

### [PRに対してファクトチェックを自動で行うことで、誤った前提のPRのマージを防ぎ、PR自体をよりエビデンスに基づくものにする](https://github.com/digitaldemocracy2030/idobata/issues/17)

**作成者:** jujunjun110  
**作成日:** 2025-04-23T13:55:16Z  
**内容:**

内容なし

**コメント:** なし

---

### [メールアドレスによるログインをつけることで、貢献などをユーザーに紐づけられるようにする](https://github.com/digitaldemocracy2030/idobata/issues/16)

**作成者:** jujunjun110  
**作成日:** 2025-04-23T13:55:12Z  
**内容:**

内容なし

**コメント:** なし

---

### [ワイヤフレームに存在する画面を一通り揃え、開発者がイメージを持ちやすくしつつ、開発を行う際の雛形を作成する(Phase1)](https://github.com/digitaldemocracy2030/idobata/issues/14)

**作成者:** jujunjun110  
**作成日:** 2025-04-23T13:41:01Z  
**内容:**

内容なし

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(1件)

### [【現状】Git知識が必要で非技術者が混乱 →【改善】専門用語の日本語化と直感的なワークフロー設計](https://github.com/digitaldemocracy2030/idobata/issues/6)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-22T09:25:07Z  
**内容:**

# 【現状】Git知識が必要で非技術者が混乱 →【改善】専門用語の日本語化と直感的なワークフロー設計

## 説明
現在のワークフローはGitの概念に精通していることを前提としており、非技術者ユーザーにとって混乱を招く可能性があります。

## 具体的なフィードバック
- "GitHub にマスターがあって、手元に下書きがあって、それを更新して完了したら PR にして、というフロー、Git がわかっているとスッと理解できるがそうでない人は混乱するかも"
- "GITHUBとかディスコースってなんか日本語でシンプルに言い換えれたらいいのかも"
- "私の認識では階層でプログラムぽいものが記載してる文字が細かく、たまにアクセスできなくなる謎サイトって感じなので"

## 改善案
- 非技術者ユーザー向けに用語を簡略化し、よりアクセスしやすい言語を使用する
- より直感的なUI要素の背後にGitの概念を抽象化する
- Gitの知識を必要とせずにワークフローをより明確に説明する
- 技術用語の日本語訳を検討する

## 期待される成果
非技術者ユーザーがGitの概念や用語を理解せずにシステムを効果的に使用できるようになる。

## 優先度
中 - ユーザー採用に影響するが、コア機能の使用を妨げるものではない


**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (30件)

### [QuestionDetail.tsxで実際のデータを取得するように実装](https://github.com/digitaldemocracy2030/idobata/pull/98)

**作成者:** jujunjun110+Devin  
**作成日:** 2025-04-30T00:48:11Z  
**変更:** +292 -87 (6ファイル)  
**マージ日:** 2025-04-30T02:32:26Z  
**内容:**

内容なし

**コメント:** なし

---

### [Update: question Link](https://github.com/digitaldemocracy2030/idobata/pull/97)

**作成者:** jujunjun110  
**作成日:** 2025-04-30T00:29:22Z  
**変更:** +111 -75 (6ファイル)  
**マージ日:** 2025-04-30T00:29:28Z  
**内容:**

# 変更の概要
* シャープな問一覧へのリンクをつけた
* テーマへのリンクのクリックしにくさを解消

# スクリーンショット
![image](https://github.com/user-attachments/assets/2b450ce3-52dc-43f7-974e-a54c99a220e3)


# 変更の背景
リンク付け忘れ

# 関連Issue
https://github.com/digitaldemocracy2030/idobata/issues/95

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Update: frontendでもmongoに合わせて_idを使うようにした](https://github.com/digitaldemocracy2030/idobata/pull/96)

**作成者:** jujunjun110  
**作成日:** 2025-04-30T00:22:23Z  
**変更:** +16 -16 (8ファイル)  
**マージ日:** 2025-04-30T00:22:29Z  
**内容:**

# 変更の概要
* mongoではデフォルトで_idを使う
* 既存実装もある中、idに毎回変更するのはコストが高いので、このPJでは既存実装に合わせてfrontendでも_idを使うようにした
* 型もあるし、それほど後戻り不可能な意思決定ではない認識

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Feature/theme detail](https://github.com/digitaldemocracy2030/idobata/pull/94)

**作成者:** jujunjun110  
**作成日:** 2025-04-29T23:37:44Z  
**変更:** +855 -124 (16ファイル)  
**マージ日:** 2025-04-29T23:45:11Z  
**内容:**

# 変更の概要
* テーマ詳細ページでもデータをつなぎこんだ
* モック用のページも一応残しておいた

# スクリーンショット
![image](https://github.com/user-attachments/assets/6ba43834-3e1e-45ee-b180-236111f084b6)
![image](https://github.com/user-attachments/assets/134a445a-6683-4bef-b8ee-72732c9209ed)


# 変更の背景
* データのつなぎ込み

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [ハンバーガーメニューでもテーマ一覧表示](https://github.com/digitaldemocracy2030/idobata/pull/92)

**作成者:** jujunjun110  
**作成日:** 2025-04-29T22:50:04Z  
**変更:** +72 -30 (3ファイル)  
**マージ日:** 2025-04-29T22:50:12Z  
**内容:**

# 変更の概要
* ハンバーガーメニューでもテーマ一覧表示

# スクリーンショット
<img width="394" alt="image" src="https://github.com/user-attachments/assets/941b4cba-0771-4da5-b4b0-a5aea84558d2" />


# 変更の背景
つなぎこみ

# 関連Issue
タスクとしてはない

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [テーマ一覧ページでテーマ一覧を表示](https://github.com/digitaldemocracy2030/idobata/pull/90)

**作成者:** jujunjun110  
**作成日:** 2025-04-29T22:38:58Z  
**変更:** +361 -65 (4ファイル)  
**マージ日:** 2025-04-29T22:40:29Z  
**内容:**

# 変更の概要
テーマ一覧ページでテーマ一覧を表示

# スクリーンショット
<img width="404" alt="image" src="https://github.com/user-attachments/assets/fc933933-b0e2-47f1-9ca4-25d02969bb1b" />


# 変更の背景
実データのつなぎ込み

# 関連Issue
なし

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [型チェック用の npm コマンドを準備し、既存のエラーを修正し、CI に型チェックを追加した](https://github.com/digitaldemocracy2030/idobata/pull/89)

**作成者:** spinute  
**作成日:** 2025-04-29T15:50:16Z  
**変更:** +13 -14 (11ファイル)  
**マージ日:** 2025-04-29T15:51:54Z  
**内容:**

# 変更の概要
- npm run typecheck を追加
    - idea-discussion-backend だけは ts 未対応
- typecheck のエラーを修正
- ci に typecheck を追加

# 関連Issue
Resolve https://github.com/digitaldemocracy2030/idobata/issues/88

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [ドキュメントに figma へのリンクを追加した](https://github.com/digitaldemocracy2030/idobata/pull/87)

**作成者:** spinute  
**作成日:** 2025-04-29T11:55:56Z  
**変更:** +1 -0 (1ファイル)  
**マージ日:** 2025-04-29T13:22:11Z  
**内容:**

# 変更の概要
ドキュメントに figma へのリンクを追加した

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [docs ディレクトリにドキュメントをまとめる](https://github.com/digitaldemocracy2030/idobata/pull/86)

**作成者:** spinute  
**作成日:** 2025-04-29T11:54:44Z  
**変更:** +3 -3 (4ファイル)  
**マージ日:** 2025-04-29T13:22:08Z  
**内容:**

# 変更の概要
project_status.md, developement-setup.md, CONTRIBUTION.md を docs ディレクトリにまとめた

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [イシューの自動プロジェクト追加先をプロジェクト#6に変更](https://github.com/digitaldemocracy2030/idobata/pull/82)

**作成者:** jujunjun110+Devin  
**作成日:** 2025-04-29T06:49:43Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-04-29T06:54:02Z  
**内容:**

# イシューの自動プロジェクト追加先を変更

## 変更内容
GitHub Actionsのワークフローファイル `.github/workflows/auto-add-issue-to-project.yml` で、新しいイシューが追加されるプロジェクト番号を1から6に変更しました。

## 理由
現在、新しいイシューが古いプロジェクト（#1）に自動的に追加されていますが、本来は新しいプロジェクト（#6）に追加されるべきです。この変更により、新しいイシューは正しいプロジェクトに自動追加されるようになります。

## テスト方法
この変更後、新しく作成されたイシューがプロジェクト#6に自動的に追加されることを確認できます。

Link to Devin run: https://app.devin.ai/sessions/d59e3470d3a245fca3d79b21a44678ea
Requested by: jujunjun110@gmail.com


**コメント:** なし

---

### [Add @biomejs/biome to policy-edit/frontend](https://github.com/digitaldemocracy2030/idobata/pull/79)

**作成者:** jujunjun110+Devin  
**作成日:** 2025-04-29T05:27:06Z  
**変更:** +1 -0 (1ファイル)  
**マージ日:** 2025-04-29T05:53:34Z  
**内容:**

# Add @biomejs/biome to policy-edit/frontend

This PR adds the @biomejs/biome package as a devDependency to the policy-edit/frontend package.json file. The package.json already had the lint and format scripts referencing biome, but the dependency itself was missing.

## Changes
- Added @biomejs/biome as a devDependency in policy-edit/frontend/package.json

## Testing
- Added @biomejs/biome to package.json to ensure it can be installed with npm install

## Link to Devin run
https://app.devin.ai/sessions/b7521d21cb584b3785a6f101812185e1

Requested by: jujunjun110@gmail.com


**コメント:** なし

---

### [管理画面ログイン機能の実装](https://github.com/digitaldemocracy2030/idobata/pull/78)

**作成者:** jujunjun110+Devin  
**作成日:** 2025-04-29T04:06:20Z  
**変更:** +3103 -37 (24ファイル)  
**マージ日:** 2025-04-29T06:38:27Z  
**内容:**

# 管理画面ログイン機能の実装

## 概要
管理画面ログイン機能を実装しました。メールアドレスとパスワードによる認証を行い、将来的にGoogle OAuth認証も追加できるように拡張性を持たせています。

## 実装内容
### バックエンド
- AdminUserモデル（パスワードハッシュ化、ロール管理）
- 認証サービス（JWT生成、検証）
- 認証コントローラー（ログイン、ユーザー情報取得）
- 認証ミドルウェア（保護されたルート、権限チェック）
- 初期管理者ユーザー作成エンドポイント

### フロントエンド
- 認証コンテキスト（ログイン状態管理）
- ログインページ
- 保護されたルートコンポーネント
- APIクライアント拡張

## テスト結果
- 初期管理者ユーザーの作成: ✅
- ログイン認証: ✅
- 保護されたルートへのアクセス: ✅
- 未認証時のリダイレクト: ✅

## 環境変数の設定
以下の環境変数が必要です：
- JWT_SECRET: JWTトークン生成用の秘密鍵
- JWT_EXPIRES_IN: トークンの有効期限（例: 1d）
- PASSWORD_PEPPER: パスワードハッシュ化用のペッパー値

## 注意点
初期管理者ユーザーを作成するには以下のAPIを使用します：
```
curl -X POST http://[サーバーのホスト名]:3000/api/auth/initialize \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"SecurePassword123","name":"Admin User"}'
```

## Link to Devin run
https://app.devin.ai/sessions/ff233ffe90184c0db5a521026cd6f9aa

## Requested by
jujunjun110@gmail.com


**コメント:** なし

---

### [feat: Configure allowedHosts for Vite from root .env variables](https://github.com/digitaldemocracy2030/idobata/pull/77)

**作成者:** Shutaro Aoyama+Devin  
**作成日:** 2025-04-29T03:04:46Z  
**変更:** +10 -1 (4ファイル)  
**マージ日:** 2025-04-29T03:14:17Z  
**内容:**

# Configure allowedHosts for Vite from root .env variables

## 変更内容
- フロントエンドとポリシー編集フロントエンドの両方で、Vite configのallowedHostsをrootの.envファイルから設定できるように変更しました。
- それぞれ別々の環境変数（VITE_FRONTEND_ALLOWED_HOSTSとVITE_POLICY_FRONTEND_ALLOWED_HOSTS）を使用しています。
- docker-compose.ymlファイルを更新して、これらの環境変数をコンテナに渡すようにしました。

## 使用方法
`.env`ファイルに以下の環境変数を追加することで、許可するホストを設定できます：
```
VITE_FRONTEND_ALLOWED_HOSTS=localhost,127.0.0.1
VITE_POLICY_FRONTEND_ALLOWED_HOSTS=localhost,127.0.0.1
```

カンマ区切りで複数のホストを指定できます。

## Link to Devin run
https://app.devin.ai/sessions/7a8c170d271846bc9facac28bbe522ec

## Requested by
Shutaro Aoyama (shutaro.aoyama@gmail.com)


**コメント:** なし

---

### [Refactor: Configure separate CORS_ORIGIN variables for each backend from root .env](https://github.com/digitaldemocracy2030/idobata/pull/76)

**作成者:** Shutaro Aoyama+Devin  
**作成日:** 2025-04-29T02:50:49Z  
**変更:** +8 -4 (3ファイル)  
**マージ日:** 2025-04-29T02:57:09Z  
**内容:**

# CORS_ORIGINをルートの.envファイルから設定できるようにする

## 変更内容
- policy-editバックエンドでPOLICY_CORS_ORIGINをルートの.envファイルから読み込むように変更
- idea-discussionバックエンドでIDEA_CORS_ORIGINをルートの.envファイルから読み込むように変更
- docker-compose.ymlを更新して各バックエンドに適切なCORS環境変数を渡すように修正
- .env.templateファイルのCORS設定を更新（実際の.envファイルは.gitignoreされているため含まれていません）

## 検証方法
1. .envファイルでIDEA_CORS_ORIGINとPOLICY_CORS_ORIGINを設定
2. docker-compose upで環境を起動
3. 両バックエンドのログでCORS設定が正しく読み込まれていることを確認

## 技術的詳細
- policy-edit: config.tsでルートの.envファイルを読み込み、POLICY_CORS_ORIGINを使用
- idea-discussion: server.jsでIDEA_CORS_ORIGINを使用し、カンマ区切りで複数オリジンをサポート
- 両バックエンドとも、環境変数が設定されていない場合はデフォルト値を使用

Link to Devin run: https://app.devin.ai/sessions/255b366632de47b98bc0356387f14c33
Requested by: Shutaro Aoyama


**コメント:** なし

---

### [Feature/documentation](https://github.com/digitaldemocracy2030/idobata/pull/75)

**作成者:** jujunjun110  
**作成日:** 2025-04-29T02:48:04Z  
**変更:** +443 -126 (6ファイル)  
**マージ日:** 2025-04-29T10:19:06Z  
**内容:**

# 変更の概要
- 開発に貢献いただける方がより理解しやすいよう現在のPJ状況にまつわる内容をドキュメンテーション
- 現在Google Docsに同様のものがあるが、github管理のほうが各種AIが読みやすいので、こちらを正としようと思っています。

# 変更の背景
- PJの骨格が整ってきている


# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ｘ] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Add: 管理画面実装](https://github.com/digitaldemocracy2030/idobata/pull/74)

**作成者:** jujunjun110+Devin  
**作成日:** 2025-04-28T16:35:52Z  
**変更:** +1666 -8 (35ファイル)  
**マージ日:** 2025-04-29T01:19:25Z  
**内容:**

# 管理画面実装

## 概要
idea-discussionアプリケーションのテーマを管理するための管理画面を実装しました。管理画面は既存のアプリケーションと並んでdocker-compose.ymlに追加される別のアプリケーションとして実装されています。

## 実装した機能
- ダッシュボード表示
- テーマ一覧表示
- テーマ作成フォーム
- テーマ編集フォーム
- テーマ削除機能

## 技術スタック
- React 19
- TypeScript
- Vite 6
- Tailwind CSS 3.x
- React Router v7
- neverthrow (エラーハンドリング)

## 修正した問題点
1. Docker設定の問題: バックエンドのボリュームマウントが正しくなかったため、APIルートが正しく読み込まれていませんでした。
2. CORS設定: バックエンドのCORS設定を更新して、管理画面からのリクエストを許可するようにしました。
3. Tailwind CSS 3系: 要件通りTailwind CSS 3系を使用するように設定を変更しました。

## テスト済み機能
- テーマの作成、表示、編集、削除の全機能が正常に動作することを確認しました。
- バックエンドAPIとの接続も正常に機能しています。

## Link to Devin run
https://app.devin.ai/sessions/4d8f2936ed3f43d0bf1a66016d7e3a40

Requested by: jujunjun110@gmail.com


**コメント:** なし

---

### [Update: マイページ一覧](https://github.com/digitaldemocracy2030/idobata/pull/73)

**作成者:** jujunjun110  
**作成日:** 2025-04-28T15:21:53Z  
**変更:** +141 -104 (2ファイル)  
**マージ日:** 2025-04-28T15:25:41Z  
**内容:**

# 変更の概要
テーマ一覧へのリンク追加

# スクリーンショット
![image](https://github.com/user-attachments/assets/f43df93e-0f4e-4d77-91b9-7b2d4a53c5f2)
# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
遷移しにくかったため

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [update biome settings in vscode](https://github.com/digitaldemocracy2030/idobata/pull/70)

**作成者:** spinute  
**作成日:** 2025-04-28T02:51:04Z  
**変更:** +20 -3 (1ファイル)  
**マージ日:** 2025-04-28T02:51:09Z  
**内容:**

# 変更の概要
update biome settings in vscode

stop using prettier explicitly

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [remove remaining settings for eslint and prettier after introducing biome](https://github.com/digitaldemocracy2030/idobata/pull/69)

**作成者:** spinute  
**作成日:** 2025-04-28T02:44:59Z  
**変更:** +0 -29 (2ファイル)  
**マージ日:** 2025-04-28T02:45:15Z  
**内容:**

# 変更の概要
remove remaining settings for eslint and prettier after introducing biome

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [frontendディレクトリのlint/formatをBiomeに統一](https://github.com/digitaldemocracy2030/idobata/pull/68)

**作成者:** jujunjun110+Devin  
**作成日:** 2025-04-28T01:28:14Z  
**変更:** +0 -72 (2ファイル)  
**マージ日:** 2025-04-28T02:02:28Z  
**内容:**

# frontendディレクトリのlint/formatをBiomeに統一

## 変更内容
- frontendディレクトリからESLintとPrettierの設定ファイルを削除
- Biomeの設定をfrontendのコードスタイルに合わせて更新（シングルクォートを使用）
- Biomeの設定に一部のESLintルールに相当する設定を追加
- 非コードファイル（MD、SVG、PNGなど）をBiomeの対象から除外

## 検証方法
- `npx biome check .` コマンドでlintエラーがないことを確認
- `npx biome check --write .` コマンドでフォーマットが適用されることを確認

Link to Devin run: https://app.devin.ai/sessions/1a45309ddcda4caebe20c4521c75a52e
By: jujunjun110@gmail.com


**コメント:** なし

---

### [問い個別ページの実装](https://github.com/digitaldemocracy2030/idobata/pull/67)

**作成者:** jujunjun110+Devin  
**作成日:** 2025-04-28T00:32:08Z  
**変更:** +440 -0 (6ファイル)  
**マージ日:** 2025-04-28T01:04:51Z  
**内容:**

# 問い個別ページの実装

問い個別ページ（/themes/{themeId}/questions/{qId}）の実装を行いました。

## 実装内容
- パンクズ表示対応
- キークエスチョン・議論サマリー・意見一覧をコンポーネント化
- モバイルファースト対応
- タブ切り替えの実装
- 市民意見レポート例の表示

## 関連コンポーネント
- KeyQuestionHeader
- DebateSummary
- OpinionCard
- CitizenReportExample

Link to Devin run: https://app.devin.ai/sessions/922dfb24ef504828b70358b551c5e27e
Requested by: jujunjun110@gmail.com


**コメント:** なし

---

### [テストの例をいくつか書いた](https://github.com/digitaldemocracy2030/idobata/pull/66)

**作成者:** spinute  
**作成日:** 2025-04-27T20:24:01Z  
**変更:** +606 -0 (3ファイル)  
**マージ日:** 2025-04-27T20:26:29Z  
**内容:**

# 変更の概要

https://github.com/digitaldemocracy2030/idobata/pull/62 で vitest を入れたのでテストの例をいくつか書いた（AI に書かせた）

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [add missing changes in package-lock.json](https://github.com/digitaldemocracy2030/idobata/pull/65)

**作成者:** spinute  
**作成日:** 2025-04-27T19:54:06Z  
**変更:** +409 -1 (1ファイル)  
**マージ日:** 2025-04-27T19:54:32Z  
**内容:**

# 変更の概要

https://github.com/digitaldemocracy2030/idobata/pull/62 で package-lock.json の差分を入れ忘れていたので入れた

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [apply biome to migrateToThemes.js and fix comments](https://github.com/digitaldemocracy2030/idobata/pull/64)

**作成者:** spinute  
**作成日:** 2025-04-27T19:49:32Z  
**変更:** +3 -2 (1ファイル)  
**マージ日:** 2025-04-27T19:51:51Z  
**内容:**

# 変更の概要
migrateToThemes.js に formatter が当たっていなかったので適用した

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました


**コメント:** なし

---

### [add missing changes in fix makefile](https://github.com/digitaldemocracy2030/idobata/pull/63)

**作成者:** spinute  
**作成日:** 2025-04-27T19:45:29Z  
**変更:** +3 -3 (1ファイル)  
**マージ日:** 2025-04-27T19:46:12Z  
**内容:**

# 変更の概要
https://github.com/digitaldemocracy2030/idobata/pull/58 の変更を反映し漏れていたので追加

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [add vitest and refactor package.jsons](https://github.com/digitaldemocracy2030/idobata/pull/62)

**作成者:** spinute  
**作成日:** 2025-04-27T19:40:46Z  
**変更:** +438 -24 (8ファイル)  
**マージ日:** 2025-04-27T19:41:44Z  
**内容:**

# 変更の概要

- vitest を導入した
- package.json をリファクタリングした

# 関連Issue
https://github.com/digitaldemocracy2030/idobata/issues/24

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Feat/biome format again](https://github.com/digitaldemocracy2030/idobata/pull/61)

**作成者:** spinute  
**作成日:** 2025-04-27T19:21:25Z  
**変更:** +5135 -3936 (120ファイル)  
**マージ日:** 2025-04-27T19:21:42Z  
**内容:**

# 変更の概要
https://github.com/digitaldemocracy2030/idobata/pull/46 の再チャレンジ

https://github.com/digitaldemocracy2030/idobata/pull/42 で入れた biome の lint を一通り通した。
（そのため、https://github.com/digitaldemocracy2030/idobata/pull/42 の後でマージする想定）

自動で修正できるものを自動で修正したあと、自動で修正できないものを AI に出力を見せてザクザク修正した。

# 関連Issue
#24 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [policy-edit/mcp/.env.example は多分もういらないので消した](https://github.com/digitaldemocracy2030/idobata/pull/59)

**作成者:** spinute  
**作成日:** 2025-04-27T17:51:00Z  
**変更:** +0 -15 (1ファイル)  
**マージ日:** 2025-04-27T17:51:14Z  
**内容:**

# 変更の概要
policy-edit/mcp/.env.example は多分もういらないので消した

コンテナ・モノレポ化する前のものが残っているっぽい気がする

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました


**コメント:** なし

---

### [makefile を追加した](https://github.com/digitaldemocracy2030/idobata/pull/58)

**作成者:** spinute  
**作成日:** 2025-04-27T17:48:52Z  
**変更:** +63 -0 (1ファイル)  
**マージ日:** 2025-04-27T17:51:10Z  
**内容:**

# 変更の概要
makefile を追加した

アプリケーションの挙動や見た目には影響しない

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Feature/refactoring chat UI](https://github.com/digitaldemocracy2030/idobata/pull/55)

**作成者:** jujunjun110  
**作成日:** 2025-04-27T13:25:36Z  
**変更:** +111 -126 (5ファイル)  
**マージ日:** 2025-04-27T13:25:44Z  
**内容:**

# 変更の概要
* chatのsheetとhamburgerのsheetに過度な抽象化があったので適切に分けた

# スクリーンショット
UIは変更ないｓ

# 変更の背景
* 設計が悪かった

# 関連Issue
なし

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### 過去7日間に作成されたPR (4件)

### [.env.templateの補足追加](https://github.com/digitaldemocracy2030/idobata/pull/93)

**作成者:** itoma-aikon  
**作成日:** 2025-04-29T23:24:53Z  
**変更:** +43 -5 (1ファイル)  
**内容:**

# 変更の概要
.env.templateの補足追加




# 変更の背景
github appの設定項目などで苦労したため

# 関連Issue
https://github.com/digitaldemocracy2030/idobata/pull/1

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Security Enhancement: HttpOnly Cookie Authentication and CSRF Protection](https://github.com/digitaldemocracy2030/idobata/pull/81)

**作成者:** jujunjun110+Devin  
**作成日:** 2025-04-29T06:41:08Z  
**変更:** +179 -88 (10ファイル)  
**内容:**

# セキュリティ向上: HttpOnly Cookie認証とCSRF保護

## 変更内容

管理画面のセキュリティを向上させる対策として、以下の実装を行いました:

1. **HttpOnly Cookie認証の実装**:
   - JWTトークンをlocalStorageからHttpOnly Cookieに移行
   - XSS攻撃からの保護強化

2. **CSRF保護の追加**:
   - csrf-csrfライブラリを使用
   - 二重送信クッキーパターンによる保護実装

## 環境変数

以下の環境変数の追加が必要です:

```
COOKIE_SECRET=your-secure-cookie-secret
CSRF_SECRET=your-secure-csrf-secret
```

## テスト結果
    
ローカル環境で以下の機能をテストし、正常に動作することを確認しました:
- ログイン機能
- 認証が必要なページへのアクセス
- ログアウト機能

Link to Devin run: https://app.devin.ai/sessions/d6fa47bde7734a388e590b56dbfe2ef0
Requested by: jujunjun110@gmail.com


**コメント:** なし

---

### [チャット機能と論点抽出機能の実装](https://github.com/digitaldemocracy2030/idobata/pull/72)

**作成者:** jujunjun110+Devin  
**作成日:** 2025-04-28T04:53:46Z  
**変更:** +1475 -127 (17ファイル)  
**内容:**

# チャット機能と論点抽出機能の実装

旧UIである `MainPage.tsx` で実現できているチャットによる意見表明と論点抽出を、新UIである `ThemeDetail.tsx` からも同様にできるように実装しました。

## 実装内容

1. 既存の `FloatingChat` コンポーネントを使用してチャット機能を拡張
2. スレッドIDとユーザーIDの管理機能を追加
3. APIクライアントを使用したメッセージ送信と抽出結果の取得
4. 抽出結果の定期的なチェック機能
5. 通知表示機能
6. 抽出結果の表示/非表示切り替え機能
7. `ThreadExtractions` コンポーネントの統合

## 変更点

- `ThemeDetail.tsx` に必要な状態管理とAPIとの連携を追加
- 抽出結果の表示領域とトグルボタンを追加
- 通知表示機能を実装

Link to Devin run: https://app.devin.ai/sessions/907b6c7c9e674be8882af0b5faa179ac
Requested by: jujunjun110@gmail.com


**コメント:** なし

---

### [Add chat extraction implementation task document](https://github.com/digitaldemocracy2030/idobata/pull/71)

**作成者:** jujunjun110+Devin  
**作成日:** 2025-04-28T04:38:14Z  
**変更:** +361 -0 (1ファイル)  
**内容:**

# チャット機能と論点抽出機能の実装手順書

旧UIである MainPage.tsx で実現できているチャットによる意見表明と論点抽出を、新UIである ThemeDetail.tsx からも同様にできるようにするための手順書を追加しました。

## 変更内容

- frontend/project/chat-extraction-implementation-task.md を追加
- 10ステップの実装手順を記載
- 実装時の注意点を記載

Link to Devin run: https://app.devin.ai/sessions/907b6c7c9e674be8882af0b5faa179ac
Requested by: jujunjun110@gmail.com


**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [readmeの作成と.env.exampleの作成](https://github.com/digitaldemocracy2030/idobata/pull/1)

**作成者:** itoma-aikon  
**作成日:** 2025-04-20T09:37:09Z  
**変更:** +161 -0 (3ファイル)  
**内容:**

readmeと.env.exampleを追加してセットアップをしやすくしました

**コメント:** なし

---

