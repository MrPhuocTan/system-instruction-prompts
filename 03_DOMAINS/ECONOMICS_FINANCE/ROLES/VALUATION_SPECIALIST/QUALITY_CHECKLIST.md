# Quality Checklist: Valuation Specialist (`VALUATION_SPECIALIST` — `ROLE-FIN-008`)

- **Role ID:** `ROLE-FIN-008`
- **Canonical Role:** `VALUATION_SPECIALIST`
- **Parent Domain:** `ECONOMICS_FINANCE` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). Verify every valuation bridge and cross-check programmatically before `PASS`.

## 1. Valuation Premise, Normalization & Peer Consistency
- [ ] Valuation date, currency, standard of value (Fair Value vs. Fair Market Value), and ownership basis (minority marketable vs. control, illiquidity discount DLOM) are explicitly stated (`FIN-QG-01`, `FIN-QG-02`).
- [ ] Public trading comps and precedent transactions are calendarized to a uniform period and normalized identically for US GAAP vs. IFRS lease accounting (ASC 842 vs. IFRS 16), SBC, non-recurring items, and unconsolidated investments.
- [ ] Valuation multiples strictly preserve numerator-denominator consistency (`EV` paired with unlevered metrics `Revenue`/`EBITDA`/`EBIT`/`UFCF`; `Equity Value` paired with `Net Income`/`Book Equity`/`FCFE`) (`FIN-QG-03`).

## 2. Intrinsic DCF, Terminal Value & Capital Waterfall Rigor
- [ ] UFCF formula accurately deducts cash taxes on EBIT (unlevered NOPAT), adds D&A, deducts Capex, and adjusts for $\Delta \text{NWC}$ consistent with underlying Balance Sheet schedules (`FIN-QG-04`).
- [ ] Mid-year discounting convention and stub-period fractional discounting are applied accurately (terminal value discounted from exact terminal cash flow timing).
- [ ] Terminal Value satisfies steady-state economic sanity: $g < \text{WACC}$, $g \le$ long-run nominal GDP growth, terminal `Capex` vs. `D&A` and $\text{ROIC}_{\text{terminal}}$ support $g$, and implied exit `EV/EBITDA` vs. implied $g$ are cross-checked side-by-side.
- [ ] EV-to-Equity-per-Share bridge (or multi-class OPM/PWERM waterfall) accurately captures total debt, preferred liquidation preferences, minority interest, excess cash, and Treasury Stock / option-tranche dilution.

## 3. Triangulation, Sensitivity & Downside Scenarios
- [ ] Valuation conclusion presents a triangulated range ("football field") across DCF, Trading Comps, and Precedents rather than a single unhedged point estimate.
- [ ] 2D sensitivity grids (WACC $\times$ $g$, WACC $\times$ Exit Multiple, Revenue CAGR $\times$ Terminal Margin) and Bull/Base/Bear cases are verified (`FIN-QG-05`, `FIN-QG-06`, `FIN-QG-07`).

## 4. Independence, Uncertainty & Non-Certification Disclosure
- [ ] Terminal value % of total EV, peer dispersion, and Level 3 unobservable input uncertainties are transparently disclosed (`FIN-QG-08`).
- [ ] Deliverable contains zero goal-seeking bias, zero emojis/placeholders, and includes explicit disclaimers (`FIN-QG-09`) that the output is not a licensed fairness opinion, certified IRC 409A safe-harbor appraisal, or statutory audit sign-off.

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
