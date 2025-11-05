# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-10-29T12:27:23.619837+09:00 から 2025-11-05T12:27:23.619837+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (2件)

### [設定の更新](https://github.com/digitaldemocracy2030/polimoney/pull/220)

**作成者:** grassfieldk  
**作成日:** 2025-10-26T07:25:44Z  
**変更:** +93 -2 (3ファイル)  
**マージ日:** 2025-11-03T06:15:59Z  
**内容:**

## 変更の概要

- Biome 設定の変更
- Copilot 指示書の作成


## 変更の背景

- Biome のバージョンが固定されておらず、環境によりフォーマットなどが統一されない問題があったため修正
- GitHub Copilot の出力の品質を高めるため指示書を作成

## 関連Issue

なし


## CLAへの同意

本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

## リリースノート

* **Documentation**
  * 開発ガイダンス用のドキュメントを追加しました。

* **Chores**
  * 開発用ツールの依存関係を更新しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [#197 サンキー図・一覧表のデータを統一](https://github.com/digitaldemocracy2030/polimoney/pull/208)

**作成者:** grassfieldk  
**作成日:** 2025-10-24T10:52:52Z  
**変更:** +3049 -185 (24ファイル)  
**マージ日:** 2025-11-03T08:34:41Z  
**内容:**

## 変更の概要

サンキー図用のデータ `Flow` を `Transaction` から生成するように変更

既存の実装との比較のため、新しい実装を適用したコードは各自 uniformed ディレクトリを作成しそこに作成し
新規ページとして実装（アクセス例: /uniformed/takahiro-anno/2024/）

将来的な機能追加の準備も兼ね、ログインしていないと該当ページが表示されないように
※ Auth0 を使用


## 変更の背景

関連 Issue を参照


## 関連Issue

- #199


## CLAへの同意

本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

## リリースノート

* **新機能**
  * ユーザー認証とアカウント管理機能を追加
  * 政治資金収支データの動的表示ページを実装
  * 収支フローを可視化するインタラクティブダッシュボードを提供
  * 画像クリップボード機能で要約をコピー可能に

* **改善**
  * ヘッダーレイアウトをレスポンシブデザインに改善
  * SNS共有機能をドロップダウンメニューに統合
  * 複数年のデータ対応と表示ロジックを最適化
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

