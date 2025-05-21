# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-05-14T12:26:30.658584+09:00 から 2025-05-21T12:26:30.658584+09:00 まで

## Issues

### 過去7日間に完了されたissue (7件)

### [PythonコードのLintが通るようにする](https://github.com/digitaldemocracy2030/polimoney/issues/64)

**作成者:** dotneet  
**作成日:** 2025-05-15T11:17:30Z  
**内容:**

今後徐々にシステムが複雑化していくと思うので、linterの恩恵が十分に受けられるようにしておきたい。
ruffのツールは導入したが、エラーが多いためチェックは無効かしている状態。

pyproject.toml でruffのチェックを有効化する。

```toml
[tool.ruff.lint]
select = ["ALL"]
```

下記のコマンドでチェックが通るようにする。

`poetry run ruff check .`


**コメント:** なし

---

### [TypeScriptのフォーマッターの導入](https://github.com/digitaldemocracy2030/polimoney/issues/54)

**作成者:** dotneet  
**作成日:** 2025-05-12T08:00:00Z  
**内容:**

biomeかprettierを導入してコードフォーマットが個々の環境に依存しないようにしたいです。
[kouchou-ai](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/biome.json) では biome 使ってますし、eslintをはずして biome にするのが良さそうな気がしますがどうでしょう。



**コメント:** なし

---

### [検索結果のサムネイルを差し替える](https://github.com/digitaldemocracy2030/polimoney/issues/46)

**作成者:** adust09  
**作成日:** 2025-05-07T14:27:14Z  
**内容:**

検索結果一覧に表示されるサムネイルが出井さんになっている
当プロジェクトを公共性の高いものとするために別の画像に差し替えることが望ましい。

![Image](https://github.com/user-attachments/assets/addd73ff-f66d-4c54-931a-f5c4c83c1e95)

以下のような点から議論をスタートすると良さそう

- 現段階で適当なサムネ画像があるか？
- 現在のOGP画像で代替するか？
- サムネイルやアイコンを新規デザインするか？



**コメント:** なし

---

### [Pythonのlinter、formatterを導入する](https://github.com/digitaldemocracy2030/polimoney/issues/34)

**作成者:** tdaira  
**作成日:** 2025-04-30T14:02:35Z  
**内容:**

- linter、formatterを導入する
- 型チェック等はまず入れてみて少しずつオプションを増やしていく方針にする

**コメント:** なし

---

### [devcontainerを設定する](https://github.com/digitaldemocracy2030/polimoney/issues/25)

**作成者:** adust09  
**作成日:** 2025-04-27T04:40:52Z  
**内容:**

# Devcontainerの導入

## 概要
開発環境の統一とセットアップの簡略化のため、devcontainerを導入する

## 目的
- チーム全員が同じ開発環境で作業できるようにする
- 新規開発者のオンボーディングを簡略化する
- CI/CD環境との一貫性を確保する

## タスク
- [x] `.devcontainer`ディレクトリの作成
- [x] `devcontainer.json`の設定
  - Node.js 20の環境設定
  - 必要なVS Code拡張機能の設定
  - 自動フォーマットの設定
  - etc
- [x] `Dockerfile`の作成
- [x] READMEの作成

**コメント:** なし

---

### [総務省ウェブサイトからの政治資金収支報告書PDF自動取得機能](https://github.com/digitaldemocracy2030/polimoney/issues/4)

**作成者:** Olemi-llm-apprentice  
**作成日:** 2025-04-12T07:21:37Z  
**内容:**

**背景:**
政治資金収支報告書の分析には、まず総務省のウェブサイトから対象となる報告書の PDF ファイルを入手する必要があります。現在は、以下のページから手動で目的の団体を探し、PDF をダウンロードする必要があります。

*   参照サイト: [政治資金収支報告書（令和6年11月29日公表（令和5年分定期公表））](https://www.soumu.go.jp/senkyo/seiji_s/seijishikin/reports/SS20241129/)

この手作業は、特に多数の団体を対象とする場合、非常に時間がかかり非効率です。

**課題:**

*   総務省のウェブサイト構造を解析し、目的の団体の報告書 PDF へのリンクを特定する必要がある。
*   ウェブサイトは団体種別（政党本部、政党支部、資金管理団体など）や、あいうえお順のインデックスで構成されており、目的の団体を見つけるために複数のページをナビゲートする必要がある場合がある。
*   手動でのダウンロードは時間と手間がかかる。

**提案:**
総務省のウェブサイトをクローリングし、指定された条件に基づいて政治資金収支報告書の PDF ファイルを自動でダウンロードするスクリプト機能を追加します。

1.  **ウェブスクレイピングの実装:**
    *   Python ライブラリ（例: `requests`, `BeautifulSoup4`）を使用して、上記の総務省のウェブサイトを解析します。
2.  **対象指定機能:**
    *   コマンドライン引数や設定ファイルで、ダウンロード対象とする報告書の公表年、団体種別（政党本部、支部、資金管理団体、その他の政治団体）、特定の団体名などを指定できるようにします。
3.  **リンク探索とダウンロード:**
    *   指定された条件に基づき、ウェブサイトのリンクをたどり、該当する団体の報告書 PDF へのリンクを特定します。
    *   特定したリンクから PDF ファイルをダウンロードし、分かりやすい命名規則（例: `報告年_団体名_種別.pdf`）で指定されたディレクトリに保存します。
4.  **負荷への配慮:**
    *   総務省サーバーへの過度な負荷を避けるため、リクエスト間に適切な待機時間（例: `time.sleep()`）を設けます。また、総務省の `robots.txt` や利用規約を尊重します。

**期待される効果:**
政治資金収支報告書 PDF の収集プロセスが自動化され、分析作業の準備にかかる時間と手間が大幅に削減される。

**担当者:** (任意)
**ラベル:** enhancement, web scraping, data acquisition, automation

**コメント:** なし

---

### [Gemini API呼び出しの並列化とエラーハンドリング強化（レートリミット対応）](https://github.com/digitaldemocracy2030/polimoney/issues/3)

**作成者:** Olemi-llm-apprentice  
**作成日:** 2025-04-12T07:16:30Z  
**内容:**

**背景:**
`analyze_image_gemini.py` は、1枚ずつ画像を Gemini API に送信して解析を実行します。多数の画像ページ（PDFから変換されたものなど）を処理する場合、この逐次処理は全体の完了までに非常に長い時間がかかります。また、API 呼び出しはネットワークエラーや API 側のレートリミット（利用制限）などにより失敗する可能性があります。

**課題:**

1.  **処理時間の長さ:** 多数の画像を処理する際の全体的なスループットが低い。
2.  **レートリミットエラー:** Gemini API のレートリミットに達した場合、処理が中断してしまう。
3.  **一時的なエラー:** ネットワークの不安定さなどによる一時的なエラーが発生した場合、処理が失敗してしまう。

**提案:**
スクリプトのパフォーマンスと安定性を向上させるために、以下の改善を実装します。

1.  **並列処理の実装:**
    *   複数の画像解析リクエストを同時に Gemini API へ送信できるように、並列処理（マルチスレッド、マルチプロセス、または非同期処理）を導入します。Python の `concurrent.futures` や `asyncio` ライブラリの活用を検討します。
    *   並列度（同時に実行するリクエスト数）を設定可能にし、実行環境や API の制限に応じて調整できるようにします。
2.  **レートリミット対応:**
    *   Gemini API からレートリミットエラー（例: HTTP 429 Too Many Requests）が返された場合に、処理を即座に中断するのではなく、一定時間待機してからリクエストを再試行するロジック（例: Exponential Backoff）を実装します。
3.  **リトライ処理の強化:**
    *   レートリミット以外の特定の一時的なエラー（ネットワークエラーなど）に対しても、リトライ処理を実装します。
4.  **エラーハンドリングの改善:**
    *   リトライしても最終的に失敗したリクエストや、その他の予期せぬエラーが発生した場合でも、全体処理が停止しないようにエラーハンドリングを強化します。失敗した画像とその理由を記録し、後で確認できるようにします。

**期待される効果:**

*   複数の画像ファイルを処理する際の全体的な実行時間が大幅に短縮される。
*   API のレートリミットや一時的なネットワークエラーに対する耐性が向上し、スクリプトの安定性が向上する。
*   エラーが発生した場合でも、成功した処理は維持され、失敗した処理を特定しやすくなる。

**担当者:** (任意)
**ラベル:** enhancement, performance, error handling, api


**コメント:** なし

---

### 過去7日間に作成されたissue (2件)

### [Github Discusisonを有効にする](https://github.com/digitaldemocracy2030/polimoney/issues/69)

**作成者:** adust09  
**作成日:** 2025-05-20T08:57:30Z  
**内容:**

#30 や #31 のように議論が中心のissueは[Github Discussion](https://docs.github.com/ja/discussions)にて行う方が良いと思う。

そもそもこのような議論はcloseするのが難しいうえ、常にオープンにしておくほうがOSS精神的に良い。
(polimoneyに限らずdd2030全体で採用していいかも)

また、ユーザーが使っていく中で欲しい機能が提案・実装されることもあるだろう。
例えば[Roo Code](https://github.com/RooVetGit/Roo-Code/issues
)ではissueタブから`Feature Request`を押すとDiscussionページに遷移し、そこで提案・議論することができる。投票機能もあって非常に便利

https://github.com/user-attachments/assets/26b40f6d-5c46-4f22-900b-9e7de9967e9c




**コメント:** なし

---

### [PRIVACY.mdを策定する](https://github.com/digitaldemocracy2030/polimoney/issues/63)

**作成者:** adust09  
**作成日:** 2025-05-15T02:45:53Z  
**内容:**

## 解決・改善したいこと

#30 に関連してプライバシーポリシーを説明するためのファイルを用意する

## 具体的な実現方法・実装方法の概要（未記入でも構いません）
- 個人情報の扱いについて記載する


**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(8件)

### [CONTRIBUTING.mdを作成する](https://github.com/digitaldemocracy2030/polimoney/issues/51)

**作成者:** adust09  
**作成日:** 2025-05-12T02:04:44Z  
**内容:**

CONTRIBUTING.mdとはOSSへコミットする際のissue作成やPR作成の手順を記した文書である。
issue templateやPR templateが[用意](https://github.com/digitaldemocracy2030/polimoney/pull/49)されたので、コントリビューションガイドも提供したい。

参考：https://zenn.dev/wakamsha/articles/encouragement-of-contributing-guide

**コメント:** なし

---

### [対内外向け[資料作成]](https://github.com/digitaldemocracy2030/polimoney/issues/40)

**作成者:** cKinu  
**作成日:** 2025-05-02T18:22:55Z  
**内容:**

**改善施策として資料作成をする目的:**
- 内からの訴求内容の一律
- 外からのツールを見た上での解釈揃え

**目標:**
- ユーザー
> - 国民の信頼につながる、政治献金につながる、手軽に導入できる
- ビューアー
> - 政治資金の関心深度とツール利活用の向上、推し活政治版（献金する）

**Todo:**
作成ツール: figma, GoogleSlide
- [ ] ポンチ絵　プロジェクト向け
- [ ] 営業資料　ユーザー向け
- [ ] プレゼン資料　ビューアー向け

**各種資料作成（イメージ案）**
Shimizuさんスライドとサイトを元に、必要ポイントをそれぞれにフォーカスした資料を作成
- ポンチ絵
> - 他のプロジェクトを踏襲し手書きなどの簡潔版
> - 担当のアイコンと立ち位置図をマトリクス表にペタペタ
- 営業資料（ユーザー向け）
> - ユーザーに刺さるメリット
> - 利用条件（スプシ使ってね）
> - 導入事例（ストーリー仕立て）
- プレゼン資料（ビューアー向け）
> - ユーザーへのメリット
> - 自分ごとに出来るような仕掛け
> - ストーリー仕立て
> - よくあるXの漫画広告形式とか？（推し活想定に因んで）

**コメント:** なし

---

### [データベース移行](https://github.com/digitaldemocracy2030/polimoney/issues/32)

**作成者:** nanocloudx  
**作成日:** 2025-04-30T13:49:38Z  
**内容:**

既に公開している数件のデータはデモとして GitHub Pages に公開している
今後の流れとしてより沢山のデータを扱うことを見越して、データを Postgres に記録していく

同様にレポートは「ブラウザ→API→Postgres」からデータを取得して表示する仕組みに変更する

**コメント:** なし

---

### [議論：収支報告書に不記載(裏金)の情報について](https://github.com/digitaldemocracy2030/polimoney/issues/31)

**作成者:** nanocloudx  
**作成日:** 2025-04-30T13:35:30Z  
**内容:**

現時点のポリマネーは収支報告書に記載されている内容を見やすくすることを目的としている
元データである収支報告書に記載されていないものは当然掲載することができない
不記載(裏金)の情報に対するアプローチ（？）をどうするかという意見があった

**コメント:** なし

---

### [議論：個人献金の個人情報を隠す必要性について](https://github.com/digitaldemocracy2030/polimoney/issues/30)

**作成者:** nanocloudx  
**作成日:** 2025-04-30T13:32:33Z  
**内容:**

個人からの献金の場合、収支報告書に名前や住所が記載されている
ポリマネーにおいてはこれを伏せるべきではないかという提案があった

**コメント:** なし

---

### [E2E動作確認（つなぎこみ）](https://github.com/digitaldemocracy2030/polimoney/issues/29)

**作成者:** nanocloudx  
**作成日:** 2025-04-30T13:26:32Z  
**内容:**

精度は悪くても良いので（OCR結果が間違っていることを許容して）、Gemini読み込みからHTML出力までを繋ぎこむ


**コメント:** なし

---

### [収支報告書のフォーマット調査](https://github.com/digitaldemocracy2030/polimoney/issues/20)

**作成者:** shumizu418128  
**作成日:** 2025-04-24T16:28:40Z  
**内容:**

## 背景
政治資金収支報告書は、提出先（各都道府県の選挙管理委員会、総務省）や報告主体（政党、資金管理団体、その他の政治団体など）によってフォーマットが異なることが分かっています。

このフォーマットの多様性は、OCRによる報告書の自動読み取りを進める上で大きな障壁となっています。

## 目的

- **フォーマットの網羅的調査**: 全国の都道府県、国レベルで提出される収支報告書、および団体の種類（政党本部・支部、資金管理団体、その他の政治団体等）によるフォーマットの違いを調査し、実例を収集します。

- **パターン化・分類**: 収集したフォーマットを分析し、共通点、相違点、特有のレイアウトなどを特定し、体系的にパターン化・分類します。

- **課題の理解深化**: 報告書フォーマットの現状を把握することで、データ化における技術的課題や、報告書作成者（政治家側）・利用者（国民側）双方にとっての潜在的な課題（分かりにくさ、比較の難しさ等）への理解を深めます。

- **OCR精度向上の基盤構築**: 特定されたフォーマットパターン情報を、将来的なデータ抽出ロジックの改善に活用します。

## 具体的なタスク

- **情報収集**:
  - 各都道府県の選挙管理委員会、総務省のウェブサイト等を調査し、公開されている政治資金収支報告書のPDFファイルや様式テンプレートを収集します。（例: 「〇〇県 政治資金収支報告書」、「総務省 政治資金収支報告書」等のキーワードで検索）

- **フォーマット分析**:
  - 収集した報告書の構成要素（表紙、収入、支出、資産等の各項目、明細書など）を確認します。
  - レイアウト、記載項目、様式番号（例: 様式その〇〇）の違いを比較・分析します。
  - 特にOCR処理で問題となりそうな箇所（罫線の有無・種類、手書き箇所の多さ、特有の注釈など）に注目します。

※ なんとなくの感想程度で構いません。**ハイレベルな文を書くより、収支報告書とかいう謎文書の手ごわさを理解するほうが大事**だと思います。

- **結果の整理・文書化**:
  - 特定したフォーマットパターンごとに、特徴、出典（都道府県/国、団体種類、年度）、該当する様式のサンプル画像（またはファイルへのリンク）を整理します。

整理した情報は、**[TODO: 記録先未定 提案募集中]** に記録します。

---

めっちゃGeminiに手伝ってもらいましたが、このissueは一応 @shumizu418128 自分で書いています。
本件は私のタスクに直結するので、現時点で本件の主担当は私 @shumizu418128 です。

polimoneyのコンセプトに対する理解への貢献、取り組みやすさの観点から、これはgood first issueになると思います。

**コメント:** なし

---

### [OCR（画像認識）の精度強化](https://github.com/digitaldemocracy2030/polimoney/issues/19)

**作成者:** shumizu418128  
**作成日:** 2025-04-23T14:10:03Z  
**内容:**

ただのメモ
4/23現在、OCR・Geminiまわりの担当は清水のみです
 
### なるべく処理ログを残す
  - どの座標をどんな文字と認識したのか記録
  - 合計金額を計算し記録（「小計」の活用）
  - 手書き文字・訂正印が邪魔で読みにくい部分を記録
  - 備考などのイレギュラー対策の検討
  - 必要に応じて画像をトリミング

目標：バグ発生時の迅速な対応を実現する

### json形式の統一
  - DBとのやりとりはPinさん担当なので相談する
  - 上記処理ログ含め残したい


[参考：4/23 ミーティングログ](https://docs.google.com/document/d/19Kn6ekK3twMVcVaSyUgptvmfzrXEJezA6GXTbPXjm9M/edit?tab=t.0)

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (20件)

### [pythonのlefthook対応とlint error修正](https://github.com/digitaldemocracy2030/polimoney/pull/73)

**作成者:** dotneet  
**作成日:** 2025-05-20T11:13:27Z  
**変更:** +54 -52 (8ファイル)  
**マージ日:** 2025-05-20T11:26:52Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->

 - 既存のpython lint errorを修正します。
 - lefthook により自動的に lint check と format を行うようにします

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **スタイル**
  - 複数のPythonファイルで、文字列やリストのフォーマットを簡潔な単一行に統一し、コードの可読性を向上しました。

- **チョア**
  - Pythonコードの自動整形とフォーマットをpre-commitフックに追加しました。
  - 開発用依存関係として`lefthook`を追加しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [analyze_image_gemini.py に並列数をコマンドライン引数で渡せるようにした](https://github.com/digitaldemocracy2030/polimoney/pull/72)

**作成者:** dotneet  
**作成日:** 2025-05-20T10:59:38Z  
**変更:** +9 -2 (1ファイル)  
**マージ日:** 2025-05-20T11:05:27Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->

 - analyze_image_gemini.py に並列数をコマンドライン引数で渡せるようにした

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

 - #3 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - 並列処理に使用するスレッド数を指定できる `--workers`（省略形 `-w`）オプションをコマンドライン引数に追加しました。デフォルト値はシステムのCPU数に基づいて自動設定されます。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix pdf downloader: カテゴリ名のより正確な抽出](https://github.com/digitaldemocracy2030/polimoney/pull/71)

**作成者:** dotneet  
**作成日:** 2025-05-20T10:53:00Z  
**変更:** +27 -8 (3ファイル)  
**マージ日:** 2025-05-20T11:05:44Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->

 - PDFダウンロード時にファイル名として使うカテゴリ名を間違えることがる不具合の修正

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - 新しいカテゴリ「資金管理団体」が追加されました。

- **改善**
  - PDFリンクのカテゴリ判定が、より詳細なURL情報に基づいて行われるようになりました。
  - ツールのREADMEに、自動修正付きのリンター実行コマンドが追加されました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [add biomejs.biome to extensions.json](https://github.com/digitaldemocracy2030/polimoney/pull/70)

**作成者:** dotneet  
**作成日:** 2025-05-20T10:29:24Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-05-20T11:03:50Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->

 - extensions.json に biome を追加

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **Chores**
  - 推奨されるVSCode拡張機能に「biomejs.biome」を追加しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [converter.ts でエラーを許容するフラグの実装](https://github.com/digitaldemocracy2030/polimoney/pull/68)

**作成者:** dotneet  
**作成日:** 2025-05-19T13:57:33Z  
**変更:** +56 -17 (2ファイル)  
**マージ日:** 2025-05-19T14:08:44Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->

 - converter.ts で一部のエラーがあってもJSON出力できるようにします
 - https://github.com/digitaldemocracy2030/polimoney/issues/29#issuecomment-2888866886 への対応です。フラグを指定するとエラーメッセージは出力しますが、JSON出力可能なエラーであればJSONの出力を行うことができます。

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [一時的なOGP画像を設定](https://github.com/digitaldemocracy2030/polimoney/pull/67)

**作成者:** dotneet  
**作成日:** 2025-05-19T04:18:51Z  
**変更:** +3 -0 (2ファイル)  
**マージ日:** 2025-05-19T07:05:02Z  
**内容:**

# 変更の概要

 - 一時的なOGP画像を設定(正式なものではありません)

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->


# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

 - #46 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - ページのOpen Graph情報に画像が追加され、SNS等でのシェア時にサムネイル画像が表示されるようになりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [E2E - Geminiプロンプト新設](https://github.com/digitaldemocracy2030/polimoney/pull/66)

**作成者:** shumizu418128  
**作成日:** 2025-05-18T08:52:38Z  
**変更:** +83 -20 (3ファイル)  
**マージ日:** 2025-05-18T08:52:46Z  
**内容:**

# 変更の概要
1. 該当年度の取得をするため、表紙に対して専用プロンプトの新設
2. 複数ページに対して個別にgeminiにid付与をさせていた影響で、idの重複が発生していた問題の修正

なお、表紙からとるべき情報はまだあるので、まだ改善が必要です。

# 変更の背景
E2E実現に向けた問題の修正です。
なお、Geminiの精度のおかげでだいぶいい感じのデータが出せるようになりましたが、収入と支出の合計値が合わず、これだけではまだエラーが出る状況です。

[出力のall.json](https://github.com/user-attachments/files/20271928/all.json)

# 関連Issue
#29 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - 画像ファイル名からページ番号を判別し、1ページ目専用のプロンプトを用いて年を抽出する機能を追加しました。

- **ドキュメント**
  - JSONデータのID付与ルールや例を明確化し、IDの一貫性に関する説明を改善しました。
  - 年度抽出用プロンプトの説明と例を追加しました。
  - 関数の説明ドキュメントを追加しました。

- **バグ修正**
  - JSONマージ時、カテゴリや取引名の先頭の数字・記号を正規表現で除去し、正しく正規化されるように改善しました。
  - 年度の決定方法を修正し、最初のファイルから取得するようにしました。
  - カテゴリや取引が存在しない場合でも安全にマージできるように修正しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [ruffのチェックを有効にする](https://github.com/digitaldemocracy2030/polimoney/pull/65)

**作成者:** dotneet  
**作成日:** 2025-05-17T03:10:57Z  
**変更:** +799 -496 (14ファイル)  
**マージ日:** 2025-05-17T10:19:01Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
 - ruff check が通るようにしました。
 - ruffのルールは[こちら](https://zenn.dev/spectee/articles/spectee-ruff-rule)やcoderabbitの指摘を参考にして絞りました。ALLで通るところまで一度修正しましたが、細かい指摘が多くそこそこ不毛に感じるところがありました。
 - analyze_image_gemini.py をリファクタしました。
 - merge_jsons.py, pdf_to_images.py はいったん ruff check を無効にしました。短いスクリプトなのであまりlint頑張る必要が今のところないと思うので。

analyze_image_gemini.py は修正前と同様に動作することを確認済みです。

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

 - #64 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

## Summary by CodeRabbit

- **新機能**
  - 画像解析ツールにGemini APIを用いた画像解析機能を追加しました。
  - 画像処理、ファイル入出力、エラーハンドリング機能をモジュール化し、CLIから一括実行できるようになりました。
  - 日本の政治資金報告書画像からテキストを抽出し、指定形式のJSONで出力するプロンプトを追加しました。

- **バグ修正**
  - ダウンローダーの一部例外型やパラメータ名の統一、型ヒントの修正を行いました。

- **ドキュメント**
  - 一部スクリプトに日本語の説明文を追加しました。

- **スタイル**
  - Ruffリントの設定を調整し、特定ファイルで警告を無効化しました。

- **リファクタリング**
  - 画像解析スクリプトを簡素化し、主要な処理を外部モジュールに委譲しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [TypeScriptのLintエラー修正](https://github.com/digitaldemocracy2030/polimoney/pull/62)

**作成者:** dotneet  
**作成日:** 2025-05-14T14:59:00Z  
**変更:** +2 -6 (2ファイル)  
**マージ日:** 2025-05-15T10:54:22Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->

 - lintエラーの修正です
 - lint導入と同時にたくさんマージしたのでlintがかかってないコードがmergeされてました。

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **スタイル**
  - 設定ファイルのインデントや配列のフォーマットを統一し、読みやすくしました。ユーザーの操作や機能に影響はありません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Pythonコードのフォーマット](https://github.com/digitaldemocracy2030/polimoney/pull/61)

**作成者:** dotneet  
**作成日:** 2025-05-14T14:53:53Z  
**変更:** +139 -79 (3ファイル)  
**マージ日:** 2025-05-15T10:54:46Z  
**内容:**

# 変更の概要

 - 導入したruffでフォーマットしただけです。それ以外の修正はありません。
 - fix #34 

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **スタイル**
  - コードの可読性向上のため、文字列のクォートやコメント、インデント、空白などのスタイルを統一しました。
  - ログメッセージや例外処理のフォーマットを整理し、長い行を複数行に分割しました。
  - 引数定義や辞書リテラルの記述方法を簡潔かつ一貫性のある形式に変更しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [政治資金収支報告書一括ダウンロード機能](https://github.com/digitaldemocracy2030/polimoney/pull/60)

**作成者:** dotneet  
**作成日:** 2025-05-14T11:54:30Z  
**変更:** +2655 -7 (19ファイル)  
**マージ日:** 2025-05-15T10:55:26Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
 - #4 への対応

lintエラーは #62 のPRで治ります。

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

 - #4

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

## Summary by CodeRabbit

- **新機能**
  - 日本の政治資金報告書PDFを自動ダウンロードするツールを追加しました。年・団体カテゴリ・名称による絞り込み、進捗バー、エラーハンドリング、メタデータ管理、robots.txt準拠、ダウンロード遅延設定などに対応しています。
- **ドキュメント**
  - ダウンローダーツールの詳細なREADMEと使い方を追加しました。
  - ツール全体のREADMEにダウンロード手順を追記しました。
- **依存関係**
  - 必要な外部ライブラリ（beautifulsoup4、tqdm、requests、pytest）を追加しました。
- **テスト**
  - メタデータ管理・PDFダウンロード機能の単体テストとテスト用フィクスチャを追加しました。
- **その他**
  - .gitignoreを追加し、不要なファイル・フォルダの管理を除外しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [pythonにruff, pyrightを導入](https://github.com/digitaldemocracy2030/polimoney/pull/59)

**作成者:** dotneet  
**作成日:** 2025-05-14T05:35:22Z  
**変更:** +134 -4 (5ファイル)  
**マージ日:** 2025-05-14T13:46:27Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
 - type checkerの導入(pyright)
 - linter, formatterの導入(ruff)
 - CIでの上記のチェック

ruffのルールはいったん適用なしにしてます。
かなりエラーが多いので全部有効にして ignore で対処する方法も使いづらいため。

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

 - コードの保守性向上のため

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

 - #34

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - Pythonコードの自動リントおよび型チェック用のGitHub Actionsワークフローを追加しました。
  - VS Code向けに「charliermarsh.ruff」拡張機能の推奨を追加しました。

- **ドキュメント**
  - コード品質維持のためのlint・format・型チェックコマンドの利用方法をREADMEに追記しました。

- **チョア**
  - 開発用依存関係としてruffおよびpyrightを追加し、関連設定を更新しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [update readme](https://github.com/digitaldemocracy2030/polimoney/pull/58)

**作成者:** dotneet  
**作成日:** 2025-05-14T03:48:23Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-05-14T04:02:21Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->

npm install できないため

**コメント:** なし

---

### [Biome + lefthookの導入](https://github.com/digitaldemocracy2030/polimoney/pull/57)

**作成者:** dotneet  
**作成日:** 2025-05-12T13:20:22Z  
**変更:** +2010 -4847 (31ファイル)  
**マージ日:** 2025-05-14T13:47:13Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->

fix #54 

 - Biomeとlefthookの導入
 - ESLintの削除(BiomeにLint機能があるため)
 - anyがエラーになってしまうので、いったん warn にしてあります。anyへの対応は進めるとしても別途PRでよいかと思い、いったんそこは保留にしてます。

フォーマット後サイトがちゃんと動くことを確認済みです。

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

フォーマッターがなく個々人の環境でソースのフォーマットが変わってしまうため。

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

 - #54 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [analyze_image_gemini.py のエラーハンドリング改善](https://github.com/digitaldemocracy2030/polimoney/pull/55)

**作成者:** dotneet  
**作成日:** 2025-05-12T10:48:11Z  
**変更:** +200 -42 (3ファイル)  
**マージ日:** 2025-05-14T13:57:43Z  
**内容:**

 - #3 関連の対応です。すべてが終わったわけではありません。エラーハンドリングのみの対応です。
 - loggingの導入(printもloggingに切り替え)
 - 一部のエラーを最大5回まで指数バックオフでリトライするように変更
 - エラーが発生した項目は error_log.json に出力して、すべての実行完了後に確認可能

下記、確認済みです。
・リトライが実行されること
・エラーのアイテムが error_log.json に吐き出されること
・これまで通り正常に画像からJSONファイルに変換できること


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - 画像解析ワークフローにエラー追跡・ログ保存機能を追加しました。
- **バグ修正**
  - API呼び出し時のリトライ処理とエラーハンドリングが強化され、信頼性が向上しました。
- **ドキュメント**
  - エラーや警告がより詳細なログとして記録されるようになりました。
- **その他**
  - 必要な依存パッケージとして tenacity が追加されました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [pinact runでバージョンをコミットハッシュにする](https://github.com/digitaldemocracy2030/polimoney/pull/50)

**作成者:** hatsu38  
**作成日:** 2025-05-10T15:49:14Z  
**変更:** +9 -9 (2ファイル)  
**マージ日:** 2025-05-14T13:46:52Z  
**内容:**

- git tagは変更可能なためセキュリティのリスクもあります
- 先日 [tj-actions/changed-files](https://github.com/tj-actions/changed-files) ではいくつものタグが特定の悪意ある コミットハッシュに置き換えられてしまう事案がありました
  - https://www.stepsecurity.io/blog/harden-runner-detection-tj-actions-changed-files-action-is-compromised
- GitHub CI/CD実践ガイドという本 にも、gitのコミットタグは可変なため、コミットハッシュで固定するのを推奨しています
- そこで  [pinact run](https://github.com/suzuki-shunsuke/pinact) コマンドを実行してバージョンをコミットハッシュに置き換えました


コミットハッシュによって最新のパッチバージョンを利用するためにはバージョンアップの必要がありますが、dependabot  などでそれほど不可なくバージョンの更新はしていけると思います。
その面倒さ以上に、セキュリティリスクの高さが上まると考えて、PRを提出しました。


**コメント:** なし

---

### [E2E - merge_jsons.py変更](https://github.com/digitaldemocracy2030/polimoney/pull/48)

**作成者:** shumizu418128  
**作成日:** 2025-05-07T15:02:55Z  
**変更:** +33 -11 (2ファイル)  
**マージ日:** 2025-05-14T13:54:26Z  
**内容:**

#47 に関連して、Geminiのプロンプトを変更したことに伴う出力jsonの変更を反映し、うまくjsonファイルをmergeするためのコードです。

一番最後のjsonファイルから、年度を読み取る(宣誓書の年)と15行目に書かれていますが、必ずしも宣誓書は最後のページであるという確認はとれていません（ほとんどの場合最後のようです）
ここは今後改修の必要があるかもしれません

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - 複数のJSONファイルの「categories」と「transactions」リストを直接マージし、1つのJSONファイルとして出力できるようになりました。
  - マージされたJSONは新しい「tools/merged_files」ディレクトリに保存されます。

- **リファクタリング**
  - データのマージ処理がDataFrameベースからJSON辞書ベースに変更されました。

- **スタイル**
  - コード内の不要な空行を削除しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [E2E - Geminiプロンプト変更](https://github.com/digitaldemocracy2030/polimoney/pull/47)

**作成者:** shumizu418128  
**作成日:** 2025-05-07T14:28:14Z  
**変更:** +56 -56 (1ファイル)  
**マージ日:** 2025-05-14T09:24:23Z  
**内容:**

converter.tsの形式に合わせた形で、Geminiに出力させることがねらいです。

現在、収支報告書をGeminiに読ませてjson出力させ、それらをまとめたall.jsonを作っても、converter.tsで形式エラーが発生している状況です。
これを解決するために、まずはGeminiにconverter.tsの想定する形式（= sample_input.jsonの形式）にさせることをねらいとしています。
[新しいプロンプトを利用して出力したものはこちらです](https://github.com/shumizu418128/polimoney/blob/test-only/output_json/05teiki-jimin_365_page_02.json)

なお、新しいプロンプトを使って作ったjsonファイルたちをそのままmerge_jsons.pyにかけると、エラーが出てマージできません。merge_jsons.pyの想定外の形式になってしまうためです。
かといってGeminiのプロンプトをこのまま変更せず（＝このプルリクをmergeしない）、merge_jsons.pyの変更のみでconverter.tsの想定する形式に持っていくことはできません。converter.tsにとって必要な情報が不足しているためです。

まずGeminiにconverter.tsの想定する形式を出力させ、後ほどmerge_jsons.pyのプルリクを出し、最終的にall.jsonをconverter.tsの想定する形式にする考えです。

よろしくお願いします。

**コメント:** なし

---

### [DevContainer configuration with Dockerfile, README, and VS Code settings](https://github.com/digitaldemocracy2030/polimoney/pull/45)

**作成者:** adust09  
**作成日:** 2025-05-07T08:59:38Z  
**変更:** +135 -0 (4ファイル)  
**マージ日:** 2025-05-14T13:47:29Z  
**内容:**

#25 
立ち上げとlocalhostの接続まで確認済みです。
利用するextensionなどは議論の余地があると思います。

**コメント:** なし

---

### [収支報告書の表現に合わせて修正](https://github.com/digitaldemocracy2030/polimoney/pull/39)

**作成者:** shumizu418128  
**作成日:** 2025-05-02T13:14:05Z  
**変更:** +11 -11 (1ファイル)  
**マージ日:** 2025-05-14T07:09:56Z  
**内容:**

tsでの表現：翌年度への繰越
gemini & 収支報告書での表現：翌年への繰越額
前年も同様

収支報告書の表記に合わせたほうがGemini出力を流すうえでラクだと思うので、修正させていただきたくPRを書きました。

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(2件)

### [gemini 2.5 pro preview 05-26 導入](https://github.com/digitaldemocracy2030/polimoney/pull/44)

**作成者:** shumizu418128  
**作成日:** 2025-05-07T00:44:04Z  
**変更:** +2 -2 (1ファイル)  
**内容:**

[geminiにアップデートが入りました](https://developers.googleblog.com/en/gemini-2-5-pro-io-improved-coding-performance/)

**コメント:** なし

---

### [E2Eテストで発生したエラーの修正](https://github.com/digitaldemocracy2030/polimoney/pull/35)

**作成者:** shumizu418128  
**作成日:** 2025-04-30T15:25:31Z  
**変更:** +26 -5 (1ファイル)  
**内容:**

https://github.com/digitaldemocracy2030/polimoney/issues/29#issuecomment-2842261513

ここで発生したエラーのうち、直さないと実行不可能なものをすべて修正しています

**diffがすごいことになっていますが、merge_jsons.py以外すべてpopplerの新規追加です**

popplerが無いとpdf2imageが動作できない
UnicodeDecodeError: 'cp932' codec can't decode byte 0x8d in position 96: illegal multibyte sequence
→原因：utf-8指定忘れ
TypeError: list indices must be integers or slices, not str
→原因：data["item"]が直接リストになっている
ValueError: No objects to concatenate
→原因：target_dirの定義が甘い
OSError: Cannot save file into a non-existent directory: 'merged_files'
→原因：保存先のフォルダ名にtoolsが入っていない

なお、typeerrorのみjsonの出力を正しく設定すれば直る可能性があり、その場合は`tools\merge_jsons.py`11行目を元に戻す必要があります

**コメント:** なし

---

