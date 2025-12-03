# GitHub レポート: digitaldemocracy2030/website

期間: 2025-11-26T12:32:12.180413+09:00 から 2025-12-03T12:32:12.180413+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (1件)

### [Week37 Summary Update](https://github.com/digitaldemocracy2030/website/pull/182)

**作成者:** github-actions[bot]  
**作成日:** 2025-11-26T03:57:53Z  
**変更:** +314 -0 (5ファイル)  
**マージ日:** 2025-11-27T13:47:01Z  
**内容:**

Auto-generated weekly summaries for week37

**コメント:** なし

---

### 過去7日間に作成されたPR (1件)

### [test](https://github.com/digitaldemocracy2030/website/pull/183)

**作成者:** kuboon  
**作成日:** 2025-12-01T08:20:24Z  
**変更:** +1 -1 (1ファイル)  
**内容:**

内容なし

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(12件)

### [Week36 Summary Update](https://github.com/digitaldemocracy2030/website/pull/179)

**作成者:** github-actions[bot]  
**作成日:** 2025-11-19T03:54:31Z  
**変更:** +311 -0 (5ファイル)  
**内容:**

Auto-generated weekly summaries for week36

**コメント:** なし

---

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

### [week14](https://github.com/digitaldemocracy2030/website/pull/136)

**作成者:** kuboon  
**作成日:** 2025-06-18T05:50:22Z  
**変更:** +374 -0 (5ファイル)  
**内容:**

内容なし

**コメント:** なし

---

### [[WIP] update logo 途中まで](https://github.com/digitaldemocracy2030/website/pull/122)

**作成者:** masatosasano2  
**作成日:** 2025-05-27T00:19:36Z  
**変更:** +18 -169 (36ファイル)  
**内容:**

公式ポータルのロゴを差し替えようとしたが、以下2点が難しそうなので中断。
フロントエンドに詳しい方に後続をお任せしたいです。

- [詳細デザイン案](https://github.com/digitaldemocracy2030/website/issues/121)が上がっている
- faviconは単体ファイルではなく複数必要（かなり色々ある。詳細は下記realfavicongeneratorの指示に従うと出てくる）

後者については、[こちらの手順書](https://medium.com/@davegray_86804/next-js-favicon-svg-icon-apple-chrome-icons-2e3c686ede79)と[realfavicongenerator](https://realfavicongenerator.net/favicon-generator/nextjs)に行き着いたものの、なぜか生成された各種ロゴが白黒になってしまい、解決策を見つけられていない。

現時点の実装までで、一応以下はできているので、ひとまずマージするのも手かもしれない。
- 公式サイトのfavicon、ヘッダ、Chrome の New Tab でのアイコン

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

### [活用事例ページをmdで管理できるようにする。](https://github.com/digitaldemocracy2030/website/pull/89)

**作成者:** yusasa16  
**作成日:** 2025-05-18T11:31:17Z  
**変更:** +221 -81 (12ファイル)  
**内容:**

## 関連イシュー
#40 

## 備考
[広聴AI](https://dd2030.org/case/kouchou-ai)ページで使われているリンクボタンの見た目を
- 横幅が親要素からはみ出している
- マークダウンでは文章中で使われているリンクとのスタイルの使い分けが難しい

という理由から下線を表示する見た目に変更しています。

また、ページ詳細のスタイルについてはapp/global.cssファイルに直接記載しています。
- ファイルを分けた方がよいか。また希望のファイルパスはあるか。
- `@apply` を使うことについては問題ないか。通常のCSSのプロパティに変換した方がよいか。

についても調整意見ありましたらお願いします。

**コメント:** なし

---

