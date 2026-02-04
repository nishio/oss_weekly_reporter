# 広聴AI 1/28~2/4 のGitHub活動まとめ

この一週間（2026-01-28 ～ 2026-02-04）での広聴AIリポジトリの活動内容です。  
新機能が追加されたPRやドキュメントの更新が行われましたので、興味がある方はぜひリポジトリをチェックしてみてください。

---

## 今週完了した内容

### マージされた Pull Request

1. [PR #777](https://github.com/digitaldemocracy2030/kouchou-ai/pull/777)  
   - 作成者: shingo-ohki  
   - ドキュメントに技術解説資料へのリンクが新たに追加されました。  
   - これにより、開発者でない方でも「この技術ってどういう背景なの？」という疑問に答えやすくなっています。

2. [PR #774](https://github.com/digitaldemocracy2030/kouchou-ai/pull/774)  
   - 作成者: shingo-ohki  
   - 既存のデータ分析ライブラリを「pandas」から「polars」に変更した余波を、requirements.lock ファイルにも反映しました。  
   - データハンドリングの高速化・効率化が期待できます。

3. [PR #773](https://github.com/digitaldemocracy2030/kouchou-ai/pull/773)  
   - 作成者: dependabot[bot]  
   - Next.jsをバージョン15.5.9から16.1.5にアップデートしたPRです。  
   - 新しいバージョンでの破壊的変更に対応しつつ、セキュリティの向上も図っています。

4. [PR #772](https://github.com/digitaldemocracy2030/kouchou-ai/pull/772)  
   - 作成者: dependabot[bot]  
   - 上と同様、Next.jsのアップデートですが、こちらは /utils/dummy-server ディレクトリ向けのアップデートです。  
   - 主に開発時のダミーサーバに影響する変更となります。

5. [PR #770](https://github.com/digitaldemocracy2030/kouchou-ai/pull/770)  
   - 作成者: nishio  
   - ドキュメントを刷新し、pnpm選定理由やプラグイン仕様などを整理しました。  
   - 特にプラグインの出力データ構造を詳細にまとめたため、プラグインを開発してみたい方にとって参考になります。

---

## 今週未完了のタスクと議論

### Issue の状況

- [Issue #775](https://github.com/digitaldemocracy2030/kouchou-ai/issues/775)  
  - タイトル: レポート生成ページから一覧ページに戻る手段がなさそう  
  - 作成者: nishio  
  - 「レポート生成ページ → 一覧ページ」の導線がなく不便という問題提起です。下記の [PR #776](https://github.com/digitaldemocracy2030/kouchou-ai/pull/776) で解決を試みています。

- [Issue #741](https://github.com/digitaldemocracy2030/kouchou-ai/issues/741)  
  - タイトル: mainブランチへのマージ時に実行されるAzureへのdeployが失敗する  
  - 作成者: shingo-ohki  
  - AzureへのDeploy時、Dockerビルド中のnpmレジストリ接続エラーが断続的に発生するという報告です。  
  - ネットワークとの兼ね合いが原因とみられ、npmの再試行やビルドの並列度調整などさまざまな対策が検討されています。

### Pull Request (未マージ)

1. [PR #776](https://github.com/digitaldemocracy2030/kouchou-ai/pull/776)  
   - 作成者: nishio  
   - 上記 [Issue #775](https://github.com/digitaldemocracy2030/kouchou-ai/issues/775) の改善策を実装。  
   - ヘッダーロゴクリックで一覧ページに戻るリンク付与、加えてキャンセルボタンも新設。ユーザーのUX向上に期待がかかります。

2. [PR #769](https://github.com/digitaldemocracy2030/kouchou-ai/pull/769)  
   - 作成者: nishio  
   - 「レポートの再利用機能」を開発する大規模なPRです。  
   - 既存のレポートを複製して新しいレポートとして起動できるほか、アーティファクトの再利用やAPI周りの設計など幅広い検討が行われています。  
   - まだ議論中の部分も多いので、興味のある方はぜひコメントをお寄せください。

---

## 参加の呼びかけ

新機能の開発やバグ修正に携わっているコントリビューターの方々のおかげで、広聴AIは日々進化を続けています。  
ドキュメントへの追加やUI向上など、初心者の方でも入りやすい課題もあります。ぜひIssuesやPull Requestsでのディスカッションに加わってみてください！  

- 新しくIssueを報告したい場合 → [Issue新規作成](https://github.com/digitaldemocracy2030/kouchou-ai/issues/new)  
- 開発ドキュメント → リポジトリ内 "docs" ディレクトリおよび最新の [技術解説資料](https://github.com/digitaldemocracy2030/kouchou-ai) を参照  

皆様のコントリビューションをお待ちしています！  