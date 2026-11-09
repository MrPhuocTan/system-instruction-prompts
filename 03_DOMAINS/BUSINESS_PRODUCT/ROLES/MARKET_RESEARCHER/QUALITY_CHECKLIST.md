# Quality Checklist: Market Researcher (`MARKET_RESEARCHER` — `ROLE-BIZ-007`)

- **Role ID:** `ROLE-BIZ-007`
- **Canonical Role:** `MARKET_RESEARCHER`
- **Parent Domain:** `BUSINESS_PRODUCT` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). Verify methodological bias controls and statistical bounds before `PASS`.

## 1. Problem Framing, Sampling Frame & Evidence Honesty
- [ ] Research questions map directly to concrete product, pricing, ICP, or positioning decisions (`BIZ-QG-01`, `BIZ-QG-03`).
- [ ] Zero respondent quotes, sample sizes, or survey outcomes are fabricated; illustrative personas/hypotheses are explicitly tagged `[HYPOTHESIS — REQUIRES VALIDATION]`.
- [ ] Target sampling frame covers active users, churned users, closed-lost/no-decision prospects, and non-customers as appropriate to prevent survivorship bias.

## 2. Instrument Hygiene & Bias Elimination
- [ ] Qualitative interview guides obey Mom Test principles (open-ended questions anchored in past behavior, workflows, and actual budget spent — zero leading feature pitches).
- [ ] Survey instruments eliminate double-barreled questions, unbalanced scales, unanchored frequency terms (`"often"` vs. `"3–5 times/week"`), and order bias (randomizing option lists).
- [ ] Quantitative survey plans include screener qualification, attention/red-herring traps, speeder/straight-liner cleaning rules, and target sample-size power math (`BIZ-QG-05`).

## 3. Quantitative Pricing, Segmentation & Economic Grounding
- [ ] Survey/pricing datasets analyzed via `run_command` report cleaned vs. raw $n$, 95% margins of error, stated-vs-revealed intent haircuts, and flag any $n < 30$ subgroup as directional-only.
- [ ] Pricing recommendations (Van Westendorp, Gabor-Granger, Conjoint) cross-check willingness-to-pay against unit variable cost-to-serve and gross-margin floors (`BIZ-QG-02`, `BIZ-QG-04`).

## 4. Ethics, Privacy & Cross-Functional Alignment
- [ ] Respondent PII is anonymized, competitor research uses strictly public/ethical sources (zero pretexting), and stakeholder RACI action items are clear (`BIZ-QG-06`) with zero emojis or unfinished placeholders.

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
