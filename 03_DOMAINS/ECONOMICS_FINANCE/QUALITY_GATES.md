# Domain 04: Economics & Finance — Mandatory Quality Gates

- **Domain ID:** `DOM-04-ECONOMICS-FINANCE`
- **Enforcement:** Mandatory pre-handoff verification for all `ECONOMICS_FINANCE` roles and pre-signoff audit for [DOMAIN_LEAD](../../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md), [QUALITY_REVIEWER](../../02_CORE_ROLES/QUALITY_REVIEWER/SYSTEM_PROMPT.md), `SA_GATE`, and `PM_GATE` per [REVIEW_AND_SIGNOFF.md](../../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md) and [INDEPENDENT_VERIFICATION.md](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md).

---

## Mandatory 9-Gate Pass/Fail Matrix

Every `ECONOMICS_FINANCE` deliverable MUST satisfy all applicable gates below before status can be marked `PASS`:

| Gate ID | Gate Name | Objective Pass Criteria | Automatic `FAIL` / `BLOCKED` Trigger |
| :--- | :--- | :--- | :--- |
| **FIN-QG-01** | **Source Reliability** | 100% of empirical historical figures cite primary authoritative sources (audited 10-K/10-Q/20-F filings, central bank/statistical releases, or verified workspace ledgers) with exact fiscal period, reporting standard (US GAAP / IFRS), currency, and unit scale. | Uncited market multiples, fabricated historical numbers, unverified secondary blog scraping treated as audited fact, or mixed fiscal/calendar periods without calendarization notes. |
| **FIN-QG-02** | **Explicit Assumption Ledger** | Dedicated table enumerating every exogenous input/driver, unit, numerical value, historical benchmark range, economic rationale, and owner; clean separation between historical facts, assumptions, and derived outputs. | Hardcoded magic numbers embedded inside formulas, undocumented growth/margin jumps, or conflation of management guidance with audited actuals. |
| **FIN-QG-03** | **Formula & Accounting Identity Correctness** | Deterministic script verification (`run_command`) confirms all formulas: EV-to-Equity bridge, WACC, UFCF/FCFE, NPV/XIRR, Treasury Stock dilution, tax shields, DuPont/ROIC, and econometric estimators; numerator/denominator consistency holds (`EV/EBITDA`, `P/E`). | Mental-math rounding errors, pairing EV with levered earnings, mismatching nominal vs. real rates, $g \ge \text{WACC}$ in Gordon Growth, or unresolved circularity divergence. |
| **FIN-QG-04** | **Balance Sheet / Cash Flow Reconciliation** | Across every historical and forecast period: $\text{Assets} - (\text{Liabilities} + \text{Equity}) = 0$ within `1e-6` tolerance; Net Income $\rightarrow$ Retained Earnings, PP&E roll-forward, NWC $\rightarrow$ Operating Cash Flow, and Debt/Cash roll-forwards reconcile with zero arbitrary plugs. | Out-of-balance Balance Sheet, use of an unexplained "plug" line to force reconciliation, or Cash Flow ending cash diverging from Balance Sheet cash. |
| **FIN-QG-05** | **Sensitivity Analysis** | Multi-way (`2D`) sensitivity matrices quantify output variance across critical value drivers (e.g., WACC $\pm 150\text{ bps}$ vs. terminal growth/exit multiple; revenue growth vs. operating margin; elasticity vs. policy shock). | Single-point valuation, forecast, or policy estimate delivered without driver elasticity or partial-derivative sensitivity bounds. |
| **FIN-QG-06** | **Scenario Analysis** | Coherent multi-variable **Bull, Base, Bear, and Stress** scenarios where revenue, cost structure, working capital, capex, and financing spreads move jointly under internally consistent macro/industry narratives. | Toggling a single isolated cell while holding correlated operational and credit variables static during a recession/stress case. |
| **FIN-QG-07** | **Risk Assessment** | Quantifies material downside, tail, liquidity, covenant-breach, credit, concentration, and model-specification risks using appropriate metrics (VaR, CVaR/Expected Shortfall, DSCR/ICR headroom, max drawdown, or probability-weighted expected loss). | Omitting debt covenant headroom, refinancing walls, liquidity runway, fat-tailed correlation breakdown, or structural regime-break risks. |
| **FIN-QG-08** | **Uncertainty Disclosure** | Explicitly reports confidence intervals, standard errors, data staleness/missingness, survivorship or selection biases, out-of-sample degradation, and unresolved analytical uncertainties (`NOT VERIFIED` items clearly labeled). | Overconfident deterministic prose, false decimal precision on noisy inputs, or hiding statistical insignificance ($p$-hacking / cherry-picked windows). |
| **FIN-QG-09** | **No Personalized Fiduciary Advice Without Licensed Review** | Includes explicit regulatory boundary notice stating the deliverable is objective analytical/educational work product and NOT personalized investment, brokerage, statutory audit, tax, or legal advice; flags required CPA/CFA/RIA/legal sign-off before execution. | Recommending personal security trades tailored to an unverified retail investor, issuing a simulated statutory audit opinion as official assurance, or omitting fiduciary caveats. |

---

## Independent Verification Protocol

1. **Programmatic Recalculation:**
   - Re-run every numerical table, reconciliation check, and sensitivity matrix via an independent Python verification script (`run_command`) aligned with [FINANCIAL_MODEL_VALIDATION](../../05_SPECIALIZED_SKILLS/FINANCIAL_MODEL_VALIDATION/SKILL.md).
   - Confirm zero `NaN`, `Inf`, `#REF!`, `#DIV/0!`, or unrounded tie-out drift (`abs_error <= 1e-6`).
2. **Boundary & Extreme-Input Stress Check:**
   - Test zero-growth, margin compression (`-500 bps`), interest-rate spike (`+300 bps`), and working-capital shock inputs.
   - Verify debt sweeps, revolver draws, tax shields (including NOL carryforwards), and option-dilution waterfalls degrade gracefully without sign-flip errors or negative cash balances.
3. **Audit Trail & Handoff Evidence Packaging:**
   - Record exact verification commands, input filing citations/cutoffs, reconciliation residuals (`max_abs_balance_error`), and any `PARTIAL` or `NOT VERIFIED` items in the worker handoff report.

---

## Mandatory Evidence Artifacts Per Complexity Level

| Task Complexity | Minimum Required Verification Evidence | Sign-Off Authority |
| :--- | :--- | :--- |
| **Level 1 (Scoped Financial Calc)** | Inline assumption table + deterministic `run_command` script verification output + non-fiduciary caveat. | Executing Specialist + Lightweight Main/SA Check |
| **Level 2 (Single-Domain Model / Memo)** | Complete Assumption Ledger + 3-statement / valuation tie-out log + 2D sensitivity matrix + Bull/Base/Bear table. | Specialist + `SA_GATE` + `PM_GATE` |
| **Level 3 (Multi-Role / Cross-Domain Deal)** | All Level 2 artifacts + independent model validation audit + cross-domain unit-economics contract alignment. | Independent Reviewer + `SA_GATE` + `PM_GATE` |
| **Level 4 (High-Assurance / Regulated)** | All Level 3 artifacts + `DOMAIN_LEAD` sign-off + reverse-stress breach matrix + explicit human approval gate. | `DOMAIN_LEAD` + `SA_GATE` + `PM_GATE` + Human Gate |

---

## Gate Escalation & Rejection Rules

- Any deliverable failing **`FIN-QG-03`** (formula/identity error), **`FIN-QG-04`** (unreconciled Balance Sheet or plug usage), or **`FIN-QG-09`** (unlicensed personalized fiduciary advice) is immediately marked **`FAILED`** and returned for remediation.
- Missing primary filing data that prevents empirical tie-out under **`FIN-QG-01`** must be marked **`PARTIAL` / `NOT VERIFIED`** and escalated to `PM` + user rather than bridged with silent guesses.
