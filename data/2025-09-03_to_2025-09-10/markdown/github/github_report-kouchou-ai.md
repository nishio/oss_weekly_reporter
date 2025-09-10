# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2025-09-03T18:20:40.079659+09:00 から 2025-09-10T18:20:40.079659+09:00 まで

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

### 過去7日間に作成されたissue (2件)

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

### [[BUG]将来の開発で必要な変更 - TODO](https://github.com/digitaldemocracy2030/kouchou-ai/issues/700)

**作成者:** nishio  
**作成日:** 2025-09-09T08:32:22Z  
**内容:**

Devin.aiのセットアップの失敗原因を解明しました。以下Devinのレポートnn

1. Biome Linter の修正 🔧

問題: biomeが正しく動作しないため、lint設定を修正する必要があります。

現在の状況:


biomeはroot package.jsonにインストールされている

client/client-adminのpackage.jsonにbiomeが含まれていない

現在のlintコマンドは絶対パスを使用している


必要な変更:

# Option A: Root level でbiomeを使用する場合
cd ~/repos/kouchou-ai && npm install @biomejs/biome@^1.9.4 --save-dev

# Option B: 各プロジェクトにbiomeを追加する場合
cd ~/repos/kouchou-ai/client && npm install @biomejs/biome@^1.9.4 --save-dev
cd ~/repos/kouchou-ai/client-admin && npm install @biomejs/biome@^1.9.4 --save-dev
推奨lint設定 (Option A):

cd ~/repos/kouchou-ai && npx biome check client
cd ~/repos/kouchou-ai && npx biome check client-admin
cd ~/repos/kouchou-ai/server && python -m ruff check .
2. Package.json の更新 📦

変更が必要なファイル:


package.json: biomeバージョンを "^1.9.4" に変更

package-lock.json: npm installによる依存関係の更新

client/package-lock.json: Next.js関連の依存関係更新


3. 環境変数の設定 🔐

現在の状況: 基本的な.envファイルは存在するが、実際のAPIキーは空

開発時に必要な設定:

# .env ファイルで設定が必要な項目（本番環境用）
OPENAI_API_KEY=your_actual_key_here
OPENROUTER_API_KEY=your_actual_key_here
BASIC_AUTH_USERNAME=your_username
BASIC_AUTH_PASSWORD=your_password
4. 依存関係の完全インストール 📥

必要なコマンド:

# Root dependencies
cd ~/repos/kouchou-ai && npm install

# Client dependencies  
cd ~/repos/kouchou-ai/client && npm install

# Client-admin dependencies
cd ~/repos/kouchou-ai/client-admin && npm install

# Server dependencies
cd ~/repos/kouchou-ai/server && uv pip install --system -r requirements-dev.lock


**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(1件)

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

### 過去7日間に作成されたPR (3件)

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
**変更:** +517 -60 (18ファイル)  
**内容:**

# 変更の概要
- 用語解説ページを追加しました
- ヘッダーにグローバルナビゲーションを追加しました
  - スマホとタブレット以上でスタイルの出し分けをしています

# スクリーンショット

<img width="999" height="591" alt="image" src="https://github.com/user-attachments/assets/bb8bcc67-4c71-495c-b830-6134fcd237ff" />


<img width="684" height="478" alt="image" src="https://github.com/user-attachments/assets/82c2af02-e6b5-4ab1-83b0-64f99ab3ec93" />


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

- 新機能
  - FAQページを追加（アコーディオン表示のQ&A）。
  - お問い合わせセクションを追加（Slackコミュニティへのリンク付き）。
  - グローバルナビゲーションを導入（PCタブ/モバイルドロワー対応）。
  - 新しいIconButtonコンポーネントを追加（テーマ適用）。

- リファクタ
  - トップ/詳細ページのレイアウトをBoxベースに変更し、Headerをコンテナ外へ移動。
  - Headerの構造と配置を更新。
  - BroadlisteningGuideを削除。

- スタイル
  - テーマにbg/borderのセマンティックトークンを追加。
  - IconButton用レシピを追加。
  - Drawerのクローズボタンをカスタマイズ可能に。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### [[FEATURE] Gemini を利用してレポート生成できるようにする](https://github.com/digitaldemocracy2030/kouchou-ai/pull/698)

**作成者:** AkioPonkotu  
**作成日:** 2025-09-03T15:42:51Z  
**変更:** +643 -39 (27ファイル)  
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
  - Google Gemini に対応（チャット/埋め込み）。プロバイダー選択に「Gemini」を追加し、複数モデルを選択可能。価格計算に Gemini を追加。
- ドキュメント
  - セットアップ手順を更新し、Gemini APIキーの取得/入力方法を追記。サーバー README に Gemini 設定を追加。
- チョア
  - 例示用環境変数に GEMINI_API_KEY を追加。セットアップスクリプトで Gemini APIキー（任意）を入力・.env へ反映。
  - 一部ログ出力を詳細化（デバッグレベル）。

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

