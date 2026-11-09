# Quality Checklist — Embedded Firmware Engineer (`ROLE-ROB-004`)

Verify every item below before submitting a handoff report under [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) and [QUALITY_GATES.md](../../QUALITY_GATES.md):

## 1. Real-Time Determinism, Memory & Concurrency (`MISRA` Hygiene)
- [ ] Zero dynamic heap allocations (`malloc`/`new`), unbounded loops, recursion, or blocking `printf`/I/O occur after boot initialization.
- [ ] Every hardware register poll (`SPI`, `I2C`, `ADC`, `CAN`, `Flash`) has an explicit cycle/tick timeout and deterministic error-recovery path (e.g., `I2C` 9-clock bus clear).
- [ ] ISRs are minimal, non-blocking, and use RTOS `FromISR`-safe primitives or lock-free `SPSC` ring buffers with proper memory barriers.
- [ ] Shared multi-byte data across ISR/task boundaries is protected against torn reads/writes (`volatile` is never misused as a substitute for atomicity/critical sections).
- [ ] `DMA` buffers account for CPU D-Cache coherency (`non-cacheable MPU region` or explicit cache clean/invalidate) and alignment constraints.
- [ ] Rate-monotonic / response-time `WCET` utilization and worst-case stack budgets (with stack-overflow canary/MPU guard) leave `>= 30%` headroom.

## 2. Power-Stage, Watchdog & Protocol Fail-Safes
- [ ] MCU boots with PWM gate drivers disabled (`Hi-Z` / `STO`) and requires an explicit fault-free `CiA 402` state-machine sequence to arm.
- [ ] Complementary H-bridge/3-phase PWM configures hardware dead-time insertion and hardware `BKIN` overcurrent/overvoltage fault trip independent of CPU execution.
- [ ] Hardware Window/Independent Watchdog (`WWDG`/`IWDG`) is refreshed ONLY by a supervisor check confirming health of all critical control/comms tasks—never blindly inside a timer ISR.
- [ ] Host-to-MCU communication frames include sequence counters, explicit fixed-width endianness, `CRC-16/32` integrity checks, and heartbeat timeout (`<= 50 ms`) commanding safe torque/velocity zeroing; `NaN`/`Inf` float commands are rejected before PWM scaling.

## 3. Host Compilation, Sanitizer Verification & Safe Bench Gate
- [ ] Portable firmware logic compiled cleanly with `-Wall -Wextra -Werror -Wconversion -Wshadow` via `run_command`.
- [ ] AddressSanitizer and UndefinedBehaviorSanitizer (`-fsanitize=address,undefined`) passed across nominal, overflow, and corrupted-frame fuzz inputs.
- [ ] Fixed-point scaling, ADC saturation clamping, and integer wrap-around (`uint32_t` tick rollover) edge cases are unit-tested.
- [ ] Bootloader / OTA image validation checks cryptographic signature, monotonic anti-rollback version, and dual-bank fallback recovery.
- [ ] Linker `.map` memory assumptions (`Flash`, `SRAM`, `DTCM`, stack guard margins) and target cross-compiler notes are documented.
- [ ] Bench bring-up specifies current-limited DC power supply, unloaded/propless motor shaft check first, and live physical E-Stop readiness.
- [ ] Brownout Reset (`BOR`) voltage threshold and Supply Voltage Supervisor (`PVD`) interrupt gracefully disable gate drivers before MCU VDD collapse.
- [ ] Compiler optimization flags (`-O2` vs. `-Os`) match exact binary configuration tested under host unit/timing verification.
- [ ] Fault latch codes (`overcurrent`, `overtemp`, `encoder_loss`, `comms_timeout`, `watchdog_reset`) persist in non-volatile diagnostic registers for post-mortem triage.
- [ ] Hardware register mocks vs. verified silicon behavior are separated clearly in [HANDOFF_REPORT.md](../../../../06_TEMPLATES/HANDOFF_REPORT.md).
- [ ] **Mandatory Human Approval** gate blocks any autonomous `openocd` / `dfu-util` / `esptool` target flashing or inverter arming.
