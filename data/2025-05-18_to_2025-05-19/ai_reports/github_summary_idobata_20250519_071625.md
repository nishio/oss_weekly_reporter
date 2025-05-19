# いどばたシステム 5/18~5/19のGitHub活動まとめ

いどばたシステム（idobata-*）のOSS開発に興味を持ってくださる方々へ、5/18から5/19にかけてのGitHub上での活動状況をまとめました。新機能の追加や既存機能の改善のために、さまざまな貢献が行われています。ぜひご一読いただき、興味のある方はぜひ議論やコントリビューションに参加してみてください！

---

## 今週完了した内容

### マージされたPR

- [PR #334](https://github.com/digitaldemocracy2030/idobata/pull/334) 「Add: factcheck function」  
  - 作者: jujunjun110  
  - 概要: ファクトチェック機能を実装するための手順書を作成  
  - 変更数: +719行 / -0行 (1ファイル)  
  - コメント: ファクトチェック機能のプロトタイプを形にする第一歩として、手順を示すドキュメントが追加されました。これにより、今後のコントリビューターがファクトチェック実装をスムーズに行えるようになります。

今回、Issueのクローズ（完了）はありませんでした。

---

## 未完了のタスク＆進行中の議論

実装途中や検討中のタスクで活発なディスカッションが行われています。引き続きご意見やコントリビューションをお待ちしています。

### 1. 新規作成されたIssue

- [Issue #336](https://github.com/digitaldemocracy2030/idobata/issues/336) 「論点ページがどのテーマの論点なのかわからない」  
  - 作成者: Gurz1019MP  
  - 内容: テーマページではパンくずリストに各テーマ情報が表示される一方、論点ページでは「テーマ」固定表示のため、どのテーマに属する論点かがわかりにくいという問題。パンくずリストを可変表示にすることで解決できないか現在検討中です。

### 2. 更新されたIssue

- [Issue #265](https://github.com/digitaldemocracy2030/idobata/issues/265) 「課題点や解決策の数が他テーマの内容を含んで集計されてしまう」  
  - 作成者: masatosasano2  
  - 内容: 課題点や解決策の集計範囲が正しくフィルタリングされておらず、他テーマの情報が含まれる不具合について議論が続いています。ログやデータ構造の見直しによる修正が必要とされています。

### 3. 新規作成されたPR

- [PR #335](https://github.com/digitaldemocracy2030/idobata/pull/335) 「ファクトチェック機能の実装」  
  - 作者: jujunjun110+Devin  
  - 概要: PRに「/fc」とコメントすると自動的にファクトチェックが実行される仕組みを提案。ChatGPT O3を活用することで、変更差分をレビューするAIアシスタントとして機能します。今後、API連携や認証方法などの詳細が詰められる見込みです。

- [PR #333](https://github.com/digitaldemocracy2030/idobata/pull/333) 「Add factcheck implementation guide」  
  - 作者: jujunjun110+Devin  
  - 概要: ファクトチェック機能をGitHub連携で実装するためのガイドラインを追加。GitHub ActionsとOpenAI GPT-4oの連携方法、認証周りの設定などが詳しく書かれています。こちらも今後のディスカッションに注目が集まっています。

---

## どんな貢献が求められているのか

- テーマページや論点ページのUI/UX改善（[Issue #336](https://github.com/digitaldemocracy2030/idobata/issues/336)）  
  → パンくずリストの柔軟な実装方法、表示内容に関するアイデア募集  
- 集計ロジックのバグ修正（[Issue #265](https://github.com/digitaldemocracy2030/idobata/issues/265)）  
  → データ集計時のフィルタリング処理の見直しやテストケース追加  
- ファクトチェック機能の実装・改善（[PR #335](https://github.com/digitaldemocracy2030/idobata/pull/335)、[PR #333](https://github.com/digitaldemocracy2030/idobata/pull/333)）  
  → ChatGPT O3連携、GitHub Actionsワークフロー、API認証についての議論・コードレビュー

リポジトリを盛り上げるために、ぜひIssueで議論したり、PRにコメントしたりしてみてください。コードを書く以外にも、ドキュメント整備やUIデザイン、ユーザビリティ向上のアイデアなど、さまざまな形での貢献が歓迎されています。

---

## 参加やコントリビュートについて

- まずは[Issue #336](https://github.com/digitaldemocracy2030/idobata/issues/336)や[Issue #265](https://github.com/digitaldemocracy2030/idobata/issues/265)など、興味のあるIssueをチェックしてみてください。  
- 追加の改善案や技術的な助言があれば、遠慮なくコメントしてください。  
- PRのレビューも大歓迎です。特に[PR #335](https://github.com/digitaldemocracy2030/idobata/pull/335)や[PR #333](https://github.com/digitaldemocracy2030/idobata/pull/333)に対して「こうしたほうがいい」というアイデアがあれば、ぜひ共有をお願いします。

いどばたシステムがより使いやすく、民主的な議論をサポートするプラットフォームとして成長できるよう、皆様の参加をお待ちしております。今後とも、どうぞよろしくお願いいたします。