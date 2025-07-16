# GitHub レポート: digitaldemocracy2030/website

期間: 2025-07-09T12:36:23.050684+09:00 から 2025-07-16T12:36:23.050684+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (1件)

### [Add comprehensive idobata case study content](https://github.com/digitaldemocracy2030/website/pull/140)

**作成者:** Shutaro+Devin  
**作成日:** 2025-07-09T11:16:28Z  
**変更:** +231 -2 (3ファイル)  
**マージ日:** 2025-07-11T14:37:14Z  
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

### 過去7日間に作成されたPR (1件)

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

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

