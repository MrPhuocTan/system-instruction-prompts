---
name: financial-model-validation
description: "Use this skill when building, auditing, or stress-testing 3-statement financial models, DCF valuations, unit-economics forecasts, capital-budgeting models, or quantitative risk spreadsheets."
---

# Financial Model Validation

## Skill Metadata
- **Skill ID:** `SKL-SPEC-007`
- **Name:** `financial-model-validation`
- **Domain:** `ECONOMICS_FINANCE, BUSINESS_PRODUCT`
- **Version:** `1.0.0`

## Purpose
Guarantee mathematical accuracy, accounting identity tie-out, formula transparency, assumption provenance, and downside stress resilience across corporate finance, valuation (`DCF`, `LBO`, `Comps`), unit-economics (`LTV/CAC`, cohort payback), and risk models before numbers inform capital allocation or strategic recommendations.

## Required Competencies
- Integrated 3-statement accounting mechanics linking `Income Statement`, `Balance Sheet`, `Cash Flow Statement`, working-capital schedules, debt/interest waterfalls, and equity roll-forwards under `GAAP` / `IFRS`.
- Valuation & corporate finance theory: unlevered/levered free cash flow (`UFCF`/`LFCF`), `WACC` consistency, Gordon Growth vs. exit-multiple terminal value cross-checks, mid-year discounting, and `NPV`/`IRR`/`MOIC` invariants.
- Spreadsheet and programmatic model auditing: separating hardcoded inputs from dynamic formula layers, sign-convention discipline, unit/currency/period alignment, and intentional circularity toggles.
- Scenario, two-way sensitivity, break-even, and Monte Carlo downside liquidity stress testing.

## Prerequisites
- Historical financials, trial balances, filings, contract schedules, or model files (`.xlsx`, `.csv`, `.py`, `.sql`) accessible via `read_file` and `run_command`.
- Explicit reporting currency, unit scale (`$ exact`, `$ thousands`, `$ millions`), fiscal calendar, and accounting standard (`US GAAP` vs. `IFRS`) pinned upfront.
- Source verification discipline loaded via [RESEARCH_AND_SOURCE_VALIDATION](../../04_CROSS_DOMAIN_SKILLS/RESEARCH_AND_SOURCE_VALIDATION/SKILL.md) and [DATA_INTERPRETATION](../../04_CROSS_DOMAIN_SKILLS/DATA_INTERPRETATION/SKILL.md).

## Workflow
1. **Verify Historical Inputs & Unit/Period Alignment:** Reconcile historical base periods line-by-line against primary audited filings or ledger exports; confirm uniform currency, real-vs-nominal inflation basis, and fiscal period lengths (monthly/quarterly/annual stub periods).
2. **Audit Formula Integrity & Eliminate Hardcoded Plugs:** Scan every calculation row/script to confirm `0` hardcoded numeric constants embedded inside formulas (`=D12*1.045` forbidden—extract `4.5%` to a labeled assumption cell/config), consistent left-to-right temporal formulas, and zero silent `#REF!`, `#DIV/0!`, `NaN`, or off-by-one range truncations.
3. **Verify Accounting Identities & Roll-Forward Tie-Outs:** Execute deterministic balance checks across every historical and projected period:
   - `Assets - (Liabilities + Stockholders' Equity) == 0.00` (within floating-point tolerance `< 1e-6`, never masked via an unexplained balance-sheet plug).
   - `Beginning Cash + Net Cash Flow (Operating + Investing + Financing + FX) == Ending Balance Sheet Cash`.
   - `Beginning Retained Earnings + Net Income - Dividends/Buybacks == Ending Retained Earnings` and working-capital deltas match cash-flow signs (`increase in AR = cash outflow`).
4. **Validate Valuation & Economic Sanity Bounds:** In `DCF`/valuation models, verify `terminal growth rate g < WACC` and `g <= long-run nominal GDP growth`, cross-check implied terminal EV/EBITDA multiple against Gordon Growth perpetuity, confirm steady-state `ROIC` vs. `WACC` convergence, and match discount-rate numerator/denominator currency and leverage basis.
5. **Run Sensitivity, Break-Even & Liquidity Stress Cases:** Compute `Base`, `Upside`, and `Severe Downside` cases plus 2D sensitivity matrices across key value drivers (revenue growth, gross margin, churn, `WACC`, exit multiple), checking debt-covenant headroom (`DSCR`, `Net Debt / EBITDA`) and minimum cash runway.
6. **Reconcile Outputs Independently via Script:** Run an independent Python verification script (`run_command` using `decimal`/`numpy`/`openpyxl`) recomputing key schedules from raw assumptions to prove zero spreadsheet/code transcription bugs.

## Tools and Techniques
- **Programmatic Tie-Out Script:** Use Python (`openpyxl`, `pandas`, `decimal.Decimal`) via `run_command` to inspect formula strings inside `.xlsx` workbooks and independently verify `IRR`, `NPV`, and balance-sheet check rows across all scenarios.
- **Circularity Breaker Switch:** Isolate interest-on-average-cash/debt loops behind an explicit binary circuit-breaker toggle so broken errors never propagate irreversibly across sheets.
- **Implied-Metric Sanity Cross-Check:** Compute implied market share, revenue per employee, `LTV/CAC`, payback months, and reinvestment rate in terminal years to expose unrealistic hockey-stick extrapolations.
- **Exact Decimal Arithmetic:** Enforce `Decimal` / integer minor-currency units (`cents`) in transactional/ledger code to prevent binary floating-point drift.

## Verification Requirements
- Balance sheet, cash roll-forward, debt schedule, and share-count schedules tie out with `0.00` unexplained variance across 100% of historical and forecast periods under all scenarios.
- Every assumption cites its source tier (`Audited Filing`, `Contracted Schedule`, `Management Guidance`, or `Explicit Sensitivity Assumption`).
- Independent script recalculation confirms headline metrics (`EBITDA`, `UFCF`, `Enterprise Value`, `Equity Value/Share`, `IRR`, `Runway`) match model outputs.

## Quality Criteria
- **Zero Hidden Plugs or Formula Overrides:** Forecast columns use uniform, auditable formulas driven strictly by an isolated assumptions block:
  | Validation Tie-Out Gate | Exact Mathematical Invariant | Tolerance / Failure Action |
  | :--- | :--- | :--- |
  | `Balance Sheet Identity` | `Total Assets - (Total Liabilities + Total Equity) == 0` | `< 1e-6` across all periods; zero plug cells |
  | `Cash Roll-Forward` | `Beg Cash + CFO + CFI + CFF + FX == Ending BS Cash` | Exact tie-out across Base, Upside, and Downside |
  | `Terminal Value Guard` | `Terminal g < WACC` and `g <= Long-Run Nominal GDP` | Cross-check Gordon Growth vs. implied `EV/EBITDA` |
  | `Formula Purity` | `0` hardcoded numeric constants inside forecast formulas | Extract every driver to labeled assumption inputs |
- **Economic & Physical Realism:** Terminal margins, growth rates, working-capital turns, and capex/depreciation ratios respect industry economics and competitive equilibrium.
- **Decision-Grade Sensitivity Transparency:** Headline valuation or ROI figures are presented as calibrated ranges across key sensitivities rather than false-precision point estimates (`$142.37M`).
- **Failure Modes to Avoid:**
  - *Plugged Balance Sheets:* Forcing `Assets == Liabilities + Equity` via an unexplained `"Other Assets / Liabilities"` plug row.
  - *Leverage / Discount Mismatch:* Discounting levered equity cash flows (`LFCF`) at `WACC` or unlevered cash flows (`UFCF`) at Cost of Equity (`Ke`).
  - *Working-Capital Sign Inversion:* Modeling accounts receivable or inventory build as a cash *inflow* instead of an operating cash *outflow*.
  - *Real-vs-Nominal Mixing:* Discounting inflation-adjusted real cash flows with a nominal `WACC` without consistent Fisher adjustment.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [SECURITY_AND_PRIVACY.md](../../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md), fiduciary/regulatory rules, or human approval policies.
- Protect Material Non-Public Information (`MNPI`), confidential deal terms, payroll tables, and customer revenue rosters from external leakage.
- Clearly label outputs as analytical/modeling work products with explicit assumption disclosures—never represent automated model outputs as licensed investment, tax, legal, or statutory audit opinions, and never manipulate assumptions to fabricate predetermined valuations.

## Expected Deliverables
- **Model Audit & Tie-Out Verification Report** confirming balance-sheet, cash-flow, formula-hygiene, and independent recalculation checks across all periods.
- **Assumptions & Provenance Schedule** documenting baseline inputs, units, sources, and economic sanity cross-checks.
- **Scenario & Sensitivity Output Pack** (`Base / Upside / Downside` tables, 2D driver sensitivity matrices, covenant/runway thresholds, and key risks).
