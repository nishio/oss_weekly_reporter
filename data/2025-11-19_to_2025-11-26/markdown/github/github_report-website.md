# GitHub レポート: digitaldemocracy2030/website

期間: 2025-11-19T12:30:03.986841+09:00 から 2025-11-26T12:30:03.986841+09:00 まで

## Issues

### 過去7日間に完了されたissue (2件)

### [新規参加者向けに「プロジェクトが今どんな状態なのか」をざっくり言語化したものをウェブサイトに掲載する](https://github.com/digitaldemocracy2030/website/issues/180)

**作成者:** shingo-ohki  
**作成日:** 2025-11-22T03:07:35Z  
**内容:**

例えば、こういうものをそのままウェブサイトに掲載するのはどうか？という話

> NISHIO Hirokazu
  [33分前](https://dd2030.slack.com/archives/C08FL58LK8V/p1763778724704149)
大木さんが直してくれた https://dd2030.org/history をGPT5.1に渡して「このプロジェクトに新しく参加した人向けの今どうなっているのかの解説」を作らせました(スレッドに貼ります) （編集済み） 
1 件の返信
NISHIO Hirokazu
  [32分前](https://dd2030.slack.com/archives/C08FL58LK8V/p1763778782849749?thread_ts=1763778724.704149&cid=C08FL58LK8V)
prompt
https://dd2030.org/history これを参考にして、このプロジェクトに新しく参加した人向けに「今どうなっているのか」の解説を作って
いまDD2030に入ってきた人向けに、「このプロジェクトは今どんな状態なのか」をざっくり言語化してみます。
>1. 全体の位置づけ：3つの柱＋大きなコミュニティ
*デジタル民主主義2030（DD2030）*は、
市民の声を可視化する 広聴AI（Talk to the City系）
大規模なオンライン熟議プラットフォーム 「いどばた」
政治資金の可視化ダッシュボード Polimoney
という3つの取り組みを中心に、「デジタルで民主主義をアップデートする」ことを目指しているプロジェクトです。([デジタル民主主義2030](https://dd2030.org/))
2025年3月にSlackが立ち上がり、最初の1週間で開発チャンネルが立ち上がり、リポジトリが公開され、OSS開発コミュニティとして一気に立ち上がりました。([デジタル民主主義2030](https://dd2030.org/history))
そこから毎週の活動を「第○週の活動」として /history にまとめていて、少なくとも36週分（2025-11-19の週）まで継続的に動いていることがわかります。([デジタル民主主義2030](https://dd2030.org/history))
>2. 「今」のスナップショット（直近1週間から見えること）
直近の「第36週（2025-11-13〜11-19）」のSlackダイジェストを見ると、今のDD2030の雰囲気がかなりよく伝わります。([デジタル民主主義2030](https://dd2030.org/history/week36_20251119/slack))
2-1. 広聴AI（ブロードリスニング）
アルゴリズム開発チャンネルが最も盛り上がっている（55件のメッセージ）。
散布図（embedding）だけにこだわらず、
「ワードクラウド＋クリックで掘り下げ」
「LLMによるクラスタリングと可視化」
 など、見た目と分析の本質を分けて考えようという議論が進行中。([デジタル民主主義2030](https://dd2030.org/history/week36_20251119/slack))
東京都の「未来の東京」戦略など既存の分類にブロードリスニングの結果をはめてみたところ、意外と全カテゴリに収まってしまい、「新しい論点が見えにくい」という問題提起も出ている。([デジタル民主主義2030](https://dd2030.org/history/week36_20251119/slack))
自治体・議員へのヒアリングやアンケートの計画を立てつつ、「人手をかけずにテキスト意見を分類したい」という現場ニーズをどう汲むかを検討している。([デジタル民主主義2030](https://dd2030.org/history/week36_20251119/slack))
トップページ側では、Local LLM対応やコスト削減機能を盛り込んだ広聴AI v3.0.0が2025-05-30にリリース済みで、ツールとしてもかなり実用度が上がっている状態です。([デジタル民主主義2030](https://dd2030.org/))
2-2. いどばた（大規模熟議）
毎週の定例ミーティングは「議題が薄い時は無理にやらない」方向にシフトしつつあり、
 必要なときに集まる実務寄りフェーズに入りつつあります。([デジタル民主主義2030](https://dd2030.org/history/week36_20251119/slack))
「区民の潜在的な不満・要望をAI対話からうまく引き出せないか？」というユースケースが議論され、
 “Option1” 的な新しいサービス案として盛り上がっています。([デジタル民主主義2030](https://dd2030.org/history/week36_20251119/slack))
いどばたから派生するプロジェクトの種がいくつも生まれつつある段階。
2-3. Polimoney（政治資金の可視化）
既存の政治資金可視化ツールと比較しつつ、
 Polimoneyの立ち位置・目的をREADMEで整理し直そうとしているところ。([デジタル民主主義2030](https://dd2030.org/history/week36_20251119/slack))
選挙運動費用や公費負担などの制度理解を深めつつ、プロダクトとしてどこを特徴にするか議論中。
2-4. Cartographer & 新しいツール群
「Cartographer」というツールを使って、コミュニティ内の認識を整理する試みが続いています。([デジタル民主主義2030](https://dd2030.org/history/week36_20251119/slack))
参加時に答えた質問＋途中で追加した「深掘り質問」をどう見せるか、といったUI/UX課題を検証中。
「じぶんレポート」を作ってSlackプロフィールに貼る、など、オンボーディングを楽しくするアイデアが出ている。
2-5. コミュニティ全体・運営
Slackには 1400人超（直近では1403人） が参加しており、新規メンバーは今も増加中。([デジタル民主主義2030](https://dd2030.org/history/week36_20251119/slack))
「完成した成果物」よりも、
 “生々しい議論“や”まだ形になっていないアイデア“をオープンに共有すること自体に価値があるという声が強く、
 それをどう外部に伝えるか（広報／PR）も議題になっています。([デジタル民主主義2030](https://dd2030.org/history/week36_20251119/slack))
/history ページの更新フローを自動化したい、アクセス解析をどう共有するかなど、
 OSSコミュニティらしい運営上の悩みも議論中。([デジタル民主主義2030](https://dd2030.org/history/week36_20251119/slack))
さらに、「ブロードリスニング本」や新しい理論・研究寄りのディスカッションも進んでおり、
 技術・実装・理論・書籍執筆が並走している状態です。([デジタル民主主義2030](https://dd2030.org/history/week36_20251119/slack))
>3. いま参加した人から見た「入りどころ」
直近のダイジェストでは、「参加すると何ができる？」として次のような入口が整理されています。([デジタル民主主義2030](https://dd2030.org/history/week36_20251119/slack))
広聴AI
AI開発・データ分析・自治体への実装に関心がある人向け
いどばた & その派生
施策を議論しながらサクッとまとめる、オンライン熟議の設計に興味がある人向け
Polimoney
政治とお金の透明化、オープンデータ可視化に興味がある人向け
コミュニティ運営
オンボーディング設計・イベント・広報など、コミュニティづくりをやりたい人向け
その他
Cartographer・ブロードリスニング本・新しい理論的検討など、研究寄り／メタな議論の場もある
>4. 新規参加者向けのおすすめ行動
「今どうなっているか」を踏まえたうえで、これから入る人向けに、ざっくりこんな動き方がよさそうです：
Slackに参加して [#1_自己紹介](https://dd2030.slack.com/archives/C08HKET1YG3) にひと言書く
 どの領域（開発／政策／デザイン／運営／研究など）に興味があるかを書いておくと、誘われやすくなります。([デジタル民主主義2030](https://dd2030.org/history/week1_20250319/slack))
/history の「最新の週」のSlackまとめだけ読む
 すべてをさかのぼる必要はなく、直近1〜2週分を読むだけで「今の空気」がだいたい掴めます。([デジタル民主主義2030](https://dd2030.org/history))
自分の関心に近いチャンネルを1〜2個だけ開く
例）広聴AIなら 2_開発_広聴ai / 2_開発_広聴ai_アルゴリズム開発
いどばたなら 2_開発_いどばた
コミュニティ運営なら 2_コミュニティ運営 など
「いま困っていること・知りたいこと」を気軽に質問する
 ダイジェストにも書かれている通り、「どのチャンネルで聞いてもOK」という文化なので、
 「何から始めたらいいですか？」自体が立派な一歩です。([デジタル民主主義2030](https://dd2030.org/history/week36_20251119/slack))
ざっくりまとめると、DD2030は「立ち上げ期」を超えて、ツールもコミュニティもかなり厚みが出てきた「実験＋実装フェーズ」に入っている状態です。
「完成したサービスにユーザとして参加する」というより、
 「一緒に実験しながら“デジタル民主主義の新しい形“をつくっていく場」に飛び込む感じで捉えてもらうと、今の状況にフィットすると思います。

from [Slack #0_全体お知らせ](https://dd2030.slack.com/archives/C08FL58LK8V/p1763778724704149)

**コメント:** なし

---

### [Google Analytics を導入してアクセス解析をできるようにする](https://github.com/digitaldemocracy2030/website/issues/174)

**作成者:** shingo-ohki  
**作成日:** 2025-11-16T06:47:16Z  
**内容:**

web サイトへのアクセス状況の把握のために、https://dd2030.org のアクセス解析ができるとよい
特段の理由がなければ Google Analytics でよいのでは？

>ふと、https://dd2030.org/history ってどれくらいアクセスがあるのかなと思ったのですが、それは見れたりするのでしょうか？

何も仕込んでなかった気がするので、仕込めば見れるようになれます！

from [#2_広報_pr チャンネル](https://dd2030.slack.com/archives/C08K4CUB12T/p1763274225496959?thread_ts=1763164197.644219&cid=C08K4CUB12T)

**コメント:** なし

---

### 過去7日間に作成されたissue (0件)

### 過去7日間に更新されたissue（作成・クローズを除く）(2件)

### [今後の「プロジェクトの歴史」の更新を可能な限り自動化する](https://github.com/digitaldemocracy2030/website/issues/177)

**作成者:** shingo-ohki  
**作成日:** 2025-11-16T07:08:06Z  
**内容:**

内容なし

**コメント:** なし

---

### [毎週のプロジェクトの活動状況の更新処理が適切に動いていない](https://github.com/digitaldemocracy2030/website/issues/173)

**作成者:** shingo-ohki  
**作成日:** 2025-11-15T14:13:37Z  
**内容:**

https://github.com/digitaldemocracy2030/website/pull/171 を見ると、処理自体は毎週動いているが、week27 という同じブランチで新しい活動状況が作られてしまっている模様

<img width="863" height="535" alt="Image" src="https://github.com/user-attachments/assets/b97ef8c1-b8ba-4898-954a-c0a38f67c8ff" />

現状の処理は、（安全側に倒して）

1. 要約を作って Pull Request の draft を作る（GitHub Actions 自動)
1. Pull Request を ready にする（人）
1. review して merge する（人）

が毎週行われることを前提にしているが、2 が滞っていたために期待した動作になっていなかった

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (2件)

### [「初めての方へ」ページを追加](https://github.com/digitaldemocracy2030/website/pull/181)

**作成者:** shingo-ohki  
**作成日:** 2025-11-22T03:48:00Z  
**変更:** +106 -1 (3ファイル)  
**マージ日:** 2025-11-23T12:26:41Z  
**内容:**

#180 
ひとまずこのようなページを追加しておいて、定期的にこのページの中身を更新するようにすればよいのではないか？
ということで、たたき台として出してみます。

**コメント:** なし

---

### [Week36 Summary Update](https://github.com/digitaldemocracy2030/website/pull/179)

**作成者:** github-actions[bot]  
**作成日:** 2025-11-19T03:54:31Z  
**変更:** +311 -0 (5ファイル)  
**マージ日:** 2025-11-19T13:23:28Z  
**内容:**

Auto-generated weekly summaries for week36

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(8件)

### [Week27 Summary Update](https://github.com/digitaldemocracy2030/website/pull/171)

**作成者:** github-actions[bot]  
**作成日:** 2025-09-17T03:45:08Z  
**変更:** +207 -0 (4ファイル)  
**内容:**

Auto-generated weekly summaries for week27

**コメント:** なし

---

### [Week26 Summary Update](https://github.com/digitaldemocracy2030/website/pull/169)

**作成者:** github-actions[bot]  
**作成日:** 2025-09-10T09:28:14Z  
**変更:** +220 -0 (5ファイル)  
**内容:**

Auto-generated weekly summaries for week26

**コメント:** なし

---

### [Slack招待リンクを再修正](https://github.com/digitaldemocracy2030/website/pull/161)

**作成者:** kuboon  
**作成日:** 2025-08-19T04:32:46Z  
**変更:** +5 -5 (4ファイル)  
**内容:**

#160 １箇所じゃなかった。。。

**コメント:** なし

---

### [week21](https://github.com/digitaldemocracy2030/website/pull/155)

**作成者:** kuboon  
**作成日:** 2025-08-06T09:56:02Z  
**変更:** +339 -0 (5ファイル)  
**内容:**

内容なし

**コメント:** なし

---

### [Replace Twitter links with proper embeds using XEmbed component](https://github.com/digitaldemocracy2030/website/pull/142)

**作成者:** Shutaro+Devin  
**作成日:** 2025-07-16T10:17:44Z  
**変更:** +18 -29 (1ファイル)  
**内容:**

# Replace Twitter links with proper embeds using XEmbed component

## Summary

Replaced 7 simple Twitter links on the case/idobata page with proper Twitter embeds using the `XEmbed` component from the existing `react-social-media-embed` library. This provides a much richer user experience by displaying full tweet content, user profiles, engagement metrics, and interactive elements directly on the page instead of requiring users to click external links.

**Key changes:**
- Imported `XEmbed` from `react-social-media-embed` 
- Replaced all 7 `<a>` elements pointing to Twitter URLs with `<XEmbed>` components
- Added `'use client'` directive and converted from `async function` to regular function due to React server component compatibility issues
- Removed outer border styling based on user feedback to eliminate "frame within frame" visual issue

## Review & Testing Checklist for Human

- [ ] **Performance testing** - Check page load time with network throttling to ensure 7 simultaneous embed loads don't significantly degrade performance, especially on mobile/slow connections
- [ ] **Fallback behavior verification** - Test with network issues or ad blockers to ensure embeds degrade gracefully and don't break the page layout when they fail to load
- [ ] **SEO impact assessment** - Verify the 'use client' conversion doesn't negatively affect SEO, initial page load performance, or hydration behavior compared to the original server component

**Recommended test plan:** Load the page fresh with network throttling enabled, test on mobile devices, verify embeds load properly, check for console errors, and test fallback behavior with blocked network requests.

---

### Diagram

```mermaid
%%{ init : { "theme" : "default" }}%%
flowchart TD
    PageTSX["app/case/idobata/page.tsx<br/>(Main file edited)"]:::major-edit
    XEmbed["XEmbed component<br/>(react-social-media-embed)"]:::context
    TwitterAPI["Twitter oEmbed API<br/>(External service)"]:::context
    
    PageTSX -->|"imports XEmbed"| XEmbed
    XEmbed -->|"fetches tweet data"| TwitterAPI
    
    subgraph "Tweet URLs (7 total)"
        Tweet1["@kazuneiwasa/1924801224198783367"]:::context
        Tweet2["@nishio/1923636525365068238"]:::context  
        Tweet3["@takahiroanno/1923253426747736186"]:::context
        TweetMore["... 4 more tweets"]:::context
    end
    
    PageTSX -->|"renders embeds for"| Tweet1
    PageTSX -->|"renders embeds for"| Tweet2
    PageTSX -->|"renders embeds for"| Tweet3
    PageTSX -->|"renders embeds for"| TweetMore
    
    subgraph Legend
        L1["Major Edit"]:::major-edit
        L2["Minor Edit"]:::minor-edit  
        L3["Context/No Edit"]:::context
    end
    
    classDef major-edit fill:#90EE90
    classDef minor-edit fill:#87CEEB
    classDef context fill:#FFFFFF
```

### Notes

- **React 19 compatibility issue**: The react-social-media-embed library had peer dependency warnings with React 19, requiring conversion from server component to client component
- **Performance consideration**: Loading 7 embeds simultaneously may impact page performance - monitor this in production
- **External dependency**: Embeds depend on Twitter's service availability and could fail to load in some network conditions
- **User feedback incorporated**: Removed outer border styling after user noted "frame within frame" visual issue
- **User requested this feature** via Slack: @blu3mo asked if tweets could be embedded "embedみたいに埋め込めない？" instead of showing as simple links

**Link to Devin run:** https://app.devin.ai/sessions/d3a86ce61ea84a388ba3269a78c26e23  
**Requested by:** @blu3mo (shutaro.aoyama@gmail.com)

![Current implementation showing Twitter embeds without borders](https://devin-public-attachments.s3.dualstack.us-west-2.amazonaws.com/attachments_private/org_59RHUaMtRiE9rGRu/bcbab853-30f5-44ba-a5e0-ba436a6c6510?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAT64VHFT7U7DJ4QUR%2F20250718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250718T083729Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLWVhc3QtMSJHMEUCIDTNaGwq7GH0KFQDi0MUi1Tb4w%2FMf%2BRszUaJH3vO4uabAiEAvO32sQzsZcwjrBu9dSwCn120h72DM%2FG8zlwJXX3iK54qwAUIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgwyNzI1MDY0OTgzMDMiDK%2F5RUyTBivoMxFJ2SqUBTTMcOPoZoF0ljHmQ0c4ydLxQB6E%2BGdhPwJ5vAbLQ5jVC7c1eGynkXOFpgabKmekyD3tGy7JC0ro1YKdfOth8Z5jqds4fsHAxDC5mUk1hQmh2MFfP2SRZTdqptYkhOjilei%2FVg%2BDdKQMxgYyfvYPwRcd0NUpBIQj14dMvnUaT72tKVPZXmhHxSG7tZKOLfFJq87HQWQoeUPro1i6eKUoVeiAlc4IX4UAHwWmgkAgduRsiuSII6pU4l2Wzo53ewMUWPXIEIxCI%2Fq3UOFrJMu%2BF3btH2M6RqfBaJY5RUqVt5kFKuxOfIitZ%2F4Bwv6HHwovv4Auhv%2Fq1QjTf1PhvIiUTheEoFbzX0GKdH7PAnf44XpWpoZ7%2FimuvbLbeg6%2Fwfrk7FqP0kbptjoHlIZvwfkVp6iqzjO7Cd4KE4upNOUI7D3JxQF8%2FH8opPXVjLjR4kj9GHBDbKhdTITKx0YfSxlPjA7gku1i%2F3Bnx%2FJMvxAx%2B2WYi6kpzLOYPqbtXhH5gDnbn%2FZDVrRrtCRHrmxu%2FsL4Muv7NltGiFdemsuKGY1HDf15lYkirtETqZcQX6i3lyuLDCCOCwST8WwsXjBa1QEcuqQs5GUExXaHTcgKWVJ4oi1VBjTy%2BhvCWSr50yRI6Er30B9LlPXQqewndlIoqmqF%2FuE%2FY%2FhGj%2FcP3tLTrrpxwXBf%2Bn34VOaT85fxiVH0BaXi4fySy38TFgSHXA2JSowvTNP2w%2FQX%2F5Irmz5tqxhqSmHNDmk5%2FvPEbCGYwgk%2BpW%2BtcN0uBvRbvr2T7IwlolL8PFAFvLVKWFIMcC0WQ4nBOxyLQJ5FsmBJvrKD7ZCQwsl6Ul%2FILuPUp%2B5CC%2BgHN803PGCl8OCtyoMi6eyLfLk3KQUwh3LOPTCCjejDBjqYAejtL2zVJW1N2rMpG0Teedtg6pBlXoCbLQiWP5OZQviGr%2B07ijJt62AXbrpPVG3gACq57aBMVwM%2BKnOD9aF68DY2WdKFgoNwBbb8N2psR1LUMu2nKYLa%2B8LcjNTP8YADrlQrqMqccp%2BBTSOP1DstcphImhOM3mKvLyi4oZPFhyTMUieotKCSHjY5ze3RHTvrnSky%2BTf9IndK&X-Amz-Signature=8275a437e525f0e5fcf651836ba1917fd9db86eb7a751edd37d90527289617c7)

**コメント:** なし

---

### [week17](https://github.com/digitaldemocracy2030/website/pull/141)

**作成者:** kuboon  
**作成日:** 2025-07-12T14:19:24Z  
**変更:** +271 -0 (5ファイル)  
**内容:**

(まだ手作業している)
(手作業が手慣れてきたので数分でできてしまう)
(自動化。。。)

**コメント:** なし

---

### [Add comprehensive idobata case study content](https://github.com/digitaldemocracy2030/website/pull/140)

**作成者:** Shutaro+Devin  
**作成日:** 2025-07-09T11:16:28Z  
**変更:** +231 -2 (3ファイル)  
**内容:**


# Add comprehensive idobata case study content

## Summary

This PR adds comprehensive case study content to the `/case/idobata` page, including detailed sections about いどばたビジョン and いどばた政策 with relevant links and user reaction tweets. The content includes:

- **いどばたビジョン section** with チームみらい「みらいいどばた会議」 information and user reaction tweets
- **立憲民主党 section** with press conference link (future implementation)
- **いどばた政策 section** with チームみらい マニフェスト information and related tweets
- **External links** to kaigi.team-mir.ai, policy.team-mir.ai, and cdp-japan.jp
- **Tweet links** displayed as styled boxes (replaced embedded tweets due to React 19 compatibility issues)

**Note**: Originally attempted to use `react-social-media-embed` for tweet embedding, but encountered compatibility issues with React 19. Replaced with styled link boxes that maintain functionality while avoiding build errors.

## Review & Testing Checklist for Human

- [ ] **Verify all external links work correctly** - Test kaigi.team-mir.ai, policy.team-mir.ai, cdp-japan.jp, and all X.com tweet links
- [ ] **Check Japanese content accuracy** - Review descriptions and explanations for accuracy and appropriate tone
- [ ] **Test visual design consistency** - Verify styling matches existing case study pages across different screen sizes
- [ ] **Validate tweet link boxes** - Confirm styled tweet boxes are an acceptable replacement for embedded tweets
- [ ] **Test mobile responsiveness** - Check page layout and functionality on mobile devices

**Recommended test plan**: Navigate to `/case/idobata`, click all external links to verify they work, check visual consistency with `/case/polimoney`, and test on mobile.

---

### Diagram

```mermaid
%%{ init : { "theme" : "default" }}%%
graph TB
    subgraph Legend
        L1["Major Edit"]:::major-edit
        L2["Minor Edit"]:::minor-edit  
        L3["Context/No Edit"]:::context
    end
    
    A["app/case/idobata/page.tsx"]:::major-edit
    B["package.json"]:::minor-edit
    C["package-lock.json"]:::minor-edit
    D["components/ui/button.tsx"]:::context
    E["components/CoCreation.tsx"]:::context
    F["@mui/icons-material"]:::context
    
    A --> D
    A --> E
    A --> F
    B --> C
    
    A -.-> G["External Links<br/>kaigi.team-mir.ai<br/>policy.team-mir.ai<br/>cdp-japan.jp"]
    A -.-> H["Tweet Links<br/>X.com URLs"]
    
    classDef major-edit fill:#90EE90
    classDef minor-edit fill:#87CEEB  
    classDef context fill:#FFFFFF
```

### Notes

- **Compatibility Issue**: Had to work around React 19 compatibility issues with `react-social-media-embed` library
- **Design Decision**: Replaced embedded tweets with styled link boxes to maintain functionality while avoiding build errors
- **External Dependencies**: Page now depends on several external URLs remaining accessible
- **Session Info**: Link to Devin run: https://app.devin.ai/sessions/5bbde99b9e37496bbc90615c611de28e
- **Requested by**: @blu3mo

![Local testing screenshot](https://devin-public-attachments.s3.dualstack.us-west-2.amazonaws.com/attachments_private/org_59RHUaMtRiE9rGRu/c6121e68-1d67-443a-96ef-8aae216c2f8e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAT64VHFT75VOUNC26%2F20250709%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250709T111728Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCICju2BKZTp18Hzg%2BaWUR6zidP35rEZhAzxZe%2BkCuieyBAiEArMMZgL5Q5z8bW%2FKVjT2esaSBmm2X2j1CK9nfZmWSerkqwAUIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgwyNzI1MDY0OTgzMDMiDMeYqk2dlniHQWkrgiqUBZ0pVjCefJJ3SDoiPNnEHrKnx%2BnAQdsY%2Fa8gz4NdqyRO5N%2FriKq00IpjB3jCGBcliDx70E4yIUBWE2J%2Fwe38o6s%2FM4MSrNPLp5exGAXay3%2B3P5RUym0FPUxNFuWQx2PymvxypkHbQd%2BQiVRLaPMDPVtNlP76lhfepS2Uxt4DEMijf8%2Bc%2BMYGWfXLThm32AqDieD80I1bw1xkctVvm5RM1SDO9ekb%2BEB4knyCaWLJaNV9MnDEPAfaj3CT4aAKkXXPZIVo00cWQSPwuKzOgkJ9LUOAzcpPg%2B6ImnKwFAYudr7SkU8Fszr2%2BuUOheYcwFn9I2IJbVph%2FFbQGenufabHvzhfr03hjOF8NLoOdBwgqNpeg93L9F%2BROYq2Azayxcftc3ZZgP2Dk660PYhyY5BR5Z2Puyb6kOxeSyYBjCnRzai1O%2FRVf7TFWXS0TPZOKOdcrdWwqKBZL1n81nwyKQelu0Jba%2B5IW3eayJebpQso4KlqiHUuRK06ra%2BwBxihxTp3tscdfNq61iavdrCPVAu8aZeGNOeABX7556GQPr760UtwT3cdlXWWtMarjwYhVaBkqTwVM49P%2FPqwja4RsuQv7Sa24G%2Bkubas7f31JkuH3KxxO7jrmefV5T7f2WjHRblfrjHMFqRic55yaXtwjzMo1Aa4aUS01cQTgryk3T%2BS7lYOXQ5JMv1ufvNUg6X4QDXEz5X8oNDkBys9JQgA3iI9ca8tUT1btFuNOfaht%2B%2FWv%2BGnF5TbuBHZfKJK7K4crM8dbSOgSF0ZzAd6cLgi3ujZXLDRrNJCaFgHXNNBIcS7hOncP5zx20f0iwLvqwS0yRowgMdfQ9dY12jfZtVHXycy7O256PU8WaRnAb%2B8hJMxio%2FUhJ6c9zClmLnDBjqYAZs70NEnacU85pxrhm5bnShk%2BQvkVFrIIJd%2BfN%2BOAj4ZiVtM%2BY53a1Tlzb%2Bjh1o7oXhH%2F%2BMIWLahusnPldlcoLftzh6fL3zqG9GsXlaIe%2FW6no9ZewdiYzl%2B%2FKkSix2xSS8hJ84GSfxhbhpb%2FzfDzZ4A9kP6S%2BM9tC%2BJHYpv23nABhoKPIIqm404FGixViiH9H8TNIRsuwaD&X-Amz-Signature=c61eec5bbc535d94d99c6bf9fccad2dff0e637002e2733fcf675e61317df54ee)


**コメント:** なし

---

### [Fix CSS and image loading on top and history pages in PR preview](https://github.com/digitaldemocracy2030/website/pull/95)

**作成者:** nishio  
**作成日:** 2025-05-19T15:12:38Z  
**変更:** +37 -5 (5ファイル)  
**内容:**

# Fix CSS and image loading on top and history pages in PR preview

トップページとhistoryページのPRプレビューでCSSや画像がロードされない問題を修正しました。

## 変更内容
- トップページの画像参照を`basePath`対応に修正
- CSSの読み込みを動的に行い`basePath`を考慮するように変更
- カスタムイメージローダーを追加して画像パスの解決を改善

この変更により、PRプレビュー環境でもトップページとhistoryページのCSSと画像が正しく表示されるようになります。

## テスト結果
- ローカルで`NEXT_PUBLIC_PR_NUMBER=test npm run build`を実行し、ビルドが正常に完了することを確認しました
- 静的エクスポートが正しく生成され、トップページとhistoryページが含まれていることを確認しました

Link to Devin run: https://app.devin.ai/sessions/150211bb7b2c456c83fde7a0385003f0
User: NISHIO Hirokazu


**コメント:** なし

---

