# Quality Checklist — Technical Privacy Specialist (`ROLE-CYB-013`)

Verify every item prior to handoff and `SA_GATE` sign-off per [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md), [WORKFLOW.md](./WORKFLOW.md), and [QUALITY_GATES.md](../../QUALITY_GATES.md).

---

## 1. Authorization, Scope, Synthetic-Data Safety & Legal Boundary (`RoE`)
- [ ] Repository/schema/pipeline **scope** and **authorization** / **Rules of Engagement (`RoE`)** were verified prior to inspection.
- [ ] All checks remained strictly **non-destructive** and operated on schemas or synthetic (`RFC 2606` / fake) fixtures—zero real production PII/SPI/PHI was queried, copied, or exposed.
- [ ] Deliverables clearly distinguish technical privacy engineering (`ISO 27701` / `NIST Privacy Framework`) from formal legal counsel.
- [ ] High-risk `DPIA` sign-offs and statutory legal interpretations are routed strictly to the human DPO/Legal Counsel.

---

## 2. Data-Flow, `LINDDUN`, `PETs` & `DSAR` Completeness
- [ ] Data-flow / `RoPA` mapping covers collection endpoints, client SDKs/cookies, primary DBs, caches, event queues, logs/APM, analytics lakes, AI/LLM pipelines, backups, and third-party subprocessors.
- [ ] De-identification controls rigorously separate reversible pseudonymization (`KMS`-peppered `HMAC` / tokenization) from true anonymization ($k$-anonymity, $l$-diversity, Differential Privacy $\epsilon, \delta$), rejecting plain unsalted hashes (`SHA-256(email)`).
- [ ] Consent/purpose gates verify zero pre-consent third-party tracker firing and honor `GPC`/opt-out signals.
- [ ] `DSAR` deletion/crypto-shredding cascades cover all downstream stores and enforce statutory retention TTLs.

---

## 3. Epistemic Classification, Risk Scoring & Redaction
- [ ] Privacy defects are strictly classified into **Confirmed Vulnerability / Confirmed Privacy Gap**, **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)**, with `LINDDUN` + `CVSS`/contextual data-subject harm scoring.
- [ ] `100%` of real PII, SPI, PHI, credentials, and session identifiers are redacted across all artifacts.

---

## 4. Actionable Remediation & Retest Verification
- [ ] Remediations provide concrete schema migrations, structured-logger PII scrubbers, consent-enforcement middleware, or `DSAR` tombstone/crypto-shredding specs.
- [ ] Deterministic **retest** verification confirms zero PII leakage in logs/network beacons prior to consent and `100%` target record erasure/redaction across `DSAR` test runs.
