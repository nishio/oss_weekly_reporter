# GitHub レポート: digitaldemocracy2030/idobata

期間: 2025-10-15T12:27:13.318175+09:00 から 2025-10-22T12:27:13.318175+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (1件)

### [いどばた政策 policy_edit から github PR 作成時の無用な MCP サーバ経由を削除](https://github.com/digitaldemocracy2030/idobata/issues/470)

**作成者:** kuboon  
**作成日:** 2025-10-15T03:15:39Z  
**内容:**

## 解決・改善したいこと
policy_edit でプルリクを作成時に、別途 MCP サーバを立ち上げてそこへ MCP コールしているが、
https://github.com/digitaldemocracy2030/idobata/blob/35b2667f51a12a891689ad7782bb879704275ffa/policy-edit/backend/src/mcp/idobataMcpService.ts#L128
`openai.chat.completions.create` のレスポンスに含まれている `tool_calls` に必要な情報は全て入っているのでこの情報を使って直接 octokit を実行すれば良い。

asis: callTool -> mcpclient-> mcpserver -> octkit
tobe: callTool -> octkit

この修正により、 github 通信時の進捗確認やエラーハンドリングが容易になり、反応も良くなります。

## 具体的な実現方法・実装方法の概要（未記入でも構いません）
https://github.com/digitaldemocracy2030/idobata/pull/429

> Closing due to inactivity for more than 7 days.

で close されてしまっていますが、 policy_edit を今後も発展させる予定があるのでしたら是非ともマージしたいです。

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(1件)

### [OGP画像を設定し、SNSでシェアしたときにサイトの魅力が閲覧者に伝わりやすくする](https://github.com/digitaldemocracy2030/idobata/issues/19)

**作成者:** jujunjun110  
**作成日:** 2025-04-23T13:55:28Z  
**内容:**

内容なし

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (0件)

### 過去7日間に作成されたPR (1件)

### [README に DeepWiki バッジを追加](https://github.com/digitaldemocracy2030/idobata/pull/471)

**作成者:** noritaka1166  
**作成日:** 2025-10-18T16:07:34Z  
**変更:** +2 -0 (1ファイル)  
**内容:**

# 変更の概要
README に DeepWiki バッジを追加

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
公聴AI のリポジトリに DeepWiki のバッジがあるのを見かけたので、 idobata にも追加してみました

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [OGP設定（エンドポイント変更対応）](https://github.com/digitaldemocracy2030/idobata/pull/184)

**作成者:** ghost  
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

