# Quality Checklist — Security GRC Specialist (`ROLE-CYB-012`)

Verify every item prior to handoff and `SA_GATE` sign-off per [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md), [WORKFLOW.md](./WORKFLOW.md), and [QUALITY_GATES.md](../../QUALITY_GATES.md).

---

## 1. Authorization, Audit Scope & Independence (`RoE`)
- [ ] System/audit boundary **scope** (`SOC 2` boundary, `ISO 27001` `ISMS` scope, `PCI-DSS` `CDE`) and **authorization** / **Rules of Engagement (`RoE`)** were verified prior to evidence inspection.
- [ ] All evidence inspection remained strictly read-only and **non-destructive**; auditor separation of duties from control implementers was enforced on Level 3–4 reviews.
- [ ] Deliverables explicitly state they constitute technical readiness/governance engineering and NOT a formal CPA/Certification Body/QSA attestation.
- [ ] All residual risk acceptances, `SoA` exclusions, and policy waivers are routed strictly to authorized human risk owners.

---

## 2. Framework Precision, Operating Effectiveness & Classification
- [ ] Exact framework editions and clause IDs are cited accurately (`NIST CSF 2.0`, `NIST SP 800-53 Rev. 5`, `ISO/IEC 27001:2022`, `SOC 2`, `PCI-DSS v4.0.1`).
- [ ] Evaluations distinguish **Design Effectiveness** (`Type I` policy/config existence) from **Operating Effectiveness** (`Type II` sustained evidence over time), rejecting paper-only policies lacking technical enforcement.
- [ ] Deficiencies are strictly classified into **Confirmed Vulnerability / Confirmed Control Gap**, **Potential Finding**, **False Positive** (verified compensating control), or **Unverified (`NOT VERIFIED`)**.

---

## 3. Risk Quantification, Evidence Integrity & Secret Redaction
- [ ] Risk Register entries document threat actor/event, affected asset, inherent risk, verified controls, residual risk (`FAIR` / `NIST SP 800-30` + `CVSS` where technical), and explicit assumptions.
- [ ] `100%` of credentials, tokens, internal keys, and employee/customer PII/PCI data are redacted from all audit samples and crosswalks, with zero backdated or fabricated artifacts.

---

## 4. Actionable Remediation, Compensating Controls & Retest Guidance
- [ ] Every control gap maps to concrete technical/procedural remediations (or formal PCI/ISO compensating-control worksheets) with accountable owners.
- [ ] Deterministic audit **retest** criteria specify the exact configuration state, automated check (`OSCAL`/CI gate), and sample population required to verify closure.
