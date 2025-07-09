# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-07-02T12:33:22.889207+09:00 から 2025-07-09T12:33:22.889207+09:00 まで

## Issues

### 過去7日間に完了されたissue (1件)

### [[FEATURE] 管理画面のレポート一覧でコメント数などを取得できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/635)

**作成者:** shgtkshruch  
**作成日:** 2025-07-05T07:49:04Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

- https://github.com/digitaldemocracy2030/kouchou-ai/issues/460 の管理画面のリデザインで、各レポートごとに以下の情報を表示したい
  - コメント数
  - 意見数
  - 意見グループ数

<img width="1047" height="286" alt="Image" src="https://github.com/user-attachments/assets/f1e12431-f94d-49d8-8137-6c93b4677c17" />

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

- 管理画面のレポート一覧を取得するエンドポイント内の処理で、上記のデータを合わせて取得してフロントエンドに返す
https://github.com/digitaldemocracy2030/kouchou-ai/blob/14b71d79b243315ecd299cb980865522e24e2076/server/src/routers/admin_report.py#L41-L43


**コメント:** なし

---

### 過去7日間に作成されたissue (9件)

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

### [[FEATURE]レポートが完成したときに通知する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/641)

**作成者:** nishio  
**作成日:** 2025-07-08T09:12:28Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
レポートが完成したら教えて欲しい時がある

# 提案内容
下記はMac環境では期待通り動く
Windowsでも動くようにするのは通知の部分がOS依存で厄介

```python
#!/usr/bin/env python3
"""
Simple script to check if any reports are currently processing
"""

import argparse
import os
import subprocess
import time

import dotenv
import requests

# Load environment variables from .env file
dotenv.load_dotenv()


def check_processing_status():
    """Check if any reports are currently processing"""

    # Get API key
    api_key = os.getenv("ADMIN_API_KEY")
    api_url = os.getenv("ADMIN_API_URL")  # https://api.<domain>/admin/reports
    if not api_key:
        print("Error: ADMIN_API_KEY environment variable required")
        return None

    # Make API request
    try:
        response = requests.get(api_url, headers={"x-api-key": api_key})

        if response.status_code != 200:
            print(f"Error: API request failed with status {response.status_code}")
            print(f"Response: {response.text}")
            return None

        reports = response.json()

        # Check for processing reports
        processing_reports = [
            report for report in reports if report.get("status") == "processing"
        ]

        is_processing = len(processing_reports) > 0

        print(f"Processing status: {is_processing}")
        print(f"Total reports: {len(reports)}")
        print(f"Processing reports: {len(processing_reports)}")

        if processing_reports:
            print("Processing report IDs:")
            for report in processing_reports:
                print(f"  - {report.get('slug', 'unknown')}")

        return is_processing

    except Exception as e:
        print(f"Error: {e}")
        return None


def send_notification(title, message):
    """Send macOS notification with sound and dialog"""
    try:
        # Send notification with sound
        subprocess.run(
            [
                "osascript",
                "-e",
                f'display notification "{message}" with title "{title}" sound name "Glass"',
            ],
            check=True,
        )

        # Also show a dialog that requires user interaction
        subprocess.run(
            [
                "osascript",
                "-e",
                f'display dialog "{message}" with title "{title}" buttons {{"OK"}} default button "OK" with icon note',
            ],
            check=True,
        )

    except subprocess.CalledProcessError as e:
        print(f"Failed to send notification: {e}")


def watch_processing_status():
    """Watch processing status and notify when complete"""
    print("Starting watch mode. Checking every 60 seconds...")
    print("Press Ctrl+C to stop")

    try:
        while True:
            print(f"\n--- Checking at {time.strftime('%Y-%m-%d %H:%M:%S')} ---")
            is_processing = check_processing_status()

            if is_processing is None:
                print("Failed to check status, retrying in 60 seconds...")
            elif is_processing:
                print("Still processing... checking again in 60 seconds")
            else:
                print("Processing complete!")
                send_notification(
                    "Processing Complete", "All reports have finished processing"
                )
                break

            time.sleep(60)

    except KeyboardInterrupt:
        print("\nWatch mode stopped by user")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check report processing status")
    parser.add_argument(
        "--watch",
        action="store_true",
        help="Watch mode: check every minute until processing is complete",
    )

    args = parser.parse_args()

    if args.watch:
        watch_processing_status()
    else:
        check_processing_status()
```


**コメント:** なし

---

### [[FEATURE]onChangeでの自動修正が入力の妨げになる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/640)

**作成者:** nishio  
**作成日:** 2025-07-08T09:07:51Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->

> クラスタ数の設定フォームが多分onChangeでvalidationをかけてくるけど、たとえば20を12に変えようとしたときに1を入力した時点で2に修正されて入力困難になるのでonBlurとかがいいと思います

https://dd2030.slack.com/archives/C08F7JZPD63/p1751948152974389

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
onBlurに変えるといいのではと思っているが未検証。「ユーザの入力の妨げにならない適切な修正方法」を特定することが必要です。

**コメント:** なし

---

### [[FEATURE]タイトルや概要空欄の状態でCSVをD&Dしたときファイル名を入れる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/639)

**作成者:** nishio  
**作成日:** 2025-07-08T09:03:05Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
たくさんのCSVを分析処理するときに、CSVの名前に合わせて間違えない様に同じ名前をタイトルに入れる作業が手間

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->
タイトルや概要空欄の状態でCSVをD&Dしたときファイル名から.csvを除いたものを空欄のところに入れる、空欄でないなら何もしない

**コメント:** なし

---

### [[FEATURE]濃い意見ビュー改善案](https://github.com/digitaldemocracy2030/kouchou-ai/issues/638)

**作成者:** nishio  
**作成日:** 2025-07-08T08:59:34Z  
**内容:**

# 背景
<!-- なぜその機能が必要なのか、何が改善されるのか具体的に記入してください -->
データ点群の重心位置にラベルがあると点群もラベルが上に乗って見づらいし、ラベル同士もしばしば重なってみづらい

# 提案内容
<!-- 実装案やデザイン案があれば記入してください -->

<img width="1594" height="722" alt="Image" src="https://github.com/user-attachments/assets/1f50a935-fb60-4c76-94a4-c818503e02e2" />


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

### [form から受け付けた API KEY を使ってレポートを生成できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/issues/633)

**作成者:** shingo-ohki  
**作成日:** 2025-07-04T12:23:38Z  
**内容:**

# 背景
#622 でユーザーが環境構築の必要がなく気軽に広聴AIを試せる環境を Azure に準備中だが、現状はセットアップ時に指定した API KEY  を使うようになっているため、ユーザーが自身の費用負担でレポート生成ができない

# 提案内容
レポート作成者が API KEY を入力し、その KEY を使ってレポート生成をできるようにする

- .env で API KEY(OPENAI_API_KEY, OPENROUTER_API_KEY)の指定がされている場合
  - フォームでの API KEY の入力は任意。フォームからの入力があった場合それを優先して使用する
- .env で API KEY(OPENAI_API_KEY, OPENROUTER_API_KEY)の指定がされていない場合
  - フォームでの API KEY の入力は必須。

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

### [[BUG]  scripts/fetch_reports.pyでは「限定公開」「非公開」状態のレポートがバックアップできない](https://github.com/digitaldemocracy2030/kouchou-ai/issues/629)

**作成者:** shingo-ohki  
**作成日:** 2025-07-03T01:10:52Z  
**内容:**

### 概要

scripts/fetch_reports.pyでは「公開」状態のレポートのバックアップは行われるが、「限定公開」「非公開」状態のレポートがバックアップできない

### 再現手順

1. レポートを限定公開にする
2.   scripts/fetch_reports.py を実行する

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->

レポートの公開状態に関わらず、レポートのバックアップが行われる
```
Fetching reports from https://api.wittyisland-cc57c95f.japaneast.azurecontainerapps.io...
Sending request to https://api.wittyisland-cc57c95f.japaneast.azurecontainerapps.io/reports with API key: xxx...
Found 1 reports
Processing report: 17dd4a5a-3b6b-4468-adfa-3c4c5e434228 - サンプルレポート
Saved report result for 17dd4a5a-3b6b-4468-adfa-3c4c5e434228 to /workspace/server/broadlistening/pipeline/outputs/17dd4a5a-3b6b-4468-adfa-3c4c5e434228/hierarchical_result.json
Updated report status in /workspace/server/data/report_status.json
Successfully processed 1 reports
```

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

make azure-update-deployment の内部で `scripts/fetch_reports.py` が実行されており、その際に気がつきました。
```
$ make azure-update-deployment
...
Fetching reports from https://api.wittyisland-cc57c95f.japaneast.azurecontainerapps.io...
Sending request to https://api.wittyisland-cc57c95f.japaneast.azurecontainerapps.io/reports with API key: xxx...
Found 0 reports
No reports were successfully processed
```

もっと言うと、以下でレポートの内容が取得できないことに起因するようでした。
```
$ curl -H 'x-api-key: xxxx' https://api.wittyisland-cc57c95f.japaneast.azurecontainerapps.io/reports
[]
$ curl -H 'x-api-key: xxxx' https://api.wittyisland-cc57c95f.japaneast.azurecontainerapps.io/reports
[{"slug":"17dd4a5a-3b6b-4468-adfa-3c4c5e434228","title":"サンプルレポート","description":"動作確認用のレポート","status":"ready","visibility":"public","isPubcom":true,"createdAt":"2025-07-01T10:39:54.599708+00:00","tokenUsage":280860,"tokenUsageInput":260160,"tokenUsageOutput":20700,"estimatedCost":0.051444,"provider":"openai","model":"gpt-4o-mini"}]
$ 
```

### その他

特に、Azure 環境で 

```
make azure-update-deployment
```

を実行する際に、`scripts/fetch_reports.py` が実行されますが、その際に「限定公開」「非公開」状態のレポートがバックアップできないため、「公開」状態のレポートのみが復元されるという状態になっています。

<!-- 追加で伝えておきたいことがあれば記入してください -->

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(3件)

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
  - [ ] github の branch へのマージをトリガーにして deploy できるようにする
- デモ環境
  - [ ] #633
  - [ ] client-admin のパスワードなしでアクセスできるようにする
  - [ ] dd2030.org ドメインでアクセスできるようにする

**コメント:** なし

---

### [[FEATURE] 意見グループの並び順を意見数の降順で表示する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/617)

**作成者:** shingo-ohki  
**作成日:** 2025-06-28T03:04:29Z  
**内容:**

# 背景
- 意見グループ編集時に、意見グループの並び順と階層表示の対応が一致していないため、修正しようとする意見グループを見つけにくい
- レポート表示時の意見グループの表示がどのような順番で表示されているのか分かりにくい

![Image](https://github.com/user-attachments/assets/20a5d180-2e9b-4937-ba58-b63069cf7583)

![Image](https://github.com/user-attachments/assets/16b43381-24ee-4ed8-b2ef-4371081c362c)

![Image](https://github.com/user-attachments/assets/ec530fe6-c9ef-4479-96da-152b08ef07fe)

# 提案内容
意見数が多い意見グループから順に表示されていると直感的に理解しやすいのでは？

**コメント:** なし

---

### [[FEATURE] 環境確認機能を作る](https://github.com/digitaldemocracy2030/kouchou-ai/issues/400)

**作成者:** tokoroten  
**作成日:** 2025-04-30T05:13:14Z  
**内容:**

# 背景
OpenAIのAPIKeyが正しくセットされているのかどうかが、実際にレポートの作成を始めるまで分からない


# 提案内容
管理画面、クライアント画面に以下の機能を付けたい

管理画面
- APIサーバが生きているかどうか
- ~~OpenAIのkeyが正しいか~~ 、疎通できるかどうか（Azureも）
  - API Key の有効性の確認は、https://github.com/digitaldemocracy2030/kouchou-ai/pull/421 で対応済み
  - 以下の検証については未対応
    - 残高不足の確認
    - RateLimitの確認
- クライアント用のフロントサーバが立っているかどうか
- ローカルLLM用のLM Studioが生きているかどうか

## デザインの検討
#447 



**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (4件)

### [[api] 管理画面のレポート一覧のレスポンスにコメント数などを含める](https://github.com/digitaldemocracy2030/kouchou-ai/pull/636)

**作成者:** shgtkshruch  
**作成日:** 2025-07-06T03:20:37Z  
**変更:** +119 -4 (5ファイル)  
**マージ日:** 2025-07-09T02:58:12Z  
**内容:**

# 変更の概要
- 管理画面のレポート一覧のレスポンスに、コメント数・意見数・意見グループ数を含めるようにしました
- フロントエンドでは、以下のようなデータ構造で取得できます。

```js
{
    "slug": "9d282108-75f7-4575-8125-df714c7e9c28",
    "title": "誰もが等しく行政サービスを使えるよう、デジタル化と人への配慮の両立をめざした行政手続きの整備を求めます。",
    "description": "デジタル化の名のもとに、紙の申請や窓口対応が急激に減り、高齢者や障がいを持つ方にとって行政手続きが「わからない」「できない」ものになりつつあります。手続きがデジタルで簡素になることは歓迎ですが、それに置き去りになる人が増えてはいけません。マイナポータルやLINEでの申請支援のような工夫を全国の自治体で共通化し、誰もが等しく使える行政サービスに整備すべきだと考えます。",
    "status": "ready",
    "visibility": "public",
    "isPubcom": false,
    "createdAt": null,
    "tokenUsage": 0,
    "tokenUsageInput": 0,
    "tokenUsageOutput": 0,
    "estimatedCost": null,
    "provider": null,
    "model": "gpt-4o-mini",
    "analysis": {
        "commentNum": 50,
        "argumentsNum": 50,
        "clusterNum": 50
    }
}
```

# スクリーンショット
- なし

# 変更の背景
- 管理画面のリデザインで、各レポートごとに以下の情報を表示したいため

# 関連Issue
- close: https://github.com/digitaldemocracy2030/kouchou-ai/issues/635

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- 管理画面のレポート一覧で、フロントエンドからコメント数・意見数・意見グループ数が取得できること

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
  * レポート一覧に「分析」データ（コメント数、議論数、クラスタ数）が表示されるようになりました。

* **バグ修正**
  * レポートの分析データ取得時のエラーが適切に処理されるようになりました。

* **テスト**
  * レポート分析データ追加機能に関するテストが追加されました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client-admin] 背景色のデザイントークンと IconButton コンポーネントを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/628)

**作成者:** shgtkshruch  
**作成日:** 2025-07-02T05:46:20Z  
**変更:** +164 -0 (3ファイル)  
**マージ日:** 2025-07-02T07:20:40Z  
**内容:**

# 変更の概要
- 管理画面のレポート一覧画面の実装に必要なデザイントークンやコンポーネントを実装しました
  - 背景色のトークンと IconButton コンポーネント

# スクリーンショット
- まだ画面に当てていないので、この PR では UI の変更はありまえん

# 変更の背景
- 管理画面のリデザインのために、デザインシステムのトークンやコンポーネントが必要なため

# 関連Issue
- https://github.com/digitaldemocracy2030/kouchou-ai/issues/460

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- 管理画面の UI が変わっていないこと

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **新機能**
  * アイコンボタン用の新しいデザインレシピを追加し、複数のバリアントやサイズに対応しました。
  * カスタムスタイルを適用した新しいアイコンボタンコンポーネントを導入しました。
  * 背景色用のセマンティックカラートークンを追加し、柔軟な配色設定が可能になりました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client-admin] レポート一覧の fetch を Server Component で実行する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/626)

**作成者:** shgtkshruch  
**作成日:** 2025-07-01T07:34:14Z  
**変更:** +87 -53 (7ファイル)  
**マージ日:** 2025-07-02T13:32:19Z  
**内容:**

# 変更の概要
- 管理画面のレポート一覧画面で、API キーを指定した fetch を Server Comopnent で実施することで、API キーが client に露出しないようにしました
  - Server で deta fetch が終わることが期待できるので、型定義で不要な optional を削除しました

# スクリーンショット
- UI の変更はありません

# 変更の背景
- adminにおいて、`process.env.NEXT_PUBLIC_ADMIN_API_KEY` でAPIキーを読んでリクエストをfastapiに送っているが、APIキーが漏洩するリスクがある

# 関連Issue
- https://github.com/digitaldemocracy2030/kouchou-ai/issues/547

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- 管理画面のレポート一覧画面が表示できること

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

* **新機能**
  * 複数のレポートを一覧表示する新しいコンポーネントを追加しました。

* **改善**
  * レポート一覧ページがサーバーサイドレンダリングに対応し、データ取得やエラーハンドリングが改善されました。
  * レポート関連コンポーネントで、配列の受け渡しが常に必須となり、より堅牢な挙動となりました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client-admin] AI サービスとの API 接続チェックの Dialog を追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/625)

**作成者:** shgtkshruch  
**作成日:** 2025-07-01T07:13:06Z  
**変更:** +802 -120 (10ファイル)  
**マージ日:** 2025-07-02T07:02:21Z  
**内容:**

# 変更の概要
- API のチェックをする UI をページから Dialog に変更しました
  - Figma: https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=266-2578&t=walX872gM1k44Efs-0
  - Dialog はレポート作成画面に配置しています
  - これまでの環境検証ページは削除しました
  - バックエンドにリクエストを投げる処理を [Server Functions ](https://ja.react.dev/reference/rsc/server-functions)で実装して、API キーが client に露出しないようにしました

# スクリーンショット
## capture

https://github.com/user-attachments/assets/d273c464-4852-4567-9d32-cf8493b80474

## 初期状態
![image](https://github.com/user-attachments/assets/d38ec2e1-dab7-468a-824a-b50d6a916798)

## 成功時
![image](https://github.com/user-attachments/assets/cd0455a4-be88-4147-85b9-0d11cee9c64a)

## 認証エラー
![image](https://github.com/user-attachments/assets/2970ecb3-f9e1-48eb-a9d8-88e650dd5144)

## 残高不足
![image](https://github.com/user-attachments/assets/faa479f4-ff3f-4141-8dec-3398529692dc)

## レート制限
![image](https://github.com/user-attachments/assets/98f9be12-b158-4ce5-b0bf-21b4a929fc22)

## 不明なエラー
![image](https://github.com/user-attachments/assets/443689ef-3573-49ac-af0b-9be7e3497fd1)


# 変更の背景
- OpenAIのAPIKeyが正しくセットされているのかどうかが、実際にレポートの作成を始めるまで分からない

# 関連Issue
- #400 
- #547

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- レポート作成画面に、API をチェックするダイアログがあること
- ダイアログから API のチェックができること

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [x] CIが全て通過している
- [x] 単体テストが実装されているか
- [x] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。


動作確認の項目については、実装者による動作確認のケースが適切かを確認してください。
必要に応じてレビュアー自身による動作確認も歓迎します（必須ではありません）。

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **新機能**
  * AIプロバイダーのAPI接続と残高を確認できる「環境チェックダイアログ」を作成フォームに追加しました。
  * 環境チェック用のカスタムアイコンを追加しました。
  * レポート作成時にAPI利用料が発生する旨の注意文を追加しました。

* **削除**
  * 管理画面の「環境検証」ページおよびそのナビゲーションリンクを削除しました。

* **テスト**
  * 環境チェックダイアログおよびAPI検証機能に対するユニットテストを追加しました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (4件)

### [[GitHub Actions] main ブランチにマージされたコードを Azure に deploy する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/642)

**作成者:** shingo-ohki  
**作成日:** 2025-07-09T01:19:42Z  
**変更:** +186 -0 (1ファイル)  
**内容:**

# 変更の概要
- digitaldemocracy2030/kouchou-ai の main ブランチにマージされると、自動的に別途用意した DD2030 が持つ azure 環境に最新のコードが deploy されるようにする

# 変更の背景
以下のような状況から DD2030 で Azure に[広聴AIの環境](https://client.wittyisland-cc57c95f.japaneast.azurecontainerapps.io/)を構築中だが、この環境の更新は現状は手動でやる必要がある
- 動作確認する環境が、開発者の手元の環境のみのため開発者以外が動作確認するすべがない
- ユーザーが広聴AIを利用するには環境構築をする必要があり、利用までに技術的なハードルがあるためデモ環境を用意したい

# 関連Issue
#622 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

deploy 処理部分は、フォークしたリポジトリから deploy できることを確認しました。
https://github.com/shingo-ohki/kouchou-ai/actions/runs/16157340778

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

* **新機能**
  * Azure Container Appsへの自動デプロイメント用GitHub Actionsワークフローを追加しました。  
  * デプロイ時に環境変数の設定、API・クライアント等のDockerイメージのビルド・プッシュ、リソース割当の更新、ヘルスチェックが自動で行われます。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[client-admin] レポート一覧のテーブルのデザインを変更する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/637)

**作成者:** shgtkshruch  
**作成日:** 2025-07-07T07:56:34Z  
**変更:** +669 -407 (29ファイル)  
**内容:**

# 変更の概要
- 管理画面のレポート一覧のテーブル部分のデザインを Figma に合わせて変更しました
  - Figma: https://www.figma.com/design/ZImSumdtUme9loVY5CejWX/%E5%BA%83%E8%81%B4AI%EF%BC%88%E3%83%87%E3%82%B8%E6%B0%912030%EF%BC%89?node-id=1117-6195&t=kLDcfUdHfbZrAyk1-4
- デザイン変更を一度に適用すると diff が大きくなりすぎるので、下記の「やっていないこと」に記載の点については、別 issue を切って対応します 

# やっていないこと
- ページ上部の見出しの変更や新規作成ボタンの追加、公開設定の合計値の表示
- レポート一覧のテーブルでレポートの複数選択に伴う操作
  - チェックボックスによる選択
  - 公開設定・CSVダウンロード・HTML書き出し・削除の一括操作
-  コメント数などの数値で 1M の略称にする処理
- レポート削除時のダイアログの実装
- Empty State のデザイン変更

# スクリーンショット

## レポート一覧
![スクリーンショット 2025-07-07 16 21 25](https://github.com/user-attachments/assets/e30d5061-c3fc-4f98-a90f-ac60cb2db7a9)

## レポート生成時（成功）

https://github.com/user-attachments/assets/2029628a-3661-46b6-9479-6fd68e39aa9c

## レポート生成（エラー）

概要生成のステップで意図的にエラーを発生させた場合

https://github.com/user-attachments/assets/748bc73f-367b-4288-82b9-f6d3e2dab45f


## インタラクション

https://github.com/user-attachments/assets/dbdbfd8e-90f4-4bf1-81d7-376685719c68

# デザイナーさんへの確認事項
- レポートの作成日時が未登録のレポートが存在し得るのですが、その場合はどのような表示にすると良いでしょうか？
  - 現状は仮で `-` を表示しています
![image](https://github.com/user-attachments/assets/65bd50fe-034e-4ef5-b3e8-7810b7fe9002)

# 変更の背景
- 管理画面の UI を使いやすくしたい

# 関連Issue
- fix: https://github.com/digitaldemocracy2030/kouchou-ai/issues/460

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->

- 管理画面のレポート一覧で、レポートの表示・生成・エラーの場合に適切に表示されること

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

### [fix: make azure-build 時に警告が出る](https://github.com/digitaldemocracy2030/kouchou-ai/pull/632)

**作成者:** shingo-ohki  
**作成日:** 2025-07-03T03:14:26Z  
**変更:** +25 -3 (4ファイル)  
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
  * Dockerイメージのビルド時に追加の環境変数が利用可能になりました。

* **スタイル**
  * `.env.example` ファイルの環境変数値から二重引用符が削除されました。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [レポートのバックアップスクリプトを docker 環境で実行する](https://github.com/digitaldemocracy2030/kouchou-ai/pull/630)

**作成者:** shingo-ohki  
**作成日:** 2025-07-03T01:52:51Z  
**変更:** +7 -1 (1ファイル)  
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
  * Pythonスクリプトの実行方法をDockerコンテナ内で行うように変更し、依存関係の管理と実行環境の分離を強化しました。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

