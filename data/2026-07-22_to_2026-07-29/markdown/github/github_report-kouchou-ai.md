# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-07-22T14:56:57.988504+09:00 から 2026-07-29T14:56:57.988504+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (0件)

### 過去7日間に作成されたPR (1件)

### [Bump next from 16.2.6 to 16.2.11 in /utils/dummy-server](https://github.com/digitaldemocracy2030/kouchou-ai/pull/904)

**作成者:** dependabot[bot]  
**作成日:** 2026-07-28T03:17:55Z  
**変更:** +1 -1 (1ファイル)  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 16.2.6 to 16.2.11.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v16.2.11</h2>
<p>This release contains security fixes for the following advisories:</p>
<p>High:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-m99w-x7hq-7vfj">Denial of Service in App Router using Server Actions</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-6gpp-xcg3-4w24">Middleware / Proxy bypass in App Router applications using Turbopack and single locale</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-p9j2-gv94-2wf4">Server-Side Request Forgery in rewrites via attacker-controlled destination hostname</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-89xv-2m56-2m9x">Server-Side Request Forgery in Server Actions on custom servers</a></li>
</ul>
<p>Moderate:</p>
<ul>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-68g3-v927-f742">Cache confusion of response bodies for requests with bodies</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-4633-3j49-mh5q">Cache confusion of response bodies for requests with bodies containing invalid UTF-8 byte sequences</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-q8wf-6r8g-63ch">Denial of Service in the Image Optimization API using SVGs</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-955p-x3mx-jcvp">Unauthenticated disclosure of internal Server Function endpoints</a></li>
<li><a href="https://github.com/vercel/next.js/security/advisories/GHSA-4c39-4ccg-62r3">Unbounded Server Action payload in Edge runtime</a></li>
</ul>
<h2>v16.2.10</h2>
<p>Contains no changes except publishing <code>@next/swc-wasm-web</code> which was accidentally not published since 16.2.4.</p>
<h2>v16.2.9</h2>
<p>Empty release to ensure <code>next@latest</code> points at a stable release. Next.js only allows publishing with Trusted Publishing enabled. In order to fix NPM dist-tags, we have to release a new version. Updating dist-tags is not possible with Trusted Publishing.</p>
<h2>v16.2.8</h2>
<p>Release with no changes in an attempt to fix <code>next@latest</code> pointing at a prerelease version.</p>
<h2>v16.2.7</h2>
<blockquote>
<p>[!NOTE]
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>Backport documentation fixes for v16.2 (<a href="https://redirect.github.com/vercel/next.js/issues/93804">#93804</a>)</li>
<li>[backport] Patch <code>playwright-core</code> to resolve <code>_finishedPromise</code> on <code>requestFailed</code> (<a href="https://redirect.github.com/vercel/next.js/issues/93920">#93920</a>)</li>
<li>[backport] Fix dev mode hydration failure when page is served from HTTP cache (<a href="https://redirect.github.com/vercel/next.js/issues/93492">#93492</a>)</li>
<li>[backport] Fix catch-all <code>router.query</code> corruption with <code>basePath</code> + <code>rewrites</code> (<a href="https://redirect.github.com/vercel/next.js/issues/93917">#93917</a>)</li>
<li>[backport] Encode non-ASCII characters in cache tags at construction (<a href="https://redirect.github.com/vercel/next.js/issues/93918">#93918</a>)</li>
<li>[backport] Fix server action forwarding loop with middleware rewrites (<a href="https://redirect.github.com/vercel/next.js/issues/93919">#93919</a>)</li>
<li>[backport] Turbopack: switch from base40 to base38 hash encoding (<a href="https://redirect.github.com/vercel/next.js/issues/93932">#93932</a>)</li>
<li>[ci] Disable hanging node 24 typescript tests on 16.2 backport branch (<a href="https://redirect.github.com/vercel/next.js/issues/94164">#94164</a>)</li>
<li>[backport] Fix &quot;type: module&quot; in project dir when using standalone or adapters (<a href="https://redirect.github.com/vercel/next.js/issues/94050">#94050</a>)</li>
<li>[backport] Propagate adapter preferred regions (<a href="https://redirect.github.com/vercel/next.js/issues/94200">#94200</a>)</li>
<li>[16.2.x] Don't drop <code>FormData</code> entries (<a href="https://redirect.github.com/vercel/next.js/issues/94240">#94240</a>)</li>
<li>[backport] feat(turbopack): add LocalPathOrProjectPath PostCSS config resolution (<a href="https://redirect.github.com/vercel/next.js/issues/94284">#94284</a>)</li>
</ul>
<h3>Credits</h3>
<p>Huge thanks to <a href="https://github.com/eps1lon"><code>@​eps1lon</code></a>, <a href="https://github.com/icyJoseph"><code>@​icyJoseph</code></a>, <a href="https://github.com/unstubbable"><code>@​unstubbable</code></a>, <a href="https://github.com/mischnic"><code>@​mischnic</code></a>, <a href="https://github.com/bgw"><code>@​bgw</code></a>, <a href="https://github.com/timneutkens"><code>@​timneutkens</code></a>, and <a href="https://github.com/lukesandberg"><code>@​lukesandberg</code></a> for helping!</p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/9beca0821cf4606ae33466ed6f4fc75f2887a4da"><code>9beca08</code></a> v16.2.11</li>
<li><a href="https://github.com/vercel/next.js/commit/3c48c7af78f2c01691065cb303da1b107a2c8617"><code>3c48c7a</code></a> [16.x] Fix Turbopack middleware matcher with i18n single locale</li>
<li><a href="https://github.com/vercel/next.js/commit/ac1eff3f7a7285176396ecc69c3b160a3d6ad1a2"><code>ac1eff3</code></a> [16.x] Improve performance of checking valid MPA form submissions</li>
<li><a href="https://github.com/vercel/next.js/commit/9a4651e754f70b12e397694ffc41f44c3ba8cc17"><code>9a4651e</code></a> [16.x] Enforce <code>serverActions.bodySizeLimit</code> for Server Actions in Edge runtime</li>
<li><a href="https://github.com/vercel/next.js/commit/b51206321854193208c0805ba42acc49287f942b"><code>b512063</code></a> [16.x] Set correct origin for internal redirects in custom server</li>
<li><a href="https://github.com/vercel/next.js/commit/d3033266c6dff23f7be71e19341fe3a8c6e2c599"><code>d303326</code></a> [16.x] Ensure exotic rewrite param values are properly encoded</li>
<li><a href="https://github.com/vercel/next.js/commit/73b94872bc343d09494b50394d8c08eb9fc8e56a"><code>73b9487</code></a> [16.x] fix(fetch-cache): key fetch(Request, init) by the effective request</li>
<li><a href="https://github.com/vercel/next.js/commit/bf9d17fb30501829f6fd7c0ee8e44e2794565742"><code>bf9d17f</code></a> [16.x] fix(incremental-cache): byte-exact fetch cache key for binary bodies</li>
<li><a href="https://github.com/vercel/next.js/commit/fe28768f533582ea8f6ee7d7a7498715927d45f5"><code>fe28768</code></a> [16.x] fix(next/image): improve performance of detectContentType()</li>
<li><a href="https://github.com/vercel/next.js/commit/d8afb8d550ac4ac5c106ea1410c3af43eaf1d469"><code>d8afb8d</code></a> [16.x] Performance improvements when decoding React Server function payloads</li>
<li>Additional commits viewable in <a href="https://github.com/vercel/next.js/compare/v16.2.6...v16.2.11">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=16.2.6&new-version=16.2.11)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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

