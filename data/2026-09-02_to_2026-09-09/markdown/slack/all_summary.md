# 2026年09月03日～2026年09月09日のSlack活動まとめ

今週は **7個**のチャンネルで合計**25件**のメッセージがやり取りされました。

## チャンネル別アクティビティ

- **#2_開発_広聴ai**: 15件のメッセージ
- **#7_雑談**: 4件のメッセージ
- **#2_コミュニティ運営**: 2件のメッセージ
- **#2_開発_polimoney**: 1件のメッセージ
- **#2_broad-listening-book**: 1件のメッセージ
- **#0_全体お知らせ**: 1件のメッセージ
- **#2_いどばたボット**: 1件のメッセージ

## チャンネル別詳細

### #2_開発_広聴ai (15件のメッセージ)

#### 09月06日(Sun) - 5件

### **Shingo OHKI** in #2_開発_広聴ai _2026-09-06 07:33:11_

【広聴AI：LLM抽出処理で気になった点】
実データを使って GPT-4o / GPT-4o-mini のレポートを比較していたところ、少し気になる挙動がありました。
同じ入力データ・同じプロンプト・同じ設定で比較したところ、
• GPT-4o：482意見抽出
• GPT-4o-mini：681意見抽出
最初はモデルによる意見の分割粒度の差かと思ったのですが、元回答ごとに確認すると、
• GPT-4o：194回答中49回答が「抽出0件」
• GPT-4o-mini：抽出0件は0回答
となっていました。

入力CSVのハッシュ、抽出プロンプト、limit等は同一で、モデルだけが違う。

現在の実装では、個別のLLM呼び出しが失敗した場合に空配列として処理を続行するため、
レポート自体は完成していても、一部回答が分析対象から落ちる可能性がありそう。
まだ原因は未特定。GPT-4o の並列数を30→5に落として再実行し、再現するか確認中。

#### スレッド返信

**Shingo OHKI** _2026-09-06 07:50:52_

GPT-4oの並列数を30→5に落として、同じ194回答で再実行。
• GPT-4o：666意見（抽出0件：0回答）
• GPT-4o-mini：681意見（抽出0件：0回答）
194回答中147回答は抽出件数も完全一致しており、前回の482 vs 681という大きな差は、モデルによる意見分割粒度の違いというより、4o実行時に一部のLLM呼び出しが失敗していた影響が大きそうです。
並列数を下げたことで一旦解消したように見えますが、今回はレポート作成を優先しているため、原因まではまだ深く追えていません。

LLM呼び出しに失敗した回答が0件として扱われてもレポート生成自体は完了する点は、別途改善を考えた方がよさそうです。

モデル比較については、正常に処理できた4oと4o-miniで抽出件数自体はかなり近くなりました。
一方、今回のレポートでは、大クラスタ・詳細クラスタともに4o-miniの方がテーマの違いを読み取りやすいラベルになっている印象です。

また、4oの再実行版では詳細クラスタのラベル生成エラーが2件残っていました。
今回のデータに限って言えば、現時点では4o-miniの方が実用上使いやすそうに感じています。

レポート内容による可能性もあるので、モデル差として一般化できるかはもう少し見てみたいです。

あわせて、現在選択できるモデルが少し古くなってきているので、新しいモデルへの対応もやりたいところ。

**Shingo OHKI** _2026-09-06 08:03:48_

• <https://github.com/digitaldemocracy2030/kouchou-ai/issues/905|[BUG] LLM呼び出し失敗時に一部回答が欠落したままレポート生成が完了する #905>
• <https://github.com/digitaldemocracy2030/kouchou-ai/issues/906|[FEATURE] GPT-5.6 Terra / Luna を選択できるようにする #906>
Slack だと一定期間で見れなくなってしまうので、Issue に追加しました。

ついでに以下も
• <https://github.com/digitaldemocracy2030/kouchou-ai/issues/907|[FEATURE] Gemini 3.8 Flash / 3.5 Flash-Lite を選択できるようにする #907>
• <https://github.com/digitaldemocracy2030/kouchou-ai/issues/908|[BUG] Azure OpenAI 選択時にモデル選択が実際のLLM呼び出しに反映されない #908>
• <https://github.com/digitaldemocracy2030/kouchou-ai/issues/909|[FEATURE] LLMモデル一覧・料金情報を更新しやすい構造にする #909>

**Shingo OHKI** _2026-09-06 08:14:05_

やっぱり、具体事例に使い始めるといろいろ分かってきますね。
 （ここまでたどり着くのが大変）

### **Shingo OHKI** in #2_開発_広聴ai _2026-09-06 08:14:05_

やっぱり、具体事例に使い始めるといろいろ分かってきますね。
 （ここまでたどり着くのが大変）


#### 09月07日(Mon) - 3件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-09-07 20:39:25_

Astraに雑な指示を出したけどちゃんとわかってくれてる、便利な時代

#### スレッド返信

**NISHIO Hirokazu** _2026-09-07 20:40:20_

多分検証実験をしたり修正提案をしたりするとこまでやってくれると思う

**NISHIO Hirokazu** _2026-09-07 20:47:51_

issuesが追加されるたびにそのissuesを解決して、それから残りのissuesをちょっと解決すれば、全体としてはissuesの数が減っていくはず… www


#### 09月08日(Tue) - 2件

### **Shingo OHKI** in #2_開発_広聴ai _2026-09-08 06:44:31_

ありがとうございます！
 （課題が見えると、速攻で実装される。最高！）


#### 09月09日(Wed) - 5件

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-09-09 03:28:21_

今回の活動について日報を書いてもらいました
<https://nishio.github.io/kouchou-ai-developer-wiki/analyses/daily-report-2026-09-09|nishio.github.io/kouchou-ai-developer-wiki/analyses/daily-report-2026-09-09>

### **中山心太（tokoroten）** in #2_開発_広聴ai _2026-09-09 08:38:51_

ひととおりfableしばいてデバッグさせたので、確認してマージしてほしい


<https://github.com/digitaldemocracy2030/kouchou-ai/pull/934|github.com/digitaldemocracy2030/kouchou-ai/pull/934>

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-09-09 15:35:45_

@shinta.nakayama 議論が深くなるとごたごたするから一旦マージはするが「Flexを使うのは時間がかかってもいいから安く済ませたい顧客なのに、エラー時に高額な側のAPIにフォールバックしていいのか？」という懸念点を一応共有しときますね

#### スレッド返信

**中山心太（tokoroten）** _2026-09-09 15:39:24_

あー、それはそうだなあ

### **NISHIO Hirokazu** in #2_開発_広聴ai _2026-09-09 16:04:30_

何かをvector embeddingしたデータを公開したい時、こんな感じでHuggingFaceでオープンデータにできるということがわかりました
<https://huggingface.co/datasets/nishiohirokazu/team-mirai-2025-embeddings|huggingface.co/datasets/nishiohirokazu/team-mirai-2025-embeddings>



### #7_雑談 (4件のメッセージ)

#### 09月03日(Thu) - 1件

### **Ohkubo KOHEI (kuboon)** in #7_雑談 _2026-09-03 15:55:45_

これは私の友人のさいたま市議会議員なのですが
<https://github.com/mikami-takashi-saitamacity/council-activity-db|https://github.com/mikami-takashi-saitamacity/council-activity-db> 
こういう動きを支援したい


#### 09月08日(Tue) - 1件

### **Ohkubo KOHEI (kuboon)** in #7_雑談 _2026-09-08 14:08:09_

X広告で流れてきた
<https://x.com/ayumi_kokkai?s=21&t=N9S2sWYwWeB_Xlmr4yoqHQ|https://x.com/ayumi_kokkai?s=21&t=N9S2sWYwWeB_Xlmr4yoqHQ> 


#### 09月09日(Wed) - 2件

### **岩永淳志** in #7_雑談 _2026-09-09 00:17:10_

今回、一個の議案の賛否を皆さんと共に決めて行きたいと思っています
もしよかったら、拡散よろしくお願いします

<https://www.threads.com/share/BAjugUh2C9/|https://www.threads.com/share/BAjugUh2C9/> 

<https://x.com/iwanaghi_eva/status/2097334722083139755?s=46|https://x.com/iwanaghi_eva/status/2097334722083139755?s=46> 

### **Ryoma Kawabe Yuki** in #7_雑談 _2026-09-09 16:02:33_

10月3日に開催されるCode for Japan Summitの*チケットが今週まで1,000円*なので紹介しておきます！
<https://luma.com/cfjsummit-2026|luma.com/cfjsummit-2026>

今年のテーマは「公共とAI」で、日本各地の自治体がどのようにAI活用に奮闘しているかが知れるセッションになっています！
• 見守りカメラの設置によるプライバシーと市民の合意形成
• 自治体職員がバイブコーディングで整理券発券システムをOSSで公開しちゃった話
• 庁内FDEワークショップ
などいろいろおもしろい話が聞けると思うのでぜひご参加ください



### #2_コミュニティ運営 (2件のメッセージ)

#### 09月04日(Fri) - 2件

### **Slackbot** in #2_コミュニティ運営 _2026-09-04 19:00:27_

リマインダー : <!here> 本日20時より、コミュニティ運営定例会議を開催します！:mega: :clock9: 20:00-21:00 :link: <https://meet.google.com/deb-krky-zxx> :memo: <https://docs.google.com/document/d/1dn9R9WLaGNMDO-t1w7m8-2gZRSrgZI4glDvSIr101J4/edit?usp=sharing> • コミュニティ運営にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！ • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！

### **Slackbot** in #2_コミュニティ運営 _2026-09-04 20:00:28_

リマインダー : <!here> 只今より、コミュニティ運営定例会議を開催します！:mega: :clock9: 20:00-21:00 :link: <https://meet.google.com/deb-krky-zxx> :memo: <https://docs.google.com/document/d/1dn9R9WLaGNMDO-t1w7m8-2gZRSrgZI4glDvSIr101J4/edit?usp=sharing> • コミュニティ運営にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！ • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！



### #2_開発_polimoney (1件のメッセージ)

#### 09月05日(Sat) - 1件

### **Slackbot** in #2_開発_polimoney _2026-09-05 19:00:26_

リマインダー : <#C08FL5L6GSH> :mega:Polimoney開発会議を開催します！:mega: :clock7:19:00-20:00（毎週土曜日） :link:<http://meet.google.com/myy-ptwx-rsu|meet.google.com/myy-ptwx-rsu> :memo:<https://docs.google.com/document/d/19Kn6ekK3twMVcVaSyUgptvmfzrXEJezA6GXTbPXjm9M/edit?tab=t.0>  • 開発にまつわる、進捗報告・相談・ネクストアクションの決定を行う会です！  • 興味ある人、どなたでも参加歓迎です！！ぜひ覗きに来てください！



### #2_broad-listening-book (1件のメッセージ)

#### 09月09日(Wed) - 1件

### **U0AQQN267H7** in #2_broad-listening-book _2026-09-09 00:45:30_

こんにちは！夏休みから戻りました。近況を伺いたいのですが、何かお手伝いできることはありますか？ また、リリースまでのおおまかなスケジュールも、どなたか共有していただけると嬉しいです。
それから、スキー旅行の前に、2027年1月24日〜27日ごろ東京にいる予定です。都合の合う方がいれば、ぜひお会いできたら嬉しいです！



### #0_全体お知らせ (1件のメッセージ)

#### 09月05日(Sat) - 1件

### **Slackbot** in #0_全体お知らせ _2026-09-05 19:00:09_

リマインダー : <!here> :mega: 1時間後より、全体定例会を開催します！ :clock8: 時刻 20:00-21:00 :link: Google Meet <https://meet.google.com/fhn-rcoj-sci> :memo: 議事録 <https://docs.google.com/document/d/1tBhaer67U9LbASfqPrg0rpmv0Tt4K7zFUTTzscKXj_I>  • プロジェクトにまつわる進捗報告・相談・TODOの決定を行う会です • どなたでも参加歓迎です！興味ある方はぜひ覗きに来てください  :open_file_folder:過去の録画格納先 <https://drive.google.com/drive/folders/1H55HTB0_rwargUwUJvEPg76Wz13i2-bp?usp=sharing>



### #2_いどばたボット (1件のメッセージ)

#### 09月05日(Sat) - 1件

### **Shingo OHKI** in #2_いどばたボット _2026-09-05 20:05:21_

意見のある人は書き終わったのかな？
この件、その後どうしましょう？


