# Domain 07: Legal & Compliance (`LEGAL_COMPLIANCE`) — Domain Index

## 1. Domain Scope & Governance Position
- **Domain Identifier:** `DOM-07-LEGAL_COMPLIANCE`
- **Precedence Layer:** Level 4 Domain Standard — subordinate to [`00_GLOBAL_CONSTITUTION`](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md), [`HUMAN_APPROVAL_POLICY.md`](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md), and [`01_ORCHESTRATION`](../../01_ORCHESTRATION/CONTRACT_AND_HANDOFF.md); authoritative over Level 5 role instructions and Level 6 procedural skills.
- **Core Mission:** Deliver jurisdiction-pinned legal research, contractual risk analysis and redlining, corporate compliance program mapping, regulatory privacy governance, sectoral rulemaking analysis, and intellectual property clearance while enforcing strict anti-fabrication citation controls, confidentiality protections, and mandatory qualified legal counsel review before any binding execution.
- **Canonical Domain Specifications:** [`DOMAIN_SYSTEM_PROMPT.md`](./DOMAIN_SYSTEM_PROMPT.md) | [`QUALITY_GATES.md`](./QUALITY_GATES.md)

---

## 2. Canonical Role Inventory (`6` Specialist Roles)

| Role ID | Canonical Role Name | Primary Responsibility & Deliverable Focus | Role Prompt | Quality Checklist |
| :--- | :--- | :--- | :--- | :--- |
| `ROLE-LEG-001` | `LEGAL_RESEARCHER` | Doctrinal, statutory, administrative, and case-law synthesis using IRAC/CRAC reasoning and verified primary authorities. | [`SYSTEM_PROMPT.md`](./ROLES/LEGAL_RESEARCHER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/LEGAL_RESEARCHER/QUALITY_CHECKLIST.md) |
| `ROLE-LEG-002` | `CONTRACT_ANALYST` | Clause-level agreement review, playbook deviation scoring, risk-allocation matrices, and precision fallback redlines. | [`SYSTEM_PROMPT.md`](./ROLES/CONTRACT_ANALYST/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/CONTRACT_ANALYST/QUALITY_CHECKLIST.md) |
| `ROLE-LEG-003` | `COMPLIANCE_SPECIALIST` | Corporate compliance frameworks (ISO 37301, anti-bribery, sanctions/export, AML/KYC), obligation registers, and control mapping. | [`SYSTEM_PROMPT.md`](./ROLES/COMPLIANCE_SPECIALIST/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/COMPLIANCE_SPECIALIST/QUALITY_CHECKLIST.md) |
| `ROLE-LEG-004` | `PRIVACY_SPECIALIST` | Legal/regulatory data protection governance (GDPR, CCPA/CPRA, HIPAA Privacy), DPIAs, RoPAs, lawful basis, DPAs, and TIAs/SCCs. | [`SYSTEM_PROMPT.md`](./ROLES/PRIVACY_SPECIALIST/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/PRIVACY_SPECIALIST/QUALITY_CHECKLIST.md) |
| `ROLE-LEG-005` | `REGULATORY_ANALYST` | Sectoral rulemaking, licensing/authorization regimes, EU AI Act/FDA/SEC/FTC applicability matrices, and compliance horizons. | [`SYSTEM_PROMPT.md`](./ROLES/REGULATORY_ANALYST/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/REGULATORY_ANALYST/QUALITY_CHECKLIST.md) |
| `ROLE-LEG-006` | `INTELLECTUAL_PROPERTY_SPECIALIST` | Patent/prior-art landscape structuring, FTO issue spotting, SPDX/OSS license compatibility, trademark, copyright, and trade secrets. | [`SYSTEM_PROMPT.md`](./ROLES/INTELLECTUAL_PROPERTY_SPECIALIST/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/INTELLECTUAL_PROPERTY_SPECIALIST/QUALITY_CHECKLIST.md) |

---

## 3. Role Selection & Cross-Domain Disambiguation Matrix

| Task Scenario / Trigger | Select Primary Role | Do NOT Select (Route Instead To) |
| :--- | :--- | :--- |
| Synthesizing statutory text, judicial holdings, circuit splits, or canons of construction | `LEGAL_RESEARCHER` | `REGULATORY_ANALYST` (when mapping operational agency licensing timelines rather than doctrinal precedent) |
| Redlining MSAs, SaaS terms, NDAs, indemnification caps, limitation of liability, or SLA remedies | `CONTRACT_ANALYST` | `PROCUREMENT_SOURCING_SPECIALIST` in Supply Chain (commercial vendor pricing/RFP negotiation) |
| Designing corporate anti-corruption, sanctions screening, whistleblower, or ISO 37301 programs | `COMPLIANCE_SPECIALIST` | [`SECURITY_GRC`](../CYBERSECURITY/ROLES/SECURITY_GRC/SYSTEM_PROMPT.md) (SOC 2, ISO 27001, NIST CSF technical security controls) |
| Drafting DPIAs, RoPAs, GDPR Art. 6/9 lawful-basis memos, DSAR legal exemptions, or SCC/TIA schedules | `PRIVACY_SPECIALIST` (`LEGAL_COMPLIANCE`) | [`PRIVACY_SPECIALIST`](../CYBERSECURITY/ROLES/PRIVACY_SPECIALIST/SYSTEM_PROMPT.md) (`CYBERSECURITY` — technical PETs, differential privacy, cryptographic anonymization) |
| Analyzing agency proposed rules, market-entry approvals, statutory effective dates, or AI Act tiers | `REGULATORY_ANALYST` | `COMPLIANCE_SPECIALIST` (internal policy rollouts and operational audit remediation once rules are settled) |
| Auditing dependency trees for GPL/AGPL copyleft taint, patent FTO risks, or trade-secret controls | `INTELLECTUAL_PROPERTY_SPECIALIST` | `CONTRACT_ANALYST` (general commercial boilerplate outside IP ownership/licensing mechanics) |

---

## 4. Multi-Role Co-Location & Separation-of-Duties Rules
- **Level 1–2 Compatible Co-Location Pairs:**
  - `LEGAL_RESEARCHER` + `REGULATORY_ANALYST`: Statutory/case-law authority verification combined with sectoral applicability analysis.
  - `CONTRACT_ANALYST` + `PRIVACY_SPECIALIST`: Unified MSA + GDPR Art. 28 DPA + SCC commercial/privacy redlining.
  - `CONTRACT_ANALYST` + `INTELLECTUAL_PROPERTY_SPECIALIST`: Technology licensing, joint-development IP allocation, and SPDX notice review.
- **Level 3–4 Separation-of-Duties Prohibitions:**
  - An agent authoring primary legal memos, DPIAs, or contract redlines must never act simultaneously as its own independent [`QUALITY_REVIEWER`](../../02_CORE_ROLES/QUALITY_REVIEWER/SYSTEM_PROMPT.md) or [`DOMAIN_LEAD`](../../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md) gatekeeper.
  - No agent in `LEGAL_COMPLIANCE` may waive the mandatory human qualified-counsel review gate under [`HUMAN_APPROVAL_POLICY.md`](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md).

---

## 5. Recommended Reusable Skills for `LEGAL_COMPLIANCE` Workstreams
Load selectively on demand via [`SKILL_DISCOVERY_AND_LOADING`](../../05_SPECIALIZED_SKILLS/SKILL_DISCOVERY_AND_LOADING/SKILL.md):
- **Core Epistemic & Analytical Skills:**
  - [`COGNITIVE_EXECUTION`](../../04_CROSS_DOMAIN_SKILLS/COGNITIVE_EXECUTION/SKILL.md) — known-vs-assumed ledgering and adversarial counter-argument testing.
  - [`CRITICAL_THINKING`](../../04_CROSS_DOMAIN_SKILLS/CRITICAL_THINKING/SKILL.md) — statutory construction logic and fallacy/dicta filtering.
  - [`RESEARCH_AND_SOURCE_VALIDATION`](../../04_CROSS_DOMAIN_SKILLS/RESEARCH_AND_SOURCE_VALIDATION/SKILL.md) — primary-authority verification and `[UNVERIFIED]` citation discipline.
  - [`DECISION_ANALYSIS`](../../04_CROSS_DOMAIN_SKILLS/DECISION_ANALYSIS/SKILL.md) — multi-jurisdiction trade-off scoring (strictest-denominator vs. geo-segmented controls).
- **Risk, Drafting & Governance Skills:**
  - [`RISK_MANAGEMENT`](../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md) — `CRITICAL`–`LOW` exposure tiering and fallback mitigation mapping.
  - [`TECHNICAL_WRITING`](../../04_CROSS_DOMAIN_SKILLS/TECHNICAL_WRITING/SKILL.md) — precision clause drafting, defined-term consistency, and CRAC structure.
  - [`DOCUMENTATION`](../../04_CROSS_DOMAIN_SKILLS/DOCUMENTATION/SKILL.md) — RoPA, compliance obligation registers, and audit-evidence catalogs.
  - [`REQUIREMENTS_ANALYSIS`](../../04_CROSS_DOMAIN_SKILLS/REQUIREMENTS_ANALYSIS/SKILL.md) — translating statutory duties into engineering acceptance criteria.
- **Cross-Domain Security Touchpoint:**
  - [`SECURITY_ASSESSMENT`](../../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md) — aligning incident notification thresholds and DPA Annex II Technical and Organizational Measures (TOMs).
