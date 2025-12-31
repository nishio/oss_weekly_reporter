# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-12-24T12:36:43.736854+09:00 から 2025-12-31T12:36:43.736854+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (2件)

### [[BUG] main ブランチへのマージ時に実行される Azure への deploy が失敗することがある](https://github.com/digitaldemocracy2030/kouchou-ai/issues/741)

**作成者:** shingo-ohki  
**作成日:** 2025-12-27T14:53:28Z  
**内容:**

### 概要

表題通り。

- 失敗したときの事例
https://github.com/digitaldemocracy2030/kouchou-ai/actions/runs/20540103407/attempts/1

- リトライで直った
https://github.com/digitaldemocracy2030/kouchou-ai/actions/runs/20540103407

### 再現手順

1. main ブランチに更新を入れる
2. GitHub Actions で Azure への deploy 処理が動く
3. たまに失敗する

### 期待する動作

毎回 deploy が成功する
<!-- 本来どう動作すべきかを記入してください -->

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

### その他

AIによると、原因はこんな感じ
```
発生箇所: Azure デプロイの Docker ビルド中、client イメージの Dockerfile:14 の RUN npm ci で npm ERR! code ECONNRESET により失敗。内容は npm レジストリへの接続リセットで、依存関係の不整合ではありません。
文脈: azure-deploy.yml:53-90 で API/client/client-admin/client-static-build の 4 イメージを並列ビルド。複数の npm ci が同時に走るため、GitHub ホストランナー上でレジストリへの接続がまれに途切れる典型的なネットワーク起因の失敗です。
他のステージ (Python 依存、client-admin ビルドなど) は完走しており、恒常的な依存問題ではなく一時的な接続切れが原因と考えられます。

対応案（優先度順）

1. まずはリトライ実行: ワークフローを再実行すれば通る可能性が高いです。
2. npm ci にリトライとタイムアウトを付与 (各 Dockerfile の npm 実行直前で):
例: npm config set fetch-retries 5 && npm config set fetch-retry-mintimeout 20000 && npm config set fetch-retry-maxtimeout 120000 && npm config set registry https://registry.npmjs.org/
あるいは npm ci --fetch-retries=5 --fetch-retry-mintimeout=20000 --fetch-retry-maxtimeout=120000 --network-timeout=600000
対象: Dockerfile:14, Dockerfile:17, Dockerfile:5 と同ファイル内 2 回目の npm ci.
3. 並列度を下げる: ワークフローで Docker ビルドを直列にする、または client 系をまとめて後段にずらすことでレジストリへの同時接続を減らす。
4. npm キャッシュ活用: Docker BuildKit のキャッシュマウントや npm ci --cache /tmp/npm-cache を併用し、外部アクセス回数を削減。
まずは 1) を試し、再発するようなら 2) を反映、それでも改善しなければ 3)/4) を検討するのが現実的です。
```

**コメント:** なし

---

### [レポート一覧取得時にslugフィールドの欠落によるValidationErrorが発生する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/740)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-12-27T14:09:44Z  
**内容:**

## 概要

レポート一覧画面でレポートの取得に失敗し、「レポートの取得に失敗しました」というエラーメッセージが表示される問題が発生しています。

## 原因

`report_status.json` に保存されている既存のレポートデータに `slug` フィールドが欠落しているため、Pydanticのバリデーションエラーが発生しています。

## エラーログ

```
pydantic_core._pydantic_core.ValidationError: 1 validation error for Report
slug
  Field required [type=missing, input_value={'status': 'ready', 'titl...token_usage_output': 70}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
```

## 再現手順

1. `docker compose up` でアプリケーションを起動
2. http://localhost:3000 または http://localhost:4000 にアクセス
3. レポート一覧を取得しようとすると、上記のエラーが発生

## 影響範囲

- レポート閲覧画面（client）のレポート一覧
- 管理画面（client-admin）のレポート一覧

## 関連コード

- `server/src/services/report_status.py` の `load_status_as_reports()` 関数
- `server/src/schemas/report.py` の `Report` スキーマ

## 提案される修正方法

1. 既存の `report_status.json` データに `slug` フィールドを追加するマイグレーションスクリプトを作成
2. または、`load_status_as_reports()` 関数で `slug` フィールドが欠落している場合のフォールバック処理を追加

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (3件)

### [Bump next from 15.4.9 to 15.4.10 in /utils/dummy-server](https://github.com/digitaldemocracy2030/kouchou-ai/pull/739)

**作成者:** dependabot[bot]  
**作成日:** 2025-12-27T13:39:30Z  
**変更:** +9 -9 (2ファイル)  
**マージ日:** 2025-12-27T14:19:32Z  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 15.4.9 to 15.4.10.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v15.4.10</h2>
<p>Please see the <a href="https://nextjs.org/blog/security-update-2025-12-11">Next.js Security Update</a> for information about this security patch.</p>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/43cb5460c809ab97b6547b7765542cf16adcfc3c"><code>43cb546</code></a> v15.4.10</li>
<li><a href="https://github.com/vercel/next.js/commit/6129673307eb9afd8fe7954162faa28064bc847b"><code>6129673</code></a> Backport <a href="https://redirect.github.com/facebook/react/issues/35351">facebook/react#35351</a> for 15.4.9 (<a href="https://redirect.github.com/vercel/next.js/issues/87087">#87087</a>)</li>
<li>See full diff in <a href="https://github.com/vercel/next.js/compare/v15.4.9...v15.4.10">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=15.4.9&new-version=15.4.10)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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

### [Bump next from 15.5.7 to 15.5.9 in /client](https://github.com/digitaldemocracy2030/kouchou-ai/pull/738)

**作成者:** dependabot[bot]  
**作成日:** 2025-12-12T02:09:50Z  
**変更:** +9 -9 (2ファイル)  
**マージ日:** 2025-12-27T14:12:26Z  
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
**マージ日:** 2025-12-27T13:38:13Z  
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

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

