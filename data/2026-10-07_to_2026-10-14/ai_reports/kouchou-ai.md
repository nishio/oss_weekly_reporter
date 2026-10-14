# 広聴AI 10/7~10/14 のGitHub活動まとめ

今週は多数のIssue/PRがクローズ・マージされ、新機能の追加や改善が活発に行われています。ここではまず完了したタスクを紹介し、続いて未完了のタスクで進行中の議論をまとめます。開発者以外のユーザのみなさんにも、どんな新機能が加わったか、また何が活発に議論されているかを知ってもらえれば嬉しいです。

---

## 完了したタスク

### 所与カテゴリへの意見分類をCLIで実現
- [Issue #994](https://github.com/digitaldemocracy2030/kouchou-ai/issues/994)  
- [PR #996](https://github.com/digitaldemocracy2030/kouchou-ai/pull/996)  
作成者: nishio さん  
概要: 抽出済みの意見を、あらかじめ決まったカテゴリへ自動で割り当てできるようにする「指定カテゴリ分類」がanalysis-coreに追加されました。これにより「交通」「防災」「その他」など、人間が定義したラベルへAIが意見を分類してくれます。

### 埋め込みモデルをチャットモデルと分離して選択可能に
- [Issue #450](https://github.com/digitaldemocracy2030/kouchou-ai/issues/450)  
- [PR #984](https://github.com/digitaldemocracy2030/kouchou-ai/pull/984)  
作成者: nishio さん  
概要: 管理画面のAI設定で、チャットモデルとは別に埋め込みモデルを選べるようになりました。開発者としてはより柔軟にLLM構成を組み合わせられ、利用者のニーズに合わせた分析が期待できます。

### LLM直接グルーピング機能を作成UIに追加
- [Issue #176](https://github.com/digitaldemocracy2030/kouchou-ai/issues/176)  
- [PR #987](https://github.com/digitaldemocracy2030/kouchou-ai/pull/987)  
作成者: nishio さん  
概要: 従来の埋め込み＋階層クラスタリングに加え、LLMが直接トピック分けを行うモードが管理画面から選択可能になりました。開発者にとってはモード別のconfig映射が少し複雑ですが、より多彩な分析スタイルを実現しています。

### OpenRouter無料モデルでstructured outputsが使えない問題を回避
- [Issue #537（関連）](https://github.com/digitaldemocracy2030/kouchou-ai/issues/537)  
- [PR #985](https://github.com/digitaldemocracy2030/kouchou-ai/pull/985)  
作成者: nishio さん  
概要: 一部のOpenRouter無料モデルがstructured outputsに対応していないため発生していた呼び出しエラーを、フォールバック機構を追加することで回避。これにより無料モデルでも解析が続行しやすくなりました。

### report.html出力時のライセンス案内改善
- [PR #970](https://github.com/digitaldemocracy2030/kouchou-ai/pull/970)  
作成者: nishio さん  
概要: CLIで生成するHTMLレポートにAGPLライセンス文章やソース同梱の仕組みを追加。OSSのライセンスに沿った形でレポート公開を行いやすくなっています。

---

## 未完了のタスク

### 日本語・英語・韓国語の言語切り替え機能（公開ビューア）
- [PR #976](https://github.com/digitaldemocracy2030/kouchou-ai/pull/976)  
作成者: nishio さん  
概要: レポート閲覧画面で日本語・英語・韓国語を切り替えられる機能を提案中。全画面表示中に言語変更できる点がポイントです。今後のレビュー・議論を経てのマージが待たれています。

### 新規に立てられた議論
- [Issue #997](https://github.com/digitaldemocracy2030/kouchou-ai/issues/997) 所与カテゴリ分類のWebUI実装検討  
- [Issue #991](https://github.com/digitaldemocracy2030/kouchou-ai/issues/991) OpenRouter無料モデルの実API動作検証呼びかけ  
- [Issue #989](https://github.com/digitaldemocracy2030/kouchou-ai/issues/989) UMAP平面使い回しのWebUI導線  
- ほか複数のIssueが立ち上がっていて、議論が盛んに進んでいます。

上記のIssueはいずれもまだ作業途中で、具体的な実装方針を詰めたり、テスト検証が必要だったりします。議論や実装に興味がある方はぜひ参加してみてください。

---

## 参加のご案内

- 機能提案やバグ発見など、どなたでもIssueにコメントOKです。  
- コードを書いてPRを送ることはもちろん、ドキュメントの翻訳修正も大歓迎です。  
- Slackでのやり取りも含め、OSSならではの多様なコラボレーションをお待ちしています。

今後も「広聴AI」は自治体やさまざまなコミュニティで活用されることを目指して開発が進みます。新しい貢献者の皆さまの参加を心よりお待ちしています！