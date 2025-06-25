# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-06-18T12:31:51.006722+09:00 から 2025-06-25T12:31:51.006722+09:00 まで

## Issues

### 過去7日間に完了されたissue (1件)

### [UIとデータフォーマットの統一](https://github.com/digitaldemocracy2030/polimoney/issues/135)

**作成者:** dotneet  
**作成日:** 2025-06-18T04:31:19Z  
**内容:**

DB化の前タスクとしていったんフォーマットとUIを整理したい。

## データフォーマット

現状３種類形式がある

・デモ用 (Transaction 型)
・実データパターン1 (OldTransaction 型)
・実データパターン2 ((OldTransaction 型, 複数レポート対応)

=> Transaction型, 複数レポート対応 のデータフォーマットに変換して１つにまとめる。

## UI
UIは２種類ある
・トランザクションに日付データあり、サブカテゴリあり、支出目的あり
・トランザクションに上記項目なし

この部分

<img width="1145" alt="Image" src="https://github.com/user-attachments/assets/c1911df8-1bee-4b57-bb7e-18b82e09c1d4" />

<img width="1136" alt="Image" src="https://github.com/user-attachments/assets/4c3280c4-0350-4e7e-bf1a-58f9ee42fb71" />

=> トランザクションを日付データをあり、サブカテゴリあり、支出目的ありに統一する。


## 既存データにない項目の対処

サブカテゴリ：表示しない
支出目的：支出先と同じ内容とする

**コメント:** なし

---

### 過去7日間に作成されたissue (0件)

### 過去7日間に更新されたissue（作成・クローズを除く）(5件)

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

### [認証機能によるプライベート試用環境実装](https://github.com/digitaldemocracy2030/polimoney/issues/120)

**作成者:** TakumiAdachiGWS  
**作成日:** 2025-06-08T08:47:17Z  
**内容:**

## 解決・改善したいこと
一般公開前に政治家の方にプライベート環境で実際に触ってもらいたいが、認証機能とダッシュボードが実装できていない。

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->
0609現在の公開フローとしては、一般公開か否かしかないが、以下のステークホルダニーズにこたえるために認証機能を追加したい。
政治家: 公開前にどのような内容が公開され、またどのようなUXが得られるのかを実際に触ってみたい。
運営側: 後で「このような機能は想定していなかった」というようなクレームを事前に排除しておきたい。

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->
[Slackスレッドリンク](https://dd2030.slack.com/archives/C08FL5L6GSH/p1749362917916339)

## 具体的な実現方法・実装方法の概要（未記入でも構いません）
- 認証機能の付与
- Google Cloud でのダッシュボードデプロイ
（認証機能の付与によるプライベート試用環境が優先）

**コメント:** なし

---

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

### [政治家さんのwebサイト・SNSへのリンク追加](https://github.com/digitaldemocracy2030/polimoney/issues/112)

**作成者:** Nozomi-M21  
**作成日:** 2025-06-04T13:29:46Z  
**内容:**

## 解決・改善したいこと
政治家さんの活動をビュアーに知ってもらうきっかけを作りたい。
資金がどんな活動に使われているのかイメージしやすくなり、政治への関心も高まる。
<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）
政治家さんの公式サイト、SNSへのリンクを追加する

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

### 過去7日間にマージされたPR (5件)

### [Bump urllib3 from 2.4.0 to 2.5.0 in /tools](https://github.com/digitaldemocracy2030/polimoney/pull/140)

**作成者:** dependabot[bot]  
**作成日:** 2025-06-22T10:08:38Z  
**変更:** +3 -3 (1ファイル)  
**マージ日:** 2025-06-22T10:10:16Z  
**内容:**

Bumps [urllib3](https://github.com/urllib3/urllib3) from 2.4.0 to 2.5.0.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/urllib3/urllib3/releases">urllib3's releases</a>.</em></p>
<blockquote>
<h2>2.5.0</h2>
<h2>🚀 urllib3 is fundraising for HTTP/2 support</h2>
<p><a href="https://sethmlarson.dev/urllib3-is-fundraising-for-http2-support">urllib3 is raising ~$40,000 USD</a> to release HTTP/2 support and ensure long-term sustainable maintenance of the project after a sharp decline in financial support. If your company or organization uses Python and would benefit from HTTP/2 support in Requests, pip, cloud SDKs, and thousands of other projects <a href="https://opencollective.com/urllib3">please consider contributing financially</a> to ensure HTTP/2 support is developed sustainably and maintained for the long-haul.</p>
<p>Thank you for your support.</p>
<h1>Security issues</h1>
<p>urllib3 2.5.0 fixes two moderate security issues:</p>
<ul>
<li>Pool managers now properly control redirects when <code>retries</code> is passed — CVE-2025-50181 reported by <a href="https://github.com/sandumjacob"><code>@​sandumjacob</code></a> (5.3 Medium, GHSA-pq67-6m6q-mj2v)</li>
<li>Redirects are now controlled by urllib3 in the Node.js runtime — CVE-2025-50182 (5.3 Medium, GHSA-48p4-8xcf-vxj5)</li>
</ul>
<h1>Features</h1>
<ul>
<li>Added support for the <code>compression.zstd</code> module that is new in Python 3.14. See <a href="https://peps.python.org/pep-0784/">PEP 784</a> for more information. (<a href="https://redirect.github.com/urllib3/urllib3/issues/3610">#3610</a>)</li>
<li>Added support for version 0.5 of <code>hatch-vcs</code> (<a href="https://redirect.github.com/urllib3/urllib3/issues/3612">#3612</a>)</li>
</ul>
<h1>Bugfixes</h1>
<ul>
<li>Raised exception for <code>HTTPResponse.shutdown</code> on a connection already released to the pool. (<a href="https://redirect.github.com/urllib3/urllib3/issues/3581">#3581</a>)</li>
<li>Fixed incorrect <code>CONNECT</code> statement when using an IPv6 proxy with <code>connection_from_host</code>. Previously would not be wrapped in <code>[]</code>. (<a href="https://redirect.github.com/urllib3/urllib3/issues/3615">#3615</a>)</li>
</ul>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/urllib3/urllib3/blob/main/CHANGES.rst">urllib3's changelog</a>.</em></p>
<blockquote>
<h1>2.5.0 (2025-06-18)</h1>
<h2>Features</h2>
<ul>
<li>Added support for the <code>compression.zstd</code> module that is new in Python 3.14.
See <code>PEP 784 &lt;https://peps.python.org/pep-0784/&gt;</code>_ for more information. (<code>[#3610](https://github.com/urllib3/urllib3/issues/3610) &lt;https://github.com/urllib3/urllib3/issues/3610&gt;</code>__)</li>
<li>Added support for version 0.5 of <code>hatch-vcs</code> (<code>[#3612](https://github.com/urllib3/urllib3/issues/3612) &lt;https://github.com/urllib3/urllib3/issues/3612&gt;</code>__)</li>
</ul>
<h2>Bugfixes</h2>
<ul>
<li>Fixed a security issue where restricting the maximum number of followed
redirects at the <code>urllib3.PoolManager</code> level via the <code>retries</code> parameter
did not work.</li>
<li>Made the Node.js runtime respect redirect parameters such as <code>retries</code>
and <code>redirects</code>.</li>
<li>Raised exception for <code>HTTPResponse.shutdown</code> on a connection already released to the pool. (<code>[#3581](https://github.com/urllib3/urllib3/issues/3581) &lt;https://github.com/urllib3/urllib3/issues/3581&gt;</code>__)</li>
<li>Fixed incorrect <code>CONNECT</code> statement when using an IPv6 proxy with <code>connection_from_host</code>. Previously would not be wrapped in <code>[]</code>. (<code>[#3615](https://github.com/urllib3/urllib3/issues/3615) &lt;https://github.com/urllib3/urllib3/issues/3615&gt;</code>__)</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/urllib3/urllib3/commit/aaab4eccc10c965897540b21e15f11859d0b62e7"><code>aaab4ec</code></a> Release 2.5.0</li>
<li><a href="https://github.com/urllib3/urllib3/commit/7eb4a2aafe49a279c29b6d1f0ed0f42e9736194f"><code>7eb4a2a</code></a> Merge commit from fork</li>
<li><a href="https://github.com/urllib3/urllib3/commit/f05b1329126d5be6de501f9d1e3e36738bc08857"><code>f05b132</code></a> Merge commit from fork</li>
<li><a href="https://github.com/urllib3/urllib3/commit/d03fe327a71d09728512217149f269763671f296"><code>d03fe32</code></a> Fix HTTP tunneling with IPv6 in older Python versions</li>
<li><a href="https://github.com/urllib3/urllib3/commit/11661e9bb4278e43d081f47a516e287a928c2206"><code>11661e9</code></a> Bump github/codeql-action from 3.28.0 to 3.29.0 (<a href="https://redirect.github.com/urllib3/urllib3/issues/3624">#3624</a>)</li>
<li><a href="https://github.com/urllib3/urllib3/commit/6a0ecc6b16fe30f721021b44a81d19615098c71e"><code>6a0ecc6</code></a> Update v2 migration guide to 2.4.0 (<a href="https://redirect.github.com/urllib3/urllib3/issues/3621">#3621</a>)</li>
<li><a href="https://github.com/urllib3/urllib3/commit/8e32e60d9024c05bc6f7adda08bdf6c539d0b0d4"><code>8e32e60</code></a> Raise exception for shutdown on a connection already released to the pool (<a href="https://redirect.github.com/urllib3/urllib3/issues/3">#3</a>...</li>
<li><a href="https://github.com/urllib3/urllib3/commit/9996e0fbf90b77083ad3c73737a6c6395703faa9"><code>9996e0f</code></a> Fix emscripten CI for Chrome 137+ (<a href="https://redirect.github.com/urllib3/urllib3/issues/3599">#3599</a>)</li>
<li><a href="https://github.com/urllib3/urllib3/commit/4fd1a99a59725faf0efc946ce3b6bc9a194420af"><code>4fd1a99</code></a> Bump RECENT_DATE (<a href="https://redirect.github.com/urllib3/urllib3/issues/3617">#3617</a>)</li>
<li><a href="https://github.com/urllib3/urllib3/commit/c4b5917e911a90c8bf279448df8952a682294135"><code>c4b5917</code></a> Add support for the new <code>compression.zstd</code> module in Python 3.14 (<a href="https://redirect.github.com/urllib3/urllib3/issues/3611">#3611</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/urllib3/urllib3/compare/2.4.0...2.5.0">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=urllib3&package-manager=pip&previous-version=2.4.0&new-version=2.5.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>Dependabot commands and options</summary>
<br />

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating it. You can achieve the same result by closing it manually
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/digitaldemocracy2030/polimoney/network/alerts).

</details>

**コメント:** なし

---

### [refs #102 準備中のComing Soon...パネルを追加](https://github.com/digitaldemocracy2030/polimoney/pull/139)

**作成者:** Osei37  
**作成日:** 2025-06-21T16:16:00Z  
**変更:** +61 -15 (3ファイル)  
**マージ日:** 2025-06-22T10:06:43Z  
**内容:**

# 変更の概要

- Comming Soon...パネルを追加
  - リンク先はないためパネルをクリックしても遷移しない（既存のパネルは変わらず遷移できる）
  - 画像は `demo-example.png` をとりあえず設定
  - パネルの数は任意の数に変更できる
    - ハードコーディングしたのでDBから取得するようにするなどの検討の余地あり
- リファクタリング
  - 変数名の修正
  - 型付け
  - 静的な属性値を文字列に変更

# スクリーンショット

| 変更前 | 変更後 |
| ------- | ------- |
| <img width="960" alt="image" src="https://github.com/user-attachments/assets/0515bd64-dda4-4364-a141-7f4d35cc748a" /> | <img width="959" alt="image" src="https://github.com/user-attachments/assets/f28bf2ad-4852-4319-8e36-37cfd1313985" /> |

- 任意の数にすることができる

| 0 | 1 | 3 | 
| ------- | ------- | ------- |
|  <img width="957" alt="image" src="https://github.com/user-attachments/assets/02fbf95a-e6fb-4293-adf8-96b0ac8e748a" /> | <img width="959" alt="image" src="https://github.com/user-attachments/assets/5416d62c-b5a1-42f9-b856-c6917dfef73f" /> | <img width="480" alt="image" src="https://github.com/user-attachments/assets/e714dd69-1f4f-4a0e-94ad-819fe976f194" /> |

# 変更の背景
#102 

# 関連Issue
#102 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - 「近日公開」プロファイルのプレースホルダーが一覧に動的に表示されるようになりました。

- **改善**
  - プロファイルカードのレイアウトが中央揃えになり、バッジの表示が条件付きでより分かりやすくなりました。
  - プロファイル一覧のリンク先が条件によって適切に制御されるようになりました。

- **スタイル**
  - JSXのプロパティ表記が統一され、コードの一貫性が向上しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [翌年への繰越額が出力されない不具合の修正](https://github.com/digitaldemocracy2030/polimoney/pull/138)

**作成者:** dotneet  
**作成日:** 2025-06-18T07:44:48Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-06-18T07:53:20Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
 - 合計・小計とみなされて「翌年への繰越額」が出力されないケースがあるので例外として認めるように変更

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

 - 「翌年への繰越額」は必須項目なので scripts/create-json-for-web.sh が通らなくなってしまうため

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - 「翌年への繰越額」が取引一覧に表示されるようになりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [データフォーマットの統一](https://github.com/digitaldemocracy2030/polimoney/pull/137)

**作成者:** dotneet  
**作成日:** 2025-06-18T06:23:42Z  
**変更:** +683 -911 (18ファイル)  
**マージ日:** 2025-06-18T09:15:58Z  
**内容:**

# 変更の概要

 - Closes #135
 - すべてのデータフォーマットを Transaction に合わせた
 - converter.ts の出力形式を新形式に対応
 - OldTransaction, OldBoardTransactions の廃止

data/demo-*.ts のexport型を新たに導入した下記の型に統一しました。converter.ts もこの形式で出力します。

```typescript
export type AccountingReports = {
  id: string;
  latestReportId: string;
  profile: Profile;
  datas: {
    report: Report;
    flows: Flow[];
    transactions: Transaction[];
  }[];
};
```

動作確認

 - 各ページの数値が現在の本番と同じになっていることを確認しました
 - scripts/create-json-for-web.sh の結果を表示できることを確認しました

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

複数のデータフォーマットとUIがありDB対応の前に整理する必要があった

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

 - #135

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - 取引データの表示項目に「目的」や「日付」の表示／非表示を切り替える機能が追加されました。

- **リファクタリング**
  - 取引データの構造が統一され、「収入」「支出」の区別やカテゴリ情報が明確になりました。
  - データ構造がフラットな形式から、複数レポートをまとめて扱う形式に変更されました。
  - 旧取引表示コンポーネントが新しいコンポーネントに置き換えられ、表示制御が細かくなりました。

- **ドキュメント**
  - データ型や構造に関する説明が最新の仕様に更新されました。

- **バグ修正**
  - 取引の方向（収入・支出）の判定が日本語から英語表記に統一されました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Bump protobuf from 4.25.6 to 4.25.8 in /tools](https://github.com/digitaldemocracy2030/polimoney/pull/136)

**作成者:** dependabot[bot]  
**作成日:** 2025-06-18T05:28:26Z  
**変更:** +12 -12 (1ファイル)  
**マージ日:** 2025-06-18T05:30:38Z  
**内容:**

Bumps [protobuf](https://github.com/protocolbuffers/protobuf) from 4.25.6 to 4.25.8.
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/protocolbuffers/protobuf/commit/a4cbdd3ed0042e8f9b9c30e8b0634096d9532809"><code>a4cbdd3</code></a> Updating version.json and repo version numbers to: 25.8</li>
<li><a href="https://github.com/protocolbuffers/protobuf/commit/29445be43d3235115f1f60c874a04c2147ea0488"><code>29445be</code></a> Merge pull request <a href="https://redirect.github.com/protocolbuffers/protobuf/issues/21880">#21880</a> from shaod2/py-25</li>
<li><a href="https://github.com/protocolbuffers/protobuf/commit/cc13b69985f90f6f142b7c3f9cb6bdebee9b4579"><code>cc13b69</code></a> Remove debugging code and add EOLs</li>
<li><a href="https://github.com/protocolbuffers/protobuf/commit/d31100c9195819edb0a12f44705dfc2da111ea9b"><code>d31100c</code></a> Manually backport recursion limit enforcement to 25.x</li>
<li><a href="https://github.com/protocolbuffers/protobuf/commit/88a3b9033014bfd4185d934bd199191667a67d2a"><code>88a3b90</code></a> Change pre-22 poison pill to only log once per affected message type. (<a href="https://redirect.github.com/protocolbuffers/protobuf/issues/21754">#21754</a>)</li>
<li><a href="https://github.com/protocolbuffers/protobuf/commit/320eafa0b7ab3c649f75bcbe851e0d3acf868cf3"><code>320eafa</code></a> Weaken vulnerable gencode poison pills to warning by default.</li>
<li><a href="https://github.com/protocolbuffers/protobuf/commit/f584fe36d4aa4af5dcc71e592c855b59e0ecee2c"><code>f584fe3</code></a> Merge branch 'protocolbuffers:25.x' into 25.x</li>
<li><a href="https://github.com/protocolbuffers/protobuf/commit/c7100368a25a849691dec7695078a113f6a4ef9f"><code>c710036</code></a> Update test_upb.yml to use ubuntu-22</li>
<li><a href="https://github.com/protocolbuffers/protobuf/commit/97217584375d1a29af91aeb607cc67327a3e05da"><code>9721758</code></a> Fix missing trailing newline.</li>
<li><a href="https://github.com/protocolbuffers/protobuf/commit/cca7b289bcda8baab9f59101d5c737790c5cc610"><code>cca7b28</code></a> Update test_upb.yml to use ubuntu-22</li>
<li>Additional commits viewable in <a href="https://github.com/protocolbuffers/protobuf/compare/v4.25.6...v4.25.8">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=protobuf&package-manager=pip&previous-version=4.25.6&new-version=4.25.8)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>Dependabot commands and options</summary>
<br />

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating it. You can achieve the same result by closing it manually
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/digitaldemocracy2030/polimoney/network/alerts).

</details>

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

