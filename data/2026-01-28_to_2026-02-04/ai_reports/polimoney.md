# Polimoney 1/28 ~ 2/4 のGitHub活動まとめ

今週もPolimoneyプロジェクトへのご参加・ご注目、ありがとうございます。こちらでは、2026年1月28日から2月4日までの間に行われたGitHub上での活動をまとめます。新機能や議論のポイントを紹介しますので、OSS開発に興味をお持ちの方はぜひご覧ください！

---

## 完了した作業

### [Issue #197](https://github.com/digitaldemocracy2030/polimoney/issues/197) サンキー図・一覧表のデータを統一

- **担当・貢献者:** grassfieldk  
- **概要:**  
  - 各議員ページで使用する資金関連データ（Flow, Transaction）の不整合を解消するための検討・調整が完了しました。  
  - これにより、サンキー図などの可視化と収支一覧表の内容に一貫性が保たれるようになります。  
  - Flow（サンキー図用）を動的に生成する方針が固まり、今後データ構造がより簡潔になる見込みです。

- **関連するIssueやタスク:**  
  - [Issue #199](https://github.com/digitaldemocracy2030/polimoney/issues/199) (blocked by)  
  - [Issue #166](https://github.com/digitaldemocracy2030/polimoney/issues/166) (blocks)  
  - [Issue #32](https://github.com/digitaldemocracy2030/polimoney/issues/32) (relates to)

**ユーザ向けポイント:**  
これまでサンキー図の数字と一覧表の数字が微妙にズレることがありましたが、今回の対応でより正確なデータが見られるようになります！

---

## 未完了のタスク・議論中の内容

### [Issue #218](https://github.com/digitaldemocracy2030/polimoney/issues/218) ディレクトリ構成の整理

- **担当・貢献者:** grassfieldk  
- **概要:**  
  - Next.jsのコードがルートディレクトリに散らばっている現状を改善し、srcやfrontendディレクトリなどに整理する案が話し合われています。  
  - プロジェクト構成を整理することでコードの見通しがよくなり、開発効率アップが期待されます。

- **議論のポイント:**  
  - ディレクトリ階層をどう設計するか  
  - Vercelなどのデプロイ環境での設定をどうするか

**ユーザ・開発者への呼びかけ:**  
フォルダ構成に関する知見や「こんなふうに分けたら便利では？」というアイデアがあれば、ぜひ [Issue #218](https://github.com/digitaldemocracy2030/polimoney/issues/218) にコメントしてください！

---

### [PR #247](https://github.com/digitaldemocracy2030/polimoney/pull/247) フロントエンドのコード整理

- **作成者:** grassfieldk  
- **概要:**  
  - フロントエンド側のコードを新たに作ったfrontendディレクトリに集約し、Next.jsの脆弱性へ対応するPRです。  
  - 動的エクスポートの採用やリファクタリングを含む大規模な変更（ファイル数95件）となっており、同時にデプロイ先をVercelへ移行するための準備も進められています。  
- **関連Issue:**  
  - Close予定: [Issue #218](https://github.com/digitaldemocracy2030/polimoney/issues/218), [Issue #219](https://github.com/digitaldemocracy2030/polimoney/issues/219)

**ユーザ向けポイント:**  
大きなリファクタリングが進むことで、今後のUI改善や新機能追加がスムーズになります。フロントエンド開発が得意な方は、このPRでどんな変更が行われているかを確認してみてください！

---

## 参加の呼びかけ

- バグ報告や提案、ドキュメント修正など、あらゆるコントリビュートが大歓迎です。  
- データ周りにご興味がある方は [Issue #197](https://github.com/digitaldemocracy2030/polimoney/issues/197) の内容やフロー生成周りの議論を参考に、ぜひ改善アイデアや質問をお寄せください。  
- ディレクトリ構成やアプリの設計に自信のある方は [Issue #218](https://github.com/digitaldemocracy2030/polimoney/issues/218) と [PR #247](https://github.com/digitaldemocracy2030/polimoney/pull/247) を要チェックです！

Polimoneyはみなさんの力でより良いプロダクトを目指しています。少しでも興味を持たれましたら、ぜひGitHub上でのやり取りに参加してみてください。疑問点や提案したいアイデアなど、自由にコメントしていただけると嬉しいです。皆さんのご参加をお待ちしています！