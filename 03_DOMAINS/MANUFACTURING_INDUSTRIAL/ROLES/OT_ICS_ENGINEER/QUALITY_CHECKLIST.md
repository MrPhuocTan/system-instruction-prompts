# Quality Checklist — Operational Technology & ICS Engineer (`ROLE-MFG-004`)

Verify every item below before submitting a handoff report under [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md):

## 1. PLC Determinism & Control Logic Integrity (`IEC 61131-3`)
- [ ] Cyclic control routines contain zero unbounded `WHILE`/`REPEAT` loops, recursion, blocking network calls, or dynamic heap allocations; worst-case scan budget (`WCET`) is bounded.
- [ ] Physical output tags are written in exactly one canonical output-mapping routine (zero double-coil conflicts), with `STOP` / `E-Stop` overrides dominating `START` commands (`Reset-Dominant` safety latches).
- [ ] Analog inputs implement `NAMUR NE 43` out-of-range / wire-break detection (`< 3.6 mA` or `> 21.0 mA`), engineering-unit scaling bounds, and explicit fallback/trip behavior.
- [ ] Closed-loop PID blocks enforce output clamping, integral anti-windup, derivative filtering, and bumpless `MANUAL` $\leftrightarrow$ `AUTO` tracking.
- [ ] State machines (`PackML` / `ISA-88`) handle `Holding`, `Aborting`, `Stopping`, and explicit `ELSE` fault states without unguarded transitions on power recovery (require deliberate operator `Reset` + `Start`, never auto-restart after fault/power loss).

## 2. Functional Safety Separation & Alarm Management
- [ ] Safety Instrumented Functions (`IEC 61511` / `IEC 61508` `SIL`) and Emergency Stops (`ISO 13850`) remain physically and logically independent of standard `BPCS` PLC/HMI code.
- [ ] Cause-and-Effect (`C&E`) matrix unambiguously defines every trip initiator, voting logic (`1oo1`, `1oo2`, `2oo3`), safe actuator state (`fail-open` vs. `fail-closed`), and reset permissive.
- [ ] `ISA-18.2` alarm configuration specifies deadbands, on/off delay timers, priority tiers, and operator response actions to prevent alarm flooding.

## 3. `IEC 62443` OT Architecture & Cybersecurity Hygiene
- [ ] Network topology enforces Purdue Model segmentation (`Levels 0–3`, `Level 3.5 IDMZ`, `Level 4 IT`) with explicit Zone & Conduit protocol/port allowlists.
- [ ] Unauthenticated cleartext protocols (`Modbus TCP`, legacy `S7comm`) are isolated inside local Level 1 conduits or wrapped via authenticated `OPC UA` (`SignAndEncrypt`) gateways at zone boundaries; zero hardcoded credentials exist in artifacts.
- [ ] Diagnostic and assessment steps use passive configuration/PCAP inspection only—never active port/vulnerability scanning against live production controllers.

## 4. Offline Verification, Commissioning & Human Approval Gate
- [ ] Nominal state sequences, interlock trips, comms drops, and simultaneous start/stop edge cases were verified via Python simulation (`run_command`).
- [ ] Controller task cycle period, watchdog timeout, and Process Safety Time (`PST`) margins are explicitly tabulated (`WCET <= 50%` of scan period).
- [ ] Vendor PLC dialect (`TIA Portal`, `Studio 5000`, `TwinCAT`, `CODESYS`) and firmware assumptions are explicitly documented.
- [ ] Backup/restore rollback plan and checksum verification steps are included for every controller configuration artifact.
- [ ] Point-to-point `FAT` emulator tests and `SAT` physical loop-check (`4 mA / 12 mA / 20 mA` injection + actuator stroke verification) checklists are provided.
- [ ] `OSHA 1910.147` `LOTO` isolation and bypassed-interlock log controls are specified for commissioning and sensor replacement.
- [ ] Handoff evidence conforms to [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md) with zero live credentials or plant IP secrets exposed.
- [ ] Deliverable carries an explicit **Management of Change (`MOC`) + Mandatory Human Approval** gate blocking autonomous live PLC/SCADA downloads.
