# Database Engineer Quality Checklist (`DATABASE_ENGINEER`)

- **Role ID:** `ROLE-IT-007`
- **Prompt Reference:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

---

## 1. Pre-Handoff Verification Checklist

### 1.1 Schema Integrity, Types & Online Migration Safety
- [ ] **Storage-Level Data Integrity:** Tables enforce explicit `PRIMARY KEY` (locality-aware `BIGINT`/`UUIDv7`), `FOREIGN KEY` actions, `NOT NULL`, `UNIQUE`, and `CHECK` invariants; currency uses exact `NUMERIC`/integer minor units and timestamps use UTC `TIMESTAMPTZ`.
- [ ] **Expand-Contract Online Migration Safety:** Schema changes avoid breaking running application versions, set explicit `lock_timeout`/`statement_timeout` bounds, and use non-blocking index/constraint creation patterns.
- [ ] **Verified Up/Down/Up Reversibility:** Migration scripts run cleanly forward, roll back without orphaned objects (or document forward-fix runbook if intentionally irreversible), and re-apply deterministically.

### 1.2 Indexing, Execution Plans & Concurrency
- [ ] **Query Plan & Index Verification:** Composite/partial/covering indexes match actual query predicates (`WHERE`, `JOIN`, `ORDER BY`) with `EXPLAIN` plans confirming absence of unintended full-table scans or write-amplifying redundant indexes.
- [ ] **Concurrency & Deadlock Hygiene:** Multi-row mutations acquire locks in deterministic key order, specify appropriate isolation levels (`REPEATABLE READ` / `SERIALIZABLE` / `FOR UPDATE`), and avoid holding open transactions across external HTTP calls.
- [ ] **Keyset Pagination & Bounded Reads:** List queries use indexed cursor pagination or strict limit bounds rather than deep `OFFSET` scans.

### 1.3 Security, Privacy & Governance Compliance
- [ ] **Parameterized Queries & Least-Privilege Roles:** `100%` of queries use bind parameters (`0` string interpolation), Row-Level Security (RLS) or tenant predicates are verified where multi-tenant, and app runtime roles exclude `SUPERUSER`/destructive DDL privileges.
- [ ] **Synthetic Fixture Privacy:** Seed scripts and migration tests use synthetic data only (`0` real production PII, credentials, or customer exports).
- [ ] **Human Approval on Destructive Ops:** Zero `DROP`, `TRUNCATE`, or live shared-DB mutations were executed without documented human authorization.
- [ ] **Exclusive Write-Lock Compliance:** All modified DDL, migration, and repository files stay strictly within assigned write-lock paths.

---

## 2. Required Handoff Evidence & Gate Classification

1. Migration execution logs (`up -> down -> up`) and negative constraint-violation test outputs via `run_command` (`PASS` / `FAILED`).
2. Captured `EXPLAIN` / `EXPLAIN ANALYZE` query plans and index inventory summary.
3. Explicit `PARTIAL` or `NOT VERIFIED` disclosure if engine-specific features were validated statically due to absent local DB daemons.
