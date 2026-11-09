# Quality Checklist: Market Research Analyst (`MARKET_RESEARCH_ANALYST` — `ROLE-FIN-010`)

- **Role ID:** `ROLE-FIN-010`
- **Canonical Role:** `MARKET_RESEARCH_ANALYST`
- **Parent Domain:** `ECONOMICS_FINANCE` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). Verify every market-sizing identity programmatically before `PASS`.

## 1. Taxonomy, Scope & Source Provenance
- [ ] Market boundary clearly specifies included/excluded products, value-chain tier (Net Revenue vs. Gross Profit vs. GMV), geographies, currency, and real-vs-nominal basis (`FIN-QG-01`).
- [ ] Primary statistical sources (Census/NAICS, BLS, Eurostat, OECD, audited competitor 10-K/20-F segment filings) are cited with publication year; zero unverified press-release CAGRs are accepted at face value.
- [ ] Every Bottom-Up parameter (eligible enterprise/household count, penetration ceiling, usage frequency, net ASP, replacement cycle) is recorded in the Explicit Assumption Ledger (`FIN-QG-02`).

## 2. Triangulation, Concentraton & Mathematical Identities
- [ ] Top-Down, Bottom-Up, and Supply-Side (competitor revenue sum) estimates are reconciled side-by-side, with residual variance explained (`FIN-QG-03`).
- [ ] Hierarchy invariant `0 <= SOM <= SAM <= TAM` holds across every customer segment, geography, and forecast year; zero value-chain double-counting across supplier/OEM/distributor tiers (`FIN-QG-04`).
- [ ] Competitor market shares sum to `100.0%` (including explicit fragmented "Other/Unpenetrated" bucket), and HHI ($\sum s_i^2$) is calculated accurately.
- [ ] Forecast CAGRs decompose explicitly into unit volume growth, penetration/adoption S-curve saturation, and net ASP price/mix change (accounting for price deflation where scale increases).

## 3. Sensitivity, Cyclicality & Competitive Risk
- [ ] 2D sensitivity matrices test TAM/SAM/SOM against net ASP compression, penetration ceiling, and replacement-cycle elongation (`FIN-QG-05`).
- [ ] Bull, Base, and Bear industry scenarios distinguish secular adoption trends from cyclical pull-forward or macro budget freezes (`FIN-QG-06`, `FIN-QG-07`).

## 4. Uncertainty, Research Ethics & Governance Hygiene
- [ ] Data gaps, private-competitor revenue estimation error bands, and international extrapolation limits are transparently disclosed (`FIN-QG-08`).
- [ ] Deliverable uses zero fabricated surveys/MNPI, zero emojis/placeholders, and includes non-fiduciary analytical disclaimers (`FIN-QG-09`).

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
