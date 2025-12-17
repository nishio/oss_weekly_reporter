# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-12-10T12:34:25.872696+09:00 から 2025-12-17T12:34:25.872696+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (1件)

### [Bump next from 15.2.3 to 15.5.7 in /client](https://github.com/digitaldemocracy2030/kouchou-ai/pull/732)

**作成者:** dependabot[bot]  
**作成日:** 2025-12-03T21:01:36Z  
**変更:** +648 -626 (2ファイル)  
**マージ日:** 2025-12-10T11:16:19Z  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 15.2.3 to 15.5.7.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v15.5.7</h2>
<p>Please see <a href="https://nextjs.org/blog/CVE-2025-66478">CVE-2025-66478</a> for additional details about this release.</p>
<h2>v15.5.6</h2>
<blockquote>
<p>[!NOTE]<br />
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>Turbopack: don't define process.cwd() in node_modules <a href="https://redirect.github.com/vercel/next.js/issues/83452">#83452</a></li>
</ul>
<h3>Credits</h3>
<p>Huge thanks to <a href="https://github.com/mischnic"><code>@​mischnic</code></a> for helping!</p>
<h2>v15.5.5</h2>
<blockquote>
<p>[!NOTE]<br />
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>Split code-frame into separate compiled package (<a href="https://redirect.github.com/vercel/next.js/issues/84238">#84238</a>)</li>
<li>Add deprecation warning to Runtime config (<a href="https://redirect.github.com/vercel/next.js/issues/84650">#84650</a>)</li>
<li>fix: unstable_cache should perform blocking revalidation during ISR revalidation (<a href="https://redirect.github.com/vercel/next.js/issues/84716">#84716</a>)</li>
<li>feat: <code>experimental.middlewareClientMaxBodySize</code> body cloning limit  (<a href="https://redirect.github.com/vercel/next.js/issues/84722">#84722</a>)</li>
<li>fix: missing next/link types with typedRoutes (<a href="https://redirect.github.com/vercel/next.js/issues/84779">#84779</a>)</li>
</ul>
<h3>Misc Changes</h3>
<ul>
<li>docs: early October improvements and fixes (<a href="https://redirect.github.com/vercel/next.js/issues/84334">#84334</a>)</li>
</ul>
<h3>Credits</h3>
<p>Huge thanks to <a href="https://github.com/devjiwonchoi"><code>@​devjiwonchoi</code></a>, <a href="https://github.com/ztanner"><code>@​ztanner</code></a>, and <a href="https://github.com/icyJoseph"><code>@​icyJoseph</code></a> for helping!</p>
<h2>v15.4.8</h2>
<p>Please see <a href="https://nextjs.org/blog/CVE-2025-66478">CVE-2025-66478</a> for additional details about this release.</p>
<h2>v15.3.6</h2>
<p>Please see <a href="https://nextjs.org/blog/CVE-2025-66478">CVE-2025-66478</a> for additional details about this release.</p>
<h2>v15.2.6</h2>
<p>Please see <a href="https://nextjs.org/blog/CVE-2025-66478">CVE-2025-66478</a> for additional details about this release.</p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/3eaf68b09b2b6b8c0c8e080a9713e131a78dc529"><code>3eaf68b</code></a> v15.5.7</li>
<li><a href="https://github.com/vercel/next.js/commit/8367ce592ad0190ec941dac1ce6d0b5a44606593"><code>8367ce5</code></a> update version script</li>
<li><a href="https://github.com/vercel/next.js/commit/9115040008baf255499136933a50084b76f4bfd8"><code>9115040</code></a> Update React Version for Next.js 15.5.7 (<a href="https://redirect.github.com/vercel/next.js/issues/10">#10</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/96f699902a5c57293e312591f843080a4d68ee1b"><code>96f6999</code></a> update tag</li>
<li><a href="https://github.com/vercel/next.js/commit/55ef0e3ebc1d43e1a4a191341dc2a415e12124d4"><code>55ef0e3</code></a> v15.5.6</li>
<li><a href="https://github.com/vercel/next.js/commit/92bbbb1beca8738c783ea36ee5dd84d89cd638be"><code>92bbbb1</code></a> Backport: don't define <code>process.cwd()</code> in node_modules (<a href="https://redirect.github.com/vercel/next.js/issues/84957">#84957</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/f895b727626ad921d5068bcfada284f68c998bfa"><code>f895b72</code></a> Fix url-imports test on 15-5 (<a href="https://redirect.github.com/vercel/next.js/issues/84966">#84966</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/81f530db2652a96d4b88fabaf4dfaf30c2269695"><code>81f530d</code></a> v15.5.5</li>
<li><a href="https://github.com/vercel/next.js/commit/9abbc0e9eba67d635d4da5293273de123263101d"><code>9abbc0e</code></a> [backport] fix: missing <code>next/link</code> types with <code>typedRoutes</code> (<a href="https://redirect.github.com/vercel/next.js/issues/82814">#82814</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/84779">#84779</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/121e1b566f8bf632dd09bf06fbbdb5ff5a21a51c"><code>121e1b5</code></a> [backport] docs: early October improvements and fixes (<a href="https://redirect.github.com/vercel/next.js/issues/84334">#84334</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/vercel/next.js/compare/v15.2.3...v15.5.7">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=15.2.3&new-version=15.5.7)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/digitaldemocracy2030/kouchou-ai/network/alerts).

</details>

**コメント:** なし

---

### 過去7日間に作成されたPR (3件)

### [Bump next from 15.5.7 to 15.5.9 in /client](https://github.com/digitaldemocracy2030/kouchou-ai/pull/738)

**作成者:** dependabot[bot]  
**作成日:** 2025-12-12T02:09:50Z  
**変更:** +9 -9 (2ファイル)  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 15.5.7 to 15.5.9.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v15.5.9</h2>
<p>Please see the <a href="https://nextjs.org/blog/security-update-2025-12-11">Next.js Security Update</a> for information about this security patch.</p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/c5de33e93ccccaf3bee60cf50603e2152f9886e1"><code>c5de33e</code></a> v15.5.9</li>
<li><a href="https://github.com/vercel/next.js/commit/dd233994aeb24e906cdb9aedca5447cdef401792"><code>dd23399</code></a> Backport <a href="https://redirect.github.com/facebook/react/issues/35351">facebook/react#35351</a> for 15.5.8 (<a href="https://redirect.github.com/vercel/next.js/issues/87086">#87086</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/7526cd6f24300726964eaba78927fe2a9c3fed5e"><code>7526cd6</code></a> v15.5.8</li>
<li><a href="https://github.com/vercel/next.js/commit/1e9ec4133af3657964833bfcc9abb0ee73fb19f0"><code>1e9ec41</code></a> Update React Version (<a href="https://redirect.github.com/vercel/next.js/issues/41">#41</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/16141e5df9ce51136ba42988b574981f89d01081"><code>16141e5</code></a> Update React Version (<a href="https://redirect.github.com/vercel/next.js/issues/30">#30</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/e01e589e181d66d48c57698238b8b7f59218dfef"><code>e01e589</code></a> Backport Next.js changes to v15.5.8 (<a href="https://redirect.github.com/vercel/next.js/issues/23">#23</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/b2706db1e62c261ddfddaa040b2b26d93a091eca"><code>b2706db</code></a> lock binaries</li>
<li>See full diff in <a href="https://github.com/vercel/next.js/compare/v15.5.7...v15.5.9">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=15.5.7&new-version=15.5.9)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/digitaldemocracy2030/kouchou-ai/network/alerts).

</details>

**コメント:** なし

---

### [Bump next from 15.2.3 to 15.4.9 in /utils/dummy-server](https://github.com/digitaldemocracy2030/kouchou-ai/pull/737)

**作成者:** dependabot[bot]  
**作成日:** 2025-12-12T01:07:44Z  
**変更:** +254 -234 (2ファイル)  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 15.2.3 to 15.4.9.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v15.4.8</h2>
<p>Please see <a href="https://nextjs.org/blog/CVE-2025-66478">CVE-2025-66478</a> for additional details about this release.</p>
<h2>v15.3.8</h2>
<p>Please see the <a href="https://nextjs.org/blog/security-update-2025-12-11">Next.js Security Update</a> for information about this security patch.</p>
<h2>v15.3.6</h2>
<p>Please see <a href="https://nextjs.org/blog/CVE-2025-66478">CVE-2025-66478</a> for additional details about this release.</p>
<h2>v15.2.8</h2>
<p>Please see the <a href="https://nextjs.org/blog/security-update-2025-12-11">Next.js Security Update</a> for information about this security patch.</p>
<h2>v15.2.6</h2>
<p>Please see <a href="https://nextjs.org/blog/CVE-2025-66478">CVE-2025-66478</a> for additional details about this release.</p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/d1449e513f1cb40739b4cd97fac5b6eaa3ea445c"><code>d1449e5</code></a> v15.4.9</li>
<li><a href="https://github.com/vercel/next.js/commit/596f51338bf77e03a363b31963b2caa133b06ef9"><code>596f513</code></a> Update React Version (<a href="https://redirect.github.com/vercel/next.js/issues/42">#42</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/2ff781e00bd7931507ed9302dff987c31a6d712e"><code>2ff781e</code></a> Update React Version (<a href="https://redirect.github.com/vercel/next.js/issues/31">#31</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/d0edaaceacd453535af61d62a0cad26b4f92d7b3"><code>d0edaac</code></a> Backport Next.js changes to v15.4.9 (<a href="https://redirect.github.com/vercel/next.js/issues/24">#24</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/bd845468a7f8f8fac639556f24abfab800662709"><code>bd84546</code></a> lock binaries</li>
<li><a href="https://github.com/vercel/next.js/commit/49668475daba15ef8cea1d8e469dc0f9a765b635"><code>4966847</code></a> v15.4.8</li>
<li><a href="https://github.com/vercel/next.js/commit/bf8d31c89caf0fc18efe91fb2dc3463fc03795c0"><code>bf8d31c</code></a> update version script</li>
<li><a href="https://github.com/vercel/next.js/commit/bed530f7294241b9f92aa2ee5abc50a92e97b7fe"><code>bed530f</code></a> Update React Version for Next.js 15.4.8 (<a href="https://redirect.github.com/vercel/next.js/issues/9">#9</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/4309d936b36e5fbdfdc9ee743dd9161c26e7220f"><code>4309d93</code></a> update tag</li>
<li><a href="https://github.com/vercel/next.js/commit/17e6873ee8320bd6bfa8f35c3d7769c0e08e1ebf"><code>17e6873</code></a> [backport]: <code>experimental.middlewareClientMaxBodySize</code> (<a href="https://redirect.github.com/vercel/next.js/issues/84722">#84722</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/vercel/next.js/compare/v15.2.3...v15.4.9">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=15.2.3&new-version=15.4.9)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/digitaldemocracy2030/kouchou-ai/network/alerts).

</details>

**コメント:** なし

---

### [docs: PR本文はAI自動生成をそのまま貼らない旨を追記](https://github.com/digitaldemocracy2030/kouchou-ai/pull/736)

**作成者:** shingo-ohki  
**作成日:** 2025-12-10T12:12:51Z  
**変更:** +5 -1 (2ファイル)  
**内容:**

# 変更の概要
- タイトル通り

# スクリーンショット
- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください

# 関連Issue
#734 #735 

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

* **ドキュメント**
  * プルリクエスト作成時のテンプレートとガイドラインを更新しました。
  * PR本文は実際の変更に合わせて自身の言葉で記載すること、AIツール利用時は出力を必ず確認・編集して貼付することを明記しました。
  * 動作確認セクションの記述にマークアップ差分が入りましたが、実質的な手順や内容に変更はありません。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

