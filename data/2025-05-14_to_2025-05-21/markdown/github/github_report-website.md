# GitHub レポート: digitaldemocracy2030/website

期間: 2025-05-14T12:26:21.150309+09:00 から 2025-05-21T12:26:21.150309+09:00 まで

## Issues

### 過去7日間に完了されたissue (2件)

### [SNSへのシェアボタンを設置する](https://github.com/digitaldemocracy2030/website/issues/80)

**作成者:** akai-OolongBreaker  
**作成日:** 2025-05-13T16:32:13Z  
**内容:**

## 概要
Webサイト全ページにSNSシェアボタンを設置したいです。
人に伝えたいと思ってもらった時に、スムーズにシェアを行って貰えるようにするのが目的です。


## 対応候補SNS
以下がSNSの対応候補です。増やしたり減らしたりする意見があれば伝えて貰いたいです

* X（旧Twitter）
* Facebook
* LINE
* はてなブックマーク


## アイコン素材
各サービスの公式のものか、使用料無料かつ、商用利用可能の画像を探して使用予定です。


## シェアした際の初期文言
ベース文言は `デジタル民主主義2030プロジェクトポータルサイト https://dd2030.org/` の予定で、SNSの雰囲気に合わせて多少変えようと思います。
例えば、ツイッターなら公式アカウントIDも入れるとか。
自分はツイッター以外はあまり馴染みが無いので、もしノウハウあったらお伝えいただけるとありがたいです。


## 実装について
自分が見様見真似でやる予定ですが、得意な方がいらっしゃったら担当してくださったり、ヘルプいただけるとありがたいです！

**コメント:** なし

---

### [ボードメンバーをaboutページに追加する](https://github.com/digitaldemocracy2030/website/issues/43)

**作成者:** moai-redcap  
**作成日:** 2025-04-27T04:49:37Z  
**内容:**

案

[画像]（Xのプロフ画像拝借）
安野 貴博
https://x.com/takahiroanno
[画像]（Xのプロフ画像拝借確認中）
鈴木 健
https://x.com/kensuzuki

こちらのスレッドを要確認
https://w1740803485-clv347541.slack.com/archives/C08K4CUB12T/p1745728260698529

**コメント:** なし

---

### 過去7日間に作成されたissue (3件)

### [DevContainerとBiome.jsの導入](https://github.com/digitaldemocracy2030/website/issues/91)

**作成者:** moai-redcap  
**作成日:** 2025-05-19T07:27:54Z  
**内容:**

プルリク時に、無駄なlintエラー等が頻発している。
開発環境を整えたい。
以下、参考記事
https://zenn.dev/ikoamu/articles/e21d9665b6189e

**コメント:** なし

---

### [googleフォームのリンク入れ替え](https://github.com/digitaldemocracy2030/website/issues/90)

**作成者:** moai-redcap  
**作成日:** 2025-05-19T07:24:14Z  
**内容:**

https://dd2030.org/co-creation
のGoogleフォームへのリンクを以下に変える。


https://docs.google.com/forms/d/e/1FAIpQLScytDD9cdYwcl_Gsr0qal-Op7mpXaQzK3KGTk_FsahY5FkU9w/viewform?usp=header

**コメント:** なし

---

### [シェアボタンを押した時に表示される初期テキストに各画面の内容を反映](https://github.com/digitaldemocracy2030/website/issues/87)

**作成者:** akai-OolongBreaker  
**作成日:** 2025-05-16T12:45:49Z  
**内容:**

## 概要
各SNSのシェアボタンを押すと、現在はどの画面であっても同じ内容が表示されるが、
これを表示している画面の内容に対応したページ名やURLが表示されるようにする。

## 例
 - 現在：デジタル民主主義2030プロジェクトポータルサイト https://dd2030.org/ 
 - 変更後：デジタル民主主義2030プロジェクトポータルサイト - デジタル民主主義 2030 とは？ https://dd2030.org/about

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(2件)

### [活用事例ページをmdで管理できるようにする。](https://github.com/digitaldemocracy2030/website/issues/40)

**作成者:** moai-redcap  
**作成日:** 2025-04-25T08:59:05Z  
**内容:**

活用事例ページをmdで管理できるようにする。

活用事例として
https://delib.takahiroanno.com/view/docs/index.md
を追加。


**コメント:** なし

---

### [ロゴの改善](https://github.com/digitaldemocracy2030/website/issues/8)

**作成者:** nishio  
**作成日:** 2025-03-27T17:17:31Z  
**内容:**

より好ましいロゴに変える議論

>Shutaro Aoyama (ぶるーも)
(仮置きならいいと思いますが、今後この雑ロゴがなし崩し的に採用されるのは望ましくないと思ってます！)
NISHIO Hirokazu
たぶん これ ( #1 ) “good first issue”だけど「画像の差し替え作業が軽い」ってだけであって「どういうロゴが好ましいか」という超重いタスクに依存してんだと思う

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (12件)

### [Fix routing for history pages](https://github.com/digitaldemocracy2030/website/pull/98)

**作成者:** masatosasano2  
**作成日:** 2025-05-19T22:50:11Z  
**変更:** +22 -24 (2ファイル)  
**マージ日:** 2025-05-19T23:30:50Z  
**内容:**

## 問題
/history 系ページが404になる

## 修正の概要
- URL内で /history が重複する
- slug はnextの仕様で1階層分しか受け取れないので、array で複数階層指定できるように変更

## 動作確認結果
<img width="1029" alt="image" src="https://github.com/user-attachments/assets/ec28a7aa-0978-40b1-ba75-020121980918" />

## 備考
local だと out/* と .next/* の2フォルダを消すまで、 `npm run dev` したときに修正前のページのURLを読み込もうとしてエラーになり、サーバ起動に失敗していました。Production モードでも発生する問題なのか調査できていませんが、念の為記載します。

**コメント:** なし

---

### [disable preview deploy](https://github.com/digitaldemocracy2030/website/pull/96)

**作成者:** nishio  
**作成日:** 2025-05-19T15:42:47Z  
**変更:** +5 -3 (1ファイル)  
**マージ日:** 2025-05-19T15:42:55Z  
**内容:**

PRでのpreview deployの挙動が直らないので自動実行をOFFにしました

**コメント:** なし

---

### [週ごとのダイジェスト表示機能を追加](https://github.com/digitaldemocracy2030/website/pull/94)

**作成者:** nishio  
**作成日:** 2025-05-19T08:52:11Z  
**変更:** +33 -22 (3ファイル)  
**マージ日:** 2025-05-19T15:31:16Z  
**内容:**

# 週ごとのダイジェスト表示機能を追加

各週のディレクトリ内に`digest.md`ファイルが存在する場合、その内容を週の見出しとリンクの間に展開表示する機能を追加しました。

## 変更内容
- `app/history/page.tsx`を修正して`digest.md`ファイルを検出する機能を追加
- 週ごとのダイジェスト内容を保存する`weeklyDigests`オブジェクトを追加
- 週の見出しとリンクの間にダイジェスト内容を表示するJSXを追加
- テスト用に`markdown/history/week1_20250319/digest.md`ファイルを作成

## 動作確認
- historyページで週のダイジェスト内容が正しく表示されることを確認
- `digest.md`が存在しない週では何も表示されないことを確認
- マークダウンの書式が正しくレンダリングされることを確認

Link to Devin run: https://app.devin.ai/sessions/dbdac634b1c14515affb00574404bff6
Requested by: NISHIO Hirokazu (nishio.hirokazu@gmail.com)


**コメント:** なし

---

### [Fix PR preview 404 error](https://github.com/digitaldemocracy2030/website/pull/93)

**作成者:** nishio  
**作成日:** 2025-05-19T08:47:46Z  
**変更:** +13 -199 (3ファイル)  
**マージ日:** 2025-05-19T14:44:42Z  
**内容:**

# Fix PR preview 404 error

## 問題
PRのプレビューデプロイが404エラーになっていました。これは、GitHub Pagesへのデプロイ時のファイル構造とPRコメントで使用されるURLパスの不一致が原因です。

## 修正内容
GitHub Actionsのワークフローに新しいステップを追加し、ビルド後にファイル構造を調整するようにしました。これにより、ファイルが正しいパス（`/pr-preview/pr-{PR番号}/`）に配置され、PRコメントのリンクが正常に機能するようになります。

## テスト方法
このPRがマージされた後、新しいPRを作成すると、プレビューデプロイのリンクが正常に機能するはずです。

Link to Devin run: https://app.devin.ai/sessions/150211bb7b2c456c83fde7a0385003f0
Requested by: NISHIO Hirokazu


**コメント:** なし

---

### [マークダウンファイルの構造を整理](https://github.com/digitaldemocracy2030/website/pull/92)

**作成者:** nishio  
**作成日:** 2025-05-19T07:57:14Z  
**変更:** +3393 -106 (41ファイル)  
**マージ日:** 2025-05-19T08:06:12Z  
**内容:**

# マークダウンファイルの構造を整理

マークダウンファイルを階層構造に整理し、historyページの実装を更新しました。

## 変更内容
- markdownファイルを `markdown/history/week{week}_{date}/` ディレクトリに整理
- `slack{week}w.md` → `markdown/history/week{week}_{date}/slack.md`
- `github{week}w-{project}.md` → `markdown/history/week{week}_{date}/{project}.md`
- historyページの実装を更新して新しいディレクトリ構造に対応
- 古い形式との互換性は維持しない（ユーザーの指示による）

## 動作確認
- historyページが正しく表示されることを確認
- 各週のプロジェクトリンクが正しく機能することを確認

Link to Devin run: https://app.devin.ai/sessions/dbdac634b1c14515affb00574404bff6
Requested by: NISHIO Hirokazu (nishio.hirokazu@gmail.com)


**コメント:** なし

---

### [logoコンペページの作成1](https://github.com/digitaldemocracy2030/website/pull/88)

**作成者:** moai-redcap  
**作成日:** 2025-05-17T05:42:36Z  
**変更:** +142 -0 (17ファイル)  
**マージ日:** 2025-05-17T06:17:18Z  
**内容:**

内容なし

**コメント:** なし

---

### [Lintエラー修正](https://github.com/digitaldemocracy2030/website/pull/86)

**作成者:** moai-redcap  
**作成日:** 2025-05-16T11:12:09Z  
**変更:** +15 -17 (2ファイル)  
**マージ日:** 2025-05-16T11:26:20Z  
**内容:**

@akai-OolongBreaker 
こちら、いどばた事例のプルリクを反映させるために修正しました。
`;`がいらないところがあったみたいです

**コメント:** なし

---

### [いどばたの事例としてチームみらいの例を追加](https://github.com/digitaldemocracy2030/website/pull/85)

**作成者:** masatosasano2  
**作成日:** 2025-05-16T10:38:57Z  
**変更:** +5 -1 (1ファイル)  
**マージ日:** 2025-05-16T11:05:11Z  
**内容:**

内容なし

**コメント:** なし

---

### [SNSへのシェアボタンを設置する](https://github.com/digitaldemocracy2030/website/pull/84)

**作成者:** akai-OolongBreaker  
**作成日:** 2025-05-15T19:59:08Z  
**変更:** +214 -0 (5ファイル)  
**マージ日:** 2025-05-16T03:21:54Z  
**内容:**

## 概要
Issue #80 を実装するために、SNSへのシェアボタンを追加しました。

## 変更内容
- SHAREボタンの追加と、押下時にSNSボタン（X、Facebook、LINE、はてブ）が展開される実装
- SNSボタンの表示にはアニメーションを追加（framer-motionを使用）
- モバイル画面で幅が小さい場合は、SNSボタンが下方向に表示
- 使用ライブラリ（react-share, framer-motion）のライセンス情報を `NOTICE` ファイルとして追加

## 備考
- SNSボタンに使用しているアイコンは、react-share が提供するアイコンを使用しています。

## スクショ
- 初期状態
![image](https://github.com/user-attachments/assets/0c63bd25-cc26-45ad-a1b3-a9a1f50428b4)

- 押して展開時
![image](https://github.com/user-attachments/assets/225ef3d9-6552-4b11-ae4e-1664e825e18b)

**コメント:** なし

---

### [Add kouchou-ai Brand Compass link button to detail page](https://github.com/digitaldemocracy2030/website/pull/83)

**作成者:** masatosasano2  
**作成日:** 2025-05-14T14:06:37Z  
**変更:** +8 -0 (1ファイル)  
**マージ日:** 2025-05-15T15:33:20Z  
**内容:**

[Brand Compass](https://www.figma.com/deck/0B55u8rxDjjjpRJbNUEP0Z/%F0%9F%A7%AD-Brand-Compass?node-id=28-1217&t=iTF8igZOaTbM8DMn-1)

![image](https://github.com/user-attachments/assets/93bb970c-25fb-49fe-8cbf-29cb09865fdc)

**コメント:** なし

---

### [/activity to /history](https://github.com/digitaldemocracy2030/website/pull/82)

**作成者:** masatosasano2  
**作成日:** 2025-05-14T13:57:11Z  
**変更:** +6 -6 (5ファイル)  
**マージ日:** 2025-05-14T14:02:08Z  
**内容:**

活動履歴へのリンクを新しい形式のものに置換（以前の置換の対応もれ）

**コメント:** なし

---

### [week9](https://github.com/digitaldemocracy2030/website/pull/81)

**作成者:** nishio  
**作成日:** 2025-05-14T09:08:32Z  
**変更:** +481 -0 (5ファイル)  
**マージ日:** 2025-05-14T09:08:43Z  
**内容:**

内容なし

**コメント:** なし

---

### 過去7日間に作成されたPR (3件)

### [Fix duplicate 'history' in URL paths causing 404 errors](https://github.com/digitaldemocracy2030/website/pull/97)

**作成者:** nishio  
**作成日:** 2025-05-19T17:41:55Z  
**変更:** +21 -19 (3ファイル)  
**内容:**

# URLパスの重複「history」を修正

## 問題
URLパスに「history」が二重に含まれているため、以下のようなURLが404エラーになっていました：
- `/history/history/week1_20250319/slack`
- `/history/history/week8_20250507/slack`

## 修正内容
1. `app/history/page.tsx`でリンク生成時の重複する「history/」を削除
2. `app/history/[slug]/page.tsx`でスラグのパース処理を修正
3. `app/history/[slug]/page.tsx`でナビゲーションリンクの生成を修正
4. `app/history/[slug]/page.tsx`でスラグの末尾のスラッシュを処理するロジックを追加
5. `next.config.ts`のルーティング設定を調整

これにより、正しいURLパス（例：`/history/week1_20250319/slack`）でページが表示されるようになります。

## Link to Devin run
https://app.devin.ai/sessions/1cc73600b90047839846e4df04181bcc

## Requested by
NISHIO Hirokazu (nishio.hirokazu@gmail.com)


**コメント:** なし

---

### [Fix CSS and image loading on top and history pages in PR preview](https://github.com/digitaldemocracy2030/website/pull/95)

**作成者:** nishio  
**作成日:** 2025-05-19T15:12:38Z  
**変更:** +37 -5 (5ファイル)  
**内容:**

# Fix CSS and image loading on top and history pages in PR preview

トップページとhistoryページのPRプレビューでCSSや画像がロードされない問題を修正しました。

## 変更内容
- トップページの画像参照を`basePath`対応に修正
- CSSの読み込みを動的に行い`basePath`を考慮するように変更
- カスタムイメージローダーを追加して画像パスの解決を改善

この変更により、PRプレビュー環境でもトップページとhistoryページのCSSと画像が正しく表示されるようになります。

## テスト結果
- ローカルで`NEXT_PUBLIC_PR_NUMBER=test npm run build`を実行し、ビルドが正常に完了することを確認しました
- 静的エクスポートが正しく生成され、トップページとhistoryページが含まれていることを確認しました

Link to Devin run: https://app.devin.ai/sessions/150211bb7b2c456c83fde7a0385003f0
User: NISHIO Hirokazu


**コメント:** なし

---

### [活用事例ページをmdで管理できるようにする。](https://github.com/digitaldemocracy2030/website/pull/89)

**作成者:** yusasa16  
**作成日:** 2025-05-18T11:31:17Z  
**変更:** +221 -81 (12ファイル)  
**内容:**

## 関連イシュー
#40 

## 備考
[広聴AI](https://dd2030.org/case/kouchou-ai)ページで使われているリンクボタンの見た目を
- 横幅が親要素からはみ出している
- マークダウンでは文章中で使われているリンクとのスタイルの使い分けが難しい

という理由から下線を表示する見た目に変更しています。

また、ページ詳細のスタイルについてはapp/global.cssファイルに直接記載しています。
- ファイルを分けた方がよいか。また希望のファイルパスはあるか。
- `@apply` を使うことについては問題ないか。通常のCSSのプロパティに変換した方がよいか。

についても調整意見ありましたらお願いします。

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

