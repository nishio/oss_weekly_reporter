# GitHub レポート: digitaldemocracy2030/website

期間: 2025-09-10T12:16:09.014433+09:00 から 2025-09-17T12:16:09.014433+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (1件)

### [毎週のプロジェクトの活動状況の更新処理を移管する](https://github.com/digitaldemocracy2030/website/issues/170)

**作成者:** shingo-ohki  
**作成日:** 2025-09-10T10:30:48Z  
**内容:**

https://dd2030.org/history の「第◯週の活動」の更新処理をこのリポジトリに移管する
 
参考情報
- [oss_weekly_reporter](https://github.com/nishio/oss_weekly_reporter) の [GitHub Actions](https://github.com/nishio/oss_weekly_reporter/actions/runs/17609207319/workflow) で動作している（API KEY は nishio さんのものを使用）
- 上記の GitHub Actions が一部エラーで止まってしまっていた際に、暫定的に https://github.com/digitaldemocracy2030/website/pull/166 でエラーを回避していた

### 経緯
```
kuboon
  [8月21日 11:08](https://dd2030.slack.com/archives/C08K4CUB12T/p1755742135001609)
https://dd2030.org/history
このページは毎週水曜に自動起動するスクリプトでAIが要約したものをアップしているのですがその AI が [@NISHIO Hirokazu](https://dd2030.slack.com/team/U08G2A216TW) の個人契約になっていて動作が停止しており、 nishio も原因がよく分からないと言っており更新が2週間止まっています。 このページを今後も同じ方針で継続的にやっていくなら個人に依存しないやり方を考えないといけない。

dd2030.orgdd2030.org
[デジタル民主主義2030](https://dd2030.org/history)
デジタル民主主義2030プロジェクトポータルサイト (23 kB)
https://dd2030.org/history

:+1:
4





29 件の返信


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
  [8月27日 10:26](https://dd2030.slack.com/archives/C08K4CUB12T/p1756257994668499?thread_ts=1755742135.001609&cid=C08K4CUB12T)
今朝も要約に失敗、これで3週分
https://github.com/nishio/oss_weekly_reporter/actions/runs/17087638521/job/48454968885


Shingo OHKI
  [8月30日 18:38](https://dd2030.slack.com/archives/C08K4CUB12T/p1756546731625309?thread_ts=1755742135.001609&cid=C08K4CUB12T)
[ここ](https://github.com/nishio/oss_weekly_reporter/tree/data/data/2025-08-06_to_2025-08-13/markdown/slack)に要約前のデータはあったので、ひとまずそのデータを使って失敗していた直近3週分(week22~24)を追加しました
https://dd2030.org/history
:arigato:
2
:両目:
1
:バンザイ:
1



Shingo OHKI
  [9月2日 22:04](https://dd2030.slack.com/archives/C08K4CUB12T/p1756818243385929?thread_ts=1755742135.001609&cid=C08K4CUB12T)
毎週自動で https://dd2030.org/history を更新するPRを作るようにしてみました
[定期的に "プロジェクトの歴史" を更新する GitHub workflow を追加](https://github.com/digitaldemocracy2030/website/pull/166)


kuboon
  [9月3日 10:27](https://dd2030.slack.com/archives/C08K4CUB12T/p1756862827422369?thread_ts=1755742135.001609&cid=C08K4CUB12T)
使えるAPIキーあるんですね、よかった :バンザイ:
1点コメントしました （編集済み） 
:arigato:
1



Shingo OHKI
  [9月3日 10:36](https://dd2030.slack.com/archives/C08K4CUB12T/p1756863390821109?thread_ts=1755742135.001609&cid=C08K4CUB12T)
使えるAPIキー
これ用にはなかったのですが、以前 広聴AIのデモ環境用に発行していただいた僕のアカウントの権限で新たにAPI KEY を発行できたので作ってみました。（経緯が分からなくなりそうなので、[こちら](https://docs.google.com/spreadsheets/d/1nxGSTcDlfhUkYyZsY18muMChgsVHV_oAbf45lr6Yp_0/edit?gid=0#gid=0&range=5:5)に書いておきました）


kuboon
  [9月3日 11:01](https://dd2030.slack.com/archives/C08K4CUB12T/p1756864904107709?thread_ts=1755742135.001609&cid=C08K4CUB12T)
https://github.com/digitaldemocracy2030/website/issues/9
おや、このページは。。？
https://dd2030.org/activity

dd2030.orgdd2030.org
[デジタル民主主義2030](https://dd2030.org/activity)
デジタル民主主義2030プロジェクトポータルサイト (23 kB)
https://dd2030.org/activity


[#9 1週間ごとの活動紹介をつくる](https://github.com/digitaldemocracy2030/website/issues/9)
NISHIO Hirokazu  
o1にSlack logを投げてまとめさせてみる！  
Nasuka Sumino  
ありがとうございます！o1まとめがだいぶいい感じですね。
https://w1740803485-clv347541.slack.com/archives/C08F7JZPD63/p1742983677103139
NISHIO Hirokazu  
僕の次の方向性としては毎週「今週の出来事」みたいな形で解説を生成してSlack外の人やSlackの流量が速すぎて追えない人向けに発信すること。  
もっと表示する
Assignees
[@nishio](https://github.com/nishio)
Comments
1
<https://github.com/[digitaldemocracy2030/website](https://github.com/digitaldemocracy2030/website)|digitaldemocracy2030/website>digitaldemocracy2030/website | 3月28日 | 投稿したメンバー: [GitHub](https://dd2030.slack.com/services/B08HGALULNT)
[11:03](https://dd2030.slack.com/archives/C08K4CUB12T/p1756865034017259?thread_ts=1755742135.001609&cid=C08K4CUB12T)
/activity にはメニューからリンク貼られてないですね
本当は /activity に入れるはずだったものが /history に入ってる？ [@NISHIO Hirokazu](https://dd2030.slack.com/team/U08G2A216TW)


kuboon
  [9月3日 12:43](https://dd2030.slack.com/archives/C08K4CUB12T/p1756870985938439?thread_ts=1755742135.001609&cid=C08K4CUB12T)
[@Shingo OHKI](https://dd2030.slack.com/team/U08H3V9KMFH) 欲を言えばスクリプト部分は別ファイルにして単体で動作確認できる方がベターかも？などありますが、とりあえず動かすのが大事なので一旦動かしてみましょうか。
:+1:
2



NISHIO Hirokazu
  [9月3日 16:48](https://dd2030.slack.com/archives/C08K4CUB12T/p1756885715324589?thread_ts=1755742135.001609&cid=C08K4CUB12T)
どっちがどっちだったか忘れたけど、どちらかが古い方で、新しいバージョンを作って、トップからのリンクを変えるか変えないかの議論の途中だったような…


kuboon
  [9月3日 17:03](https://dd2030.slack.com/archives/C08K4CUB12T/p1756886612960949?thread_ts=1755742135.001609&cid=C08K4CUB12T)
/history というと組織立ち上げまでの話というイメージが強い気がする


Shingo OHKI
  [9月3日 17:55](https://dd2030.slack.com/archives/C08K4CUB12T/p1756889751786559?thread_ts=1755742135.001609&cid=C08K4CUB12T)
とりあえず動かすのが大事なので一旦動かしてみましょうか。
[定期的に "プロジェクトの歴史" を更新する GitHub workflow を追加](https://github.com/digitaldemocracy2030/website/pull/166)
こちらマージして動かしてみました。
ひとまず動いてそうなので history 更新しました！
https://dd2030.org/history
:バンザイ:
2



kuboon
  [9月3日 18:06](https://dd2030.slack.com/archives/C08K4CUB12T/p1756890364811799?thread_ts=1755742135.001609&cid=C08K4CUB12T)
すばらC~~~


Shingo OHKI
  [1時間前](https://dd2030.slack.com/archives/C08K4CUB12T/p1757495685191729?thread_ts=1755742135.001609&cid=C08K4CUB12T)
[@NISHIO Hirokazu](https://dd2030.slack.com/team/U08G2A216TW)
https://github.com/nishio/oss_weekly_reporter/commits/data/
こちら今週分のデータが data ブランチに追加されないのって原因分かりますか？
Slack アプリ絡みの関係で、[先週追加したワークフロー](https://dd2030.slack.com/archives/C08K4CUB12T/p1756889751786559?thread_ts=1755742135.001609&cid=C08K4CUB12T) は上記のリポジトリのデータに一部依存してまして。




Shingo OHKI
とりあえず動かすのが大事なので一旦動かしてみましょうか。
[定期的に "プロジェクトの歴史" を更新する GitHub workflow を追加](https://github.com/digitaldemocracy2030/website/pull/166)
こちらマージして動かしてみました。
ひとまず動いてそうなので history 更新しました！
もっと表示する
[2_広報_pr 内のスレッド](https://dd2030.slack.com/archives/C08K4CUB12T/p1756889751786559?thread_ts=1755742135.001609&amp;cid=C08K4CUB12T) | [9月3日](https://dd2030.slack.com/archives/C08K4CUB12T/p1756889751786559?thread_ts=1755742135.001609&amp;cid=C08K4CUB12T) | [返信を確認する](https://dd2030.slack.com/archives/C08K4CUB12T/p1756889751786559?thread_ts=1755742135.001609&amp;cid=C08K4CUB12T)


NISHIO Hirokazu
  [1時間前](https://dd2030.slack.com/archives/C08K4CUB12T/p1757495766957009?thread_ts=1755742135.001609&cid=C08K4CUB12T)
あっ、すみません、認識違いがあって「dd2030の方でやるようになったからこっちは止めていいな」と思って止めちゃいました
[18:16](https://dd2030.slack.com/archives/C08K4CUB12T/p1757495803421099?thread_ts=1755742135.001609&cid=C08K4CUB12T)
あー、そうか、SlackのAPIキーの情報がないからdd2030に移行し切れてないんですね


Shingo OHKI
  [1時間前](https://dd2030.slack.com/archives/C08K4CUB12T/p1757495942805709?thread_ts=1755742135.001609&cid=C08K4CUB12T)
そうなんです。
Slack アプリを追加して新たに API キーを発行しようとも思ったのですが、Slack の free プランでアプリがもう追加できなかったり、新たにアプリを作ってしまうと Slack API の制限が付与されてしまったりで、手っ取り早くは今動いているものを流用した方がよさそうだったので、きれいには移行できてないんです。 （編集済み） 


NISHIO Hirokazu
  [43分前](https://dd2030.slack.com/archives/C08K4CUB12T/p1757496093598149?thread_ts=1755742135.001609&cid=C08K4CUB12T)
とりあえず手動で実行しました
:arigato:
1

[18:22](https://dd2030.slack.com/archives/C08K4CUB12T/p1757496131195019?thread_ts=1755742135.001609&cid=C08K4CUB12T)
APIキーがなんであったかを思い出して適切に移管すべきですね
:祈る:
1



Shingo OHKI
  [31分前](https://dd2030.slack.com/archives/C08K4CUB12T/p1757496800849259?thread_ts=1755742135.001609&cid=C08K4CUB12T)
無事今回の分、反映されました
https://dd2030.org/history
image.png
 
image.png


:力こぶ:
1



kuboon
  [21分前](https://dd2030.slack.com/archives/C08K4CUB12T/p1757497428567099?thread_ts=1755742135.001609&cid=C08K4CUB12T)
APIキーは再発行すればいいですが、 python の script を全部 dd2030/website に入れる方針になりますかね？
```
from [slack 2_広報_pr](https://dd2030.slack.com/archives/C08K4CUB12T/p1755742135001609)

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (1件)

### [Week26 Summary Update](https://github.com/digitaldemocracy2030/website/pull/169)

**作成者:** github-actions[bot]  
**作成日:** 2025-09-10T09:28:14Z  
**変更:** +220 -0 (5ファイル)  
**マージ日:** 2025-09-10T09:30:13Z  
**内容:**

Auto-generated weekly summaries for week26

**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

