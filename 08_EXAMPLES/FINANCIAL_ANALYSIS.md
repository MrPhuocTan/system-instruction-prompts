# End-to-End Walkthrough: Level 3 / Level 4 Corporate Valuation & DCF Model (`FINANCIAL_ANALYSIS.md`)

> **Walkthrough Governance:** Demonstrates non-software domain rigor (**Complexity Level 3 -> Level 4**) inside `ECONOMICS_FINANCE` ([DOMAIN_SYSTEM_PROMPT.md](../03_DOMAINS/ECONOMICS_FINANCE/DOMAIN_SYSTEM_PROMPT.md), [QUALITY_GATES.md](../03_DOMAINS/ECONOMICS_FINANCE/QUALITY_GATES.md)), preventing IT-only team bias and enforcing primary-source tie-outs, reconciliation checks, sensitivity matrices, and calibrated uncertainty disclosures.

---

## 1. Realistic User Scenario
**User Prompt:**
> "Using the audited FY2023–FY2025 financial filings in `filings/industrial_telemetry_10k.pdf` and peer multiples in `data/public_comps.csv`, build an integrated 5-year 3-statement forecast (FY2026E–FY2030E) and unlevered DCF valuation for Industrial Telemetry Corp to support our Investment Committee acquisition bid."

---

## 2. Complexity Routing & Specialist Non-IT Role Allocation
1. **Complexity Classification ([TASK_COMPLEXITY_ROUTER.md](../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md)):** Escalated from **Level 3** to **Level 4** because outputs inform a consequential capital-allocation M&A bid requiring institutional accounting auditability, scenario stress testing, and human investment sign-off ([HUMAN_APPROVAL_POLICY.md](../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md)).
2. **Domain-Authentic Team Selection (Zero IT-Only Bias):**
   - `ws-accounting-audit`: [ACCOUNTING_SPECIALIST](../03_DOMAINS/ECONOMICS_FINANCE/ROLES/ACCOUNTING_SPECIALIST/SYSTEM_PROMPT.md) -> Owns `analysis/historical_tieout.md` | Skills: [RESEARCH_AND_SOURCE_VALIDATION](../04_CROSS_DOMAIN_SKILLS/RESEARCH_AND_SOURCE_VALIDATION/SKILL.md), [DATA_INTERPRETATION](../04_CROSS_DOMAIN_SKILLS/DATA_INTERPRETATION/SKILL.md)
   - `ws-3stmt-dcf`: [FINANCIAL_MODELING](../03_DOMAINS/ECONOMICS_FINANCE/ROLES/FINANCIAL_MODELING/SYSTEM_PROMPT.md) + [VALUATION_SPECIALIST](../03_DOMAINS/ECONOMICS_FINANCE/ROLES/VALUATION_SPECIALIST/SYSTEM_PROMPT.md) -> Owns `models/dcf_3statement.py`, `outputs/valuation_tables.csv` | Skills: [FINANCIAL_MODEL_VALIDATION](../05_SPECIALIZED_SKILLS/FINANCIAL_MODEL_VALIDATION/SKILL.md)
   - `ws-risk-review`: Independent [RISK_ANALYST](../03_DOMAINS/ECONOMICS_FINANCE/ROLES/RISK_ANALYST/SYSTEM_PROMPT.md) + [QUALITY_REVIEWER](../02_CORE_ROLES/QUALITY_REVIEWER/SYSTEM_PROMPT.md) -> Owns `reports/ic_valuation_memo.md`, `tests/test_model_reconciliation.py` | Skills: [RISK_MANAGEMENT](../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md), [DECISION_ANALYSIS](../04_CROSS_DOMAIN_SKILLS/DECISION_ANALYSIS/SKILL.md)

---

## 3. Primary-Source Tie-Out & Explicit Assumption Ledger
1. **Historical GAAP Normalization (`ws-accounting-audit`):**
   - Verified FY2025 audited revenue (`$184.2M`), GAAP operating income (`$24.6M`), ASC 842 operating lease liabilities (`$11.4M`), capitalized software R&D (`$6.8M`), and diluted share count (`42.85M` shares including RSUs via treasury stock method) directly against Note 7, Note 11, and Note 14 of `filings/industrial_telemetry_10k.pdf`.
   - Refused to treat recurring stock-based compensation (`$9.2M`, `5.0%` of revenue) as a "cash-free add-back" in unlevered free cash flow (`UFCF`) without modeling dilution parity; treated SBC as a real economic expense in Base Case `UFCF`.
2. **Epistemic Separation Ledger (Facts vs. Assumptions):**
   - **Verified Historical Facts:** FY2023–FY2025 revenue CAGR (`16.4%`), gross margin (`71.2%`), net cash (`$31.5M` cash less `$18.0M` term debt = `$13.5M` net cash), statutory + state effective tax rate (`24.5%`).
   - **Parameterized Forecast Assumptions (Base Case):** Revenue growth tapering from `15.0%` (FY2026E) to `9.5%` (FY2030E); EBIT margin expanding from `13.4%` to `18.5%`; CapEx at `3.8%` of revenue; NWC at `6.5%` of incremental revenue; WACC = `10.0%` (`Rf = 4.25%`, `ERP = 5.0%`, relevered $\beta = 1.18$); perpetuity terminal growth $g = 3.0\%$ ($g < \text{WACC}$).

---

## 4. Deterministic Model Reconciliation & Sensitivity Verification
`ws-risk-review` executes `pytest tests/test_model_reconciliation.py` against `models/dcf_3statement.py`:

| Validation Check (`FINANCIAL_MODEL_VALIDATION`) | Invariant Tested Across FY2023–FY2030E | Observed Max Delta | Verdict |
| :--- | :--- | :---: | :---: |
| **Balance Sheet Identity** | `Total Assets - (Total Liabilities + Stockholders' Equity)` | `$0.0000M` (`< 1e-9`) | `PASS` |
| **Cash Flow Bridge** | `Beginning Cash + CFO + CFI + CFF - Ending Cash` | `$0.0000M` (`< 1e-9`) | `PASS` |
| **Working Capital Sign Check** | AR/Inventory increase -> cash outflow; AP/Deferred Rev increase -> inflow | `100%` consistent | `PASS` |
| **Terminal Value Sanity** | Implied exit `EV / FY2030E EBITDA` at `WACC=10.0%, g=3.0%` vs. peer median (`13.8x`) | `12.6x` (`61.4%` of EV) | `PASS` |

**2D Sensitivity Matrix — Implied Equity Value per Diluted Share (`$`):**

| WACC \ Perpetuity Growth ($g$) | `2.0%` | `2.5%` | `3.0%` (Base) | `3.5%` |
| :--- | :---: | :---: | :---: | :---: |
| **`9.0%`** | `$11.08` | `$11.79` | `$12.63` | `$13.63` |
| **`9.5%`** | `$10.22` | `$10.82` | `$11.52` | `$12.35` |
| **`10.0%` (Base)** | `$9.46` | `$9.97` | **`$10.42`** | `$11.27` |
| **`10.5%`** | `$8.79` | `$9.23` | `$9.73` | `$10.31` |
| **`11.0%`** | `$8.20` | `$8.57` | `$9.00` | `$9.49` |

*(Note: Base Case `$10.42/share` includes mid-year convention adjustment and exact net cash bridge `+$13.5M / 42.85M` diluted shares; sensitivity grid reflects full iterative treasury-stock RSU dilution recalculation at each implied share price.)*

**Operating Scenario Summary:**
- **Bear Case (`WACC = 11.5%`, $g = 2.0\%$, terminal EBIT margin `14.5%`):** `$6.85 / share` (`$293.5M` equity value)
- **Base Case (`WACC = 10.0%`, $g = 3.0\%$, terminal EBIT margin `18.5%`):** **`$10.42 / share`** (`$446.5M` equity value)
- **Bull Case (`WACC = 9.0%`, $g = 3.5\%$, terminal EBIT margin `21.0%`):** `$14.18 / share` (`$607.6M` equity value)
- **Trading Comps Cross-Check (`public_comps.csv` 25th–75th percentile NTM EV/EBITDA `11.5x–15.0x`):** `$9.60 – $12.15 / share`.

---

## 5. Unverified Items, Risk Register & Dual Gate Signoff
- **Explicit `NOT VERIFIED` Due-Diligence Items:** Unaudited Q1 FY2026 customer churn cohort ledger, off-balance-sheet warranty indemnification caps, and Section 382 NOL carryforward limitations require virtual data room (`VDR`) legal/tax diligence prior to binding LOI.
- **`SA_GATE = PASS` ([TECHNICAL_REVIEW.md](../06_TEMPLATES/TECHNICAL_REVIEW.md)):** Verified zero circularity errors, exact 3-statement tie-out (`< 1e-9`), deterministic Python recalculation, and primary 10-K filing citation accuracy.
- **`PM_GATE = PASS` ([BUSINESS_REVIEW.md](../06_TEMPLATES/BUSINESS_REVIEW.md)):** Confirmed institutional memo clarity, customer-concentration sensitivity disclosure (top 3 OEMs = `28%` of ARR logged in [RISK_REGISTER.md](../06_TEMPLATES/RISK_REGISTER.md)), and explicit non-fiduciary human approval boundary before any binding bid submission ([FINAL_DELIVERY.md](../06_TEMPLATES/FINAL_DELIVERY.md)).
