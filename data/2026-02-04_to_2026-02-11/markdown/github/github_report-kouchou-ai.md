# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-02-04T13:01:09.535791+09:00 から 2026-02-11T13:01:09.535791+09:00 まで

## Issues

### 過去7日間に完了されたissue (3件)

### [public-viewer が起動時ビルドで失敗しヘルスチェックがタイムアウトする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/783)

**作成者:** nishio  
**作成日:** 2026-02-07T04:23:11Z  
**内容:**

## 概要
Azure Container Apps の `public-viewer` が起動時に `next build` を実行して失敗し、Viewer 側のヘルスチェックがタイムアウトします。CI の Azure Deployment でも失敗します。

## 事象
- API は 200 を返すが、`public-viewer` はタイムアウト
- `public-viewer` コンテナログで Turbopack の root 解決エラーが出る

## ログ抜粋
```
Error: Next.js inferred your workspace root, but it may not be correct.
We couldn't find the Next.js package (next/package.json) from the project directory: /repo/apps/public-viewer/app
To fix this, set turbopack.root in your Next.js config, or ensure the Next.js package is resolvable from this directory.
```

## 影響
- `public-viewer` が起動できず、Viewer のヘルスチェックが失敗
- Azure Deployment の CI が失敗する

## 対応案
- `apps/public-viewer/next.config.ts` に `turbopack.root` を明示（`__dirname` からワークスペースルート）
- 併せて runner イメージに `pnpm-lock.yaml` をコピーする案も検討

## 補足
- PR #782（public-viewer の runner へルートファイルコピー、CI の viewer ヘルスチェック追加）をマージ済みだが、現象は継続


**コメント:** なし

---

### [[FEATURE]レポート生成ページから一覧ページに戻る手段がなさそう](https://github.com/digitaldemocracy2030/kouchou-ai/issues/775)

**作成者:** nishio  
**作成日:** 2026-02-03T11:59:00Z  
**内容:**

# 背景
レポート生成ページから一覧ページに戻る手段がなさそう
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

**コメント:** なし

---

### [[REFACTOR] 未解決パスが最終キー欠落時に None になり、誤設定が黙殺される可能性](https://github.com/digitaldemocracy2030/kouchou-ai/issues/766)

**作成者:** nishio  
**作成日:** 2026-01-26T01:56:24Z  
**内容:**

# 現在の問題点
packages/analysis-core/src/analysis_core/workflow/engine.py (1)
219-241: 未解決パスが最終キー欠落時に None になり、誤設定が黙殺される可能性があります。


# 提案内容

最終キーが存在しない場合は明示的にエラーにするべきです。現状だと None が静かに混入し、後段で原因特定が難しくなります。

```
                result = full_config
                for key in path.split("."):
                    if isinstance(result, dict):
-                        result = result.get(key)
+                        if key not in result:
+                            raise ...
+                        result = result[key]
                    else:
                        return value  # Can't resolve, return original
                return result
```

**コメント:** なし

---

### 過去7日間に作成されたissue (0件)

### 過去7日間に更新されたissue（作成・クローズを除く）(1件)

### [[BUG] main ブランチへのマージ時に実行される Azure への deploy が失敗する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/741)

**作成者:** shingo-ohki  
**作成日:** 2025-12-27T14:53:28Z  
**内容:**

### 概要

表題通り。

- 失敗したときの事例
https://github.com/digitaldemocracy2030/kouchou-ai/actions/runs/20540103407/attempts/1

- リトライで直った
https://github.com/digitaldemocracy2030/kouchou-ai/actions/runs/20540103407

### 再現手順

1. main ブランチに更新を入れる
2. GitHub Actions で Azure への deploy 処理が動く
3. たまに失敗する

### 期待する動作

毎回 deploy が成功する
<!-- 本来どう動作すべきかを記入してください -->

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

### その他

AIによると、原因はこんな感じ
```
発生箇所: Azure デプロイの Docker ビルド中、client イメージの Dockerfile:14 の RUN npm ci で npm ERR! code ECONNRESET により失敗。内容は npm レジストリへの接続リセットで、依存関係の不整合ではありません。
文脈: azure-deploy.yml:53-90 で API/client/client-admin/client-static-build の 4 イメージを並列ビルド。複数の npm ci が同時に走るため、GitHub ホストランナー上でレジストリへの接続がまれに途切れる典型的なネットワーク起因の失敗です。
他のステージ (Python 依存、client-admin ビルドなど) は完走しており、恒常的な依存問題ではなく一時的な接続切れが原因と考えられます。

対応案（優先度順）

1. まずはリトライ実行: ワークフローを再実行すれば通る可能性が高いです。
2. npm ci にリトライとタイムアウトを付与 (各 Dockerfile の npm 実行直前で):
例: npm config set fetch-retries 5 && npm config set fetch-retry-mintimeout 20000 && npm config set fetch-retry-maxtimeout 120000 && npm config set registry https://registry.npmjs.org/
あるいは npm ci --fetch-retries=5 --fetch-retry-mintimeout=20000 --fetch-retry-maxtimeout=120000 --network-timeout=600000
対象: Dockerfile:14, Dockerfile:17, Dockerfile:5 と同ファイル内 2 回目の npm ci.
3. 並列度を下げる: ワークフローで Docker ビルドを直列にする、または client 系をまとめて後段にずらすことでレジストリへの同時接続を減らす。
4. npm キャッシュ活用: Docker BuildKit のキャッシュマウントや npm ci --cache /tmp/npm-cache を併用し、外部アクセス回数を削減。
まずは 1) を試し、再発するようなら 2) を反映、それでも改善しなければ 3)/4) を検討するのが現実的です。
```

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (19件)

### [docs: add AI assistant skills and usage guide](https://github.com/digitaldemocracy2030/kouchou-ai/pull/793)

**作成者:** nishio  
**作成日:** 2026-02-10T13:36:49Z  
**変更:** +187 -200 (6ファイル)  
**マージ日:** 2026-02-10T14:41:26Z  
**内容:**

# 変更の概要
- CLAUDE.md をスキル索引に整理し、skills/ にアーキテクチャ/開発/テストのスキルを追加
- Claude Code/Codex でのスキル利用手順を docs に追加し、mkdocs ナビにも追加
- kouchou-ai-development スキルに PR テンプレ遵守の記載を追加

# スクリーンショット
- なし（ドキュメント変更のみ）

# 変更の背景
- CLAUDE.md の内容を skills に分割し、AI 連携で必要な情報を扱いやすくするため
- Codex 利用時の導線を docs に用意するため

# 関連Issue
なし

# 動作確認の結果
未実施（ドキュメント更新のみ）

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **ドキュメント**
  * 大規模ガイドを簡潔な「スキル索引」へ置換し、個別スキル文書への参照に集約しました
  * Claude/Codex 向けの開発者向けガイドを追加（セットアップ例と利用手順を含む）
  * アーキテクチャ／開発／テストに関する三つの新しいスキル文書を追加し手順や運用メモを整理しました
  * サイトナビゲーションに新セクションを追加しました
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [docs: fix docs site URLs in README](https://github.com/digitaldemocracy2030/kouchou-ai/pull/792)

**作成者:** nishio  
**作成日:** 2026-02-10T12:59:52Z  
**変更:** +9 -9 (1ファイル)  
**マージ日:** 2026-02-10T13:00:17Z  
**内容:**

# 変更の概要
- README の docs site URL 末尾のスラッシュを削除し、404 を解消

# スクリーンショット
- なし（UI 変更なし）

# 変更の背景
- GitHub Pages で末尾スラッシュ付き URL が 404 になる報告があったため

# 関連Issue
- なし

# 動作確認の結果
- なし

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


**コメント:** なし

---

### [docs: embed repo readmes](https://github.com/digitaldemocracy2030/kouchou-ai/pull/791)

**作成者:** nishio  
**作成日:** 2026-02-10T11:39:19Z  
**変更:** +61 -23 (8ファイル)  
**マージ日:** 2026-02-10T12:55:32Z  
**内容:**

# 変更の概要
- repo README は mkdocs の pre-build フックで docs にコピー生成し、snippets の利用を廃止
- docs site から GitHub Markdown に遷移しないよう、コピー時にリンクを書き換え
- ルート README のドキュメント参照を docs site のURLに統一
- repo-readmes を生成物として ignore に追加

# スクリーンショット
- なし（UI 変更なし）

# 変更の背景
- docs site 内で完結する導線を作り、リンク切れ検知と運用負荷を下げるため

# 関連Issue
- なし

# 動作確認の結果
- `mkdocs build`

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


**コメント:** なし

---

### [docs: consolidate and clean up documentation](https://github.com/digitaldemocracy2030/kouchou-ai/pull/790)

**作成者:** nishio  
**作成日:** 2026-02-10T11:24:27Z  
**変更:** +16 -3888 (23ファイル)  
**マージ日:** 2026-02-10T11:29:33Z  
**内容:**

# 変更の概要
- Azure のデプロイ手順を docs 配下へ移動し、リンク/フック/ignore を整理
- 重複/古いドキュメント（how_to_use、計画/テスト計画）を削除
- MkDocs のアンカー/リンク修正と nav 更新（testing 追加）
- 各ディレクトリの README を docs に埋め込み（pymdownx.snippets）

# スクリーンショット
- なし（UI 変更なし）

# 変更の背景
- リポジトリ整理の一環として、ドキュメントの配置・重複・古い資料を整理するため

# 関連Issue
- なし

# 動作確認の結果
- `mkdocs build`

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


**コメント:** なし

---

### [テストからPandas依存を取り除く](https://github.com/digitaldemocracy2030/kouchou-ai/pull/789)

**作成者:** nishio  
**作成日:** 2026-02-10T10:00:51Z  
**変更:** +26 -27 (3ファイル)  
**マージ日:** 2026-02-10T10:43:33Z  
**内容:**

テストにPandas依存が残っていたので取り除く

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Fix cluster count display for single-level reports](https://github.com/digitaldemocracy2030/kouchou-ai/pull/788)

**作成者:** nishio  
**作成日:** 2026-02-09T08:26:14Z  
**変更:** +15 -6 (2ファイル)  
**マージ日:** 2026-02-10T05:11:59Z  
**内容:**

- Guard against missing level 2 cluster counts in Analysis summary\n- Skip arrow/level-2 output when only one hierarchy level exists

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Refactor**
  * クラスター階層番号の表示ロジックを改善しました。第1レベルは欠損時に0を表示するよう安定化し、第2レベルが存在する場合は矢印で第1→第2の表記を追加、第2レベルがない場合でも表示が崩れないようにしました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix: ReportConfig.nameをオプショナルに変更（CLI生成レポート対応）](https://github.com/digitaldemocracy2030/kouchou-ai/pull/787)

**作成者:** nishio  
**作成日:** 2026-02-09T07:07:54Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2026-02-09T07:29:32Z  
**内容:**

# 変更の概要
- `ReportConfig.name`を必須からオプショナル（`str | None = None`）に変更
- CLI経由でパイプラインを実行した場合、configに`name`フィールドが含まれないケースに対応

# スクリーンショット
- UIの変更なし

# 変更の背景
- WebUI経由: `report_launcher.py`で`name`フィールドが自動追加される
- CLI経由: ユーザーが用意したconfigをそのまま使用するため、`name`が含まれない

CLI生成レポートをWebUIで表示しようとすると、Pydanticのバリデーションエラーが発生していた：
ValidationError: 1 validation error for ReportConfig name Field required [type=missing, ...]

# 関連Issue
なし（運用中に発見した問題）

# 動作確認の結果
- CLI生成レポート（`name`なし）がWebUIで表示できることを確認
- 既存のWebUI経由で作成したレポートが引き続き正常に動作することを確認

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

🤖 Generated with [Claude Code](https://claude.com/claude-code)

**コメント:** なし

---

### [Azure Deployment のヘルスチェックを改善（public-viewer 起動遅延を許容）](https://github.com/digitaldemocracy2030/kouchou-ai/pull/785)

**作成者:** nishio  
**作成日:** 2026-02-07T05:04:06Z  
**変更:** +15 -10 (1ファイル)  
**マージ日:** 2026-02-07T05:14:52Z  
**内容:**

## 概要
Azure Deployment の「デプロイ確認」(ヘルスチェック) を、`public-viewer` の起動に時間がかかる場合でも false negative にならないように改善します。

## 背景
`public-viewer` は起動時に `next build` を実行するため、デプロイ直後に数分間 200 を返せないことがあります。
現状のリトライ回数 (6回) だと、実際にはその後正常起動しているのに CI 側が失敗扱いになるケースがありました。

## 変更内容
- リトライ回数を 6回 -> 15回 に増加
- 各試行で API / viewer の HTTP ステータスコードを表示
- 失敗時に API / public-viewer の最新 revision 状態 (health/running/details) を出力

## 期待する効果
- `public-viewer` の起動遅延による一時的なタイムアウトで CI が落ちにくくなる
- 失敗時の原因調査がログだけでしやすくなる


- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **改善点**
  * デプロイメント時のヘルスチェック機能を強化しました。リトライメカニズムを改善し、より堅牢なサービス検証機能を実装しました。エラー時の診断情報も拡張されています。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [public-viewer の turbopack root を明示して起動時ビルドを修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/784)

**作成者:** nishio  
**作成日:** 2026-02-07T04:26:03Z  
**変更:** +5 -0 (1ファイル)  
**マージ日:** 2026-02-07T04:35:44Z  
**内容:**

## 概要
- `apps/public-viewer/next.config.ts` に `turbopack.root` を明示して、モノレポのワークスペースルート解決に失敗する問題を回避します。

## 背景
- `public-viewer` の起動時 `next build` が Turbopack の root 推論に失敗し、コンテナが起動できずヘルスチェックがタイムアウトしていました。

## 影響
- Viewer の起動失敗を解消し、CI のヘルスチェックも通るようにします。

Fixes #783

## テスト
- 未実施（インフラ/設定変更）

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **その他**
  * ビルドシステムの設定を更新しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Fix public-viewer runtime build by copying workspace root files](https://github.com/digitaldemocracy2030/kouchou-ai/pull/782)

**作成者:** nishio  
**作成日:** 2026-02-07T03:04:29Z  
**変更:** +140 -0 (4ファイル)  
**マージ日:** 2026-02-07T03:41:45Z  
**内容:**

## Summary
- Fix public-viewer runtime build by copying workspace root files into the runner image (package.json / pnpm-workspace.yaml / .npmrc)
- Fail fast if public-viewer build fails at container startup
- Add public-viewer health check to Azure deploy workflow
- Document Azure Container Apps rename migration

## Why
- The container was failing at runtime with Turbopack root inference errors because the workspace root metadata was missing in the runner image.

[x]CLAの内容を読み、同意しました

## Testing
- Not run (infra changes)

**コメント:** なし

---

### [fix(api): Pandas依存が残っていたところをPolarsに一本化](https://github.com/digitaldemocracy2030/kouchou-ai/pull/781)

**作成者:** nishio  
**作成日:** 2026-02-05T08:56:56Z  
**変更:** +63 -20 (4ファイル)  
**マージ日:** 2026-02-06T06:19:18Z  
**内容:**

## Summary
- replace pandas usage in plugin base with polars
- update YouTube plugin + plugin endpoints to use polars DataFrames
- update plugin registry tests accordingly

## Testing
- rye run pytest tests/plugins

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

# リリースノート

* **リファクタ**
  * データ処理ライブラリをPolarsへ移行し、内部パフォーマンスと処理効率を向上させました。
* **API変更**
  * インポートおよびプレビューで返されるコメントデータのフォーマットを見直し、より一貫した配列形式で返すように最適化しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Fix Azure deploy build context for monorepo](https://github.com/digitaldemocracy2030/kouchou-ai/pull/780)

**作成者:** nishio  
**作成日:** 2026-02-05T05:57:25Z  
**変更:** +17 -3 (1ファイル)  
**マージ日:** 2026-02-05T14:28:15Z  
**内容:**

## 変更内容
- api/public-viewer/admin の Docker build をリポジトリルートのコンテキストで実行し、各 Dockerfile を明示指定
- ルートコンテキスト化に伴う `.env.azure` の混入リスクを避けるため、ビルド中は一時退避して終了後に復元

## この修正をしようと考えた理由
PR #746 で monorepo 構成（`apps/`, `packages/`）に移行した結果、各 Dockerfile が `COPY apps/...` や `COPY packages/...` を前提とする構成になりました。
しかし azure-deploy.yml では `docker build ... ./apps/<name>` のようにサブディレクトリをコンテキストにしていたため、BuildKit のログに `"/apps/*" not found` や `"/packages/*" not found` が出て即失敗していました。
このため、Docker build のコンテキストをリポジトリルートに戻し、`-f apps/.../Dockerfile` を明示する修正が必要と判断しました。
また、ルートコンテキスト化により `.env.azure` が build context に含まれるため、誤ってイメージに取り込まれるリスクがあり、ワークフロー内で一時退避する対応を追加しました。

## テスト
- 未実施（CI ワークフローの修正のみ）

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **チョア**
  * デプロイメント ワークフローを改善し、環境変数の一時保護と復元を導入してデプロイの安定性を向上しました。
  * コンテナビルド手順を明確化・統一し、複数サービスのビルド処理をより確実に実行するようにしました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [chore: migrate from deprecated google-generativeai to google-genai](https://github.com/digitaldemocracy2030/kouchou-ai/pull/779)

**作成者:** nishio  
**作成日:** 2026-02-04T18:37:33Z  
**変更:** +249 -417 (13ファイル)  
**マージ日:** 2026-02-07T16:02:12Z  
**内容:**

# 変更の概要
- 非推奨となった `google-generativeai` パッケージから新しい `google-genai` パッケージへの移行
- インポート文を `import google.generativeai as genai` から `from google import genai` に変更
- エラーハンドリングを `google.api_core.exceptions` から `google.genai.errors` に変更（`ClientError`/`ServerError` + `code` 判定）
- 新しい Client-based API へ移行（`genai.configure()` / `GenerativeModel` → `genai.Client()`）
- `generate_content` / `embed_content` の呼び出しを新SDKの形式に更新
- `apps/api` / `packages/analysis-core` の lockfile（`requirements*.lock`）を再生成し、CIの `pip install -r requirements-dev.lock` が通る状態に修正
- `google-genai` 版に合わせて `apps/api` のユニットテストを更新
- optional dependency の import が `ImportError` でも落ちないように調整（`google` 名前空間のみ存在する環境向け）

# スクリーンショット
- UIの変更はありません

# 変更の背景
`google.generativeai` パッケージが非推奨となり、以下のFutureWarningが表示されるようになったため：
```
FutureWarning: All support for the `google.generativeai` package has ended.
It will no longer be receiving updates or bug fixes.
Please switch to the `google.genai` package as soon as possible.
```

参考: https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md

# 動作確認の結果
- `apps/api`: `rye run pytest`（171 passed, 2026-02-07）
- `apps/api`: `rye run ruff check . --ignore I`
- Gemini API の実アカウントでの疎通は未実施（ユニットテストはモック）

# レビュー時の注意点
1. **contentsフォーマットの変更**: 旧SDKでは `parts: [content]` でしたが、新SDKでは `parts: [{"text": content}]` の形式に変更しています
2. **エラーハンドリングの変更**: 個別の例外クラス（`Unauthenticated`, `InvalidArgument`等）から、`ClientError`/`ServerError` + エラーコードでの判定に変更しています
3. **レート制限処理**: 429 の場合は指数バックオフでリトライします（レスポンスから `retry_delay` を拾う処理は削除）

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する

---
Link to Devin run: https://app.devin.ai/sessions/b52ba5460bda4bc482c0cf7b4945349c
Requested by: NISHIO (@nishio)


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **チョア**
  * Google Gemini API パッケージの依存関係を更新しました

* **バグ修正**
  * Gemini API のエラーハンドリングと レート制限の再試行ロジックを改善しました
  * API レスポンス処理の安定性を向上させました

* **その他**
  * 内部コードの整理と最適化を実施しました

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat(admin): レポート可視性アイコンにツールチップを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/778)

**作成者:** nishio  
**作成日:** 2026-02-04T18:22:01Z  
**変更:** +228 -212 (4ファイル)  
**マージ日:** 2026-02-05T08:54:24Z  
**内容:**

# 変更の概要
- 管理画面のレポートカードにある可視性アイコン（公開/限定公開/非公開）にマウスホバー時のツールチップを追加
- ツールチップには現在の可視性状態のテキスト（「公開」「限定公開」「非公開」）が表示される
- メニューが開いている間はツールチップを非表示にする制御を追加
- IconButtonに`aria-label`を追加してアクセシビリティを向上

# スクリーンショット
<img width="309" height="132" alt="image" src="https://github.com/user-attachments/assets/7368eccc-76ae-4f2a-abeb-f36504e8bbcc" />
<img width="149" height="153" alt="image" src="https://github.com/user-attachments/assets/1cae96ed-cb32-45db-917b-3c9f50621aaf" />


- ローカル環境で動作確認済み（ツールチップが正しく表示されることを確認）

# 変更の背景
アイコンだけでは意味がわからないユーザーがいるため、マウスホバー時にツールチップで説明を表示することでUXを改善する。

Slackでの依頼: https://dd2030.slack.com/archives/C08PRQVQWSE/p1770228861671249

# 関連Issue
なし

# 動作確認の結果
- ローカル環境でdummy-serverとadminアプリを起動し、以下を確認：
  - 可視性アイコンにマウスホバーするとツールチップが表示される
  - ツールチップに正しい可視性テキスト（「非公開」など）が表示される
  - メニューを開くとツールチップが消える

# レビュー時の確認ポイント
- ツールチップがホバー時に正しく表示されるか
- ツールチップとメニューの開閉が干渉しないか（メニューを開いた際にツールチップが消えるか）
- スクリーンリーダーで`aria-label`が正しく読み上げられるか

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している

---
Link to Devin run: https://app.devin.ai/sessions/0dcf4f55f28d439f9b6e0533fe174b0d
Requested by: NISHIO (@nishio)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **新機能**
  * 各レポート数ブロックにツールチップを追加し、可視性ラベルをホバーで表示。
  * アクションメニューに「レポート名編集」「再利用」「CSV/JSON/HTML出力」など新しい項目を追加（ダウンロード種別の選択やグループ化を含む）。
* **Refactor**
  * メニュー構造とツールチップの表示ロジックを整理し重複表示を回避。
  * ツールチップの振る舞いをルート側で制御するよう改善。
* **アクセシビリティ**
  * 各操作要素にaria-labelを追加。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat: レポート作成ページから一覧ページに戻る手段を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/776)

**作成者:** nishio  
**作成日:** 2026-02-03T12:09:51Z  
**変更:** +13 -4 (2ファイル)  
**マージ日:** 2026-02-05T07:28:10Z  
**内容:**

# 変更の概要
- Headerのロゴをクリックすると一覧ページ（`/`）に遷移するようにした
- レポート作成ページに「キャンセル」ボタンを追加し、一覧ページに戻れるようにした

# スクリーンショット
- UIの変更を伴うため、レビュアーによる動作確認をお願いします

# 変更の背景
レポート作成ページ（`/create`）から一覧ページに戻る手段がなく、ブラウザの「戻る」ボタンを使うかURLを直接入力するしかなかった。一般的なUXパターンとして、ロゴクリックでホームに戻る機能と、明示的なキャンセルボタンの両方を追加した。

# 関連Issue
Closes #775

# 動作確認の結果
- lintチェック（biome check）をパスすることを確認

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

---

Link to Devin run: https://app.devin.ai/sessions/31494be5fd754bb182ffcec0b6d792f7
Requested by: @nishio

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **新機能**
  * 作成ページにキャンセルボタンを追加。ホームページへ戻る機能を提供
  * ヘッダーロゴをクリック可能にしました。ロゴをクリックするとホームページに移動します

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat: public-viewer の API 接続エラー時にわかりやすいメッセージを表示](https://github.com/digitaldemocracy2030/kouchou-ai/pull/771)

**作成者:** nishio  
**作成日:** 2026-01-26T14:16:35Z  
**変更:** +162 -38 (6ファイル)  
**マージ日:** 2026-02-05T05:24:41Z  
**内容:**

# 変更の概要
- public-viewer で API への接続エラーが発生した際に、500エラーではなく詳細な診断情報を含むエラーページを表示するように改善
- 新しい `ApiConnectionError` コンポーネントを追加し、以下の情報を表示:
  - 接続先 API URL
  - リクエスト元（サーバーサイド/クライアントサイド）
  - エラー詳細メッセージ
  - 考えられる原因と対処法（特に Container Apps 環境での設定ミスについて）

# スクリーンショット
- UIの変更を伴いますが、エラー発生時のみ表示されるため、スクリーンショットは省略

# 変更の背景
Container Apps 環境で public-viewer が 500 エラーになる場合、server-side fetch が `api:8000` に向いており到達不可となることが原因でした。しかし、単なる 500 エラーを見てからサーバーのエラーログを見て修正するのは難易度が高いため、ブラウザ上でわかりやすいメッセージを出すように改善しました。

# 関連Issue
なし

# 動作確認の結果
- lint チェック（biome check）が通過することを確認

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

## レビュー時の確認ポイント
- エラーハンドリングはネットワークレベルのエラー（ECONNREFUSED, ENOTFOUND等）のみをキャッチしています。HTTP エラーレスポンス（500等）は別途処理が必要な場合があります
- `ApiConnectionError` コンポーネントの日本語テキストが適切か確認してください
- Chakra UI のスタイリングが意図通りに表示されるか確認してください

---
Link to Devin run: https://app.devin.ai/sessions/cd5292e87671419da5e14e5ca0541780
Requested by: @nishio

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **新機能**
  * API接続エラー用の詳しいエラー画面を追加。接続先URL、エラー詳細、考えられる原因や対処法が表示されます。
  * サーバー／クライアントの起点情報や再試行ボタンの視覚改善を反映。

* **リファクタ**
  * 複数ページでのエラー表示を共通化し、表示フローを統一しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [レポートの再利用機能](https://github.com/digitaldemocracy2030/kouchou-ai/pull/769)

**作成者:** nishio  
**作成日:** 2026-01-26T07:34:36Z  
**変更:** +2869 -2361 (69ファイル)  
**マージ日:** 2026-02-05T00:53:42Z  
**内容:**

# 変更の概要

主要機能：既存のレポートを複製し「再利用」して新規レポートを作成する機能の実装・実運用化
- レポート複製の計画策定〜実装まで完了（plan → backend → UI → tests）。
- 再利用専用ページ /reuse/:slug を追加し、UI/フローを構築。
- ローカルでの手でのテスト、Azure環境にDeployしての手でのテスト、および自動テストを通過


# スクリーンショット

既存のレポートを再利用して、英語で要約するようにプロンプトを変えて再実行している様子:

<img width="838" height="660" alt="image" src="https://github.com/user-attachments/assets/1a5780d6-2402-4260-bada-bb5836f52cd9" />
<img width="1114" height="1228" alt="image" src="https://github.com/user-attachments/assets/50d1aad1-82b7-41fb-80b1-6b61515be931" />
<img width="2532" height="1748" alt="image" src="https://github.com/user-attachments/assets/f18747cd-645f-4a22-b46c-445a86922862" />


# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [x] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

 
# 細かい変更点
API・再利用ロジックの堅牢化
- slug検証の共通化（utilsへ移動）＆ duplicate slug の厳密チェック。
- 設定ファイル・入力ファイルが欠けている旧レポートの再利用に対応(hierarchical_result.json内の config を利用, arguments から CSV を再構成)
- ロガー出力先を環境変数 LOG_FILE で指定可能に。

管理画面の安定化・安全性
- 再利用フローの 送信/取得/エラー処理を強化。
- config 取得は server route経由でAPIキー露出を回避。
- UIの hydration error（<p> 入れ子など）を修正。

E2E・CIの安定化
- Playwright用の static build・basePathのテスト安定化。
- slugを固定し、テストを安定化
- 再利用フローの E2E アサーションを追加/修正。

Next.js 16 対応（影響範囲が広いため明記）
- Next.js 16.1.5 への更新（public-viewer / admin / dummy-server）。DependabotのNext 16.1.5更新PR（main側）を取り込んだ結果、revalidateTagのシグネチャやstatic export出力先の変更に追随する必要が出ました。
- revalidateTag(tag, "max") へ更新（Next 16 シグネチャ対応）。
- static export 出力先が out ではなく distDir になる変更に対応 → build script を更新、.next キャッシュ分離。
- basePath付きの static build で生成されるRSC用のテキストリソース `__next.*.txt` を テスト側で許容。以前のテストは「/kouchou-ai/_next と /kouchou-ai/images 以外のURLはNG」という判定だったので、新しい正当なURLが「不正扱い」になって落ちていた。

ドキュメント/雑務
- ローカル開発の quickstart とトラブルシュート（undefined link など）を追加。
- E2E安定化のログを docs に記録。
- pnpm 前提へ docs/scripts を整備。

依存更新 / maintenance
- Next.js 16 への依存更新（mainからのmerge含む）。
- pandas→polars の lock 反映。
- ruff/CI lint の整合性改善（CIとローカルの lint を一致させる調整）。


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * レポートの複製・再利用ワークフローを追加。既存レポートを新IDで複製し、タイトル／概要／プロンプト／クラスタ／モデル等を上書き可能。管理UIから操作でき、進行状況表示とコンフリクト検出を提供します。

* **Documentation**
  * ユーザー向け「レポート再利用」ガイドと実装計画、E2E安定化計画を追加・更新。

* **Bug Fixes / Tests**
  * 複製フローの単体・E2Eテストを追加し、競合・ファイル処理の挙動を検証。

* **Chores**
  * 開発・CIのパッケージ管理をpnpmへ移行し、関連スクリプト・設定を更新。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat: CLI使用時に.envの設定不良をfail-fastする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/768)

**作成者:** nishio  
**作成日:** 2026-01-26T02:14:01Z  
**変更:** +162 -8 (3ファイル)  
**マージ日:** 2026-02-05T01:46:16Z  
**内容:**

# 変更の概要
- CLIでパイプラインを実行する際、APIキーが設定されていない場合に即座にエラーを出すfail-fast機能を追加
- `validate_api_keys()`関数を追加し、パイプライン開始前にAPIキーの設定を検証
- 対応プロバイダー: openai, azure, gemini, openrouter, local

# スクリーンショット
UIの変更はありません。

# 変更の背景
現状、APIキーが設定されていないままパイプラインを実行すると、N件のAPI呼び出しを試みてから失敗していました。これはユーザー体験として良くないため、実行開始時に即座にエラーを出すようにしました。

# 関連Issue
なし（Slackでの依頼）

# 動作確認の結果
- `packages/analysis-core`のユニットテストを実行し、24件すべてパス
- 新規追加した`TestValidateApiKeys`クラスで以下のケースをテスト:
  - OpenAI APIキー未設定時にエラー
  - OpenAI APIキー設定時にパス
  - ユーザー提供APIキーでパス
  - Gemini APIキー未設定時にエラー
  - Azure環境変数未設定時にエラー
  - OpenRouter APIキー未設定時にエラー
  - localプロバイダーはAPIキー不要でパス
  - 不明なプロバイダーでエラー

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

## レビュー時の確認ポイント
- `validate_api_keys()`の検証ロジックが`services/llm.py`の各プロバイダーの要件と一致しているか
- 既存テストの`provider`を`"openai"`から`"local"`に変更した影響がないか

---
Link to Devin run: https://app.devin.ai/sessions/eda174f2d4364653ad20fd4753c5868b
Requested by: @nishio

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * 複数プロバイダ（OpenAI、Azure、Gemini、OpenRouter、Local）向けの環境変数ベースAPIキー検証を追加し、実行前にキー状態を早期検出します
  * ユーザ提供キーでの上書き対応と詳しいエラーメッセージを導入

* **Tests**
  * APIキー検証と設定検証の振る舞いを網羅するテストスイートを追加・拡張しました

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix: raise error when config key is missing during path resolution](https://github.com/digitaldemocracy2030/kouchou-ai/pull/767)

**作成者:** nishio  
**作成日:** 2026-01-26T02:08:54Z  
**変更:** +6 -1 (1ファイル)  
**マージ日:** 2026-02-05T01:40:44Z  
**内容:**

# 変更の概要
- 設定パス解決時（例: `${config.extraction.limit}`）に、キーが存在しない場合に明示的なエラーを発生させるように変更
- 従来は `dict.get(key)` を使用していたため、キーが存在しない場合は `None` が静かに返されていた
- 変更後は `WorkflowExecutionError` を発生させ、どのキーが見つからなかったか、どのパスを解決しようとしていたかを明示

# スクリーンショット
- UIの変更はありません

# 変更の背景
- 設定ミスがあった場合、`None` が静かに混入し、後段の処理で原因特定が困難になる問題があった
- 明示的なエラーを発生させることで、設定ミスを早期に検出できるようになる

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/766

# 動作確認の結果
- 既存のワークフローエンジンテスト（`tests/test_workflow_engine.py`）が全て通過することを確認
- ruff format チェックが通過することを確認

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

## レビュー時の確認ポイント
- この変更は破壊的変更の可能性があります。既存のワークフローで、存在しないキーを参照している設定がある場合、以前は `None` が渡されていたものがエラーになります
- これは意図された動作であり、設定ミスを早期に検出するための改善です

---
Link to Devin run: https://app.devin.ai/sessions/46a9282c389f43348281fa07077ad289
Requested by: @nishio

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## Bug Fixes
  * ワークフロー実行中に存在しない設定キーが参照された場合、明確なエラーメッセージが表示されるようになりました。設定の問題がより容易に特定・解決できます。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (1件)

### [docs: Azure Container Apps 移行メモを実装に合わせて更新](https://github.com/digitaldemocracy2030/kouchou-ai/pull/786)

**作成者:** nishio  
**作成日:** 2026-02-09T06:43:52Z  
**変更:** +118 -58 (1ファイル)  
**内容:**

## 何をしたか
`docs/deployment/azure-migration-20260207.md` を、実際に動作する状態まで到達した手順/対策に合わせて更新しました。

- Azure 側の移行手順を、運用者がそのまま再現できる形で整理
- 旧 `client*` から新 `public-viewer/admin/static-site-builder` への作成/secret 移設/環境変数更新/再起動/削除
- 移行後に出た `public-viewer` の起動タイムアウトと CI ヘルスチェック false negative の恒久対策を追記
  - PR #782 / #784 / #785 の内容を前提に記載

## 背景
リファクタ後は命名規約（`docs/refactoring/naming_convention.md`）に合わせて Container Apps 名も `apps/*` と揃う前提ですが、既存 Azure 環境には旧名称の Container Apps しか残っておらず、GitHub Actions/Makefile のデプロイで `... does not exist` が発生していました。

## 注意
- secret 値はドキュメント上ではマスクし、`<value>` で表記しています。


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **ドキュメント**
  * Azure マイグレーション ガイドを詳細化し、ステップバイステップの手順を追加しました。
  * 具体的なコマンド例と実行結果のサンプルを含めました。
  * トラブルシューティング セクションとマイグレーション後の検証手順を追加しました。
  * 既知の問題と実装済みの対策をドキュメント化しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

