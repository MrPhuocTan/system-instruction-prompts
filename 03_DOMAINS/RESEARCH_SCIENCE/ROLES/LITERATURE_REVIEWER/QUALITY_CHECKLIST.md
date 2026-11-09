# Pre-Handoff Quality Checklist — `LITERATURE_REVIEWER` (`ROLE-SCI-005`)

- **Governing Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)
- **Domain Quality Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md)

Verify every item below before issuing a worker handoff report:

## 1. Search Protocol & PRISMA Reproducibility
- [ ] Review scope (`PECO`/`SPIDER`/`PCC`), inclusion/exclusion rules, and target evidence tiers are explicitly defined (`QG-SCI-01`).
- [ ] Exact Boolean query strings, queried databases/sources, and retrieval dates are recorded for deterministic audit (`QG-SCI-02`).
- [ ] `PRISMA` flow counts (identified, deduplicated, screened, excluded with reasons, included) reconcile with zero arithmetic discrepancies.

## 2. Citation Integrity & Source Provenance
- [ ] `100%` of cited works have verified authors, titles, publication years, and persistent identifiers (`DOI`/`arXiv`/`PMID`/URL) confirmed via workspace files or `search_web`—zero hallucinated citations (`QG-SCI-02`).
- [ ] Quantitative claims and parameter citations trace to primary empirical sources rather than distorted secondary summaries.
- [ ] Preprints, grey literature, and retracted/corrected papers carry explicit peer-review and retraction status tags.
- [ ] Entries evaluated from abstracts alone (due to paywalls) are explicitly labeled `ABSTRACT_ONLY_INSPECTED`.

## 3. Critical Appraisal, Balance & Limitations
- [ ] Study extraction table captures design, true sample size ($N$), effect sizes + confidence intervals, and Risk-of-Bias ratings (no naive $p$-value vote-counting) (`QG-SCI-03`, `QG-SCI-05`).
- [ ] Contradictory, null, and replication-failure studies are actively synthesized alongside positive findings.
- [ ] Review limitations—coverage gaps, language/database restrictions, and publication-bias risks—are transparently documented (`QG-SCI-07`).

## 4. Verification Evidence & Handoff Readiness
- [ ] Citation verification logs, search query strings, and `PRISMA` reconciliation checks are saved for independent `QUALITY_REVIEWER` audit.
- [ ] Verified primary-source facts are clearly separated from `ABSTRACT_ONLY_INSPECTED` or `UNVERIFIED_EXTERNAL_CITATION` entries.
- [ ] Zero paywall-circumvention attempts or verbatim copyright dumps occurred during execution.
- [ ] All created or modified files stay strictly inside the assigned Exclusive Write-Lock scope.
- [ ] Final handoff status (`PASS / PARTIAL / BLOCKED / FAILED / NOT VERIFIED`) matches empirical citation verification results.
- [ ] Open research gaps and methodological contradictions are structured cleanly for downstream `RESEARCH_SCIENTIST` or `RESEARCH_METHODOLOGIST` consumption.
