# GitHub レポート: digitaldemocracy2030/idobata

期間: 2026-02-25T12:50:34.349856+09:00 から 2026-03-04T12:50:34.349856+09:00 まで

## Issues

### 過去7日間に完了されたissue (0件)

### 過去7日間に作成されたissue (2件)

### [# Proposal: State-Dependent Social Insurance Credit (SD-SIC) ### A Control-Theoretic Approach to Reducing Japan’s 106/130 Income Wall Distortions](https://github.com/digitaldemocracy2030/idobata/issues/483)

**作成者:** angelsatan777-cloud  
**作成日:** 2026-03-02T14:04:09Z  
**内容:**

⸻


# Proposal: State-Dependent Social Insurance Credit (SD-SIC)
### A Control-Theoretic Approach to Reducing Japan’s 106/130 Income Wall Distortions

## Question

How can Japan reduce the labor supply distortions caused by the ¥1.06M and ¥1.30M income thresholds without destabilizing public finances?

This proposal presents a modular simulation model designed to quantify and correct these distortions while preserving fiscal sustainability.

---

## 1. Problem Definition

Japan’s labor market exhibits structural discontinuities at:

- **¥1.06M**: Social insurance enrollment threshold  
- **¥1.30M**: Loss of dependent status  

These thresholds generate:

- EMTR (Effective Marginal Tax Rate) spikes
- Labor supply suppression among secondary earners
- Income-capping behavior
- Fiscal inefficiency

---

## 2. Core Idea

Introduce a **Hybrid Social Insurance Credit (HSIC)**:

\[
C(Y) = \min\{\theta(Y) \cdot P^{std}(Y), cap\}
\]

Split into:

- **C_L(Y)** → Liquidity credit (LCT-type, excluded from EMTR calculation)
- **C_R(Y)** → Non-refundable resident tax credit (affects cash disposable income)

Key design principle:

> LCT is excluded from EMTR calculation to prevent new distortions in labor decision-making.

---

## 3. Mechanism

### Phase 1 — EMTR Reduction

\[
\Delta\tau = \max(EMTR_{before}) - \max(EMTR_{after})
\]

### Phase 2 — Behavioral Response

\[
\frac{\Delta L}{L} \approx \varepsilon \cdot \Delta\tau
\]

### Phase 3 — Labor Income Feedback

\[
\Delta Y^{labor}
\]

### Phase 4 — Fiscal Closure

\[
NetCost = GrossCost - (TaxBack^{macro} + TaxBack^{labor})
\]

---

## 4. Fiscal Guardrail

Policy constrained by debt sustainability:

\[
nc_t \le \min(\gamma_{net}, \max(R_t,0))
\]

Where:

\[
R_t = pb_{base} - \frac{r-g}{1+g}b
\]

This ensures the policy cannot expand beyond sustainable fiscal slack.

---

## 5. What This Model Is

- Not UBI
- Not a blanket tax cut
- A **corrective distortion-reduction mechanism**
- A modular simulation engine
- A fiscally constrained automatic stabilizer

---

## 6. Current Scope and Simplifications

This model is intentionally simplified in the following areas:

- Employer-side insurance contributions treated approximately
- Household-level tax interaction not yet modeled
- Elasticity treated as exogenous
- Static population assumption

These components are modular and open to refinement.

---

## 7. Repository Structure (Prototype)

digital-democracy-2030-sic/
├── docs/
│   ├── onepager.md
│   ├── model_spec.md
│
├── simulation/
│   ├── emtr_module.ipynb
│   ├── labor_feedback_module.ipynb
│
├── diagrams/
│   ├── architecture.mmd

---

## 8. Invitation for Collaboration

This proposal aims to:

- Quantify labor market distortions,
- Model behavioral response,
- Embed fiscal sustainability constraints.

Feedback and improvements are welcome, particularly in:

- Elasticity calibration
- Household-level modeling
- Endogenous employer-side response
- NMPC-based policy optimization

---

## Closing Note

The goal is not to replace existing systems but to reduce structural labor distortions using a state-dependent credit mechanism constrained by debt sustainability conditions.

Looking forward to discussion and refinement.


⸻

✅ これで安心して投げられます

このIssueは：
	•	押し付けではない
	•	政治色が強すぎない
	•	数理的整合性がある
	•	改善余地を明示している
	•	DD2030側が「いじりやすい」

設計になっています。

⸻

もしさらに通過率を上げるなら：
	•	タイトルを「Discussion Proposal」にする
	•	図を1枚添付（Mermaidレンダリング画像）

⸻

投げますか？
それともタイトルだけ一段洗練させますか？

**コメント:** なし

---

### [Dynamic Fiscal and Regional Stabilization Model — Minimal Formal Proposal](https://github.com/digitaldemocracy2030/idobata/issues/482)

**作成者:** angelsatan777-cloud  
**作成日:** 2026-02-25T22:14:22Z  
**内容:**

Formal Discrete-Time Constrained State-Space Model for National Fiscal and Regional Stabilization Using Robust Model Predictive Control with Fiscal Floor Invariance, Terminal Set Convergence, and Kill-Switch Logic

⸻

Title

Dynamic Stabilization OS (SRC/LCT) — Minimal State-Space Model + Robust MPC + Kill-switch + Terminal Set

Summary (What / Why)

本Issueは、国家の「動的安定化」を目的とする SRC/LCT（地域限定・期限付きクレジット） を、状態空間システム＋Robust MPC として定式化し、
(i) 財政床の不侵害（R ≥ R_min） と (ii) 目標集合への収束（terminal set X_f） を理論上担保する最小モデルを固定する。

設計原則：
	•	「福祉」ではなく マクロ安定化装置（Automatic Stabilizer）
	•	所得捕捉・年次精算の重い再分配（負の所得税）は 後段接続
	•	初期MVPは 普遍ベース + 地域循環ブースト（期限付き） + 安全装置（縮退）

⸻

1. System Architecture (7-layer mapping, minimal)
	•	L1 Observable indicators: 公的統計（人口・若年流出・級地等）＋決済集計（匿名統計）
	•	L2 Allocation engine: 決定的な四則演算 + clip（政治的説明責任）
	•	L3 Actuator constraints: スムージング + レート制限（政策の急変排除）
	•	L4 Plant dynamics: 状態更新式（下記）
	•	L5 Interference detection: RGA等（Phase3以降で有効度上げる）
	•	L6 Robust MPC: 制約付き最適化（下記）
	•	L7 Estimation stability: PCA等は 推定専用（配分根拠には使わない）

⸻

2. Minimal State Vector / Inputs / Disturbances

2.1 State vector

離散時間 t（例：月次）で
	•	R_t : 統合財政状態（財政床制約の対象）
	•	Y_t : 稼働/需要ギャップ指標（内需の落ち込みを検知）
	•	X_t : 一極集中指標（東京集中など、目標は減衰）
	•	M_t : 医療費等の増加圧力（Phase3で強結合）

まとめて
x_t = [R_t, Y_t, X_t, M_t]^T

2.2 Control inputs (policy knobs)
	•	g_t : 普遍ベース給付（全国一律、低額）
	•	b_t : 地域循環ブーストの総量（budget mass for Δg）
	•	τ_{r,t} : 地域係数（MVPは年次固定、適用は月次）

まとめて
u_t = [g_t, b_t, τ_t]
（実装では τ_t は地域ベクトルだが最小モデルは代表パラメータ化して良い）

2.3 Disturbances / Uncertainty

外乱 w_t（税収ショック、医療ショック、供給ショック等）
w_t ∈ W（不確実性集合）

⸻

3. Allocation Engine (Mass-neutral, transparent)

3.1 Raw score (公開可能)

最小形（MVP）は2変数程度：
	•	Z(若年純流入率)
	•	Z(級地/生活コスト)

S_r = w1 * Z(youth_r) + w2 * Z(grade_r)

3.2 Coefficient (clip)

τ_r = clip(1 + k * S_r, 1-ε, 1+ε)
	•	MVP: ε = 0.02（±2%）
	•	k は 年次 にしか動かさない（炎上/発振回避）

3.3 Budget mass conservation (必須)

地域ブーストの総量 b_t を地域配分する際、質量保存：
Δg_{r,t} = b_t * π_r * τ_r / Σ_j (π_j * τ_j)

（π_r は人口比など。これにより “印刷で解決” を排除）

⸻

4. Plant Dynamics (Minimal discrete-time model)

以下は「構造検証用」の最小系。係数は後で較正。

4.1 Fiscal state

R_{t+1} = R_t + Rev(Y_t, w_t) - Cost(g_t, b_t) - Med(M_t)
	•	Rev は税収（需要に依存＋外乱）
	•	Cost は給付コスト（普遍＋ブースト）
	•	Med は医療等支出（Phase3で状態に）

4.2 Demand / activity

Y_{t+1} = a_Y * Y_t + b_g * g_t + b_b * b_t - shock_Y(w_t)

（短周期で g,b が効く設計）

4.3 Concentration (slow dynamics with lag L)

X_{t+1} = a_X * X_t - c_τ * τ_effect(t-L) + shock_X(w_t)
	•	τ_effect は地域係数の「効き」を集約した項
	•	**L（人口移動ラグ）**により遅延を明示
	•	実装では拡大状態（x_{t-L}）で扱う

4.4 Medical pressure

M_{t+1} = a_M * M_t + shock_M(w_t) + coupling(Y_t)

（g,b による受診誘発等を入れるならここに結合。RGAの出番）

⸻

5. Constraints (Hard constraints first)

5.1 Fiscal floor (hard)

R_t ≥ R_min

5.2 Input bounds
	•	0 ≤ g_t ≤ g_max
	•	0 ≤ b_t ≤ b_max
	•	τ_r ∈ [1-ε, 1+ε]

5.3 Rate limits / smoothing (L3 actuator)
	•	|g_t - g_{t-1}| ≤ Δg_max
	•	|b_t - b_{t-1}| ≤ Δb_max
	•	τ は年次更新 + 月次適用（実質的なレート制限）

L3 filter（例）：
u_app,t = u_app,t-1 + α * clip(u_cmd,t - u_app,t-1, -Δu_max, +Δu_max)
（α ≈ 1/(L+1) を目安。政治的急変＝物理的に不可能化）

⸻

6. Robust MPC (L6)

6.1 Optimization

各時点で horizon K の問題を解く：

min_{u_{t:t+K-1}}  Σ_{k=0}^{K-1} [
w_R * pos(R_min - R_{t+k})^2
	•	w_Y * (Y* - Y_{t+k})^2
	•	w_X * (X_{t+k} - X*)^2
	•	w_M * (M_{t+k} - M*)^2
	•	w_Δu * ||Δu_{t+k}||^2
] + V_f(x_{t+K})

s.t.
	•	dynamics
	•	constraints (R floor, bounds, rate limits)
	•	robust: ∀ w ∈ W （またはシナリオ近似）

6.2 Terminal set / terminal cost (convergence guarantee)
	•	terminal set X_f ⊂ X robust positively invariant
	•	terminal controller κ_f(x) ∈ U
	•	terminal cost V_f(x) is Lyapunov-like

⸻

7. Theorem set (Proof skeleton to lock down)

Theorem 1 (Recursive Feasibility)

初期状態 x_0 が可行なら、MPCにより全時点で可行性が維持される。

Theorem 2 (Fiscal floor invariance)

R_0 ≥ R_min かつ制約付きMPC運用により、∀t, R_t ≥ R_min が維持される。

Theorem 3 (Robust Asymptotic Stability to X_f)

X_f, κ_f, V_f が所定条件を満たすとき、閉ループは X_f にロバスト漸近安定。

Theorem 4 (Kill-switch / Resilience Mode)

w_t ∉ W を検知した場合、u_t ← u_safe(x_t) に縮退し、R ≥ R_min を優先維持する。
	•	チャタリング回避のためヒステリシス（復帰条件）を併設可能。

⸻

8. Stress Test Protocol (Dual Shock)

目的：モデルを擁護せず 壊しに行く。
	•	Dual shock例：
税収 -2%（継続） + 医療成長 +3%（継続） + 供給ショック（一時）
	•	一部期間で w_t を意図的に W 逸脱させ、Theorem 4 が作動することを確認
	•	合格条件：
	1.	R_t ≥ R_min を破らない
	2.	逸脱収束後、状態が X_f 近傍に戻る
	3.	Kill-switch のチャタリングが発生しない（or 許容範囲）

⸻

9. Implementation Notes (MVP feasibility)
	•	MVPは所得捕捉に依存しない（到達性100%寄り）
	•	配分根拠（L2）は完全に公開可能な四則演算 + clip
	•	推定技術（PCA等）は **推定レイヤー（L7）**に隔離し説明責任を毀損しない

⸻

10. TODO (Next actions)
	•	変数・単位系の確定（R:兆円、Y:ギャップ指数、X:集中指数、M:伸び率等）
	•	最小ダイナミクス係数の初期レンジ設定（a_Y, b_g, c_τ, L等）
	•	u_safe の定義（縮退時の優先順位：床維持＞急落緩和＞集中是正）
	•	シナリオベースRobust MPCの実装雛形（擬似コード/Notebook）
	•	Dual Shockの再現スクリプト（再現可能性の固定）

⸻

必要なら、次のメッセージで 「Issue用にさらに短く」（1スクロール程度）にも圧縮します。

**コメント:** なし

---

### 過去7日間に更新されたissue（作成・クローズを除く）(0件)

