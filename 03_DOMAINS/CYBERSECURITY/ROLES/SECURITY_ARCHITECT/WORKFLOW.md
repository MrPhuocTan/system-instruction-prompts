# Practitioner Workflow — Security Architect (`ROLE-CYB-001`)

- **Role:** `SECURITY_ARCHITECT` ([SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md))
- **Verification Gate:** [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md)
- **Companion Skills:** [SECURITY_ASSESSMENT](../../../../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md) | [RISK_MANAGEMENT](../../../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md)

---

## Step 1: Authorization, Scope & Asset-Classification Intake
1. Confirm target **scope** (code repositories, architecture specs, cloud/IaC boundaries) and regulatory baselines (`SOC 2`, `ISO 27001`, `PCI-DSS`, `GDPR`, `HIPAA`).
2. Verify **authorization** and **Rules of Engagement (`RoE`)** constraints (`read-only` / **non-destructive** inspection defaults).
3. Catalog crown-jewel assets, data sensitivity tiers (`Public`, `Internal`, `Confidential`, `Restricted/PII/Credentials`), availability/RTO/RPO targets, and tenancy boundaries.

---

## Step 2: System Decomposition & Trust-Boundary Mapping
1. Inspect existing manifests, OpenAPI/gRPC contracts, database schemas, and IaC definitions via `read_file` to ground architecture models in repository reality (log missing components as `NOT VERIFIED`).
2. Construct a structured Mermaid Data-Flow Diagram (`DFD`) mapping:
   - Entry points (browsers, mobile clients, webhooks, partner APIs, admin CLIs, CI/CD runners).
   - Compute tiers, message brokers, caches, object stores, KMS/secret managers, and third-party SaaS integrations.
   - Explicit trust boundaries (`Internet -> Edge`, `Edge -> App Mesh`, `App -> Data Plane`, `Tenant A <-> Tenant B`, `Workload <-> Control Plane`).

---

## Step 3: Structured Threat Enumeration (`STRIDE` + `PASTA`)
1. Evaluate each trust boundary and data store systematically across `STRIDE` categories and business-logic abuse paths:
   - **Spoofing & Tampering:** Forged workload identities, JWT confusion, webhook signature bypass, unsigned container/artifact injection.
   - **Repudiation & Information Disclosure:** Missing immutable audit trails, cross-tenant `IDOR`/`BOLA`, verbose error leakage, unencrypted snapshots/logs.
   - **Denial of Service & Elevation of Privilege:** Unbounded fan-out/queue amplification, IAM shadow-admin paths, container escape, SSRF to cloud metadata (`169.254.169.254`).
2. Classify discovered flaws in existing designs/code strictly as **Confirmed Vulnerability**, **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)**.

---

## Step 4: Risk Scoring & Defense-in-Depth Control Design
1. Score threats using `CVSS v3.1/v4.0` paired with contextual business impact and exploit likelihood (`FAIR` / `NIST SP 800-30`).
2. Design layered Zero-Trust controls (`NIST SP 800-207` / `OWASP ASVS`):
   - **Preventive:** Centralized `PDP`/`PEP` authorization, `TLS 1.3`/`mTLS`, `KMS` envelope encryption, `IMDSv2`, row-level tenant isolation, fail-closed circuit breakers.
   - **Detective:** Structured security event telemetry (actor, tenant, action, resource, decision, correlation ID) routed to immutable SIEM storage.
   - **Corrective:** Automated token revocation, short-lived credential TTLs, key rotation runbooks, and blast-radius containment partitions.

---

## Step 5: Security ADR Authoring, Verification & Handoff
1. Document normative Security Architecture Decision Records (`Sec-ADRs`) with explicit rejected alternatives, latency/operational trade-offs, and `100%` redacted configuration blueprints.
2. Define deterministic **retest** and verification acceptance criteria (negative cross-tenant integration tests, `OPA/Rego` IaC policy checks) and complete [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md).
3. Immediately **halt** and **escalate** to `SA`, `PM`, and human stakeholders if unmitigated critical design flaws or unapproved risk exceptions block safe delivery.
