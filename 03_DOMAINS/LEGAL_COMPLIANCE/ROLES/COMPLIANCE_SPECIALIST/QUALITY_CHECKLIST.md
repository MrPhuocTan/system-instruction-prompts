# Quality Checklist: Compliance Specialist (`ROLE-LEG-003`)

Pre-handoff verification checklist aligned with [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) and [`QUALITY_GATES.md`](../../QUALITY_GATES.md). Every item must pass before handoff.

## 1. Jurisdictional Scope & Framework Alignment
- [ ] Operating jurisdictions, industry sectors, government/public-official touchpoints, and cross-border trade/payment flows are explicitly documented.
- [ ] Applicable statutory regimes (e.g., FCPA, UKBA, OFAC/EU sanctions, EAR/ITAR, AMLD/BSA, UFLPA/CSDDD) and CMS standards (ISO 37301, ISO 37001, DOJ ECCP) are accurately pinned with currency verified.
- [ ] Intersections or conflicts between extraterritorial obligations and local national laws (blocking statutes, labor/privacy limits on monitoring) are explicitly flagged for legal counsel.

## 2. Obligation-to-Control Traceability & Auditability
- [ ] Every statutory or regulatory obligation in scope maps deterministically to: (a) Policy Clause, (b) Preventative Control, (c) Detective Control, (d) Accountable Role/Owner, and (e) Verifiable Evidence Artifact.
- [ ] Zero "paper-only" abstract mandates exist without concrete operational thresholds, approval workflows, exception-escalation paths, and record-retention periods.
- [ ] Control boundaries with [`SECURITY_GRC`](../../../CYBERSECURITY/ROLES/SECURITY_GRC/SYSTEM_PROMPT.md) and [`PRIVACY_SPECIALIST`](../PRIVACY_SPECIALIST/SYSTEM_PROMPT.md) are cleanly separated without gaps or conflicting ownership.

## 3. Risk Tiering, Third-Party Governance & CAPA Rigor
- [ ] Compliance gaps are rated (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`) based on statutory penalty exposure, enforcement likelihood, criminal/civil liability, and operational impact.
- [ ] Third-party/intermediary risk tiers (distributors, customs brokers, agents, suppliers) define proportional due diligence (CDD vs. EDD), beneficial-ownership checks, and audit/termination rights.
- [ ] Whistleblower/speak-up reporting channels enforce confidentiality, non-retaliation protections, and independent investigation routing.
- [ ] Corrective and Preventive Actions (CAPAs) define root-cause fixes, measurable acceptance criteria, target milestones, and re-audit verification steps.

## 4. Runtime Honesty, Confidentiality & Counsel Sign-Off
- [ ] Static policy/matrix analysis is clearly distinguished from live sanctions/PEP/export-list screening; any unverified statutory citation or list status is tagged `[UNVERIFIED]`.
- [ ] Zero internal investigation details, whistleblower identities, counterparty PII, or MNPI were leaked to `search_web` or unredacted outputs.
- [ ] Mandatory review and approval by qualified legal counsel / Chief Compliance Officer is explicitly required before policy enactment, high-risk counterparty clearance, or regulatory self-disclosure.
- [ ] Formatting contains zero emojis, zero unfinished placeholders, and 100% valid relative Markdown links.

## 5. Pre-Handoff Independent Verification Summary

| Verification Dimension | Evidence Inspected | Status |
| :--- | :--- | :--- |
| Statutory & CMS Standard Currency | ISO 37301/37001, DOJ ECCP, and statutory citations verified | `PASS / BLOCKED / FAILED` |
| Obligation-to-Control-to-Evidence Map | 100% of obligations linked to preventative/detective controls + logs | `PASS / BLOCKED / FAILED` |
| Third-Party CDD/EDD & Whistleblower Rules | Risk-proportional screening tiers and non-retaliation gates defined | `PASS / BLOCKED / FAILED` |
| Live Screening & Confidentiality Bounds | Static vs. live SDN/PEP feed disclosed; zero PII leaked externally | `PASS / BLOCKED / FAILED` |
| CCO / Qualified Legal Counsel Sign-Off | Human compliance/counsel approval gate documented prior to rollout | `PASS / BLOCKED / FAILED` |
