# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-06-24T13:37:55.066142+09:00 から 2026-07-01T13:37:55.066142+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (0件)

### 過去7日間に作成されたPR (1件)

### [docs: Web UI の Node runtime 依存インベントリを追加 (#885)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/903)

**作成者:** yasumorishima  
**作成日:** 2026-06-27T09:38:54Z  
**変更:** +113 -0 (1ファイル)  
**内容:**

## 概要

#885 の完了条件 第1項「Web UI の runtime Node 依存一覧のドキュメント化」に向けて、current `main` を精読し、`apps/admin` / `apps/public-viewer` / `apps/static-site-builder` の Node.js runtime 依存を棚卸しした docs を追加します。

- 追加: `docs/development/web-ui-node-runtime-dependencies.md`（`mkdocs.yml` は `nav:` 明示なし＝自動ナビなので追加だけで反映されます）
- **ドキュメントのみの変更で、挙動への影響はありません。**

## 主な発見

- **admin**: Node runtime 依存はほぼ「FastAPI への薄い proxy（Server Action 15本）」と「static export 阻害設定」だけ。Node 固有処理（ファイル生成 / zip / build）は 0。
- **public-viewer**: 既に `NEXT_PUBLIC_OUTPUT_MODE=export` モードを持ち、runtime の Node 依存（ISR / `connection()` / server fetch）は export ビルドで build 時処理に倒れて解決済み。残るのは「export ビルド自体に Node + Next + API 到達が必要」という build 時依存のみ。
- **static-site-builder**: ⭐ 単一exe化の最大の障壁。`POST /build` のたびに runtime で `next build`（`pnpm run build:static`）を子プロセス実行し、生成した `out/` を zip 返却する設計。「静的ファイルを生成する行為そのもの」が runtime の Node/Next build に依存しています。

## ひとつ伺いたい設計判断

admin の Server Action 14本は既に `NEXT_PUBLIC_ADMIN_API_KEY`（client 露出可）+ `getApiBaseUrl()` を使うだけの proxy なので、`"use server"` を外せば機械的に client fetch 化できます。ただしこれは **standalone（hosted）モードのネットワークモデルも「ブラウザ→Next サーバ経由」から「ブラウザ→FastAPI 直 + CORS」へ変える**ことを意味します。

- **(A)** export / local desktop モードのみ client 直叩きにし、standalone は現状の Server Action proxy を維持（モード分岐を持つ）
- **(B)** 両モードとも client 直叩きに寄せて Server Action を廃し、hosted では FastAPI 側に CORS / 認証を持たせる

どちらの方針が好ましいでしょうか。これが決まれば prototype（admin の export 化）を進めます。`ADMIN_API_KEY`（真にサーバ専用）を使う `duplicateReport` と `config` route handler だけは、local desktop の threat model（client にキーを載せてよいか）を別途決める必要があります。

## 補足

- 配置パス・粒度・ファイル名はご希望に合わせて調整します（不要であれば close いただいて構いません）。


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Documentation**
  * Added a new reference documenting Node.js runtime dependencies across the web UI apps.
  * Clarified which apps still rely on build-time Node.js tasks versus those that can run without runtime Node.js.
  * Summarized current blockers and next steps for moving toward export-based builds and simpler deployment.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [[codex] 混在型の入力CSV属性を文字列として扱う](https://github.com/digitaldemocracy2030/kouchou-ai/pull/897)

**作成者:** 101ta28  
**作成日:** 2026-06-05T07:16:48Z  
**変更:** +71 -9 (8ファイル)  
**内容:**

## 概要
- analysis-core で入力CSVを検証・読み込みする際、ユーザー入力由来の列を文字列として扱うようにしました。
- API が生成する入力CSVについて、動的な属性列を含めて文字列スキーマで保存するようにしました。
- 数値のような値と文字列ラベルが混在する属性列の回帰テストを追加しました。

## 原因
属性列の先頭付近だけを見ると Polars が数値型として推定することがあり、その後に文字列カテゴリが現れるとCSV読み込みに失敗していました。この失敗が、分析開始前の入力CSVヘッダー読み込みエラーとして表示されていました。

## 影響
今後、カテゴリ属性列に数値風の値と文字列ラベルが混在するCSVでも、入力検証・抽出・集約処理を継続できるようになります。

## 検証
- `docker compose exec -T api pytest tests/services/test_report_launcher.py tests/services/test_report_duplicate.py tests/routers/test_get_current_step.py -q`
- `docker compose run --rm -T -v "${PWD}/packages/analysis-core:/packages/analysis-core" api sh -lc 'uv pip install --system -e "/packages/analysis-core[clustering]" && pytest /packages/analysis-core/tests -q --ignore=/packages/analysis-core/tests/e2e'`
- `docker compose run --rm -T -v "${PWD}/packages/analysis-core:/packages/analysis-core" api sh -lc 'uv pip install --system -e "/packages/analysis-core[dev]" && ruff check /packages/analysis-core/src/analysis_core/core/orchestration.py'`
- `git diff --check`

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Improved handling of mixed-type data in CSV input files, ensuring consistent column type preservation for categorical and metadata fields.

* **Tests**
  * Added test coverage for validating proper CSV serialization with mixed-type columns and attribute values.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

