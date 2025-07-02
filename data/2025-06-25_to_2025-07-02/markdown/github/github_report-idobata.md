# GitHub レポート: digitaldemocracy2030/idobata

期間: 2025-06-25T12:31:43.650858+09:00 から 2025-07-02T12:31:43.650858+09:00 まで

## Issues

### 過去7日間に完了されたissue (1件)

### [シードデータを投入できない。](https://github.com/digitaldemocracy2030/idobata/issues/408)

**作成者:** nishidashib  
**作成日:** 2025-06-19T13:07:18Z  
**内容:**

## 問題

<!-- どこでどのような問題が起きているかを教えてください。問題の発生する画面の URL や、問題が発生しているときのスクリーンショットや録画を添付していただけると理解の助けになります。 -->

<!-- この問題が解決されないと、どのような人がどのように困るか、できれば利用者を主語にして記載してください。 -->
[https://github.com/digitaldemocracy2030/idobata/tree/main/idea-discussion#シードデータの投入方法](https://github.com/digitaldemocracy2030/idobata/tree/main/idea-discussion#%E3%82%B7%E3%83%BC%E3%83%89%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E6%8A%95%E5%85%A5%E6%96%B9%E6%B3%95) を参考に
シードデータを投入しようとしたができなかった。

## 修正方法の概要（未記入でも構いません）
[backendのコード](https://github.com/digitaldemocracy2030/idobata/blob/main/idea-discussion/backend/controllers/importController.js)を確認すると、`themeId` をpathに追加しないといけないことがわかった。
実際に修正後のendpointではシードデータを投入することができた。

**コメント:** なし

---

### 過去7日間に作成されたissue (1件)

### [api側のCORSエラー判定を少し緩くしたい。](https://github.com/digitaldemocracy2030/idobata/issues/412)

**作成者:** nishidashib  
**作成日:** 2025-06-25T15:37:18Z  
**内容:**

## 解決・改善したいこと
idea-backendの環境変数でCORS 設定するための`IDEA_CORS_ORIGIN`という設定値があるが、
,区切りの前後にスペースがあるだけで、CORSエラーでapiを叩けなくなってしまう。

```
OK)  IDEA_CORS_ORIGIN=http://localhost:5173,http://localhost:5175
NG)  IDEA_CORS_ORIGIN=http://localhost:5173, http://localhost:5175 
↑
, の後ろにスペースがあると、後ろのhttp://localhost:5175 がCORSエラーになってしまう。
このあたりの差分はプリ側で巻き取って、後ろのhttp://localhost:5175 もCORSエラーにならないようにしたい。
```
<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）
[このあたりの付近](https://github.com/digitaldemocracy2030/idobata/blob/main/idea-discussion/backend/server.js#L36)で trimなどで前後のスペースを削除する。


**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (1件)

### [シードデータ投入のパスを修正](https://github.com/digitaldemocracy2030/idobata/pull/409)

**作成者:** nishidashib  
**作成日:** 2025-06-19T13:41:21Z  
**変更:** +5 -2 (1ファイル)  
**マージ日:** 2025-06-25T10:06:56Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
シードデータを投入するendpointに`themeId` を追加してシードデータを投入できるようにした。
[backendのコード](https://github.com/digitaldemocracy2030/idobata/blob/main/idea-discussion/backend/controllers/importController.js)を確認すると、`themeId` をpathに追加する必要があったため。


# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
https://github.com/digitaldemocracy2030/idobata/tree/main/idea-discussion#シードデータの投入方法 を参考に
シードデータを投入しようとしたができなかったため。
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->
https://github.com/digitaldemocracy2030/idobata/issues/408
# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### 過去7日間に作成されたPR (1件)

### [api側のCORSエラー判定を少し緩くしたい。](https://github.com/digitaldemocracy2030/idobata/pull/413)

**作成者:** nishidashib  
**作成日:** 2025-06-27T05:06:38Z  
**変更:** +1 -1 (1ファイル)  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
環境変数`IDEA_CORS_ORIGIN` には、ユーザー用frontendとadmin用frontend(= 管理画面)の2つのURLが設定されるはずで、カンマ区切りの前後にスペースがあれば、

たとえば
`IDEA_CORS_ORIGIN=http://localhost:5173,   http://localhost:5175` 
のように、カンマの後ろにspaceが入ると、後ろのURLが文頭にspaceが入った`  http://localhost:5175`となり、正しいURL`http://localhost:5175`と認識されず、CORSエラーになってAPIを叩けない。 
意図せずspaceが入る時があるので、その場合はtrimでspaceを削除し、正しいURLとして認識させたい。

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->
https://github.com/digitaldemocracy2030/idobata/issues/412
# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

