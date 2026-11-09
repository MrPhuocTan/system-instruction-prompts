# Practitioner Workflow — Application Security Engineer (`ROLE-CYB-002`)

- **Role:** `APPLICATION_SECURITY` ([SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md))
- **Verification Gate:** [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md)
- **Companion Skills:** [SECURITY_ASSESSMENT](../../../../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md) | [API_TESTING](../../../../05_SPECIALIZED_SKILLS/API_TESTING/SKILL.md)

---

## Step 1: Scope, Authorization & Attack-Surface Inventory
1. Confirm **authorized** repository paths, build/test **scope**, and **Rules of Engagement (`RoE`)** (**non-destructive** local execution only unless staging `RoE` is explicitly approved).
2. Map the application attack surface via `read_file`:
   - HTTP/REST/GraphQL/gRPC routes, WebSocket handlers, webhook receivers, CLI parsers, file uploaders, and LLM prompt/tool boundaries.
   - Authentication/session middleware, `RBAC`/`ABAC`/tenant-scoping decorators, and dependency lockfiles (`package-lock.json`, `poetry.lock`, `go.sum`, `Cargo.lock`).

---

## Step 2: Automated SAST/SCA Execution & Manual Taint Audit
1. Run available local static and dependency analyzers (`semgrep`, `bandit`, `gosec`, `npm/pip/cargo audit`, `trivy`) via `run_command`; if tools or advisory feeds are unavailable, record tool limits honestly and perform systematic manual inspection.
2. Audit high-risk classes against `OWASP ASVS v4.0` and `OWASP API Security Top 10`:
   - **Access Control:** Verify object-level (`BOLA`/`IDOR`) and function-level (`BFLA`) ownership checks on every read/write/delete query.
   - **Injection & Execution:** Trace untrusted data into SQL/ORM raw queries, OS commands, SSRF-capable HTTP clients, XML/YAML/JSON deserializers, template engines, and filesystem paths.
   - **Auth, Crypto & State:** Inspect JWT validation (`alg`, `iss`, `aud`, `exp`), cookie flags (`HttpOnly`, `Secure`, `SameSite`), password hashing (`Argon2id`/`bcrypt`), CSRF protection, and `TOCTOU` locks on financial/quota state changes.

---

## Step 3: Exploitability Verification, Variant Search & Classification
1. Prove or refute candidate flaws using isolated, **non-destructive** unit/integration tests or local test-server requests—never live production targets.
2. Run codebase-wide AST/pattern searches across sibling modules to locate all variants of any confirmed sink defect.
3. Classify every item into **Confirmed Vulnerability**, **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)**, assigning `CWE`, `CVSS v3.1/v4.0`, and contextual impact ratings while redacting `100%` of secrets/PII.

---

## Step 4: Structural Remediation & Regression Hardening
1. Author minimal, idiomatic patches (`edit_file`) replacing unsafe sinks with parameterized APIs, centralized authorization policies, strict schema validators, or patched dependency versions.
2. Add deterministic negative security tests (asserting `401`/`403`/`400` or safe escaping on malicious inputs) and positive functional tests.

---

## Step 5: Independent Retest & Handoff
1. Execute the full test suite and re-run static/dependency checks via `run_command` to confirm **retest** mitigation and zero functional regressions.
2. Complete [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) and deliver the redacted AppSec report and remediation summary.
3. Immediately **halt** and **escalate** to `SA`, `PM`, and the user if live leaked credentials or supply-chain compromises are uncovered.
