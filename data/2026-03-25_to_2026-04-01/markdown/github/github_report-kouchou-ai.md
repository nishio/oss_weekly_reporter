# GitHub レポート: digitaldemocracy2030/kouchou-ai

期間: 2026-03-25T13:08:28.201222+09:00 から 2026-04-01T13:08:28.201222+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (2件)

### [静的エクスポート環境向けのCSP設定ガイドをドキュメントに追加する](https://github.com/digitaldemocracy2030/kouchou-ai/issues/820)

**作成者:** tokoroten  
**作成日:** 2026-03-29T12:44:22Z  
**内容:**

## 背景

PR #819 で、Plotly の PNG ダウンロードが CSP の `img-src` に `blob:` が含まれていないためブロックされる問題が報告されました。

https://www.broadlistening-hiroshima.com/ の本番環境では、Azure Static Web Apps 側で以下の CSP ヘッダーが付与されています：

```
content-security-policy: default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://js.monitor.azure.com; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self' https://js.monitor.azure.com https://*.applicationinsights.azure.com https://*.azurestaticapps.net; font-src 'self' data:; frame-ancestors 'none';
```

`next.config.ts` の `headers()` は `output: 'export'`（静的ビルド）時には無効（Next.js の仕様で no-op）のため、アプリケーション側での対応だけでは不十分です。

## やりたいこと

リバースプロキシ / CDN / 静的ホスティング環境での CSP 設定ガイドをドキュメントに追加する。

具体的には：
- `img-src` に `blob:` を含める必要がある旨の説明（Plotly の PNG エクスポートに必要）
- Azure Static Web Apps（`staticwebapp.config.json`）での設定例
- その他のホスティング環境（Nginx、Cloudflare 等）での設定例

## 関連
- #819

**コメント:** なし

---

### [PNGでダウンロードボタンが死んでいる可能性がある。](https://github.com/digitaldemocracy2030/kouchou-ai/issues/818)

**作成者:** tokoroten  
**作成日:** 2026-03-29T08:52:54Z  
**内容:**

PNGでダウンロードボタンが死んでいる可能性がある。
要調査
<img width="1241" height="740" alt="Image" src="https://github.com/user-attachments/assets/02137572-8913-4872-85be-e8219c6b3fc7" />

コンソールには次のエラーが出てきた
```
Loading the image 'blob:https://www.broadlistening-hiroshima.com/f28317b7-2c10-4b7b-8534-1ef4a988968b' violates the following Content Security Policy directive: "img-src 'self' data:". The action has been blocked.
```

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

## Pull Requests

### 過去7日間にマージされたPR (0件)

### 過去7日間に作成されたPR (1件)

### [Fix Plotly PNG download blocked by CSP missing blob: in img-src](https://github.com/digitaldemocracy2030/kouchou-ai/pull/819)

**作成者:** Copilot  
**作成日:** 2026-03-29T08:54:09Z  
**変更:** +15 -0 (1ファイル)  
**内容:**

Plotly's PNG export pipeline internally renders SVG via `new Image()` with a `blob:` URL (`URL.createObjectURL(svgBlob)`) before drawing to canvas. The CSP `img-src 'self' data:` didn't include `blob:`, causing the snapshot to fail silently with a CSP violation.

## Change

- **`apps/public-viewer/next.config.ts`**: Added `headers()` to emit `Content-Security-Policy: img-src 'self' data: blob:;` on all routes.

```typescript
async headers() {
  return [
    {
      source: "/(.*)",
      headers: [
        {
          key: "Content-Security-Policy",
          // blob: is required for Plotly's PNG download, which internally loads
          // an SVG as a blob: URL on a canvas before exporting as PNG.
          value: "img-src 'self' data: blob:;",
        },
      ],
    },
  ];
},
```

> Note: `headers()` is a no-op when `output: 'export'` is set (static builds). Those deployments would need `blob:` added at the web-server/CDN layer separately.

<!-- START COPILOT CODING AGENT TIPS -->
---

⌨️ Start Copilot coding agent tasks without leaving your editor — available in [VS Code](https://gh.io/cca-vs-code-docs), [Visual Studio](https://gh.io/cca-visual-studio-docs), [JetBrains IDEs](https://gh.io/cca-jetbrains-docs) and [Eclipse](https://gh.io/cca-eclipse-docs).


**コメント:** なし

---

### 過去7日間に更新されたPR（作成・マージを除く）(0件)

