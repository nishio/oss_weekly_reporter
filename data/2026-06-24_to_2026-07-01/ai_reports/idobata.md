# いどばたシステム 6/24~7/1のGitHub活動まとめ

いどばたシステム(idobata)リポジトリでは、開発者のみならず一般ユーザーの方にも興味を持っていただきたいという思いから、多様な課題や機能追加に取り組んでいます。今週（2026-06-24～2026-07-01）に完了したタスクと、まだ議論が続いているタスクをまとめました。ぜひOSS開発に参加して、よりよいシステムを一緒に目指しましょう。

---

## 今週完了したタスク

### 完了したIssue

- [Issue #500](https://github.com/digitaldemocracy2030/idobata/issues/500)  
  作成者: YusukeHayashiii  
  ローカル環境でのセットアップ～試用レポートとして、ドキュメント不足やAIチャット動作不良などの課題を詳細にまとめてくださいました。これによって開発者が見落としていた箇所が明らかになり、ドキュメント整備と機能改善につながりました。

### マージされたPull Request

1. [PR #504](https://github.com/digitaldemocracy2030/idobata/pull/504) (作者: kuboon)  
   - ドキュメント一式（READMEやdevelopment-setup.md）を最新化。加えて [Issue #500](https://github.com/digitaldemocracy2030/idobata/issues/500) の指摘にあったAIモデルIDのハードコードやテーマ一覧表示バグの修正が含まれています。

2. [PR #503](https://github.com/digitaldemocracy2030/idobata/pull/503) (作者: kuboon)  
   - 未使用の暗号ライブラリ(cryptoパッケージ)を削除して依存を軽量化。Node.js組込みのcrypto機能を使うことで冗長なパッケージを取り除きました。

3. [PR #502](https://github.com/digitaldemocracy2030/idobata/pull/502) (作者: kuboon)  
   - いどばた政策モジュール(policy)が外部プロセス(MCPサーバ)経由でGitHub連携を行っていた部分を廃止し、backendから直接Octokitを呼び出す形に整理しました。これにより構成がシンプルになり、開発効率が上がっています。

4. [PR #501](https://github.com/digitaldemocracy2030/idobata/pull/501) (作者: kuboon)  
   - いどばたビジョン(vision)といどばた政策(policy)という2つのサブプロジェクトをリポジトリ直下にフォルダ分割し、分かりやすく整理。DockerやMakefile設定も合わせて更新され、開発者にとって見通しが良くなりました。

---

## まだ議論中・作業中のタスク

以下のPull Requestはいずれも未完了、またはクローズされずに議論が続いているものです。コメントの追加やレビューを歓迎しています。

1. [PR #497](https://github.com/digitaldemocracy2030/idobata/pull/497) (作者: 101ta28)  
   - トップページの振る舞いやGitHub App秘密鍵の扱いを改善する提案。VercelやRailwayなど具体的なホスティングサービスには依存しない範囲での修正を目指しており、まだ調整中とのことです。

2. [PR #448](https://github.com/digitaldemocracy2030/idobata/pull/448) (作者: noritaka1166)  
   - こちらも“cryptoパッケージの削除”が趣旨ですが、ディレクトリ大幅整理(#501)との競合でマージが止まっています。既に類似の修正が別PR(#503)でマージされているため、今後どう扱うかを検討中です。

3. [PR #429](https://github.com/digitaldemocracy2030/idobata/pull/429) (作者: kuboon+Devin)  
   - AI連携を強化するため、MCPサーバをバイパスして直接GitHub APIを呼ぶアイデアを早期に試みたPRです。途中でリポジトリ構成変更が発生し、現在はクローズせず保留状態ですが、議論を継続すれば新方針(#502)との統合も検討できそうです。

---

## さいごに

今週も多くのコントリビューターが活発に活動し、ドキュメント整備や不具合修正、リファクタリングが進みました。未完のPRには引き続き議論の余地があり、みなさんの知見が必要です。

いどばたシステムの改善に興味がある方、ぜひIssueやPull Requestにコメントしたり、ドキュメント修正などのコントリビュートをお待ちしています！OSS開発を通じて、より使いやすい民主的対話プラットフォームを一緒に実現していきましょう。