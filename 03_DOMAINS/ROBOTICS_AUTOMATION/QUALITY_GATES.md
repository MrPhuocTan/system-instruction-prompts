# Robotics & Autonomous Automation Quality Gates (`ROBOTICS_AUTOMATION`)

All deliverables within `03_DOMAINS/ROBOTICS_AUTOMATION/` must pass the objective engineering and safety gates below prior to `DOMAIN_LEAD`, `SA`, and `PM` sign-off under [REVIEW_AND_SIGNOFF.md](../../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md) and [INDEPENDENT_VERIFICATION.md](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md). Any physical hardware behavior not empirically tested on a target bench must be explicitly tagged `SIMULATION-VERIFIED ONLY — HARDWARE HIL/CELL SIGN-OFF REQUIRED`.

## 1. Mandatory Domain Quality Gates (`QG-ROB-01` – `QG-ROB-06`)

### `QG-ROB-01` — Kinematic, Frame & Dynamic Feasibility Gate
- **Pass Criteria:** Unambiguous `SE(3)` coordinate frame tree (`REP-103` / `URDF`), rotation/quaternion convention, and SI units; IK round-trip pose error `< 1e-4 m` / `< 1e-4 rad` within workspace; damped singularity handling where Jacobian manipulability $w(q)$ drops below threshold; planned trajectories satisfy joint position, velocity, acceleration, bounded jerk, and motor torque-speed curves with `>= 20%` continuous torque thermal margin.
- **Required Evidence:** Executed Python/C++ numerical check (`run_command`) testing FK/IK round-trip, finite-difference vs. analytical Jacobian agreement (`< 1e-6`), singularity behavior, and worst-case payload inverse-dynamics torque peaks.
- **Blocking Failure:** Frame/unit ambiguity, unguarded $J^{-1}$ division near singularities, or trajectories exceeding actuator torque/brake holding capacity.

### `QG-ROB-02` — Real-Time Control Stability & Latency Budget Gate
- **Pass Criteria:** Closed-loop discrete-time poles strictly inside the unit circle ($|\lambda_i| < 1$) across nominal and delayed plants; classical loops achieve `Gain Margin >= 6 dB` and `Phase Margin >= 45 deg` including sensor + ZOH + actuation transport delay; real-time threads/ISRs are zero-allocation, non-blocking, and bounded (`WCET + jitter <= 70%` of control period).
- **Required Evidence:** Discrete-time stability / Bode / step-response simulation log (`run_command`) testing saturation anti-windup and `1–3` cycle loop delay, plus end-to-end sense-plan-act latency budget table.
- **Blocking Failure:** Unstable oscillation under `1–2` cycle delay, integral windup on actuator saturation, or dynamic heap/blocking I/O inside real-time control loops.

### `QG-ROB-03` — Sim-to-Real & Perturbation Robustness Gate
- **Pass Criteria:** Closed-loop controller/planner succeeds across randomized physical perturbations: payload mass/inertia `+/- 20%`, joint friction/stiction `+/- 30%`, sensor noise/bias injection, and communication packet loss/jitter without violating safety envelopes.
- **Required Evidence:** Multi-seed Monte Carlo simulation rollout summary (`N >= 25` perturbed trials via `run_command` or physics engine) reporting tracking RMSE, max overshoot, and zero self/environment collisions.
- **Blocking Failure:** Tuning gains exclusively on an idealized zero-noise, zero-delay, exact-mass nominal model with no robustness sweep.

### `QG-ROB-04` — Sensor Fusion Consistency & Perceptual Degeneracy Gate
- **Pass Criteria:** State estimators (`EKF`, `UKF`, `ESKF`, factor graph) maintain positive-definite covariance, pass `NEES` / `NIS` chi-square consistency bounds (zero filter divergence/overconfidence), enforce Mahalanobis outlier gating, synchronize sensor timestamps (`PTP` / IMU pre-integration), and trigger deterministic safe-stop fallbacks on LiDAR/visual degeneracy or sensor timeout.
- **Required Evidence:** Executed synthetic trajectory + sensor dropout/outlier test verifying covariance health and bounded timeout-to-safe-stop transition (`<= watchdog limit`).
- **Blocking Failure:** Silently extrapolating dead-reckoning odometry indefinitely after localization loss or trusting single-modality 2D sensors against overhanging/negative obstacles.

### `QG-ROB-05` — Functional Safety (`ISO 10218` / `ISO/TS 15066` / `ISO 3691-4` / `IEC 61508`) Gate
- **Pass Criteria:** Documented `ISO 12100` Hazard Analysis (`HARA`); hardware-independent dual-channel E-Stop (`ISO 13850`) and `STO`/`SS1` (`IEC 60204-1` Stop Category `0` or `1` matched to inertia + gravity brake capture) meeting target `ISO 13849 PL d/e` or `IEC 61508 SIL 2/3`; collaborative motions satisfy `ISO/TS 15066` body-region quasi-static/transient force & pressure caps or `ISO 13855` protective separation distance $S_p = S_h + S_r + S_s + C + Z_d + Z_r$.
- **Required Evidence:** Safety Function Allocation Table, stopping-time/distance calculation at maximum payload and extension, and watchdog heartbeat fault-reaction matrix.
- **Blocking Failure:** Implementing E-Stop/`STO` purely in `ROS 2`/Linux software, omitting gravity-holding brake checks on power cut, or permitting head/neck collaborative impact paths.

### `QG-ROB-06` — Disarmed Default & Mandatory Human Approval Gate
- **Pass Criteria:** All generated firmware, `ROS 2` launch files, and control scripts default to `SIMULATION` / `DISARMED` state, enforce heartbeat timeouts (`<= 50–200 ms`) that command zero velocity/torque on comms loss, and carry a prominent **Mandatory Human Approval + Physical E-Stop Pre-Check** gate before hardware execution.
- **Required Evidence:** Configuration/code inspection confirming disarmed defaults, watchdog zeroing, and explicit sign-off notice in [HANDOFF_REPORT.md](../../06_TEMPLATES/HANDOFF_REPORT.md).
- **Blocking Failure:** Attempting autonomous hardware actuation/flashing from the agent runtime or leaving actuators holding last-commanded velocity upon host crash.

## 2. Independent Verification & Separation-of-Duties Protocol
1. **Analytical vs. Numerical Cross-Check:**
   - Every analytical Jacobian, Lie-algebra update, state-estimator covariance step, or stopping-distance equation must be cross-checked numerically via `run_command` (e.g., central finite-difference vs. analytical Jacobian within `< 1e-6`).
2. **Independent Safety Validation:**
   - For Level 3–4 systems involving physical hardware or human proximity, `ROBOTICS_SAFETY_VALIDATION_ENGINEER` (or [QUALITY_REVIEWER](../../02_CORE_ROLES/QUALITY_REVIEWER/SYSTEM_PROMPT.md)) must independently audit `QG-ROB-05` and `QG-ROB-06`.
   - Safety sign-off may never be self-certified by the same agent instance that authored the motion controller, navigation planner, or embedded firmware.
3. **Explicit Sim-to-Real Gap Ledger:**
   - Every handoff report must enumerate modeled vs. unmodeled physical effects (gearbox backlash, cable drag, tire slip, rolling-shutter skew, floor slope) so commissioning engineers test residual risks deliberately.
4. **Zero Autonomous Hardware Actuation Audit:**
   - Confirm in [HANDOFF_REPORT.md](../../06_TEMPLATES/HANDOFF_REPORT.md) that all code/launch files remain in `disarmed / simulation` state pending explicit human execution sign-off.
