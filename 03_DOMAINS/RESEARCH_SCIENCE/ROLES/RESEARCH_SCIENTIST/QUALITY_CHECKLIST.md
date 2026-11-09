# Pre-Handoff Quality Checklist — `RESEARCH_SCIENTIST` (`ROLE-SCI-001`)

- **Governing Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Quality Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

Verify every item below before issuing a worker handoff report (`PASS` requires `100%` satisfaction or explicit `NOT VERIFIED` disclosure):

## 1. Epistemic & Hypothesis Rigor
- [ ] Primary research question is framed as a falsifiable hypothesis pair ($H_0$ vs. $H_1$) with explicit observable refutation criteria (`QG-SCI-01`).
- [ ] Pre-specified confirmatory claims are strictly separated from exploratory or post-hoc observations (zero `HARKing`).
- [ ] Causal terminology is used only where experimental randomization or defended causal identification warrants it; associational claims use non-causal language.
- [ ] Assumptions ledger explicitly distinguishes verified empirical facts, mathematical axioms, simplifying approximations, and unresolved uncertainties.

## 2. Mathematical, Mechanistic & Data Integrity
- [ ] All equations, variables, physical units, and coordinate/normalization conventions are dimensionally consistent across prose and code.
- [ ] Analytical or numerical models are tested against known boundary conditions, conservation invariants, and asymptotic limiting cases.
- [ ] Raw input datasets remain unmodified; preprocessing, exclusions, and transformations are scripted and auditable (`QG-SCI-04`).
- [ ] Point estimates are accompanied by uncertainty bounds (confidence/credible intervals, error bars, sensitivity ranges) rather than isolated $p$-values (`QG-SCI-05`).

## 3. Citation, Reproducibility & Safety Hygiene
- [ ] `100%` of cited papers, authors, years, and identifiers (`DOI`/`PMID`/`arXiv`/URL) are verified against workspace files or `search_web` (or explicitly flagged `UNVERIFIED_EXTERNAL_CITATION`) (`QG-SCI-02`).
- [ ] Simulation/analysis scripts run deterministically via `run_command` with pinned `PRNG` seeds and regenerate reported tables/figures (`QG-SCI-06`).
- [ ] Dedicated limitations section documents negative results, model breakdown regimes, unmeasured confounders, and runtime/data constraints (`QG-SCI-07`).
- [ ] Zero fabricated empirical measurements, zero unredacted human-subject PII, and zero dual-use hazard instructions are present.

## 4. Verification Evidence & Handoff Readiness
- [ ] Exact `run_command` invocations, exit codes, and output artifact paths are recorded for independent `REPRODUCIBILITY_AUDITOR` inspection.
- [ ] All modified files reside strictly inside the assigned Exclusive Write-Lock scope.
- [ ] Unverified external dependencies (offline citations, unexecuted wet-lab validations) are explicitly marked `NOT VERIFIED` rather than `PASS`.
- [ ] Cross-stream dependencies and follow-up validation steps are documented for `PM` and `SA`.
- [ ] Final role status (`PASS / PARTIAL / BLOCKED / FAILED / NOT VERIFIED`) aligns strictly with observed verification evidence.
