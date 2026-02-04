# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2026-01-28T12:51:36.590875+09:00 から 2026-02-04T12:51:36.590875+09:00 まで

## Issues

### 過去7日間に完了されたissue (1件)

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
※ ただし Flow にはカテゴリの親子関係も記録されているため、これについては別途定義が必要

よって、サンキー図のデータは整合性が確実に担保される動的生成に変更する

## 現状

現在定義されているデータに不整合あり
※ チェック用スクリプトで確認

<details>
<summary>不整合の詳細</summary>

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
</details>


## 実装中に気づいた課題など

- カテゴリの親子関係が議員データによって異なる
- Transaction から読み取れない情報が Flows に記載されている


## 関連 Issue

- blocked by #199 
- blocks #166 
- relates to #32 

**コメント:** なし

---

### 過去7日間に作成されたissue (0件)

### 過去7日間に更新されたissue（作成・クローズを除く）(1件)

### [ディレクトリ構成の整理](https://github.com/digitaldemocracy2030/polimoney/issues/218)

**作成者:** grassfieldk  
**作成日:** 2025-10-26T04:41:46Z  
**内容:**

## 解決・改善したいこと

Next.js のコードがプロジェクトルートに並んでおり、共通の設定ファイルなどと区別がつきづらい
また、Next.js のコードだけをみても src ディレクトリが採用されておらず管理がしづらい


## 具体的な実現方法・実装方法の概要（未記入でも構いません）

frontend/ ディレクトリを作成し、次のようにまとめる
※ デプロイの都合上これだとうまくいかない可能性もあるため注意

```
frontend/app/
frontend/components/
frontend/data/
frontend/models/
frontend/public/
frontend/utils/
frontend/next.config.ts
frontend/next-env.d.ts
```

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (0件)

### 過去7日間に作成されたPR (1件)

### [フロントエンドのコード整理](https://github.com/digitaldemocracy2030/polimoney/pull/247)

**作成者:** grassfieldk  
**作成日:** 2026-01-29T12:47:21Z  
**変更:** +1555 -1872 (95ファイル)  
**内容:**

## 変更の概要

- フロントエンドのコードを frontend ディレクトリにまとめる
- Next.js の脆弱性への対応
- 動的エクスポートへの変更およびこれに伴うリファクタリング


## 変更の背景

- ルートディレクトリ配下にフロントエンド・バックエンドのコードが混在し、わかりづらくなっていたため
- デプロイ先を GitHub Pages から Vercel に変えたことにより動的サイトの実行が可能となったため


## 関連Issue

Close: #218 #219 


## CLAへの同意

本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **新機能**
  * 認証ミドルウェアと認証用ルートを追加し、ログイン／ログアウトの挙動をリダイレクトベースに統一

* **リファクタリング**
  * フロントエンド／バックエンドの構成を明確化し、Next.js周りをfrontendディレクトリ中心に再構成
  * レイアウトがサーバーサイドでセッションを取得するよう変更

* **Chores**
  * デプロイ設定をVercelに移行し、ワークスペース設定を導入

* **ドキュメント**
  * パスやデプロイ手順をfrontend中心に更新し、説明を簡素化

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

