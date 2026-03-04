# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2026-02-25T12:50:38.216560+09:00 から 2026-03-04T12:50:38.216560+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (0件)

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [フロントエンドのコード整理](https://github.com/digitaldemocracy2030/polimoney/pull/247)

**作成者:** grassfieldk  
**作成日:** 2026-01-29T12:47:21Z  
**変更:** +1742 -20101 (154ファイル)  
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

## リリースノート

* **構造の最適化**
  * フロントエンド・バックエンド分離により、プロジェクト構造を再編成しました。
  * フロントエンドファイルを `frontend/` ディレクトリに統合しました。

* **デプロイメント改善**
  * GitHub PagesからVercelへの移行により、ホスティングを簡素化しました。
  * ビルドおよびCI/CDパイプラインを更新しました。

* **バックエンド削除**
  * バックエンドサービスおよび関連ツールを削除しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

