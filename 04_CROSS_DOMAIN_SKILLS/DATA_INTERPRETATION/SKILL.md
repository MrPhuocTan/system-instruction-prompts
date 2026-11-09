---
name: data-interpretation
description: "Use this skill when analyzing datasets, telemetry, experimental metrics, financial tables, or survey results to extract accurate statistical insights without aggregation fallacies or misread distributions."
---

# Data Interpretation

## Skill Metadata
- **Skill ID:** `SKL-CORE-005`
- **Name:** `data-interpretation`
- **Domain:** `CROSS_DOMAIN`
- **Version:** `1.0.0`

## Purpose
Transform raw tabular data, time-series telemetry, cohort metrics, benchmark logs, and experimental outputs into statistically sound, decision-ready conclusions. This skill enforces schema and data-hygiene profiling, distribution-aware summarization, subgroup decomposition (Simpson's Paradox screening), uncertainty quantification, and strict separation of descriptive patterns from causal claims.

## Required Competencies
- Exploratory data profiling: missingness mechanisms (`MCAR`, `MAR`, `MNAR`), duplicate keys, schema drift, unit mismatches, and censoring/truncation.
- Distributional literacy: skewness, heavy tails, multimodality, percentile semantics (`p50`, `p95`, `p99`), variance, and outlier forensics.
- Cohort, time-series, and panel analysis: seasonality, structural breaks, survivorship/attrition bias, right-censoring, and denominator stability.
- Statistical inference hygiene: confidence/credible intervals, statistical power, multiple-hypothesis testing corrections, and practical effect size vs. p-value significance.

## Prerequisites
- Raw dataset, query output, benchmark artifact, or summary table accessible via `read_file` or reproducible `run_command` scripts.
- Data dictionary or upstream generation logic defining units, timestamps/timezones, null encodings, and inclusion/exclusion filters.
- Clearly framed analytical question aligned with [CRITICAL_THINKING](../CRITICAL_THINKING/SKILL.md).

## Workflow
1. **Audit Data Lineage & Hygiene First:** Inspect row counts, primary-key uniqueness, schema types, time ranges, timezone normalization, null/sentinel values (`-1`, `9999`, `NaN`, `0`), and join cardinality before computing aggregates.
2. **Characterize Full Distributions (Never Mean-Only):** Compute central tendency alongside dispersion and tail quantiles (`min`, `p25`, `median`, `mean`, `std/IQR`, `p95`, `p99`, `max`). Flag skewed or bimodal distributions where arithmetic means mislead.
3. **Stratify & Screen for Aggregation Artifacts:** Decompose headline metrics across key dimensions (cohort, region, device, version, customer tier) to detect Simpson's Paradox, mix-shift effects, and denominator drift.
4. **Analyze Temporal & Sequential Dynamics:** Separate secular trends from day-of-week/seasonal cycles, instrumentation rollouts, backfill spikes, and right-censored recent windows.
5. **Quantify Uncertainty & Effect Magnitude:** Report sample sizes (`n`), confidence intervals or bootstrap bounds, and practical domain effect sizes; apply multiple-comparison discipline (`Benjamini-Hochberg` / `Bonferroni`) when scanning many slices.
6. **Reconcile & Cross-Check Totals:** Verify that subgroup counts sum to population totals, accounting identities balance, and outlier removal rules are transparent and sensitivity-tested (with vs. without outliers).

## Tools and Techniques
- **Deterministic Profiling Scripts:** Execute reproducible Python (`pandas`, `duckdb`, `numpy`, `scipy`, `csv`/`sqlite3` stdlib) or SQL checks via `run_command` rather than performing mental arithmetic on large tables.
- **Mix-Shift Decomposition (Kitagawa-Oaxaca):** Separate true within-segment rate changes from compositional traffic shifts across segments.
- **Sensitivity & Winsorization Tables:** Present key findings alongside outlier-included and outlier-trimmed sensitivity bounds.
- **Sanity-Bound Cross-Checks:** Validate derived figures against physical constraints (e.g., percentages in `[0, 100]`, monotonic cumulative counters, latency `>= 0`, conservation of mass/currency).

## Verification Requirements
- Every reported number, percentage change, ratio, and aggregate is computed deterministically via script or query and reconciled against raw input totals.
- Join operations explicitly verify row-count invariants before and after joins to prevent silent many-to-many fan-out inflation or inner-join attrition.
- Units, currencies, bases (basis points vs. percentage points vs. relative percent), and observation windows are explicitly labeled on every metric.

## Quality Criteria
- **Zero Mental-Math Hallucinations:** Calculations are script-verified and reproducible from workspace artifacts.
- **Precision in Rate Semantics:** Explicitly distinguishes relative change (`+20%`) from absolute percentage-point change (`+2.0 pp` from `10.0%` to `12.0%`) and basis points (`+200 bps`):
  | Data Characteristic | Diagnostic Check | Required Reporting Standard |
  | :--- | :--- | :--- |
  | Heavy-Tailed / Skewed Metric | `mean >> median` or high kurtosis (latency, spend) | Report `p50`, `p95`, `p99`, `IQR`, and `mean` together |
  | Multi-Segment Aggregate | Opposite trend inside cohorts vs. overall | Stratify by cohort + run mix-shift decomposition |
  | Small Sample (`n < 30`) | Wide confidence intervals / discrete jumps | Report exact `n/N` fractions + exact binomial/bootstrap CI |
  | Time-Series Window | Incomplete trailing day/week or backfill spike | Exclude or explicitly flag right-censored partial periods |
- **Transparent Data Limitations:** Missingness, sample attrition, instrumentation gaps, and observational confounding are prominently disclosed alongside conclusions.
- **Failure Modes to Avoid:**
  - *Mean-Only Reporting:* Summarizing skewed latency or revenue data by arithmetic average alone, hiding severe tail degradation.
  - *Simpson's Paradox Blindness:* Mistaking traffic composition shift across segments for a genuine within-segment regression or lift.
  - *Join Fan-Out Inflation:* Multiplying revenue or event counts silently via unkeyed many-to-many SQL joins.
  - *Unadjusted Slice Dredging:* Scanning 50 subgroup cuts and celebrating a single `p = 0.04` noise artifact as causal truth.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [SECURITY_AND_PRIVACY.md](../../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md) or data-governance rules.
- Never print raw PII, PHI, payment card numbers, or user secrets to stdout/logs during exploratory profiling; aggregate or mask sensitive columns first.
- Never drop inconvenient data ranges, cherry-pick time windows, or alter outlier thresholds post-hoc to manufacture desired outcomes.

## Expected Deliverables
- **Data Hygiene & Schema Audit Summary** (sample sizes, date range, missingness, anomalies, and join/accounting reconciliation).
- **Distributional & Segment Findings Table** reporting exact units, denominators, quantiles, effect sizes, and uncertainty bounds.
- **Analytical Interpretation & Caveats Brief** separating verified empirical facts from hypotheses requiring controlled experimentation.
