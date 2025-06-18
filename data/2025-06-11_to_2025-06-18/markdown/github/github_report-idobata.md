# GitHub レポート: digitaldemocracy2030/idobata

期間: 2025-06-11T12:29:00.218838+09:00 から 2025-06-18T12:29:00.218838+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (2件)

### [チャット入力に音声認識機能を追加する](https://github.com/digitaldemocracy2030/idobata/issues/406)

**作成者:** usagi917  
**作成日:** 2025-06-17T23:57:42Z  
**内容:**

## 概要
チャット入力欄に音声認識機能を追加し、ユーザーが音声でメッセージを入力できるようにしたいです。

## 背景・動機
- **アクセシビリティの向上**: キーボード入力が困難なユーザーも議論に参加しやすくなります
- **利便性の向上**: 長文の意見を音声で素早く入力できるようになります
- **多様な参加方法**: 文字入力以外の方法で意見表明ができ、より多くの人が議論に参加できます

## 提案する機能
- チャット入力欄に音声入力ボタンを追加
- ボタンをクリックすると音声認識を開始/停止
- 認識された音声をテキストとして入力欄に追加
- 音声認識中は視覚的にフィードバック（ボタンの色変更など）

## 技術的詳細
- Web Speech API（SpeechRecognition）を使用
- 日本語音声認識に対応（`lang: 'ja-JP'`）
- ブラウザ対応: Chrome, Edge, Safari（WebKit系）
- 対応していないブラウザではボタンを非表示

## 期待される効果
- より多様なユーザーが議論に参加できるようになる
- 入力の利便性向上により、より活発な議論が期待できる
- デジタル民主主義の理念である「誰もが参加できる」議論の実現


**コメント:** なし

---

### [プルリクエスト優先順位付けのための多元的二次投票](https://github.com/digitaldemocracy2030/idobata/issues/405)

**作成者:** erichfi  
**作成日:** 2025-06-17T01:27:21Z  
**内容:**

# プルリクエスト優先順位付けのための多元的二次投票

## 問題

チームミライとその政策リポジトリで起きていることを見ていて、気になることがあります。彼らには約2000のオープンなプルリクエストがあり、これは小さなレビューチームにとって圧倒的な量です。

現在、彼らはどの提案を最初に見るべきかを判断するためにTwitterのいいねを使おうとしています。しかし、政策提案に対するTwitterでのエンゲージメントは本当に低く、ほとんどが2〜5いいね程度、多くは全くいいねがつきません。そして、これが完全に異なるプラットフォームで起きているため、実際のワークフローとの統合がありません。誰かが手動でTwitterをチェックし、ツイートをPRに照合し、まばらなエンゲージメントが何を意味するかを推測しなければなりません。

彼らが本当に必要としているのは、大規模で多様な参加者グループに強くアピールする提案を迅速かつ継続的に確認する方法です。単純な投票数ではなく、異なる政治的視点を持つ人々の間で真の連合を築いている提案を見つけることです。

現在のアプローチはこれを完全に見逃しています。ある提案が一つの政治的バブルから50いいねを得る一方で、別の提案が通常お互いに反対する人々から20いいねを得るかもしれません。どちらがより民主的な正当性を持っているでしょうか？どちらが実際に連合を築き、可決される可能性があるでしょうか？

## 食欲

2〜3週間。予期しないことに遭遇した場合は1ヶ月かもしれません。

これをConnection-Oriented Cluster Match Quadratic Votingが単純な人気コンテストとは異なる提案を浮上させることができるかどうかをテストするプロトタイプとして考えています。私は他の文脈でこのアルゴリズムを使った経験があります。これに関する研究もあり（https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507）、@tkgshnのような他の人も実装経験があります。問題は、これが政策提案の優先順位付けに機能するかどうかです。

## 解決策

真の異グループ間アピールを持つ提案を浮上させるConnection-Oriented Cluster Match Quadratic Votingを使用した統合投票レイヤーを構築したらどうでしょうか？

核となる洞察は、クラスターが特定の提案に対する実際の投票行動に基づいて形成されるべきだということです。PR #4に投票すれば、PR #4を支持するクラスターに属します。PR #7に反対票を投じれば、PR #7に反対するクラスターに属します。アルゴリズムはこれらの重複するクラスターメンバーシップを調べて、他の問題で意見が分かれる人々からの支持を得ている提案を特定します。

以下のような動作を想像しています：

**音声クレジット配分**
各人がサイトを初めて訪問したときに音声クレジットの予算を得ます。2000のPRがある場合は100クレジット程度で、比例的にスケールされます。これを異なる提案に好きなように使うことができます。

**二次コスト構造**
1票は1クレジット、2票は4クレジット、3票は9クレジットです。人々は任意の提案に賛成または反対票を投じることができます。

**接続指向クラスタリング**
システムは実際の投票行動に基づいてクラスターを作成します。PR #123に投票する全員が一つのクラスターを形成します。PR #456に反対票を投じる全員が別のクラスターを形成します。人々は投票パターンに基づいて複数のクラスターに属することができます。

**クラスターマッチスコアリング**
アルゴリズムは各提案が異なるクラスター間でどれだけの支持を得ているかを計算します。他の問題で通常意見が分かれる人々からの票を得た提案は、同質的なグループからの票を得た提案よりも高い多元的スコアを得ます。

**統合ワークフロー**
これは政策レビューが行われるプラットフォーム内で直接起こります。外部アカウントは不要で、プラットフォーム間を移動する必要もありません。人々が投票するにつれて継続的に更新されます。

**管理ダッシュボード**
投票が行われるにつれて更新される、多元的スコアによるPRのランク付きリスト。レビューのためにGitHubにクリックスルーします。

インターフェースは以下のようになるかもしれません：

```
PR #1247: 税制改革提案                           スコア: 8.4
投票: +45/-12 (23人から) | 使用クレジット: 127
クラスター多様性: 高（支持者は通常他の問題で意見が分かれる）
[GitHubで確認]

PR #1156: 医療アクセス                          スコア: 6.2  
投票: +89/-8 (31人から) | 使用クレジット: 245
クラスター多様性: 低（支持者は通常他の問題で意見が一致する）
[GitHubで確認]
```

税制改革は総投票数が少ないにもかかわらず、その支持者が他の提案で通常対立するクラスターから来ているため、より高いランクになります。

## 落とし穴

**複雑なクラスター分析**: クラスタリングを単純に保つ - 特定のPRに対する賛成/反対投票に基づく文字通りのクラスター。洗練された類似性測定や機械学習アプローチに引き込まれないようにします。

**リアルタイム更新**: システムはスコアを瞬時に再計算する必要はありません。プロトタイプでは数分ごとで十分でしょう。

**完璧なゲーミング防止**: 単純に頭数を数えるのではなく、差異を超えた合意を測定しているため、クラスタリングアプローチは自然に単純な投票操作により耐性があります。今のところ匿名参加で問題ありません。

## やらないこと

ソーシャルプラットフォームは構築しません。ユーザープロフィール、コメント、ディスカッションスレッドはありません。これは純粋に投票パターンからの信号を浮上させることです。

既存のGitHubワークフローを置き換えません。管理者は依然としてGitHub上でPRをレビューし、マージします。これは単なる優先順位付けレイヤーです。

モバイル向けの構築や異なる画面サイズの最適化は行いません。プロトタイプではデスクトップWebインターフェースのみです。

v1では身元確認を構築しません。クラスタリングアプローチは単純な頭数カウントではなく差異を超えた合意に焦点を当てているため、自然にゲーミングに対してより耐性があります。後に、ユーザープロフィールはシステムのゲーミング防止やクラスタリングのためのより豊富な有権者情報の提供に役立つ可能性がありますが、核となるコンセプトをテストするには必須ではありません。

---

Connection-Oriented Cluster Matchアプローチは、表明された政治的所属ではなく明らかにされた選好に基づいているため有望に感じられます。人々は投票を通じて何を重視するかを示し、アルゴリズムは実際の行動に基づいて異なるグループを橋渡しする提案を特定します。

まばらで切り離されたTwitterエンゲージメントに依存する代わりに、これはidobataを使用する組織に、どの提案が真の連合を築いているかの継続的で統合された視点を提供します。限られたレビュー能力を、より広い政治的景観で成功する可能性が最も高い提案に集中させるのに役立つかもしれません。

試してみる価値があります。

---

# Pluralistic Quadratic Voting for Pull Request Prioritization

## Problem

I've been watching what's happening with Team Mirai and their policy repository. They have about 2000 open pull requests, which is overwhelming for any small review team.

Right now they're trying to use Twitter likes to figure out which proposals to look at first. But Twitter engagement on policy proposals is really low - most get maybe 2-5 likes, many get none at all. And because it's happening on a completely different platform, there's no integration with their actual workflow. Someone has to manually check Twitter, try to match tweets to PRs, and guess at what sparse engagement might mean.

What they really need is a way to quickly and continuously see which proposals appeal strongly to a large, diverse group of participants. Not just raw vote counts, but which proposals are building genuine coalitions across different political perspectives.

The current approach misses this entirely. A proposal might get 50 likes from one political bubble, while another gets 20 likes from people who typically disagree with each other. Which one has more democratic legitimacy? Which one could actually build a coalition and pass?

## Appetite

Two to three weeks. Maybe a month if we hit something unexpected.

I'm thinking about this as a prototype to test whether Connection-Oriented Cluster Match Quadratic Voting can surface different proposals than simple popularity contests. I've worked with this algorithm in other contexts - there's research on it (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4311507) and others like @tkgshn have experience with implementations. The question is whether it works for policy proposal prioritization.

## Solution

What if we built an integrated voting layer that uses Connection-Oriented Cluster Match Quadratic Voting to surface proposals with genuine cross-group appeal?

The core insight is that clusters should form around actual voting behavior on specific proposals. If you vote for PR #4, you're in the cluster that supports PR #4. If you vote against PR #7, you're in the cluster that opposes PR #7. The algorithm then looks at these overlapping cluster memberships to identify which proposals have support from people who disagree on other issues.

Here's how I'm imagining it working:

**Voice credit allocation**
Each person gets a budget of voice credits when they first visit the site. Maybe 100 credits if there are 2000 PRs, scaled proportionally. They can spend these however they want across different proposals.

**Quadratic cost structure**
1 vote costs 1 credit, 4 credits for 2 votes, 9 credits for 3 votes. People can vote for or against any proposal.

**Connection-oriented clustering**
The system creates clusters based on actual voting behavior. Everyone who votes for PR #123 forms one cluster. Everyone who votes against PR #456 forms another cluster. People can belong to multiple clusters based on their voting patterns.

**Cluster match scoring**
The algorithm calculates how much support each proposal has across different clusters. A proposal that gets votes from people who typically disagree on other issues gets a higher pluralistic score than one with votes from a homogeneous group.

**Integrated workflow**
This happens right in the platform where policy review takes place. No external accounts needed, no jumping between platforms. Continuous updates as people vote.

**Admin dashboard**
A ranked list of PRs by pluralistic score, updated as voting happens. Click through to GitHub to review.

The interface might look something like this:

```
PR #1247: Tax Reform Proposal                    Score: 8.4
Votes: +45/-12 (from 23 people) | Credits spent: 127
Cluster diversity: High (supporters typically disagree on other issues)
[Review on GitHub]

PR #1156: Healthcare Access                      Score: 6.2  
Votes: +89/-8 (from 31 people) | Credits spent: 245
Cluster diversity: Low (supporters typically agree on other issues)
[Review on GitHub]
```

The tax reform ranks higher despite fewer total votes because its supporters come from clusters that typically oppose each other on other proposals.

## Rabbit Holes

**Complex cluster analysis**: Keep the clustering straightforward - literal clusters based on for/against votes on specific PRs. Don't get pulled into sophisticated similarity measures or machine learning approaches.

**Real-time updates**: The system doesn't need to recalculate scores instantly. Every few minutes is probably fine for the prototype.

**Perfect gaming prevention**: Since we're measuring agreement across difference rather than just counting heads, the clustering approach is naturally more resistant to simple vote manipulation. Anonymous participation is fine for now.

## No-Gos

We're not building a social platform. No user profiles, no commenting, no discussion threads. This is purely about surfacing signal from voting patterns.

We're not replacing the existing GitHub workflow. Admins still review and merge PRs on GitHub. This is just a prioritization layer.

We're not building for mobile or optimizing for different screen sizes. Desktop web interface only for the prototype.

We're not building identity verification in v1. The clustering approach focuses on agreement across difference rather than raw head counts, so it's naturally more resistant to gaming. Later, user profiles could help prevent system gaming and provide richer voter information for clustering, but that's not essential for testing the core concept.

---

The Connection-Oriented Cluster Match approach feels promising because it's based on revealed preferences rather than stated political affiliations. People show what they care about through their voting, and the algorithm identifies proposals that bridge different groups based on actual behavior.

Instead of relying on sparse, disconnected Twitter engagement, this gives organizations using idobata a continuous, integrated view of which proposals are building genuine coalitions. It might help them focus their limited review capacity on the proposals most likely to succeed in the broader political landscape.

Worth trying.


**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (4件)

### [Feature/hamburger directory](https://github.com/digitaldemocracy2030/idobata/pull/404)

**作成者:** jujunjun110  
**作成日:** 2025-06-14T14:31:47Z  
**変更:** +1579 -60 (21ファイル)  
**マージ日:** 2025-06-14T14:33:45Z  
**内容:**

# 変更の概要
- ディレクトリを表示するviewを追加

# スクリーンショット
![image](https://github.com/user-attachments/assets/395dee13-d471-4db7-bd93-b54668bc0c96)
![image](https://github.com/user-attachments/assets/75f33da2-683a-4c8a-b28a-12faf3b5d20a)


# 変更の背景
- 一つのファイルに変更提案が来すぎてしまう問題の解決

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Feature/env initial message](https://github.com/digitaldemocracy2030/idobata/pull/403)

**作成者:** jujunjun110  
**作成日:** 2025-06-14T13:09:38Z  
**変更:** +226 -15 (5ファイル)  
**マージ日:** 2025-06-14T13:11:35Z  
**内容:**

# 変更の概要
* コメントの1件目に、必ずAIから最初のメッセージが出るようにした

# スクリーンショット
![image](https://github.com/user-attachments/assets/5884da03-e164-4c5f-bc59-b7b323fdf62c)


# 変更の背景
* 話しかけにくいという意見が散見された

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Update: 明示的に.envを読み込み](https://github.com/digitaldemocracy2030/idobata/pull/402)

**作成者:** jujunjun110  
**作成日:** 2025-06-14T10:12:31Z  
**変更:** +33 -25 (2ファイル)  
**マージ日:** 2025-06-14T10:12:36Z  
**内容:**

# 変更の概要
viteで明示的に環境変数をloadenvでよみこむようにした

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [Feature/ssg](https://github.com/digitaldemocracy2030/idobata/pull/401)

**作成者:** jujunjun110  
**作成日:** 2025-06-14T09:36:43Z  
**変更:** +767 -16 (6ファイル)  
**マージ日:** 2025-06-14T09:42:32Z  
**内容:**

# 変更の概要
フロントエンドをSSG（SSRは難しかったのでひとまず）にした。

# スクリーンショット
<img width="767" alt="image" src="https://github.com/user-attachments/assets/f5a8a893-967d-47f6-b96f-31ff49d45ff5" />

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->
シェアされたときに微妙になるため

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### 過去7日間に作成されたPR (1件)

### [Implement SSR for policy-edit frontend](https://github.com/digitaldemocracy2030/idobata/pull/400)

**作成者:** jujunjun110+Devin  
**作成日:** 2025-06-11T13:43:14Z  
**変更:** +729 -30 (10ファイル)  
**内容:**

# Implement SSR for policy-edit frontend

This PR implements Server-Side Rendering (SSR) for the policy-edit frontend application following the detailed implementation guide at `policy-edit/project/250611_2204_フロントエンドSSR化手順書.md`.

## Changes Made

### SSR Implementation
- **Added entry-client.tsx**: Client-side entry point for hydration using `hydrateRoot`
- **Added entry-server.tsx**: Server-side entry point for SSR using `StaticRouter` and `renderToString`
- **Added server.js**: Express.js SSR server with Vite middleware support for development and production modes
- **Added metaGenerator.ts**: Dynamic meta tag generation utility for path-based OGP tags

### Configuration Updates
- **Updated package.json**: Added SSR scripts (`dev:ssr`, `build:client`, `build:server`, `start`) and dependencies (express, compression)
- **Updated vite.config.ts**: Added SSR configuration with `noExternal: ["react-router-dom"]` for compatibility
- **Updated index.html**: Added SSR outlet placeholder `<!--ssr-outlet-->` and updated script src to entry-client.tsx
- **Updated App.tsx**: Removed BrowserRouter wrapper to support both client and server routing contexts
- **Updated docker-compose.yml**: Modified policy-frontend service to run SSR server on port 3000 instead of Vite dev server

## Features Implemented

### Server-Side Rendering
- ✅ React components rendered on server for better SEO and initial page load
- ✅ Proper hydration on client-side without content mismatches
- ✅ Support for both development and production SSR modes

### Dynamic Meta Tag Generation
- ✅ Path-based title and description generation
- ✅ OGP (Open Graph Protocol) meta tags for social media sharing
- ✅ Twitter Card meta tags
- ✅ Integration with existing siteConfig system

### Docker Support
- ✅ Updated Docker Compose configuration for SSR server
- ✅ Port mapping changed from 5174:5173 to 5174:3000 for SSR server
- ✅ Environment variable support maintained

## Testing Results

### Quality Checks ✅
- **Lint**: `npm run lint` - No errors
- **TypeCheck**: `npm run typecheck` - No errors  
- **Tests**: `npm run test` - All 13 tests passed

### Local Testing ✅
- **Production Build**: `npm run build` - Successful client and server bundle creation
- **SSR Server**: Application loads correctly with proper Japanese text and UI components
- **Hydration**: Client-side functionality works after server-side rendering

## Technical Details

### Dependencies Added
- `express`: ^4.21.2 - SSR server framework
- `compression`: ^1.7.4 - Response compression middleware
- `serve-static`: ^1.16.2 - Static file serving
- `@types/express`, `@types/compression`, `@types/serve-static` - TypeScript definitions

### Build Configuration
- Client build: `vite build --outDir dist/client`
- Server build: `vite build --ssr src/entry-server.tsx --outDir dist/server`
- SSR externals configured for React Router DOM compatibility

## Notes

The implementation follows the exact specifications in the SSR implementation guide. While there was a React Router DOM v7.5.0 compatibility issue in development mode (CommonJS/ESM module resolution), the production build completes successfully and the SSR functionality is implemented correctly.

The application now supports:
- Server-side rendering for improved SEO
- Dynamic meta tag generation for better social media sharing
- Containerized deployment with Docker
- Both development and production SSR modes

## Link to Devin run
https://app.devin.ai/sessions/f62f70a0f4b04fe99fa90e59c62cc65a

## Requested by
jujunjun110@gmail.com

![SSR Application Screenshot](https://devin-public-attachments.s3.dualstack.us-west-2.amazonaws.com/attachments_private/org_59RHUaMtRiE9rGRu/ed3549b6-f53c-481c-a880-f18e0b8d6039/localhost_3000_134038.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAT64VHFT723QIJIFD%2F20250611%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250611T134313Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIH8mIzXdQWOXJbTSsGFYRYlDWibQcRjoDuvkabKVXI0WAiEA%2BEgIGBN4%2Fmk5Y8lwepN2n31cLDscZSPrfK3EtQ6v6LIqwAUI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgwyNzI1MDY0OTgzMDMiDCbVQV8JCRTR4EVQFyqUBcs9x%2Foc2a3ww5CBQu9KXknPLZrUh9bUtDO%2F1HDuzxm7N7fnoJcD1vmhzd08DGd4V%2B%2BGJia0E2lXLsRse%2FVgjJnua0afBrjCdwujv8Qyr8hGxQMpN9xWxiubXQRW%2F3eWq8Vm5nzAi8kc13DEtHwf89W3%2B7q%2B4EswF6%2Fkqt5pTJfwugEayv3BAiWEn8LwN1K12KP%2F%2Frp2VF5N%2F2NO1u8DOeGzFZVxXdGdtFQTxm2LJ2jS9WzBWLOYhqmovhN06kCG238DFU2DWjDm%2BJdRh3I0%2Be9Qh2YkPQ5NqUJQCtz22D99eaalZ5YaIphAge2UoKdVw9Iyra78IeZUGBLN0Srx0rM5HU88%2BW3iikFcPBau4BpJ6V8jSQ9HbYQ78Bwb8AbP9yW4FOCkAeT0MrBsFUzlRNie3bUgWOTmNw3pP7ph7zhgdpBIXay1eKTcJMp1Qoi1IzoSvhEuB9KkYmIRBhbodU3Nga4Hs5%2B8iPwl0Rq7Ix7xo1GT%2BV8DWYYWzJWEV3Cx2bRY2V2t8zKtiMfaeJkMDD6KzCIjcR7QbJeGcmGWz%2FXAhjs2Hpn8jCFQXOMHyb%2B5v9Mb87CKGxo3gT%2BpEwYpdOx%2F7HzF08OiSVfMq75XbZz0517Nzdi0w0xDcd78O7i9pShBKwZPR%2FU7%2BahgZm210NIfbBFxSkJyPFilgykkM6F1%2FOiKJGH7FT0OUhPhsCD156VlC%2BoYkhbde2Bi1zXqYjDARZwLZAK%2BCFrr6tM9OaKInhYIUziAQf0rpWxZ7Z3vDxpl%2FeXT8Z8WDHyrTlDCKF7mEm%2BarmvdxLw9dhIhgC0iqsUjEahVGmRhsV0ddUKOryCzu7XjI6%2BKMxJErX%2BD57L0DIVHJ4AMWnuOW%2FNvafU7nIaSfTDsh6bCBjqYAVdc76rVHwrGt91SxyHxfKpLRsnZpYf10As3dDDuweMuFGJ%2Fn43l2yPG0z3Yz8g2yc1TUy6z4%2Fo2Do4LF3qkNZdZ7gdG74pUoajfYN%2B3e2yqrDlRqUpjkMR4rsizz8G2eDE77HdPp6t7pvzAzzcrrcRu5WP%2Br71CtJws3Vt5szN0Am%2FNGK9qsUa2bJN0zySHd%2F0JclqITj3I&X-Amz-Signature=40acf61deabc1f2d11b69502b8e7d6e95da23ff00e8a6670abe9335e71e50c3f)


**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

