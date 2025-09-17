# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-09-10T12:15:59.724824+09:00 から 2025-09-17T12:15:59.724824+09:00 まで

## Issues

### 過去7日間に完了されたissue (1件)

### [[REFACTOR] client-admin: lint error が出ている](https://github.com/digitaldemocracy2030/kouchou-ai/issues/702)

**作成者:** shingo-ohki  
**作成日:** 2025-09-10T07:55:56Z  
**内容:**

# 現在の問題点
<!-- 現在のコードの何が問題なのか、どのような技術的負債があるかを説明してください -->
client-admin で `npm run lint` を実行すると以下のようなエラーが出ている

```
% cd client-admin && npm run lint

> kouchou-ai-client-admin@0.1.0 lint
> biome check .

./package.json format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✖ Formatter would have printed the following content:
  
    41 41 │       "typescript": "^5"
    42 42 │     }
    43    │ - }
       43 │ + }
       44 │ + 
  

./app/create/utils/validation.ts format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✖ Formatter would have printed the following content:
  
     27  27 │     }
     28  28 │   
     29     │ - ··if·(id.startsWith('-'))·{
         29 │ + ··if·(id.startsWith("-"))·{
     30  30 │       return { isValid: false, errorMessage: "IDはハイフンで始めることができません" };
     31  31 │     }
     32  32 │   
     33     │ - ··if·(id.endsWith('-'))·{
         33 │ + ··if·(id.endsWith("-"))·{
     34  34 │       return { isValid: false, errorMessage: "IDはハイフンで終わることができません" };
     35  35 │     }
  

./app/create/utils/validation.test.ts:48:7 lint/complexity/noForEach ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✖ Prefer for...of instead of forEach.
  
    46 │       ];
    47 │ 
  > 48 │       testCases.forEach((id) => {
       │       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  > 49 │         const result = validateReportId(id);
  > 50 │         expect(result).toEqual({ isValid: true });
  > 51 │       });
       │       ^^
    52 │     });
    53 │ 
  
  ℹ forEach may lead to performance issues when working with large arrays. When combined with functions like filter or map, this causes multiple iterations over the same type.
  

./app/create/utils/validation.test.ts:112:7 lint/complexity/noForEach ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✖ Prefer for...of instead of forEach.
  
    110 │       ];
    111 │ 
  > 112 │       testCases.forEach((id) => {
        │       ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  > 113 │         const result = validateReportId(id);
         ...
  > 117 │         });
  > 118 │       });
        │       ^^
    119 │     });
    120 │ 
  
  ℹ forEach may lead to performance issues when working with large arrays. When combined with functions like filter or map, this causes multiple iterations over the same type.
  

Checked 108 files in 18ms. No fixes applied.
Found 4 errors.
check ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✖ Some errors were emitted while running checks.
 ```

**コメント:** なし

---

### 過去7日間に作成されたissue (1件)

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

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (1件)

### [fix: client-admin lint error](https://github.com/digitaldemocracy2030/kouchou-ai/pull/703)

**作成者:** shingo-ohki  
**作成日:** 2025-09-10T08:15:38Z  
**変更:** +7 -7 (3ファイル)  
**マージ日:** 2025-09-10T08:38:02Z  
**内容:**

# 変更の概要
client-admin で lint error が出ていたので解消します

# 関連Issue
#702 

# 動作確認の結果
<!-- 実装者は動作確認の結果を記載してください（例: レポート作成を実行し、正常にレポートが作成されることを確認した） 複数の動作確認を行った場合は、それぞれの結果を記載してください -->
今回の修正箇所の

- レポート作成時のIDのバリデーション動作に影響がないこと
- `app/create/utils/validation.test.ts` が成功すること

を確認しました

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

* テスト
  * 複数ケース検証のループ記法を統一し可読性を改善。期待結果や動作は変更ありません。
* リファクタ
  * バリデーション処理の文字列表現を整理。ロジックやエラーメッセージに変更はありません。
* チョア
  * 設定ファイルのフォーマットを微調整し整合性を向上。機能面への影響はありません。
* 影響
  * 今回はユーザー向けの新機能や不具合修正はありません。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に作成されたPR (2件)

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

### 過去7日間に更新されたPR（作成・マージを除く）(2件)

### [[FEATURE] Gemini を利用してレポート生成できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/698)

**作成者:** AkioPonkotu  
**作成日:** 2025-09-03T15:42:51Z  
**変更:** +656 -40 (26ファイル)  
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

