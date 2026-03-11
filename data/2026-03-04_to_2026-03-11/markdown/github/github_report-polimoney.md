# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2026-03-04T12:51:07.643448+09:00 から 2026-03-11T12:51:07.643448+09:00 まで

## Issues

### 過去7日間に完了されたissue (1件)

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

### 過去7日間に作成されたissue (0件)

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (1件)

### [フロントエンドのコード整理](https://github.com/digitaldemocracy2030/polimoney/pull/247)

**作成者:** grassfieldk  
**作成日:** 2026-01-29T12:47:21Z  
**変更:** +1743 -20230 (158ファイル)  
**マージ日:** 2026-03-05T10:29:46Z  
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

* **構造の最適化**
  * フロントエンドを専用ディレクトリに集約し、プロジェクト構成を整理しました。

* **デプロイメント改善**
  * GitHub PagesからVercel中心のデプロイへ移行し、フロントエンド向けビルド設定を更新しました。

* **削除/整理**
  * バックエンド関連のサービス・ツール群、画像/データ生成ツール、及び多くのドキュメントやサンプルデータを削除・整理しました。

* **ドキュメント**
  * README等の説明を簡潔化・再構成しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

