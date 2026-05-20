# 広聴AI 5/13~5/20 のGitHub活動まとめ

ここ1週間（2026-05-13 ～ 2026-05-20）での広聴AI (kouchou-ai) リポジトリの活動内容をまとめました。まずは完了したIssueやマージされたPull Requestを紹介し、続いて現在進行中の議論や未完了のIssue/PRを挙げています。OSS開発に興味を持ってくださった方は、ぜひリポジトリを訪れてディスカッションや実装に参加してみてください。

---

## 1. 今週完了したIssue

### [Issue #830](https://github.com/digitaldemocracy2030/kouchou-ai/issues/830)  
- 作成者: nishio  
- CLI/analysis-coreでクラスタ数(cluster_nums)を省略時に自動計算できるようにし、膨大なコメント数でも適切なクラスタリングを行いやすくしました。  
- 解決したPR: [PR #832](https://github.com/digitaldemocracy2030/kouchou-ai/pull/832)

### [Issue #800](https://github.com/digitaldemocracy2030/kouchou-ai/issues/800)  
- 作成者: tokoroten  
- Overviewコンポーネントでresult.configがundefinedの場合にクラッシュする不具合を修正。  
- 解決したPR: [PR #834](https://github.com/digitaldemocracy2030/kouchou-ai/pull/834)

### [Issue #726](https://github.com/digitaldemocracy2030/kouchou-ai/issues/726)  
- 作成者: nishio  
- 公開状態にしたレポートがないまま静的HTML出力を行うとわかりにくいエラーが出る問題を修正し、わかりやすい日本語のメッセージで対処を促すようにしました。  
- 解決したPR: [PR #814](https://github.com/digitaldemocracy2030/kouchou-ai/pull/814)

---

## 2. 今週マージされたPull Request

以下は過去7日間（5/13～5/20）にマージされたPR一覧です。開発者ではないユーザにとっては馴染みの薄い変更もありますが、新機能追加や不具合修正に貢献してくださった方々を紹介します。

- [PR #839](https://github.com/digitaldemocracy2030/kouchou-ai/pull/839)  
  - 作成者: nishio  
  - 内容: 不要なlockfileのgit追跡をignoreに追加し、ビルドノイズを減らす調整。

- [PR #835](https://github.com/digitaldemocracy2030/kouchou-ai/pull/835)  
  - 作成者: nishio  
  - 内容: 静的ビルド時のエラーハンドリングを改善し、ようこそページやOGP画像生成で発生する不具合をよりわかりやすく修正。

- [PR #834](https://github.com/digitaldemocracy2030/kouchou-ai/pull/834)  
  - 作成者: nishio  
  - 内容: 不正な`hierarchical_result.json`が返される場合にAPI側で事前に検証・エラー送出を行い、public-viewerのクラッシュを防止。(Issue #800を解決)

- [PR #832](https://github.com/digitaldemocracy2030/kouchou-ai/pull/832)  
  - 作成者: nishio  
  - 内容: `cluster_nums` 未指定時に自動でクラスタ数を算出する機能をanalysis-core側に追加。(Issue #830を解決)

- [PR #831](https://github.com/digitaldemocracy2030/kouchou-ai/pull/831)  
  - 作成者: nishio  
  - 内容: analysis-coreをPyPIに自動リリースするCIワークフローを追加。

- [PR #829](https://github.com/digitaldemocracy2030/kouchou-ai/pull/829)  
  - 作成者: nishio  
  - 内容: hierarchical clusteringで固定の`random_state=42`を廃止し、並列化を有効に。

- [PR #828](https://github.com/digitaldemocracy2030/kouchou-ai/pull/828)  
  - 作成者: nishio  
  - 内容: public-viewerで使用しているAPIのベースURLが不一致の場合に発生するビルド失敗を修正。

- [PR #827](https://github.com/digitaldemocracy2030/kouchou-ai/pull/827)  
  - 作成者: nishio  
  - 内容: LLMの機能や可視化要件を整理する将来的な計画ドキュメントを追加。

- [PR #826](https://github.com/digitaldemocracy2030/kouchou-ai/pull/826)  
  - 作成者: nishio  
  - 内容: analysis-core向けのCIとテスト修正を行い、CLIの`--dry-run`機能を強化。

- [PR #825](https://github.com/digitaldemocracy2030/kouchou-ai/pull/825)  
  - 作成者: nishio  
  - 内容: analysis-coreでHTMLレポートを自動生成する際の仕組みをself-contained HTMLに統合。`--without-html`の既定値見直しなどを実施。

- [PR #824](https://github.com/digitaldemocracy2030/kouchou-ai/pull/824)  
  - 作成者: nishio  
  - 内容: ローカル推論用LLMの接続先をフルURLで指定できる機能を追加。認証付きゲートウェイにも対応。

- [PR #823](https://github.com/digitaldemocracy2030/kouchou-ai/pull/823)  
  - 作成者: dependabot[bot]  
  - 内容: Next.jsバージョンアップの自動依存関係更新。セキュリティ修正が含まれるため重要。

- [PR #822](https://github.com/digitaldemocracy2030/kouchou-ai/pull/822)  
  - 作成者: dependabot[bot]  
  - 内容: こちらもNext.jsの依存関係更新。ダミーサーバーのパッケージを含むため、テスト用途の環境整備が進む。

- [PR #817](https://github.com/digitaldemocracy2030/kouchou-ai/pull/817)  
  - 作成者: shingo-ohki  
  - 内容: 誤って混入したCI設定(CodeRabbitやCodeQL)を見直し、不要な部分を整理。

- [PR #814](https://github.com/digitaldemocracy2030/kouchou-ai/pull/814)  
  - 作成者: Copilot  
  - 内容: 公開レポートが0件の場合の静的ビルドエラーをわかりやすいメッセージで示すよう改善。(Issue #726を解決)

---

## 3. 未完了・進行中のIssue

### 新しく作成されたIssue (4件)
- [Issue #836](https://github.com/digitaldemocracy2030/kouchou-ai/issues/836): analysis-core CLIのfilesystem実行方法ドキュメント化 (作成者: nishio)  
- [Issue #837](https://github.com/digitaldemocracy2030/kouchou-ai/issues/837): analysis-core CLIにconfig/inputの事前検証機能を追加検討 (作成者: nishio)  
- [Issue #838](https://github.com/digitaldemocracy2030/kouchou-ai/issues/838): 出力アーティファクトの検証方法を検討 (作成者: nishio)  
- [Issue #833](https://github.com/digitaldemocracy2030/kouchou-ai/issues/833): #685のフォローアップとしてapps/*ツリーへCSP修正を再実装 (作成者: nishio)

### 過去7日間に更新されたIssue (2件)
- [Issue #721](https://github.com/digitaldemocracy2030/kouchou-ai/issues/721) (作成者: NISHIO + Devin)  
  ファイルシステムベース実行方式の明確化と検証テスト追加。引き続きCLI検証フローの改良やドキュメントの整備が議論されています。  
- [Issue #493](https://github.com/digitaldemocracy2030/kouchou-ai/issues/493) (作成者: mtane0412)  
  スクロール時にScatterChartが拡大縮小されてしまう問題に対し、オーバーレイで誤操作を防ぐアプローチが検討・実装途中です。

---

## 4. 進行中のPull Request

### 新規作成されたPR (1件)
- [PR #840](https://github.com/digitaldemocracy2030/kouchou-ai/pull/840) (作成者: nishio)  
  analysis-coreのワークフロー実行をデフォルト化する準備として、入力アーティファクトやlegacy設定の同期を追加した段階的リファクタです。今後さらなる調整が行われる見込み。

### 更新されているPR (9件)
- [PR #810](https://github.com/digitaldemocracy2030/kouchou-ai/pull/810) (作成者: Copilot)  
  UMAPの`random_state`を設定可能にし並列化を有効にする提案。現在別方向のPR(#829)が先にマージされ、一部競合中。
- [PR #802](https://github.com/digitaldemocracy2030/kouchou-ai/pull/802) (作成者: Copilot)  
  Overviewコンポーネントのクラッシュ防止修正案だが、こちらも#834が先にマージされたため扱いが検討中。
- [PR #801](https://github.com/digitaldemocracy2030/kouchou-ai/pull/801) (作成者: Copilot)  
  Reactの重複インストールで起きるローカル開発クラッシュを解消するための修正。まだレビュー中の様子。
- [PR #735](https://github.com/digitaldemocracy2030/kouchou-ai/pull/735) (作成者: Devesh36)  
  CSPとLocalLLM取得処理をまとめて修正する試み。現行の`apps/*`構成とコンフリクトしており、re-implementが必要との議論。
- [PR #734](https://github.com/digitaldemocracy2030/kouchou-ai/pull/734) (作成者: Devesh36)  
  Biomeによるリンティングとフォーマットを段階的に統合する案。まだフェーズ1のまま残っており、完全施行には至っていない。
- [PR #727](https://github.com/digitaldemocracy2030/kouchou-ai/pull/727) (作成者: NISHIO+Devin)  
  静的ビルド開始前に公開レポートがあるか検証するスクリプトを追加する提案。#814等と同様の狙いが重複しており、今後の統合方針を検討中。
- [PR #722](https://github.com/digitaldemocracy2030/kouchou-ai/pull/722) (作成者: NISHIO+Devin)  
  ファイルシステムベース実行のドキュメントとバリデーションテスト追加の大規模PR。レビューは概ね好評ながら、一部ステップの兼ね合いでマージタイミング調整中。
- [PR #597](https://github.com/digitaldemocracy2030/kouchou-ai/pull/597) (作成者: dentaro)  
  ScatterChartの意図しない拡大縮小を回避する試作実装。Issue #493の解消を目指すが、最新のChart構成とも調整が必要との声あり。

---

## 5. 参加の呼びかけ

- 使ってみて気になった点を [Issue](https://github.com/digitaldemocracy2030/kouchou-ai/issues) で報告いただけると助かります。
- コード修正や新機能提案の [Pull Request](https://github.com/digitaldemocracy2030/kouchou-ai/pulls) も歓迎です。  
- ドキュメント作成やレビューなどプログラム以外の貢献もお待ちしています。

ぜひOSS開発に参加して、広聴AIを一緒により良いものにしていきましょう！ご協力よろしくお願いいたします。