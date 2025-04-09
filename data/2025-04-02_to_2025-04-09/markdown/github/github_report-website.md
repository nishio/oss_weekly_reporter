# GitHub レポート: digitaldemocracy2030/website

期間: 2025-04-02 から 2025-04-09 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (1件)

### [SEO的に必要なメタタグ等の項目の整理](https://github.com/digitaldemocracy2030/website/issues/12)

**作成者:** rysh  
**作成日:** 2025-04-05T03:29:27Z  
**内容:**

Twitterカードがなかったり、リンク先の概要が見えなかったりすると、クリック率が顕著に落ちる。高度なSEOは必要ないが、意欲のあるプロジェクトであることをアピールするためには当たり前品質には達していたい

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (4件)

### [Fix: Add generateStaticParams function for dynamic routes](https://github.com/digitaldemocracy2030/website/pull/14)

**作成者:** nishio  
**作成日:** 2025-04-05T11:49:19Z  
**変更:** +24 -9 (1ファイル)  
**マージ日:** 2025-04-05T11:49:28Z  
**内容:**

## 問題
GitHub Actionsのビルドで以下のエラーが発生していました：
[Error: Page "/activity/[slug]" is missing "generateStaticParams()" so it cannot be used with "output: export" config.]

## 修正内容
- `app/activity/[slug]/page.tsx`に`generateStaticParams()`関数を追加
- 「github」または「slack」で始まるMarkdownファイルだけを検出し、対応するスラッグを生成するように設定

この修正により、Next.jsのビルド時に必要な静的ページだけが生成されるようになり、`output: export`設定でも正常にビルドできるようになります。

**コメント:** なし

---

### [fix promise slug & lint](https://github.com/digitaldemocracy2030/website/pull/13)

**作成者:** nanocloudx  
**作成日:** 2025-04-05T06:20:27Z  
**変更:** +135 -150 (7ファイル)  
**マージ日:** 2025-04-05T06:20:51Z  
**内容:**

内容なし

**コメント:** なし

---

### [毎週の活動ページを表示する仕組みを作成](https://github.com/digitaldemocracy2030/website/pull/11)

**作成者:** nishio  
**作成日:** 2025-04-04T03:51:11Z  
**変更:** +741 -2 (13ファイル)  
**マージ日:** 2025-04-05T03:59:55Z  
**内容:**

3週間分のSlack活動まとめを作りました。トップからはまだリンクしていません。この方針で良さそうなら今後GitHub版を作ります。GitHub版はrepoごとに作られる予定です。
各レポート間のnavigationは改善が必要です。現在は何もありません。

# 活動記録機能の追加

## 変更内容
- Slack活動記録（第1〜3週）を追加しました
- GitHub活動記録（第1週, sample）を追加しました
- 活動記録を表示するための機能を実装しました
  - 活動記録一覧ページ（`app/activity/page.tsx`）
  - 活動記録詳細ページ（`app/activity/[slug]/page.tsx`）

## 背景・目的
デジタル民主主義2030プロジェクトの活動を透明化し、コミュニティメンバーや興味を持つ方々に共有するため、SlackとGitHubでの活動記録を閲覧できる機能を追加しました。

## 技術的詳細
- マークダウンファイルを使用して活動記録を管理（`markdown/`ディレクトリ）
- Next.jsのダイナミックルーティングを活用して、各活動記録の詳細ページを実装
- ファイル名の先頭（「slack」または「github」）に基づいて、活動記録を自動的に分類して表示

## 今後の展開
- 今後も週次でSlackとGitHubの活動記録を追加していく予定です

**コメント:** なし

---

### [Slackへのリンクを無期限にする](https://github.com/digitaldemocracy2030/website/pull/10)

**作成者:** nishio  
**作成日:** 2025-03-28T04:49:02Z  
**変更:** +2 -2 (2ファイル)  
**マージ日:** 2025-04-05T03:59:26Z  
**内容:**

内容なし

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

