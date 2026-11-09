# Quality Checklist: BI Analyst (`ROLE-DATA-004`)

- **Role:** [`BI_ANALYST`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Semantic Consistency & Accounting Identities
- [ ] Bound every KPI to one canonical formula (numerator, denominator, exclusions, currency conversion rule, `UTC`/business timezone, and grain) aligned with governed marts.
- [ ] Verified stock-and-flow waterfall identities (`Beginning + Additions - Reductions == Ending`) and `MECE` segment rollups reconcile to `100%` of control totals (`0.00` unexplained variance).
- [ ] Computed rolled-up ratios (`SUM(num) / NULLIF(SUM(denom), 0)`) and semi-additive snapshot balances (`LAST_VALUE` across time) without naive averaging of percentages.

## 2. Cohort Maturation, Mix-Shift & Calendar Rigor
- [ ] Censored cohort comparisons to equal maturation tenure (`D7` vs. `D7`, `M3` vs. `M3`) so immature recent cohorts do not create artificial decline illusions.
- [ ] Excluded or explicitly annotated incomplete trailing periods (`WTD`/`MTD`/`QTD`) and normalized working-day / seasonality effects (`YoY` alongside `MoM`).
- [ ] Tested aggregate rate movements for `Simpson's paradox` via `Price-Volume-Mix` (`PVM`) / shift-share decomposition across primary segments.
- [ ] Confirmed historical cohorts include churned entities (`0` active-only survivorship bias).

## 3. Interpretability, Caveats & Utilitarian Clarity
- [ ] Reported raw sample sizes (`n`) alongside percentages and distinguished descriptive variance attribution from causal inference (`correlation != causation`).
- [ ] Eliminated decorative `"AI Sign"` emojis, misleading dual axes, and vanity metrics lacking counterbalancing guardrail KPIs.

## 4. Reproducibility & Data Privacy
- [ ] Enforced small-cell (`k`-anonymity) suppression and confirmed zero individual `PII` or credentials appear in exported workbooks, CSVs, or executive readouts.
- [ ] Clearly labeled unaudited operational telemetry vs. accounting-closed `GAAP`/`IFRS` figures.

## 5. Independent Verification & Handoff Completeness
- [ ] Re-executed all SQL/Python analysis scripts from clean state verifying every headline KPI, waterfall step, and `PVM` attribution matches reported tables exactly.
- [ ] Handed off canonical metric dictionary and edge-state rules to [`DATA_VISUALIZATION_SPECIALIST`](../DATA_VISUALIZATION_SPECIALIST/SYSTEM_PROMPT.md) and [`ANALYTICS_ENGINEER`](../ANALYTICS_ENGINEER/SYSTEM_PROMPT.md).
- [ ] Explicitly separated empirically verified local query results from `NOT VERIFIED` live SaaS BI portal rendering or unclosed period estimates.
