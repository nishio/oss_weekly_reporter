# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-12-10T12:34:36.971874+09:00 から 2025-12-17T12:34:36.971874+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (1件)

### [選挙運動費用収支報告書の分析時、metadata取得](https://github.com/digitaldemocracy2030/polimoney/issues/236)

**作成者:** shumizu418128  
**作成日:** 2025-12-16T05:07:28Z  
**内容:**

TODO: excelの分析だけではすべての情報はとれないので、今回追加された情報の取得方法はbackendへの導入時に考える

_Originally posted by @shumizu418128 in https://github.com/digitaldemocracy2030/polimoney/issues/235#issuecomment-3658865562_
            

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (3件)

### [選挙運動費用収支報告書用JSONの更新提案](https://github.com/digitaldemocracy2030/polimoney/pull/235)

**作成者:** moai-redcap  
**作成日:** 2025-12-16T05:03:48Z  
**変更:** +832 -0 (3ファイル)  
**マージ日:** 2025-12-16T08:46:57Z  
**内容:**

# 変更の概要
選挙運動費用収支報告書用JSONの更新提案です。meta情報追加、共通識別子の導入などです。

# 変更の背景
会計ソフトや、将来的に公開するであろう外部用APIで、政治家識別子や選挙識別子等が必要になると考えました。

# 関連Issue
なし

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **ドキュメント**
  * Polimoney APIの新しいJSON形式仕様書を追加しました
  * API構造、メタデータ定義、カテゴリコード、サンプルデータを記載
  * JavaScript/TypeScript、Pythonでの実装例を提供

* **新機能**
  * TypeScript型定義をサポート
  * 選挙財務データの実サンプルを追加

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [ゼロ埋めやめる](https://github.com/digitaldemocracy2030/polimoney/pull/234)

**作成者:** shumizu418128  
**作成日:** 2025-12-11T10:16:54Z  
**変更:** +490 -490 (1ファイル)  
**マージ日:** 2025-12-11T10:18:18Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
CSVの団体コード　ゼロ埋めやめる
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


**コメント:** なし

---

### [選挙運動費用収支報告書DB仕様策定](https://github.com/digitaldemocracy2030/polimoney/pull/233)

**作成者:** shumizu418128  
**作成日:** 2025-12-10T12:04:23Z  
**変更:** +1896 -53 (2ファイル)  
**マージ日:** 2025-12-10T12:17:46Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
選挙運動費用収支報告書のDBのカラムをつくりました
総務省が定義した
「都道府県コード及び市区町村コード」
に衆議院・参議院を追加して地域コードとして使用します

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

## リリースノート

* **リファクタリング**
  * 候補者情報を専用のモデルに整理し、氏名、かな、政党、選挙区種別、選挙日など詳細なメタデータを記録できるようにしました
  * 選挙資金・支出のデータを別モデルに分離し、候補者との関連を明確化して参照できるようにしました
  * データ構造と関連付けを見直し、整合性と可搬性を向上させました

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

