# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-04-30T16:23:22.865006+09:00 から 2025-05-07T16:23:22.865006+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (8件)

### [対内外向け[資料露出]](https://github.com/digitaldemocracy2030/polimoney/issues/41)

**作成者:** cKinu  
**作成日:** 2025-05-02T18:30:00Z  
**内容:**

**発進方法案**
**発信の目的:**
認知度向上による利用者数、ボランティア数の増加
**フォーマル発信**
- ターゲット
> - ユーザー、ビューアー共に
- 露出先
> - PRTIMESや公式Youtube
- 何を
> - ポンチ絵と営業資料
- 目的
> - 国民の信頼につながる、政治献金につながる、手軽に導入できるための流入間口を広げる

**カジュアル発信**
- ターゲット
> - ビューアーに絞る場合
> > - 新規、ネームのみ認知あり、認知あり興味を深めたいの3層に分けて添付資料を変えて発信
> > - デジ民2030の紹介は全てに必ず入れる
- 露出先
> - X?
- 何を
> - ビューアーの層に合わせ添付資料変更
- 目的
> - ボランティア数の増加
> - 政治資金の関心深度とツール利活用の向上

備忘
営業資料は、メールで国会議員一括送信という手も詳細詰める

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

### [Pythonのlinter、formatterを導入する](https://github.com/digitaldemocracy2030/polimoney/issues/34)

**作成者:** tdaira  
**作成日:** 2025-04-30T14:02:35Z  
**内容:**

- linter、formatterを導入する
- 型チェック等はまず入れてみて少しずつオプションを増やしていく方針にする

**コメント:** なし

---

### [ドキュメントを整理する](https://github.com/digitaldemocracy2030/polimoney/issues/33)

**作成者:** adust09  
**作成日:** 2025-04-30T14:01:16Z  
**内容:**

# 背景
- 新規開発者むけにドキュメントを整理する
- Vibe codingで効率的に実装を進めたい

# 方法
手動ではなくDevinWikiを使って自動生成させる。
Devinのアクセス権はSlackにて申請できるのでまずはそこから。

# MTG資料
https://docs.google.com/document/d/19Kn6ekK3twMVcVaSyUgptvmfzrXEJezA6GXTbPXjm9M/edit?tab=t.0#heading=h.2sk7iuwum47u

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

### 過去7日間に更新されたissue（作成・クローズを除く）(3件)

### [支出のどれが税金で賄われているか明示](https://github.com/digitaldemocracy2030/polimoney/issues/21)

**作成者:** shumizu418128  
**作成日:** 2025-04-24T16:30:47Z  
**内容:**

> 国会議員で税金を収入として受け取っている場合、どの使途が税金部分かを明示するのは価値があるのではないかというインプットがありました

[という提案が安野さんに来ていたようです](https://w1740803485-clv347541.slack.com/archives/C08FL5L6GSH/p1745483561743249)のでissueにしておきます。

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

### 過去7日間にマージされたPR (3件)

### [フロントエンド：スキーマ変更２](https://github.com/digitaldemocracy2030/polimoney/pull/37)

**作成者:** nanocloudx  
**作成日:** 2025-05-01T04:44:03Z  
**変更:** +121 -133 (10ファイル)  
**マージ日:** 2025-05-01T04:44:49Z  
**内容:**

#36 の続きです
Source, Summary, Metadata 型を削除し、Report 型に統合しました
この変更はデータベースのテーブルを以下の３つにするための下準備です

- 政治家一覧を持つ Profiles
- 収支報告書一覧を持つ Reports
- 収支一覧を持つ Transactions


**コメント:** なし

---

### [フロントエンド：スキーマ変更](https://github.com/digitaldemocracy2030/polimoney/pull/36)

**作成者:** nanocloudx  
**作成日:** 2025-04-30T17:23:11Z  
**変更:** +878 -1055 (20ファイル)  
**マージ日:** 2025-05-01T04:13:20Z  
**内容:**

#22 に対応するため、スキーマの変更およびコンポーネント修正を行いました
既に公開している安野さん＆出井さんのレポートは一旦維持しつつ、元の収支一覧コンポーネントはリネームして deprecated としています

ーーーーー
本PRとは別 Issue としてデータベース化を計画しています
Profile と Transaction はこのPRの内容で概ねFIXで良いかと思います
Source, Summary, Metadata の内容は同じテーブルにする見込みなので、この３つは近々マージする可能性があります
（チャートの内容を示す Flow についてはまだ検討に余地があるかもしれません）

`/app/[slug]` は一時的に削除していますが、こちらはデータベース化に合わせて復活させる想定です
既存のレポートには demo- というプレフィックスを付けており、データベースから取得できるようになったタイミングで置き換えるため削除予定です

**コメント:** なし

---

### [linterをPR作成時に走らせる設定の追加](https://github.com/digitaldemocracy2030/polimoney/pull/28)

**作成者:** tdaira  
**作成日:** 2025-04-29T23:11:05Z  
**変更:** +55 -0 (1ファイル)  
**マージ日:** 2025-04-30T06:00:02Z  
**内容:**

PR作成時にlintの実行漏れに気付けるるようにGitHub Actionsの設定を行いました。
個人のリポジトリでは問題なく実行されることを確認しています。
https://github.com/tdaira/polimoney/pull/1

こちらのリポジトリでは、maintainerの許可が必要なようです。
<img width="634" alt="スクリーンショット 2025-04-30 8 13 05" src="https://github.com/user-attachments/assets/e25ef1f4-7703-4377-bdb3-78efe8a35a09" />

今後の運用としては、mainに向けたPRマージの前にStatus checkでこの設定のチェックを有効にできると、lint漏れが防げると思います
https://docs.github.com/ja/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks


**コメント:** なし

---

### 過去7日間に作成されたPR (6件)

### [gemini 2.5 pro preview 05-26 導入](https://github.com/digitaldemocracy2030/polimoney/pull/44)

**作成者:** shumizu418128  
**作成日:** 2025-05-07T00:44:04Z  
**変更:** +2 -2 (1ファイル)  
**内容:**

[geminiにアップデートが入りました](https://developers.googleblog.com/en/gemini-2-5-pro-io-improved-coding-performance/)

**コメント:** なし

---

### [docs: Add Japanese translation of project documentation](https://github.com/digitaldemocracy2030/polimoney/pull/43)

**作成者:** obama00300+Devin  
**作成日:** 2025-05-06T13:09:18Z  
**変更:** +962 -0 (5ファイル)  
**内容:**

# 日本語ドキュメントの追加

このPRでは、Polimoneyプロジェクトのドキュメントを日本語に翻訳し、`docs/wiki_ja.md`として追加しています。

## 変更内容

- プロジェクトの概要、構成、主要コンポーネント、および用語集を日本語に翻訳
- `docs`ディレクトリを作成し、翻訳したドキュメントを追加

## リンク

- [Link to Devin run](https://app.devin.ai/sessions/ff9bd4a6b4e84c15b2fd837436438e1c)
- 依頼者: obama00300@gmail.com


**コメント:** なし

---

### [Devin wikiコンテンツのドキュメント追加](https://github.com/digitaldemocracy2030/polimoney/pull/42)

**作成者:** obama00300+Devin  
**作成日:** 2025-05-06T07:55:38Z  
**変更:** +65 -0 (2ファイル)  
**内容:**

# Devin wikiコンテンツのドキュメント追加

## 概要
このPRでは、Devinとの協働に関するドキュメントをPolimoney用に追加しています。これらのファイルは、GitHub wikiが有効になった後にwikiコンテンツとして使用することができます。

## 変更内容
- `docs/DEVIN_COLLABORATION.md`: Devinとの協働方法に関するドキュメント
- `docs/Home.md`: wikiのホームページ用テンプレート

## GitHub wikiの有効化と設定方法
現在、Polimoneyリポジトリにはwiki機能が無効になっています。以下の手順でwikiを有効にし、コンテンツを追加できます：

1. リポジトリの設定ページ（Settings）に移動
2. 「Features」セクションで「Wikis」を有効にする
3. wikiページに移動し、コンテンツを追加

## Link to Devin run
https://app.devin.ai/sessions/e3837c2614284fbc8c05d348af492ccc

## Requested by
obama00300@gmail.com


**コメント:** なし

---

### [収支報告書の表現に合わせて修正](https://github.com/digitaldemocracy2030/polimoney/pull/39)

**作成者:** shumizu418128  
**作成日:** 2025-05-02T13:14:05Z  
**変更:** +11 -11 (1ファイル)  
**内容:**

tsでの表現：翌年度への繰越
gemini & 収支報告書での表現：翌年への繰越額
前年も同様

収支報告書の表記に合わせたほうがGemini出力を流すうえでラクだと思うので、修正させていただきたくPRを書きました。

**コメント:** なし

---

### [all.jsonをsample_input.json形式に変換するスクリプト](https://github.com/digitaldemocracy2030/polimoney/pull/38)

**作成者:** hagi5  
**作成日:** 2025-05-02T11:55:29Z  
**変更:** +276 -0 (1ファイル)  
**内容:**

## 目的
https://github.com/digitaldemocracy2030/polimoney/issues/29 のall.jsonをdata/sample_input.json っぽいデータに変換する

### 補足
カテゴリの分類のためにページ番号が欲しかったので all.json をページごとのデータにsplitしています
[all_page2.json](https://github.com/user-attachments/files/20012673/all_page2.json)

## 使い方
```shell
python tools/convert.py tools/merged_files/all_page2.json -o output.json
````
## 出力サンプル
[output.json](https://github.com/user-attachments/files/20012442/output.json)

## レビューしていただきたい点

- 出力サンプルが最低限使えるものかどうか
  - ここをもっとこうしてほしいなど指摘があればお願いします
- all_page2.jsonにページ番号を含めたことの是非


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

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [update readme](https://github.com/digitaldemocracy2030/polimoney/pull/24)

**作成者:** adust09  
**作成日:** 2025-04-27T04:05:02Z  
**変更:** +27 -1 (1ファイル)  
**内容:**

AIに書かせたREADMEであり、一部コマンドは私の方でまだ検証できていません。


**コメント:** なし

---

