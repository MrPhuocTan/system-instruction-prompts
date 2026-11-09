# Quality Checklist — Quality Control & Six Sigma (`ROLE-MFG-003`)

Verify every item below before submitting a handoff report under [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md):

## 1. Measurement System Analysis (`MSA` / Gage R&R)
- [ ] Calibration status and Test Uncertainty Ratio (`TUR >= 4:1` target) are verified before accepting raw measurement datasets.
- [ ] Crossed or nested ANOVA Gage R&R decomposes Repeatability (`EV`), Reproducibility (`AV`), Operator-by-Part interaction, and Part-to-Part (`PV`) variance accurately.
- [ ] `%GRR` (both `%Study Variation` and `%Tolerance`) and Number of Distinct Categories (`ndc >= 5`) are computed and dispositioned (`< 10%` pass; `10–30%` conditional with risk rationale; `> 30%` fail).

## 2. Statistical Process Control (`SPC`) & Capability Rigor
- [ ] Subgroup scheme follows rational subgrouping (capturing within-subgroup common cause and between-subgroup special cause) and checks serial autocorrelation.
- [ ] Control limits are derived strictly from process dispersion ($\mu_{\text{hat}}, \sigma_{\text{within}}$ using exact $d_2 / c_4 / A_2 / B_3 / B_4$ constants)—never from `USL`/`LSL` specification limits.
- [ ] Normality is tested quantitatively (`Anderson-Darling` / `Shapiro-Wilk`); skewed/bounded geometric tolerances use valid transformations or non-parametric capability ($C_{npk}$).
- [ ] Both short-term ($C_p, C_{pk}$) and overall ($P_p, P_{pk}$) indices are reported alongside `95%` lower confidence bounds (`n >= 100` / `25+` subgroups recommended; small-sample penalty disclosed if smaller).

## 3. Sampling Plans, DOE & 8D / CAPA Traceability
- [ ] Lot acceptance sampling specifies both Producer Risk (`AQL`, $\alpha$) and Consumer Risk (`LTPD`/`RQL`, $\beta$) via exact hypergeometric/binomial OC curve calculations; zero-acceptance or `100%` automated inspection mandated for `Severity 9–10` characteristics.
- [ ] `DOE` designs state resolution (`IV` or `V+` for factor screening/modeling), randomization, center-point curvature checks, and residual diagnostics.
- [ ] `8D` / `CAPA` records distinguish **Occurrence Root Cause** and **Escape Root Cause**, reject `"human error"` closures, verify containment of suspect WIP/field lots (`D3`), and update PFMEA + Control Plan (`D7`).

## 4. Verification, Traceability & Integrity Gates
- [ ] All ANOVA tables, Shewhart constants, p-values, OC curves, and capability indices were computed deterministically via `run_command`.
- [ ] Attribute inspection gages (Go/No-Go plugs, visual standards) verify `AIAG` kappa agreement ($\kappa \ge 0.75$) and zero false-accept calls on master border samples.
- [ ] Any outlier exclusion documents a verified physical assignable cause; sensitivity results with and without the contested point are reported.
- [ ] Lot/serial genealogy and `ISO 9001` / `IATF 16949` / `ISO 13485` document revision IDs are linked across PFMEA, Control Plan, and inspection sheets.
- [ ] Out-of-control Action Plans (`OCAP`) define immediate `100%` containment sorting back to the last known good verification check.
- [ ] Independent reviewer separation is maintained—quality sign-off is not performed by the same agent instance that authored process parameters.
- [ ] Requalification / annual layout inspection cadence (`IATF 16949` clause `8.6.2`) is defined in the ongoing Control Plan.
- [ ] Gauge bias and linearity across the operating range were checked alongside repeatability and reproducibility (`ANOVA`).
- [ ] Empirical plant measurements are explicitly separated from simulated or parametric baseline assumptions in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] Formal Material Review Board (`MRB`) + Mandatory Human Approval Gate is enforced before any `use-as-is` concession or specification deviation.
