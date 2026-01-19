# Glossary

**Technical terms, acronyms, and definitions for the 8-bit discrete transistor ALU project**

---

## A

**ALU (Arithmetic Logic Unit)**
- Digital circuit that performs arithmetic and logical operations
- Core component of a CPU
- In this project: 8-bit combinational ALU with 19 operations

**ASR (Arithmetic Shift Right)**
- Shift operation that preserves the sign bit
- Used for signed division by 2
- Example: `0x85 >> 1 = 0xC2` (sign-extended)

**Asynchronous**
- Operation without a clock signal
- Outputs change immediately when inputs change
- Characteristic of this ALU design

---

## B

**BOM (Bill of Materials)**
- List of all components needed for the project
- Includes part numbers, quantities, and suppliers
- See [build-notes/bom.md](build-notes/bom.md)

**BS250 / BSS84**
- P-channel MOSFET transistor (BS250: TO-92, BSS84: SOT-23)
- Used for pull-up networks in CMOS gates
- Complement to 2N7000 / BSS138

---

## C

**Carry-Lookahead Adder**
- Fast adder architecture with O(log n) delay
- Alternative to ripple-carry adder
- Not used in this project (ripple-carry chosen for simplicity)

**CI/CD (Continuous Integration / Continuous Deployment)**
- Automated testing and deployment pipeline
- Implemented via GitHub Actions
- Runs test suite on every commit

**CLI (Command Line Interface)**
- Text-based interface for interacting with the ALU
- Implemented in `alu_cli.py`
- See [CLI_GUIDE.md](CLI_GUIDE.md)

**CMOS (Complementary Metal-Oxide-Semiconductor)**
- Technology using both NMOS and PMOS transistors
- Low static power consumption
- Used throughout this project

**Combinational Logic**
- Digital logic without memory or state
- Output depends only on current inputs
- Entire ALU is combinational (no registers)

**COUT (Carry Out)**
- Output flag indicating arithmetic overflow
- Set when addition exceeds 8 bits
- Example: `200 + 100 = 44` with `COUT=1`

---

## D

**Datapath**
- Path data flows through the ALU
- Includes arithmetic unit, logic unit, and MUX
- See [ARCHITECTURE.md](ARCHITECTURE.md)

**Decoupling Capacitor**
- Capacitor placed near ICs to filter power supply noise
- Typically 100nF ceramic
- Critical for stable operation

---

## E

**EQUAL Flag**
- Output flag indicating A == B
- Implemented with XOR gates and NOR
- Used for comparison operations

---

## F

**FA (Full Adder)**
- 1-bit adder with carry-in and carry-out
- Building block of multi-bit adders
- Equations: `Sum = A ⊕ B ⊕ Cin`, `Cout = AB + Cin(A ⊕ B)`

**Flag**
- Status output indicating result properties
- This ALU has 4 flags: LESS, EQUAL, POSITIVE, COUT
- See [FLAG_IMPLEMENTATION_GUIDE.md](FLAG_IMPLEMENTATION_GUIDE.md)

**FPGA (Field-Programmable Gate Array)**
- Reconfigurable digital logic device
- Used for prototyping and verification
- Future integration planned for this project

---

## G

**Gerber Files**
- Standard format for PCB manufacturing
- Generated from KiCad
- Sent to fabrication house (JLCPCB, PCBWay)

**Global Inverter**
- Single 8-bit inverter after the main MUX
- Enables AND, OR, XNOR from NAND, NOR, XOR
- Saves 89% transistors vs. separate gates

**Golden Model**
- Reference implementation for verification
- Written in Python
- Used to generate expected test results

---

## H

**HDL (Hardware Description Language)**
- Language for describing digital circuits
- Examples: Verilog, VHDL, SystemVerilog
- Logisim can export to HDL

---

## I

**IC (Integrated Circuit)**
- Electronic circuit on a single chip
- This project uses minimal ICs (mostly discrete transistors)
- 74HC series used for MUX and glue logic

**INV_OUT**
- Control signal for global inverter
- When high, inverts the output
- Enables derived operations (AND from NAND, etc.)

---

## J

**JLCPCB**
- PCB fabrication service
- Used for manufacturing the ALU boards
- Alternative: PCBWay

---

## K

**KiCad**
- Open-source PCB design software
- Used for all schematics and PCB layouts
- Version 7.0+ required
- See [schematics/kicad/](../schematics/kicad/)

---

## L

**LESS Flag**
- Output flag indicating A < B (unsigned)
- Implemented with cascaded comparator
- Used for comparison operations

**Logisim Evolution**
- Digital logic simulator
- Used for system-level verification
- All 19 operations verified in simulation

**LSB (Least Significant Bit)**
- Rightmost bit (bit 0)
- Lowest value bit in binary number
- Example: In `0b10110101`, LSB = 1

**LSL (Logical Shift Left)**
- Shift all bits left by one position
- Fills LSB with 0
- Example: `0x05 << 1 = 0x0A`

**LSR (Logical Shift Right)**
- Shift all bits right by one position
- Fills MSB with 0
- Example: `0x05 >> 1 = 0x02`

---

## M

**M (Mode Control)**
- Control signal for ADD/SUB selection
- M=0: Addition, M=1: Subtraction
- Controls XOR array and carry-in

**MSB (Most Significant Bit)**
- Leftmost bit (bit 7 in 8-bit system)
- Highest value bit in binary number
- Often used as sign bit in signed arithmetic

**MUX (Multiplexer)**
- Digital switch selecting one of multiple inputs
- This ALU uses 2:1 MUX (arithmetic vs. logic)
- Also 5:1 MUX for logic operation selection

---

## N

**NAND Gate**
- NOT-AND gate: output = ~(A & B)
- Universal gate (can build any logic from NAND)
- Base operation in this ALU

**NMOS (N-channel MOSFET)**
- Transistor type used for pull-down networks
- Part numbers: 2N7000 (TO-92), BSS138 (SOT-23)
- Conducts when gate is high

**NOR Gate**
- NOT-OR gate: output = ~(A | B)
- Universal gate (can build any logic from NOR)
- Base operation in this ALU

---

## O

**Opcode**
- Operation code specifying which operation to perform
- 5 bits in this ALU (32 possible, 19 implemented)
- See [OPCODE_TABLE.md](OPCODE_TABLE.md)

**Oscilloscope**
- Test equipment for viewing electrical waveforms
- Used to measure propagation delay
- Essential for hardware debugging

---

## P

**PCB (Printed Circuit Board)**
- Board with copper traces connecting components
- This project: 270×270mm, 2-layer FR-4
- See [media/pcb/](../media/pcb/)

**PMOS (P-channel MOSFET)**
- Transistor type used for pull-up networks
- Part numbers: BS250 (TO-92), BSS84 (SOT-23)
- Conducts when gate is low

**POSITIVE Flag**
- Output flag indicating result > 0
- Logic: `~OUT[7] & (OUT != 0)`
- Indicates positive, non-zero result

**Propagation Delay**
- Time for output to change after input changes
- This ALU: ~400ns for arithmetic, ~80ns for logic
- Limited by ripple-carry adder

---

## R

**REV (Reverse)**
- Operation that reverses bit order
- Example: `0xB1 (10110001) → 0x8D (10001101)`
- Useful for endianness conversion

**Ripple-Carry Adder**
- Simple adder where carry propagates through stages
- O(n) delay, but simple and compact
- Used in this ALU (8 stages, ~400ns)

---

## S

**SPICE (Simulation Program with Integrated Circuit Emphasis)**
- Analog circuit simulator
- Used for transistor-level verification
- Tool: ngspice

**Stuck-at Fault**
- Fault model where signal is stuck at 0 or 1
- Used for fault coverage analysis
- This project: ~95% stuck-at fault coverage

---

## T

**Test Vector**
- Set of inputs and expected outputs for testing
- This project: 1,247,084 test vectors
- Format: JSON files in `test/vectors/`

**Transistor Count**
- Number of discrete transistors in the design
- This ALU: 3,488 transistors
- See [POWER.md](POWER.md) for breakdown

**Truth Table**
- Table showing all input/output combinations
- Used to specify gate behavior
- Example: NAND gate has 4 rows (2² inputs)

**2's Complement**
- Method for representing signed integers
- Negative of N = ~N + 1
- Used for subtraction: A - B = A + (~B) + 1

**2N7000 / BSS138**
- N-channel MOSFET transistor (2N7000: TO-92, BSS138: SOT-23)
- Used for pull-down networks in CMOS gates
- Complement to BS250 / BSS84

---

## V

**VCC**
- Positive power supply voltage
- 5V in this project
- Also called VDD

**Verilator**
- Verilog simulator and compiler
- Can be used for HDL verification
- Alternative to Logisim

**VLSI (Very Large Scale Integration)**
- Process of creating ICs with millions of transistors
- This project uses VLSI design principles
- See [media/design/vlsi/](../media/design/vlsi/)

---

## X

**XOR (Exclusive OR)**
- Logic gate: output = A ^ B
- True when inputs differ
- Used extensively in adders and subtraction

**XOR Array**
- Array of XOR gates for conditional inversion
- Used for ADD/SUB mode switching
- Saves 40% transistors vs. MUX approach

---

## Acronyms Quick Reference

| Acronym | Full Name |
|---------|-----------|
| ALU | Arithmetic Logic Unit |
| ASR | Arithmetic Shift Right |
| BOM | Bill of Materials |
| CI/CD | Continuous Integration / Continuous Deployment |
| CLI | Command Line Interface |
| CMOS | Complementary Metal-Oxide-Semiconductor |
| CPU | Central Processing Unit |
| FA | Full Adder |
| FPGA | Field-Programmable Gate Array |
| HDL | Hardware Description Language |
| IC | Integrated Circuit |
| LSB | Least Significant Bit |
| LSL | Logical Shift Left |
| LSR | Logical Shift Right |
| MSB | Most Significant Bit |
| MUX | Multiplexer |
| NMOS | N-channel Metal-Oxide-Semiconductor |
| PCB | Printed Circuit Board |
| PMOS | P-channel Metal-Oxide-Semiconductor |
| REV | Reverse |
| SPICE | Simulation Program with Integrated Circuit Emphasis |
| VLSI | Very Large Scale Integration |
| XOR | Exclusive OR |

---

## Related Documentation

- [ARCHITECTURE.md](ARCHITECTURE.md) - Technical architecture details
- [OPCODE_TABLE.md](OPCODE_TABLE.md) - Operation specifications
- [DOCUMENTATION_MAP.md](DOCUMENTATION_MAP.md) - Complete documentation guide

---

**Last Updated**: January 2026  
**Version**: 1.0  
**Terms**: 50+ definitions
