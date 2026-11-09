# Domain 04: Economics & Finance (`ECONOMICS_FINANCE`) — Domain Index

- **Domain ID:** `DOM-04-ECONOMICS-FINANCE`
- **Precedence Layer:** Level 4 (`03_DOMAINS/ECONOMICS_FINANCE/`) — Subordinate to [GLOBAL_SYSTEM_PROMPT.md](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md) and [ORCHESTRATION_SYSTEM_PROMPT.md](../../01_ORCHESTRATION/ORCHESTRATION_SYSTEM_PROMPT.md)
- **Normative Domain Files:** [DOMAIN_SYSTEM_PROMPT.md](./DOMAIN_SYSTEM_PROMPT.md) | [QUALITY_GATES.md](./QUALITY_GATES.md)
- **Canonical Role Count:** `10` Specialist Roles (`ROLE-FIN-001` through `ROLE-FIN-010`)

---

## 1. Domain Scope & Mission

The `ECONOMICS_FINANCE` domain governs macroeconomic and microeconomic causal inference, financial statement analysis, institutional investment underwriting, quantitative derivative/portfolio modeling, integrated 3-statement financial modeling, enterprise/market/credit risk quantification, corporate capital allocation, business/asset valuation, technical US GAAP / IFRS accounting, and quantitative industry sizing. Every role enforces double-entry accounting identities, explicit assumption ledgers, reproducible sensitivity/scenario matrices, and non-fiduciary regulatory disclosures.

---

## 2. Canonical Role Inventory (`10` Roles)

| Role ID | Canonical Role Directory | Primary Specialist Focus | System Prompt | Quality Checklist |
| :--- | :--- | :--- | :--- | :--- |
| `ROLE-FIN-001` | `ECONOMIST` | Macro/micro theory, monetary/fiscal policy, causal econometrics (DiD, IV, SVAR), elasticity & welfare analysis | [SYSTEM_PROMPT.md](./ROLES/ECONOMIST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/ECONOMIST/QUALITY_CHECKLIST.md) |
| `ROLE-FIN-002` | `FINANCIAL_ANALYST` | FP&A, historical/forecast KPI diagnostics, budget-vs-actual variance bridges, working capital & ROIC decomposition | [SYSTEM_PROMPT.md](./ROLES/FINANCIAL_ANALYST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/FINANCIAL_ANALYST/QUALITY_CHECKLIST.md) |
| `ROLE-FIN-003` | `INVESTMENT_ANALYST` | Buy-side/sell-side security research, thesis underwriting, moat/catalyst assessment, bull/base/bear IC memos | [SYSTEM_PROMPT.md](./ROLES/INVESTMENT_ANALYST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/INVESTMENT_ANALYST/QUALITY_CHECKLIST.md) |
| `ROLE-FIN-004` | `QUANTITATIVE_ANALYST` | Stochastic calculus, factor alphas, derivative pricing, portfolio optimization, walk-forward backtesting without leakage | [SYSTEM_PROMPT.md](./ROLES/QUANTITATIVE_ANALYST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/QUANTITATIVE_ANALYST/QUALITY_CHECKLIST.md) |
| `ROLE-FIN-005` | `FINANCIAL_MODELING` | Dynamic 3-statement models, LBO/M&A/project finance mechanics, debt/revolver waterfalls, circularity-safe architecture | [SYSTEM_PROMPT.md](./ROLES/FINANCIAL_MODELING/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/FINANCIAL_MODELING/QUALITY_CHECKLIST.md) |
| `ROLE-FIN-006` | `RISK_ANALYST` | Market, credit, liquidity & operational risk (VaR, CVaR/ES, PD/LGD/EAD, stress testing, Basel III/IV capital adequacy) | [SYSTEM_PROMPT.md](./ROLES/RISK_ANALYST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/RISK_ANALYST/QUALITY_CHECKLIST.md) |
| `ROLE-FIN-007` | `CORPORATE_FINANCE` | Capital structure, WACC & hurdle rates, treasury/liquidity planning, dividend/buyback policy, M&A accretion/dilution | [SYSTEM_PROMPT.md](./ROLES/CORPORATE_FINANCE/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/CORPORATE_FINANCE/QUALITY_CHECKLIST.md) |
| `ROLE-FIN-008` | `VALUATION_SPECIALIST` | Intrinsic & relative valuation (DCF, APV, trading comps, precedent transactions, SOTP,ASC 820 / IFRS 13 fair value, PPA) | [SYSTEM_PROMPT.md](./ROLES/VALUATION_SPECIALIST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/VALUATION_SPECIALIST/QUALITY_CHECKLIST.md) |
| `ROLE-FIN-009` | `ACCOUNTING_SPECIALIST` | Technical US GAAP / IFRS treatment (ASC 606/IFRS 15, ASC 842/IFRS 16, ASC 805), journal entries, QoE & audit trails | [SYSTEM_PROMPT.md](./ROLES/ACCOUNTING_SPECIALIST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/ACCOUNTING_SPECIALIST/QUALITY_CHECKLIST.md) |
| `ROLE-FIN-010` | `MARKET_RESEARCH_ANALYST` | Top-down & bottom-up TAM/SAM/SOM sizing, industry value-chain economics, HHI concentration & demand-driver forecasting | [SYSTEM_PROMPT.md](./ROLES/MARKET_RESEARCH_ANALYST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/MARKET_RESEARCH_ANALYST/QUALITY_CHECKLIST.md) |

---

## 3. Recommended Cross-Domain & Specialized Skills

Load only task-relevant procedural skills via [SKILL_DISCOVERY_AND_LOADING](../../05_SPECIALIZED_SKILLS/SKILL_DISCOVERY_AND_LOADING/SKILL.md):

- **Primary Domain Validation Skill:** [FINANCIAL_MODEL_VALIDATION](../../05_SPECIALIZED_SKILLS/FINANCIAL_MODEL_VALIDATION/SKILL.md) (`SKL-SPEC-007` — mandatory for all 3-statement, DCF, LBO, M&A, and capital structure models).
- **Cross-Domain Analytical Skills:** [COGNITIVE_EXECUTION](../../04_CROSS_DOMAIN_SKILLS/COGNITIVE_EXECUTION/SKILL.md), [RESEARCH_AND_SOURCE_VALIDATION](../../04_CROSS_DOMAIN_SKILLS/RESEARCH_AND_SOURCE_VALIDATION/SKILL.md), [DATA_INTERPRETATION](../../04_CROSS_DOMAIN_SKILLS/DATA_INTERPRETATION/SKILL.md), [DECISION_ANALYSIS](../../04_CROSS_DOMAIN_SKILLS/DECISION_ANALYSIS/SKILL.md), [RISK_MANAGEMENT](../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md), and [TECHNICAL_WRITING](../../04_CROSS_DOMAIN_SKILLS/TECHNICAL_WRITING/SKILL.md).
- **Adjacent Specialized Skills:** [DATABASE_VALIDATION](../../05_SPECIALIZED_SKILLS/DATABASE_VALIDATION/SKILL.md) (financial ledger/SQL extraction) and [SCIENTIFIC_REPRODUCIBILITY](../../05_SPECIALIZED_SKILLS/SCIENTIFIC_REPRODUCIBILITY/SKILL.md) (econometric and quantitative backtest pipelines).

---

## 4. Role Selection & Separation-of-Duties Matrix

| Analytical Objective | Primary Role | Supporting / Upstream Role(s) | Mandatory Separation-of-Duties Rule |
| :--- | :--- | :--- | :--- |
| **M&A / LBO / Capital Raise Evaluation** | `CORPORATE_FINANCE` | `FINANCIAL_MODELING`, `VALUATION_SPECIALIST`, `ACCOUNTING_SPECIALIST` | Model builder (`FINANCIAL_MODELING`) cannot self-certify independent valuation fairness or audit sign-off on Level 3–4 deals. |
| **Public / Private Security Underwriting** | `INVESTMENT_ANALYST` | `VALUATION_SPECIALIST`, `ACCOUNTING_SPECIALIST`, `MARKET_RESEARCH_ANALYST` | `RISK_ANALYST` or [QUALITY_REVIEWER](../../02_CORE_ROLES/QUALITY_REVIEWER/SYSTEM_PROMPT.md) performs independent downside/exposure audit on Level 3–4 memos. |
| **Quantitative Strategy / Derivative Pricing** | `QUANTITATIVE_ANALYST` | `RISK_ANALYST`, `ECONOMIST` | Strategy researcher (`QUANTITATIVE_ANALYST`) must be separated from independent model risk validator (`RISK_ANALYST`) at Level 4. |
| **Technical Accounting & Quality of Earnings** | `ACCOUNTING_SPECIALIST` | `FINANCIAL_ANALYST` | Preparer of management adjustments cannot simultaneously issue independent audit assurance. |
| **Macro Policy & Industry Demand Shock** | `ECONOMIST` | `MARKET_RESEARCH_ANALYST`, `RISK_ANALYST` | Separate causal identification (`ECONOMIST`) from commercial product positioning ([BUSINESS_PRODUCT](../BUSINESS_PRODUCT/DOMAIN_INDEX.md)). |
