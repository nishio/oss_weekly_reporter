# いどばたシステム 7/1~7/8 のGitHub活動まとめ

いどばたシステム（digitaldemocracy2030/idobata）における、最新1週間（2026/07/01～2026/07/08）の開発・議論状況をご紹介します。ドキュメント改善や機能追加など、活発に進んでおりますので、興味のある方はぜひOSS開発に参加してみてください。

---

## 今週完了したIssue・新機能

### [Issue #500](https://github.com/digitaldemocracy2030/idobata/issues/500)  
「idobata（DD2030）セットアップ〜試用レポート / ドキュメント不足点まとめ」  
作成者: YusukeHayashiii  
- ローカルDocker起動手順を試す過程で、AIチャットのモデルが提供終了していたり、GitHub鍵がないとビルドが通らないなどの問題点を詳細に報告いただきました。  
- このIssueをきっかけにドキュメント修正やAIモデルのenv化が行われ、初学者がつまずきにくくなる改善が進みました。

### マージされたPull Request

1. [PR #504](https://github.com/digitaldemocracy2030/idobata/pull/504) (by kuboon)  
   - (Issue #500 の(A)(F)対応)  
   - ドキュメントを最新構成に合わせて整理し、LLMモデルのハードコードを環境変数で置き換え、さらに管理画面のテーマ一覧が「非アクティブ」表示になるバグを修正しました。  
   - 初心者がセットアップしやすいように「お試し最小構成」「トラブルシューティング」を追加したのもポイントです。

2. [PR #505](https://github.com/digitaldemocracy2030/idobata/pull/505) (by kuboon)  
   - リポジトリの特定フォルダのみを「いどばた政策」画面で閲覧・編集・PR 作成できるようにする機能を実装しました。  
   - `GITHUB_TARGET_PATH` という環境変数を設定するだけで、フォルダのスコープを限定可能。リポジトリ全体にアクセスさせたくないケースで重宝しそうです。

---

## 未完了のタスク・進行中の議論

下記のIssueやPRはまだクローズ/マージされていないため、意見や実装アイデアを募集中です。

- [PR #497](https://github.com/digitaldemocracy2030/idobata/pull/497) (by 101ta28)  
  トップページ表示とGitHub App秘密鍵読み込み方式の改善案。すでにある程度の型拡張やトップページUIが調整され、詳細を詰めつつある段階です。  
  デプロイ環境を選ばない工夫がされており、幅広く使えるよう検討が続いています。

- [PR #362](https://github.com/digitaldemocracy2030/idobata/pull/362) (by masatosasano2)  
  「LICENSEファイルなど拡張子が無いファイルを一覧に表示させない」ための修正提案。開発環境での動作確認がまだ完了しておらず、レビューや導入テストの協力が求められています。

- [Issue #396](https://github.com/digitaldemocracy2030/idobata/issues/396) (by ghost)  
  「MCP連携でインターネット検索を可能にし、深い議論をサポートするには？」というアイデア。外部検索のコスト問題・ユーザー体験の向上策など、意見交換が行われています。  
  政策議論で参考情報を即座に参照できるアプローチとして、導入の是非が検討中です。

- その他、angelsatan777-cloud さんが提起している多数の「LCT-BI研究」や「地域通貨」「デジタル自治体政策」系Issue（例: [Issue #495](https://github.com/digitaldemocracy2030/idobata/issues/495), [Issue #496](https://github.com/digitaldemocracy2030/idobata/issues/496) など）も続々とオープン中です。こちらは文書整備やモデル仕様の議論が中心で、今後の反映に向けた協力が歓迎されています。

---

## 参加方法

1. まずはリポジトリをクローン:  
   ```
   git clone https://github.com/digitaldemocracy2030/idobata.git
   ```
2. `docs/development-setup.md` を参考にDockerで起動し、ブラウザからアクセスしてみましょう。  
3. 改善点や疑問点があれば、Issue や Pull Request でぜひご提案ください。

OSS開発は、コードを書くことだけが貢献ではありません。ドキュメント整備やUIアイデア、試用レポートの共有など、さまざまなかたちで参加できます。みなさんのご協力・ご意見をお待ちしています。一緒にいどばたシステムをより良いものにしていきましょう！