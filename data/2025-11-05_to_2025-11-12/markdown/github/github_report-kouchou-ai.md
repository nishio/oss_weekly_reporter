# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-11-05T12:27:42.084599+09:00 から 2025-11-12T12:27:42.084599+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (0件)

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(2件)

### [静的ビルド実行前に公開状態のレポートが存在するかを検証](https://github.com/digitaldemocracy2030/kouchou-ai/pull/727)

**作成者:** NISHIO+Devin  
**作成日:** 2025-10-27T16:49:22Z  
**変更:** +84 -1 (2ファイル)  
**内容:**

# 変更の概要
- 静的ビルド実行前に公開状態のレポートが存在するかを検証するスクリプトを追加
- 公開レポートが存在しない場合に、わかりやすい日本語のエラーメッセージを表示するように改善

# スクリーンショット
N/A（UIの変更なし）

# 変更の背景
Issue #726 で報告された問題を解決するための変更です。

現状では、公開状態のレポートがない状態で静的HTML出力を実行すると、Next.jsから以下のような分かりにくいエラーメッセージが表示されていました：

```
'[Error: Page "/[slug]/opengraph-image.png" is missing "generateStaticParams()" so it cannot be used with "output: export" config.]\n'
```

このエラーメッセージでは根本原因（公開レポートがない）が分からず、ユーザーが適切に対処できない問題がありました。

# 関連Issue
Fixes #726

# 実装の詳細

## 追加ファイル
- `client/scripts/validate-reports.mjs`: レポート検証スクリプト

## 変更ファイル  
- `client/package.json`: `prebuild:static` スクリプトに検証を追加

## 検証ロジック
1. 静的エクスポートモード時のみ実行（`NEXT_PUBLIC_OUTPUT_MODE === "export"`）
2. API エンドポイント `/reports` からレポート一覧を取得
3. `status === "ready"` のレポートが存在するかをチェック
4. 存在しない場合は、詳細な日本語エラーメッセージを表示してビルドを中断

## エラーメッセージの改善点
- APIサーバー未起動時とレポート未作成時で異なるエラーメッセージを表示
- 具体的な対処方法を箇条書きで提示
- 現在のレポート数と公開レポート数を表示

# 動作確認の結果
- APIサーバー未起動時に適切なエラーメッセージが表示されることを確認
- Biomeのlintチェックが通過することを確認

**⚠️ レビュアーへの注意事項:**
- テスト環境のAPI側に既存の不具合があったため、「公開レポートがない状態でAPIが正常に動作している」というシナリオの完全な動作確認は実施できていません
- 実際の環境で公開レポートがない状態での動作確認を推奨します

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか（※今回は検証スクリプトのため単体テスト未実装）
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する

## レビュー時の重点確認項目
- [ ] 公開レポートがない状態で `make client-build-static` を実行し、わかりやすい日本語エラーメッセージが表示されることを確認
- [ ] 公開レポートが存在する状態で静的ビルドが正常に完了することを確認
- [ ] エラーメッセージの内容が適切で、ユーザーが対処方法を理解できることを確認
- [ ] API レスポンスの形式が想定と異なる場合のエラーハンドリングが適切か確認

---

**Link to Devin run:** https://app.devin.ai/sessions/edece407fde44bd8935bd2d410bfbfc8  
**Requested by:** NISHIO (@nishio) - nishio.hirokazu@gmail.com

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **新機能**
  * 静的エクスポートビルド時に、レポートの可用性を事前検証するステップを追加しました。準備完了したレポートが存在しない場合、ビルドプロセスは停止され、詳細なエラーメッセージが表示されます。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Add filesystem-based usage documentation and validation tests](https://github.com/digitaldemocracy2030/kouchou-ai/pull/722)

**作成者:** NISHIO+Devin  
**作成日:** 2025-10-23T07:46:58Z  
**変更:** +2088 -3 (24ファイル)  
**内容:**

# 変更の概要
APIサーバーを起動せずに、ファイルシステムベースでパイプラインを実行するための機能を明確化し、入出力の検証機能とテストを追加しました。

**主な追加内容:**
- ファイルシステムベース実行の包括的なドキュメント（FILESYSTEM_USAGE.md、388行）
- Pydanticによる入力CSV、設定JSON、出力JSONのスキーマ定義と検証
- CLIバリデーションオプション（`--validate-input`, `--validate-config`, `--validate-output`, `--dry-run`）
- 54個のテストケースを含む包括的なテストスイート

# スクリーンショット
UIの変更はありません（CLI機能の追加のみ）

# 変更の背景
Issue #721で指摘された通り、kouchou-aiには既にファイルシステムベースでパイプラインを実行する機能がありましたが、以下の点が不明確でした：
- 入力CSVファイルの正確な形式
- 設定JSONファイルの詳細な仕様
- 出力ファイルの構造
- バリデーション方法

この変更により、開発者やパワーユーザーがAPIサーバーなしでパイプラインを実行し、入力データの妥当性を事前に検証できるようになります。

# 関連Issue
Resolves #721

# 動作確認の結果
以下のテストを実行し、すべて成功しました：

```bash
ENV_FILE=.env.test python -m pytest tests/broadlistening/test_input_validation.py -v
# 14 passed

ENV_FILE=.env.test python -m pytest tests/broadlistening/test_config_validation.py -v  
# 20 passed

ENV_FILE=.env.test python -m pytest tests/broadlistening/test_output_validation.py -v
# 11 passed

ENV_FILE=.env.test python -m pytest tests/broadlistening/test_pipeline_e2e.py -v
# 9 passed
```

**⚠️ 重要な注意点**: 
- テストは全てスキーマ検証とファイル構造の確認のみ
- 実際のAPIキーを使用したパイプライン実行は未テスト
- 新しいCLIオプション（`--validate-*`, `--dry-run`）の動作確認は手動テストが必要

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか → ✅ 54テスト実装済み
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する

## レビュー時に特に確認してほしい点

### 1. hierarchical_main.pyの変更（高リスク）
- 72-90行目: 新しいバリデーションフラグの処理ロジック
- 98行目: `--dry-run`フラグが`--skip-interaction`と組み合わせて使われている点
- 105-117行目: dry-runモードの実装
- **確認ポイント**: 既存の実行フローを壊していないか、早期returnが適切か

### 2. スキーマ定義の妥当性
- `server/broadlistening/pipeline/schemas/config_schema.py`: 設定のデフォルト値と制約
- `server/broadlistening/pipeline/schemas/input_csv_schema.py`: CSV検証ルール
- **確認ポイント**: バリデーションが厳しすぎないか、緩すぎないか

### 3. ドキュメントの正確性
- `server/broadlistening/FILESYSTEM_USAGE.md`: 388行の包括的なドキュメント
- **確認ポイント**: 実装と一致しているか、誤解を招く記述がないか

### 4. 手動動作確認の推奨
以下のコマンドで実際に動作確認することを推奨します：
```bash
# 設定ファイルのバリデーション
python hierarchical_main.py configs/dummy-comments-japan.json --validate-config

# 入力ファイルのバリデーション  
python hierarchical_main.py configs/dummy-comments-japan.json --validate-input

# Dry-run実行
python hierarchical_main.py configs/dummy-comments-japan.json --dry-run
```

---

**Devin実行セッション**: https://app.devin.ai/sessions/3c421325d5604e71ba8e800747f59e40  
**リクエスト元**: NISHIO (nishio.hirokazu@gmail.com / @nishio)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **新機能**
  * ファイルシステムベースでのパイプライン直接実行が可能に（APIサーバー不要）
  * 設定・入力・出力の検証オプション（--validate-config、--validate-input、--validate-output）を追加
  * パイプライン実行前の確認用ドライランモード（--dry-run）を実装

* **ドキュメント**
  * ファイルシステムベースでの使用方法に関する詳細ガイドを追加

* **テスト**
  * パイプライン検証機能の包括的なテストカバレッジを追加

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

