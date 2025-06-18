# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-06-11T12:29:06.482635+09:00 から 2025-06-18T12:29:06.482635+09:00 まで

## Issues

### 過去7日間に完了されたissue (2件)

### [サンキー図のコピー機能](https://github.com/digitaldemocracy2030/polimoney/issues/124)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-06-10T20:48:45Z  
**内容:**

## 解決・改善したいこと

サンキー図をコピーできるようにすることで資料として用いることが可能になる。

シェア機能の一環としてあったらいいのではないかなと思いました。

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

BoardSummaryの部分を丸ごと画像として保存できるようにする。

**コメント:** なし

---

### [シェアボタンの実装](https://github.com/digitaldemocracy2030/polimoney/issues/103)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-05-29T14:23:06Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->
任意の閲覧者が各政治家の収支の流れをSNSでシェアーできるようにする。
アクティブな参加を促す。
polimoneyの周知、関心を持ってもらえる。
<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->
polimoney ver1.0 -> 短期のマイルストーン -> シェアボタン
## 具体的な実現方法・実装方法の概要（未記入でも構いません）
各政治家の個人のページにシェアボタンを作る。
イメージはデジタル民主主義2030のウェブサイトにあるシェアボタンのような感じ。
X, LINE, Facebook, Instagramなどでシェアー。また、リンクもコピーできるようにする。
(サンキー図の画像をコピーする機能があってもいいかも？)
<br></br>

<ジャストアイデア>
いいねボタン、ページ閲覧数などが見れても面白いかも？


**コメント:** なし

---

### 過去7日間に作成されたissue (3件)

### [[シェア機能]タイトルとサムネイルを変更する](https://github.com/digitaldemocracy2030/polimoney/issues/134)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-06-12T07:50:04Z  
**内容:**

## 解決・改善したいこと

シェアした時に表示されるタイトルとサムネイルの画像がそのページの政治家さんの名前と顔写真の方がいいのではないか。

イメージはspotifyやapple musicのスタイルかなと思われます。


## 具体的な実現方法・実装方法の概要（未記入でも構いません）
今はハードコーディングしているのでDBが整ってからでも

AsIs
タイトル："Polimoney"
サムネイル：Polimoneyのデフォルト画像

ToBe
タイトル：{政治家さんの名前} + "Polimoney"
サムネイル：{政治家さんの顔写真}

**コメント:** なし

---

### [渉外時の承諾確認リストを作成](https://github.com/digitaldemocracy2030/polimoney/issues/131)

**作成者:** Nozomi-M21  
**作成日:** 2025-06-11T12:44:20Z  
**内容:**

渉外時の確認項目をクリアにし、渉外フローに組み込む
【確認項目】

1. データいただく＞非公開確認＞公開の流れでよいか？
2. 事例として紹介してよいか？（website、note、SNS）
3. ユーザーインタビューしてよいか？（これはオプション的に聞く）

[営業資料に追加](https://docs.google.com/presentation/d/1d5OqyfjVNiQCokVXgEdy9K1RTlEExyQUWOeEFXVl2UM/edit?usp=sharing)

**コメント:** なし

---

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

### 過去7日間に更新されたissue（作成・クローズを除く）(1件)

### [準備中の「Coming Soon..」パネルをUIに追加](https://github.com/digitaldemocracy2030/polimoney/issues/102)

**作成者:** Nozomi-M21  
**作成日:** 2025-05-28T13:15:27Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->
準備中の人数分「Coming Soon..」パネルを足したらユーザーの期待値が高まりそう

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）
テスト太郎の横にパネルを追加

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (6件)

### [コピー機能がモバイル画面で表示されないように修正](https://github.com/digitaldemocracy2030/polimoney/pull/133)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-06-12T07:32:02Z  
**変更:** +8 -4 (2ファイル)  
**マージ日:** 2025-06-12T07:46:04Z  
**内容:**

# 変更の概要
モバイル画面では表示されないように修正しました

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
iphoneで画像コピーを試みましたが失敗しました。
モバイル画面ではサンキー図がスクロール表示されているため画像コピーしても途中で途切れてしまいました。

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **スタイル**
  - コピー画像ボタンが小さい画面サイズでは非表示になり、中〜大画面サイズでのみ表示されるようになりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [#125 サンキー図のコピー機能 の conflict 解決版](https://github.com/digitaldemocracy2030/polimoney/pull/132)

**作成者:** dotneet  
**作成日:** 2025-06-11T23:48:15Z  
**変更:** +1431 -844 (3ファイル)  
**マージ日:** 2025-06-11T23:53:30Z  
**内容:**

#125 を参照してください

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - サマリーセクション全体を画像としてクリップボードにコピーできるボタンを追加しました。

- **依存関係の更新**
  - 新しいパッケージ（@chakra-ui/icons、@emotion/styled、framer-motion、html2canvas）を追加し、既存パッケージ（@chakra-ui/react）をアップデートしました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Bump requests from 2.32.3 to 2.32.4 in /tools](https://github.com/digitaldemocracy2030/polimoney/pull/130)

**作成者:** dependabot[bot]  
**作成日:** 2025-06-11T10:46:52Z  
**変更:** +11 -11 (2ファイル)  
**マージ日:** 2025-06-11T10:55:52Z  
**内容:**

Bumps [requests](https://github.com/psf/requests) from 2.32.3 to 2.32.4.
<details>
<summary>Release notes</summary>
<p><em>Sourced from <a href="https://github.com/psf/requests/releases">requests's releases</a>.</em></p>
<blockquote>
<h2>v2.32.4</h2>
<h2>2.32.4 (2025-06-10)</h2>
<p><strong>Security</strong></p>
<ul>
<li>CVE-2024-47081 Fixed an issue where a maliciously crafted URL and trusted
environment will retrieve credentials for the wrong hostname/machine from a
netrc file. (<a href="https://redirect.github.com/psf/requests/issues/6965">#6965</a>)</li>
</ul>
<p><strong>Improvements</strong></p>
<ul>
<li>Numerous documentation improvements</li>
</ul>
<p><strong>Deprecations</strong></p>
<ul>
<li>Added support for pypy 3.11 for Linux and macOS. (<a href="https://redirect.github.com/psf/requests/issues/6926">#6926</a>)</li>
<li>Dropped support for pypy 3.9 following its end of support. (<a href="https://redirect.github.com/psf/requests/issues/6926">#6926</a>)</li>
</ul>
</blockquote>
</details>
<details>
<summary>Changelog</summary>
<p><em>Sourced from <a href="https://github.com/psf/requests/blob/main/HISTORY.md">requests's changelog</a>.</em></p>
<blockquote>
<h2>2.32.4 (2025-06-10)</h2>
<p><strong>Security</strong></p>
<ul>
<li>CVE-2024-47081 Fixed an issue where a maliciously crafted URL and trusted
environment will retrieve credentials for the wrong hostname/machine from a
netrc file.</li>
</ul>
<p><strong>Improvements</strong></p>
<ul>
<li>Numerous documentation improvements</li>
</ul>
<p><strong>Deprecations</strong></p>
<ul>
<li>Added support for pypy 3.11 for Linux and macOS.</li>
<li>Dropped support for pypy 3.9 following its end of support.</li>
</ul>
</blockquote>
</details>
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/psf/requests/commit/021dc729f0b71a3030cefdbec7fb57a0e80a6cfd"><code>021dc72</code></a> Polish up release tooling for last manual release</li>
<li><a href="https://github.com/psf/requests/commit/821770e822a20a21b207b3907ea83878bda1d396"><code>821770e</code></a> Bump version and add release notes for v2.32.4</li>
<li><a href="https://github.com/psf/requests/commit/59f8aa2adf1d3d06bcbf7ce6b13743a1639a5401"><code>59f8aa2</code></a> Add netrc file search information to authentication documentation (<a href="https://redirect.github.com/psf/requests/issues/6876">#6876</a>)</li>
<li><a href="https://github.com/psf/requests/commit/5b4b64c3467fd7a3c03f91ee641aaa348b6bed3b"><code>5b4b64c</code></a> Add more tests to prevent regression of CVE 2024 47081</li>
<li><a href="https://github.com/psf/requests/commit/7bc45877a86192af77645e156eb3744f95b47dae"><code>7bc4587</code></a> Add new test to check netrc auth leak (<a href="https://redirect.github.com/psf/requests/issues/6962">#6962</a>)</li>
<li><a href="https://github.com/psf/requests/commit/96ba401c1296ab1dda74a2365ef36d88f7d144ef"><code>96ba401</code></a> Only use hostname to do netrc lookup instead of netloc</li>
<li><a href="https://github.com/psf/requests/commit/7341690e842a23cf18ded0abd9229765fa88c4e2"><code>7341690</code></a> Merge pull request <a href="https://redirect.github.com/psf/requests/issues/6951">#6951</a> from tswast/patch-1</li>
<li><a href="https://github.com/psf/requests/commit/6716d7c9f29df636643fa2489f98890216525cb0"><code>6716d7c</code></a> remove links</li>
<li><a href="https://github.com/psf/requests/commit/a7e1c745dc23c18e836febd672416ed0c5d8d8ae"><code>a7e1c74</code></a> Update docs/conf.py</li>
<li><a href="https://github.com/psf/requests/commit/c799b8167a13416833ad3b4f3298261a477e826f"><code>c799b81</code></a> docs: fix dead links to kenreitz.org</li>
<li>Additional commits viewable in <a href="https://github.com/psf/requests/compare/v2.32.3...v2.32.4">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=requests&package-manager=pip&previous-version=2.32.3&new-version=2.32.4)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **Chores**
  - `requests`パッケージのバージョン指定を`2.32.3`から`2.32.4`に更新しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Manual](https://github.com/digitaldemocracy2030/polimoney/pull/128)

**作成者:** shumizu418128  
**作成日:** 2025-06-11T02:22:45Z  
**変更:** +238 -4 (2ファイル)  
**マージ日:** 2025-06-11T02:23:14Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
仮設ページ作成マニュアル

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **ドキュメント**
  - 政治家の財務報告デモページ作成手順の詳細マニュアルを追加しました。データ準備、ファイル作成、出力確認、データ構造、命名規則、型安全性、トラブルシューティングなどを解説しています。

- **スタイル**
  - 政治家プロフィールデータの文字列プロパティから不要なコメント記号を削除しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [openaiとanthropicをサポート](https://github.com/digitaldemocracy2030/polimoney/pull/127)

**作成者:** dotneet  
**作成日:** 2025-06-11T01:13:26Z  
**変更:** +1939 -483 (16ファイル)  
**マージ日:** 2025-06-11T04:37:53Z  
**内容:**

# 変更の概要

 - langchainを導入し、openaiとanthropicのモデルでもOCRが動作するようにした
 - googleのライブラリに基づいた処理は削除
 - ファイル名を analyze_image_gemini.py から analyze_image.py に変更

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

 - gemini以外のモデルの実験が困難であったため

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - LangChainベースのLLMクライアントを導入し、Google Gemini APIに加えてAnthropicやOpenAIのプロバイダーもサポート。
  - コマンドラインでLLMプロバイダーの選択や既存出力スキップが可能に。
  - LLMプロバイダー用の設定管理やテストスクリプトを追加。

- **ドキュメント**
  - 画像解析ツールや関連スクリプトの説明を「Google Gemini API」から「LangChain」や「vLLM」へ更新。
  - 使用方法やプロジェクト構成の記述を新しい仕組みに合わせて修正。

- **リファクタ**
  - Gemini専用実装を汎用LLMクライアントに置き換え、依存性注入やエラー処理を改善。
  - インターフェースやクラス構成の見直しにより拡張性を向上。

- **その他**
  - プロジェクト名や依存パッケージをLLMベースに変更。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [シェアボタンの実装](https://github.com/digitaldemocracy2030/polimoney/pull/126)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-06-10T21:40:06Z  
**変更:** +244 -20 (4ファイル)  
**マージ日:** 2025-06-11T12:42:30Z  
**内容:**

# 変更の概要
シェアボタンを実装しました

# スクリーンショット
-変更後
![スクリーンショット 2025-06-11 5 57 41（2）](https://github.com/user-attachments/assets/20253618-b65a-481a-8fa3-62314fd59a96)
![スクリーンショット 2025-06-11 5 57 49（2）](https://github.com/user-attachments/assets/a1b8f8f9-9ebc-42a4-a8ec-c4fe8e2a015e)
![スクリーンショット 2025-06-11 5 57 52（2）](https://github.com/user-attachments/assets/ac383fea-607c-4c14-b023-24df7872c731)



# 変更の背景
シェアボタンがあることでビューワー(市民)の能動的な参加につながる。ユーザー(政治家)もより見られている意識が高まる。
polimoneyの認知度向上にもつながる。

# 関連Issue
[シェアボタンの実装#103](https://github.com/digitaldemocracy2030/polimoney/issues/103)

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - ページ上にSNS共有パネルを追加し、LINE・Facebook・X（Twitter）でのシェアやURLコピーが可能になりました。

- **依存関係の変更**
  - SNS共有機能のための新しいライブラリを追加しました。
  - Reactのバージョンをダウングレードしました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [サンキー図のコピー機能](https://github.com/digitaldemocracy2030/polimoney/pull/125)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-06-10T21:18:00Z  
**変更:** +1460 -866 (3ファイル)  
**内容:**

# 変更の概要
サンキー図をコピーできる機能を実装しました。

# スクリーンショット
-変更後
![スクリーンショット 2025-06-11 6 06 43（2）](https://github.com/user-attachments/assets/cdeccd0d-3e99-47f9-9c54-f4fd9a7264c7)
![スクリーンショット 2025-06-11 6 06 48（2）](https://github.com/user-attachments/assets/896ac15e-727d-4390-9466-6d7475669352)
-googleドキュメントに添付した例
![スクリーンショット 2025-06-11 6 07 18（2）](https://github.com/user-attachments/assets/a13f95dc-c9ff-4b81-85e7-6d7c9818e4f1)


# 変更の背景
シェアする際にページのリンクを共有するだけでなくて、サンキー図そのものを資料として使いたい需要があると思ったので作成しました。

# 関連Issue
[サンキー図のコピー機能 #124](https://github.com/digitaldemocracy2030/polimoney/issues/124)

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - サマリーセクションを画像としてクリップボードにコピーできるボタンを追加しました。コピー成功時には確認メッセージが表示されます。

- **その他**
  - 必要な依存パッケージの追加およびバージョン更新を行いました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

