# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-05-06T13:24:50.496545+09:00 から 2026-05-13T13:24:50.496545+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (0件)

### 過去7日間に作成されたPR (2件)

### [chore(deps): bump next from 16.2.3 to 16.2.6](https://github.com/digitaldemocracy2030/kouchou-ai/pull/823)

**作成者:** dependabot[bot]  
**作成日:** 2026-05-13T00:14:10Z  
**変更:** +167 -139 (3ファイル)  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 16.2.3 to 16.2.6.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v16.2.6</h2>
<blockquote>
<p>[!NOTE]
This release contains security fixes and backported bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Security Fixes</h3>
<p>The following advisories have been addressed:</p>
<p><strong>High:</strong></p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj">GHSA-8h8q-6873-q5fj: Denial of Service with Server Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f">GHSA-267c-6grr-h53f: Middleware / Proxy bypass in App Router applications via segment-prefetch routes</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-26hh-7cqf-hhc6">GHSA-26hh-7cqf-hhc6: Middleware / Proxy bypass in App Router applications via segment-prefetch routes - <strong>Incomplete Fix Follow-Up</strong></a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx">GHSA-mg66-mrh9-m8jx: Denial of Service via connection exhaustion in applications using Cache Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-492v-c6pp-mqqv">GHSA-492v-c6pp-mqqv: Middleware / Proxy bypass through dynamic route parameter injection</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-c4j6-fc7j-m34r">GHSA-c4j6-fc7j-m34r: Server-side request forgery in applications using WebSocket upgrades</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-36qx-fr4f-26g5">GHSA-36qx-fr4f-26g5: Middleware / Proxy bypass in Pages Router applications using i18n</a></li>
</ul>
<p><strong>Moderate:</strong></p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-ffhc-5mcf-pf4q">GHSA-ffhc-5mcf-pf4q: Cross-site scripting in App Router applications using CSP nonces</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-gx5p-jg67-6x7h">GHSA-gx5p-jg67-6x7h: Cross-site scripting in beforeInteractive scripts with untrusted input</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-h64f-5h5j-jqjh">GHSA-h64f-5h5j-jqjh: Denial of Service in the Image Optimization API</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-wfc6-r584-vfw7">GHSA-wfc6-r584-vfw7: Cache poisoning in React Server Component responses</a></li>
</ul>
<p><strong>Low:</strong></p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-vfv6-92ff-j949">GHSA-vfv6-92ff-j949: Cache poisoning via collisions in React Server Component cache-busting</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-3g8h-86w9-wvmq">GHSA-3g8h-86w9-wvmq: Middleware / Proxy redirects can be cache-poisoned</a></li>
</ul>
<h3>Core Changes</h3>
<ul>
<li>fix: preserve HTTP access fallbacks during prerender recovery (<a href="https://redirect.github.com/vercel/next.js/issues/92231">#92231</a>)</li>
<li>Fix fallback route params case in app-page handler (<a href="https://redirect.github.com/vercel/next.js/issues/91737">#91737</a>)</li>
<li>Fix invalid HTML response for route-level RSC requests in deployment adapter (<a href="https://redirect.github.com/vercel/next.js/issues/91541">#91541</a>)</li>
<li>Patch setHeader for direct route handlers (<a href="https://redirect.github.com/vercel/next.js/issues/93101">#93101</a>)</li>
<li>Include deployment id in <code>cacheHandlers</code> keys (<a href="https://redirect.github.com/vercel/next.js/issues/93453">#93453</a>)</li>
<li>Fix double-encoding of URL pathname parts in client param parsing (<a href="https://redirect.github.com/vercel/next.js/issues/93491">#93491</a>)</li>
</ul>
<h2>v16.2.5</h2>
<blockquote>
<p>[!NOTE]
This release contains security fixes and backported bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Security Fixes</h3>
<p>The following advisories have been addressed:</p>
<p><strong>High:</strong></p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-8h8q-6873-q5fj">GHSA-8h8q-6873-q5fj: Denial of Service with Server Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-267c-6grr-h53f">GHSA-267c-6grr-h53f: Middleware / Proxy bypass in App Router applications via segment-prefetch routes</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-mg66-mrh9-m8jx">GHSA-mg66-mrh9-m8jx: Denial of Service via connection exhaustion in applications using Cache Components</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-492v-c6pp-mqqv">GHSA-492v-c6pp-mqqv: Middleware / Proxy bypass through dynamic route parameter injection</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-c4j6-fc7j-m34r">GHSA-c4j6-fc7j-m34r: Server-side request forgery in applications using WebSocket upgrades</a></li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/ee6e79b1792a4d401ddf2480f40a83549fe8e722"><code>ee6e79b</code></a> v16.2.6</li>
<li><a href="https://github.com/vercel/next.js/commit/afa053d9eb9c2a68c7eba43e84fe6bed8babcd45"><code>afa053d</code></a> Turbopack: Match proxy matchers with webpack implementation (<a href="https://redirect.github.com/vercel/next.js/issues/93594">#93594</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/97a154e5bbee0cb1ac3fb8aa4db66ac36e796e3d"><code>97a154e</code></a> Turbopack: Fix middleware matcher suffix (<a href="https://redirect.github.com/vercel/next.js/issues/93590">#93590</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/83899bc89103d4df1479e065c7c1e09d4698a7b6"><code>83899bc</code></a> [backport] Disable build caches for production/staging/force-preview deploys ...</li>
<li><a href="https://github.com/vercel/next.js/commit/7b222b90954d607fc28a34e9b360a9b1636bc206"><code>7b222b9</code></a> [backport][test] Pin package manager to patch versions (<a href="https://redirect.github.com/vercel/next.js/issues/93595">#93595</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/a8dc24f1fe23d4a22d24fac734837f7c824138f7"><code>a8dc24f</code></a> [backport] Turbopack: more strict vergen setup (<a href="https://redirect.github.com/vercel/next.js/issues/93587">#93587</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/766148f9cd48c0e218acafcd0f15defc14871bf4"><code>766148f</code></a> v16.2.5</li>
<li><a href="https://github.com/vercel/next.js/commit/0dd94836a8b43209fcfefa448c141683c22c1a27"><code>0dd9483</code></a> fix: add explicit checks for RSC header (<a href="https://redirect.github.com/vercel/next.js/issues/83">#83</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/98">#98</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/d166096c399c4fc4e09cd2d1bf26dca6579a855d"><code>d166096</code></a> fix proxy matching for segment prefetch URLs (<a href="https://redirect.github.com/vercel/next.js/issues/89">#89</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/96">#96</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/9d50c0b7190f59c470308578e12882788819f14c"><code>9d50c0b</code></a> Strip next-resume header from incoming requests (<a href="https://redirect.github.com/vercel/next.js/issues/92">#92</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/vercel/next.js/compare/v16.2.3...v16.2.6">compare view</a></li>
</ul>
</details>
<details>
<summary>Maintainer changes</summary>
<p>This version was pushed to npm by <a href="https://www.npmjs.com/~GitHub%20Actions">GitHub Actions</a>, a new releaser for next since your current version.</p>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=16.2.3&new-version=16.2.6)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/digitaldemocracy2030/kouchou-ai/network/alerts).

</details>

**コメント:** なし

---

### [chore(deps): bump next from 16.1.5 to 16.2.6 in /utils/dummy-server](https://github.com/digitaldemocracy2030/kouchou-ai/pull/822)

**作成者:** dependabot[bot]  
**作成日:** 2026-05-12T08:03:37Z  
**変更:** +1 -1 (1ファイル)  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 16.1.5 to 16.2.6.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v16.2.6</h2>
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
<h2>v16.2.5</h2>
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
<h2>v16.2.4</h2>
<blockquote>
<p>[!NOTE]
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>chore: Bump reqwest to 0.13.2 (Fixes Google Fonts with Turbopack for Windows on ARM64) (<a href="https://redirect.github.com/vercel/next.js/issues/92713">#92713</a>)</li>
</ul>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/ee6e79b1792a4d401ddf2480f40a83549fe8e722"><code>ee6e79b</code></a> v16.2.6</li>
<li><a href="https://github.com/vercel/next.js/commit/afa053d9eb9c2a68c7eba43e84fe6bed8babcd45"><code>afa053d</code></a> Turbopack: Match proxy matchers with webpack implementation (<a href="https://redirect.github.com/vercel/next.js/issues/93594">#93594</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/97a154e5bbee0cb1ac3fb8aa4db66ac36e796e3d"><code>97a154e</code></a> Turbopack: Fix middleware matcher suffix (<a href="https://redirect.github.com/vercel/next.js/issues/93590">#93590</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/83899bc89103d4df1479e065c7c1e09d4698a7b6"><code>83899bc</code></a> [backport] Disable build caches for production/staging/force-preview deploys ...</li>
<li><a href="https://github.com/vercel/next.js/commit/7b222b90954d607fc28a34e9b360a9b1636bc206"><code>7b222b9</code></a> [backport][test] Pin package manager to patch versions (<a href="https://redirect.github.com/vercel/next.js/issues/93595">#93595</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/a8dc24f1fe23d4a22d24fac734837f7c824138f7"><code>a8dc24f</code></a> [backport] Turbopack: more strict vergen setup (<a href="https://redirect.github.com/vercel/next.js/issues/93587">#93587</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/766148f9cd48c0e218acafcd0f15defc14871bf4"><code>766148f</code></a> v16.2.5</li>
<li><a href="https://github.com/vercel/next.js/commit/0dd94836a8b43209fcfefa448c141683c22c1a27"><code>0dd9483</code></a> fix: add explicit checks for RSC header (<a href="https://redirect.github.com/vercel/next.js/issues/83">#83</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/98">#98</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/d166096c399c4fc4e09cd2d1bf26dca6579a855d"><code>d166096</code></a> fix proxy matching for segment prefetch URLs (<a href="https://redirect.github.com/vercel/next.js/issues/89">#89</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/96">#96</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/9d50c0b7190f59c470308578e12882788819f14c"><code>9d50c0b</code></a> Strip next-resume header from incoming requests (<a href="https://redirect.github.com/vercel/next.js/issues/92">#92</a>)</li>
<li>Additional commits viewable in <a href="https://github.com/vercel/next.js/compare/v16.1.5...v16.2.6">compare view</a></li>
</ul>
</details>
<details>
<summary>Maintainer changes</summary>
<p>This version was pushed to npm by <a href="https://www.npmjs.com/~GitHub%20Actions">GitHub Actions</a>, a new releaser for next since your current version.</p>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=16.1.5&new-version=16.2.6)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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
You can disable automated security fix PRs for this repo from the [Security Alerts page](https://github.com/digitaldemocracy2030/kouchou-ai/network/alerts).

</details>

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

