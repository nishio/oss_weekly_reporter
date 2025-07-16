# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-07-09T12:36:26.404518+09:00 から 2025-07-16T12:36:26.404518+09:00 まで

## Issues

### 過去7日間に完了されたissue (1件)

### [レポート選択プルダウンメニューを年で降順ソート（新しい年順）に変更](https://github.com/digitaldemocracy2030/polimoney/issues/150)

**作成者:** soranjiro  
**作成日:** 2025-07-14T12:40:59Z  
**内容:**

## 解決・改善したいこと

レポート選択のプルダウンメニューにおいて、レポートが順不同で表示されており、年数が増えていった時や昨年のレポートを参照したい時、ユーザーが特定の年のレポートを探す時に時間がかかってしまう問題があります。

<img width="1107" height="320" alt="Image" src="https://github.com/user-attachments/assets/2f131ab0-a353-436e-8815-65ec80ca6bd1" />

政治家の収支報告書を年代順で確認したいユーザーが、最新のレポートから順番に見たいと思った時に、現在の表示順では目的のレポートを素早く見つけることができませんでした。特に、複数年のレポートがある政治家の場合、最新の情報を優先的に確認したいというニーズが高いため、直感的な並び順（新しい年から古い年の順）での表示が求められると思います。

この改善により、ユーザーは最新のレポートを上部で素早く見つけることができ、時系列順でデータを把握しやすくなります。

## 具体的な実現方法・実装方法の概要

`BoardSummary.tsx`コンポーネントの`allReports`配列に年での降順ソート機能を追加します。



**コメント:** なし

---

### 過去7日間に作成されたissue (1件)

### [toolsのテストが落ちる](https://github.com/digitaldemocracy2030/polimoney/issues/148)

**作成者:** shumizu418128  
**作成日:** 2025-07-13T07:16:25Z  
**内容:**

## 問題

<!-- どこでどのような問題が起きているかを教えてください。問題の発生する画面の URL や、問題が発生しているときのスクリーンショットや録画を添付していただけると理解の助けになります。 -->

<!-- この問題が解決されないと、どのような人がどのように困るか、できれば利用者を主語にして記載してください。 -->

NISHIOさんからの報告。現時点ではこれしか情報が無いのでコメントに詳しく調べた結果を残します

<img width="720" height="506" alt="Image" src="https://github.com/user-attachments/assets/3bb22aab-5c41-42af-99b0-b2ae2949a7c9" />

## 再現手順（未記入でも構いません）

1.
1.
1.

<!-- どのようにしたらバグが再現されるか、わかれば記載して下さい。 -->

## 修正方法の概要（未記入でも構いません）


**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(1件)

### [データベース移行](https://github.com/digitaldemocracy2030/polimoney/issues/32)

**作成者:** nanocloudx  
**作成日:** 2025-04-30T13:49:38Z  
**内容:**

既に公開している数件のデータはデモとして GitHub Pages に公開している
今後の流れとしてより沢山のデータを扱うことを見越して、データを Postgres に記録していく

同様にレポートは「ブラウザ→API→Postgres」からデータを取得して表示する仕組みに変更する

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (8件)

### [Add dynamic page titles for demo pages](https://github.com/digitaldemocracy2030/polimoney/pull/152)

**作成者:** kuboon+Devin  
**作成日:** 2025-07-15T04:54:24Z  
**変更:** +45 -0 (6ファイル)  
**マージ日:** 2025-07-15T12:46:40Z  
**内容:**


# Add dynamic page titles for demo pages

## Summary

This PR implements dynamic page titles for all demo pages by adding `generateMetadata()` functions that display politician names in the browser tab title. Instead of all demo pages showing the generic "Polimoney (ポリマネー)" title, they now show "{politician name} | Polimoney (ポリマネー)" format.

**Changes made:**
- Added `generateMetadata()` function to 6 demo pages: `demo-takahiro-anno-2024`, `demo-ryosuke-idei-2024`, `demo-koki-fujisaki-2024`, `demo-koki-fujisaki-2023`, `demo-koki-fujisaki-2022`, and `demo-example`
- Added `import type { Metadata } from 'next';` to all affected pages
- Handled two different data import patterns:
  - Direct import pattern: `data.profile.name` (takahiro-anno, ryosuke-idei, example)
  - getDataByYear pattern: `getDataByYear(year).profile.name` (all koki-fujisaki pages)

**Testing performed:**
- Verified browser titles display correctly for 4 demo pages locally
- Confirmed both data import patterns work as expected
- Linting passed with no issues

## Review & Testing Checklist for Human

- [ ] **Test all 6 demo pages** - Navigate to each demo page and verify browser tab titles show the correct politician name in format "{name} | Polimoney (ポリマネー)"
- [ ] **Check for missed demo pages** - Verify I didn't miss any other demo pages that should also have dynamic titles
- [ ] **Verify title format accuracy** - Ensure the spacing, characters, and format exactly match the requirement
- [ ] **Test other metadata preservation** - Confirm that description, OpenGraph tags, and other metadata still work properly
- [ ] **Test homepage unchanged** - Verify the homepage still shows the original generic "Polimoney (ポリマネー)" title

---

### Diagram

```mermaid
%%{ init : { "theme" : "default" }}%%
graph TD
    A["app/layout.tsx<br/>Global metadata"]:::context
    B["app/demo-takahiro-anno-2024/page.tsx<br/>+ generateMetadata()"]:::major-edit
    C["app/demo-ryosuke-idei-2024/page.tsx<br/>+ generateMetadata()"]:::major-edit
    D["app/demo-koki-fujisaki-2024/page.tsx<br/>+ generateMetadata()"]:::major-edit
    E["app/demo-koki-fujisaki-2023/page.tsx<br/>+ generateMetadata()"]:::major-edit
    F["app/demo-koki-fujisaki-2022/page.tsx<br/>+ generateMetadata()"]:::major-edit
    G["app/demo-example/page.tsx<br/>+ generateMetadata()"]:::major-edit
    
    H["data/demo-takahiroanno.ts<br/>profile.name"]:::context
    I["data/demo-ryosukeidei.ts<br/>profile.name"]:::context
    J["data/demo-kokifujisaki.ts<br/>getDataByYear().profile.name"]:::context
    K["data/demo-example.ts<br/>profile.name"]:::context
    
    A -.-> B
    A -.-> C
    A -.-> D
    A -.-> E
    A -.-> F
    A -.-> G
    
    H --> B
    I --> C
    J --> D
    J --> E
    J --> F
    K --> G
    
    subgraph Legend
        L1[Major Edit]:::major-edit
        L2[Minor Edit]:::minor-edit
        L3[Context/No Edit]:::context
    end
    
    classDef major-edit fill:#90EE90
    classDef minor-edit fill:#87CEEB
    classDef context fill:#FFFFFF
```

### Notes

- This change affects SEO metadata, so proper testing is important for search engine indexing
- The implementation handles two different data patterns found in the codebase
- Local testing confirmed titles work correctly, but comprehensive testing across all pages is recommended
- Session requested by kuboon (kuboon@trick-with.net) in Slack channel #8_devinと人間たちの部屋
- Link to Devin run: https://app.devin.ai/sessions/44adba67f4ca493e91f6dbac65812b39

**Screenshots from local testing:**
![demo-takahiro-anno-2024](https://devin-public-attachments.s3.dualstack.us-west-2.amazonaws.com/attachments_private/org_59RHUaMtRiE9rGRu/381e0ef7-09f2-4049-b0ef-cd7be9c17ef4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAT64VHFT7TYSZRBSD%2F20250715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250715T045525Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLWVhc3QtMSJIMEYCIQDWm0f5xNwE4uFnQsSDvL2zba9j9RRSp3bXNnJRorj8AQIhAMxa54w9jZbfH6E8r1wIBSdwm0wxeWLdX74DYfgY0%2BgSKrcFCD4QARoMMjcyNTA2NDk4MzAzIgy05CuwAYwdV0wySZEqlAVHjDKN%2FmcEZhBccd2Q5bMoYi75reRPmCrBDcG5Upsu%2BGzY5UXxoiMCkepiuLwSrMpWWzRuGRcUbbX4BZHOmfkM9ia9h5zM7LuwtubQVyVQqzRZFMPbsFscaI1KigfjAmZhIypXJxinNBU6%2FW%2BHAqXFDNtOv8xU%2Fsq1fI1cKkZXwIKPHVYPFVaSncS5bkCrAzjGQr9ozfAkB2Rn0GmolHBoIfMHoYgkBIdvXLBn78bnV3TqKzP4WeGbi3cILylGxxKcVLQj3rmVxdDK4ULG3azxKuApvj3ut53zvZ%2F8mKgmF%2FYRyA%2BjN2grCZAx%2BL6AVZD7hASl%2F9kwZxCINeW0EcALAJc2Iy%2BED7RoXe4Vlco%2FX9RYuok3dgIfWof5EzuaPriWft%2FbeC6gbk6dmkr2I3JEqj0qomB%2F3M4QdSJOpdyvkAAXiBsGot11mPELCINfPsTXnTua%2FqLJEh0uFdOCZSAd4xbfXoko8jjpuHyxrICq9E7YlnVQGOUUXhvLtcdh3B4w7eV%2F8Gu8GaIzPUl4BTt9xg2kV8fxOLOm29UpTiF7inVdYsW%2FVaKb5aG5dpvKvGLhQ6EQd61jNeTzzBkzE%2FxI%2Bryp076XMKZLp%2Fr1o%2FhNaJRva%2BsVQ%2BKSVGtsKLBpilpluJuQScxPQTQaQkbMGkWR9Q9rlY3yfeWZSLGuhrVAnuDqt6etqzoN%2FnKAQzNJcKOXvjygNkhVLcfTqziZ9EzaPeECIL%2BAMYd9RVlJT3gicSx1Ua15ZWUXNHyjobvjXZFPP0Lvbkz6mFTGWr9k4DT0lvModHid14TYxdm1ytXekA8yE4bZ0REw3s3JxW3o3N6gjq6wwIKzR%2BIHmI9h9F8uDeUjzdl%2F5Zq2z3nqHZJ8%2FAQ2TEUw6bvXwwY6lwHVjZPiUmX9Wo0ySjCrlA9rg4dbSij82JUtrx5nqF7g2tDIl%2Fwh%2FSjaBbzEPFqJNOux4xjf6%2Bgm1LbTOVCst7dkPFpzUPD6rWOnRiCWdcPkra9O7%2FZVljoOklr2CRzxPr8dZyh0GF1v4p97%2Fy2fx5%2FxOQF6Oh2gyL1uiFqmE8E3HugDpiyunEOHs%2BOPdInvToqNn1cZ41Gu&X-Amz-Signature=70e2f6ad06bdad49c596cf6031349bb8a7da05f6b4fcebec5bf39a621fa033e5)
![demo-ryosuke-idei-2024](https://devin-public-attachments.s3.dualstack.us-west-2.amazonaws.com/attachments_private/org_59RHUaMtRiE9rGRu/efbdf5e0-3c35-486a-836f-aa332bcce1fd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAT64VHFT7TYSZRBSD%2F20250715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250715T045525Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLWVhc3QtMSJIMEYCIQDWm0f5xNwE4uFnQsSDvL2zba9j9RRSp3bXNnJRorj8AQIhAMxa54w9jZbfH6E8r1wIBSdwm0wxeWLdX74DYfgY0%2BgSKrcFCD4QARoMMjcyNTA2NDk4MzAzIgy05CuwAYwdV0wySZEqlAVHjDKN%2FmcEZhBccd2Q5bMoYi75reRPmCrBDcG5Upsu%2BGzY5UXxoiMCkepiuLwSrMpWWzRuGRcUbbX4BZHOmfkM9ia9h5zM7LuwtubQVyVQqzRZFMPbsFscaI1KigfjAmZhIypXJxinNBU6%2FW%2BHAqXFDNtOv8xU%2Fsq1fI1cKkZXwIKPHVYPFVaSncS5bkCrAzjGQr9ozfAkB2Rn0GmolHBoIfMHoYgkBIdvXLBn78bnV3TqKzP4WeGbi3cILylGxxKcVLQj3rmVxdDK4ULG3azxKuApvj3ut53zvZ%2F8mKgmF%2FYRyA%2BjN2grCZAx%2BL6AVZD7hASl%2F9kwZxCINeW0EcALAJc2Iy%2BED7RoXe4Vlco%2FX9RYuok3dgIfWof5EzuaPriWft%2FbeC6gbk6dmkr2I3JEqj0qomB%2F3M4QdSJOpdyvkAAXiBsGot11mPELCINfPsTXnTua%2FqLJEh0uFdOCZSAd4xbfXoko8jjpuHyxrICq9E7YlnVQGOUUXhvLtcdh3B4w7eV%2F8Gu8GaIzPUl4BTt9xg2kV8fxOLOm29UpTiF7inVdYsW%2FVaKb5aG5dpvKvGLhQ6EQd61jNeTzzBkzE%2FxI%2Bryp076XMKZLp%2Fr1o%2FhNaJRva%2BsVQ%2BKSVGtsKLBpilpluJuQScxPQTQaQkbMGkWR9Q9rlY3yfeWZSLGuhrVAnuDqt6etqzoN%2FnKAQzNJcKOXvjygNkhVLcfTqziZ9EzaPeECIL%2BAMYd9RVlJT3gicSx1Ua15ZWUXNHyjobvjXZFPP0Lvbkz6mFTGWr9k4DT0lvModHid14TYxdm1ytXekA8yE4bZ0REw3s3JxW3o3N6gjq6wwIKzR%2BIHmI9h9F8uDeUjzdl%2F5Zq2z3nqHZJ8%2FAQ2TEUw6bvXwwY6lwHVjZPiUmX9Wo0ySjCrlA9rg4dbSij82JUtrx5nqF7g2tDIl%2Fwh%2FSjaBbzEPFqJNOux4xjf6%2Bgm1LbTOVCst7dkPFpzUPD6rWOnRiCWdcPkra9O7%2FZVljoOklr2CRzxPr8dZyh0GF1v4p97%2Fy2fx5%2FxOQF6Oh2gyL1uiFqmE8E3HugDpiyunEOHs%2BOPdInvToqNn1cZ41Gu&X-Amz-Signature=3cd9b37cf9a0f0b5d3b4c7e2c2956a555d61b4d05aaf6cd8a032921f13ccc1df)
![demo-koki-fujisaki-2024](https://devin-public-attachments.s3.dualstack.us-west-2.amazonaws.com/attachments_private/org_59RHUaMtRiE9rGRu/e2b13dd8-7c05-4bd9-a32f-58a9fee63d35?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAT64VHFT7TYSZRBSD%2F20250715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250715T045526Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLWVhc3QtMSJIMEYCIQDWm0f5xNwE4uFnQsSDvL2zba9j9RRSp3bXNnJRorj8AQIhAMxa54w9jZbfH6E8r1wIBSdwm0wxeWLdX74DYfgY0%2BgSKrcFCD4QARoMMjcyNTA2NDk4MzAzIgy05CuwAYwdV0wySZEqlAVHjDKN%2FmcEZhBccd2Q5bMoYi75reRPmCrBDcG5Upsu%2BGzY5UXxoiMCkepiuLwSrMpWWzRuGRcUbbX4BZHOmfkM9ia9h5zM7LuwtubQVyVQqzRZFMPbsFscaI1KigfjAmZhIypXJxinNBU6%2FW%2BHAqXFDNtOv8xU%2Fsq1fI1cKkZXwIKPHVYPFVaSncS5bkCrAzjGQr9ozfAkB2Rn0GmolHBoIfMHoYgkBIdvXLBn78bnV3TqKzP4WeGbi3cILylGxxKcVLQj3rmVxdDK4ULG3azxKuApvj3ut53zvZ%2F8mKgmF%2FYRyA%2BjN2grCZAx%2BL6AVZD7hASl%2F9kwZxCINeW0EcALAJc2Iy%2BED7RoXe4Vlco%2FX9RYuok3dgIfWof5EzuaPriWft%2FbeC6gbk6dmkr2I3JEqj0qomB%2F3M4QdSJOpdyvkAAXiBsGot11mPELCINfPsTXnTua%2FqLJEh0uFdOCZSAd4xbfXoko8jjpuHyxrICq9E7YlnVQGOUUXhvLtcdh3B4w7eV%2F8Gu8GaIzPUl4BTt9xg2kV8fxOLOm29UpTiF7inVdYsW%2FVaKb5aG5dpvKvGLhQ6EQd61jNeTzzBkzE%2FxI%2Bryp076XMKZLp%2Fr1o%2FhNaJRva%2BsVQ%2BKSVGtsKLBpilpluJuQScxPQTQaQkbMGkWR9Q9rlY3yfeWZSLGuhrVAnuDqt6etqzoN%2FnKAQzNJcKOXvjygNkhVLcfTqziZ9EzaPeECIL%2BAMYd9RVlJT3gicSx1Ua15ZWUXNHyjobvjXZFPP0Lvbkz6mFTGWr9k4DT0lvModHid14TYxdm1ytXekA8yE4bZ0REw3s3JxW3o3N6gjq6wwIKzR%2BIHmI9h9F8uDeUjzdl%2F5Zq2z3nqHZJ8%2FAQ2TEUw6bvXwwY6lwHVjZPiUmX9Wo0ySjCrlA9rg4dbSij82JUtrx5nqF7g2tDIl%2Fwh%2FSjaBbzEPFqJNOux4xjf6%2Bgm1LbTOVCst7dkPFpzUPD6rWOnRiCWdcPkra9O7%2FZVljoOklr2CRzxPr8dZyh0GF1v4p97%2Fy2fx5%2FxOQF6Oh2gyL1uiFqmE8E3HugDpiyunEOHs%2BOPdInvToqNn1cZ41Gu&X-Amz-Signature=610028b4506f9eb09260168a27b3d517407904ffbc1d71a4c2132b83077c847e)
![demo-example](https://devin-public-attachments.s3.dualstack.us-west-2.amazonaws.com/attachments_private/org_59RHUaMtRiE9rGRu/d362526d-b9fd-43f6-b1d2-5944ac236ae1?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAT64VHFT7TYSZRBSD%2F20250715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250715T045526Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLWVhc3QtMSJIMEYCIQDWm0f5xNwE4uFnQsSDvL2zba9j9RRSp3bXNnJRorj8AQIhAMxa54w9jZbfH6E8r1wIBSdwm0wxeWLdX74DYfgY0%2BgSKrcFCD4QARoMMjcyNTA2NDk4MzAzIgy05CuwAYwdV0wySZEqlAVHjDKN%2FmcEZhBccd2Q5bMoYi75reRPmCrBDcG5Upsu%2BGzY5UXxoiMCkepiuLwSrMpWWzRuGRcUbbX4BZHOmfkM9ia9h5zM7LuwtubQVyVQqzRZFMPbsFscaI1KigfjAmZhIypXJxinNBU6%2FW%2BHAqXFDNtOv8xU%2Fsq1fI1cKkZXwIKPHVYPFVaSncS5bkCrAzjGQr9ozfAkB2Rn0GmolHBoIfMHoYgkBIdvXLBn78bnV3TqKzP4WeGbi3cILylGxxKcVLQj3rmVxdDK4ULG3azxKuApvj3ut53zvZ%2F8mKgmF%2FYRyA%2BjN2grCZAx%2BL6AVZD7hASl%2F9kwZxCINeW0EcALAJc2Iy%2BED7RoXe4Vlco%2FX9RYuok3dgIfWof5EzuaPriWft%2FbeC6gbk6dmkr2I3JEqj0qomB%2F3M4QdSJOpdyvkAAXiBsGot11mPELCINfPsTXnTua%2FqLJEh0uFdOCZSAd4xbfXoko8jjpuHyxrICq9E7YlnVQGOUUXhvLtcdh3B4w7eV%2F8Gu8GaIzPUl4BTt9xg2kV8fxOLOm29UpTiF7inVdYsW%2FVaKb5aG5dpvKvGLhQ6EQd61jNeTzzBkzE%2FxI%2Bryp076XMKZLp%2Fr1o%2FhNaJRva%2BsVQ%2BKSVGtsKLBpilpluJuQScxPQTQaQkbMGkWR9Q9rlY3yfeWZSLGuhrVAnuDqt6etqzoN%2FnKAQzNJcKOXvjygNkhVLcfTqziZ9EzaPeECIL%2BAMYd9RVlJT3gicSx1Ua15ZWUXNHyjobvjXZFPP0Lvbkz6mFTGWr9k4DT0lvModHid14TYxdm1ytXekA8yE4bZ0REw3s3JxW3o3N6gjq6wwIKzR%2BIHmI9h9F8uDeUjzdl%2F5Zq2z3nqHZJ8%2FAQ2TEUw6bvXwwY6lwHVjZPiUmX9Wo0ySjCrlA9rg4dbSij82JUtrx5nqF7g2tDIl%2Fwh%2FSjaBbzEPFqJNOux4xjf6%2Bgm1LbTOVCst7dkPFpzUPD6rWOnRiCWdcPkra9O7%2FZVljoOklr2CRzxPr8dZyh0GF1v4p97%2Fy2fx5%2FxOQF6Oh2gyL1uiFqmE8E3HugDpiyunEOHs%2BOPdInvToqNn1cZ41Gu&X-Amz-Signature=e74cd3b65868ec292a437929650a2a7005d7c31ea69babd1fee560ae13df7282)


**コメント:** なし

---

### [feat: レポート選択プルダウンを年で降順ソートする機能を追加](https://github.com/digitaldemocracy2030/polimoney/pull/151)

**作成者:** soranjiro  
**作成日:** 2025-07-14T13:03:52Z  
**変更:** +2 -2 (1ファイル)  
**マージ日:** 2025-07-15T12:47:27Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
- レポート選択プルダウンメニューでレポートが順不同で表示されていたため、直感的な並び順（年の降順）に修正

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->
変更前
<img width="1101" height="173" alt="スクリーンショット 2025-07-14 21 59 39" src="https://github.com/user-attachments/assets/ca4aa101-39c1-443c-805e-033fdbb78efd" />
変更後
<img width="1114" height="167" alt="スクリーンショット 2025-07-14 21 59 11" src="https://github.com/user-attachments/assets/54cc3c51-8db8-4135-817f-e5414d780d7b" />

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->

- レポート選択プルダウンメニューでレポートが順不同で表示されていたため、特定の年のレポートを探す際に手間がかかる問題が発生していた。
- 特に最新のレポートを優先的に確認したいユーザーにとって、直感的な並び順（新しい年から古い年の順）が求められていた。

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->

#150 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **バグ修正**
  * レポート一覧の表示順が年順（降順）に並ぶようになりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [chore(deps): react と react-dom を v18 → v19 へアップデート](https://github.com/digitaldemocracy2030/polimoney/pull/149)

**作成者:** noritaka1166  
**作成日:** 2025-07-13T16:05:13Z  
**変更:** +173 -160 (2ファイル)  
**マージ日:** 2025-07-15T12:48:04Z  
**内容:**

# 変更の概要
v18 にダウングレードされていた、 react と react-dom を v19 へアップデートしました
- <https://github.com/facebook/react/blob/main/CHANGELOG.md>

@nivo/pie と @nivo/sankey が 0.88.0 だと v19 に対応していなかったようで warning が出ましたが、
最新版の 0.99.0 では v19 に対応しているため合わせてアップデートしました
<https://github.com/plouc/nivo/releases>

シェアボタン・図は問題なく動いていそうなことはローカルで動かして確認済みです

# スクリーンショット
なし

# 変更の背景
シェアボタンの実装 の PR <https://github.com/digitaldemocracy2030/polimoney/pull/126> にて、 v18 へダウングレードされたようですが、[react-share は v19 に対応している](https://github.com/nygardk/react-share)ようなのでバージョンを v19 に戻しました


# 関連Issue
なし

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Chores**
  * `@nivo/pie` と `@nivo/sankey` の依存バージョンを更新しました。
  * React および React DOM のバージョンを更新しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [chore(deps): biome を v1 → v2 へアップデート](https://github.com/digitaldemocracy2030/polimoney/pull/147)

**作成者:** noritaka1166  
**作成日:** 2025-07-12T09:00:38Z  
**変更:** +90 -105 (21ファイル)  
**マージ日:** 2025-07-12T15:37:10Z  
**内容:**

# 変更の概要
@biomejs/biome  を v1 → v2 へアップデート
- <https://github.com/biomejs/biome/blob/main/packages/%40biomejs/biome/CHANGELOG.md>
-  [マイグレーションガイド](https://biomejs.dev/ja/guides/upgrade-to-biome-v2/>)を参考にアップデート
   -  import の sort の仕方が変わったようですが、問題ないと判断しています
- npm run lint と npm run check が動くことを確認済み
  - いくつか warning / error が出たので対応しています  


# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->
なし

# 変更の背景
<!-- ここに変更が必要となった背景を記載してください -->
@biomejs/biome の v1 を使用していたため、バージョンアップを実施しました

# 関連Issue
<!-- 関連するIssueのリンクをこちらに記載してください -->
なし

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **スタイル**
  * インポート文の順序を整理し、可読性を向上しました。

* **ドキュメント**
  * 一部のコメントを具体的な日本語説明に更新しました。

* **設定・チョア**
  * Biomeの設定ファイルと依存パッケージを最新バージョンに更新し、コーディングスタイルのルールを強化しました。

* **リファクタリング**
  * 使われていない型や変数を削除し、型注釈の記述スタイルを統一しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [refactor: 不要なインポートとconsole.logの削除](https://github.com/digitaldemocracy2030/polimoney/pull/146)

**作成者:** noritaka1166  
**作成日:** 2025-07-12T06:52:32Z  
**変更:** +0 -4 (2ファイル)  
**マージ日:** 2025-07-12T07:03:05Z  
**内容:**

# 変更の概要
<!-- ここに変更の概要を記載してください -->
プロダクトコード内の不要なインポートとconsole.logの削除

# スクリーンショット
<!-- UIの変更を伴う場合は、変更前後のスクリーンショットもしくはgif画像をこちらに記載してください -->

# 変更の背景
開発者ツールを開いて眺めていたら気づいたので対応させていただきました。
<!-- ここに変更が必要となった背景を記載してください -->

# 関連Issue
なし
<!-- 関連するIssueのリンクをこちらに記載してください -->

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **スタイル**
  * 不要なログ出力や未使用のインポートを削除し、コードのクリーンアップを行いました。ユーザーの操作や表示には影響ありません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [詳細解説モーダルをつける](https://github.com/digitaldemocracy2030/polimoney/pull/145)

**作成者:** nishio  
**作成日:** 2025-07-11T11:22:36Z  
**変更:** +64 -2 (3ファイル)  
**マージ日:** 2025-07-11T11:40:27Z  
**内容:**

# 変更の概要
詳細解説をつけられるようにする

# スクリーンショット
https://gyazo.com/017341df3d12a97a3659f44de4765de5

# 変更の背景
タイトルだけでは誤解を招いて問い合わせが来るケースで、問い合わせ回答を掲載したい。

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **新機能**
  * 取引項目に情報アイコンを追加し、ツールチップによる詳細説明を表示できるようになりました。
  * アイコンをクリックすると「詳細説明」ダイアログが開き、説明文を確認できます。

* **ドキュメント**
  * 特定の取引データに詳細な説明文（ツールチップ）を追加しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [chore: 使用していないパッケージの削除 (dependencies)](https://github.com/digitaldemocracy2030/polimoney/pull/143)

**作成者:** noritaka1166  
**作成日:** 2025-07-06T14:11:01Z  
**変更:** +0 -209 (2ファイル)  
**マージ日:** 2025-07-12T05:09:12Z  
**内容:**

# 変更の概要
使用していないパッケージの削除 (dependencies)

# スクリーンショット
なし

# 変更の背景
使用していない dependencies がいくつかあるように見えたため、対応しました。  
意図的に入れているものでしたらすみません...

# 関連Issue
なし

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Chores**
  * 不要な依存パッケージおよび開発用依存パッケージを削除しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [chore: @biomejs/biome を devDependencies へ移動](https://github.com/digitaldemocracy2030/polimoney/pull/142)

**作成者:** noritaka1166  
**作成日:** 2025-07-06T13:33:52Z  
**変更:** +11 -2 (2ファイル)  
**マージ日:** 2025-07-12T06:42:11Z  
**内容:**

# 変更の概要
@biomejs/biome を devDependencies へ移動

# スクリーンショット
なし

# 変更の背景
@biomejs/biome は プロダクトコードでは使用しておらず、  
開発でしか使用されていないかと思うので dependencies から devDependencies へ移動しました

# 関連Issue
なし

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit


* **Chores**
  * 「@biomejs/biome」依存関係を開発用依存関係に移動しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (1件)

### [Add tooltip functionality for donation transaction explanation](https://github.com/digitaldemocracy2030/polimoney/pull/144)

**作成者:** NISHIO+Devin  
**作成日:** 2025-07-11T08:59:21Z  
**変更:** +76 -2 (3ファイル)  
**内容:**


# Fix desktop tooltip hover functionality for donation transaction

## Summary

This PR fixes the desktop tooltip hover functionality for the donation transaction (250万円) in the BoardTransactions component. The user reported that the (i) icon was displaying correctly but the desktop tooltip hover was not working, while the mobile modal was functioning properly.

**Key Changes:**
- Simplified the desktop tooltip implementation from complex Chakra UI Tooltip structure to native HTML `title` attribute
- Maintained separate IconButton components for desktop (hover) and mobile (click) interactions
- Preserved mobile modal functionality while fixing desktop tooltip display
- Resolved conflicts between hover and click interactions

**Files Modified:**
- `components/BoardTransactions.tsx`: Simplified tooltip implementation in `renderTooltipIcon` function

## Review & Testing Checklist for Human

**⚠️ Important:** This PR went through multiple iterations to fix the desktop tooltip, indicating potential complexity or underlying issues. Please test thoroughly.

- [ ] **Test desktop tooltip hover** - Hover over the (i) icon next to "寄付" (250万円) on desktop to verify the Japanese explanation text appears in a native browser tooltip
- [ ] **Test mobile modal tap** - Switch to mobile view and tap the (i) icon to verify the modal opens with complete Japanese text and proper formatting
- [ ] **Verify responsive behavior** - Test at different screen sizes (especially around lg breakpoint ~1024px) to ensure correct IconButton visibility
- [ ] **Check Japanese text formatting** - Verify that line breaks in the Japanese text display correctly in both desktop tooltip and mobile modal
- [ ] **Test for regressions** - Ensure other transaction displays are not affected and the overall component still functions correctly

**Test Plan:**
1. Navigate to http://localhost:3000/demo-takahiro-anno-2024/
2. Find the "寄付" transaction (250万円) in the expenses table
3. On desktop: hover over the (i) icon - tooltip should appear with Japanese explanation
4. Switch to mobile view and tap the (i) icon - modal should open with formatted text
5. Test across different browsers if possible

---

### Diagram

```mermaid
%%{ init : { "theme" : "default" }}%%
graph TD
    TypeDef["models/type.d.ts<br/>Transaction type"]:::context
    DemoData["data/demo-takahiroanno.ts<br/>Donation transaction data"]:::context
    BoardTrans["components/BoardTransactions.tsx<br/>renderTooltipIcon function"]:::major-edit
    
    TypeDef --> DemoData
    DemoData --> BoardTrans
    BoardTrans --> DesktopTooltip["Desktop: HTML title attribute"]
    BoardTrans --> MobileModal["Mobile: Dialog modal"]
    
    subgraph Legend
        L1[Major Edit]:::major-edit
        L2[Minor Edit]:::minor-edit
        L3[Context/No Edit]:::context
    end
    
    classDef major-edit fill:#90EE90
    classDef minor-edit fill:#87CEEB
    classDef context fill:#FFFFFF
```

### Notes

**Implementation History:**
- Initially attempted complex Chakra UI Tooltip structure with `Tooltip.Root`, `Tooltip.Trigger`, `Tooltip.Positioner`, and `Tooltip.Content`
- Multiple debugging attempts revealed the Chakra UI Tooltip wasn't rendering on hover
- Final solution simplified to native HTML `title` attribute for desktop tooltips
- Mobile modal functionality worked correctly throughout all iterations

**Potential Concerns:**
- Native HTML title tooltips may not display multi-line text as elegantly as custom tooltip components
- The root cause of Chakra UI Tooltip failure was not fully investigated
- Responsive design uses separate components which adds complexity

**Session Details:**
- Requested by: @nishio
- Devin session: https://app.devin.ai/sessions/a7a0df6650c74772b8efc26de32da988


**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

