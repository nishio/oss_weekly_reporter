# GitHub レポート: digitaldemocracy2030/website

期間: 2025-05-28T12:29:22.779510+09:00 から 2025-06-04T12:29:22.779510+09:00 まで

## Issues

### 過去7日間に完了されたissue (1件)

### [お知らせページへの動線がない](https://github.com/digitaldemocracy2030/website/issues/128)

**作成者:** shingo-ohki  
**作成日:** 2025-05-30T06:11:02Z  
**内容:**

https://dd2030.org/news への動線が見つけられませんでした。トップページから辿れるといいのかも？

**コメント:** なし

---

### 過去7日間に作成されたissue (4件)

### [最新のお知らせを動的に更新する](https://github.com/digitaldemocracy2030/website/issues/131)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-05-31T11:38:24Z  
**内容:**

CMSで解決？

**コメント:** なし

---

### [ウェブサイトの入場時にアニメーションをつける](https://github.com/digitaldemocracy2030/website/issues/127)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-05-30T03:48:23Z  
**内容:**

ウェブサイトに入場したタイミングでアニメーションが起動する

#### イメージ
1. 全画面中央に「デジタル民主主義2030」の名前とロゴデザインが表示される
2. 扉が開いて(または扉が大きくなって)吸い込まれるようにデフォルトのページに遷移する

名探偵コナンのCM後の感じ

#### 目的
期待感、わくわく感が生まれる





**コメント:** なし

---

### [各プロダクトの詳細ページから活用事例に飛べるようにする](https://github.com/digitaldemocracy2030/website/issues/126)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-05-29T13:28:55Z  
**内容:**

詳細ページから活用事例のページに飛べないのは直感に反する&アクセシビリティが良くない

**コメント:** なし

---

### [[活用事例]リンク追加/UI改善](https://github.com/digitaldemocracy2030/website/issues/125)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-05-29T13:22:05Z  
**内容:**

[広聴AI]の活用事例

-  [選挙報道]のリンク  (「広聴AIの活用事例」ではないかも？)
  こちらでいいでしょうか？　https://news.ntv.co.jp/static/shugiinsenkyo2024/whole-1022/index.html

-  [東京都の長期戦略「2050東京戦略（案）」の策定]のリンク (「広聴AIの活用事例」ではないかも？)
 こちらでいいでしょうか？　https://broadlistening.seisakukikaku.metro.tokyo.lg.jp/20250131/index.html



[いどばた]の活用事例UI

「詳細はこちら」という風に説明文中に書かれていますが、他のと同様に別途ボタンを作るか文中に書くかどちらかに統一したほうが良さそう。
事例が増えるといちいちボタンにするのは面倒？？
「詳細はこちら」を青文字＋下線とかはよく見る形式ではある。。
事例が少ないうちはボタンで飛べるようにしておいてもいいかも？？




**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (3件)

### [お知らせページへの動線作り](https://github.com/digitaldemocracy2030/website/pull/130)

**作成者:** kotaro-yamasaki  
**作成日:** 2025-05-31T11:29:15Z  
**変更:** +35 -0 (2ファイル)  
**マージ日:** 2025-05-31T11:34:54Z  
**内容:**

### 変更点

1. ホーム画面に最新のお知らせ欄を作成
2. タスクバーにお知らせを作成

### 今後の課題
最新のお知らせを動的に更新できるようにする

**コメント:** なし

---

### [Add kouchou-ai v3.0.0 release announcement article](https://github.com/digitaldemocracy2030/website/pull/129)

**作成者:** NISHIO+Devin  
**作成日:** 2025-05-30T06:18:35Z  
**変更:** +111 -0 (3ファイル)  
**マージ日:** 2025-05-30T06:22:30Z  
**内容:**

# kouchou-ai v3.0.0 リリース記事追加

## 概要
広聴AI v3.0.0のリリース記事を追加しました。v2.0.0の記事を参考に、以下の主要な新機能を強調しています：

- **LocalLLM対応**: API費用なしで利用可能、Ollamaサーバー連携、日本語モデル自動ダウンロード
- **ソースリンク機能**: 散布図から元データへの直接リンク
- **コスト表示機能**: トークン使用量と推定コストの可視化

## 変更内容
- `markdown/kouchou-ai-v3.md`: リリース記事の本文
- `app/news/kouchou-ai-v3/page.tsx`: 記事表示用のページコンポーネント
- `app/news/page.tsx`: お知らせ一覧に v3.0.0 記事を追加

## スクリーンショット
![記事一覧ページ](https://devin-public-attachments.s3.dualstack.us-west-2.amazonaws.com/attachments_private/org_59RHUaMtRiE9rGRu/191ae82f-8fdb-4634-848c-3f4caec4e8ee/localhost_3000_news_061713.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAT64VHFT76EXS4B5J%2F20250530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250530T061834Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIHHZoCRgx1pv5JmiSSIeBqn4Fqps%2FaPYDpskI3Z%2FOoGcAiEAg%2FaPMdPDjlKoJul6Z8vicPxOg7fihk%2FpaVCi02sQrvIqwAUIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgwyNzI1MDY0OTgzMDMiDOvH19kt02FvF7HHdiqUBTQPQwJ%2FVJvHht%2FI9BhDk%2FKA9ALD2B%2FfT%2Bin3g27%2BqJGmevTQHERywUW%2B9ZQCnvCds1%2FQh5IztmIRIC2AqKstCJfTaOSCC%2FXsy5OzMgY6fx9zzjEMsD3%2B%2FD56Q4CoVv%2BhFQrYW9owmZ4gphb0cVe6FkwkjxK%2BaXX%2B3MqeV4xXEBXZRKrgXQuHjfY6KZauIhvhCALnzzgejtMGuveVx9ViQ%2BTiK01wz8EhVW8mrS4liXn8CW8uNzvF0EN8ydNCoHWkmes7gggTXANl%2BPopVQaiyXqaribrkSxYHB1bwlQ9k2%2FoQsEsCZiPQXMGdazkaUJz7h71rDV6NplxA4Qqld1T1lN57GoA5xsYRk483dr0qcLHlAvNEK7VdWsh%2F6eV5uT1kZsL10D%2BrLfGzU1qYIPOMSTX7Dy11NLwwAU%2BPbqSZ6D7C9sWZyn2rrw1n90UAf2rpAqt2SJtxTWMnGBe6dC0dpGnfkoCfZBGmTfRO5lN3y0rqV7lUZeOYGwHyk7C733Pm6qlAjzF4o7RwClI7n%2FUhOIxT1b03tVY1ATmFFm8PvJLgueWM7q38gCNuaNzYtjIY5gE7z1%2BHB9lJ2%2BSSs8ajeUSTRdiRzqUuyjd6iNFaqyty2BEk6PrJtkPvvlNtL3QZ0GMGr%2FKZh3aKAXxiJ1MC12IWe9GboJXyK3oB4kMWEzpkSId1Jd%2F9HBKOhunieThXBcra1kAz7eLqeQIUMhJYaBfQYrkUcOWuRMm1MoHoMMLIn0rbqReqIM%2B2m7GoQtg5MF3idbjVduFCTLmPu%2FbjHBNf6oB%2Fo3ppYChGDtmR8wmO5Zw7vHIV1CKONniixA0p37NEG3lZImLFgcrmvaS7xdpBkKXevSSw1rzd1EiLAenZO%2FrzCykOXBBjqYASs3vteMCeEZKe3SxoQaAVnDmvpNSYmitI7VopEwy8fURGkgRwZiS%2BVIEjeU8PEvpFcgGCb3%2BZl6pcKIQRRLzq0SgT%2FULZDWHedLa%2BHQv3cr54kq%2FhqM0fTqHrinsxrRzPb4mGf%2FpyKWedj3AcjgTRji8luYI8VazHjz%2BE94z%2FcvG7v6iFWNlxCMS6W4h5QSQ1UNeQ6EQj3m&X-Amz-Signature=9fe1107e46218d3eba2b9ee099c893d57b0fd707842c6bf6049afaa3fb57a4ed)
![記事詳細ページ](https://devin-public-attachments.s3.dualstack.us-west-2.amazonaws.com/attachments_private/org_59RHUaMtRiE9rGRu/ff2a7fad-25f2-4d30-923a-40630e23d746/localhost_3000_news_061729.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAT64VHFT76EXS4B5J%2F20250530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250530T061835Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIHHZoCRgx1pv5JmiSSIeBqn4Fqps%2FaPYDpskI3Z%2FOoGcAiEAg%2FaPMdPDjlKoJul6Z8vicPxOg7fihk%2FpaVCi02sQrvIqwAUIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARABGgwyNzI1MDY0OTgzMDMiDOvH19kt02FvF7HHdiqUBTQPQwJ%2FVJvHht%2FI9BhDk%2FKA9ALD2B%2FfT%2Bin3g27%2BqJGmevTQHERywUW%2B9ZQCnvCds1%2FQh5IztmIRIC2AqKstCJfTaOSCC%2FXsy5OzMgY6fx9zzjEMsD3%2B%2FD56Q4CoVv%2BhFQrYW9owmZ4gphb0cVe6FkwkjxK%2BaXX%2B3MqeV4xXEBXZRKrgXQuHjfY6KZauIhvhCALnzzgejtMGuveVx9ViQ%2BTiK01wz8EhVW8mrS4liXn8CW8uNzvF0EN8ydNCoHWkmes7gggTXANl%2BPopVQaiyXqaribrkSxYHB1bwlQ9k2%2FoQsEsCZiPQXMGdazkaUJz7h71rDV6NplxA4Qqld1T1lN57GoA5xsYRk483dr0qcLHlAvNEK7VdWsh%2F6eV5uT1kZsL10D%2BrLfGzU1qYIPOMSTX7Dy11NLwwAU%2BPbqSZ6D7C9sWZyn2rrw1n90UAf2rpAqt2SJtxTWMnGBe6dC0dpGnfkoCfZBGmTfRO5lN3y0rqV7lUZeOYGwHyk7C733Pm6qlAjzF4o7RwClI7n%2FUhOIxT1b03tVY1ATmFFm8PvJLgueWM7q38gCNuaNzYtjIY5gE7z1%2BHB9lJ2%2BSSs8ajeUSTRdiRzqUuyjd6iNFaqyty2BEk6PrJtkPvvlNtL3QZ0GMGr%2FKZh3aKAXxiJ1MC12IWe9GboJXyK3oB4kMWEzpkSId1Jd%2F9HBKOhunieThXBcra1kAz7eLqeQIUMhJYaBfQYrkUcOWuRMm1MoHoMMLIn0rbqReqIM%2B2m7GoQtg5MF3idbjVduFCTLmPu%2FbjHBNf6oB%2Fo3ppYChGDtmR8wmO5Zw7vHIV1CKONniixA0p37NEG3lZImLFgcrmvaS7xdpBkKXevSSw1rzd1EiLAenZO%2FrzCykOXBBjqYASs3vteMCeEZKe3SxoQaAVnDmvpNSYmitI7VopEwy8fURGkgRwZiS%2BVIEjeU8PEvpFcgGCb3%2BZl6pcKIQRRLzq0SgT%2FULZDWHedLa%2BHQv3cr54kq%2FhqM0fTqHrinsxrRzPb4mGf%2FpyKWedj3AcjgTRji8luYI8VazHjz%2BE94z%2FcvG7v6iFWNlxCMS6W4h5QSQ1UNeQ6EQj3m&X-Amz-Signature=73f8ca27763a7a1a2f2022dd862ffd0aee5e505d31996d525658c861fb8f6c93)

## テスト
ローカル環境で動作確認済み：
- お知らせ一覧ページ (http://localhost:3000/news)
- 記事詳細ページ (http://localhost:3000/news/kouchou-ai-v3)

## Link to Devin run
https://app.devin.ai/sessions/dd916545ea6143c88ef38c76bb87d0ac

## Requested by
NISHIO (nishio.hirokazu@gmail.com)


**コメント:** なし

---

### [week11](https://github.com/digitaldemocracy2030/website/pull/124)

**作成者:** nishio  
**作成日:** 2025-05-28T08:39:59Z  
**変更:** +370 -0 (5ファイル)  
**マージ日:** 2025-05-28T08:40:58Z  
**内容:**

内容なし

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

