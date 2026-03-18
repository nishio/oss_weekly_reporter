# いどばたシステム 3/11~3/18のGitHub活動まとめ

今週（3/11〜3/18）における「いどばたシステム」のGitHub上での活動状況をご紹介します。新機能や文言変更など、目に見える改善点も多いので、OSS開発に興味を持ってくださる方はぜひご覧ください。

---

## 今週完了したタスク

今週は中学校での授業利用を想定したフラット化対応が大きく進み、以下の9件のIssueが完了しました。  
すべての対応で、開発者の yama36 さんが大きく貢献してくれています。

1. [Issue #492](https://github.com/digitaldemocracy2030/idobata-analyst/issues/492)  
   → 教育モード / LLM プロンプト用語の切り替え（任意対応）を完了。  
2. [Issue #491](https://github.com/digitaldemocracy2030/idobata-analyst/issues/491)  
   → 学校向けセットアップドキュメントの追加。  
3. [Issue #490](https://github.com/digitaldemocracy2030/idobata-analyst/issues/490)  
   → 管理画面・ThemeCard のデフォルトを政治色のない中立的なラベルへ。  
4. [Issue #489](https://github.com/digitaldemocracy2030/idobata-analyst/issues/489)  
   → トップページのモック・サンプルデータを授業向けテーマに置き換え。  
5. [Issue #488](https://github.com/digitaldemocracy2030/idobata-analyst/issues/488)  
   → フッター説明文から「政治・行政」「政策反映」の直接言及を排除。  
6. [Issue #487](https://github.com/digitaldemocracy2030/idobata-analyst/issues/487)  
   → ヘッダーのフォールバック文言を中立的に変更。  
7. [Issue #486](https://github.com/digitaldemocracy2030/idobata-analyst/issues/486)  
   → トップやテーマ一覧の文言「政策づくり」→「話し合いのまとめ」等に変更。  
8. [Issue #485](https://github.com/digitaldemocracy2030/idobata-analyst/issues/485)  
   → サイト設定デフォルトの文言を「XX党」「政策」から中立表現に差し替え。  
9. [Issue #484](https://github.com/digitaldemocracy2030/idobata-analyst/issues/484)  
   → 中学校授業向けフラット化の親Issue。上記の一連対応を統括する形でクローズ。

これらの変更によって、初期セットアップ状態や各画面の表示が、授業などにも使いやすい中立的な文言に統一されました。政治色の強いイメージを避けたいユーザにとっても、使いやすいデフォルト設定になっています。

---

## 未完了のタスク・議論中のIssue

今週は以下の4件の新規Issueが作成され、まだクローズされていません。作者はいずれも angelsatan777-cloud さんですが、内容はLCT-BI（Local Circulation Token × Basic Income）の研究ドキュメントやガバナンス設計など、高度な経済・制度設計を取り入れた提案です。興味のある方はぜひ議論に参加してください。

1. [Issue #496](https://github.com/digitaldemocracy2030/idobata-analyst/issues/496)  
   - CORE_MODEL.md v5.0 の追加。非線形制御系モデルを活用した地域経済・財政モデルの提案が含まれています。
2. [Issue #495](https://github.com/digitaldemocracy2030/idobata-analyst/issues/495)  
   - 最終微修正版 README v5.0 について。LCT-BIの概要やセーフティフィルター（CBF）などの要旨が詳述。
3. [Issue #494](https://github.com/digitaldemocracy2030/idobata-analyst/issues/494)  
   - LCT-BI研究用のリポジトリテンプレート。AIによる誤読を防止する工夫を組み込むアイデアが提案されています。
4. [Issue #493](https://github.com/digitaldemocracy2030/idobata-analyst/issues/493)  
   - 「サナエトークン」と題したガバナンスアーキテクチャの概念整理。Civic DAO との連動や経済層のフィードバック構造が示され、いどばたシステムとの親和性を議論中。

いずれのIssueも、地域経済のデジタル化やガバナンス設計に関わる要素が多いため、単なるウェブアプリ開発だけでなく制度設計・制御理論・経済学などの異分野専門家からのフィードバックも歓迎されています。こうした議論の蓄積が、より多面的なOSSプロジェクトとして成長していく鍵となります。

---

## 参加の呼びかけ

- 中学校など教育現場での利用に興味がある方  
  → 「中学校授業向けフラット化」のIssue群はすでに完了しているため、実際の授業向けに試してフィードバックをお寄せください。
- 地域通貨や経済制御理論に関心がある方  
  → [Issue #496](https://github.com/digitaldemocracy2030/idobata-analyst/issues/496) や [Issue #495](https://github.com/digitaldemocracy2030/idobata-analyst/issues/495) など、LCT-BIに関連する議論が活発化しています。ぜひ専門知見やアイデアを共有してください。

いどばたシステム（idobata）プロジェクトは、プログラミングだけでなく、政策・教育・経済理論など、さまざまな分野の知見が求められる総合的なOSSです。皆さんの参加をお待ちしています。ぜひIssueにコメントを残したり、新しい提案を投げたりして、コミュニティを一緒に盛り上げましょう！