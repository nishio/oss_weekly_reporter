# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-06-18T12:31:34.393831+09:00 から 2025-06-25T12:31:34.393831+09:00 まで

## Issues

### 過去7日間に完了されたissue (3件)

### [[REFACTOR] レポーター情報のデフォルト値を空にしたい（なってる?）](https://github.com/digitaldemocracy2030/kouchou-ai/issues/590)

**作成者:** UtkNggc  
**作成日:** 2025-06-05T16:09:40Z  
**内容:**

## 背景
https://github.com/digitaldemocracy2030/kouchou-ai/issues/438 にて、今までAbout情報だったものをレポーター情報としてまとめた。

## 問題点
metadata.jsonを見たところ、現在はデフォルトのレポーター情報にdd2030の情報が入ってるみたいで、初期値は何もない方が自然なので空にしたい。

<img width="1046" alt="Image" src="https://github.com/user-attachments/assets/7b8c31fe-8f71-4c0d-8614-43832f602e85" />


## 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->
初期値を空にする。
空にすると、「レポーター情報が未設定です。〜」という表示になるはず。
<img width="524" alt="Image" src="https://github.com/user-attachments/assets/93877486-6352-45ac-9879-9c22bc8832a1" />

※もしも私が見てるファイルがちがってて問題なかったら本Issueは閉じちゃってくださいー！！

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

### [[FEATURE]レポート一覧画面：レポートタイトルと本文に文字数制限](https://github.com/digitaldemocracy2030/kouchou-ai/issues/427)

**作成者:** UtkNggc  
**作成日:** 2025-05-04T16:51:40Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

<img width="677" alt="Image" src="https://github.com/user-attachments/assets/197f3a31-0800-4956-a94c-929b335e9020" />

本画面は一覧の役割をもつページである。
長いテキストが流し込まれた時にそれが全部表示されると一覧性が阻害されてしまうため、ある程度で文字をカットしたい。

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
▼以下の議論をしたうえで、
①制限が必要かどうか（もしかしたら何か意図があって制限してないのかも説）
②どう制限するか（文字数や行数など）

２で確定した仕様でデザイン調整したいです。
ちなみにデザイン観点では行数で制限した方がスマートですがwantくらいの温度感です。

**コメント:** なし

---

### 過去7日間に作成されたissue (1件)

### [[FEATURE] フォームから入力された API Key を使ってレポートを生成できる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/613)

**作成者:** shingo-ohki  
**作成日:** 2025-06-24T11:19:25Z  
**内容:**

# 背景
- 現状の広聴AIは、セットアップのためにある程度のテクニカルスキル(git, コマンドライン操作など)が必要であり、
利用にはこの部分が一定のハードルになっている。
- DD2030 のドメインで Azure 環境に動作確認やデモ環境を準備しようという動きがある。
- フォームから入力したAPI Key を使ってレポート生成ができるようになれば、上記のデモ環境でユーザーがセットアップ作業なしに広聴AIを試すことができる

# 提案内容
フォームから入力された API Key を使ってレポートを生成できるようにする

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(2件)

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

## Pull Requests

### 過去7日間にマージされたPR (5件)

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

### [[client-admin] トークン使用量等を計算するロジックを Custom Hook に切り出す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/611)

**作成者:** shgtkshruch  
**作成日:** 2025-06-23T10:04:21Z  
**変更:** +255 -183 (4ファイル)  
**マージ日:** 2025-06-24T06:57:54Z  
**内容:**

# 変更の概要
- client-admin のレポート一覧ページで、トークンの使用量やコストを計算するロジックを Custom Hook に切り出して、ロジックと UI を分離しました
- 新しい client-admin の UI に移行しやすいようにするために、不要なロジックを削除しました

# スクリーンショット
- リファクタリングなので、見た目の変更はありません

# 変更の背景
- トークンの使用量やコストを計算する Custom Hook に切り出す
  - Custom Hook にしてテストしやすくなったので、Jest のテストも [co-location](https://www.mizdra.net/entry/2022/12/11/203940) する形で追加
- 今進行している client-admin のリデザイン([Figma](https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=1117-6204&t=lLYRYfA3mwpMG5e9-4))では、レポート生成中にトークンの使用量やコストを閲覧する UI はなくなっているので、そのためのロジックを削除しました
  - レポート生成後にインフォマークからコストは確認可能になる
  ![image](https://github.com/user-attachments/assets/a0853fbb-3c27-44e0-a3b2-cac6466ff85c)
  - レポート生成中はコストを確認する UI はない
  ![image](https://github.com/user-attachments/assets/215daee4-2eab-4d5c-b7a0-f846d3487f59)
  - 個人的にも分析後に最終的なコストが見えていれば十分に思ったので、上記の方針で実装していますが、何か気になる点があればコメントいただけると 🙏 
- レポート作成後の画面の更新処理が二箇所に実装されていたので、一箇所にまとめました
  - 現状の実装では全てのレポートのコンポーネント内で更新処理を実装していますが、本来は作成中のレポートのみで更新処理を呼べば良いはずだと思っています
  - ただ、ここに手を入れると本来の PR のスコープから外れてしまうので、後続の PR でリファクタリング予定です

# 関連Issue
- #604 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- client-admin でコストの表示がリファクタリング前後で変わっていないこと
- Jest のテストがパスすること

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
  - レポートのトークン使用量や推定コストの表示が改善され、詳細な情報やフォールバックメッセージが分かりやすくなりました。
  - 新しいカスタムフックが導入され、トークン使用量やコスト情報の取得と表示がより効率的に行われるようになりました。

- **バグ修正**
  - トークン使用量やコスト情報がない場合の表示が適切に処理されるようになりました。

- **テスト**
  - トークン使用量やコスト情報の表示に関する新しいテストが追加されました。

- **その他**
  - テスト設定に新しいファイル拡張子の対応が追加されました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client] レポートのタイトルと本文に行数制限を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/610)

**作成者:** shgtkshruch  
**作成日:** 2025-06-20T08:33:20Z  
**変更:** +2 -2 (1ファイル)  
**マージ日:** 2025-06-23T00:42:51Z  
**内容:**

# 変更の概要
- client のレポート一覧画面で、レポートの一覧性を向上させるために、デバイスサイズに応じて適切な行数でレポートのタイトルと説明文を省略表示するようにしました

# スクリーンショット
## SP
タイトルは2行、説明文は3行以上になったら省略表示にします。

![localhost_3000_ (4)](https://github.com/user-attachments/assets/5bc619fc-18e1-4bf5-ab09-b3d0ac66bc82)

## タブレット以上
タイトル・説明文共に2行以上になったら省略表示にします。

![localhost_3000_ (3)](https://github.com/user-attachments/assets/fb46f912-8dae-42e5-8f01-5e7fa5d1b446)


# 変更の背景
- Chakra UI にテキストを特定の行数以上の場合に省略表示にする props があるので、そちらを利用して実装しました
  - https://chakra-ui.com/docs/components/text#line-clamp

# 関連Issue
- fix: #427

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

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
  - レポートリストカードのタイトルと説明文に行数制限を追加し、テキストの表示が2～3行で切り取られるようになりました。これにより、レイアウトの一貫性が向上し、テキストのはみ出しが防止されます。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [不要になったコメントを削除](https://github.com/digitaldemocracy2030/kouchou-ai/pull/608)

**作成者:** shingo-ohki  
**作成日:** 2025-06-19T15:36:16Z  
**変更:** +0 -1 (1ファイル)  
**マージ日:** 2025-06-19T16:04:31Z  
**内容:**

# 変更の概要
- #607 の修正で不要になったコメントを削除します

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

レポーターの表示部分に特に影響がないことを確認しました。

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
  - コメント行を削除し、コードの可読性を向上させました。ユーザー向けの機能や表示に変更はありません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client] meta タグやレポーター情報の初期値を変更する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/607)

**作成者:** shgtkshruch  
**作成日:** 2025-06-18T13:53:22Z  
**変更:** +6 -6 (3ファイル)  
**マージ日:** 2025-06-19T15:25:39Z  
**内容:**

# 変更の概要
- デフォルトの metadata の内容を検索エンジンで表示されて違和感のないものに変更
- カスタムの metadata がない場合は、レポーター名に「名前未設定ユーザー」と表示する

# スクリーンショット

## client トップページの meta タグ
![image](https://github.com/user-attachments/assets/96241178-5419-481d-8b4d-991758f09e08)

## レポーター表示
![image](https://github.com/user-attachments/assets/600844bf-3fa8-4242-bac2-d2483bc5b23d)


# 変更の背景
- reporter の初期値をテスト環境 -> 名称未設定ユーザーに変更
  - 実際に起きているのはメタデータが未設定で、環境の問題ではないため
- レポーター情報を表示するコンポーネントでも、metadata がない場合にユーザー名として「名前未設定ユーザー」と表示する
  - 上記の変更と合わせて client に表示される情報と meta タグ内の情報を揃える
- titile から「デジタル民主主義2030」の文言を削除
  - 複数のページで同じ内容が載ってることで、検索エンジンに忌避されるリスクがあるため
  - 現状でも client のレポート個別ページでは「デジタル民主主義2030」の文言はないので、そちらとも揃う

# 関連Issue
- fix: #590 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- metadata を未設定の状態で、client の meta タグが適切に表示され、レポーター情報に「名前未設定ユーザー」と表示されること
- metadata を設定した状態で、その情報をもとに meta タグが設定されて、レポーター情報にも表示されること

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
  - デフォルトのレポーター名が「名前未設定ユーザー」に変更されました。
- **改善**
  - メタデータのタイトル表示がより分かりやすい形式になりました。
  - レポーター名が常に表示されるようになりました。
- **ドキュメント**
  - メタデータの説明文が、レポーター情報未設定時の案内に更新されました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (1件)

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

### 過去7日間に更新されたPR（作成・マージを除く）(3件)

### [[client] デザインシステムの Button を適用する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/602)

**作成者:** shgtkshruch  
**作成日:** 2025-06-15T06:35:35Z  
**変更:** +188 -65 (5ファイル)  
**内容:**

# 変更の概要
- Figma で作成中のデザインシステムの Button コンポーネントを client に適用します
- Figma: https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=931-3156&t=dDDYeVZGk6s6vTGD-4
![image](https://github.com/user-attachments/assets/fce555ba-00af-4cf8-b34d-0c5a1902cb34)

# スクリーンショット
通常の表示はこれまでと同じです。

![localhost_3000_](https://github.com/user-attachments/assets/ca17074c-c5dc-4f6c-9fe2-47435ca21eb3)

hover 時に背景色が変わって box-shadow がつくようになりました。

![image](https://github.com/user-attachments/assets/64d1f5d5-db7a-4ac3-8e9d-e8e1b48baa06)

# 変更の背景
- Figma を参考に Button コンポーネントを追加しました
  - これまで独自にスタイリングしていたコードが共通コンポーネントになりました
- client の以下の要素に上記の Button コンポーネントを適用しました
  - レポーターの表示 UI
  - Footer

# 関連Issue
- fix: #599 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- client の画面で、レポーター UI と Footer にデザインシステムの Button コンポーネントが反映されていること

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
  - カスタムボタンコンポーネントを追加し、統一されたボタンスタイル（primary、secondary、tertiary、ghost）とサイズバリエーション（xs、md、xl）を導入しました。
  - ボタン用の新しいカラートークンを追加しました。

- **リファクタ**
  - 既存のボタンを新しいUIボタンコンポーネントに置き換え、スタイル指定を簡素化しました。
  - すべてのボタンのバリアント指定を標準化し、個別のカスタムスタイルを削除しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client] レポーター画像が Docker 環境で取得できないエラーを修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/595)

**作成者:** shgtkshruch  
**作成日:** 2025-06-09T09:09:13Z  
**変更:** +40 -30 (3ファイル)  
**内容:**

# 変更の概要
- #581 で追加した Reporter コンポーネントで、レポーターの画像が  Docker Compose 起動時に取得できないエラーが出ていたので修正しました
```
Failed to fetch reporter image: TypeError: fetch failed
client-1               |     at async a (.next/server/chunks/296.js:1:399) {
client-1               |   [cause]: [AggregateError: ] { code: 'ECONNREFUSED' }
client-1               | }
```

# スクリーンショット
赤枠で囲った画像が今回の修正対象です

![スクリーンショット 2025-06-09 17 26 38](https://github.com/user-attachments/assets/e53c43c6-9981-4fd3-8b4e-cd47c9c14821)

# 変更の背景
- レポーターの画像オプショナルなので、server 側で画像があるかどうかを判定しています
  - client 側で判定すると、画像の有無によってレイアウトがガタつくので、client でレンダリングする前に判定できる server で処理をしています
  - 画像があれば client から取得できる URL を設定した Image コンポーネントを返すようにしました
  - 元の実装で使っていた `getImageFromServerSrc` は[サーバーサイドレンダリング時に `NEXT_PUBLIC_API_BASEPATH` を使っていて](https://github.com/shgtkshruch/kouchou-ai/blob/e9b403e844ddc4a7f33562f681149f28b6379c21/client/app/utils/image-src.ts#L56-L57)、こちらは [cilent rendering 用の `API_BASEPATH`](https://github.com/digitaldemocracy2030/kouchou-ai/blob/e9b403e844ddc4a7f33562f681149f28b6379c21/.env.example#L39-L40) で実装とコメントに差異があるので、一旦使用するのを避けました
- Biome のフォーマット漏れのコードがあったので、合わせて修正しました

# 関連Issue
- #581

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- Docker Comopse 環境でレポータの画像を設定したら、エラーなく表示されること
- Static Build をした場合にもレポーター画像が表示されること

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
  - インポート文やコードの整形、クォートやインデントの統一など、コードスタイルを改善しました。

- **バグ修正**
  - レポーター画像の取得方法を修正し、環境変数を利用したURL生成に変更しました。これにより、画像の取得がより安定します。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client] Dialog を開いた際の Initial Focus を変更する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/593)

**作成者:** shgtkshruch  
**作成日:** 2025-06-06T10:28:03Z  
**変更:** +9 -5 (1ファイル)  
**内容:**

# 変更の概要
- client の Footer 内にある「謝辞」と「免責」の Dialog を開いた際に、閉じるボタンに foucs が当たるようにしました

# スクリーンショット
## 謝辞

![image](https://github.com/user-attachments/assets/e6184ccb-7b74-48d5-93bf-bcd62dfd45ec)

## 免責

![image](https://github.com/user-attachments/assets/dfcb1398-8d3c-4139-a3bb-016c58784d9b)

# 変更の背景
- 元の実装は Chakra UI のデフォルトの挙動で、Dialog 内に出現する Initial Focusable Element にフォーカスが当たるようになっていました
  - おそらくこちらの挙動を実施しているものと思われます
  > ダイアログを実装する際には、ユーザーのフォーカスを設定する場所として最も適切な場所を検討することが重要です。HTMLDialogElement.showModal() を用いて <dialog> を開いたとき、フォーカスは内部で最初のフォーカス可能な要素に設定されます。
ref: [<dialog>: ダイアログ要素 - HTML: ハイパーテキストマークアップ言語 | MDN](https://developer.mozilla.org/ja/docs/Web/HTML/Reference/Elements/dialog#%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B7%E3%83%93%E3%83%AA%E3%83%86%E3%82%A3)
- この挙動によって、「謝辞」の Dialog を開いた際に「[AI Objectives Institute](https://ai.objectives.institute/)」の Link に対して Initial Focus が当たっていました
- 上記のリンクは参考情報を掲載したもので、ユーザーに MUST で閲覧してもらうことを期待した Link ではないので、Initail Focus が当たることは違和感がある
- W3C の Accecibiliy のガイドラインでは追加的な情報を表示する Dialog について最も頻繁に使われそうな要素に focus するのが望ましいという記述があるので、今回は「閉じる」ボタンに Initial Focus を当てるように変更しました
  > If a dialog is limited to interactions that either provide additional information or continue processing, it may be advisable to set focus to the element that is likely to be most frequently used, such as an OK or Continue button.
ref: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/
- Chakra UI で Initial Foucs を設定する方法: https://www.chakra-ui.com/docs/components/dialog#initial-focus

# 関連Issue
- https://github.com/digitaldemocracy2030/kouchou-ai/pull/589#issuecomment-2948651314

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- client で謝辞と免責の Dialog を開いて、閉じるボタンにフォーカスが当たっている

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
  - ダイアログ表示時に「閉じる」ボタンへ初期フォーカスが自動的に当たるようになりました。

- **改善**
  - フォーカス管理とアクセシビリティが向上しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

