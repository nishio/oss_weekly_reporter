# デジタル民主主義WEB 4/23〜4/30 のGitHub活動まとめ

今週(2025/4/23〜4/30)の「デジタル民主主義WEB」リポジトリで行われた活動をまとめました。新機能や改善点を知ることで、開発に参加するきっかけになれば幸いです。

---

## 今週完了した主な作業

### ドキュメントページ（Docsページ）の新設と関連修正
- [Issue #41](https://github.com/digitaldemocracy2030/website/issues/41) の完了に伴い、Docsページの内容を整備。  
- 複数のPRがマージされ、ビルドエラー対応やページ構成の改善が随時行われました。  
  - [PR #48](https://github.com/digitaldemocracy2030/website/pull/48), [PR #51](https://github.com/digitaldemocracy2030/website/pull/51), [PR #53](https://github.com/digitaldemocracy2030/website/pull/53), [PR #54](https://github.com/digitaldemocracy2030/website/pull/54), [PR #55](https://github.com/digitaldemocracy2030/website/pull/55), [PR #56](https://github.com/digitaldemocracy2030/website/pull/56) などを中心に、主に moai-redcap さんや <NISHIO Hirokazu+Devin> さんの貢献が光っています。  
- これによりプロジェクトの使い方やFAQなどを追加しやすくなり、ユーザビリティと開発者の作業効率がアップしました。

### 広聴AI v2.0.0リリース関連
- [Issue #36](https://github.com/digitaldemocracy2030/website/issues/36) の対応として、Next.js のセキュリティ更新と一部依存関係の修正を実施。  
- [PR #47](https://github.com/digitaldemocracy2030/website/pull/47), [PR #49](https://github.com/digitaldemocracy2030/website/pull/49), [PR #57](https://github.com/digitaldemocracy2030/website/pull/57) では、広聴AI v2.0.0 リリース情報のページとコントリビューターリスト追加などを行い、<NISHIO Hirokazu+Devin> さんの寄与が目立ちました。  
- 新機能や改善点がまとめられたリリースノートを公開することで、開発に参加していない人にもソフトウェアの進化をわかりやすくアピールできています。

### Next.js のアップデート
- [PR #45](https://github.com/digitaldemocracy2030/website/pull/45), [PR #46](https://github.com/digitaldemocracy2030/website/pull/46) によって、Next.js が最新の安定版にアップデートされました。  
- moai-redcap さんによる作業で、GitHubのセキュリティ通知 ( [Issue #36](https://github.com/digitaldemocracy2030/website/issues/36) ) への対応も同時に進行し、セキュリティ向上に貢献しています。

### その他の小さな改善
- [PR #42](https://github.com/digitaldemocracy2030/website/pull/42) でのタイポ修正(nakasyouさん)など、見た目・表記の修正が細やかに行われました。  
- [PR #35](https://github.com/digitaldemocracy2030/website/pull/35) で、広聴AIの歴史セクションが追加され、<NISHIO Hirokazu+Devin> さんが執筆。背景や経緯をわかりやすく紹介しています。  
- [PR #34](https://github.com/digitaldemocracy2030/website/pull/34) では、nishio さんが第6週の活動まとめを追加。過去の進捗を振り返りやすくなりました。  

---

## 未完了のタスク・進行中の議論

### PRプレビューデプロイメントの実装
- [Issue #50](https://github.com/digitaldemocracy2030/website/issues/50) に対応する [PR #52](https://github.com/digitaldemocracy2030/website/pull/52) がまだマージされていません。  
- PRが作成されるたびに自動プレビュー環境がデプロイされる運用を構築する試みで、<NISHIO Hirokazu+Devin> さんが実装を進め中。レビューやテストに興味がある方はぜひ合流ください。

### 宇多津町のブロードリスニング事例ページ
- [PR #58](https://github.com/digitaldemocracy2030/website/pull/58) では、宇多津町のブロードリスニング事例を紹介するページ追加が提案されています。  
- Publicセクターの実例として非常に参考になるため、内容レビューやフィードバック歓迎です。

### ボードメンバー追加やアクティビティページの改善
- [Issue #43](https://github.com/digitaldemocracy2030/website/issues/43) では、aboutページにボードメンバー情報を追加する作業が残っています。  
- [Issue #33](https://github.com/digitaldemocracy2030/website/issues/33), [Issue #32](https://github.com/digitaldemocracy2030/website/issues/32), [Issue #31](https://github.com/digitaldemocracy2030/website/issues/31) など、アクティビティページの「プロジェクトの歴史」表示やナビゲーションの強化、OSSツールのクレジット表記なども引き続き議論中です。

---

## 参加の呼びかけ

今回のアップデートでは多数の改善が行われ、Docsページの拡充やセキュリティ対応など、より参加しやすい環境が整いつつあります。とはいえ、まだ議論の最中のタスクや要望も多く、開発チームは協力してくれる新しい参加者を大歓迎しています。

- 小さな文字修正のような軽微なコントリビュートでもOK  
- コードレビューや議論への参加、ドキュメントの新規執筆も大歓迎  

多様な視点を持った人々が集まることで、よりよい「デジタル民主主義WEB」になるはずです。ぜひ気になるIssueやPRにコメントしたり、Pull Requestを送ってみてください。皆さんのご意見やご協力をお待ちしています！