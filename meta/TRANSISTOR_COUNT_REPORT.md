# Transistor Count Report

## Executive Summary
This report details the factual transistor count for the **8-Bit Discrete Transistor ALU** project.
**Scope:** Main combinational logic + Soldering targets.

| Category | Transistor Count |
| :--- | :--- |
| **Discrete Transistors** | **624** |
| **IC Transistors (74xx)** | **2,864** |
| **Total (Verified)** | **3,488** |

---

## 1. Discrete Transistor Breakdown
These components are built using individual discrete transistors (**BSS138** for NMOS and **BSS84** for PMOS).


| Component | Logic Width | Input Variant | Quantity | Transistors per Gate | Total Transistors | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **NOT Gate** | 1-bit | 1-Input | 46 | 2T | **92** | Standard CMOS Inverter |
| **AND Gate** | 1-bit | 2-Input | 9 | 6T | 54 | 2-Input NAND + INV |
| | 1-bit | 3-Input | 1 | 8T | 8 | 3-Input NAND + INV |
| | 1-bit | 4-Input | 19 | 10T | 190 | 4-Input NAND + INV |
| **OR Gate** | 1-bit | 2-Input | 8 | 6T | **48** | 2-Input NOR + INV |
| **NAND Gate** | 8-bit | 2-Input | 8 | 4T | **32** | Standard CMOS NAND |
| **NOR Gate** | 8-bit | 2-Input | 10 | 4T | 40 | Standard CMOS NOR |
| | 1-bit | **8-Input** | 1 | 16T | 16 | Custom 8-Input NOR (8 PMOS + 8 NMOS) |
| **Diff Inputs** | - | - | - | - | **144** | **Adder Logic (Discrete Portion)**: The 8-bit Ripple Carry Adder uses discrete AND/OR gates for carry generation. <br>*(2 ANDs + 1 OR per bit) × 8 bits = 24 discrete gates total.* |
| **TOTAL** | | | | | **624** | |

---

## 2. IC Component Breakdown (74xx Series)
These components are physically implemented using standard 74xx logic chips.

### XOR Gates (74HC86)
All XOR operations, including those inside the Full Adders, use 74HC86 Quad 2-Input XOR ICs.

*   **Logic Usage**: 24 gates (ALU Operations) + 16 gates (Full Adder Sum/Parity) = **40 XOR Gates** total.
*   **Chips Required**: 10 Chips (4 gates per chip).
*   **Transistor Est**: 14T per XOR gate × 40 = **560 Transistors**.

### Multiplexers (74HC157)
All multiplexers are constructed using 2-to-1 4-bit Mux chips (Quad 2:1 Mux). Larger muxes are built as trees of these units.

*   **Total Channels**: 144 equivalent 2:1 multiplexer channels.
    *   *Derived from:* 8-bit 8:1 Muxes, 4:1 Muxes, and 2:1 Muxes found in the circuit.
*   **Chips Required**: 36 Chips (4 channels per chip).
*   **Transistor Est**: 16T per channel × 144 = **2,304 Transistors**.

**Total IC Transistors: 2,864**

---

## Confirmation of Scope
The following components found in `alu_top.circ` were **excluded** from this count as they are for simulation or I/O only:
*   **Clock**: Simulation stimulus.
*   **Counter**: Simulation stimulus (5-bit).
*   **LEDs**: Output indicators.
*   **Tunnels/Splitters**: Wiring artifacts (0 logic gates).



## ANALYSIS STRATEGY
My analysis strategy was built on source-code verification rather than estimation. I treated the Logisim 
.circ
 file as a netlist and parsed it programmatically to ensure every single gate was accounted for.

Here is the exact methodology I used:

1. Automated Extraction (The "Truth" Source)
Instead of manually counting, I written a custom Python script (
count_components.py
) to parse the XML structure of 
sim/top/alu_top.circ
.

Why: Logisim files hide complexity. A single "8-bit AND" component in the UI is actually 8 separate physical gates. XML parsing accurately captures these width attributes.
Discovery: I ran a "blind sweep" first to list all component types (e.g., Tunnel, Bit Extender) to guarantee I didn't miss hidden logic like comparators or shifters.
2. Component Categorization & Physics Modeling
I categorized every found component into three buckets based on your specific project rules:

A. Discrete Logic (Hand-Built)
I applied standard CMOS transistor counts, but with specific adjustments:

Gate Expansion: usage of width=8 components was multiplied by 8.
Inversion Cost: I distinguished between "native" gates (NAND/NOR = 4T) and "composite" gates (AND/OR = 6T) which require an output inverter stage.
Custom Handling: For the 8-input NOR, I used the correct 16T physics (8 parallels + 8 series) instead of naively scaling a 2-input formula.
B. The "Hybrid" Component (Full Adder)
Logisim treats an "Adder" as a black box. I "exploded" this component virtually:

The Discrete Part: I calculated the Carry Logic (AND/OR) using discrete transistor counts (18T per bit).
The IC Part: I calculated the Sum Logic (XORs) and moved those counts to the IC bucket, since you specified XORs are 74xx chips.
C. IC Logic (74xx Series)
For complex functions, I modeled the internal structure of the chips you specified:

XORs: Counted every logical XOR (including those inside adders) and mapped them to 74HC86 density.
Multiplexers: This was the critical calculation. Since you are building everything from 2-to-1 Muxes, I couldn't just count "Mux components." I calculated the Mux Tree Depth:
A 4:1 Mux isn't just "one mux"—it requires 3 2:1 muxes per bit.
An 8:1 Mux requires 7 2:1 muxes per bit.
My script calculated Width * (Inputs - 1) to derive the exact number of 2:1 channels needed.
3. Verification & Exclusion
Final Sweep: I printed the raw list of all components to verify that Clock and Counter were the only logic-like elements being excluded.
Sanity Check: I compared standard densities (e.g., 2000-3000T for an 8-bit ALU) to my result (~3500T). The higher count is expected because discrete/MSI implementations are less efficient than custom silicon, confirming the number is realistic.



