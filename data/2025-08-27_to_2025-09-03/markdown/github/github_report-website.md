# GitHub レポート: digitaldemocracy2030/website

期間: 2025-08-27T12:15:24.175592+09:00 から 2025-09-03T12:15:24.175592+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (1件)

### [「プロジェクトの歴史-第○週の活動」の更新処理が失敗している](https://github.com/digitaldemocracy2030/website/issues/165)

**作成者:** shingo-ohki  
**作成日:** 2025-08-30T09:51:01Z  
**内容:**

[プロジェクトの歴史](https://dd2030.org/history)ページの第○週の活動の更新処理が失敗している

>kuboon
  [11:08](https://dd2030.slack.com/archives/C08K4CUB12T/p1755742135001609)
https://dd2030.org/history
このページは毎週水曜に自動起動するスクリプトでAIが要約したものをアップしているのですがその AI が [@NISHIO Hirokazu](https://dd2030.slack.com/team/U08G2A216TW) の個人契約になっていて動作が停止しており、 nishio も原因がよく分からないと言っており更新が2週間止まっています。 このページを今後も同じ方針で継続的にやっていくなら個人に依存しないやり方を考えないといけない。
Shingo OHKI
  [8月21日 12:05](https://dd2030.slack.com/archives/C08K4CUB12T/p1755745513698249?thread_ts=1755742135.001609&cid=C08K4CUB12T)
仕組みがあんまり分かってないですが、[この処理](https://github.com/nishio/oss_weekly_reporter/blob/main/.github/workflows/weekly-report.yml)を https://github.com/digitaldemocracy2030/website のリポジトリで動かして適切な認証情報を設定すると良さそうな感じがしますが、どうなんでしょう。
kuboon
  [8月21日 14:49](https://dd2030.slack.com/archives/C08K4CUB12T/p1755755354035159?thread_ts=1755742135.001609&cid=C08K4CUB12T)
根本的には、 LLM のAPIを誰の名義で契約してどう管理するか、という話なのですが、 dd2030 で組織として利用と支払いがなされている LLM サービスって既にあるのですか？
[14:51](https://dd2030.slack.com/archives/C08K4CUB12T/p1755755479973979?thread_ts=1755742135.001609&cid=C08K4CUB12T)
単発的なデータ処理とかは従来通り各自が手元のLLMでやるで良いと思うのですが、毎週やることが確定している作業にLLMを使うのであれば個人に依存するのは難しいのではないかと。LLMを使わないようにする、という方向も要検討だと思います。
Shingo OHKI
  [8月21日 14:53](https://dd2030.slack.com/archives/C08K4CUB12T/p1755755619568019?thread_ts=1755742135.001609&cid=C08K4CUB12T)
そういう話であれば、プロジェクトの広報活動や運営に必要なものなので、負担する判断はされていそうですね。
そこから先どう進んでいるかがちょっと分かってないですが
https://docs.google.com/spreadsheets/d/1nxGSTcDlfhUkYyZsY18muMChgsVHV_oAbf45lr6Yp_0/edit?gid=0#gid=0&range=5:5
[14:55](https://dd2030.slack.com/archives/C08K4CUB12T/p1755755713346529?thread_ts=1755742135.001609&cid=C08K4CUB12T)
管理者立てて進めるというところで、リソースがなくて止まってそう
kuboon
  [8月21日 15:00](https://dd2030.slack.com/archives/C08K4CUB12T/p1755756017845919?thread_ts=1755742135.001609&cid=C08K4CUB12T)
 OpenAI API Keyが欲しい。
CfJのnakakuboさんに発行をお願いします
→5/23 環境を用意しましたので運用管理者の選定をお願いします／C4J [@Satoru Nakakubo](https://dd2030.slack.com/team/U08N4BTNYN6)
→6/3 各プロダクトの運用管理者：[PO/PjM](https://dd2030.slack.com/archives/C08FL58LK8V/p1748702584694419) ／[@sasano](https://dd2030.slack.com/team/U08LQ25DPAB)
このメッセージは投稿から 90 日以上経過したため、非表示になっています。表示するには、有料プランへアップグレードしてください。
kuboon
  [8月21日 15:05](https://dd2030.slack.com/archives/C08K4CUB12T/p1755756343999799?thread_ts=1755742135.001609&cid=C08K4CUB12T)
dd2030 の azure アカウント (テナント？) があるっぽいので、そこにLLMのエンドポイント建ててもらうのが簡単ですかね
Shingo OHKI
  [8月21日 15:08](https://dd2030.slack.com/archives/C08K4CUB12T/p1755756490288659?thread_ts=1755742135.001609&cid=C08K4CUB12T)
各プロダクトごとには管理者を立てていますが、広報やwebsite の部分の管理者がいないということだと思います。
[15:09](https://dd2030.slack.com/archives/C08K4CUB12T/p1755756590233619?thread_ts=1755742135.001609&cid=C08K4CUB12T)
[@モアイ（小野）コミュマネ](https://dd2030.slack.com/team/U08HWJ80CHG) さんがあちこち見てくださってますが、範囲が広すぎるので全部は見きれないという状態かと
kuboon
  [水曜日 10:26](https://dd2030.slack.com/archives/C08K4CUB12T/p1756257994668499?thread_ts=1755742135.001609&cid=C08K4CUB12T)
今朝も要約に失敗、これで3週分
https://github.com/nishio/oss_weekly_reporter/actions/runs/17087638521/job/48454968885
Shingo OHKI
  [10分前](https://dd2030.slack.com/archives/C08K4CUB12T/p1756546731625309?thread_ts=1755742135.001609&cid=C08K4CUB12T)
[ここ](https://github.com/nishio/oss_weekly_reporter/tree/data/data/2025-08-06_to_2025-08-13/markdown/slack)に要約前のデータはあったので、ひとまずそのデータを使って失敗していた直近3週分(week22~24)を追加しました
https://dd2030.org/history

from [2_広報_pr channel](https://dd2030.slack.com/archives/C08K4CUB12T/p1755742135001609)

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (3件)

### [week24](https://github.com/digitaldemocracy2030/website/pull/164)

**作成者:** shingo-ohki  
**作成日:** 2025-08-30T09:23:22Z  
**変更:** +265 -0 (4ファイル)  
**マージ日:** 2025-08-30T09:32:32Z  
**内容:**

内容なし

**コメント:** なし

---

### [week23](https://github.com/digitaldemocracy2030/website/pull/163)

**作成者:** shingo-ohki  
**作成日:** 2025-08-30T09:21:37Z  
**変更:** +380 -0 (5ファイル)  
**マージ日:** 2025-08-30T09:28:47Z  
**内容:**

内容なし

**コメント:** なし

---

### [week22](https://github.com/digitaldemocracy2030/website/pull/162)

**作成者:** shingo-ohki  
**作成日:** 2025-08-30T09:19:20Z  
**変更:** +321 -0 (5ファイル)  
**マージ日:** 2025-08-30T09:26:27Z  
**内容:**

内容なし

**コメント:** なし

---

### 過去7日間に作成されたPR (1件)

### [定期的に "プロジェクトの歴史" を更新する GitHub workflow を追加](https://github.com/digitaldemocracy2030/website/pull/166)

**作成者:** shingo-ohki  
**作成日:** 2025-09-02T12:44:55Z  
**変更:** +180 -0 (1ファイル)  
**内容:**

定期的に[プロジェクトの歴史](https://dd2030.org/history) の slack, github の週ごとのサマリーを更新するようにします

Slack, GitHub からのデータの抽出までは[このリポジトリのワークフロー](https://github.com/nishio/oss_weekly_reporter/actions/runs/17256391901/workflow)にて定期的に取得されているため、そのデータを使って要約を生成し、このリポジトリにPR(draft) を提出するようにします。

- dd2030 が費用負担する OPENAI_API_KEY を利用（リポジトリに設定）
- 毎週水曜 12:30 JSTに実行（[元データの処理が毎週水曜 12:00 JST に実行される](https://github.com/nishio/oss_weekly_reporter/blob/6dd583d0492f1ff029d6dc5a837f8530fea1e93d/.github/workflows/weekly-report.yml#L6)ため、それ以降の時間を指定）

## 動作確認
自分のリポジトリで試してみました
- GitHub Actions: https://github.com/shingo-ohki/dd2030-website/actions/runs/17403185245
- 作成されたPR: https://github.com/shingo-ohki/dd2030-website/pull/3/files

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

