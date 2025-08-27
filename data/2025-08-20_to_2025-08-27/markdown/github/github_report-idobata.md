# GitHub レポート: digitaldemocracy2030/idobata

期間: 2025-08-20T12:22:17.667604+09:00 から 2025-08-27T12:22:17.667604+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (1件)

### [chore:  idea-discussion 内の不要な devDependencies を削除](https://github.com/digitaldemocracy2030/idobata/pull/447)

**作成者:** noritaka1166  
**作成日:** 2025-08-04T15:26:43Z  
**変更:** +0 -22 (2ファイル)  
**マージ日:** 2025-08-20T10:44:38Z  
**内容:**

# 変更の概要
idea-discussion 内の不要な devDependencies を削除
- 元のパッケージ自体に型が含まれるようになったため不要
  - <https://www.npmjs.com/package/@types/mongoose> 
  - <https://www.npmjs.com/package/@types/bcryptjs>

# スクリーンショット
なし

# 変更の背景
npm install 時に deprecated のワーニングが出ていたため対応

# 関連Issue
なし

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### 過去7日間に作成されたPR (2件)

### [Add real-time updates for question page opinions](https://github.com/digitaldemocracy2030/idobata/pull/463)

**作成者:** blu3mo  
**作成日:** 2025-08-20T09:40:54Z  
**変更:** +95 -17 (1ファイル)  
**内容:**

## Summary

- Add WebSocket subscription for real-time updates when new problems/solutions are extracted from chat
- Separate chat functionality from page updates for better separation of concerns  
- Prevent duplicate opinions with ID checking
- Update "ほかの人の意見" section without full page reload

## Technical Changes

- Add dedicated WebSocket subscription in QuestionDetail component
- Implement opinions state management with duplicate prevention
- Separate chat manager initialization from page update logic
- Initialize opinions from existing questionDetail data

## Test Plan

- [x] Navigate to question detail page
- [x] Start chatting with solutions/problems (e.g., "駐車場が不足している", "新しい駐車場を建設する") 
- [x] Verify "ほかの人の意見" section updates in real-time without page reload
- [x] Verify no duplicate opinions are added
- [x] Verify chat notifications still work correctly

🤖 Generated with [Claude Code](https://claude.ai/code)

**コメント:** なし

---

### [Add expand/collapse functionality to other opinions section](https://github.com/digitaldemocracy2030/idobata/pull/462)

**作成者:** Shutaro+Devin  
**作成日:** 2025-08-20T09:25:17Z  
**変更:** +74 -46 (1ファイル)  
**内容:**

# 変更の概要
「ほかの人の意見」セクションに展開・折りたたみ機能を追加しました。従来は4件の意見のみが表示され、グラデーションオーバーレイで隠された意見にアクセスできませんでしたが、「もっと見る」ボタンをクリックすることで、その場で全ての意見を表示できるようになりました。

## 主な変更内容
- `isOpinionsExpanded`ステートによる展開状態の管理
- 展開時は全意見、折りたたみ時は上位4件の意見を表示
- 動的テキスト付きの展開・折りたたみボタン（「もっと見る (X件)」/「折りたたむ」）
- 展開時はグラデーションオーバーレイとスクロールバーを非表示
- 既存のカードスタイリングとレイアウトを維持

# スクリーンショット
展開前（初期状態）:
![展開前](https://devin-public-attachments.s3.dualstack.us-west-2.amazonaws.com/attachments_private/org_59RHUaMtRiE9rGRu/796035b8-4f82-40ad-9f77-812db15e6954?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAT64VHFT75K4IPI4K%2F20250820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250820T092514Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQDTJu%2BeWu3C2rzDCoX%2BHETBMQndd7mVdX3s8wVMP8GwbgIhAMCATXRJzeLolBSjoDkGa2vXWfzddpxYQNqU%2FbRKaHAzKsAFCNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQARoMMjcyNTA2NDk4MzAzIgycxUhZ1dh70xLAxFMqlAWzn1aTlPEp3%2FIwAyo81f0mDCUa3rqUmePMeZZdQTZm8ASzHoTuB348%2FwlYESwG5276P7Osj1HBWjsN1GcY0%2BoHKiN3D%2Bwb7VFnfPnjh8sJSTdi7kGpCFyvCyaYfyDEol61LN3u4Z8J0Kui7fvRTyhm1gHUL%2FxMpmpmIScZms%2FLbZyFx19JbRfFmgoVjpI63ynKwLyCdnJxJtpYdtXGy314MQ0hd1Cn7pzXnQWIoMBRaY0QW8393tkQhQ9z%2F558kOVAP8m5h6uMW%2BUAe1kZLbElhp%2F2Bc5D7UK%2B5MqZZApvBmQlR2BQ7aT8vOO4APwuO6McXdjGna7bw%2BPWN8axc3MIOG%2Btp%2B9Y4MSbW7Gudm2DMBOw4tW8Kfbz7Tk3PtRr4hEopIj8TJ3o1POFyzZFOXHqy3dg0NYe7wxLdEAoi065CfRrLVMDGwoS5SS86%2Bhp7SH%2FmOX7tarG4xsuNZ28yhWw9cAO8uzo6UM4oidzKmwzLAcBj54jDT4ElGsxEDUL86KX%2BIwp8%2BEffJs8Nz%2F2rnFrmdy9l%2F6KboPVWEXFj8sQdJuZoUMb3IJwSD3UXSCbK%2F%2BhTbXOju6T2jIyiCFdWyDFDPwh5KJzrCz9vnIlrCMYCo9dMWefKuIYl7emDuYsCaRIyZFlbfZV76L0v1xer8dw1ETN8jU8qqbjyznaPXul7MIVmZq3KguBsl6nbx2wgAbpe9E31%2FJKXckKWsNMBjuUI6OF74tGjJqiCL6Zqi%2FckZ5kF4s0RqJuJEUzWQStkD9JO%2FLNMCmKQ2fpQnGJYS9VHqKjEHDkeYmY6Ouyg7V0xtTrITo8Y8LeSJ9vcFvloQE0LrxEgW8mmkfF8uIHGu4QxExAhVZrcZoANXX71yBbhMOUpY0w1KSWxQY6lwHFi12cduhbvGwm3mU1DoCDJ8joRC47aolUuDw%2Fv4VQrNz7DAa7m%2FcubT9xXTx%2F4yi9zufrm0wSOIEj5rZUuEWfmE6sJMhWRBMxgK%2FNKqa0eD4RT9Cx%2FGcKF52w%2BWr1PID5rDgIG%2B9VYgJ4yw8tpwEmR2OP%2FNgegoqSYDLsS3pAGf61pl6PSZPEM7zwUSWnvwuSKJGGaPgY&X-Amz-Signature=950803a86728f572dc20e549f1a60b51c271a7053d7d720fd5693d5f626e4827)

展開後（全意見表示）:
![展開後](https://devin-public-attachments.s3.dualstack.us-west-2.amazonaws.com/attachments_private/org_59RHUaMtRiE9rGRu/16284fd0-dabc-45c5-947a-ece7b01fd66e?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAT64VHFT75K4IPI4K%2F20250820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250820T092515Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQDTJu%2BeWu3C2rzDCoX%2BHETBMQndd7mVdX3s8wVMP8GwbgIhAMCATXRJzeLolBSjoDkGa2vXWfzddpxYQNqU%2FbRKaHAzKsAFCNL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQARoMMjcyNTA2NDk4MzAzIgycxUhZ1dh70xLAxFMqlAWzn1aTlPEp3%2FIwAyo81f0mDCUa3rqUmePMeZZdQTZm8ASzHoTuB348%2FwlYESwG5276P7Osj1HBWjsN1GcY0%2BoHKiN3D%2Bwb7VFnfPnjh8sJSTdi7kGpCFyvCyaYfyDEol61LN3u4Z8J0Kui7fvRTyhm1gHUL%2FxMpmpmIScZms%2FLbZyFx19JbRfFmgoVjpI63ynKwLyCdnJxJtpYdtXGy314MQ0hd1Cn7pzXnQWIoMBRaY0QW8393tkQhQ9z%2F558kOVAP8m5h6uMW%2BUAe1kZLbElhp%2F2Bc5D7UK%2B5MqZZApvBmQlR2BQ7aT8vOO4APwuO6McXdjGna7bw%2BPWN8axc3MIOG%2Btp%2B9Y4MSbW7Gudm2DMBOw4tW8Kfbz7Tk3PtRr4hEopIj8TJ3o1POFyzZFOXHqy3dg0NYe7wxLdEAoi065CfRrLVMDGwoS5SS86%2Bhp7SH%2FmOX7tarG4xsuNZ28yhWw9cAO8uzo6UM4oidzKmwzLAcBj54jDT4ElGsxEDUL86KX%2BIwp8%2BEffJs8Nz%2F2rnFrmdy9l%2F6KboPVWEXFj8sQdJuZoUMb3IJwSD3UXSCbK%2F%2BhTbXOju6T2jIyiCFdWyDFDPwh5KJzrCz9vnIlrCMYCo9dMWefKuIYl7emDuYsCaRIyZFlbfZV76L0v1xer8dw1ETN8jU8qqbjyznaPXul7MIVmZq3KguBsl6nbx2wgAbpe9E31%2FJKXckKWsNMBjuUI6OF74tGjJqiCL6Zqi%2FckZ5kF4s0RqJuJEUzWQStkD9JO%2FLNMCmKQ2fpQnGJYS9VHqKjEHDkeYmY6Ouyg7V0xtTrITo8Y8LeSJ9vcFvloQE0LrxEgW8mmkfF8uIHGu4QxExAhVZrcZoANXX71yBbhMOUpY0w1KSWxQY6lwHFi12cduhbvGwm3mU1DoCDJ8joRC47aolUuDw%2Fv4VQrNz7DAa7m%2FcubT9xXTx%2F4yi9zufrm0wSOIEj5rZUuEWfmE6sJMhWRBMxgK%2FNKqa0eD4RT9Cx%2FGcKF52w%2BWr1PID5rDgIG%2B9VYgJ4yw8tpwEmR2OP%2FNgegoqSYDLsS3pAGf61pl6PSZPEM7zwUSWnvwuSKJGGaPgY&X-Amz-Signature=9010182b3220fc6c83d629d1b6508a6cb2082e489ff2616122208ce81e64667b)

# 変更の背景
ユーザーから「『ほかの人の意見』がたくさんある時に、フェードしている先のデータが読めなくて困る。展開できるようにしてほしい」という要望があり、UXの改善を目的として実装しました。

# 関連Issue
なし（Slackでの直接的な要望に対応）

# レビューポイント
以下の点を重点的にレビューしてください：

## 機能面
- [ ] 実際のAPIデータで展開・折りたたみが正常に動作するか
- [ ] 意見数が0件、1-3件、4件、5件以上の各ケースで適切に動作するか
- [ ] 大量の意見データでのパフォーマンスに問題がないか

## UI/UX面  
- [ ] ボタンのスタイリングが既存のデザインシステムと一致しているか
- [ ] 展開・折りたたみアニメーションが自然か
- [ ] モバイルでの表示が適切か

## アクセシビリティ
- [ ] キーボードナビゲーションが正常に動作するか
- [ ] スクリーンリーダーでボタンの機能が適切に読み上げられるか

## コード品質
- [ ] TypeScriptの型定義が適切か
- [ ] lint/typecheckが通過しているか
- [ ] パフォーマンス最適化の余地がないか

# 実装ノート
- テスト時はバックエンドが起動していなかったため、モックデータを使用して動作確認を実施
- 意見の表示順序は関連度（relevance）の高い順でソートして表示
- 既存の`OtherOpinionCard`コンポーネントをそのまま活用

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

---

**Link to Devin run**: https://app.devin.ai/sessions/56c62b41ca5e42e5bd71aa4fb2b4802a  
**Requested by**: @blu3mo

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

