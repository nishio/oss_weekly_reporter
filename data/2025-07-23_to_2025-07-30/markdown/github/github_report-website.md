# GitHub レポート: digitaldemocracy2030/website

期間: 2025-07-23T12:38:00.687451+09:00 から 2025-07-30T12:38:00.687451+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (4件)

### [Slack への参加ができない（もしくは受付終了の案内がされていない）](https://github.com/digitaldemocracy2030/website/issues/153)

**作成者:** grassfieldk  
**作成日:** 2025-07-29T12:14:58Z  
**内容:**

※ 本リポジトリへのコントリビューション規約が見当たらなかったため外部のものですが Issue を立てました、問題あれば遠慮なく削除ください

https://dd2030.org/co-creation 下部にある Slack への参加ボタンからワークスペースへの参加ができませんでした

私は本日（2025/07/29）参加しようとしたのですが、
参加ボタンから Slack へアクセスしてメールで届いた認証コードを入力するとワークスペースに存在しないユーザーである旨のメッセージが表示され、参加ができませんでした

[安野氏のツイート](https://x.com/takahiroanno/status/1900073162370658464) にある招待リンクはすでに有効期限が切れているところを見ると
現在はもう参加を募っていないのでしょうか？

もし有効期限が切れているだけであればリンクなどの更新をしていただきたいです
募集を終了しているのであればその旨をサイトに記載するか、Slack のリンクを削除するかしたほうがよいのではと思いました

**コメント:** なし

---

### [textlint を入れてもいいかもしれない](https://github.com/digitaldemocracy2030/website/issues/151)

**作成者:** noritaka1166  
**作成日:** 2025-07-26T12:34:15Z  
**内容:**

現在はそこまでページ数がないので問題ない気もしますが、今後増えてきた際に文言がバラバラになってしまう可能性があるため、  
文章の校正を行う textlint を入れてもいいかもしれないなと思いました。  
textlint は、 React や Vue の日本語のドキュメントにも使われているツールです。

- <https://textlint.org/>
- <https://github.com/textlint/textlint>
- <https://efcl.info/2015/09/10/introduce-textlint/>

**コメント:** なし

---

### [[Question]Discouseサーバについて](https://github.com/digitaldemocracy2030/website/issues/147)

**作成者:** takeruhukushima  
**作成日:** 2025-07-26T05:31:11Z  
**内容:**

dd2030のリポジトリ内にdiscourse botのリポジトリを拝見しましたが、公式に提供されたdiscouseサーバーは存在していますか？

仮に存在していない場合、今後作る予定はありますか？

ご回答いただけますと幸いです。

**コメント:** なし

---

### [CMSを導入する](https://github.com/digitaldemocracy2030/website/issues/145)

**作成者:** moai-redcap  
**作成日:** 2025-07-26T02:04:31Z  
**内容:**

https://lume.land/cms/

azureにホスティング

詳細はモアイまで

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (2件)

### [week19](https://github.com/digitaldemocracy2030/website/pull/152)

**作成者:** kuboon  
**作成日:** 2025-07-28T03:58:31Z  
**変更:** +386 -0 (5ファイル)  
**マージ日:** 2025-07-28T05:02:31Z  
**内容:**

内容なし

**コメント:** なし

---

### [week18](https://github.com/digitaldemocracy2030/website/pull/143)

**作成者:** kuboon  
**作成日:** 2025-07-17T02:52:11Z  
**変更:** +328 -0 (5ファイル)  
**マージ日:** 2025-07-26T01:54:46Z  
**内容:**

内容なし

**コメント:** なし

---

### 過去7日間に作成されたPR (4件)

### [chore: npm audit fix 実行](https://github.com/digitaldemocracy2030/website/pull/150)

**作成者:** noritaka1166  
**作成日:** 2025-07-26T11:28:11Z  
**変更:** +241 -225 (1ファイル)  
**内容:**

`npm audit` 実行時にいくつか脆弱性が出ていたので `npm audit fix` を実行しました  

`npm run dev` で問題なく動作すること、`npm run build` と `npm run lint` が動くことを確認済み
```
@eslint/plugin-kit  <0.3.3
Severity: high
@eslint/plugin-kit is vulnerable to Regular Expression Denial of Service attacks through ConfigCommentParser - https://github.com/advisories/GHSA-xffm-g5w8-qvg7
fix available via `npm audit fix`
node_modules/@eslint/plugin-kit
  eslint  9.10.0 - 9.26.0
  Depends on vulnerable versions of @eslint/plugin-kit
  node_modules/eslint

brace-expansion  1.0.0 - 1.1.11 || 2.0.0 - 2.0.1
brace-expansion Regular Expression Denial of Service vulnerability - https://github.com/advisories/GHSA-v6h2-p8h4-qcjw
brace-expansion Regular Expression Denial of Service vulnerability - https://github.com/advisories/GHSA-v6h2-p8h4-qcjw
fix available via `npm audit fix`
node_modules/@typescript-eslint/typescript-estree/node_modules/brace-expansion
node_modules/brace-expansion

next  15.3.0 - 15.3.2
Next.js has a Cache poisoning vulnerability due to omission of the Vary header - https://github.com/advisories/GHSA-r2fc-ccr8-96c4
fix available via `npm audit fix`
node_modules/next

4 vulnerabilities (2 low, 2 high)
```

**コメント:** なし

---

### [refactor: オプショナルチェーンを使用](https://github.com/digitaldemocracy2030/website/pull/149)

**作成者:** noritaka1166  
**作成日:** 2025-07-26T11:10:11Z  
**変更:** +1 -1 (1ファイル)  
**内容:**

より簡潔で読みやすくするため、代わりにオプショナルチェーンを使用するようにリファクタリングしました

**コメント:** なし

---

### [Footerコンポーネントから不要なspanを削除](https://github.com/digitaldemocracy2030/website/pull/148)

**作成者:** noritaka1166  
**作成日:** 2025-07-26T11:05:31Z  
**変更:** +0 -5 (1ファイル)  
**内容:**

Footer に 空の spanタグが入っていますが、不要かと思うので削除しました
<img width="592" height="116" alt="スクリーンショット 2025-07-26 午後8 01 21" src="https://github.com/user-attachments/assets/8d25d99b-0f83-40b9-8e4f-ebf03da2a39b" />

これにより少しリンク同士の間隔が狭まりましたが、問題ないレベルかと思います。
<img width="582" height="145" alt="スクリーンショット 2025-07-26 午後8 03 59" src="https://github.com/user-attachments/assets/e504b2d3-5218-4b82-afb8-0971edf8158c" />


**コメント:** なし

---

### [feat: Polimoney Webサイトのリンクの追加](https://github.com/digitaldemocracy2030/website/pull/146)

**作成者:** takeruhukushima  
**作成日:** 2025-07-26T05:26:05Z  
**変更:** +38 -1 (4ファイル)  
**内容:**

トップページとPolimoneyのページにPolimoneyのウェブサイトへのリンクを追加しました。

fixes #144 

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

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

