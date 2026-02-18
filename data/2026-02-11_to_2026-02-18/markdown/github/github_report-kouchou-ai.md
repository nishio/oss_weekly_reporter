# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-02-11T12:54:09.825734+09:00 から 2026-02-18T12:54:09.825734+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (0件)

### 過去7日間に作成されたPR (2件)

### [Increase analysis-core timeout defaults to 300 seconds](https://github.com/digitaldemocracy2030/kouchou-ai/pull/795)

**作成者:** nishio  
**作成日:** 2026-02-16T12:22:25Z  
**変更:** +48 -17 (3ファイル)  
**内容:**

# 変更の概要
- analysis-core の LLM リクエストタイムアウト既定値を 300 秒に引き上げました
- `hierarchical_overview` で使う LLM リクエストに 300 秒タイムアウトを明示的に指定しました
- `extraction` のバッチ待機タイムアウトを 300 秒に変更し、`config["extraction"]["timeout_seconds"]` で上書き可能にしました

# スクリーンショット
- UI変更なし

# 変更の背景
- `hierarchical_overview` で `Request timed out.` が発生し、分析パイプライン全体が失敗するケースが継続的に発生していました
- 既存の 30 秒タイムアウトでは外部 LLM 応答遅延時に失敗しやすいため、分析系のタイムアウトを 300 秒へ統一しました
- レポートの再利用によって今までのようにextractionからスタートしないケースが増えたため、後半のLLM呼び出しでcold startを踏むケースが増えたのだと思われます

# 関連Issue
- なし

# 動作確認の結果
- `python3 -m py_compile packages/analysis-core/src/analysis_core/services/llm.py packages/analysis-core/src/analysis_core/steps/extraction.py packages/analysis-core/src/analysis_core/steps/hierarchical_overview.py`
  - 成功
- `python3 -m ruff check ...`
  - 実行環境に `ruff` が未インストールのため未実施

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **新機能**
  * LLM関連リクエストに共通のタイムアウト設定を導入しました。デフォルトは300秒で、抽出処理や階層的概要生成を含むすべてのAI呼び出しで一貫して適用されます。長時間処理やローカル/外部プロバイダ間でのタイムアウト挙動が統一され、設定可能になりました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [docs: add plan for llm grouping and capability auto-detection](https://github.com/digitaldemocracy2030/kouchou-ai/pull/794)

**作成者:** nishio  
**作成日:** 2026-02-12T06:58:07Z  
**変更:** +275 -0 (1ファイル)  
**内容:**

## Summary\n- add initial implementation plan document for LLM grouping and capability auto-detection\n- clarify short-term compatibility approach and long-term capability-driven visualization gating\n\n## Notes\n- this PR is intended as a base branch to stack follow-up commits\n- unrelated local files are intentionally excluded\n

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **Documentation**
  * AI搭載オピニオングループ化機能の今後の計画書を追加。今後の開発ロードマップを定義します。

**注:** この変更は内部計画ドキュメントであり、ユーザー向けの機能変更は含まれていません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

