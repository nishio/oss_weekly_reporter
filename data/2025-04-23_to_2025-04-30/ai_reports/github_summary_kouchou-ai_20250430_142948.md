# 広聴AI 4/23~4/30 のGitHub活動まとめ

今週(2025-04-23～2025-04-30)の「広聴AI(kouchou-ai)」リポジトリでは、多数のIssueとPull Requestがやり取りされ、多くの新機能やドキュメント改善が完了しました。ここでは「完了したタスク」と「未完了・議論中のタスク」に分けてご紹介します。開発者だけでなく、OSSに興味のある方や実際に使ってみたい方に向けて、なるべくわかりやすくまとめました。

---

## 完了した主なタスク

### 1. 新機能の追加・修正 (マージされたPR)

- [PR #404](https://github.com/digitaldemocracy2030/kouchou-ai/pull/404) 散布図へのズーム・パン機能追加  
  作者: tokoroten  
  → 意見の散布図を自由に拡大・移動でき、さらにスクリーンショットボタンも利用可能になりました。

- [PR #392](https://github.com/digitaldemocracy2030/kouchou-ai/pull/392) 文脈埋め込み（エンベデッド）をローカルLLMで動かす機能を導入  
  作者: tokoroten  
  → OpenAIのAPIを使わなくても、SentenceTransformerを用いてローカル環境で「意見の埋め込み(embedding)」を計算できるように。自治体などでAPI契約が難しいケースに役立ちます。

- [PR #390](https://github.com/digitaldemocracy2030/kouchou-ai/pull/390) 基本的なE2Eテスト環境構築  
  作者: NISHIO Hirokazu+Devin  
  → Playwrightを利用した自動テスト環境が導入され、エンドツーエンドテストを実行できるようになりました。開発時の動作確認がスムーズに。

- [PR #389](https://github.com/digitaldemocracy2030/kouchou-ai/pull/389) 「クラスタ」を「意見グループ」に用語統一  
  作者: nsk.smn+Devin  
  → UI上の文言をわかりやすくするため、「クラスタ」は「意見グループ」と呼ぶ表記に変更しました。これにより利用者にとって理解しやすいインターフェースに。

- [PR #387](https://github.com/digitaldemocracy2030/kouchou-ai/pull/387) Windows環境セットアップガイドの改善  
  作者: NISHIO Hirokazu+Devin  
  → WindowsでのDockerインストールやAPIキー設定に関するドキュメントが充実。これから試す方でも手順を踏みやすくなりました。

- [PR #384](https://github.com/digitaldemocracy2030/kouchou-ai/pull/384) プロンプト編集バグの修正＆リファクタリング再適用  
  作者: mtane0412  
  → 一度revertされたリファクタを再適用しつつ、レポート作成時に編集したプロンプトが反映されないバグを解消。これでカスタムプロンプトが正しく使えます。

- [PR #382](https://github.com/digitaldemocracy2030/kouchou-ai/pull/382) LLM出力をStructured OutputによりJSONフォーマット強制  
  作者: tokoroten  
  → OpenAIのStructured Output機能を使い、LLMによる出力フォーマットのばらつきを減らす取り組み。解析処理がより安定します。

- [PR #360](https://github.com/digitaldemocracy2030/kouchou-ai/pull/360) admin画面にて「staticなHTMLファイル」をダウンロード可能に  
  作者: shgtkshruch  
  → 「広聴AI」で生成したレポートを静的ファイルとしてまとめてExportし、Zipでダウンロードできる芸が実装。Webサーバを別途用意して公開する流れがスムーズに。

- [PR #359](https://github.com/digitaldemocracy2030/kouchou-ai/pull/359) 階層図UIの改善  
  作者: masatosasano2  
  → 階層図を深掘り表示してから戻るときの操作やパンくずリストの見せ方などを調整し、使い勝手が向上。

- [PR #353](https://github.com/digitaldemocracy2030/kouchou-ai/pull/353) langchain依存の削除  
  作者: nishio  
  → 不要ライブラリの依存を外し、openai公式SDKに一本化。コード量を削減しメンテナンス性が向上。

この他にも、ドキュメント拡充やE2Eテスト関連の追加修正など、多数のPRがマージされています。詳しくはリポジトリの[Pull Request一覧](https://github.com/digitaldemocracy2030/kouchou-ai/pulls?q=is%3Apr+is%3Aclosed)を参照ください。

### 2. 修正・完了した主なIssue

- [Issue #401](https://github.com/digitaldemocracy2030/kouchou-ai/issues/401), [Issue #388](https://github.com/digitaldemocracy2030/kouchou-ai/issues/388)  
  用語の「クラスタ」→「グループ」への言い換え。UI・ドキュメント両面で混在していた箇所を修正。  
- [Issue #375](https://github.com/digitaldemocracy2030/kouchou-ai/issues/375)  
  レポート作成時にプロンプト編集が反映されないバグの修正完了。  
- [Issue #371](https://github.com/digitaldemocracy2030/kouchou-ai/issues/371)  
  プロンプトにAI導入(バイアス的文言)が混ざる問題の修正。  

このほかにも、多数のバグ修正や機能改善Issueがクローズされました。

---

## 議論中・未完了のタスク

ここからはまだクローズされていないIssue、あるいは作成されたばかりのIssueの中で注目の議論をご紹介します。参加者を募集しているトピックもあるので、ぜひご覧ください。

- [Issue #398](https://github.com/digitaldemocracy2030/kouchou-ai/issues/398)  
  「Devin とのうまい協働方法を考える」  
  → AIアシスタントが自動コミット・自動PRを行うことで、人間のコントリビューション意欲やコードレビュー体験にどんな影響があるのか。人間とAIがどう住み分けつつ協働すれば良いか、意見が交わされています。

- [Issue #402](https://github.com/digitaldemocracy2030/kouchou-ai/issues/402)  
  「OpenRouterを使えるようにする」  
  → OpenAI以外のLLMを使えるようにする取り組み。政治関連のプロンプト利用制限を避けたい、または複数のLLMを使い分けたいという要望が続いており、導入に向けた議論が進行中。

- [Issue #400](https://github.com/digitaldemocracy2030/kouchou-ai/issues/400)  
  「環境確認機能を作る」  
  → 「APIキーが正しく設定されているか？」「認証が正しいか？」などを一括で確認できる管理画面機能を入れるかどうかの検討。自治体など非エンジニアユーザーの躓きポイントを減らす狙いがあります。

- [Issue #385](https://github.com/digitaldemocracy2030/kouchou-ai/issues/385)  
  「ローカルLLM / embedding を利用できるようにする」  
  → すでに一部機能は実装されましたが、まだ完全ではなく、モデルの選定・安定動作の評価について議論中。低スペック環境でも動くLLMの検証が課題になっています。

- [Issue #398](https://github.com/digitaldemocracy2030/kouchou-ai/issues/398) ほかにも複数…  
  → OSS開発で多様な後見者やガイドを可視化する動きもあり、コミュニティとしてさらに参加しやすい環境を作る議論が活発です。

このほかにも、より細かいバグ報告やドキュメントの追加要望など、多くのIssueがオープンされています。実装や議論に興味がある方は、ぜひ[Issueリスト](https://github.com/digitaldemocracy2030/kouchou-ai/issues)を覗いてみてください。

---

## 参加の呼びかけ

- 「コードを書かないけど興味がある」という方でも、Issueへのコメントやバグ報告、提案は大歓迎です。  
- 「こんな使い方がしたい」「この機能がわかりづらい」などの意見はプロダクトを磨くうえでとても重要なフィードバックとなります。  
- Devin(自動PR作成bot)と共に作業する際の体験談や改善案もぜひお寄せください。  

リポジトリへのスター、Issueへのコメントやリアクションが開発を前に進める大きな力になります。ぜひ皆さんのご参加をお待ちしています！  