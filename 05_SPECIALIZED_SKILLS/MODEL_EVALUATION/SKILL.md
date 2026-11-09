---
name: model-evaluation
description: "Use this skill when evaluating machine learning, deep learning, computer vision, NLP, or LLM/RAG systems for data leakage, baseline uplift, slice fairness, calibration, out-of-distribution robustness, and cost-latency trade-offs."
---

# Model Evaluation

## Skill Metadata
- **Skill ID:** `SKL-SPEC-009`
- **Name:** `model-evaluation`
- **Domain:** `AI_MACHINE_LEARNING, DATA_ANALYTICS`
- **Version:** `1.0.0`

## Purpose
Rigorously evaluate predictive, generative, retrieval-augmented (`RAG`), and multimodal AI systems against real-world operational utility rather than aggregate benchmark vanity metrics (`Low model loss != real-world problem solved`). This skill enforces leakage-free split auditing, non-trivial baseline comparisons, subgroup slice disaggregation, probability calibration, out-of-distribution (`OOD`) and adversarial robustness testing, qualitative error-taxonomy inspection, and inference cost/latency profiling.

## Required Competencies
- Leakage-proof evaluation design: temporal/rolling-origin splits, entity/group-disjoint splits (user/patient/document/camera ID), near-duplicate decontamination (`MinHash`/`embedding similarity`), and preprocessing pipeline isolation.
- Task-aligned metric selection: `PR-AUC`, `ROC-AUC`, `F_beta` at operational decision thresholds, `RMSE`/`MAE`/`Pinball Loss`, calibration (`ECE`, Brier score), ranking (`NDCG@k`, `MRR`), and grounded `RAG`/LLM rubrics (faithfulness, citation recall, hallucination rate, human-calibrated judge agreement).
- Disaggregated slice analysis, distribution-shift (`OOD`) stress testing, and adversarial/prompt-injection red-teaming.
- Operational deployment Pareto evaluation across quality, `p95/p99` TTFT/latency, VRAM/memory footprint, and cost per 1,000 requests.

## Prerequisites
- Evaluation datasets, split generation scripts, baseline/candidate inference code, and operational failure-cost asymmetry inspected via `read_file`.
- Reproducibility controls aligned with [SCIENTIFIC_REPRODUCIBILITY](../SCIENTIFIC_REPRODUCIBILITY/SKILL.md) and latency harnessing aligned with [PERFORMANCE_BENCHMARKING](../PERFORMANCE_BENCHMARKING/SKILL.md).
- Clear business/domain cost ratio between False Positives (`FP`) and False Negatives (`FN`) or hallucination severity.

## Workflow
1. **Audit Data Splits & Eliminate Leakage First:** Verify zero entity overlap, future-timestamp lookahead, target proxy features, or benchmark test-set contamination across train, validation, and held-out test partitions before trusting any metric.
2. **Benchmark Against Simple & Strong Baselines:** Always compare candidate models against (a) trivial majority/persistence baseline, (b) simple interpretable heuristic/linear/gradient-boosted or zero-shot prompt baseline, and (c) current production incumbent on identical splits.
3. **Compute Operational Metrics & Confidence Bounds:** Evaluate calibration (`ECE`), threshold-specific precision/recall/cost curves (tuning decision thresholds strictly on validation, never on held-out test), and bootstrap `95%` confidence intervals so noise is never mistaken for model uplift.
4. **Disaggregate Across Critical Slices & Tail Cohorts:** Break performance down across minority classes, demographic/regional slices, input lengths, noisy/low-light inputs, cold-start entities, and rare high-severity edge cases where aggregate accuracy hides failure.
5. **Stress-Test `OOD`, Perturbations & Adversarial Inputs:** Probe behavior under temporal drift, corrupted/missing features, formatting variations, negation/distractor traps, and (for LLMs/agents) prompt injection, jailbreak attempts, and unanswerable abstention cases (`I do not have sufficient evidence`).
6. **Conduct Qualitative Error Taxonomy & Cost-Latency Audit:** Manually inspect `>= 30-50` representative failure cases via `read_file` to categorize root error modes (label noise vs. missing context vs. reasoning failure), and pair quality gains with `p95` latency, throughput, and unit inference cost.

## Tools and Techniques
- **Leakage & Contamination Scanner:** Hash/n-gram/entity-ID intersection script via `run_command` proving `|Train_Entities intersect Test_Entities| == 0` and `max(Train_Time) < min(Test_Time)`.
- **LLM-as-a-Judge Bias Controls:** When using model-based evaluators, enforce rubric-anchored pairwise/pointwise scoring with position-swap debiasing, length-bias checks, deterministic `temperature=0`, and spot-audit agreement (` Cohen's kappa `) against ground-truth human/programmatic labels.
- **Calibration & Abstention Curve:** Plot reliability diagrams and accuracy-coverage curves verifying confidence scores reflect true empirical correctness probabilities.
- **Structured Failure Taxonomy Table:** Bucket inspected errors by concrete cause and actionable fix (data curation, retrieval chunking, threshold shift, architecture change) rather than blind hyperparameter sweeps.

## Verification Requirements
- Held-out test evaluation runs once per final candidate via automated script with verified zero train-test feature/scaler/entity leakage.
- Reported metrics include sample counts (`n`), bootstrap uncertainty intervals, baseline deltas, and operational threshold specifications.
- Qualitative error analysis cites real inspected prediction transcripts/examples rather than aggregate numbers alone.

## Quality Criteria
- **Real-World Task Alignment:** Optimizes business/clinical/engineering utility and abstention safety rather than gaming flawed leaderboard proxies (`accuracy` on 99:1 imbalanced data or uncalibrated `BLEU`/`ROUGE`):
  | Evaluation Gate | Mandatory Check | Failure Indicator |
  | :--- | :--- | :--- |
  | `Split Hygiene` | Entity, group, temporal, and near-duplicate disjointness | Shared user/doc IDs or future features across train/test |
  | `Baseline Uplift` | Trivial + simple heuristic/linear + incumbent comparison | Complex model fails to beat tuned baseline on `PR-AUC`/cost |
  | `Slice & Calibration` | Tail cohort metrics + `ECE` / Brier reliability curve | High aggregate score masking minority-slice collapse |
  | `OOD & Adversarial` | Corruptions, drift, prompt injection, abstention probes | Confident hallucinations on unanswerable/injected inputs |
- **Slice & `OOD` Honesty:** Explicitly flags degraded cohorts and boundary conditions where human-in-the-loop fallback or guardrails are required.
- **Complete Pareto Visibility:** Presents quality alongside latency, memory, and dollar cost so `SA` and `PM` can judge deployment viability honestly.
- **Failure Modes to Avoid:**
  - *Test-Set Overfitting:* Iterating prompts or hyperparameters dozens of times directly against the final held-out test set.
  - *Temporal Lookahead Leakage:* Including full-history customer aggregates or post-event status fields inside training features.
  - *Uncalibrated LLM Judge Bias:* Trusting single-pass LLM judges without position-swap, verbosity normalization, or human-label spot checks.
  - *Silent Threshold Mismatch:* Reporting `ROC-AUC` without verifying false-positive blast radius at the actual production operating threshold.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [SECURITY_AND_PRIVACY.md](../../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md), safety-critical human oversight rules, or regulatory AI governance.
- Screen generative/agentic models explicitly for secret memorization, PII regurgitation, unsafe tool invocation, and indirect prompt-injection susceptibility before production sign-off.
- Never deploy automated model decisions into high-stakes clinical, legal, financial-credit, or physical-safety domains without documented fairness/safety validation and human oversight gates.

## Expected Deliverables
- **Leakage & Split Integrity Audit** confirming entity, temporal, and contamination isolation across partitions.
- **Baseline-vs-Candidate Evaluation Scorecard** (overall + disaggregated slice metrics, `95% CIs`, calibration, `OOD`/adversarial pass rates, and cost/latency profile).
- **Qualitative Error Taxonomy & Deployment Readiness Brief** detailing top failure modes, recommended guardrails/thresholds, and operational monitoring drift triggers.
