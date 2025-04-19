# 広聴AI 第5週（4/9 ~ 4/16）のGitHub活動まとめ

こんにちは！「デジタル民主主義2030」プロジェクト、広聴AIコミュニティマネージャです。2025-04-09から2025-04-16までの1週間で行われた開発状況をまとめました。OSS開発に参加してみたい方は、ぜひ今回のアップデートや議論の内容を参考にしていただければ幸いです。

---
## 今週「完了」した主なIssueと対応PR

先週から今週にかけては、合計10件のIssueが完了（クローズ）され、新機能の追加や不具合修正が行われました。以下が主なものです。機能名が難しく感じても、担当者の貢献内容を知ることで開発の進捗がよりイメージしやすくなると思います。

1. [Issue #298](https://github.com/digitaldemocracy2030/kouchou-ai/issues/298)  
   - 「docker-compose → docker compose」への修正を行い、コマンド認識エラー問題を解消しました。  
   - [PR #299](https://github.com/digitaldemocracy2030/kouchou-ai/pull/299) にて nishio さんが対応。

2. [Issue #278](https://github.com/digitaldemocracy2030/kouchou-ai/issues/278)  
   - 全画面表示した際に要約文が「全画面終了」ボタンの裏に隠れる不具合を修正。  
   - [PR #282](https://github.com/digitaldemocracy2030/kouchou-ai/pull/282) を masatosasano2 さんが作成し解決。

3. [Issue #277](https://github.com/digitaldemocracy2030/kouchou-ai/issues/277)  
   - CSVアップロード時にエラーで途中停止しても進捗状況が正しく更新されるように改善。  
   - [PR #279](https://github.com/digitaldemocracy2030/kouchou-ai/pull/279) にて 101ta28 さんが対応。

4. [Issue #268](https://github.com/digitaldemocracy2030/kouchou-ai/issues/268)  
   - Admin画面のレポート一覧にも作成日時を表示できるようにしました。  
   - [PR #272](https://github.com/digitaldemocracy2030/kouchou-ai/pull/272) は「<人間>+Devin」名義（devin-ai-integration[bot] がサポート）で対応。

5. [Issue #243](https://github.com/digitaldemocracy2030/kouchou-ai/issues/243)  
   - 初期設定時（Windows環境など）に生じる entrypoint.sh の改行コードエラーを解消。  
   - [PR #314](https://github.com/digitaldemocracy2030/kouchou-ai/pull/314) を take365 さんが提出し、解決。

6. [Issue #241](https://github.com/digitaldemocracy2030/kouchou-ai/issues/241)  
   - コメント件数から推奨のクラスタ数を自動算出する「おすすめクラスタ数設定」機能を追加。  
   - [PR #244](https://github.com/digitaldemocracy2030/kouchou-ai/pull/244) にて「<人間>+Devin」名義で実装。

7. [Issue #222](https://github.com/digitaldemocracy2030/kouchou-ai/issues/222)  
   - 「クラスタ数の直接変更が面倒」という声に応え、数値入力フォームの準備が進みました。  
   - （関連PRは複数議論中ですが、一部修正が完了しクローズ済み。今後もUI改善が検討されています）

8. [Issue #218](https://github.com/digitaldemocracy2030/kouchou-ai/issues/218)  
   - レポート一覧に作成日時を追加し、いつ生成したものか判別しやすく。  
   - [PR #245](https://github.com/digitaldemocracy2030/kouchou-ai/pull/245) を「<人間>+Devin」名義で対応。

9. [Issue #84](https://github.com/digitaldemocracy2030/kouchou-ai/issues/84)  
   - フロントエンド部分のフォーマッタ（Biome）を導入し、コードの書式揺れを自動化。  
   - [PR #270](https://github.com/digitaldemocracy2030/kouchou-ai/pull/270) を shgtkshruch さんが作成し、Lintチェック導入を完了。

10. [Issue #54](https://github.com/digitaldemocracy2030/kouchou-ai/issues/54)  
   - GoogleAnalytics を導入し、広聴AIがどれくらい参照されているかを可視化。  
   - [PR #251](https://github.com/digitaldemocracy2030/kouchou-ai/pull/251) で「<人間>+Devin」名義にて対応。

いずれも多彩な方々が関わっていることが分かるかと思います。「<人間>+Devin」と記載した箇所は、人間の開発者がAIアシスタントを活用しながら実装したPRで、背後には実際のメンバーが存在しています。さまざまな貢献者がいるところもOSSの魅力ですね。

---
## まだ議論中・対応中の主なIssueやPR

今週は新たに多くのIssueやPRが作成されてもいますが、その中で議論が活発なものや、特に参加が期待されるものをピックアップします。多様な視点の議論はOSS開発にとって大切ですので、気軽にご意見をお寄せください。

### 1) Windows環境への対応強化
- [Issue #300](https://github.com/digitaldemocracy2030/kouchou-ai/issues/300)  
  「Windowsユーザが簡単にセットアップできるように」という要望から、Docker環境構築を手助けするバッチファイルなどが整備されています。PRも多数マージされていますが、他にも [PR #313](https://github.com/digitaldemocracy2030/kouchou-ai/pull/313) 等でさらなる改善が検討中です。

### 2) 静的ファイルエクスポート機能の強化
- [PR #309](https://github.com/digitaldemocracy2030/kouchou-ai/pull/309)  
  「<人間>+Devin」名義で投稿され、Admin画面からレポートを一括エクスポート（ZIPダウンロード）できる機能を追加する提案。.  
- [Issue #274](https://github.com/digitaldemocracy2030/kouchou-ai/issues/274)  
  GitHub Pages などで公開する際に、画像やリンクがうまく表示されない問題があり、相対パス指定などの改善が議論されています。

### 3) UI/UX 改善・バックログ
- [Issue #306](https://github.com/digitaldemocracy2030/kouchou-ai/issues/306)  
  「全体図」「濃い意見グループ」画面でのズーム操作を分かりやすくしてほしい――など、UI改善案が出ています。  
- [Issue #290](https://github.com/digitaldemocracy2030/kouchou-ai/issues/290)  
  階層図でノードが重なりやすい場合に「戻るボタン」やパンくずリストを付けるなど、使いやすさ向上が活発に議論中です。  

### 4) デプロイや配布形態に関する議論
- [Issue #308](https://github.com/digitaldemocracy2030/kouchou-ai/issues/308)  
  HTMLフォーム入力でAzureリソースを自動構築するような、より簡易なデプロイを検討する提案。  
- [Issue #289](https://github.com/digitaldemocracy2030/kouchou-ai/issues/289)  
  あらかじめビルドした「.exe形式」での配布はできないか？という要望。自治体のセキュリティポリシーやPython/Docker未導入環境を意識して議論が行われています。

上記のほかにも多くのすぐ対応できそうなタスクや、実験が必要なアイデアがIssueとして立ち上がっています。詳しくはリポジトリのIssue一覧をご覧ください。

---
## 今後の参加の呼びかけ

- 開発に参加したい方は、まだ着手されていないIssueや新機能提案スレッドへのコメント、ドキュメント整備など、ぜひお気軽にチャレンジしてみてください。
- バグ報告やUI改善提案など、「自分でコード書くのはちょっと...」という方の意見も大歓迎です。
- 多様な後見者（レビューア、ドキュメント執筆者、テスターなど）を歓迎しています。ぜひいろいろな観点のご意見やご協力をお願いします。

それでは来週も、広聴AIを通じて、デジタル民主主義を前進させるOSS開発を進めていきましょう！ありがとうございました。