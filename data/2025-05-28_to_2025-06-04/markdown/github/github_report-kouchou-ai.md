# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-05-28T12:28:52.721502+09:00 から 2025-06-04T12:28:52.721502+09:00 まで

## Issues

### 過去7日間に完了されたissue (5件)

### [[BUG] client のヘッダー画像の表示・非表示に一貫性がない](https://github.com/digitaldemocracy2030/kouchou-ai/issues/585)

**作成者:** shgtkshruch  
**作成日:** 2025-05-30T10:02:00Z  
**内容:**

### 概要

<!-- バグの簡潔な説明をお願いします -->

- clinet のヘッダーの画像（reporter.png）の表示が、ページ遷移やページのリロードをすると表示されたり表示されなかったりする

### 再現手順

1. client のレポート一覧画面を開く
2. レポート個別ページを開く
3. レポート一覧画面に戻る
4. ページをリロードする

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->

- ヘッダーの画用の表示が、ページの初期表示・SPA のページ遷移・リロード時に一貫していること

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

https://github.com/user-attachments/assets/10931b98-63f3-4a8f-8c24-0d0bfc1a63ca

### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->

- こちらの issue https://github.com/digitaldemocracy2030/kouchou-ai/issues/403 の対応が影響しているかもしれません

**コメント:** なし

---

### [[design] デザインシステム構築／数値環境](https://github.com/digitaldemocracy2030/kouchou-ai/issues/506)

**作成者:** UtkNggc  
**作成日:** 2025-05-13T12:14:28Z  
**内容:**

https://github.com/digitaldemocracy2030/kouchou-ai/issues/443 で全体の設計ができたので、構築開始できます。
1つ1つのタスクが重いのでIssue分散してます。

このIssueでは、spacing、radius、border、effect、max.min-sizeなどの数値周りの環境を整備します。

## 手順
作業は広聴AIのFigmaファイルで行います。

1. chakraUIの数値情報すべてvariablesで定義
2. 使うものだけ洗い出して作業パネルで呼び出せるように設定
3. そのtokenを使用してstylesに登録
4. Figmaファイル内にガイドライン作成（ブランド思想用ではなくデザイナ&エンジニアが見る用に一覧性のあるもの）

### 期待できる効果

- デザイナーが容易に数値選定できるようになる（エンハンス時の数値の迷いを大幅に削減）
- chakraUI範囲内の数値を使用するため実装がやりやすいのではないか
- 将来的にchakraUIをはがして独自サイズを使うことになったとしてもVariablesの変更ですべて置き換わる

### 留意点
ブランドコンパス内に明記されてるブランドパーソナリティのデザイントンマナを叶える設計にする。
https://www.figma.com/slides/0B55u8rxDjjjpRJbNUEP0Z/%F0%9F%A7%AD-Brand-Compass?t=yLYyNEeIO9pprmn3-6

**コメント:** なし

---

### [[design] デザインシステム構築／Typography環境](https://github.com/digitaldemocracy2030/kouchou-ai/issues/505)

**作成者:** UtkNggc  
**作成日:** 2025-05-13T12:05:53Z  
**内容:**

https://github.com/digitaldemocracy2030/kouchou-ai/issues/443 で全体の設計ができたので、構築開始できます。
1つ1つのタスクが重いのでIssue分散してます。

このIssueではタイポグラフィに関わる環境を整備します。

## 手順
作業は広聴AIのFigmaファイルで行います。

1. chakraUIのタイポ情報すべてvariablesで定義
2. 使うものだけ洗い出してsemantic定義
3. そのtokenを使用してstylesに登録
4. Figmaファイル内にタイポグラフィガイドライン作成（ブランド思想用ではなくデザイナ&エンジニアが見る用に一覧性のあるもの）

### 検討が必要なこと

- 日本語family優先順位の検討（Noto sans, Hiragino Kaku Gothic ProN, YuGothic, Meiryo、など
- 英数字family変える変えない
- size, line-heightの取捨選択

### 期待できる効果

- デザイナーが容易にタイポ選定できるようになる（エンハンス時の色の迷いを大幅に削減）
- chakraUI範囲内の数値を使用するため実装がやりやすいのではないか
- 将来的にchakraUIをはがして独自タイポを使うことになったとしてもVariablesの変更ですべて置き換わる

### 留意点
ブランドコンパス内に明記されてるブランドパーソナリティの「ボイス」を叶える設計にする。
https://www.figma.com/slides/0B55u8rxDjjjpRJbNUEP0Z/%F0%9F%A7%AD-Brand-Compass?t=yLYyNEeIO9pprmn3-6

**コメント:** なし

---

### [[design] デザインシステム構築／color環境](https://github.com/digitaldemocracy2030/kouchou-ai/issues/504)

**作成者:** UtkNggc  
**作成日:** 2025-05-13T11:57:14Z  
**内容:**

https://github.com/digitaldemocracy2030/kouchou-ai/issues/443 で全体の設計ができたので、構築開始できます。
1つ1つのタスクが重いのでIssue分散してます。

このIssueではカラーに関わる環境を整備します。

## 手順

作業は広聴AIのFigmaファイルで行います。

1. chakraUIのカラーたちをすべてPrimitiveにいれる
2. Primitiveから選定してSemanticで定義（実質上のプロダクトカラー）
3. stylesに登録
4. Figmaファイル内にカラーガイドライン作成（ブランド思想用ではなくデザイナ&エンジニアが見る用に一覧性のあるもの）

### 期待できる効果

- デザイナーが容易に色選定できるようになる（エンハンス時の色の迷いを大幅に削減）
- chakraUI範囲内のカラーのため実装がやりやすいのではないか
- 将来的にchakraUIをはがして独自カラーを使うことになったとしてもPrimitiveの変更ですべて置き換わる

### 留意点
ブランドコンパス内のブランドパーソナリティとデザイントンマナを叶える設計にする
https://www.figma.com/slides/0B55u8rxDjjjpRJbNUEP0Z/%F0%9F%A7%AD-Brand-Compass?t=yLYyNEeIO9pprmn3-6

**コメント:** なし

---

### [[FEATURE] ISRによる表示遅延の案内表示](https://github.com/digitaldemocracy2030/kouchou-ai/issues/61)

**作成者:** nanocloudx  
**作成日:** 2025-03-16T08:08:04Z  
**内容:**

# 背景
新しいレポートが生成されてから、閲覧可能になるまでの間には約５分のラグがある
これは client で ISR を行っており、この頻度を 300sec にしているのが原因（この仕組み自体は問題ない認識）
この仕組みを知らないとレポート作成者が迷ってしまうので、５分遅れる旨を client-admin に書くとよさそう

Reference
https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration

# 提案内容
client-admin にレポート生成完了から５分ぐらいは表示できないことがわかる文言を追加する


**コメント:** なし

---

### 過去7日間に作成されたissue (4件)

### [[DOCUMENT]ローカル LLM の使用時のdocker composeコマンドについて](https://github.com/digitaldemocracy2030/kouchou-ai/issues/587)

**作成者:** dentaro  
**作成日:** 2025-05-31T14:59:36Z  
**内容:**

# 現在の問題点
README.mdの「ローカル LLM の使用」の項で、通らないコマンドがありました。

# 提案内容
「広聴AI」のREADME.mdの

docker compose up -d --profile ollama

Docker の version v2.35.1-desktop.1で、WINとMACで試しましたが、どちらも通らないようです。

docker compose --profile ollama up -d

だと通るようになりました。

**コメント:** なし

---

### [[REFACTOR] フロントエンド共通で利用するデザインシステムの開発基盤を作る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/586)

**作成者:** shgtkshruch  
**作成日:** 2025-05-31T09:34:50Z  
**内容:**

# 現在の問題点
<!-- 現在のコードの何が問題なのか、どのような技術的負債があるかを説明してください -->

- デザイナーさんの方でデザインシステムの整備を進めていただいています
  - https://github.com/digitaldemocracy2030/kouchou-ai/issues/504
  - https://github.com/digitaldemocracy2030/kouchou-ai/issues/505
  - https://github.com/digitaldemocracy2030/kouchou-ai/issues/506
- このデザインシステムは client, client-admin で使う想定で作成されています
- フロントエンドの実装としてもデザインシステムを整備して、client, client-admin など複数のサービスから import して使えるようにしたいです
  - 2025/05/31 時点では、複数のサービスで共通して使うライブラリやモジュールを配置して他のサービスから import しつつ、その依存関係を管理する仕組みはない認識です

# 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->

- 今は package manager として npm を採用しているので、まずはミニマムで [npm workspaces](https://docs.npmjs.com/cli/v8/using-npm/workspaces) で対応できると良いかなと考えています
  - 対象: client, client-admin, client-static-build とこれから実装する design-system


**コメント:** なし

---

### [[BUG] レポート編集、意見グループ編集を行うと、トークン使用量や推定コストが0になる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/584)

**作成者:** shingo-ohki  
**作成日:** 2025-05-29T12:25:46Z  
**内容:**

### 概要
タイトル通り

### 再現手順

1. Azure デプロイした環境でレポート生成する（このときトークン使用量、推定コストには値が入っている）
2. 生成したレポートの「レポート編集」「意見グループ編集」を行う
3.該当のレポートのトークン使用量、推定コストが 0 になる

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

#### 「レポート編集」「意見グループ編集」前
![Image](https://github.com/user-attachments/assets/015ccaed-61e2-406e-9616-93ce36ce9dfa)
#### 「レポート編集」「意見グループ編集」後
![Image](https://github.com/user-attachments/assets/ab1c1370-8944-48d8-b62d-d02abce87ccd)

### その他
個々の意見データから url を紐づけてリンクしていた場合、リンクも消える（スクリーンショット取り忘れました）

<!-- 追加で伝えておきたいことがあれば記入してください -->

**コメント:** なし

---

### [[BUG]分析対象のカラムにから文字列が含まれているとエラーになる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/583)

**作成者:** shingo-ohki  
**作成日:** 2025-05-29T09:25:11Z  
**内容:**

### 概要

> 中山心太（tokoroten）
  16:45
分析対象のカラムに空文字が入っていると、大量のエラーが出ますね。
自由記述アンケートの分析をやろうとしたら、死にました。
中山心太（tokoroten）
  [16:58](https://dd2030.slack.com/archives/C08F7JZPD63/p1748505525503179)
空行（改行だけとか、スペースだけとか）が入ってもダメなのかも。この辺要検討です。 （編集済み） 
中山心太（tokoroten）
  17:05
属性フィルタ、カテゴリ値で値がnullの場合がケア出来てないので、空白の選択肢を用意する

### 再現手順

1. <!-- バグが再現する手順をステップごとに記入してください -->
2. 
3. 

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(4件)

### [[FEATURE] データの有無に応じた UI のパターンを確認しやすくする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/566)

**作成者:** shgtkshruch  
**作成日:** 2025-05-23T09:39:49Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

- データの有無に応じた UI のパータンが増えてきた
  - #428
      - レポートが0件 or 1件以上
  - #438
    - metadata.json のデータの有無
- 自分はこれらの UI パターンを実装する際に、サーバーから取得するデータを変更したり、コード上で条件分岐を変えたりしているのですが、これが少し手間だなと思っています
- デザイナーがデータの有無で表示が切り替わる UI を確認する際にも、データを作ったり or 消したりする必要がありそうです
  - 例えばレポート一覧画面の Empty State を確認する場合は、レポートを0件にするなど


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
- [Storybook](https://storybook.js.org/) でデータがある場合の UI・データない場合の UI を登録して、サーバーのデータを変更することなくそれぞれの UI を確認できるようにする
   - 他にも UI をパターンごとに登録できるツールがあれば、そちらでも良いと思います
   - こういったツールがあると、エンジニアは手軽に手元で UI のパターンを確認できるようになりそうです
   - 導入する場合でも Storybook の実装・メンテナンスコストは多少かかるので、コストとメリットの比較は必要だと思います

# その他
- デザイナーがデータの有無に応じた UI を確認できるようにする場合は、Storybook など UI をカタログ化したものをホスティング環境もあると良さそうです
  - この場合はこの issue の解決が前提になるので、この issue が対応できてから必要があれば別 issue を切るでも良いかなと思いました
   - Chromatic (5000 snapshot まで無料), GitHub Pages, Netlify, etc...

**コメント:** なし

---

### [活用事例を集めて公開する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/564)

**作成者:** shingo-ohki  
**作成日:** 2025-05-23T03:27:56Z  
**内容:**

（[website の Issue](https://github.com/digitaldemocracy2030/website/issues) には存在せず、website は現段階では定例が存在しないため、一旦、広聴AI側で Issue を立ててみる）

# 目的
これから広聴AIを利用しようとするユーザーからすると、様々な活用事例があると導入ハードルが下がる
事例を集めて公開する




**コメント:** なし

---

### [[FEATURE][design] レポート管理画面：直感的に使いやすくしたい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/460)

**作成者:** UtkNggc  
**作成日:** 2025-05-07T16:09:28Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
現状の管理画面は直感的に使いにくい。
あるていど機能がそろった現時点で管理画面を改善したい。

▼現状
![Image](https://github.com/user-attachments/assets/600f5c6f-4dda-4b0d-a272-75088588f063)

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
・機能の見出しを上部バーにまとめる
・各機能ボタンはアイコンやトグルなど直感的にわかるものにする
・新規作成ボタンを右上に移動
・作成日時の秒数トルツメ（もしかすると時間も？）
・レポートのURL表示トルツメ
![Image](https://github.com/user-attachments/assets/3777dc40-ec37-4dd7-ba76-db6323453f23)

# デザイン時に検討するもの
・全レポートをエクスポート機能の位置
・エラー、作成中、のstatesの表現どうするか
・エラー、作成中、のステップの要 / 不要 -> 要るならステップ数やプログレスバーも検討
・もしレポートのURLが必要なら「シェア」みたいな表現でもいいかも。

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/437：見出し文言&位置変更

**コメント:** なし

---

### [[DOCUMENT]OpenAI APIの課金設定に関する混乱](https://github.com/digitaldemocracy2030/kouchou-ai/issues/292)

**作成者:** nishio  
**作成日:** 2025-04-13T00:52:56Z  
**内容:**

# 現在の問題点
非エンジニアにとって、OpenAI APIキーの取得と課金設定（クレジット購入）が必要であることが分かりにくく、ChatGPT Plusと混同しやすい。設定不備によりQuota超過エラー (429) が発生する。

「OpenAIの課金の設定してなかった」
「Error code: 429 - 'You exceeded your current quota, please check your plan and billing details.'」
「非エンジニアの場合、環境を設定した際にOpenAI APIに課金するというステップがわからない(たねのぶ)」
「OpenAIに課金=ChatGPT Plusだと思う人もいる」

# 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->
(解決策) READMEに、OpenAI APIキーの取得手順と、ChatGPT Plusとは別にAPI利用のためのクレジット購入（支払い方法登録）が必要であることを明記する。Quota超過エラーの意味と対処法も説明する。


**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (4件)

### [[client] ヘッダーの画像をデジタル民主主義2030のロゴに変更](https://github.com/digitaldemocracy2030/kouchou-ai/pull/588)

**作成者:** shgtkshruch  
**作成日:** 2025-06-02T12:07:40Z  
**変更:** +13 -26 (4ファイル)  
**マージ日:** 2025-06-02T16:20:48Z  
**内容:**

# 変更の概要
- client のヘッダーの画像をリポーターの画像から、デジタル民主主義2030のロゴに変更しました

# スクリーンショット

![image](https://github.com/user-attachments/assets/10ef5535-7695-452f-8e1b-3cf09bee7427)

# 変更の背景
- 元々の実装では、meta データの有無に応じでレポーターの画像の表示・非表示を切り替えていましたが、その挙動が不安定だった
- デザイナーが作成してる新しいデザインでは、ヘッダーの画像がレポーターの画像からデジタル民主主義2030のロゴに変更になった
  - https://github.com/digitaldemocracy2030/kouchou-ai/issues/585#issuecomment-2930346552

# 関連Issue
- fix: #585

# 動作確認の結果
- client のレポート一覧画面・レポート詳細画面のヘッダーにデジタル民主主義2030のロゴが表示されている

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [ ] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
  - ヘッダーに常に固定ロゴ画像を表示するようになりました。

- **リファクタリング**
  - ヘッダーコンポーネントからmeta情報に関連するロジックとプロパティが削除され、よりシンプルな構成になりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [team-mirai fork repoで実装した機能](https://github.com/digitaldemocracy2030/kouchou-ai/pull/582)

**作成者:** nasuka  
**作成日:** 2025-05-28T12:35:09Z  
**変更:** +432 -59 (17ファイル)  
**マージ日:** 2025-05-29T12:33:20Z  
**内容:**

# 変更の概要
機能としては以下の改修を反映
* https://github.com/team-mirai/kouchou-ai/pull/1
* https://github.com/team-mirai/kouchou-ai/pull/3
* https://github.com/team-mirai/kouchou-ai/pull/4
* https://github.com/team-mirai/kouchou-ai/pull/5

（機能単位でcommitをcherry pickをするのが手間なのでまとめて送っています 🙇 ）

# スクリーンショット
個別のPRに記載

# 変更の背景
詳細は個別のPRに記載

修正内容をざっと書くと、
* https://github.com/team-mirai/kouchou-ai/pull/1, https://github.com/team-mirai/kouchou-ai/pull/4
  * Claude Code用のmdを追加
* https://github.com/team-mirai/kouchou-ai/pull/3
  * Azure環境上で更新機能が動かないバグがあったので修正
* https://github.com/team-mirai/kouchou-ai/pull/5
  * 意見に元URLがある場合（e.g. githubのissue url）に、URLにとんで元データを確認したい -> とべるようにした


# 動作確認の結果
Azure環境のバグ関連
* Azure上で、意見グループのタイトル・説明と、レポートのタイトル・調査概要を編集できることを確認

ソースリンク関連
* ソースリンクの表示オプションをONにしてレポート作成すると、クリック時にソースページに飛べる
* ソースリンクの表示オプションをOFFにしてレポート作成すると、従来の形式でレポートが作成できる
* 機能実装前に作成していたレポートが問題なくclientで表示できる

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - レポート作成時に「ソースリンク機能」を有効化できる設定を追加しました。散布図のデータポイントをクリックすると、元データのURL（CSV列に含まれる場合）にアクセス可能です。
- **ドキュメント**
  - 開発・運用ガイドやシステム構成、セットアップ手順などを詳述した新しいドキュメント「CLAUDE.md」を追加しました。
- **バグ修正**
  - ログメッセージの誤記を修正しました（JSONファイル書き込み時のエラー表記）。
- **その他**
  - CSVインポート時に既存のIDやURL列を優先的に利用するよう改善しました。
  - レポート同期処理でのファイルダウンロード機能を拡充し、初期化処理の信頼性を向上しました。
  - ストレージへのファイルアップロード時の既存ファイルスキップ設定のデフォルト値を変更しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client] レポーター情報を表示するコンポーネントを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/581)

**作成者:** shgtkshruch  
**作成日:** 2025-05-28T09:53:47Z  
**変更:** +185 -50 (5ファイル)  
**マージ日:** 2025-06-03T07:38:19Z  
**内容:**

# 変更の概要
- client にレポーター情報を表示する Reporter コンポーネントを追加しました
- これまでレポーター情報を表示していた About コンポーネントを削除しました ✂️ 

# スクリーンショット
## 345px

![sm](https://github.com/user-attachments/assets/8744cfa4-3e90-466e-a541-4fb62cb17772)

## 768px

![md](https://github.com/user-attachments/assets/86544c35-b7f9-49db-88f4-429c7b7bac66)

## 1280px

![lg](https://github.com/user-attachments/assets/08619cd0-cfa0-4c75-bcc7-6721c3b68edb)

## 全文表示

![open](https://github.com/user-attachments/assets/e9f41e12-8ac7-425f-b3ad-61ae6819bfb8)

## Empty

![empty](https://github.com/user-attachments/assets/d51b1425-e7bc-453c-a459-7bd13c4ff094)


## loading & interaction

※ 画面収録の関係で Button などに hover してもカーソルが変わっていませんが、実際に操作するとカーソルがポインターになっています

https://github.com/user-attachments/assets/3d86d22d-798d-4561-a1b2-0faa9dd81a2b

## レポート詳細ページ

![slug](https://github.com/user-attachments/assets/7f7c14a8-8de4-45e9-9bcf-59ce9b16886e)


# 変更の背景
- Figma のデザインをレポーター表示用のコンポーネントを実装しました
  - https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=271-3763&t=UcTD1CXbrIY3IoBT-11

# 関連Issue
- #438 
- 上記 issue には Footer の実装も含まれていますが、そちらはデザインが決まり次第、別 PR で対応予定です

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- client のレポート一覧画面で以下の場合のレポーターの表示を確認
  - metadata.json が設定されている場合の表示
  - metadata.json が未設定の場合の表示（Empty）
- client のレポート個別画面でも、上記の metadata.json の設定に応じてレポーター情報が表示されていることを確認

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - 新しい「Reporter」コンポーネントを追加し、レポーター情報や画像、関連リンクを表示できるようになりました。
  - メッセージが長い場合、「続きを読む」ボタンで全文表示が可能になりました。

- **変更**
  - 「About」コンポーネントを削除し、「Reporter」コンポーネントに置き換えました。
  - メインコンテンツの最大幅を広げ、レイアウトを調整しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [限定公開のレポートでは検索エンジンにインデックスされないようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/574)

**作成者:** shingo-ohki  
**作成日:** 2025-05-26T08:48:51Z  
**変更:** +168 -5 (6ファイル)  
**マージ日:** 2025-06-03T01:43:13Z  
**内容:**

# 変更の概要
- タイトル通り

# 関連Issue
#520 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- 限定公開に設定されたレポートページに、`<meta name="robots" content="noindex, nofollow">` が追加されることを確認
- 限定公開されていたページを公開ページにした場合に上記が削除されることを確認

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - レポートの可視性（public/unlisted/private）がAPIレスポンスやクライアントで明示的に表示されるようになりました。
  - 「unlisted」レポートの場合、検索エンジンによるインデックスやリンク追跡が無効化されます。

- **バグ修正**
  - レポートの可視性に応じた適切なエラーメッセージやステータスコードが返されるようになりました。

- **テスト**
  - レポートの可視性や存在しないレポートに関するテストケースが追加・強化されました。

- **その他**
  - 一部型定義の整理とテスト設定の柔軟性が向上しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (2件)

### [[client] Footer にプロジェクトの概要をまとめる](https://github.com/digitaldemocracy2030/kouchou-ai/pull/589)

**作成者:** shgtkshruch  
**作成日:** 2025-06-03T10:39:31Z  
**変更:** +369 -133 (11ファイル)  
**内容:**

# 変更の概要
- Footer を新しいデザインに合わせて実装しました
  - 広聴AI やデジタル民主主義2030 プロジェクトの概要の情報がこちらに配置されます
- Figma: https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=509-3935&t=ourvDYxYXZbZlZBY-4

# スクリーンショット
## 375px
### Footer
![sm](https://github.com/user-attachments/assets/89a43141-dc1d-47e0-8503-8239571f114a)

### 謝辞
![image](https://github.com/user-attachments/assets/6646a1b6-8aa3-4c24-ae0d-87802c629d69)


### 免責
![image](https://github.com/user-attachments/assets/45cdb71c-df24-41e9-93e3-f197b83dbaf6)


## 768px
### Footer
![md](https://github.com/user-attachments/assets/2d70a1ce-ad81-42e4-8fe6-153b74cd5ebd)

### 謝辞
![image](https://github.com/user-attachments/assets/208ecf50-5e75-4b35-8f48-805a901e0b40)

### 免責
![image](https://github.com/user-attachments/assets/510ecbd0-44a0-4c32-a311-fd6d5a2923a5)


## 1280px
### Footer

![lg](https://github.com/user-attachments/assets/61351dff-79cc-488b-9df5-43c567ef164d)

### Empty

metadata が未設定で、レポートが0件の場合。
レポート件数が少ない場合でも、Footer はページ下部に固定して配置しています。

![empty](https://github.com/user-attachments/assets/a6c280de-2132-4689-9793-912c8cfbd7af)


### レポート詳細画面

![report-detail](https://github.com/user-attachments/assets/18f6a1cd-e90c-48b9-af74-2a8688a1b616)


### インタラクション
※ スクリーンキャプチャのツールの影響でボタンに hover した際にカーソルが変わっていませんが、実際は pointer になります

https://github.com/user-attachments/assets/86acd60b-e8d7-451b-97ac-9ff90fcec1c2


# 変更の背景

- Footer のデザインが更新されたので、実装も追従しました
- まだデザインシステムが未整備なので、Typography（font-family, letterSpacing など）は取り込めていません
  - こちらの issue でフロントエンドのデザインシステムの開発基盤ができたら、そこに Typography の定義をした後に、client から読み込む形にできればと思っています
  - https://github.com/digitaldemocracy2030/kouchou-ai/issues/586

# 関連Issue
- fix: #438 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

**コメント:** なし

---

### [claude.mdをアップデート](https://github.com/digitaldemocracy2030/kouchou-ai/pull/580)

**作成者:** nasuka  
**作成日:** 2025-05-28T05:25:39Z  
**変更:** +365 -33 (13ファイル)  
**内容:**

# 変更の概要
claude codeで/initを実行し、claude.mdをアップデート

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(2件)

### [Revert "Merge pull request #567 from take365/feature/auto-cluster-clean"](https://github.com/digitaldemocracy2030/kouchou-ai/pull/579)

**作成者:** nasuka  
**作成日:** 2025-05-27T08:58:08Z  
**変更:** +247 -1242 (27ファイル)  
**内容:**

This reverts commit c559f8e256b0966e959140c8dfbe7eeabf96a937, reversing changes made to 196a4534ff71a08bd2cc3c4fe4d21ea4159a26ab.

# 変更の概要
https://github.com/digitaldemocracy2030/kouchou-ai/pull/567
こちらのrevert

# 変更の背景
以下の問題が起きていたのでrevertします

* debug logが大量に出力される
* ファイルによってはembedding実行時に以下のエラーが出る（embedding モデルはopenai）

```
api-1                  | openai.BadRequestError: Error code: 400 - {'error': {'message': "'$.input' is invalid. Please check the API reference: https://platform.openai.com/docs/api-reference.", 'type': 'invalid_request_error', 'param': None, 'code': None}}
```

エラーが起きたのは以下のcsvファイル
https://github.com/team-mirai/random/tree/devin/1747880446-generate-pr-csv/pr_analysis_results/merged

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [ ] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **新機能**
	- なし

- **機能変更**
	- レポート作成時の「スキップ」オプションや自動クラスタ数調整機能が削除され、すべての処理ステップが常に実行されるようになりました。
	- AIプロバイダー選択から「使用しない」オプションが削除されました。
	- クラスタ設定が簡素化され、手動でクラスタ数を指定する方式に統一されました。

- **UIの改善**
	- AI設定・クラスタ設定画面がシンプルになり、不要なチェックボックスや入力項目が削除されました。

- **バグ修正**
	- なし

- **ドキュメント**
	- なし

- **その他**
	- 内部処理の簡素化・不要なコードや型定義の削除が行われました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [LLMのスキップ、自動クラス数決定、タイトル省略](https://github.com/digitaldemocracy2030/kouchou-ai/pull/567)

**作成者:** take365  
**作成日:** 2025-05-23T09:47:35Z  
**変更:** +1242 -247 (27ファイル)  
**内容:**

# 変更の概要

1. グループ数を自動で決定するを追加
2. AIプロバイダーに「使用しない」を追加。（LLM全スキップ）
3. 抽出、初期、統合、要約にスキップを追加
4. タイトル、概要の必須を外し、省略時タイトル自動補完
5. 分析の概要の説明からOpen AIを削除（LLMには触れない）
6. 分析手順でスキップした手順ではモデル表示はスキップ
7. グループ数を自動で決定の場合にグループ数試行結果ボタン・画面表示

# スクリーンショット
1. 
![Screenshot_1](https://github.com/user-attachments/assets/4f9e8867-0dac-45b3-b044-23fcbc6ac746)
2. 
![Screenshot_2](https://github.com/user-attachments/assets/d2a407a0-d188-4eed-8771-36103086fab9)
3. 
![Screenshot_3](https://github.com/user-attachments/assets/5a40ab5e-3e5c-49a9-949b-30e01bf1194e)
4. 
![Screenshot_5](https://github.com/user-attachments/assets/c4dfff8b-213e-4695-a4ed-c6b43b9e6acf)
5. 
![Screenshot_6](https://github.com/user-attachments/assets/de6249da-53ce-4477-adde-ce03348d9d8e)
6. 
![Screenshot_8](https://github.com/user-attachments/assets/09017439-e726-40bd-93d2-6e94a43fdd30)
7. 
![image](https://github.com/user-attachments/assets/df27af90-82ab-45b5-bf94-4dc71285c9bc)

# 変更の背景
- イシュー対応

# 関連Issue
- (情報整理)試行錯誤の負担を減らす [#221](https://github.com/digitaldemocracy2030/kouchou-ai/issues/221)
- [BUG] OpenAI API以外のLLMを使っても、OpenAI APIを利用したと表示される [#494](github.com/digitaldemocracy2030/kouchou-ai/issues/494)
-[FEATURE]CSVアップロード時にタイトルや説明文を自動で埋めてほしい [#305](https://github.com/digitaldemocracy2030/kouchou-ai/issues/305)
-[ALGORITHM]クラスタ数、エンベディング、次元圧縮の違いのモデルの違いによるシルエットスコア（まとまり具合）の変化の調査 [#516](https://github.com/digitaldemocracy2030/kouchou-ai/issues/516)

# 動作確認の結果
・各種スキップ状態でレポート作成
・自動クラスタでレポート作成
・フィルター機能確認

# CLAへの同意
- [X ] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ X] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **新機能**
  - レポート作成時にスキップフラグや自動クラスタリング設定をAPIに渡すオプションを追加しました。
  - 自動クラスタリングの有効化やクラスタ範囲設定（Lv1, Lv2）を導入しました。
  - AIモデル未使用の設定（"none"）を追加し、その場合はAI処理をスキップします。
  - 自動クラスタリング結果の可視化やシルエットスコアの表示機能を追加しました。

- **改善**
  - タイトルや紹介文の未入力時に自動生成される仕組みを導入しました。
  - クラスタ範囲やクラスタ数の入力値バリデーションを強化し、不正値時に警告を表示します。
  - ステップのスキップ状態やAIモデル名がタイムライン上でわかりやすく表示されるようになりました。

- **バグ修正**
  - トークン数超過の入力に対し、自動でトークナイズし長さを調整する処理を追加しました。

- **ドキュメント**
  - 各設定項目に対する説明やヘルプテキストを追記しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

