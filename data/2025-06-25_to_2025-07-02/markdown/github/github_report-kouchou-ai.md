# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-06-25T12:31:34.859945+09:00 から 2025-07-02T12:31:34.859945+09:00 まで

## Issues

### 過去7日間に完了されたissue (2件)

### [[REFACTOR] 管理画面のレポート一覧画面をコンポーネント分割する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/604)

**作成者:** shgtkshruch  
**作成日:** 2025-06-16T10:58:09Z  
**内容:**

# 現在の問題点
<!-- 現在のコードの何が問題なのか、どのような技術的負債があるかを説明してください -->

- https://github.com/digitaldemocracy2030/kouchou-ai/issues/460 で管理画面のレポート一覧画面のリデザインが進んでいます
  - 今の所、既存の機能に変更はありませんが、一括編集のような機能が追加されたり、機能への動線が変わりそうです
- [今の管理画面のレポート一覧の実装](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/client-admin/app/page.tsx)は、コンポーネント分割がされていないので、このままデザインの変更を適用すると diff が大きくなる可能性が高い
  - デザインのみを変更したい場合でも、見た目とロジックが密結合しているので、ロジックのコードも移動する diff が発生しそう

# 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->

- 管理画面の一覧画面を機能単位でコンポーネント分割する
- ロジック部分はカスタムフックなどに切り出す
  - 新しい UI からも呼び出せるので実装がしやすくなりそう


**コメント:** なし

---

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

### 過去7日間に作成されたissue (4件)

### [[FEATURE] Azure に動作確認環境・デモ環境を作る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/622)

**作成者:** shingo-ohki  
**作成日:** 2025-06-29T08:25:09Z  
**内容:**

# 背景
- 現状、新しい機能の開発やソフトウェア改善を行った場合の動作確認は、エンジニアの手元の開発環境で行っているが、UI/UX の改善を行う際などはデザイナーなどエンジニア以外の方にも確認してもらいたいがその環境がない
- ユーザーが広聴AIを試すには環境構築をする必要があるが、これは多少のエンジニアリングスキルを必要とするため、簡単に試すことができない

<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->


# 提案内容
上記を解決するために、dd2030 が管理する Azure 環境に常に広聴AIがデプロイされているような環境を用意する

<!-- 実装案やデザイン案があれば記入してください -->

- 動作確認環境
  - [x] Azure 環境にセットアップする
  - [ ] github の branch へのマージをトリガーにして deploy できるようにする
  - [ ] dd2030.org ドメインでアクセスできるようにする
- デモ環境
  - [ ] .env で OPENAI_API_KEY を設定せず、form から受け付けた OpenAI API KEY を使ってレポートを生成できるようにする
  - [ ] client-admin のパスワードなしでアクセスできるようにする

**コメント:** なし

---

### [管理画面アクション関数のエラーハンドリング改善](https://github.com/digitaldemocracy2030/kouchou-ai/issues/621)

**作成者:** coderabbitai[bot]  
**作成日:** 2025-06-28T09:56:21Z  
**内容:**

## 概要

管理画面のアクション関数（visibilityUpdate、csvDownload、reportDelete等）において、エラーハンドリングがconsole.errorによるログ出力のみとなっており、ユーザーへの適切なフィードバックが提供されていません。

## 現在の問題

- エラーが発生してもユーザーに通知されない
- 操作が失敗したかどうかをユーザーが判断できない
- エラーの詳細がコンソールにのみ出力される

## 改善提案

以下のようなユーザーフィードバック機能の実装を検討：
- UIアラート・トースト通知の表示
- エラーレスポンスの返却（フロントエンドでの表示用）
- 操作結果の明確な表示

## 対象ファイル

- client-admin/app/_actions/visibilityUpdate.ts
- client-admin/app/_actions/csvDownload.ts
- client-admin/app/_actions/csvDownloadForWindows.ts
- client-admin/app/_actions/reportDelete.ts

## 関連PR・コメント

- PR: https://github.com/digitaldemocracy2030/kouchou-ai/pull/618
- コメント: https://github.com/digitaldemocracy2030/kouchou-ai/pull/618#discussion_r2173188154
- 起票者: @shgtkshruch

**コメント:** なし

---

### [CSVダウンロード機能のエラーハンドリング改善](https://github.com/digitaldemocracy2030/kouchou-ai/issues/620)

**作成者:** coderabbitai[bot]  
**作成日:** 2025-06-28T09:52:54Z  
**内容:**

## 問題

現在のCSVダウンロード機能（`client-admin/app/_actions/csvDownload.ts`）では、エラー発生時にコンソールへのログ出力のみが行われており、ユーザーへのフィードバックが不足しています。

## 改善提案

UI上でエラー状態を表示する仕組みを実装し、ユーザーがCSVダウンロードの失敗を認識できるようにする必要があります。

## 対象ファイル

- `client-admin/app/_actions/csvDownload.ts`
- `client-admin/app/_actions/csvDownloadForWindows.ts`（同様の問題を抱えている可能性）

## 関連

- PR: https://github.com/digitaldemocracy2030/kouchou-ai/pull/618
- コメント: https://github.com/digitaldemocracy2030/kouchou-ai/pull/618#discussion_r2173188152

## 備考

エラーハンドリングは将来的に共通化/標準化予定のため、そのタイミングでの対応を検討。

**コメント:** なし

---

### [[FEATURE] 意見グループの並び順を意見数の降順で表示する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/617)

**作成者:** shingo-ohki  
**作成日:** 2025-06-28T03:04:29Z  
**内容:**

# 背景
- 意見グループ編集時に、意見グループの並び順と階層表示の対応が一致していないため、修正しようとする意見グループを見つけにくい
- レポート表示時の意見グループの表示がどのような順番で表示されているのか分かりにくい

![Image](https://github.com/user-attachments/assets/20a5d180-2e9b-4937-ba58-b63069cf7583)

![Image](https://github.com/user-attachments/assets/16b43381-24ee-4ed8-b2ef-4371081c362c)

![Image](https://github.com/user-attachments/assets/ec530fe6-c9ef-4479-96da-152b08ef07fe)

# 提案内容
意見数が多い意見グループから順に表示されていると直感的に理解しやすいのでは？

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(3件)

### [[FEATURE] adminにおいて、APIルートを介してfastapiにリクエストを送る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/547)

**作成者:** nasuka  
**作成日:** 2025-05-20T08:25:30Z  
**内容:**

# 背景
* adminにおいて、 `process.env.NEXT_PUBLIC_ADMIN_API_KEY` でAPIキーを読んでリクエストをfastapiに送っているが、APIキーが漏洩するリスクがある
* APIキーの露出をさせられる（攻撃できる）のは、以下の状況に限定されるためリスクが高い訳ではないが、ゼロではない
  * 広聴AIをリモートでホスティングしている
  * 攻撃者が管理画面のURLを知っている
  * 攻撃者が管理画面にログインしている（id/passwordを知っている）

参考
https://github.com/digitaldemocracy2030/kouchou-ai/pull/545#discussion_r2097241946


# 提案内容
Next.jsのAPIルートをadminに用意したうえで、fastapiと疎通する
（一旦CodeRabbitの指摘内容をそのまま書いていますがこの方針が妥当か自信がないので、next.jsに詳しい方いたらコメントいただけると助かります）

**コメント:** なし

---

### [[FEATURE][design] レポート管理画面：直感的に使いやすくしたい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/460)

**作成者:** UtkNggc  
**作成日:** 2025-05-07T16:09:28Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
現状の管理画面は直感的に使いにくいかもしれない。
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

### [[FEATURE] 環境確認機能を作る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/400)

**作成者:** tokoroten  
**作成日:** 2025-04-30T05:13:14Z  
**内容:**

# 背景
OpenAIのAPIKeyが正しくセットされているのかどうかが、実際にレポートの作成を始めるまで分からない


# 提案内容
管理画面、クライアント画面に以下の機能を付けたい

管理画面
- APIサーバが生きているかどうか
- ~~OpenAIのkeyが正しいか~~ 、疎通できるかどうか（Azureも）
  - API Key の有効性の確認は、https://github.com/digitaldemocracy2030/kouchou-ai/pull/421 で対応済み
  - 以下の検証については未対応
    - 残高不足の確認
    - RateLimitの確認
- クライアント用のフロントサーバが立っているかどうか
- ローカルLLM用のLM Studioが生きているかどうか

## デザインの検討
#447 



**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (8件)

### [[client-admin] 管理画面の Footer の UI を変更する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/624)

**作成者:** shgtkshruch  
**作成日:** 2025-06-29T10:12:18Z  
**変更:** +164 -10 (10ファイル)  
**マージ日:** 2025-06-30T09:42:02Z  
**内容:**

# 変更の概要
- 管理画面の Footer を [Figma の新しいデザイン](https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=1089-5476&t=YIniV852d6LnbHCG-4)に合わせて変更しました
  - UI 実装で必要だったので、Dialog と CloseButton コンポーネントを client から持ってきました

# スクリーンショット
## Footer
![image](https://github.com/user-attachments/assets/eaca9aab-3c93-4d77-abc5-c63291db8d42)

## レポート一覧画面
![image](https://github.com/user-attachments/assets/f833e73f-c76f-4d45-8d13-54ae3fdb5351)

## 免責の Diaog を開く
![image](https://github.com/user-attachments/assets/e0be1492-04c3-46f7-9aa0-abc73cbfa474)


# 変更の背景
- 管理画面の UI を使いやすくしたい

# 関連Issue
- https://github.com/digitaldemocracy2030/kouchou-ai/issues/460

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- 管理画面の Footer が Figma の通りに実装されていること
  - デザイナー確認は Footer だけだとわかりにくいと思うので、管理画面ページを一通り実装してから見ていただこうと思います

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

* **新機能**
  * フッターにAPIから取得したメタデータを表示し、利用規約リンクや「免責」ダイアログを追加しました。
  * 「免責」ボタンをクリックすると、AIの限界や注意事項を説明するダイアログが表示されます。
  * カスタムダイアログ、クローズボタンなどのUIコンポーネントを追加しました。

* **スタイル**
  * ページ下部の余白を追加し、全体のレイアウトを調整しました。
  * bodyのグラデーション背景とfooterのスタイルを削除しました。

* **その他**
  * 一部コンポーネントをクライアントサイドで動作するよう明示しました。
  * ビルド時に環境変数が設定されるようになりました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client-admin] 管理画面のコンポーネントを別ファイルに切り出す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/623)

**作成者:** shgtkshruch  
**作成日:** 2025-06-29T09:35:17Z  
**変更:** +435 -424 (22ファイル)  
**マージ日:** 2025-06-30T00:44:37Z  
**内容:**

# 変更の概要
- 管理画面のレポート一覧で、page を構成するコンポーネントを個別のファイルに切り出しました
  - static export した成果物をダウンロードするボタン
  - Emtpy State のコンポーネント
  - 個別のレポートの行をレンダリングする ReportCard コンポーネント
- ReportCard が個別のコンポーネントになったので、CSV ダウンロードやレポートを削除する関数なども、こちらのコンポーネントと co-location する形でディレクトリ構成を整理しました

# スクリーンショット
- リファクタリングなので、UI の変更はありませんが、動作確認用のキャプチャです

https://github.com/user-attachments/assets/5e32d51c-7bf6-436e-a92e-9510f6abf6e9


https://github.com/user-attachments/assets/d92f0f61-9f87-462b-ae74-1f71b40bc7a0


# 変更の背景
- 管理画面のデザイン変更が予定されているが、コンポーネント分割がされていないのとロジックと UI が分離されていないので、このままデザインの変更を適用することが困難なため

# 関連Issue
- fix: https://github.com/digitaldemocracy2030/kouchou-ai/issues/604
  - こちらの PR で管理画面のコンポーネント分割・関数の分割は終了です 🎉 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

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

* **新機能**
  * レポートが存在しない場合の案内画面を追加しました。
  * 「全レポートをエクスポート」ボタンを追加し、レポートの一括ダウンロードが可能になりました。
  * レポートの詳細情報を表示するカード型UIを追加しました。CSVダウンロードや可視性の切り替え、編集・削除などの操作が行えます。

* **リファクタ**
  * ページ構成を見直し、各機能を独立したコンポーネントに分割しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client-admin] デザインシステムのトークンやコンポーネントを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/619)

**作成者:** shgtkshruch  
**作成日:** 2025-06-28T09:41:20Z  
**変更:** +1862 -19 (12ファイル)  
**マージ日:** 2025-06-29T08:03:16Z  
**内容:**

# 変更の概要
- client-admin に color や typography などのデザインシステムのトークンやコンポーネントを追加しました
  - デザインシステムは client と共通なので、そのままコードを持ってきました
  - https://github.com/digitaldemocracy2030/kouchou-ai/issues/586 でデザインシステムの共通基盤を作りたいですが、現状はないので一旦複製しています

# スクリーンショット
- この PR では、デザイントークンやコンポーネントをコピーしただけなので、既存の画面に変更はありません

# 変更の背景
- 管理画面のリデザインのために、デザインシステムのトークンやコンポーネントが必要なため

# 関連Issue
- https://github.com/digitaldemocracy2030/kouchou-ai/issues/460

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- 管理画面の UI が変わっていないこと

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

## Summary by CodeRabbit

* **新機能**
  * カスタムフォントファミリーとテキストスタイルを追加し、テーマの一貫性を向上。
  * ボタンとリンクのための新しいスタイリングレシピを導入。
  * ボタンとリンクのカスタムReactコンポーネントを追加し、バリアントやサイズ指定に対応。
  * UI全体のテーマ設定（semanticTokens含む）を強化し、色やフォントのセマンティックな管理が可能に。
  * Chakra UI CLIを利用したテーマの型生成スクリプトを追加。

* **リファクタ**
  * Chakra UIのテーマシステムを外部モジュール化し、Providerの構成を整理。

* **修正**
  * フォントのエラー色のセマンティックトークンを標準の赤色トークンに変更。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client-admin] 管理画面の更新ロジックを関数に切り出す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/618)

**作成者:** shgtkshruch  
**作成日:** 2025-06-28T09:35:52Z  
**変更:** +718 -126 (11ファイル)  
**マージ日:** 2025-06-29T07:56:58Z  
**内容:**

# 変更の概要
- 管理画面で View に書かれていたデータの更新ロジックをぞれぞれ個別の関数に切り出しました
  - それぞれの関数のテストを追加しました

# スクリーンショット
- リファクタリングなので UI の変更はありませんが、動作確認用のキャプチャです

https://github.com/user-attachments/assets/8bff8de3-7ba3-4661-bea4-bb3550bfb7f1

# 変更の背景
- 管理画面のデザイン変更が予定されているが、コンポーネント分割がされていないのとロジックと UI が分離されていないので、このままデザインの変更を適用することが困難なため

# 関連Issue
- #604

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- 管理画面で CSV ダウンロード、レポートの公開状態の変更、レポートの削除ができること

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [x] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **新機能**
  * CSVダウンロード（通常/Windows対応）、レポート削除、レポートの公開範囲更新の各アクション機能を追加しました。
  * 公開範囲の選択肢（公開、限定公開、非公開）を提供します。

* **リファクタ**
  * 管理画面のページで各種アクション処理を専用モジュールに分離し、コードを整理しました。
  * レポート情報の解析ユーティリティ関数の名称を変更し、利用方法を統一しました。

* **テスト**
  * CSVダウンロード、Windows向けCSVダウンロード、レポート削除、公開範囲更新、解析情報ユーティリティ関数に対する包括的なテストを追加しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client-admin] 管理画面の Header の UI を変更する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/616)

**作成者:** shgtkshruch  
**作成日:** 2025-06-27T11:15:21Z  
**変更:** +27 -46 (6ファイル)  
**マージ日:** 2025-06-28T03:18:37Z  
**内容:**

# 変更の概要
- 管理画面の Header を[新しいデザイン](https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=226-636&t=PIAiRFYgGT7ReJNb-11)に合わせて変更しました
  - Figma に合わせて余白を調整
  - Header に表示する画像を固定で DD2030 の画像に変更

# スクリーンショット
## Before
![image](https://github.com/user-attachments/assets/363c2bb2-d46a-4861-8345-a2344959f5d3)

## After
![image](https://github.com/user-attachments/assets/eb11061c-2ade-4d58-8e07-e6f822a4aa34)

# 変更の背景
- 管理画面の UI を改善したい

# 関連Issue
- https://github.com/digitaldemocracy2030/kouchou-ai/issues/460

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- 管理画面の Header が、レポート一覧・レポート作成画面・環境確認ページで適切に表示されていること

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

**コメント:** なし

---

### [[client-admin] 意見グループを編集する dialog をコンポーネントに切り出す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/615)

**作成者:** shgtkshruch  
**作成日:** 2025-06-26T07:43:56Z  
**変更:** +459 -166 (5ファイル)  
**マージ日:** 2025-06-28T03:07:09Z  
**内容:**

# 変更の概要
- 管理画面のレポート一覧で、意見グループを編集する dialog を別コンポーネントに切り出しました
  - このコンポーネントはリデザイン後も利用するので、テストも実装しました
  - ユーザーのインタラクションを含んだテストを実装するために [`@testing-library/user-event`](https://testing-library.com/docs/user-event/intro/) を package.json に追加しました

# スクリーンショット
- リファクタリングなので UI の変更はないですが、動作確認用のキャプチャです

https://github.com/user-attachments/assets/85d3bdde-c63c-4326-95b3-3342e43e502d

# 変更の背景
- 管理画面のデザイン変更が予定されているが、コンポーネント分割がされていないのとロジックと UI が分離されていないので、このままデザインの変更を適用することが困難なため

# 関連Issue
- #604

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- 管理画面で意見グループの編集ができること

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

* **新機能**
  * クラスター編集ダイアログの包括的なユニットテストを追加しました。

* **リファクタ**
  * クラスター編集ダイアログの内部状態管理を強化し、外部からの複雑なプロパティ受け渡しを簡素化しました。
  * クラスター編集に関するロジックをダイアログ内に集約しました。
  * クラスター編集ダイアログの開閉制御を単一の状態管理に統合しました。

* **チョア**
  * テスト用パッケージ "@testing-library/user-event" を開発依存に追加しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client-admin] レポート生成時の Polling 処理と UI を別ファイルに切り出す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/614)

**作成者:** shgtkshruch  
**作成日:** 2025-06-25T06:13:48Z  
**変更:** +471 -176 (4ファイル)  
**マージ日:** 2025-06-25T23:44:51Z  
**内容:**

# 変更の概要
- 管理画面で、レポート生成時の Polling 処理を Custom Hooks に、UI を別コンポーネントに切り出しました
  - Polling 処理は管理画面のリデザイン後も利用するので、テストを実装ました
  - レポート生成の進捗を表示する UI は、リデザイン後に UI が変わる想定のためテストは書いていません

# スクリーンショット
- リファクタリングなので UI の変更はありませんが、動作確認用のキャプチャです

https://github.com/user-attachments/assets/acb339a2-62ee-4923-9d37-f7103e273032


# 変更の背景
- 管理画面のデザイン変更が予定されているが、コンポーネント分割がされていないのとロジックと UI が分離されていないので、このままデザインの変更を適用することが困難なため

# 関連Issue
- #604

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- client-admin で、レポートの生成中に進捗が更新され、作成が完了したらレポートが閲覧できること

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
  - レポート処理の進捗を視覚的に表示する「ProgressSteps」コンポーネントを追加しました。
- **リファクタ**
  - 進捗表示とポーリング処理を「ProgressSteps」コンポーネントに集約し、レポートカードのコードを簡素化しました。
- **テスト**
  - 進捗ポーリング用カスタムフックの包括的なユニットテストを追加しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client-admin] レポート編集 dialog をコンポーネントとして切り出す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/612)

**作成者:** shgtkshruch  
**作成日:** 2025-06-24T08:48:48Z  
**変更:** +454 -131 (5ファイル)  
**マージ日:** 2025-06-25T01:39:02Z  
**内容:**

# 変更の概要
- レポートの編集 dialog を独立したコンポーネントとして切り出しました
  - こちらのコンポーネントは、管理画面のリデザイン後も利用されるため、Jest でテストを実装しました
  - JSX を使ったコンポーネントのテストのために必要な設定も追加しました

# スクリーンショット
- リファクタリングなので見た目の変更はありませんが、動作確認用のキャプチャーです

https://github.com/user-attachments/assets/a688b11d-d7af-4ddd-a77e-ce617f7b50c5

# 変更の背景
- 管理画面のデザイン変更が予定されているが、コンポーネント分割がされていないのとロジックと UI が分離されていないので、このままデザインの変更を適用することが困難

# 関連Issue
- #604 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- client-admin でレポートのタイトルと調査概要を更新できること

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
  - レポートのタイトルと説明を編集できるモーダルダイアログを追加しました。
- **リファクタリング**
  - レポート編集ダイアログの実装を独立したコンポーネントに分離し、コードを整理しました。
- **テスト**
  - レポート編集ダイアログの表示、入力、保存、アクセシビリティを検証するテストを追加しました。
- **チョア**
  - Jestのテスト環境に`structuredClone`のポリフィルを追加しました。
  - TypeScriptで`@testing-library/jest-dom`の型定義を有効化しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (3件)

### [fix: GPUに関連するパッケージの分岐処理が適切に動かなくなっている](https://github.com/digitaldemocracy2030/kouchou-ai/pull/627)

**作成者:** shingo-ohki  
**作成日:** 2025-07-01T10:09:16Z  
**変更:** +6 -5 (4ファイル)  
**内容:**

# 変更の概要
- GPUを利用しない場合は、ビルド時間短縮のため不要なパッケージをインストールしないようにする

# 変更の背景
- 以前 #442 で対応を行ったが十分でなかったため、再び api コンテナのビルド時に不要なパッケージのインストール処理が行われるようになってしまっていた

# 関連Issue
#442 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->
- api コンテナに不要なパッケージがインストールされていないこと
- レポート作成を実行し、エラーなく正常にレポートが作成されること

を確認した

```
$ docker compose exec api pip list | grep torch
torch                     2.7.0+cpu
torchaudio                2.7.0+cpu
torchvision               0.22.0+cpu
```

![Screenshot From 2025-07-01 19-08-05](https://github.com/user-attachments/assets/a9f17278-ade6-42fd-a5b7-adb39b5db34e)

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

* **Chores**
  * Dockerイメージ作成時、GPU版PyTorchのインストール条件を修正しました。
  * PyTorchのバージョンを固定（torch==2.7.0）に変更しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client-admin] レポート一覧の fetch を Server Component で実行する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/626)

**作成者:** shgtkshruch  
**作成日:** 2025-07-01T07:34:14Z  
**変更:** +92 -58 (7ファイル)  
**内容:**

# 変更の概要
- 管理画面のレポート一覧画面で、API キーを指定した fetch を Server Comopnent で実施することで、API キーが client に露出しないようにしました
  - Server で deta fetch が終わることが期待できるので、型定義で不要な optional を削除しました

# スクリーンショット
- UI の変更はありません

# 変更の背景
- adminにおいて、`process.env.NEXT_PUBLIC_ADMIN_API_KEY` でAPIキーを読んでリクエストをfastapiに送っているが、APIキーが漏洩するリスクがある

# 関連Issue
- https://github.com/digitaldemocracy2030/kouchou-ai/issues/547

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- 管理画面のレポート一覧画面が表示できること

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

* **新機能**
  * 複数のレポートを一覧表示する新しいコンポーネントを追加しました。

* **改善**
  * レポート一覧ページがサーバーサイドレンダリングに対応し、データ取得やエラーハンドリングが改善されました。
  * レポート関連コンポーネントで、配列の受け渡しが常に必須となり、より堅牢な挙動となりました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client-admin] AI サービスとの API 接続チェックの Dialog を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/625)

**作成者:** shgtkshruch  
**作成日:** 2025-07-01T07:13:06Z  
**変更:** +802 -120 (10ファイル)  
**内容:**

# 変更の概要
- API のチェックをする UI をページから Dialog に変更しました
  - Figma: https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=266-2578&t=walX872gM1k44Efs-0
  - Dialog はレポート作成画面に配置しています
  - これまでの環境検証ページは削除しました
  - バックエンドにリクエストを投げる処理を [Server Functions ](https://ja.react.dev/reference/rsc/server-functions)で実装して、API キーが client に露出しないようにしました

# スクリーンショット
## capture

https://github.com/user-attachments/assets/d273c464-4852-4567-9d32-cf8493b80474

## 初期状態
![image](https://github.com/user-attachments/assets/d38ec2e1-dab7-468a-824a-b50d6a916798)

## 成功時
![image](https://github.com/user-attachments/assets/cd0455a4-be88-4147-85b9-0d11cee9c64a)

## 認証エラー
![image](https://github.com/user-attachments/assets/2970ecb3-f9e1-48eb-a9d8-88e650dd5144)

## 残高不足
![image](https://github.com/user-attachments/assets/faa479f4-ff3f-4141-8dec-3398529692dc)

## レート制限
![image](https://github.com/user-attachments/assets/98f9be12-b158-4ce5-b0bf-21b4a929fc22)

## 不明なエラー
![image](https://github.com/user-attachments/assets/443689ef-3573-49ac-af0b-9be7e3497fd1)


# 変更の背景
- OpenAIのAPIKeyが正しくセットされているのかどうかが、実際にレポートの作成を始めるまで分からない

# 関連Issue
- #400 
- #547

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- レポート作成画面に、API をチェックするダイアログがあること
- ダイアログから API のチェックができること

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

* **新機能**
  * AIプロバイダーのAPI接続と残高を確認できる「環境チェックダイアログ」を作成フォームに追加しました。
  * 環境チェック用のカスタムアイコンを追加しました。
  * レポート作成時にAPI利用料が発生する旨の注意文を追加しました。

* **削除**
  * 管理画面の「環境検証」ページおよびそのナビゲーションリンクを削除しました。

* **テスト**
  * 環境チェックダイアログおよびAPI検証機能に対するユニットテストを追加しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [Replace random sampling with Farthest Point Sampling for better spatial coverage](https://github.com/digitaldemocracy2030/kouchou-ai/pull/609)

**作成者:** shinta.nakayama+Devin  
**作成日:** 2025-06-20T08:19:46Z  
**変更:** +14 -1 (1ファイル)  
**内容:**

# Replace Random Sampling with Farthest Point Sampling for Better Spatial Coverage

## Overview
This PR replaces the current random sampling implementation in the hierarchical merge labelling step with Farthest Point Sampling (FPS) to achieve better spatial coverage of opinions across the entire opinion space.

## Changes Made
- **Added fpsample library import** to `hierarchical_merge_labelling.py`
- **Replaced random sampling logic** in `process_merge_labelling` function with FPS using x,y coordinates
- **Added robust error handling** to fallback to random sampling if x,y coordinates are unavailable or FPS fails
- **Maintained existing interface** - no changes to function signatures or sampling_num parameter behavior

## Benefits
- **Better spatial coverage**: FPS selects points that are maximally distant from each other in the x,y coordinate space
- **More representative sampling**: Ensures comprehensive coverage of the opinion space rather than potentially clustering around similar spatial regions
- **Robust fallback**: Gracefully handles edge cases by falling back to original random sampling when needed

## Technical Details
- Uses `fpsample.fps_sampling()` - a high-performance Rust-based FPS implementation (100x faster than numpy)
- Checks for presence of x,y coordinates before applying FPS
- Handles cases where sampling_num >= available data points
- Maintains backward compatibility with existing pipeline configuration

## Testing
- ✅ Lint checks pass (`python -m ruff check .`)
- ✅ Import verification successful
- ✅ Error handling tested for missing coordinates scenario

## Link to Devin run
https://app.devin.ai/sessions/ad4f0bb2409a43c798480409db4c336d

## Requested by
shinta.nakayama@gmail.com


**コメント:** なし

---

