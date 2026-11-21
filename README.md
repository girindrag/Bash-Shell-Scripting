# Bash Shell Scripting — Zero to Production SRE & DevOps

Comprehensive hands-on curriculum and code repository for mastering production Bash scripting for SRE, DevOps, Cloud infrastructure, and IoT Edge automation.

---

## 🗺️ Mastery Roadmap Overview

1. **Stage 1: Mental Models & Core Foundations** (The Unix philosophy, file descriptors, quoting, subshells)
2. **Stage 2: Syntax, Idioms & Core Tooling** (Expansions, conditionals, safe loops, arrays, functions)
3. **Stage 3: Deep Under-the-Hood Mechanics** (Process lifecycle, traps/signals, concurrency, file descriptors)
4. **Stage 4: Real-World Architecture & Production Patterns** (`set -euo pipefail`, CLI parsing, `bats` testing)
5. **Stage 5: Capstone Production Project** (`sysmesh-cli` automation suite)

---

## 📁 Repository Structure & Progress

| Module | Script | Topic & Core Concept |
| :--- | :--- | :--- |
| **Module 1** | [`server-info.sh`](./server-info.sh) | The Anatomy of a Script, Portable Shebang (`#!/usr/bin/env bash`), permissions (`chmod +x`), sequential command execution. |
| **Module 2** | [`deploy_config.sh`](./deploy_config.sh) | Variables, assignment rules (no spaces around `=`), parameter concatenation `${VAR}_suffix`, double-quoting standards. |
| **Module 3** | *(Upcoming)* | Command Substitution `$(...)` and dynamic live system telemetry extraction. |

---

## 🚀 Running the Scripts

Ensure execution permissions are set:
```bash
chmod +x *.sh
```

Execute any module:
```bash
./server-info.sh
./deploy_config.sh
```
