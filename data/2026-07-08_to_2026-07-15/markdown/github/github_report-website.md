# GitHub レポート: digitaldemocracy2030/website

期間: 2026-07-08T14:37:41.089181+09:00 から 2026-07-15T14:37:41.089181+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (1件)

### [Add English landing page](https://github.com/digitaldemocracy2030/website/pull/217)

**作成者:** howaeri  
**作成日:** 2026-06-17T15:27:21Z  
**変更:** +319 -0 (6ファイル)  
**マージ日:** 2026-07-11T11:12:13Z  
**内容:**

## Summary
英語ページ作成 issue #23 に関連する、英語ランディングページを追加します。

- Adds a standalone `/en/` landing page for international readers.
- Links the English page from the drawer navigation and footer.
- Summarizes DD2030's mission, neutrality, projects, and participation paths.
- Uses English-labeled versions of the project diagrams and marks Japanese-only links as `(Japanese)`.
- Adds a link to the political neutrality FAQ after #192 was merged.

## Notes
- This intentionally does not introduce full i18n routing, translation dictionaries, or duplicated layouts.
- The page is written as a neutral overview rather than a full translation of the Japanese site.
- Japanese-only links are labeled so English readers know what to expect.

Related to #23.

## Checks
- `deno task build`
- `deno test`

`deno lint` currently reports existing repo lint issues in `src/_components/topics.tsx` and `packages/markdown-config/mod.tsx`, unrelated to this change.

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [Week51 Summary Update](https://github.com/digitaldemocracy2030/website/pull/211)

**作成者:** github-actions[bot]  
**作成日:** 2026-04-22T05:37:04Z  
**変更:** +161 -0 (3ファイル)  
**内容:**

Auto-generated weekly summaries for week51

**コメント:** なし

---

