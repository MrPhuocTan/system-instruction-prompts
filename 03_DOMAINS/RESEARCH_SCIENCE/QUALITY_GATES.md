# Scientific Research Domain Quality Gates (`RESEARCH_SCIENCE`)

- **Domain ID:** `DOM-06-RESEARCH_SCIENCE`
- **Governing Standard:** [DOMAIN_SYSTEM_PROMPT.md](./DOMAIN_SYSTEM_PROMPT.md) & [INDEPENDENT_VERIFICATION.md](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md)
- **Signoff Consumers:** `REPRODUCIBILITY_AUDITOR`, `DOMAIN_LEAD`, `SYSTEM_ARCHITECT` (`SA_GATE`), and `PROJECT_MANAGER` (`PM_GATE`)

Every substantive deliverable in `RESEARCH_SCIENCE` (`Level 1`–`Level 4`) must be evaluated against the seven objective pass/fail gates below using canonical statuses (`PASS`, `PARTIAL`, `BLOCKED`, `FAILED`, `NOT VERIFIED`).

---

## 1. Mandatory Domain Verification Gates (`QG-SCI-01` – `QG-SCI-07`)

### `QG-SCI-01` — Research Question Falsifiability & Endpoint Pre-Specification
- **Pass Criteria:** Primary research questions are operationalized into mathematically or empirically falsifiable hypotheses ($H_0$ vs. $H_1$) with explicit estimands, target populations/regimes, and pre-declared primary vs. exploratory endpoints.
- **Fail Trigger:** Vague unfalsifiable claims, shifting outcome definitions after inspecting data, or conflating exploratory data mining with confirmatory proof (`HARKing`).

### `QG-SCI-02` — Literature Quality, Source Triangulation & Zero Fabricated Citations
- **Pass Criteria:** Search queries, databases/sources queried, inclusion/exclusion rules, and retrieval dates are logged; foundational and contradictory studies are represented; `100%` of cited authors, titles, years, and identifiers (`DOI`/`PMID`/`arXiv`/URL) resolve to verified workspace or web sources (or carry explicit `UNVERIFIED_EXTERNAL_CITATION` flags when offline).
- **Fail Trigger:** Any fabricated citation, hallucinated DOI/PMID, misattributed finding, or one-sided cherry-picking that omits known refuting evidence.

### `QG-SCI-03` — Experimental & Observational Methodology Validity
- **Pass Criteria:** Study design explicitly addresses internal, external, construct, and statistical-conclusion validity. Experimental protocols specify randomization, blinding/masking, positive/negative controls, and blocking; observational studies formalize causal graphs (`DAGs`), confounding adjustment sets, and falsification/negative-control checks.
- **Fail Trigger:** Uncontrolled confounding presented as causal effect, missing control baselines, survivorship/selection bias ignored, or pseudo-replication of non-independent units.

### `QG-SCI-04` — Sample Adequacy, Measurement Provenance & Data Quality
- **Pass Criteria:** True independent unit of analysis ($N$) is distinguished from technical replicates ($k$); raw-to-processed data lineage is immutable and scripted; missingness mechanisms (`MCAR`/`MAR`/`MNAR`), outlier rules, measurement error/instrument precision, and schema invariants are verified prior to inference.
- **Fail Trigger:** Destructive in-place mutation of raw datasets, undocumented row drops, unverified synthetic data treated as empirical observation, or silent target leakage.

### `QG-SCI-05` — Statistical Validity & Multiplicity Control
- **Pass Criteria:** Power, precision, or Minimum Detectable Effect (`MDE`) is quantified; model assumptions (normality, homoscedasticity, proportional hazards, independence, MCMC `R-hat <= 1.01` & `ESS`) are diagnostically checked; family-wise (`FWER`) or false-discovery (`FDR`) multiplicity controls are applied; outputs report effect sizes and confidence/credible intervals alongside exact test statistics.
- **Fail Trigger:** Isolated `p < 0.05` thresholding without effect sizes/intervals, uncorrected multiple comparisons ($p$-hacking), violated model assumptions without robust/non-parametric fallback, or interpreting `p > 0.05` in low-power regimes as proof of zero effect.

### `QG-SCI-06` — Computational Reproducibility & Artifact Determinism
- **Pass Criteria:** Clean execution via `run_command` regenerates all numerical tables, metrics, and figures within documented floating-point tolerance from locked raw/seed inputs; dependencies, versions, and `PRNG` seeds are pinned; code and data paths match documented manifests.
- **Fail Trigger:** Hardcoded manual numbers in prose that diverge from script outputs, unseeded stochastic runs with unstable conclusions, or missing environment specifications.

### `QG-SCI-07` — Explicit Limitations, Negative Results & Scope Boundaries
- **Pass Criteria:** Deliverable contains a dedicated limitations section enumerating unmeasured confounders, boundary regimes where models break down, negative or null sensitivity results, data-access constraints, and ethical/dual-use/PII compliance checks.
- **Fail Trigger:** Omitting failed sensitivity runs, over-extrapolating beyond observed parameter ranges, or leaking identifiable human-subject data.

---

## 2. Gate Enforcement Matrix by Complexity Level

| Gate ID | Gate Name | Level 1 (Scoped) | Level 2 (Multi-Step) | Level 3–4 (Multi-Role / High-Assurance) |
| :--- | :--- | :--- | :--- | :--- |
| `QG-SCI-01` | Falsifiability & Estimand Clarity | Self-check by worker | `SA` + Worker contract check | `DOMAIN_LEAD` + `PM_GATE` lock |
| `QG-SCI-02` | Literature & Zero Citation Fabrication | `100%` citation spot-check | Full citation verification log | Independent `LITERATURE_REVIEWER` / `QUALITY_REVIEWER` audit |
| `QG-SCI-03` | Experimental / Causal Methodology | Assumptions stated | Validity matrix required | `RESEARCH_METHODOLOGIST` / `EXPERIMENTAL_DESIGNER` signoff |
| `QG-SCI-04` | Sample & Data Quality Lineage | Schema & $N$ verified | Automated data-quality script | Immutable hash + lineage audit by `REPRODUCIBILITY_AUDITOR` |
| `QG-SCI-05` | Statistical Validity (Power, FDR, CI) | Effect size + CI required | Diagnostics + multiplicity check | Independent `STATISTICIAN` + `REPRODUCIBILITY_AUDITOR` verification |
| `QG-SCI-06` | Computational Reproducibility | Deterministic script run | Seed + dependency lock verified | Clean re-execution audit (`SA_GATE` blocker if `FAILED`) |
| `QG-SCI-07` | Explicit Limitations & Safety | Scope caveats listed | Structured limitations section | Mandatory sensitivity + dual-use/ethics gate (`PM_GATE` blocker) |
