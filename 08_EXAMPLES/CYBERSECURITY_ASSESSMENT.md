# End-to-End Walkthrough: Level 4 Authorized Web/API Security Assessment (`CYBERSECURITY_ASSESSMENT.md`)

> **Walkthrough Governance:** Demonstrates **Complexity Level 4** security operations governed by [SECURITY_AND_PRIVACY.md](../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md), [HUMAN_APPROVAL_POLICY.md](../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md), [SECURITY_AGENT_PROMPT.md](../07_SUBAGENT_PROMPTS/SECURITY_AGENT_PROMPT.md), and [CYBERSECURITY/DOMAIN_SYSTEM_PROMPT.md](../03_DOMAINS/CYBERSECURITY/DOMAIN_SYSTEM_PROMPT.md).

---

## 1. Realistic User Scenario
**User Prompt:**
> "Perform a pre-release OWASP API security assessment against our isolated staging Disbursements API (`http://127.0.0.1:8443/v1/disbursements`) and local codebase `services/disbursements-api/`, classify findings rigorously, implement fixes on branch `sec/bola-remediation`, and run a retest."

---

## 2. Mandatory Authorization, RoE & Human Approval Gate (`Level 4`)
Before reading secrets or issuing a single HTTP probe, `PM` + `SA` + [DOMAIN_LEAD](../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md) enforce the pre-execution gate:
1. **Authorization & Signed RoE Verification:** Verified `configs/security_roe_2026_11.md` inside the target workspace confirming local isolated Docker Compose environment (`127.0.0.1:8443` + synthetic test tenants `tenant_alpha_test` / `tenant_beta_test`), zero production DB connectivity, rate cap `<= 10 RPS`, and strict prohibition of DoS, fuzz-flooding, or external webhook egress.
2. **Explicit Human Approval Gate:** Invoked `ask_question` presenting exact target URLs, synthetic test accounts, non-destructive OWASP API Top 10 test plan, and branch write scope; execution proceeded only after explicit human confirmation (`APPROVED`).
3. **Role Allocation (Separation of Duties):**
   - `ws-sec-audit`: [APPLICATION_SECURITY](../03_DOMAINS/CYBERSECURITY/ROLES/APPLICATION_SECURITY/SYSTEM_PROMPT.md) + [PENETRATION_TESTER](../03_DOMAINS/CYBERSECURITY/ROLES/PENETRATION_TESTER/SYSTEM_PROMPT.md) following [PENETRATION_TESTER/WORKFLOW.md](../03_DOMAINS/CYBERSECURITY/ROLES/PENETRATION_TESTER/WORKFLOW.md) and [SECURITY_ASSESSMENT](../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md) -> Owns `reports/security_assessment.md`, `tests/security/test_api_authz.py`.
   - `ws-remediation`: Backend remediation worker -> Owns `services/disbursements-api/routes/**` (deployed only after `ws-sec-audit` locks findings).
   - `ws-retest`: Independent [QUALITY_REVIEWER](../02_CORE_ROLES/QUALITY_REVIEWER/SYSTEM_PROMPT.md) + `ws-sec-audit` retest verification.

---

## 3. Non-Destructive Testing & Epistemic Finding Classification
`ws-sec-audit` combines static code analysis (`semgrep`, AST route inspection) with controlled local [API_TESTING](../05_SPECIALIZED_SKILLS/API_TESTING/SKILL.md) requests, redacting synthetic JWTs as `REDACTED_JWT_9F2A` and separating findings into canonical tiers:

| Finding ID | Classification | Title & OWASP Category | Severity | Evidence & Analysis Summary |
| :--- | :--- | :--- | :---: | :--- |
| `SEC-001` | **Confirmed Vulnerability** | Cross-Tenant BOLA on `PATCH /v1/disbursements/{id}/destination` (`API1:2023`) | `CRITICAL` (`CVSS 9.1`) | Route queried `WHERE id = :id` without `AND tenant_id = :jwt_tenant_id`. Authenticated `tenant_beta_test` token modified `tenant_alpha_test` draft payout destination (`HTTP 200`). |
| `SEC-002` | **Confirmed Vulnerability** | Mass Assignment of `approval_state` on `POST /v1/disbursements` (`API3:2023`) | `HIGH` (`CVSS 8.1`) | Pydantic request schema reused ORM model attributes, allowing `"approval_state": "APPROVED"` in JSON body to bypass maker-checker workflow. |
| `SEC-003` | **Potential Finding** | Missing Upstream Gateway Rate-Limit Headers on Local Compose (`API4:2023`) | `MEDIUM` | Local container lacks Envoy rate-limit filter declared in `infra/envoy_prod.yaml`; flagged for staging Kubernetes verification (`NOT VERIFIED` locally). |
| `SEC-004` | **False Positive** | SAST Alert on Unauthenticated `GET /.well-known/jwks.json` | `NONE` | Scanner flagged public route; code audit confirmed endpoint exposes only public RSA `RS256` verification keys (`n`, `e`, `kid`) per RFC 7517 with zero private key material. |

---

## 4. Remediation & Deterministic Retest Verification
1. **Root-Cause Remediation (`ws-remediation`):**
   - Enforced mandatory tenant-scoped repository dependency (`session.execute(select(Disbursement).where(Disbursement.id == id, Disbursement.tenant_id == principal.tenant_id))`) plus PostgreSQL `RLS` defense-in-depth policy.
   - Replaced shared input schema with strict `CreateDisbursementRequest( extra="forbid" )` excluding `approval_state`, `approved_by`, and `tenant_id`.
2. **Independent Retest (`ws-sec-audit` + `QUALITY_REVIEWER`):**
   - `pytest tests/security/test_api_authz.py` executed against rebuilt container:
     - Cross-tenant `PATCH` attempt -> `HTTP 404 Not Found` + PostgreSQL row unchanged (`destination_iban` verified intact).
     - Mass-assignment `"approval_state": "APPROVED"` payload -> `HTTP 422 Unprocessable Entity` (`extra_forbidden`); valid creation forces `approval_state = "PENDING_REVIEW"`.
   - Secret hygiene scan (`git diff` + report scan) confirmed `0` unredacted tokens or keys.

---

## 5. Redacted Proof-of-Concept & Retest Evidence Excerpt (`SEC-001`)
```http
# Pre-Remediation (Confirmed Vulnerability — Isolated Local Docker 127.0.0.1:8443)
PATCH /v1/disbursements/01930a8c-71b2-7d10-9a11-0042ac120002/destination HTTP/1.1
Host: 127.0.0.1:8443
Authorization: Bearer REDACTED_JWT_9F2A  # Principal: tenant_beta_test
Content-Type: application/json

{"destination_iban": "DE89370400440532013000"}
-> HTTP/1.1 200 OK (Unauthorized cross-tenant mutation succeeded)

# Post-Remediation Retest (Branch: sec/bola-remediation)
-> HTTP/1.1 404 Not Found {"error_code": "DISBURSEMENT_NOT_FOUND"}
# Verified in PostgreSQL: tenant_alpha_test destination_iban unchanged; security_audit_log recorded cross-tenant probe.
```

---

## 6. Epistemic Summary & Dual Gate Signoff (`SA_GATE` + `PM_GATE`)
| Security Governance Check | Standard / Policy Enforced | Outcome |
| :--- | :--- | :---: |
| **Written Authorization & Signed RoE** | [SECURITY_AND_PRIVACY.md](../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md) | `PASS` |
| **Pre-Execution Human Approval Gate** | [HUMAN_APPROVAL_POLICY.md](../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md) (`ask_question`) | `PASS` |
| **Cybersecurity Domain Quality Gates** | [CYBERSECURITY/QUALITY_GATES.md](../03_DOMAINS/CYBERSECURITY/QUALITY_GATES.md) | `PASS` |
| **Zero Secret / Token Exposure** | All tokens masked (`REDACTED_JWT_9F2A`); `0` production targets touched | `PASS` |

- **`SA_GATE = PASS` ([TECHNICAL_REVIEW.md](../06_TEMPLATES/TECHNICAL_REVIEW.md)):** Confirmed `100%` RoE compliance, non-destructive execution, tenant isolation at both application and DB layers, and deterministic regression tests.
- **`PM_GATE = PASS` ([BUSINESS_REVIEW.md](../06_TEMPLATES/BUSINESS_REVIEW.md)):** Confirmed all 6 mandatory security report fields (severity, impact, redacted evidence, repro steps, remediation, retest verification) and logged `SEC-003` staging gateway verification in [RISK_REGISTER.md](../06_TEMPLATES/RISK_REGISTER.md) and [FINAL_DELIVERY.md](../06_TEMPLATES/FINAL_DELIVERY.md).
