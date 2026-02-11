# 広聴AI 2/4~2/11 のGitHub活動まとめ

今週は多数の機能追加やドキュメント整備に関するPull Request (PR) がマージされ、同時にいくつかのIssueが完了しました。開発者でない方々にもわかるように、まずはどのような新機能や改善が行われたのかをご紹介し、その後、まだ未完了のタスクで進行中の議論についてまとめます。興味を持たれた方はぜひリポジトリのIssueやPRを覗いてみてください！

---

## 今週完了した主なIssue

- [Issue #783](https://github.com/digitaldemocracy2030/kouchou-ai/issues/783)  
  「public-viewer が起動時ビルドで失敗しヘルスチェックがタイムアウトする」問題が解消されました。  
  → [PR #784](https://github.com/digitaldemocracy2030/kouchou-ai/pull/784) や [PR #782](https://github.com/digitaldemocracy2030/kouchou-ai/pull/782) などを通じて、モノレポのルート設定 (turbopack.root) やDockerビルド周りの修正が行われ、起動遅延に対応できるようになりました。  
  実装は nishio+Devin が担当しています。

- [Issue #775](https://github.com/digitaldemocracy2030/kouchou-ai/issues/775)  
  「レポート生成ページから一覧ページに戻る手段がなさそう」という要望に応えて追加機能が実装されました。  
  → [PR #776](https://github.com/digitaldemocracy2030/kouchou-ai/pull/776) により、ページ上部のロゴやキャンセルボタンから一覧に戻れるUIが入りました。  
  実装は nishio+Devin が担当しています。

- [Issue #766](https://github.com/digitaldemocracy2030/kouchou-ai/issues/766)  
  「未解決パスが最終キー欠落時に None になる問題」について、設定読み込み時にキー不足を即座にエラー表示にするよう修正されました。  
  → [PR #767](https://github.com/digitaldemocracy2030/kouchou-ai/pull/767) で対応。  
  実装は nishio+Devin が担当しています。

---

## 今週マージされた主なPRと新機能

今週は計19件のPRがマージされ、多数の新機能・改善が行われました。特に注目のトピックをいくつかピックアップします。

### 1. ドキュメントの整理・拡充
- [PR #793](https://github.com/digitaldemocracy2030/kouchou-ai/pull/793), [PR #792](https://github.com/digitaldemocracy2030/kouchou-ai/pull/792), [PR #791](https://github.com/digitaldemocracy2030/kouchou-ai/pull/791) など  
  → AI連携やOSS参加手順をより分かりやすくするため、Markdownドキュメントを大幅に整理・拡充。URLの修正や複数リポジトリREADMEの埋め込み対応、mkdocs構成の改善など、多くの文書面でパッチが入りました。  
  担当は nishio+Devin。

### 2. レポートの「再利用」機能
- [PR #769](https://github.com/digitaldemocracy2030/kouchou-ai/pull/769)  
  既存のレポートを複製して、新しい設定やプロンプトで再実行できるようになりました。今後、似た構成のレポートを何度も作る際にとても便利になります。  
  担当は nishio+Devin。

### 3. APIキー未設定の早期検知 (CLI向け)
- [PR #768](https://github.com/digitaldemocracy2030/kouchou-ai/pull/768)  
  CLI実行時にAPIキーが設定されていない場合、始める前に明示的にエラーを出して止める機能が追加。無駄に時間をかけずに設定漏れに気づけます。  
  担当は nishio+Devin。

### 4. Polarsへの移行・Pandas除去
- [PR #781](https://github.com/digitaldemocracy2030/kouchou-ai/pull/781), [PR #789](https://github.com/digitaldemocracy2030/kouchou-ai/pull/789)  
  データフレーム処理をPolarsに統一。Pandas依存があった箇所を整理してビルドを軽量化し、実行パフォーマンスを高めています。  
  担当は nishio+Devin。

### 5. public-viewer周辺の起動・ヘルスチェック改善
- [PR #785](https://github.com/digitaldemocracy2030/kouchou-ai/pull/785)  
  Azure のdeploy時にpublic-viewerがタイムアウトしにくくするリトライとログ出力の改善が入り、CIが落ちづらくなりました。  
  こちらも nishio+Devin が対応。

---

## 未完了のタスクと議論

### 1. [Issue #741](https://github.com/digitaldemocracy2030/kouchou-ai/issues/741) 「main ブランチへのマージ時に実行されるAzureへのdeployがたまに失敗する」
現在も続いているデプロイ失敗のバグです。ネットワーク回りでnpmレジストリへの接続が途切れることが原因とみられ、以下のような議論が進んでいます。  
- リトライのお手軽対処 vs. npmの設定をカスタムして再試行回数を増やす  
- Dockerビルド段階の並列数を落として安定性を高めるかどうか  
- npmキャッシュを活用してネットワーク負荷を軽減するか  
引き続き意見を募集しています。

### 2. [PR #786](https://github.com/digitaldemocracy2030/kouchou-ai/pull/786) 「docs: Azure Container Apps 移行メモを実装に合わせて更新」
移行ドキュメントをより実用的にするために書かれたPRですが、まだマージされていません。Azure Container Apps 環境でリネームや秘密情報をどう扱うかなど、インフラ担当同士で追加の情報交換が進んでおり、反映後にマージされる見込みです。  
資料の充実に興味がある方は、ぜひこのPRのディスカッションに参加してみてください。

---

## おわりに

今週はドキュメント面・機能面とも大きな前進があり、開発体制がより整ってきました。一方で、まだ議論中のIssueやPRもあり、新しい参加者のアイデアや視点を歓迎しています。もし興味のあるIssueやPRがあれば、ぜひコメントやレビューで参加してみてください。OSS開発の現場は、実際に試したり意見を交わしたりする中でどんどん学びが得られる場所です。

引き続き、広聴AI (kouchou-ai) の開発にご注目ください！また次回のアップデートでお会いしましょう。