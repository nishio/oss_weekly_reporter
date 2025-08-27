# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-08-20T12:22:13.986157+09:00 から 2025-08-27T12:22:13.986157+09:00 まで

## Issues

### 過去7日間に完了されたissue (2件)

### [[FEATURE]ハイフンで終わるIDが受理されないことを注意書きやエラーで知らせたい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/692)

**作成者:** yuneko1127  
**作成日:** 2025-08-08T14:50:56Z  
**内容:**

# 背景
レポート作成画面でIDを変更するとき、ハイフンで終了する文字列はエラーになるが、そのことが下の注意書きでもエラーでもそのことが知らされない。
何故受理されていないかを確認できるようにした方が良い。
3.00verを使っています。

<img width="366" height="107" alt="Image" src="https://github.com/user-attachments/assets/726b7be1-3314-40c0-9d92-ceee73398923" />


# 提案内容

1. ハイフンで終了するような文字列が入力されてエラーが出ているときに、ハイフンで終了する文字列は使えませんのようなエラーに変更する
2. 「英字小文字と数字とハイフンのみ(URLで利用されます)」という注意書きに、ハイフンで終了できないことも示す。

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

### 過去7日間に作成されたissue (1件)

### [[FEATURE] 広聴AIで作成したレポートを誤って解釈をしないようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/696)

**作成者:** shingo-ohki  
**作成日:** 2025-08-21T08:09:56Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

[広聴AI開発定例 2025/8/20](https://docs.google.com/document/d/1plggszRTxEEYUcZuCLiHkPrBsMtxr3RQpctKtZe5y4M/edit?tab=t.0#heading=h.yyt1ivvnrs0q) 内でレポートの解釈の仕方について話題になり、その辺りの説明が必要ではないか？という話になった

> 中山心太（tokoroten）
  [21:11](https://dd2030.slack.com/archives/C08F7JZPD63/p1755691873351029)
[【参院選】「AI分析で民意を可視化」の落とし穴…“数”は無意味？“サイエンス風”に惑わされないために｜アベヒル](https://www.youtube.com/watch?v=0_wIbDMvpMg)
公聴AIを使う場合、どういうふうなデータが得られて、どういうふうに偏っているのかはこの動画が詳しいので、おすすめです。
NISHIO Hirokazu
  [21:14](https://dd2030.slack.com/archives/C08F7JZPD63/p1755692086840979)
いっそおすすめ動画として広聴AIのWebサイトに載せたらいいのかも
中山心太（tokoroten）
  [21:29](https://dd2030.slack.com/archives/C08F7JZPD63/p1755692945671519)
良くも悪くも、中核メンバーがデータ分析者すぎるので、クセを分かってたわけだけど、
そこから一般に広がっていく過程で、その暗黙の前提知識が失われたせいで、誤った分析がなされるというのが起こっているので、なんとかしたいですね。 （編集済み） 
中山心太（tokoroten）
  [00:04](https://dd2030.slack.com/archives/C08F7JZPD63/p1755702294919739)
広聴AIの性質と、データの読み方、何が得られるのか、追加調査の考え方、みたいなのが整理できるといいな
[00:05](https://dd2030.slack.com/archives/C08F7JZPD63/p1755702301469099)
当たり前すぎて気づいてなかった
[21:31](https://dd2030.slack.com/archives/C08F7JZPD63/p1755693063767919)
書籍化するなら、↑の動画の二人に寄稿してもらえんかなー、公聴AIの限界やクセと言う話で。
[ブロードリスニングはノイジーマイノリティを積極的に拾ってしまうので、選挙に使う場合は注意が必要](https://scrapbox.io/dd2030/%E3%83%96%E3%83%AD%E3%83%BC%E3%83%89%E3%83%AA%E3%82%B9%E3%83%8B%E3%83%B3%E3%82%B0%E3%81%AF%E3%83%8E%E3%82%A4%E3%82%B8%E3%83%BC%E3%83%9E%E3%82%A4%E3%83%8E%E3%83%AA%E3%83%86%E3%82%A3%E3%82%92%E7%A9%8D%E6%A5%B5%E7%9A%84%E3%81%AB%E6%8B%BE%E3%81%A3%E3%81%A6%E3%81%97%E3%81%BE%E3%81%86%E3%81%AE%E3%81%A7%E3%80%81%E9%81%B8%E6%8C%99%E3%81%AB%E4%BD%BF%E3%81%86%E5%A0%B4%E5%90%88%E3%81%AF%E6%B3%A8%E6%84%8F%E3%81%8C%E5%BF%85%E8%A6%81)
書いておきました。
youkiti
  [今日 10:29](https://dd2030.slack.com/archives/C08F7JZPD63/p1755739749894699?thread_ts=1755738362.393659&cid=C08F7JZPD63)
理論的な基盤としてはこういうのがありますね
「ブロードリスニング」は、質的な調査
https://www.jstage.jst.go.jp/article/hokenshikyouiku/5/1/5_7/_pdf/-char/ja
中山心太（tokoroten）
  [今日 10:44](https://dd2030.slack.com/archives/C08F7JZPD63/p1755740657846419?thread_ts=1755738362.393659&cid=C08F7JZPD63)
データ分析を生業にしている人は、ブロードリスニングは質的調査、定性分析ツールだというのが分かっているんですが、
そこから一般に広がるにあたって「なんとなく説得力を産むツール」に変貌してしまっていて、そこで問題が起きてる感じですね
Shingo OHKI
  [今日 10:48](https://dd2030.slack.com/archives/C08F7JZPD63/p1755740894940289?thread_ts=1755738362.393659&cid=C08F7JZPD63)
「課題発見ツールです」と言い切ってしまった方がよいのかも？
[10:51](https://dd2030.slack.com/archives/C08F7JZPD63/p1755741075506609?thread_ts=1755738362.393659&cid=C08F7JZPD63)
可視化ツールに見えるから、説得力を持たせたくなる？
中山心太（tokoroten）
  [今日 10:51](https://dd2030.slack.com/archives/C08F7JZPD63/p1755741119292499?thread_ts=1755738362.393659&cid=C08F7JZPD63)
画像になるから説得力を利用者が感じてしまって、それが「良い分析である」と勘違いしてしまっていることですね
Shingo OHKI
  [今日 11:11](https://dd2030.slack.com/archives/C08F7JZPD63/p1755742305951539?thread_ts=1755738362.393659&cid=C08F7JZPD63)
クラスタをすべて同じ形と大きさの領域で表すようにしてそれをただ並べただけの画像にしたらミスリードは少なくなりそうな気がしました
[11:13](https://dd2030.slack.com/archives/C08F7JZPD63/p1755742412988739?thread_ts=1755738362.393659&cid=C08F7JZPD63)
それがこれなのかな
[11:14](https://dd2030.slack.com/archives/C08F7JZPD63/p1755742454819579?thread_ts=1755738362.393659&cid=C08F7JZPD63)
ラベルのところだけの羅列でもよさそうな
Shingo OHKI
  [今日 11:26](https://dd2030.slack.com/archives/C08F7JZPD63/p1755743196948079?thread_ts=1755738362.393659&cid=C08F7JZPD63)
ただ、なんとなく見栄えがいいから興味を持つということもありそうなので、難しいですね
中山心太（tokoroten）
  [今日 11:29](https://dd2030.slack.com/archives/C08F7JZPD63/p1755743349725199?thread_ts=1755738362.393659&cid=C08F7JZPD63)
なので、言い方が悪いですが、有権者へのアピールと、内部利用の分析は方針を分けないといけないわけですが、それを混同するから問題が起こるわけです。
ここら辺の注意書き、誰かに清書してもらって、プロダクトの中に組み入れてほしい。

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
やり方はいろいろありそう
- README などのドキュメントに入れる
- プロダクトの中に組み入れる
- 事例とともに website に載せる
- 解説記事を書く、書籍化する

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (2件)

### [[FEATURE]ハイフンで終わるIDが受理されないことを注意書きやエラーで知らせたい](https://github.com/digitaldemocracy2030/kouchou-ai/pull/697)

**作成者:** mochizuki-pg  
**作成日:** 2025-08-26T06:05:50Z  
**変更:** +187 -13 (5ファイル)  
**マージ日:** 2025-08-26T07:11:43Z  
**内容:**

# 変更の概要
https://github.com/digitaldemocracy2030/kouchou-ai/issues/692

既存のバリデーションロジックにおいて、ハイフン始まり / 終わり に対する
バリデーションメッセージの表示がなかったので表示するようにしました

# スクリーンショット

https://github.com/user-attachments/assets/9c54d566-e678-4ddb-8fe8-cf809796ceb2


# 変更の背景
- ここに変更が必要となった背景を記載してください

# 関連Issue
関連するIssueのリンクをこちらに記載してください

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- 新機能
  - レポートID向けの詳細なバリデーションを追加し、入力状況に応じた明確なエラーメッセージを表示
  - 入力欄でのアクセシビリティ対応（ARIAのエラーステータス）と枠線色の視覚的フィードバックを反映
- リファクタリング
  - 作成フローでIDの有効性とエラーメッセージを明示的に扱うように変更
- テスト
  - バリデータの振る舞いと各種エラーメッセージをカバーする単体テストを追加
- その他
  - 既存の汎用バリデーションには影響なし
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[FEATURE] headerにプロダクト名を表示する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/695)

**作成者:** mochizuki-pg  
**作成日:** 2025-08-19T13:46:51Z  
**変更:** +40 -3 (5ファイル)  
**マージ日:** 2025-08-20T00:06:51Z  
**内容:**

# 変更の概要
https://github.com/digitaldemocracy2030/kouchou-ai/issues/441

[Figma](https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88dd2030%EF%BC%89?node-id=434-2041&t=fTo0ASfN0PwOagCB-0)

Figmaから落としてきたものをそのまま使用し、大きさは明示的に変更していませんが
特に問題はないように見受けられました

Client側、SPでロゴの分岐があった為、いれています
ファイル名の命名は他に合わせて `-sp` としましたが指定があれば修正します

# スクリーンショット

##  Client
<img width="1311" height="839" alt="スクリーンショット 2025-08-19 22 36 23" src="https://github.com/user-attachments/assets/ebe91197-605d-478b-8fce-dba04e06fb02" />

### SP
<img width="388" height="838" alt="スクリーンショット 2025-08-19 23 25 04" src="https://github.com/user-attachments/assets/5313743d-b694-45fa-a228-08fde2fae3a9" />


## Admin
<img width="1312" height="713" alt="スクリーンショット 2025-08-19 22 40 15" src="https://github.com/user-attachments/assets/ddcbdc21-4cd0-4ba0-ab5f-a7df84dae3fc" />


# 変更の背景
- ここに変更が必要となった背景を記載してください

# 関連Issue
関連するIssueのリンクをこちらに記載してください

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- スタイル
  - 管理画面および一般ユーザー画面のヘッダーロゴを新デザインへ変更（画像を /images/logo.svg、代替テキストを「広聴AI」に更新）
  - ロゴ画像の明示的な幅・高さ指定を削除し、周囲のレイアウトに応じた自動サイズ調整に変更

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [fix: Azure Deploy 時に client コンテナの環境変数が未設定になる](https://github.com/digitaldemocracy2030/kouchou-ai/pull/688)

**作成者:** shingo-ohki  
**作成日:** 2025-08-04T04:59:19Z  
**変更:** +61 -16 (1ファイル)  
**内容:**

# 変更の概要
- Azure デプロイ時のコンテナの環境変数の設定に不足があったため、これを修正します 
- Azure のコンテナ更新と環境変数の設定は同時に行うようにします

# 変更の背景
- #642 で azure へ deploy するワークフローを追加したが不十分な箇所があった

# 関連Issue
#682 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

一時的にフォークしたリポジトリからワークフローを実行できるようにし、[こちら](https://github.com/digitaldemocracy2030/kouchou-ai/issues/682#issuecomment-3149067334)の問題が解消していることを確認しました。
Github Actions のワークフローログ
https://github.com/shingo-ohki/kouchou-ai/actions/runs/16715007751

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit



## Summary by CodeRabbit

* **Chores**
  * デプロイワークフローを更新し、すべてのコンテナ（api、client、client-admin、client-static-build）のシークレット登録と環境変数設定を並列で実行するよう改善しました。これによりデプロイの効率と安定性が向上します。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

