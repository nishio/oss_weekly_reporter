# GitHub レポート: digitaldemocracy2030/website

期間: 2025-04-23T18:03:38.729761+09:00 から 2025-04-30T18:03:38.729761+09:00 まで

## Issues

### 過去7日間に完了されたissue (5件)

### [Docsページの計画を建てる](https://github.com/digitaldemocracy2030/website/issues/41)

**作成者:** moai-redcap  
**作成日:** 2025-04-25T11:51:45Z  
**内容:**

- get start的なものは確実に入れたい
- FAQも確実に入れたい（中身は空でもマークダウンで追加できるように）

**コメント:** なし

---

### [いどばたの活用事例ページへのリンクを貼る](https://github.com/digitaldemocracy2030/website/issues/39)

**作成者:** moai-redcap  
**作成日:** 2025-04-25T08:56:20Z  
**内容:**

いどばたのページから
https://dd2030.org/case/idobata
へのリンクを作る

**コメント:** なし

---

### [このIssueを分解、作業できる状態にする](https://github.com/digitaldemocracy2030/website/issues/37)

**作成者:** moai-redcap  
**作成日:** 2025-04-25T08:48:02Z  
**内容:**

内容なし

**コメント:** なし

---

### [Githubのセキュリティ通知直す](https://github.com/digitaldemocracy2030/website/issues/36)

**作成者:** moai-redcap  
**作成日:** 2025-04-25T07:19:55Z  
**内容:**

https://github.com/digitaldemocracy2030/website/security/dependabot/4
これやらないとどう悪いのかわからない。調べる→やる。

**コメント:** なし

---

### [アクティビティページのデザイン改善](https://github.com/digitaldemocracy2030/website/issues/29)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-23T10:26:25Z  
**内容:**

# アクティビティページのデザイン改善

## 概要
[アクティビティページ](https://dd2030.org/activity)の全体的な見た目とユーザーインターフェースを改善するための提案です。

## 提案内容
- 全体的なレイアウトの見直し
- より見やすく、使いやすいデザインへの変更
- モバイル対応の確認と改善
- 視覚的な一貫性の確保

## 期待される効果
- ユーザーエクスペリエンスの向上
- 情報の視認性の向上
- プロジェクト活動の把握がしやすくなる

## 参考
Slackチャンネル #2_開発_デジ民ウェブサイト での議論に基づいています。


**コメント:** なし

---

### 過去7日間に作成されたissue (9件)

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

### [ボードメンバーをaboutページに追加する](https://github.com/digitaldemocracy2030/website/issues/43)

**作成者:** moai-redcap  
**作成日:** 2025-04-27T04:49:37Z  
**内容:**

案

[画像]（Xのプロフ画像拝借）
安野 貴博
https://x.com/takahiroanno
[画像]（Xのプロフ画像拝借確認中）
鈴木 健
https://x.com/kensuzuki

こちらのスレッドを要確認
https://w1740803485-clv347541.slack.com/archives/C08K4CUB12T/p1745728260698529

**コメント:** なし

---

### [活用事例ページをmdで管理できるようにする。](https://github.com/digitaldemocracy2030/website/issues/40)

**作成者:** moai-redcap  
**作成日:** 2025-04-25T08:59:05Z  
**内容:**

活用事例ページをmdで管理できるようにする。

活用事例として
https://delib.takahiroanno.com/view/docs/index.md
を追加。


**コメント:** なし

---

### [広聴AIページに使い方ボタンを作成、githubのhow_to_useへリンクを飛ばす](https://github.com/digitaldemocracy2030/website/issues/38)

**作成者:** moai-redcap  
**作成日:** 2025-04-25T08:51:21Z  
**内容:**

https://github.com/digitaldemocracy2030/kouchou-ai/tree/main/how_to_use
へリンクを飛ばす。

**コメント:** なし

---

### [アクティビティページへの「powered by oss_weekly_reporter」表示の追加](https://github.com/digitaldemocracy2030/website/issues/33)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-23T10:27:30Z  
**内容:**

# アクティビティページへの「powered by oss_weekly_reporter」表示の追加

## 概要
[アクティビティページ](https://dd2030.org/activity)に「powered by oss_weekly_reporter」の表示を追加する提案です。

## 提案内容
- ページのどこかに「powered by [oss_weekly_reporter](https://github.com/nishio/oss_weekly_reporter)」の表示を追加
- AI/LLM関連のキーワードを含めることを検討
- クレジット表示の適切な配置場所の検討
- デザインとの調和を考慮した表示方法

## 期待される効果
- 使用ツールの適切なクレジット表示
- AI/LLM技術の活用をアピール
- オープンソースツールの認知度向上への貢献

## 参考
Slackチャンネル #2_開発_デジ民ウェブサイト での議論に基づいています。


**コメント:** なし

---

### [各プロジェクトの最新レポートへのリンク作成](https://github.com/digitaldemocracy2030/website/issues/32)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-23T10:27:14Z  
**内容:**

# 各プロジェクトの最新レポートへのリンク作成

## 概要
各プロジェクトの最新レポートに直接アクセスできるURLを作成し、プロジェクト説明ページからリンクする提案です。

## 提案内容
- 各プロジェクトの最新レポートに直接飛べるURLを作成
- プロジェクト説明ページからこれらのリンクを追加
- 最新の活動状況が一目でわかるようにする
- レポート更新時に自動的にリンク先が更新される仕組みの検討

## 期待される効果
- ユーザーが各プロジェクトの最新状況にすぐにアクセスできる
- プロジェクト間の関連性が明確になる
- 情報へのアクセス性が向上する

## 参考
Slackチャンネル #2_開発_デジ民ウェブサイト での議論に基づいています。


**コメント:** なし

---

### [アクティビティページへのナビゲーション強化](https://github.com/digitaldemocracy2030/website/issues/31)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-23T10:26:57Z  
**内容:**

# アクティビティページへのナビゲーション強化

## 概要
[アクティビティページ](https://dd2030.org/activity)へのアクセス動線を強化する提案です。

## 提案内容
- サイト内の各セクションからアクティビティページへの動線を強化
- メインナビゲーションでの位置づけの見直し
- アクティビティページの存在を目立たせる工夫
- 関連ページからの参照リンクの追加

## 期待される効果
- アクティビティページへのアクセス数の増加
- ユーザーがプロジェクトの活動を見つけやすくなる
- サイト全体の回遊性の向上

## 参考
Slackチャンネル #2_開発_デジ民ウェブサイト での議論に基づいています。


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

### 過去7日間に更新されたissue（作成・クローズを除く）(3件)

### [SEO的に必要なメタタグ等の項目の整理](https://github.com/digitaldemocracy2030/website/issues/12)

**作成者:** rysh  
**作成日:** 2025-04-05T03:29:27Z  
**内容:**

Twitterカードがなかったり、リンク先の概要が見えなかったりすると、クリック率が顕著に落ちる。高度なSEOは必要ないが、意欲のあるプロジェクトであることをアピールするためには当たり前品質には達していたい

**コメント:** なし

---

### [紹介する事例案](https://github.com/digitaldemocracy2030/website/issues/4)

**作成者:** nishio  
**作成日:** 2025-03-26T16:05:23Z  
**内容:**

デジタル民主主義2030の広聴AIを試してみた！政治家目線での期待と感触｜ほづみゆうき@中央区議会議員
https://note.com/yukihoz/n/n06360c9a17fd

**コメント:** なし

---

### [広聴AIといどばたのリンク](https://github.com/digitaldemocracy2030/website/issues/2)

**作成者:** kixyz-dev  
**作成日:** 2025-03-24T02:23:12Z  
**内容:**

広聴AIといどばたのリンクがあると、わかりやすいと思いました。

例
<p class="chakra-card__description css-b9p74s">どなたでも[広聴AI](https://github.com/digitaldemocracy2030/kouchou-ai/tree/main/how_to_use)や[大規模熟議](https://large-scale-conversation-sandbox.discourse.group/t/topic/39)を利用して、様々な意見や議論を届けることができます。ぜひ以下の活用事例からご参加ください！</p>

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (15件)

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

### [docsページBuildエラー対応](https://github.com/digitaldemocracy2030/website/pull/56)

**作成者:** moai-redcap  
**作成日:** 2025-04-29T08:21:55Z  
**変更:** +18 -19 (5ファイル)  
**マージ日:** 2025-04-29T08:22:06Z  
**内容:**

内容なし

**コメント:** なし

---

### [buildエラーが修正できているか確認](https://github.com/digitaldemocracy2030/website/pull/55)

**作成者:** moai-redcap  
**作成日:** 2025-04-29T06:49:34Z  
**変更:** +4 -3 (2ファイル)  
**マージ日:** 2025-04-29T06:49:42Z  
**内容:**

内容なし

**コメント:** なし

---

### [buildエラーチャレンジ](https://github.com/digitaldemocracy2030/website/pull/54)

**作成者:** moai-redcap  
**作成日:** 2025-04-29T06:15:13Z  
**変更:** +6 -0 (1ファイル)  
**マージ日:** 2025-04-29T06:15:21Z  
**内容:**

内容なし

**コメント:** なし

---

### [fix Error: Route "/docs/[...slug]" used `params.slug`. `params` shoul…](https://github.com/digitaldemocracy2030/website/pull/53)

**作成者:** moai-redcap  
**作成日:** 2025-04-29T05:21:43Z  
**変更:** +8 -2 (1ファイル)  
**マージ日:** 2025-04-29T05:21:49Z  
**内容:**

…d be awaited before using its properties.

**コメント:** なし

---

### [Docsページ群の作成](https://github.com/digitaldemocracy2030/website/pull/51)

**作成者:** moai-redcap  
**作成日:** 2025-04-29T05:06:07Z  
**変更:** +58 -71 (6ファイル)  
**マージ日:** 2025-04-29T05:06:17Z  
**内容:**

内容なし

**コメント:** なし

---

### [Fix kouchou-ai project website link](https://github.com/digitaldemocracy2030/website/pull/49)

**作成者:** NISHIO Hirokazu+Devin  
**作成日:** 2025-04-29T04:49:28Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-04-29T04:54:11Z  
**内容:**

# Fix kouchou-ai project website link

This PR fixes the broken link to the kouchou-ai project website in the v2.0.0 release announcement.

## Changes
- Updated the project website link from `https://digitaldemocracy2030.github.io/` to `https://github.com/digitaldemocracy2030/kouchou-ai/`

Link to Devin run: https://app.devin.ai/sessions/3c1994aa11f94b94b576f8ce0a5b59c5
Requested by: NISHIO Hirokazu (nishio.hirokazu@gmail.com)


**コメント:** なし

---

### [Docsページ制作完了](https://github.com/digitaldemocracy2030/website/pull/48)

**作成者:** moai-redcap  
**作成日:** 2025-04-29T04:36:35Z  
**変更:** +4292 -150 (23ファイル)  
**マージ日:** 2025-04-29T04:36:58Z  
**内容:**

#41 

**コメント:** なし

---

### [Add news page for kouchou-ai v2.0.0 release](https://github.com/digitaldemocracy2030/website/pull/47)

**作成者:** NISHIO Hirokazu+Devin  
**作成日:** 2025-04-29T04:27:30Z  
**変更:** +115 -0 (3ファイル)  
**マージ日:** 2025-04-29T04:34:04Z  
**内容:**

# Add news page for kouchou-ai v2.0.0 release

This PR adds a news page for the kouchou-ai v2.0.0 release announcement. The content is written in a user-friendly way to explain the new features and improvements in the stable release.

## Changes
- Added Markdown content for the kouchou-ai v2.0.0 release
- Created a news section with a listing page
- Added a dedicated page for the kouchou-ai v2.0.0 release announcement
- Added JSON-LD structured data for better SEO

The page will be accessible at https://dd2030.org/news/kouchou-ai-v2 after deployment.

Link to Devin run: https://app.devin.ai/sessions/3c1994aa11f94b94b576f8ce0a5b59c5
Requested by: NISHIO Hirokazu (nishio.hirokazu@gmail.com)


**コメント:** なし

---

### [nextを最新安定版にアップデート](https://github.com/digitaldemocracy2030/website/pull/46)

**作成者:** moai-redcap  
**作成日:** 2025-04-27T09:28:46Z  
**変更:** +58 -479 (2ファイル)  
**マージ日:** 2025-04-27T09:29:00Z  
**内容:**

#36 

**コメント:** なし

---

### [nextjsのアップデート](https://github.com/digitaldemocracy2030/website/pull/45)

**作成者:** moai-redcap  
**作成日:** 2025-04-27T08:24:27Z  
**変更:** +79 -42 (2ファイル)  
**マージ日:** 2025-04-27T08:28:53Z  
**内容:**

[#36](https://github.com/digitaldemocracy2030/website/issues/36)

**コメント:** なし

---

### [fix(typo): Github -> GitHub](https://github.com/digitaldemocracy2030/website/pull/42)

**作成者:** nakasyou  
**作成日:** 2025-04-27T02:07:30Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-04-27T03:40:36Z  
**内容:**

GitHub の `H` は大文字なので、フッターを修正しました。

**コメント:** なし

---

### [広聴AIページに歴史セクションを追加](https://github.com/digitaldemocracy2030/website/pull/35)

**作成者:** NISHIO Hirokazu+Devin  
**作成日:** 2025-04-25T03:42:44Z  
**変更:** +12 -0 (1ファイル)  
**マージ日:** 2025-04-25T04:10:19Z  
**内容:**

noteの記事（https://note.com/nishiohirokazu/n/nb37adf96fe50）を参考に、Talk to the Cityから広聴AIへの進化の歴史を説明するセクションを追加しました。

依頼者: NISHIO Hirokazu (nishio.hirokazu@gmail.com)
Devin実行URL: https://app.devin.ai/sessions/f84aee916f4948689b562b091f1c8f91

**コメント:** なし

---

### [week6](https://github.com/digitaldemocracy2030/website/pull/34)

**作成者:** nishio  
**作成日:** 2025-04-23T13:12:04Z  
**変更:** +435 -0 (5ファイル)  
**マージ日:** 2025-04-23T13:12:11Z  
**内容:**

第6週の活動まとめを追加

**コメント:** なし

---

### [Update slack5w.md : add Polimoney meeting info](https://github.com/digitaldemocracy2030/website/pull/27)

**作成者:** masatosasano2  
**作成日:** 2025-04-22T06:55:59Z  
**変更:** +2 -1 (1ファイル)  
**マージ日:** 2025-04-23T13:12:40Z  
**内容:**

内容なし

**コメント:** なし

---

### 過去7日間に作成されたPR (2件)

### [宇多津町のブロードリスニング事例を追加](https://github.com/digitaldemocracy2030/website/pull/58)

**作成者:** NISHIO Hirokazu+Devin  
**作成日:** 2025-04-30T03:25:49Z  
**変更:** +4 -0 (1ファイル)  
**内容:**

# 宇多津町の事例紹介を追加

宇多津町が実施した「ブロードリスニング」の事例を広聴AIの活用事例として追加しました。

参考URL: https://www.town.utazu.lg.jp/page/4114.html

Link to Devin run: https://app.devin.ai/sessions/10542d74a949498abe86f10164df3d86
Requested by: NISHIO Hirokazu (nishio.hirokazu@gmail.com)


**コメント:** なし

---

### [PRプレビューデプロイメントの実装](https://github.com/digitaldemocracy2030/website/pull/52)

**作成者:** NISHIO Hirokazu+Devin  
**作成日:** 2025-04-29T05:07:01Z  
**変更:** +328 -211 (10ファイル)  
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

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

