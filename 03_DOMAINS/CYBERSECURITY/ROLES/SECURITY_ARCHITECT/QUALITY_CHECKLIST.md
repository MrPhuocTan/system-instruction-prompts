# Quality Checklist — Security Architect (`ROLE-CYB-001`)

Use this pre-handoff checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md), [WORKFLOW.md](./WORKFLOW.md), and [QUALITY_GATES.md](../../QUALITY_GATES.md).

---

## 1. Authorization, Scope & Rules of Engagement (`RoE`)
- [ ] Workspace/system target **scope** (`repositories`, `services`, `environments`) and documented **authorization** / **Rules of Engagement (`RoE`)** were verified prior to inspection.
- [ ] All architectural validation remained strictly **non-destructive**; zero unauthorized active probing, exploitation, or out-of-scope network contact occurred.
- [ ] Separation of duties was enforced (no self-certification of independent pentest or compliance sign-off on Level 3–4 engagements).

---

## 2. Threat Model & Zero-Trust Completeness
- [ ] Data-Flow Diagrams (`DFDs`) enumerate all external actors, internal services, asynchronous queues, data stores, CI/CD control planes, and trust boundaries.
- [ ] Every trust-boundary crossing specifies mutual authentication (`TLS 1.3` / `mTLS` / workload identity), fine-grained authorization (`PDP`/`PEP`), and fail-closed error semantics.
- [ ] `STRIDE` / `PASTA` threats cover multi-tenant isolation, privilege escalation, replay/downgrade attacks, supply-chain dependencies, and secret/key compromise scenarios.
- [ ] Cryptographic specs mandate authenticated encryption (`AES-256-GCM` / `ChaCha20-Poly1305`), `KMS`/`HSM` envelope key management, rotation schedules, and zero hardcoded secrets.
- [ ] Availability, key-recovery, and P99 latency trade-offs are documented so security controls do not induce operational fragility.

---

## 3. Evidence Quality, Epistemic Classification & Secret Redaction
- [ ] Every architectural gap or design defect cites exact repository `file:line` paths, IaC resources, or API specifications.
- [ ] Observations are strictly categorized as **Confirmed Vulnerability**, **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)**.
- [ ] Severity ratings pair valid `CVSS v3.1/v4.0` vectors with contextual business/asset exposure rationale.
- [ ] `100%` of live credentials, cryptographic keys, tokens, internal customer identifiers, and PII/PHI are redacted across all diagrams, tables, and `ADRs`.

---

## 4. Actionable Remediation & Retest Guidance
- [ ] Each high/medium threat maps to concrete preventive, detective, and corrective controls (`NIST SP 800-53` / `OWASP ASVS`) rather than generic advisories.
- [ ] Remediations define deterministic **retest** / acceptance verification criteria (negative boundary integration tests + policy-as-code checks) for downstream QA.
- [ ] Residual architectural risks or policy exceptions are explicitly flagged for human risk-owner approval rather than silently accepted.
