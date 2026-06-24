# GitHub レポート: digitaldemocracy2030/idobata

期間: 2026-06-17T13:31:29.456708+09:00 から 2026-06-24T13:31:29.456708+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (1件)

### [idobata（DD2030）セットアップ〜試用レポート / ドキュメント不足点まとめ](https://github.com/digitaldemocracy2030/idobata/issues/500)

**作成者:** YusukeHayashiii  
**作成日:** 2026-06-22T15:17:03Z  
**内容:**

> digitaldemocracy2030/idobata をクローンし、Docker でローカル起動して一通り触ってみた記録。主眼は「公式ドキュメントだけでセットアップ〜試用まで完走できるか」。結論は No（一部不十分）。以下、Issue として起票することを想定した形でまとめる。


## TL;DR

リポジトリの README / [development-setup.md](http://development-setup.md/) は高レベルの理解と Docker 起動コマンドには十分だが、手順通りに進めても **AIチャットが動かない**・**政策モジュールのビルドが通らない** という2つの致命的な壁にぶつかった。初見でクローン〜試用まで完走するには、最低でも以下の補強が必要。

**(1)** LLMモデルのハードコードが提供終了（致命・コード修正必須・env化されていない）

**(2)** policy-backend がビルド時に GitHub 秘密鍵を必須とし、無いとビルド失敗（致命・モック構成の案内なし）

## 検証環境（このPC）

本レポートの検証を行ったマシン・ツールチェーンのバージョンは以下のとおり。

**ハードウェア**：MacBook Air（Mac17,3）／ チップ Apple M5（10コア：高性能4＋高効率6）／ メモリ 16GB／ アーキテクチャ arm64

**OS**：macOS 26.5.1（build 25F80）

**Docker**：Docker 29.5.3（build d1c06ef）／ Docker Compose v5.1.4／ Docker Desktop 4.78.0（Homebrew cask で導入）

**Node.js**：v26.0.0（※プロジェクトの想定は Node 20。今回は v26 でも Docker コンテナ内は node:20 系イメージのため起動には支障なし）

**npm**：11.12.1

**Homebrew**：6.0.2

**Python3**：3.9.6（システム標準。python-service はコンテナ内でビルドするためホスト側のバージョンは不問）

**git**：2.50.1（Apple Git-155）

**補足**：arm64（Apple Silicon）環境のため、Docker Desktop 導入時に Rosetta のインストール失敗が出たが、今回使用するイメージ（node / mongo / postgres / nginx / python）はマルチアーキ対応で arm64 ネイティブ動作するため Rosetta は無効のまま支障なし。

## 実施した一連の流れ

**1. HTTPSでクローン** → OK

**2. Docker Desktop を Homebrew で導入**（未インストールだった） → sudoリンクで一度失敗、手動再実行で解決

**3. `.env.template` を `.env` にコピー、JWT生成・モック設定・OpenRouterキー投入** → テンプレに無い変数を手動追加

**4. いどばたビジョン起動**（frontend / idea-backend / mongo / admin） → OK

**5. 管理者ユーザー作成**（`POST /api/auth/initialize`） → OK

**6. いどばた政策起動**（policy-frontend / policy-backend / postgres） → ビルド失敗→ダミー鍵で回避。postgresは起動失敗

**7. テーマ作成→アクティブ化→ユーザー画面で確認** → 仕様/UI導線で混乱

**8. AIチャット送信** → モデル404で失敗→コード修正で解決

**9. 重要論点生成→お題がトップに表示** → OK

**10. 政策モジュールでAIと対話・変更提案** → 保存はGitHub未連携のため失敗（仕様通り）

## ドキュメントが十分だった点

**README.md**：プロダクトの目的・2モジュール構成（いどばたビジョン／いどばた政策）・全体像が充実。

**docs/development-setup.md**：Docker前提の起動コマンド、ポート一覧（5173/5174/5175/3000/3001）、部分起動コマンドが明快。

**admin/README.md**：初期管理者ユーザー作成の `curl` 手順が具体的。

**アーキテクチャ**（モノレポ／2モジュール／MongoDB・PostgreSQL分離）は読めば把握できる。

## ドキュメントが不十分・詰まった箇所

ざっくりと、1>2>3の順で重大だと感じた

### 1. 致命的（手順通りでも動かない）

**(A) AIチャットのLLMモデルが提供終了していて全AI機能が500エラー**

事象：`idea-discussion/backend/services/llmService.js` がモデルを `google/gemini-2.0-flash-001` にハードコード。OpenRouterで現在 `404 No endpoints found` を返し、チャット・論点抽出など全AI機能が落ちる。

ドキュメントの現状：モデルに関する記載が一切なし。モデルを環境変数で差し替える手段も無い（コード修正必須）。

改善案：モデルIDを `.env`（例 `LLM_MODEL=`）で上書き可能にする＋デフォルトを現行モデルに更新。提供終了時の差し替え方を明記。

**(B) policy-backend がビルド時に GitHub 秘密鍵を必須とし、無いとビルド自体が失敗**

事象：`policy-edit/backend/Dockerfile` に `COPY ./policy-edit/backend/secrets/github-key.pem`。鍵が無いとイメージビルドがエラーで停止（UIを見たいだけでも起動不可）。

ドキュメントの現状：「鍵を配置せよ」とはあるが、無いとビルドが壊れること・お試し用にダミー鍵で回避できることが未記載。`VITE_USE_MOCK_GITHUB_CLIENT` でGitHub Appなしに触れる「最小構成パス」が案内されていない。

改善案：「お試し（モック）構成」セクションを新設し、ダミー鍵生成（`openssl genrsa ...`）と `VITE_USE_MOCK_GITHUB_CLIENT=true` をセットで明記。理想はビルド時COPYをやめ実行時マウントに変更。

### 2. 動くが迷う

**(C) `.env.template` に必要変数が欠けている／説明不足**

`VITE_USE_MOCK_GITHUB_CLIENT` が `.env.template` に無い（`.env.example` 側にだけ存在）。`docker-compose.yml` は参照しているのに、テンプレを使うと未設定になる。「いどばたビジョンだけなら実質 `OPENROUTER_API_KEY` だけでOK」「idea-backendはGITHUB_*を実際には使わない（docker-composeで渡しているが未使用）」といった最小要件の切り分けも書かれていない。

**(D) 市民向けの利用フローとUI導線が未文書化**

お題（＝重要論点）はテーマ作成だけでは出ず、管理画面の「重要論点生成」ボタンを手動実行して初めて生成される。この一連（テーマ作成→アクティブ化→意見投稿→重要論点生成→トップに表示）がどのドキュメントにも無い。さらにトップページ／ヘッダーにテーマ一覧（`/themes`）への導線が無い（直接URLが必要）。`project_status.md` で「UIブラッシュアップ」が未完項目として認知済み。

### 3. 品質上直したい

**(E) `postgres:latest` が起動失敗（PG18の仕様変更）**

事象：`docker-compose.yml` が `image: postgres:latest`。現在のlatest=PostgreSQL18でデータ配置仕様が変わり、`postgres-policy` が `Exited(1)`。

影響：チャット応答自体は正常動作する（`ProcessChatMessageUsecase` はログ保存失敗を握り潰して応答を返す設計）。現フローでPostgresを使うのは `interaction_logs`（対話ログ）への保存のみで、停止時の実害は「**対話ログが残らない**」「チャット毎に `ENOTFOUND postgres-policy` のエラーログが出続ける（ノイズ）」だけ。ただし将来ログイン機能（`users`/`sessions` テーブル）が有効化されると必須になる。

ドキュメントの現状：記載なし（イメージのタグ固定もされていない）。

改善案：`postgres:16` 等にメジャーバージョンをピン留め（`latest` を使わない）。

**(F) 管理画面テーマ一覧の表示バグ**

DBは `isActive:true` でも一覧が「非アクティブ」、作成日時が「N/A」と表示される（一覧APIの `enhancedThemes` が `isActive`/`createdAt` を返していない）。ユーザーが「アクティブにしたのに反映されない」と誤解する原因に。

**(G) `docker-compose`（ハイフン）表記**

ドキュメントは `docker-compose up`。新規にDocker Desktopを入れた環境では v2 の `docker compose`（スペース）が標準で、ハイフン版が無い場合がある。表記を `docker compose` に統一推奨。

## 「ドキュメントだけで完走できるか？」への結論

現状：No（一部不十分）。ただし致命的なのは (A)(B) の2点に絞られる。

(A)(B) を自力で解決しないと AIチャット／お題表示・政策起動まで到達できない

(C)(D) が無いと利用フローで迷子になる。

(E)(F)(G) は品質上の改善点。

→ 「Quick Start（お試し最小構成）」ドキュメントが1枚あれば、初見でもクローン〜AIチャット〜お題表示まで完走できるようになる。

具体的には、

- OpenRouterキーのみで動くいどばたビジョン最小起動
- ダミー鍵＋モックで動く政策
- LLMモデルの差し替え方
- テーマ→お題までの操作フロー

を1ページに集約する。

## 補足：理解した設計上のポイント

いどばたビジョンといどばた政策は **独立した2システム**（DBもMongo/Postgresで別、コード上の相互参照なし）。両者の統合は `project_status.md` のマイルストーン③（将来）で構想されており、現状のコードには未実装。

政策モジュールの「文言変更」はローカル即時編集ではなく、**新ブランチへのコミット→Pull Request提案型**。フロントのGitHubクライアントは読み取り専用（`fetchContent` のみ）で、編集機能自体が存在しない。PRがマージされ再読込された時に初めて反映される（＝人間レビューを前提とするガバナンス設計）。

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (2件)

### [docs: Policy Edit の DB 起動手順と migration 手順を development-setup に追記](https://github.com/digitaldemocracy2030/idobata/pull/499)

**作成者:** shingo-ohki  
**作成日:** 2026-06-18T12:33:34Z  
**変更:** +22 -2 (1ファイル)  
**マージ日:** 2026-06-23T03:50:12Z  
**内容:**

## 変更の概要
Policy Edit の開発手順に、実態と異なる記載があったため修正します。
あわせて、初回起動時に必要な migration 手順を追記し、interaction_logs テーブル未作成時の対処が分かるようにします。

## 変更内容
- Policy Edit 起動手順を修正（PostgreSQL サービスを含める）
- migration 実行手順を追記
- テーブル作成確認手順を追記
- relation interaction_logs does not exist エラー時の確認ポイントを追記

## 期待効果
初回セットアップ時の詰まりどころを減らす
テーブル未作成によるエラーを自己解決しやすくする

## 影響範囲
`development-setup.md` のみ

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### [fix: postgres:latest 更新に伴うエラー回避](https://github.com/digitaldemocracy2030/idobata/pull/498)

**作成者:** shingo-ohki  
**作成日:** 2026-06-18T12:15:47Z  
**変更:** +3 -2 (1ファイル)  
**マージ日:** 2026-06-23T03:49:39Z  
**内容:**

## 変更の概要
開発時から時間が経過し `postgres:latest` が 18系になったことで、`postgres-policy` が起動時に以下のエアーで停止してしまうようです。
この影響を回避し、まずは既存の開発フローを安定して動かすため、Policy Edit で利用する PostgreSQL イメージを 17系に固定します。
あわせて、バックエンドがDB起動完了前に立ち上がるレースコンディションを防ぐため、policy-backend の起動条件に `postgres-policy` のヘルスチェック待機を追加します。

PostgreSQL 18系への追従対応は、本PRでは扱わず、必要に応じて別PRで実施します。

```
postgres-policy-dev  | Error: in 18+, these Docker images are configured to store database data in a
postgres-policy-dev  |        format which is compatible with "pg_ctlcluster" (specifically, using
postgres-policy-dev  |        major-version-specific directory names).  This better reflects how
postgres-policy-dev  |        PostgreSQL itself works, and how upgrades are to be performed.
postgres-policy-dev  | 
postgres-policy-dev  |        See also https://github.com/docker-library/postgres/pull/1259
postgres-policy-dev  | 
postgres-policy-dev  |        Counter to that, there appears to be PostgreSQL data in:
postgres-policy-dev  |          /var/lib/postgresql/data (unused mount/volume)
postgres-policy-dev  | 
postgres-policy-dev  |        This is usually the result of upgrading the Docker image without
postgres-policy-dev  |        upgrading the underlying database using "pg_upgrade" (which requires both
postgres-policy-dev  |        versions).
postgres-policy-dev  | 
postgres-policy-dev  |        The suggested container configuration for 18+ is to place a single mount
postgres-policy-dev  |        at /var/lib/postgresql which will then place PostgreSQL data in a
postgres-policy-dev  |        subdirectory, allowing usage of "pg_upgrade --link" without mount point
postgres-policy-dev  |        boundary issues.
postgres-policy-dev  | 
postgres-policy-dev  |        See https://github.com/docker-library/postgres/issues/37 for a (long)
postgres-policy-dev  |        discussion around this process, and suggestions for how to do so.
```

## 変更内容
- postgres-policy のイメージを postgres:latest から postgres:17 へ変更
- policy-backend の depends_on を service_healthy 条件付きへ変更

## 期待効果
- latest 追従に伴う想定外の互換性問題を回避
- PostgreSQL準備完了前のバックエンド起動を防止

## 影響範囲
- docker-compose の Policy Edit 関連サービス定義のみ

# CLAへの同意
本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/idobata/blob/main/CLA.md)に同意することが必須です。

内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました


**コメント:** なし

---

### 過去7日間に作成されたPR (0件)

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

