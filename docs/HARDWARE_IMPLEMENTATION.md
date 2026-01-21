# Hardware Implementation

This document details the physical construction of the 8-Bit Discrete Transistor ALU, from PCB design to assembly and telemetry.

## Physical Implementation

### PCB Design

<div align="center">

![Main ALU PCB](../media/pcb/renders/alu_full_3d.png)
*Fabricated 270×270mm ALU board*

</div>

**Board Stack-up:**

- **Main ALU:** 270×270mm, 3,488 transistors, 2-layer FR-4
- **Flags:** Integrated or separate board for LESS/EQUAL/POSITIVE/COUT
- **Control:** Opcode decoder and control signal generation
- **Display:** LED panels for 8-bit output visualization

<div align="center">

| Flags Board                         | Control Board                                | LED Panel                               |
| ----------------------------------- | -------------------------------------------- | --------------------------------------- |
| ![Flags](../media/pcb/layouts/flags.png) | ![Control](../media/pcb/layouts/main_control.png) | ![LED](../media/pcb/layouts/led_panel_1.png) |
| *LESS, EQUAL, POSITIVE, COUT*     | *Opcode decoder*                           | *8-bit output display*                |

</div>

> **Evidence:** Modular board design for systematic assembly and testing.

### Assembly Process

<div align="center">

<img src="../media/photos/assembly/not_closeup_soldered_mosfets.jpg" alt="Assembly Close-up" width="70%">
*Hand-soldered MOSFET pairs: 2N7000 (NMOS) + BS250 (PMOS)*

</div>

**Assembly statistics:**

-  **Estimated Time:** ~60 hours hand soldering
- **Solder joints:** ~5,000 (transistor pairs, ICs, LEDs, bypass caps)
-  **Success rate:** Pending assembly


> **Evidence:** Complete fabrication process documented.

## Engineering Telemetry

**Verified Effort: ~350+ Hours**
Based on session telemetry logs, this project required sustained engineering effort averaging 8-15 hours/day over a one-month sprints.

| Session Log 01 (9.7h) | Session Log 02 (14h) | Session Log 03 (11h) |
| --------------------- | -------------------- | -------------------- |
| ![Log 1](../media/evidence/kicad_session_log_01.png) | ![Log 2](../media/evidence/kicad_session_log_02.png) | ![Log 3](../media/evidence/kicad_session_log_03.png) |
| *Late night routing session* | *Marathon design sprint* | *All night design sprint* |

> **Metric:** Unlike typical student projects which span a semester of light work, this was a compressed, high-intensity engineering sprint.

## Build Gallery

<details>
<summary><b>Click to see complete 8-phase build process</b></summary>

### Phase 1: VLSI Transistor Design from Logic Block

![VLSI Design](../media/design/vlsi/design_vlsi_inverter_mosfet.jpg)
*Transistor-level layout in Electric VLSI: NMOS + PMOS complementary pairs*

![NAND Gate](../media/design/vlsi/design_vlsi_nand_mosfet.jpg)
*NAND gate: 2 PMOS parallel (pull-up) + 2 NMOS series (pull-down)*

### Phase 2: SPICE Simulation

![SPICE Waveforms](../media/simulations/spice/or-spice.png)
*OR gate transient analysis: [![SPICE Video](../media/simulations/spice/not_spice_sim.png)](../media/videos/process/sim_ngspice_nor_kicad.mp4)
*Watch: NOR gate transient analysis (click to play)**

### Phase 3: Logisim System Simulation

![Logisim Full](../media/simulations/logisim/logism-evolution-full-circuit.png)
*Complete 8-bit ALU in Logisim Evolution: 19 operations integrated*

### Phase 4: KiCad Schematic Capture

![Main Logic Schematic](../media/schematics/boards/main_logic.svg)
*Main ALU schematic: 3,488 transistors organized into functional blocks*

![Flags Schematic](../media/schematics/boards/flags.svg)
*Flag generation: LESS, EQUAL, POSITIVE, COUT comparison logic*

### Phase 5: PCB Layout & Routing

[![Routing Demo](../media/design/kicad/design_kicad_alu_schematic.jpg)](../media/videos/process/routing-demo.mp4)
*Watch: PCB routing process (click to play)*

![PCB 3D View](../media/pcb/renders/alu-full-3d.png)
*270×270mm PCB 3D render: component placement optimized for signal flow*

### Phase 6: PCB Fabrication

![PCB Fab](../media/pcb/layouts/main_logic.png)
*Fabricated main logic board: 2-layer FR-4, ENIG finish, 1.6mm thickness*

![Control Board](../media/pcb/layouts/main_control.png)
*Control decoder board: opcode → internal control signals*

![Flags Board](../media/pcb/layouts/flags.png)
*Flags generation board: comparison logic for LESS/EQUAL/POSITIVE*

### Phase 7: Component Assembly

<img src="../media/photos/assembly/not_closeup_soldered_mosfets.jpg" alt="NOT Gate Close-up" width="70%">
*Hand-soldered MOSFET pairs: BSS138 (NMOS) + BSS84 (PMOS)*

![Assembly Progress](../media/timeline/process_timeline_02_schematic.jpg)
*Assembly in progress: systematic placement, section-by-section soldering*

### Phase 8: Testing & Verification

*Watch: Future Implementation*

### Phase 9: Final Integration

Future Implementation
*Complete 8-bit ALU: 270×270mm, 3,488 transistors, 19 operations, fully operational*

**Build Statistics:**

-  **Estimated Assembly time:** ~60 hours (hand soldering)
-  **Solder joints:** ~5,000 (transistor pairs, ICs, LEDs, bypass caps)
-  **Success rate:** Pending assembly

-  **Learning:** Priceless

</details>
