# 広聴AI 2026/06/03 ~ 2026/06/10 のGitHub活動まとめ

今週（2026/06/03〜2026/06/10）の広聴AIリポジトリ(digitaldemocracy2030/kouchou-ai)での活動状況をご報告します。  
新機能やバグ修正に関するIssueやPRがクローズ・マージされました。また、未解決のIssueで議論が盛り上がっています。

---

## 今週完了したIssue

- [Issue #894](https://github.com/digitaldemocracy2030/kouchou-ai/issues/894)  
  - 作成者: shingo-ohki  
  - 内容: レポート生成がうまく動作しないバグの報告。クラスタリング用の依存関係をインストールしていない場合に発生するエラーが確認されました。修正によって、エラーなくレポートが生成できるようになっています。

エンドユーザ視点では、「レポート生成時に発生していたエラーが解消された」という形で新機能というよりはバグ修正ですが、開発者の皆さんが頑張って最小限の修正で対応してくれています。ぜひ試してみてください！

---

## 今週マージされたPull Request

1. [PR #899](https://github.com/digitaldemocracy2030/kouchou-ai/pull/899) (作成者: nishio)  
   - [Issue #898](https://github.com/digitaldemocracy2030/kouchou-ai/issues/898) への対策として、aarch64環境のDockerでNumbaのCPU targetをgenericに固定。  
   - aarch64マシンが手元にある方は、ぜひビルドして動作を確認してみてください。

2. [PR #897](https://github.com/digitaldemocracy2030/kouchou-ai/pull/897) (作成者: 101ta28)  
   - CSVファイルの属性を数値か文字列か混在する場合でも文字列として扱うように修正。  
   - ユーザがアップロードするデータに数値・文字列が混在していてもエラーなく処理が進むようになりました。

3. [PR #896](https://github.com/digitaldemocracy2030/kouchou-ai/pull/896) (作成者: nishio)  
   - API Dockerfileでanalysis-coreの依存関係を正しくインストールしているか検証するテストを追加し、依存不足の再発を防止。  
   - テスト面の充実によって、今後のアップデートで同種の不具合が混入しにくくなっています。

4. [PR #895](https://github.com/digitaldemocracy2030/kouchou-ai/pull/895) (作成者: Devin AI+Devin)  
   - API Dockerfileでanalysis-coreのclustering依存をインストールするよう修正。  
   - [Issue #894](https://github.com/digitaldemocracy2030/kouchou-ai/issues/894)への対策として行われた変更で、Docker環境でのクラスタリング処理が問題なく動作するように。

これらのPRは、クラスタリング周りの依存関係を整えたり、混在型CSVへの対応強化を行ったりと、開発者だけでなくエンドユーザにとっても重要な改修ばかりです。開発者の皆さんがつまづきそうなポイントが大幅に減り、かつユーザが持ち込むさまざまな形式のCSVに柔軟に対応できるようになりました。

---

## 未完了のIssue・議論中の内容

- [Issue #898](https://github.com/digitaldemocracy2030/kouchou-ai/issues/898)  
  - 作成者: shingo-ohki  
  - aarch64環境(Apple Silicon等)でクラスタリングを行おうとすると実行時エラーが出る問題。  
  - ただし、[PR #899](https://github.com/digitaldemocracy2030/kouchou-ai/pull/899) 等でNumbaの設定を変更する対策が追加されています。実際に問題が解消したか、さらに設定が必要かなどの追加報告をお待ちしています。

このIssueでは、Dockerコンテナ上でのaarch64対応例などが議論されています。Apple Siliconの方や他のaarch64マシンをお持ちの方は、検証に参加して「セットアップ手順の改善」「クラスタリング性能の確認」など、ぜひフィードバックをお願いします！

---

## 今後の参加の呼びかけ

- 依存関係や環境固有の問題はOSS開発ではよくあるトピックです。今回のaarch64対応のように、多様な環境を持つ方の貢献が非常に助けになります。  
- CSVファイルの形式や属性値の混在など、実務ではさまざまなデータが登場します。まだテストが十分でないケースやユースケースがあれば、Issueを立てたりPRを送っていただけると嬉しいです。  

新しい機能追加やバグ修正を続けるにあたり、皆さんの協力が欠かせません。ぜひIssueでのディスカッションやPRレビューなど、Open Sourceならではのコラボレーションを一緒に進めましょう。お気軽にご参加ください！