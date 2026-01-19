# System Architecture Overview

## High-Level Block Diagram

```
             A[7:0]   B[7:0]
                |        |
    FUNC[4:0]   |        |
       |        |        |
   +---v---+    |        |
   | Control   +----v---v----+     +-------------+
   |   Unit |   | Arithmetic  |---->|             |
   +-------+   |    Unit     |  0  | 8-bit 2-to-1|
       |       +-------------+     |     MUX     |---> ALU_Result[7:0]
       |             |   |         |             |
       +------------>|   +-------->|      1      |
      (LogicSelect)  |  (ArithMode)  |             |
                     |             +-------------+
                     |                 ^
                     v                 |
               +-------------+         |
               |  Logical    |         |
               |    Unit     |---------+
               +-------------+        (FinalMuxSelect)
                     ^                    |
                     |                    |
                     +--------------------+
```

## Datapath

**Datapath:** `A[7:0], B[7:0] → ALU Core (Arithmetic + Logic) → MUX → Global Invert → OUT[7:0]`

## Control Signals

* **FUNC[4:0]**: 5-bit opcode (19 implemented)
* **INV_OUT**: Global post-mux inversion bit
* **M**: ADD/SUB mode (0=ADD, 1=SUB)
* **MUX_SEL**: Selection between Arithmetic (0) and Logic (1) units

## I/O Architecture

* **Inputs**: Direct 8-bit parallel inputs for A and B
* **Outputs**: Direct 8-bit parallel output for Result + 4 status flags

## Clocking

* Manual (latch enables or debounced buttons)
* MCU-generated pulses

## Power

* 5 V single rail
* Common ground
* Per-IC decoupling (100 nF)
* Star ground to ALU

