# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2026-09-30T19:04:47.470422+09:00 から 2026-10-07T19:04:47.470422+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (0件)

### 過去7日間に作成されたPR (1件)

### [chore(ci): update GitHub Actions and pin to commit SHAs](https://github.com/digitaldemocracy2030/polimoney/pull/258)

**作成者:** noritaka1166  
**作成日:** 2026-10-03T17:40:38Z  
**変更:** +4 -4 (2ファイル)  
**内容:**

## 変更の概要

GitHub Actions を最新の安定版に更新し、すべての参照を40桁のコミット SHA に固定。

対応するバージョンはコメントに記載。

| Action | 更新前 | 更新後 |
|---|---|---|
| actions/checkout | v4.2.2 | v7.0.1 |
| actions/setup-node | v4.4.0 | v7.0.0 |
| actions/cache | v4.2.3 | v6.1.0 |
| actions/github-script | v6 | v9.0.0 |

以下の検証を実施。

- ワークフローの YAML とスクリプトの構文検証
- 公式リリースとコミット SHA の照合

GitHub 上での CI 実行は未実施

## 変更の背景

各アクションの修正を取り込むため、最新の安定版に更新。

また、タグの参照先変更によって実行されるコードが変わることを防ぐため、コミット SHA に固定。

## スクリーンショット

該当なし（UI の変更なし）

## 関連Issue

なし

## CLAへの同意

本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"[ ]" を "[x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Chores**
  * GitHub Actions の利用バージョンを更新しました。コメントによる割り当て・解除の動作や、Node.js のバージョン、キャッシュ設定に変更はありません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

