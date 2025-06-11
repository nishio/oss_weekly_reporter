# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-06-04T12:30:05.345726+09:00 から 2025-06-11T12:30:05.345726+09:00 まで

## Issues

### 過去7日間に完了されたissue (2件)

### [OCR改善: 同じカテゴリが複数回別のIDで出力されてしまう](https://github.com/digitaldemocracy2030/polimoney/issues/109)

**作成者:** dotneet  
**作成日:** 2025-06-04T05:35:32Z  
**内容:**

１ページずつOCRしてjson化して最後にjsonをマージする手法をとっているが、ページごとにカテゴリとそのIDを生成しているため、最後にJSONをマージした後で同じカテゴリが別IDとして出力されてしまう。
merge_jsons.py でまとめる時などに同じカテゴリを同じIDに統合する必要がある。
この際、表記揺れにも注意が必要。

**コメント:** なし

---

### [OCR改善: 出力結果に合計や小計などのtransactionsとして不適切な項目が出力されてしまう](https://github.com/digitaldemocracy2030/polimoney/issues/108)

**作成者:** dotneet  
**作成日:** 2025-06-04T01:22:40Z  
**内容:**

表題の通り。
これらの結果として converter.ts で計算結果やカテゴリ情報の不整合が起きてしまう。
category_id は末端のカテゴリが指定される必要があるが、この出力例では末端ではなく親カテゴリのIDが付いている。
合計、小計などの集計金額が含まれないようにすればこういった問題も解消するはず。
・合計、小計だけでなく寄付金、印刷費などの項目もあるので注意。
<img width="618" alt="Image" src="https://github.com/user-attachments/assets/3df96612-e9f3-4b49-ba9d-3c68445f33cc" />


**コメント:** なし

---

### 過去7日間に作成されたissue (4件)

### [サンキー図のコピー機能](https://github.com/digitaldemocracy2030/polimoney/issues/124)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-06-10T20:48:45Z  
**内容:**

## 解決・改善したいこと

サンキー図をコピーできるようにすることで資料として用いることが可能になる。

シェア機能の一環としてあったらいいのではないかなと思いました。

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

BoardSummaryの部分を丸ごと画像として保存できるようにする。

**コメント:** なし

---

### [認証機能によるプライベート試用環境実装](https://github.com/digitaldemocracy2030/polimoney/issues/120)

**作成者:** TakumiAdachiGWS  
**作成日:** 2025-06-08T08:47:17Z  
**内容:**

## 解決・改善したいこと
一般公開前に政治家の方にプライベート環境で実際に触ってもらいたいが、認証機能とダッシュボードが実装できていない。

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->
0609現在の公開フローとしては、一般公開か否かしかないが、以下のステークホルダニーズにこたえるために認証機能を追加したい。
政治家: 公開前にどのような内容が公開され、またどのようなUXが得られるのかを実際に触ってみたい。
運営側: 後で「このような機能は想定していなかった」というようなクレームを事前に排除しておきたい。

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->
[Slackスレッドリンク](https://dd2030.slack.com/archives/C08FL5L6GSH/p1749362917916339)

## 具体的な実現方法・実装方法の概要（未記入でも構いません）
- 認証機能の付与
- Google Cloud でのダッシュボードデプロイ
（認証機能の付与によるプライベート試用環境が優先）

**コメント:** なし

---

### [カテゴリ数や深さが一定を超えるとサンキー図がとても見づらくなる](https://github.com/digitaldemocracy2030/polimoney/issues/118)

**作成者:** dotneet  
**作成日:** 2025-06-05T15:02:58Z  
**内容:**

トランザクション数が多いとカテゴリ数も自然と増え、同レベルのカテゴリ数も増えより深くなる。
同レベルのカテゴリ数や深さが一定以上にならないような制御が必要。

対処案

 - カテゴリの重要度を手動またはAIにより設定させる
 - 重要度の高いカテゴリは残しつつ、同階層のカテゴリが5個を超えるようであれば「その他」カテゴリなどにまとめてしまう
 - 深さも income と expense でそれぞれ3階層程度を上限とし、それ以下のカテゴリ・トランザクションは上位カテゴリに繰り上げる

**コメント:** なし

---

### [政治家さんのwebサイト・SNSへのリンク追加](https://github.com/digitaldemocracy2030/polimoney/issues/112)

**作成者:** Nozomi-M21  
**作成日:** 2025-06-04T13:29:46Z  
**内容:**

## 解決・改善したいこと
政治家さんの活動をビュアーに知ってもらうきっかけを作りたい。
資金がどんな活動に使われているのかイメージしやすくなり、政治への関心も高まる。
<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）
政治家さんの公式サイト、SNSへのリンクを追加する

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(5件)

### [会計ソフトの仕様書づくり](https://github.com/digitaldemocracy2030/polimoney/issues/106)

**作成者:** moai-redcap  
**作成日:** 2025-05-31T01:37:57Z  
**内容:**

## 解決・改善したいこと
会計ソフトの仕様書がなく、開発がすすめられない。
部分的にでもいいので開発が進められる様にしたい。

## 具体的な実現方法・実装方法の概要（未記入でも構いません）
- まずはfreeeなどにあたってみて、forkして使わせてもらえないかきく。
- ダメだった場合は１から仕様書を書く。

**コメント:** なし

---

### [OCRの出力項目にプロフィール情報などウェブの表示に必要な情報がない](https://github.com/digitaldemocracy2030/polimoney/issues/104)

**作成者:** dotneet  
**作成日:** 2025-05-31T00:56:44Z  
**内容:**

profile, reports などウェブの表示項目がOCRの出力情報に含まれていない。
https://github.com/digitaldemocracy2030/polimoney/issues/80#issuecomment-2922695531

**コメント:** なし

---

### [シェアボタンの実装](https://github.com/digitaldemocracy2030/polimoney/issues/103)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-05-29T14:23:06Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->
任意の閲覧者が各政治家の収支の流れをSNSでシェアーできるようにする。
アクティブな参加を促す。
polimoneyの周知、関心を持ってもらえる。
<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->
polimoney ver1.0 -> 短期のマイルストーン -> シェアボタン
## 具体的な実現方法・実装方法の概要（未記入でも構いません）
各政治家の個人のページにシェアボタンを作る。
イメージはデジタル民主主義2030のウェブサイトにあるシェアボタンのような感じ。
X, LINE, Facebook, Instagramなどでシェアー。また、リンクもコピーできるようにする。
(サンキー図の画像をコピーする機能があってもいいかも？)
<br></br>

<ジャストアイデア>
いいねボタン、ページ閲覧数などが見れても面白いかも？


**コメント:** なし

---

### [「polimoney」検索結果で表示されるアイキャッチ画像の変更](https://github.com/digitaldemocracy2030/polimoney/issues/101)

**作成者:** Nozomi-M21  
**作成日:** 2025-05-28T13:05:18Z  
**内容:**

## 問題

<!-- どこでどのような問題が起きているかを教えてください。問題の発生する画面の URL や、問題が発生しているときのスクリーンショットや録画を添付していただけると理解の助けになります。 -->
「polimoney」と検索すると、検索結果で出井さんの写真が出てしまっている。
![Image](https://github.com/user-attachments/assets/9e5c3bd0-4d25-4b40-9690-e4d96c0aca53)

<!-- この問題が解決されないと、どのような人がどのように困るか、できれば利用者を主語にして記載してください。 -->
政治的中立性の観点から、特定の方の写真を検索結果に表示させることは避けたい。
## 再現手順（未記入でも構いません）

1.
1.
1.

<!-- どのようにしたらバグが再現されるか、わかれば記載して下さい。 -->

## 修正方法の概要（未記入でも構いません）
DD2030のロゴを指定して表示させる
Google search consoleを調査　etc...

**コメント:** なし

---

### [E2E動作確認（つなぎこみ）](https://github.com/digitaldemocracy2030/polimoney/issues/29)

**作成者:** nanocloudx  
**作成日:** 2025-04-30T13:26:32Z  
**内容:**

精度は悪くても良いので（OCR結果が間違っていることを許容して）、Gemini読み込みからHTML出力までを繋ぎこむ


**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (11件)

### [Manual](https://github.com/digitaldemocracy2030/polimoney/pull/128)

**作成者:** shumizu418128  
**作成日:** 2025-06-11T02:22:45Z  
**変更:** +238 -4 (2ファイル)  
**マージ日:** 2025-06-11T02:23:14Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
仮設ページ作成マニュアル

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **ドキュメント**
  - 政治家の財務報告デモページ作成手順の詳細マニュアルを追加しました。データ準備、ファイル作成、出力確認、データ構造、命名規則、型安全性、トラブルシューティングなどを解説しています。

- **スタイル**
  - 政治家プロフィールデータの文字列プロパティから不要なコメント記号を削除しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [顔写真追加](https://github.com/digitaldemocracy2030/polimoney/pull/123)

**作成者:** shumizu418128  
**作成日:** 2025-06-10T03:06:30Z  
**変更:** +1 -1 (2ファイル)  
**マージ日:** 2025-06-10T03:37:41Z  
**内容:**

# 変更の概要
藤崎さんの顔写真追加
（あだちさん承認待ち）

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **バグ修正**
  - プロフィール画像が正しい画像に更新されました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [藤崎さん掲載](https://github.com/digitaldemocracy2030/polimoney/pull/122)

**作成者:** shumizu418128  
**作成日:** 2025-06-10T02:31:37Z  
**変更:** +797 -15 (6ファイル)  
**マージ日:** 2025-06-10T02:35:35Z  
**内容:**

# 変更の概要
依頼があった藤崎さんの収支報告書を掲載。
3年分あるので、ドロップダウンで選択することで年度切り替え可能。
デフォルトは2024(最新版)

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->
![image](https://github.com/user-attachments/assets/189d20a5-2af5-4859-a04e-65e417ca0086)
![image](https://github.com/user-attachments/assets/892d0ed1-43ea-42be-934d-f6184d30c186)
![image](https://github.com/user-attachments/assets/596e21c0-d979-44b9-8923-a3f8050c6494)

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - 藤崎剛暉氏（自由民主党）の2022年、2023年、2024年の財務データを表示する新しいデモページを追加しました。
  - 各年度ごとにプロフィール、財務サマリー、収支内訳、取引明細、メタデータ、注意事項、フッターなどを含むダッシュボードを提供します。
  - デモ一覧ページに藤崎剛暉氏のプロフィールが新たに表示されます。
- **改善**
  - サマリーボードのレポート選択ドロップダウンが、現在のレポートも選択肢に含めるようになりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [PDFからWeb表示用のJSONを作成するシェルスクリプトの追加](https://github.com/digitaldemocracy2030/polimoney/pull/119)

**作成者:** dotneet  
**作成日:** 2025-06-05T16:18:41Z  
**変更:** +106 -36 (6ファイル)  
**マージ日:** 2025-06-05T16:41:36Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->

 - 表題の通りです。 ./scripts/create-json-for-web.sh で PDF => Web用JSON を実行できます。

```
# 下記が成功すれば /reports/hoge でWebからデータが見れます。
./scripts/create-json-for-web.sh hoge.pdf ./public/reports/hoge.json
```

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - PDFファイルをWeb表示用JSONに変換する新しいスクリプトを追加しました。

- **ドキュメント**
  - READMEにPDFからWeb表示用JSONを作成する手順を追加しました。
  - Pythonの必要バージョンを3.10に更新し、画像解析コマンドのオプション説明を修正しました。

- **バグ修正**
  - 画像解析・JSONマージ用スクリプトのコマンドライン引数名をより分かりやすいものに変更しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [レポートページの追加(コミット漏れ)](https://github.com/digitaldemocracy2030/polimoney/pull/117)

**作成者:** dotneet  
**作成日:** 2025-06-05T14:53:39Z  
**変更:** +93 -0 (1ファイル)  
**マージ日:** 2025-06-05T14:56:04Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->

 - #115 のコミット漏れです。一番大事なファイルが抜けてました。。。

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - レポートIDに基づき動的にレポートを表示する新しいページを追加しました。
  - レポートデータの取得に失敗した場合は404ページが表示されます。
  - レポートにはヘッダー、サマリーボード、収入・支出のトランザクションボード、メタデータ、注意事項、フッターが含まれます。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix build and add check Next.js build](https://github.com/digitaldemocracy2030/polimoney/pull/116)

**作成者:** dotneet  
**作成日:** 2025-06-05T14:15:53Z  
**変更:** +12 -4 (3ファイル)  
**マージ日:** 2025-06-05T14:21:59Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->

 - ビルドエラーの修正

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - なし

- **バグ修正**
  - ルートカテゴリ「総収入」の方向が「income」から「expense」に変更されました。

- **その他**
  - 一部のプロパティで許容される値が拡張され、より柔軟に入力できるようになりました。
  - GitHub Actionsのワークフローにビルドチェックが追加され、ビルドの検証が可能になりました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [OCR結果のJSONからWeb表示までできるようにした](https://github.com/digitaldemocracy2030/polimoney/pull/115)

**作成者:** dotneet  
**作成日:** 2025-06-05T13:30:21Z  
**変更:** +1374 -23 (8ファイル)  
**マージ日:** 2025-06-05T14:09:29Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->

 - /reports/[id] で /public/data/[id].json のファイルを取得して表示するUIの作成
 - converter.ts が必要とする出力項目になるように merge_jsons.py を修正

補足

 - 既存の BoardChart.tsx 実装は互換性のために残したが、name を id の代わりに使っており修正が必要だった
 - 日付については十分な対応ができておらず、日付が指定できないtransactionについてはいったん unknown と表示するようにした
 - converter.ts は income と expense の合計不一致のエラーだけはどうしても出てしまうので、--ignore-errors オプションはまだ必要。これ以外のエラーはそこそこ大きな収支報告書で発生しないところまでエラーを潰せた。

fix #109 
fix #108 

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

<img width="1385" alt="image" src="https://github.com/user-attachments/assets/6f29cfc4-e501-47f7-810e-f92c3a722e2f" />


# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

 - OCRからWeb表示まで一気通関で可能にすることで開発やデバッグを容易にする

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - 固定サイズのSankeyチャートを表示する新コンポーネントを追加しました。
  - サンプル用の財務レポートJSONファイル（demo-example.json）を追加しました。

- **機能改善**
  - サマリー画面で新しいチャート表示方式の切り替えができるようになりました。
  - データ変換処理が拡張され、より詳細な財務情報やプロフィール情報を出力できるようになりました。

- **バグ修正**
  - 取引データの方向（income/expense）が厳密に型指定されるようになりました。

- **ドキュメント**
  - 取引リストに集計値を含めない旨の記述を追加しました。

- **テスト**
  - カテゴリ統合や階層整理のロジックに関する単体テストを追加しました。

- **その他**
  - JSONマージツールにカテゴリ重複や階層構造の自動修正機能を追加しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [報告書の基本情報をdemo-ryosukeidei.tsに合わせて設定](https://github.com/digitaldemocracy2030/polimoney/pull/113)

**作成者:** shumizu418128  
**作成日:** 2025-06-05T02:23:43Z  
**変更:** +32 -18 (1ファイル)  
**マージ日:** 2025-06-05T02:30:57Z  
**内容:**

# 変更の概要
#80 で指摘され、#104 でissueとして扱われているように、収支報告書の基本情報を、すでにある形式に合わせてGeminiに取得させる

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - 日本の政治資金報告書から抽出される情報項目が拡充され、組織名、代表者、会計責任者、事務担当者、組織種別、活動地域、資金管理団体指定など、より多くの基本情報が取得されるようになりました。
- **ドキュメント**
  - 抽出手順や出力形式に関する説明がより明確になり、不足項目の扱いや数値の出力形式についても詳細な指示が追加されました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Bump tar-fs from 3.0.8 to 3.0.9](https://github.com/digitaldemocracy2030/polimoney/pull/111)

**作成者:** dependabot[bot]  
**作成日:** 2025-06-04T12:39:52Z  
**変更:** +3 -3 (1ファイル)  
**マージ日:** 2025-06-05T02:29:30Z  
**内容:**

Bumps [tar-fs](https://github.com/mafintosh/tar-fs) from 3.0.8 to 3.0.9.
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/mafintosh/tar-fs/commit/2ceedf4cf807e89a071ebd585291aa785c980829"><code>2ceedf4</code></a> 3.0.9</li>
<li><a href="https://github.com/mafintosh/tar-fs/commit/647447b572bc135c41035e82ca7b894f02b17f0f"><code>647447b</code></a> check windows tweak (<a href="https://redirect.github.com/mafintosh/tar-fs/issues/115">#115</a>)</li>
<li>See full diff in <a href="https://github.com/mafintosh/tar-fs/compare/v3.0.8...v3.0.9">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=tar-fs&package-manager=npm_and_yarn&previous-version=3.0.8&new-version=3.0.9)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>Dependabot commands and options</summary>
<br />

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating it. You can achieve the same result by closing it manually
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/digitaldemocracy2030/polimoney/network/alerts).

</details>

**コメント:** なし

---

### [add thumbnail](https://github.com/digitaldemocracy2030/polimoney/pull/110)

**作成者:** dotneet  
**作成日:** 2025-06-04T07:38:31Z  
**変更:** +3 -0 (1ファイル)  
**マージ日:** 2025-06-04T09:35:33Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->

 - #101

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - ページのメタデータにサムネイル画像が追加されました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [代表者名などの基本情報のjsonへの出力](https://github.com/digitaldemocracy2030/polimoney/pull/107)

**作成者:** dotneet  
**作成日:** 2025-06-04T00:59:54Z  
**変更:** +34 -23 (4ファイル)  
**マージ日:** 2025-06-04T12:27:33Z  
**内容:**


# 変更の概要
<!-- ここに変更の概要を記載してください -->
 - 代表者、会計責任者、事務所の所在地、組織の情報をJSONに含める
 - lintエラー修正

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

 - 必要な表示項目がJSONに含まれていないため

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

 - #104

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - 日本の政治資金報告書から抽出される情報が拡張され、年度に加えて代表者名、主たる事務所の所在地、会計責任者名、政治団体名などの基本情報も含まれるようになりました。
  - JSONマージ時に基本情報も統合されるようになりました。

- **スタイル**
  - コードのフォーマットや引数の整列など、可読性向上のための軽微な書式調整を行いました。

- **バグ修正**
  - 画像処理時の例外処理で、IOErrorからOSErrorへの変更を行い、より適切なエラー処理となりました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (4件)

### [openaiとanthropicをサポート](https://github.com/digitaldemocracy2030/polimoney/pull/127)

**作成者:** dotneet  
**作成日:** 2025-06-11T01:13:26Z  
**変更:** +1942 -474 (16ファイル)  
**内容:**

# 変更の概要

 - langchainを導入し、openaiとanthropicのモデルでもOCRが動作するようにした
 - googleのライブラリに基づいた処理は削除
 - ファイル名を analyze_image_gemini.py から analyze_image.py に変更

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

 - gemini以外のモデルの実験が困難であったため

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - LangChainベースのLLMクライアントを導入し、Google Gemini APIに加えてAnthropicやOpenAIのプロバイダーもサポート。
  - コマンドラインでLLMプロバイダーの選択や既存出力スキップが可能に。
  - LLMプロバイダー用の設定管理やテストスクリプトを追加。

- **ドキュメント**
  - 画像解析ツールや関連スクリプトの説明を「Google Gemini API」から「LangChain」や「vLLM」へ更新。
  - 使用方法やプロジェクト構成の記述を新しい仕組みに合わせて修正。

- **リファクタ**
  - Gemini専用実装を汎用LLMクライアントに置き換え、依存性注入やエラー処理を改善。
  - インターフェースやクラス構成の見直しにより拡張性を向上。

- **その他**
  - プロジェクト名や依存パッケージをLLMベースに変更。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [シェアボタンの実装](https://github.com/digitaldemocracy2030/polimoney/pull/126)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-06-10T21:40:06Z  
**変更:** +244 -20 (4ファイル)  
**内容:**

# 変更の概要
シェアボタンを実装しました

# スクリーンショット
-変更後
![スクリーンショット 2025-06-11 5 57 41（2）](https://github.com/user-attachments/assets/20253618-b65a-481a-8fa3-62314fd59a96)
![スクリーンショット 2025-06-11 5 57 49（2）](https://github.com/user-attachments/assets/a1b8f8f9-9ebc-42a4-a8ec-c4fe8e2a015e)
![スクリーンショット 2025-06-11 5 57 52（2）](https://github.com/user-attachments/assets/ac383fea-607c-4c14-b023-24df7872c731)



# 変更の背景
シェアボタンがあることでビューワー(市民)の能動的な参加につながる。ユーザー(政治家)もより見られている意識が高まる。
polimoneyの認知度向上にもつながる。

# 関連Issue
[シェアボタンの実装#103](https://github.com/digitaldemocracy2030/polimoney/issues/103)

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - ページ上にSNS共有パネルを追加し、LINE・Facebook・X（Twitter）でのシェアやURLコピーが可能になりました。

- **依存関係の変更**
  - SNS共有機能のための新しいライブラリを追加しました。
  - Reactのバージョンをダウングレードしました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [サンキー図のコピー機能](https://github.com/digitaldemocracy2030/polimoney/pull/125)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-06-10T21:18:00Z  
**変更:** +1460 -866 (3ファイル)  
**内容:**

# 変更の概要
サンキー図をコピーできる機能を実装しました。

# スクリーンショット
-変更後
![スクリーンショット 2025-06-11 6 06 43（2）](https://github.com/user-attachments/assets/cdeccd0d-3e99-47f9-9c54-f4fd9a7264c7)
![スクリーンショット 2025-06-11 6 06 48（2）](https://github.com/user-attachments/assets/896ac15e-727d-4390-9466-6d7475669352)
-googleドキュメントに添付した例
![スクリーンショット 2025-06-11 6 07 18（2）](https://github.com/user-attachments/assets/a13f95dc-c9ff-4b81-85e7-6d7c9818e4f1)


# 変更の背景
シェアする際にページのリンクを共有するだけでなくて、サンキー図そのものを資料として使いたい需要があると思ったので作成しました。

# 関連Issue
[サンキー図のコピー機能 #124](https://github.com/digitaldemocracy2030/polimoney/issues/124)

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - サマリーセクションを画像としてクリップボードにコピーできるボタンを追加しました。コピー成功時には確認メッセージが表示されます。

- **その他**
  - 必要な依存パッケージの追加およびバージョン更新を行いました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [coderabbitに日本語をしゃべらせる](https://github.com/digitaldemocracy2030/polimoney/pull/114)

**作成者:** shumizu418128  
**作成日:** 2025-06-05T02:28:22Z  
**変更:** +1 -0 (1ファイル)  
**内容:**

# 変更の概要
coderabbitに日本語をしゃべらせる

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - 日本語（ja-JP）設定用の新しい構成ファイルが追加されました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

