# Robotics & Autonomous Automation Domain Index (`ROBOTICS_AUTOMATION`)

## 1. Domain Overview & Mission Scope
The **Robotics & Autonomous Automation (`ROBOTICS_AUTOMATION`)** domain governs serial/parallel manipulators, Autonomous Mobile Robots (`AMRs` / `AGVs`), legged and aerial platforms, real-time motion control, multi-sensor state estimation (`SLAM`), deterministic embedded firmware, and functional machine safety.

Because robotic software directly commands physical kinetic energy, torques, and high-speed actuators around human operators and costly hardware, every specialist in this domain is strictly subordinated to:
- [Global System Prompt](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md)
- [Human Approval Policy](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md)
- [Independent Verification](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md)
- [Robotics Domain System Prompt](./DOMAIN_SYSTEM_PROMPT.md)

## 2. Canonical Role Inventory (`5` Roles)

| Role ID | Canonical Role Name | Primary Engineering Scope | Role Specification | Quality Checklist |
| :--- | :--- | :--- | :--- | :--- |
| `ROLE-ROB-001` | `ROBOTICS_SYSTEMS_ARCHITECT` | Sense-plan-act architecture, `ROS 2`/DDS QoS contracts, compute/power/latency budgets, `URDF`/`TF2` frame trees, hardware-software co-design | [SYSTEM_PROMPT.md](./ROLES/ROBOTICS_SYSTEMS_ARCHITECT/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/ROBOTICS_SYSTEMS_ARCHITECT/QUALITY_CHECKLIST.md) |
| `ROLE-ROB-002` | `CONTROLS_AND_KINEMATICS_ENGINEER` | `SE(3)` forward/inverse kinematics, Jacobian singularities, RNEA dynamics, impedance/MPC/PID control, phase margins, jerk-bounded trajectories | [SYSTEM_PROMPT.md](./ROLES/CONTROLS_AND_KINEMATICS_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/CONTROLS_AND_KINEMATICS_ENGINEER/QUALITY_CHECKLIST.md) |
| `ROLE-ROB-003` | `AUTONOMOUS_NAVIGATION_SLAM_ENGINEER` | LiDAR/Visual-Inertial SLAM, EKF/factor-graph sensor fusion, `NEES` consistency, occupancy/costmap planning, dynamic obstacle avoidance | [SYSTEM_PROMPT.md](./ROLES/AUTONOMOUS_NAVIGATION_SLAM_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/AUTONOMOUS_NAVIGATION_SLAM_ENGINEER/QUALITY_CHECKLIST.md) |
| `ROLE-ROB-004` | `EMBEDDED_FIRMWARE_ENGINEER` | Bare-metal/RTOS (`FreeRTOS`/`Zephyr`) firmware, ISR/WCET determinism, CAN-FD/EtherCAT/SPI drivers, hardware watchdogs, `MISRA C` safety coding | [SYSTEM_PROMPT.md](./ROLES/EMBEDDED_FIRMWARE_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/EMBEDDED_FIRMWARE_ENGINEER/QUALITY_CHECKLIST.md) |
| `ROLE-ROB-005` | `ROBOTICS_SAFETY_VALIDATION_ENGINEER` | `ISO 10218`, `ISO/TS 15066`, `ISO 3691-4`, `ISO 13849` (`PL d/e`), `IEC 61508` (`SIL`), `STO`/`SLS`/E-Stop circuits, sim-to-real & HARA sign-off | [SYSTEM_PROMPT.md](./ROLES/ROBOTICS_SAFETY_VALIDATION_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/ROBOTICS_SAFETY_VALIDATION_ENGINEER/QUALITY_CHECKLIST.md) |

## 3. Role-Selection Matrix & Multi-Domain Routing

| Engineering Problem / Deliverable | Primary Owner Role | Supporting / Review Role(s) | Cross-Domain Escalation Target |
| :--- | :--- | :--- | :--- |
| End-to-end robot architecture, `ROS 2` node/DDS topology, latency/power budget | `ROBOTICS_SYSTEMS_ARCHITECT` | `EMBEDDED_FIRMWARE_ENGINEER`, `ROBOTICS_SAFETY_VALIDATION_ENGINEER` | [IT_SOFTWARE](../IT_SOFTWARE/DOMAIN_INDEX.md) (`SOFTWARE_ARCHITECT`) |
| 6/7-DOF IK solver, singularity avoidance, torque/impedance loop, trajectory generation | `CONTROLS_AND_KINEMATICS_ENGINEER` | `ROBOTICS_SAFETY_VALIDATION_ENGINEER` | [MANUFACTURING_INDUSTRIAL](../MANUFACTURING_INDUSTRIAL/DOMAIN_INDEX.md) (`MANUFACTURING_PROCESS_ENGINEER`) |
| VIO/LiDAR SLAM, EKF/UKF fusion, `Nav2` trajectory planner, localization degeneracy | `AUTONOMOUS_NAVIGATION_SLAM_ENGINEER` | `ROBOTICS_SYSTEMS_ARCHITECT` | [AI_MACHINE_LEARNING](../AI_MACHINE_LEARNING/DOMAIN_INDEX.md) (`COMPUTER_VISION_ENGINEER`) |
| MCU motor-drive loop, DMA/SPI/CAN-FD bus timing, RTOS priority & watchdog design | `EMBEDDED_FIRMWARE_ENGINEER` | `CONTROLS_AND_KINEMATICS_ENGINEER` | [CYBERSECURITY](../CYBERSECURITY/DOMAIN_INDEX.md) (`APPLICATION_SECURITY`) |
| Collaborative force/pressure limits (`ISO/TS 15066`), E-Stop Stop Category, `PL`/`SIL` audit | `ROBOTICS_SAFETY_VALIDATION_ENGINEER` | `ROBOTICS_SYSTEMS_ARCHITECT` | [MANUFACTURING_INDUSTRIAL](../MANUFACTURING_INDUSTRIAL/DOMAIN_INDEX.md) (`OT_ICS_ENGINEER`) |

## 4. Recommended Cross-Domain & Specialized Skills
Load procedural skills progressively via [Skill Discovery and Loading](../../05_SPECIALIZED_SKILLS/SKILL_DISCOVERY_AND_LOADING/SKILL.md):
- **Core Analytical & Engineering Skills:**
  - [Cognitive Execution](../../04_CROSS_DOMAIN_SKILLS/COGNITIVE_EXECUTION/SKILL.md) — Explicit separation of URDF/datasheet parameters vs. unmeasured payload inertia and friction priors.
  - [Systems Thinking](../../04_CROSS_DOMAIN_SKILLS/SYSTEMS_THINKING/SKILL.md) — End-to-end sense-plan-act delay coupling, thermal derating, and power-rail droop modeling.
  - [Risk Management](../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md) — `ISO 12100` Hazard Analysis and Risk Assessment (`HARA`) and sensor-degeneracy fault trees.
  - [Quality Assurance](../../04_CROSS_DOMAIN_SKILLS/QUALITY_ASSURANCE/SKILL.md) — Traceable verification against [Robotics Quality Gates](./QUALITY_GATES.md).
- **Specialized Technical Skills:**
  - [Performance Benchmarking](../../05_SPECIALIZED_SKILLS/PERFORMANCE_BENCHMARKING/SKILL.md) — Control-loop WCET/jitter profiling (`P99.9` latency) and DDS message drop testing.
  - [Scientific Reproducibility](../../05_SPECIALIZED_SKILLS/SCIENTIFIC_REPRODUCIBILITY/SKILL.md) — Deterministic physics-simulation rollouts and seeded Monte Carlo sim-to-real sweeps.
  - [Model Evaluation](../../05_SPECIALIZED_SKILLS/MODEL_EVALUATION/SKILL.md) — Out-of-distribution perception testing whenever learned policies or detectors feed robot planners.

## 5. Complexity Routing & Separation-of-Duties Rules
- **Level 1–2 Kinematics / Simulation Tasks:** One subagent may combine `ROBOTICS_SYSTEMS_ARCHITECT` + `CONTROLS_AND_KINEMATICS_ENGINEER` for offline analytical or simulation tasks.
- **Level 3–4 Physical Actuation or Human-Collaborative Cells:** `ROBOTICS_SAFETY_VALIDATION_ENGINEER` MUST operate as an independent reviewer separate from the motion/navigation/firmware author before any hardware test plan is approved.

## 6. Governance & Gate Artifacts
- Domain Engineering Standards: [DOMAIN_SYSTEM_PROMPT.md](./DOMAIN_SYSTEM_PROMPT.md)
- Mandatory Sign-Off Criteria: [QUALITY_GATES.md](./QUALITY_GATES.md)
- Orchestration Review Gate: [REVIEW_AND_SIGNOFF.md](../../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md)
- Domain Lead Oversight Role: [DOMAIN_LEAD](../../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md)
