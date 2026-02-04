# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-01-28T12:51:25.527586+09:00 から 2026-02-04T12:51:25.527586+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (1件)

### [[FEATURE]レポート生成ページから一覧ページに戻る手段がなさそう](https://github.com/digitaldemocracy2030/kouchou-ai/issues/775)

**作成者:** nishio  
**作成日:** 2026-02-03T11:59:00Z  
**内容:**

# 背景
レポート生成ページから一覧ページに戻る手段がなさそう
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(1件)

### [[BUG] main ブランチへのマージ時に実行される Azure への deploy が失敗する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/741)

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

## Pull Requests

### 過去7日間にマージされたPR (5件)

### [ドキュメントに技術解説資料へのリンクを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/777)

**作成者:** shingo-ohki  
**作成日:** 2026-02-03T13:47:29Z  
**変更:** +1 -0 (1ファイル)  
**マージ日:** 2026-02-03T15:12:02Z  
**内容:**

# 変更の概要
- ドキュメントに技術解説資料へのリンクを追加します

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

## リリースノート

* **ドキュメンテーション**
  * ドキュメント構成に技術解説資料への外部リンクを追加しました。ユーザーが技術情報へより簡単にアクセスできるようになりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [pandas -> polars の変更をrequirements.lock にも反映](https://github.com/digitaldemocracy2030/kouchou-ai/pull/774)

**作成者:** shingo-ohki  
**作成日:** 2026-02-03T03:25:44Z  
**変更:** +8 -20 (2ファイル)  
**マージ日:** 2026-02-03T08:03:49Z  
**内容:**

# 変更の概要
- 表題通り

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

**コメント:** なし

---

### [chore(deps): bump next from 15.5.9 to 16.1.5](https://github.com/digitaldemocracy2030/kouchou-ai/pull/773)

**作成者:** dependabot[bot]  
**作成日:** 2026-01-28T19:29:00Z  
**変更:** +252 -226 (4ファイル)  
**マージ日:** 2026-02-03T15:24:13Z  
**内容:**

# 変更の概要
- Next.js を 15.5.9 から 16.1.5 にアップグレード（dependabot による自動PR）
- Next.js 16 の破壊的変更に対応するため、`revalidateTag` の呼び出しを修正

# スクリーンショット
- UIの変更はありません

# 変更の背景
dependabot によるセキュリティアップデートPRです。Next.js 16 では `revalidateTag` 関数のAPIが変更され、第2引数（profile）が必須になりました。

**修正内容:**
```typescript
// Before (Next.js 15)
revalidateTag(tag);

// After (Next.js 16)
revalidateTag(tag, "max");
```

`"max"` プロファイルを使用すると、タグはstaleとしてマークされ、次回アクセス時にstale-while-revalidateセマンティクスが適用されます（バックグラウンドで新しいデータを取得しながら古いコンテンツを提供）。

## Next.js 16 リリースノート
<details>
<summary>Release notes</summary>

- v16.1.5: セキュリティリリース（CVE-2025-59471, CVE-2025-59472, CVE-2026-23864）
- Turbopack がデフォルトバンドラーに
- `revalidateTag` API の変更（第2引数が必須に）

詳細: https://nextjs.org/blog/next-16
</details>

# 関連Issue
N/A（dependabot セキュリティアップデート）

# 動作確認の結果
- CI（build, test, e2e-tests）が全てパスすることを確認

# CLAへの同意
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [ ] `"max"` プロファイルによるキャッシュ動作の変更が許容できるか確認（stale-while-revalidate方式に変更）
- [ ] Next.js 16 の他の破壊的変更がアプリケーションに影響しないか確認

---

**Link to Devin run:** https://app.devin.ai/sessions/c0b3879548cc4061aca5fe1a05ebaf19
**Requested by:** NISHIO (@nishio)

**コメント:** なし

---

### [chore(deps): bump next from 15.4.10 to 16.1.5 in /utils/dummy-server](https://github.com/digitaldemocracy2030/kouchou-ai/pull/772)

**作成者:** dependabot[bot]  
**作成日:** 2026-01-28T17:59:49Z  
**変更:** +55 -44 (2ファイル)  
**マージ日:** 2026-02-03T12:05:30Z  
**内容:**

Bumps [next](https://github.com/vercel/next.js) from 15.4.10 to 16.1.5.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/vercel/next.js/releases">next's releases</a>.</em></p>
<blockquote>
<h2>v16.1.5</h2>
<p>Please refer the following changelogs for more information about this security release:</p>
<p><a href="https://vercel.com/changelog/summaries-of-cve-2025-59471-and-cve-2025-59472">https://vercel.com/changelog/summaries-of-cve-2025-59471-and-cve-2025-59472</a>
<a href="https://vercel.com/changelog/summary-of-cve-2026-23864">https://vercel.com/changelog/summary-of-cve-2026-23864</a></p>
<h2>v16.1.4</h2>
<blockquote>
<p>[!NOTE]
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>Only filter next config if experimental flag is enabled (<a href="https://redirect.github.com/vercel/next.js/issues/88733">#88733</a>)</li>
</ul>
<h3>Credits</h3>
<p>Huge thanks to <a href="https://github.com/mischnic"><code>@​mischnic</code></a> for helping!</p>
<h2>v16.1.3</h2>
<blockquote>
<p>[!NOTE]
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>Fix linked list bug in LRU deleteFromLru (<a href="https://redirect.github.com/vercel/next.js/issues/88652">#88652</a>)</li>
<li>Fix relative same host redirects in node middleware (<a href="https://redirect.github.com/vercel/next.js/issues/88253">#88253</a>)</li>
</ul>
<h3>Credits</h3>
<p>Huge thanks to <a href="https://github.com/acdlite"><code>@​acdlite</code></a> and <a href="https://github.com/ijjk"><code>@​ijjk</code></a> for helping!</p>
<h2>v16.1.2</h2>
<blockquote>
<p>[!NOTE]
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<h3>Core Changes</h3>
<ul>
<li>Turbopack: Update to swc_core v50.2.3 (<a href="https://redirect.github.com/vercel/next.js/issues/87841">#87841</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/88296">#88296</a>)
<ul>
<li>Fixes a crash when processing mdx files with multibyte characters. (<a href="https://redirect.github.com/vercel/next.js/issues/87713">#87713</a>)</li>
</ul>
</li>
<li>Turbopack: <a href="https://microsoft.github.io/mimalloc/">mimalloc</a> upgrade and enabling it on musl (<a href="https://redirect.github.com/vercel/next.js/issues/88503">#88503</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/87815">#87815</a>) (<a href="https://redirect.github.com/vercel/next.js/issues/88426">#88426</a>)
<ul>
<li>Fixes <a href="https://redirect.github.com/vercel/next.js/pull/88426">a significant performance issue</a> on musl-based Linux distributions (e.g. Alpine in Docker) related to musl's allocator.</li>
<li>Other platforms have always used mimalloc, but we previously did not use mimalloc on musl because of compilation issues that have since been resolved.</li>
</ul>
</li>
</ul>
<h3>Credits</h3>
<p>Huge thanks to <a href="https://github.com/mischnic"><code>@​mischnic</code></a> for helping!</p>
<h2>v16.1.1</h2>
<blockquote>
<p>[!NOTE]
This release is backporting bug fixes. It does <strong>not</strong> include all pending features/changes on canary.</p>
</blockquote>
<!-- raw HTML omitted -->
</blockquote>
<p>... (truncated)</p>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/vercel/next.js/commit/acba4a6b9f48e0a067c592dac322410c0e122018"><code>acba4a6</code></a> v16.1.5</li>
<li><a href="https://github.com/vercel/next.js/commit/e1d1fc6525ef74b2bf78149f1669c2eab437c06a"><code>e1d1fc6</code></a> Add maximum size limit for postponed body parsing (<a href="https://redirect.github.com/vercel/next.js/issues/88175">#88175</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/500ec83743639addceaede95e95913398975156c"><code>500ec83</code></a> fetch(next/image): reduce maximumResponseBody from 300MB to 50MB (<a href="https://redirect.github.com/vercel/next.js/issues/88588">#88588</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/1caaca3cdbd2da76698bb9e60ff07d21a6fb6e77"><code>1caaca3</code></a> feat(next/image)!: add <code>images.maximumResponseBody</code> config (<a href="https://redirect.github.com/vercel/next.js/issues/88183">#88183</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/522ed840be26899bb88e73e2a5d3695f3c640d22"><code>522ed84</code></a> Sync DoS mitigations for React Flight</li>
<li><a href="https://github.com/vercel/next.js/commit/8cad197c76dd9583b1a6d52f5e423e7075f6bee9"><code>8cad197</code></a> [backport][cna] Ensure created app is not considered the workspace root in pn...</li>
<li><a href="https://github.com/vercel/next.js/commit/27186615d7c792f2c6627d3ac750d14951221e4c"><code>2718661</code></a> Backport/docs fixes (<a href="https://redirect.github.com/vercel/next.js/issues/89031">#89031</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/53336250b3a4b2b23198aaa9cf9549f9fff1bb39"><code>5333625</code></a> Backport/docs fixes 16.1.5 (<a href="https://redirect.github.com/vercel/next.js/issues/88916">#88916</a>)</li>
<li><a href="https://github.com/vercel/next.js/commit/60de6c21144a78622eb8c4763f364fcb59f7aa59"><code>60de6c2</code></a> v16.1.4</li>
<li><a href="https://github.com/vercel/next.js/commit/5f75d22b804d444d6c27240f5f7af32aee4a8f92"><code>5f75d22</code></a> backport: Only filter next config if experimental flag is enabled (<a href="https://redirect.github.com/vercel/next.js/issues/88733">#88733</a>) (#...</li>
<li>Additional commits viewable in <a href="https://github.com/vercel/next.js/compare/v15.4.10...v16.1.5">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=next&package-manager=npm_and_yarn&previous-version=15.4.10&new-version=16.1.5)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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

### [docs: why-pnpm刷新とプラグイン出力仕様の整理](https://github.com/digitaldemocracy2030/kouchou-ai/pull/770)

**作成者:** nishio  
**作成日:** 2026-01-26T13:20:08Z  
**変更:** +323 -19 (3ファイル)  
**マージ日:** 2026-02-03T16:58:18Z  
**内容:**

# 変更の概要
- why-pnpm の説明を刷新し、hoisting問題とプラグイン運用の必然性を明確化
- 入力プラグイン/分析プラグインの出力データ構造を新規ドキュメント化
- 上記ドキュメントをMkDocsナビに追加

# スクリーンショット
- なし（ドキュメントのみ）

# 変更の背景
- プラグインシステム導入にあたり、pnpm採用理由とデータ構造の契約を読者に明確に伝えるため

# 関連Issue
- なし

# 動作確認の結果
- 未実施（ドキュメントのみ）

# CLAへの同意
- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

## リリースノート

* **Documentation**
  * プラグイン出力データ構造に関する開発者向けドキュメントを新規追加しました（出力フォーマットや必須/任意列、欠落値の扱いなどを明記）。
  * 開発ツール選定に関する文書を再構成・拡充し、プラグインの独立性やホイスティング問題への対応理由を明確化しました。
  * 開発者向けナビゲーションに新規ドキュメントを追加しました。

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (1件)

### [feat: レポート作成ページから一覧ページに戻る手段を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/776)

**作成者:** nishio  
**作成日:** 2026-02-03T12:09:51Z  
**変更:** +13 -4 (2ファイル)  
**内容:**

# 変更の概要
- Headerのロゴをクリックすると一覧ページ（`/`）に遷移するようにした
- レポート作成ページに「キャンセル」ボタンを追加し、一覧ページに戻れるようにした

# スクリーンショット
- UIの変更を伴うため、レビュアーによる動作確認をお願いします

# 変更の背景
レポート作成ページ（`/create`）から一覧ページに戻る手段がなく、ブラウザの「戻る」ボタンを使うかURLを直接入力するしかなかった。一般的なUXパターンとして、ロゴクリックでホームに戻る機能と、明示的なキャンセルボタンの両方を追加した。

# 関連Issue
Closes #775

# 動作確認の結果
- lintチェック（biome check）をパスすることを確認

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

---

Link to Devin run: https://app.devin.ai/sessions/31494be5fd754bb182ffcec0b6d792f7
Requested by: @nishio

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [レポートの再利用機能](https://github.com/digitaldemocracy2030/kouchou-ai/pull/769)

**作成者:** nishio  
**作成日:** 2026-01-26T07:34:36Z  
**変更:** +2575 -2298 (58ファイル)  
**内容:**


<img width="1145" height="509" alt="image" src="https://github.com/user-attachments/assets/f5db90e6-c554-435b-813e-e090627d673b" />


## Summary
- add detailed plan for report duplication/reuse with API/UI flow, reuse strategy, and rollout

## Testing
- not run (doc-only)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * 管理画面から既存レポートを複製し、アーティファクトを再利用できるワークフローを追加（複製状況の返却、競合時は409）。

* **UI**
  * レポートカードに「再利用/複製」アクションと複製ダイアログ、専用再利用ページを追加（新ID、タイトル、プロンプト、モデル/プロバイダ、クラスタ設定、再利用トグル）。

* **API**
  * 管理向け複製APIと複製元参照の追跡を導入。

* **Tests**
  * 単体・E2Eテストを追加し、複製フローとファイル処理を検証。

* **Documentation / Chores**
  * 複製計画文書を追加。開発コマンドをpnpmへ統一しE2E周りを安定化。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

