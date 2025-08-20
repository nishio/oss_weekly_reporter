# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-08-13T12:25:06.714302+09:00 から 2025-08-20T12:25:06.714302+09:00 まで

## Pull Requests

### 過去7日間にマージされたPR (3件)

### [fix: トップページに不要なリンクが表示されてしまっているので修正](https://github.com/digitaldemocracy2030/polimoney/pull/177)

**作成者:** noritaka1166  
**作成日:** 2025-08-14T13:58:27Z  
**変更:** +27 -29 (1ファイル)  
**マージ日:** 2025-08-14T14:04:59Z  
**内容:**

# 変更の概要
トップページに表示されるようになってしまった不要なリンクが表示されなくなるように修正

# スクリーンショット
- 修正前
<img width="1186" height="465" alt="スクリーンショット 2025-08-14 午後10 56 50" src="https://github.com/user-attachments/assets/501601c9-5d32-4809-a305-b9efaa233b13" />

- 修正後
<img width="1164" height="448" alt="スクリーンショット 2025-08-14 午後10 57 16" src="https://github.com/user-attachments/assets/5e119130-da13-4b0e-9eab-4a2b19e72862" />


# 変更の背景
- トップページに不要なリンクが表示されてしまっていることに気づいたため修正
  - モバイルの幅だと表示されないが、webの幅だと表示されるようになってしまっていた

# 関連Issue
- 関連するPR
  -   <https://github.com/digitaldemocracy2030/polimoney/pull/176>

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [feat: ヘッダーのレスポンシブデザインを改善](https://github.com/digitaldemocracy2030/polimoney/pull/176)

**作成者:** takeruhukushima  
**作成日:** 2025-08-14T10:14:43Z  
**変更:** +60 -23 (1ファイル)  
**マージ日:** 2025-08-14T11:09:27Z  
**内容:**

# 変更の概要
ヘッダーのレスポンシブデザインを改善し、モバイルとデスクトップでの表示を最適化しました。

# スクリーンショット
<img width="557" height="742" alt="スクリーンショット 2025-08-14 19 11 27" src="https://github.com/user-attachments/assets/bebe5bf5-9769-43d0-8fee-6ace49b93374" />

# 変更の背景
- 共有ボタンの表示位置が画面幅によって適切でなかった

# 主な変更点
- モバイル表示時のレイアウトを最適化

# 関連Issue
#172 In digitaldemocracy2030/polimoney;

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- 新機能
  - ヘッダーをレスポンシブ対応。デスクトップで右寄せナビ（サマリー・収入・支出）を追加。モバイルは中央タイトルと右端のシェアボタンを表示。シェアは非トップページでのみ表示。
- リファクタ
  - レイアウトを再構成し、絶対/相対配置でデスクトップ・モバイルの配置を最適化。パディングをブレークポイントに応じて調整。
- スタイル
  - ナビの文字サイズ/太さと余白を見直し、視認性を向上。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat: 404ページの実装](https://github.com/digitaldemocracy2030/polimoney/pull/175)

**作成者:** noritaka1166  
**作成日:** 2025-08-11T15:08:55Z  
**変更:** +52 -0 (1ファイル)  
**マージ日:** 2025-08-13T07:47:48Z  
**内容:**

# 変更の概要
404ページを実装し、存在しないURLの場合に表示されるようにした

# スクリーンショット
<img width="1470" height="719" alt="スクリーンショット 2025-08-12 午前0 08 15" src="https://github.com/user-attachments/assets/de9dbedd-5a61-4f23-8956-f25cfaa7fed3" />

# 変更の背景
デフォルトの404ページが表示されてしまっていたので対応

# 関連Issue
なし

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- 新機能
  - 日本語対応の404ページを追加。大きな「404」表示と説明文で、誤ったURLや存在しないページへの到達時に状況を明確化。「トップページへ戻る」ボタンでワンクリック復帰が可能。画面中央のカードを用いたレスポンシブなレイアウトで可読性を向上し、既存のヘッダー・お知らせ・フッターと統一感のあるデザインを維持。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

