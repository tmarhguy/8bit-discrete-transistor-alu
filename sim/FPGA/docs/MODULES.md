# Module Documentation

**Detailed Documentation of All FPGA Modules (SystemVerilog Implementation)**

---

## Table of Contents

- [Top-Level Modules](#top-level-modules)
- [ALU Core](#alu-core)
- [Support Modules](#support-modules)

---

## Top-Level Modules

### `FPGA_Top` - Hardware Wrapper

**Location**: `src/FPGA_Top.sv`

**Description**: The top-level module for physical FPGA deployment. It handles clock management, I/O mapping, and instantiates the ALU core.

**Ports**:

| Port | Width | Direction | Description |
|------|-------|-----------|-------------|
| `CLK_100MHZ` | 1 | Input | On-board master clock |
| `SW` | 16 | Input | Hardware switches (Operands A & B) |
| `BTN` | 5 | Input | Hardware buttons (Opcode select/Reset) |
| `LED` | 16 | Output | Hardware LEDs (Result & Flags) |

**Functionality**:
- Instantiates `ClockDivider` for lower-frequency operation if needed.
- Maps physical switch inputs to ALU operands.
- Instantiates `ALU.sv` core.
- Drives physical LEDs with ALU outputs and status flags.

---

## ALU Core

### `ALU` - 8-Bit Arithmetic Logic Unit

**Location**: `src/ALU.sv`

**Description**: High-performance, synthesizable SystemVerilog behavioral model of the 8-bit discrete transistor ALU.

**Parameters**:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `WIDTH` | 8 | Data bus width |

**Ports**:

| Port | Width | Direction | Description |
|------|-------|-----------|-------------|
| `A` | 8 | Input | Operand A |
| `B` | 8 | Input | Operand B |
| `Opcode` | 5 | Input | Operation selector |
| `Result` | 8 | Output | 8-bit calculation result |
| `CarryOut` | 1 | Output | Arithmetic carry/borrow |
| `Zero` | 1 | Output | True if Result == 0 |
| `Negative` | 1 | Output | True if MSB of Result is 1 |
| `Overflow` | 1 | Output | Signed overflow detection |
| `Equal` | 1 | Output | Comparison: A == B |
| `Great` | 1 | Output | Comparison: A > B |
| `Less` | 1 | Output | Comparison: A < B |

**Implementation**:
- Optimized `case` statement for all 19 operations.
- Full 2's complement arithmetic.
- Bitwise logic operations.
- Hardware-optimized shift logic.
- Dedicated unsigned magnitude comparison logic.

---

## Support Modules

### `ClockDivider` - Timining Management

**Location**: `src/ClockDivider.sv`

**Description**: Divides the high-frequency FPGA system clock down to human-observable or stable internal frequencies.

### `Counter` - Cycle Generator

**Location**: `src/Counter.sv`

**Description**: Simple parameterizable counter used to cycle through opcodes for automated demonstrations or diagnostic test patterns on hardware.

---

## Module Hierarchy

```
FPGA_Top (Hardware Wrapper)
├── ALU (Core Logic)
├── ClockDivider (Timing)
└── Counter (Demo Sequencer)
```

---

## Design Philosophy

The FPGA implementation has transitioned from an auto-generated netlist (verbose and hard to maintain) to a **Hand-Coded RTL** approach using SystemVerilog.

1. **Synthesizability**: All code uses synthesizable behavioral constructs targeting Xilinx Artix-7 fabric.
2. **Coherence**: Port names and operation indices match the discrete transistor architecture and main project specifications exactly.
3. **Efficiency**: Leverages high-level HDL features while maintaining the architectural constraints of the original 3,488-transistor design.

---

## References

- [Verilog HDL Reference Manual](https://www.xilinx.com/support/documentation/sw_manuals/xilinx14_7/ug901-vivado-synthesis.pdf)
- [FPGA Design Best Practices](https://www.xilinx.com/support/documentation/sw_manuals/xilinx2020_1/ug949-vivado-design-methodology.pdf)
