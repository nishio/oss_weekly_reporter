# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-06-03T13:36:06.875536+09:00 から 2026-06-10T13:36:06.875536+09:00 まで

## Issues

### 過去7日間に完了されたissue (1件)

### [[BUG] レポート生成しようとすると Hierarchical clustering requires the optional 'clustering' dependencies. というエラーが出る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/894)

**作成者:** shingo-ohki  
**作成日:** 2026-06-05T05:37:48Z  
**内容:**

### 概要
サンプルCSVファイルを使ってレポート生成を行おうとすると以下のエラーが出力される
<!-- バグの簡潔な説明をお願いします -->
```
Step 'clustering' failed: Hierarchical clustering requires the optional 'clustering' dependencies. Install with: pip install 'kouchou-ai-analysis-core[clustering]'
```

### 再現手順

1. docker-compose up
2. http://localhost:4000/ からサンプルCSVでレポート生成

### 期待する動作

エラー無くレポートが生成される
<!-- 本来どう動作すべきかを記入してください -->

### スクリーンショット・ログ

<img width="701" height="850" alt="Image" src="https://github.com/user-attachments/assets/392f1e9c-59af-43a2-b342-0c00b68f1ab4" />

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->

**コメント:** なし

---

### 過去7日間に作成されたissue (1件)

### [[BUG] aarch64 環境で、クラスタリング処理の途中で実行時エラーになる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/898)

**作成者:** shingo-ohki  
**作成日:** 2026-06-05T07:56:36Z  
**内容:**

### 概要

aarch64 環境で、クラスタリング処理の途中で実行時エラーになる（Azure デモ環境 x86_64 環境では問題ない）


<!-- バグの簡潔な説明をお願いします -->

### 再現手順

1. aarch64環境（例えば Apple sillicon の macOS) で手順通り docker-compose up
2. レポート生成

### 期待する動作

エラーなくレポートが生成される
<!-- 本来どう動作すべきかを記入してください -->

### スクリーンショット・ログ

<img width="1023" height="531" alt="Image" src="https://github.com/user-attachments/assets/fb92ba37-25ea-44b1-a4ec-eaf390d00b91" />

<img width="808" height="387" alt="Image" src="https://github.com/user-attachments/assets/77faf7a2-91e6-44ac-bbe7-de4e372136d5" />

### その他

AIはこう言っているけど、この対応が適切なのかどうか...
```
環境依存で落ちる実装
これは「コードのバグ」というより、aarch64 環境で umap がそのままでは落ちる、という実行環境依存の問題でした。
今回の検証では、api コンテナ内で NUMBA_DISABLE_JIT=1 を付けると import umap が通り、さらに UMAP 経路のクラスタリング本体も成功しています。
なので、少なくとも今回の macOS Apple Silicon 環境については、コード修正ではなくセットアップ手順の調整で吸収できる可能性が高いです。
```
<!-- 追加で伝えておきたいことがあれば記入してください -->

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (4件)

### [[codex] aarch64 Docker向けに Numba CPU target を generic にする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/899)

**作成者:** nishio  
**作成日:** 2026-06-05T12:07:44Z  
**変更:** +5 -0 (4ファイル)  
**マージ日:** 2026-06-05T22:45:43Z  
**内容:**

## 概要

Refs #898

ローカル Docker の API コンテナで、Numba JIT の CPU target を `generic` に固定します。

- `compose.yaml` で `NUMBA_CPU_NAME=${NUMBA_CPU_NAME:-generic}` を API service に渡す
- `.env.example` に `NUMBA_CPU_NAME=generic` を追加
- `setup_mac.sh` / `setup_linux.sh` が生成する `.env` に同じ設定を追加

## 背景

issue #898 では、aarch64 環境の Docker コンテナ内で `import umap` 自体が `Illegal instruction` で落ちています。`NUMBA_DISABLE_JIT=1` で回避する案もありますが、これは JIT を丸ごと無効化するため、まずは JIT を有効にしたまま LLVM の CPU target だけを保守的にする方針にしています。

UMAP やクラスタリング処理の実装は変更していません。

## aarch64 実機確認について

この PR は **aarch64 環境の人に試してもらう必要があります**。

手元では Linux/aarch64 Docker コンテナ内の再現確認ができていません。確認したいことは、Apple Silicon などの aarch64 環境で `docker compose up --build` 後にレポート生成を実行し、クラスタリング開始時の `import umap` / `Illegal instruction` が解消するかです。

期待する確認観点:

- API コンテナ内で `NUMBA_CPU_NAME=generic` が設定されていること
- `python -c "import numba; print(numba.config.CPU_NAME); import umap; print(umap.UMAP)"` が `generic` を表示して成功すること
- issue #898 の再現手順でレポート生成がクラスタリング以降へ進むこと

## 確認済み

- `bash -n setup_mac.sh setup_linux.sh`
- `git diff --check`
- macOS arm64 の既存 venv で `NUMBA_CPU_NAME=generic` が Numba に読まれ、`import umap` が成功すること

## 未確認

- Linux/aarch64 Docker コンテナ内での再現・解消確認
- 実際の `docker compose up --build` からのレポート生成完走確認

上記が残っているため draft PR としています。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Chores**
  * Added `NUMBA_CPU_NAME` environment variable to setup scripts and Docker configuration (defaults to `generic` for broad system compatibility).

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[codex] 混在型の入力CSV属性を文字列として扱う](https://github.com/digitaldemocracy2030/kouchou-ai/pull/897)

**作成者:** 101ta28  
**作成日:** 2026-06-05T07:16:48Z  
**変更:** +71 -9 (8ファイル)  
**マージ日:** 2026-06-05T07:53:25Z  
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

### [[codex] API Docker の analysis-core 依存検証を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/896)

**作成者:** nishio  
**作成日:** 2026-06-05T06:57:46Z  
**変更:** +117 -1 (4ファイル)  
**マージ日:** 2026-06-05T07:52:35Z  
**内容:**

## 概要

- API Dockerfile の `analysis-core` install を `/packages/analysis-core[full]` に固定しました。
- `apps/api/tests/test_dockerfile_dependencies.py` を追加し、`analysis-core` の `full` extra が pipeline に必要な optional groups を含むことと、API Dockerfile が quote 付きで `full` extra を install することを検証します。
- `server-pytest.yml` の path filter に `apps/api/Dockerfile` を追加し、Dockerfile 変更時にも contract test が走るようにしました。
- `API Docker Dependency Smoke` workflow を追加し、Dockerfile / dependency manifest 変更時だけ API image を build して、container 内で clustering / embeddings / gemini 関連 import を smoke します。

## 背景

PR #895 で、`analysis-core` の clustering 依存が optional extras 化された後も API Dockerfile が extras なしで local package を install していたことが分かりました。既存 CI は dev lock / all-features 前提で依存が揃うため、この Docker image 固有の差分を検知できていませんでした。

この PR は #895 と同じ Dockerfile の 1 行修正を含みつつ、同じ退行を CI で落とす検証を追加します。

## 確認

- `ADMIN_API_KEY=dummy PUBLIC_API_KEY=dummy OPENAI_API_KEY=dummy uv run --with pytest --with fastapi --with pydantic-settings --with python-dotenv --with httpx python -m pytest tests/test_dockerfile_dependencies.py -q`
- `uv run --with ruff ruff check tests/test_dockerfile_dependencies.py`
- `uv run --with ruff ruff format --check tests/test_dockerfile_dependencies.py`
- workflow YAML parse と `run:` block の `bash -n` 構文チェック

実 Docker build / container import smoke は、この PR の `API Docker Dependency Smoke` workflow で確認します。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Chores**
  * Added automated validation for API Docker image dependencies
  * Extended server test triggers to include API Dockerfile changes
  * Updated API Docker build configuration to include additional optional dependencies

* **Tests**
  * Added validation tests for API Docker dependency installation

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix: API Dockerfileでanalysis-coreのclustering依存をインストールするよう修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/895)

**作成者:** Devin AI+Devin  
**作成日:** 2026-06-05T06:17:08Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2026-06-05T07:04:20Z  
**内容:**

# 変更の概要
- `apps/api/Dockerfile`で`analysis-core`パッケージをインストールする際、`/packages/analysis-core` → `"/packages/analysis-core[full]"` に変更し、clustering用オプション依存（scikit-learn, scipy, umap-learn, numba）が含まれるようにした。

# スクリーンショット
- UIの変更なし

# 変更の背景
コミット `0b720f3b`（"Split analysis-core optional dependencies into extras"）で、clustering依存がbase依存からオプション extras `[clustering]` に分離されたが、Dockerfileは更新されなかった。その結果、Docker環境でパイプラインを実行するとクラスタリングステップで以下のエラーが発生するようになった：

```
Step 'clustering' failed: Hierarchical clustering requires the optional 'clustering' dependencies.
Install with: pip install 'kouchou-ai-analysis-core[clustering]'
```

## 既存テストで検出できなかった理由

1. **CIテストは`requirements-dev.lock`でインストール** — このlockfileは`all-features: true`で生成されており、clustering依存が常に含まれる。CIではエラーが再現しない。
2. **`test_hierarchical_clustering.py`** — `calculate_recommended_cluster_nums`のみテストしており、UMAP/scipy/sklearnの実際のimportは不要。
3. **`test_llm_grouping.py`** — `_load_clustering_dependencies`をmonkeypatchで`FakeUMAP`に差し替えており、実際のimportをテストしていない。
4. **`test_imports.py`** — lazy importのテストのみで、Dockerイメージに依存が含まれているかは検証対象外。
5. **Dockerビルドのインテグレーションテストが存在しない** — 実際のDockerイメージで全依存が揃っていることを検証するテストがない。

要約すると、テスト環境では常に全依存がインストールされており、Dockerfileでの`[full]`指定漏れはテストで検出できない構造だった。

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/894

# 動作確認の結果
- Dockerfileの変更差分を確認し、`uv pip install`に渡されるパス指定が`"/packages/analysis-core[full]"`になっていることを確認。
- `[full]`エクストラは`pyproject.toml`で`[gemini,embeddings,clustering]`に展開されるため、clustering依存（scikit-learn, scipy, umap-learn, numba）が含まれる。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


Link to Devin session: https://app.devin.ai/sessions/42313eb582eb45e2b9dfcfdb001da682
Requested by: @nishio

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

