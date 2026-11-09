# Quality Checklist — Controls & Kinematics Engineer (`ROLE-ROB-002`)

Verify every item below before submitting a handoff report under [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md):

## 1. `SE(3)` Kinematics, Quaternions & Singularity Handling
- [ ] `DH` (Standard vs. Modified) or `PoE` screw convention, frame origins, quaternion ordering, and SI units (`m`, `rad`) are explicitly stated.
- [ ] Rotation matrices satisfy $R^T R = I, \det(R) = +1$, and orientation error enforces quaternion shortest-arc hemisphere check ($q_d \cdot q < 0$ sign flip) with zero $2\pi$ unwind bug.
- [ ] Analytical Jacobian (spatial vs. body frame declared) matches central finite-difference numerical differentiation within `< 1e-6` across random poses.
- [ ] `IK` solver handles workspace boundaries, joint limits, and low-manipulability singularities cleanly via damped least-squares (`DLS`) or constrained `QP` without `NaN`/`Inf` blow-up.

## 2. Rigid-Body Dynamics & Trajectory Feasibility
- [ ] Dynamic model includes link inertias, reflected geared rotor inertia ($N^2 I_m$), gravity vector, and Coulomb/viscous friction bounds.
- [ ] Trajectory generator enforces `C^2` continuity with explicit velocity, acceleration, and jerk (`S-curve`) bounds—zero raw step inputs fed to high-gain loops.
- [ ] Peak torque stays within motor/gearbox intermittent ratings and `back-EMF` speed ceiling; RMS torque stays `>= 20%` below continuous thermal limit.

## 3. Discrete-Time Stability, Anti-Windup & Sim-to-Real Robustness
- [ ] Closed-loop controller is analyzed in discrete time at sample period $T_s$ with `1–3` cycles of sensor/actuation delay ($z^{-d}$); all closed-loop poles satisfy $|\lambda_i| < 1$.
- [ ] Classical loops achieve `Gain Margin >= 6 dB` and `Phase Margin >= 45 deg`; impedance/force loops respect discrete passivity stiffness-damping ratios.
- [ ] Actuator saturation clamping, integral anti-windup, and derivative low-pass filtering are active and verified on large-error step/disturbance inputs.
- [ ] Perturbed Monte Carlo rollouts (`+/- 20%` payload inertia, `+/- 30%` friction, sensor noise) were executed via `run_command` with tracking RMSE and overshoot logged.

## 4. Safe Bring-Up, Telemetry & Governance Hygiene
- [ ] Controller code defaults to zero-torque / disarmed mode upon startup and faults safely on `NaN`/`Inf` encoder or command inputs.
- [ ] Heartbeat watchdog (`<= 50 ms`) ramps/zeros actuator commands immediately if upstream planner or host communication stalls.
- [ ] Software position, velocity, and torque clamps sit strictly inside physical hard-stops and gearbox peak-torque ratings.
- [ ] Notch/low-pass filters document phase-lag cost and avoid eroding discrete-time Phase Margin below `45 deg`.
- [ ] Gravity compensation is verified independently in low-gain passive/backdrivable check before enabling high-gain trajectory tracking.
- [ ] Staged commissioning protocol starts at `<= 10%` max speed (`<= 250 mm/s` `ISO 10218` reduced speed) with unloaded end-effector.
- [ ] Known CAD mass/inertia parameters are separated from unmeasured friction/payload assumptions in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] **Mandatory Human Approval** gate and live physical E-Stop verification precede any hardware gain/trajectory test.
