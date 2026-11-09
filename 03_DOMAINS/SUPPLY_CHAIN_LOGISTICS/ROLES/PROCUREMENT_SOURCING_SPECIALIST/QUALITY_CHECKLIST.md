# Quality Checklist — Procurement & Sourcing Specialist (`ROLE-SCM-004`)

Verify every item below before submitting a handoff report under [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md):

## 1. Landed `TCO` & Should-Cost Financial Accuracy
- [ ] Bottom-up should-cost separates raw material commodity content, conversion/machine burden, scrap allowance, packaging, SG&A, and margin.
- [ ] Landed `TCO` waterfall includes unit price, freight, insurance, customs duty (`FOB` vs. `CIF` valuation basis matched to importing jurisdiction!), port/brokerage fees, `MOQ` + pipeline + safety-stock carrying cost, and quality `COPQ`.
- [ ] Payment-term differences (`Net 30` vs. `Net 90`, early-pay `2/10 Net 30` APR!) are discounted accurately using stated buyer/supplier `WACC`.
- [ ] Foreign-exchange (`FX`), commodity indexation collar, and `+10–25%` tariff shock sensitivities were executed via `run_command`.

## 2. Kraljic Strategy, Supplier `HHI` & Dual-Source Optimization
- [ ] Vendor spend is normalized to ultimate corporate parents before computing `HHI` (scale `0–1.0` vs. `0–10,000` explicitly stated).
- [ ] Concentration audit checks **both Tier-1 legal entities AND shared sub-tier manufacturing sites, raw-material mines/fabs, and port chokepoints**.
- [ ] Dual-sourcing split (`e.g., 75/25`) quantifies incremental unit/tooling cost against expected single-source disruption loss ($\text{Outage Prob} \times \text{TTR} \times \text{Margin/Day}$).
- [ ] Supplier financial solvency, capacity headroom, and `OTIF`/`PPM` quality SLA remedies (tooling bailment, lead-time freeze fences) are specified.
- [ ] Combinatorial `RFx` award `MILP` model verifies `100%` demand coverage and respects supplier capacity/minimum-share constraints.

## 3. `Incoterms 2020`, Customs & Ethical Trade Compliance
- [ ] `Incoterms 2020` rule specifies exact **3-letter code + Named Place/Terminal + `"Incoterms 2020"`** and matches transport mode (`FCA`/`CIP`/`DAP` for containers; avoiding `FOB`/`CIF` container terminal traps and `EXW`/`DDP` customs pitfalls).
- [ ] Any `HS`/`HTS` tariff code or `FTA` Rules-of-Origin estimate is explicitly marked `PROVISIONAL — REQUIRES LICENSED CUSTOMS BROKER / LEGAL RULING`.
- [ ] Mandatory screening gates cover `OFAC`/`BIS`/`EU` sanctions, anti-bribery (`FCPA`), `UFLPA` / `EU CSDDD` forced-labor origin tracing, and `3TG` conflict minerals.

## 4. Confidentiality, Reproducibility & Commercial Governance
- [ ] All `TCO` waterfalls, `WACC` payment-term discounts, `HHI` indices, and `MILP` split awards were verified via Python (`run_command`).
- [ ] Tooling ownership, mold maintenance life, IP/NDA protection, and end-of-life last-time-buy (`LTB`) notice periods are specified in SLA terms.
- [ ] Supplier transition/qualification switching costs (`PPAP`/`FAI` lead time + safety buffer build) are netted against Year-1 unit savings.
- [ ] Competing supplier bid prices are kept strictly confidential with zero cross-bidder disclosure or anti-competitive signaling.
- [ ] Offline vs. live sanctions/tariff database timestamps are explicitly disclosed in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] Commercial SLA term sheets carry a clear non-legal-advice notice and escalate binding contract redlines to `LEGAL_COMPLIANCE`.
- [ ] **Mandatory Human Approval** gate blocks autonomous `RFx` release, supplier award notification, or live ERP `PO` creation.
