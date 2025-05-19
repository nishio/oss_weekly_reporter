# 広聴AI 5/18~5/19 のGitHub活動まとめ

このまとめでは、2025-05-18 16:13 から 2025-05-19 16:13 にかけての「広聴AI(kouchou-ai)」リポジトリのIssue・Pull Requestの動きを解説します。  
新しい機能やデザイン変更が活発に進行中です。OSS開発に興味を持っていただくきっかけになれば幸いです。

---

## 今回完了したIssueとPR

### 完了したIssue (4件)

- [Issue #532](https://github.com/digitaldemocracy2030/kouchou-ai/issues/532)  
  ┗ バグ修正。実装済みのLocal LLM機能について「将来実装予定」という文言が残っていた問題を解消。  
  ┗ 同時に [PR #534](https://github.com/digitaldemocracy2030/kouchou-ai/pull/534) (作成者: shingo-ohki) により修正されました。

- [Issue #447](https://github.com/digitaldemocracy2030/kouchou-ai/issues/447)  
  ┗ 管理画面のボタン追加(#400, #421に関連)に伴うデザインのマスター反映。デザイン制作が完了。

- [Issue #402](https://github.com/digitaldemocracy2030/kouchou-ai/issues/402)  
  ┗ OpenRouter を使えるようにする機能の要望。  
  ┗ [PR #526](https://github.com/digitaldemocracy2030/kouchou-ai/pull/526) (作成者: takumi19910112) にて実装しました。

- [Issue #274](https://github.com/digitaldemocracy2030/kouchou-ai/issues/274)  
  ┗ Github Pagesで静的ファイルが正しく表示されない問題。こちらもクローズされました。

### マージされたPR (4件)

- [PR #535](https://github.com/digitaldemocracy2030/kouchou-ai/pull/535)  
  ┗ 「プルリクエストのテンプレートの項目順」を修正。作成者: shingo-ohki

- [PR #534](https://github.com/digitaldemocracy2030/kouchou-ai/pull/534)  
  ┗ LocalLLMに関する説明文から「将来実装予定」の文言を削除し、正式機能であることを明示。作成者: shingo-ohki

- [PR #533](https://github.com/digitaldemocracy2030/kouchou-ai/pull/533)  
  ┗ CODE_REVIEW_GUIDELINES.mdに「デザインフェーズ→開発フェーズの移行プロセス」を追記。作成者: masatosasano2

- [PR #526](https://github.com/digitaldemocracy2030/kouchou-ai/pull/526)  
  ┗ OpenRouterを介してAIモデルを使用できるようにする機能を実装。作成者: takumi19910112

---

## 未完了のタスクと最新の議論

### 新しく作成されたIssue (2件)

- [Issue #539](https://github.com/digitaldemocracy2030/kouchou-ai/issues/539)  
  ┗ 「利用規約をoptionalに」という要望。利用規約リンクを不要とする議論が進行中です。  
  ┗ 実装予定の議論で、termsLinkをnullにした場合はフッター表示しないなどの仕様が検討されています。

- [Issue #537](https://github.com/digitaldemocracy2030/kouchou-ai/issues/537)  
  ┗ OpenRouterの無料モデル追加を提案するIssueです。無料枠ではAPI側の仕様が特殊でありエラーを吐くケースがあるため、その原因究明や対処法について議論されています。

### 更新されたIssue (4件)

- [Issue #529](https://github.com/digitaldemocracy2030/kouchou-ai/issues/529) / [Issue #528](https://github.com/digitaldemocracy2030/kouchou-ai/issues/528)  
  ┗ いずれもデザイン関連。レポート詳細や説明画像の更新で、よりわかりやすさを追求するためのデザイン案が検討されています。

- [Issue #478](https://github.com/digitaldemocracy2030/kouchou-ai/issues/478)  
  ┗ バグ報告。意見テキストの禁則処理が正しく行われない問題。改行処理をより自然に行う方法を模索中です。

- [Issue #400](https://github.com/digitaldemocracy2030/kouchou-ai/issues/400)  
  ┗ 環境確認機能に関する要望。APIキーの有効性やRate Limitの確認など、デプロイ前のチェック機能のアイデア交換がされています。

### 新しく作成されたPR (4件)

- [PR #541](https://github.com/digitaldemocracy2030/kouchou-ai/pull/541) (作成者: nasuka)  
  ┗ フッター説明文の修正。デジタル民主主義2030と広聴AIの関連を明確にし、OSSプロジェクトの成果であることを周知する改善。

- [PR #540](https://github.com/digitaldemocracy2030/kouchou-ai/pull/540) (作成者: nasuka)  
  ┗ [Issue #539](https://github.com/digitaldemocracy2030/kouchou-ai/issues/539) への対応。利用規約リンクのデフォルトをnullにすることで、サービス利用時の必須表示を解除する修正。

- [PR #538](https://github.com/digitaldemocracy2030/kouchou-ai/pull/538) (作成者: shinta.nakayama+Devin)  
  ┗ 属性フィルタ機能([PR #531](https://github.com/digitaldemocracy2030/kouchou-ai/pull/531))のリファクタリング版。型安全性向上やコンポーネント分割など大幅な整理が図られています。

- [PR #536](https://github.com/digitaldemocracy2030/kouchou-ai/pull/536) (作成者: 種延真之+Devin)  
  ┗ トークン使用量の追跡と表示機能の実装。OpenAIやローカルLLMなど複数のモデル呼び出しで使用したトークン量が一目で分かるようになり、コスト管理や最適化に役立つ議論が進行中です。

### 更新されたPR (WIP)

- [PR #531](https://github.com/digitaldemocracy2030/kouchou-ai/pull/531) (作成者: tokoroten)  
  ┗ 「属性フィルタ機能の実装」。アップロード時に指定した属性カラムでデータを絞り込み、レポートを表示する機能を試作中。  
  ┗ [PR #538](https://github.com/digitaldemocracy2030/kouchou-ai/pull/538) とあわせて最終的にどのような形で統合するかが検討されています。

---

## コントリビュートに興味のある方へ

- 完了したIssueやマージ済みPRを読めば、機能追加やバグ修正の流れ、提案内容の実装方法がイメージしやすくなります。
- 未完了のIssueや進行中のPRでは、まだまだ議論や実装の余地があります。気になるトピックがあればぜひコメントや提案をお願いします。
- 多くのコントリビューターが関わり、デザインから機能開発、ドキュメント整備まで様々な分野で協力しているので、ご自身の得意分野でもご参加いただけます。

一人ひとりの貢献が「広聴AI」をより良いサービスにしていきます。ぜひお気軽にIssueやPRへコメントいただき、OSS開発に参加してみてください。お待ちしています！