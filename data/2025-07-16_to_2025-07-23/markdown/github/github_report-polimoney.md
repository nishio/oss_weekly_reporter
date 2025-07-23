# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-07-16T12:37:06.710122+09:00 から 2025-07-23T12:37:06.710122+09:00 まで

## Issues

### 過去7日間に完了されたissue (7件)

### [渉外時の承諾確認リストを作成](https://github.com/digitaldemocracy2030/polimoney/issues/131)

**作成者:** Nozomi-M21  
**作成日:** 2025-06-11T12:44:20Z  
**内容:**

渉外時の確認項目をクリアにし、渉外フローに組み込む
【確認項目】

1. データいただく＞非公開確認＞公開の流れでよいか？
2. 事例として紹介してよいか？（website、note、SNS）
3. ユーザーインタビューしてよいか？（これはオプション的に聞く）

[営業資料に追加](https://docs.google.com/presentation/d/1d5OqyfjVNiQCokVXgEdy9K1RTlEExyQUWOeEFXVl2UM/edit?usp=sharing)

**コメント:** なし

---

### [セキュリティアラートの解決](https://github.com/digitaldemocracy2030/polimoney/issues/129)

**作成者:** moai-redcap  
**作成日:** 2025-06-11T10:41:02Z  
**内容:**

## 問題

[セキュリティアラート](https://github.com/digitaldemocracy2030/polimoney/security/dependabot/2)がでているので解決したい

## 再現手順（未記入でも構いません）

## 修正方法の概要（未記入でも構いません）


**コメント:** なし

---

### [OCRの出力項目にプロフィール情報などウェブの表示に必要な情報がない](https://github.com/digitaldemocracy2030/polimoney/issues/104)

**作成者:** dotneet  
**作成日:** 2025-05-31T00:56:44Z  
**内容:**

profile, reports などウェブの表示項目がOCRの出力情報に含まれていない。
https://github.com/digitaldemocracy2030/polimoney/issues/80#issuecomment-2922695531

**コメント:** なし

---

### [準備中の「Coming Soon..」パネルをUIに追加](https://github.com/digitaldemocracy2030/polimoney/issues/102)

**作成者:** Nozomi-M21  
**作成日:** 2025-05-28T13:15:27Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->
準備中の人数分「Coming Soon..」パネルを足したらユーザーの期待値が高まりそう

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）
テスト太郎の横にパネルを追加

**コメント:** なし

---

### [converter.ts の出力ファイルを使った可視化ページの表示](https://github.com/digitaldemocracy2030/polimoney/issues/80)

**作成者:** dotneet  
**作成日:** 2025-05-21T15:58:50Z  
**内容:**

政治資金収支報告書の可視化ページは、現在はデータを直接ハードコーディングしている。

OCRからconverter.ts までのフローの結果の妥当性を視覚的に判断しやすいように、converter.ts の出力ファイル(json)を手軽に可視化ページで見れるようにしたい。



**コメント:** なし

---

### [E2E動作確認（つなぎこみ）](https://github.com/digitaldemocracy2030/polimoney/issues/29)

**作成者:** nanocloudx  
**作成日:** 2025-04-30T13:26:32Z  
**内容:**

精度は悪くても良いので（OCR結果が間違っていることを許容して）、Gemini読み込みからHTML出力までを繋ぎこむ


**コメント:** なし

---

### [収支報告書のスキーマ定義](https://github.com/digitaldemocracy2030/polimoney/issues/22)

**作成者:** nanocloudx  
**作成日:** 2025-04-25T10:19:13Z  
**内容:**

紙や PDF や Excel で提出されている収支報告書について、実際に手作業で Spreadsheet に転記する作業をしてみました。
（備考１：転記するだけでも心が折れそうになったので、これを作成している秘書の皆様はすげぇな...という気持ちになりました）
（備考２：どう考えても複式簿記にすべきだろ...という気持ちにもなりました、その他に丸め込まれる科目が多すぎる）

その結果、以下のようなラベルを持つ CSV または JSON にできると、取り回ししやすいのではという仮説を持ちました

```
- id
  - 識別番号
  - 収支報告書の大項目、中項目、行番号みたいなのを用いれると識別しやすそう
  - 例：７寄附の内訳 > １個人 > 行番号１ であれば 7-1-1 みたいな
- direction
  - 収入か支出か
  - 大項目2~12がだいたい収入、大項目13以降が支出っぽいです
- category
  - カテゴリー
  - シート左上に大項目みたいなのがある
- subCategory
  - サブカテゴリー
  - シート右上に中項目みたいなのがある
- purpose
  - 目的
  - これは支出にだけ項目がある
- amount
  - 金額
- name
  - 収入元または支出先の名称
- date
  - 日付
  - R5のような表記は西暦に直したほうがフレンドリーと思われる
```

またいくつか注意すべき発見がありました

- 支出＞経常経費＞人件費には内訳の記載がない
- 各大項目の最終ページには「その他の収入」みたいな欄がある(見落としがち)
- 大項目３の内容は大項目１０の内容と重複し、さらに大項目１１に大項目１０の内訳の一部が掲載されている
- 大項目16の内容は他の支出内容の内訳なので重複しうる
- 大項目17以降の内容は一旦無視でも良さそう？（記載のあるケースをまだ見てないので知見が足りない）

<img width="1121" alt="Image" src="https://github.com/user-attachments/assets/7c9a83cf-a0e4-41ac-8d81-505870735b39" />

**コメント:** なし

---

### 過去7日間に作成されたissue (2件)

### [テストを書く - backend](https://github.com/digitaldemocracy2030/polimoney/issues/159)

**作成者:** shumizu418128  
**作成日:** 2025-07-19T13:23:48Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->
backendフォルダはGoのサーバーです
テストコードを書きたいです

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### [dependabotを設定する](https://github.com/digitaldemocracy2030/polimoney/issues/158)

**作成者:** adust09  
**作成日:** 2025-07-19T13:18:47Z  
**内容:**

セキュリティアラートの対応に人的コストがかかっているので、自動化したい。
以下の通り、dependabotと自動マージの設定をする。
ただし、テストが通った場合のみ自動マージする。

> 今後もどんどん出てくると思うので dependabot と自動マージ設定を入れた方が良さそうですね。
> 自動マージするなら自動テストがあった方が安全なので、重要なスクリプトが一通り動作してメイン導線が動く確認ができるテストを書いたほうがよさそう。 

 _Originally posted by @dotneet in [#129](https://github.com/digitaldemocracy2030/polimoney/issues/129#issuecomment-2982606406)_

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(2件)

### [カテゴリ数や深さが一定を超えるとサンキー図がとても見づらくなる](https://github.com/digitaldemocracy2030/polimoney/issues/118)

**作成者:** dotneet  
**作成日:** 2025-06-05T15:02:58Z  
**内容:**

トランザクション数が多いとカテゴリ数も自然と増え、同レベルのカテゴリ数も増えより深くなる。
同レベルのカテゴリ数や深さが一定以上にならないような制御が必要。

対処案

 - カテゴリの重要度を手動またはAIにより設定させる
 - 重要度の高いカテゴリは残しつつ、同階層のカテゴリが5個を超えるようであれば「その他」カテゴリなどにまとめてしまう
 - 深さも income と expense でそれぞれ3階層程度を上限とし、それ以下のカテゴリ・トランザクションは上位カテゴリに繰り上げる

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

## Pull Requests

### 過去7日間にマージされたPR (10件)

### [README.mdのGoのインストール要件を1.24以上から1.23以上に修正](https://github.com/digitaldemocracy2030/polimoney/pull/164)

**作成者:** shumizu418128  
**作成日:** 2025-07-22T11:37:39Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-07-22T11:37:47Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->

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

### [test: add backend tests - models and middleware layers](https://github.com/digitaldemocracy2030/polimoney/pull/163)

**作成者:** adust09  
**作成日:** 2025-07-22T06:12:36Z  
**変更:** +3264 -1 (17ファイル)  
**マージ日:** 2025-07-22T07:50:39Z  
**内容:**

## Summary
- Implements comprehensive test suite for backend models and middleware layers
- Addresses issue #159 to add test coverage for the Go backend server
- Achieves 93.5% coverage for models and 90.1% coverage for middleware

## Changes
### Models Layer Tests
- ✅ User repository tests (CRUD operations, queries)
- ✅ Health repository tests (connection checks, stats)

### Middleware Layer Tests
- ✅ Auth middleware tests (Signup, Login, JWT generation)
- ✅ User middleware tests (GetAllUsers, GetUserByID with validation)
- ✅ Health middleware tests (health status reporting)
- ✅ Common middleware tests (CORS, JWT auth, error handling, request ID, HTTPS redirect)

### Test Infrastructure
- Created test helper utilities (fixtures, helpers, mocks)
- Added testing dependencies (testify, go-sqlmock)
- Fixed compilation issues in test utilities

## Test Results
```
ok  github.com/digitaldemocracy2030/polimoney/middleware  2.119s  coverage: 90.1% of statements
ok  github.com/digitaldemocracy2030/polimoney/models      0.233s  coverage: 93.5% of statements
```

All tests are passing ✅

## Next Steps
Controllers and config layer tests can be added in future PRs to achieve complete test coverage.

Closes #159

🤖 Generated with [Claude Code](https://claude.ai/code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **ドキュメント**
  * Claude Code（claude.ai/code）向けの包括的な開発ガイド「CLAUDE.md」を追加しました。

* **テスト**
  * バックエンドのミドルウェア、モデル、コントローラー、認証、ユーザー関連機能に対する包括的なユニットテストを追加しました。
  * 環境変数チェックやデータベース接続設定のテストも含まれています。
  * テスト用のモックデータ、ヘルパー関数、SQLモックのセットアップ機能を追加しました。

* **チョア**
  * Goモジュールにテスト・デバッグ用の依存パッケージを追加しました（go-sqlmock、testify など）。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [add preview page](https://github.com/digitaldemocracy2030/polimoney/pull/162)

**作成者:** kuboon  
**作成日:** 2025-07-22T03:04:23Z  
**変更:** +106 -0 (3ファイル)  
**マージ日:** 2025-07-22T03:42:23Z  
**内容:**

# 変更の概要
`https://polimoney.dd2030.org/preview?url=`
というページを新規に追加する。
url 以降に、 json を返す任意の url (gist を使うのが簡単) を渡すことで、そこから読んだデータで ページをプレビューできる。URL を知った人にしか事前に見られることはなく、 git への push も不要。

サンプルデータ https://gist.githubusercontent.com/kuboon/8896a4a4b7eaac4cab38e8a01c0d3eb4/raw/preview-demo.json

# スクリーンショット
<img width="1020" height="882" alt="image" src="https://github.com/user-attachments/assets/cd08743c-8fb4-4ae5-9e8b-35ebc8ef8066" />

# 変更の背景
新規にデータを追加する際、 public github へ push する前に確認をしたい、という要望があったため。

# 関連Issue
https://github.com/digitaldemocracy2030/polimoney/issues/32

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [認証機能](https://github.com/digitaldemocracy2030/polimoney/pull/161)

**作成者:** shumizu418128  
**作成日:** 2025-07-21T13:48:03Z  
**変更:** +389 -118 (15ファイル)  
**マージ日:** 2025-07-21T14:08:21Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->

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

* **新機能**
  * サインアップおよびログインAPIエンドポイントを追加しました。
  * JWT認証ミドルウェアを導入し、管理者ルートの保護を強化しました。
  * HTTPSリダイレクト機能を追加しました（本番環境のみ有効）。
  * 環境変数の必須チェック機能を追加しました。
  * サンプル環境変数ファイル（.env.example）を追加しました。

* **バグ修正**
  * ユーザーモデルのロール情報取得方法を改善し、関連情報の取得を簡素化しました。

* **ドキュメント**
  * 環境変数設定手順をREADMEに追記しました。

* **その他**
  * サンプルデータ挿入SQLをコメントアウトし、テストクエリファイルを削除しました。
  * 依存パッケージを追加・整理しました。
  * Docker Composeに環境変数を追加しました。
  * .gitignoreの.envファイルの除外パターンを修正しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [GORM導入](https://github.com/digitaldemocracy2030/polimoney/pull/160)

**作成者:** shumizu418128  
**作成日:** 2025-07-20T06:22:17Z  
**変更:** +444 -200 (12ファイル)  
**マージ日:** 2025-07-20T06:41:04Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
query直書きしてたところを修正

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

* **新機能**
  * ヘルスチェックAPIエンドポイント（/api/v1/health）を追加し、システムおよびデータベースの状態を確認できるようになりました。
  * ユーザー一覧取得API（/api/v1/admin/users）およびユーザー詳細取得API（/api/v1/admin/users/:id）を追加しました。

* **リファクタ**
  * データベース処理をGORM ORMに移行し、より効率的なデータアクセスと管理が可能になりました。
  * ユーザーモデルおよびロールモデルをGORMに最適化しました。
  * ユーザー関連のコントローラー構成を整理し、ヘルスチェック機能を専用コントローラーに移行しました。
  * データベース接続の初期化とクリーンアップ処理を改善しました。

* **依存関係**
  * GORM関連パッケージを導入し、不要となった旧パッケージを削除しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Dockerfileに日本のタイムゾーン設定を追加](https://github.com/digitaldemocracy2030/polimoney/pull/157)

**作成者:** shumizu418128  
**作成日:** 2025-07-19T08:54:13Z  
**変更:** +5 -0 (1ファイル)  
**マージ日:** 2025-07-19T08:54:19Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
タイムゾーンを設定しただけ

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

* **Chores**
  * バックエンドコンテナのタイムゾーンを日本標準時（Asia/Tokyo）に設定しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [開発環境構築](https://github.com/digitaldemocracy2030/polimoney/pull/156)

**作成者:** shumizu418128  
**作成日:** 2025-07-19T08:48:59Z  
**変更:** +593 -74 (13ファイル)  
**マージ日:** 2025-07-19T08:49:10Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
ローカル上でPostgreSQLが起動し、テスト用データが自動で入り、仮のエンドポイントでアクセスできるようになりました

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->
#32 #120 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **新機能**
  * ユーザー管理およびロールベースアクセス制御のためのデータベーススキーマとサンプルデータを追加しました。
  * ユーザー一覧取得、ユーザー詳細取得、ヘルスチェックAPIエンドポイントを追加しました。
  * Gin用のCORS、リクエストID、DB接続、エラーハンドラーの各種ミドルウェアを追加しました。

* **ドキュメント**
  * PostgreSQLのデータベース名やサービス名を「polimoney」に変更しました。

* **その他**
  * Dockerfileとdocker-composeの設定を更新し、タイムゾーンデータやサービス名の変更に対応しました。
  * 依存パッケージを追加・整理しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [ひな形作成](https://github.com/digitaldemocracy2030/polimoney/pull/155)

**作成者:** shumizu418128  
**作成日:** 2025-07-19T05:23:36Z  
**変更:** +188 -9 (6ファイル)  
**マージ日:** 2025-07-19T05:36:34Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
空っぽのGoサーバー・PostgreSQLを作成
どちらもDocker上で動く

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->
#32 #120 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **新機能**
  * DockerとDocker ComposeによるバックエンドAPIとPostgreSQLのコンテナ起動に対応しました。
  * データベース接続待機用スクリプトを追加しました。
  * 新しいエンドポイント「/」（GET）および「/health」（POST）を追加しました。

* **ドキュメント**
  * READMEを大幅に更新し、セットアップ手順や環境変数、データベース設定、Docker Composeの利用方法を明記しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat: 環境変数からポートを取得し、サーバー起動時にログ出力を追加](https://github.com/digitaldemocracy2030/polimoney/pull/154)

**作成者:** shumizu418128  
**作成日:** 2025-07-16T13:11:29Z  
**変更:** +13 -2 (1ファイル)  
**マージ日:** 2025-07-16T13:11:36Z  
**内容:**

# 変更の概要
Coderabbitに言われたこと
portをenvからとる


# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **改善**
  * サーバー起動時に使用するポート番号が環境変数「PORT」から取得されるようになりました（未設定時は8080が使用されます）。
  * サーバー起動時に使用ポートをログ出力し、起動失敗時にはエラーメッセージが表示されるようになりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [バックエンド helloworld](https://github.com/digitaldemocracy2030/polimoney/pull/153)

**作成者:** shumizu418128  
**作成日:** 2025-07-16T12:50:55Z  
**変更:** +196 -0 (4ファイル)  
**マージ日:** 2025-07-16T12:52:33Z  
**内容:**

# 変更の概要
バックエンドフォルダを作りました
内容は今後つくっていきます

#32 
#120 

言語はGoを採用、サーバーはAzureを使うことになりそう、とのことです（モアイさんより）
GCPプロジェクトはあるけど...

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **新機能**
  * Ginフレームワークを使用したGo製バックエンドサーバーを追加しました。`/api/hello`エンドポイントで挨拶メッセージを返します。

* **ドキュメント**
  * バックエンドのセットアップ手順を記載したREADMEファイルを追加しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [報告書の基本情報をdemo-ryosukeidei.tsに合わせて設定](https://github.com/digitaldemocracy2030/polimoney/pull/113)

**作成者:** shumizu418128  
**作成日:** 2025-06-05T02:23:43Z  
**変更:** +32 -18 (1ファイル)  
**内容:**

# 変更の概要
#80 で指摘され、#104 でissueとして扱われているように、収支報告書の基本情報を、すでにある形式に合わせてGeminiに取得させる

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - 日本の政治資金報告書から抽出される情報項目が拡充され、組織名、代表者、会計責任者、事務担当者、組織種別、活動地域、資金管理団体指定など、より多くの基本情報が取得されるようになりました。
- **ドキュメント**
  - 抽出手順や出力形式に関する説明がより明確になり、不足項目の扱いや数値の出力形式についても詳細な指示が追加されました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

