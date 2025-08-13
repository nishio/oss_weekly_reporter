# GitHub レポート: digitaldemocracy2030/website

期間: 2025-08-06T12:32:26.599131+09:00 から 2025-08-13T12:32:26.599131+09:00 まで

## Issues

### 過去7日間に完了されたissue (1件)

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

### 過去7日間に作成されたissue (0件)

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (2件)

### [week21](https://github.com/digitaldemocracy2030/website/pull/155)

**作成者:** kuboon  
**作成日:** 2025-08-06T09:56:02Z  
**変更:** +339 -0 (5ファイル)  
**マージ日:** 2025-08-06T10:02:50Z  
**内容:**

内容なし

**コメント:** なし

---

### [week20](https://github.com/digitaldemocracy2030/website/pull/154)

**作成者:** kuboon  
**作成日:** 2025-08-04T09:32:01Z  
**変更:** +350 -0 (5ファイル)  
**マージ日:** 2025-08-06T00:49:16Z  
**内容:**

内容なし

**コメント:** なし

---

### 過去7日間に作成されたPR (3件)

### [chore: marked を v15 から v16 へアップデート](https://github.com/digitaldemocracy2030/website/pull/158)

**作成者:** noritaka1166  
**作成日:** 2025-08-09T14:53:58Z  
**変更:** +6 -6 (2ファイル)  
**内容:**

marked を v15 から v16 へアップデート
- <https://github.com/markedjs/marked/releases>
  - `npm run build` でエラーにならないこと、`npm run dev` で動かしてみて問題なく表示されていることを確認済み
 
node v20 未満はサポート対象外になりましたが、 node v20未満は既にEOLであり、  
使用していないかと思うので問題なしと判断しています

**コメント:** なし

---

### [feat: HSTS の設定を追加](https://github.com/digitaldemocracy2030/website/pull/157)

**作成者:** noritaka1166  
**作成日:** 2025-08-09T01:57:07Z  
**変更:** +13 -0 (1ファイル)  
**内容:**

よりセキュアにするため HSTS の設定を追加
- <https://nextjs.org/docs/pages/api-reference/config/next-config-js/headers>
-  <https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security>

http を使っている箇所はないかと思うので、下記で設定
- max-age は 2年が推奨されているので 63072000 に設定
- includeSubDomains あり
- preload あり
<img width="898" height="499" alt="スクリーンショット 2025-08-09 午前10 55 46" src="https://github.com/user-attachments/assets/0cabb0df-cfe5-4ba1-a287-1d762607d468" />

<https://developer.chrome.com/docs/lighthouse/best-practices/has-hsts?hl=ja>




**コメント:** なし

---

### [fix: polimoney の活用事例のリンクを修正](https://github.com/digitaldemocracy2030/website/pull/156)

**作成者:** noritaka1166  
**作成日:** 2025-08-06T16:10:15Z  
**変更:** +3 -3 (1ファイル)  
**内容:**

polimoney の活用事例のリンクが切れてしまっていたため、修正

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

