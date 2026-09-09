# 広聴AI 2026/09/02～2026/09/09 のGitHub活動まとめ

今週は多数のIssueがクローズとなり、多くの新機能や修正がマージされました。ここではまず完了したアップデートを紹介し、その後、まだ議論中・対応中のタスクについて解説します。多様なコントリビュータが貢献してくださっているので、ぜひ参考にしてください。

---

## 今週完了した主なアップデート

### 1. OpenAI/Gemini/Azureなど LLM 周りの改善

- [PR #934](https://github.com/digitaldemocracy2030/kouchou-ai/pull/934) (作者: tokoroten)  
  - [Issue #916](https://github.com/digitaldemocracy2030/kouchou-ai/issues/916) をクローズ。GPT-5/6向けにFlex Processingを正しく利用できるようにし、タイムアウトや再試行の制御を強化しました。

- [PR #914](https://github.com/digitaldemocracy2030/kouchou-ai/pull/914) (作者: nishio)  
  - [Issue #909](https://github.com/digitaldemocracy2030/kouchou-ai/issues/909)、[Issue #906](https://github.com/digitaldemocracy2030/kouchou-ai/issues/906)、[Issue #907](https://github.com/digitaldemocracy2030/kouchou-ai/issues/907) を同時にクローズ。カタログを統一し、新しいGPT-5.6 / Gemini 3.8モデルを「未検証だけど選択可能」に。  
  - 動的リスト取得と提供終了モデルの扱いなどをサーバー側で一元管理し、管理画面でも反映可能となりました。

- [PR #911](https://github.com/digitaldemocracy2030/kouchou-ai/pull/911) (作者: nishio)  
  - [Issue #908](https://github.com/digitaldemocracy2030/kouchou-ai/issues/908)、[Issue #477](https://github.com/digitaldemocracy2030/kouchou-ai/issues/477) をクローズ。Azureの場合、実際のdeploymentが環境変数で固定されているため、UIモデル選択を無効化。混乱の原因だった箇所を明示化しました。

- [PR #920](https://github.com/digitaldemocracy2030/kouchou-ai/pull/920) (作者: nishio)  
  - [Issue #452](https://github.com/digitaldemocracy2030/kouchou-ai/issues/452) をクローズ。LLM呼び出しのタイムアウトを環境変数で指定できるようになり、ローカルLLMや大規模入力時も融通が利くようになりました。

### 2. レポートの作成・表示・エラー検知まわりの刷新

- [PR #935](https://github.com/digitaldemocracy2030/kouchou-ai/pull/935) (作者: yasumorishima)  
  - exportビルドでデータを埋めこまず、HTMLとJSONを分離する「shellビルド」機能を追加。レポートを配布するときに再ビルド不要となる下地ができました（関連Issue #885 へ段階的対応）。

- [PR #933](https://github.com/digitaldemocracy2030/kouchou-ai/pull/933) (作者: nishio)  
  - [Issue #478](https://github.com/digitaldemocracy2030/kouchou-ai/issues/478)、[Issue #283](https://github.com/digitaldemocracy2030/kouchou-ai/issues/283)、[Issue #253](https://github.com/digitaldemocracy2030/kouchou-ai/issues/253)、[Issue #872](https://github.com/digitaldemocracy2030/kouchou-ai/issues/872)、[Issue #566](https://github.com/digitaldemocracy2030/kouchou-ai/issues/566) を一挙クローズ。  
  - 日本語の改行、全画面表示の操作、スマホ向けの初期ビューなどUIを大幅に改善。複数の不具合修正により閲覧性が向上しました。

- [PR #910](https://github.com/digitaldemocracy2030/kouchou-ai/pull/910) (作者: nishio)  
  - [Issue #905](https://github.com/digitaldemocracy2030/kouchou-ai/issues/905) に部分対応。意見抽出で一部失敗があっても「0件」と扱われていた問題を修正し、失敗時は途中で中断してエラーを明示。抽出漏れのまま完了しなくなりました。

- [PR #919](https://github.com/digitaldemocracy2030/kouchou-ai/pull/919) (作者: nishio)  
  - [Issue #915](https://github.com/digitaldemocracy2030/kouchou-ai/issues/915) をクローズ。ラベリング工程でエラー応答が返ってきた場合、誤ってラベルに「エラー文」を含めずに処理を停止するよう変更。部分的にしかラベル生成されない状態を防ぎました。

- [PR #922](https://github.com/digitaldemocracy2030/kouchou-ai/pull/922) (作者: nishio)  
  - [Issue #884](https://github.com/digitaldemocracy2030/kouchou-ai/issues/884) をクローズ。レポート作成前確認のUIが追加され、入力データの件数やクラスタ数、API接続チェックがまとめて見られるように。

- [PR #923](https://github.com/digitaldemocracy2030/kouchou-ai/pull/923) (作者: nishio)  
  - [Issue #97](https://github.com/digitaldemocracy2030/kouchou-ai/issues/97) をクローズ。CSVの壊れたフォーマットや列不整合を事前に検知し、ユーザーに修正方法を表示する機能が追加。パース失敗のまま処理が進むことを予防。

- [PR #924](https://github.com/digitaldemocracy2030/kouchou-ai/pull/924) (作者: nishio)  
  - [Issue #696](https://github.com/digitaldemocracy2030/kouchou-ai/issues/696) をクローズ。レポート上部に「読み方ガイド」を追加。全回答数や偏りについての注意喚起を表示し、利用者が誤解しにくくなりました。

- [PR #918](https://github.com/digitaldemocracy2030/kouchou-ai/pull/918) (作者: nishio)  
  - [Issue #639](https://github.com/digitaldemocracy2030/kouchou-ai/issues/639) をクローズ。CSVをアップロードした際、タイトルと説明文が空欄ならファイル名から自動入力されるように。

- [PR #927](https://github.com/digitaldemocracy2030/kouchou-ai/pull/927) (作者: nishio)  
  - [Issue #528](https://github.com/digitaldemocracy2030/kouchou-ai/issues/528) をクローズ。階層図と表示テキストのミスマッチを解消し、ツリー図をクリックして階層を降りても説明が連動するようになりました。

- その他にも、[PR #926](https://github.com/digitaldemocracy2030/kouchou-ai/pull/926) (provider・モデルの接続確認機能)、[PR #930](https://github.com/digitaldemocracy2030/kouchou-ai/pull/930) (抽出プロンプト改善ドキュメント追加)など、多くの改善が行われています。

### 3. Windowsサポート・ドキュメント関連

- [PR #929](https://github.com/digitaldemocracy2030/kouchou-ai/pull/929) (作者: nishio)  
  - [Issue #877](https://github.com/digitaldemocracy2030/kouchou-ai/issues/877) をクローズ。Windows向けセットアップガイドで前提環境と失敗時の切り分け手順を明確化し、Docker Desktopが使えない組織PCでも対応策を提示。

- [PR #936](https://github.com/digitaldemocracy2030/kouchou-ai/pull/936) (作者: yasumorishima)  
  - exportビルド時にOGP画像が生成されない点をドキュメントで訂正し、混乱を解消。

- [PR #903](https://github.com/digitaldemocracy2030/kouchou-ai/pull/903) (作者: yasumorishima)  
  - [Issue #885](https://github.com/digitaldemocracy2030/kouchou-ai/issues/885) の前提として、現状のNode runtime依存をインベントリ化。単一実行ファイル化を進めるうえでの基盤資料となっています。

---

## まだ完了していないタスク・議論中のIssue

- [Issue #905](https://github.com/digitaldemocracy2030/kouchou-ai/issues/905)  
  - 抽出工程の部分失敗をエラー検知する対応は [PR #910](https://github.com/digitaldemocracy2030/kouchou-ai/pull/910) で進みましたが、同Issueで報告されていた「詳細クラスタの一部ラベルが失敗したまま生成完了扱いになる」ケースまでは未対応。さらなる修正やテストが検討されています。

- [Issue #885](https://github.com/digitaldemocracy2030/kouchou-ai/issues/885)  
  - Windows向け単一実行ファイル配布を目指す大きなテーマで、複数のPR ([PR #903](https://github.com/digitaldemocracy2030/kouchou-ai/pull/903), [PR #935](https://github.com/digitaldemocracy2030/kouchou-ai/pull/935), ほか) ですでに一部対応中。static-site-builderのNode依存をどう除去するかが今後の焦点です。

- [Issue #921](https://github.com/digitaldemocracy2030/kouchou-ai/issues/921)  
  - ブラウザ版(kouchou-ai-serverless)を広聴AIの本流とするかどうか、まだ議論中。本体とserverlessの使い分けや、OSSコミュニティの運営方式がテーマになっています。

- [Issue #912](https://github.com/digitaldemocracy2030/kouchou-ai/issues/912)、[Issue #913](https://github.com/digitaldemocracy2030/kouchou-ai/issues/913)  
  - GPT-5.6系 / Gemini 3.8系の実API動作を検証するTask。PR #914で選択肢が追加されましたが、まだ「動作未確認」のステータスにとどまっています。APIキー確保や費用見積もりなど実際の試験実施が必要です。

- このほか、OpenRouter接続(#537)やDockerなし運用(#496)、Embeddingモデル選択(#450)やラベル重なりのUI(#294)など、多数の未完了タスクがあります。各Issueでの議論が進行中です。ぜひ意見や要望を寄せてください。

---

## おわりに

今週は多くのIssueがクローズし、新機能や改善の量も非常に多い1週間でした。特にレポート生成前後のエラー検知・UI改善・新モデル対応が進み、利用体験が大きく向上しています。一方で、Windows単一実行ファイル化やserverlessとの統合方針など、コミュニティ参加による検討が必要な大きなテーマも残っています。

興味を持たれた方は、未解決のIssueにコメントや議論をぜひ寄せてください。多様なコントリビュータが参加することで、さらに円滑なOSS開発が進むと期待しています。ご協力よろしくお願いいたします。