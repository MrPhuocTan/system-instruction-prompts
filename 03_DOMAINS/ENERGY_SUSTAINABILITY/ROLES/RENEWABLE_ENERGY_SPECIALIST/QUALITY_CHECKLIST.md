# Quality Checklist: Renewable Energy Specialist (`ROLE-ENG-003`)

- **Role:** [RENEWABLE_ENERGY_SPECIALIST](./SYSTEM_PROMPT.md)
- **Domain Gates:** [QUALITY_GATES.md](../../QUALITY_GATES.md) (`QG-ENG-001`, `QG-ENG-003`)

## 1. Meteorological Resource & Solar/Wind Physics QA
- [ ] Site coordinates, elevation, timezone offset, and air-density / surface-albedo parameters are verified against source metadata.
- [ ] Hourly solar geometry uses interval-midpoint (`30`-minute) zenith/azimuth conventions with zero sunrise/sunset timestamp shift artifacts.
- [ ] Irradiance components (`GHI`, `DNI`, `DHI`) satisfy physical closure (`GHI = DNI*cos(theta_z) + DHI`) and clear-sky upper bounds.
- [ ] Wind speed series are screened for sensor icing, mast shading, hub-height shear extrapolation bounds, and site air-density power-curve scaling.
- [ ] Long-term `MCP` reference correlation and Interannual Variability (`IAV`) statistics are documented separately from single-year `TMY` profiles.

## 2. Plant Configuration & Multiplicative Loss Cascade
- [ ] Both `MW_dc` (`kWp`) and `MW_ac` (`POI` limit) ratings, `DC:AC` `ILR`, `GCR`/pitch, and turbine hub height/rotor diameter are explicitly labeled in all tables.
- [ ] Energy loss waterfall compounds stages multiplicatively ($\prod (1 - L_i)$) rather than summing percentages arithmetically.
- [ ] Shading/wake, IAM/spectral, thermal derating, module/string mismatch, DC/AC ohmic, inverter clipping, availability, auxiliary, transformer, and curtailment losses are all accounted for.
- [ ] Hourly `8760` AC export never exceeds inverter rating or `POI` interconnect cap; DC-coupled clipping recapture respects `BESS` charge-power and `SoC` headroom limits.

## 3. Degradation, `BESS` Sizing & `P50`/`P90` Uncertainty
- [ ] Year-1 (`LID`/`BOI`) and annual linear degradation rates are modeled across every contract year (`Year 1` through `Year N`).
- [ ] `BESS` sizing deducts `SoC` floor/ceiling buffers, converter/transformer losses, HVAC auxiliary loads, and `BOL`-to-`EOL` cycle + calendar fade, with an explicit augmentation schedule.
- [ ] `P50`, `P75`, `P90`, and `P99` exceedance tables distinguish `1-Year` from `10-Year`/`20-Year` `IAV` scaling ($\sigma_{IAV}/\sqrt{N}$) with full `RSS` uncertainty components.

## 4. Verification, Safety & Bankability Disclosure
- [ ] Automated Python check confirms waterfall product equals net `8760` sum ($\le 0.01\%$ delta) and $P99 < P90 < P75 < P50$ monotonically.
- [ ] Zero nighttime positive solar PV generation or wind output above high-wind cutout speed (`hysteresis` band) occurs in the `8760` series.
- [ ] Weather-corrected Performance Ratio (`PR`) and temperature-corrected specific yield (`kWh/kWp/yr`) are reported with exact formula definitions.
- [ ] Open-source (`pvlib`/Python) vs. commercial (`PVsyst`/`WindPRO`) simulation scope and satellite vs. ground-mast data tiers are transparently disclosed.
- [ ] `NFPA 855` / `UL 9540A` `BESS` thermal-runaway spacing, structural load (`ASCE 7` / `IEC 61400`), and aviation glare hazards are flagged for human PE review.
- [ ] Measured site facts, loss assumptions, statistical yield estimates, and unverified geotechnical/curtailment risks are separated in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
