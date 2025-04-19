# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-04-09 から 2025-04-16 まで

## Issues

### 過去7日間に完了されたissue (10件)

### [[DOCUMENT]docker-compose → docker compose](https://github.com/digitaldemocracy2030/kouchou-ai/issues/298)

**作成者:** nishio  
**作成日:** 2025-04-13T01:41:53Z  
**内容:**

https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1744505244553429

NISHIO Hirokazu
>「README.md記載の「docker-compose up」ではコマンド未発見エラー：「docker compose up」とハイフンなしにして解決」
>(解決策) READMEのコマンドを docker compose up (ハイフンなし) に修正する。

これはどっちが正しいんだろ


Pin
docker-compose が v1、docker compose が v2 で、前者が廃止予定で後者に徐々に置き換わっていっています
そのため docker-compose コマンドが入っていない環境が増えてきていて、v2 出てからもう結構経つので、基本は v2 に寄せていく方針が良さそうです
逆に docker-compose があって docker compose がない状況になるのは、v2 以前に構築した docker 環境をアップデートせずに使っている場合くらいかなと思いますが、そういう人は自力で読み替えられそうかなと:blob-thinking:（おそらく docker 歴5年〜の人なので）

**コメント:** なし

---

### [[BUG]階層図を全画面表示にすると一番右上の要約文が「全画面終了」ボタンの後ろに隠れてしまう](https://github.com/digitaldemocracy2030/kouchou-ai/issues/278)

**作成者:** masatosasano2  
**作成日:** 2025-04-11T01:26:15Z  
**内容:**

### 概要

全画面表示の「全画面終了」ボタンの後ろに要素の要約文が一部隠れてしまい、読めないことがある。

### 再現手順

1. レポート画面を開く
2. 「階層図」chartに切り替える
3. 「全画面表示」ボタンを押す
4. 一番右上のパネルにマウスカーソルを重ねる

発生条件：正確な条件は未調査。他のchat（全体図、濃い意見グループ）でもノードの配置によっては発生しそう。

### 期待する動作

要約文が隠れないで欲しいです。

修正されるにあたって以下の点が満たされてほしいのですが、具体的な修正案はありません。
・画面右上に要素が密集していても問題ないようにする
　（なので、おそらく「要約文を要素の左上に出す」ではNG）
・「全画面終了」ボタンが隠れてしまい見つけられないことを防ぐ
　（なので、おそらく「要約文を最前面に出す」ではNG）

### スクリーンショット・ログ

![Image](https://github.com/user-attachments/assets/d0fbad20-e890-4901-b39f-1ebc3aaae5d2)


**コメント:** なし

---

### [[FEATURE]管理画面でCSVをアップロードしたとき、エラーで落ちても進捗状況を自動更新する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/277)

**作成者:** masatosasano2  
**作成日:** 2025-04-11T01:04:01Z  
**内容:**

# 背景
正常に動作するとstep1(抽出)からstep8(可視化)まで自動更新され、その後レポートのURLが表示されるが、
エラーで落ちると進捗が更新されず、ページを再読込して初めてエラーになったことが可視化される。

実際に発生したケース：OpenAPIのクレジットが足りず初手の抽出で落ちた。
正確な発生条件：未調査

# 提案内容
`client-admin/app/page.tsx` で `useReportProgressPoll` の結果が "completed" の場合にページがリロードされているが、 "error" の場合の処理も必要そう。

**コメント:** なし

---

### [[FEATURE]adminのレポート一覧画面にも作成日時を追加する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/268)

**作成者:** nasuka  
**作成日:** 2025-04-09T05:09:39Z  
**内容:**

# 背景
* client側ではレポート一覧画面で作成日時が表示されるようになったが、adminでは表示がされない
  * client側のPR: https://github.com/digitaldemocracy2030/kouchou-ai/pull/245


# 提案内容
* client側と同様、admin側でも一覧画面で各レポートの作成日時を表示する

**コメント:** なし

---

### [初期設定時のentrypoint.shエラー](https://github.com/digitaldemocracy2030/kouchou-ai/issues/243)

**作成者:** nasuka  
**作成日:** 2025-04-06T11:02:11Z  
**内容:**

## バグの内容
初期設定時にentrypoint.shエラーが出たため、ChatGPTに解決策を聞いたものとなります。
http://localhost:3000/　http://localhost:4000/のページは見れるようになりました。
環境がWindows10で、PowerShell 5.xです。

【エラー内容①】
client-1 exited with code 0
/entrypoint.sh: line 5: syntax error: unexpected "fi" (expecting "then")

●エラーの意味：
client（レポート表示画面）の起動時に、entrypoint.sh という起動スクリプトの中に文法ミスがあります

正確には：
if 文が書いてあるけど、その中に then がない
そのまま fi（if の終わり）に到達して、エラーになってる

●修正案１（？）
if [ "$NODE_ENV" = "production" ]; then
  npm run start
else
  npm run dev
fi

●修正案２（？）
#!/bin/sh
# 起動時に全て削除した上でbuildしなおす
if [ -d ".next" ]; then
  rm -rf .next
fi  

# build時にAPIサーバーを参照するため、APIサーバーの起動を待ってからbuildを行う
npm run build
exec npm run start

●修正案３（？）
Windowsメモ帳が改行コードをCRLF（\r\n）にしてしまうせいで、Docker内で「: not found」や syntax error: unexpected "fi" が出る。
✅ 対処方法（メモ帳ユーザーでもOK）
PowerShellで改行コードをLFに変換する（推奨）
以下を PowerShell で kouchou-ai フォルダ内で実行：
＜PowerShell＞
手順１（PowerShell 7.x対応）
cd ~\kouchou-ai
(Get-Content .\client\entrypoint.sh) -join "`n" | Set-Content -NoByteOrderMark -Encoding utf8 .\client\entrypoint.sh

手順１修正版コマンド（PowerShell 5.x対応）
(Get-Content .\client\entrypoint.sh) -join "`n" | Set-Content -Encoding UTF8 .\client\entrypoint.sh
手順２
docker-compose down
docker-compose up --build






【エラー内容②】
client-1 | ./entrypoint.sh: line 1: ﻿#!/bin/sh: not found
この「﻿」は見えないBOM文字。Windowsのメモ帳で保存した .sh ファイルはUTF-8 with BOMになりやすい。
手順１：entrypoint.sh の最初の行のBOMを完全に除去する
●修正案②ー１（PowerShell 7.x対応）
Get-Content .\client\entrypoint.sh | Out-File -Encoding ASCII -NoNewline .\client\entrypoint.sh
●修正案②ー２（PowerShell 7.x対応）
Get-Content .\client\entrypoint.sh | Set-Content -Encoding UTF8 -NoByteOrderMark .\client\entrypoint.sh
●修正案②ー３（PowerShell 5.x対応）
[System.IO.File]::WriteAllLines('.\client\entrypoint.sh', [System.IO.File]::ReadAllLines('.\client\entrypoint.sh'), (New-Object System.Text.UTF8Encoding($false)))


手順２：フルリセットして再起動
docker-compose down --volumes --remove-orphans
docker-compose build --no-cache
docker-compose up


---
こちらのイシューはGoogle Form経由で投稿されたものです

**コメント:** なし

---

### [[FEATURE]おすすめクラスタ数設定機能](https://github.com/digitaldemocracy2030/kouchou-ai/issues/241)

**作成者:** nishio  
**作成日:** 2025-04-06T03:54:15Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

>yuneko
意見グループ数(クラスタ数)をどのくらいで試せばいいのか、目安が知りたいです。この件数(列数)だとまずこれにするといいよというのがわかると、お試しで自分のデータを試したときに、うまく行ったなという感覚になりやすい気がします。
NISHIO Hirokazu
模索段階ではあるんですけど漠然と思ってることとしては、データが1000件あるなら10→100にするのが良さそうという感じです
8000件だったら20→400、125件だったら5→25
∛1000=10ということです。
その理屈でいうとサンプルの400件のデータは7→50がいい気がしましたが、今の5→50と7→50に変えたのとでどちらが良いのかを雰囲気ではなくちゃんと科学的根拠を持って言えるようになるといいなぁと思ってて、その研究の緊急度が低くて放置されていますw
yuneko
いいレポートを明らかに評価できると嬉しいですね。(嬉しいけど放置はされそう)
ヒューリスティクスでも少し評価できるなら、一定の初期値で固定しておくより、できるならコメントの件数によって勝手にクラスタ数を変更する(例えば∛の切り捨てとか)にした方がユーザーフレンドリーかもと思いました。もしくは、おすすめクラスタ数を選択したら、勝手にいい感じのクラスタ数に変更するなど。

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

案0: READMEに書く

案1: CSVアップロード後に「おすすめクラスタ数設定 7→50 [button: この設定にする]」みたいな表示を出す
 
問題点
- Google Spreadsheetから読むのってクライアントサイドだったかな... サーバサイドで読むまでデータ量がわからないのだとするとこの方法では無理
- 一旦Google Spreadsheetは無視すると言うのも手

案2: パラメータを変えて再分析する機能ができた後なら、前の分析の情報を使っておすすめを出すことができるかも？

**コメント:** なし

---

### [[FEATURE]クラスタ数変更を直接入力可能にする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/222)

**作成者:** nishio  
**作成日:** 2025-04-02T16:27:55Z  
**内容:**

# 背景

<img width="302" alt="Image" src="https://github.com/user-attachments/assets/257a3fed-faab-4e86-ba90-8fd6c3126f42" />

データが8000件とかある場合、20 > 400 とかにしたくなるわけだけど、現状では350回のクリックが必要では

# 提案内容

クラスタ数変更を直接入力可能にする

**コメント:** なし

---

### [[FEATURE]レポート一覧に作成日時を追加する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/218)

**作成者:** ei-blue  
**作成日:** 2025-04-02T03:55:52Z  
**内容:**

# 背景
現状、レポート一覧ではレポート名でしか区別がつけられないが、
- 同じ内容で複数回レポートを作成と区別がつかない
- 作成したレポートがいつ時点までのアップデートを反映したものかわからない

ため、レポート作成日時があると便利なのではと思いました。

# 提案内容
以下は一案です。

- レポート作成時にreport_status.jsonに日時を追加
- レポート一覧ページでタイトルの下に日時を表示


**コメント:** なし

---

### [[REFACTOR] フロントエンドのコードを Biome でフォーマットをする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/84)

**作成者:** shgtkshruch  
**作成日:** 2025-03-18T03:59:30Z  
**内容:**

# 現在の問題点
<!-- 現在のコードの何が問題なのか、どのような技術的負債があるかを説明してください -->

- この issue のスコープとしては、フロントエンドに関わる client, client-admin, utils/dummy-server を想定しています
- コードの formatter が導入されていないため、開発者によってコードの書き方（ex. 改行、スペースの入れ方）に差分出てくる可能性がある

# 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->
- フロントエンドで広く利用されている [prettier](https://prettier.io/) を導入して、コードのフォーマットを自動化する
  - 一部 ESLint でフォーマットのチェックをしているところも prettier に寄せたい気持ちです
    https://github.com/digitaldemocracy2030/kouchou-ai/blob/c0a10e33f3f0ea458525a19a55a887b3f3f4792b/client/eslint.config.mjs#L16-L20
    https://github.com/digitaldemocracy2030/kouchou-ai/blob/c0a10e33f3f0ea458525a19a55a887b3f3f4792b/client-admin/eslint.config.mjs#L16-L20
  https://github.com/digitaldemocracy2030/kouchou-ai/blob/c0a10e33f3f0ea458525a19a55a887b3f3f4792b/utils/dummy-server/eslint.config.mjs#L16-L20
- pre-commit or pre-push hook などで prettier を実行する仕組みを導入して、フォーマットされたコードが GitHub に push されるようにする
  - これを実現するツールとしては [husky](https://github.com/typicode/husky) や [lefthook](https://github.com/evilmartians/lefthook) などがありますが、個人的には実行のパフォーマンスと設定のシンプルさから lefthook が良いかなと思っています

**コメント:** なし

---

### [[FEATURE] GoogleAnalytics 対応](https://github.com/digitaldemocracy2030/kouchou-ai/issues/54)

**作成者:** nanocloudx  
**作成日:** 2025-03-16T03:47:30Z  
**内容:**

# 背景
レポートがどれくらい表示されたのかなど統計を知りたいニーズがありそう

# 提案内容
トラッキングIDを環境変数で指定した場合は、必要なスクリプトが読み込まれるようにする


**コメント:** なし

---

### 過去7日間に作成されたissue (27件)

### [[FEATURE] LLMが出力した結果の手動修正機能がほしい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/310)

**作成者:** nasuka  
**作成日:** 2025-04-15T05:38:53Z  
**内容:**

# 背景
* LLMが出力したクラスタ名や説明、argumentが適切でない場合がある
  * e.g.
    * 公開するのに不適切な単語や表現がクラスタ名に含まれている
    * 他のクラスタと同一の内容がクラスタ名に含まれている
* このようなケースにおいては、LLMのアウトプットを見た後に人間が手動で文言を修正したい

# 提案内容
LLMが出力したテキスト（クラスタタイトル・説明・概要・argument）について、手動で編集する画面をadminに設け、レポートに編集内容を反映する


(admin)
* 上記の編集画面を設ける
  * 編集後のデータを編集用のendpointに送る

(api)
* 編集用のendpointを実装する
  * リクエストで受け取ったデータを各種中間ファイル（args.csv等）に保存
  * hierarchical_aggregation.pyを再度実行し、更新後のデータでhierarchical_result.jsonを保存する

そもそも全要素を編集できるようにするかというのは議論の余地がある。やるとしても、まずはクラスタ名のみを対象にするなど、部分的に始めていくのが良さそう。
また、透明性担保のために編集履歴を残すようにするかも議論の余地がある。

**コメント:** なし

---

### [[FEATURE] HTML フォーム入力による広聴 AI システムの簡易デプロイ機能](https://github.com/digitaldemocracy2030/kouchou-ai/issues/308)

**作成者:** shingo-ohki  
**作成日:** 2025-04-15T00:11:32Z  
**内容:**

# 背景

先日のハッカソンに参加して、改めて広聴 AI の導入について技術的なハードルの高さとその導入サポートにに課題がありそうだと感じました。

#300 によって Windows 環境でのセットアップは大きく改善されますが、
- PC へのソフトウェアインストール自体が難しい場合もある
- Azure 環境の構築に make コマンドが必要（WSL2 などのセットアップ含む）

といった点が、導入の障壁として残っている（そこまで現段階で対応するかどうかは議論の余地あり）と考えています。

# 提案内容

## 概要
HTML フォーム + Azure Functions（または Azure に限らず同等のことが実現できる環境） のセットを提供することで、ユーザーがフォームに必要な情報（Azure 認証情報、OpenAI API キーなど）を入力するだけで、自動的に自身の Azure 環境上に広聴 AI の環境を構築できる仕組みを提供します。

## 想定構成

![Image](https://github.com/user-attachments/assets/cab67945-f74a-49d6-8650-88249f766d57)

- static form(HTML フォーム)
  - Azure Storage の Static Web Hosting に設置
  - 必要な認証情報や設定項目を入力
- Azure Functions
  - 入力された情報をもとに、Azure 上に必要なリソース（Container Apps 等）を作成・デプロイ

※フォームと Functions はセットで提供され、ユーザー操作は基本的にフォーム入力のみで完結

## 構築される環境
- 広聴 AI のシステム（Azure Container Apps による server, client, client-admin 構成）
- 利用料金はユーザーの Azure アカウントにて発生
- Static HTML と Azure Functions はプロジェクト側または第三者がホスティング（マネージドサービスかつ無料枠の想定、要検証）

# 利点
- PC 操作に不慣れな方でも数ステップで導入が可能
- コマンド操作・ローカル環境構築が不要
- ユーザーごとの環境依存によるトラブル発生率の低下
- 実証実験・テスト環境など、導入コストを下げたい場面での展開が容易
- サポート負担の軽減

# 懸念点・検討課題
- そもそもこのニーズはあるか？今やるべきか？
- フォーム経由で機微情報（Azure 認証情報、OpenAI API キーなど）を扱うこと
- Azure アカウントの事前取得が必要
- Static HTML + Azure Functions をプロジェクトとしてホスティングできるか？

**コメント:** なし

---

### [[FEATURE]「全体図」「濃い意見グループ」のUI/UX改善](https://github.com/digitaldemocracy2030/kouchou-ai/issues/306)

**作成者:** masatosasano2  
**作成日:** 2025-04-13T11:20:06Z  
**内容:**

# 背景

操作しててたまたま以下に気づいたが、見ただけでは分からない。
・範囲指定（ドラッグ）すると拡大できること
・拡大した状態から元の倍率に戻すにはダブルクリックすること

# 提案内容

ズームイン/アウトのUIがあるとよさそう


**コメント:** なし

---

### [[FEATURE]CSVアップロード時にタイトルや説明文を自動で埋めてほしい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/305)

**作成者:** masatosasano2  
**作成日:** 2025-04-13T07:45:30Z  
**内容:**

# 背景
入力の一手間を減らしたい
入力漏れでエラーにならないでほしい

# 提案内容
- タイトルと説明文を optional にする
- 空の場合にCSVの内容から自動生成する　※説明文は必須でないかも

**コメント:** なし

---

### [[FEATURE]CSVアップロード時にコメント列を自動で特定してほしい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/304)

**作成者:** masatosasano2  
**作成日:** 2025-04-13T06:59:09Z  
**内容:**

# 背景
コメント列の指定の一手間を減らしたい

# 提案内容
- コメントの列名が「コメント」「comment」「意見」「要望」「投稿」などであったらデフォルトでその列を指定してほしい
- 候補の列名はハードコードで一定カバーし、マッチしなかったらLLMに一番それっぽいのを選んでほしい
- 列が1つしかなかったらそれをコメント列と判定してほしい
- 数値/日付型でない列が1つしかなかったらそれをコメント列と判定してほしい

**コメント:** なし

---

### [[FEATURE]CSVアップロード時にデフォルトでクラスタ数が設定されてほしい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/303)

**作成者:** masatosasano2  
**作成日:** 2025-04-13T06:58:07Z  
**内容:**

# 背景
クラスタ数の設定の一手間を減らしたい

# 提案内容
- クラスタ数について「この設定にする」を押さないと推奨設定通りにならず、そのことが詳細画面を開かないとわかりにくい
- クラスタ数のデフォルト値より小さい件数のCSVを取り込んだ時、先に進もうとするとアラートが出てくれるのは嬉しいが、それなら最初から推奨設定をセットして欲しい


**コメント:** なし

---

### [[FEATURE]「公開」ボタンを押した時の効果を分かりやすくする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/302)

**作成者:** masatosasano2  
**作成日:** 2025-04-13T06:51:12Z  
**内容:**

# 背景
キャプションが「公開」の状態のボタンを押すと非公開になり、「非公開」の状態のボタンを押すと公開になる。
キャプションの意味は現在の状態であってボタンを押した時に発生するアクションではないので間違ってはいないのだが、
client-adminでもclientでも大抵のボタンのキャプションは押した時のアクションに近いので、やや紛らわしい。

# 提案内容
- 案1：マウスオーバー中のみ「非公開にする」「公開にする」などのヒントを表示する
- 案2：マウスオーバー中のみ逆の状態の見た目にする
- 案3：ボタンからスイッチに変える
- 案4：ボタンからチェックボックスに変える　＊この場合、「非公開にする」チェックの方が自然かも

**コメント:** なし

---

### [[FEATURE]Windowsユーザの利用環境構築](https://github.com/digitaldemocracy2030/kouchou-ai/issues/300)

**作成者:** nishio  
**作成日:** 2025-04-13T03:36:08Z  
**内容:**

# 背景

Windowsユーザーがkouchou-aiを利用する際、現在は複数のセットアップ方法（WSL2+Docker、Docker単体、生環境）があり、開発者ではなくただ使いたいユーザーにとって環境構築が難しい状況です。特に環境変数の設定やパスの問題が発生しやすく、環境ごとの違いが多くてトラブルシューティングも困難です。

# 提案内容

Docker-outside-of-Docker（DooD）方式を使用して、Windowsユーザー向けのセットアップを簡素化します。

## ユーザストーリー
- Docker Desktopをインストール
- zipでrepoをダウンロード
- OpenAI APIキーを取得して$5くらいチャージする
- setup_win.batを実行
- ブラウザでアクセス可能になる

## 実装方法
setup_win.batがDocker環境内にUbuntuコンテナを作成し、その後の作業は全てDocker内で実行します。具体的には：

1. OpenAI APIキーの入力プロンプトを表示
2. 環境変数を自動設定
3. docker composeでサービスを起動

## メリット
- WSL2の複雑な設定が不要
- 環境変数の問題を回避
- Windowsの環境の違いによる問題を解消
- コマンドラインの知識が不要

## 技術的詳細
- ホストのDockerソケットをマウント（/var/run/docker.sock）
- 必要なポート（3000, 4000, 8000）をマッピング
- 環境変数を適切に設定

これにより、Windowsユーザーでも簡単にkouchou-aiを利用できるようになります。


**コメント:** なし

---

### [[FEATURE]CSVダウンロード時の文字化け (Windows)](https://github.com/digitaldemocracy2030/kouchou-ai/issues/297)

**作成者:** nishio  
**作成日:** 2025-04-13T01:36:52Z  
**内容:**

# 背景
Admin DashboardからレポートデータをCSV形式でダウンロードすると、WindowsのExcelなどで開いた際に文字化けが発生する。

「Dashboard reportsのCSVファイルをダウンロードしたら、Windowsでは文字化けする」


# 提案内容
(解決策) CSVファイルを生成する際に、文字コードをUTF-8 BOM (Byte Order Mark) 付きで出力するなどのオプションを選択可能にする。



**コメント:** なし

---

### [[FEATURE]LLM出力形式の揺らぎによる抽出エラー](https://github.com/digitaldemocracy2030/kouchou-ai/issues/296)

**作成者:** nishio  
**作成日:** 2025-04-13T01:22:24Z  
**内容:**

# 背景
LLMからの応答が、プロンプトで期待したJSON形式（例: 文字列リスト [str]）と異なる形式（例: オブジェクトリスト [{“意見”:str, “トピック”:str}]）で返ってくることがあり、データ抽出が失敗したり、抽出される意見数が少なくなったりする。

「Rate limitかと思われた抽出データが少ない事例の一つにおいて、JSON List[str]ではなく[{“意見”:str, “トピック”:str}]が返っていたせい(nishio)」
「これのせいで抽出されるデータが減るのは困るし、それに多分ユーザは気づけなくて「こんなもんか〜」となりそう」

# 解決策

プロンプトを改善し、出力形式の指示をより明確かつ堅牢にする。

LLMからの応答をパースする際に、期待する形式以外もある程度許容する、またはエラーハンドリングを強化して異常を検知できるようにする。

**コメント:** なし

---

### [OpenAI API Rate Limit関連の問題](https://github.com/digitaldemocracy2030/kouchou-ai/issues/295)

**作成者:** nishio  
**作成日:** 2025-04-13T01:19:38Z  
**内容:**

## 課題

広聴AIのレポート生成プロセスにおいて、OpenAI API の Rate Limit (利用制限) に起因する問題が複数発生しています。

1.  **Rate Limit によるエラー頻発 (特にTier1ユーザー):**
    *   OpenAI API を使い始めたばかりのユーザー (Usage tier が Tier 0 や Tier 1) は、分間あたりのリクエスト数 (RPM) やトークン数 (TPM) の制限が非常に厳しいです。
    *   そのため、数百件程度のコメントデータであっても、レポート生成中に RateLimitError (HTTPステータスコード 429) が頻発し、処理が遅延したり失敗したりします。
    > 「OpenAI始めたばかりだとTier1問題」
    > 「300コメント程度でもrate limitが出る」
    > (大量のRateLimitErrorログ引用: `ERROR:root:Task ... failed with error: Error code: 429 - {'error': {'message': 'Rate limit reached for gpt-4o-mini ...` )

2.  **Rate Limit エラー発生時の不完全なレポート生成:**
    *   現在の実装では、Rate Limit エラーが発生しても、処理は停止せず続行されます。
    *   リトライが上限に達した場合、該当部分のデータ取得（例: クラスタラベルの生成）がスキップされ、結果として一部の情報が欠落した「不完全なレポート」がエラー表示なく生成されてしまうことがあります。
    *   ユーザーは、Rate Limit が原因であることや、レポートが不完全であることに気づきにくい状態です。
    > 「エラーでラベル名が取得できませんでしたが複数現れた」
    > 「今回のケースでは、ラベル名のみ生成に失敗していた」
    > 「rate limit errorが出るもののうごいているので、処理は正常にされたと思っていましたが、どうやらリトライされず一部エラーになったまま処理が終了されちゃったみたいです」
    > 「中途半端に抽出されたレポートができるのは不適切なので、rate limitの時にエラーとしてスルーしないようにする必要がある(nishio)」

## 解決策案

**1. Rate Limit エラー頻発への対策:**

*   **指数バックオフ付きリトライ処理の実装:** API呼び出し部分で RateLimitError (429) を検知した場合、待機時間を指数関数的に増やしながら、複数回（上限を設定して）API呼び出しを再試行する処理を実装します。
*   **ドキュメントでの周知:** README などに以下の情報を記載します。
    *   OpenAI API の Rate Limit の存在と Tier システムについて。
    *   自分のアカウントの Tier と Limit を確認する方法（OpenAI Platform の設定画面へのリンク）。
    *   Tier を上げるための条件（例: 一定額の支払いと利用期間）と公式ドキュメントへのリンク。「Rate limits - OpenAI API」「RateLimitError | OpenAI Help Center」
*   **(検討) 代替APIへの対応:** OpenRouter など、Rate Limit が比較的緩い、または管理しやすい API サービスへの対応を検討します。「OpenRouter APIにするのも候補の一つ。」
*   **(検討) 意図的な待機時間の挿入:** API リクエスト間に短い sleep を入れることで、瞬間的なリクエスト集中を緩和します。

**2. 不完全なレポート生成の防止:**

*   **エラーハンドリングの強化:** Rate Limit エラーが発生し、上記のリトライ処理を行っても成功しない場合は、**処理をスキップせずにレポート生成プロセス全体を明確なエラーとして中断・失敗させる**ように修正します。これにより、ユーザーは問題発生を確実に認識でき、不完全なデータが出力されることを防ぎます。
    *   リトライ回数には上限を設定し、無限ループ（や無限課金）を防ぎます。「無限リトライはしないので(元データがおかしい時に無限にお金を使う)3回くらい試して先に進んでるかと(nishio)」

**コメント:** なし

---

### [[FEATURE]ラベルが多い時の重なりの問題](https://github.com/digitaldemocracy2030/kouchou-ai/issues/294)

**作成者:** nishio  
**作成日:** 2025-04-13T00:59:47Z  
**内容:**

## 課題

広聴AIのレポート画面に表示されるプロットグラフにおいて、分析によって生成されたクラスタ（意見グループ）の数が多い場合に、各クラスタを示すラベルが互いに重なり合ってしまい、判読が困難になるという問題があります。

特に、自治体での利用など、詳細な分析のためにクラスタを細かく分ける傾向がある場合に、この見にくさが顕著になります。
> 「自治体的には、クラスタを細かく分ける方向の議論が強い。」
> 「UIの観点で、プロットグラフがそれに対応していけるとよさそう。」
> 「ラベルは重なって見にくくならないようにできるとか」

現状のままでは、せっかく詳細に分類された意見グループの内容を、グラフ上で直感的に把握することが難しくなっています。

## 解決策案

グラフ上でのラベルの重なりを軽減し、視認性を向上させるために、以下のいずれか、または組み合わせによる改善策を検討します。

*   **ラベル表示の選択的ON/OFF:** ユーザーが表示したいラベルを選択したり、一定数以上のラベルはデフォルトで非表示にする機能を追加する。
    > 「ラベル全部は表示しない設定」
*   **重なり回避アルゴリズムの導入:** ラベルの位置を自動的に調整し、重なりを最小限に抑えるアルゴリズムを実装する。
*   **インタラクティブなラベル操作:** ユーザーがグラフ上でラベルをドラッグ＆ドロップして任意の位置に移動できるようにする。
*   **ズームレベルに応じた表示制御:** グラフの拡大率に応じて、表示するラベルの数を調整する（例: 縮小時は主要なラベルのみ表示）。

**コメント:** なし

---

### [[FEATURE]レポート表示画面上で、使用したプロンプトを直接編集可能にする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/293)

**作成者:** nishio  
**作成日:** 2025-04-13T00:58:21Z  
**内容:**

## 課題

現在、生成された広聴AIレポートの内容（特に要約文言など）に不満があり修正したい場合、以下の手順を踏む必要があり、手間と時間がかかります。

1.  Admin Dashboard画面に戻る。
2.  対象のレポートを探して複製する。
3.  複製したレポートの設定（主にプロンプト）を調整する。
4.  再度レポート生成を実行する。

> 「ユーザーとして、広聴AIレポート画面で出力された成果物に不満があり作り直したい場合に、手間と時間がかかる（Admin Dashboard画面に戻り、レポートを複製し、文言調整を行う。1度の修正ごとにレポートが1枚のレポートを生成する必要がある）」

特に、プロンプトの微調整を繰り返して最適な出力結果を得たい場合、この往復作業は大きな負担となります。

## 提案

レポート表示画面（例: `http://localhost:5173/reports/{report_id}`）に、そのレポート生成に使用されたプロンプトを表示し、**直接編集および更新（再生成）** できる機能を追加します。

**具体的な流れ:**

1.  レポート表示画面の下部など（例: 現状「分析手順」が表示されている箇所）に、編集可能なプロンプト入力欄を表示する。
2.  ユーザー（※後述の権限者のみ）がプロンプトを編集する。
3.  「更新して再生成」のようなボタンをクリックすると、編集後のプロンプトを使用してレポートの再生成処理が開始される。
4.  レポート表示画面が更新され、新しい結果が表示される。

これにより、Admin Dashboardに戻ることなく、試行錯誤しながらレポートの質を効率的に向上させることが可能になります。（参考: TTTCTurboのレポート画面における同様の機能）
> 「TOBE：利用したプロンプトを編集、更新できる（参考TTTCTurboのレポート画面）」

## 考慮事項

*   **権限管理:** 広聴AIでは、レポートの作成権限を持つユーザーと閲覧権限のみを持つユーザーが存在する想定です。プロンプトの編集・再生成機能は、**レポート作成権限を持つユーザーのみ**が利用できるように制限する必要があります。閲覧権限のみのユーザーには、プロンプトの表示は行うかもしれませんが、編集・再生成ボタンは表示しない、または無効化するなどの制御が必要です。
*   **コスト:** レポートの再生成にもLLM APIのコストが発生するため、実行前に確認を促すなどのUI上の配慮が必要になる可能性があります。
*   **UI/UX:** プロンプト編集エリアのデザイン、再生成中のステータス表示方法などを検討する必要があります。


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

### [[DOCUMENT].envファイルの不可視問題 (Mac Finder)](https://github.com/digitaldemocracy2030/kouchou-ai/issues/291)

**作成者:** nishio  
**作成日:** 2025-04-13T00:51:49Z  
**内容:**

# 現在の問題点
MacのFinderでは .env ファイルがデフォルトで非表示のため、cp example.env .env を実行した後、ファイルを見つけられないユーザーがいる。

「.env見つからない」
「Sampleからコピーしてきたとき、それをVScodeで開こうとするときに見つからない」
「隠しファイルをfinderで開こうとしていた」


# 提案内容

READMEで、FinderではなくVSCodeなどのエディタでプロジェクトフォルダを開いて .env ファイルを編集することを推奨する。「実はFinder経由でどうこうするよりVSCodeでフォルダを開いてしまうほうが良かった」


**コメント:** なし

---

### [[FEATURE]階層図のUI/UX改善](https://github.com/digitaldemocracy2030/kouchou-ai/issues/290)

**作成者:** nishio  
**作成日:** 2025-04-13T00:49:58Z  
**内容:**

# 背景
階層図の操作性や情報表示に改善の余地がある (クリック操作の分かりにくさ、表示リセット、親子関係不明瞭、命名規則、戻るボタン欠如)。

from 4/12 meetup
>「階層図のギミックを確認、初見でクリックによって深層に移動できることがわからなかった。」
「全体図、濃い意見グループ、階層図を行き来するときに階層図の表示がリセットされなくなるとうれしい。」
「濃い意見グループで上がってきているクラスタが第一階層？のクラスタのどれに属すのかがわかるとうれしい。」
「階層図の第一階層？第二階層の名前が決まっていると嬉しい。」
「「１階層前に戻る」ボタンがあると助かります」

# 提案内容
(解決策) クリック操作のガイド表示、表示状態の保持、親子関係の明示（例: パンくずリスト）、階層命名規則の明確化、戻るボタンの追加など、UIを改善する。


**コメント:** なし

---

### [[FEATURE]exe形式での配布によるインストール簡略化](https://github.com/digitaldemocracy2030/kouchou-ai/issues/289)

**作成者:** nishio  
**作成日:** 2025-04-13T00:24:58Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
現状の広聴AIはDockerとGitの知識・インストールが前提となっており、特にITスキルやセキュリティ制限のある自治体ユーザーにとっては導入のハードルが高い。

>「Dockerのインストールが認められてない（情シス部門の理解が必要）」「自治体関係者の中でのアーリーアダプターたちが試す際に、最初の①リポジトリをクローン」段階で既にかなり大きなハードルになっている。」

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

(解決策案) アプリケーションを単一の実行ファイル（.exe形式）にパッケージ化し、DockerやGitのインストール、コマンドライン操作を不要にすることを検討する。

>「exe化は難しいだろうか？(たねのぶ)」。

これにより、ダブルクリック等で簡単に起動でき、非エンジニアやセキュリティ制限のある環境でも利用しやすくなる可能性がある。ただし、技術的な実現可能性や配布ファイルサイズなどの課題も考慮する必要がある。


(nishioコメント) DockerやGitを「インストールできるが難しい」のケースには有効かも。「Dockerのインストールが認められてない」の場合、広聴AI.exeが作られたところでそれのインストールが認められないのではという気がする。

**コメント:** なし

---

### [[FEATURE]zipでのリリース](https://github.com/digitaldemocracy2030/kouchou-ai/issues/288)

**作成者:** nishio  
**作成日:** 2025-04-13T00:14:59Z  
**内容:**

# 背景
Docker/Gitのインストール障壁 (特に自治体ユーザー)
セキュリティポリシーやITスキル不足により、DockerやGitのインストール自体が大きなハードルとなっている。
「リポジトリ」などのIT専門用語が、非エンジニアのユーザーにとって理解しにくい。

>「自治体関係者の中でのアーリーアダプターたちが試す際に、最初の①リポジトリをクローン」段階で既にかなり大きなハードルになっている。」
「Dockerのインストール、Gitのインストールという部分で既にわけがわからなくなっている。」
>「リポジトリ」概念を避けて行政に納品する際は、zip圧縮などをしたりします。
> 「非エンジニアユーザー向けに、GitをインストールせずにZIPダウンロードで運用のほうがよい？(たねのぶ)」

# 解決策

zipでリリースすればgit cloneの部分の解説は必要なくなる


**コメント:** なし

---

### [[DOCUMENT]Windows向けのセットアップ手順](https://github.com/digitaldemocracy2030/kouchou-ai/issues/287)

**作成者:** nishio  
**作成日:** 2025-04-13T00:02:52Z  
**内容:**

# 現在の問題点
<!-- 現在のコードの何が問題なのか、どのような技術的負債があるかを説明してください -->

## 課題

現在の `README.md` は主にUNIX系（Linux, macOS）環境を前提としており、Windowsユーザーが広聴AIをセットアップする際に特有の課題に直面することが多いです。

*   **必須ツールのインストールと設定:** Docker DesktopやGit for Windowsのインストール、特に環境変数Pathの設定 (`'git' は、内部コマンドまたは外部コマンド...`) やWSL連携で躓く可能性がある。
*   **改行コードの問題:** クローン時に適切に対応しないと、シェルスクリプト (`entrypoint.sh`) 実行時にエラーが発生する。
*   **コマンドの違い:** `cp` コマンドなど、コマンドプロンプトとPowerShellでの違いに戸惑う可能性がある。
*   **隠しファイル:** `.env` ファイルがデフォルトで非表示のため、作成・編集時に混乱が生じやすい。
*   **Docker関連のエラー:** `npm ci` エラー、ポート競合 (`port is already allocated`)、証明書エラーなど、Windows環境固有または頻出する可能性のあるエラーへの対処法が不明確。

これらの問題により、特に非エンジニアやITスキルに不安のあるWindowsユーザーにとって、導入のハードルが高くなっています。「WindowsユーザーはDocker Desktopのダウンロードからはじまる」「GithubのREADMEは現在UNIX系前提?」「'git' は、内部コマンドまたは外部コマンド...」「パスを通すという困難な作業」「entrypoint.shの5行目でエラー。改行コードの関係」「.env見つからない」「Powershellでないとないかも。cmdではない」

## 提案

Windowsユーザー向けの専用セットアップガイドを `README.md` に追記、または別ドキュメントとして作成する。

**含めるべき内容:**

1.  **必要なソフトウェア:**
    *   Docker Desktop (インストール方法、wingetコマンド例、注意点: セキュリティポリシー、WSL/ログインエラー)
    *   Git for Windows (インストール方法、wingetコマンド例、**Path設定の重要性**、確認方法)
    *   (推奨) テキストエディタ (VSCodeなど)
2.  **セットアップ手順:**
    *   リポジトリのクローン (**`--config core.autocrlf=false`** オプションの明記)
    *   `.env` ファイルの作成 (Windowsコマンド: `copy` / `cp`、**隠しファイル問題**とVSCodeでの編集推奨)
    *   アプリケーションの起動 (**`docker compose up`** コマンドの明記、初回ビルド時間について)
3.  **よくある問題と対処法 (Windows向け):**
    *   `git` コマンドが見つからない → Path設定の確認
    *   `entrypoint.sh` エラー → 改行コード問題の確認と再クローン
    *   `npm ci` エラー → (現状考えられる原因や再試行)
    *   証明書エラー → セキュリティソフトの確認
    *   ポート競合エラー → 他コンテナ停止 or ポート変更
    *   `.env` ファイルが見つからない → 隠しファイル設定 or VSCode利用
    *   コマンドの違い (`cp` vs `copy`)
4.  **トラブルシューティングTips:**
    *   エラーメッセージをLLMに質問するなどの自助努力の方法提示

これにより、Windowsユーザーがスムーズにセットアップを完了できるよう支援し、利用者の裾野を広げることを目指します。

# 仮原稿
## はじめに
このドキュメントは、Windows環境で広聴AIのセットアップを行うユーザー向けの手順と注意点をまとめたものです。現在の公式READMEは主にUNIX系（Linux, macOS）環境を前提としているため、Windows特有の考慮事項があります。

## 必要なソフトウェア
セットアップには以下のソフトウェアが必要です。事前にインストールしてください。

1.  **Docker Desktop:**
    *   公式サイトからダウンロードしてインストールします。
    *   `winget install -e --id Docker.DockerDesktop` コマンドでもインストール可能です。
    *   インストール後、Docker Desktopを起動し、必要な初期設定（WSL連携など）を完了させてください。
    *   **注意:** 自治体PCなどでは、セキュリティポリシーによりインストールが許可されていない場合があります。情報システム部門にご確認ください。
    *   **注意:** Googleアカウントでのログイン時やWSLアップデート時にエラーが発生することが報告されています。エラーメッセージに従って対処するか、IT管理者に相談してください。「Docker、Googleアカウントにてログイン時にエラー。」「wsl update failed: update failed: updating wsl: exit code: 1...」

2.  **Git for Windows:**
    *   公式サイトからインストーラーをダウンロードしてインストールします。「Git for Windows Portable」ではなく、通常のインストーラー版を使用してください。
    *   `winget install -e --id Git.Git` コマンドでもインストール可能です。
    *   **重要:** インストール中に「Adjusting your PATH environment」の項目で、「Git from the command line and also from 3rd-party software」を選択することを推奨します。これにより、コマンドプロンプトやPowerShellから `git` コマンドが利用可能になります。
    *   **パス設定確認:** インストール後、コマンドプロンプトまたはPowerShellを開き、`git --version` を実行してバージョン情報が表示されればOKです。表示されない場合（「'git' は、内部コマンドまたは外部コマンド...として認識されていません。」エラー）、環境変数のPathにGitの実行ファイルパス（例: `C:\Program Files\Git\cmd`）を手動で追加する必要があります。「パスを通すという困難な作業」 - 不明な場合はChatGPT等で「Windows 環境変数 パス 通し方」などで検索・質問してください。

3.  **(推奨) テキストエディタ:**
    *   VSCodeなどのテキストエディタがあると、設定ファイルの編集に便利です。

## セットアップ手順

1.  **リポジトリのクローン (改行コード問題対策):**
    *   コマンドプロンプトまたはPowerShellを開き、作業したいディレクトリに移動します。
    *   以下のコマンドを実行して、リポジトリをクローンします。`--config core.autocrlf=false` オプションは、WindowsとLinux/macOS間の改行コードの違いによるエラー (`entrypoint.sh` 関連など) を防ぐために重要です。
        ```bash
        git clone --config core.autocrlf=false https://github.com/digitaldemocracy2030/kouchou-ai.git
        ```
    *   クローンした `kouchou-ai` ディレクトリに移動します。
        ```bash
        cd kouchou-ai
        ```

2.  **環境設定ファイルの作成:**
    *   `example.env` ファイルをコピーして `.env` ファイルを作成します。PowerShellでは以下のコマンドで実行できます。
        ```powershell
        cp example.env .env
        ```
        (コマンドプロンプトの場合は `copy example.env .env`)
    *   **注意:** `.env` は隠しファイル属性が付くことがあります。Windowsのエクスプローラーで表示されない場合は、「表示」タブ -> 「隠しファイル」にチェックを入れるか、VSCodeなどのエディタで `kouchou-ai` フォルダを開いて `.env` ファイルを編集してください。「.env見つからない」「隠しファイルをfinderで開こうとしていた」
    *   `.env` ファイルを開き、OpenAI APIキーなどの必要な設定値を記述します。

3.  **アプリケーションの起動:**
    *   Docker Desktopが起動していることを確認します。
    *   `kouchou-ai` ディレクトリ内で、以下のコマンドを実行します。**ハイフンなしの `docker compose up` を使用してください。**
        ```bash
        docker compose up
        ```
    *   初回起動時は、Dockerイメージのダウンロードとビルドに時間がかかります（数分～十数分程度）。「Docker imageがない状態でdocker compose upすると500s以上かかる」
    *   ビルドと起動が正常に完了すると、ログの最後に `Application startup complete.` のようなメッセージが表示され、Webブラウザで `http://localhost:3000` (Admin Dashboard) と `http://localhost:5173` (レポート画面) にアクセスできるようになります。

## よくある問題と対処法

*   **`git` コマンドが見つからない:**
    *   Git for Windowsのインストール時にパス設定が適切に行われなかった可能性があります。上記「必要なソフトウェア」のGitの項目を確認し、環境変数Pathを修正してください。
*   **`entrypoint.sh` 関連のエラー:**
    *   改行コードの問題である可能性が高いです。上記「リポジトリのクローン」の手順に従い、`--config core.autocrlf=false` オプション付きでクローンし直してください。
*   **`docker compose up` 中の `npm ci` エラー:**
    *   `[client-admin builder ... ] RUN npm ci` でエラーが発生する場合があります。(ログ参照) 根本的な解決策はログに記載されていませんが、ネットワーク環境やDockerのリソース割り当てなどが影響している可能性があります。時間をおいて再試行するか、Docker Desktopの設定を見直してください。
*   **`docker compose up` 中の証明書エラー (`uv` など):**
    *   会社のセキュリティソフトなどがDocker内の通信をブロックしている可能性があります。「自治体のセキュリティによってuvのインストール時に証明書エラーがおきた」一時的にセキュリティソフトを無効にするか、Docker関連の通信を許可する設定を行ってください。
*   **`Bind for 0.0.0.0:3000 failed: port is already allocated` エラー:**
    *   ポート3000が他のアプリケーション（他のDockerコンテナ等）によって既に使用されています。「原因：3000ポートをすでに使っているdocker containerが立ち上がっていた」他のアプリケーションを停止するか、`.env` ファイルで `APP_PORT` を別の番号（例: `3001`）に変更してください。
*   **`.env` ファイルが見つからない/編集できない:**
    *   隠しファイルになっている可能性があります。上記「環境設定ファイルの作成」の注意点を確認してください。VSCodeでフォルダを開くのが確実です。
*   **コマンドプロンプトで `cp` コマンドが使えない:**
    *   `cp` はPowerShellのコマンドです。コマンドプロンプトでは `copy` を使用してください。もしくはPowerShellを起動して作業してください。「Powershellでないとないかも。cmdではない」

## トラブルシューティングTips
*   エラーが発生した場合、表示されたエラーメッセージ全体をコピーし、ChatGPTなどのLLMに貼り付けて「このエラーの原因と解決策を教えてください」と質問すると、具体的な解決策が見つかることがあります。「エラーが出たら内容張り付けて「エラーでた助けて」といえばほぼほぼ解決もしてくれます。」


**コメント:** なし

---

### [Windows環境でのセットアップの困難さ低減](https://github.com/digitaldemocracy2030/kouchou-ai/issues/286)

**作成者:** nishio  
**作成日:** 2025-04-12T23:58:34Z  
**内容:**

READMEがUNIX系前提であり、WindowsユーザーはDocker/Gitのインストール、パス設定、改行コード問題などで躓きやすい。

from 4/12 meetup
>「WindowsユーザーはDocker Desktopのダウンロードからはじまる」
「GithubのREADMEは現在UNIX系前提?」
「Git for Windowsのダウンロード」
「'git' は、内部コマンドまたは外部コマンド、操作可能なプログラムまたはバッチ ファイルとして認識されていません。」
「パスを通すという困難な作業」
「entrypoint.shの5行目でエラー。改行コードの関係」

(解決策)

Windows向けのセットアップ手順（Docker, Gitインストール、パス設定含む）をREADMEに詳細に追記する。

改行コード問題を回避するため、リポジトリに .gitattributes ファイルを設定する。「これは.gitattributesで解決可能？(たねのぶ)」「可能です」

クローン時に git clone --config core.autocrlf=false ... を実行するよう案内する。

**コメント:** なし

---

### [[FEATURE]利用可能なLLMを増やす](https://github.com/digitaldemocracy2030/kouchou-ai/issues/285)

**作成者:** nishio  
**作成日:** 2025-04-12T23:50:46Z  
**内容:**

# 背景
現在OpenAI APIのみ対応しており、Gemini無料枠やLocalLLMなど他の選択肢を利用できない。

from 4/12 meetup
>「Geminiの無料枠をOpen AI互換で使えたりする？」
「他LLM対応はうれしい（LocalLLMなど）」
「Local LLM(OpenAI互換)、embeddingなどで開発はケチりたい」
「idobataの方ではopenrouterが使われているのに対して、kouchouではopenaiが使われているのが不便に思った。統一してくれるとありがたいと思う。」


<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
>Gemini API、OpenRouter API、OpenAI互換のLocalLLMなど、複数のLLMに対応する。

(nishioコメント) OpenRouter APIには追加で対応してもいいかもしれない、ただし「統一」はありえない(OpenRouterを使えないユーザを締め出すことになるから)

**コメント:** なし

---

### [[FEATURE]かかったコストの表示機能](https://github.com/digitaldemocracy2030/kouchou-ai/issues/284)

**作成者:** nishio  
**作成日:** 2025-04-12T23:42:45Z  
**内容:**

# 背景
実行ごとのトークン数やコストが表示されず、利用者がコスト感を把握しにくい。

from 4/12 meetup
>「clineのように実行のたびにトークン、コストが表示されるUIは確かによい(たねのぶ)」
>「使用者にコスト感覚がついていく」


# 提案内容
(解決策) UIに実行ごとのトークン数と推定コストを表示する機能を追加する。

(nishio補足) 実行前に推定費用を表示する案は過去にあった、これは実行後に実際にかかった費用を表示するところが新しい
 - https://github.com/digitaldemocracy2030/kouchou-ai/issues/79

**コメント:** なし

---

### [[BUG]ScatterChartの全画面表示で要約文が「全画面終了」ボタンの後ろに隠れないようにする処理が不安定](https://github.com/digitaldemocracy2030/kouchou-ai/issues/283)

**作成者:** masatosasano2  
**作成日:** 2025-04-12T18:36:39Z  
**内容:**

### 概要
Issue #278 が PR #282 で修正されたが、以下の課題が残ったため本Issueに切り出された。

PR #282 の修正内容
![Image](https://github.com/user-attachments/assets/a7a1bd58-febe-4993-a49a-2612b1c90ec9)

残課題
![Image](https://github.com/user-attachments/assets/3d080c1d-1502-4b09-8aca-fb2c1fdb9e52)

### 再現手順

1. 「全体図」または「濃い意見グループ」モードを選択する
2. 「全画面表示」ボタンを押す
3. ブラウザのサイズを極力小さくする
4. 画面上部の、右端より少し左側あたりでマウスを動かし続ける

### 期待する動作

要約文が「全画面終了」ボタンの後ろに隠れない（正確には、隠れたままにならない）ようにする


**コメント:** なし

---

### [[FEATURE]属性フィルタ](https://github.com/digitaldemocracy2030/kouchou-ai/issues/281)

**作成者:** nishio  
**作成日:** 2025-04-11T14:37:35Z  
**内容:**

# 背景
from有賀さん
>年齢層・居住エリアなどで比較をみるニーズは結構ある。
>一方で、現状それをやろうとすると、集合が異なるcsvを別々に分析にかける形になり、クラスタの括りやビジュアル上の配置も異なるので比較しにくい
>全部まとめてextractionしてクラスタリング・ラベリングまでした後で、特定のフィルタをかけて件数分布や要約したり、それを比較できると理想
>そうすると、全て最初に分析されているというよりは、ダッシュボード上で追加で分析をまわす感じか。
フィルタリングごとの内容の違いの説明まで生成したい。

その機能は過去に実装済み
- https://github.com/takahiroanno2024/anno-broadlistening/issues/9
- 具体的には下記2つのPR
- server side: https://github.com/takahiroanno2024/anno-broadlistening/pull/15
- client side: https://github.com/takahiroanno2024/anno-broadlistening/pull/21

階層表示をもった広聴AIにする際に、この機能の優先度が低くて移植していないだけ

# 提案内容

サーバサイドはほぼ使えるのではないかと思う
クライアントサイドはviewがplotlyに変わっていることで同じ方法は使えなくなっていると思う
この二つをsub-issueにしてやっていくのが良さそう

**コメント:** なし

---

### [[FEATURE] テスト用のパブコメデータをCSV化する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/280)

**作成者:** ei-blue  
**作成日:** 2025-04-11T07:59:01Z  
**内容:**

コードには直接関係ないですが、TODOメモとしてイシューにしておきます。
（これはFeatureじゃなくてDocumentなんですかね？）

# 背景
- 自治体での活用を想定して、CSVモード（パブコメモード）を実装した
- 大量のデータに対してクラスタリングが適切に機能することを確認するため、実際のパブコメデータに対して実験を行いたい
- そのためのデータ整備をする必要

# 提案内容
- 最近の件数多めのパブコメとして、以下の資料に含まれる意見をCSVにする
- やり方はなんでもあり。Pythonを練習したい人にもいいかも。
環境省
[除去土壌](https://public-comment.e-gov.go.jp/servlet/Public?CLASSNAME=PCM1040&id=195240105&Mode=1)
経産省
[第７次エネルギー基本計画](https://public-comment.e-gov.go.jp/pcm/1040?CLASSNAME=PCM1040&id=620224019&Mode=1)
内閣府
[「「新型インフルエンザ等対策政府行動計画」（案）](https://public-comment.e-gov.go.jp/servlet/Public?CLASSNAME=PCM1040&id=060512703&Mode=1)

**コメント:** なし

---

### [[BUG] 静的ファイルがGithub Pagesでうまく表示されない件](https://github.com/digitaldemocracy2030/kouchou-ai/issues/274)

**作成者:** keisuke-a  
**作成日:** 2025-04-10T06:52:19Z  
**内容:**

### 概要

静的ファイルをoutして、その中身をgithub pagesで公開すると、out/index.html自体は表示はされるが、画像要素がなかったりリンク先（個別ページ）が404になるなど、うまく表示されない。（参照が絶対パスになってることによる？）


**コメント:** なし

---

### [[DOCUMENT] 静的ファイルのホスティング手順のドキュメント化](https://github.com/digitaldemocracy2030/kouchou-ai/issues/271)

**作成者:** nasuka  
**作成日:** 2025-04-09T13:48:25Z  
**内容:**

# 現在の問題点
* static exportで出力したhtmlファイルを、ユーザー（出力者）がどのようにホスティングすべきかわからないことがある
  * ホスティングには一定のソフトウェアエンジニアリングの知識が必要

# 提案内容
ホスティング方法に関するマニュアルを記載する
ホスティングするサービスの候補としては以下がありそう？

* Github Pages
  * issue起票済み
    * https://github.com/digitaldemocracy2030/kouchou-ai/issues/235
  * 無料で利用可能  
  * 認証がかけられないのがネックになる可能性がある
* Netlify
  * 認証をかけられる & 設定も比較的容易なので、Netlifyを採用できる組織・ユーザーであれば、機能としては恐らくこちらが要件に適しているケースは多そう
  * ただし、そもそも利用者側でNetlifyを契約できない可能性がある
* AWS/Azure
  * 元々これらのクラウドサービスを契約しているのであれば、利用者側での導入は最も容易だと思われるが、設定としてはGithub Pages/Netlifyよりも複雑になりそう


AWS/Azureでのニーズがどの程度あるのか見えていないので、一旦Github Pages/Netlifyあたりの手順をまとめられると良さそう？

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(18件)

### [[FEATURE]クラスタ数が増えた場合に散布図上でクラスタラベルが被ってしまう](https://github.com/digitaldemocracy2030/kouchou-ai/issues/266)

**作成者:** nasuka  
**作成日:** 2025-04-08T14:20:10Z  
**内容:**

# 背景
* クラスタ数が増えた場合に散布図上でクラスタラベルが被ってしまう
  * 添付画像は40件で出力したケース。多くのクラスタラベルが被ってしまっている。
![Image](https://github.com/user-attachments/assets/c8e61e43-ef60-4054-91d0-4b8f3e6f4847)

* この問題により、現在は第一階層のクラスタ数を大きな数値に設定できない
  * 現在は上限を20としているが、TTTCの過去事例では30件を表示していたケースもあるため、上限をもう少し大きくしたい

# 提案内容
解決するアプローチは幾つかありそう。

## 対策方針（Claudeによる案）
1. ラベル表示の選択的制限

- 重要度ベースの選択：クラスタサイズなどに基づき重要なラベルのみ表示
- 最大表示数の制限：表示するラベル数に上限を設定（例: 最大15個）
- ユーザー選択型表示：選択されたクラスタのみラベル表示

2. ラベルの視覚的最適化

- フォントサイズの縮小：ラベルのフォントサイズを小さくして占有面積を減らす
- 可変フォントサイズ：クラスタの重要度に応じてフォントサイズを調整
- ラベル省略表示：長いラベルを省略形で表示（例: "長いラベル名" → "長いラ..."）

3. インタラクティブ手法

- 凡例コンポーネントの追加：画面端に凡例を設け、クラスタ一覧を表示
- ホバー/クリック表示：マウスホバーやクリック時のみラベルを表示
- ハイライト機能：選択クラスタを強調し他を半透明化

4. レイアウト最適化

- ラベル位置の調整：ラベル同士の衝突を検出し位置を最適化
- クラスタのグルーピング：近接するクラスタを階層的に表示

**コメント:** なし

---

### [[REFACTOR] GitHub Actions で Biome の lint, format のチェックを実行する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/264)

**作成者:** shgtkshruch  
**作成日:** 2025-04-08T12:47:44Z  
**内容:**

# 現在の問題点
<!-- 現在のコードの何が問題なのか、どのような技術的負債があるかを説明してください -->

- #84 で Biome を導入しましたが、format, lint エラーがあるコードがプルリクエストに含まれていても気づく仕組みが現状では整っていません
- Biome の lint, format を適用しないコードが取り込まれると、コード全体の統一性が落ちるのと、Biome を適用した他のプルリクエストでコードの差分が出る可能性があります
  - 本来のプルリクエストとは関係のない差分が出ることで、レビューの負荷が上がりそう

# 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->

- client, client admin のコードの修正を含むプルリクエストを作成したら、CI で Biome の format, lint のチェックを実行する
  - [公式で提供している GitHub Actions と `biome ci`](https://biomejs.dev/recipes/continuous-integration/) コマンドが利用できるかもしれません

**コメント:** なし

---

### [(情報整理)OpenAIが使えないケースのケア](https://github.com/digitaldemocracy2030/kouchou-ai/issues/255)

**作成者:** nishio  
**作成日:** 2025-04-08T03:21:10Z  
**内容:**

# 背景

政党に売り込む上で「ChatGPTの政治利用NG」が障害になる可能性がある？→あるのでケアが必要

解決案
 - A: そもそもAzure OpenAI ServiceならOKなのでは説(=対処完了済み)
 - B: Geminiを叩けるように変える
   - B-1: 直接Geminiを叩く分岐を環境変数でやる
   - B-2: OpenRouter経由にすることでOpenAI API形式でGeminiを叩けるようにする
   - B-3: [LiteLLM Proxy](https://scrapbox.io/nishio/LiteLLM_Proxy) でやるマニュアルを作る


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

**コメント:** なし

---

### [(情報整理)Windows環境で試す人のためのガイドが必要](https://github.com/digitaldemocracy2030/kouchou-ai/issues/254)

**作成者:** nishio  
**作成日:** 2025-04-08T03:14:53Z  
**内容:**

Windows環境で試す人の踏みそうなトラブルシューティング

西尾も角野さんもMacなのでどんなトラブルが起きるのかを観測できてない感、issueでもslackでもガンガン書いてもらえるといいと思う

Windows環境で試すとなった時に、まずいきなり「生環境でやる」「WSLでやる」「Dockerでやる」の3つの選択肢があると思ってて、どれが一番スムーズなのかはよくわかってない、Windows環境のある人の協力があるとありがたいゾーン

関連Slack: https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1744081553571589

**コメント:** なし

---

### [[FEATURE]静的HTML出力してローカルファイルシステムで開いたときに詳細なエラー表示をする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/253)

**作成者:** nishio  
**作成日:** 2025-04-08T03:13:48Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

Q: 静的HTML出力してローカルファイルシステムで開いたとき読み込み中のまま進まない、バグ？
A: →ブラウザがデータをローカルファイルシステムから読めないことに起因する、GitHubPagesなどにデプロイしちゃえば動くと思う、手元でサーバを立てるてもある、解説があるとベター

関連Slack: https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1744080063900439

# 提案内容

この件は読み込み中のバーが回りっぱなしになるが裏では即座にエラーになってるはずで、エラーメッセージを出して解決策解説ページへのリンクを示すのが親切だと思う



**コメント:** なし

---

### [[DOCUMENT] README に GitHub Pages で公開する手順を記載する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/235)

**作成者:** shgtkshruch  
**作成日:** 2025-04-05T07:07:57Z  
**内容:**

# 現在の問題点
<!-- 現在のコードの何が問題なのか、どのような技術的負債があるかを説明してください -->

- client を static build して GitHub Pages で公開する場合、ビルドしたファイルをアップロードすると一部のコードが動かない
  - 原因: GitHub Pages で動いている Jekyll が `_` から始まるファイルやディレクトリを無視するため、static build 後の `_next` 以下のファイルが 404 になる
    - https://github.blog/news-insights/the-library/bypassing-jekyll-on-github-pages/
  - `.nojekyll` というファイルをルートに置くと動くようになるが、この挙動は知らない人が多そうで GitHub Pages で公開する人が同じ罠にハマる可能性がある

# 提案内容
<!-- どのようなリファクタリングを提案するのか、具体的に説明してください -->

- README の静的ファイル出力のセクションに、GitHub Pages で公開する場合の手順を記載する
  - ルートに `.nojekyll` ファイルを追加することもここに記載する

**コメント:** なし

---

### [[FEATURE]濃い意見グループの設定画面について](https://github.com/digitaldemocracy2030/kouchou-ai/issues/227)

**作成者:** nishio  
**作成日:** 2025-04-03T13:37:38Z  
**内容:**

# 背景

![Image](https://github.com/user-attachments/assets/bb76f174-3347-4e73-aeed-823e8f4272d1)
最小クラスタは2以上。上が10でいいかは少し微妙で、2,5,10,25,50,100くらいの選択式がいいかもという気持ち
閉じるボタンが文章に被んている件、見出しと説明が横並びなのを縦並びにすると良いかも
「濃いグループの設定しかないので中に入れたらどうか」という話が以前悪化が、この設定によって濃いグループを選択できるかどうかが変わるのでそとにあるべき、将来的にはカラーバレットの設定などもここにはいるのかなと思う

<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->


# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

**コメント:** なし

---

### [[BUG] ２回目以降、静的ファイル出力（static build）時 パーミッションエラーが発生する？](https://github.com/digitaldemocracy2030/kouchou-ai/issues/225)

**作成者:** naoyo4  
**作成日:** 2025-04-03T00:12:34Z  
**内容:**

### 概要

<!-- バグの簡潔な説明をお願いします -->
静的ファイル出力（static build） を行う際、最初は問題なく出力ディレクトリーが作成されるが、再度実行するとパーミッションエラーが発生する？

### 再現手順

1. README の手順に則り（ make client-build-static ）、静的ファイル生成（ out ディレクトリ出力 ）
2. 再度同じことを行うとMakefile手順の最初（ rm -rf out ）でパーミッションエラーが発生
3. （ Webサーバーにも、FTP でUP時、パーミッションエラーが発生 ）

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->
２回目以降もパーミッションエラーが発生せず、処理できる。
（ WebサーバーにFTPでUPできる ）

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->
(base) nao@d500:~/kouchou-ai$ make client-build-static
rm -rf out
rm: 'out/images/broadlistening.png' を削除できません: 許可がありません
rm: 'out/404.html' を削除できません: 許可がありません
rm: 'out/_next/static/chunks/polyfills-42372ed130431b0a.js' を削除できません: 許可がありません
：
：

### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->
Issue 上げること自体ほぼ初めてで、内容自体も自信ありませんが、アドバイスだけでもいただければ幸いです。
http-server による動作等は、問題ないことは確認済み。

**コメント:** なし

---

### [[FEATURE] frontからstaticなHTMLファイルをexportしてDownloadできるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/220)

**作成者:** takahiroanno  
**作成日:** 2025-04-02T11:43:27Z  
**内容:**

# 背景
* static exportが実装されたが、現在はCLIで実行することしかできず、Webアプリ上で実行できない
  * `make client-build-static` を実行するとCLIではstatic exportができる
  * 参考
    * https://github.com/digitaldemocracy2030/kouchou-ai/pull/198
    * https://github.com/digitaldemocracy2030/kouchou-ai/pull/195


# 提案内容
* adminの一覧画面で、static exportを実行できるようにする

**コメント:** なし

---

### [[FEATURE]OOMの事後処理](https://github.com/digitaldemocracy2030/kouchou-ai/issues/211)

**作成者:** nishio  
**作成日:** 2025-04-01T06:00:12Z  
**内容:**

# 背景
エラー時にはレポート一覧にその旨が出るが、Out of Memoryで死んだ場合にはエラー内容を書き込む前に死ぬので「処理中」の表示が続いてしまう


# 提案内容
良い解決方法を考えたい

案
- pidをstatusにもつ
-  レポート一覧APIが呼ばれた時に、未完了のレポートについてプロセスが生きてるか確認して、死んでるならstatusをエラーに変える


**コメント:** なし

---

### [[FEATURE]1回のextractionで複数のcommentを処理する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/190)

**作成者:** nasuka  
**作成日:** 2025-03-28T02:12:39Z  
**内容:**

# 背景
* 現在のextraction処理は1リクエストに1件のコメントを処理しているため、実行に時間がかかる
  * リクエストそのものの並列化は行われているが、OpenAI APIのrate limitの関係で並列化による高速化も限界がある


# 提案内容
* 1回のextractionで複数のコメントを同時に処理する
  * 同時処理の件数が増えることで、rate limit(requests per minute)の問題が緩和される

プロンプトのイメージ
```
あなたは専門的なリサーチアシスタントで、整理された議論のデータセットを作成するお手伝いをする役割です。
人工知能に関する公開協議を実施した状況を想定しています。一般市民から寄せられた議論の例を提示しますので、それらをより簡潔で読みやすい形に整理するお手伝いをお願いします。必要な場合は2つの別個の議論に分割することもできますが、多くの場合は1つの議論にまとめる方が望ましいでしょう。
結果は出力例に記載したjson形式で出力して

## 入力例
- id1: AIは仕事の効率化に役立つ。人生の相談相手にもなってくれる。
- id2: AIは電力を消費しすぎる問題がある
- id3: AIには反対です

## 出力例
{
    "id1": [
        "AIは仕事の効率化に役立つ",
        "AIは人生の相談相手になる"
    ],
    "id2": [
        "AIは電力消費が大きい"
    ],
    "id3": [
        "AIには反対"
    ]
}
```

extraction実行時のLLMのresponse formatが変わるため、周辺の実装も変える必要がある。

## 進め方
* まずは、上記のようなプロンプト・出力フォーマットに変更して同時処理数を増やした場合にどのようにアウトプットの文言が変わるかを確認する
  * 入力データは、ツイートレベルの長さのケースと、aipubcomのように1コメントが長いケースの両方で確かめた方が良さそう
* 抽出結果が問題なさそうであればプロダクトに機能実装する


**コメント:** なし

---

### [[FEATURE]ファクトチェック機能の実装](https://github.com/digitaldemocracy2030/kouchou-ai/issues/170)

**作成者:** nasuka  
**作成日:** 2025-03-25T06:18:39Z  
**内容:**

# 背景
* 入力ファイル内のコメントが虚偽の場合がある
  * e.g. 「◯◯という人物が✗✗という発言をしていたが大変嘆かわしい」というコメントがあったとして、現状ではこのコメントの真偽に関わらずコメントが分析結果に組み込まれてしまう

# 提案内容
* 個別のコメント（or 意見）についてファクトチェックを行う
* クラスタリングやクラスタ説明文の生成時にファクトチェックの結果を組み込み
  * 組み込む方法はいくつかパターンがありそう
    * 1. 虚偽と判定されたargumentはクラスタ生成以降のプロセスで除外する
    * 2. クラスタタイトルや説明文生成時に、argumentのテキストだけでなくファクトチェックの結果（真偽）も入力して生成を行う
    * 3. 散布図上でargumentをホバー表示する際に、虚偽の疑いがあるargumentはそのことが分かるように表示を変える
  * ↑は一例だが、実現方針の具体化からassigneeの方にやっていただけるとありがたい

# 進め方
* いきなり機能を実装するのではなく、プロダクトとは独立してスクリプトを実装し、検証用のデータセットを使って結果の妥当性を評価する
  * 問題なければプロダクトの機能として実装を進める
  * 一旦実験系のIssueだけ立てておき、実験結果より自動評価が機能することがわかった段階でプロダクトへの実装イシューを立てる



**コメント:** なし

---

### [[FEATURE]LLMによるクラスタ品質の自動評価（実験）](https://github.com/digitaldemocracy2030/kouchou-ai/issues/144)

**作成者:** nasuka  
**作成日:** 2025-03-25T03:36:54Z  
**内容:**

# 背景
https://github.com/digitaldemocracy2030/kouchou-ai/issues/143

* こちらのイシューは上記のサブイシュー


# 提案内容
* LLMによるクラスタ品質の自動評価の実験を行う
  * 出力されたクラスタタイトル・説明文・所属データ点の情報に基づいて、LLMでクラスタの品質を評価する
* どのようなアプローチで評価するかは、assigneeの方におまかせする
  * 例としては、例えば以下のような評価項目のスコアをLLMで出力するようなアプローチがある
    * クラスタ内部の一貫性評価
      * クラスタタイトル・説明文・所属データのテキストを入力し、一貫性を100点満点でスコアリングする
    * クラスタ外部との分離度の評価
      * クラスタAの情報（タイトルや所属データ等）と、重心の距離が最もAに近いクラスタBの情報をLLMに入力し、分離度を出力する


**コメント:** なし

---

### [[REFACTOR] 濃いクラスタのアイコン変更](https://github.com/digitaldemocracy2030/kouchou-ai/issues/113)

**作成者:** nishio  
**作成日:** 2025-03-20T12:20:30Z  
**内容:**

# 現在の問題点

<img width="249" alt="Image" src="https://github.com/user-attachments/assets/bc626d04-e7c0-4245-9b01-e762d433a434" />

濃いクラスタのアイコンは特に意味はなくこれになっている


# 提案内容

多分叩き台の案がないとどう変えたらいいかの議論もできないと思うので雑に描いておく

![Image](https://github.com/user-attachments/assets/9e46dfd6-71d4-4c2b-bbd5-1c79220c8d80)

アイコンとしてデザインできるかは度外視して描くとこんな感じで「全体像」は全体にたくさんの点が散らばっており、「濃いクラスタ」はぎゅっとした「濃い」「密度の高い」塊がいくつかある感じ

**コメント:** なし

---

### [[FEATURE]CSVアップロード時にそれを処理した場合のコストを表示](https://github.com/digitaldemocracy2030/kouchou-ai/issues/79)

**作成者:** nishio  
**作成日:** 2025-03-18T03:19:29Z  
**内容:**

# 背景

>安野貴博: ファイルアップロードすると解析掛ける前にコストを教えてくれるの良さそうですね
>ほづみゆうき: ついにレポート出力まで漕ぎ着けたのですがAPI料金がどれくらいになるのかまったく感覚的に分からずドキドキだったので素人にはあると嬉しいと思います！

# 提案内容

これを実現するためには2つの要素が必要

- 1: done( ~~いまCSVアップロード即処理開始になっているが、一旦確認ダイアログを挟む必要がある~~ )
- 2: どのくらいのデータだとどれくらいの費用になるのかの見積もり関数が必要

## (2)の真面目な作り方

(1)は @nanocloudx さんが詳しいと思うが、(2)の部分がわからなくて着手できないと思う。
UI改善に着手する前に、この関数を作るためのデータ自体を集めていないのでそこからやる必要がある。

- a: extraction
- b: embedding
- c: その後のレポート作成

(a)がO(N)でgpt4oなので大きく、(b)はO(N)だがembedding modelなので安く、cはクラスタ数のオーダー(階層モデルなど今回いろいろ追加したから読めない)という感じで、このそれぞれに分けて料金を出せるようにしてデータ量違いでデータを集めればよい。

## (2)の雑な作り方

ユーザのペインは「すごい高額だったらどうしよう」だと思うので、まず「100円未満っすね」「100~1000円くらい」「これはでかいから1000円以上かかるよ」の3段階でいいのでは説

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

### [[FEATURE] チャート表示に連動した文章表示](https://github.com/digitaldemocracy2030/kouchou-ai/issues/52)

**作成者:** nanocloudx  
**作成日:** 2025-03-16T03:43:03Z  
**内容:**

# 背景
レポートはチャートとクラスター文章から成っている
現在はチャート表示を切り替えたりしても、クラスター文章は初期表示のままである

# 提案内容
表示範囲の更新に合わせて、チャート下部にあるクラスター内容文章(cluster.takeaway)も更新する

**コメント:** なし

---

### [[FEATURE]レポートの複製・再利用機能](https://github.com/digitaldemocracy2030/kouchou-ai/issues/19)

**作成者:** nasuka  
**作成日:** 2025-03-04T11:38:39Z  
**内容:**

# 背景
* 設定を少しだけ変えて実行したいケースがある
  * 例えばクラスタ数だけ変えるなど


# 提案内容
* レポートの設定複製機能を実装する


# 機能の提供価値
* LLM APIコストの削減
  * レポート出力までのステップを途中から実行できるようになるためAPIのコストを削減できる
* レポート出力の高速化

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (16件)

### [改行コード混在の解消のため .gitattributes を追加（#243 対応）](https://github.com/digitaldemocracy2030/kouchou-ai/pull/314)

**作成者:** take365  
**作成日:** 2025-04-16T03:07:22Z  
**変更:** +2 -0 (1ファイル)  
**マージ日:** 2025-04-16T04:17:35Z  
**内容:**

# 変更の概要

- `.gitattributes` を追加し、改行コード（LF / CRLF）をファイル種別ごとに明示的に制御するようにしました。

# 変更の背景

- Windows環境での利用時、Git の自動変換（`core.autocrlf`）やエディタの設定により `.sh` ファイルが CRLF になってしまい、
  POSIXシェルで構文エラー（"unexpected 'fi' (expecting 'then')"）が発生するケースがありました。
- これは entrypoint.sh の構文の問題ではなく、改行コードが Windows形式（CRLF）で保存されたことが原因です。
- `.gitattributes` によって `*.sh` は LF、`*.bat` や `*.cmd` は CRLF に固定することで、OS間の不整合を防ぎます。

# 関連Issue

- https://github.com/digitaldemocracy2030/kouchou-ai/issues/243
- https://github.com/digitaldemocracy2030/kouchou-ai/issues/286
# CLAへの同意

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Windowsユーザの利用環境構築 #300　の調整](https://github.com/digitaldemocracy2030/kouchou-ai/pull/313)

**作成者:** take365  
**作成日:** 2025-04-16T02:49:17Z  
**変更:** +50 -20 (4ファイル)  
**マージ日:** 2025-04-16T04:17:06Z  
**内容:**

# 変更の概要
setup_win.bat の文言を英語化し、Docker起動時の挙動を --build に変更
起動・停止用の補助バッチファイル（start_win.bat, stop_win.bat）を追加
運用手順を含めたガイド（windows-setup.md）を追記

# 変更の背景
リンクが切れている部分があった(sample.envとずれていた）
日本語の影響で処理が異常になった。かといってSJISにするとwebで化ける
docker compose up -d では.env の変更が反映されないことがあるため、初回実行時から --build を使うように変更
コマンド操作が苦手な非エンジニアの利用者向けに、クリックだけで起動・停止できるバッチファイルを用意
その利用手順を windows-setup.md に明記し、運用しやすい形にしました

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/300


- [x ] CLAの内容を読み、同意しました

**コメント:** なし

---

### [濃いクラスタ抽出で対象となるクラスタがない時にはボタンをdisabledにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/312)

**作成者:** nishio  
**作成日:** 2025-04-15T09:31:15Z  
**変更:** +103 -26 (3ファイル)  
**マージ日:** 2025-04-15T09:51:35Z  
**内容:**

# 変更の背景+概要

https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1743685246693499
>少ないデータに「濃い意見グループ」分析をかけた時に何が起こるか
>- getDenseClusters関数が末端グループを対象に濃度でのフィルタリングをする。この時「最小クラスタサイズ」の制約があるのでみんな小さすぎる時はフィルター結果が空になる。このフィルターは末端グループだけフィルターし、親グループはそのまま残す仕組みになっている。
>- フィルターされた結果を受け取ったChartコンポーネントは、チャートの種類選択が「濃い意見グループ」の時、データから一番深いグループを計算してそのレベルのグループを表示する。このとき「本来の末端グループがすべてフィルターされてる」ことで、上位のグループが表示されてしまう
>- 修正案: getDenseClustersが「フィルター結果がemptyか」のbooleanをセットで返すようにし、emptyな時には「濃い意見グループ」のボタンをdisabledにする

# 関連Issue
- #96

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [レビュアー向けのガイドラインを追記](https://github.com/digitaldemocracy2030/kouchou-ai/pull/311)

**作成者:** nasuka  
**作成日:** 2025-04-15T09:25:07Z  
**変更:** +16 -0 (2ファイル)  
**マージ日:** 2025-04-15T09:47:10Z  
**内容:**

# 変更の概要
レビュアー向けのガイドラインを追記し、DevinのPRに関する取り扱いルールを記載


# 変更の背景
DevinのPRについて、レビュアー側がどのようなアクションを起こすべきかわからず戸惑う場面があった

引用
```
DevinによるPR、作成中で裏で人間と議論してるのか、一旦終わって他人のレビューを待ってるのか区別つかないのでトリガー引いた人がコメントしてからレビューするとかなんかいい感じの運用方針が必要な気がする
```

# 関連Issue
関連するIssueのリンクをこちらに記載してください

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Update windows-setup.md](https://github.com/digitaldemocracy2030/kouchou-ai/pull/307)

**作成者:** nishio  
**作成日:** 2025-04-13T13:51:57Z  
**変更:** +5 -4 (1ファイル)  
**マージ日:** 2025-04-13T13:52:08Z  
**内容:**

軽微なドキュメントの更新

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Windows環境でのセットアップ簡素化 (Issue #300)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/301)

**作成者:** nishio  
**作成日:** 2025-04-13T04:02:24Z  
**変更:** +98 -0 (2ファイル)  
**マージ日:** 2025-04-13T10:01:59Z  
**内容:**

## 概要

このPRはIssue #300に対応し、Windows環境でのkouchou-aiのセットアップを簡素化するための実装を提供します。

## 実装内容

1. `setup_win.bat` - Windowsユーザー向けセットアップスクリプト
   - Docker Desktopの起動確認
   - OpenAI APIキーの入力プロンプト
   - 環境変数の自動設定
   - docker composeによるサービス起動

2. `docs/windows-setup.md` - Windows環境でのセットアップ手順ドキュメント
   - 前提条件の説明
   - Docker Desktopのインストール手順
   - リポジトリのダウンロード方法
   - OpenAI APIキーの取得方法
   - セットアップの実行手順
   - トラブルシューティング

## ユーザーストーリー

このPRにより、以下のユーザーストーリーが実現されます：
- Docker Desktopをインストール
- zipでrepoをダウンロード
- OpenAI APIキーを取得してくらいチャージする
- setup_win.batを実行
- ブラウザでアクセス可能になる

## この後の流れ

これをマージした後で、Windowsユーザに`docs/windows-setup.md`の手順でセットアップができるか試してもらう

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [docker-compose → docker compose](https://github.com/digitaldemocracy2030/kouchou-ai/pull/299)

**作成者:** nishio  
**作成日:** 2025-04-13T01:43:23Z  
**変更:** +3 -3 (1ファイル)  
**マージ日:** 2025-04-13T02:57:04Z  
**内容:**

# 変更の概要
- ここに変更の概要を記載してください

# 変更の背景
- ここに変更が必要となった背景を記載してください

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/298

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [fix issue #278 : 要約文が「全画面終了」ボタンの後ろに隠れないようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/282)

**作成者:** masatosasano2  
**作成日:** 2025-04-11T20:22:05Z  
**変更:** +51 -3 (3ファイル)  
**マージ日:** 2025-04-15T02:11:36Z  
**内容:**

# 変更の背景
全画面表示の「全画面終了」ボタンの後ろに要素の要約文が一部隠れてしまい、読めないことがある。

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/278

# 変更の概要
- `client/components/charts/ScatterChart.tsx` と`client/components/charts/TreemapChart.tsx` の props に `onHover` 用のfunctionを追加。 `onHover` が有効であることは以下で確認： https://github.com/plotly/react-plotly.js/blob/master/src/factory.js
- `client/components/report/Chart.tsx` に `onHover` 用のfunctionを実装。内容は「全画面終了ボタンと要約文の吹き出しが重なる場合に重ならなくなる位置まで吹き出しを下方向にずらす」。

# 動作確認結果
○
- 全画面表示でない場合は挙動が変わらない
- 要約文がボタンに隠れない場合は挙動が変わらない
- 要約文がボタンに隠れる場合は、一番右上の要素でなくとも被らなくなるまで要約文が下方向にずれる
- 下方向にずれた場合、要約文の背景が吹き出し型であれば吹き出しの先端だけ元の位置に紐づく

△
- `ScatterChart` の場合、マウス移動のたびに `onHover` と `onUnhover` が交互に発火されるのだが、 `onHover` のたびに要約文が再描画され、本修正の位置ずらしがリセットされてしまう。そのため、 `ScatterChart` ではsetTimeoutで位置ずらしを実行するタイミングを遅らせている。これにより概ね意図通り動作するようになったが、マウスの動かし具合によっては戻ってしまうこともある。ReactのイベントとしてはonMouseMoveなどほしいものが発火されていないので、これ以上精度を上げるには独自にmousemoveイベントなどを作成する必要があるが、効果の割に影響範囲調査含めて実装コストが高そうなので、Issue [#283](https://github.com/digitaldemocracy2030/kouchou-ai/issues/283) に分離する。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [エラーで落ちても進捗状況を自動更新する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/279)

**作成者:** 101ta28  
**作成日:** 2025-04-11T07:26:14Z  
**変更:** +141 -34 (2ファイル)  
**マージ日:** 2025-04-11T11:30:40Z  
**内容:**

close #277 

# 変更の概要
- server/serc/routers/admin_report.py
  - ステータスの追加・修正
-  client-admin/app/page.tsx
  - useReportProgressPollの修正
  - ReportCardの修正
  - リロードなしで画面更新するようにしました

## 添付画像

エラーが発生した場合

![error](https://github.com/user-attachments/assets/46c419b4-b8d7-4c70-b7e6-25408f0504f9)

処理が成功した場合

![success](https://github.com/user-attachments/assets/104445f1-58b3-409a-ba7a-e53d657bb4fd)

# 変更の背景
> 正常に動作するとstep1(抽出)からstep8(可視化)まで自動更新され、その後レポートのURLが表示されるが、
> エラーで落ちると進捗が更新されず、ページを再読込して初めてエラーになったことが可視化される。

# 関連Issue
#277 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [revert #258](https://github.com/digitaldemocracy2030/kouchou-ai/pull/276)

**作成者:** nishio  
**作成日:** 2025-04-10T16:07:46Z  
**変更:** +1 -1 (1ファイル)  
**マージ日:** 2025-04-10T16:08:43Z  
**内容:**

# 変更の概要
- #258 の変更により、想定外の環境でデグレが発生しているため一旦もとに戻す
- コメントはこちら: https://github.com/digitaldemocracy2030/kouchou-ai/pull/258#issuecomment-2792560274

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [[FEATURE]adminのレポート一覧画面にも作成日時を追加する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/272)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-10T02:06:40Z  
**変更:** +10 -0 (2ファイル)  
**マージ日:** 2025-04-10T02:15:53Z  
**内容:**

issue #268の対応: adminのレポート一覧画面にも作成日時を表示するよう実装しました。\n\nクライアント側と同様の実装を行い、日付はJSTタイムゾーンで表示されるようにしています。\n\nLink to Devin run: https://app.devin.ai/sessions/5f09835c41a24e2d9f91ed475d0536ff\nRequested by: nsk.smn@gmail.com

**コメント:** なし

---

### [frontend のコードを push する際に Biome の Lint を実行できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/270)

**作成者:** shgtkshruch  
**作成日:** 2025-04-09T09:53:33Z  
**変更:** +299 -47 (12ファイル)  
**マージ日:** 2025-04-10T02:02:15Z  
**内容:**

# 変更の概要
- [Lefthook](https://github.com/evilmartians/lefthook) を使って、Git Hooks の pre-push で Biome の Lint を実行できるようにしました
- CONTRIBUTING.md に client, client-admin のコードチェックに関する記載を追加しました
- 動作確認をしている際にフォーマット漏れのコードがあったので、Biome のフォーマットを適用しました

# 変更の背景
-  Lefthook はデフォルトでは off にしていて、設定ファイルを作成することで on になる設計にしています
    - 理由: 現状の Lefthook の設定は frontend のコードのみで、server 側の開発をする人にも有効にした場合に弊害が出る可能性を避けたかった
    - 最初は安全側に倒して、導入してみて良さそうであればデフォルトで on に変えても良いかもしれません
- pre-commit で毎回チェックすると少し煩雑かなと思ったので、pre-push でチェックするようにしました

# 関連Issue
- fix: #84 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [client-admin に Biome を適用](https://github.com/digitaldemocracy2030/kouchou-ai/pull/262)

**作成者:** shgtkshruch  
**作成日:** 2025-04-08T12:26:20Z  
**変更:** +1173 -4101 (32ファイル)  
**マージ日:** 2025-04-09T01:02:00Z  
**内容:**

# 変更の概要
- client-admin に Biome を適用しました

# 変更の背景
- 差分が大きいのでコミット単位でみていただけると良さそうです
  - https://github.com/digitaldemocracy2030/kouchou-ai/commit/4af790cd4bd43d37ea6ef118c9fad9b57fc33541 ESLint を削除
  - https://github.com/digitaldemocracy2030/kouchou-ai/commit/0e9e28da0793a9e2d03b6949caf5c632822e1f2b npm script に Biome のコマンドを追加
  - https://github.com/digitaldemocracy2030/kouchou-ai/commit/680a97801f1e5bef81c846ba4c3230627ce89869 Biome の format を適用（自動で修正できるもののみなので、コードの構造は変わっていない認識です）
  - https://github.com/digitaldemocracy2030/kouchou-ai/commit/d6bd0b4da71079b7437ad0f1082263f66a7bcc4c 自動で直せない format, lint エラーを修正（ここは手動で対応したので見てもらいたいところです）

# 関連Issue
- #84 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [[FEATURE] GoogleAnalytics 対応 #54](https://github.com/digitaldemocracy2030/kouchou-ai/pull/251)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-08T02:32:53Z  
**変更:** +1012 -0 (12ファイル)  
**マージ日:** 2025-04-09T07:56:31Z  
**内容:**

GoogleAnalyticsを実装しました。

環境変数`NEXT_PUBLIC_GA_MEASUREMENT_ID`を追加し、client と client-admin の両方のアプリケーションでGoogleAnalytics 4のトラッキングコードを実装しました。

開発環境では自動的にGAが無効になるよう実装しています。

Link to Devin run: https://app.devin.ai/sessions/bf89d99cdeb94897a6a5085d8e34826e
Requested by: annyotaka@gmail.com

**コメント:** なし

---

### [[FEATURE] レポート一覧に作成日時を追加する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/245)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-07T10:00:47Z  
**変更:** +9 -0 (4ファイル)  
**マージ日:** 2025-04-09T01:09:47Z  
**内容:**

Issue #218 の対応: レポート一覧に作成日時を追加しました。\n\nLink to Devin run: https://app.devin.ai/sessions/b13628010677450a813d14ed748a51ca\nRequested by: annyotaka@gmail.com

**コメント:** なし

---

### [[FEATURE] おすすめクラスタ数設定機能の実装 (#241)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/244)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-07T10:00:36Z  
**変更:** +82 -1 (3ファイル)  
**マージ日:** 2025-04-09T04:31:12Z  
**内容:**

Issue #241 の実装を行いました。

- 案0: README.mdとhow_to_use/README.mdに推奨クラスタ数の情報を追加
- 案1: CSVアップロード後に推奨クラスタ数設定UIを追加
- 計算方法: コメント数の立方根(∛n)を基準に計算

Google Spreadsheetの部分は無視しています。

テスト手順:
1. CSVファイルをアップロード
2. 推奨クラスタ数が表示されることを確認
3. 「この設定にする」ボタンで設定が適用されることを確認

Link to Devin run: https://app.devin.ai/sessions/4edce5fbbb4241d3b2c60118e98d4b8d
Requested by: annyotaka@gmail.com

**コメント:** なし

---

### 過去7日間に作成されたPR (3件)

### [静的ファイルエクスポート機能の追加 (#220)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/309)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-15T05:29:02Z  
**変更:** +194 -10 (11ファイル)  
**内容:**

# 静的ファイルエクスポート機能の追加

Issue: #220

## 変更内容
- clientアプリに静的ファイル出力用APIエンドポイント（/api/static-export）を追加
- client-adminアプリの一覧画面に「全レポートをエクスポート」ボタンを追加
- ボタンクリック時にclientの/api/static-exportエンドポイントを呼び出し、静的ビルドを実行
- 生成されたZIPファイルをダウンロードする機能を実装

## テスト方法
- clientアプリの/api/static-exportエンドポイントにアクセスし、静的ビルドが実行されZIPファイルがダウンロードされることを確認
- client-adminアプリの一覧画面の「全レポートをエクスポート」ボタンをクリックし、静的ビルドが実行されZIPファイルがダウンロードされることを確認

Link to Devin run: https://app.devin.ai/sessions/c429bebcd84540059a6560b3dad3db7a


**コメント:** なし

---

### [Fix #274: 静的ビルド時のhttp://localhostの参照を相対パスに修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/275)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-10T07:00:47Z  
**変更:** +29 -17 (8ファイル)  
**内容:**

このPRでは、静的ビルド時に含まれる絶対URLパス（http://localhost）を相対パスに修正し、どこでも動作するようにします。

修正内容:
- getApiBaseUrl() 関数を修正して静的ビルド時に相対パスを返すよう変更
- エラーメッセージの中のURLパス参照を修正
- metadataBase の設定を静的ビルド時に適切に処理するよう修正
- GitHub Actions のビルド設定を修正

Link to Devin run: https://app.devin.ai/sessions/11ffaf2b93ea42538a5b43e27563b24c
Requested by: nsk.smn@gmail.com

**コメント:** なし

---

### [[FEATURE] Admin一覧画面からstatic exportを実行できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/273)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-10T03:16:15Z  
**変更:** +970 -27 (11ファイル)  
**内容:**

## 変更内容
- Admin一覧画面に「全レポートをエクスポート」ボタンを追加
- クライアントサイドにstatic exportを実行するAPIエンドポイントを追加
- エクスポート結果をZIPファイルとしてダウンロードする機能を実装

issue #220 の対応

### テスト方法
1. Admin画面のレポート一覧で「全レポートをエクスポート」ボタンをクリック
2. エクスポート処理が完了するとZIPファイルがダウンロードされる
3. ZIPファイルを展開し、HTMLファイルが正しく含まれていることを確認

### 実装の詳細
- 本番環境ではDockerが利用できない可能性があるため、クライアントサイドでビルドを実行する方式に変更
- クライアントアプリに専用のAPIエンドポイント（/api/static-export）を追加し、npmスクリプトを実行
- 管理画面からはこのエンドポイントを呼び出してZIPファイルをダウンロード

Link to Devin run: https://app.devin.ai/sessions/99a83805083043dcb3b8a24f38fc766a
Requested by: nsk.smn@gmail.com

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(3件)

### [Fix: 静的ビルド時のパーミッションエラー修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/258)

**作成者:** nishio  
**作成日:** 2025-04-08T07:20:09Z  
**変更:** +1 -1 (1ファイル)  
**内容:**

# 静的ビルド時のパーミッションエラー修正

## 問題
静的ファイル出力（static build）を行う際、2回目以降にパーミッションエラーが発生する問題を修正しました。
Dockerコンテナ内でrootユーザーとしてファイルが生成されるため、ホスト側の通常ユーザーが`rm -rf out`でファイルを削除できなくなっていました。

## 解決策
Dockerコンテナ起動時にホストと同じユーザーIDを指定する方法（ユーザー指定アプローチ）を実装しました。
`docker compose run`コマンドに`--user $(shell id -u):$(shell id -g)`オプションを追加することで、
生成されるファイルの所有者がホストユーザーになり、パーミッションエラーが発生しなくなります。

## メリット
- 根本的な解決策（原因を解決）
- 生成されるファイルの所有者が最初からホストユーザーになる
- セキュリティ的に優れている（最小権限の原則に従う）

Fixes #225

Link to Devin run: https://app.devin.ai/sessions/b996b4b929424c5788a064bcafebf242
Requested by: NISHIO Hirokazu (nishio.hirokazu@gmail.com)

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [[FEATURE] レポートの複製・再利用機能 (Issue #19)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/248)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-07T10:07:21Z  
**変更:** +231 -7 (5ファイル)  
**内容:**

このPRはIssue #19の実装です。レポートの設定を複製・再利用する機能を追加します。

## 変更内容
- 管理画面に「既存レポートの再利用」オプションを追加
- 既存レポートの設定を取得するAPIエンドポイントを追加
- レポート生成時に複製元のレポートの中間成果物をコピーする機能を追加

## リンク
- Issue: #19
- Link to Devin run: https://app.devin.ai/sessions/7f69c1c5eace4259828fdcd2cce6f06a

## 検証方法
1. 管理画面で「既存レポートの再利用」を選択
2. 既存レポートを選択して設定を読み込む
3. 設定を変更して新しいレポートを作成
4. レポートが正常に生成されることを確認

**コメント:** なし

---

### [[FEATURE] 1回のextractionで複数のcommentを処理する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/246)

**作成者:** devin-ai-integration[bot]  
**作成日:** 2025-04-07T10:02:28Z  
**変更:** +360 -65 (5ファイル)  
**内容:**

# 複数コメントを1回のextraction処理で処理する

## 概要
Issue #190 の実装です。1回のLLMリクエストで複数のコメントを同時に処理できるようにしました。これにより、処理速度の向上とOpenAI APIのレート制限の問題の緩和が期待できます。

## 変更内容
- extractionPromptを更新し、複数コメントを一度に処理できるフォーマットに変更
- extraction.pyにバッチ処理のロジックを実装
- parse_json_list.pyを拡張し、新しいJSONレスポンス形式に対応

## テスト
- 短いコメント（ツイートレベル）と長いコメント（公開コメントレベル）の両方でテスト
- 従来の方法と比較して処理速度の向上を確認

Link to Devin run: https://app.devin.ai/sessions/c9d31459eaed4fe9bc2274aaf699d893
Requested by: annyotaka@gmail.com


**コメント:** なし

---

