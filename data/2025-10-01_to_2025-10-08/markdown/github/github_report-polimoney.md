# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-10-01T12:17:56.079683+09:00 から 2025-10-08T12:17:56.079683+09:00 まで

## Issues

### 過去7日間に完了されたissue (1件)

### [資金項目データ定義方法の統一](https://github.com/digitaldemocracy2030/polimoney/issues/199)

**作成者:** grassfieldk  
**作成日:** 2025-09-14T15:07:26Z  
**内容:**

## 解決・改善したいこと

データ定義ファイル（`data/demo-*.ts`）間でデータ構造がばらばらになっているため、統一する

**現在の問題点：**
- `getDataByYear`関数の実装方法が各ファイルで異なる（シンプルな実装 vs 複雑なフォールバック機能付き）
- `demo-comingsoon.ts`では`getDataByYear`関数が存在しない
- 関数定義方法が混在（arrow function vs function declaration）
- 型定義が異なる（`Profile` vs `ProfileList`）
- 一部ファイルのみに追加機能（`getDataByPath`）が存在


## 具体的な実現方法・実装方法の概要

1. **`getDataByYear`関数の統一**
   - 全ファイルで同じ実装パターンに統一
   - `demo-comingsoon.ts`に不足している`getDataByYear`関数を追加

2. **関数定義方法の統一**
   - arrow function または function declaration のどちらかに統一

3. **型定義の統一**
   - `Profile`型で統一（`ProfileList`の使用を見直し）

4. **追加機能の取扱い**
   - `getDataByPath`のような追加機能の必要性を検討し、必要であれば全ファイルに実装

5. **テンプレートまたはスキーマの作成**
   - 新しいデータファイル作成時のガイドライン策定

## 関連 Issue

- blocks #197 

**コメント:** なし

---

### 過去7日間に作成されたissue (0件)

### 過去7日間に更新されたissue（作成・クローズを除く）(2件)

### [サンキー図・一覧表のデータを統一](https://github.com/digitaldemocracy2030/polimoney/issues/197)

**作成者:** grassfieldk  
**作成日:** 2025-09-12T07:37:15Z  
**内容:**

## 解決・改善したいこと

各議員ページに表示する資金項目データのフォーマット統一を図りたい

サンキー図用に Flow / Transaction の２つのデータ型が存在しているため、これを統合したい


## Flow と Transaction の関係

Flow: サンキー図用のデータ、カテゴリごとの合計値
Transaction: 収支一覧用のデータ、各項目の詳細

Flow は Transaction から生成可能
ページ表示時に生成してもよいが、プレ生成しているのが現状

### 整合性要件

- Transaction の category ごとに Flow が存在すること（総収入は除く）
- Flow と同じ category を持つ Transaction[].amount 合計値が Flow.value になっていること


## 対応方針

下記に示す通り現状不整合が起きているが、あくまででもデータのため問題ではない
ただ Flow は動的生成できるため Transaction さえあればよく、生成処理の負荷も非常に低いはず
また今後 RDB などを使えばビューなどで処理を DB に任せることも可能
※ ただし Flow にはカテゴリの親子関係も記録されているため、これについては別途定義が必要

よって、サンキー図のデータは整合性が確実に担保される動的生成に変更する

## 現状

現在定義されているデータに不整合あり
※ チェック用スクリプトで確認

<details>
<summary>不整合の詳細</summary>

```plaintext
[demo-comingsoon.ts] OK
[demo-example.ts] category='寄附' の Flow が存在しません
[demo-example.ts] Flow.name='個人からの寄附' に対応する Transaction がありません
[demo-example.ts] Flow.name='総収入' に対応する Transaction がありません
[demo-example.ts] Flow.name='翌年への繰越額' に対応する Transaction がありません
[demo-example.ts] Flow.name='人件費' に対応する Transaction がありません
[demo-kokifujisaki.ts] category='前年繰越' の Flow が存在しません
[demo-kokifujisaki.ts] category='党費・会費' の Flow が存在しません
[demo-kokifujisaki.ts] category='交付金' の Flow が存在しません
[demo-kokifujisaki.ts] Flow.name='前年からの繰越額' に対応する Transaction がありません
[demo-kokifujisaki.ts] Flow.name='本年の収入額' に対応する Transaction がありません
[demo-kokifujisaki.ts] Flow.name='個人の負担する党費又は会費' に対応する Transaction がありません
[demo-kokifujisaki.ts] Flow.name='本部又は支部から供与された交付金' に対応する Transaction がありません
[demo-kokifujisaki.ts] Flow.name='総収入' に対応する Transaction がありません
[demo-kokifujisaki.ts] Flow.name='組織活動費' に対応する Transaction がありません
[demo-kokifujisaki.ts] Flow.name='翌年への繰越' に対応する Transaction がありません
[demo-ryosukeidei.ts] category='前年繰越' の Flow が存在しません
[demo-ryosukeidei.ts] category='党費・会費' の Flow が存在しません
[demo-ryosukeidei.ts] category='交付金' の Flow が存在しません
[demo-ryosukeidei.ts] category='その他収入' の Flow が存在しません
[demo-ryosukeidei.ts] category='政治活動費' の合計値不一致: Transaction合計=7723335, Flow.value=14575541
[demo-ryosukeidei.ts] Flow.name='前年からの繰越額' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='個人の負担する党費又は会費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='個人からの寄附' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='法人その他の団体からの寄附' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='政治団体からの寄附' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='本部又は支部から供与された交付金' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='その他の収入' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='本年の収入額' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='総収入' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='人件費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='光熱水費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='備品・消耗品費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='事務所費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='組織活動費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='選挙関係費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='宣伝事業費' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='寄附・交付金' に対応する Transaction がありません
[demo-ryosukeidei.ts] Flow.name='翌年への繰越' に対応する Transaction がありません
[demo-takahiroanno.ts] category='組織活動費' の Flow が存在しません
[demo-takahiroanno.ts] Flow.name='総収入' に対応する Transaction がありません
[demo-takahiroanno.ts] Flow.name='事務所費' に対応する Transaction がありません
[demo-takahiroanno.ts] Flow.name='宣伝事業費' に対応する Transaction がありません
[demo-takahiroanno.ts] Flow.name='政治活動費' に対応する Transaction がありません
[demo-takahiroanno.ts] Flow.name='翌年への繰越額' に対応する Transaction がありません
```
</details>


## 実装中に気づいた課題など

- カテゴリの親子関係が議員データによって異なる
- Transaction から読み取れない情報が Flows に記載されている


## 関連 Issue

- blocked by #199 
- blocks #166 
- relates to #32 

**コメント:** なし

---

### [テストを書く - backend](https://github.com/digitaldemocracy2030/polimoney/issues/159)

**作成者:** shumizu418128  
**作成日:** 2025-07-19T13:23:48Z  
**内容:**

## 解決・改善したいこと

<!-- この提案はどのようなものかを説明してください。また、どのような人がどのように嬉しい提案なのかを、できればユーザーを主語にして記載してください。 -->
backendフォルダはGoのサーバーです
テストコードを書きたいです

<!-- 対象画面の URL や関連する議論や資料の URL があれば、添付いただけると理解の助けになります。 -->

## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (3件)

### [chore(deps-dev): bump tar-fs from 3.0.9 to 3.1.1](https://github.com/digitaldemocracy2030/polimoney/pull/205)

**作成者:** dependabot[bot]  
**作成日:** 2025-10-04T08:31:32Z  
**変更:** +3 -3 (1ファイル)  
**マージ日:** 2025-10-04T08:33:12Z  
**内容:**

Bumps [tar-fs](https://github.com/mafintosh/tar-fs) from 3.0.9 to 3.1.1.
<details>
<summary>Commits</summary>
<ul>
<li><a href="https://github.com/mafintosh/tar-fs/commit/0aa57de79eb58a5206992c979a7fd5c4df85e07c"><code>0aa57de</code></a> 3.1.1</li>
<li><a href="https://github.com/mafintosh/tar-fs/commit/0bd54cdf06da2b7b5b95cd4b062c9f4e0a8c4e09"><code>0bd54cd</code></a> expand check</li>
<li><a href="https://github.com/mafintosh/tar-fs/commit/cb1c571fba8ec6dd56340f55dcd5d284372a8249"><code>cb1c571</code></a> 3.1.0</li>
<li><a href="https://github.com/mafintosh/tar-fs/commit/374460e9973a5ac5655b7f21a84dfa9b64da5d78"><code>374460e</code></a> add optional disablement of symlink validation (<a href="https://redirect.github.com/mafintosh/tar-fs/issues/119">#119</a>)</li>
<li><a href="https://github.com/mafintosh/tar-fs/commit/5bfe6dfb9d26436829ec6a6400eca3a030d4757a"><code>5bfe6df</code></a> 3.0.10</li>
<li><a href="https://github.com/mafintosh/tar-fs/commit/63e12f94740afa9ba87f91c1a530ad91548ba3a9"><code>63e12f9</code></a> bare support</li>
<li>See full diff in <a href="https://github.com/mafintosh/tar-fs/compare/v3.0.9...v3.1.1">compare view</a></li>
</ul>
</details>
<br />


[![Dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=tar-fs&package-manager=npm_and_yarn&previous-version=3.0.9&new-version=3.1.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

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

### [Docker イメージのバージョン設定を変更](https://github.com/digitaldemocracy2030/polimoney/pull/204)

**作成者:** grassfieldk  
**作成日:** 2025-10-03T16:13:34Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-10-03T16:55:38Z  
**内容:**

## 変更の概要

Docker イメージのベース OS を固定


## 変更の背景

`mcr.microsoft.com/devcontainers/javascript-node:20` はベース OS が複数あるため、
環境によっては apt リポジトリ変更による Python 環境構築エラーなどが発生する場合がある

本日開発コンテナを再構築したところ、
ベース OS が以前と変わっており、apt リポジトリも変更になった影響で Python のインストールに失敗した
OS を固定することで解消した


## CLAへの同意

本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- チョア
  - 開発用コンテナのベースOSを Bookworm 版に更新。パッケージ入手性とセキュリティ更新の追従性を改善。
  - 既存のセットアップ手順（Python/Poetry/npm/venv）は従来どおりの構成で継続し、再構築時の依存解決がより安定。
  - 将来的な開発ツールとの互換性向上を見込み。アプリの機能や挙動への影響はありません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [作業ファイルの削除](https://github.com/digitaldemocracy2030/polimoney/pull/203)

**作成者:** grassfieldk  
**作成日:** 2025-10-03T08:00:13Z  
**変更:** +0 -167 (2ファイル)  
**マージ日:** 2025-10-03T08:02:25Z  
**内容:**

## 変更の概要

誤ってコミットしてしまっていた作業用ファイルを削除


## CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- ドキュメント
  - 古くなった設計メモを削除し、情報を整理しました。
- チョア
  - 内部のデータ整合性チェック用スクリプトを削除し、メンテナンス性を向上しました。
- その他
  - ユーザー向け機能やUIの変更はありません。パフォーマンスや互換性への影響もありません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

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

