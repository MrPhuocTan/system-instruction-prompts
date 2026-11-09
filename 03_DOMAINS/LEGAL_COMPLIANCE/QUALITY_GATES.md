# Domain 07: Legal & Compliance (`LEGAL_COMPLIANCE`) — Mandatory Quality Gates

Every deliverable produced by any role in `03_DOMAINS/LEGAL_COMPLIANCE/` must pass all **7 Domain Quality Gates** below prior to [`DOMAIN_LEAD`](../../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md), `SA`, and `PM` sign-off under [`REVIEW_AND_SIGNOFF.md`](../../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md) and [`INDEPENDENT_VERIFICATION.md`](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md). Failure on any gate blocks delivery (`STATUS = BLOCKED` or `FAILED`).

---

## Gate 1: Applicable Jurisdiction & Choice-of-Law Identification
- **Pass Criteria:**
  1. Governing law, forum/venue, and regulatory territorial reach (e.g., Delaware corporate law, New York commercial contract law, EU GDPR Art. 3 extraterritorial scope, California CPRA, U.S. Federal Circuit patent law) are explicitly stated in the header or scope section.
  2. Conflict-of-laws rules, mandatory local public-policy overrides (such as non-waivable statutory consumer, employment, or data-subject protections), and cross-border enforcement constraints are surfaced whenever parties or operations span multiple jurisdictions.
- **Fail Condition:** Applying generic common-law or statutory assumptions without naming the jurisdiction, or applying one jurisdiction's statute to an out-of-scope entity without analyzing territorial applicability triggers.

## Gate 2: Current Authoritative Primary Sources & Zero Fabricated Citations
- **Pass Criteria:**
  1. Every cited statute, regulation, treaty article, administrative rule, or judicial decision includes exact title/code section or case identifier, issuing court/agency, and enactment/decision year, verified against workspace files (`read_file`) or authoritative official portals (`search_web`).
  2. Effective dates, sunset clauses, transition grace periods, and statutory amendments are checked for currency.
  3. Any citation whose full text or citator history ("good law" status) could not be independently verified due to paywall/offline constraints is explicitly labeled `[UNVERIFIED - REQUIRES CITATOR/REPORTER CHECK]`.
- **Fail Condition:** Any fabricated, misquoted, repealed, or hallucinated case name, docket number, reporter citation, or statutory provision (`ZERO TOLERANCE` immediate `FAILED` status).

## Gate 3: Contractual Clause Precision & Cross-Reference Integrity
- **Pass Criteria:**
  1. All capitalized Defined Terms match exact definitions in the agreement's definitions section or master agreement without orphan, circular, or inconsistent capitalization.
  2. Redlines reconcile interdependent clauses across the entire instrument: Limitation of Liability caps/super-caps <-> Indemnification obligations <-> Confidentiality/Data Protection breaches <-> IP infringement carve-outs <-> Insurance minimums <-> Termination & Survival clauses.
  3. Vague obligations ("promptly", "reasonable efforts", "appropriate measures") are either anchored to objective SLAs/deadlines/standards or explicitly flagged with their ambiguity trade-off.
- **Fail Condition:** Modifying an isolated section while creating a contradiction in survival, liability carve-outs, order-of-precedence schedules, or defined terms.

## Gate 4: Legal Uncertainty, Split-of-Authority & Ambiguity Disclosure
- **Pass Criteria:**
  1. Unsettled legal questions, conflicting appellate/supervisory interpretations, pending rulemaking, and missing factual predicates are explicitly segregated from settled black-letter requirements.
  2. Where outcome depends on unverified facts (e.g., transaction value thresholds, employee headcount, data volume, patent claim construction), conditional branches (`If Fact X -> Rule A; If Fact Y -> Rule B`) are documented clearly.
- **Fail Condition:** Presenting a contested legal interpretation, split authority, or fact-contingent standard as an unconditional legal certainty.

## Gate 5: Structured Legal & Regulatory Risk Tiering
- **Pass Criteria:**
  1. Every identified legal, contractual, compliance, privacy, or IP issue is assigned an explicit risk tier (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`) supported by statutory penalty ceilings, litigation/injunction exposure, commercial uncapped-liability risk, or operational business blockage.
  2. Each `CRITICAL` and `HIGH` risk includes a concrete, actionable remediation path (exact fallback redline text, required compliance control, licensing alternative, or escalation decision).
- **Fail Condition:** Unranked laundry lists of issues without severity differentiation, rationale, or actionable mitigation language.

## Gate 6: Privilege, Confidentiality & Data Redaction Protection
- **Pass Criteria:**
  1. Zero confidential party names, unredacted PII/PHI, MNPI, proprietary source code, or privileged litigation strategy fragments are transmitted to external web searches (`search_web`) or exposed in unredacted logs per [`SECURITY_AND_PRIVACY.md`](../../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md).
  2. Record-retention and legal-hold preservation duties are respected across all recommended remediation steps.
- **Fail Condition:** Exposing sensitive client/counterparty identifiers in external queries or recommending deletion of regulated audit/evidentiary records.

## Gate 7: Mandatory Qualified Legal Counsel Review Gate
- **Pass Criteria:**
  1. Deliverable includes a prominent, specific sign-off boundary noting that the output constitutes non-binding legal/compliance decision-support analysis and requires review and approval by qualified, licensed legal counsel in the applicable jurisdiction(s) prior to contract execution, regulatory filing, public disclosure, or binding operational reliance per [`HUMAN_APPROVAL_POLICY.md`](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md).
- **Fail Condition:** Framing output as formal legal representation or instructing autonomous execution of legally binding instruments without human counsel sign-off.

---

## Domain Sign-Off Summary Table (Required in Handoff)

| Gate ID | Gate Name | Verification Evidence Required | Gate Status |
| :--- | :--- | :--- | :--- |
| `LEG-G1` | Jurisdiction & Choice-of-Law | Named governing law, forum, and territorial trigger check | `PASS / BLOCKED / FAILED` |
| `LEG-G2` | Primary Sources & Zero Fabrication | Verified source paths/URLs + explicit `[UNVERIFIED]` ledger | `PASS / BLOCKED / FAILED` |
| `LEG-G3` | Clause Precision & Cross-References | Defined-term and interdependent-clause reconciliation audit | `PASS / BLOCKED / FAILED` |
| `LEG-G4` | Uncertainty & Split Disclosure | Explicit settled-vs-unsettled and factual-assumption ledger | `PASS / BLOCKED / FAILED` |
| `LEG-G5` | Risk Tiering & Mitigations | Severity ratings (`CRITICAL`–`LOW`) + concrete fallback/controls | `PASS / BLOCKED / FAILED` |
| `LEG-G6` | Privilege & Confidentiality | Sanitized external query check + PII/secret redaction check | `PASS / BLOCKED / FAILED` |
| `LEG-G7` | Qualified Legal Counsel Gate | Explicit human counsel review checkpoint documented | `PASS / BLOCKED / FAILED` |
