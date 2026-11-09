# Quality Checklist: Business Strategist (`BUSINESS_STRATEGIST` — `ROLE-BIZ-003`)

- **Role ID:** `ROLE-BIZ-003`
- **Canonical Role:** `BUSINESS_STRATEGIST`
- **Parent Domain:** `BUSINESS_PRODUCT` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). Verify strategic coherence and economic math before `PASS`.

## 1. Structural Diagnosis & Customer Value Grounding
- [ ] Diagnosis isolates the root competitive/economic bottleneck backed by graded customer and industry evidence rather than generic buzzwords (`BIZ-QG-01`).
- [ ] At least 3 genuinely distinct strategic options (including calibrated `Status Quo` baseline) pass the Lafley-Martin Opposite-Choice Test (`BIZ-QG-03`).
- [ ] `Where NOT to Play` (excluded segments, geographies, channels, and features) and resource opportunity costs are explicitly locked.

## 2. Moat Durability, Retaliation & Unit Economics
- [ ] Claimed competitive advantages specify both the **economic benefit** (pricing power, lower unit cost, higher retention) and the **structural barrier to imitation** (7 Powers analysis).
- [ ] Multi-move competitor retaliation (incumbent bundling, price cuts, fast-follower cloning, supplier squeeze) is war-gamed explicitly.
- [ ] Strategy and pricing/packaging tiers are grounded in verified gross-margin-adjusted unit economics (`Contribution Margin`, `LTV:CAC`, `Payback`, cannibalization impact) computed via `run_command` (`BIZ-QG-02`).

## 3. Capability Feasibility & WWHTBT Validation Plan
- [ ] Required engineering, GTM, support, and balance-sheet capabilities are realistic and sequenced across horizon gates (`BIZ-QG-04`).
- [ ] Critical assumptions are framed as falsifiable "What Would Have to Be True" (WWHTBT) conditions with concrete empirical tests and kill/pivot thresholds (`BIZ-QG-05`).

## 4. Stakeholder Governance & Ethical Compliance
- [ ] Executive decision options, RACI accountability, and cross-domain handoffs (`ECONOMICS_FINANCE`, `IT_SOFTWARE`, `LEGAL_COMPLIANCE`) are clearly specified (`BIZ-QG-06`).
- [ ] Output contains zero antitrust-violating collusion/predatory schemes, zero emojis, zero promotional "AI Sign" fluff, and zero unfinished placeholders.

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
