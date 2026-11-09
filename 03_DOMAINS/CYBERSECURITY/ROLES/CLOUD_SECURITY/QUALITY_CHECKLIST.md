# Quality Checklist — Cloud Security Engineer (`ROLE-CYB-009`)

Verify all items prior to handoff and `SA_GATE` sign-off per [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md), [WORKFLOW.md](./WORKFLOW.md), and [QUALITY_GATES.md](../../QUALITY_GATES.md).

---

## 1. Authorization, Scope & State/Lockout Safety (`RoE`)
- [ ] Cloud account/cluster/IaC repository **scope** and **authorization** / **Rules of Engagement (`RoE`)** were verified prior to inspection.
- [ ] All checks remained strictly **non-destructive**: zero unauthorized `terraform apply`/`destroy` mutations, zero out-of-scope cloud account queries, and mandatory human approval before any live cloud changes.
- [ ] Proposed IaC, KMS, bucket, and `SCP`/Org Policy patches were audited for `forces replacement` data-loss risk and admin/break-glass lockout prevention.
- [ ] Builder/auditor separation of duties was respected on Level 3–4 reviews.

---

## 2. Cloud, Container & Kubernetes Technical Depth
- [ ] Controls are evaluated against `CIS Cloud/Kubernetes Benchmarks`, `IMDSv2` enforcement, `KMS` customer-managed encryption, public-access blocks, private networking, and immutable multi-account audit logging.
- [ ] Workloads use short-lived OIDC/federated identities (`IRSA`, Workload Identity, `SPIFFE`) with zero hardcoded static cloud keys and least-privilege `Resource` + `Condition` scopes (including `iam:PassRole` checks).
- [ ] Container/Kubernetes specs enforce `restricted` Pod Security Standards (`runAsNonRoot`, `readOnlyRootFilesystem`, dropped capabilities, seccomp, no host-socket mounts, pinned/signed digests).

---

## 3. Epistemic Classification, Scoring & Redaction
- [ ] Findings strictly separate **Confirmed Vulnerability** (verified in IaC/config), **Potential Finding** (runtime drift unknown), **False Positive** (mitigated by upstream `SCP`/admission policy), and **Unverified (`NOT VERIFIED`)**.
- [ ] Severity ratings pair `CVSS v3.1/v4.0` vectors with multi-tenant/account blast-radius context.
- [ ] `100%` of cloud access keys, `.tfvars` secrets, state-file tokens, and PII are redacted across reports and diffs.

---

## 4. Policy-as-Code Remediation & Retest Verification
- [ ] Concrete IaC/manifest patches are paired with automated `OPA/Rego`, `Kyverno`, or `Checkov`/`Trivy` policy-as-code guardrails.
- [ ] Deterministic **retest** evidence confirms policy scanners and manifest validators pass on the remediated configs AND block insecure regression fixtures.
