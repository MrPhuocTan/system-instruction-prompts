# Quality Checklist: Data Governance Specialist (`ROLE-DATA-006`)

- **Role:** [`DATA_GOVERNANCE_SPECIALIST`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Classification, Catalog & Producer Contract Completeness
- [ ] Assigned explicit domain steward/owner, atomic grain, business glossary definition, and sensitivity tier (`Public`, `Internal`, `Confidential`, `Restricted PII/PHI/PCI`) to every table and column in scope.
- [ ] Scanned semi-structured JSON blobs, URL query strings, free-text notes, and Dead-Letter Queues (`DLQ`s) for hidden `PII`, `PHI`, or session tokens (`default-deny` enforced on unclassified fields).
- [ ] Codified producer-consumer data contracts in version-controlled YAML/JSON enforced in CI (schema types, freshness SLAs, breaking-change deprecation windows).

## 2. Lineage, Access Control & Cryptographic De-Identification
- [ ] Verified column-level AST lineage propagation so restricted sensitivity tags inherit automatically across `staging -> intermediate -> mart -> BI/ML` views.
- [ ] Replaced any unsalted identifier hashes (`MD5`/`SHA-256`) with KMS-managed `HMAC-SHA256` or vault tokenization and assessed quasi-identifier (`k`-anonymity) re-identification risks.
- [ ] Verified `RBAC`/`ABAC` dynamic column masking and row-level security (`RLS`) policies across authorized vs. unauthorized test personas, ensuring BI service accounts cannot bypass `RLS`.

## 3. Retention, Legal Hold & Subject Erasure (`DSR`)
- [ ] Defined explicit `TTL` retention schedules, legal-hold override locks, and end-to-end `GDPR`/`CCPA` erasure workflows covering raw `Bronze` storage, `SCD2` snapshots, `CDC` logs, and downstream ML/vector stores.
- [ ] Verified legal-hold locks deterministically suspend automated `TTL` and `DSR` purges on litigated or audited records without affecting unrelated subjects.
- [ ] Confirmed purpose-limitation checks gate downstream AI/ML training or third-party export consumption.

## 4. Auditability & Human Approval Boundaries
- [ ] Confirmed zero live `PII`, `PHI`, or secrets appear inside governance catalogs, lineage diagrams, or audit reports.
- [ ] Gated any destructive `DSR`/retention purge or live IAM privilege modification behind explicit human approval ([`HUMAN_APPROVAL_POLICY.md`](../../../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md)).
- [ ] Documented statutory/legal review touchpoints clearly without claiming unauthorized legal representation.

## 5. Independent Verification & Handoff Completeness
- [ ] Executed automated tests (`pytest`/`sqlglot`/`DuckDB`) verifying YAML contract schemas, AST tag propagation, `HMAC` de-identification, and persona-based masking/`RLS` enforcement.
- [ ] Handed off locked sensitivity tags and access matrices to [`DATA_ARCHITECT`](../DATA_ARCHITECT/SYSTEM_PROMPT.md), [`DATA_ENGINEER`](../DATA_ENGINEER/SYSTEM_PROMPT.md), and [`SYSTEM_ARCHITECT`](../../../../02_CORE_ROLES/SYSTEM_ARCHITECT/SYSTEM_PROMPT.md).
- [ ] Explicitly separated empirically verified local policy simulations from `NOT VERIFIED` live cloud-catalog IAM enforcement.
