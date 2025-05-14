# GitHub レポート: digitaldemocracy2030/idobata

期間: 2025-05-07T17:37:24.496804+09:00 から 2025-05-14T17:37:24.496804+09:00 まで

## Issues

### 過去7日間に完了されたissue (4件)

### [個人情報生成と除去率測定の機能追加](https://github.com/digitaldemocracy2030/idobata/issues/280)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-05-13T09:29:36Z  
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

### [Issuesを自動的にProjectに追加する](https://github.com/digitaldemocracy2030/idobata/issues/278)

**作成者:** masatosasano2  
**作成日:** 2025-05-10T22:43:20Z  
**内容:**

自動化することでProjectボードで管理した場合の漏れを防止したい。

参考実装（いどばた）
https://github.com/digitaldemocracy2030/idobata/blob/main/.github/workflows/auto-add-issue-to-project.yml


**コメント:** なし

---

### [[チャット][UI] Shift+Enterで改行したい](https://github.com/digitaldemocracy2030/idobata/issues/256)

**作成者:** masatosasano2  
**作成日:** 2025-05-09T12:44:15Z  
**内容:**

## 解決・改善したいこと

Shift+Enterで改行したい

## 要検討

Enterで改行、Ctrl + Enter で送信したい派閥もいる


**コメント:** なし

---

### [「もっと見る」も他のButtonコンポーネントと同じスタイルに](https://github.com/digitaldemocracy2030/idobata/issues/131)

**作成者:** moai-redcap  
**作成日:** 2025-05-01T16:28:17Z  
**内容:**

## 解決・改善したいこと
ボタンであることを認識しやすくし、
また大切なボタン（Deleteやlogout）でないことをわかりやすくするために、
極力ボタンのstyleを少なくしたい

## 具体的な実現方法・実装方法の概要（未記入でも構いません）
「もっと見る」ボタンのスタイルを他のButtonコンポーネントと同じスタイルに

**コメント:** なし

---

### 過去7日間に作成されたissue (21件)

### [チュートリアルがほしい](https://github.com/digitaldemocracy2030/idobata/issues/277)

**作成者:** masatosasano2  
**作成日:** 2025-05-10T12:10:08Z  
**内容:**

## 解決・改善したいこと

- いどばた自体のコンセプトや使い方の説明がいどばたの機能外（体験会のファシリテーター）でなされた
- 機能でカバーできているとよい

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

- 初回利用時のツアー機能
- ヘルプアイコン
- この製品について、とか操作マニュアルのページをメニューに追加

**コメント:** なし

---

### [ロシア語表記が出る](https://github.com/digitaldemocracy2030/idobata/issues/276)

**作成者:** masatosasano2  
**作成日:** 2025-05-10T12:07:13Z  
**内容:**

## 問題

ロシア語表記が表示されることがある（5/9体験会の会話より、詳細不明）

## 修正方法の概要

- 言語設定・i18nの確認と修正

**コメント:** なし

---

### [「気になる」ボタンの活用](https://github.com/digitaldemocracy2030/idobata/issues/275)

**作成者:** masatosasano2  
**作成日:** 2025-05-10T12:05:04Z  
**内容:**

## 解決・改善したいこと

- カウントアップだけされているが、それ以上に活用されてなさそう

## 具体的な実現方法・実装方法の概要

- フィルタ、ソートできるようにする？
- 課題点や解決策も同様のことが言えそう

**コメント:** なし

---

### [[チャット] 新しい投稿が下に表示されるのは直感に反する](https://github.com/digitaldemocracy2030/idobata/issues/274)

**作成者:** masatosasano2  
**作成日:** 2025-05-10T12:02:08Z  
**内容:**

## 解決・改善したいこと

- 新しいものは上に来てほしいという声が5/9の体験会で上がった
- 流派がありそう

## 具体的な実現方法・実装方法の概要

-  時系列や重要度によるソート機能

**コメント:** なし

---

### [[UI][チャット]「話題を変える」ボタンをもっと目立たせたい](https://github.com/digitaldemocracy2030/idobata/issues/273)

**作成者:** masatosasano2  
**作成日:** 2025-05-10T12:00:00Z  
**内容:**

## 解決・改善したいこと

- 機能はいいが初見で気付きにくい

## 具体的な実現方法・実装方法の概要

- より目立つ配色やフォントにする
- チャット欄の右上（入力欄外）ではなく、入力欄の中に配置する

**コメント:** なし

---

### [[UI]プロフィール保存が失敗したことがわからない](https://github.com/digitaldemocracy2030/idobata/issues/272)

**作成者:** masatosasano2  
**作成日:** 2025-05-10T11:56:45Z  
**内容:**

## 解決・改善したいこと

-「保存ボタン」を押した結果、保存が成功したのかどうかがわかりにくい
- 関連Issue: #264 

## 具体的な実現方法・実装方法の概要

- 成功/失敗のメッセージをトースターか何かで表示する
- 失敗時はできれば原因も知りたい


**コメント:** なし

---

### [タブUIのキーボード操作での振る舞いなどを改善したい](https://github.com/digitaldemocracy2030/idobata/issues/271)

**作成者:** yusasa16  
**作成日:** 2025-05-10T10:52:09Z  
**内容:**

## 解決・改善したいこと

現在、タブの切り替えはマウス操作のみ対応しており、キーボードユーザーやスクリーンリーダーユーザーにとって操作性が低いため、改善したい。

対象ページは下記。

- /themes/{tid}/
- /themes/{tid}/questions/{qid}
- /themes/{tid}/questions/{qid}/comments


共通化するイシューが立てられているため、こちらが完了次第取り掛かりたい。

#228 

## 具体的な実現方法・実装方法の概要（未記入でも構いません）
ARIA Authoring Practices Guide (APG)で紹介されている[Example of Tabs with Manual Activation](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/examples/tabs-manual/)を参考に実装する。

**コメント:** なし

---

### [同期的に意見収集するイベントではフェーズ変更時に会話をリセットさせたい](https://github.com/digitaldemocracy2030/idobata/issues/270)

**作成者:** masatosasano2  
**作成日:** 2025-05-09T13:45:39Z  
**内容:**

## 解決・改善したいこと

チャットタイム > 分析 > 分析結果からテーマを絞る > チャットタイム > 分析 > ...

というイベントの例だと、テーマを絞るタイミングで参加者のチャットがクリアされると参加者にとって余分な情報に惑わされずに最新テーマにフォーカスしやすくなる。

## 具体的な実現方法・実装方法の概要


**コメント:** なし

---

### [[チャット] 複数画面でチャットできるが、役割が同じであることが確信できない](https://github.com/digitaldemocracy2030/idobata/issues/269)

**作成者:** masatosasano2  
**作成日:** 2025-05-09T13:38:01Z  
**内容:**

## 解決・改善したいこと

- 同じコメントを異なる画面で投稿するとレスポンスが変わるんだろうか、と余計なことが気になる
- 実害はあまりない

## 具体的な実現方法・実装方法の概要

**コメント:** なし

---

### [[UI] 重要論点のタグの役割や機能が分かりにくい](https://github.com/digitaldemocracy2030/idobata/issues/268)

**作成者:** masatosasano2  
**作成日:** 2025-05-09T13:36:14Z  
**内容:**

## 解決・改善したいこと

- 一見、クリックするとそのタグでフィルタリングされた論点等が一覧化されそうだが、そうはならず、重要論点のページに遷移する
- おそらく重要論点の中のサブ論点の一部が一言で表現されている？がそうと分かりにくい

## 具体的な実現方法・実装方法の概要

こんなのどうでしょう
> ### **重要論点**
> 　説明文説明文説明文説明文説明文説明文
> ┗サブ論点　┗サブ論点

**コメント:** なし

---

### [[テーマ][レポート] 前回閲覧時からの差分を知りたい](https://github.com/digitaldemocracy2030/idobata/issues/267)

**作成者:** masatosasano2  
**作成日:** 2025-05-09T13:30:15Z  
**内容:**

## 解決・改善したいこと

情報量が多いので、同じテーマページやレポートページを見た時に前回閲覧時から変わったところだけを拾って見たい。

## 具体的な実現方法・実装方法の概要

- 更新履歴管理
- 閲覧履歴管理
- 差分の可視化
    - ハイライトとか？
        - 伝わるだろうか
        - イラストとは干渉しそう

**コメント:** なし

---

### [[いどばたビジョン][UI] 課題点や解決策の右にある数字の意味が分かりにくい](https://github.com/digitaldemocracy2030/idobata/issues/266)

**作成者:** masatosasano2  
**作成日:** 2025-05-09T13:25:22Z  
**内容:**

## 解決・改善したいこと

- 単純に課題や解決策の数を表している
- が、確かに「関連度」や「気になる」と異なり何の数字なのか明示はされていない

## 具体的な実現方法・実装方法の概要

- 「個」と書くとか？


**コメント:** なし

---

### [課題点や解決策の数が他テーマの内容を含んで集計されてしまう](https://github.com/digitaldemocracy2030/idobata/issues/265)

**作成者:** masatosasano2  
**作成日:** 2025-05-09T13:20:05Z  
**内容:**

## 問題

- 課題点や解決策の数が他テーマの内容を含んで集計されてしまう
    - 集計範囲のフィルタが正しく効いていない
    - 対象テーマのみを対象にする必要あり

## 修正方法の概要

**コメント:** なし

---

### [プロフィールの画像登録が失敗することがある](https://github.com/digitaldemocracy2030/idobata/issues/264)

**作成者:** masatosasano2  
**作成日:** 2025-05-09T13:14:52Z  
**内容:**

## 問題

- 保存ボタンを押した後、意図通り登録される場合とされない場合がある
- 拡張子やサイズによるかもしれない

されなかった例で登録した画像とPC画面上の見え方：

<img src="https://github.com/user-attachments/assets/d6063a29-e37e-47d1-a307-198f28bb17ad" width="300px"/><img src="https://github.com/user-attachments/assets/1c21a72d-5bc9-486a-adee-205d720499ad" width="500px"/>

## 修正方法の概要

**コメント:** なし

---

### [[チャット][UX] プロフィールに設定した名前で呼びかけてほしい](https://github.com/digitaldemocracy2030/idobata/issues/263)

**作成者:** masatosasano2  
**作成日:** 2025-05-09T13:12:05Z  
**内容:**

## 解決・改善したいこと

プロフィールに名前を登録したら、その名前で呼びかけてほしい

## 具体的な実現方法・実装方法の概要

**コメント:** なし

---

### [プロフィール名が未設定の時に誤った名前で呼びかけられることがある](https://github.com/digitaldemocracy2030/idobata/issues/262)

**作成者:** masatosasano2  
**作成日:** 2025-05-09T13:10:57Z  
**内容:**

## 問題

- プロフィール名が未設定の時に誤った名前で呼びかけられることがある
- 誤った名前の出所は不明（例：impcat さん）

## 修正方法の概要

**コメント:** なし

---

### [[チャット] ハイコンテクストな問題提起への反応がイマイチ](https://github.com/digitaldemocracy2030/idobata/issues/261)

**作成者:** masatosasano2  
**作成日:** 2025-05-09T13:08:06Z  
**内容:**

## 経緯と課題

5/9 のいどばた体験会で、いどばたを広めるためのアイデアが募集された。
そこで、dd2030.org 以外の団体との連携の提案が行われたが、提案の意味を汲み取れていないような回答が続いた。

## 原因予想

質問者が知っている以下のコンテクストをAIが共有していなかったことに由来する可能性がある。
- いどばたというプロダクトの概要
- デジタル民主主義というプロジェクトや組織の概要、いどばたとの関連性
- いどばたが若いOSSであり開発や利用を更に促進していくための道筋を模索中であること
- 質問者が想定する他の団体の関心事や役割、どのような連携が考えられるか
- そのような連携が現在とられておらず、機会損失があること

## TODO

- 具体的にどんな会話があったのかをヒアリング
- 会話ログが残っている場合、詳細分析

## 具体的な実現方法・実装方法の概要

**コメント:** なし

---

### [[いどばたビジョン][UI] タイトルや概要が固定表示されていてほしい](https://github.com/digitaldemocracy2030/idobata/issues/260)

**作成者:** masatosasano2  
**作成日:** 2025-05-09T12:57:55Z  
**内容:**

## 解決・改善したいこと

PC上でテーマページや論点ページを下スクロールすると、タイトル / パンくず / 概要などが隠れてしまう。
情報量の多い画面たちなので、読んでいるうちにコンテキストを見失うので、どこかに固定してほしい。

## 具体的な実現方法・実装方法の概要

**コメント:** なし

---

### [[レポート][UI] まとめと意見一覧を横並びで見たい](https://github.com/digitaldemocracy2030/idobata/issues/258)

**作成者:** masatosasano2  
**作成日:** 2025-05-09T12:53:21Z  
**内容:**

## 解決・改善したいこと

- PC表示では「論点まとめ・イラスト」と「意見一覧」を横並びで見たい
    - まとめと一覧の関連性が可視化されているとなお良い
- 関連Issue： #220 もPC版レイアウト改善提案

## 具体的な実現方法・実装方法の概要

**コメント:** なし

---

### [[チャット] 他の人の意見とチャットを分けて表示してほしい](https://github.com/digitaldemocracy2030/idobata/issues/257)

**作成者:** masatosasano2  
**作成日:** 2025-05-09T12:50:36Z  
**内容:**

## 解決・改善したいこと

他の意見はチャットとは別位置に表示してほしい
補足：構造的にセグメント分けされた表示が望ましい

関連Issue： #206 

## 具体的な実現方法・実装方法の概要

**コメント:** なし

---

### [チャット欄を右に固定する。](https://github.com/digitaldemocracy2030/idobata/issues/252)

**作成者:** moai-redcap  
**作成日:** 2025-05-07T11:47:47Z  
**内容:**

## 解決・改善したいこと
PCユーザーのUX改善
チャット欄を右に固定したい

## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(7件)

### [[レポート] 論点まとめの「対立軸」と「対立点」の役割と内容が重複している](https://github.com/digitaldemocracy2030/idobata/issues/221)

**作成者:** masatosasano2  
**作成日:** 2025-05-05T08:16:54Z  
**内容:**

## 解決・改善したいこと

現状は以下のような構成になっている。

論点まとめ
- 主要な論点と対立軸
    - 論点
        - 対立軸
- 合意形成の状況
    - 合意点
    - 対立点

このうち、「対立軸」と「対立点」の内容が重複している

<img width="929" alt="Image" src="https://github.com/user-attachments/assets/b9ecd23f-c1cd-4fbc-a467-1ce5148fb402" />

## 具体的な実現方法・実装方法の概要

例えば以下のような構成はどうでしょう

論点まとめ
- 合意点
- 主要な論点と対立軸
    - 論点
        - 対立軸

**コメント:** なし

---

### [[チャット] 他の人の反対意見を知りたい](https://github.com/digitaldemocracy2030/idobata/issues/206)

**作成者:** masatosasano2  
**作成日:** 2025-05-05T07:22:45Z  
**内容:**

## 解決・改善したいこと

- もうちょっと「他の人はこう言ってるよ」みたいな反論が多いと間接的にみんなと喋ってる、、、！感が増しそう
    - 他の人の意見出てくると一人相撲感減りそう
    - 直接人に話すわけじゃないので、他人の反対意見に対しても凄い発言しやすい

## 具体的な実現方法・実装方法の概要

**コメント:** なし

---

### [[UI] 会話の終わり方に迷う](https://github.com/digitaldemocracy2030/idobata/issues/205)

**作成者:** masatosasano2  
**作成日:** 2025-05-05T07:04:28Z  
**内容:**

## 解決・改善したいこと

- チャットのやり取りで、質問が無限につづくのか、どこまでやりとりすればいいのかがわかるとやっていて心地よい。
- AIから質問がどんどん来るのが負担に感じるかも。
- チャット欄を閉じてから別のチャットを始めようとすると、前の会話の続きからになる。課題一覧画面に戻ってからチャットに入ると新しい会話になるが、操作が煩雑。

## 具体的な実現方法・実装方法の概要

- 会話中断ボタンがあると良い
    - これを押したら、ゲーム終了画面みたいな感じで「この会話から○○件の解決策が抽出されました！素晴らしい！」みたいなメッセージを出してあげると良さそう。
        - SNSシェアできるなイメージ
- 途中で切ってそれまでの内容で投稿できるようにするとかでも。
- 「別の話題に移る」ボタンなどもあって良さそう
- ボタン3つぐらいで成立しそう
- 非同期的に使ってもらう場合も、「5分間のチャット」みたいな感じでタイムリミットをあえて設定してあげる
    - Twitterに「[idobata-demo.dd2030.org](http://idobata-demo.dd2030.org/) にアクセスして、5分間AIとチャットしてみよう！何件の意見が出せたか教えてね！」みたいな投稿が流れてくるイメージ
    -  「とりあえずチャットしてみて」より「5分間AIとチャットしてみて」の方が参加してみたい気持ちが湧きそう（仮説）
        - ゴールが明確なので
    - 「5分間でどれだけ課題/解決策を提供できるか」みたいなタイムアタックの楽しみ方が生まれそう（妄想）
    - ワークショップ的な場面だと特にハマる気がします
        - いどばた使うデザインスプリント https://www.gv.com/sprint/ みたいなフレームワーク開発できそう
        - スタート→入力→タイムリミットになったら一旦切る→一連の意見をまとめ（何件の意見がでました）、褒める（今日のランキング◯位、すごい！）→次のアクションを提示（結果をシェアする、もう1回やる、別のテーマに移る、まとめを見に行く）

**コメント:** なし

---

### [[UI] チャットのAIがマークダウンで回答した場合、整形されたビューを表示してほしい](https://github.com/digitaldemocracy2030/idobata/issues/203)

**作成者:** masatosasano2  
**作成日:** 2025-05-05T06:54:05Z  
**内容:**

## 解決・改善したいこと

体験会のFBより
- 時々マークダウン形式で回答しようとするが、ビューが未対応

## 具体的な実現方法・実装方法の概要

**コメント:** なし

---

### [[UI] チャット内で改行したい](https://github.com/digitaldemocracy2030/idobata/issues/202)

**作成者:** masatosasano2  
**作成日:** 2025-05-05T06:51:32Z  
**内容:**

## 解決・改善したいこと

体験会のFBより
- チャット内で改行したい

## 具体的な実現方法・実装方法の概要


**コメント:** なし

---

### [レポート（市民意見レポート、イラストまとめ、論点まとめ）の質を上げる](https://github.com/digitaldemocracy2030/idobata/issues/185)

**作成者:** spinute  
**作成日:** 2025-05-04T06:39:00Z  
**内容:**

## 解決・改善したいこと

#106 #107 #108 でレポート機能を一通り動くようにした。

この issue ではレポートの質的な伸びしろを探る。

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

当事者として関われる本格的なデータがあれば質的な改善を回せそう。

5/4 に dd2030 に関して実際にみんなでいどばたを使ってみる回があるので、そこでデータ意見を元によりよいレポートを作る。

**コメント:** なし

---

### [表画面の文字サイズ調整](https://github.com/digitaldemocracy2030/idobata/issues/126)

**作成者:** moai-redcap  
**作成日:** 2025-05-01T16:04:47Z  
**内容:**

## 解決・改善したいこと
市民が書き込む各画面のUIの文字サイズが小さいため、調整したい


## 具体的な実現方法・実装方法の概要（未記入でも構いません）
デザインを参照して調整したい。
https://www.figma.com/design/Td64AEvdk42ov6t6IPEvTN/DD2030?node-id=1465-1461&t=kclAvqcRnXfuwnix-1

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (3件)

### [Add Open Graph and Twitter Card metadata to index.html](https://github.com/digitaldemocracy2030/idobata/pull/281)

**作成者:** ttizze  
**作成日:** 2025-05-13T09:49:40Z  
**変更:** +34 -11 (2ファイル)  
**マージ日:** 2025-05-14T03:26:14Z  
**内容:**

# 変更の概要
OGP設定

# スクリーンショット
動的にできないため本番で確かめる必要がある

# 変更の背景
OGPのため

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Add '話題を変える' button to chat header](https://github.com/digitaldemocracy2030/idobata/pull/255)

**作成者:** Shutaro Aoyama+Devin  
**作成日:** 2025-05-09T10:20:52Z  
**変更:** +25 -2 (2ファイル)  
**マージ日:** 2025-05-09T10:52:06Z  
**内容:**

# Add "話題を変える" button to chat header

## Changes
- Added a "話題を変える" (Change topic) button to the chat header
- When clicked, the button sends a message "話題を変えましょう" (Let's change the topic)
- The button is positioned on the left side of the chat header for better visibility
- Styled to match existing UI patterns

## Testing
- The button appears in the correct location in the chat header
- Clicking the button sends the message "話題を変えましょう"
- The AI responds to this message through the normal application flow

## Link to Devin run
https://app.devin.ai/sessions/412243110cb049f9bc13d543434c7916

Requested by: Shutaro Aoyama


**コメント:** なし

---

### [メタデータのタイトルを修正：いどばたビジョンといどばた政策](https://github.com/digitaldemocracy2030/idobata/pull/251)

**作成者:** tomoki2757+Devin  
**作成日:** 2025-05-07T06:41:58Z  
**変更:** +2 -2 (2ファイル)  
**マージ日:** 2025-05-13T09:38:42Z  
**内容:**

# タイトル修正

## 変更内容
- フロントエンドのタイトルを「いどばた」から正確な「いどばたビジョン」に変更
- 政策編集モジュールのタイトルを「GitHubリポジトリブラウザ」から「いどばた政策」に変更

これにより、ブラウザのタブに表示されるタイトルがそれぞれのモジュールの正式名称と一致するようになります。

## 検証方法
- ブラウザでアプリを開き、タブのタイトルが正しく表示されることを確認

Link to Devin run: https://app.devin.ai/sessions/aa5c860642c6435c9c5e033f71136221
Requested by: tomoki2757@gmail.com


**コメント:** なし

---

### 過去7日間に作成されたPR (6件)

### [モバイル向けチャットUIの改善](https://github.com/digitaldemocracy2030/idobata/pull/282)

**作成者:** Shutaro Aoyama+Devin  
**作成日:** 2025-05-14T08:04:47Z  
**変更:** +97 -5 (3ファイル)  
**内容:**

# モバイル向けチャットUIの改善

## 変更内容
- モバイルデバイスでは、デフォルトでチャットパネルを非表示にする機能を追加
- 画面右下に浮かぶチャットボタンを実装
- ボタンをタップするとチャットパネルが画面下部からスライドアップして表示される
- スムーズなアニメーション効果を追加

## テスト内容
- `npm run lint`と`npm run typecheck`を実行して問題がないことを確認
- ブラウザでの動作確認を実施
  - デスクトップ表示: チャットパネルが常に表示される
  - モバイル表示: デフォルトではチャットパネルが非表示、ボタンタップで表示

## 技術的な詳細
- Tailwind CSSを使用したレスポンシブデザイン
- React Hooksを使用した状態管理（`useState`、`useEffect`）
- CSSトランジションによるスムーズなアニメーション

Link to Devin run: https://app.devin.ai/sessions/b8a5438e574f4d0cbdd07332d058d6aa
Requested by: Shutaro Aoyama


**コメント:** なし

---

### [[UI] チャット入力欄へのfocusの改善](https://github.com/digitaldemocracy2030/idobata/pull/279)

**作成者:** yusasa16  
**作成日:** 2025-05-11T15:42:40Z  
**変更:** +13 -1 (1ファイル)  
**内容:**

# 変更の概要
入力欄をクリックした時にフォーカスが一回で入力欄に移るようにしました。
またチャットを送信した時にもフォーカスが入力欄に留まるようにしました。

## 補足
チャットの送信後は処理の完了を待つため、再び入力欄にフォーカスが当たるまで一瞬時間がかかります。

# スクリーンショット
<img width="1021" alt="スクリーンショット 2025-05-12 0 38 02" src="https://github.com/user-attachments/assets/dbce3ea1-d71b-4c5c-ac32-e71a6f2b286f" />

# 関連Issue
fix #201

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [チャットUIでShift+Enterで改行できるように修正](https://github.com/digitaldemocracy2030/idobata/pull/259)

**作成者:** Satoru Horie+Devin  
**作成日:** 2025-05-09T12:53:47Z  
**変更:** +3 -3 (1ファイル)  
**内容:**

# チャットUIでShift+Enterで改行できるように修正

## 変更内容
- ChatSheetコンポーネントのinput要素をtextarea要素に変更
- textareaのスタイリングを調整（resize-none, min-height, max-height, overflow-y-auto）
- Shift+Enterで改行、Enterで送信の動作を実装

## 関連Issue
Closes #256
Closes #202 

## テスト方法
- チャットUIでShift+Enterを押して改行できることを確認
- Enterキーを押してメッセージが送信されることを確認

## Link to Devin run
https://app.devin.ai/sessions/75285f5302f746db8f73cabada9fec52

## Requested by
Satoru Horie (Pin) (spinutids@gmail.com)


**コメント:** なし

---

### [PC時チャットを右に固定](https://github.com/digitaldemocracy2030/idobata/pull/254)

**作成者:** moai-redcap  
**作成日:** 2025-05-07T15:59:26Z  
**変更:** +141 -7 (4ファイル)  
**内容:**

プルリクの仕方間違ってたすみません。
その際はご教示いただきたいです。

# 変更の概要
aboutページのみですが、PC表示時、チャットを右に固定にしました。

# スクリーンショット
![image](https://github.com/user-attachments/assets/21af1a19-d436-4dfa-a687-a0c442cca486)

# 変更の背景
PC時のUXの向上のため。

# 関連Issue
#252 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [PC時チャットを右に固定（aboutページのみ）](https://github.com/digitaldemocracy2030/idobata/pull/253)

**作成者:** moai-redcap  
**作成日:** 2025-05-07T14:45:31Z  
**変更:** +166 -19 (3ファイル)  
**内容:**

プルリクの仕方間違ってたすみません。
その際はご教示いただきたいです。

# 変更の概要
aboutページのみですが、PC表示時、チャットを右に固定にしました。

# スクリーンショット
![image](https://github.com/user-attachments/assets/21af1a19-d436-4dfa-a687-a0c442cca486)

# 変更の背景
PC時のUXの向上のため。

# 関連Issue
#252 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Add demo URLs to README.md](https://github.com/digitaldemocracy2030/idobata/pull/250)

**作成者:** tomoki2757+Devin  
**作成日:** 2025-05-07T06:20:00Z  
**変更:** +5 -0 (1ファイル)  
**内容:**

# Add demo URLs to README.md

Added a new "デモ" (Demo) section to the README.md file with links to:
- いどばたビジョンデモ: https://idobata-demo.dd2030.org/top
- いどばた政策デモ: https://delib.takahiroanno.com/

The section was placed after the project overview and before the "提供する価値" section.

Requested by: tomoki2757@gmail.com

Link to Devin run: https://app.devin.ai/sessions/aee52de5b9874b4e83d37b00c0d36e1e


**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(10件)

### [AIチャットの応答を段階的に送信する機能を実装](https://github.com/digitaldemocracy2030/idobata/pull/240)

**作成者:** Shutaro Aoyama+Devin  
**作成日:** 2025-05-05T12:51:38Z  
**変更:** +191 -21 (4ファイル)  
**内容:**

# AIチャットの応答を段階的に送信する機能の実装

## 変更内容

AIのチャットの挙動を調整し、回答を生成した後にそれを一気に流すのではなく、以下の方法で段階的に送信するように変更:

- 句点（。）、感嘆符（！）、疑問符（？）で応答を分割
- 一言目はすぐに返す
- 二言目以降は、それぞれ文字数*0.2秒待機してから送信
- 待機中に新しいメッセージが来た場合は、キューの中身をクリア

## 実装詳細

1. ChatThreadモデルに`pendingSentences`フィールドを追加して、送信待ちの文を保存
2. socketService.jsに新しい関数を追加して、チャットレスポンスのストリーミングを処理
3. server.jsにソケットイベントハンドラを追加して、キューをクリアする機能を実装
4. chatController.jsを修正して、応答の分割と段階的な送信を実装

## 検証方法

1. AIとチャットを開始
2. AIから複数の文からなる応答が返ってきた場合、最初の文がすぐに表示され、その後の文が遅延して表示されることを確認
3. 文の表示途中で新しいメッセージを送信し、キューがクリアされることを確認

Link to Devin run: https://app.devin.ai/sessions/0a91cdb71cd4487ab33b9502e86cc4cd
Requested by: Shutaro Aoyama


**コメント:** なし

---

### [Remove Dead Code](https://github.com/digitaldemocracy2030/idobata/pull/239)

**作成者:** Satoru Horie+Devin  
**作成日:** 2025-05-05T12:17:41Z  
**変更:** +168 -1561 (40ファイル)  
**内容:**

# Remove Dead Code

This PR removes dead code from the repository as identified by knip.

## Changes:
- Removed 15 unused files
- Removed 8 unused dependencies and 6 unused devDependencies
- Removed 37 unused exports and 17 unused exported types
- Fixed 3 duplicate exports
- Added 1 missing dependency (@octokit/plugin-rest-endpoint-methods)

## Verification:
- Ran knip to identify and remove dead code
- Ran `npm run check` to verify changes don't break functionality

Link to Devin run: https://app.devin.ai/sessions/f3d3a88383d2453b8129a0092b2af38c
Requested by: Satoru Horie (Pin)


**コメント:** なし

---

### [Remove dead code](https://github.com/digitaldemocracy2030/idobata/pull/237)

**作成者:** Satoru Horie+Devin  
**作成日:** 2025-05-05T11:46:53Z  
**変更:** +173 -463 (7ファイル)  
**内容:**

# Remove Dead Code

This PR removes dead code from several files in the repository:

1. Removed a large commented-out block in extractionWorker.js
2. Removed unused variable assignments in extractionWorker.js
3. Removed the deprecated sheet.tsx file which was only maintained for backward compatibility
4. Removed the createRepeatedData function and related mock data logic in CommentsPage.tsx
5. Refactored duplicate code in ThemeDetailChatManager and QuestionChatManager by creating a base class

The changes remove approximately:
- 110 lines from extractionWorker.js
- 33 lines from sheet.tsx
- 15 lines from CommentsPage.tsx
- ~150 lines of duplicate code from ThemeDetailChatManager and QuestionChatManager

This work was requested by Satoru Horie (Pin).

Link to Devin run: https://app.devin.ai/sessions/c8f895fcbd2d4ec0a16e8ad2b25689be


**コメント:** なし

---

### [（提案者：Devin）プルリクエストタイトル形式の標準化【PR Format】](https://github.com/digitaldemocracy2030/idobata/pull/196)

**作成者:** Shutaro Aoyama+Devin  
**作成日:** 2025-05-05T01:01:11Z  
**変更:** +58 -6 (5ファイル)  
**内容:**

# PR: プルリクエストタイトル形式の標準化

須田英太郎さんの提案に基づき、PR一覧画面でどのdocに対する修正案なのかが分かるようにプルリクエストのタイトル形式を標準化しました。

## 新しいPRタイトル形式
「（提案者：名前）内容【ドキュメント名】」

例：「（提案者：山田太郎）AIチューターの格差是正策とプライバシー保護の追記【1.1_教育DXへの生成AI活用】」

これにより、PR一覧から各ドキュメントの担当者が自分の担当分かどうかを確認しやすくなります。

## 実装内容
1. ドキュメント名を抽出する関数を追加
   - `extractDocumentName`: ファイルパスからドキュメント名を抽出
   - `formatPrTitle`: 標準化されたPRタイトルを生成

2. PR作成時にタイトルを統一形式で設定する機能を追加
   - `updatePr.ts`のスキーマを拡張して`filePath`と`userName`を受け取れるように
   - デフォルトのPRタイトル生成ロジックを更新

3. ユーザー名とドキュメント名を取得する処理を追加
   - バックエンドとフロントエンドの連携を強化
   - `currentPath`をAPIリクエストに含めるよう修正

## 変更点の詳細
- `policy-edit/mcp/src/github/prTitleUtils.ts`: 新規作成したユーティリティ関数
- `policy-edit/mcp/src/handlers/updatePr.ts`: PRタイトル生成ロジックの更新
- `policy-edit/backend/src/routes/chat.ts`: `currentPath`パラメータの追加
- `policy-edit/backend/src/mcp/client.ts`: `currentPath`パラメータのサポート
- `policy-edit/frontend/src/components/ChatPanel.tsx`: `currentPath`をペイロードに追加

依頼者: Shutaro Aoyama
Devin Run: https://app.devin.ai/sessions/20d82ba86076490e83f466d80f314d64


**コメント:** なし

---

### [PRの説明文で変更点よりも意図と経緯を重視するようプロンプトを修正](https://github.com/digitaldemocracy2030/idobata/pull/195)

**作成者:** Shutaro Aoyama+Devin  
**作成日:** 2025-05-05T01:00:32Z  
**変更:** +1 -1 (1ファイル)  
**内容:**

# PR説明文のプロンプト修正

## 変更内容と目的
このPRでは、policy-editモジュールのプルリクエスト説明文作成に使われるプロンプトを修正しています。変更の目的は、PRの説明文において「変更点の詳細な説明」よりも「変更の意図や経緯」を重視するよう促すことです。

## 変更の背景
須田英太郎さんからSlackで要望があり、PRコメントで重要なのは変更点よりも改善の意図であり、変更点自体はFiles changedから見たほうが分かりやすいとのことでした。そのため、AIが生成するPR説明文の内容をこの要望に沿って修正しました。

## 変更箇所
- システムプロンプト内の「レビュー依頼の準備」セクションのテキストを、変更の意図や背景を重視するように修正
- 「変更点自体はFiles changedから確認できる」という文言を追加し、変更の意図と経緯を伝えることに集中するよう明示

## 検証方法
このテキスト変更はAIプロンプトの修正であり、実際の効果はAIが生成するPR説明文の内容で確認できます。修正後は、PR説明文が変更点の詳細よりも変更の意図や経緯に焦点を当てたものになることが期待されます。

Link to Devin run: https://app.devin.ai/sessions/7d8ae072b2d54fe2a1d2e48013ba6536
Requested by: Shutaro Aoyama (ぶるーも)


**コメント:** なし

---

### [課題点と解決策の数の修正](https://github.com/digitaldemocracy2030/idobata/pull/194)

**作成者:** Shutaro Aoyama+Devin  
**作成日:** 2025-05-05T00:47:06Z  
**変更:** +16 -2 (3ファイル)  
**内容:**

# 課題点と解決策の数の修正

## 問題
/topページの意見募集中テーマに表示される「課題点」と「解決策」の数字が間違っていました。
- 課題点：誤ってキークエスチョンの数（keyQuestionCount）を表示していた
- 解決策：誤ってコメントの数（commentCount）を表示していた

## 修正内容
- バックエンド：`topPageController.js`を修正して、各テーマの正しい課題点（Problem）と解決策（Solution）の数を返すようにしました
- フロントエンド：`types.ts`にプロパティを追加し、`Top.tsx`で正しい数値を使用するように修正しました

## 検証方法
- /topページと/themes/:themeIdページの両方を確認し、課題点と解決策の数が一致することを確認

Link to Devin run: https://app.devin.ai/sessions/0bcd23ed193846e4a397c7cf49bf5451
Requested by: Shutaro Aoyama


**コメント:** なし

---

### [OGP設定（エンドポイント変更対応）](https://github.com/digitaldemocracy2030/idobata/pull/184)

**作成者:** itoma-aikon  
**作成日:** 2025-05-04T04:53:12Z  
**変更:** +1680 -369 (18ファイル)  
**内容:**

# 変更の概要
お待たせしました。
OGP設定機能の追加をしました。
エラー時用のデフォルトOGP画像は白紙ですが、必要でしたら変更してください。


# スクリーンショット
![スクリーンショット 2025-04-27 000331](https://github.com/user-attachments/assets/881ffc55-d3ae-4ae3-84cd-45ea77b15c5a)
![ogp_image_596a5175862dc9fa11c21ccd9e47fb73e2467196f3918573c1d9aed38c3f1688](https://github.com/user-attachments/assets/6785e001-6220-4d64-b185-011383bd6ffc)


# 関連Issue
https://github.com/digitaldemocracy2030/idobata/issues/19

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Implement Google Authentication Integration](https://github.com/digitaldemocracy2030/idobata/pull/176)

**作成者:** kainekominto299+Devin  
**作成日:** 2025-05-03T17:44:09Z  
**変更:** +679 -48 (11ファイル)  
**内容:**

# Google認証統合の実装（エンドユーザーのみ）

このPRでは、いどばたプロジェクトにGoogle認証機能を追加し、エンドユーザー向けの認証システムを強化します。フィードバックに基づき、管理者パネルと一般ユーザーの認証システムは分離したままとし、Google認証はエンドユーザー向けにのみ実装しています。

## 主な変更点

### フロントエンド（エンドユーザー向け）
- Google認証ボタンの追加
- 統合認証コンテキスト（UnifiedAuthContext）の実装
- Googleコールバックページの追加
- APIクライアントにGoogle認証メソッドを追加

### バックエンド
- Google OAuth認証プロバイダーの実装
- ユーザーモデルにGoogle認証フィールドを追加
- 認証ミドルウェアの分離（管理者用とエンドユーザー用）
- 認証コントローラーの更新

## 認証システムの分離

- **管理者認証**: 従来のID/パスワード認証を維持
- **エンドユーザー認証**: Google認証を追加しつつ、既存のUUID識別も維持

## テスト方法

1. 環境変数の設定:
   - `GOOGLE_CLIENT_ID`
   - `GOOGLE_CLIENT_SECRET`
   - `GOOGLE_REDIRECT_URI`
   - `FRONTEND_URL`

2. フロントエンドでのGoogle認証フローのテスト:
   - ログインボタンをクリック
   - Googleアカウント選択
   - リダイレクト後の認証状態確認

## 注意点

- 管理者パネルではGoogle認証は利用できません
- エンドユーザーはGoogle認証またはUUID識別のいずれかを使用できます
- 既存のユーザーデータは保持されます

## Link to Devin run
https://app.devin.ai/sessions/ee5e1e9b89c245f3949b5c1974582652

## Requested by
kainekominto299@gmail.com


**コメント:** なし

---

### [政策生成プロセスの強化：エンベディングと階層的クラスタリングの導入](https://github.com/digitaldemocracy2030/idobata/pull/152)

**作成者:** Shutaro Aoyama+Devin  
**作成日:** 2025-05-02T14:06:36Z  
**変更:** +275 -67 (1ファイル)  
**内容:**

## 変更内容

Policy Generator 改善仕様書に基づき、政策生成プロセスを以下の方法で強化しました：

1. 政策作成前に、関連するProblemとSolutionのエンベディングが生成・更新されていることを確認
2. これらのProblemとSolutionに対して、エンベディングに基づいた階層的クラスタリングを実行
3. 階層的クラスタリングの結果から得られたアイテムの順序を、LLMプロンプトの主要なコンテキストとして使用

詳細な実装ステップ：
- エンベディング生成ロジックの追加
- 階層的クラスタリングの実行
- クラスターツリーの関連性スコアによるソート
- ソート済みクラスターからの順序付きアイテムIDの抽出
- LLMプロンプトの更新

Link to Devin run: https://app.devin.ai/sessions/9dac3d3903534041b100235956163f74

このPRでは、Shutaro Aoyama様のリクエストに基づいて実装を行いました。


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

