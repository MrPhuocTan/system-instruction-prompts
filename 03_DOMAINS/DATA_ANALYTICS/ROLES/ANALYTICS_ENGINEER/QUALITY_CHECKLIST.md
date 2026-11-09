# Quality Checklist: Analytics Engineer (`ROLE-DATA-003`)

- **Role:** [`ANALYTICS_ENGINEER`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Layering, Grain & Join Cardinality Integrity
- [ ] Enforced clean `staging -> intermediate -> fct/dim` DAG layering (`0` direct raw-table references in marts; explicit typed column lists instead of `SELECT *` in final projections).
- [ ] Declared atomic grain for every model and passed automated `not_null` + `unique` primary/surrogate key assertions.
- [ ] Proved zero unintended join fan-out (`1:N` / `M:N` chasm traps) and zero silent `INNER JOIN` row attrition (`LEFT JOIN` + explicit `'UNKNOWN'` dimension key handling verified).

## 2. SQL Edge-Case & Temporal Correctness
- [ ] Eliminated SQL three-valued `NULL` bugs (`NOT EXISTS` instead of nullable `NOT IN`; `NULLIF` on denominators; `COALESCE` on additive sums; collision-free surrogate key hashing).
- [ ] Verified `SCD Type 2` temporal joins use half-open `[valid_from, valid_to)` intervals without overlapping validity windows or boundary double-counting.
- [ ] Verified incremental models (`merge` / `insert_overwrite` + late-arrival lookback window) produce `100%` identical rows and sums to a full refresh on multi-batch test fixtures.

## 3. Control-Total Reconciliation & Semantic Consistency
- [ ] Reconciled `fct_*` control totals (`SUM` of `DECIMAL` monetary measures, distinct entity counts) against `stg_*` sources with `0.00` unexplained variance.
- [ ] Locked canonical metric formulas (including non-additive ratios and semi-additive snapshot balances) in versioned semantic/mart YAML specifications.

## 4. Privacy, Dialect Portability & Cost Hygiene
- [ ] Masked or excluded restricted `PII` columns from general-access `dim_*`/`fct_*` marts and propagated sensitivity tags in model YAML metadata.
- [ ] Kept partition predicates `sargable` (`0` functions wrapping partition keys), avoided integer-division truncation traps, and confirmed zero secrets in `profiles.yml` or SQL files.

## 5. Independent Verification & Handoff Completeness
- [ ] Executed SQL unit and reconciliation tests locally (`DuckDB` / `dbt test` / `pytest`) covering `NULL` predicates, duplicate upstream rows, `1:N` fan-out prevention, and `SCD2` interval boundaries.
- [ ] Verified zero orphaned foreign keys (`relationships` check) between `fct_*` tables and conformed `dim_*` tables.
- [ ] Published column-level descriptions and canonical metric YAML specs for [`BI_ANALYST`](../BI_ANALYST/SYSTEM_PROMPT.md) and [`DATA_QUALITY_ENGINEER`](../DATA_QUALITY_ENGINEER/SYSTEM_PROMPT.md).
- [ ] Explicitly separated empirically verified local SQL fixture runs from `NOT VERIFIED` live cloud-warehouse full-table execution.
