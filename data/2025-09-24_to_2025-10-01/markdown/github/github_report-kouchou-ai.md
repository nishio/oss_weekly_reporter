# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-09-24T12:26:54.436632+09:00 から 2025-10-01T12:26:54.436632+09:00 まで

## Issues

### 過去7日間に完了されたissue (6件)

### [[BUG]client の開発環境がうまく動かない](https://github.com/digitaldemocracy2030/kouchou-ai/issues/712)

**作成者:** rolzy  
**作成日:** 2025-09-25T21:27:23Z  
**内容:**

### 概要
`README.md` の "[client の開発環境の構築手順](https://github.com/digitaldemocracy2030/kouchou-ai?tab=readme-ov-file#client-%E3%81%AE%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83%E3%81%AE%E6%A7%8B%E7%AF%89%E6%89%8B%E9%A0%86)" で構築されるフロントエンドアプリがエラーを吐いてしまう。


### 再現手順
1. レポジトリのmainブランチをクローン
2. `make client-setup && make client-dev -j 3`
3. localhost:3000 及び localhost:4000 を開く

### 期待する動作
`make client-setup && make client-dev -j 3` したらフロントエンドが動く


### スクリーンショット・ログ

**client (localhost:3000)**

<img width="966" height="779" alt="Image" src="https://github.com/user-attachments/assets/64ac61f2-1e52-465a-9ac3-c0fefbb2c5f1" />

```
TypeError: Invalid URL

components/reporter/Reporter.tsx (9:15) @ hasReporterImage

   7 |
   8 | async function hasReporterImage() {
>  9 |   const url = new URL(imagePath, process.env.API_BASEPATH).toString();
     |               ^
  10 |   try {
  11 |     const res = await fetch(url);
  12 |     return res.status === 200;
```

**client-admin (localhost:4000)**

<img width="964" height="845" alt="Image" src="https://github.com/user-attachments/assets/4c442541-20f8-4f23-ac68-16623c5b4bb2" />

```
Error: can't access property "commentNum", report.analysis is undefined

app/_components/ReportCard/ReportCard.tsx (53:30) @ ReportDataAndActions

  51 |             </GridItem>
  52 |             <GridItem>
> 53 |               <NumberDisplay value={report.analysis.commentNum} />
     |                              ^
  54 |             </GridItem>
  55 |             <GridItem>
  56 |               <NumberDisplay value={report.analysis.argumentsNum} />
```

### その他
**client** エラーについて
- `API_BASEPATH`環境変数が`make`だと設定されないっぽいです
- `client/.env` に`NEXT_PUBLIC_API_BASEPATH`が設定されてるので、それを読み込むor`API_BASEPATH`変数を別で定義する必要がありそう

**client-admin** エラーについて
- dummyデータの値やタイプがコードが求めてるものとちょっと違うみたいです。
- client側でchainingしたりデフォの値を定義することで改善できそう
- dummyデータの値も直したほうが良い

**コメント:** なし

---

### [[REFACTOR] client: lint error が出ている](https://github.com/digitaldemocracy2030/kouchou-ai/issues/701)

**作成者:** shingo-ohki  
**作成日:** 2025-09-10T07:50:13Z  
**内容:**

# 現在の問題点
<!-- 現在のコードの何が問題なのか、どのような技術的負債があるかを説明してください -->

client で `npm run lint` を実行すると以下のようなエラーが出ている
```
% cd client && npm run lint

> kouchou-ai-client@0.1.0 lint
> biome check .

./app/layout.tsx format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✖ Formatter would have printed the following content:
  
    14 14 │           <link rel="preconnect" href="https://fonts.googleapis.com" />
    15 15 │           <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
    16    │ - ········<link
    17    │ - ··········href="https://fonts.googleapis.com/css2?family=BIZ+UDPGothic&display=swap"
    18    │ - ··········rel="stylesheet"
    19    │ - ········/>
       16 │ + ········<link·href="https://fonts.googleapis.com/css2?family=BIZ+UDPGothic&display=swap"·rel="stylesheet"·/>
    20 17 │   
    21 18 │           <link rel={"icon"} href={getImageFromServerSrc("/meta/icon.png")} sizes={"any"} />
  

./components/Header.tsx format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✖ Formatter would have printed the following content:
  
     7  7 │     const logoSrc = useBreakpointValue({
     8  8 │       base: "/images/logo-sp.svg",
     9    │ - ····md:·"/images/logo.svg"
        9 │ + ····md:·"/images/logo.svg",
    10 10 │     });
    11 11 │   
    12 12 │     return (
    13 13 │       <HStack justify="space-between" py="5" mb={8} mx={"auto"} maxW={"1200px"}>
    14    │ - ······<Image
    15    │ - ········src={logoSrc}
    16    │ - ········alt="広聴AI"
    17    │ - ······/>
       14 │ + ······<Image·src={logoSrc}·alt="広聴AI"·/>
    18 15 │         <BroadlisteningGuide />
    19 16 │       </HStack>
  

./components/charts/ScatterChart.tsx:247:71 lint/style/noUnusedTemplateLiteral  FIXABLE  ━━━━━━━━━━━

  ✖ Do not use template literals if interpolation and special-character handling are not needed.
  
    245 │             text: matching.map((arg) => {
    246 │               const argumentText = arg.argument.replace(/(.{30})/g, "$1<br />");
  > 247 │               const urlText = config?.enable_source_link && arg.url ? `<br><b>🔗 クリックしてソースを見る</b>` : "";
        │                                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    248 │               return `<b>${cluster.label}</b><br>${argumentText}${urlText}`;
    249 │             }),
  
  ℹ Unsafe fix: Replace with string literal
  
    245 245 │               text: matching.map((arg) => {
    246 246 │                 const argumentText = arg.argument.replace(/(.{30})/g, "$1<br />");
    247     │ - ··············const·urlText·=·config?.enable_source_link·&&·arg.url·?·`<br><b>🔗·クリックしてソースを見る</b>`·:·"";
        247 │ + ··············const·urlText·=·config?.enable_source_link·&&·arg.url·?·"<br><b>🔗·クリックしてソースを見る</b>"·:·"";
    248 248 │                 return `<b>${cluster.label}</b><br>${argumentText}${urlText}`;
    249 249 │               }),
  

./components/charts/ScatterChart.tsx:391:27 lint/suspicious/noExplicitAny ━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✖ Unexpected any. Specify a different type.
  
    389 │           onHover={onHover}
    390 │           onUpdate={onUpdate}
  > 391 │           onClick={(data: any) => {
        │                           ^^^
    392 │             if (!config?.enable_source_link) return;
    393 │ 
  
  ℹ any disables many type checking rules. Its use should be avoided.
  

./components/theme/fonts.ts format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✖ Formatter would have printed the following content:
  
    1   │ - const·fontFamily·=·'"BIZ·UDPGothic",·"Hiragino·Kaku·Gothic·ProN",·Meiryo,·sans-serif'
      1 │ + const·fontFamily·=·'"BIZ·UDPGothic",·"Hiragino·Kaku·Gothic·ProN",·Meiryo,·sans-serif';
    2 2 │   
    3 3 │   export const fonts = {
    4 4 │     main: { value: fontFamily },
    5   │ - }
      5 │ + };
    6 6 │   
  

./components/theme/recipe/link.ts format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✖ Formatter would have printed the following content:
  
    24 24 │             opacity: 0.75,
    25 25 │             textDecoration: "none",
    26    │ - ········}
       26 │ + ········},
    27 27 │         },
    28 28 │       },
    ····· │ 
    32 32 │       variant: "underline",
    33 33 │     },
    34    │ - })
       34 │ + });
    35 35 │   
  

Checked 71 files in 30ms. No fixes applied.
Found 6 errors.
check ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✖ Some errors were emitted while running checks.
```

**コメント:** なし

---

### [[BUG] main へマージ時に DD2030 の azure 環境へのデプロイが失敗する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/682)

**作成者:** shingo-ohki  
**作成日:** 2025-07-29T01:36:13Z  
**内容:**

### 概要

https://github.com/digitaldemocracy2030/kouchou-ai/pull/642 で main にマージされるたびに DD2030 の Azure 環境に deploy されるようにしたがエラーが発生する

<!-- バグの簡潔な説明をお願いします -->

### 再現手順

1.  main ブランチにコードがマージされる

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->

### スクリーンショット・ログ
出力されているログ
https://github.com/digitaldemocracy2030/kouchou-ai/actions/runs/16584250059/job/46906413136

```
...
Error: The subscription of '79e8ef5-7461-407d-84b6-b4f37b9f31c1' doesn't exist in cloud 'AzureCloud'.

Error: Login failed with Error: The process '/usr/bin/az' failed with exit code 1. Double check if the 'auth-type' is correct. Refer to https://github.com/Azure/login#readme for more information.
```
<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->


**コメント:** なし

---

### [[FEATURE] Gemini を利用してレポート生成できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/634)

**作成者:** shingo-ohki  
**作成日:** 2025-07-04T13:15:56Z  
**内容:**

# 背景
#622, #633 に関連して、
Gemini であれば職員が自由に使えるようになっている自治体があり、この環境下で発行した Gemini の API Key がそのまま使えると活用が広がる

# 提案内容
OPENAI_API_KEY, OPENROUTER_API_KEY の他に GEMINI_API_KEY を指定してレポート生成ができるようにする

**コメント:** なし

---

### [[BUG] azure-build 時に警告が出る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/631)

**作成者:** shingo-ohki  
**作成日:** 2025-07-03T03:00:37Z  
**内容:**

### 概要

`azure-build` 時に警告が出る（build 自体は完了し、のちの `azure-config-update` で環境変数は設定されるので実質問題はない）

<!-- バグの簡潔な説明をお願いします -->

### 再現手順

1. [Azure 環境へのセットアップ方法](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/Azure.md) に従って設定し `make azure-build` を実行する

### 期待する動作

警告が出力されずに build が正常に完了する

<!-- 本来どう動作すべきかを記入してください -->

### スクリーンショット・ログ

`azure build` 時に以下のような警告が出ます。

```
>>> コンテナイメージのビルド...
...
 4 warnings found (use docker --debug to expand):
 - UndefinedVar: Usage of undefined variable '$NEXT_PUBLIC_API_BASEPATH' (line 20)
 - UndefinedVar: Usage of undefined variable '$NEXT_PUBLIC_PUBLIC_API_KEY' (line 21)
 - UndefinedVar: Usage of undefined variable '$NEXT_PUBLIC_SITE_URL' (line 22)
 - UndefinedVar: Usage of undefined variable '$API_BASEPATH' (line 23)
...
```

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

**コメント:** なし

---

### [[FEATURE]用語解説ページをつける](https://github.com/digitaldemocracy2030/kouchou-ai/issues/111)

**作成者:** nishio  
**作成日:** 2025-03-20T12:07:35Z  
**内容:**

# 背景
「プロンプト」「埋め込み」「濃い(クラスタ)」について、単語レベルで言い換えてもわかりやすくならない気がするので、やるとしたら用語解説ページをつけるとかかな

「縦軸・横軸はなんだろう」についても解説

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

**コメント:** なし

---

### 過去7日間に作成されたissue (1件)

### [[BUG]url情報のある散布図で点をクリックしてもリンク先にジャンプできない現象](https://github.com/digitaldemocracy2030/kouchou-ai/issues/710)

**作成者:** nishio  
**作成日:** 2025-09-24T08:36:35Z  
**内容:**

### 概要

url情報のある散布図で点をクリックしてもリンク先にジャンプできない

### 再現手順

1. url情報のある散布図で点をクリック 
2. 何も起きない

### 期待する動作

新しいタブでリンク先が開く


### その他

displayModeBar: "hover"を削除すれば筆者環境では直ったが、PRを作成する上での再現性が微妙なので他の人の環境で再現するまで保留中
https://github.com/digitaldemocracy2030/kouchou-ai/blob/40d228c8f791d269fd69eae7aed33320c0f241d9/client/components/charts/ScatterChart.tsx#L385

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(3件)

### [Docker build時のシークレット渡し方法の改善](https://github.com/digitaldemocracy2030/kouchou-ai/issues/643)

**作成者:** coderabbitai[bot]  
**作成日:** 2025-07-09T02:10:10Z  
**内容:**

## 概要

現在、GitHub Actions の Azure デプロイワークフローにて、`docker build --build-arg` を使用してシークレット値（API キー、パスワード等）を渡しています。

## 現状の実装
- `.github/workflows/azure-deploy.yml` にて `PUBLIC_API_KEY`, `ADMIN_API_KEY`, `BASIC_AUTH_PASSWORD` 等を `--build-arg` で渡している
- 現在はプライベートレジストリ（ACR）への push のみで外部配布は行っていない
- Dockerfile 内でシークレット値の出力処理は行っていない

## 改善提案
将来的なセキュリティ強化として、以下の方法への移行を検討：
- Docker BuildKit の `--secret` 機能の活用
- `az acr build --secret-arg` の利用
- シークレット情報のビルドログへの露出防止

## 関連情報
- PR: https://github.com/digitaldemocracy2030/kouchou-ai/pull/642
- コメント: https://github.com/digitaldemocracy2030/kouchou-ai/pull/642#discussion_r2193711408
- 提起者: @shingo-ohki

## 優先度
現在の運用リスクは限定的であるため、将来的な改善項目として位置づけ

**コメント:** なし

---

### [[FEATURE] Azure に動作確認環境・デモ環境を作る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/622)

**作成者:** shingo-ohki  
**作成日:** 2025-06-29T08:25:09Z  
**内容:**

# 背景
- 現状、新しい機能の開発やソフトウェア改善を行った場合の動作確認は、エンジニアの手元の開発環境で行っているが、UI/UX の改善を行う際などはデザイナーなどエンジニア以外の方にも確認してもらいたいがその環境がない
- ユーザーが広聴AIを試すには環境構築をする必要があるが、これは多少のエンジニアリングスキルを必要とするため、簡単に試すことができない

<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->


# 提案内容
上記を解決するために、dd2030 が管理する Azure 環境に常に広聴AIがデプロイされているような環境を用意する

<!-- 実装案やデザイン案があれば記入してください -->

- 動作確認環境
  - [x] Azure 環境にセットアップする
  - [x]  #642 
  - [x] #688 
- デモ環境
  - [x] #633
  - [ ] client-admin のパスワードなしでアクセスできるようにする
  - [ ] dd2030.org ドメインでアクセスできるようにする

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

## Pull Requests

### 過去7日間にマージされたPR (10件)

### [client開発環境が正しく動くように修正](https://github.com/digitaldemocracy2030/kouchou-ai/pull/713)

**作成者:** rolzy  
**作成日:** 2025-09-25T21:47:01Z  
**変更:** +13 -7 (4ファイル)  
**マージ日:** 2025-09-26T03:46:01Z  
**内容:**

# 変更の概要
`README.md` の "[client の開発環境の構築手順](https://github.com/digitaldemocracy2030/kouchou-ai?tab=readme-ov-file#client-%E3%81%AE%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83%E3%81%AE%E6%A7%8B%E7%AF%89%E6%89%8B%E9%A0%86)" が正しく動くように修正しました。

**client**
- `client/entrypoint.sh` と同様に `API_BASEURL` 環境変数を `client/.env.sample` に追加

**client-admin**
- dummy APIからのデータが不完全だったので、不完全データに対応できるよう変更
    - Optinal Chainingで `report.analysis` があるかどうか確認、ない場合はレポートの コメント/意見/意見グループが`-`と表示される
    - レポートのデフォルト公開設定を`private` に変更 

必要であれば dummy dataも更新します

# 変更の背景
- clientの開発環境を構築しようとしたら予期せぬエラーがあったので修正

# 関連Issue
#712 

# 動作確認の結果
デフォルト値が設定されたdummy dataレポート
<img width="1067" height="370" alt="image" src="https://github.com/user-attachments/assets/453c4c26-c69f-4565-bb0b-ea9c317e7d16" />

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

- バグ修正
  - NumberDisplay が未定義の値を受け取り「-」を表示。大きな数値のフォーマットは従来どおり。
  - ReportCard の分析値取得をオプショナルチェイニング化し、analysis 未定義でもランタイムエラーを防止。
  - 可視性アイコンは未設定時に private を既定値として表示し、表示不整合を回避。

- ドキュメント
  - client/.env-sample に API_BASEPATH を追加し、ローカル設定例を明確化。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Azure Blob Storage への接続と基本アップロードを検証するテストツールを追加 -](https://github.com/digitaldemocracy2030/kouchou-ai/pull/711)

**作成者:** nishio  
**作成日:** 2025-09-25T07:00:51Z  
**変更:** +104 -0 (1ファイル)  
**マージ日:** 2025-09-26T03:12:06Z  
**内容:**


- Azure Blob Storage への接続と基本アップロードを検証するテストツールを追加
- 目的: Azure Blob Storageの設定が正しいかどうかを検証する方法が、ブラウザを操作してCSVからレポートを作成することでは検証しづらいため、手軽な手段を追加した


# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）]
- [x] CLAの内容を読み、同意しました


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- 新機能
  - クラウドストレージへの接続確認と簡易アップロードを行う検証用スクリプトを追加。結果の成功/失敗を表示し、一時ファイルを自動クリーンアップ。例外時は詳細なエラー情報を出力。
- ドキュメント
  - 利用手順、必要な環境変数の概要、ローカル実行とクラウド実行時の注意点を追記。
- 雑務
  - 環境変数ベースの設定読込に対応し、ストレージサービスの初期化からアップロード、結果報告までのフローを整備。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [Fix hardcoded image paths for GitHub Pages subpath hosting](https://github.com/digitaldemocracy2030/kouchou-ai/pull/709)

**作成者:** NISHIO+Devin  
**作成日:** 2025-09-24T03:15:52Z  
**変更:** +14 -14 (3ファイル)  
**マージ日:** 2025-09-24T11:30:46Z  
**内容:**

# 変更の概要
- Footer.tsx とReporter.tsx のハードコードされた画像パスを `getImageFromServerSrc()` ユーティリティ関数を使用するように修正
- GitHub Pagesのサブパスホスティング（`https://username.github.io/repository-name/`）で画像が正しく表示されるようにベースパス対応を実装

# 変更の背景
GitHub Pagesでサブパスホスティングを行う際に `NEXT_PUBLIC_STATIC_EXPORT_BASE_PATH` を設定すると、ハードコードされた画像パス（`/images/...`）がリンク切れになる問題があった。既存の `getImageFromServerSrc()` ユーティリティ関数を使用することで、静的エクスポート時に適切なベースパスを自動で付与するように修正。

# 関連Issue
docs/github-pages-hosting.md で言及されている静的HTMLエクスポートでの画像パス問題の解決

# 動作確認の結果
<!-- 実装者による動作確認は未実施。レビュアーによる以下の確認をお願いします：
1. 開発環境での画像表示確認
2. NEXT_PUBLIC_STATIC_EXPORT_BASE_PATH設定時の静的エクスポートでの画像表示確認
3. フッターの背景画像、ロゴ画像、レポーター画像が正しく表示されることの確認 -->

**⚠️ 重要**: 実装者による動作確認が未実施のため、レビュアーによる徹底的な動作確認が必要です。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] **重要**: 開発環境でフッターとレポーターの画像が正常に表示されることを確認
- [ ] **重要**: `NEXT_PUBLIC_STATIC_EXPORT_BASE_PATH` 設定時の静的エクスポートで画像が正常に表示されることを確認
- [ ] CSS background-imageの構文が正しく動作することを確認
- [ ] `getImageFromServerSrc()` が削除された `reporterImageSrc()` の機能を適切に代替していることを確認

---

**Link to Devin run**: https://app.devin.ai/sessions/dab70bfbb4914f05a4c7ffe77f385e59
**Requested by**: @nishio

**コメント:** なし

---

### [Improve Azure OpenAI setup experience with better error handling](https://github.com/digitaldemocracy2030/kouchou-ai/pull/708)

**作成者:** NISHIO+Devin  
**作成日:** 2025-09-22T13:06:56Z  
**変更:** +154 -73 (9ファイル)  
**マージ日:** 2025-09-24T13:25:12Z  
**内容:**

# 変更の概要
- Azure OpenAI設定時の環境変数不足に対する明確なエラーメッセージを追加
- 管理者向け検証エンドポイントをAzureプロバイダーに対応
- `.env.example`の説明を改善し、正しい環境変数名を強調
- フロントエンド検証機能をAzureプロバイダーテストに対応
- 新しい検証機能の包括的なテストを追加

# 変更の背景
ユーザーがAzure OpenAI設定時に直感的な`AZURE_OPENAI_*`環境変数を設定したが、コードが期待する`AZURE_CHATCOMPLETION_*`変数名との不一致により「result is empty, maybe bad prompt」という分かりにくいエラーが発生していた問題を解決する。

現在のエラーハンドリングでは、Azure OpenAIクライアントがNone値で初期化され、API呼び出し時に下流で混乱を招くエラーが発生していた。

# 関連Issue
Slackでの報告: https://dd2030.slack.com/archives/C08PRQVQWSE/p1757662904699399

# 動作確認の結果
- Azure環境変数が未設定の場合に適切なエラーメッセージが表示されることを確認
- 既存のAzure設定が正しく動作することを確認  
- 新しいプロバイダーパラメータ付きの検証エンドポイントが動作することを確認
- 全てのLLMサービステスト（26件）が通過することを確認
- Lintチェックが通過することを確認

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 環境変数検証ロジックが既存の正常な設定を破損させないことを確認
- [ ] 管理者APIエンドポイントの後方互換性を確認（デフォルトパラメータが適切に動作）
- [ ] エラーメッセージが正確で有用であることを確認
- [ ] Azure環境変数が未設定の場合に新しい検証が適切に動作することを確認

---

**Link to Devin run**: https://app.devin.ai/sessions/2121b3d2b8f3434aa13845a45ea9d11c  
**Requested by**: @nishio

**重要な確認ポイント**:
1. **環境変数検証の安全性**: 新しい検証ロジックが既存の動作中の設定を破損させないか
2. **API後方互換性**: `provider`パラメータの追加が既存の呼び出しに影響しないか  
3. **エラーメッセージの正確性**: 表示される環境変数名と実際に必要な変数名が一致しているか

**コメント:** なし

---

### [[REFACTOR] client: lint error が出ている](https://github.com/digitaldemocracy2030/kouchou-ai/pull/706)

**作成者:** mochizuki-pg  
**作成日:** 2025-09-20T06:01:32Z  
**変更:** +26 -34 (5ファイル)  
**マージ日:** 2025-09-24T11:10:41Z  
**内容:**

# 変更の概要
https://github.com/digitaldemocracy2030/kouchou-ai/issues/701

# スクリーンショット
```bash
cd client && npm run lint           


> kouchou-ai-client@0.1.0 lint
> biome check .

Checked 72 files in 35ms. No fixes applied.
```

# 変更の背景
- ここに変更が必要となった背景を記載してください

# 関連Issue
関連するIssueのリンクをこちらに記載してください

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

### [[client] 用語解説ページとグローバルナビゲーションを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/699)

**作成者:** shgtkshruch  
**作成日:** 2025-09-08T12:23:20Z  
**変更:** +540 -56 (18ファイル)  
**マージ日:** 2025-09-24T14:08:22Z  
**内容:**

# 変更の概要
- 用語解説ページを追加しました
- ヘッダーにグローバルナビゲーションを追加しました
  - スマホとタブレット以上でスタイルの出し分けをしています

# スクリーンショット

## FAQ
<img width="999" height="591" alt="image" src="https://github.com/user-attachments/assets/bb8bcc67-4c71-495c-b830-6134fcd237ff" />


<img width="684" height="478" alt="image" src="https://github.com/user-attachments/assets/82c2af02-e6b5-4ab1-83b0-64f99ab3ec93" />

## お問い合わせ

### sm
<img width="554" height="593" alt="image" src="https://github.com/user-attachments/assets/fa90337d-cd7d-4b22-890a-20ba3509b15f" />


### lg
<img width="1085" height="386" alt="image" src="https://github.com/user-attachments/assets/f8f0979a-e3f1-4ef6-8a3a-2a84703043c2" />


# 変更の背景
- 「埋め込み」「濃いクラスタ」など初見で意味が取りずらい言葉があるので、解説ページを作りたい

# 関連Issue
- fix: #111 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- client でグローバルナビゲーションがスマホ・タブレット以上でそれぞれ表示されること
- 用語解説ページにアクセスして、Drawer で個別の FAQ を開閉して閲覧できること

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
  - FAQページ（アコーディオン式Q&A）とお問い合わせセクションを追加。Slackへ移動するボタンを搭載。
  - グローバルナビ導入（PC横並びナビ＋モバイル用ドロワー）およびヘッダー統合。
  - 新しいアイコンボタンUIコンポーネントを追加。

- **リファクタ**
  - 主要ページコンテナをBoxベースに置換し、ヘッダーをコンテナ外へ移動。

- **削除**
  - 既存のガイド表示機能を削除。

- **スタイル**
  - セマンティックトークンに背景・境界色グループを追加。アイコンボタン用スタイルレシピを導入。

- **改善**
  - ドロワーのクローズ操作を柔軟化。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[FEATURE] Gemini を利用してレポート生成できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/698)

**作成者:** AkioPonkotu  
**作成日:** 2025-09-03T15:42:51Z  
**変更:** +861 -137 (32ファイル)  
**マージ日:** 2025-09-24T11:25:03Z  
**内容:**

# 変更の概要
レポート作成でGemini を選択/使用可能にし、トークン使用量と推定料金を算出・表示できるようにした。

環境変数やセットアップドキュメントを更新し、新APIキーの設定方法を追加。
- server/broadlistening/pipeline/services/llm.py にGemini向けリクエスト処理を実装。
- server/src/services/llm_models.py でGeminiのモデル一覧取得に対応。
- server/src/services/llm_pricing.py にGeminiの料金テーブルとコスト計算ロジックを追加。
- server/src/config.py へ GEMINI_API_KEY を追加し、admin_report ルーターでトークン使用量と推定コストを返却。
- フロントエンド (client-admin/app/create/...) にプロバイダ・モデル選択UIを追加
- .env.example や各OS向けセットアップガイドをGemini API対応に更新。

# スクリーンショット
<img width="500" height="341" alt="image" src="https://github.com/user-attachments/assets/6f961243-e4e8-4145-8ddd-e7371c29f600" />

<img width="486" height="257" alt="image" src="https://github.com/user-attachments/assets/5afd6bf1-b9fc-4123-bf97-007135805bd8" />

# 変更の背景
レポート生成でGoogle GeminiAPIが使用できなかった。

# 関連Issue
[関連するIssueのリンクをこちらに記載してください](https://github.com/digitaldemocracy2030/kouchou-ai/issues/634)

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->
GeminiAPIのFreeTierで件数を削減したサンプルcsvでレポート作成を実行し、正常にレポートが作成されることを確認しました。

変更した設定値
AIプロバイダー:Gemini
並列実行数:1
AIモデル:Gemini 2.5 Flash

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

- 新機能
  - Google Gemini プロバイダーを追加（チャット/埋め込み対応、モデル選択に Gemini 追加、料金計算対応）。UI から Gemini と各モデルを選択可能。環境変数 GEMINI_API_KEY に対応。
- ドキュメント
  - 各 OS 向けセットアップ、サーバー README を更新。Gemini API キーの取得/設定、プロンプト、アクセス URL、トラブルシュートを追記。
- テスト
  - Gemini 向けのチャット/埋め込み/料金計算テストを追加。
- チョア
  - セットアップスクリプトと .env サンプルに GEMINI_API_KEY を追加。依存に Gemini クライアントを追加。ログ出力レベルを調整。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix: Azure Deploy 時に client コンテナの環境変数が未設定になる](https://github.com/digitaldemocracy2030/kouchou-ai/pull/688)

**作成者:** shingo-ohki  
**作成日:** 2025-08-04T04:59:19Z  
**変更:** +61 -16 (1ファイル)  
**マージ日:** 2025-09-24T13:39:50Z  
**内容:**

# 変更の概要
- Azure デプロイ時のコンテナの環境変数の設定に不足があったため、これを修正します 
- Azure のコンテナ更新と環境変数の設定は同時に行うようにします

# 変更の背景
- #642 で azure へ deploy するワークフローを追加したが不十分な箇所があった

# 関連Issue
#682 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

一時的にフォークしたリポジトリからワークフローを実行できるようにし、[こちら](https://github.com/digitaldemocracy2030/kouchou-ai/issues/682#issuecomment-3149067334)の問題が解消していることを確認しました。
Github Actions のワークフローログ
https://github.com/shingo-ohki/kouchou-ai/actions/runs/16715007751

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



## Summary by CodeRabbit

* **Chores**
  * デプロイワークフローを更新し、すべてのコンテナ（api、client、client-admin、client-static-build）のシークレット登録と環境変数設定を並列で実行するよう改善しました。これによりデプロイの効率と安定性が向上します。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [fix: make azure-build 時に警告が出る](https://github.com/digitaldemocracy2030/kouchou-ai/pull/632)

**作成者:** shingo-ohki  
**作成日:** 2025-07-03T03:14:26Z  
**変更:** +48 -10 (4ファイル)  
**マージ日:** 2025-09-24T13:45:15Z  
**内容:**

# 変更の概要
- `make azure-build`時に警告が出ないようにします
-  `.env.example` の環境変数の指定フォーマットにブレがあったので、`（") 二重引用符なし` に統一しました

# 関連Issue
#631 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

make azure-build 時に、以下のような警告が出ないこと、build が正常に行われることを確認しました。
```
 4 warnings found (use docker --debug to expand):
 - UndefinedVar: Usage of undefined variable '$NEXT_PUBLIC_API_BASEPATH' (line 20)
 - UndefinedVar: Usage of undefined variable '$NEXT_PUBLIC_PUBLIC_API_KEY' (line 21)
 - UndefinedVar: Usage of undefined variable '$NEXT_PUBLIC_SITE_URL' (line 22)
 - UndefinedVar: Usage of undefined variable '$API_BASEPATH' (line 23)
 ```
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

* **新機能**
  * Dockerイメージのビルド時に追加の環境変数／ビルド引数が反映されるようになりました（ビルド結果に必要な設定が確実に渡されます）。

* **スタイル**
  * .env.example の URL 値から二重引用符を削除しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [レポートのバックアップスクリプトを docker 環境で実行する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/630)

**作成者:** shingo-ohki  
**作成日:** 2025-07-03T01:52:51Z  
**変更:** +7 -1 (1ファイル)  
**マージ日:** 2025-09-24T13:47:35Z  
**内容:**

# 変更の概要
- `make azure-update-deployment` 実行時に実行環境を整える必要がないように、docker 環境で実行するように修正しました

# 変更の背景
- #622 の作業時に、そのままではローカル環境を整える必要があることに気がつきました

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

修正後の Makefile で、`make azure-update-deployment` を実行した際に適切にレポートのバックアップスクリプトが動作することを確認しました。

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

* **Chores**
  * Pythonスクリプトの実行をホスト上からコンテナ内に移行し、ランタイム依存の自動インストールと環境ファイルの読み込みを追加して実行環境を分離・安定化しました。APIエンドポイント等の引数はコンテナ起動時に引き継がれます。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(2件)

### [Feature/issue 493 レポート画面のスクロールイベント回避を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/597)

**作成者:** dentaro  
**作成日:** 2025-06-09T12:11:47Z  
**変更:** +141 -161 (2ファイル)  
**内容:**

# 変更の概要
client/components/chart.tsx
図の上にオーバーレイをかけることにより、レポートページを見ようとスクロールしても図が拡大縮小されないようにした。
1秒で自動解除。図内を出ると自動1秒でオーバーレイ復帰。
図の描画速度を向上させた。

# スクリーンショット
![image](https://github.com/user-attachments/assets/5d8d4190-239c-484b-bad0-3c2e8e81be15)
![image](https://github.com/user-attachments/assets/507f3cbc-2e45-4152-bf79-80e7c993bfdb)

# 変更の背景
ScatterChartの領域でスクロールで拡大縮小できるようになった。
このことにより「レポートページを見るためにスクロールする→図が拡大/縮小される」というユーザーが意図しない動作がほぼ発生する。何らかの方法でユーザー操作を直感的にする必要がある。

# 関連Issue
[FEATURE] レポートページを見ようとスクロールすると図が拡大縮小される #493

# 動作確認の結果
「親画面が一定時間（1秒）スクロールしていないこと」を拡大縮小のトリガーにする
親画面スクロール中にScatterChartにマウスオーバーしたら半透明のグレーのパネル（=操作無効）をChartに被せ、そのままスクロールで通り過ぎられるようにした
図内に入るとクリックしなくてもオーバーレイが解除される
意図しないスクロールによる拡大縮小を、オーバーレイのオン状態の時にキャンセルしている

以下の既存のエラー、警告は維持されているので、別のissueで対応すべき
・No label associated with a form field
・mg タグ、video タグ、canvas タグに overflow: visible を指定すると、要素の境界外にビジュアル コンテンツが作成される場合があります。https://github.com/WICG/shared-element-transitions/blob/main/debugging_overflow_on_images.md をご覧ください。

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）]
- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [] CIが全て通過している
- [] 単体テストが実装されているか
- [] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

- **ドキュメント**
  - READMEに「Windowsからプッシュ！！」という一文を追加しました。

- **リファクタ**
  - チャートのフィルタリング処理を効率化し、メモ化によるパフォーマンス向上を行いました。
  - チャートの描画ロジックを整理し、共通プロパティの管理を簡素化しました。

- **新機能**
  - チャート上にインタラクティブなオーバーレイを追加し、意図しない操作を防止できるようになりました。

- **スタイル**
  - フルスクリーンボタンやオーバーレイの表示位置・見た目を微調整しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [アドミン管理画面でリロードを抑制する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/543)

**作成者:** tokoroten  
**作成日:** 2025-05-19T14:34:06Z  
**変更:** +37 -22 (1ファイル)  
**内容:**

# 変更の概要
- 現在の管理画面では、完了やエラーになった項目も、何度もリロードしている
- フロントの判定を変えて、リロードを抑制する

# スクリーンショット

# 変更の背景
- 管理画面のリロードがひどくて、サーバのログが流れてしまって

# 関連Issue

# 動作確認の結果
処理中のレポートのみがリロードされていることを確認した。

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

- **バグ修正**
  - 完了またはエラー状態のレポートに対して不要なポーリングが行われないようになりました。
  - レポートの進捗が変化した際、ステータス更新が一度だけ行われるよう改善されました。
  - 完了やエラー時にページが自動リロードされなくなりました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

