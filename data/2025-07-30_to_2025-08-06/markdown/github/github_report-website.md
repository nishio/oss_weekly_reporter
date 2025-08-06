# GitHub レポート: digitaldemocracy2030/website

期間: 2025-07-30T12:38:10.561104+09:00 から 2025-08-06T12:38:10.561104+09:00 まで

## Issues

### 過去7日間に完了されたissue (1件)

### [polimoney紹介コーナーにpolimoneyサイトリンクを貼る](https://github.com/digitaldemocracy2030/website/issues/144)

**作成者:** shumizu418128  
**作成日:** 2025-07-20T10:45:35Z  
**内容:**

https://dd2030.org/ （polimoneyの紹介をしている部分）
https://dd2030.org/polimoney

これらのヘッダーと画像の間にURL https://polimoney.dd2030.org/ を貼りたい

**コメント:** なし

---

### 過去7日間に作成されたissue (0件)

### 過去7日間に更新されたissue（作成・クローズを除く）(1件)

### [Slack への参加ができない（もしくは受付終了の案内がされていない）](https://github.com/digitaldemocracy2030/website/issues/153)

**作成者:** grassfieldk  
**作成日:** 2025-07-29T12:14:58Z  
**内容:**

※ 本リポジトリへのコントリビューション規約が見当たらなかったため外部のものですが Issue を立てました、問題あれば遠慮なく削除ください

https://dd2030.org/co-creation 下部にある Slack への参加ボタンからワークスペースへの参加ができませんでした

私は本日（2025/07/29）参加しようとしたのですが、
参加ボタンから Slack へアクセスしてメールで届いた認証コードを入力するとワークスペースに存在しないユーザーである旨のメッセージが表示され、参加ができませんでした

[安野氏のツイート](https://x.com/takahiroanno/status/1900073162370658464) にある招待リンクはすでに有効期限が切れているところを見ると
現在はもう参加を募っていないのでしょうか？

もし有効期限が切れているだけであればリンクなどの更新をしていただきたいです
募集を終了しているのであればその旨をサイトに記載するか、Slack のリンクを削除するかしたほうがよいのではと思いました

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (5件)

### [week20](https://github.com/digitaldemocracy2030/website/pull/154)

**作成者:** kuboon  
**作成日:** 2025-08-04T09:32:01Z  
**変更:** +350 -0 (5ファイル)  
**マージ日:** 2025-08-06T00:49:16Z  
**内容:**

内容なし

**コメント:** なし

---

### [chore: npm audit fix 実行](https://github.com/digitaldemocracy2030/website/pull/150)

**作成者:** noritaka1166  
**作成日:** 2025-07-26T11:28:11Z  
**変更:** +241 -225 (1ファイル)  
**マージ日:** 2025-07-30T07:07:27Z  
**内容:**

`npm audit` 実行時にいくつか脆弱性が出ていたので `npm audit fix` を実行しました  

`npm run dev` で問題なく動作すること、`npm run build` と `npm run lint` が動くことを確認済み
```
@eslint/plugin-kit  <0.3.3
Severity: high
@eslint/plugin-kit is vulnerable to Regular Expression Denial of Service attacks through ConfigCommentParser - https://github.com/advisories/GHSA-xffm-g5w8-qvg7
fix available via `npm audit fix`
node_modules/@eslint/plugin-kit
  eslint  9.10.0 - 9.26.0
  Depends on vulnerable versions of @eslint/plugin-kit
  node_modules/eslint

brace-expansion  1.0.0 - 1.1.11 || 2.0.0 - 2.0.1
brace-expansion Regular Expression Denial of Service vulnerability - https://github.com/advisories/GHSA-v6h2-p8h4-qcjw
brace-expansion Regular Expression Denial of Service vulnerability - https://github.com/advisories/GHSA-v6h2-p8h4-qcjw
fix available via `npm audit fix`
node_modules/@typescript-eslint/typescript-estree/node_modules/brace-expansion
node_modules/brace-expansion

next  15.3.0 - 15.3.2
Next.js has a Cache poisoning vulnerability due to omission of the Vary header - https://github.com/advisories/GHSA-r2fc-ccr8-96c4
fix available via `npm audit fix`
node_modules/next

4 vulnerabilities (2 low, 2 high)
```

**コメント:** なし

---

### [refactor: オプショナルチェーンを使用](https://github.com/digitaldemocracy2030/website/pull/149)

**作成者:** noritaka1166  
**作成日:** 2025-07-26T11:10:11Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-07-30T07:04:17Z  
**内容:**

より簡潔で読みやすくするため、代わりにオプショナルチェーンを使用するようにリファクタリングしました

**コメント:** なし

---

### [Footerコンポーネントから不要なspanを削除](https://github.com/digitaldemocracy2030/website/pull/148)

**作成者:** noritaka1166  
**作成日:** 2025-07-26T11:05:31Z  
**変更:** +0 -5 (1ファイル)  
**マージ日:** 2025-07-30T05:59:46Z  
**内容:**

Footer に 空の spanタグが入っていますが、不要かと思うので削除しました
<img width="592" height="116" alt="スクリーンショット 2025-07-26 午後8 01 21" src="https://github.com/user-attachments/assets/8d25d99b-0f83-40b9-8e4f-ebf03da2a39b" />

これにより少しリンク同士の間隔が狭まりましたが、問題ないレベルかと思います。
<img width="582" height="145" alt="スクリーンショット 2025-07-26 午後8 03 59" src="https://github.com/user-attachments/assets/e504b2d3-5218-4b82-afb8-0971edf8158c" />


**コメント:** なし

---

### [feat: Polimoney Webサイトのリンクの追加](https://github.com/digitaldemocracy2030/website/pull/146)

**作成者:** takeruhukushima  
**作成日:** 2025-07-26T05:26:05Z  
**変更:** +38 -1 (4ファイル)  
**マージ日:** 2025-07-30T05:58:28Z  
**内容:**

トップページとPolimoneyのページにPolimoneyのウェブサイトへのリンクを追加しました。

fixes #144 

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

