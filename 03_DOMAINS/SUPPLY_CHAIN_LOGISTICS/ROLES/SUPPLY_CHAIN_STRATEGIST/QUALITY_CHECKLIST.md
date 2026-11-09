# Quality Checklist — Supply Chain Strategist (`ROLE-SCM-001`)

Verify every item below before submitting a handoff report under [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md):

## 1. End-to-End Segmentation, `CODP` & Postponement Rigor
- [ ] Product-market portfolio is segmented quantitatively (`ABC-XYZ` volume/margin vs. `CV` volatility) rather than applying a uniform global policy.
- [ ] Customer Order Decoupling Points (`MTS`, `ATO`, `MTO`, `ETO`) verify that customer tolerance lead time exceeds downstream manufacturing + delivery lead time.
- [ ] Risk-pooling / postponement calculations include explicit inter-region / inter-SKU demand correlation ($\rho_{ij}$), avoiding naive zero-correlation assumptions during seasonal/macro peaks.
- [ ] `S&OP` / `IBP` governance preserves the unconstrained statistical baseline separately from commercial overrides (tracking `Forecast Value Added` of executive adjustments).

## 2. Bullwhip Mitigation & `TTS` / `TTR` Resilience Stress-Testing
- [ ] Order-to-demand variance amplification (**Bullwhip Ratio**) is calculated across echelons with concrete structural fixes for batching, promo forward-buying, and shortage gaming.
- [ ] Node disruption analysis compares **Time-to-Survive (`TTS`)** against **Time-to-Recover (`TTR`)** and ranks bottlenecks by **Revenue-at-Risk (`RaR`)**—not Tier-1 spend alone.
- [ ] Stress tests (`run_command`) evaluate port/lane closure, single-source plant outage, tariff shock, and `+20%` demand surge impacts on `OTIF` and expedite cost.
- [ ] Sub-tier geographic and chokepoint concentration (`HHI`) is audited alongside Tier-1 supplier diversity.

## 3. Working Capital (`C2C`) & Financial Integrity
- [ ] `DIO` and `DPO` use `COGS` / material spend denominators while `DSO` uses Revenue (`365`-day convention stated explicitly) with zero denominator mixing.
- [ ] Inventory carrying-cost rate (`WACC` + storage + insurance + obsolescence/shrinkage) is explicitly parameterized on the service-vs.-cash efficient frontier.
- [ ] Expedite air-freight, lost-margin stockouts, and changeover costs are netted honestly against inventory reduction claims.

## 4. Verification, Alignment & Commercial Governance Hygiene
- [ ] All pooling, bullwhip, `TTS`/`TTR`, and `C2C` models were executed deterministically via Python (`run_command`).
- [ ] Frozen, slushy, and liquid `S&OP` planning time fences align quantitatively with manufacturing setup and supplier procurement lead times.
- [ ] Incentive alignment across Sales, Procurement, Manufacturing, and Logistics eliminates KPI conflicts (e.g., `PPV` vs. `EOQ` inventory bloat).
- [ ] Scope 3 logistics/supply-chain carbon impacts are flagged for cross-domain review where regionalization or air-freight trade-offs apply.
- [ ] Antitrust, sanctions, and forced-labor (`UFLPA` / `CSDDD`) guardrails are respected across all network restructuring options.
- [ ] Service-level tiering differentiates contractual SLA penalty exposure across strategic vs. transactional customer segments.
- [ ] Capital expenditure (`CapEx`) vs. Third-Party Logistics (`3PL` variable `OpEx`) option value is evaluated across demand downside scenarios.
- [ ] Verified ERP/financial actuals vs. scenario priors are separated transparently in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] **Mandatory Human Approval** gate blocks execution of facility restructurings, supplier terminations, or binding `S&OP` financial commitments.
