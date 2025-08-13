# GitHub レポート: digitaldemocracy2030/polimoney

期間: 2025-08-06T12:32:32.252665+09:00 から 2025-08-13T12:32:32.252665+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (1件)

### [スマホで開いた時にもSNS共有リンクが表示されるようにする](https://github.com/digitaldemocracy2030/polimoney/issues/172)

**作成者:** noritaka1166  
**作成日:** 2025-08-07T14:19:58Z  
**内容:**

## 解決・改善したいこと
PCから開くと、SNS共有リンクが表示できるが、
スマホで開いた時には、SNS共有リンクが表示されていないため表示したい

## 具体的な実現方法・実装方法の概要（未記入でも構いません）


**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(1件)

### [理解の助けになるよう、収支項目の解説を書き込む](https://github.com/digitaldemocracy2030/polimoney/issues/166)

**作成者:** grassfieldk  
**作成日:** 2025-07-29T12:26:57Z  
**内容:**

## 解決・改善したいこと

起票者である私も含め、政治や経済についての知識が浅い人間が見たときの助けとなる UI/UX の導入を図りたい
現在の状態でもなんとなく

## 具体的な実現方法・実装方法の概要（未記入でも構いません）

### ツールチップによる補足説明

すでに [こちらのページ](https://polimoney.dd2030.org/takahiro-anno/2024) の [支出の一覧] にも限定的に実装はされていますが、
全体的に専門用語や意図が掴みづらい表現などの解説を導入すべきかと思います

例えば "個人からの寄附" という項目について、私のようなリテラシのない人間からすれば
「政治家って個人からの寄附もらっていいの？」「そもそも寄附ってどうするの？できるなら自分もしたい」
という疑問が浮かびます
正直、国民の大半の政治知識レベルはその程度だと思います（悲観しているわけではなく、事実として）

ですので、下記画像のようにツールチップによる補足説明が充実していれば、なんとなくお金の動きを見たいだけだったユーザーもより政治の仕組みについて詳しくなれ、興味を持ちやすくなっていくと思います
<img width="1334" height="669" alt="Image" src="https://github.com/user-attachments/assets/69cff889-8a1e-435b-a7e1-fd79518c1074" />

ちなみに、ソニー損保の契約ページなどがとてもわかり易く参考になるかと思います
保険契約をするうえで出てくる専門用語や会社独自のサービス名などの説明がツールチップでされており、非常にわかりやすく難解なはずの保険契約で困ったことがありません
※ 契約を持っていなくても新規契約ページの閲覧は可能です

---

あらゆる事象や活動の可視化による国民が監視しやすい仕組みを作ることの物理的効果だけでなく、
誰もが見やすく興味を持てるような仕組みを取り入れていくことで、より多くの人が政治に関心を持つ心理的な効果をねらっていきたいと感じました

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (4件)

### [feat: robots.txt の更新](https://github.com/digitaldemocracy2030/polimoney/pull/174)

**作成者:** noritaka1166  
**作成日:** 2025-08-07T14:49:55Z  
**変更:** +3 -1 (1ファイル)  
**マージ日:** 2025-08-08T13:57:38Z  
**内容:**

# 変更の概要
robots.txt を更新
- Disallow に藤崎さんの画像を追加
- Allow に ogp 配下を追加

# スクリーンショット
なし

# 変更の背景
クローラーが参照するrobots.txtを更新して、藤崎さんの画像をクローラーが取得しに行かないようにしたい

# 関連Issue
#101 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **ドキュメント**
  * robots.txtに新たなDisallowルール（/demo-kokifujisaki.jpg）を追加しました。
  * /ogpパスに対するAllowルールを明示的に追加しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix: サムネイルのURLを絶対パスに更新](https://github.com/digitaldemocracy2030/polimoney/pull/171)

**作成者:** noritaka1166  
**作成日:** 2025-08-06T16:44:58Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-08-06T23:49:25Z  
**内容:**

# 変更の概要
thumbnail の指定を相対パスから絶対パスに変更

# スクリーンショット
なし

# 変更の背景
現在、thumbnail が正しく検索結果に表示されない状態のままかと思います。  
今設定している値は相対パスになっていますが、これを絶対パスに変えることでもしかしたら表示されるようになったりしないかなと思っています。

# 関連Issue
#101 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **その他**
  * サムネイル画像の参照先が相対パスから絶対URLに変更されました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [feat: SNS共有リンクに名前を追加 & ハッシュタグ追加](https://github.com/digitaldemocracy2030/polimoney/pull/170)

**作成者:** noritaka1166  
**作成日:** 2025-08-06T15:16:52Z  
**変更:** +9 -11 (3ファイル)  
**マージ日:** 2025-08-06T15:24:58Z  
**内容:**

# 変更の概要
SNSへの共有リンクに名前とハッシュタグを追加
- タイトルは {政治家さんの名前} + "Polimoney" になるように変更
- react-share では、ハッシュタグもつけられることがわかったため追加
  - Facebook は 1つだけつけられるようになっていたため、 "Polimoney"
  - X は複数つけられるようになっていたため、"Polimoney", "デジタル民主主義2030" 

# スクリーンショット
なし

# 変更の背景
#134 のタイトル変更のみ実施

# 関連Issue
#134 

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **新機能**
  * シェア機能で政治家のプロフィール名がSNS共有タイトルに表示されるようになりました。
  * SNS共有時に「Polimoney」と「デジタル民主主義2030」のハッシュタグが自動で追加されます。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [chore: 使用していない @eslint/eslintrc を削除](https://github.com/digitaldemocracy2030/polimoney/pull/169)

**作成者:** noritaka1166  
**作成日:** 2025-08-06T14:12:52Z  
**変更:** +0 -212 (2ファイル)  
**マージ日:** 2025-08-06T15:25:12Z  
**内容:**

# 変更の概要
使用していない @eslint/eslintrc を削除

# スクリーンショット
なし

# 変更の背景
現在、biome を使用しており、eslint は使用していないため

# 関連Issue
なし

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Chores**
  * 開発用依存関係から "@eslint/eslintrc" を削除しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (2件)

### [feat: 404ページの実装](https://github.com/digitaldemocracy2030/polimoney/pull/175)

**作成者:** noritaka1166  
**作成日:** 2025-08-11T15:08:55Z  
**変更:** +52 -0 (1ファイル)  
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

### [feat: 存在しないページの場合にはトップページにリダイレクトされるようにした](https://github.com/digitaldemocracy2030/polimoney/pull/173)

**作成者:** noritaka1166  
**作成日:** 2025-08-07T14:36:02Z  
**変更:** +9 -0 (1ファイル)  
**内容:**

# 変更の概要
存在しないページに遷移しようとした場合、トップページにリダイレクトされるようにした

# スクリーンショット
なし

# 変更の背景
存在しないページに遷移しようとすると、next.js のデフォルトの404ページが表示されてしまっていた

# 関連Issue
なし

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **新機能**
  * 存在しないページにアクセスした際、自動的に環境に応じたURLへリダイレクトされるようになりました（本番環境では polimoney.dd2030.org、開発環境では localhost:3000 へ）。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

