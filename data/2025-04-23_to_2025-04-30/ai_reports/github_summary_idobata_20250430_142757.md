# いどばたシステム 4/23~4/30 のGitHub活動まとめ

いどばたシステム(“idobata-*”)のOSS開発にご関心をお持ちいただきありがとうございます。今週（2025-04-23 から 2025-04-30）のGitHub上での主な活動内容をまとめました。新機能や議論の進捗を把握し、ぜひ今後の開発にもご参加ください。

---

## 今週完了した主な項目

### クローズされたIssue（6件）
以下のIssueが完了しました。開発者の皆さんの貢献により、機能追加・修正が進み、利用者にとっての使い勝手が向上しています。

- [Issue #95](https://github.com/digitaldemocracy2030/idobata/issues/95) テーマ一覧のタップ可能エリアが小さすぎる  
  → UIのクリック判定を大きくし、スマホでも押しやすくなりました。作者: jujunjun110

- [Issue #88](https://github.com/digitaldemocracy2030/idobata/issues/88) /frontend buildエラー（win）  
  → Windows環境でのTypeScriptコンパイルエラーを修正し、ビルドがスムーズに行えるように。作者: moai-redcap

- [Issue #37](https://github.com/digitaldemocracy2030/idobata/issues/37) 利用者がキークエスチョンを一目で理解できるように文章を簡潔にする  
  → AIが生み出す長文を簡潔にまとめ、キークエスチョンの可読性向上に成功。作者: devin-ai-integration[bot]（実質: <人間>+Devin）

- [Issue #24](https://github.com/digitaldemocracy2030/idobata/issues/24) CI/CDを整備することでコードPush時に改変に問題あるコードが入り込みにくくする  
  → CIパイプラインに型チェックやlintを導入し、レビュー時の負担を軽減。作者: jujunjun110

- [Issue #15](https://github.com/digitaldemocracy2030/idobata/issues/15) 読みやすさに特化したレポートを作成できるようにし、初めてそのテーマを訪問した人の興味を満たせるようにする  
  → レポートに見出し表示を導入し、概要を一目で掴みやすく改善。作者: jujunjun110

- [Issue #13](https://github.com/digitaldemocracy2030/idobata/issues/13) プロジェクトをコンテナでビルドできるようにすることで、誰でも手元でデバッグ・開発ができるようにする  
  → Dockerを用いたビルド環境を整備し、セットアップが簡単に。作者: jujunjun110

### マージされたPull Request（30件）
今週は合計30件のPRがマージされました。大幅な機能追加やリファクタリング、ドキュメント更新など多岐にわたっています。主なものをピックアップします。

- [PR #98](https://github.com/digitaldemocracy2030/idobata/pull/98) QuestionDetail.tsxで実際のデータを取得するように実装  
  - 作者: jujunjun110+Devin  
  - テーマ詳細画面で、実際のデータを参照して表示するようになり、利用者がより正確な情報を得られるように。

- [PR #78](https://github.com/digitaldemocracy2030/idobata/pull/78) 管理画面ログイン機能の実装  
  - 作者: jujunjun110+Devin  
  - メールアドレスとパスワードでログインできる管理画面が整備され、運用者にとっての利便性が大幅に向上。

- [PR #81](https://github.com/digitaldemocracy2030/idobata/pull/81) Security Enhancement: HttpOnly Cookie Authentication and CSRF Protection  
  - 作者: jujunjun110+Devin  
  - HttpOnlyクッキーによる認証やCSRF対策の追加で、セキュリティが一段と強化。

- [PR #72](https://github.com/digitaldemocracy2030/idobata/pull/72) チャット機能と論点抽出機能の実装  
  - 作者: jujunjun110+Devin  
  - 旧UIで提供していたチャット機能を新UIにも拡張し、意見掲出から論点抽出まで強化。  

- [PR #89](https://github.com/digitaldemocracy2030/idobata/pull/89) 型チェック用の npm コマンドを準備し、既存のエラーを修正し、CI に型チェックを追加  
  - 作者: spinute  
  - CIにTypeScriptの型チェックが組み込まれ、ビルド時にエラーを把握しやすくなりました。

- ほかにもUIの調整、ドキュメンテーション整理など、多数の貢献があります。

---

## 継続中のタスク・議論中のIssue

以下はまだクローズされていないIssueやPRで、今後議論や実装が期待されるものです。積極的なコメントやコントリビューションをお待ちしています。

- [Issue #91](https://github.com/digitaldemocracy2030/idobata/issues/91) 各ホスティング主体が、サイト名やaboutの文章を、管理画面から好きに変更できるようにする  
  → 多様な運営主体が独自のブランディングを実施できるようにするためのIssue。設定画面の設計が需要。

- [Issue #57](https://github.com/digitaldemocracy2030/idobata/issues/57) ホスティング主体者が議論の段階に応じた適切なフィードバックを得られるように確信度レバーを実装する  
  → AIの反論や提案レベルを可変にし、議論の初期から後期まで柔軟にサポートするアイデア。運営者・利用者どちらにもメリットがあると注目度が高いです。

- [Issue #56](https://github.com/digitaldemocracy2030/idobata/issues/56) ホスティング主体者がPRの可読性を高めるためにPR作成時の不要な改行や区切りを削除する  
  → AIが提出するPRのフォーマットをより見やすくする取り組み。OSSプロジェクト全般でのレビュー効率にも関わります。

- 新規発行されたPRについて  
  - [PR #93](https://github.com/digitaldemocracy2030/idobata/pull/93) .env.templateの補足追加 (作者: itoma-aikon)  
  - [PR #81](https://github.com/digitaldemocracy2030/idobata/pull/81) Security Enhancement: HttpOnly Cookie Authentication and CSRF Protection (マージ済みだが追加実装の議論継続中)  
  - [PR #71](https://github.com/digitaldemocracy2030/idobata/pull/71), [PR #72](https://github.com/digitaldemocracy2030/idobata/pull/72) なども併せてご覧ください。

---

## 多様なメンバーによる貢献

今週だけでも、以下のように多くのメンバー（例: jujunjun110, spinute, Shutaro Aoyama, moai-redcap など）や「<人間>+Devin」形式でAIアシスタントを活用しながら活動いただきました。多様な後見者の存在こそが、いどばたシステムのOSS開発を支える大きな力となっています。

---

## 参加の呼びかけ

- IssueやPRのコメント欄でのフィードバックは大歓迎です。  
- 小さな修正から大きな機能追加まで、どんな形でもコントリビュートできます。  
- わからないことがあればIssueを立て、ぜひコミュニティメンバーにご相談ください。

今後とも、いどばたシステムの開発にご注目・ご参加いただければ幸いです。どうぞよろしくお願いいたします。