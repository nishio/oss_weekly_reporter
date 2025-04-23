# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-04-16 から 2025-04-23 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (2件)

### [OGPタグを書く](https://github.com/digitaldemocracy2030/polimoney/issues/13)

**作成者:** takahiroanno  
**作成日:** 2025-04-21T12:09:52Z  
**内容:**

- SNSでURLをシェアしたとき、OGPカードとして表示されるようにしたい
  - 画面中央のサンキーダイアグラムが見える
  - 議員の名前が見える

**コメント:** なし

---

### [LICENSE / CLAを書く](https://github.com/digitaldemocracy2030/polimoney/issues/12)

**作成者:** takahiroanno  
**作成日:** 2025-04-21T12:09:03Z  
**内容:**

diitaldemocracy2030/kouchou-ai に準拠で良い

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (7件)

### [Add LICENSE file (AGPL-3.0)](https://github.com/digitaldemocracy2030/polimoney/pull/14)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-21T12:14:09Z  
**変更:** +661 -0 (1ファイル)  
**マージ日:** 2025-04-21T12:15:16Z  
**内容:**

# Add LICENSE file

This PR adds the GNU Affero General Public License v3 (AGPL-3.0) to the repository as requested in issue #12.

The license is the same as the one used in digitaldemocracy2030/kouchou-ai.

Link to Devin run: https://app.devin.ai/sessions/61fd23ca07404b8bac16a95fba4f07ab
Requested by: annyotaka@gmail.com


**コメント:** なし

---

### [jsonスキーマを採用](https://github.com/digitaldemocracy2030/polimoney/pull/11)

**作成者:** shumizu418128  
**作成日:** 2025-04-20T11:05:13Z  
**変更:** +6 -1 (1ファイル)  
**マージ日:** 2025-04-23T02:10:50Z  
**内容:**

Gemini APIにある、出力をJSONに固定できる機能の実装です。
https://ai.google.dev/gemini-api/docs/structured-output?hl=ja&lang=python

※意図してこれを採用していなかった場合は、このプルリクを消していただいて構いません。

これを採用する場合、
- clean_response (19行目～) がおそらく不要になります。
- まれに出力がjsonにならない（カンマ忘れなど）ことがありますが、数回再試行させるとだいたい直ります。
  - 再試行させるコードを書いてもいいと思います。現状1回問題があると即エラーを出しているようです。
- [出力形式をプロンプトではなくpythonのクラスで指定できます。](https://ai.google.dev/gemini-api/docs/structured-output?hl=ja&lang=python#supply-schema-in-config)プロンプトでも指定可能ですが、こちらのほうがより出力形式が安定します。

**コメント:** なし

---

### [Update: 支出を表すアイコンを`BanknoteArrowUpIcon`から`BanknoteArrowDownIcon`に変更](https://github.com/digitaldemocracy2030/polimoney/pull/10)

**作成者:** yoshimatsu567  
**作成日:** 2025-04-19T15:30:56Z  
**変更:** +8 -2 (1ファイル)  
**マージ日:** 2025-04-21T06:06:10Z  
**内容:**

## 変更の概要
支出を表すアイコンを `BanknoteArrowUpIcon` から `BanknoteArrowDownIcon` に変更しました。

Lucide Icons のドキュメントに `BanknoteArrowUpIcon` は主に「収入（income）」、`BanknoteArrowDownIcon` は「支出（expense）」を示す旨の記載があったので、本PRを作成しました。


## 変更箇所のスクリーンショット
| before | after |
| ------ | ----- |
|![image](https://github.com/user-attachments/assets/f2792e28-47b6-49e7-9ba8-94ff9b81940e)        |![image](https://github.com/user-attachments/assets/9a029bdf-0ab8-4cfa-8126-51ee90c7bc7e)       |
|![image](https://github.com/user-attachments/assets/507fa8f0-3131-429f-b267-b2b26b57b7ae)|![image](https://github.com/user-attachments/assets/b4e99407-5288-44d1-897a-a8453c7cc58c)|


## 参照
- [BanknoteArrowUpIcon – Lucide Icons](https://lucide.dev/icons/banknote-arrow-up)
- [BanknoteArrowDownIcon – Lucide Icons](https://lucide.dev/icons/banknote-arrow-down)


---

Polimoney を拝見していて気になった点をPRとして上げさせていただきました。
不要な変更であればそのままクローズいただいて構いません🙇‍♂️
ご確認のほど、よろしくお願いいたします。


**コメント:** なし

---

### [Update: アイテムカテゴリを増やした](https://github.com/digitaldemocracy2030/polimoney/pull/9)

**作成者:** jujunjun110  
**作成日:** 2025-04-19T01:42:54Z  
**変更:** +12 -4 (2ファイル)  
**マージ日:** 2025-04-19T01:43:01Z  
**内容:**

内容なし

**コメント:** なし

---

### [Feature/improve gemini format](https://github.com/digitaldemocracy2030/polimoney/pull/8)

**作成者:** jujunjun110  
**作成日:** 2025-04-18T00:48:54Z  
**変更:** +1430 -153 (8ファイル)  
**マージ日:** 2025-04-18T00:49:22Z  
**内容:**

* Geminiの書き出しフォーマット改善
* Geminiの実行を並列化
* Geminiの書き出した多数のjsonをmergeするミニスクリプトを追加

**コメント:** なし

---

### [Feature/pdf2image2gemini](https://github.com/digitaldemocracy2030/polimoney/pull/7)

**作成者:** nanocloudx  
**作成日:** 2025-04-17T06:41:24Z  
**変更:** +391 -0 (7ファイル)  
**マージ日:** 2025-04-17T06:41:36Z  
**内容:**

内容なし

**コメント:** なし

---

### [可視化にデータを繋ぎこむ処理を実装](https://github.com/digitaldemocracy2030/polimoney/pull/6)

**作成者:** spinute  
**作成日:** 2025-04-14T20:28:30Z  
**変更:** +863 -0 (3ファイル)  
**マージ日:** 2025-04-16T05:43:50Z  
**内容:**

https://w1740803485-clv347541.slack.com/archives/C08FL5L6GSH/p1744618040915549 のもの

- 現サイトは example.ts に書いてある固定のサンプルデータを表示している
- これを実データに切り替えるために、支出報告書から抽出したデータから、可視化用データを作成したい。convert.ts はこの変換処理を（現状ざっくり）実装している
- 使い方：`node --experimental-strip-types generator.ts -i sample_input.json -o sample_output.json`
    - 今は CLI から実行する作りになっているので、抽出→変換→可視化が繋がって動くようにする必要もある
- 入力形式は完全には確定しておらず、データ抽出処理と細部のすり合わせが必要
    - 基本的には `{ year: number, categories: InputCategory[], transactions: InputTransaction[] }` 型のデータがあれば可視化用のデータを作れる
    - transactions の細かい入れ方は、自信ないのでとりあえず決め打ちで validation をたくさん入れてある。すり合わせが必要
        - 「翌年度への繰越」を transaction として明に含むか、transactions には含まずに収支の差から計算するか、等
}`
- 出力形式は example.ts の型に合わせている
    - `{ summary: Summary, flows: Flow[], incomeTransactions: Transaction[], expenseTransactions: Transaction[] }`

**コメント:** なし

---

### 過去7日間に作成されたPR (2件)

### [docstring整備](https://github.com/digitaldemocracy2030/polimoney/pull/16)

**作成者:** shumizu418128  
**作成日:** 2025-04-23T03:08:21Z  
**変更:** +22 -5 (1ファイル)  
**内容:**

ドキュメントのみ追加しました。コードの変更はありません。

個人的には詳細な説明は理解の助けになると考えているため、もしよければ今後も機能改修と並行してドキュメント作成を進めていきたいと思います。

なお、`analyze_image_with_gemini` (32行目) については、既存のドキュメントと実際のコード実装に齟齬があったため、正確な内容に修正しています。

**コメント:** なし

---

### [Add CLA and PR template](https://github.com/digitaldemocracy2030/polimoney/pull/15)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-21T12:18:50Z  
**変更:** +70 -0 (2ファイル)  
**内容:**

# Add CLA and PR template

This PR adds:
1. Contributor License Agreement (CLA.md) based on the reference from takahiroanno2024/policy-repository
2. PR template for manifest changes (.github/PULL_REQUEST_TEMPLATE/manifest_pull_request_template.md)

Resolves issue #12 (LICENSE / CLAを書く)

Link to Devin run: https://app.devin.ai/sessions/61fd23ca07404b8bac16a95fba4f07ab
Requested by: annyotaka@gmail.com


**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

