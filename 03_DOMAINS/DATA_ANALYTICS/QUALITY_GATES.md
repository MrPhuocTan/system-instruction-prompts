# Data Engineering & Analytics Quality Gates (`DOM-10-DATA`)

All `DATA_ANALYTICS` workstreams (`Level 1`–`Level 4`) must pass the objective verification gates below before [`DOMAIN_LEAD`](../../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md), [`SYSTEM_ARCHITECT`](../../02_CORE_ROLES/SYSTEM_ARCHITECT/SYSTEM_PROMPT.md) (`SA_GATE`), and [`PROJECT_MANAGER`](../../02_CORE_ROLES/PROJECT_MANAGER/SYSTEM_PROMPT.md) (`PM_GATE`) sign-off. Any gate requiring unavailable live production warehouse credentials or GUI tools must be verified on local synthetic/fixture engines (`DuckDB`/`SQLite`/`pytest`) and explicitly flagged `NOT VERIFIED` against production scale.

---

## Gate Summary Matrix

| Gate ID | Gate Name | Mandatory Evidence Artifact | Blocking Failure Condition |
| :--- | :--- | :--- | :--- |
| `DATA-QG-01` | Schema & Grain Contracts | Typed table/event contract + grain & PK uniqueness test output | Undeclared grain, duplicate primary keys, or breaking unversioned schema drift |
| `DATA-QG-02` | Idempotent & Replayable Pipelines | Double-run (`2x` replay) equivalence & late-arrival test log | Duplicate rows on rerun, non-deterministic ordering, or silent data loss on backfill |
| `DATA-QG-03` | End-to-End Lineage & Impact | Source-to-mart-to-BI DAG + column-level impact map | Orphaned tables, circular dependencies, undocumented OLTP coupling, or broken downstream refs |
| `DATA-QG-04` | Reconciliation & Quality Assertions | Source-vs-target row/control-sum diff (`== 0`) + null/FK/distribution log | Unexplained join fan-out, silent `INNER JOIN` row drops, `FLOAT` rounding drift, or silent `NULL` traps |
| `DATA-QG-05` | Metric Semantic Consistency | Canonical metric spec (numerator, denominator, filters, grain, TZ) | Conflicting KPI totals across marts/dashboards or non-additive ratio averaging (`AVG` of `%`) |
| `DATA-QG-06` | Data Privacy, Access & Governance | PII classification matrix, masking/RLS policy test, retention rule | Raw `PII`/`PHI`/secrets in logs/unmasked marts, missing erasure path, or unauthorized prod mutation |
| `DATA-QG-07` | Truthful Visualization & UX Hygiene | Chart spec/screenshot audit, axis/scale/denominator check, `WCAG` contrast | Truncated bar baselines, misleading dual axes, unflagged partial periods, or `"AI Sign"` clutter |

---

## Detailed Gate Specifications

### `DATA-QG-01` — Schema & Grain Contracts
- Declare atomic grain (`1 row = ...`), primary/natural keys, nullable vs. `NOT NULL` constraints, data types (`DECIMAL` for currency, `UTC` timestamps), and enum/domain bounds for every dataset.
- Assert `COUNT(*) == COUNT(DISTINCT primary_key)` and `SUM(CASE WHEN primary_key IS NULL THEN 1 ELSE 0 END) == 0` automatically on every build.

### `DATA-QG-02` — Idempotent Pipelines & Late-Data Handling
- Execute every batch/incremental transformation twice (`run 1` -> `run 2`) over identical inputs (including out-of-order and late-arriving records within watermark lookback windows) and assert bit-identical row counts and metric sums.
- Verify failed mid-flight jobs roll back or isolate staged data (`Write-Audit-Publish`) without leaving partial/corrupted state visible to readers.

### `DATA-QG-03` — Lineage & Dependency Hygiene
- Maintain acyclic (`DAG`) transformation graphs (`source -> staging -> intermediate -> fct/dim -> semantic/BI`) with zero direct BI queries bypassing governed marts to hit raw ingestion tables.
- Document upstream SLA freshness expectations and downstream blast radius before altering column names, types, or business logic.

### `DATA-QG-04` — Reconciliation & Row/Null/Distribution Assertions
- Reconcile target mart control totals (`SUM(amount)`, distinct entity counts, row counts before/after joins) against upstream source staging tables within `0` unexplained variance (`<= 0.00` currency unit after documented exclusions).
- Test explicit SQL edge cases: `1:N` and `M:N` join fan-out traps, `NULL`-safe comparisons (`IS DISTINCT FROM` / `COALESCE`), division-by-zero (`NULLIF(denom, 0)`), `UTF-8` encoding anomalies, and historical distribution z-score bounds.

### `DATA-QG-05` — Metric Semantic Consistency
- Verify semi-additive (account balances, inventory snapshots: `LAST_VALUE` across time, `SUM` across entities) and non-additive metrics (conversion rates, `AOV`, `p95` latency: recomputed from summed numerators/denominators or raw distributions, NEVER averaged across rollups) aggregate accurately across all filter combinations.

### `DATA-QG-06` — Data Privacy, Security & Governance
- Confirm column-level `PII`/`PHI`/`PCI` tagging, dynamic masking or salted hashing/tokenization, row-level tenant/region isolation (`RLS`), and `GDPR`/`CCPA` subject deletion propagation across snapshots and backups/lakehouse history (`DELETE`/`VACUUM` policy).

### `DATA-QG-07` — Truthful Visualization & Human-Centric Usability
- Confirm bar/column/area baselines start at `0`, time axes preserve equidistant intervals (never skipping empty dates silently), and incomplete current periods (`MTD`/`WTD`) are visually distinguished or excluded.
- Verify color palettes pass `WCAG 2.2 AA` contrast and deuteranopia/protanopia safety (never encoding directional status by red/green hue alone).
- Verify chart tooltips escape untrusted strings (`XSS` safety), suppress individual `PII`, handle empty/zero/loading/error states cleanly, and contain zero decorative emojis or `"AI Sign"` filler.
