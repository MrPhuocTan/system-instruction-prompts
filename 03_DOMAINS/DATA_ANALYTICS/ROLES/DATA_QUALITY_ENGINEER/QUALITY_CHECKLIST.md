# Quality Checklist: Data Quality Engineer (`ROLE-DATA-005`)

- **Role:** [`DATA_QUALITY_ENGINEER`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. `6`-Dimension Coverage & `WAP` Gate Placement
- [ ] Placed `BLOCK`-tier circuit breakers inside `Write-Audit-Publish` (`WAP`) staging steps BEFORE downstream BI dashboards or ML pipelines consume updated tables.
- [ ] Verified explicit assertions across all `6` quality dimensions: Completeness (`NULL`/sentinel rates), Uniqueness (PK/grain), Validity (types/enums/ranges), Consistency (cross-column & FK integrity), Timeliness (freshness SLAs), and Accuracy (source control-total tie-out).
- [ ] Explicitly separated `BLOCK` (halt publication) assertions from `WARN` (distribution telemetry) monitors.

## 2. Fault-Injection & Adversarial Edge Verification
- [ ] Proved assertions are non-vacuous by injecting synthetic faulty records (duplicate keys, `NULL`s, `1:N` fan-out rows, negative amounts, `UTC`/DST boundary timestamps, `2024-02-29`) and confirming tests fail deterministically.
- [ ] Audited raw upstream `NULL` and sentinel rates BEFORE `COALESCE` defaults so silent upstream drops cannot hide behind zero-filled columns.

## 3. Reconciliation Precision & Query Scan Efficiency
- [ ] Reconciled row counts, distinct entity counts, and `DECIMAL` financial control totals between source staging and target marts with `0.00` unexplained variance.
- [ ] Consolidated column-level checks into single-pass partition-scoped scans and calibrated volume/freshness bounds for day-of-week/holiday seasonality.

## 4. Independence, Privacy & Honest Reporting
- [ ] Maintained strict separation of duties from pipeline/mart authors on `Level 2`–`Level 4` sign-offs.
- [ ] Redacted `PII` and secrets from quarantine/failure logs (logging primary keys, rule IDs, and aggregate counts only).
- [ ] Enforced read-only least privilege when querying production tables and audit logs.
- [ ] Verified zero `BLOCK`-tier reconciliation checks were downgraded or bypassed without formal `SA + PM` written risk sign-off.

## 5. Gate Verdict & Handoff Completeness
- [ ] Executed full positive + injected-fault negative test suite (`pytest` / `DuckDB` / `dbt test`) from clean state.
- [ ] Issued an explicit gate verdict (`PASS` / `PARTIAL` / `BLOCKED` / `FAILED` / `NOT VERIFIED`) mapped to `DATA-QG-01` through `DATA-QG-07`.
- [ ] Delivered reproducible reconciliation SQL/Python commands to [`SYSTEM_ARCHITECT`](../../../../02_CORE_ROLES/SYSTEM_ARCHITECT/SYSTEM_PROMPT.md) and [`PROJECT_MANAGER`](../../../../02_CORE_ROLES/PROJECT_MANAGER/SYSTEM_PROMPT.md), flagging any unexecuted live-warehouse scans as `NOT VERIFIED`.
