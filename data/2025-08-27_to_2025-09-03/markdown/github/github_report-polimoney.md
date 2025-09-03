# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-08-27T12:15:28.385045+09:00 から 2025-09-03T12:15:28.385045+09:00 まで

## Issues

### 過去7日間に完了されたissue (1件)

### [Chore: nextjs-check.ymlを関連コードを修正された場合のみ実行されるように変更](https://github.com/digitaldemocracy2030/polimoney/issues/187)

**作成者:** YukihiroArakawa  
**作成日:** 2025-08-30T08:54:04Z  
**内容:**

## 解決・改善したいこと

現在、リポジトリ上でどのような変更がプッシュされたときでも、nextjs-check.ymlが実行されます。

そのため、関連するjsのコードが変更された場合のみ当ワークフローを実行されるようにして、github actionsを節約できるようにしたいです。


<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

以下のようにトリガーとなる条件にパスを追加することで関連ファイルの修正時のみワークフローが実行されるようにしたいです。

```yml
 name: Check Next.js

 on:
   pull_request:
     types: [opened, synchronize, reopened]
+    paths:
+      - 'app/**'
+      - 'components/**'
+      - 'data/**'
+      - 'models/**'
+      - 'public/**'
+      - 'next.config.ts'
+      - 'tsconfig.json'
+      - 'package.json'
+      - 'package-lock.json'
```


**コメント:** なし

---

### 過去7日間に作成されたissue (1件)

### [選挙運動費用収支報告書に対応](https://github.com/digitaldemocracy2030/polimoney/issues/191)

**作成者:** shumizu418128  
**作成日:** 2025-09-02T05:59:44Z  
**内容:**

現時点では、和歌山県議員・[岩永さんの選挙運動費用収支報告書](https://drive.google.com/drive/folders/13bMJ4q2mOg_CtAg1YUSe9RrK1U04cn3q)に対応することを目指す。

政治資金収支報告書とは別の書類であり、ルールが変わってくるため、データ構造形式など検討が必要。
参考Slack：https://dd2030.slack.com/archives/C08FL5L6GSH/p1756387625940919

※Slackにまだ参加していない方は私をメンションしてください
招待URLを差し上げます

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (5件)

### [家屋費](https://github.com/digitaldemocracy2030/polimoney/pull/193)

**作成者:** shumizu418128  
**作成日:** 2025-09-02T06:40:03Z  
**変更:** +210 -11 (4ファイル)  
**マージ日:** 2025-09-02T06:40:08Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
#191 つづき
家屋費の収集
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

- 新機能
  - 和歌山の家屋関連支出データの取り込みに対応（選挙事務所・集会場の明細と合計）。
  - 解析結果をJSONファイルとして保存。income_data.json、personnel_data.json、building_data.jsonを出力（UTF-8・インデント付き）。

- リファクタリング
  - 収入・人件費の結果を標準出力ではなく構造化データとして扱い、ファイル出力に統一。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [支出の部 1 人件費までできた](https://github.com/digitaldemocracy2030/polimoney/pull/192)

**作成者:** shumizu418128  
**作成日:** 2025-09-02T06:07:18Z  
**変更:** +93 -2 (3ファイル)  
**マージ日:** 2025-09-02T06:36:58Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
#190 つづき
人件費の分析までできた

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->
#191 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- 新機能
  - 人件費データの解析・出力に対応。収支分析フローに人件費シートを追加し、個別明細と合計をJSONで表示します。既存の収入解析は従来通り動作します。
- ドキュメント
  - 収入集計の列参照に関するコメントを更新（列Bを明記）。機能変更はありません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [選挙活動費用収支報告書の分析コード](https://github.com/digitaldemocracy2030/polimoney/pull/190)

**作成者:** shumizu418128  
**作成日:** 2025-09-02T05:35:12Z  
**変更:** +201 -0 (3ファイル)  
**マージ日:** 2025-09-02T06:01:02Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
まだ全然できてないですが収入の部だけデータ構造化するコードを書きました

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

- 新機能
  - Excelファイルの「収入」シートを解析する日本語対応CLIツールを追加
  - 個別収入の一覧をJSONで出力（日付・金額・区分・備考）
  - 収入合計（寄附・その他・計・総計）をJSONで出力
  - 公費負担相当額の総額と内訳を抽出しJSONで出力
  - 入力ファイルの基本的な検証と、開始・完了・エラーのログ出力（日本語）を実装

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [chore: 関連するjs/tsのコードが変更された場合のみnextjs-checkが実行されるようにpathを追加](https://github.com/digitaldemocracy2030/polimoney/pull/189)

**作成者:** YukihiroArakawa  
**作成日:** 2025-08-30T09:04:38Z  
**変更:** +10 -1 (1ファイル)  
**マージ日:** 2025-08-30T09:05:12Z  
**内容:**

# 変更の概要
関連するjsのコードが変更された場合のみ当ワークフローを実行されるようにして、github actionsを節約できるようにしました。


# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景

現在、リポジトリ上でどのような変更がプッシュされたときでも、nextjs-check.ymlが実行されるため。

# 関連Issue

https://github.com/digitaldemocracy2030/polimoney/issues/187

<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- チョア
  - PRワークフローが特定の変更が含まれる場合のみ実行されるよう調整し、不要な実行を抑制。レビュー/CIの待ち時間を軽減。
- スタイル
  - ワークフロー定義の余分な空行を整理し、可読性を向上。

ユーザー向けの機能変更や修正はありません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Bump next from 15.2.4 to 15.4.7](https://github.com/digitaldemocracy2030/polimoney/pull/188)

**作成者:** dependabot[bot]  
**作成日:** 2025-08-30T09:04:09Z  
**変更:** +196 -163 (2ファイル)  
**マージ日:** 2025-08-30T09:04:46Z  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 15.2.4 to 15.4.7.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v15.4.7</h2>
<blockquote>
<p>[!NOTE]<br />
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>fix router handling when setting a location response header <a href="https://redirect.github.com/vercel/next.js/issues/82588">#82588</a></li>
</ul>
<h3>Credits</h3>
<p>Huge thanks to <a href="https://github.com/ztanner"><code>@​ztanner</code></a> for helping!</p>
<h2>v15.4.6</h2>
<blockquote>
<p>[!NOTE]<br />
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>fix: <code>_error</code> page's <code>req.url</code> can be overwritten to dynamic param on minimal mode (<a href="https://redirect.github.com/vercel/next.js/issues/82347">#82347</a>)</li>
<li>fix: add <code>?dpl</code> to fonts in <code>/_next/static/media</code> (<a href="https://redirect.github.com/vercel/next.js/issues/82384">#82384</a>)</li>
</ul>
<h3>Credits</h3>
<p>Huge thanks to <a href="https://github.com/devjiwonchoi"><code>@​devjiwonchoi</code></a>, <a href="https://github.com/ijjk"><code>@​ijjk</code></a>, and <a href="https://github.com/styfle"><code>@​styfle</code></a> for helping!</p>
<h2>v15.4.5</h2>
<blockquote>
<p>[!NOTE]<br />
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>Fix API stripping JSON incorrectly (<a href="https://redirect.github.com/vercel/next.js/issues/82062">#82062</a>)</li>
<li>Fix i18n fallback: false collision (<a href="https://redirect.github.com/vercel/next.js/issues/82158">#82158</a>)</li>
<li>Revert &quot;Fix tracing of server actions imported by client components (<a href="https://redirect.github.com/vercel/next.js/issues/82167">#82167</a>)</li>
<li>Ensure setAssetPrefix updates config instance (<a href="https://redirect.github.com/vercel/next.js/issues/82165">#82165</a>)</li>
<li>Turbopack: update mimalloc (<a href="https://redirect.github.com/vercel/next.js/issues/82166">#82166</a>)</li>
<li>fix(next/image): fix image-optimizer.ts headers (<a href="https://redirect.github.com/vercel/next.js/issues/82175">#82175</a>)</li>
<li>fix(next/image): improve and simplify detect-content-type (<a href="https://redirect.github.com/vercel/next.js/issues/82174">#82174</a>)</li>
</ul>
<h3>Credits</h3>
<p>Huge thanks to <a href="https://github.com/ijjk"><code>@​ijjk</code></a>, <a href="https://github.com/sokra"><code>@​sokra</code></a>, and <a href="https://github.com/styfle"><code>@​styfle</code></a> for helping!</p>
<h2>v15.4.4</h2>
<blockquote>
<p>[!NOTE]<br />
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>Fix dynamicParams false layout case in dev (<a href="https://redirect.github.com/vercel/next.js/issues/82026">#82026</a>)</li>
<li>Turbopack: fix scope hoisting variable renaming bug (<a href="https://redirect.github.com/vercel/next.js/issues/81640">#81640</a>)</li>
<li>Upgrade to swc v33 (<a href="https://redirect.github.com/vercel/next.js/issues/81750">#81750</a>)</li>
<li>Revert &quot;[metadata] use https protocol for schema urls&quot; (<a href="https://redirect.github.com/vercel/next.js/issues/81934">#81934</a>)</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/f30d815859e932e09222e93bb6e8a376b918d874"><code>f30d815</code></a> v15.4.7</li>
<li><a href="https://github.com/vercel/next.js/commit/1a026e338d2b8c977c8949a134168952338d6d01"><code>1a026e3</code></a> fix router handling when setting a location response header (<a href="https://redirect.github.com/vercel/next.js/issues/82588">#82588</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/be4aafd4b744fbf6500b311b74c84243f70a3059"><code>be4aafd</code></a> v15.4.6</li>
<li><a href="https://github.com/vercel/next.js/commit/91e5b6b84f56c096dc2bb647eb384388e06489fd"><code>91e5b6b</code></a> Backport &quot;fix: add <code>?dpl</code> to fonts in <code>/_next/static/media</code> (<a href="https://redirect.github.com/vercel/next.js/issues/82384">#82384</a>)&quot; (<a href="https://redirect.github.com/vercel/next.js/issues/82421">#82421</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/f1629d939597cc46ccbe44fe66bda91eac31e219"><code>f1629d9</code></a> Backport &quot;[Pages] fix: <code>_error</code> page's <code>req.url</code> can be overwritten t… (<a href="https://redirect.github.com/vercel/next.js/issues/82377">#82377</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/b9aab5dbe926c256d439bfecb226693dcd1a1be4"><code>b9aab5d</code></a> v15.4.5</li>
<li><a href="https://github.com/vercel/next.js/commit/a8c93c49dd2d42a2ced8a17bc53b3fea11d25c96"><code>a8c93c4</code></a> Disable test new tests jobs</li>
<li><a href="https://github.com/vercel/next.js/commit/ed2a6c754831406f8cd724eb52a562bb124c1504"><code>ed2a6c7</code></a> [backport]: fix(next/image): improve and simplify detect-content-type (<a href="https://redirect.github.com/vercel/next.js/issues/82118">#82118</a>...</li>
<li><a href="https://github.com/vercel/next.js/commit/f00fcc9011e7d0ef027021fc8424f51b8ac97880"><code>f00fcc9</code></a> [backport]: fix(next/image): fix image-optimizer.ts headers (<a href="https://redirect.github.com/vercel/next.js/issues/82114">#82114</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/82175">#82175</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/55a7568e9d12459f8c5f5ae120fe2e228af284bb"><code>55a7568</code></a> Backport: Turbopack: update mimalloc (<a href="https://redirect.github.com/vercel/next.js/issues/81993">#81993</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/82166">#82166</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/vercel/next.js/compare/v15.2.4...v15.4.7">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=15.2.4&new-version=15.4.7)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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

### 過去7日間に作成されたPR (1件)

### [Flow/Transaction の型定義検証](https://github.com/digitaldemocracy2030/polimoney/pull/186)

**作成者:** grassfieldk  
**作成日:** 2025-08-28T11:33:49Z  
**変更:** +785 -318 (4ファイル)  
**内容:**

> [!NOTE]
>  ※ #166 に関連したコード共有用プルリクエストです（マージ・レビュー不要）
> 2025/08/28 の定例での話に基づき作成しました

## 変更の概要

Flow/Transaction（議員ページ上に表示されている各種データ）型定義を強化し、
データ定義の段階で id や収支の整合性が担保されるようにするための検証ブランチ

## 変更の背景

議員データの取得元の都合で整合性が担保されない状態にあるため、
最低限整えられたデータが作成されるようにしておくことで今後の機能拡張がしやすいようにしたい
完全に整理されたデータ生成はまだ難しいと思うので、あくまで今後の拡張の土台として試験的に型定義を導入

今回追加した型定義をデータ生成時に AI に読み込ませることで、より統一された形でのデータ生成ができることも狙い

## 関連Issue
[#166 理解の助けになるよう、収支項目の解説を書き込む](https://github.com/digitaldemocracy2030/polimoney/issues/166)

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- 新機能
  - サンプルの入出金カテゴリと取引データを追加し、デモ利用が容易になりました。
  - フロー/取引/レポート/プロフィールのデータ表現を拡充し、IDと分類の整合性が向上しました。

- ドキュメント
  - ID命名規則を新設し、関連セクションから参照するよう整理しました。
  - デモページの説明を箇条書き中心に再構成し、読みやすさを改善しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

