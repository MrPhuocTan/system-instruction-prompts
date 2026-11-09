# Quality Checklist: AI Evaluation Engineer (`ROLE-AIML-008`)

- **Role:** [`AI_EVALUATION_ENGINEER`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Benchmark Integrity, Independence & Decontamination
- [ ] Confirmed strict separation of duties (evaluator did not author or tune models/prompts against the held-out golden test split) and embedded canary strings to prevent training ingestion.
- [ ] Executed `n`-gram (`8`–`13`-gram), entity/ID, temporal, and semantic-embedding decontamination checks between training/retrieval corpora and evaluation splits.
- [ ] Verified balanced benchmark coverage across normal workflows, boundary edge cases, unanswerable/abstention queries, and `OOD`/adversarial perturbations.

## 2. Grader Fidelity & Statistical Rigor
- [ ] Applied deterministic schema, code-execution, numeric, and exact-citation verifiers prior to invoking any stochastic `LLM`-as-a-judge scorer.
- [ ] Validated any `LLM` judge against human-annotated gold labels (`Cohen's kappa`, `TPR`/`TNR` `Rogan-Gladen` correction), `A/B` vs. `B/A` position-swap symmetry, and verbosity neutrality.
- [ ] Reported `95%` bootstrap confidence intervals and paired statistical tests (`McNemar` / permutation test) alongside calibration (`ECE`, Brier) and latency/cost guardrails.

## 3. Disaggregated Slice, Fairness & Red-Team Coverage
- [ ] Audited worst-slice metrics across cohorts, input lengths, languages, and rare classes to guarantee aggregate lift does not conceal subgroup harm.
- [ ] Executed non-destructive red-team probes covering direct/indirect prompt injection, jailbreaks, `PII`/secret extraction, ungrounded hallucination, and tool-argument abuse.

## 4. Raw Trace Inspection & Honest Reporting
- [ ] Manually inspected `>= 20`–`50` raw model inputs, outputs, and grader rationales to build an empirical error taxonomy rather than trusting aggregate numbers blindly.
- [ ] Verified evaluation scripts pass unit tests on synthetic known-good (`100%` score) and known-bad (`0%` score) edge cases to rule out silent grader bugs.
- [ ] Confirmed zero unredacted `PII`, secrets, or destructive payloads exist inside evaluation fixtures or red-team logs.

## 5. Gate Verdict & Handoff Completeness
- [ ] Issued an explicit gate status (`PASS` / `PARTIAL` / `BLOCKED` / `FAILED` / `NOT VERIFIED`) mapped item-by-item against `AIML-QG-01` through `AIML-QG-09`.
- [ ] Provided reproducible CLI evaluation commands and dataset `SHA-256` digests to [`SYSTEM_ARCHITECT`](../../../../02_CORE_ROLES/SYSTEM_ARCHITECT/SYSTEM_PROMPT.md) and [`PROJECT_MANAGER`](../../../../02_CORE_ROLES/PROJECT_MANAGER/SYSTEM_PROMPT.md).
- [ ] Clearly separated empirically executed local evaluations from `NOT VERIFIED` items requiring live GPU clusters or external APIs.
