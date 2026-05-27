# 広聴AI 5/20~5/27 のGitHub活動まとめ

今週（2026-05-20〜2026-05-27）の広聴AI (リポジトリ: [digitaldemocracy2030/kouchou-ai](https://github.com/digitaldemocracy2030/kouchou-ai)) での活動をまとめました。新機能や修正が多数あり、Windows環境サポートからCSP設定の改善、LLMを使ったグルーピング分析まで盛りだくさんです。ぜひ興味を持った方は開発に参加していただけると嬉しいです！

---

## 今週完了した主な項目

### マージされたPull Request（19件）

以下のPRはいずれも nishio さん (＋AIアシスタントDevin) が主に実装し、今週マージされました:

- [PR #865](https://github.com/digitaldemocracy2030/kouchou-ai/pull/865): legacy pipeline やリファクタリング専用ドキュメント削除など大規模な整理
- [PR #864](https://github.com/digitaldemocracy2030/kouchou-ai/pull/864): CLI とサブプロセスを組み合わせた動作検証でワークフローのパスを修正
- [PR #862](https://github.com/digitaldemocracy2030/kouchou-ai/pull/862): Windows セットアップを実機 E2E と軽量 CI の両面から整備
- [PR #857](https://github.com/digitaldemocracy2030/kouchou-ai/pull/857): Plotly散布図でリンククリックが阻害される問題を修正
- [PR #856](https://github.com/digitaldemocracy2030/kouchou-ai/pull/856): 旧レポートで slug フィールドが欠落していても動くように修正
- [PR #855](https://github.com/digitaldemocracy2030/kouchou-ai/pull/855): reuse画面のBiomelint警告を修正
- [PR #854](https://github.com/digitaldemocracy2030/kouchou-ai/pull/854): テストの共通モック/fixture 重複を整理
- [PR #853](https://github.com/digitaldemocracy2030/kouchou-ai/pull/853): ユーザー入力のAPIキーで接続チェック可能に
- [PR #852](https://github.com/digitaldemocracy2030/kouchou-ai/pull/852): レポート生成失敗時に管理画面上でエラーログを表示
- [PR #851](https://github.com/digitaldemocracy2030/kouchou-ai/pull/851): Azureデプロイで必要なCSPに対応
- [PR #850](https://github.com/digitaldemocracy2030/kouchou-ai/pull/850): LocalLLMのモデル自動取得UXを改善
- [PR #849](https://github.com/digitaldemocracy2030/kouchou-ai/pull/849): 静的ホスティング環境向けCSP設定ガイドを追加
- [PR #848](https://github.com/digitaldemocracy2030/kouchou-ai/pull/848): env設定を考慮したCSPヘッダを追加
- [PR #847](https://github.com/digitaldemocracy2030/kouchou-ai/pull/847): secure context以外でのUUID生成fallbackを実装
- [PR #844](https://github.com/digitaldemocracy2030/kouchou-ai/pull/844): analysis-coreのCLIにconfig/入力ファイル検証（preflight validation）を追加
- [PR #843](https://github.com/digitaldemocracy2030/kouchou-ai/pull/843): analysis-coreの重い依存をextrasに分離し、軽量化
- [PR #841](https://github.com/digitaldemocracy2030/kouchou-ai/pull/841): 旧APIステップのimport箇所を整形してRuff対応
- [PR #840](https://github.com/digitaldemocracy2030/kouchou-ai/pull/840): workflowベース実行をデフォルトに近づけるための土台整備
- [PR #839](https://github.com/digitaldemocracy2030/kouchou-ai/pull/839): apps/apiのuv lockファイルが不要にcommitされないように.gitignoreを追加

### 完了した主なIssue

先週から今週にかけて、「Windows実機でのDocker検証手順 (#860)」「LocalLLM の自動取得UX (#845)」「CSP設定の再考 (#846)」「テスト共通Fixture整理 (#842)」など、多数のIssueがクローズされました。  
また、CLI関連では「ファイルシステムベースの実行ガイド/プリフライト検証 (#836, #837)」「UUID fallback (#833)」なども完了し、新機能や改善が一気に進んでいます。

こうした修正・機能追加の結果、Windows環境やパブリックIP経由アクセス時の使い勝手が大きく向上し、テスト基盤やCSP(セキュリティ)周りの品質も改善しました。

---

## まだ議論中・未完了のタスク

### 新しく作成されたIssue（4件）

- [Issue #872](https://github.com/digitaldemocracy2030/kouchou-ai/issues/872): スマホ環境で散布図に代わるビューを検討する提案  
- [Issue #870](https://github.com/digitaldemocracy2030/kouchou-ai/issues/870): fetch_reports.pyを通常運用から外し、緊急救済用途に再定位する案  
- [Issue #871](https://github.com/digitaldemocracy2030/kouchou-ai/issues/871): Azureデプロイ時の安全チェックを「fetch_reports」ではなくBlob Storageベースに切り替える検討  
- [Issue #869](https://github.com/digitaldemocracy2030/kouchou-ai/issues/869): analysis-core label refinement PR化に向けた残作業調整

### 過去7日間に更新されたIssue（5件）

- [Issue #741](https://github.com/digitaldemocracy2030/kouchou-ai/issues/741): mainブランチマージ時にAzureへのデプロイがたまに競合で失敗する問題  
- [Issue #731](https://github.com/digitaldemocracy2030/kouchou-ai/issues/731): Windows環境で文字化け発生によりセットアップが停止する問題  
- [Issue #478](https://github.com/digitaldemocracy2030/kouchou-ai/issues/478): 禁則処理が効かず、意見の説明が改行不正になる問題  
- [Issue #283](https://github.com/digitaldemocracy2030/kouchou-ai/issues/283): 全画面表示で散布図要約文がボタンに隠れる不具合の残課題  
- [Issue #121](https://github.com/digitaldemocracy2030/kouchou-ai/issues/121): 縦長画面で散布図アスペクト比が崩れる問題

これらは引き続き議論や対応が進んでおり、追加のアイデア・実装PRを歓迎しています！

### 作成されたがまだマージされていないPR（8件）

- [PR #874](https://github.com/digitaldemocracy2030/kouchou-ai/pull/874): 新たにsemantic island layoutを導入し、クラスタの可視化を追加する提案  
- [PR #873](https://github.com/digitaldemocracy2030/kouchou-ai/pull/873): Azureデプロイを直列化して競合を回避する取り組み  
- [PR #868](https://github.com/digitaldemocracy2030/kouchou-ai/pull/868): 実行時ユーザーAPIキーをanalysis-coreへ正しく渡すための修正  
- [PR #867](https://github.com/digitaldemocracy2030/kouchou-ai/pull/867): CLIに「--reuse-from」を追加して既存出力を再利用可能にする  
- [PR #866](https://github.com/digitaldemocracy2030/kouchou-ai/pull/866): LLMによるグルーピング分析モードを追加する試み  
- [PR #863](https://github.com/digitaldemocracy2030/kouchou-ai/pull/863): Windows向けセットアップをPowerShellに分割して日本語対応をしやすくする計画  
- [PR #861](https://github.com/digitaldemocracy2030/kouchou-ai/pull/861): Windows向けsetup_win.batの軽量CIを追加する  
- [PR #858](https://github.com/digitaldemocracy2030/kouchou-ai/pull/858): バッチファイル内の文字化け防止のため英語化＆prefix比較によるAPIキー検証

---

## 参加方法 & コミュニティへの呼びかけ

- GitHub上でIssueを確認していただき、「やってみたい！」と思ったものがあればぜひコメントを残してください。  
- Windowsやスマホへの対応強化など、多くの人に使いやすくするための改善ポイントもまだまだ探っています。初めての方の参加も大歓迎です！  
- Issueに対して質問や提案のコメントをするだけでも貢献になります。  
- コードの書き方で迷った場合はPull RequestやDraftで気軽に意見を求めてください。  

より多くの方が参加して、この「広聴AI」がより使いやすく成長していくことを期待しています。気になったIssuesやPRがあれば、ぜひお気軽に声をかけてください。よろしくお願いします！