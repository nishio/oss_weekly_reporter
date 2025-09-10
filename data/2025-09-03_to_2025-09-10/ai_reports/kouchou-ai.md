# 広聴AI 9/3~9/10 のGitHub活動まとめ

今週も「広聴AI」リポジトリでさまざまなIssue・Pull Request（PR）が作成・更新・マージされました。新しい機能や修正に関する情報を共有し、今後の議論や実装への参加を歓迎します！

---

## 今週完了したIssue

- [Issue #702](https://github.com/digitaldemocracy2030/kouchou-ai/issues/702) (作成: shingo-ohki)  
  client-adminでlintエラーが出ていた問題が解消されました。  
  これは一見ユーザーにはわかりづらい修正ですが、開発環境でエラーを無くすことで開発効率が向上し、今後の機能拡張や不具合修正のスピードアップに繋がります。

## 今週マージされたPR

- [PR #703](https://github.com/digitaldemocracy2030/kouchou-ai/pull/703) (作成: shingo-ohki)  
  上記の[Issue #702](https://github.com/digitaldemocracy2030/kouchou-ai/issues/702)を修正したPRです。lintエラーを解消し、テストが通るように調整されています。見た目や機能に大きな変化はありませんが、内部的な保守性が高まりました。

---

## 未完了のIssueでの議論

- [Issue #701](https://github.com/digitaldemocracy2030/kouchou-ai/issues/701) (作成: shingo-ohki)  
  client側でもlintエラーが出ているため、同様のリファクタ対応が必要とされています。具体的なエラーログや解決方法がIssue本文に記載されており、誰でも修正に参加できます。

- [Issue #700](https://github.com/digitaldemocracy2030/kouchou-ai/issues/700) (作成: nishio)  
  将来的に必要な変更点のリストです。Biome Linterの設定やパッケージ管理、環境変数設定などがまとめられており、「今後どうプロジェクトを整備していくか」についての議論を歓迎しています。

- [Issue #111](https://github.com/digitaldemocracy2030/kouchou-ai/issues/111) (作成: nishio)  
  「用語解説ページ」の追加要望です。実際の操作画面で「プロンプト」や「埋め込み」「クラスタ」が何を指すのかなど、わかりやすいドキュメント不足を補うための改善策が検討されています。

---

## 未完了のPRでの議論

- [PR #704](https://github.com/digitaldemocracy2030/kouchou-ai/pull/704) (作成: NISHIO+Devin)  
  [PR #703](https://github.com/digitaldemocracy2030/kouchou-ai/pull/703)のマージ後に残ったlintエラーやテスト失敗をまとめて解消するためのPRです。ScatterChartのonClickハンドラなど、一部TypeScriptの型修正も含まれています。レビュアーのチェック待ちであり、追加の検証やフィードバックを歓迎しています。

- [PR #699](https://github.com/digitaldemocracy2030/kouchou-ai/pull/699) (作成: shgtkshruch)  
  「用語解説ページ」と「グローバルナビゲーション」をclient（フロントエンド）に追加する試みです。画面のヘッダーにメニューを配置し、FAQ形式の用語説明ページを実装しています。皆さんからの「用語の追加提案」や「UIの改善アイデア」を募集中です。

- [PR #698](https://github.com/digitaldemocracy2030/kouchou-ai/pull/698) (作成: AkioPonkotu)  
  新たにGoogle Geminiを利用してレポートを生成できるようにするPRです。APIキーの設定方法やトークン使用量・推定料金がわかる機能が盛り込まれています。開発者向けドキュメントの充実や、他のAIプロバイダーとの連携方法なども話題に上がっており、より多様なAI連携を目指すうえで重要な変更点となりそうです。  
  このPRは[Issue #634](https://github.com/digitaldemocracy2030/kouchou-ai/issues/634)も参照しつつ実装が進行中。レビューや動作確認レポートが歓迎されています。

---

## 参加のお願い

- コミュニティによる議論とフィードバックでOSSがより良いものになります。 
- 「広聴AI」に興味を持った方は、IssueやPRを気軽に読んでみてください。  
- 小さな修正や提案でも大歓迎です。あなたの貢献がプロジェクトを前進させます！

今週も多様なメンバーがlint修正から機能追加、ドキュメント充実まで幅広く盛り上げてくれました。引き続き、皆さんの参加をお待ちしております。