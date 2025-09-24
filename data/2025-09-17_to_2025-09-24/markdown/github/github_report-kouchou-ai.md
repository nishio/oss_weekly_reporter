# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-09-17T12:19:02.271139+09:00 から 2025-09-24T12:19:02.271139+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (1件)

### [[BUG]APIが利用可能であってもAPI接続チェックが失敗する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/707)

**作成者:** nishio  
**作成日:** 2025-09-22T08:18:37Z  
**内容:**

### 概要
APIが利用可能であってもAPI接続チェックが失敗する
<img width="478" height="371" alt="Image" src="https://github.com/user-attachments/assets/f27a182d-116c-48ea-b91e-4ba2e5b3e859" />

表示されるエラーメッセージは事実に反するものである。

>エラーが見つかりました。
>内容をご確認ください。
>APIキーが無効または期限切れです。.envファイルを確認し修正してください。APIキーを改めて取得し直した場合も再設定が必要です。

### 再現手順

1. Azure環境で正しくセットアップした後で接続チェックをする

### その他

この環境&設定で問題なくレポートが作れるので、おそらくAzure環境などの条件を正しくチェックしないでAPI接続チェックをしているのだと思う。

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(2件)

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

### [[BUG] 静的ファイル出力時に公開状態のレポートがない場合にエラーとなる](https://github.com/digitaldemocracy2030/kouchou-ai/issues/683)

**作成者:** shingo-ohki  
**作成日:** 2025-07-31T01:14:24Z  
**内容:**

### 概要

<!-- バグの簡潔な説明をお願いします -->
公開状態のレポートがない状態で、[静的ファイル出力](https://github.com/digitaldemocracy2030/kouchou-ai?tab=readme-ov-file#%E9%9D%99%E7%9A%84%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%87%BA%E5%8A%9B)を行うとエラーが出る。


### 再現手順

1. レポートを生成する
2. すべてのレポートを「公開」以外の状態にする
3. [静的ファイル出力](https://github.com/digitaldemocracy2030/kouchou-ai?tab=readme-ov-file#%E9%9D%99%E7%9A%84%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%87%BA%E5%8A%9B)を行う

または、レポートがない状態で 3 を行う。

### 期待する動作

<!-- 本来どう動作すべきかを記入してください -->
例えば以下などが考えられるが、どうすべきかは議論が必要そう
- 適切なエラー（「公開状態のレポートがないためレポートを静的出力できません」etc.）を表示する
- 公開状態にかかわらず静的レポートを出力できるようにする

### スクリーンショット・ログ

<!-- 必要に応じてスクリーンショットやエラーログなどを添付してください -->

```
❯ make client-build-static
rm -rf out
docker compose up -d --wait api
[+] Running 1/1
 ✔ Container kouchou-ai-api-1  Healthy                                                                                        0.5s 
docker compose run --rm -e BASE_PATH= -e NEXT_PUBLIC_OUTPUT_MODE=export -v /home/tizze/program/digital-democracy/kouchou-ai/server:/server -v /home/tizze/program/digital-democracy/kouchou-ai/out:/app/dist client sh -c "npm run build:static && cp -r out/* dist && touch dist/.nojekyll"
[+] Creating 1/1
 ✔ Container kouchou-ai-api-1  Running                                                                                        0.0s 

> kouchou-ai-client@0.1.0 prebuild:static
> npm run copy-image && NEXT_PUBLIC_OUTPUT_MODE=export npm run rename-file


> kouchou-ai-client@0.1.0 copy-image
> node scripts/copy-image.mjs

Copied from default: icon.png
Copied from default: reporter.png
Copied from default: ogp.png
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

> Build error occurred
[Error: Page "/[slug]/opengraph-image.png" is missing "generateStaticParams()" so it cannot be used with "output: export" config.]
npm notice
```
### その他

<!-- 追加で伝えておきたいことがあれば記入してください -->
[BUG] scripts/fetch_reports.pyでは「限定公開」「非公開」状態のレポートがバックアップできない #629 
も似た話

**コメント:** なし

---

## Pull Requests

### 過去7日間にマージされたPR (0件)

### 過去7日間に作成されたPR (3件)

### [Fix hardcoded image paths for GitHub Pages subpath hosting](https://github.com/digitaldemocracy2030/kouchou-ai/pull/709)

**作成者:** NISHIO+Devin  
**作成日:** 2025-09-24T03:15:52Z  
**変更:** +11 -12 (2ファイル)  
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
**変更:** +105 -5 (6ファイル)  
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

### 過去7日間に更新されたPR（作成・マージを除く）(4件)

### [Add GitHub Issues extraction and problem awareness analysis](https://github.com/digitaldemocracy2030/kouchou-ai/pull/705)

**作成者:** NISHIO+Devin  
**作成日:** 2025-09-11T03:57:50Z  
**変更:** +526 -152 (18ファイル)  
**内容:**

# 変更の概要
- GitHub IssuesからkouchouAIパイプラインで「問題意識」を抽出・クラスタリングする機能を追加
- GitHub API統合によるIssue自動取得とCSV出力機能
- 散布図からGitHub Issueへの直接ジャンプ機能（URL field）
- APIキー未設定時のサンプルデータフォールバック機能

# スクリーンショット
UIの変更はありません

# 変更の背景
GitHub Issues内に蓄積された問題意識を可視化・優先順位付けすることで、プロジェクト改善の意思決定を支援するため。散布図上のクラスタから個別Issueに直接ジャンプできることで、詳細な問題把握が可能になります。

# 関連Issue
関連するIssueはありませんが、@nishio からの要望により実装されました。

# 動作確認の結果
⚠️ **制限事項**: GITHUB_TOKENおよびOPENAI_API_KEYが未設定のため、完全なend-to-endテストは実行できていません

**実行済みの確認項目:**
- ✅ fetch_github_issues.py: サンプルデータ生成機能の動作確認
- ✅ CSV出力形式: パイプライン入力要件との適合性確認
- ✅ 設定ファイル: 問題意識抽出プロンプトの定義確認
- ❌ GitHub API統合: APIキー未設定により未確認
- ❌ 完全パイプライン: OpenAI APIキー未設定により未確認
- ❌ URL field保持: 最終CSV出力での確認が必要

**要レビュー項目:**
1. 実際のGitHub Issuesでのデータ取得テスト
2. パイプライン実行後のCSVにURL fieldが正しく保持されているかの確認
3. サンプルデータの代表性（実際のIssue構造との整合性）

Link to Devin run: https://app.devin.ai/sessions/98463f85a4214ec2a343a24c9b4b432a
Requested by: @nishio

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する

**重要な確認項目:**
- [ ] **GitHub API統合**: GITHUB_TOKENを設定してfetch_github_issues.pyが実際のIssuesを取得できるか
- [ ] **完全パイプライン**: OPENAI_API_KEYを設定してanalyze_github_issues.pyが正常に完了するか  
- [ ] **URL field保持**: 最終出力CSVにurl列が含まれ、散布図からのジャンプが機能するか
- [ ] **設定ファイル**: github-issues-analysis.jsonがパイプライン要件を満たしているか
- [ ] **依存関係**: PyGithubライブラリの追加が適切か（requirements.txtへの追加要否）
- [ ] **サンプルデータ**: create_sample_issues_csv()の内容が実際のGitHub Issues構造を適切に模擬しているか

**コメント:** なし

---

### [Fix remaining lint and test issues after PR #703](https://github.com/digitaldemocracy2030/kouchou-ai/pull/704)

**作成者:** NISHIO+Devin  
**作成日:** 2025-09-10T08:46:41Z  
**変更:** +1603 -1324 (6ファイル)  
**内容:**

# 変更の概要
- PR #703 マージ後に残っていたlintエラーとテスト失敗を修正
- clientコンポーネントのTypeScript formatエラー6件を修正
- client-adminのJestテスト依存関係エラー2件を修正

# スクリーンショット
UIの変更はありません（formatとlint修正のみ）

# 変更の背景
PR #703のマージ後、以下の問題が残っていました：
- clientのBiome lintエラー6件（formatエラー5件 + `any`型使用エラー1件）
- client-adminのJestテストで`@testing-library/user-event`モジュールが見つからないエラー2件

これらを修正してすべてのlint・テストを通すため。

# 関連Issue
なし

# 動作確認の結果
以下のコマンドがすべて成功することを確認：
- ✅ `make lint/api-check` (Python linting) 
- ✅ `make test/api` (Python tests: 116 passed, 5 skipped)
- ✅ `npm run lint` in client (Biome TypeScript linting)
- ✅ `npm run lint` in client-admin (Biome TypeScript linting) 
- ✅ `npm test` in client-admin (Jest tests: 12 test suites passed, 90 tests passed)

# CLAへの同意
- 本リポジトリへのコントリビュートには、[コントリビューターライセンス契約（CLA）](https://github.com/digitaldemocracy2030/kouchou-ai/blob/main/CLA.md)に同意することが必須です。
内容をお読みいただき、下記のチェックボックスにチェックをつける（"- [ ]" を "- [x]" に書き換える）ことで同意したものとみなします。

- [x] CLAの内容を読み、同意しました

# マージ前のチェックリスト（レビュアーがマージ前に確認してください）
- [ ] CIが全て通過している
- [ ] 単体テストが実装されているか
- [ ] 今回実装した機能および影響を受けると思われる機能について、適切な動作確認が行われているかを確認する。

## 特に確認が必要な項目
- [ ] ScatterChart.tsxのonClickハンドラの型変更が正しく動作することを確認（ソースリンククリック機能）
- [ ] client-adminの依存関係更新（package-lock.json）が既存機能に影響しないことを確認

---

**Link to Devin run:** https://app.devin.ai/sessions/cd2769dc283c437088f41a71e72f5a8d  
**Requested by:** @nishio

**コメント:** なし

---

### [[client] 用語解説ページとグローバルナビゲーションを追加](https://github.com/digitaldemocracy2030/kouchou-ai/pull/699)

**作成者:** shgtkshruch  
**作成日:** 2025-09-08T12:23:20Z  
**変更:** +542 -60 (18ファイル)  
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
  - FAQページ（アコーディオン式Q&A）とお問い合わせセクションを追加。Slackへ移動するボタンあり。
  - レポート一覧／FAQへのグローバルナビ導入（PC横並び＋モバイル用ドロワー）。
  - アイコンボタンの新UIコンポーネントを追加。

- **リファクタ**
  - 各ページの主要コンテナをBoxベースに変更し、ヘッダーをコンテナ外へ移動。
  - 旧ガイド表示を削除。

- **スタイル**
  - セマンティックトークンに背景と境界カラー群を追加。
  - アイコンボタン用のスタイルレシピを導入。

- **改善**
  - ドロワーのクローズ操作が柔軟に利用可能に。
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[FEATURE] Gemini を利用してレポート生成できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/698)

**作成者:** AkioPonkotu  
**作成日:** 2025-09-03T15:42:51Z  
**変更:** +861 -137 (32ファイル)  
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

