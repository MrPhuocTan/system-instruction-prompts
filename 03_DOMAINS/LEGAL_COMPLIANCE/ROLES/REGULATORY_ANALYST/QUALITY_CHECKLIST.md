# Quality Checklist: Regulatory Analyst (`ROLE-LEG-005`)

Pre-handoff verification checklist aligned with [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) and [`QUALITY_GATES.md`](../../QUALITY_GATES.md). Every item must pass before handoff.

## 1. Jurisdictional, Sectoral & Operator Classification Precision
- [ ] Target geographic markets, sectoral regulators (e.g., EU AI Office / national market surveillance, FDA, SEC, FTC, EBA, FCA), and cross-border service delivery triggers are explicitly pinned.
- [ ] Statutory operator role (e.g., Provider, Deployer, Authorized Representative, Distributor, Controller, Issuer, Intermediary) is determined using exact statutory definitions.
- [ ] Both stated **Intended Purpose** and **Reasonably Foreseeable Misuse** / marketing claims were evaluated when determining risk tier or licensing thresholds.
- [ ] Statutory exemptions, R&D/sandbox exclusions, de minimis thresholds, and grandfathering rules were explicitly checked.

## 2. Primary Gazette Currency & Legal Force Separation
- [ ] Final enacted article/section numbers and annex references match the official published gazette/code (EUR-Lex Official Journal, CFR/Federal Register, national statute book)—never superseded legislative drafts.
- [ ] Every cited instrument is tagged with its exact legal status: `ENACTED & IN FORCE`, `ENACTED - PHASED TRANSITION`, `PROPOSED RULE / DRAFT`, or `NON-BINDING AGENCY GUIDANCE`.
- [ ] Zero fabricated regulation numbers, docket IDs, enforcement actions, or harmonized standard identifiers exist; any unavailable national transposition rule is marked `[UNVERIFIED]`.
- [ ] Staggered effective dates, grace periods, and reporting deadlines are broken out chronologically per obligation rather than lumped under a single enactment date.

## 3. Operational Translation & Risk Tiering
- [ ] Each applicable regulatory obligation is risk-tiered (`CRITICAL`–`LOW`) with statutory maximum penalties (e.g., percentage of global turnover, injunctions, market withdrawal) noted accurately.
- [ ] Regulatory mandates are translated into concrete engineering, documentation, human-oversight, logging, or conformity-assessment deliverables consumable by downstream `SA`, `IT_SOFTWARE`, `AI_MACHINE_LEARNING`, or `COMPLIANCE_SPECIALIST` workstreams.
- [ ] Unsettled agency interpretations, pending delegated acts, or missing harmonized technical standards are explicitly isolated in an Ambiguity & Regulatory Watch Ledger.

## 4. Confidentiality & Qualified Sectoral Counsel Gate
- [ ] Unreleased product roadmaps, proprietary algorithms, and client identifiers were excluded from external `search_web` queries.
- [ ] Deliverable explicitly requires formal sign-off by qualified sectoral legal/regulatory counsel prior to market launch, conformity declaration, licensing reliance, or regulator engagement.
- [ ] Formatting contains zero emojis, zero unfinished placeholders, and 100% valid relative Markdown links.

## 5. Pre-Handoff Independent Verification Summary

| Verification Dimension | Evidence Inspected | Status |
| :--- | :--- | :--- |
| Market, Agency & Statutory Operator Role | Target jurisdictions, agencies, and Provider/Deployer status pinned | `PASS / BLOCKED / FAILED` |
| Enacted Gazette vs. Draft/Guidance Status | Final Official Journal / CFR citations + phased dates verified | `PASS / BLOCKED / FAILED` |
| Intended Purpose & Foreseeable Misuse Check | Product claims and edge-case misuse evaluated against risk tiers | `PASS / BLOCKED / FAILED` |
| Engineering & Conformity Translation | Concrete technical, logging, oversight, and dossier duties mapped | `PASS / BLOCKED / FAILED` |
| Sectoral Legal Counsel Sign-Off Gate | Human regulatory counsel sign-off required before market reliance | `PASS / BLOCKED / FAILED` |
