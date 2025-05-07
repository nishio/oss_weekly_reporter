# GitHub レポート: digitaldemocracy2030/website

期間: 2025-04-30T16:23:05.312997+09:00 から 2025-05-07T16:23:05.312997+09:00 まで

## Issues

### 過去7日間に完了されたissue (4件)

### [[BUG] [2025/05/07] どのページに遷移しても空白ページになる](https://github.com/digitaldemocracy2030/website/issues/69)

**作成者:** masatosasano2  
**作成日:** 2025-05-07T04:33:36Z  
**内容:**

- 任意のページ遷移をすると空白ページになる（下記参考画像）
- 再読込すると正常に表示される
- 次のページ遷移でまた発生する
- 何度同じページを開いても再発するので、単純な静的リソースのブラウザキャッシュではなさそう
- Incognito Windowだと発生しないので、何らかのキャッシュではありそう
- Consoleには以下のエラーが出る

<img width="1370" alt="Image" src="https://github.com/user-attachments/assets/5f603106-692b-4ec0-9c3c-84293c2eee90" />

<img width="1662" alt="Image" src="https://github.com/user-attachments/assets/0d73bdcb-8d70-46b3-a117-715806ec6bb1" />

**コメント:** なし

---

### [PRプレビューデプロイメントの実装](https://github.com/digitaldemocracy2030/website/issues/50)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-29T04:58:57Z  
**内容:**

# PRプレビューデプロイメントの実装

## 概要
PRが作成された時に自動的にプレビュー環境をデプロイする機能を実装します。これにより、コードレビューの際に実際の動作を確認することができ、開発効率が向上します。

## 現状
- 現在のウェブサイトはNext.js 15.3.1を使用
- GitHub Pagesを使用して本番環境にデプロイ
- 静的エクスポート（`./out`ディレクトリに出力）
- GitHub Actionsワークフロー（nextjs.yml）がmainブランチへのプッシュ時にビルドとデプロイを実行

## 実装方針
GitHub Pagesと既存のGitHub Actionsワークフローを活用し、PRごとにプレビュー環境を自動的にデプロイします。

### 実装手順

1. 新しいGitHub Actionsワークフローファイル（`.github/workflows/pr-preview.yml`）を作成

```yaml
name: PR Preview Deployment

on:
  pull_request:
    types: [opened, synchronize, reopened]

permissions:
  contents: read
  pages: write
  id-token: write
  pull-requests: write

jobs:
  build-preview:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      
      # 本番環境と同じセットアップ
      - name: Detect package manager
        id: detect-package-manager
        run: |
          if [ -f "${{ github.workspace }}/yarn.lock" ]; then
            echo "manager=yarn" >> $GITHUB_OUTPUT
            echo "command=install" >> $GITHUB_OUTPUT
            echo "runner=yarn" >> $GITHUB_OUTPUT
            exit 0
          elif [ -f "${{ github.workspace }}/package.json" ]; then
            echo "manager=npm" >> $GITHUB_OUTPUT
            echo "command=ci" >> $GITHUB_OUTPUT
            echo "runner=npx --no-install" >> $GITHUB_OUTPUT
            exit 0
          else
            echo "Unable to determine package manager"
            exit 1
          fi
      
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: ${{ steps.detect-package-manager.outputs.manager }}
      
      - name: Setup Pages
        uses: actions/configure-pages@v5
        with:
          static_site_generator: next
      
      - name: Install dependencies
        run: ${{ steps.detect-package-manager.outputs.manager }} ${{ steps.detect-package-manager.outputs.command }}
      
      - name: Build with Next.js
        run: ${{ steps.detect-package-manager.outputs.runner }} next build
      
      # PRごとのサブディレクトリにデプロイ
      - name: Deploy PR Preview
        uses: rossjrw/pr-preview-action@v1
        with:
          source-dir: ./out
          preview-branch: gh-pages
          umbrella-dir: pr-preview
      
      # PRにプレビューURLをコメント
      - name: Comment PR
        uses: actions/github-script@v6
        with:
          script: |
            const prNumber = context.issue.number;
            const previewUrl = `https://digitaldemocracy2030.github.io/website/pr-preview/pr-${prNumber}/`;
            github.rest.issues.createComment({
              issue_number: prNumber,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `📝 プレビューデプロイが完了しました！ \n\n[プレビューを表示](${previewUrl})`
            });
```

## メリット
- 既存のGitHub Pages設定とシームレスに統合
- 無料（GitHub提供のランナーを使用）
- 外部サービスが不要
- デプロイプロセスを完全にコントロール可能
- 既存のGitHub Actionsワークフローを活用

## 注意点
- 古いプレビューの手動クリーンアップが必要になる場合がある
- 無料枠では同時ビルド数に制限がある

## 代替案
- Vercel統合：Next.jsに最適だが、本番環境もVercelに移行する必要がある
- Netlify統合：シンプルなセットアップだが、本番環境もNetlifyに移行する必要がある
- Cloudflare Pages：無制限の無料枠があるが、本番環境もCloudflare Pagesに移行する必要がある

## 次のステップ
1. PR-Previewワークフローファイルの作成
2. 権限設定の確認
3. テストPRでの動作確認
4. ドキュメントの更新


**コメント:** なし

---

### [アクティビティページのコンテンツ整理：「プロジェクトの歴史」](https://github.com/digitaldemocracy2030/website/issues/30)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-23T10:26:41Z  
**内容:**

# アクティビティページのコンテンツ整理：「プロジェクトの歴史」

## 概要
[アクティビティページ](https://dd2030.org/activity)のコンテンツを「プロジェクトの歴史」として週ごとに整理する提案です。

## 提案内容
- コンテンツを「プロジェクトの歴史」として再構成
- 週ごとにアクティビティをまとめて表示
- 時系列で活動を追跡しやすい構造に変更
- 各週の重要なマイルストーンをハイライト

## 期待される効果
- プロジェクトの進捗が時系列で理解しやすくなる
- 活動の流れが視覚的に把握しやすくなる
- 過去の活動を参照しやすくなる

## 参考
Slackチャンネル #2_開発_デジ民ウェブサイト での議論に基づいています。


**コメント:** なし

---

### [アクティビティページ(dd2030.org/activity)の改善](https://github.com/digitaldemocracy2030/website/issues/28)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-23T09:52:00Z  
**内容:**

# アクティビティページの改善提案

## 概要
[アクティビティページ](https://dd2030.org/activity)の見た目と機能性を改善するための提案です。このページはプロジェクトの活動を表示する重要なセクションですが、いくつかの改善点があります。

## 提案内容

### 1. ページデザインの改善
- 全体的な見た目の改善
- より見やすく、使いやすいレイアウトへの変更

### 2. コンテンツの整理
- 「プロジェクトの歴史」として週ごとにコンテンツをまとめる
- 時系列で活動を追跡しやすくする

### 3. ナビゲーションの強化
- アクティビティページへの動線を強化
- サイト内の他のセクションからのアクセスを改善

### 4. プロジェクトレポートへのリンク
- 各プロジェクトの最新レポートに直接飛べるURLを作成
- 各プロジェクトの説明ページからこれらのリンクを追加

### 5. クレジット表示
- ページのどこかに「powered by [oss_weekly_reporter](https://github.com/nishio/oss_weekly_reporter)」の表示を追加
- AI/LLM関連のキーワードを含めることを検討

## 期待される効果
- ユーザーがプロジェクトの活動を把握しやすくなる
- プロジェクト間の関連性が明確になる
- 活動の時系列的な流れが理解しやすくなる
- 他のプロジェクトにはない特徴として、活動の透明性をアピールできる

## 参考
Slackチャンネル #2_開発_デジ民ウェブサイト での議論に基づいています。


**コメント:** なし

---

### 過去7日間に作成されたissue (1件)

### [[FEATURE]デモサイトへのリンクがほしい](https://github.com/digitaldemocracy2030/website/issues/66)

**作成者:** masatosasano2  
**作成日:** 2025-05-01T01:28:58Z  
**内容:**

実際に動いているサイトを見たい。そうでないとイメージが湧きづらい
例：
- 広聴AI https://kouchou-ai.dd2030.org/
- いどばたビジョン https://idobata-demo.dd2030.org/
- いどばた政策立案 https://delib.takahiroanno.com/ ？
- Polimoney https://polimoney.dd2030.org/

相談ポイント：
- とはいえ上の例は対外向けのデモサイトではなく開発環境なので、適切でないかもしれない
- 画面キャプチャや動画でもいいかもしれない

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(1件)

### [紹介する事例案](https://github.com/digitaldemocracy2030/website/issues/4)

**作成者:** nishio  
**作成日:** 2025-03-26T16:05:23Z  
**内容:**

デジタル民主主義2030の広聴AIを試してみた！政治家目線での期待と感触｜ほづみゆうき@中央区議会議員
https://note.com/yukihoz/n/n06360c9a17fd

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (15件)

### [lintエラー修正](https://github.com/digitaldemocracy2030/website/pull/72)

**作成者:** moai-redcap  
**作成日:** 2025-05-07T07:14:03Z  
**変更:** +4 -6 (1ファイル)  
**マージ日:** 2025-05-07T07:16:25Z  
**内容:**

内容なし

**コメント:** なし

---

### [貢献者向けガイドラインを追加](https://github.com/digitaldemocracy2030/website/pull/71)

**作成者:** kojino  
**作成日:** 2025-05-07T07:01:14Z  
**変更:** +78 -0 (3ファイル)  
**マージ日:** 2025-05-07T07:04:44Z  
**内容:**

内容なし

**コメント:** なし

---

### [next.configが複数ファイルあったので削除](https://github.com/digitaldemocracy2030/website/pull/70)

**作成者:** moai-redcap  
**作成日:** 2025-05-07T05:07:49Z  
**変更:** +0 -2 (2ファイル)  
**マージ日:** 2025-05-07T05:09:37Z  
**内容:**

内容なし

**コメント:** なし

---

### [Markdown.tsxを修正 buildエラー修正](https://github.com/digitaldemocracy2030/website/pull/68)

**作成者:** moai-redcap  
**作成日:** 2025-05-07T03:48:38Z  
**変更:** +12 -12 (1ファイル)  
**マージ日:** 2025-05-07T03:49:01Z  
**内容:**

内容なし

**コメント:** なし

---

### [ボードメンバーを更新](https://github.com/digitaldemocracy2030/website/pull/67)

**作成者:** kojino  
**作成日:** 2025-05-07T02:49:56Z  
**変更:** +99 -6 (12ファイル)  
**マージ日:** 2025-05-07T03:29:24Z  
**内容:**

内容なし

**コメント:** なし

---

### [サイドメニューの活動履歴のリンクを /activity から /history に変更](https://github.com/digitaldemocracy2030/website/pull/65)

**作成者:** masatosasano2  
**作成日:** 2025-04-30T17:49:50Z  
**変更:** +3 -3 (2ファイル)  
**マージ日:** 2025-05-05T08:47:30Z  
**内容:**

関連Issue：#9

**コメント:** なし

---

### [Fix PR preview deployment 404 error](https://github.com/digitaldemocracy2030/website/pull/64)

**作成者:** NISHIO Hirokazu+Devin  
**作成日:** 2025-04-30T16:37:00Z  
**変更:** +4 -0 (2ファイル)  
**マージ日:** 2025-04-30T16:58:12Z  
**内容:**

# PR preview deployment の404エラーを修正

## 問題
PRプレビューデプロイのリンクが `http://dd2030.org/pr-preview/pr-[PR番号]/` として生成されていますが、実際のファイルはルートディレクトリにデプロイされているため404エラーが発生していました。

## 解決策
1. PRプレビュー用にNext.jsの `basePath` を条件付きで設定しました
2. GitHub Actionsワークフローで環境変数 `NEXT_PUBLIC_PR_NUMBER` を設定するようにしました

これにより、PRプレビュー時にはすべてのリソースが `/pr-preview/pr-[PR番号]/` パスからロードされるようになり、プレビューリンクが正しく機能するようになります。

Link to Devin run: https://app.devin.ai/sessions/f2a16214fd36458c8d5a7664e1b96f13
Requested by: NISHIO Hirokazu (nishio.hirokazu@gmail.com)


**コメント:** なし

---

### [add history page](https://github.com/digitaldemocracy2030/website/pull/63)

**作成者:** nishio  
**作成日:** 2025-04-30T16:19:27Z  
**変更:** +288 -0 (2ファイル)  
**マージ日:** 2025-04-30T16:19:40Z  
**内容:**

内容なし

**コメント:** なし

---

### [宇多津町のリンクを外部リンクスタイルに変更](https://github.com/digitaldemocracy2030/website/pull/62)

**作成者:** NISHIO Hirokazu+Devin  
**作成日:** 2025-04-30T16:15:11Z  
**変更:** +14 -1 (1ファイル)  
**マージ日:** 2025-04-30T16:34:38Z  
**内容:**

# 宇多津町のリンクを外部リンクスタイルに変更

宇多津町の事例ページにあるリンクをインラインリンクから明確な外部リンクボタンに変更しました。これにより、リンクがより視覚的に識別しやすくなります。

変更内容：
- インラインの `<a>` タグを外部リンクを示すスタイルのボタンに変更
- NavigateNextIcon を追加して外部リンクであることを明示
- リンクテキストを「宇多津町」から「AIで多くの住民の意見を政策立案に反映する『ブロードリスニング』の先進的なトライアルを実施しました（宇多津町の公式サイト）」に変更してより明確に

Link to Devin run: https://app.devin.ai/sessions/0c766650dea0472f815af9d27e9cb944
Requested by: NISHIO Hirokazu


**コメント:** なし

---

### [add week7](https://github.com/digitaldemocracy2030/website/pull/61)

**作成者:** nishio  
**作成日:** 2025-04-30T16:05:43Z  
**変更:** +421 -0 (5ファイル)  
**マージ日:** 2025-04-30T16:08:10Z  
**内容:**

内容なし

**コメント:** なし

---

### [宇多津町の事例にリンクを追加](https://github.com/digitaldemocracy2030/website/pull/60)

**作成者:** NISHIO Hirokazu+Devin  
**作成日:** 2025-04-30T10:39:30Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-04-30T10:53:58Z  
**内容:**

# 宇多津町の事例にリンクを追加

宇多津町の事例紹介に、元の情報源へのリンクを追加しました。

参考URL: https://www.town.utazu.lg.jp/page/4114.html

Link to Devin run: https://app.devin.ai/sessions/10542d74a949498abe86f10164df3d86
Requested by: NISHIO Hirokazu (nishio.hirokazu@gmail.com)


**コメント:** なし

---

### [Fix merge conflicts in PR #52](https://github.com/digitaldemocracy2030/website/pull/59)

**作成者:** 小野翔太（モアイ）+Devin  
**作成日:** 2025-04-30T09:45:42Z  
**変更:** +42 -43 (6ファイル)  
**マージ日:** 2025-04-30T10:18:13Z  
**内容:**

# Fix merge conflicts in PR #52

This PR resolves the merge conflicts in PR #52 by:

- Keeping the main branch's file structure with `[[...slug]]` for docs pages
- Removing conflicting files that are no longer needed
- Preserving the PR preview deployment workflow changes

Once this PR is merged into the PR #52 branch, PR #52 can be merged into main without conflicts.


**コメント:** なし

---

### [宇多津町のブロードリスニング事例を追加](https://github.com/digitaldemocracy2030/website/pull/58)

**作成者:** NISHIO Hirokazu+Devin  
**作成日:** 2025-04-30T03:25:49Z  
**変更:** +4 -0 (1ファイル)  
**マージ日:** 2025-04-30T10:21:28Z  
**内容:**

# 宇多津町の事例紹介を追加

宇多津町が実施した「ブロードリスニング」の事例を広聴AIの活用事例として追加しました。

参考URL: https://www.town.utazu.lg.jp/page/4114.html

Link to Devin run: https://app.devin.ai/sessions/10542d74a949498abe86f10164df3d86
Requested by: NISHIO Hirokazu (nishio.hirokazu@gmail.com)


**コメント:** なし

---

### [広聴AI v2.0.0リリースページにコントリビューターリストを追加](https://github.com/digitaldemocracy2030/website/pull/57)

**作成者:** NISHIO Hirokazu+Devin  
**作成日:** 2025-04-30T00:30:24Z  
**変更:** +19 -0 (1ファイル)  
**マージ日:** 2025-04-30T00:48:49Z  
**内容:**

# 広聴AI v2.0.0リリースページにコントリビューターリストを追加

## 変更内容
- 広聴AI v2.0.0リリースページの末尾にコントリビューターリストを追加しました
- 各コントリビューターのGitHubプロフィールへのリンクを設定しました
- dependabotとdevin-ai-integrationは除外しました
- コントリビューターリストはアルファベット順にソートしました

## 背景
いしばしさんからの提案で、プレスリリースにコントリビューターの名前を入れることでエンジニアのキャリアにプラスになり、参加するモチベーションになるとのことでした。

Link to Devin run: https://app.devin.ai/sessions/07dea2a8c80645f39c129785a1481c19
Requested by: NISHIO Hirokazu (nishio.hirokazu@gmail.com)


**コメント:** なし

---

### [PRプレビューデプロイメントの実装](https://github.com/digitaldemocracy2030/website/pull/52)

**作成者:** NISHIO Hirokazu+Devin  
**作成日:** 2025-04-29T05:07:01Z  
**変更:** +296 -199 (9ファイル)  
**マージ日:** 2025-04-30T10:20:33Z  
**内容:**

# PRプレビューデプロイメントの実装

## 概要
PRが作成された時に自動的にプレビュー環境をデプロイする機能を実装しました。これにより、コードレビューの際に実際の動作を確認することができ、開発効率が向上します。

## 変更内容
- `.github/workflows/pr-preview.yml` ファイルを追加
- PR作成・更新時に自動的にプレビュー環境をデプロイするワークフローを設定
- PRコメント欄にプレビューURLを自動的に追加する機能を実装

## 動作確認
- このPRがマージされた後、次のPRから自動的にプレビュー環境がデプロイされます

## 関連Issue
Fixes #50

Link to Devin run: https://app.devin.ai/sessions/779250f9742041dabc0d395bf370202f
Requested by: NISHIO Hirokazu (nishio.hirokazu@gmail.com)


**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

