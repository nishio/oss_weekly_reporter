# GitHub レポート: digitaldemocracy2030/idobata

期間: 2025-10-08T12:23:36.073406+09:00 から 2025-10-15T12:23:36.073406+09:00 まで

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

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

