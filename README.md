# Predictive Memory Reclamation Engine for Mobile OS

**Author:** Radha Varadendra Kulkarni  
**Register No.:** 24BKT0102  
**Institution:** Vellore Institute of Technology, Vellore  
**Course/Review:** VTOP Review 2 & 3 Submission  

---

## Overview
This repository contains a trace-driven Python simulation script modeling proactive memory reclamation in mobile operating systems. The engine shifts from traditional reactive threshold eviction (like Android LMKD) to proactive state evaluation by evaluating:
1. **Runtime Behavior Monitor ($P_{reuse,i}$):** Temporal usage patterns and access decay.
2. **Application State Analyzer ($C_{launch,i}$):** Relaunch cold-start costs, RAM footprints, and active session security flags.
3. **Multi-Factor Decision Matrix ($S_i$):** Dynamic priority scoring to prevent user state loss.

---

## Technology Stack & Prerequisites
- **Language:** Python 3.x
- **Libraries:** Standard Built-in Libraries (`time`, `random`)
- **Environment:** Any standard Python 3 interpreter (IDLE, VS Code, PyCharm, or Terminal)
