# End-to-End Walkthrough: Level 3 AI/ML Pipeline & Leakage Audit (`AI_ML_PROJECT.md`)

> **Walkthrough Governance:** Demonstrates **Complexity Level 3** machine learning engineering across `AI_MACHINE_LEARNING` and `DATA_ANALYTICS`, enforcing point-in-time data leakage audits, deterministic baselines, calibration/slice metrics via [MODEL_EVALUATION](../05_SPECIALIZED_SKILLS/MODEL_EVALUATION/SKILL.md), and `Low Loss != Solved Real-World Problem` verification.

---

## 1. Realistic User Scenario
**User Prompt:**
> "Train and evaluate a 90-day B2B invoice delinquency risk model using our 2.4M-row historical ledger (`data/raw/invoices_2022_2025.parquet`) and customer event log (`data/raw/payment_events.parquet`), and expose a reproducible batch scoring CLI."

---

## 2. Domain Routing, Roles & Skill Loading
- **Complexity Level:** **Level 3** ([TASK_COMPLEXITY_ROUTER.md](../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md))
- **Active Domains:** `AI_MACHINE_LEARNING` ([DOMAIN_SYSTEM_PROMPT.md](../03_DOMAINS/AI_MACHINE_LEARNING/DOMAIN_SYSTEM_PROMPT.md), [QUALITY_GATES.md](../03_DOMAINS/AI_MACHINE_LEARNING/QUALITY_GATES.md)) + `DATA_ANALYTICS` ([DOMAIN_SYSTEM_PROMPT.md](../03_DOMAINS/DATA_ANALYTICS/DOMAIN_SYSTEM_PROMPT.md))
- **Persistent Governance:** `PM` + `SA` initialize [PROJECT_MANIFEST.md](../06_TEMPLATES/PROJECT_MANIFEST.md) and [AGENT_COMMUNICATE.md](../06_TEMPLATES/AGENT_COMMUNICATE.md), locking hardware safeguards (cap CPU threads to `6`, memory `< 12 GB`, deterministic seed `42`).
- **Disjoint Workstreams & Loaded Skills:**
  1. `ws-data-integrity` ([DATA_QUALITY_ENGINEER](../03_DOMAINS/DATA_ANALYTICS/ROLES/DATA_QUALITY_ENGINEER/SYSTEM_PROMPT.md)) -> Owns `src/features/**`, `tests/test_leakage.py` | Skills: [DATABASE_VALIDATION](../05_SPECIALIZED_SKILLS/DATABASE_VALIDATION/SKILL.md), [DATA_INTERPRETATION](../04_CROSS_DOMAIN_SKILLS/DATA_INTERPRETATION/SKILL.md)
  2. `ws-modeling` ([MACHINE_LEARNING_ENGINEER](../03_DOMAINS/AI_MACHINE_LEARNING/ROLES/MACHINE_LEARNING_ENGINEER/SYSTEM_PROMPT.md)) -> Owns `src/models/**`, `src/cli/score_batch.py` | Skills: [SCIENTIFIC_REPRODUCIBILITY](../05_SPECIALIZED_SKILLS/SCIENTIFIC_REPRODUCIBILITY/SKILL.md), [COGNITIVE_EXECUTION](../04_CROSS_DOMAIN_SKILLS/COGNITIVE_EXECUTION/SKILL.md)
  3. `ws-eval-audit` ([AI_EVALUATION_ENGINEER](../03_DOMAINS/AI_MACHINE_LEARNING/ROLES/AI_EVALUATION_ENGINEER/SYSTEM_PROMPT.md)) -> Owns `tests/eval/**`, `reports/model_card.md` (independent non-author of `src/models/**`) | Skills: [MODEL_EVALUATION](../05_SPECIALIZED_SKILLS/MODEL_EVALUATION/SKILL.md), [PERFORMANCE_BENCHMARKING](../05_SPECIALIZED_SKILLS/PERFORMANCE_BENCHMARKING/SKILL.md)

---

## 3. Dataset Integrity & Temporal Leakage Discovery
Before training any model, `ws-data-integrity` audits `invoices_2022_2025.parquet` and `payment_events.parquet`:
1. **Point-in-Time Join Audit:** Discovers two critical leakage vectors that would have produced artificially inflated (`0.98+` ROC-AUC) offline metrics:
   - `dunning_notice_count` in `invoices_2022_2025.parquet` was mutated in-place *after* invoice due dates (`t > issue_date`).
   - Random `80/10/10` row splitting placed invoices from the same `customer_id` and macroeconomic quarter across both train and test sets.
2. **Remediation Locked in Contract:**
   - Reconstruct features strictly using `event_timestamp <= invoice_issue_timestamp` (as-of join verified by `tests/test_leakage.py` mutating future events and asserting `0.0` feature change).
   - Enforce strict **out-of-time + grouped evaluation splits** with a 90-day embargo gap to prevent label horizon overlap:
     - **Train:** `2022-01-01` to `2024-03-31` (+ 90d label maturity embargo)
     - **Validation:** `2024-07-01` to `2024-12-31` (+ 90d embargo)
     - **Out-of-Time Holdout Test:** `2025-04-01` to `2025-09-30`

---

## 4. Baseline Comparison, Calibration & Distribution Shift Audit
`ws-modeling` trains three reproducible candidates; `ws-eval-audit` independently evaluates them on the untouched `2025` holdout set (`prevalence = 6.8%` delinquency):

| Model Candidate | PR-AUC (Holdout) | ROC-AUC | Brier Score | Expected Calibration Error (`ECE`) | Recall @ Top 10% Risk Queue |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Rule Baseline (Trailing 12m Late Rate)** | `0.241` | `0.742` | `0.061` | `0.039` | `46.2%` |
| **L2 Logistic Regression (WOE/Spline)** | `0.338` | `0.819` | `0.052` | `0.018` | `59.4%` |
| **LightGBM + Isotonic Calibration** | **`0.419`** | **`0.864`** | **`0.046`** | **`0.011`** | **`68.7%`** |

**Real-World Distribution Shift & Subgroup Stress Findings (`ws-eval-audit`):**
- Uncalibrated LightGBM had higher raw PR-AUC (`0.420`) but poor probability calibration (`ECE = 0.064`), over-predicting risk by `1.9x` on net-60 contracts; isotonic calibration on the validation fold reduced `ECE` to `0.011`.
- **Cold-Start Subgroup Limitation Identified:** For first-time buyers (`0` prior invoices, `9.4%` of holdout volume), LightGBM PR-AUC drops to `0.214` (only `+0.019` over sector baseline). Logged explicitly in `reports/model_card.md` and [RISK_REGISTER.md](../06_TEMPLATES/RISK_REGISTER.md) with a `cold_start_flag=true` output column so collections teams apply manual credit-bureau review rather than automated credit holds.

---

## 5. Independent Reproducibility & CLI Contract Verification
`ws-eval-audit` and `SA` independently execute deterministic pipeline checks (`Low Training Loss != Solved Real-World Problem`):

| Verification Gate | Command Executed | Observed Empirical Evidence | Verdict |
| :--- | :--- | :--- | :---: |
| **Temporal Leakage Invariance** | `pytest tests/test_leakage.py` | Perturbing all `payment_events` timestamps `> issue_date` produces `0.000000` max feature delta | `PASS` |
| **Deterministic Seed Parity** | `python3 -m src.cli.score_batch --seed 42` (run twice) | SHA-256 of output `predictions_2025.parquet` identical across runs | `PASS` |
| **Schema & Null Edge Cases** | `pytest tests/eval/test_cli_contracts.py` | Missing `credit_limit` or unseen `industry_code` handled cleanly without `NaN` probabilities | `PASS` |
| **Host Resource & Thermal Cap** | `/usr/bin/time -l python3 -m src.models.train` | `6` threads respected; peak RSS `4.12 GB` (`< 12 GB` budget); runtime `84s` | `PASS` |

---

## 6. Epistemic Summary & Dual Gate Signoff (`SA_GATE` + `PM_GATE`)
- **Verified Facts:** Out-of-time `2025` holdout PR-AUC `0.419` vs. `0.241` trailing-rate rule baseline; calibrated `ECE = 0.011`.
- **Explicit Assumptions & Operational Guardrails:** Model assumes net-30/net-60/net-90 contract terms remain structurally comparable to `2022–2025`; monthly Population Stability Index (`PSI > 0.20`) drift monitoring alert configured in `src/cli/score_batch.py`.
- **`SA_GATE = PASS`:** Verified bit-exact scoring determinism, future-mutation invariance test, memory footprint (`4.12 GB` peak RSS), and zero out-of-lock edits ([TECHNICAL_REVIEW.md](../06_TEMPLATES/TECHNICAL_REVIEW.md)).
- **`PM_GATE = PASS`:** Confirmed business lift (`+22.5` percentage points recall in top-decile collections queue over current rule baseline), transparent cold-start limitation disclosure, and clean CLI documentation ([FINAL_DELIVERY.md](../06_TEMPLATES/FINAL_DELIVERY.md)).
