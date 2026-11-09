# Quality Checklist: Quantitative Analyst (`QUANTITATIVE_ANALYST` — `ROLE-FIN-004`)

- **Role ID:** `ROLE-FIN-004`
- **Canonical Role:** `QUANTITATIVE_ANALYST`
- **Parent Domain:** `ECONOMICS_FINANCE` ([DOMAIN_INDEX.md](../../DOMAIN_INDEX.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md))
- **Role Specification:** [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md)

> Pre-handoff verification checklist aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md). Every mathematical and empirical check must pass deterministically via `run_command`.

## 1. Mathematical & Arbitrage-Free Integrity
- [ ] Probability measure ($\mathbb{Q}$ risk-neutral for pricing vs. $\mathbb{P}$ physical for portfolio/risk forecasting), day-count convention (`ACT/360`, `ACT/365`, `30/360`), and compounding basis (continuous vs. discrete) are explicitly stated and consistent (`FIN-QG-03`).
- [ ] Limiting-case and no-arbitrage identities pass automated tests: put-call parity, martingale discounted asset expectation, boundary conditions ($S \to 0, \sigma \to 0, T \to 0$), and non-negative butterfly/calendar implied variance.
- [ ] Analytical Greeks match central finite-difference bump-and-revalue approximations within documented numerical tolerance; Monte Carlo outputs include standard error bars and deterministic RNG seeds.

## 2. Point-in-Time Data Hygiene & Leakage Prevention
- [ ] Fundamental, macro, and corporate-action inputs strictly enforce public `as-of` availability timestamps (filing/release date, never fiscal period-end date) (`FIN-QG-01`).
- [ ] Investment universe handles delistings, bankruptcies, mergers, splits, and dividends cleanly without survivorship bias.
- [ ] Rolling z-scores, PCA factors, covariance matrices, and ML parameters are fit strictly inside expanding/rolling training windows with purged/embargoed gaps prior to evaluation windows.

## 3. Portfolio Optimization, Transaction Costs & Stress Testing
- [ ] Covariance matrices are verified positive-semi-definite (eigenvalue check $\lambda_{\min} \ge 0$) with shrinkage or factor regularization documented (`FIN-QG-02`).
- [ ] Backtests report both Gross and Net-of-Cost metrics (Sharpe, Sortino, Information Ratio, Calmar, Max Drawdown, annualized turnover) incorporating spread, commission, market-impact, and short-borrow assumptions (`FIN-QG-05`).
- [ ] Strategy/pricing behavior is stress-tested across historical liquidity/volatility crises and $2\times$–$3\times$ transaction-cost shocks (`FIN-QG-06`, `FIN-QG-07`).

## 4. Statistical Honesty, Reproducibility & Governance
- [ ] Trial count, parameter degrees of freedom, out-of-sample decay, and Deflated Sharpe / multiple-testing caveats are transparently disclosed (`FIN-QG-08`).
- [ ] Zero live order-execution code runs without explicit human authorization; deliverables contain zero emojis/placeholders and include SR 11-7 model-risk and non-fiduciary notices (`FIN-QG-09`).

## 5. Handoff & Governance Readiness
- [ ] Exclusive Write-Lock boundaries were strictly honored (`0` files modified outside assigned workstream paths).
- [ ] Deterministic `run_command` verification commands, script exit codes, and observed numerical outputs are recorded.
- [ ] Verified empirical facts, explicit model assumptions, and any `PARTIAL` or `NOT VERIFIED` items are cleanly separated.
- [ ] Internal relative Markdown links resolve cleanly on disk with zero `TODO`/`TBD` tokens or decorative prose.
- [ ] Structured 8-item Worker Handoff Report is complete and ready for `SA_GATE` and `PM_GATE` signoff.
