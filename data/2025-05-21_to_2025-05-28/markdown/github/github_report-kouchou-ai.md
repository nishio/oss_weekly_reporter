# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-05-21T12:26:44.112004+09:00 から 2025-05-28T12:26:44.112004+09:00 まで

## Issues

### 過去7日間に完了されたissue (13件)

### [[FEATURE][design] admin コンテンツ量が少ない時もフッターが画面下部にあるようにしたい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/572)

**作成者:** UtkNggc  
**作成日:** 2025-05-26T07:39:14Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
レポートが0件や数件の場合、ユーザーのデバイスによって、デバイス縦幅よりもコンテンツの高さが少ないこともありそう。
現状は、フッターの下部が延長される（左）仕組みになってるので、
「コンテンツ部分の下の白背景が伸びる」にしたい（右）。

<img width="849" alt="Image" src="https://github.com/user-attachments/assets/d0340d44-5ddd-4b75-8172-dbc36021aa0c" />

## 目的
フッターはいつもデバイスの足元にいるという安定感、統一された体験を作る。

## 補足
本件は admin画面のみです。
client画面は https://github.com/orgs/digitaldemocracy2030/projects/3?pane=issue&itemId=109263338&issue=digitaldemocracy2030%7Ckouchou-ai%7C438 で対応予定。

**コメント:** なし

---

### [[FEATURE] 文字列の検索によるフィルタを実装する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/560)

**作成者:** nasuka  
**作成日:** 2025-05-22T06:31:44Z  
**内容:**

# 背景
* 属性フィルタの実装によって、属性情報でフィルタリングできるようになった
* 同様の枠組みで、文字列によるフィルタリングもできると分析が捗りそう


# 提案内容
clientの「全体」「濃い意見」において、以下の検索フィルターを実装する

フィルタの仕様
* 入力された文字列が含まれているテキスト（argument）のみをフィルタして表示する機能を実装する
  * フィルタは、既存の「属性フィルタ」のダイアログ内部に追加で実装する
    * これに伴い、「属性フィルタ」の名称を「フィルタ」に変更する

**コメント:** なし

---

### [[FEATURE] セグメントコントロールon mouse時のカーソルを手のポインターにしたい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/559)

**作成者:** UtkNggc  
**作成日:** 2025-05-22T05:00:31Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
押せることをユーザーに明示し、直感的に使ってもらえるプロダクトにする。

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
セグメントコントロールのグレーの部分にonmouseした時に手のポインターになる。
<img width="507" alt="Image" src="https://github.com/user-attachments/assets/995829b4-d2c9-42d5-8764-eb6b2da02b5a" />

ChakraUIの公式ではカーソルは三角矢印のままだが、UX観点では手のポインターのほうがより好ましいと考え、Issue化しました。
https://chakra-ui.com/docs/components/segmented-control

## ご相談したいこと
現在地の白い部分は押しても何も変わらないので、理想でいうと、切り替えられるグレー部分のみ手にして「押せるよ」と明示したい。でも、これを叶えるために複雑な処理が必要なのであれば、白いエリアも同じ手のポインターでもUX観点で許容範囲です！

**コメント:** なし

---

### [[BUG] report_status.jsonが初期化される](https://github.com/digitaldemocracy2030/kouchou-ai/issues/553)

**作成者:** mtane0412  
**作成日:** 2025-05-21T01:54:38Z  
**内容:**

### 概要

一旦メモ

1. docker compose up後にlocalhost:4000が立ち上がる
2. localhost:4000を開くとレポートが読込中
3. このタイミングでブラウザ更新する
4. ログでslugに関して例外が出てレポートが表示されなくなる

手動でreport_status.jsonのtest-slugの情報を消すとレポートなしの状態で再び使えるようになる。
```report_status.json
{}
```

scripts/fetch_reports.py で作成されたレポートから復元できる？
やってみたけどなんかのAPIキーが必要そう(Azure限定?)

#549 作業中に発生して関連がないか調べる。
dockerのディスク空き容量で` No space left on device` が出ていたのでそっち関連かもしれない。
mainブランチで発生するかまだ調べていない。


### 再現手順
todo: 調べる
1. <!-- バグが再現する手順をステップごとに記入してください -->
2. 
3. 

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->

### スクリーンショット・ログ

report_status.jsonがこのデフォルトの状態になっている
```
{
    "test-slug": {
        "status": "ready",
        "title": "Test Report",
        "description": "Test Description",
        "visibility": "public",
        "is_pubcom": false,
        "created_at": "2023-01-01T00:00:00Z",
        "token_usage": 800,
        "token_usage_input": 350,
        "token_usage_output": 450,
        "provider": "openai",
        "model": "gpt-4o"
    }
}
```
この状態でtest-slugを取りに行くのでエラーが出る。
```
api-1 | 2025-05-20 14:21:10 [error ] Request URL: http://api:8000/reports - Exception: 1 validation error for Report
api-1 | slug
api-1 | Field required [type=missing, input_value={'status': 'ready', 'titl...nai', 'model': 'gpt-4o'}, input_type=dict]
```

### その他
report_status.json まわりの挙動をよく理解していない

**コメント:** なし

---

### [PR #531 レビュー：属性カラム選択とフィルタリング機能](https://github.com/digitaldemocracy2030/kouchou-ai/issues/552)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-05-21T00:38:16Z  
**内容:**

# PR #531 レビュー：属性カラム選択とフィルタリング機能

## 概要
このPRは広聴AIアプリケーションに属性カラム選択とフィルタリング機能を実装しています。ユーザーはCSV/スプレッドシートデータのインポート時に属性カラムを選択し、これらの属性に基づいてレポートの可視化をフィルタリングすることができます。

## フロントエンド変更点
- データインポート時に属性カラムを選択するための新しいコンポーネント `AttributeColumnsSelector.tsx` を追加
- 属性カラム選択を統合するために `CsvFileTab.tsx` と `SpreadsheetTab.tsx` を修正
- 属性に基づいてデータをフィルタリングするための `AttributeFilterDialog.tsx` コンポーネントを追加
- フィルタリングされたビューをサポートするために可視化コンポーネントを強化：
  - フィルターに基づいてポイントをハイライト/薄暗くするように `ScatterChart.tsx` を修正
  - 属性フィルタリングをサポートするように `TreemapChart.tsx` を更新
  - チャートコントロールに属性フィルターボタンを追加
- フィルタリングロジックのための `attributeFilterUtils.ts` にユーティリティ関数を追加

## バックエンド変更点
- "attribute_" プレフィックスを持つ属性フィールドを処理するために <ref_file file="/home/ubuntu/repos/kouchou-ai/server/src/services/report_launcher.py" /> を更新
- <ref_file file="/home/ubuntu/repos/kouchou-ai/server/broadlistening/pipeline/steps/hierarchical_aggregation.py" /> を強化：
  - レポート生成パイプラインで属性データを処理
  - NumPy型のJSONシリアル化を追加
  - CSV出力に属性カラムを含める

## 良い点
- 機能実装はフルスタック全体にわたって包括的
- 属性選択のUIは直感的で既存のワークフローとうまく統合されている
- フィルタリング機能はカテゴリ型と数値型の両方の属性タイプをサポート
- 可視化コンポーネントはフィルタリングされたデータを視覚的な区別で適切に処理
- バックエンド変更は後方互換性を維持

## 改善点
1. **エラー処理**：
   - 属性カラム選択の検証と特殊文字の処理の改善
   - フィルターの無効な数値範囲のエラー状態の追加

2. **パフォーマンスの考慮事項**：
   - 大きな属性リストには仮想スクロールが実装されていますが、多くの属性を持つデータセットには他の最適化が必要かもしれません
   - 非常に大きなデータセットに対する遅延読み込みまたはページネーションの検討

3. **コード構成**：
   - 一部のコンポーネント（`AttributeFilterDialog.tsx`など）はかなり大きく、さらに分割できる可能性があります
   - フィルタリングロジックは複数の場所で重複しており、さらに集中化できる可能性があります

4. **テスト**：
   - この機能のテスト更新は見つかりませんでした
   - 属性フィルタリングロジックの単体テストとUIコンポーネントの統合テストの追加を検討

5. **ドキュメント**：
   - 新しい属性フィルタリング機能のユーザードキュメントを追加
   - 複雑なフィルタリングロジックにコードコメントを追加することを検討

## 推奨事項
1. 異なる属性データ型のエッジケースのエラー処理に対応
2. 新機能の包括的なテストを追加
3. より良いメンテナンス性のために大きなコンポーネントのリファクタリングを検討
4. 属性フィルタリング機能のユーザードキュメントを強化


**コメント:** なし

---

### [PR #531 Review: Attribute Column Selection and Filtering Feature](https://github.com/digitaldemocracy2030/kouchou-ai/issues/551)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-05-21T00:37:42Z  
**内容:**

# PR #531 Review: Attribute Column Selection and Filtering Feature

## Overview
This PR implements attribute column selection and filtering functionality in the kouchou-ai application. It allows users to select attribute columns from CSV/spreadsheet data during import and then filter report visualizations based on these attributes.

## Frontend Changes
- Added new component `AttributeColumnsSelector.tsx` for selecting attribute columns during data import
- Modified `CsvFileTab.tsx` and `SpreadsheetTab.tsx` to integrate attribute column selection
- Added `AttributeFilterDialog.tsx` component for filtering data based on attributes
- Enhanced visualization components to support filtered views:
  - Modified `ScatterChart.tsx` to highlight/dim points based on filters
  - Updated `TreemapChart.tsx` to support attribute filtering
  - Added attribute filter button to chart controls
- Added utility functions in `attributeFilterUtils.ts` for filtering logic

## Backend Changes
- Updated <ref_file file="/home/ubuntu/repos/kouchou-ai/server/src/services/report_launcher.py" /> to handle attribute fields with "attribute_" prefix
- Enhanced <ref_file file="/home/ubuntu/repos/kouchou-ai/server/broadlistening/pipeline/steps/hierarchical_aggregation.py" /> to:
  - Process attribute data in the report generation pipeline
  - Add JSON serialization for NumPy types
  - Include attribute columns in CSV export

## Positive Aspects
- Feature implementation is comprehensive across the full stack
- UI for attribute selection is intuitive and integrates well with existing workflows
- Filtering functionality supports both categorical and numeric attribute types
- Visualization components properly handle filtered data with visual distinctions
- Backend changes maintain backward compatibility

## Areas for Improvement
1. **Error Handling**:
   - Better validation for attribute column selection and handling of special characters
   - Error states for invalid numeric ranges in filters

2. **Performance Considerations**:
   - Virtual scroll is implemented for large attribute lists, but other optimizations may be needed for datasets with many attributes
   - Consider lazy loading or pagination for very large datasets

3. **Code Organization**:
   - Some components (like `AttributeFilterDialog.tsx`) are quite large and could be broken down further
   - Filtering logic is duplicated in a few places and could be further centralized

4. **Testing**:
   - No test updates were found for this feature
   - Consider adding unit tests for attribute filtering logic and integration tests for the UI components

5. **Documentation**:
   - Add user documentation for the new attribute filtering functionality
   - Consider adding code comments for complex filtering logic

## Recommendations
1. Address error handling for edge cases with different attribute data types
2. Add comprehensive tests for the new functionality
3. Consider refactoring larger components for better maintainability
4. Enhance user documentation for the attribute filtering feature


**コメント:** なし

---

### [[FEATURE]windows直環境での起動手順・構成を整備する（python仮想環境＋npm 対応）](https://github.com/digitaldemocracy2030/kouchou-ai/issues/509)

**作成者:** take365  
**作成日:** 2025-05-13T14:28:44Z  
**内容:**

### 🔍 概要
現在の `kouchou-ai` プロジェクトは Linux/Mac 環境での実行を前提にしている部分があり、Windows 環境での手動起動・開発がやや煩雑です。  
この Issue では、Windows 上で仮想環境（Python venv）や npm を活用しながら、直接実行できる構成を整備することを目的とします。

---

### 🧭 背景
- #496 で求められている「すぐに動かせる構成」の一環。
- Windowsユーザーが詰まりやすい起動手順の改善。
- bash系スクリプトを使わずに、`cmd` / `PowerShell` で起動できる手順の整備。

---

### ✅ 対応内容（予定）
- `dev_win_direct.bat` の整備
  - 仮想環境 (`venv`) の `activate` による Python 実行
- `.env` の読み込み自動化（`python-dotenv` などを検討）
- README への起動手順（Windows向け）追記

---

### 🔗 関連PR
- draft: [PR #499](https://github.com/digitaldemocracy2030/kouchou-ai/pull/499)  
  → 本 Issue をもとに今後ブラッシュアップ予定

---



**コメント:** なし

---

### [メンテナ以外が /コマンドで一定のstatus変更をできるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/459)

**作成者:** masatosasano2  
**作成日:** 2025-05-07T12:47:55Z  
**内容:**

# 目的

メンテナの管理コスト削減


# コマンド例
- /ready
- /in_progess
- /wontfix

**コメント:** なし

---

### [[FEATURE]レポート一覧画面：レポート0件時のエンプティ表現をする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/428)

**作成者:** UtkNggc  
**作成日:** 2025-05-04T17:07:41Z  
**内容:**

# 現状
エンジニアさんに調べていただいたところ、
・管理画面（client-admin）では「レポートがありません」が表示される
・ユーザー向け（client）の一覧画面では何も表示されない
<img width="1471" alt="Image" src="https://github.com/user-attachments/assets/dc103f60-8421-4079-b7a3-e09e1887195a" />
<img width="1477" alt="Image" src="https://github.com/user-attachments/assets/f0eeed4d-3dad-4816-ac18-f6d40dc48353" />

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
エンプティには
・現状を知らせる（ユーザーを迷子にしない）
・次のアクションの誘導（行動促進）
・プロダクトに対する信頼獲得
などの役割があります。

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
具体的にはデザイン時に検討したいですが、少なくとも、
・現状を伝える
・エンプティを解消するために何をしたらいいかを伝える
を満たすUIにはしたい。

# 担当デザイナーへ
かけられる開発工数や、ここに到達するユーザーの背景次第で、どれだけリッチにするかが変わります。
なのでそれを踏まえたうえで、
・文字のみ
・文字 + イメージイラスト
・参照できるものがあればそこへのリンク
・ユーザーにとっては使い方の学習の機会にもなるかもしれないため、その観点でデザインにできることがないか
などを検討していただけるといいかも。

**コメント:** なし

---

### [[GITHUB ACTIONS] 開発状況に応じてProjectsのstatusを自動更新する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/425)

**作成者:** masatosasano2  
**作成日:** 2025-05-04T04:31:06Z  
**内容:**

以下の3パターンの更新を自動化したい

| 元のstatus  | きっかけ | 変更後のstatus |
| ------------- | ------------- | ------------- |
| No Status, Cold List, Need Refinement  | Assign | Ready |
| Ready (and assigned)  | Create PR, comment | In Progress |
| In Progress | Unassigned | Ready |

**コメント:** なし

---

### [[FEATURE]ローカル文脈埋め込み（エンベデッド）をもっとアピールする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/414)

**作成者:** take365  
**作成日:** 2025-05-02T07:05:58Z  
**内容:**

# 背景
控えめに追加された、ローカル文脈埋め込み（エンベデッド）が実は精度がよいと思われる。
![Image](https://github.com/user-attachments/assets/39c45b76-9cdb-4f8e-9086-23852dbba806)

![Image](https://github.com/user-attachments/assets/dfea0951-55fe-45aa-9993-9c91fb78fc39)

サンプルデータで１６クラスタ
text-embedding-3-small　 シルエットスコア（まとまりのよさ）：4.25
https://take365.github.io/1d161322-8480-4805-bda4-f7f613540ba2/
https://take365.github.io/evaluation/evaluation_1d161322-8480-4805-bda4-f7f613540ba2.pdf

ローカル               シルエットスコア（まとまりのよさ）：4.69
https://take365.github.io/1d161322-8480-4805-bda4-f7f613540ba2/
https://take365.github.io/evaluation/evaluation_f339b806-773d-47ca-a257-7f43c4748da1.pdf

※私の公開画面が壊れ気味なのは無理やりリンク作ったのでゆるしてください


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
１．AI詳細設定オプションから１つ格上げして、意見グループ数設定と同じレベルにする
２．控えめな文言からもう少しアピールする。

文言の案
＜課金ふれない＞※要約などLLM部分にくらべエンベディングの費用は低く相対的に微差。
サーバ内で埋め込み処理を行う方式です。意見のグループ化や可視化との相性が良く、まとまりのあるクラスタが得られやすい傾向があります（768次元）。
※OpenAIの埋め込みと比較して異なる特性があります。目的に応じてご利用ください。

＜ほどほど＞
APIを使わず、サーバ内で埋め込みを実行します。費用を抑えられるほか、意見のグループ化や可視化において良好な結果が得られるケースもあります（768次元）。
※精度や結果の傾向はモデルにより異なります。用途に応じてお試しください。

＜強気＞
意見の分類・可視化に適した高精度な埋め込みをサーバ内で実行できます。OpenAI APIを使わずに済むため、費用を抑えながらも高い分類性能が期待できます（768次元）。
※OpenAIモデル（1536次元）と比較し、クラスタのまとまりや分離性が良好な場合があります。

**コメント:** なし

---

### [[FEATURE]かかったコストの表示機能](https://github.com/digitaldemocracy2030/kouchou-ai/issues/284)

**作成者:** nishio  
**作成日:** 2025-04-12T23:42:45Z  
**内容:**

# 背景
実行ごとのトークン数やコストが表示されず、利用者がコスト感を把握しにくい。

from 4/12 meetup
>「clineのように実行のたびにトークン、コストが表示されるUIは確かによい(たねのぶ)」
>「使用者にコスト感覚がついていく」


# 提案内容
(解決策) UIに実行ごとのトークン数と推定コストを表示する機能を追加する。

(nishio補足) 実行前に推定費用を表示する案は過去にあった、これは実行後に実際にかかった費用を表示するところが新しい
 - https://github.com/digitaldemocracy2030/kouchou-ai/issues/79

**コメント:** なし

---

### [[REFACTOR] 濃いクラスタのアイコン変更](https://github.com/digitaldemocracy2030/kouchou-ai/issues/113)

**作成者:** nishio  
**作成日:** 2025-03-20T12:20:30Z  
**内容:**

# 現在の問題点

<img width="249" alt="Image" src="https://github.com/user-attachments/assets/bc626d04-e7c0-4245-9b01-e762d433a434" />

濃いクラスタのアイコンは特に意味はなくこれになっている


# 提案内容

多分叩き台の案がないとどう変えたらいいかの議論もできないと思うので雑に描いておく

![Image](https://github.com/user-attachments/assets/9e46dfd6-71d4-4c2b-bbd5-1c79220c8d80)

アイコンとしてデザインできるかは度外視して描くとこんな感じで「全体像」は全体にたくさんの点が散らばっており、「濃いクラスタ」はぎゅっとした「濃い」「密度の高い」塊がいくつかある感じ

**コメント:** なし

---

### 過去7日間に作成されたissue (7件)

### [自動クラスタ数調整機能のベータ評価と継続判断](https://github.com/digitaldemocracy2030/kouchou-ai/issues/577)

**作成者:** coderabbitai[bot]  
**作成日:** 2025-05-27T06:33:50Z  
**内容:**

## 概要

PR #567 で実装された自動クラスタ数調整機能について、ベータ機能としてリリースし、実際の使用状況を観察して継続判断を行う。

## 背景

- APIパラメータが複雑化している
- シルエットスコアに基づく調整が実際にワークするかは不明
- 実際のレポート出力を観察して判断する必要がある

## 実施計画

### フェーズ1: ベータリリース
- [ ] プロダクト上でベータ機能である旨を表示
- [ ] 実際の利用開始

### フェーズ2: 評価期間
- [ ] 出力されるレポートの品質観察
- [ ] ユーザーフィードバックの収集
- [ ] シルエットスコアによる自動調整の効果測定

### フェーズ3: 継続判断
以下のいずれかを実施：
- [ ] 機能がワークしている場合：ベータ表記を削除
- [ ] 機能がワークしていない場合：機能そのものを削除

## 評価期間

TBD（適切な評価期間を設定）

## 関連

- 元PR: https://github.com/digitaldemocracy2030/kouchou-ai/pull/567
- 元コメント: https://github.com/digitaldemocracy2030/kouchou-ai/pull/567#issuecomment-2911274980

リクエスト者: @nasuka

**コメント:** なし

---

### [朝日新聞のTTTC（ブロードリスニング）のプロンプトを取り入れる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/576)

**作成者:** masatosasano2  
**作成日:** 2025-05-26T13:33:27Z  
**内容:**

色々工夫されてるので、真似できるところはしたい。
https://github.com/asahi-research/TTTC_consumption_tax_20250525/tree/main/scatter/pipeline/prompts
- そのまま使えるパターンはまんま流用
- 利用用途が限定されるパターンは一工夫が必要。例：Xの「RT：」の処理用プロンプトは、ソースがXの時だけ差し込む

**コメント:** なし

---

### [[ALGORITHM] PLaMo-Embedding-1Bの動作実験](https://github.com/digitaldemocracy2030/kouchou-ai/issues/573)

**作成者:** tokoroten  
**作成日:** 2025-05-26T08:27:08Z  
**内容:**

# 背景

現在使っているSentenseTransformerはマルチランゲージ対応

PLaMo-Embedding-1Bは日本語特化で作られているので、日本語特化版で性能比較をしたい
https://tech.preferred.jp/ja/blog/plamo-embedding-1b/

現在使われているSentenseTransformerよりも、良い結果が出るのであれば、組み込みembededdingを交換可能にしたい


**コメント:** なし

---

### [[FEATURE] データの有無に応じた UI のパターンを確認しやすくする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/566)

**作成者:** shgtkshruch  
**作成日:** 2025-05-23T09:39:49Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

- データの有無に応じた UI のパータンが増えてきた
  - #428
      - レポートが0件 or 1件以上
  - #438
    - metadata.json のデータの有無
- 自分はこれらの UI パターンを実装する際に、サーバーから取得するデータを変更したり、コード上で条件分岐を変えたりしているのですが、これが少し手間だなと思っています
- デザイナーがデータの有無で表示が切り替わる UI を確認する際にも、データを作ったり or 消したりする必要がありそうです
  - 例えばレポート一覧画面の Empty State を確認する場合は、レポートを0件にするなど


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
- [Storybook](https://storybook.js.org/) でデータがある場合の UI・データない場合の UI を登録して、サーバーのデータを変更することなくそれぞれの UI を確認できるようにする
   - 他にも UI をパターンごとに登録できるツールがあれば、そちらでも良いと思います
   - こういったツールがあると、エンジニアは手軽に手元で UI のパターンを確認できるようになりそうです
   - 導入する場合でも Storybook の実装・メンテナンスコストは多少かかるので、コストとメリットの比較は必要だと思います

# その他
- デザイナーがデータの有無に応じた UI を確認できるようにする場合は、Storybook など UI をカタログ化したものをホスティング環境もあると良さそうです
  - この場合はこの issue の解決が前提になるので、この issue が対応できてから必要があれば別 issue を切るでも良いかなと思いました
   - Chromatic (5000 snapshot まで無料), GitHub Pages, Netlify, etc...

**コメント:** なし

---

### [活用事例を集めて公開する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/564)

**作成者:** shingo-ohki  
**作成日:** 2025-05-23T03:27:56Z  
**内容:**

（[website の Issue](https://github.com/digitaldemocracy2030/website/issues) には存在せず、website は現段階では定例が存在しないため、一旦、広聴AI側で Issue を立ててみる）

# 目的
これから広聴AIを利用しようとするユーザーからすると、様々な活用事例があると導入ハードルが下がる
事例を集めて公開する




**コメント:** なし

---

### [[REFACTOR]  api（server）のテストをしやすいように設計を修正する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/558)

**作成者:** nasuka  
**作成日:** 2025-05-21T12:01:59Z  
**内容:**

# 現在の問題点
* `server` 配下のコードについて、テストコードが書きにくい構成になっている
  * report_status.jsonやレポートの出力フォルダについて実行環境のものが参照されるようになっており、テストコード実装時に意図してmockしないと実行環境のものが編集される可能性がある

# 提案内容
改善案
* TestConfigを作成し、テスト実行時はそちらのconfigを参照する
  * 実装箇所: https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/server/src/config.py
* is_testの環境変数を作成して分岐させる

**コメント:** なし

---

### [[デザイン] アクセシビリティの向上](https://github.com/digitaldemocracy2030/kouchou-ai/issues/556)

**作成者:** masatosasano2  
**作成日:** 2025-05-21T08:45:35Z  
**内容:**

アクセシビリティの向上によって新たに429万人が利用可能になる。

デジタル庁のガイドラインにTODOが非常によくまとまっているので、順次対応したい。
https://www.digital.go.jp/resources/introduction-to-web-accessibility-guidebook

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(10件)

### [[FEATURE]限定公開のページにはnoindexオプションを付ける](https://github.com/digitaldemocracy2030/kouchou-ai/issues/520)

**作成者:** tokoroten  
**作成日:** 2025-05-15T09:24:45Z  
**内容:**

# 背景

限定公開のページであっても、過去に公開していたり、何らかのひょうしにURLが外部に漏れると、ウェブクローラが巡回して拾っていく可能性がある

# 提案内容

限定公開の時はnorobotを付けて、検索エンジン避けをしておく
```html

<meta name="robots" content="noindex" />
```

**コメント:** なし

---

### [ウェルカムミーティングで募集すべき役割を具体化する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/517)

**作成者:** shingo-ohki  
**作成日:** 2025-05-14T11:51:15Z  
**内容:**

募集する役割を整理したほうがいいかも？

- PdM
- フロントエンジニア

>小野翔太
20:48
＞リクルーティングのはなし
コミュニティ運営で、ウェルカムミーティングを開催しようと思っています。そこでつかう資料に、募集をかけるスライドがあるので、そこに載せたいです

from 開発定例

**コメント:** なし

---

### [[design] デザインシステム構築／数値環境](https://github.com/digitaldemocracy2030/kouchou-ai/issues/506)

**作成者:** UtkNggc  
**作成日:** 2025-05-13T12:14:28Z  
**内容:**

https://github.com/digitaldemocracy2030/kouchou-ai/issues/443 で全体の設計ができたので、構築開始できます。
1つ1つのタスクが重いのでIssue分散してます。

このIssueでは、spacing、radius、border、effect、max.min-sizeなどの数値周りの環境を整備します。

## 手順
作業は広聴AIのFigmaファイルで行います。

1. chakraUIの数値情報すべてvariablesで定義
2. 使うものだけ洗い出して作業パネルで呼び出せるように設定
3. そのtokenを使用してstylesに登録
4. Figmaファイル内にガイドライン作成（ブランド思想用ではなくデザイナ&エンジニアが見る用に一覧性のあるもの）

### 期待できる効果

- デザイナーが容易に数値選定できるようになる（エンハンス時の数値の迷いを大幅に削減）
- chakraUI範囲内の数値を使用するため実装がやりやすいのではないか
- 将来的にchakraUIをはがして独自サイズを使うことになったとしてもVariablesの変更ですべて置き換わる

### 留意点
ブランドコンパス内に明記されてるブランドパーソナリティのデザイントンマナを叶える設計にする。
https://www.figma.com/slides/0B55u8rxDjjjpRJbNUEP0Z/%F0%9F%A7%AD-Brand-Compass?t=yLYyNEeIO9pprmn3-6

**コメント:** なし

---

### [[design] デザインシステム構築／Typography環境](https://github.com/digitaldemocracy2030/kouchou-ai/issues/505)

**作成者:** UtkNggc  
**作成日:** 2025-05-13T12:05:53Z  
**内容:**

https://github.com/digitaldemocracy2030/kouchou-ai/issues/443 で全体の設計ができたので、構築開始できます。
1つ1つのタスクが重いのでIssue分散してます。

このIssueではタイポグラフィに関わる環境を整備します。

## 手順
作業は広聴AIのFigmaファイルで行います。

1. chakraUIのタイポ情報すべてvariablesで定義
2. 使うものだけ洗い出してsemantic定義
3. そのtokenを使用してstylesに登録
4. Figmaファイル内にタイポグラフィガイドライン作成（ブランド思想用ではなくデザイナ&エンジニアが見る用に一覧性のあるもの）

### 検討が必要なこと

- 日本語family優先順位の検討（Noto sans, Hiragino Kaku Gothic ProN, YuGothic, Meiryo、など
- 英数字family変える変えない
- size, line-heightの取捨選択

### 期待できる効果

- デザイナーが容易にタイポ選定できるようになる（エンハンス時の色の迷いを大幅に削減）
- chakraUI範囲内の数値を使用するため実装がやりやすいのではないか
- 将来的にchakraUIをはがして独自タイポを使うことになったとしてもVariablesの変更ですべて置き換わる

### 留意点
ブランドコンパス内に明記されてるブランドパーソナリティの「ボイス」を叶える設計にする。
https://www.figma.com/slides/0B55u8rxDjjjpRJbNUEP0Z/%F0%9F%A7%AD-Brand-Compass?t=yLYyNEeIO9pprmn3-6

**コメント:** なし

---

### [[design] デザインシステム構築／color環境](https://github.com/digitaldemocracy2030/kouchou-ai/issues/504)

**作成者:** UtkNggc  
**作成日:** 2025-05-13T11:57:14Z  
**内容:**

https://github.com/digitaldemocracy2030/kouchou-ai/issues/443 で全体の設計ができたので、構築開始できます。
1つ1つのタスクが重いのでIssue分散してます。

このIssueではカラーに関わる環境を整備します。

## 手順

作業は広聴AIのFigmaファイルで行います。

1. chakraUIのカラーたちをすべてPrimitiveにいれる
2. Primitiveから選定してSemanticで定義（実質上のプロダクトカラー）
3. stylesに登録
4. Figmaファイル内にカラーガイドライン作成（ブランド思想用ではなくデザイナ&エンジニアが見る用に一覧性のあるもの）

### 期待できる効果

- デザイナーが容易に色選定できるようになる（エンハンス時の色の迷いを大幅に削減）
- chakraUI範囲内のカラーのため実装がやりやすいのではないか
- 将来的にchakraUIをはがして独自カラーを使うことになったとしてもPrimitiveの変更ですべて置き換わる

### 留意点
ブランドコンパス内のブランドパーソナリティとデザイントンマナを叶える設計にする
https://www.figma.com/slides/0B55u8rxDjjjpRJbNUEP0Z/%F0%9F%A7%AD-Brand-Compass?t=yLYyNEeIO9pprmn3-6

**コメント:** なし

---

### [[ALGORITHM] bonsaiの検証をする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/474)

**作成者:** tokoroten  
**作成日:** 2025-05-10T15:33:22Z  
**内容:**

# 背景

bonsaiという面白そうなツリークラスタリングのアルゴリズムが登場したので実験したい

![Image](https://github.com/user-attachments/assets/5f193a78-4101-4c44-bd07-ed6a2339d813)
https://x.com/DucheneJohan/status/1920819010221769022


https://github.com/dhdegroot/Bonsai-data-representation

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

# 対象データ
<!-- 実験に用いるデータについて記入してください。検討中の場合はその旨を記載してください。 -->


# 実験結果について（実験を実施される方向け）
* 実験結果はこちらの[Google Docs](https://docs.google.com/document/d/1GK4Arh8ZyJmQjQ4iW1CRMruEUPicKAAUZEZi2TpAo4w/edit?tab=t.0#heading=h.j72jxw32gila)に記載してください

**コメント:** なし

---

### [OpenAI APIキーの確保](https://github.com/digitaldemocracy2030/kouchou-ai/issues/464)

**作成者:** nasuka  
**作成日:** 2025-05-08T01:53:19Z  
**内容:**

# 現在の問題点
* OpenAIのAPIキーを使ってイシューにラベリングする仕組みがあるが、現状APIキーがないため動作しなくなっている
https://w1740803485-clv347541.slack.com/archives/C08FL58LK8V/p1746668461239949?thread_ts=1746662038.867129&cid=C08FL58LK8V

# 対策
1. 何らかの方法でAPIキーを確保する（ボードメンバーに打診する等）
2. （無料のものがあれば） OpenAI API以外のLLM APIを使って分類する
3. LLMによる分類は廃止する



**コメント:** なし

---

### [[FEATURE][design] レポート管理画面：直感的に使いやすくしたい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/460)

**作成者:** UtkNggc  
**作成日:** 2025-05-07T16:09:28Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
現状の管理画面は直感的に使いにくい。
あるていど機能がそろった現時点で管理画面を改善したい。

▼現状
![Image](https://github.com/user-attachments/assets/600f5c6f-4dda-4b0d-a272-75088588f063)

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
・機能の見出しを上部バーにまとめる
・各機能ボタンはアイコンやトグルなど直感的にわかるものにする
・新規作成ボタンを右上に移動
・作成日時の秒数トルツメ（もしかすると時間も？）
・レポートのURL表示トルツメ
![Image](https://github.com/user-attachments/assets/3777dc40-ec37-4dd7-ba76-db6323453f23)

# デザイン時に検討するもの
・全レポートをエクスポート機能の位置
・エラー、作成中、のstatesの表現どうするか
・エラー、作成中、のステップの要 / 不要 -> 要るならステップ数やプログレスバーも検討
・もしレポートのURLが必要なら「シェア」みたいな表現でもいいかも。

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/437：見出し文言&位置変更

**コメント:** なし

---

### [[FEATURE][design] コンテンツ下部のAbout情報をFooterにまとめる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/438)

**作成者:** UtkNggc  
**作成日:** 2025-05-06T09:36:29Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
コンテンツエリア内はその画面独自のコンテンツのみにしたい。
About情報はプロジェクト情報なので、footerにまとめるのが適切。

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
Aboutの内容とFooterの内容を組み合わせたfooterを作成する。

※具体的なVDは担当デザイナーが作成します。

**コメント:** なし

---

### [[FEATURE] LLMが出力した結果の手動修正機能（編集機能）がほしい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/310)

**作成者:** nasuka  
**作成日:** 2025-04-15T05:38:53Z  
**内容:**

# 背景
* LLMが出力したクラスタ名や説明、argumentが適切でない場合がある
  * e.g.
    * 公開するのに不適切な単語や表現がクラスタ名に含まれている
    * 他のクラスタと同一の内容がクラスタ名に含まれている
* このようなケースにおいては、LLMのアウトプットを見た後に人間が手動で文言を修正したい

# 提案内容
LLMが出力したテキスト（クラスタタイトル・説明・概要・argument）について、手動で編集する画面をadminに設け、レポートに編集内容を反映する


(admin)
* 上記の編集画面を設ける
  * 編集後のデータを編集用のendpointに送る

(api)
* 編集用のendpointを実装する
  * リクエストで受け取ったデータを各種中間ファイル（args.csv等）に保存
  * hierarchical_aggregation.pyを再度実行し、更新後のデータでhierarchical_result.jsonを保存する

そもそも全要素を編集できるようにするかというのは議論の余地がある。やるとしても、まずはクラスタ名のみを対象にするなど、部分的に始めていくのが良さそう。
また、透明性担保のために編集履歴を残すようにするかも議論の余地がある。

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (16件)

### [Revert "Merge pull request #567 from take365/feature/auto-cluster-clean"](https://github.com/digitaldemocracy2030/kouchou-ai/pull/579)

**作成者:** nasuka  
**作成日:** 2025-05-27T08:58:08Z  
**変更:** +247 -1242 (27ファイル)  
**マージ日:** 2025-05-27T08:58:33Z  
**内容:**

This reverts commit c559f8e256b0966e959140c8dfbe7eeabf96a937, reversing changes made to 196a4534ff71a08bd2cc3c4fe4d21ea4159a26ab.

# 変更の概要
https://github.com/digitaldemocracy2030/kouchou-ai/pull/567
こちらのrevert

# 変更の背景
以下の問題が起きていたのでrevertします

* debug logが大量に出力される
* ファイルによってはembedding実行時に以下のエラーが出る（embedding モデルはopenai）

```
api-1                  | openai.BadRequestError: Error code: 400 - {'error': {'message': "'$.input' is invalid. Please check the API reference: https://platform.openai.com/docs/api-reference.", 'type': 'invalid_request_error', 'param': None, 'code': None}}
```

エラーが起きたのは以下のcsvファイル
https://github.com/team-mirai/random/tree/devin/1747880446-generate-pr-csv/pr_analysis_results/merged

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
	- なし

- **機能変更**
	- レポート作成時の「スキップ」オプションや自動クラスタ数調整機能が削除され、すべての処理ステップが常に実行されるようになりました。
	- AIプロバイダー選択から「使用しない」オプションが削除されました。
	- クラスタ設定が簡素化され、手動でクラスタ数を指定する方式に統一されました。

- **UIの改善**
	- AI設定・クラスタ設定画面がシンプルになり、不要なチェックボックスや入力項目が削除されました。

- **バグ修正**
	- なし

- **ドキュメント**
	- なし

- **その他**
	- 内部処理の簡素化・不要なコードや型定義の削除が行われました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client-admin] コンテンツ量が少ない時でも Footer を画面下部に配置する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/575)

**作成者:** shgtkshruch  
**作成日:** 2025-05-26T09:33:59Z  
**変更:** +3 -0 (1ファイル)  
**マージ日:** 2025-05-26T10:26:30Z  
**内容:**

# 変更の概要
- client-admin で、コンテンツの高さが Window の高さよりも小さい場合でも Footer が画面下部に配置されるようにしました
  - コンテンツの高さが Window の高さよりも大きい場合は、通常通りスクロール可能です

# スクリーンショット
## before
![before](https://github.com/user-attachments/assets/8e641d84-f627-4f28-889e-2ac0de36f518)

## after
![after](https://github.com/user-attachments/assets/67167114-1a21-44e0-98b9-5d8f22bb08d2)

# 変更の背景
- Footer はいつもデバイスの足元にいるという安定感、統一された体験を作るため
- ミニマムで対応するために、global.css に FlexBox のプロパティを追加して対応しました
  - body や container に書かれているスタイルも Chakra UI の Box コンポーネントなどを利用して実装できると良さそうですが、今回の issue の目的とずれてくるので、必要になったタイミングで対応できれば良いかなと思います

# 関連Issue
- fix: #572 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- client-admin でレポートの件数が0件の場合に、footer がページ下部に配置されている
- client-admin でレポートの件数が数件ある状態（コンテンツの高さが Window の高さより大きい）では、通常通りスクロールしてページが閲覧できる

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [ ] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **スタイル**
  - ページ全体のレイアウトが縦方向のフレックスボックスに変更され、コンテンツの配置やスペース配分が改善されました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Cold List に一定期間いるIssueを自動的に Archived にする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/571)

**作成者:** masatosasano2  
**作成日:** 2025-05-24T19:12:22Z  
**変更:** +121 -1 (5ファイル)  
**マージ日:** 2025-05-26T00:19:06Z  
**内容:**

# 変更の概要
- Cold List ステータスのIssuesのうち、最終更新日が指定された日数より前のものを自動的に Archived にする

# 変更の背景
- 対応しないIssueが溜まり続ける事態を避けたい
- Closeすると見落とされるリスクがあるので、念の為closeではなくArchivedステータスにしたい

# 関連Issue
#454 
先にPR #570 がマージされている必要があります

# 動作確認の結果
WIP

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - Issueコメントで「/ready」または「/archive」と入力することで、プロジェクトのステータスを「Ready」または「Archived」に自動更新できるようになりました。

- **ドキュメント**
  - GitHub Actionsによるプロジェクトステータス自動更新の設定手順書を追加しました。
  - PROJECTS.mdに「Archived」ステータスの追加や、コメントコマンドによるステータス更新に関する説明を追記しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [スラッシュコマンドでissueのstatusを更新できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/570)

**作成者:** masatosasano2  
**作成日:** 2025-05-24T18:20:45Z  
**変更:** +69 -7 (4ファイル)  
**マージ日:** 2025-05-26T00:19:04Z  
**内容:**

# 変更の概要
- 「/ready」または「/archive」とコメントすると status を Ready または Archived に更新する

# 変更の背景
- メンテナー以外がステータス更新を判断できることがあるので、更新できるようにしたい
    - 例：デザイン系のサブタスクが完了したので開発可能な状態になった
    - 例：重複Issueの片方を破棄したい
    - 例：Cold List に分類されているIssueが対応不要と確定した

# 関連Issue
#459 
※先にPR #568 をmergeする必要があります

# 動作確認の結果
[/ready](https://github.com/sasa-test-org/kouchou-ai-copy/actions/runs/15229909070)
[/archive](https://github.com/sasa-test-org/kouchou-ai-copy/actions/runs/15229914971)

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - イシューコメントで「/ready」や「/archive」と入力することで、イシューのステータスを「Ready」または「Archived」に自動更新できるようになりました。
  - GitHub Actions ワークフローを追加し、コメント内容に応じたステータス更新処理を自動化しました。

- **ドキュメント**
  - PROJECTS.md に「Archived」ステータスの追加や、ステータス操作方法の説明を追記しました。
  - GitHub Projects のステータス自動更新設定手順をまとめた新しいドキュメントを追加しました。

- **その他**
  - プロジェクトボードの責任者表記を一部修正しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix github actions error, add setup doc md](https://github.com/digitaldemocracy2030/kouchou-ai/pull/568)

**作成者:** masatosasano2  
**作成日:** 2025-05-24T17:25:21Z  
**変更:** +58 -0 (2ファイル)  
**マージ日:** 2025-05-26T00:10:47Z  
**内容:**

# 変更の概要
以下の2点です。
- PR #512 の修正もれのfix
- 設定手順のmdを作成（PR 512に記載されていた内容）

# 変更の背景
- PR 512の作成後にcoderabbitaiの指摘事項に対応した際にデグレードが発生していました
- 設定手順が資料化されていませんでした

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/425
(後続Issue: https://github.com/digitaldemocracy2030/kouchou-ai/issues/454 , https://github.com/digitaldemocracy2030/kouchou-ai/issues/459 )

# 動作確認の結果
[Assign](https://github.com/sasa-test-org/kouchou-ai-copy/actions/runs/15229149314/job/42834885229)、[unassign](https://github.com/sasa-test-org/kouchou-ai-copy/actions/runs/15229154820/job/42834895404) ともに期待通りに動作しました。

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **ドキュメント**
  - GitHub Projectsのステータスフィールドを自動更新するためのセットアップ手順を新たに追加しました。
  - GitHub Appの作成や必要な権限、シークレットの設定方法などを詳細に説明しています。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [LLMのスキップ、自動クラス数決定、タイトル省略](https://github.com/digitaldemocracy2030/kouchou-ai/pull/567)

**作成者:** take365  
**作成日:** 2025-05-23T09:47:35Z  
**変更:** +1242 -247 (27ファイル)  
**マージ日:** 2025-05-27T06:33:48Z  
**内容:**

# 変更の概要

1. グループ数を自動で決定するを追加
2. AIプロバイダーに「使用しない」を追加。（LLM全スキップ）
3. 抽出、初期、統合、要約にスキップを追加
4. タイトル、概要の必須を外し、省略時タイトル自動補完
5. 分析の概要の説明からOpen AIを削除（LLMには触れない）
6. 分析手順でスキップした手順ではモデル表示はスキップ
7. グループ数を自動で決定の場合にグループ数試行結果ボタン・画面表示

# スクリーンショット
1. 
![Screenshot_1](https://github.com/user-attachments/assets/4f9e8867-0dac-45b3-b044-23fcbc6ac746)
2. 
![Screenshot_2](https://github.com/user-attachments/assets/d2a407a0-d188-4eed-8771-36103086fab9)
3. 
![Screenshot_3](https://github.com/user-attachments/assets/5a40ab5e-3e5c-49a9-949b-30e01bf1194e)
4. 
![Screenshot_5](https://github.com/user-attachments/assets/c4dfff8b-213e-4695-a4ed-c6b43b9e6acf)
5. 
![Screenshot_6](https://github.com/user-attachments/assets/de6249da-53ce-4477-adde-ce03348d9d8e)
6. 
![Screenshot_8](https://github.com/user-attachments/assets/09017439-e726-40bd-93d2-6e94a43fdd30)
7. 
![image](https://github.com/user-attachments/assets/df27af90-82ab-45b5-bf94-4dc71285c9bc)

# 変更の背景
- イシュー対応

# 関連Issue
- (情報整理)試行錯誤の負担を減らす [#221](https://github.com/digitaldemocracy2030/kouchou-ai/issues/221)
- [BUG] OpenAI API以外のLLMを使っても、OpenAI APIを利用したと表示される [#494](github.com/digitaldemocracy2030/kouchou-ai/issues/494)
-[FEATURE]CSVアップロード時にタイトルや説明文を自動で埋めてほしい [#305](https://github.com/digitaldemocracy2030/kouchou-ai/issues/305)
-[ALGORITHM]クラスタ数、エンベディング、次元圧縮の違いのモデルの違いによるシルエットスコア（まとまり具合）の変化の調査 [#516](https://github.com/digitaldemocracy2030/kouchou-ai/issues/516)

# 動作確認の結果
・各種スキップ状態でレポート作成
・自動クラスタでレポート作成
・フィルター機能確認

# CLAへの同意
- [X ] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ X] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - レポート作成時にスキップフラグや自動クラスタリング設定をAPIに渡すオプションを追加しました。
  - 自動クラスタリングの有効化やクラスタ範囲設定（Lv1, Lv2）を導入しました。
  - AIモデル未使用の設定（"none"）を追加し、その場合はAI処理をスキップします。
  - 自動クラスタリング結果の可視化やシルエットスコアの表示機能を追加しました。

- **改善**
  - タイトルや紹介文の未入力時に自動生成される仕組みを導入しました。
  - クラスタ範囲やクラスタ数の入力値バリデーションを強化し、不正値時に警告を表示します。
  - ステップのスキップ状態やAIモデル名がタイムライン上でわかりやすく表示されるようになりました。

- **バグ修正**
  - トークン数超過の入力に対し、自動でトークナイズし長さを調整する処理を追加しました。

- **ドキュメント**
  - 各設定項目に対する説明やヘルプテキストを追記しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [グラフ選択の UI を Figma と揃える](https://github.com/digitaldemocracy2030/kouchou-ai/pull/563)

**作成者:** shgtkshruch  
**作成日:** 2025-05-22T09:53:04Z  
**変更:** +2 -2 (1ファイル)  
**マージ日:** 2025-05-22T10:14:15Z  
**内容:**

# 変更の概要
- スマホサイズの SegmentControl の高さが Figma と異なっていたので、修正しました
- Figma: https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=48-14037&t=193sCKxfNOY0fQKb-0

# スクリーンショット
## before
![image](https://github.com/user-attachments/assets/18a75ad4-007b-42f0-8d75-a60d71094332)


## after

![image](https://github.com/user-attachments/assets/7044847e-c693-4168-a08a-35308924204e)


# 変更の背景
- https://github.com/digitaldemocracy2030/kouchou-ai/pull/531/ で、SegmentControl の高さがずれていた不具合を修正した際にスマホ時の高さがを考慮する指定がなくなったため

# 関連Issue
https://dd2030.slack.com/archives/C08F7JZPD63/p1747901201788969?thread_ts=1747883068.322639&cid=C08F7JZPD63

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

画面サイズをスマホサイズにして、Figma と同じ高さの SegmentControl になっていることを確認しました。

ここに関連する箇所の以前の PR で意図しないデザインの崩れがあったので、念の為レビュアーの方のローカルでも表示を確認していただけると嬉しいです :pray:

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **スタイル**
  - セグメントグループの高さがレスポンシブになり、小さい画面では80px、大きい画面では56pxに調整されました。
  - 内部アイテムの高さが親コンテナに合わせて自動調整されるようになりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[FEATURE] 文字列の検索によるフィルタを実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/561)

**作成者:** nsk.smn+Devin  
**作成日:** 2025-05-22T06:41:44Z  
**変更:** +169 -72 (8ファイル)  
**マージ日:** 2025-05-22T07:57:03Z  
**内容:**

# [FEATURE] 文字列の検索によるフィルタを実装

Fixes #560

## 変更内容

- 既存の「属性フィルタ」ダイアログ内に文字列検索フィールドを追加
- 「属性フィルタ」の名称を「フィルタ」に変更
- 文字列検索フィルタのロジックを実装
  - 大文字/小文字を区別せず、部分一致で検索
  - 引数の「argument」フィールド（意見の内容）に対して検索
  - 文字列検索と属性フィルタは論理AND条件で結合

## テスト内容

- 「全体」「濃い意見」セクションでの文字列検索機能の動作確認
- 文字列検索単体での動作確認
- 文字列検索と属性フィルタの組み合わせでの動作確認

Link to Devin run: https://app.devin.ai/sessions/99e1c9ed71044e81807acae974aed745


**コメント:** なし

---

### [レポート一覧画面に Empty State を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/557)

**作成者:** shgtkshruch  
**作成日:** 2025-05-21T09:06:46Z  
**変更:** +67 -30 (4ファイル)  
**マージ日:** 2025-05-21T14:31:50Z  
**内容:**

# 変更の概要
- client, client admin でレポートが0件の場合の表示（Empty State）を Figma のデザインに合わせて実装しました
- Figma: https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=166-6&t=jloyS7fu33z6K5Lk-11

# スクリーンショット
## client

### 375px
![image](https://github.com/user-attachments/assets/f365963b-b286-4d05-982d-e0f31f5ba80c)


### 768px
![image](https://github.com/user-attachments/assets/2581c3fb-61be-4193-8127-d2debec913eb)


## client-admin
### 375px
![image](https://github.com/user-attachments/assets/567c79b3-2ccf-438d-b680-5074e4823eb5)


### 768px
![image](https://github.com/user-attachments/assets/7595b2fa-a1fa-4c34-bf41-dd2e7d371e44)


# 変更の背景
- Empty State で現在の状態をユーザーに伝えるテキストが不足していた


# 関連Issue
- fix: #428 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

client, client-admin のレポート一覧画面で、取得するレポートが0件の場合に Figma のような UI になることを確認しました

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - レポートが存在しない場合に、イラストと説明文、レポート作成ページへのボタンを含む新しい空状態表示（EmptyState）が追加されました。

- **改善**
  - レポート一覧ページの見出しが「レポート管理」から「レポート一覧」に変更されました。
  - レポートがない場合の表示がテキストのみから、より分かりやすいデザインに変更されました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix: report_status.jsonを上書きするテストを削除](https://github.com/digitaldemocracy2030/kouchou-ai/pull/555)

**作成者:** mtane0412  
**作成日:** 2025-05-21T02:51:59Z  
**変更:** +0 -64 (1ファイル)  
**マージ日:** 2025-05-21T03:32:48Z  
**内容:**

test-slug データが report_status.json に書き込まれる問題を修正しました。
実装内容
最新のmainブランチから新しいブランチ devin/fix-test-slug-leak-latest を作成し、`test_update_token_usage.py` に teardown_method を追加しました：
def teardown_method(self):
    """各テスト後に_report_statusをクリア"""
    _report_status.clear()
この修正により、テスト実行後に _report_status グローバル変数がクリアされ、テストデータが本番環境に漏れることを防ぎます。
実装状況
- 最新のmainブランチから新しいブランチを作成
- test_update_token_usage.py に teardown_method を追加
- 変更を devin/fix-test-slug-leak-latest ブランチにコミットしてプッシュ
- :x: PRの作成（コマンドが失敗）

次のステップ
GitHub上で手動でPRを作成していただくか、以下のURLから直接ブランチを確認できます：
https://github.com/digitaldemocracy2030/kouchou-ai/tree/devin/fix-test-slug-leak-latest
修正内容は test_update_token_usage.py に実装されています。
Devinセッション
この作業は https://app.devin.ai/sessions/7408ab9acf194f3eb709d0c7c5f844a0 で行われました。
[11:49](https://dd2030.slack.com/archives/C08PRQVQWSE/p1747795779395259?thread_ts=1747792798.579469&cid=C08PRQVQWSE)
追加の検証結果
コードベース全体を検索した結果、`_report_status` グローバル変数を操作しているのは test_update_token_usage.py のみであることを確認しました。また、`update_token_usage` 関数を呼び出しているのも同じファイルのみです。
これにより、今回実装した修正（`teardown_method` の追加）が問題を完全に解決することが確認できました。テスト実行後に _report_status がクリアされるため、test-slug データが本番環境に漏れることはなくなります。
修正内容は既に devin/fix-test-slug-leak-latest ブランチにプッシュされています。GitHub上でPRを作成していただければ、この修正をmainブランチにマージできます。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **テスト**
  - `update_token_usage` 関連のテストスイートを削除しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [npm run format](https://github.com/digitaldemocracy2030/kouchou-ai/pull/554)

**作成者:** nishio  
**作成日:** 2025-05-21T02:21:51Z  
**変更:** +38 -24 (1ファイル)  
**マージ日:** 2025-05-21T02:25:38Z  
**内容:**

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **スタイル**
  - コードの可読性向上のため、フォーマットやインデントを整理しました。機能や画面表示に変更はありません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [デザイン変更: セグメントビューでの全体・濃い意見・階層の切り替え機能](https://github.com/digitaldemocracy2030/kouchou-ai/pull/550)

**作成者:** shgtkshruch  
**作成日:** 2025-05-20T12:13:32Z  
**変更:** +177 -71 (3ファイル)  
**マージ日:** 2025-05-21T01:47:15Z  
**内容:**

# 変更の概要
- https://github.com/digitaldemocracy2030/kouchou-ai/pull/487 を引き継いで、チャートの切り替え UI を Figma のデザインをもとに実装しました

# スクリーンショット

figma のデザインにある画面幅に設定して、スクリーンショット撮っています 📷 
https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=171-2&t=GXKzpACguMXTJ59Z-0

## 375px
![image](https://github.com/user-attachments/assets/83f31382-fca2-4693-873e-4a18f3ed031c)

## 768px
![image](https://github.com/user-attachments/assets/1bbfcc29-fec9-4082-8062-012fcf86a095)

## 1280px
![image](https://github.com/user-attachments/assets/956398a3-c245-4840-85d8-b7165b39c394)


# 変更の背景
- Chakra UI の Segment Control コンポーネントを使いつつ、Figma のデザインに合わせて実装しています
  - Figma: https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=171-2&t=GXKzpACguMXTJ59Z-0
- ブレイクポイントは Chakra UI のデフォルトのものを使用しています
  - https://www.chakra-ui.com/docs/theming/breakpoints
- Chakra UI の styel props に配列を渡すと上記ブレイクポイントごとに切り替わるので、この機能を使ってレスポンシブ対応をしています
  - https://v2.chakra-ui.com/docs/styled-system/responsive-styles

# 関連Issue
- fix: https://github.com/digitaldemocracy2030/kouchou-ai/issues/113

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

Google Chrome でレポート詳細画面開いて、ブラウザ幅を変更して Figma のデザインように UI が切り替わることを確認しました。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [ ] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - チャートの表示切替ボタンに新しいセグメントコントロールUIを導入し、選択肢ごとにアイコンを追加しました。
  - 新しいアイコン（全体表示、密集表示、階層表示）を追加しました。

- **改善**
  - チャート切替UIのレイアウトと操作性を向上し、選択肢の動的生成やツールチップ表示に対応しました。
  - レイアウト調整により、チャート概要部分の余白を縮小しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [レポートページに推定コスト表示機能を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/549)

**作成者:** 種延真之+Devin  
**作成日:** 2025-05-20T11:32:07Z  
**変更:** +433 -8 (9ファイル)  
**マージ日:** 2025-05-25T14:56:53Z  
**内容:**

# レポートページに推定コスト表示機能を追加

## 概要
Issue #284 の実装として、レポートページにLLMの使用コスト（推定）を表示する機能を追加しました。トークン使用量と同様に、レポート作成中にリアルタイムで更新され、プロバイダーとモデル情報も合わせて表示されます。

## 変更内容

### バックエンド
- `LLMPricing`サービスを新規作成し、各プロバイダー・モデルの最新料金情報を定義
  - OpenAI (gpt-4o-mini, gpt-4o, o3-mini)
  - Azure OpenAI
  - OpenRouter
- レポートスキーマに推定コスト、プロバイダー、モデル情報のフィールドを追加
- レポート作成中にリアルタイムで推定コストを計算する機能を実装
- レポート作成過程でプロバイダーとモデル情報を保持する仕組みを追加
- `LLMPricing`サービスのユニットテストを実装

### フロントエンド
- レポートカードに推定コスト表示を追加（`$1.2345 (OpenAI GPT-4o-mini)`形式）
- レポート作成中のポーリングで推定コスト、プロバイダー、モデル情報を取得・表示
- レポート完了後も推定コストとプロバイダー・モデル情報を保持して表示

## 動作確認
- トークン使用量と同じくリアルタイムで更新されることを確認
- 推定コスト情報がないレポートは「情報なし」と表示
- OpenAI + GPT-4o-miniの組み合わせで正常に動作することを確認

## スクリーンショット
![推定コスト表示のスクリーンショット](https://github.com/user-attachments/assets/4d4fb551-d9f1-4af5-9143-8b682df5b0b4)

## 関連Issue
Closes #284

## Devinセッション
https://app.devin.ai/sessions/85a9f2748ead4343ba46d0795f960e3c


**コメント:** なし

---

### [意見グループのタイトル・説明を手動で編集できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/545)

**作成者:** nasuka  
**作成日:** 2025-05-20T04:31:31Z  
**変更:** +1600 -126 (22ファイル)  
**マージ日:** 2025-05-24T07:07:26Z  
**内容:**

# 変更の概要
* 出力済みのレポートに対して、意見グループのタイトル・説明を編集する機能を実装

# スクリーンショット
![60fead70df97d60ba2ff8cc81ecffbbd](https://github.com/user-attachments/assets/eedddfcb-bacc-4745-9727-6f2d4b82cf0c)


# 変更の背景
* LLMが出力したクラスタ名や説明、argumentが適切でない場合があるので、出力後に手動で修正したい
  * e.g.
    * 公開するのに不適切な単語や表現がクラスタ名に含まれているケース
    * 他のクラスタと同一の内容がクラスタ名に含まれているケース

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/310

# 動作確認の結果
* クラスタのタイトル・説明が編集できる
  * 第1階層・第2階層それぞれ確認
* レポート作成が実行できる
  * レポート作成に関連する関数も少し修正しているため確認

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。



# 実装方針に関する補足

実装方針および検討した内容の詳細は以下のコメントに記載。
最終的に、以下のような更新を実施するアプローチを採用している。

1. クラスタラベルの中間ファイル（hierarchical_merge_labelling.pyの成果物）を更新
2. そのうえで `hierarchical_result.json` （フロントで描画に使われるjsonファイル） を更新

ファイル更新なので、例えば複数のユーザーが同一のクラスタのタイトル・説明を同時に編集しているような場合は不整合が起きうる（後に更新した人の内容だけが反映される可能性がある）。
一方で、DB導入については上記のイシューにコメントしたようなハードルがあり、また上記のリスクがあるとしてもこの機能によって得られる便益が大きいので、今回はそのリスクを許容してでもこの機能をマージしたほうが良いと考えています。
https://github.com/digitaldemocracy2030/kouchou-ai/issues/310#issuecomment-2888243252

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - レポートカードに「意見グループを編集する」機能を追加し、意見グループ（クラスタ）のタイトルや説明を管理画面から編集可能に。
  - クラスタ編集用ダイアログを実装し、階層レベルやクラスタの選択・編集ができるようになりました。
  - レポート設定の更新APIが追加され、設定内容の管理が強化されました。

- **バグ修正**
  - レポート設定編集時のAPIエンドポイントおよびリクエスト項目名が変更されました（title/description → question/intro）。

- **ドキュメント**
  - クラスタ関連およびレポート設定に関する型定義・スキーマを新規追加。

- **テスト**
  - クラスタ編集機能と関連APIエンドポイントの単体テストを新規追加。

- **その他**
  - キャッシュ無効化処理をパスベースからタグベースへ変更し、効率的なキャッシュ管理を実現。
  - 内部処理のファイルパスを絶対パス化し、安定性を向上。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [属性フィルタ機能の実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/531)

**作成者:** tokoroten  
**作成日:** 2025-05-17T22:10:05Z  
**変更:** +2203 -903 (22ファイル)  
**マージ日:** 2025-05-22T06:10:26Z  
**内容:**

# 変更の概要
- アップロード時に後でスライスするための属性カラムを指定できる
- サーバでの処理の最後に、もともとの属性カラムを結合する
- クライアントで属性カラムをフィルターをかけることを可能にする

## 属性フィルタ付きのサンプルデータ
https://gist.github.com/tokoroten/0115947bc25a53caa53d2f1e55a0b1df

# スクリーンショット
## アップロード時の分析用カラム
![image](https://github.com/user-attachments/assets/317badba-80a4-4eca-87e0-8110f7b477b2)


## クライアントでの属性スライサー
![image](https://github.com/user-attachments/assets/d488ff3f-c276-44f1-8493-07c24aeadbd0)

![image](https://github.com/user-attachments/assets/70d70bd7-ac4a-47cc-9fad-082188d9eee1)

## 属性スライス結果

![image](https://github.com/user-attachments/assets/702d26b0-337b-48bc-b1d0-e861e470f5bb)


# 変更の背景
- どのような属性の人がどこの意見にいるのかの分布を見たい
- 年齢・性別・職業・支持政党などでフィルターが行えると、政党は選挙キャンペーンの意思決定が行いやすくなる

# 関連Issue
#281

# 動作確認の結果
とりあえず動いている

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認を行っても良いですが、動作確認は必須ではありません。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - CSVやスプレッドシートから複数の属性カラムを選択できるUIを追加しました。
  - 属性ごとの値でデータを絞り込むフィルタダイアログを新設しました。
  - 属性フィルタと密度フィルタを組み合わせてチャートやレポートを動的に絞り込めるようになりました。
  - 散布図やツリーマップに属性フィルタ結果を反映し、フィルタ対象外のデータをグレーアウト表示で区別できるようになりました。
  - 属性フィルタの適用状態をチャートやUIコンポーネント間で同期し、操作性を向上しました。

- **改善**
  - コメントやレポートに属性情報が保持され、より柔軟な分析が可能になりました。
  - 大規模属性値リストの表示に仮想化技術を導入し、UIパフォーマンスを向上しました。

- **依存関係**
  - UI高速化のため `react-window` を追加しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [デザイン変更: セグメントビューでの全体・濃い意見・階層の切り替え機能](https://github.com/digitaldemocracy2030/kouchou-ai/pull/487)

**作成者:** nsk.smn+Devin  
**作成日:** 2025-05-12T06:27:57Z  
**変更:** +178 -71 (5ファイル)  
**マージ日:** 2025-05-21T01:47:17Z  
**内容:**

# デザイン変更: セグメントビューでの全体・濃い意見・階層の切り替え機能

## 変更内容
- セグメントビューを使用して全体・濃い意見・階層のビュー切り替え機能を実装
- 新しいカスタムアイコンを作成（全体、濃い意見、階層）
- Chakra UIのカラーパレット（gray.100, gray.200, gray.500）を使用
- モバイル表示では縦積みレイアウトに対応
- デスクトップ表示では横並びレイアウトに対応

## デザイン意図
- 「ビューの切り替え機能」だと伝えるためにセグメントビューに変更
- 「当たり前に押す機能」としてアピールするため中央配置 & やや大きめサイズ
- 本プロダクトのキモとなる機能のため1つ1つを主張させるためアイコンで表現

## 実装詳細
- Chakra UIのsegmented-controlコンポーネントを使用
- カスタムアイコンを新規作成
- レスポンシブデザインに対応（モバイルでは縦積み、デスクトップでは横並び）

Link to Devin run: https://app.devin.ai/sessions/8b3acd70772247219783e236a211bc16
Requested by: nsk.smn@gmail.com


**コメント:** なし

---

### 過去7日間に作成されたPR (5件)

### [自動クラスタ数調整機能にベータ表記を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/578)

**作成者:** nasuka  
**作成日:** 2025-05-27T06:53:01Z  
**変更:** +36 -33 (3ファイル)  
**内容:**

# 変更の概要
*自動クラスタ数調整機能にベータ表記を追加
* 一部ファイルに対して npm run format を適用

# スクリーンショット
![image](https://github.com/user-attachments/assets/e13ffec0-8f63-41a8-a017-641a7c66f9f8)


# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/577


# 動作確認の結果
・表記が反映されていることを確認
・レポート出力が実行できることを確認

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **スタイル**
  - クラスタ数自動決定のチェックボックスラベルに「（ベータ版機能）」の表記を追加しました。

- **リファクタ**
  - コスト計算処理を最適化し、パフォーマンス向上のためフックの依存関係を整理しました。
  - 一部のインポート文やコードの整形を行い、可読性を向上させました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [限定公開のレポートでは検索エンジンにインデックスされないようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/574)

**作成者:** shingo-ohki  
**作成日:** 2025-05-26T08:48:51Z  
**変更:** +170 -7 (6ファイル)  
**内容:**

# 変更の概要
- タイトル通り

# 関連Issue
#520 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- 限定公開に設定されたレポートページに、`<meta name="robots" content="noindex, nofollow">` が追加されることを確認
- 限定公開されていたページを公開ページにした場合に上記が削除されることを確認

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - レポートの可視性（public/unlisted/private）がAPIレスポンスやクライアントで明示的に表示されるようになりました。
  - 「unlisted」レポートの場合、検索エンジンによるインデックスやリンク追跡が無効化されます。

- **バグ修正**
  - レポートの可視性に応じた適切なエラーメッセージやステータスコードが返されるようになりました。

- **テスト**
  - レポートの可視性や存在しないレポートに関するテストケースが追加・強化されました。

- **その他**
  - 一部型定義の整理とテスト設定の柔軟性が向上しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [スラッシュコマンドでstatusを更新する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/569)

**作成者:** masatosasano2  
**作成日:** 2025-05-24T18:06:15Z  
**変更:** +54 -1 (2ファイル)  
**内容:**

# 変更の概要
- 「/ready」または「/archive」とコメントすると status を Ready または Archived に更新する

# 変更の背景
- メンテナー以外がステータス更新を判断できることがあるので、更新できるようにしたい
    - 例：デザイン系のサブタスクが完了したので開発可能な状態になった
    - 例：重複Issueの片方を破棄したい
    - 例：Cold List に分類されているIssueが対応不要と確定した

# 関連Issue
#459 

# 動作確認の結果
WIP

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

**コメント:** なし

---

### [Draft/221 auto cluster and skip](https://github.com/digitaldemocracy2030/kouchou-ai/pull/565)

**作成者:** take365  
**作成日:** 2025-05-23T03:45:03Z  
**変更:** +842 -169 (22ファイル)  
**内容:**

 #221 自動クラスタ設定＋スキップ設定＋省略タイトル補完
 のドラフト
 
 
# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

**コメント:** なし

---

### [フィルタアイコンの件数カウントにテキスト検索を含める](https://github.com/digitaldemocracy2030/kouchou-ai/pull/562)

**作成者:** nsk.smn+Devin  
**作成日:** 2025-05-22T07:09:14Z  
**変更:** +63 -12 (4ファイル)  
**内容:**

# [FEATURE] フィルタアイコンの件数カウントにテキスト検索を含める

Fixes #560

## 変更内容

- フィルタアイコンの件数カウントにテキスト検索を含めるように修正
  - `showAttentionFilterBadge` の条件に `textSearch.trim() !== ""` を追加
  - `attentionFilterBadgeCount` の計算に `textSearch` が空でない場合の処理を追加

## テスト内容

- テキスト検索を適用した場合にフィルタアイコンのバッジカウントが増加することを確認
- テキスト検索を削除した場合にバッジカウントが減少することを確認
- 属性フィルタと組み合わせた場合も正しくカウントされることを確認

Link to Devin run: https://app.devin.ai/sessions/99e1c9ed71044e81807acae974aed745


**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(2件)

### [windows直環境対応#](https://github.com/digitaldemocracy2030/kouchou-ai/pull/524)

**作成者:** take365  
**作成日:** 2025-05-15T16:39:27Z  
**変更:** +208 -0 (2ファイル)  
**内容:**

# 変更の概要
Windows 環境で Docker を使用せずに開発環境を構築・起動する手順をまとめた Markdown ファイルを新たに追加しました。
起動用のdirect_start_win.batを追加しました
検証・開発用途を想定しており、非推奨構成として experimental 配下に配置しています。
pdm を利用しつつ pyproject.toml に準拠したセットアップ手順を記載しています。
.env の分割処理や各サービスの依存ライブラリインストール方法を明記しました。


当初はご提案いただいたとおり、rye + make を使った構成に合わせようと検討しましたが、以下の理由から今回は断念し、代替手段として pdm ベースでの手順を採用しました。

rye の実行ファイルは、インストール時にセキュリティ警告を無視する必要があり、加えて Windows 環境での実行にはセキュリティ設定の調整が必要となる場面がありました。
make も別途 exe をダウンロードし、Path に追加する必要がありますが、最終的には rye に依存するため、初心者や非エンジニアにとっては敷居が高い構成になってしまうと判断しました。
.env の分割処理などもバッチスクリプトで補完する必要があり、結果的に純粋な make ベースの恩恵が限定的である点も考慮しました。
そのため、server 側では pyproject.toml を活かしつつも、pdm を使ったセットアップに調整しています。
また、report_launcher.pyの変更は起動時の仮想環境を引き継げていたため取り下げました。
なお、この手順は「非推奨手順」として kouchou-ai/experimental/direct_win に配置し、軽量な検証や個人開発向けの補助的な位置づけとして取り扱っています。


# スクリーンショット
- UIなし

# 変更の背景
- issu対応

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/509
https://github.com/digitaldemocracy2030/kouchou-ai/pull/499

# 動作確認の結果
pdm で作った仮想環境を使いつつ起動、レポート作成の完了。

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [x ] 単体テストが実装されているか
- [x ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。




- [x ] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **ドキュメント**
  - Windows環境でDockerを使わずに開発環境を構築するためのユーザーガイドを追加しました。

- **新機能**
  - Windows向けの環境構築・起動用バッチスクリプトを追加しました。複数サービスの起動や環境変数の自動設定が可能です。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [レビューのガイドラインを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/457)

**作成者:** nasuka  
**作成日:** 2025-05-07T12:27:49Z  
**変更:** +26 -0 (2ファイル)  
**内容:**

# 変更の概要
* メンテナー向けのレビューガイドラインを追加
* レビューのトータルコストを下げるために、PRテンプレートに以下を追加
  * レビュー前のチェックリスト
  * `動作確認の結果 ` の項目を追加

# 変更の背景
何がクリアされていればマージしてよいのか、基準が明文化されていないため、レビュー時にメンテナーが判断に迷う場面があった

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/456

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **Documentation**
  - Enhanced the pull request template with sections for documenting test results and a pre-merge checklist to ensure thorough verification.
  - Updated review guidelines to emphasize system improvement over perfection and clarified when to request changes or approve pull requests.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

