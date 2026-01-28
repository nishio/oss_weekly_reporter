# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-01-21T12:38:36.955456+09:00 から 2026-01-28T12:38:36.955456+09:00 まで

## Issues

### 過去7日間に完了されたissue (8件)

### [[BUG]pip installして使った時、大量のDEBUGログが出る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/764)

**作成者:** nishio  
**作成日:** 2026-01-25T12:46:04Z  
**内容:**

### 概要

pip installして使った時、大量のDEBUGログが出る

pip installしていなくても同様かもしれない

### 期待する動作

デバッグ出力を精査し、デバッグ時以外の正常動作にはログを出さないのが良い

**コメント:** なし

---

### [[FEATURE]レポート生成時にタイトルと概要を必須で要求しない](https://github.com/digitaldemocracy2030/kouchou-ai/issues/752)

**作成者:** nishio  
**作成日:** 2026-01-21T07:09:21Z  
**内容:**

# 背景
あとから修正できるのに必須で要求されて手間

# 提案内容
タイトル省略時は日時、概要省略時は空文字列とする


**コメント:** なし

---

### [[FEATURE]pre-push hook にruff formatを追加する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/751)

**作成者:** nishio  
**作成日:** 2026-01-21T07:07:32Z  
**内容:**

# 背景

pushしてからCIでRuff checkエラーになる

# 提案内容

push前のhookが既に導入されているのでそこにruff formatを追加する

**コメント:** なし

---

### [[FEATURE].envとshell envが食い違っている時にその旨を表示する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/750)

**作成者:** nishio  
**作成日:** 2026-01-21T01:11:33Z  
**内容:**

# 背景
adminサーバの起動の際、.envと異なった値(特にport番号)がshell envで指定されている場合、shell envが優先される。しかしこれは暗黙的に行われるので食い違いに気付きにくい(特にshell envの設定をAIエージェントがやっていて、しかもそのことを忘れている場合)

なので.envをshell envがoverrideしている場合にその旨がサーバ起動時のメッセージで出るようにする。

# 提案内容
```
[env-check] WARNING: Shell environment variables are overriding .env file values:
  API_BASEPATH:
    .env file:    http://localhost:8000
    shell env:    http://localhost:8001 (this value is used)
  ...

To fix this, either:
  1. Unset the shell environment variables: unset API_BASEPATH NEXT_PUBLIC_API_BASEPATH
  2. Or start in a new terminal session
  3. Or explicitly set correct values when starting: API_BASEPATH=http://localhost:8000 npm run dev
```


**コメント:** なし

---

### [[FEATURE]「レポートの取得に失敗しました」を親切にする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/749)

**作成者:** nishio  
**作成日:** 2026-01-21T00:46:59Z  
**内容:**

# 提案内容
admin画面がapiサーバからの
```
>  9 |     const response = await fetch(`${getApiBaseUrl()}/admin/reports`, {
```
に失敗した時に表示される

```
レポートの取得に失敗しました
エラー：データの取得に失敗しました
Error: fetch failed to http://localhost:8000.
```
について、もう少し親切なメッセージにする。
apiサーバからレポート一覧を取得しようとしたこと、サーバにそもそも接続できてないのか(=apiサーバが起動していない、addressやportが間違っている)、接続したけどパスワード違いでrejectされたのか、など。

<img width="897" height="330" alt="Image" src="https://github.com/user-attachments/assets/55e1ae1f-7f3f-410d-b527-441814affb3b" />

**コメント:** なし

---

### [[FEATURE]JSONダウンロード](https://github.com/digitaldemocracy2030/kouchou-ai/issues/748)

**作成者:** nishio  
**作成日:** 2026-01-21T00:37:22Z  
**内容:**

# 背景
サーバで広聴AIを動かしているケースで、分析後にJSONファイルを使って「広聴AI上での可視化」以外のことを可能にする(他のBIツールと連携するなど)ために、JSONをダウンロードするAPIとメニューをつける


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

`/reports/{slug}`が今までそれに近いことをしていたが、これは内部APIであり、管理画面でレポート表示パラメータを設定可能にするにあたって設定も含まれるようになった。
これとは別に、パイプラインが出力したJSONを取得するシンプルなAPIがあるべきである。
またUIもあるのがベター。

<img width="318" height="358" alt="Image" src="https://github.com/user-attachments/assets/9dd8da79-b79c-44bf-98f5-cccd82c34c37" />

**コメント:** なし

---

### [[DOCUMENT]ドキュメントをorganizeする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/747)

**作成者:** nishio  
**作成日:** 2026-01-21T00:22:30Z  
**内容:**

# 現在の問題点
色々なファイルがあるが目次などが整備されていない

# 提案内容
よくあるOSSのドキュメントみたいなものをMkDocs Material作り、CI+GitHub Pagesで公開する


**コメント:** なし

---

### [[FEATURE] バックエンドの pandas を polars に置換する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/745)

**作成者:** 101ta28  
**作成日:** 2026-01-20T05:24:37Z  
**内容:**

# 背景
パッケージを pandas から polars にすることで、処理の高速化が見込まれるため。


# 提案内容
- polars パッケージの導入
- pandas で処理している部分を polars の記法に置き換え

**コメント:** なし

---

### 過去7日間に作成されたissue (1件)

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

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (12件)

### [fix: remove DEBUG logging configuration that causes excessive log output](https://github.com/digitaldemocracy2030/kouchou-ai/pull/765)

**作成者:** nishio  
**作成日:** 2026-01-25T12:52:37Z  
**変更:** +297 -257 (23ファイル)  
**マージ日:** 2026-01-26T01:57:15Z  
**内容:**

# 変更の概要
- `packages/analysis-core/src/analysis_core/steps/extraction.py` から `logging.basicConfig(level=logging.DEBUG)` を削除
- analysis-coreパッケージ全体にruffフォーマットを適用（インポート順序とコードスタイルの修正）

# スクリーンショット
- UIの変更はありません

# 変更の背景
pip installしてパッケージを使用した際に、大量のDEBUGログが出力される問題がありました。原因は`extraction.py`のモジュールレベルで`logging.basicConfig(level=logging.DEBUG)`が設定されていたためです。この設定はモジュールがインポートされた時点でグローバルに適用され、すべてのロガーがDEBUGレベルのメッセージを出力するようになっていました。

# 関連Issue
Fixes #764

# 動作確認の結果
- ruff check および ruff format を実行し、コードが正しくフォーマットされていることを確認
- 実際のpip install環境でのDEBUGログ出力の確認は未実施

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

## レビュー時の確認ポイント
1. `extraction.py`から`logging.basicConfig(level=logging.DEBUG)`を削除することで、他の期待されるログ動作に影響がないか確認
2. フォーマット変更は自動ツール（ruff）によるものなので、機能的な変更はありません

---
**Link to Devin run**: https://app.devin.ai/sessions/fa5ba27f20c54bb79f48ffe72fca2028
**Requested by**: @nishio

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **Refactor**
  * パイプライン設定の値解決ロジックを改善

* **Style**
  * コード全体の整形とフォーマッティングを統一

* **Tests**
  * テストコードのフォーマッティングを調整

* **Chores**
  * インポート順序を最適化
  * ロギング設定を整理

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix: Add validate_slug to all slug parameter handlers for consistent validation](https://github.com/digitaldemocracy2030/kouchou-ai/pull/763)

**作成者:** nishio  
**作成日:** 2026-01-25T04:10:56Z  
**変更:** +10 -0 (2ファイル)  
**マージ日:** 2026-01-25T07:13:37Z  
**内容:**

# 変更の概要
- 全てのslugパラメータを受け取るエンドポイントに`validate_slug()`呼び出しを追加し、一貫したバリデーションを実現
- `SLUG_PATTERN`（`r"^[A-Za-z0-9_-]+$"`）は変更せず、厳格なパターンを維持

追加されたエンドポイント:
- `get_current_step` (admin_report.py)
- `delete_report` (admin_report.py)
- `update_report_visibility` (admin_report.py)
- `update_report_config_endpoint` (admin_report.py)
- `get_clusters` (admin_report.py)
- `update_cluster_label` (admin_report.py)
- `get_visualization_config` (admin_report.py)
- `update_visualization_config` (admin_report.py)
- `report` (report.py - 公開エンドポイント)

# スクリーンショット
- UIの変更はありません

# 変更の背景
`validate_slug()`はCSV/JSONダウンロードエンドポイントでのみ呼び出されていましたが、他のslug使用箇所でも一貫して検証する必要がありました。slugはファイルシステムパスやURLに使用されるため、全てのエンドポイントで厳格なバリデーションを行うことでセキュリティを強化します。

# 関連Issue
Slackでの指摘に基づく修正

# 動作確認の結果
- `make lint/api-check`でlintチェックが通過することを確認
- `make test/api`で全169件のテストが通過することを確認

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

## レビュー時の確認ポイント
- 全てのslugを受け取るエンドポイントに`validate_slug()`が追加されているか
- `SLUG_PATTERN`が変更されていないこと（英数字・ハイフン・アンダースコアのみ許可）

---
Link to Devin run: https://app.devin.ai/sessions/db013531560049e99829b04b6fd99cad
Requested by: NISHIO (@nishio)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

## バグ修正
- レポート識別子（スラッグ）の形式検証を強化しました。複数の管理／レポート用APIでリクエスト開始時に検証を行い、許容される文字は英数字、アンダースコア、ハイフンのみに制限します。不正な識別子を含むリクエストはエラー（400）で拒否され、入力の安全性と一貫性が向上します。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [docs: polish plugin system doc](https://github.com/digitaldemocracy2030/kouchou-ai/pull/762)

**作成者:** nishio  
**作成日:** 2026-01-25T02:34:46Z  
**変更:** +66 -8 (8ファイル)  
**マージ日:** 2026-01-25T02:40:58Z  
**内容:**

書きかけだったプラグインシステムの話を執筆

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **ドキュメンテーション**
  * プラグインシステムの設計に関するドキュメントを再構成しました。各プラグインカテゴリの役割と運用上の考慮事項についての説明が改善され、より明確に理解できるようになりました。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix(admin): Add cluster settings for plugin imports](https://github.com/digitaldemocracy2030/kouchou-ai/pull/760)

**作成者:** nishio  
**作成日:** 2026-01-24T02:54:28Z  
**変更:** +14 -0 (1ファイル)  
**マージ日:** 2026-01-24T03:36:38Z  
**内容:**

## Summary

プラグイン（YouTube等）でデータをインポートした際に、クラスタ設定セクションが表示されない問題を修正しました。

CSVアップロード時と同様に、プラグインでインポート完了後にクラスタ数（Lv1/Lv2）を調整できるようになります。

## Changes

- プラグインタブでインポート完了後に `ClusterSettingsSection` を表示
- `activePluginId` と `activePluginState` を追加してプラグインの状態を追跡

## Test plan

- [x] YouTube プラグイン等でデータをインポート
- [x] インポート完了後にクラスタ設定セクションが表示されることを確認
- [x] クラスタ数を変更してレポート作成が成功することを確認

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## 新機能

* **プラグイン設定の拡張**
  * プラグイン導入時にクラスター設定が構成できるようになりました。プラグインデータに対するクラスター関連の設定オプションがUI上で利用可能になります。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat(admin): Make title and survey overview optional in report creation](https://github.com/digitaldemocracy2030/kouchou-ai/pull/759)

**作成者:** nishio  
**作成日:** 2026-01-24T02:41:23Z  
**変更:** +30 -22 (3ファイル)  
**マージ日:** 2026-01-25T02:46:40Z  
**内容:**

## Summary

Closes #752

レポート作成時にタイトルと概要を必須で要求しないようにしました。

- タイトル省略時は日時をデフォルト値として使用
- 概要省略時は空文字列を使用
- バリデーションエラーメッセージを改善し、どのフィールドに問題があるか分かりやすく表示

## Test plan

- [x] タイトルを空のままレポート作成を試み、日時がデフォルトで入ることを確認
- [x] 概要を空のままレポート作成が成功することを確認
- [ ] CSVファイル未選択時に適切なエラーメッセージが表示されることを確認

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **新機能**
  * タイトルと調査概要をオプショナルフィールドに変更
  * タイトルが未入力の場合、作成日時が自動的にタイトルとして使用されるように改善

* **改善**
  * フォーム検証メッセージをより詳細かつ具体的に改善し、ユーザーがエラーの原因を素早く特定できるように強化
  * 入力フォーム内のヘルパーテキストを拡充し、各フィールドの仕様を明確化

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat(admin): Default to Azure OpenAI when USE_AZURE=true](https://github.com/digitaldemocracy2030/kouchou-ai/pull/758)

**作成者:** nishio  
**作成日:** 2026-01-24T02:40:35Z  
**変更:** +14 -3 (2ファイル)  
**マージ日:** 2026-01-25T03:18:51Z  
**内容:**

## Summary

`NEXT_PUBLIC_USE_AZURE=true` の場合、AI プロバイダーのデフォルトを Azure OpenAI に設定します。

- `DEFAULT_PROVIDER` 定数を追加し、`NEXT_PUBLIC_USE_AZURE` をチェック
- `useState` 初期値と `resetAISettings` で `DEFAULT_PROVIDER` を使用
- Dockerfile に `NEXT_PUBLIC_USE_AZURE` の ARG/ENV を追加

## Test plan

- [ ] `NEXT_PUBLIC_USE_AZURE=true` で起動し、プロバイダーのデフォルトが Azure OpenAI になることを確認
- [ ] `NEXT_PUBLIC_USE_AZURE` 未設定で起動し、デフォルトが OpenAI のままであることを確認

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **New Features**
  * AI プロバイダーを Azure または OpenAI から選択できるようになりました。

* **Chores**
  * 静的サイトビルダーのベースパスを環境変数で設定できるように対応しました。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [chore: Add ruff check and format to pre-push hook](https://github.com/digitaldemocracy2030/kouchou-ai/pull/757)

**作成者:** nishio  
**作成日:** 2026-01-24T02:25:50Z  
**変更:** +8 -0 (1ファイル)  
**マージ日:** 2026-01-25T03:35:51Z  
**内容:**

## Summary

Closes #751

pre-push フックに ruff check と ruff format を追加し、CI でエラーになる前にローカルで検出できるようにしました。

追加内容:
- `api-ruff-check`: `rye run ruff check .` を実行
- `api-ruff-format`: `rye run ruff format . --check` を実行

## Test plan

- [ ] Python ファイルに lint エラーを含む変更を加えて push を試み、ブロックされることを確認
- [ ] フォーマット違反を含む変更を加えて push を試み、ブロックされることを確認
- [ ] 正常なコードで push が成功することを確認

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Chores**
  * コード品質検証機能を強化しました。開発者がリモートへプッシュする前に、API関連のPythonファイルに対して静的解析によるチェックを追加しました。
  * 同時に、コード整形（フォーマット）の適用有無を検証するチェックも追加し、プッシュ前の品質保証を強化しました。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat(admin): Improve error messages when API connection fails](https://github.com/digitaldemocracy2030/kouchou-ai/pull/756)

**作成者:** nishio  
**作成日:** 2026-01-24T02:18:07Z  
**変更:** +88 -19 (1ファイル)  
**マージ日:** 2026-01-25T03:51:05Z  
**内容:**

## Summary

Closes #749

管理画面でレポート取得に失敗した際のエラーメッセージを改善しました。

エラーの種類に応じて、より親切なメッセージを表示します：

- **接続エラー**: API サーバーの URL を表示し、サーバーが起動しているか確認を促す
- **401 エラー**: API キーが無効であることを示し、`NEXT_PUBLIC_ADMIN_API_KEY` の確認を促す
- **404 エラー**: API サーバーのバージョン不一致の可能性を示唆
- **500/502/503 エラー**: サーバーログの確認を促す

## Test plan

- [x] API サーバーを停止した状態で管理画面にアクセスし、接続エラーメッセージを確認
- [ ] 不正な API キーを設定して 401 エラーメッセージを確認
- [x] 正常な状態でレポート一覧が表示されることを確認

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **バグ修正**
  * エラーメッセージの表示が改善されました。API接続エラーやHTTPエラー(401、403、404、500など)に対して、より詳細で一貫性のある情報が表示されるようになりました。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat(admin): Add JSON download feature for reports](https://github.com/digitaldemocracy2030/kouchou-ai/pull/755)

**作成者:** nishio  
**作成日:** 2026-01-24T02:15:17Z  
**変更:** +247 -1 (5ファイル)  
**マージ日:** 2026-01-25T03:59:50Z  
**内容:**

## Summary

Closes #748

分析結果の JSON ファイルをダウンロードする機能を追加しました。

- `/admin/reports/{slug}/json` API エンドポイントを追加（hierarchical_result.json をダウンロード）
- admin フロントエンドに jsonDownload サーバーアクションを追加
- ActionMenu に JSON ダウンロードメニュー項目を追加（レポートステータスが ready の場合のみ表示）
- 新機能のユニットテストを追加

<img width="318" alt="menu" src="https://github.com/user-attachments/assets/9dd8da79-b79c-44bf-98f5-cccd82c34c37" />

## Test plan

- [ ] レポートの ActionMenu から「JSONをダウンロード」を選択
- [ ] hierarchical_result.json がダウンロードされることを確認
- [ ] `npm test` でユニットテストがパスすることを確認

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * レポートをJSON形式でダウンロードできる操作オプションを追加しました（準備完了のレポートに表示）。

* **Backend**
  * レポートのJSONを返す新しい管理用エンドポイントを追加しました（ダウンロード可能、パスと識別子の検証を実施）。

* **Tests**
  * フロントエンドのJSONダウンロード処理と、エンドポイントの成功・未検出・エラーケースをカバーするテストを追加しました。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [docs: Add MkDocs Material documentation site with CI/CD](https://github.com/digitaldemocracy2030/kouchou-ai/pull/754)

**作成者:** nishio  
**作成日:** 2026-01-24T02:13:34Z  
**変更:** +561 -3 (25ファイル)  
**マージ日:** 2026-01-24T03:39:16Z  
**内容:**

## Summary

Closes #747

- MkDocs Material をセットアップし、日本語対応のドキュメントサイトを構築
- docs/ ディレクトリを構造化されたディレクトリに再編成:
  - `getting-started/`: セットアップガイド (Windows/Mac/Linux)
  - `user-guide/`: 使い方、CLI、インポート、FAQ
  - `development/`: コントリビューション、プラグイン開発
  - `deployment/`: Azure、GitHub Pages デプロイ
  - `misc/`: プロジェクト一覧、CLA、提案など
- ルートレベルのMDファイルを自動コピーする `docs_hooks.py` を追加
- GitHub Pages への自動デプロイ用 GitHub Actions ワークフローを追加

## Test plan

- [ ] `pip install -r docs/requirements.txt && mkdocs serve` でローカルプレビュー確認
- [ ] main ブランチマージ後、GitHub Pages で公開確認
- [ ] リポジトリ Settings → Pages で GitHub Actions を選択

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **ドキュメント**
  * ドキュメントサイトの自動ビルドおよびデプロイワークフローを実装しました。
  * 初心者向けクイックスタート、ユーザーガイド、開発者ガイドを含む包括的なドキュメントを追加しました。
  * 日本語対応のドキュメントサイト（Material テーマ）を構築し、GitHub Pages で公開するように設定しました。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [refactor: migrate from pandas to polars for improved performance](https://github.com/digitaldemocracy2030/kouchou-ai/pull/753)

**作成者:** nishio  
**作成日:** 2026-01-23T07:18:24Z  
**変更:** +368 -276 (19ファイル)  
**マージ日:** 2026-01-25T11:40:17Z  
**内容:**

# 変更の概要
pandas から polars へのデータフレームライブラリの移行を実施しました。

主な変更点:
- `apps/api/` と `packages/analysis-core/` の両方で pandas を polars に置き換え
- pyproject.toml の依存関係を pandas から polars に変更
- DataFrame操作のAPI変換（read_csv, write_csv, join, filter, sample等）
- embeddings.pkl の保存形式を pandas DataFrame から `list[dict]` 形式に変更
- 旧形式（pandas pickle）との後方互換性を hierarchical_clustering.py に追加

## Updates since last revision
CodeRabbitのレビューコメントに基づき、以下の互換性問題を修正しました:

1. **pandas DataFrame pickle の後方互換性修正**: pandas DataFrameを直接イテレートするとカラム名が返される問題を修正。`embeddings_data["embedding"].values.tolist()` を使用するように変更
2. **embeddings と args の順序ズレ防止**: `packages/analysis-core` の hierarchical_clustering.py に arg-id ベースの並べ替えと件数一致検証を追加
3. **Argument TypedDict の comment_id フィールド追加**: `_build_arguments` 関数で TypedDict に定義された `comment_id` フィールドを設定するように修正

# スクリーンショット
UIの変更はありません。

# 変更の背景
PR #744 のアイデア（pandas→polars移行による処理速度向上）を参考に、現在のmainブランチの構造に合わせて新規実装しました。#744 は大規模なディレクトリ構造変更（#746）後のmainとコンフリクトが多いため、コンフリクト解決ではなく新規実装を選択しました。

# 関連Issue
- 参考PR: #744

# 動作確認の結果
- ruff lint チェック: パス
- CI（ruff, test）: パス
- 実際のパイプライン実行テストは未実施

**注意**: 本PRはライブラリ移行のため、実際のレポート作成パイプラインでの動作確認を推奨します。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

## レビュー時の重点確認ポイント
1. **pickle後方互換性**: `hierarchical_clustering.py` の旧pandas形式との互換処理（`embeddings_data["embedding"].values.tolist()`）が正しく動作するか
2. **arg-id順序検証**: `packages/analysis-core` の embeddings/args 順序整合性チェックが適切か
3. **join操作**: pandas `.merge()` から polars `.join()` への変換で結果が同等か
4. **実際のパイプライン実行**: レポート作成が正常に完了するか

---
Link to Devin run: https://app.devin.ai/sessions/a6c56ce15dd44a83b68bbc9faa12d0cc
Requested by: NISHIO (@nishio)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

## リリースノート

* **パフォーマンス改善**
  * データ処理基盤を刷新し、CSV入出力とバッチ処理の速度と安定性を向上しました。

* **バグ修正**
  * 不正なコメントID検出を強化し、日本語の分かりやすいエラーメッセージを追加しました。
  * 埋め込みデータの読み書きでID順序・整合性の扱いを改善しました。

* **改善**
  * 外部フォーマット互換性と出力の堅牢性を向上しました。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [安定運用したいコアと実験的な拡張を分離し、壊れにくい形に設計変更する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/746)

**作成者:** nishio  
**作成日:** 2026-01-20T23:48:34Z  
**変更:** +32227 -25379 (497ファイル)  
**マージ日:** 2026-01-23T04:02:20Z  
**内容:**

# 目的
安定運用したいコアと実験的な拡張（新しい解析手法・ビュー・入力ソース）を技術的に分離し、壊れにくい契約（API/manifest）を軸に拡張できる構造へリファクタすること。あわせて、CLI/PyPI での再利用や運用の整理（アプリ/パッケージ/プラグインの分離）を実現するのが狙い。

詳細: docs/M5_REFACTORING_PLAN.md

## 細部の変更
- リポジトリ構造の整理と命名統一
  - `server`→`apps/api`、`client`→`apps/public-viewer`、`client-admin`→`apps/admin`、`client-static-build`→`apps/static-site-builder` へ移行し、docker/CI/ドキュメントの参照を更新
  - `scripts`→`tools/scripts`、`experimental`→`experiments` へ移動
  - `pnpm-workspace.yaml` と `pnpm-lock.yaml` を追加してワークスペース化し、root の `.npmrc` を整備
- パイプラインのパッケージ化（analysis-core）
  - `packages/analysis-core` を新設し、ワークフローエンジン・互換レイヤ・CLI を実装
  - API 側は従来のパイプラインに依存せず `analysis_core` を subprocess で起動する構成に移行
  - テストや依存関係を整理
- 入力プラグイン機構の導入（API＋管理UI）
  - `apps/api/src/plugins` にプラグイン基盤（manifest/registry）を追加し、YouTube 取得プラグインを実装
  - 管理画面のレポート作成 UI にプラグインタブを追加し、検証・プレビュー・インポートのフローを統合
- 可視化プラグイン＋可視化設定の整備
  - `apps/public-viewer` にチャートのプラグインレジストリを導入（scatter/treemap/階層リスト）し、動的な表示切り替えに対応
  - `visualizationConfig` のスキーマと API を追加し、管理画面に可視化設定ダイアログを実装
  - 公開画面は設定値を優先し、既存の既定挙動と互換性を維持
- CI/運用・Docker/Azureの更新
  - GitHub Actions を pnpm 前提に変更し、パスやビルドコマンドを新構成に合わせて更新
  - `compose.yaml` と Azure デプロイのコンテナ名・ビルドパスを新しいアプリ構成に揃えた
  - `.dockerignore` を新規追加し、ビルド対象を整理
- ドキュメントと計画の追加・更新
  - `docs/PLUGIN_GUIDE.md` などプラグイン関連のドキュメントを拡充
  - `M5_REFACTORING_PLAN.md`、`M5_PLUGIN_SYSTEM_PLAN.md` など計画・背景文書を追加し、方向性を明文化

# スクリーンショット
> `apps/public-viewer` にチャートのプラグインレジストリを導入（scatter/treemap/階層リスト）し、動的な表示切り替えに対応
https://gyazo.com/af56999b44a99ee8e1497158086cdabe][https://gyazo.com/43ddac15c0ab52f89a54eb60512a9832

>`apps/api/src/plugins` にプラグイン基盤（manifest/registry）を追加し、YouTube 取得プラグインを実装

<img width="1000" height="331" alt="image" src="https://github.com/user-attachments/assets/81a5fbeb-9b16-4726-8308-71932b91d3e3" />

# 動作確認の結果

Result: All 167 tests now pass

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [x] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

**コメント:** なし

---

### 過去7日間に作成されたPR (6件)

### [feat: public-viewer の API 接続エラー時にわかりやすいメッセージを表示](https://github.com/digitaldemocracy2030/kouchou-ai/pull/771)

**作成者:** nishio  
**作成日:** 2026-01-26T14:16:35Z  
**変更:** +152 -31 (5ファイル)  
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

## リリースノート

* **新機能**
  * API接続エラー時の表示が改善されました。エラーの詳細情報、接続先URL、考えられる原因などが表示されるようになります。

* **リファクタ**
  * エラーハンドリングロジックが統一されました。複数のページにおけるエラー表示の実装が一元化されます。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [docs: why-pnpm刷新とプラグイン出力仕様の整理](https://github.com/digitaldemocracy2030/kouchou-ai/pull/770)

**作成者:** nishio  
**作成日:** 2026-01-26T13:20:08Z  
**変更:** +323 -19 (3ファイル)  
**内容:**

# 変更の概要
- why-pnpm の説明を刷新し、hoisting問題とプラグイン運用の必然性を明確化
- 入力プラグイン/分析プラグインの出力データ構造を新規ドキュメント化
- 上記ドキュメントをMkDocsナビに追加

# スクリーンショット
- なし（ドキュメントのみ）

# 変更の背景
- プラグインシステム導入にあたり、pnpm採用理由とデータ構造の契約を読者に明確に伝えるため

# 関連Issue
- なし

# 動作確認の結果
- 未実施（ドキュメントのみ）

# CLAへの同意
- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

## リリースノート

* **Documentation**
  * プラグイン出力データ構造に関する開発者向けドキュメントを新規追加しました（出力フォーマットや必須/任意列、欠落値の扱いなどを明記）。
  * 開発ツール選定に関する文書を再構成・拡充し、プラグインの独立性やホイスティング問題への対応理由を明確化しました。
  * 開発者向けナビゲーションに新規ドキュメントを追加しました。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Add report duplication plan](https://github.com/digitaldemocracy2030/kouchou-ai/pull/769)

**作成者:** nishio  
**作成日:** 2026-01-26T07:34:36Z  
**変更:** +167 -0 (1ファイル)  
**内容:**

## Summary
- add detailed plan for report duplication/reuse with API/UI flow, reuse strategy, and rollout

## Testing
- not run (doc-only)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

# リリースノート

このPRは計画ドキュメントの追加のみであり、エンドユーザーに対する直接的な機能変更を含みません。

**適用可能なカテゴリーはありません。**

※ 今後の実装段階でレポート複製機能がリリースされる際に、詳細なリリースノートを提供予定です。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat: CLI使用時に.envの設定不良をfail-fastする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/768)

**作成者:** nishio  
**作成日:** 2026-01-26T02:14:01Z  
**変更:** +162 -8 (3ファイル)  
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

### [docs/mkdocs 747](https://github.com/digitaldemocracy2030/kouchou-ai/pull/761)

**作成者:** nishio  
**作成日:** 2026-01-24T17:14:26Z  
**変更:** +66 -8 (8ファイル)  
**内容:**

- Add MkDocs Material documentation site with CI/CD
- Add documentation for pnpm adoption
- Add cluster settings for plugin imports
- fix: Update mkdocs-material to >=9.7.1 for security fixes
- fix: Add language tag to code fence (MD040)
- docs: polish plugin system doc


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **ドキュメント**
  * プラグインシステムの設計根拠に関する詳細なドキュメントを整備しました。コアコンポーネントの責務分離、プラグインの分類、および運用上の考慮事項についての構造化された説明を提供します。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(2件)

### [バックエンドの pandas を polars に変更](https://github.com/digitaldemocracy2030/kouchou-ai/pull/744)

**作成者:** 101ta28  
**作成日:** 2026-01-20T03:14:22Z  
**変更:** +298 -213 (11ファイル)  
**内容:**

close #745 

# 変更の概要
- server 側の DataFrame 処理（スプレッドシート取込・レポート入力保存・パイプライン各ステップ）を pandas から polars へ移行し、`pyproject.toml` の依存を polars に置き換えました。
- パイプライン各ステップ（extraction/embedding/hierarchical_*）は polars 用 API で再実装し、CSV/PKL の入出力や NaN 取扱いを polars ベースに統一しました。
- `hierarchical_initial_labelling.py` では polars 変換に伴う `cluster_id` 非存在時の例外を防ぐため、列存在チェックを追加しました。

# スクリーンショット
- UI 変更はありません。

# 変更の背景
- pandas から polars に一本化し、処理速度やメモリ効率の改善と依存関係の簡素化を図るため。

# 動作確認の結果
- `python server/broadlistening/pipeline/hierarchical_main.py configs/<slug>.json --skip-interaction --without-html` を実行し、各ステップが polars ベースで正常に完了することを確認しました。
- extraction や embedding の処理速度が向上しました。

## pandas実装でのログ
```md
[2026-01-20T02:07:30.434587] Pipeline started (force=False, only=None)
[2026-01-20T02:07:30.434656] Execution plan: extraction -> not trace of previous run, embedding -> not trace of previous run, hierarchical_clustering -> not trace of previous run, hierarchical_initial_labelling -> not trace of previous run, hierarchical_merge_labelling -> not trace of previous run, hierarchical_overview -> not trace of previous run, hierarchical_aggregation -> not trace of previous run, hierarchical_visualization (skip: skipping html output)
[2026-01-20T02:07:30.491381] Step 'extraction' started
[2026-01-20T02:08:00.566242] Step 'extraction' completed in 30.07s (token_usage=219804, cost=$0.0386)
[2026-01-20T02:08:00.566657] Step 'embedding' started
[2026-01-20T02:09:54.465461] Step 'embedding' completed in 113.90s (token_usage=0, cost=$0.0386)
[2026-01-20T02:09:54.470881] Step 'hierarchical_clustering' started
[2026-01-20T02:10:17.690810] Step 'hierarchical_clustering' completed in 23.22s (token_usage=0, cost=$0.0386)
[2026-01-20T02:10:17.691584] Step 'hierarchical_initial_labelling' started
[2026-01-20T02:10:25.716891] Step 'hierarchical_initial_labelling' completed in 8.03s (token_usage=41476, cost=$0.0477)
[2026-01-20T02:10:25.717396] Step 'hierarchical_merge_labelling' started
[2026-01-20T02:10:29.967746] Step 'hierarchical_merge_labelling' completed in 4.25s (token_usage=15450, cost=$0.0505)
[2026-01-20T02:10:29.968368] Step 'hierarchical_overview' started
[2026-01-20T02:10:33.520297] Step 'hierarchical_overview' completed in 3.55s (token_usage=1518, cost=$0.0508)
[2026-01-20T02:10:33.525990] Step 'hierarchical_aggregation' started
[2026-01-20T02:10:33.629066] Step 'hierarchical_aggregation' completed in 0.10s (token_usage=0, cost=$0.0508)
[2026-01-20T02:10:33.629110] Skipping step 'hierarchical_visualization' (skipping html output)
[2026-01-20T02:10:33.629686] Pipeline completed successfully in 183.19s
```

## polars実装でのログ
```md
[2026-01-20T02:46:20.192634] Pipeline started (force=False, only=None)
[2026-01-20T02:46:20.192672] Execution plan: extraction -> not trace of previous run, embedding -> not trace of previous run, hierarchical_clustering -> not trace of previous run, hierarchical_initial_labelling -> not trace of previous run, hierarchical_merge_labelling -> not trace of previous run, hierarchical_overview -> not trace of previous run, hierarchical_aggregation -> not trace of previous run, hierarchical_visualization (skip: skipping html output)
[2026-01-20T02:46:20.194132] Step 'extraction' started
[2026-01-20T02:46:44.269107] Step 'extraction' completed in 24.07s (token_usage=219789, cost=$0.0386)
[2026-01-20T02:46:44.269520] Step 'embedding' started
[2026-01-20T02:48:32.488457] Step 'embedding' completed in 108.22s (token_usage=0, cost=$0.0386)
[2026-01-20T02:48:32.493790] Step 'hierarchical_clustering' started
[2026-01-20T02:48:55.816983] Step 'hierarchical_clustering' completed in 23.32s (token_usage=0, cost=$0.0386)
[2026-01-20T02:48:55.817834] Step 'hierarchical_initial_labelling' started
[2026-01-20T02:49:02.517996] Step 'hierarchical_initial_labelling' completed in 6.70s (token_usage=41416, cost=$0.0477)
[2026-01-20T02:49:02.522667] Step 'hierarchical_merge_labelling' started
[2026-01-20T02:49:06.590521] Step 'hierarchical_merge_labelling' completed in 4.07s (token_usage=15159, cost=$0.0505)
[2026-01-20T02:49:06.594908] Step 'hierarchical_overview' started
[2026-01-20T02:49:10.318800] Step 'hierarchical_overview' completed in 3.72s (token_usage=1597, cost=$0.0508)
[2026-01-20T02:49:10.324562] Step 'hierarchical_aggregation' started
[2026-01-20T02:49:10.348322] Step 'hierarchical_aggregation' completed in 0.02s (token_usage=0, cost=$0.0508)
[2026-01-20T02:49:10.348372] Skipping step 'hierarchical_visualization' (skipping html output)
[2026-01-20T02:49:10.349008] Pipeline completed successfully in 170.16s
```

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

* **リファクタリング**
  * 全体的にデータ処理基盤をpandasからpolarsへ移行し、入出力と処理効率を改善
  * 埋め込みやクラスタリング、抽出〜集約〜ラベリングの各処理をpolarsベースで統一
  * スプレッドシート/レポート出力のCSV処理と列操作をpolarsに更新

* **バグ修正 / 安定性**
  * 埋め込み読み込みの形式検証、不整合検出、空結果や例外処理を強化

* **その他**
  * ビルド・依存設定を整理・拡充

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Bump qs from 6.14.0 to 6.14.1 in /client](https://github.com/digitaldemocracy2030/kouchou-ai/pull/743)

**作成者:** dependabot[bot]  
**作成日:** 2026-01-05T01:09:41Z  
**変更:** +3 -3 (1ファイル)  
**内容:**

Bumps [qs](https://github.com/ljharb/qs) from 6.14.0 to 6.14.1.
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/ljharb/qs/blob/main/CHANGELOG.md">qs's changelog</a>.</em></p>
<blockquote>
<h2><strong>6.14.1</strong></h2>
<ul>
<li>[Fix] ensure arrayLength applies to <code>[]</code> notation as well</li>
<li>[Fix] <code>parse</code>: when a custom decoder returns <code>null</code> for a key, ignore that key</li>
<li>[Refactor] <code>parse</code>: extract key segment splitting helper</li>
<li>[meta] add threat model</li>
<li>[actions] add workflow permissions</li>
<li>[Tests] <code>stringify</code>: increase coverage</li>
<li>[Dev Deps] update <code>eslint</code>, <code>@ljharb/eslint-config</code>, <code>npmignore</code>, <code>es-value-fixtures</code>, <code>for-each</code>, <code>object-inspect</code></li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/ljharb/qs/commit/3fa11a5f643c76896387bd2d86904a2d0141fdf7"><code>3fa11a5</code></a> v6.14.1</li>
<li><a href="https://github.com/ljharb/qs/commit/a62670423c1ccab0dd83c621bfb98c7c024e314d"><code>a626704</code></a> [Dev Deps] update <code>npmignore</code></li>
<li><a href="https://github.com/ljharb/qs/commit/3086902ecf7f088d0d1803887643ac6c03d415b9"><code>3086902</code></a> [Fix] ensure arrayLength applies to <code>[]</code> notation as well</li>
<li><a href="https://github.com/ljharb/qs/commit/fc7930e86c2264c1568c9f5606830e19b0bc2af2"><code>fc7930e</code></a> [Dev Deps] update <code>eslint</code>, <code>@ljharb/eslint-config</code></li>
<li><a href="https://github.com/ljharb/qs/commit/0b06aac566abee45ef0327667a7cc89e7aed8b58"><code>0b06aac</code></a> [Dev Deps] update <code>@ljharb/eslint-config</code></li>
<li><a href="https://github.com/ljharb/qs/commit/64951f6200a1fb72cc003c6e8226dde3d2ef591f"><code>64951f6</code></a> [Refactor] <code>parse</code>: extract key segment splitting helper</li>
<li><a href="https://github.com/ljharb/qs/commit/e1bd2599cdff4c936ea52fb1f16f921cbe7aa88c"><code>e1bd259</code></a> [Dev Deps] update <code>@ljharb/eslint-config</code></li>
<li><a href="https://github.com/ljharb/qs/commit/f4b3d39709fef6ddbd85128d1ba4c6b566c4902e"><code>f4b3d39</code></a> [eslint] add eslint 9 optional peer dep</li>
<li><a href="https://github.com/ljharb/qs/commit/6e94d9596ca50dffafcef40a5f64eca89962cf34"><code>6e94d95</code></a> [Dev Deps] update <code>eslint</code>, <code>@ljharb/eslint-config</code>, <code>npmignore</code></li>
<li><a href="https://github.com/ljharb/qs/commit/973dc3c51c86da9f4e30edeb4b1725158d439102"><code>973dc3c</code></a> [actions] add workflow permissions</li>
<li>Additional commits viewable in <a href="https://github.com/ljharb/qs/compare/v6.14.0...v6.14.1">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=qs&package-manager=npm_and_yarn&previous-version=6.14.0&new-version=6.14.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>Dependabot commands and options</summary>
<br />

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating it. You can achieve the same result by closing it manually
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/digitaldemocracy2030/kouchou-ai/network/alerts).

</details>

**コメント:** なし

---

