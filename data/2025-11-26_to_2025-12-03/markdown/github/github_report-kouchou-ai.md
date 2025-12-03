# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-11-26T12:31:47.149292+09:00 から 2025-12-03T12:31:47.149292+09:00 まで

## Issues

### 過去7日間に完了されたissue (1件)

### [【合意募集】Brand Compassの物差し＋実態ベースライン＋優先順位リブートを決めたい（〜次回定例）](https://github.com/digitaldemocracy2030/kouchou-ai/issues/728)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-11-18T07:14:10Z  
**内容:**

## 結論（Why now）

方向はBrand Compassで定義済み。でも**「実態データの当たり」と「優先順位の運用」がなく、毎週の意思決定がぶれています**。

この2週間で、物差し／ベースライン／運用を仮決めして回し始めないと、現場対応が属人的になり、直す順番も毎回ゼロからになります。

**今日「仮で回す」ことに合意して、2週間後に振り返りましょう。**

---

## 今回、合意したい3点（Decision requests）

### 1) Brand Compassの1ページ要約を優先順位判断の物差しとして採用
- 対象ユーザー/提供価値/非目標/判断基準を明文化
- **受け入れ基準**: 次回定例までに1pドラフトをレビュー→「これで判断する」に👍

### 2) 利用実態の暫定ベースラインを作る（手集計可）
- 直近N件の「件数・成功/失敗・P50/P95時間・概算コスト」を表で提示
- **受け入れ基準**: 次回定例までに暫定集計を提示→データの取り方に👍

### 3) 優先順位のリブートを始める
- 棚卸し（重複/陳腐化/非目標をアーカイブ）→Top5選定→週次トリアージ
- **受け入れ基準**: 棚卸し方針に👍→週1トリアージ枠をカレンダー化

---

## やると何が良いか（Benefits）

- **「何からやるか」を毎回ゼロから議論しない**（判断時間が半減）
- **直すべき箇所がユーザーの痛みと方向性に沿って可視化される**
- **小さな成功を2週間でつくり、チームの推進力を上げる**

---

## この2週間の小さな成果（Quick wins 候補）

以下3件を候補として提案（最終的な優先順位は棚卸し後に決定）:

- **#716 管理画面からエラーログを見られるようにする** → 現場の「詰まり」を自分で解ける
- **#726 わかりにくいエラーメッセージを改善** → 問い合わせ削減
- **#710 散布図リンク不具合を修正** → レポートの活用性が上がる

**目標**: 2週間で少なくとも1件を「完了」

---

## お願い（Call to action）

- **次回定例までに 👍 で合意／💬 で懸念コメント**
- 次回定例で最終合意→2週間運用→振り返りの順で回します

---

## Plan（最短ルート）

- **Day1**: Brand Compass要約1pドラフト共有（対象/価値/非目標/判断基準）
- **Day2**: ベースラインの項目定義＋一次データの当たり確認
- **Day3**: Issue棚卸し方針ドラフト→週次トリアージ枠のカレンダー招待
- **並行**: Quick winsの担当アサインと着手

---

## ToDo（担当/期限）

- [ ] Brand Compass要約1pドラフト（担当: PM支援、期限: 次回定例）
- [ ] ベースライン集計（担当: PM支援＋運用、期限: 次回定例）
- [ ] Issue棚卸し方式の合意（担当: メンテナー/コミッター、期限: 次回定例）
- [ ] 週次トリアージの定例化（担当: PM支援/メンテナー、期限: 次回定例）
- [ ] Quick winsの担当アサイン（担当: 各担当、期限: 2週間以内）

---

## 前提の共有（短く）

- Cartographerは調査設計の議論であり、アンケート実施ツールではない
- 実績件数は未確定（まずは手集計で事実把握）
- 既存の"high priority"ラベルは現行優先ではない（今回リブートする）

---

## 参考

- Brand Compass: https://www.figma.com/deck/0B55u8rxDjjjpRJbNUEP0Z/
- 議事録（Google Doc）: https://docs.google.com/document/d/1plggszRTxEEYUcZuCLiHkPrBsMtxr3RQpctKtZe5y4M/edit
- Devin session: https://app.devin.ai/sessions/9919a0b6149143e69ba287b3bb82b909

**コメント:** なし

---

### 過去7日間に作成されたissue (0件)

### 過去7日間に更新されたissue（作成・クローズを除く）(1件)

### [[BUG]将来の開発で必要な変更 - TODO](https://github.com/digitaldemocracy2030/kouchou-ai/issues/700)

**作成者:** nishio  
**作成日:** 2025-09-09T08:32:22Z  
**内容:**

Devin.aiのセットアップの失敗原因を解明しました。以下Devinのレポートnn

1. Biome Linter の修正 🔧

問題: biomeが正しく動作しないため、lint設定を修正する必要があります。

現在の状況:


biomeはroot package.jsonにインストールされている

client/client-adminのpackage.jsonにbiomeが含まれていない

現在のlintコマンドは絶対パスを使用している


必要な変更:

# Option A: Root level でbiomeを使用する場合
cd ~/repos/kouchou-ai && npm install @biomejs/biome@^1.9.4 --save-dev

# Option B: 各プロジェクトにbiomeを追加する場合
cd ~/repos/kouchou-ai/client && npm install @biomejs/biome@^1.9.4 --save-dev
cd ~/repos/kouchou-ai/client-admin && npm install @biomejs/biome@^1.9.4 --save-dev
推奨lint設定 (Option A):

cd ~/repos/kouchou-ai && npx biome check client
cd ~/repos/kouchou-ai && npx biome check client-admin
cd ~/repos/kouchou-ai/server && python -m ruff check .
2. Package.json の更新 📦

変更が必要なファイル:


package.json: biomeバージョンを "^1.9.4" に変更

package-lock.json: npm installによる依存関係の更新

client/package-lock.json: Next.js関連の依存関係更新


3. 環境変数の設定 🔐

現在の状況: 基本的な.envファイルは存在するが、実際のAPIキーは空

開発時に必要な設定:

# .env ファイルで設定が必要な項目（本番環境用）
OPENAI_API_KEY=your_actual_key_here
OPENROUTER_API_KEY=your_actual_key_here
BASIC_AUTH_USERNAME=your_username
BASIC_AUTH_PASSWORD=your_password
4. 依存関係の完全インストール 📥

必要なコマンド:

# Root dependencies
cd ~/repos/kouchou-ai && npm install

# Client dependencies  
cd ~/repos/kouchou-ai/client && npm install

# Client-admin dependencies
cd ~/repos/kouchou-ai/client-admin && npm install

# Server dependencies
cd ~/repos/kouchou-ai/server && uv pip install --system -r requirements-dev.lock


**コメント:** なし

---

