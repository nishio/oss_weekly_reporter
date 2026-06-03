# 広聴AI 5/27~6/3 のGitHub活動まとめ

今週(2026/05/27〜2026/06/03)の開発ハイライトです。多くのPRがマージされ、バグ修正やリファクタが進む一方、新機能やドキュメント整備のIssueも多数立ち上がっています。

以下の内容を参考に、ぜひOSS開発に参加してみてください。

---

## 今週完了した内容

今週は以下の4件のIssueがクローズされました。新機能の追加だけでなく、バグ修正やリファクタにより、安定性や使い勝手が向上しています。

1. [Issue #886](https://github.com/digitaldemocracy2030/kouchou-ai/issues/886)  
   WebGLがサポートされているブラウザでも旧バージョンのレポート表示時に「WebGL is not supported…」と出てしまう問題を修正しました。  
   - 対応PR: [PR #887](https://github.com/digitaldemocracy2030/kouchou-ai/pull/887)  
   - 主な貢献者: 101ta28 +Devin  
   - 内容: Content Security Policy(CSP)の修正によりPlotlyのscatterglが正常に動作するように修正。

2. [Issue #870](https://github.com/digitaldemocracy2030/kouchou-ai/issues/870)  
   `fetch_reports.py` を通常運用から外してBlob Storageベースの運用に一本化しました。  
   - 対応PR: [PR #875](https://github.com/digitaldemocracy2030/kouchou-ai/pull/875)  
   - 主な貢献者: nishio +Devin  
   - 内容: 古いスクリプトを削除し、Azure Blob Storageが正規のバックアップ/リストア手段となるようドキュメントやワークフローを整理。

3. [Issue #741](https://github.com/digitaldemocracy2030/kouchou-ai/issues/741)  
   main へのマージ時に発生していたAzureへのdeploy失敗の問題が解消されました。  
   - 対応PR: [PR #873](https://github.com/digitaldemocracy2030/kouchou-ai/pull/873)  
   - 主な貢献者: nishio +Devin  
   - 内容: デプロイワークフローを直列化し、Container Appsでの更新競合による失敗を抑止。

4. [Issue #731](https://github.com/digitaldemocracy2030/kouchou-ai/issues/731)  
   Windows環境でセットアップバッチ実行時に文字化けが起こり強制終了する問題を修正しました。  
   - 対応PR: [PR #863](https://github.com/digitaldemocracy2030/kouchou-ai/pull/863)  
   - 主な貢献者: nishio +Devin  
   - 内容: setupスクリプトをPowerShellに分割し、文字化けを回避。Docker未起動時のエラー表示などUI面も改善。

---

## 未完了だが議論中の内容

下記のIssueは、まだクローズされていないものの、有意義な議論が進行中です。機能提案やドキュメント改善、ラベル品質の実験計画など、多様なテーマがあります。ぜひ意見や実装でご参加ください。

### 新機能提案や機能拡張

- [Issue #885](https://github.com/digitaldemocracy2030/kouchou-ai/issues/885) Windows単一実行ファイル配布に向けたNode runtimeの置き換え検討  
- [Issue #884](https://github.com/digitaldemocracy2030/kouchou-ai/issues/884) レポート作成前に入力・コスト・API状態を確認する新パネル  
- [Issue #882](https://github.com/digitaldemocracy2030/kouchou-ai/issues/882) KJ法プロンプトがラベル品質に与える影響の比較実験  
- [Issue #881](https://github.com/digitaldemocracy2030/kouchou-ai/issues/881) ラベル品質改善の実験や議論を追跡可能にするトラッキングIssue  
- [Issue #880](https://github.com/digitaldemocracy2030/kouchou-ai/issues/880) [8, 64]分析をマンダラート可視化する試み  
- [Issue #879](https://github.com/digitaldemocracy2030/kouchou-ai/issues/879) クラスタと時刻を掛け合わせたヒートマップ表示の検討

### ドキュメント整備・開発者支援

- [Issue #878](https://github.com/digitaldemocracy2030/kouchou-ai/issues/878) AIエージェントを使うコントリビュータ向け作業導線の集約  
- [Issue #877](https://github.com/digitaldemocracy2030/kouchou-ai/issues/877) Windowsセットアップガイドの前提条件と失敗時の分岐を整理  
- [Issue #876](https://github.com/digitaldemocracy2030/kouchou-ai/issues/876) README / docs の開発者向け導線をcurrent mainに合わせて再整理

### 既存機能の改善やリファクタ

- [Issue #869](https://github.com/digitaldemocracy2030/kouchou-ai/issues/869) analysis-coreのラベルリファイン実装をPR化するための残作業整理  
- [Issue #391](https://github.com/digitaldemocracy2030/kouchou-ai/issues/391) レポート作成時、APIエラーが起きた場合のわかりやすいメッセージ表示  
- [Issue #292](https://github.com/digitaldemocracy2030/kouchou-ai/issues/292) OpenAIの課金設定(クレジット)とChatGPT Plusの混同を防ぐ案内強化  
- [Issue #221](https://github.com/digitaldemocracy2030/kouchou-ai/issues/221) 試行錯誤の負担を減らす方法を検討  
- [Issue #97](https://github.com/digitaldemocracy2030/kouchou-ai/issues/97) CSVフォーマットのエラーをもっとわかりやすく伝える  
- [Issue #79](https://github.com/digitaldemocracy2030/kouchou-ai/issues/79) CSVアップロード時の概算コスト表示機能  
- [Issue #11](https://github.com/digitaldemocracy2030/kouchou-ai/issues/11) レポート出力にかかる時間の目安を表示  

---

## 参加の呼びかけ

- 新しく立ち上がったIssueは、まだ意見が十分に集まっていないものも多いです。ぜひコメントや提案、PRでお手伝いください。
- バグ報告や機能要望はもちろん、UIの改善やドキュメント翻訳など、多様な貢献を歓迎します。
- コントリビューション方法は[Issue #878](https://github.com/digitaldemocracy2030/kouchou-ai/issues/878)の改善議論や、本リポジトリのCONTRIBUTING.mdも参考にどうぞ。

OSSの協力が「デジタル民主主義2030」の未来を支えます。今後とも応援・参加よろしくお願いします！  