# 広聴AI 第5週（2025/04/09~2025/04/16）のGitHub活動まとめ

この1週間の「いどばたシステム(idobata-analyst)」リポジトリでの活動内容をお届けします。完成した機能や進行中のタスクをまとめていますので、コミュニティの皆さんの議論への参加やOSS開発へのコントリビュートのきっかけにぜひ活用してください！

---

## 今週完了したタスク（新機能・不具合修正など）

### 1. ビジュアル分析タブの余白を調整し、スマホ表示を快適に（Issue [#72](https://github.com/digitaldemocracy2030/idobata-analyst/issues/72) → PR [#89](https://github.com/digitaldemocracy2030/idobata-analyst/pull/89)）
- スマホ表示や小さい画面でビジュアル分析タブが読みにくい問題を解決。  
- div の入れ子を減らす・余白を少なくすることで、よりスッキリしたレイアウトに。  
- 実装者: spinute  

### 2. GitHub Actionsでテスト・リントを実行（Issue [#71](https://github.com/digitaldemocracy2030/idobata-analyst/issues/71) → PR [#104](https://github.com/digitaldemocracy2030/idobata-analyst/pull/104)）
- コードの品質を保つために、自動でテストとリントを走らせるワークフローを導入。  
- PRが出るたびにCIで検証されるようになり、開発者が安心してコントリビュートできるように。  
- 実装者: takker99  

### 3. OpenRouter クレジット残量のアラート表示（Issue [#22](https://github.com/digitaldemocracy2030/idobata-analyst/issues/22) → PR [#60](https://github.com/digitaldemocracy2030/idobata-analyst/pull/60)）
- OpenRouter APIのクレジットが少なくなった際にアラートを出し、開発者が早めに気づけるように。  
- 残量が100を切った場合にログ出力（将来的にはSlack等へ通知予定）。  
- 実装者: spinute  

### 4. コメント左側バーの色を円グラフと一致させる（Issue [#15](https://github.com/digitaldemocracy2030/idobata-analyst/issues/15) → PR [#99](https://github.com/digitaldemocracy2030/idobata-analyst/pull/99)）
- 「論点ごとの分析ページ」で、円グラフの色とコメント左のバーをそろえることで視認性向上。  
- 立場（スタンス）がひと目でわかりやすくなり、ビジュアル分析がさらに活用しやすく。  
- 実装者: spinute  

### 5. ディスプレイサイズに応じてページ幅を自動調整（PR [#102](https://github.com/digitaldemocracy2030/idobata-analyst/pull/102)）
- 画面が広い場合も余白が多すぎず、逆に狭い場合も読みやすいようにレイアウトを調整。  
- Issue の関連付けはありませんが、ユーザビリティ改善としてマージ済みです。  
- 実装者: spinute  

---

## 今週議論中（未完了）のタスク

「何が議論されているか」を知ることで、興味・知識が近い分野に飛び込んでいただけると嬉しいです。ぜひIssueやPRでアイデア・知見をお寄せください！

### 1. プロジェクトレポート失敗時に理由を表示（Issue [#105](https://github.com/digitaldemocracy2030/idobata-analyst/issues/105)）
- 「分析に失敗しました」とだけ表示され、詳細が示されないためユーザが混乱しがち。  
- 失敗原因をどう通知するか、よくある例を含めて検討中。  

### 2. 「deep search」でファクトチェック機能（Issue [#97](https://github.com/digitaldemocracy2030/idobata-analyst/issues/97)）
- ディスカッションの根拠にあたるファクトを手軽に検索・チェックしたいという要望。  
- 具体的な仕組みやUIなど、議論が始まった段階。  

### 3. ビジュアル分析をシェアしやすくしたい（Issue [#81](https://github.com/digitaldemocracy2030/idobata-analyst/issues/81)）
- SNSで分析結果を共有して広められる仕組みの要望。  
- 画像分割ダウンロードやURLシェアなどのUI改善を検討中。  

### 4. チャット履歴の保存と再開（Issue [#77](https://github.com/digitaldemocracy2030/idobata-analyst/issues/77)）
- AIとの対話を日をまたいで継続したい、という声が多数。  
- マイページやブラウザ再読み込みとの兼ね合いなど実装方法を話し合い中。  

### 5. バックエンド/フロントエンドのテスト導入（Issues [#70](https://github.com/digitaldemocracy2030/idobata-analyst/issues/70), [#69](https://github.com/digitaldemocracy2030/idobata-analyst/issues/69)）
- 継続的なコード品質の向上のため、各パッケージでテストを整備していきたいという提案。  
- Jest を活用する方針などが議題に。  

### 6. 論点抽出の仕組み改善（Issue [#58](https://github.com/digitaldemocracy2030/idobata-analyst/issues/58)）
- 「マイナーだけど重要な論点」を見逃さず抽出したい、などLLM活用についての試行錯誤中。  
- コストとのバランスや分析結果の説明可能性をどの程度重視するかが論点。  

### 7. レポートタイトルと作成日時のレイアウト（Issue [#57](https://github.com/digitaldemocracy2030/idobata-analyst/issues/57)）
- ビジュアルレポートのタイトル文字列に絡み、日時表示が重なって見づらい問題。  
- 小規模なUI修正で解決できそうだが、対応方法を検討中。  

### 8. extractionフェーズでの情報の捨象（Issue [#39](https://github.com/digitaldemocracy2030/idobata-analyst/issues/39)）
- AIによる意見抽出が過度に抽象化され、投稿者の意図が薄まる事例が見られる問題。  
- Prompt調整などで最適な落としどころを探っている段階。  

### 9. コメント左バー色一致の別アプローチ（PR [#37](https://github.com/digitaldemocracy2030/idobata-analyst/pull/37)）
- 実はIssue [#15](https://github.com/digitaldemocracy2030/idobata-analyst/issues/15)向けの別実装があり、javasparrows氏がPRを作成済み。  
- すでに spinute 氏によるPR [#99](https://github.com/digitaldemocracy2030/idobata-analyst/pull/99) がマージされたが、こちらの手法も参考になる部分があるかもしれず、オープンのまま議論中。  

---

## ぜひあなたのアイデアをお寄せください！

いどばたシステムのデータ分析を通じて、より充実したデジタル民主主義の場をつくることを目指しています。未完了のタスクではまだまだ多くのアイデア・議論を受け付けています。  
- 技術面での知見共有  
- ユーザの立場からの意見・要望  
- デザイン・UI/UXへの改善提案  

小さなコメントだけでも大歓迎ですので、ぜひIssueやPRにご参加ください。  
今後とも「広聴AI」のOSS開発をよろしくお願いいたします。  