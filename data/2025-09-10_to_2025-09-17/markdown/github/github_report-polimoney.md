# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-09-10T12:16:11.970916+09:00 から 2025-09-17T12:16:11.970916+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (2件)

### [資金項目データ定義方法の統一](https://github.com/digitaldemocracy2030/polimoney/issues/199)

**作成者:** grassfieldk  
**作成日:** 2025-09-14T15:07:26Z  
**内容:**

## 解決・改善したいこと

データ定義ファイル（`data/demo-*.ts`）間でデータ構造がばらばらになっているため、統一する

**現在の問題点：**
- `getDataByYear`関数の実装方法が各ファイルで異なる（シンプルな実装 vs 複雑なフォールバック機能付き）
- `demo-comingsoon.ts`では`getDataByYear`関数が存在しない
- 関数定義方法が混在（arrow function vs function declaration）
- 型定義が異なる（`Profile` vs `ProfileList`）
- 一部ファイルのみに追加機能（`getDataByPath`）が存在


## 具体的な実現方法・実装方法の概要

1. **`getDataByYear`関数の統一**
   - 全ファイルで同じ実装パターンに統一
   - `demo-comingsoon.ts`に不足している`getDataByYear`関数を追加

2. **関数定義方法の統一**
   - arrow function または function declaration のどちらかに統一

3. **型定義の統一**
   - `Profile`型で統一（`ProfileList`の使用を見直し）

4. **追加機能の取扱い**
   - `getDataByPath`のような追加機能の必要性を検討し、必要であれば全ファイルに実装

5. **テンプレートまたはスキーマの作成**
   - 新しいデータファイル作成時のガイドライン策定

## 関連 Issue

- blocks #197 

**コメント:** なし

---

### [サンキー図・一覧表のデータを統一](https://github.com/digitaldemocracy2030/polimoney/issues/197)

**作成者:** grassfieldk  
**作成日:** 2025-09-12T07:37:15Z  
**内容:**

## 解決・改善したいこと

各議員ページに表示する資金項目データのフォーマット統一を図りたい

サンキー図用に Flow / Transaction の２つのデータ型が存在しているため、これを統合したい


## Flow と Transaction の関係

Flow: サンキー図用のデータ、カテゴリごとの合計値
Transaction: 収支一覧用のデータ、各項目の詳細

Flow は Transaction から生成可能
ページ表示時に生成してもよいが、プレ生成しているのが現状

### 整合性要件

- Transaction の category ごとに Flow が存在すること（総収入は除く）
- Flow と同じ category を持つ Transaction[].amount 合計値が Flow.value になっていること


## 対応方針

下記に示す通り現状不整合が起きているが、あくまででもデータのため問題ではない
ただ Flow は動的生成できるため Transaction さえあればよく、生成処理の負荷も非常に低いはず
また今後 RDB などを使えばビューなどで処理を DB に任せることも可能

よって、サンキー図のデータは整合性が確実に担保される動的生成に変更する


## 現状

現在定義されているデータに不整合あり
※ チェック用スクリプトで確認

```plaintext
[demo-comingsoon.ts] OK
[demo-example.ts] category='寄附' の Flow が存在しません
[demo-example.ts] Flow.name='個人からの寄附' に対応する Transaction がありません
[demo-example.ts] Flow.name='総収入' に対応する Transaction がありません
[demo-example.ts] Flow.name='翌年への繰越額' に対応する Transaction がありません
[demo-example.ts] Flow.name='人件費' に対応する Transaction がありません
[demo-kokifujisaki.ts] category='前年繰越' の Flow が存在しません
[demo-kokifujisaki.ts] category='党費・会費' の Flow が存在しません
[demo-kokifujisaki.ts] category='交付金' の Flow が存在しません
[demo-kokifujisaki.ts] Flow.name='前年からの繰越額' に対応する Transaction がありません
[demo-kokifujisaki.ts] Flow.name='本年の収入額' に対応する Transaction がありません
[demo-kokifujisaki.ts] Flow.name='個人の負担する党費又は会費' に対応する Transaction がありません
[demo-kokifujisaki.ts] Flow.name='本部又は支部から供与された交付金' に対応する Transaction がありません
[demo-kokifujisaki.ts] Flow.name='総収入' に対応する Transaction がありません
[demo-kokifujisaki.ts] Flow.name='組織活動費' に対応する Transaction がありません
[demo-kokifujisaki.ts] Flow.name='翌年への繰越' に対応する Transaction がありません
[demo-ryosukeidei.ts] category='前年繰越' の Flow が存在しません
[demo-ryosukeidei.ts] category='党費・会費' の Flow が存在しません
[demo-ryosukeidei.ts] category='交付金' の Flow が存在しません
[demo-ryosukeidei.ts] category='その他収入' の Flow が存在しません
[demo-ryosukeidei.ts] category='政治活動費' の合計値不一致: Transaction合計=7723335, Flow.value=14575541
[demo-ryosukeidei.ts] Flow.name='前年からの繰越額' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='個人の負担する党費又は会費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='個人からの寄附' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='法人その他の団体からの寄附' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='政治団体からの寄附' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='本部又は支部から供与された交付金' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='その他の収入' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='本年の収入額' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='総収入' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='人件費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='光熱水費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='備品・消耗品費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='事務所費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='組織活動費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='選挙関係費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='宣伝事業費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='寄附・交付金' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='翌年への繰越' に対応する Transaction がありません
[demo-takahiroanno.ts] category='組織活動費' の Flow が存在しません
[demo-takahiroanno.ts] Flow.name='総収入' に対応する Transaction がありません
[demo-takahiroanno.ts] Flow.name='事務所費' に対応する Transaction がありません
[demo-takahiroanno.ts] Flow.name='宣伝事業費' に対応する Transaction がありません
[demo-takahiroanno.ts] Flow.name='政治活動費' に対応する Transaction がありません
[demo-takahiroanno.ts] Flow.name='翌年への繰越額' に対応する Transaction がありません
```

## 関連 Issue

- blocked by #199 
- blocks #166 
- relates to #32 

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(3件)

### [選挙運動費用収支報告書に対応](https://github.com/digitaldemocracy2030/polimoney/issues/191)

**作成者:** shumizu418128  
**作成日:** 2025-09-02T05:59:44Z  
**内容:**

現時点では、和歌山県議員・[岩永さんの選挙運動費用収支報告書](https://drive.google.com/drive/folders/13bMJ4q2mOg_CtAg1YUSe9RrK1U04cn3q)に対応することを目指す。

政治資金収支報告書とは別の書類であり、ルールが変わってくるため、データ構造形式など検討が必要。
参考Slack：https://dd2030.slack.com/archives/C08FL5L6GSH/p1756387625940919

※Slackにまだ参加していない方は私をメンションしてください
招待URLを差し上げます

**コメント:** なし

---

### [理解の助けになるよう、収支項目の解説を書き込む](https://github.com/digitaldemocracy2030/polimoney/issues/166)

**作成者:** grassfieldk  
**作成日:** 2025-07-29T12:26:57Z  
**内容:**

## 解決・改善したいこと

起票者である私も含め、政治や経済についての知識が浅い人間が見たときの助けとなる UI/UX の導入を図りたい
現在の状態でもなんとなく


## 具体的な実現方法・実装方法の概要（未記入でも構いません）

### ツールチップによる補足説明

すでに [こちらのページ](https://polimoney.dd2030.org/takahiro-anno/2024) の [支出の一覧] にも限定的に実装はされていますが、
全体的に専門用語や意図が掴みづらい表現などの解説を導入すべきかと思います

例えば "個人からの寄附" という項目について、私のようなリテラシのない人間からすれば
「政治家って個人からの寄附もらっていいの？」「そもそも寄附ってどうするの？できるなら自分もしたい」
という疑問が浮かびます
正直、国民の大半の政治知識レベルはその程度だと思います（悲観しているわけではなく、事実として）

ですので、下記画像のようにツールチップによる補足説明が充実していれば、なんとなくお金の動きを見たいだけだったユーザーもより政治の仕組みについて詳しくなれ、興味を持ちやすくなっていくと思います
<img width="1334" height="669" alt="Image" src="https://github.com/user-attachments/assets/69cff889-8a1e-435b-a7e1-fd79518c1074" />

ちなみに、ソニー損保の契約ページなどがとてもわかり易く参考になるかと思います
保険契約をするうえで出てくる専門用語や会社独自のサービス名などの説明がツールチップでされており、非常にわかりやすく難解なはずの保険契約で困ったことがありません
※ 契約を持っていなくても新規契約ページの閲覧は可能です

---

あらゆる事象や活動の可視化による国民が監視しやすい仕組みを作ることの物理的効果だけでなく、
誰もが見やすく興味を持てるような仕組みを取り入れていくことで、より多くの人が政治に関心を持つ心理的な効果をねらっていきたいと感じました


## 関連 Issue

- blocked by #197 

**コメント:** なし

---

### [データベース移行](https://github.com/digitaldemocracy2030/polimoney/issues/32)

**作成者:** nanocloudx  
**作成日:** 2025-04-30T13:49:38Z  
**内容:**

既に公開している数件のデータはデモとして GitHub Pages に公開している
今後の流れとしてより沢山のデータを扱うことを見越して、データを Postgres に記録していく

同様にレポートは「ブラウザ→API→Postgres」からデータを取得して表示する仕組みに変更する

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (2件)

### [報告書アップロード用のエンドポイントを追加](https://github.com/digitaldemocracy2030/polimoney/pull/198)

**作成者:** shumizu418128  
**作成日:** 2025-09-14T08:06:47Z  
**変更:** +788 -2 (9ファイル)  
**マージ日:** 2025-09-14T12:58:49Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
収支報告書のデータをアップロードするエンドポイントを用意
型は決まってないので未設定

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->
#120 #32 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - 管理者向けに政治資金・選挙資金の登録APIを追加（/api/v1/admin/political_funds, /api/v1/admin/election_funds）。JWT認証が必須。
  - サーバー側で詳細な入力バリデーションを導入し、不正入力時は400、保存失敗時は500を返却。
  - 登録成功時にステータスと送信データをJSONで返却。
  - 各種登録データの保存・検索を想定したモデルとクエリ機能を追加。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [東京都　運動費用収支報告書](https://github.com/digitaldemocracy2030/polimoney/pull/196)

**作成者:** shumizu418128  
**作成日:** 2025-09-11T11:16:01Z  
**変更:** +654 -110 (14ファイル)  
**マージ日:** 2025-09-11T11:35:47Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
#191 
東京都にも対応
また、今後他の地域にも対応できるよう、READMEを策定

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

- 新機能
  - 東京向けの選挙収支解析を追加し、Excelから各カテゴリのJSONを自動生成、コマンドライン実行に対応。
- ドキュメント
  - 都道府県別の実装ガイドと命名・出力規約を追加。
- リファクタ
  - 列定義と数値抽出処理を共通化し、既存処理を移行して数値解析の堅牢性を向上。
  - 出力を入力ファイルごとのサブフォルダに整理。
- 雑務
  - .gitignoreをディレクトリ単位に拡張。
  - 使用方法メッセージを修正。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (1件)

### [#199 データ定義方法の統一](https://github.com/digitaldemocracy2030/polimoney/pull/200)

**作成者:** grassfieldk  
**作成日:** 2025-09-14T18:05:09Z  
**変更:** +1406 -1171 (15ファイル)  
**内容:**

## 変更の概要

資金項目のデータ定義（`data/demo-*.ts`）の方法がバラバラであったため統一


## 変更の背景

データ構造が異なることにより、型定義の修正やそれに関連するロジック修正でエラーが起きやすくなっていた
データ定義を統一することでデータモデルの可読性を上げ、今後のデータまわりの作業効率を上げる

## 関連 Issue

- #199 


## CLAへの同意

本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- Refactor
  - データ構造を年別に再編し、フィールド名を datas → data に統一。関連画面の読み込みと表示を安定化。
  - レポート詳細ページ（/reports/[id]）を削除し、関連処理を整理。
- Documentation
  - Flow と Transaction の整合性方針を記したメモを追加。
- Chores
  - TypeScript 型チェック／ウォッチ用の VSCode タスクを追加。
  - データ整合性を検証するスクリプトを追加。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

