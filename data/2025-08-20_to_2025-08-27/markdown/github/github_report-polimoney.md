# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-08-20T12:22:22.671142+09:00 から 2025-08-27T12:22:22.671142+09:00 まで

## Issues

### 過去7日間に完了されたissue (3件)

### [サーバーサイドでのEmailバリデーションの追加](https://github.com/digitaldemocracy2030/polimoney/issues/180)

**作成者:** YukihiroArakawa  
**作成日:** 2025-08-23T07:28:47Z  
**内容:**

## はじめに

`CONTRIBUTING.md`を一読しましたが、このプロジェクトで初めてイシュー作成になります
そのため、手順に誤りなどありましたら、お手数おかけしますが、ご指摘いただけると幸いです。

## 解決・改善したいこと

この提案は、ユーザーがアカウントを新規登録する際に、サーバーサイドでメールアドレスの形式が正しいかを検証する機能を追加するものです。

この改善により、以下のような利点があります。
 
* ユーザーが、メールアドレスの入力ミス（例: @の欠落、ドメインのタイプミスなど）をした場合に、
     その場でエラーに気づくことができます。これにより、「登録したのに確認メールが届かない」といっ
     た問題を未然に防ぎ、スムーズなサービス利用開始を支援します。
* 開発者・サービス運用者は、データベースに不正な形式のメールアドレスが保存されるのを防ぐことが
     できます。これにより、データの整合性が向上し、無効なアドレスへのメール送信エラーや、それに伴
     う調査コストを削減できます。

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

フォークした以下のリポジトリに仮実装をコミットしています。

https://github.com/YukihiroArakawa/forked-polimoney/commit/9a95d2a756f722bb337792c71dd2cfceb392bde7

実装の基本方針としては以下の3点です。

1. 既存データへの影響を抑えるため、DBのCHECK制約としてバリデーションを実装せずにバックエンドのロジックとして実装する
2. Emailのバリデーションはビジネスロジックとみなして、middleware層(service層)で行う
3. バリデーションロジックはmiddleware層とは別クラスで実装して、middleware層から呼出すようにすることで、DBを使わずに軽量なテストをできるようにする

## さいごに

当方針で問題なさそうでしたらPR作成をしようかと思います。

**コメント:** なし

---

### [スマホで開いた時にもSNS共有リンクが表示されるようにする](https://github.com/digitaldemocracy2030/polimoney/issues/172)

**作成者:** noritaka1166  
**作成日:** 2025-08-07T14:19:58Z  
**内容:**

## 解決・改善したいこと
PCから開くと、SNS共有リンクが表示できるが、
スマホで開いた時には、SNS共有リンクが表示されていないため表示したい

## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### [「polimoney」検索結果で表示されるアイキャッチ画像の変更](https://github.com/digitaldemocracy2030/polimoney/issues/101)

**作成者:** Nozomi-M21  
**作成日:** 2025-05-28T13:05:18Z  
**内容:**

## 問題

<!-- どこでどのような問題が起きているかを教えてください。問題の発生する画面の URL や、問題が発生しているときのスクリーンショットや録画を添付していただけると理解の助けになります。 -->
「polimoney」と検索すると、検索結果で出井さんの写真が出てしまっている。
![Image](https://github.com/user-attachments/assets/9e5c3bd0-4d25-4b40-9690-e4d96c0aca53)

<!-- この問題が解決されないと、どのような人がどのように困るか、できれば利用者を主語にして記載してください。 -->
政治的中立性の観点から、特定の方の写真を検索結果に表示させることは避けたい。
## 再現手順（未記入でも構いません）

1.
1.
1.

<!-- どのようにしたらバグが再現されるか、わかれば記載して下さい。 -->

## 修正方法の概要（未記入でも構いません）
DD2030のロゴを指定して表示させる
Google search consoleを調査　etc...

**コメント:** なし

---

### 過去7日間に作成されたissue (0件)

### 過去7日間に更新されたissue（作成・クローズを除く）(1件)

### [[シェア機能]タイトルとサムネイルを変更する](https://github.com/digitaldemocracy2030/polimoney/issues/134)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-06-12T07:50:04Z  
**内容:**

## 解決・改善したいこと

シェアした時に表示されるタイトルとサムネイルの画像がそのページの政治家さんの名前と顔写真の方がいいのではないか。

イメージはspotifyやapple musicのスタイルかなと思われます。


## 具体的な実現方法・実装方法の概要（未記入でも構いません）
今はハードコーディングしているのでDBが整ってからでも

AsIs
タイトル："Polimoney"
サムネイル：Polimoneyのデフォルト画像

ToBe
タイトル：{政治家さんの名前} + "Polimoney"
サムネイル：{政治家さんの顔写真}

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (7件)

### [chore: PR作成時にGO言語のlintを実行するワークフローを作成](https://github.com/digitaldemocracy2030/polimoney/pull/185)

**作成者:** YukihiroArakawa  
**作成日:** 2025-08-25T13:00:33Z  
**変更:** +236 -196 (21ファイル)  
**マージ日:** 2025-08-25T13:01:24Z  
**内容:**

# 変更の概要

PR作成時にGO言語のlintを実行するワークフローを作成しました。
またgofmtを初めてプロジェクトで実行するため、`gofmt -w ./backend`を実行した変更結果についてもコミットしています。

# スクリーンショット

forkしたリポジトリにてbackendディレクトリに変更が入った場合にlintが実行されるようになっていることを確認済みです。

https://github.com/YukihiroArakawa/forked-polimoney/actions/runs/17209158801/job/48816436244?pr=1

<img width="1268" height="1091" alt="Screenshot from 2025-08-25 21-44-04" src="https://github.com/user-attachments/assets/f0ad1e89-e247-4c90-bc70-8c2d1678c967" />

<img width="1268" height="1091" alt="Screenshot from 2025-08-25 21-51-16" src="https://github.com/user-attachments/assets/88d82159-ecf7-4550-8d5e-950a63a491ad" />



# 変更の背景

nextjsのリントを実行するワークフローは存在していたためGo言語についても同様に追加しました。


# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- チョア
  - PR時に自動でGoコードのフォーマットを検査するワークフローを追加し、不整形がある場合は失敗させることで一貫性を強化。
- スタイル
  - バックエンド全体でインデントや空白などのコード整形を実施。機能的な挙動の変更はなし。
- テスト
  - 改行・空白の整理などの整形を実施。パスワード検証の前処理をより実運用に近い形へ更新。テストの期待値・挙動は維持。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [refactor: オプショナルチェーンを使用](https://github.com/digitaldemocracy2030/polimoney/pull/184)

**作成者:** noritaka1166  
**作成日:** 2025-08-24T10:47:21Z  
**変更:** +1 -2 (1ファイル)  
**マージ日:** 2025-08-24T11:05:03Z  
**内容:**

# 変更の概要
オプショナルチェーンを使用して、条件文を簡単にした  
合わせて、AIを使って生成したと思われるコメントを削除

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
軽微なリファクタリング

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- 新機能
  - なし（本リリースでのユーザー向け新機能はありません）

- リファクタリング
  - データ取得時のガード条件を簡潔化し、未定義の場合も安全に処理するよう改善（表示や操作への影響なし）

- スタイル
  - 不要なコメントを削除（機能・表示への影響なし）

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [refactor: SNSボタンコンポーネントの分離](https://github.com/digitaldemocracy2030/polimoney/pull/183)

**作成者:** noritaka1166  
**作成日:** 2025-08-24T10:36:15Z  
**変更:** +86 -68 (1ファイル)  
**マージ日:** 2025-08-24T11:05:13Z  
**内容:**

# 変更の概要
SNSボタンコンポーネントの分離

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
コンポーネントの中でコンポーネントを定義するのは、  
あまり良くないのでリファクタリング

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- スタイル
  - コピー状態の視覚フィードバックを改善。未コピー時は灰色のコピーアイコン、コピー後は緑色のチェックを表示。スクリーンリーダー向けタイトルも「URLをコピー」/「コピー済み」に自動切替。
- リファクタ
  - 共有ボタン群の内部構成を整理し再利用性を向上。既存の共有フロー、ポップオーバー、コピー動作と1.5秒のフィードバックは従来通り。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat: backendにemailのバリデーションロジックを追加](https://github.com/digitaldemocracy2030/polimoney/pull/182)

**作成者:** YukihiroArakawa  
**作成日:** 2025-08-23T08:57:40Z  
**変更:** +91 -0 (3ファイル)  
**マージ日:** 2025-08-23T09:16:51Z  
**内容:**

# 変更の概要

バックエンドのユーザー登録処理において、メールアドレスの形式を検証するバリデーション機能を追加しました。

主な変更点は以下の通りです。
- `middleware.Signup` 関数にバリデーションチェックを導入
- バリデーションロジックを責務分離のため `middleware/validators` パッケージとして新規作成
- `net/mail` 標準パッケージを利用した堅牢なメールアドレス形式チェック
- テスト駆動開発（TDD）に基づき、バリデーション用のテストコードを実装

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景

これまでユーザー登録時にメールアドレスの形式チェックが行われておらず、不正な形式のデータが登録される可能性がありました。
この変更により、サーバーサイドでメールアドレスの有効性を検証し、データの整合性を担保することを目的としています。
また、今後の拡張性を考慮し、バリデーションに関するロジックは独立したパッケージとして実装しました。

# 関連Issue

https://github.com/digitaldemocracy2030/polimoney/issues/180

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- 新機能
  - サインアップ時にメールアドレスの形式を検証し、不正な場合は「無効なメールアドレスです」と表示されるようになりました。入力品質の向上により、登録時のエラーを早期に発見できます。
- テスト
  - 代表的な有効・無効なメールアドレスを対象にした検証テストを追加し、バリデーションの動作を確認しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [プロフィール用エンドポイントを用意](https://github.com/digitaldemocracy2030/polimoney/pull/181)

**作成者:** shumizu418128  
**作成日:** 2025-08-23T08:10:54Z  
**変更:** +125 -0 (3ファイル)  
**マージ日:** 2025-08-23T08:11:09Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
プロフィール用エンドポイントを用意
TODO: DBの詳細仕様策定とかAzure設定とか

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->
#120 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- 新機能
  - 認証済みユーザー向け「マイページ」APIを追加。/api/v1/profile（GET）で自分のプロフィールを取得可能。
  - 成功時はユーザーデータをJSONで返却。未認証は401、該当ユーザーがいない場合は404、その他のエラーは500を返します。
- セキュリティ
  - 新APIはJWT認証を必須化。
- 影響範囲
  - 既存の管理者・ユーザー向けエンドポイントへの影響はありません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [chore: BUG Report の形式不備修正](https://github.com/digitaldemocracy2030/polimoney/pull/179)

**作成者:** noritaka1166  
**作成日:** 2025-08-23T03:54:49Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-08-23T07:42:29Z  
**内容:**

# 変更の概要
BUG Report で ダブルクォート が1つ抜けていたので修正

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

- チョア
  - GitHub のバグ報告テンプレートの YAML 構文エラーを修正し、labels が ["DEV", "bug"] として正しく適用されるようにしました。フロントマターの整合性が保たれ、バグ報告時の自動ラベル付けが安定します。プロダクト機能や画面への影響はありません。
  - 変更は最小で、他の内容変更はありません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [VS Code のフォーマッタ設定を追加](https://github.com/digitaldemocracy2030/polimoney/pull/178)

**作成者:** grassfieldk  
**作成日:** 2025-08-20T14:36:12Z  
**変更:** +19 -1 (1ファイル)  
**マージ日:** 2025-08-20T15:25:07Z  
**内容:**

# 変更の概要
Visual Studio Code でのフォーマッタ設定を追加（`.vscode/settings.json`）

# 変更の背景
Visual Studio Code のデフォルト設定として Prettier などの別のフォーマッタを設定している場合でも biome によるフォーマットを行うように設定を追加

# 関連Issue
なし

# CLAへの同意

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- Chores
  - VS Code 設定を更新し、JSON/JSONC/JavaScript/TypeScript/JSX/TSX の既定フォーマッタを Biome に統一。cSpell の設定を維持しつつ整備。実行時の挙動や機能への影響はありません。
- Style
  - 編集時の自動整形を一貫化し、開発環境間でのコードスタイルの再現性を向上。不要な差分を抑制し、レビュー効率を改善します。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

