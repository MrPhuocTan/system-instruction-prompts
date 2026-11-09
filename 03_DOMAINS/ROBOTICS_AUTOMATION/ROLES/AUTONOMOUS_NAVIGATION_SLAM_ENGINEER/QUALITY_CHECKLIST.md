# Quality Checklist — Autonomous Navigation & SLAM Engineer (`ROLE-ROB-003`)

Verify every item below before submitting a handoff report under [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md):

## 1. Frame Tree (`REP-105`), Extrinsics & Time Synchronization
- [ ] `map -> odom -> base_link` adheres strictly to `REP-105`: `odom -> base_link` is continuous and jump-free; discrete SLAM/GNSS corrections apply strictly to `map -> odom`.
- [ ] Sensor `SE(3)` extrinsics, optical vs. FLU (`X-forward, Y-left, Z-up`) camera frame rotations, and timestamp offsets (`PTP` / hardware sync) are explicitly verified.
- [ ] 3D sensor FoV overlap and blind spots (overhanging loads, negative obstacles/drop-offs, ground clearance) are geometrically bounded against maximum speed.

## 2. Probabilistic State Estimation & SLAM Consistency
- [ ] Kalman / manifold updates use numerically stable `Joseph form` or square-root covariance updates preserving Symmetric Positive-Definiteness (`SPD`).
- [ ] IMU noise densities and random-walk biases are parameterized consistently in discrete time ($\sigma_d = \sigma_c / \sqrt{\Delta t}$ vs. $\sigma_{rw,d} = \sigma_{rw,c}\sqrt{\Delta t}$).
- [ ] Estimator passes `NEES` and `NIS` `95%` chi-square consistency bounds across synthetic Monte Carlo runs (`run_command`) without overconfident divergence.
- [ ] Mahalanobis `NIS` gating and robust M-estimators (`Huber`/`Cauchy`) reject wheel slip, dynamic obstacles, and perceptual-aliasing false loop closures.
- [ ] Online degeneracy monitoring ($\lambda_{\min}$ of ICP/hessian or feature count) triggers bounded velocity scaling or `SAFE_STOP` within watchdog timeout upon sensor freeze/blindness.

## 3. Costmaps, Kinodynamic Planning & Braking Horizon
- [ ] Costmap raytrace clearing distinguishes `max_range` free-space returns (`Inf`) from invalid/absorbed sensor dropouts (`NaN`) so dark/glass obstacles are never accidentally erased.
- [ ] Footprint polygon (not point-robot circle on rectangular/forked chassis!) and inflation radii account for non-holonomic turning sweep (`Ackermann` / differential / omni).
- [ ] Maximum commanded speed satisfies $v_{\max}$ lookahead braking inequality: sensor effective detection range $>$ latency travel + worst-case wet/loaded braking distance + safety margin.

## 4. Verification, Privacy & Safety Governance
- [ ] `ATE`, `RPE`, `NEES` consistency, and dynamic-obstacle / kidnapped-robot recovery tests were executed deterministically via `run_command`.
- [ ] Loop-closure backend enforces geometric consistency (`RANSAC` / `PCM`) before committing global pose-graph edges.
- [ ] Multi-floor / ramp elevation transitions (`2.5D` / `3D` terrain slope) do not trigger false ground-plane obstacle strikes on ramps.
- [ ] Dynamic pedestrian/forklift prediction margins prevent cutting immediately across the front path of moving actors.
- [ ] Camera/LiDAR recording pipelines redact human faces/badges/PII where required by site privacy policies.
- [ ] Navigation software preserves independent `ISO 3691-4` `PL d` hardware safety-scanner protective fields untouched.
- [ ] Launch configurations default to `simulation / disarmed` mode with zero autonomous physical `/cmd_vel` dispatch.
- [ ] Sim-to-real perception assumptions and a **Mandatory Human Approval** gate are documented in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
