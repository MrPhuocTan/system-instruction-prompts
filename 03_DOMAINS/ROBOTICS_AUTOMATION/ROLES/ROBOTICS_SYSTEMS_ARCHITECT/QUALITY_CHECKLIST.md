# Quality Checklist — Robotics Systems Architect (`ROLE-ROB-001`)

Verify every item below before submitting a handoff report under [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md):

## 1. Coordinate Frames (`REP-103` / `REP-105`) & `URDF` Integrity
- [ ] Every coordinate frame adheres to right-handed `REP-103` (`X-forward, Y-left, Z-up`) and SI units (`m`, `rad`, `kg`, `N·m`).
- [ ] Frame graph (`map -> odom -> base_link -> sensors/end_effector`) forms a strict single-parent tree with zero competing broadcasters or cycles.
- [ ] Every dynamic `URDF`/`SDF` link has positive mass, Symmetric Positive-Definite (`SPD`) inertia tensor, and satisfies principal-moment triangle inequalities ($I_{xx} + I_{yy} \ge I_{zz}$ cyclic permutations).
- [ ] Simplified convex collision geometries bound physical links with conservative clearance margins and are separated from high-poly visual meshes.

## 2. Real-Time Compute, Bus & Middleware (`ROS 2` / `DDS`) Architecture
- [ ] Hard real-time servo/safety loops (`>= 500 Hz`) are isolated on dedicated MCU/RTOS or real-time cores—decoupled from non-deterministic Linux/Python/GPU workloads.
- [ ] DDS QoS profiles match stream semantics (`BEST_EFFORT + KEEP_LAST(1) + DEADLINE` for high-rate commands/telemetry; `RELIABLE` for lifecycle/maps).
- [ ] Multi-sensor time synchronization specifies hardware triggers + `IEEE 1588 PTP` / `chrony` bounds (`< 1 ms` camera-IMU-LiDAR skew).
- [ ] End-to-end sense-plan-act `WCET` + `P99.9` jitter budget and bus bandwidth (`EtherCAT`, `CAN-FD`, `Ethernet <= 60%` peak load) are verified via script.

## 3. Power, Thermal & Degraded-Mode Safety Architecture
- [ ] Electrical power budget covers continuous load, peak multi-axis stall/inrush current, regenerative braking clamping, and brownout compute hold-up.
- [ ] Hardware-independent dual-channel E-Stop (`ISO 13850`) and `STO` (`IEC 61800-5-2`) cut actuator power independently of Linux/`ROS 2` software health.
- [ ] Supervisory Behavior Tree / state machine defines deterministic transitions to `SAFE_STOP` on DDS `DEADLINE` miss, localization failure, or battery critical low.

## 4. Verification, Integration & Governance Hygiene
- [ ] `URDF` inertial checks, `TF` DAG acyclicity, and power/latency budget scripts were executed deterministically via `run_command`.
- [ ] Network security enclaves (`SROS2` DDS permissions / mTLS) isolate robot command topics from untrusted enterprise/guest Wi-Fi networks.
- [ ] Diagnostic telemetry (`rosbag2` / `.mcap` black-box flight recorder) captures ring-buffered pre-fault topics without blocking real-time threads.
- [ ] Calibration storage separates factory static extrinsics from per-unit calibrated offsets with versioned checksums.
- [ ] Thermal derating bounds (`CPU`/`GPU`/motor winding `I^2t`) define graceful performance throttling prior to hard thermal shutdown.
- [ ] All launch/config artifacts default to `simulation / disarmed` mode with zero autonomous live-robot command execution.
- [ ] Datasheet specs, CAD estimates, and unmeasured payload assumptions are separated in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] **Mandatory Human Approval** gate and physical E-Stop readiness checklist are attached before any hardware bring-up.
