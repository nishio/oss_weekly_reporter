# 広聴AI 2/25~3/4 のGitHub活動まとめ

この一週間（2026-02-25～2026-03-04）における「広聴AI (kouchou-ai)」リポジトリの開発活動をまとめます。興味を持たれた方はぜひIssueやPRをのぞいてみてください！

---

## 今週完了した内容（マージ済みPR）

### 1. [PR #812](https://github.com/digitaldemocracy2030/kouchou-ai/pull/812)  
- **タイトル**: feat: 散布図のデータポイントホバー時にクラスタラベルを非表示にする  
- **実装者**: tokoroten  
- **概要**:
  - Plotlyの散布図において、マウスホバー時に該当クラスタのラベル（アノテーション）を一時的に消すことで、ホバーしたポイントが見えやすくなる機能を追加しました。  
  - 別クラスタにマウスを移動するとラベルは戻り、新たにホバーしたクラスタのラベルが一時的に消える設計です。マウスが散布図外に離れた際は全ラベルが復帰します。

### 2. [PR #811](https://github.com/digitaldemocracy2030/kouchou-ai/pull/811)  
- **タイトル**: refactor: 属性フィルタロジックの統合とstale closureバグ修正  
- **実装者**: tokoroten  
- **概要**:
  - 属性フィルタに関連する重複ロジックを1つのユーティリティファイルへ統合し、メンテナンス性を向上。  
  - フィルタ結果をメモ化して再計算を抑制する実装に変更することで、不要な再レンダリングを削減。  
  - コードの簡素化とバグ修正（stale closure）による安定性向上が図られました。

### 3. [PR #808](https://github.com/digitaldemocracy2030/kouchou-ai/pull/808)  
- **タイトル**: fix: override minimatch to ^10.2.1 to fix CVE-2026-26996 (ReDoS)  
- **実装者**: shingo-ohki  
- **概要**:
  - `minimatch` のバージョンを強制的に 10系へ上げ、ReDoS脆弱性 (CVE-2026-26996) に対応。  
  - 併せて依存関係のバージョンアップを行い、Node.js 22 以上で動作するように確認済み。  
  - セキュリティ強化を目的とした修正です。

---

## 未完了のタスクと議論中の内容

### 1. [Issue #809](https://github.com/digitaldemocracy2030/kouchou-ai/issues/809) と [PR #810](https://github.com/digitaldemocracy2030/kouchou-ai/pull/810)  
- **内容**: UMAPの`random_state`を`None`にして並列化を有効にしたい要望です。  
- **提案されている解決策**:  
  - `random_state`のデフォルト値を切り替え可能にし、必要に応じて再現性を保ちつつ並列化を有効化。  
  - PR #810をCopilotが作成し、Admin UIから再現性フラグを設定できるようにする修正案が出ています。  
- **呼びかけ**: 既存のエンベディング再利用フローとの兼ね合いをどうするか、まだ議論可能です。

### 2. [Issue #726](https://github.com/digitaldemocracy2030/kouchou-ai/issues/726) と [PR #814](https://github.com/digitaldemocracy2030/kouchou-ai/pull/814)  
- **内容**: 公開レポートがない状態で静的HTMLを出力した際のエラーメッセージがわかりにくいというバグレポート。  
- **提案されている修正**:
  - CopilotがPR #814で、エクスポート時に公開レポート数が0だった場合に早い段階で日本語メッセージを表示し、処理を中断する改修を提案しています。  
- **呼びかけ**: 実際にエクスポートを試したことがあるユーザのフィードバックも歓迎です。

### 3. [Issue #583](https://github.com/digitaldemocracy2030/kouchou-ai/issues/583) 関連のフィルタ機能向上PR  
空コメントや空白のみのコメントをLLM処理前に除外し、エラー多発を防止する対応が進行中です。現在、以下2つのPRが存在し、コンフリクトの解消議論が行われています。  
- [PR #796](https://github.com/digitaldemocracy2030/kouchou-ai/pull/796) (作者: yasumorishima)  
- [PR #813](https://github.com/digitaldemocracy2030/kouchou-ai/pull/813) (作者: nishio)  

後者が前者の内容を統合し、コンフリクトを解消して再提出したものとなっているため、どちらをマージするか・タイミングをどうするか等の調整が必要です。

---

## 参加の呼びかけ

- 「散布図のホバー機能を試してみたい」「UMAPの再現性より処理時間が気になる」など、どんな視点でも大歓迎です。  
- バグ報告やUI改善案は[Issue](https://github.com/digitaldemocracy2030/kouchou-ai/issues)を活用してください。  
- コードに興味がある方は[Pull Request](https://github.com/digitaldemocracy2030/kouchou-ai/pulls)を確認し、レビューやコメントをぜひお寄せください。  

多くの方の参加・意見交換によって「デジタル民主主義2030」を盛り上げましょう！  