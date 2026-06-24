# GitHub レポート: digitaldemocracy2030/website

期間: 2026-06-17T13:31:35.341575+09:00 から 2026-06-24T13:31:35.341575+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (1件)

### [政治的中立性に関するFAQページを追加し、貢献者ガイドから導線を設置](https://github.com/digitaldemocracy2030/website/pull/192)

**作成者:** shingo-ohki  
**作成日:** 2025-12-29T01:45:15Z  
**変更:** +112 -0 (2ファイル)  
**マージ日:** 2026-06-19T11:43:23Z  
**内容:**

こちらもこんなものを追加してみるのはどうでしょうか？

## 概要
- `/faq` に「政治的中立性に関するよくある質問」ページを新設（Q1～Q10）
- Q1でチームみらいとの関係性の誤解を解消（安野氏ボード退任のnoteへリンク）
- 貢献者向けガイドライン末尾からFAQへの導線を追加

## 背景
- Aboutに中立性の定義を追加（PR #191）したが、具体的なケースや判断基準を説明するFAQが不足していた
- コミュニティ内で「チームみらいの活動では？」「政治の話はNG？」といった誤解が見られるため、外向け誤解解消と内向け運用ガイドを兼ねたFAQを整備

## 主な内容
- Q1: チームみらいとの関係（独立性、ボード退任の仕組み）
- Q2～Q6: 中立の定義、参加条件、個人活動との分離
- Q7: 選挙運動でのリソース利用禁止理由（中立性＋法的遵守）
- Q8: 政党・議員からのツール利用申し出への対応（歓迎・等距離運用）
- Q9: コミュニティ内での政策議論の扱い
- Q10: グレーケースの相談先（Slack、GitHub、問い合わせフォーム）

## 特に確認してもらいたいこと
- 相談先は適切と思われるものを記載してみたが、公式にはどの様に案内するのがよいか？

**コメント:** なし

---

### 過去7日間に作成されたPR (1件)

### [Add English landing page](https://github.com/digitaldemocracy2030/website/pull/217)

**作成者:** howaeri  
**作成日:** 2026-06-17T15:27:21Z  
**変更:** +319 -0 (6ファイル)  
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

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [Week51 Summary Update](https://github.com/digitaldemocracy2030/website/pull/211)

**作成者:** github-actions[bot]  
**作成日:** 2026-04-22T05:37:04Z  
**変更:** +165 -0 (4ファイル)  
**内容:**

Auto-generated weekly summaries for week51

**コメント:** なし

---

