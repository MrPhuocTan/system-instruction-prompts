# Quality Checklist: Privacy Specialist — Legal & Regulatory (`ROLE-LEG-004`)

Pre-handoff verification checklist aligned with [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) and [`QUALITY_GATES.md`](../../QUALITY_GATES.md). Every item must pass before handoff.

## 1. Jurisdictional Reach, Role Characterization & Scope Boundary
- [ ] Territorial applicability triggers (GDPR Art. 3 establishment/targeting, CCPA/CPRA thresholds, HIPAA Covered Entity/Business Associate status, LGPD/PIPL reach) are explicitly verified.
- [ ] Party status (Controller, Joint Controller, Processor, Sub-processor; CPRA Business, Service Provider, Contractor, Third Party) is grounded in factual decision-making over purposes and means.
- [ ] Legal/regulatory privacy scope (`LEGAL_COMPLIANCE/ROLES/PRIVACY_SPECIALIST`) is cleanly separated from technical privacy engineering (`CYBERSECURITY/ROLES/PRIVACY_SPECIALIST`), with explicit handoff notes where technical PETs or Annex II TOMs are needed.

## 2. Lawful Basis, DPIA & Data Lifecycle Completeness
- [ ] Every distinct processing purpose maps to an explicit lawful basis (e.g., GDPR Art. 6(1)(a)–(f), plus Art. 9(2) condition where special-category/biometric/health data is involved) and a bounded retention schedule.
- [ ] Where Legitimate Interests (`Art. 6(1)(f)`) is invoked, a 3-step LIA (legitimate purpose, strict necessity, balancing against data-subject expectations/rights) is documented.
- [ ] High-risk processing (profiling, automated decision-making under Art. 22, large-scale sensitive data, systematic monitoring, vulnerable subjects/minors, AI model training on personal data) includes full DPIA risk scoring and residual-risk mitigations.
- [ ] Pseudonymous identifiers (hashed emails, user IDs, IP addresses, device fingerprints) are never misclassified as anonymous non-personal data.

## 3. Cross-Border Transfers, DPAs, DSARs & Transparency
- [ ] Cross-border transfers map to exact legal instruments (Adequacy / DPF, 2021 EU SCCs with exact Module 1–4 pinned, UK IDTA/Addendum, PIPL mechanism) plus TIA supplementary measures where required.
- [ ] DPA review verifies GDPR Art. 28(3) / CPRA mandatory clauses: documented instructions, confidentiality, security TOMs, sub-processor authorization/flow-down, audit rights, DSAR assistance, breach notice SLA, and post-termination deletion/return.
- [ ] Consent and opt-out UX specifications prohibit dark patterns and preserve symmetric withdraw/reject frictionless parity (including Global Privacy Control [GPC] signal recognition where CPRA applies).

## 4. Citation Currency, Redaction & DPO / Counsel Sign-Off
- [ ] Supervisory guidance and statutory citations are current and verified (`0` fabricated articles, recitals, or enforcement fines; unverified items tagged `[UNVERIFIED]`).
- [ ] Zero real data-subject PII/PHI or incident victim records appear in external queries or unredacted artifacts.
- [ ] Explicit DPO and qualified privacy legal counsel sign-off checkpoint is included prior to publishing notices, signing DPAs/SCCs, or notifying regulators/individuals of a breach.
- [ ] Deliverable contains zero emojis, zero unfinished placeholders, and 100% valid relative Markdown links.

## 5. Pre-Handoff Independent Verification Summary

| Verification Dimension | Evidence Inspected | Status |
| :--- | :--- | :--- |
| Territorial Scope & Controller/Processor Role | GDPR/CPRA/HIPAA/LGPD/PIPL triggers + factual role characterization | `PASS / BLOCKED / FAILED` |
| Legal vs. Cybersecurity Scope Separation | Governance/DPIA/SCC scope distinct from technical PET engineering | `PASS / BLOCKED / FAILED` |
| Lawful Basis, LIA/DPIA & Retention Bounds | Art. 6/9 basis, risk balancing, and retention mapped per purpose | `PASS / BLOCKED / FAILED` |
| Cross-Border SCC Module & DPA Completeness | Exact SCC Module (1–4), TIA, and Art. 28 clauses reconciled | `PASS / BLOCKED / FAILED` |
| DPO / Privacy Legal Counsel Sign-Off Gate | Human DPO/counsel sign-off required prior to notice/filing/execution | `PASS / BLOCKED / FAILED` |
