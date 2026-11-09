# Quality Checklist: Investment Analyst (`INVESTMENT_ANALYST` — `ROLE-FIN-003`)

- **Role ID:** `ROLE-FIN-003`
- **Canonical Role:** `INVESTMENT_ANALYST`
- **Parent Domain:** `ECONOMICS_FINANCE` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). All checks must pass prior to IC memo delivery.

## 1. Primary Filing Evidence & Fact-vs-Opinion Separation
- [ ] All historical financials, segment disclosures, customer concentration figures, and debt terms cite primary regulatory filings (10-K, 10-Q, 20-F, DEF 14A, credit agreements) with exact fiscal period and currency (`FIN-QG-01`).
- [ ] Verified historical facts, consensus/market-implied benchmarks, and analyst forecast assumptions are strictly distinguished throughout prose and tables (`FIN-QG-02`).
- [ ] Exact market data/price cutoff date is disclosed; zero consensus figures or multiples are fabricated.

## 2. Capital Structure, EV Bridge & Unit Economics
- [ ] Enterprise Value to Equity Value bridge accurately accounts for basic shares, Treasury Stock Method dilutive options/RSUs, convertible debt, preferred stock, minority interest, total debt/leases, and unrestricted cash (`FIN-QG-03`).
- [ ] GAAP/IFRS Net Income and Operating Cash Flow are reconciled to Adjusted EBITDA and Free Cash Flow, treating stock-based compensation and recurring restructuring transparently.
- [ ] Competitive moat claims are backed by quantitative evidence (gross margin stability, NDR/churn, market share shifts, incremental ROIC vs. WACC, and pricing power vs. inflation).
- [ ] Management incentive alignment (DEF 14A KPI metrics, insider ownership, historical M&A/buyback ROIC) and accounting red flags (DSO/DIO divergence, capitalized costs) are audited.

## 3. Variant Perception, Scenarios & Downside Risk
- [ ] Reverse-DCF or market-implied multiple analysis explicitly states what growth/margin path current valuation prices in and why a variant perception is justified.
- [ ] Coherent Bull, Base, and Bear cases model joint operating, working-capital, leverage, and valuation-multiple outcomes with explicit probability weights and IRR/expected-return skew (`FIN-QG-05`, `FIN-QG-06`).
- [ ] Liquidity, maturity wall, covenant headroom, and thesis-disconfirming "kill criteria" milestones are explicitly quantified (`FIN-QG-07`, `FIN-QG-08`).

## 4. Regulatory & Governance Compliance
- [ ] Deliverable contains zero MNPI usage, zero promotional hype, zero emojis, and zero unfinished placeholders.
- [ ] Prominent non-fiduciary disclaimer (`FIN-QG-09`) confirms the research is objective institutional analysis and not personalized investment advice or a solicitation to buy/sell securities.

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
