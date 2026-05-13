# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2026-05-06T13:24:59.403210+09:00 から 2026-05-13T13:24:59.403210+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (5件)

### [マージのため変更を取り消し](https://github.com/digitaldemocracy2030/polimoney/pull/252)

**作成者:** grassfieldk  
**作成日:** 2026-05-10T14:14:34Z  
**変更:** +22 -78 (4ファイル)  
**マージ日:** 2026-05-10T14:14:54Z  
**内容:**

## 変更の概要

一時的な変更を取り消し

## CLAへの同意

本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"[ ]" を "[x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **バグ修正**
  * 認証ゲーティングを調整し、未認証ユーザーのアクセスを適切に制限しました。

* **リファクタリング**
  * 候補者プロフィール画像の表示を削除しました。
  * ページヘッダーのレイアウトを簡潔に整理し、タイトル、日付、名前のフィールドを表示するよう変更しました。
  * リンクナビゲーションのロジックを改善しました。

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/polimoney/pull/252)

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [ページ構成の見直し](https://github.com/digitaldemocracy2030/polimoney/pull/251)

**作成者:** grassfieldk  
**作成日:** 2026-05-09T17:02:22Z  
**変更:** +1363 -1278 (29ファイル)  
**マージ日:** 2026-05-10T14:15:47Z  
**内容:**

## 変更の概要

ページ構成を大幅に変更

```
/                                                - トップ（政治家・政治団体の上位数件）
/politicians                                     - 政治家一覧
/politicians/{politician_id}                     - 政治家詳細（政治・選挙収支一覧）
/politicians/{politician_id}/political/{data_id} - 政治資金収支報告
/politicians/{politician_id}/election/{data_id}  - 選挙運動収支報告
/organizations                                   - 政治団体一覧
/organizations/{org_id}                          - 政治団体詳細（政治収支一覧・代表者）
/organizations/{org_id}/political/{data_id}      - 政治資金収支報告
```

## 変更の背景

新しいデータソースである選挙運動収支報告書を追加するにあたり、現状のページ構成では表現できなくなったため

## CLAへの同意

本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"[ ]" を "[x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **New Features**
  * 政治家一覧ページを追加しました。
  * 政治団体一覧ページを追加しました。
  * パンくずナビゲーション機能を追加しました。
  * 各ページのメタデータ（タイトル）を改善しました。

* **Documentation**
  * AI コーディング指示書を日本語で再編成しました。
  * プロジェクト構成ドキュメントを更新しました。

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/digitaldemocracy2030/polimoney/pull/251)

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [chore(deps): bump next from 15.5.12 to 15.5.18](https://github.com/digitaldemocracy2030/polimoney/pull/250)

**作成者:** dependabot[bot]  
**作成日:** 2026-05-08T14:03:49Z  
**変更:** +42 -49 (2ファイル)  
**マージ日:** 2026-05-10T14:17:21Z  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 15.5.12 to 15.5.18.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v15.5.18</h2>
<p>This release contains security fixes for the following advisories:</p>
<p>High:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj">GHSA-8h8q-6873-q5fj: Denial of Service with Server Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f">GHSA-267c-6grr-h53f: Middleware / Proxy bypass in App Router applications via segment-prefetch routes</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-26hh-7cqf-hhc6">GHSA-26hh-7cqf-hhc6: Middleware / Proxy bypass in App Router applications via segment-prefetch routes - Incomplete Fix Follow-Up</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx">GHSA-mg66-mrh9-m8jx: Denial of Service via connection exhaustion in applications using Cache Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-492v-c6pp-mqqv">GHSA-492v-c6pp-mqqv: Middleware / Proxy bypass through dynamic route parameter injection</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-c4j6-fc7j-m34r">GHSA-c4j6-fc7j-m34r: Server-side request forgery in applications using WebSocket upgrades</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-36qx-fr4f-26g5">GHSA-36qx-fr4f-26g5: Middleware / Proxy bypass in Pages Router applications using i18n</a></li>
</ul>
<p>Moderate:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-ffhc-5mcf-pf4q">GHSA-ffhc-5mcf-pf4q: Cross-site scripting in App Router applications using CSP nonces</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-gx5p-jg67-6x7h">GHSA-gx5p-jg67-6x7h: Cross-site scripting in beforeInteractive scripts with untrusted input</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-h64f-5h5j-jqjh">GHSA-h64f-5h5j-jqjh: Denial of Service in the Image Optimization API</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-wfc6-r584-vfw7">GHSA-wfc6-r584-vfw7: Cache poisoning in React Server Component responses</a></li>
</ul>
<p>Low:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-vfv6-92ff-j949">GHSA-vfv6-92ff-j949: Cache poisoning via collisions in React Server Component cache-busting</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-3g8h-86w9-wvmq">GHSA-3g8h-86w9-wvmq: Middleware / Proxy redirects can be cache-poisoned</a></li>
</ul>
<h2>v15.5.16</h2>
<p>This release contains security fixes for the following advisories:</p>
<p>High:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj">GHSA-8h8q-6873-q5fj: Denial of Service with Server Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f">GHSA-267c-6grr-h53f: Middleware / Proxy bypass in App Router applications via segment-prefetch routes</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx">GHSA-mg66-mrh9-m8jx: Denial of Service via connection exhaustion in applications using Cache Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-492v-c6pp-mqqv">GHSA-492v-c6pp-mqqv: Middleware / Proxy bypass through dynamic route parameter injection</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-c4j6-fc7j-m34r">GHSA-c4j6-fc7j-m34r: Server-side request forgery in applications using WebSocket upgrades</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-36qx-fr4f-26g5">GHSA-36qx-fr4f-26g5: Middleware / Proxy bypass in Pages Router applications using i18n</a></li>
</ul>
<p>Moderate:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-ffhc-5mcf-pf4q">GHSA-ffhc-5mcf-pf4q: Cross-site scripting in App Router applications using CSP nonces</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-gx5p-jg67-6x7h">GHSA-gx5p-jg67-6x7h: Cross-site scripting in beforeInteractive scripts with untrusted input</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-h64f-5h5j-jqjh">GHSA-h64f-5h5j-jqjh: Denial of Service in the Image Optimization API</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-wfc6-r584-vfw7">GHSA-wfc6-r584-vfw7: Cache poisoning in React Server Component responses</a></li>
</ul>
<p>Low:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-vfv6-92ff-j949">GHSA-vfv6-92ff-j949: Cache poisoning via collisions in React Server Component cache-busting</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-3g8h-86w9-wvmq">GHSA-3g8h-86w9-wvmq: Middleware / Proxy redirects can be cache-poisoned</a></li>
</ul>
<h2>v15.5.15</h2>
<p>Please refer the following changelogs for more information about this security release:</p>
<p><a href="https://vercel.com/changelog/summary-of-cve-2026-23869">https://vercel.com/changelog/summary-of-cve-2026-23869</a></p>
<h2>v15.5.14</h2>
<blockquote>
<p>[!NOTE]</p>
</blockquote>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/9ff92cebcaa6ba4e7463b6fd037a8510ba9b81ec"><code>9ff92ce</code></a> v15.5.18</li>
<li><a href="https://github.com/vercel/next.js/commit/00ebe23562bd7eb32dd78730984bfadb47138bcf"><code>00ebe23</code></a> [backport] Disable build caches for production/staging/force-preview deploys ...</li>
<li><a href="https://github.com/vercel/next.js/commit/62c97ab0b5825e2cbc15f6b682d8286a8dd6a038"><code>62c97ab</code></a> v15.5.17</li>
<li><a href="https://github.com/vercel/next.js/commit/423623ae38c106273085b66946ee5bf9aab77f2c"><code>423623a</code></a> Turbopack: Match proxy matchers with webpack implementation (<a href="https://redirect.github.com/vercel/next.js/issues/93594">#93594</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/fa787399b38d9aa702118f9bd23a8315b9f0ecc6"><code>fa78739</code></a> Turbopack: Fix middleware matcher suffix (<a href="https://redirect.github.com/vercel/next.js/issues/93590">#93590</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/36e62c6eb7813e42d409eb487f93b829f4ad77e8"><code>36e62c6</code></a> [backport] Turbopack: more strict vergen setup (<a href="https://redirect.github.com/vercel/next.js/issues/93588">#93588</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/36589b5db512b7704cdadd873cbe49b6dbcc9261"><code>36589b5</code></a> [backport][test] Pin package manager to patch versions (<a href="https://redirect.github.com/vercel/next.js/issues/93596">#93596</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/ad6fd4e50e5aba20b60d283c42b89273a3167ccd"><code>ad6fd4e</code></a> v15.5.16</li>
<li><a href="https://github.com/vercel/next.js/commit/79d7dff1448483f0c8f187f98887b31019f6e494"><code>79d7dff</code></a> Ignore malformed CSP nonce headers (<a href="https://redirect.github.com/vercel/next.js/issues/103">#103</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/c4f69086cc8dcbd81b1dbc321c98ea874d90d6f8"><code>c4f6908</code></a> router-server: guard upgrade proxy against absolute-url SSRF (<a href="https://redirect.github.com/vercel/next.js/issues/77">#77</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/102">#102</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/vercel/next.js/compare/v15.5.12...v15.5.18">compare view</a></li>
</ul>
</details>
<details>
<summary>Maintainer changes</summary>
<p>This version was pushed to npm by <a href="https://www.npmjs.com/~GitHub%20Actions">GitHub Actions</a>, a new releaser for next since your current version.</p>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=15.5.12&new-version=15.5.18)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/digitaldemocracy2030/polimoney/network/alerts).

</details>

**コメント:** なし

---

### [chore(deps-dev): bump basic-ftp from 5.2.0 to 5.3.1](https://github.com/digitaldemocracy2030/polimoney/pull/249)

**作成者:** dependabot[bot]  
**作成日:** 2026-05-08T14:03:16Z  
**変更:** +4 -11 (1ファイル)  
**マージ日:** 2026-05-10T14:18:02Z  
**内容:**

Bumps [basic-ftp](https://github.com/patrickjuchli/basic-ftp) from 5.2.0 to 5.3.1.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/patrickjuchli/basic-ftp/releases">basic-ftp's releases</a>.</em></p>
<blockquote>
<h2>5.3.1</h2>
<ul>
<li>Fixed: Protect against unbounded control response, fixes <a href="https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-rpmf-866q-6p89">https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-rpmf-866q-6p89</a>.</li>
</ul>
<h2>5.3.0</h2>
<ul>
<li>Changed: Introduced an upper bound for total bytes of directory listing, fixes <a href="https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-rp42-5vxx-qpwr">https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-rp42-5vxx-qpwr</a>.</li>
<li>Added: Option to increase the upper bound for total bytes of directory listing in Client constructor.</li>
</ul>
<h2>5.2.2</h2>
<ul>
<li>Fixed: Improve control character rejection, fixes <a href="https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-6v7q-wjvx-w8wg">https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-6v7q-wjvx-w8wg</a>.</li>
</ul>
<h2>5.2.1</h2>
<ul>
<li>Fixed: Reject control character injection attempts using paths. See <a href="https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-chqc-8p9q-pq6q">https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-chqc-8p9q-pq6q</a>.</li>
</ul>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/patrickjuchli/basic-ftp/blob/master/CHANGELOG.md">basic-ftp's changelog</a>.</em></p>
<blockquote>
<h2>5.3.1</h2>
<ul>
<li>Fixed: Protect against unbounded control response, fixes <a href="https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-rpmf-866q-6p89">https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-rpmf-866q-6p89</a>.</li>
</ul>
<h2>5.3.0</h2>
<ul>
<li>Changed: Introduced an upper bound for total bytes of directory listing, fixes <a href="https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-rp42-5vxx-qpwr">https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-rp42-5vxx-qpwr</a>.</li>
<li>Added: Option to increase the upper bound for total bytes of directory listing in Client constructor.</li>
</ul>
<h2>5.2.2</h2>
<ul>
<li>Fixed: Improve control character rejection, fixes <a href="https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-6v7q-wjvx-w8wg">https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-6v7q-wjvx-w8wg</a>.</li>
</ul>
<h2>5.2.1</h2>
<ul>
<li>Fixed: Reject control character injection attempts using paths. See <a href="https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-chqc-8p9q-pq6q">https://github.com/patrickjuchli/basic-ftp/security/advisories/GHSA-chqc-8p9q-pq6q</a>.</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/patrickjuchli/basic-ftp/commit/980371bb6057d78d479b5cfc18683392abd2c45f"><code>980371b</code></a> Guard against unbounded control response</li>
<li><a href="https://github.com/patrickjuchli/basic-ftp/commit/50827c73ca6c1d786c97276e47be8a33d0f2277d"><code>50827c7</code></a> Adjust changelog to match release notes</li>
<li><a href="https://github.com/patrickjuchli/basic-ftp/commit/c9378a8ff73b96e89f17525266d648ce495286a6"><code>c9378a8</code></a> Fix test</li>
<li><a href="https://github.com/patrickjuchli/basic-ftp/commit/22abe4356782f499d97418f0a7a2c3bb02db72b7"><code>22abe43</code></a> Update Github Actions</li>
<li><a href="https://github.com/patrickjuchli/basic-ftp/commit/0feaaec3d4394bb3470edd006df933d2b6e64689"><code>0feaaec</code></a> Fix test</li>
<li><a href="https://github.com/patrickjuchli/basic-ftp/commit/6629d7d7abe9169543a8ff60a6dc32e6fe7cf91c"><code>6629d7d</code></a> Improve error message</li>
<li><a href="https://github.com/patrickjuchli/basic-ftp/commit/9c3bf4f893470cd2418b54862eb9b609efc3d335"><code>9c3bf4f</code></a> Set higher default value for max size of directory listing</li>
<li><a href="https://github.com/patrickjuchli/basic-ftp/commit/acd3942c81ac27caf998b0ed13f3ce85c0fc6320"><code>acd3942</code></a> Bump version</li>
<li><a href="https://github.com/patrickjuchli/basic-ftp/commit/130442932b1ef27a550c915f231c07eae01e665a"><code>1304429</code></a> Offer maxListingBytes as an option</li>
<li><a href="https://github.com/patrickjuchli/basic-ftp/commit/5cb5367e86d8a2991224fb2b82e4933d27c07904"><code>5cb5367</code></a> Add bounded StringWriter</li>
<li>Additional commits viewable in <a href="https://github.com/patrickjuchli/basic-ftp/compare/v5.2.0...v5.3.1">compare view</a></li>
</ul>
</details>
<details>
<summary>Maintainer changes</summary>
<p>This version was pushed to npm by <a href="https://www.npmjs.com/~patrickjuchli">patrickjuchli</a>, a new releaser for basic-ftp since your current version.</p>
</details>
<details>
<summary>Install script changes</summary>
<p>This version adds <code>prepare</code> script that runs during installation. Review the package contents before updating.</p>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=basic-ftp&package-manager=npm_and_yarn&previous-version=5.2.0&new-version=5.3.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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
- `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/digitaldemocracy2030/polimoney/network/alerts).

</details>

**コメント:** なし

---

### [岩永さん公開暫定対応](https://github.com/digitaldemocracy2030/polimoney/pull/248)

**作成者:** shumizu418128  
**作成日:** 2026-05-08T13:50:20Z  
**変更:** +78 -22 (4ファイル)  
**マージ日:** 2026-05-08T14:00:51Z  
**内容:**

## 変更の概要

<!-- ここに変更の概要を記載してください -->

## 変更の背景

<!-- ここに変更が必要となった背景を記載してください -->

## スクリーンショット

<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

## 関連Issue

<!-- 関連する Issue がある場合、こちらに記載してください -->

## CLAへの同意

本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"[ ]" を "[x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

## リリースノート

* **バグ修正**
  * Auth0の読み込み状態中の処理を改善しました
  * 認証状態に基づくアクセス制御の動作を調整しました

* **新機能**
  * 特定のエントリに直接リンク機能を追加し、ナビゲーションの柔軟性が向上しました

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

