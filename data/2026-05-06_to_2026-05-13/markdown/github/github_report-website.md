# GitHub レポート: digitaldemocracy2030/website

期間: 2026-05-06T13:24:55.899486+09:00 から 2026-05-13T13:24:55.899486+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (1件)

### [広聴AIの「使い方を見てみる」のリンクが切れている](https://github.com/digitaldemocracy2030/website/issues/213)

**作成者:** shingo-ohki  
**作成日:** 2026-05-12T10:29:10Z  
**内容:**

https://dd2030.org/kouchou-ai/
このページの「使い方を見てみる」のリンクが切れている。
現状
https://github.com/digitaldemocracy2030/kouchou-ai/tree/main/how_to_use
正しくはこれ
https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/docs/user-guide/how-to-use.md

おそらくドキュメント整理のときに website 側のリンクの更新が漏れたのかも。

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (1件)

### [ブロードリスニングのページを追加し「5つの取り組み」に更新](https://github.com/digitaldemocracy2030/website/pull/212)

**作成者:** nishio  
**作成日:** 2026-05-09T04:06:00Z  
**変更:** +121 -5 (3ファイル)  
**マージ日:** 2026-05-09T09:14:43Z  
**内容:**

## Summary
- 第5の活動として「ブロードリスニング」（解説書出版プロジェクト）を `kouchou-ai` などと並列に追加
- 広聴AIの位置づけを「ブロードリスニングを支援するツール開発」として整理
- ドロワーメニューに「ブロードリスニング」を追加

## 変更内容
- 新規 `src/broad-listening/index.vto`
  - 書籍サイト（ja/en）への導線
  - 背景・歴史（2025-08-13〜2026-05-04）
  - About / Feedback / Wiki への関連リソース
  - 関連プロジェクトとして広聴AIへリンク
  - GitHub（原書 / 英訳 / 書籍サイト）
- `src/index.vto`
  - 「4つの取り組み」→「5つの取り組み」
  - ブロードリスニングのカードを追加
  - 広聴AI のタグライン・説明文を新しい位置づけに合わせて調整
- `src/_components/drawer.vto`
  - ドロワーメニューに「ブロードリスニング」を追加

## 背景
Slackでの議論（@nishio / @ohki）を踏まえ、書籍プロジェクトを広聴AIと並列の第5の活動として配置する方針を採用しました。dd2030.org 側はフラットに5プロジェクトを露出させ、`broadlisteningbook.com` 側からは広聴AIを「DD2030が開発するブロードリスニング支援OSSツールの一つ」として相互リンクする構成を想定しています。

## Test plan
- [x] `CMS_PASSWORD=dev deno task serve` でローカル起動し、以下を確認：
  - [x] `/` ホームの「5つの取り組み」にブロードリスニングカードが表示される
  - [x] `/broad-listening/` が表示され、各リンクが正しく開く
  - [x] ドロワーメニューに「ブロードリスニング」が出る
  - [x] 広聴AIカードのタグライン・説明文の変更が意図どおり

<img width="3308" height="1900" alt="image" src="https://github.com/user-attachments/assets/867f6e3d-a9e4-489c-b075-8d22a4d9c50e" />

🤖 Generated with [Claude Code](https://claude.com/claude-code)

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [Week51 Summary Update](https://github.com/digitaldemocracy2030/website/pull/211)

**作成者:** github-actions[bot]  
**作成日:** 2026-04-22T05:37:04Z  
**変更:** +55 -0 (2ファイル)  
**内容:**

Auto-generated weekly summaries for week51

**コメント:** なし

---

