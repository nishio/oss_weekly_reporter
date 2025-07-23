# GitHub レポート: digitaldemocracy2030/website

期間: 2025-07-16T12:37:02.771107+09:00 から 2025-07-23T12:37:02.771107+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (1件)

### [polimoney紹介コーナーにpolimoneyサイトリンクを貼る](https://github.com/digitaldemocracy2030/website/issues/144)

**作成者:** shumizu418128  
**作成日:** 2025-07-20T10:45:35Z  
**内容:**

https://dd2030.org/ （polimoneyの紹介をしている部分）
https://dd2030.org/polimoney

これらのヘッダーと画像の間にURL https://polimoney.dd2030.org/ を貼りたい

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (1件)

### [week17](https://github.com/digitaldemocracy2030/website/pull/141)

**作成者:** kuboon  
**作成日:** 2025-07-12T14:19:24Z  
**変更:** +271 -0 (5ファイル)  
**マージ日:** 2025-07-16T10:20:20Z  
**内容:**

(まだ手作業している)
(手作業が手慣れてきたので数分でできてしまう)
(自動化。。。)

**コメント:** なし

---

### 過去7日間に作成されたPR (2件)

### [week18](https://github.com/digitaldemocracy2030/website/pull/143)

**作成者:** kuboon  
**作成日:** 2025-07-17T02:52:11Z  
**変更:** +328 -0 (5ファイル)  
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

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

