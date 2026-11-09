# Quality Checklist — Robotics Safety & Validation Engineer (`ROLE-ROB-005`)

Verify every item below before granting safety gate clearance under [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md):

## 1. `ISO 12100` HARA & Functional Safety Architecture (`ISO 13849` / `IEC 61508`)
- [ ] Hazard Analysis (`HARA`) covers all lifecycle modes (automatic, manual/teach `<= 250 mm/s` with 3-position enabling device, maintenance, fault recovery) AND end-effector + payload hazards.
- [ ] Required Performance Level (`PLr a–e`) or `SIL` is derived transparently for every identified hazard and mapped to a formal Safety Requirements Specification (`SRS`).
- [ ] Zero credit (`PL = none / SIL = 0`) is assigned to Linux, `ROS 2`, Python, AI/ML models, or standard non-safety MCU software for primary safety risk reduction.
- [ ] Dual-channel hardware safety chains (`Cat. 3 / Cat. 4`) specify cross-fault monitoring, discrepancy timeouts, Safe Torque Off (`STO`), and Safe Brake Control (`SBC` preventing vertical gravity drop!).
- [ ] Stop Category (`IEC 60204-1` `Cat. 0` vs. `Cat. 1`) is justified quantitatively against manipulator/vehicle kinetic coasting vs. controlled regenerative braking distance.
- [ ] Single Point of Control (`ISO 10218`) prevents simultaneous remote/network command execution when local teach/manual mode is active, and safeguard resets require deliberate manual latch outside the hazard zone (zero auto-restart).

## 2. Protective Distance (`ISO 13855`) & Collaborative Biomechanics (`ISO/TS 15066`)
- [ ] Protective separation distance $S_p$ is computed via Python (`run_command`) at maximum payload, full reach, worst-case floor friction, human approach speed ($1600\text{–}2000\text{ mm/s}$), and total safety-chain reaction latency.
- [ ] Collaborative `PFL` velocity limits bound transient energy transfer $\frac{1}{2}\mu v_{\text{rel}}^2 \le \frac{F_{\max}^2}{2 k_{\text{body}}}$ and contact pressure ($F / A_{\text{contact}}$) across gripper/part edges, strictly excluding head/neck/face trajectories.
- [ ] `AMR`/`AGV` safeguarding (`ISO 3691-4`) covers overhanging/3D obstacles, negative obstacles (docks/stairs), stability/tip-over during E-Stop, and muted-zone transitions.

## 3. Sim-to-Real Pre-Flight, Commissioning & Mandatory Human Approval Gate
- [ ] Independent audit confirms motion, navigation, and firmware modules passed perturbed sim-to-real gates (`QG-ROB-01` through `QG-ROB-04`).
- [ ] Separation of duties is verified: safety sign-off was not executed by the agent instance that authored robot control or firmware code.
- [ ] All software and firmware artifacts boot strictly in `DISARMED / SIMULATION` mode with verified heartbeat timeout zeroing.
- [ ] `STPA` unsafe control action (`UCA`) matrix covers missing, spurious, delayed/out-of-order, and prematurely/late-terminated commands.
- [ ] Lockout/Tagout (`OSHA 1910.147` / `ISO 14118`) pneumatic, electrical, and gravity-blocking steps are specified for cell maintenance entry.
- [ ] Physical commissioning test plan specifies single-fault wire-break injection, calibrated stop-time measurement, and biofidelic force/pressure testing.
- [ ] Residual hazards, operator warning labels, and PPE / training prerequisites (`ISO 12100` Step 3) are documented without omissions.
- [ ] Emergency manual brake-release procedure (`ISO 10218-1`) specifies trapped-person rescue steps while preventing uncontrolled arm drop under gravity.
- [ ] Safety PLC / safety-scanner configuration checksum (`CRC`) and password/key-switch tamper lock controls are verified.
- [ ] Cyber-physical access controls (`SROS2` / safety network segmentation) prevent unauthorized network modification of safety zones.
- [ ] Periodic proof-test interval (`T1`) and diagnostic test schedule are specified for all safety-related parts of control systems (`SRP/CS`).
- [ ] Calculated analytical margins vs. unverified field commissioning measurements are explicitly distinguished in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] Prominent **Mandatory Human Approval** gate blocks any transition from offline simulation to energized physical hardware actuation.
