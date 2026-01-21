# GitHub レポート: digitaldemocracy2030/website

期間: 2026-01-14T12:38:38.998604+09:00 から 2026-01-21T12:38:38.998604+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (1件)

### [Google Analytics を復活させる](https://github.com/digitaldemocracy2030/website/issues/199)

**作成者:** shingo-ohki  
**作成日:** 2026-01-19T00:52:24Z  
**内容:**

website の構成変更時に Google Analytics の設定が未設定の状態になってしまい、website のアクセス状況の確認がしづらい。
改めて設定を行う。

参考: 以前の対応 https://github.com/digitaldemocracy2030/website/pull/175

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (4件)

### [公開設定を詳細化](https://github.com/digitaldemocracy2030/website/pull/200)

**作成者:** kuboon  
**作成日:** 2026-01-20T12:40:06Z  
**変更:** +33 -23 (6ファイル)  
**マージ日:** 2026-01-20T12:49:31Z  
**内容:**

内容なし

**コメント:** なし

---

### [fix cms](https://github.com/digitaldemocracy2030/website/pull/198)

**作成者:** kuboon  
**作成日:** 2026-01-15T07:13:32Z  
**変更:** +213 -210 (7ファイル)  
**マージ日:** 2026-01-15T10:11:40Z  
**内容:**

内容なし

**コメント:** なし

---

### [Mdx の導入、 h1 等の整理](https://github.com/digitaldemocracy2030/website/pull/197)

**作成者:** kuboon  
**作成日:** 2026-01-15T03:00:47Z  
**変更:** +222 -162 (20ファイル)  
**マージ日:** 2026-01-15T03:40:44Z  
**内容:**

# テンプレートエンジンとして mdx を導入
(mdx plugin 内で url 等の filter が使えないのが判明し、 lume リリース待ち https://github.com/lumeland/lume/pull/804)

# markdown engine を default の markdown-it から remark へ変更し、書き換えを mdx と共有。
remark, rehype plugin をいくつか導入したが依存が多い割に中身はシンプルだったので全部統合して1つのファイルで実装した
- md 内の # を h2, ## を h3 など、1段階下げるようにした
  - frontmatter の title で h1 を使っている
  - tailwindcss/typography (prose) をそのまま使いたい
  - md 内で # を使いたい
- md 内の h1, h2 に対して自動で anchor を作り、a タグで囲んでページ内リンクを容易に取得、シェアできるようにした
- a href が外部へのリンクの場合、自動的に target=_blank を付与

# metas plugin の出力と重複していた記述を削除
https://lume.land/plugins/metas/

**コメント:** なし

---

### [Week43 Summary Update](https://github.com/digitaldemocracy2030/website/pull/196)

**作成者:** github-actions[bot]  
**作成日:** 2026-01-14T04:31:51Z  
**変更:** +98 -0 (2ファイル)  
**マージ日:** 2026-01-18T10:22:22Z  
**内容:**

Auto-generated weekly summaries for week43

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(4件)

### [政治的中立性に関するFAQページを追加し、貢献者ガイドから導線を設置](https://github.com/digitaldemocracy2030/website/pull/192)

**作成者:** shingo-ohki  
**作成日:** 2025-12-29T01:45:15Z  
**変更:** +112 -0 (2ファイル)  
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

### [Add kouchou-ai v4.0.0 release announcement article](https://github.com/digitaldemocracy2030/website/pull/190)

**作成者:** nishio  
**作成日:** 2025-12-28T13:38:23Z  
**変更:** +84 -0 (1ファイル)  
**内容:**

# Add kouchou-ai v4.0.0 release announcement article

## Summary
広聴AI v4.0.0のリリース記事を追加します。v3.0.0の記事（`src/topics/kouchou-ai-v3.md`）と同じ構成で作成しました。

主な内容:
- AI選択肢の拡大（Gemini対応、APIキーのフォーム入力）
- 管理画面の信頼性・UX向上
- レポート閲覧体験の改善（用語解説ページ、全画面表示改善）
- 公開・安全・運用面の強化
- ブロードリスニング解説本の告知（2025年6月発売予定）

## Updates since last revision
レビューコメントを反映しました:
- GitHub Pages対応の説明をより具体的に修正
- 「ご利用方法」セクションから「最適な」を削除（意味が不明確なため）
- Slackチャンネルに実際のリンクを追加: [#2_broad-listening-book](https://dd2030.slack.com/archives/C09J7A6HKRA)

## Review & Testing Checklist for Human
- [ ] 機能説明がv4.0.0の実際の変更内容と一致しているか確認
- [ ] コントリビューターリストに漏れがないか確認（v3.0.0..v4.0.0間の貢献者全員が含まれているか）
- [ ] ブロードリスニング本の情報（著者、発売時期）が正確か確認
- [ ] サイトをビルドして記事が正しく表示されるか確認

### Notes
- コントリビューターリストはGitHub Release notesから抽出し、ボット（Devin AI、dependabot）を除外しました

Link to Devin run: https://app.devin.ai/sessions/d167d50edaaa43ee8eb72e4068e54a48
Requested by: NISHIO (nishio.hirokazu@gmail.com) / @nishio

**コメント:** なし

---

### [Week41 Summary Update](https://github.com/digitaldemocracy2030/website/pull/188)

**作成者:** github-actions[bot]  
**作成日:** 2025-12-24T04:08:29Z  
**変更:** +177 -0 (4ファイル)  
**内容:**

Auto-generated weekly summaries for week41

**コメント:** なし

---

### [Week40 Summary Update](https://github.com/digitaldemocracy2030/website/pull/187)

**作成者:** github-actions[bot]  
**作成日:** 2025-12-17T04:04:46Z  
**変更:** +204 -0 (4ファイル)  
**内容:**

Auto-generated weekly summaries for week40

**コメント:** なし

---

