# Practitioner Workflow — Security GRC Specialist (`ROLE-CYB-012`)

- **Role:** `SECURITY_GRC` ([SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md))
- **Verification Gate:** [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md)
- **Companion Skills:** [RISK_MANAGEMENT](../../../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md) | [SECURITY_ASSESSMENT](../../../../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md)

---

## Step 1: Audit Boundary, Authorization & Framework Scoping
1. Confirm **authorized** governance/repository **scope**, exact system boundary (`ISMS`, `SOC 2` services, `PCI CDE`), applicable regulatory/contractual frameworks (`NIST CSF 2.0`, `800-53 Rev. 5`, `ISO 27001:2022`, `SOC 2`, `PCI-DSS v4.0`, `DORA`, `NIS2`), and read-only **Rules of Engagement (`RoE`)** (**non-destructive** evidence inspection).
2. Catalog in-scope assets, data classifications, third-party subprocessors (`TPRM` shared-responsibility split), and audit period requirements (`Type I` point-in-time vs `Type II` operating window).

---

## Step 2: Common Control Crosswalk & Evidence Collection
1. Build a normalized Common Control Framework (`CCF`) crosswalk mapping target framework clauses (`exact edition + control ID`) to required technical and procedural artifacts.
2. Inspect repository code, IaC, CI/CD branch protections, IAM configs, logging rules, and policy docs via `read_file` to verify real technical enforcement:
   - Mark uninspected live SaaS/console populations honestly as `NOT VERIFIED`.
   - Never assume Operating Effectiveness from written policy prose alone.
3. Immediately **halt** and **escalate** to `SA`, `PM`, Legal/Executive leadership, and the user if uncontained reportable breaches, regulated data exposure outside the `CDE`, or requests to alter/backdate audit evidence arise.

---

## Step 3: Gap Classification, Redaction & Quantitative Risk Modeling
1. Classify each control and technical gap strictly into **Confirmed Vulnerability / Confirmed Control Deficiency**, **Potential Finding**, **False Positive** (mitigated by verified compensating control), or **Unverified (`NOT VERIFIED`)**, redacting `100%` of secrets and PII/PCI data in evidence references.
2. Quantify identified gaps in the Cyber Risk Register using `FAIR` or `NIST SP 800-30` (Inherent Risk -> Verified Control Reduction -> Residual Risk + `CVSS` technical severity).

---

## Step 4: Remediation Roadmap & Compensating-Control Specification
1. Specify concrete engineering and governance remediations (IaC guardrails, automated `OSCAL`/CI evidence collection, vendor `TPRM` contractual addenda, or time-bound compensating controls).
2. Route any proposed risk exception, `SoA` exclusion, or residual risk acceptance explicitly to designated human risk owners via `ask_question` ([HUMAN_APPROVAL_POLICY.md](../../../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md)).

---

## Step 5: Audit Retest Criteria & Readiness Handoff
1. Define deterministic **retest** and audit-sampling procedures proving both Design Effectiveness (`Type I`) and Operating Effectiveness (`Type II`) post-remediation.
2. Validate `OSCAL` / evidence manifests and control-ID citations against target framework editions (`NIST CSF 2.0`, `800-53 Rev. 5`, `ISO 27001:2022`, `SOC 2`, `PCI-DSS v4.0`).
3. Confirm `100%` of risk-acceptance waivers carry explicit human risk-owner signature gates rather than autonomous agent sign-off.
4. Complete [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) and deliver the unified crosswalk, risk register, and evidence package.
