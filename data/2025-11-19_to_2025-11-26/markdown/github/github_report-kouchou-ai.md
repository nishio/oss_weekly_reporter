# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-11-19T12:29:59.335247+09:00 から 2025-11-26T12:29:59.335247+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (1件)

### [[BUG] Windows環境でインストールしようとすると文字化けが発生して中断する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/731)

**作成者:** Puni-Pon  
**作成日:** 2025-11-23T10:05:48Z  
**内容:**

### 概要

Windows環境でインストールしようとすると文字化けが発生して中断する

### 再現手順

1. 配布ファイルをダウンロード
2. Dockerを起動
3. setup_win.batを実行

### 期待する動作

APIを入力するとビルドがはじまり、管理画面にアクセスできるようになる

### スクリーンショット・ログ

```
kouchou-ai-3.0.0>echo Kouchou-AI Setup Tool
Kouchou-AI Setup Tool
kouchou-ai-3.0.0>echo =====================
=====================
kouchou-ai-3.0.0>REM Check if Docker Desktop is running
kouchou-ai-3.0.0>docker info  1>nul 2>&1
kouchou-ai-3.0.0>if 0 NEQ 0 (
echo Docker Desktop is not running.
 echo Please start Docker Desktop and try again.
 echo 豕ｨ諢・ Docker縺ｮ繧､繝ｳ繧ｹ繝医・繝ｫ逶ｴ蠕後・蜀崎ｵｷ蜍輔′蠢・ｦ√↑蝣ｴ蜷医′縺ゅｊ縺ｾ縺吶・
 pause
 exit /b
)
kouchou-ai-3.0.0>REM Enter OpenAI API key
kouchou-ai-3.0.0>echo OpenAI API繧ｭ繝ｼ繧貞・蜉帙＠縺ｦ縺上□縺輔＞縲・
OpenAI API繧ｭ繝ｼ繧貞・蜉帙＠縺ｦ縺上□縺輔＞縲・
kouchou-ai-3.0.0>∝承繧ｯ繝ｪ繝・け縺励※縲瑚ｲｼ繧贋ｻ倥￠縲阪ｒ驕ｸ謚槭＠縺ｦ縺上□縺輔＞縲・
'∝承繧ｯ繝ｪ繝・け縺励※縲瑚ｲｼ繧贋ｻ倥￠縲阪ｒ驕ｸ謚槭＠縺ｦ縺上□縺輔＞縲・' は、内部コマンドまたは外部コマンド、
操作可能なプログラムまたはバッチ ファイルとして認識されていません。
kouchou-ai-3.0.0>set /p OPENAI_API_KEY=Enter your OpenAI API key:
Enter your OpenAI API key:
```

APIキーを入力しても以下の表示になり強制終了

```
kouchou-ai-3.0.0>if 0 NEQ 0 (
echo 隴ｦ蜻・ 蜈･蜉帙＆繧後◆API繧ｭ繝ｼ縺ｮ蠖｢蠑上′豁｣縺励￥縺ｪ縺・庄閭ｽ諤ｧ縺後≠繧翫∪縺吶・
 ｼ縺ｯ縲茎k-縲阪〒蟋九∪繧翫∪縺吶・
 陦後＠縺ｾ縺吶°・・(Y/N
)

kouchou-ai-3.0.0>set /p CONTINUE=
```

### その他

WSL越しにsetup_linux.shを使って手順通りにセットアップすることで、Windows環境でも広聴aiの起動には成功しました。
ノンエンジニア向けにWindows環境でも使えるようにする、という目的を踏まえると、「setup_win.batを改修する」というアプローチのほかにも「WSLのインストールを促す」というアプローチも考えられるかなとは思います。

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (2件)

### [Bump glob from 10.4.5 to 10.5.0 in /client-static-build](https://github.com/digitaldemocracy2030/kouchou-ai/pull/730)

**作成者:** dependabot[bot]  
**作成日:** 2025-11-22T03:34:56Z  
**変更:** +3 -3 (1ファイル)  
**マージ日:** 2025-11-23T10:22:41Z  
**内容:**

Bumps [glob](https://github.com/isaacs/node-glob) from 10.4.5 to 10.5.0.
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/isaacs/node-glob/commit/56774ef73b495eb0b17cdd0f42921f5ef62297c1"><code>56774ef</code></a> 10.5.0</li>
<li><a href="https://github.com/isaacs/node-glob/commit/1e4e297342a09f2aa0ced87fcd4a70ddc325d75f"><code>1e4e297</code></a> bin: Do not expose filenames to shell expansion</li>
<li>See full diff in <a href="https://github.com/isaacs/node-glob/compare/v10.4.5...v10.5.0">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=glob&package-manager=npm_and_yarn&previous-version=10.4.5&new-version=10.5.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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

### [Bump glob from 10.4.5 to 10.5.0 in /client](https://github.com/digitaldemocracy2030/kouchou-ai/pull/729)

**作成者:** dependabot[bot]  
**作成日:** 2025-11-19T22:59:46Z  
**変更:** +3 -3 (1ファイル)  
**マージ日:** 2025-11-19T23:07:54Z  
**内容:**

Bumps [glob](https://github.com/isaacs/node-glob) from 10.4.5 to 10.5.0.
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/isaacs/node-glob/commit/56774ef73b495eb0b17cdd0f42921f5ef62297c1"><code>56774ef</code></a> 10.5.0</li>
<li><a href="https://github.com/isaacs/node-glob/commit/1e4e297342a09f2aa0ced87fcd4a70ddc325d75f"><code>1e4e297</code></a> bin: Do not expose filenames to shell expansion</li>
<li>See full diff in <a href="https://github.com/isaacs/node-glob/compare/v10.4.5...v10.5.0">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=glob&package-manager=npm_and_yarn&previous-version=10.4.5&new-version=10.5.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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

