# Quality Checklist — Domain Lead (`ROLE-CORE-003`)

## 1. Wave 0 Domain Framing & Specialist Selection Checks
- [ ] **Canonical Domain Standards Loaded**
  - Active `03_DOMAINS/<DOMAIN>/DOMAIN_INDEX.md`, `DOMAIN_SYSTEM_PROMPT.md`, and `QUALITY_GATES.md` inspected directly via `read_file` for every domain in scope.
- [ ] **Authentic Specialist Role Mapping**
  - Assigned worker roles match exact sub-disciplinary requirements (e.g., `VALUATION_SPECIALIST` vs. `ACCOUNTING_SPECIALIST`; `CLINICAL_RESEARCHER` vs. `PATIENT_SAFETY_REVIEWER`) with zero incompatible role co-location.
- [ ] **Domain Invariants Locked in Contracts**
  - Units, currencies, statistical/evaluation protocols, regulatory baselines, citation standards, and `RoE` safety boundaries explicitly written into [`WORKSTREAM_CONTRACT.md`](../../06_TEMPLATES/WORKSTREAM_CONTRACT.md) before Wave 2 starts.
- [ ] **Multi-Domain Conflict Resolution Verified**
  - Where `2+` domains intersect, permitted actions reflect the strictest safety/regulatory intersection and verification gates include the union of all active `QUALITY_GATES.md` checks.
- [ ] **Domain Risk Register Populated**
  - Domain-specific hazards, assumption sensitivities, and human-approval triggers logged in [`RISK_REGISTER.md`](../../06_TEMPLATES/RISK_REGISTER.md).

## 2. In-Flight Methodological Governance Checks
- [ ] **Zero Cross-Stream Convention Drift**
  - Shared domain definitions (date horizons, inflation bases, coordinate frames, ontology codes, or risk thresholds) remain synchronized across parallel batches.
- [ ] **Tool & Environment Realism Confirmed**
  - Any unavailable physical lab instrument, proprietary data feed, or industrial controller is explicitly accounted for via simulation or operator protocol per [`TOOL_USAGE_AND_LIMITATIONS.md`](../../00_GLOBAL_CONSTITUTION/TOOL_USAGE_AND_LIMITATIONS.md).
- [ ] **Instruction Hierarchy Subordination Preserved**
  - Domain guidelines tighten methodological rigor without weakening `Level 1`–`Level 3` constitutional or authorization rules.

## 3. Wave 3 Domain Gate & Epistemic Rigor Checks
- [ ] **Domain Methodology Soundness**
  - Deliverables satisfy core disciplinary invariants (zero train/test leakage, balanced accounting identities, valid experimental controls, defensible threat models, or physical safety margins).
- [ ] **Primary-Source & Citation Integrity**
  - Every referenced standard, statute, clinical guideline, RFC, or research paper verified against authoritative sources; zero fabricated citations or guessed clause numbers.
- [ ] **Calibrated Uncertainty & Scope Framing**
  - Sensitivity bounds, confidence intervals, model limitations, and non-substitution disclaimers (legal, medical, financial, safety) stated clearly without hedging filler.
- [ ] **100% Domain Quality Gate Pass**
  - Every applicable item in `03_DOMAINS/<DOMAIN>/QUALITY_GATES.md` and active role `QUALITY_CHECKLIST.md` files empirically verified and recorded prior to `SA_GATE` and `PM_GATE`.
