# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-04-15 から 2025-04-22 まで

## Issues

### 過去7日間に完了されたissue (17件)

### [[BUG]Dockerコンテナでのazureモジュールインポートエラー](https://github.com/digitaldemocracy2030/kouchou-ai/issues/355)

**作成者:** nishio  
**作成日:** 2025-04-21T18:40:37Z  
**内容:**

下記のDevinの提案する解決策が妥当かどうかわからないのでコメントが欲しいです

## 問題の説明
ローカル環境（Macbook上のDocker Desktop）でDocker Composeを使用して起動した際に、以下のエラーが発生しています：

```
ModuleNotFoundError: No module named 'azure'
```

このエラーは`storage.py`ファイルでAzureモジュールが無条件にインポートされているために発生しています。実際には`STORAGE_TYPE=local`（デフォルト設定）の場合、Azureモジュールは使用されないにもかかわらず、常にインポートが試行されています。

## 原因
`server/src/services/storage.py`ファイルの先頭で、以下のようにAzureモジュールを無条件にインポートしています：

```python
from azure.core.exceptions import ResourceNotFoundError
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
```

しかし、実際にAzureモジュールが使用されるのは`STORAGE_TYPE=azure_blob`が設定されている場合のみです。ローカル開発環境では通常`STORAGE_TYPE=local`が使用されるため、Azureモジュールは不要です。

## 解決プラン

1. `storage.py`ファイルを修正し、Azureモジュールのインポートを条件付きにする
2. Azureモジュールのインポートを`AzureBlobStorageService`クラス内に移動し、このクラスが実際に使用される場合のみインポートされるようにする
3. `ResourceNotFoundError`の例外処理を修正し、型名で確認するように変更する

## 修正案

```python
# storage.pyの先頭部分を修正
import os
from abc import ABC, abstractmethod
from pathlib import Path

from src.config import settings
from src.utils.logger import setup_logger

logger = setup_logger()
```

```python
# AzureBlobStorageServiceクラスの__init__メソッドを修正
def __init__(self):
    """AzureBlobStorageServiceのコンストラクタ

    設定からAzure Blob Storageの接続情報を取得し、クライアントを初期化します。
    Azureモジュールの読み込みはこのクラスが必要な場合のみ行います。
    """
    # Azure関連のモジュールを必要なときのみインポート
    from azure.core.exceptions import ResourceNotFoundError  # noqa: F401
    from azure.identity import DefaultAzureCredential
    from azure.storage.blob import BlobServiceClient
    
    self.blob_service_client = BlobServiceClient(
        account_url=settings.azure_blob_storage_account_url,
        credential=DefaultAzureCredential(),
    )
    self.container_client = self.blob_service_client.get_container_client(
        settings.AZURE_BLOB_STORAGE_CONTAINER_NAME
    )
```

この修正により、ローカル開発環境ではAzureパッケージがインストールされていなくても、`STORAGE_TYPE=local`の場合にアプリケーションが正常に起動できるようになります。


**コメント:** なし

---

### [[REFACTOR] broadlistening.pngが重い](https://github.com/digitaldemocracy2030/kouchou-ai/issues/347)

**作成者:** mtane0412  
**作成日:** 2025-04-21T08:13:32Z  
**内容:**

# 現在の問題点
broadlistening.pngが1.2MBで表示されている。
低速環境やモバイル通信などで問題のあるサイズ。
![](https://i.gyazo.com/95c3d41fe7fd1bd576e0e3a2fe89624e.png)

# 提案内容
画像はNextImageを使用して最適化して表示するようにする
https://chakra-ui.com/docs/components/image#nextjs-image

**コメント:** なし

---

### [[BUG] レポート数が多いときにstatic buildのOGP画像生成でエラーが出る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/343)

**作成者:** mtane0412  
**作成日:** 2025-04-20T07:31:13Z  
**内容:**

### 概要

レポート数が一定数を超えた状態で静的サイト出力を行うと、OGP画像の生成時にAPI通信エラー（fetch failed）が発生し、ビルドが失敗することがあります。

問題を確認している時点での静的ページ数
Generating static pages (26/26)

### 再現手順

1. レポートをたくさん作る
2. `make client-build-static` で静的サイト出力
3.  ビルドプロセス中、 /app/[slug]/opengraph-image.png ルートのプリレンダリング段階で TypeError: fetch failed を伴うエラーが発生し、ビルドが途中で終了する

### 期待する動作

レポートの数に関係なく静的サイト出力できる

### スクリーンショット・ログ

一例。毎回エラーが起きるレポートページのslugは様々で、ごくまれに全部出力が成功することもある。

```shell
(3.12.0) mtane0412@mtane0412 kouchou-ai % make client-build-static
rm -rf out
docker compose up -d api
[+] Running 2/2
 ✔ Network kouchou-ai_app-network  Created                                                 0.0s 
 ✔ Container kouchou-ai-api-1      Started                                                 0.2s 
docker compose run --rm -v /Users/mtane0412/dev/kouchou-ai/server:/server -v /Users/mtane0412/dev/kouchou-ai/out:/app/dist client sh -c "npm run build:static && cp -r out/* dist"
[+] Creating 1/0
 ✔ Container kouchou-ai-api-1  Running                                                     0.0s 
> kouchou-ai-client@0.1.0 prebuild:static
> npm run copy-image && NEXT_PUBLIC_OUTPUT_MODE=export npm run rename-file
> kouchou-ai-client@0.1.0 copy-image
> node scripts/copy-image.mjs
Copied from default: icon.png
Copied from default: ogp.png
Copied from default: reporter.png
✅ All images copied successfully.
> kouchou-ai-client@0.1.0 rename-file
> node scripts/rename-file.mjs rename
Renamed: app/[slug]/opengraph-image.tsx → _opengraph-image.tsx
> kouchou-ai-client@0.1.0 build:static
> NEXT_PUBLIC_OUTPUT_MODE=export next build

   ▲ Next.js 15.2.3

   Creating an optimized production build ...
 ✓ Compiled successfully
 ✓ Linting and checking validity of types    
 ✓ Collecting page data    

Error occurred prerendering page "/794f022e-2086-48ca-8e49-d442049627c0/opengraph-image.png". Read more: https://nextjs.org/docs/messages/prerender-error

TypeError: fetch failed
    at node:internal/deps/undici/undici:13502:13
    at processTicksAndRejections (node:internal/process/task_queues:105:5)
    at runNextTicks (node:internal/process/task_queues:69:3)
    at listOnTimeout (node:internal/timers:555:9)
    at process.processTimers (node:internal/timers:529:7)
    at async Promise.all (index 0)
    at async g (/app/.next/server/app/[slug]/opengraph-image.png/route.js:1:924)
    at async to.do (/app/node_modules/next/dist/compiled/next-server/app-route.runtime.prod.js:18:18556)
    at async to.handle (/app/node_modules/next/dist/compiled/next-server/app-route.runtime.prod.js:18:23632)
    at async exportAppRoute (/app/node_modules/next/dist/export/routes/app-route.js:94:26)
Export encountered an error on /[slug]/opengraph-image.png/route: /794f022e-2086-48ca-8e49-d442049627c0/opengraph-image.png, exiting the build.
 ⨯ Next.js build worker exited with code: 1 and signal: null
npm notice
npm notice New major version of npm available! 10.9.2 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice
make: *** [client-build-static] Error 1
```

### その他

修正投げます。

**コメント:** なし

---

### [[FEATURE]Scatterにおいてラベルの表示/非表示を選択できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/327)

**作成者:** nasuka  
**作成日:** 2025-04-18T05:09:15Z  
**内容:**

# 背景
* 意見グループ数が増えるとラベルが重なって見にくくなるという問題がある
* この問題があるため、意見グループを一定以上に増やすことが難しい


# 提案内容
* ラベルの表示/非表示を設定できるようにする
  * 表示の場合は全ラベルを表示し、非表示の場合はどのラベルも表示しない

**コメント:** なし

---

### [[BUG]Azure Storage連携をしている場合にパブコメモードのCSVファイルがDLできなくなる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/325)

**作成者:** nasuka  
**作成日:** 2025-04-17T16:26:03Z  
**内容:**

### 概要
Azure Storage連携をしている際に、スクショ部分のCSVファイルがDLできない

![Image](https://github.com/user-attachments/assets/893a2ac4-d4f4-4ae5-8cc1-e77c8c68ccbe)

ストレージ連携をしている場合は、ストレージに出力ファイル等をアップロードをした後に容量節約のために不要なファイルを削除しているが、その際に当該のCSVファイルも削除されてしまっているためDLできなくなっている。


**コメント:** なし

---

### [[FEATURE] 作成日時がUTCで出力される](https://github.com/digitaldemocracy2030/kouchou-ai/issues/317)

**作成者:** mtane0412  
**作成日:** 2025-04-17T02:03:03Z  
**内容:**

# 背景
- macOSでdockerを使用してセットアップした環境では、レポートの作成日時がUTCで表示されている
- 非技術者がいつデータを作成したのかという点で混乱しそう

# 提案内容
- タイムゾーン設定を追加する
- デフォルトタイムゾーンを日本時間にする

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

### [[FEATURE]Azureのデプロイ更新作業をMakefileにまとめる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/214)

**作成者:** nishio  
**作成日:** 2025-04-01T08:22:16Z  
**内容:**

# 背景
作業が複雑なため

## chat log
nishio
最新版でAzureにデプロイされているものを更新しようとしたのですが、色々トラブって結局できませんでした。 makeでazure-login azure-build azure-acr-login-auto azure-push make azure-config-update make azure-fix-client-adminまでやったのですが見た目が変わらなくて、何がいけなかったのかなぁと思っています。
truego
上記だと、clien-admin コンテナは新しいもので起動しますが、client と api のコンテナは古いまま（イメージは新しくなったけどコンテナは古いもので起動したまま）になりそうですね。 azure-fix-client-admin の処理の中の以下の部分（古いイメージのコンテナを停止して、新しく push されたイメージでコンテナを起動する）と同様のことを client, api コンテナでもやる必要がありそうな気がしました。
```
az containerapp update --name client-admin --resource-group $(AZURE_RESOURCE_GROUP) --min-replicas 0 && \ echo '>>> 再度スケールアップ...' && \ sleep 5 && \ az containerapp update --name client-admin --resource-group $(AZURE_RESOURCE_GROUP) --min-replicas 1"
```

nishio
apiサーバを再起動したらレポートが全部消えたので無事コンテナの更新ができたようです:爆笑: Spreadsheetを読む機能が増えてたのでソースコードの更新は成功、問題はレポートの復元だけ


# 提案内容
Makefileにターゲットとしてまとめる


**コメント:** なし

---

### [[DOCUMENT] Azure である程度の期間運用する際に必要な項目を追加する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/175)

**作成者:** shingo-ohki  
**作成日:** 2025-03-25T08:21:14Z  
**内容:**

# 現在の問題点
- 最初に構築するときのことしかケアできていない
- 何らかの理由(環境変数を更新した、新機能が使いたくてコードを更新した、ロゴを設定した、など)でコンテナを作り直すときにはまりどころがある

> フルでmakeしちゃうと新しいACRが作られちゃうのか？→.env.azure.generatedに書き出されたACR名を.env.azureに転記していなかったので毎回生成されていた
from https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1742889861058199?thread_ts=1742886821.947769&cid=C08F7JZPD63

> コンテナを再起動して生成済みレポートが消える
> ソースコードが更新されて新機能が追加されたらみんな新機能を使いたくて作り直しをすると思いますけど、それでレポートが全部消えてたら泣かれるかもw
> 分析して「よし静的HTMLを生成して公開しよう、そのためにはロゴを入れて更新」で分析結果が消える
from https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1742889178309719

# 提案内容

> 環境変数を変更したい時とか、ソースコードをupdateしたい時のためのマニュアルがあればいい

**コメント:** なし

---

### [[FEATURE] 生成するレポートを永続化できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/174)

**作成者:** shingo-ohki  
**作成日:** 2025-03-25T08:17:16Z  
**内容:**

# 背景
（特に Azure 環境では）コンテナをつくり直すとそれまでに生成したレポートが消えてしまう
https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1742889178309719

# 提案内容
例えば、
1. レポート生成時に永続化できるようにする（Azure のストレージサービスや Google drive など?） 

**コメント:** なし

---

### [[FEATURE]50件の小さいデータで試した場合に濃いクラスタ抽出で見た目が変わらない問題の解決](https://github.com/digitaldemocracy2030/kouchou-ai/issues/96)

**作成者:** nishio  
**作成日:** 2025-03-19T02:41:35Z  
**内容:**

# 背景
50件の小さいデータで試した場合に濃いクラスタ抽出で見た目が変わらないことに混乱する


# 提案内容

案1:

>濃いクラスタ抽出で見た目が変わらないのはデータが少なすぎて実行されてないからか？そういう時にはボタンを非表示にしたいかも。クリックして変わらないのは混乱させる

この方法が良いかはわからない

**コメント:** なし

---

### [(情報整理)Azureについて](https://github.com/digitaldemocracy2030/kouchou-ai/issues/80)

**作成者:** nishio  
**作成日:** 2025-03-18T03:33:26Z  
**内容:**

自治体や大企業などを中心にAzureを使いたいというニーズがある。

これを分解整理する

- 1: ✅ OpenAIのAPIを直接叩くのではなくAzure OpenAI Serviceを使いたい( #89)
- 2: ✅ Azureでホストしたい(#94)
- 3: Azure Container Appsでホストしている場合にソースコードのアップデートをすると既存のレポートが消えてしまう問題の解決

- x: Azureでのセットアップガイド ( #133 #175)

## 3に関して

- https://github.com/digitaldemocracy2030/kouchou-ai/pull/180 で消失を防いでいるが部分的解決に過ぎない
- https://github.com/digitaldemocracy2030/kouchou-ai/issues/214 で更新時に自動的に保存する方針にした
- これらをビルドに含めることができれば実は解決なのでは？という気もする https://github.com/digitaldemocracy2030/kouchou-ai/issues/216

- 王道の解決方法はストレージ接続の #174 #46 だと思うが、デフォルトでONにしないなら「ストレージOFFで始めて試して、いいレポートができたので保存したくなったので更新しようとして消える」というバターンが発生することのケアが必要

**コメント:** なし

---

### 過去7日間に作成されたissue (16件)

### [[REFACTOR] client-admin/app/create/page.tsx のリファクタリング](https://github.com/digitaldemocracy2030/kouchou-ai/issues/350)

**作成者:** mtane0412  
**作成日:** 2025-04-21T15:26:43Z  
**内容:**

# 現在の問題点
- client-admin/app/create/page.tsx が1200行を超えている
- LLMも読むのに苦労している

# 提案内容
componentやhookを分離する

**コメント:** なし

---

### [(実験) 同一の内容が大量に投稿される問題への対処法](https://github.com/digitaldemocracy2030/kouchou-ai/issues/346)

**作成者:** nasuka  
**作成日:** 2025-04-21T05:54:34Z  
**内容:**

# 背景
https://github.com/digitaldemocracy2030/kouchou-ai/issues/345
上記のIssueに紐づく実験のIssue

以下元Issueの背景を転載
* [パブコメの大量投稿](https://x.com/takahiroanno/status/1914151807443718381) によって、入力データの中に似通った内容が大量に含まれる場合がある
* これによって、以下の問題が起きる
  * 1.フロントの処理負荷が高くなる
    * 現在の設計では、数万件〜規模のデータは描画の負荷が高くPCによっては正常に表示できない可能性がある
  * 2.バックエンドの処理負荷・コストが高くなる
    * レポート出力処理の際のクラスタリングの計算負荷が高くなる・extraction処理にかかるLLM APIのコストが高くなる
  * 3.ユーザーの認知負荷が高くなる
    * 今の形式でクラスタリングや可視化を行うと、スパム的な意見が意見全体の大半を占めるために、本来着目したい意見が目立たなくなってしまう可能性がある


# 提案内容
* 類似する意見をあらかじめまとめたうえで、まとめた後の意見を広聴AIの分析にかける。
  * まとめた後の意見が表示されるようになることで、フロントの処理負荷が下がり、またユーザーの認知負荷も下がる
* まとめ方には幾つかのアプローチがありそう。
e.g. クラスタリングでまとめる、LLMでまとめる、そのハイブリッド等

↑は問題解決の一つのアプローチの案として記載していますが、他にアプローチがあれば随時コメントにご記載ください。

## 想定する進め方
* 実験データの選定（or 作成）
* 実験データに対して、アルゴリズムを適用し、アウトプットを確認
  * * @nishio , @nasuka （+ 時間があれば@takahiroanno も）あたりは確認しておけると良さそう
* 問題なさそうであれば機能実装の検討に移る




**コメント:** なし

---

### [（情報整理）同一の内容が大量に投稿される問題への対処法](https://github.com/digitaldemocracy2030/kouchou-ai/issues/345)

**作成者:** nasuka  
**作成日:** 2025-04-21T05:40:51Z  
**内容:**

# 背景
* [パブコメの大量投稿](https://x.com/takahiroanno/status/1914151807443718381) によって、入力データの中に似通った内容が大量に含まれる場合がある
* これによって、以下の問題が起きる
  * 1.フロントの処理負荷が高くなる
    * 現在の設計では、数万件〜規模のデータは描画の負荷が高くPCによっては正常に表示できない可能性がある
  * 2.バックエンドの処理負荷・コストが高くなる
    * レポート出力処理の際のクラスタリングの計算負荷が高くなる・extraction処理にかかるLLM APIのコストが高くなる
  * 3.ユーザーの認知負荷が高くなる
    * 今の形式でクラスタリングや可視化を行うと、スパム的な意見が意見全体の大半を占めるために、本来着目したい意見が目立たなくなってしまう可能性がある


# 進め方
* アルゴリズムの改善によって上記の問題を解決するかを検討する。
* いきなり機能を実装するのではなく、プロダクトとは独立して実験スクリプトを実装し、検証用のデータセットを使って結果の妥当性を評価する
* 問題なければプロダクトの機能として実装を進める
  * 一旦実験系のIssueだけ立てておき、機能することがわかった段階でプロダクトへの実装イシューを立てる

```
1: 独立したスクリプトとして機能するものを作れるが実験
2: それをapiサーバに統合するか検討
3: それをどんなGUIでユーザに見せるか検討
という流れがスムーズかなと思いました
```

**コメント:** なし

---

### [[FEATURE]文脈をふまえた生データの整形](https://github.com/digitaldemocracy2030/kouchou-ai/issues/342)

**作成者:** masatosasano2  
**作成日:** 2025-04-19T18:09:28Z  
**内容:**

# 背景
例えばXの投稿を元にクラスタリングする場合、今だと生の投稿がそのままクラスタリング対象となっている。
しかし、返信元の投稿、引用元の投稿、1つ前の投稿、同時に貼られている画像/音声/URLなどの文脈を踏まえないと内容の解釈の正確性が落ちる。

# 提案内容
クラスタリングの前処理として生のデータに文脈情報を付与したい。
例えば、「〇〇すべき」という投稿に対してついた「反対」という返信は単独だと意味不明だが、「〇〇すべきでない」などと整形しておけば処理しやすくなる。


**コメント:** なし

---

### [[FEATURE] レポートの限定公開](https://github.com/digitaldemocracy2030/kouchou-ai/issues/341)

**作成者:** mtane0412  
**作成日:** 2025-04-19T14:49:51Z  
**内容:**

# 背景
- レポートの公開ステータスは公開と非公開で、非公開にした場合、管理者であってもレポートページを参照することができない
- 面白いレポートができたので他人に共有したいが、一般に広く公開したいわけではないものがある。既に作成したデータも公開しているので、部分公開しようと思うと手間がかかる。


# 提案内容
- Youtubeの限定公開のように、URLを知っている人だけがアクセスできるレポートページの状態を作る
- 単純にトップページからリンクされないように出力すればできる？

**コメント:** なし

---

### [[FEATURE]同義語マップがほしい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/339)

**作成者:** masatosasano2  
**作成日:** 2025-04-19T06:48:31Z  
**内容:**

# 背景

- 一般的なLLMが学習していない特殊な同義語が色々ありそう（スラング、愛称、蔑称、プロパガンダ用の言い換えなど）
- 単なる略称などの表記ゆれもカバーできてない可能性がある

# 提案内容

- 同義語マップを差し込めるようにする
- デフォルトマップを用意し、育てていきたい
- ユーザー用マップの情報を得て適宜デフォルトマップに反映したい（要人間判断）

**コメント:** なし

---

### [[FEATURE] 「全体図」と「階層図」の意見グループの色を揃える](https://github.com/digitaldemocracy2030/kouchou-ai/issues/337)

**作成者:** shingo-ohki  
**作成日:** 2025-04-19T05:17:29Z  
**内容:**

# 背景
「全体図」から「階層図」に切り替えた時に、注目していた意見グループを見失いがち（もちろん文字を読めば分かる）

from 2025.4.19 広聴AIもくもく会


# 提案内容
「全体図」と「階層図」の意見グループの色を揃えてはどうか？

**コメント:** なし

---

### [[FEATURE] static exportしたHTMLファイルをwebサーバーなしで閲覧できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/333)

**作成者:** nasuka  
**作成日:** 2025-04-18T08:28:41Z  
**内容:**

# 背景
* static exportしたhtmlファイルについて、現在はwebサーバーにhtmlを配置しないと閲覧できないという問題がある。
  * 添付したスクショの様にエラーが発生し、データ・スクリプト・画像等が読み込めない
* この問題により、閲覧する際にWebサーバーが必須となるためレポートを共有するハードルが高い

![Image](https://github.com/user-attachments/assets/40e25d38-31d3-4517-90e2-d3e2bb14b7cf)

# 提案内容
Webサーバーなしで閲覧できるhtmlファイルを作成できるようにする。
自分がフロントに余り詳しくなく、上記を実現するための具体的なアプローチを思いつく方はコメントいただけると助かります。


**コメント:** なし

---

### [[FEATURE]第一階層の意見グループ数の上限を増やす](https://github.com/digitaldemocracy2030/kouchou-ai/issues/330)

**作成者:** nasuka  
**作成日:** 2025-04-18T05:59:54Z  
**内容:**

# 背景
* 現在、全体図などの散布図において意見グループの個数上限は20となっている
  * ラベルが重なってしまう問題があったため上限を20にしていたが、この問題は回避策のPR（ https://github.com/digitaldemocracy2030/kouchou-ai/pull/329 ）が出されている

# 提案内容
* グループ数の上限を40に増やす
* グループのカラーバリエーションも20 -> 40に増やす

**コメント:** なし

---

### [[FEATURE] レポートのタイトルを変更できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/328)

**作成者:** mtane0412  
**作成日:** 2025-04-18T05:21:40Z  
**内容:**

# 背景
現在最初に設定したタイトルの変更は管理画面からはできない(という認識)。

クラスタ設定を間違えたり、Rate Limitが発生して不完全なレポートでも出力例として残したい場合などに、タイトルを変更してわかりやすく管理したい。

# 提案内容
レポート一のオプションボタンからタイトルを編集できるようにする

![](https://i.gyazo.com/45b10370a28fd77f8ed520ec8bc7f702.png)

**コメント:** なし

---

### [[FEATURE]ファクトチェックロジックの実験](https://github.com/digitaldemocracy2030/kouchou-ai/issues/324)

**作成者:** masatosasano2  
**作成日:** 2025-04-17T14:09:02Z  
**内容:**

# 背景
各サービスでファクトチェックが必要とされている。
ファクトチェック処理は共通化できるので、本Issueはその共通処理を実験するためのIssueとする。
処理のコードをどこに置くべきかはidobata側のリポジトリの統一後に検討する。

# 関連Issue

1. https://github.com/digitaldemocracy2030/kouchou-ai/issues/170
2. https://github.com/digitaldemocracy2030/idobata-analyst/issues/97
3. https://github.com/digitaldemocracy2030/idobata-discourse-agent/issues/51

# 関連Issue1から抜粋

<img width="600" alt="Image" src="https://github.com/user-attachments/assets/5968bb66-9070-4a84-b0cb-170205f319e5" />

# 提案内容

- 実装方針：どこかで議論されていたとおり怪しいものは弾かずOKにして、明確に偽情報と判断した場合のみ弾く。
- 準備：偽情報を含みそうな適当なデータセットを用意し、人力で正解データを作る。
- 実験概要：以下のコストや精度を比較する。他のアプローチがあれば随時試す。
    - 既存のファクトチェックサービスで偽と判定された場合のみNGとする
    - いくつかの信用できる情報源を指定し、そこから取得できる事実から偽と判定された場合のみNGとする
    - 単純なWeb検索の結果から偽と判定された場合のみNGとする
    - DeepResearch的な仕組を自作し、それに偽と判定された場合のみNGとする
    - 既存のDeepResearch系のサービスで偽と判定された場合のみNGとする

**コメント:** なし

---

### [[FEATURE] レポートの多言語対応](https://github.com/digitaldemocracy2030/kouchou-ai/issues/323)

**作成者:** mtane0412  
**作成日:** 2025-04-17T11:57:43Z  
**内容:**

# 背景
Steamのレビューデータで遊んでいるときに、コメントは多言語でLLMも読めるが、最後のレポートでも元言語で表示されるために多言語混在状態となり、人間が読みづらい問題があるかなと思いました。
実運用場面では、異なる言語を話す住民に対して同一の調査を実施できるようになるというストーリーがありそうだなと思いました。


# 提案内容
Pol.isのようなレポート出力時の翻訳機能をつける
出力言語を選択できるようにする

**コメント:** なし

---

### [[FEATURE] 意見を抽出できなかったときのエラーハンドリング](https://github.com/digitaldemocracy2030/kouchou-ai/issues/318)

**作成者:** mtane0412  
**作成日:** 2025-04-17T02:28:08Z  
**内容:**

# 背景
XのポストやSteamのレビューなどで試しているときに、extractionの段階で大量の `ERROR:root:Task <Future at 0xffff7d57f470 state=finished raised RuntimeError> failed with error: JSON list not found` が出ます。
おそらくコメントの中から意見を抽出できないことが多いと推測。(違ったら教えて下さい。)

実運用ではまとまった意見のデータが使われると思いますが、レポート作成者が「抽出段階でよくわからないエラーが出ている」という体験がありそうかなと思いました。

#315 が実装された場合に向けてログのノイズを減少させる。

# 提案内容
意見が抽出できなかった場合、元コメントと併記して意見が抽出できなかったことをログ出力する。

**コメント:** なし

---

### [[FEATURE]エラーログをファイルに出力する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/315)

**作成者:** nasuka  
**作成日:** 2025-04-16T12:06:28Z  
**内容:**

# 背景
* 自治体の担当者などが広聴AIを動かしてエラーがおきた際に、どのようなエラーが起きているのかを広聴AI開発サイドに伝えてもらいたいが、担当者側でエラーログを確認するのが難しい


# 提案内容
* エラーログをファイルに出力するようにする
  * エラーが起きた場合は、ファイルに書き出された内容を伝えてもらう or ファイルの内容をそのまま教えてもらう

広聴AIでsentryを用意し、エラーログをそちらに集約する案も出たが、機微情報が含まれることが懸念される可能性がある。上述した方式であれば、機微情報は担当者側で削除した上でエラーログを連携してもらうことが可能。

**コメント:** なし

---

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

### 過去7日間に更新されたissue（作成・クローズを除く）(28件)

### [[FEATURE]「全体図」「濃い意見グループ」のUI/UX改善](https://github.com/digitaldemocracy2030/kouchou-ai/issues/306)

**作成者:** masatosasano2  
**作成日:** 2025-04-13T11:20:06Z  
**内容:**

# 背景

操作しててたまたま以下に気づいたが、見ただけでは分からない。
・範囲指定（ドラッグ）すると拡大できること
・拡大した状態から元の倍率に戻すにはダブルクリックすること

濃い意見グループで上がってきているクラスタが第一階層？のクラスタのどれに属すのかがわからない。

# 提案内容

ズームについて
- ヒントアイコンで操作方法のヒントを表示する
- ズームイン/アウトの操作ボタンを用意する（ドラッグでパンできないので、上下左右の移動ボタンも必要？）
- 表示モードや全画面に切り替えたときに表示がリセットされないように Issue #290 を参考に状態保持を実装する

濃い意見グループについて
- ラベルか色で表現する？

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

### [（アルゴリズム検証） 広聴AIで出力したクラスタのタイトルが抽象的になる問題の解決](https://github.com/digitaldemocracy2030/kouchou-ai/issues/269)

**作成者:** nasuka  
**作成日:** 2025-04-09T06:22:31Z  
**内容:**

# 背景
広聴AIで出力した第一階層のクラスタタイトルが、TTTCのタイトルと比べて具体性に欠けるという声がある。
 
衆院選のデータセットでクラスタタイトルを出力した例を以下に記載する。クラスタ数はどちらも15で設定している。
本来はクラスタに属するデータ点との整合性なども含めて議論するのが理想だが、こちらではクラスタの抽象度についてのみ議論する。

### TTTCの出力結果
レポートのURL: https://news.ntv.co.jp/static/shugiinsenkyo2024/closed-1027/index.html

選挙結果への関心と不安
立憲民主党の支持増加と自民党への批判
過半数割れの可能性と連立政権の模索
投票率と市民参加の重要性
候補者の当選とその影響
選挙特番のエンタメ化
国民民主党と立憲民主党の議席増加への注目
議員の落選に対する反応
石破氏の責任問題
政権交代の可能性
地域別支持動向
和歌山2区の選挙結果
選挙結果の誤報や虚偽情報への懸念
れいわ新選組の躍進と支持拡大への関心
出口調査結果への関心と懐疑


### 広聴AIの出力結果

選挙結果と政治倫理に対する多様な反応と期待
地域別選挙動向と多様な反応
選挙に対する多様な関心と報道の影響
選挙参加と投票率に関する多様な視点と期待
選挙における政党の躍進と略称問題に対する多様な反応
衆院選結果に対する多様な反応と政治的期待
選挙における政党批判と有権者の多様な視点
選挙報道とスポーツ中継の視聴体験とメディアの役割
選挙結果の信頼性と世襲政治に対する多様な反応
日本の政治再編と選挙結果の影響
石破政権の持続性と自民党の未来に対する懸念と期待
日本の政治情勢における政党支持の変動とその影響
衆院選後の政治的再編と連立政権の行方
れいわ新選組の議席増加に対する多様な反応と期待
選挙における政権交代と地域政党の影響に関する多様な視点


感覚的だが、TTTCの出力結果が具体的な行動・現象や固有名詞（個人名・政党名等）がクラスタ名に含まれる傾向がある一方で、広聴AIの方は抽象性の高いタイトルがついているケースが多い。
一概にどちらが悪いといえるものはないが、実用性を考えるとTTTC程度の抽象度で記載されている方が有用な場合がある。

なお、o3-miniでも評価したが、同様の評価が記載されている。
https://chatgpt.com/share/67f60d38-43b4-800f-a20f-3836dbfa4518

![Image](https://github.com/user-attachments/assets/00a6bc92-5a48-4237-8da8-72be1dfbc1e5)

このような差分が生まれる要因として、以下が想定される。

* クラスタリングアルゴリズムの違い
  * 広聴AIではk-meansで第二階層のクラスタを形成した後にクラスタをマージして第一階層を形成するが、TTTCではspectral clusteringでクラスタを形成する
* クラスタリング時に用いる埋め込みの次元の違い
    * 広聴AIではUMAP後の2次元でクラスタリングを行っているが、TTTCでは元のembeddingでクラスタリングを行っている
      * 二次元空間上で飛び地ができるのを防ぐために広聴AIではこのような実装となっている
* プロンプトの違い
  * （アルゴリズムの違いに依存する話だが）広聴AIでは、第二階層のクラスタのタイトル・説明と、サンプリングしたクラスタに属するデータのテキストの情報に基づいて第一階層のタイトル・説明を生成している。一方でTTTCでは、下層のクラスタタイトル・説明を用いていない。
    * 下層のクラスタのタイトル・説明を包含するように指示しているため、抽象的なタイトルが生成されている可能性がある。


# 提案内容
プロンプトレベルでの修正と、アルゴリズムレベルでの修正がある。

## プロンプトレベルでの修正
1. デフォルトプロンプトの文言のチューニング・修正
2. プロンプトに入力する情報の修正
    例. 下層のタイトル・説明は含めずに、純粋にデータ点の情報だけ入力して第一階層のタイトル・説明を生成する


## アルゴリズムレベルでの修正
1. 元の埋込を用いてクラスタリングする
2. k-means以外のアルゴリズム（spectral clustering, hdbscan）を採用する


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

### [[BUG]縦長画面での散布図の表示がおかしい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/121)

**作成者:** nishio  
**作成日:** 2025-03-21T15:32:58Z  
**内容:**

### 概要

<img width="453" alt="Image" src="https://github.com/user-attachments/assets/c20dbff2-454c-4b23-bf8b-973bcc6c96fd" />


横長の時の表示:
<img width="1512" alt="Image" src="https://github.com/user-attachments/assets/1b7a062a-5413-4d24-b5f3-91cb81059d07" />

<!-- バグの簡潔な説明をお願いします -->

### 再現手順

1. 縦長画面で見る

### 期待する動作

- 理論的な理想を言うと、そもそもアスペクト比は1:1であるべき
- 一方でそれにこだわって徹底した場合にみやすさが損なわれるのも問題がある
- 縦長画面で見た場合はラベルの幅との干渉でアスペクト比が大きく狂っているのでそこだけでも直すか？

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->

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

### [[FEATURE] ツールの利用状況を知る仕組み](https://github.com/digitaldemocracy2030/kouchou-ai/issues/104)

**作成者:** shingo-ohki  
**作成日:** 2025-03-20T07:42:15Z  
**内容:**

# 背景
このツールが様々なところで使われるようになった際に、現状想定している利用方法（各利用者がツールの環境を作って利用する）の場合、このツールの実際の利用状況を知る手段が少ない


# 提案内容
例えば、あらかじめドキュメントなどで説明した上で、レポート生成を行うたびに Google Analytics が設定された特定のURLにリクエスト（生成するレポートについての情報は含まない、ツールを使ったということが分かる情報のみ）を飛ばすようにしておくと、そのアクセス解析を行うことで、いつどこでレポート生成が行われたかを知ることができ、このツールの利用状況が得られるようになり、その情報を広報活動や開発に活用できる

というのはどうでしょうか？

**コメント:** なし

---

### [[FEATURE] 濃いクラスタのしきい値のデフォルト値をレポートごとに設定できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/55)

**作成者:** nanocloudx  
**作成日:** 2025-03-16T03:55:36Z  
**内容:**

# 背景
現在の濃いクラスタのしきい値のデフォルト値はレポートごとに一律で固定値（上位20%・最小5件以上）となっている。
レポート出力者が、出力結果を確認した上で、しきい値のデフォルト値を変更できると良い

# 提案内容
- client-admin にて、出力済みのレポートに対して、デフォルトのしきい値を追加保存できるようにする
- client では濃いクラスタの初期表示が、レポート出力者の指定したしきい値になるようにする

**コメント:** なし

---

### [[FEATURE]濃いクラスタを表示している際は、クラスタの説明文も濃いクラスタに合わせたい](https://github.com/digitaldemocracy2030/kouchou-ai/issues/24)

**作成者:** nasuka  
**作成日:** 2025-03-06T05:36:37Z  
**内容:**

# 背景
* 現状は濃いクラスタ表示した際も、全体図と同じクラスタの説明文が並んでいる（最上位層のクラスタが並んでいる）
  * 添付画像のように、現状は散布図上のタイトルと下部のタイトルが整合しない
![Image](https://github.com/user-attachments/assets/27fde824-7e69-4c3d-8f0a-475ca265b20d)

# 提案内容
* 「濃いクラスタ」が選択されている場合はそれらの説明文を表示したい
  * フィルタされているクラスタの解説文のみをページ下部に表示する






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

### [[FEATURE]レポート出力にかかる時間の目安を記載する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/11)

**作成者:** nasuka  
**作成日:** 2025-03-04T10:59:48Z  
**内容:**

# 背景
* レポート出力までに何分程度かかるのかがユーザー目線でわからない


# 提案内容
* 実行時間の目安を記載する


**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (19件)

### [broadlistening.pngの圧縮](https://github.com/digitaldemocracy2030/kouchou-ai/pull/349)

**作成者:** mtane0412  
**作成日:** 2025-04-21T12:58:17Z  
**変更:** +0 -0 (1ファイル)  
**マージ日:** 2025-04-21T13:07:56Z  
**内容:**

# 変更の概要
- broadlistening.pngをImageoptimを用いて圧縮した(1.2MB → 283kB)

```zsh
i Running ImageOptim...
✓ broadlistening.png was: 1.2MB now: 293kB saving: 911kB (75.69%)
✓ TOTAL was: 1.2MB now: 293kB saving: 911kB (75.69%)
✓ Finished
```

## 圧縮前
<img width="1576" alt="broadlistening_before" src="https://github.com/user-attachments/assets/e9c45061-8e25-45e6-8a64-4d49e142d0a6" />

## 圧縮後
![broadlistening](https://github.com/user-attachments/assets/82fde9c9-8f3d-4487-8e13-c48e04235053)


# 変更の背景
- ブロードリスニングのイメージ図が1.2MBと大きいサイズで、低速環境やモバイル環境にフレンドリーではなかった
- next/imageなどを用いた最適化は静的サイト出力に用いることができない
- 静的サイトビルド時に圧縮をかけるなどの方法もあるが、現時点で大きな画像はこの1ファイルのみなので単純に元画像を圧縮すれば済む

# 関連Issue
 #347 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [make azure-cleanup 時に確認メッセージを出す](https://github.com/digitaldemocracy2030/kouchou-ai/pull/348)

**作成者:** shingo-ohki  
**作成日:** 2025-04-21T12:33:30Z  
**変更:** +7 -0 (1ファイル)  
**マージ日:** 2025-04-21T14:11:58Z  
**内容:**

# 変更の概要
- make azure-cleanup 時に確認メッセージを出すようにします

# 変更の背景
- make azure-cleaup は、作成した Azure 環境をすべて削除するコマンドのため、誤って実行したときのために確認メッセージを出したほうがよいのではないか？と思いました
- 別件の作業時に make azure-cleanup を実行する機会があり、その際に気が付きました

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [Bug修正: static build時のOGP画像のリトライ処理を実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/344)

**作成者:** mtane0412  
**作成日:** 2025-04-20T07:37:21Z  
**変更:** +38 -3 (1ファイル)  
**マージ日:** 2025-04-20T12:23:23Z  
**内容:**

# 変更の概要
静的サイト出力時のOGP画像生成の安定化。`OpImage` 関数内のAPIデータ取得処理にリトライ機構を追加します。

# 変更の背景
現在の静的サイト出力（`make client-build-static`）において、特にレポート数が多い場合に、OGP画像生成プロセス（`client/app/[slug]/opengraph-image.png/route.ts` から呼ばれる `OpImage` 関数）がAPIからのデータ取得に失敗し（`Workspace failed`）、ビルドが中断される問題が確認されています。

この問題は、Next.jsの静的エクスポートが複数のOGP画像を並列で生成する際に、起動したばかりのAPIサービスへの同時多数アクセスが集中し、APIがリクエストを処理しきれない、あるいは一時的な通信エラーが発生することが原因と推測されます。エラーは非決定的（ランダム）に発生し、処理対象のレポート数が多いほど顕著になります。

この変更は、APIの準備が整う前のアクセスや、瞬間的な高負荷による一時的な通信失敗を吸収するため、`client/app/[slug]/_op-image.tsx` 内のAPI fetchにリトライ処理を導入することで、静的サイト出力の安定性を向上させることを目的としています。

# 関連Issue
#343 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [shingo-ohkiさんをメンテナーに追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/340)

**作成者:** nasuka  
**作成日:** 2025-04-19T13:45:38Z  
**変更:** +5 -4 (1ファイル)  
**マージ日:** 2025-04-19T13:45:58Z  
**内容:**

# 変更の概要
* @shingo-ohki さんがメンテナーになったのでドキュメントを追記


# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [CSVアップロード時におすすめクラスタ数をデフォルトとして設定する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/335)

**作成者:** mtane0412  
**作成日:** 2025-04-18T10:29:25Z  
**変更:** +386 -165 (3ファイル)  
**マージ日:** 2025-04-21T06:19:19Z  
**内容:**

# 変更の概要
- レポート作成画面の「おすすめクラスタ数設定」を「現在のクラスタ数設定」に変更
- 「この設定にする」ボタンを削除(変更は詳細設定の方で行う)
- 詳細設定を変更すると「現在のクラスタ数設定」と連動するようにした(一旦現在のUIをそこまで崩さないようにする措置)
- 何らかの原因でおすすめクラスタ数設定がnullの場合は初期値の5→50となる
- ドキュメントの関連の説明部分を仕様変更に合うように変更

連動動作の動画: 
![](https://i.gyazo.com/e748bd74f25f9c98e1d541bf73b61487.gif)

作成されたレポートへの反映を確認:
![](https://i.gyazo.com/cf3a64e9830985b2eb395b7f6b1f5dcc.png)


# 変更の背景
- クラスタ数の設定の一手間を減らしたい
- 現在のクラスタ数設定が詳細設定を開くまでわからない
- この設定にするボタンを押しても反映されているかわからない

クラスタ数設定のUIは検討する余地があるが、別スコープとして一旦変更案をあげた。

# 関連Issue
#303

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [[FEATURE] 意見グループのカラーバリエーションを20から40に増やす](https://github.com/digitaldemocracy2030/kouchou-ai/pull/332)

**作成者:** nsk.smn+Devin  
**作成日:** 2025-04-18T06:11:11Z  
**変更:** +20 -0 (1ファイル)  
**マージ日:** 2025-04-18T06:25:46Z  
**内容:**

# 概要
Issue #330 の対応として、意見グループのカラーバリエーションを20から40に増やしました。

## 変更内容
- `client/components/charts/ScatterChart.tsx` の `softColors` 配列に20色を追加
- 既存の色合いと被らないように新しい色を選定

## 関連Issue
Closes #330

## Link to Devin run
https://app.devin.ai/sessions/13cf7d9312e1499bbeda7a28e54f55af
Requested by: nsk.smn@gmail.com


**コメント:** なし

---

### [意見グループのタイトルの表示/非表示を設定する項目を実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/329)

**作成者:** nasuka  
**作成日:** 2025-04-18T05:38:30Z  
**変更:** +92 -22 (6ファイル)  
**マージ日:** 2025-04-21T15:36:23Z  
**内容:**

# 変更の概要
* 意見グループのタイトルの表示/非表示を設定する項目を実装
  * 元々あった「濃い意見グループ設定」のモーダルを「表示設定」に改名し、その中にトグルスイッチを配置している
* 表示がONの場合は全てのタイトルが表示され、OFFの場合はどのクラスタのタイトルも表示されない
  * ON/OFFの状態は全画面表示の際も引き継がれる


設定モーダル
![image](https://github.com/user-attachments/assets/474f7635-a3e3-4a26-94d0-004c3e6aec4d)


動作イメージ
![a3e20d4504a83d9a139a4953257cb8db](https://github.com/user-attachments/assets/a5c21b07-488b-4fa6-9046-3290901e1e15)



# 変更の背景
- 意見グループ数が増えるとラベルが重なって見にくくなるという問題がある
  - この問題があるため、意見グループを一定以上に増やすことが難しい

# 関連Issue
Close https://github.com/digitaldemocracy2030/kouchou-ai/issues/327

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [CSVダウンロード機能に用いるcsvを、Azure Blob Storage連携時の削除対象から除外](https://github.com/digitaldemocracy2030/kouchou-ai/pull/326)

**作成者:** nasuka  
**作成日:** 2025-04-17T16:33:35Z  
**変更:** +9 -8 (2ファイル)  
**マージ日:** 2025-04-17T17:00:05Z  
**内容:**

# 変更の概要
* CSVダウンロード機能に用いるcsv( `final_result_with_comments.csv` )を、Azure Blob Storage連携時の削除対象から除外
  * 従来は誤って削除対象になっていた
* アプリ起動時の同期対象に同ファイルを含めるよう修正

# 変更の背景
ストレージ連携をしている場合は、ストレージに出力ファイル等をアップロードをした後に容量節約のために不要なファイルを削除しているが、その際に当該のCSVファイルも削除されてしまっているためDLできなくなっていた。
当該ファイルはAzure Blob Storage上には保存されているが、アプリ起動時の同期対象からも外れておりアプリ上には存在しないため、アプリの再起動やコンテナの更新を行った場合もDLできなくなっていた。
ストレージにはcsvは保管されているので、今回の修正を反映した上でアプリ（コンテナ）を再起動すれば、以降はCSVをDLできるようになる。


# 関連Issue
Close https://github.com/digitaldemocracy2030/kouchou-ai/issues/325

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [レポート作成時にISR関連の注意書きを追加する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/322)

**作成者:** mtane0412  
**作成日:** 2025-04-17T11:30:55Z  
**変更:** +106 -0 (2ファイル)  
**マージ日:** 2025-04-17T14:37:44Z  
**内容:**

# 変更の概要
以下の注意書きをAlertコンポーネントでレポート作成ボタンの上に追加 ([@nasuka案](https://github.com/digitaldemocracy2030/kouchou-ai/issues/61#issuecomment-2795883061)) 
- レポートの作成には数分から数十分程度の時間がかかります
- 作成が完了したレポートが一覧画面に反映されるまで5分程度かかります

![](https://i.gyazo.com/334fa5543cea24e5512c14b4d941d02a.png)

# 変更の背景
> 新しいレポートが生成されてから、閲覧可能になるまでの間には約５分のラグがある
> これは client で ISR を行っており、この頻度を 300sec にしているのが原因（この仕組み自体は問題ない認識）
> この仕組みを知らないとレポート作成者が迷ってしまうので、５分遅れる旨を client-admin に書くとよさそう

# 関連Issue
#61 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [CSVダウンロードにBOM付きオプションを追加する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/321)

**作成者:** mtane0412  
**作成日:** 2025-04-17T10:21:24Z  
**変更:** +110 -42 (1ファイル)  
**マージ日:** 2025-04-17T16:09:46Z  
**内容:**

# 変更の概要
- CSVダウンロードボタンを押してCSVをダウンロードするのを、Popoverを表示して通常CSVとUTF-8 BOM (Byte Order Mark) 付きのCSVを選んでダウンロードできるようにした
- 通常のCSVは「CSV」で、BOM付きは「CSV for Excel (Windows)」とした
- UTF-8 BoM付きCSVは `original-name_excel.csv` のような形式でダウンロードする

![](https://i.gyazo.com/c900123a1fdd45ee8ced48243eba6aa4.png)

# 変更の背景
- WindowsユーザーがExcelを開くとBOM付きでないCSVは文字化けする問題がある
- 「UTF-8 BOM」という表記は非技術者に伝わりづらいため、CSV for Excel (Windows)と表現した。

# 関連Issue
#297

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [レポート作成日時にtimezoneをつけて保存](https://github.com/digitaldemocracy2030/kouchou-ai/pull/320)

**作成者:** nasuka  
**作成日:** 2025-04-17T05:05:34Z  
**変更:** +2 -2 (1ファイル)  
**マージ日:** 2025-04-17T16:58:40Z  
**内容:**

# 変更の概要
- レポート作成日時対してtimezone（UTC）つきで保存するように変更
  - これにより、レポートの一覧画面でJSTで作成日時が表示されるようになる（従来はUTCだった）
# 変更の背景
- 従来の保存形式ではtimezoneの情報が付加されていなかった
  - フロント側ではJSTに変換して日時を表示するようになっているが、保存されている元データにtimezoneの情報がないためUTCのまま表示されていた
    - 今回の実装のスコープにはしていないが、本来的にはJST固定ではなく閲覧しているブラウザの環境情報等からtimezoneを読み取った上で時刻表示するのが望ましい（現状日本以外ではそこまで使われないと思われるので対応していない）


注意点として、以前のバージョンで出力したレポートについては引き続きUTCのまま時刻が表示される。
（timezoneなしの作成日時が保存されている場合にtimezoneつきに変換する処理を入れれば対応可能ではあるが、実装が若干増えるのに対してインパクトが見合わないように思ったので対応していない）

# 関連Issue
Close https://github.com/digitaldemocracy2030/kouchou-ai/issues/317

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [ラベリングのデフォルトプロンプトをアップデート](https://github.com/digitaldemocracy2030/kouchou-ai/pull/319)

**作成者:** nasuka  
**作成日:** 2025-04-17T04:41:43Z  
**変更:** +25 -17 (2ファイル)  
**マージ日:** 2025-04-17T08:06:05Z  
**内容:**

# 変更の概要
* 初期ラベリング・統合ラベリングのプロンプトをアップデート
  * 従来のプロンプトは抽象的なタイトルがつけられがちだったので、より具体性のあるタイトルをつけるようにプロンプトをアップデート

新プロンプト・旧プロンプトの結果比較はこちら
https://docs.google.com/spreadsheets/d/1xjZ48M-haKk1y6znsuMeverotwAw-kBJjTtCcQ0qpP8/edit?gid=1478680723#gid=1478680723

# 変更の背景
* 広聴AIで出力した第一階層のクラスタタイトルが、TTTCのタイトルと比べて具体性に欠ているという声があった

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/269

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [レポート一覧のクリック可能範囲を広げる(#207)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/316)

**作成者:** mtane0412  
**作成日:** 2025-04-16T15:11:44Z  
**変更:** +56 -13 (1ファイル)  
**マージ日:** 2025-04-16T16:34:54Z  
**内容:**

# 変更の概要
- レポート一覧画面で各カードにマウスオーバーするとカードがグレーになり、中央に「レポートを表示」というボックスが表示される
- カード全体(既存のボタンを除く)をクリックするとレポートが開く
- 既存のレポートページへ飛ぶアイコンは削除

![](https://i.gyazo.com/f4b591f63332a0d3bc21741c95e6b581.jpg)

# 変更の背景
- 初見のユーザーがどこをクリックしていいか分からない問題があった
- マウスオーバー効果でクリッカブルであることが分からない層にも伝わるように「レポートを表示」を出すようにした
- 既存のレポート表示ボタンは重複するので削除した

# 関連Issue
#207 

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

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

### [Azureの更新のためのターゲットを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/215)

**作成者:** nishio  
**作成日:** 2025-04-01T08:25:51Z  
**変更:** +67 -18 (1ファイル)  
**マージ日:** 2025-04-17T14:50:50Z  
**内容:**

# 変更の背景
https://github.com/digitaldemocracy2030/kouchou-ai/issues/214

# 変更の概要
- Azureの更新のためのターゲットを追加


# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/214


# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### 過去7日間に作成されたPR (9件)

### [add ruff setting on .vscode/settings.json](https://github.com/digitaldemocracy2030/kouchou-ai/pull/354)

**作成者:** nishio  
**作成日:** 2025-04-21T17:55:52Z  
**変更:** +12 -1 (1ファイル)  
**内容:**

# 変更の背景/概要
- Biomeの設定は書かれているがRuffの設定は書かれていない、書いたほうがいい？

# 関連Issue
関連するIssueのリンクをこちらに記載してください

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [[REFACTOR] langchainの依存を削除する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/353)

**作成者:** nishio  
**作成日:** 2025-04-21T17:52:06Z  
**変更:** +20 -16 (4ファイル)  
**内容:**

## 変更内容

- `server/broadlistening/pipeline/services/llm.py`: langchainのOpenAIEmbeddingsを直接OpenAI SDKの呼び出しに置き換え
- `server/broadlistening/pipeline/utils.py`: langchainのメッセージスキーマを直接OpenAI SDKの形式に置き換え
- `server/pyproject.toml`: langchain関連の依存関係を削除

## 関連Issue

Closes #58

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [LLM出力形式の揺らぎによる抽出エラーの修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/352)

**作成者:** nishio  
**作成日:** 2025-04-21T17:21:42Z  
**変更:** +84 -13 (4ファイル)  
**内容:**

# LLM出力形式の揺らぎによる抽出エラーの修正

## 問題点
LLMからの応答が、プロンプトで期待した形式（例：文字列リスト `[str]`）と異なる形式（例：オブジェクトリスト `[{意見:"str", トピック:"str"}]`）で返ってくることがあり、データ抽出が失敗したり、抽出される意見数が少なくなったりする問題を修正しました。

## 修正内容
1. **プロンプトの改善**：
   - 出力形式をより明確に指定するようプロンプトを更新
   - 期待される出力形式の例をより詳細に提示

2. **構造化出力の活用**：
   - is_json=Trueオプションを使用して、JSON形式の応答を強制

3. **エラーハンドリングの強化**：
   - 異なる形式の応答にも対応できるよう、パース処理を改善
   - オブジェクトリスト形式からの文字列抽出ロジックを追加
  

# 関連Issue
- #296

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [client-admin/app/create/page.tsx のリファクタリング](https://github.com/digitaldemocracy2030/kouchou-ai/pull/351)

**作成者:** mtane0412  
**作成日:** 2025-04-21T15:56:09Z  
**変更:** +1485 -1110 (18ファイル)  
**内容:**

# 変更の概要

このPRでは、レポート生成ページ（client-admin/app/create/page.tsx）のリファクタリングを行いました。今後の機能追加や保守性を考慮し、コードの可読性と保守性を向上させることを目的としています。

## 1. 状態管理の整理
関連する状態を各カスタムフックにまとめました
- useBasicInfo: 基本情報（タイトル、調査概要、ID）
- useInputData: 入力データ（CSVファイル、スプレッドシート）
- useAISettings: AIモデル設定（モデル、並列実行数、出力モード）
- useClusterSettings: クラスタ設定
- usePromptSettings: プロンプト設定

## 2. コンポーネントの分割
UIを独立したコンポーネントに分割しました
- BasicInfoSection: 基本情報入力セクション
- AISettingsSection: AI詳細設定セクション
- WarningSection: 警告メッセージセクション
- ClusterSettingsSection: クラスタ設定セクション
- CommentColumnSelector: コメントカラム選択コンポーネント
- CsvFileTab: CSVファイル入力タブ
- SpreadsheetTab: スプレッドシート入力タブ

## 3. ロジックの分離
ビジネスロジックをUIから分離しました
- api/report.ts: レポート作成API
- api/spreadsheet.ts: スプレッドシートAPI
- utils/validation.ts: バリデーション関数
- utils/error-handler.ts: エラーハンドリング関数

## 4. 型定義の整理
型定義を types/index.ts にまとめました

# 変更の背景
- client-admin/app/create/page.tsxが1200行を超えており、LLMが読むのに苦労していた

# 関連Issue
#350

# その他

Rooで別のに取り掛かっていたら読み込みに相当苦労していたので一旦リファクタリングさせてみました。
Next.jsのベストプラクティス的な知識は弱いので、お手数ですが確認よろしくお願いします。
あとテスト方法もよくわかっておらず、手動でCSVとかを試して確認しているくらいです。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [REVALIDATE周りの設定をAzureのセットアップスクリプトに追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/338)

**作成者:** nasuka  
**作成日:** 2025-04-19T05:36:24Z  
**変更:** +12 -1 (1ファイル)  
**内容:**

# 変更の概要
* REVALIDATE_URLをcliで取得し、環境変数にセットした上でアップデートをかけるように修正
* .envにREVALIDATE_SECRETが存在しない場合は `azure-update-deployment` を実施しないよう修正

# 変更の背景

上記の実装に伴って、AzureのセットアップスクリプトでREVALIDATE周りの修正が必要
このPRは、https://github.com/digitaldemocracy2030/kouchou-ai/pull/336 と同時にmergeを行う

# 関連Issue
https://github.com/digitaldemocracy2030/kouchou-ai/issues/328

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [レポート一覧からタイトルと調査概要を変更可能にする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/336)

**作成者:** mtane0412  
**作成日:** 2025-04-18T11:54:54Z  
**変更:** +332 -4 (7ファイル)  
**内容:**

# 変更の概要
- レポート編集機能の追加
  - 管理画面でレポートのタイトルと説明文を編集できる機能を実装
  - 編集用のダイアログUIを追加
  - 更新成功時のトースト通知を実装
- バックエンド側の対応
  - レポートメタデータ更新用のAPIエンドポイントを追加 (/admin/reports/{slug}/metadata)
  - メタデータ更新用のスキーマ ReportMetadataUpdate を追加
  - レポート情報を更新する処理 update_report_metadata 関数を実装
  
 ![](https://i.gyazo.com/0cfb203326cdda1f11289dd5b048eb09.gif)

# 変更の背景
- 最初に設定したタイトルや調査概要を変更することができなかった

# 関連Issue
#328

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [第1階層の意見グループ数の上限を 20 -> 40に増加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/334)

**作成者:** nasuka  
**作成日:** 2025-04-18T08:42:15Z  
**変更:** +3 -3 (1ファイル)  
**内容:**

# 変更の概要
- 第1階層の意見グループ数の上限を 20 -> 40に増やした

# 変更の背景
* 現在、全体図などの散布図において意見グループの個数上限は20となっている
  * ラベルが重なってしまう問題があったため上限を20にしていたが、この問題は回避策のPR（ https://github.com/digitaldemocracy2030/kouchou-ai/pull/329 ）が出されている

# 備考
 https://github.com/digitaldemocracy2030/kouchou-ai/pull/329 がmergeされた後にmergeする
特に論点ないと思われるので、self mergeします

# 関連Issue
close https://github.com/digitaldemocracy2030/kouchou-ai/issues/330

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

**コメント:** なし

---

### [OpenAI API Rate Limit対策の実装](https://github.com/digitaldemocracy2030/kouchou-ai/pull/331)

**作成者:** nsk.smn+Devin  
**作成日:** 2025-04-18T06:00:08Z  
**変更:** +395 -26 (2ファイル)  
**内容:**

# OpenAI API Rate Limit対策の実装

## 概要
Issue #295 に記載されている問題を解決するため、OpenAI APIのRate Limit (429) エラーに対して指数バックオフ付きリトライ処理を実装しました。

## 変更内容
- tenacityライブラリを使用して、OpenAI APIのRate Limit (429) エラーに対する指数バックオフ付きリトライ処理を実装
- `request_to_openai`と`request_to_azure_chatcompletion`関数に対してリトライデコレータを追加
- エラー発生時のログ出力を追加
- リトライ設定：
  - 最大3回のリトライ
  - 指数バックオフ（初期2秒、最大60秒）
  - RateLimitErrorとAPIStatusErrorに対してリトライ

## テスト
- 実装後の動作確認を行いました

Link to Devin run: https://app.devin.ai/sessions/67c2a06784d74e068af3a03c787f2394
Requested by: nsk.smn@gmail.com


**コメント:** なし

---

### [静的ファイルエクスポート機能の追加 (#220)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/309)

**作成者:** nsk.smn+Devin  
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

### 過去7日間に更新されたPR（作成・マージを除く）(1件)

### [Windows環境でのセットアップ簡素化 (Issue #300)](https://github.com/digitaldemocracy2030/kouchou-ai/pull/301)

**作成者:** nishio  
**作成日:** 2025-04-13T04:02:24Z  
**変更:** +98 -0 (2ファイル)  
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

