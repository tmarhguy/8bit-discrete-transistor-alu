# Testing Guide

**Comprehensive Testing Procedures for FPGA ALU Implementation (SystemVerilog)**

---

## Table of Contents

- [Overview](#overview)
- [Testbench Structure](#testbench-structure)
- [Running Tests](#running-tests)
- [Test Coverage](#test-coverage)
- [Debugging](#debugging)

---

## Overview

The FPGA ALU implementation includes a SystemVerilog testbench (`testbench/alu_tb.sv`) covering all 19 operations, edge cases, and 8-bit flag generation.

### Test Files

- `testbench/alu_tb.sv` - Main SystemVerilog testbench
- `testbench/test_vectors.sv` - Pre-defined test vectors (if applicable)

---

## Testbench Structure

The main testbench is organized into hierarchical test suites matching the main README categories:

1. **Arithmetic Operations** - ADD, SUB, INC, DEC, LSL, LSR, ASR, REV
2. **Logic Operations** - NAND, NOR, XOR, PASS A, PASS B, AND, OR, XNOR
3. **Special Operations** - CMP, NOT A, NOT B
4. **Flag Verification** - Comprehensive check for CarryOut, Zero, Negative, Overflow, Equal, Great, Less.

---

## Running Tests

### Using Vivado Simulator (Batch Mode)

1. Navigate to the testbench directory:
   ```bash
   cd sim/FPGA/testbench
   ```

2. Run the simulation script:
   ```bash
   vivado -mode batch -source run_sim.tcl
   ```

### Using Vivado GUI

1. Open Vivado and create a new project.
2. Add all `src/*.sv` files as Design Sources.
3. Add `testbench/alu_tb.sv` as a Simulation Source.
4. Run Behavioral Simulation.

---

## Test Coverage

### Operation Coverage

| Operation | Test Category | Status |
|-----------|---------------|--------|
| ADD-REV   | Arithmetic    | Complete |
| NAND-XNOR | Logic         | Complete |
| CMP-NOT B | Special       | Complete |

### Flag Coverage

The testbench verifies the full **8-bit flag vector**:
- **Arithmetic Flags**: CarryOut, Zero, Negative, Overflow.
- **Comparison Flags**: Equal, Great, Less.

---

## Debugging

### Port Mapping Reference

When debugging signals in the waveform viewer, use the following port mappings (updated from legacy names):

| Signal Name | Width | Type | Description |
|-------------|-------|------|-------------|
| `A` | 8 | Input | Operand A |
| `B` | 8 | Input | Operand B |
| `Opcode` | 5 | Input | Operation Select |
| `Result` | 8 | Output | Main output bus |
| `CarryOut` | 1 | Output | Carry/Borrow |
| `Zero` | 1 | Output | Zero result flag |

### Common Issues

1. **Opcode Mismatch**: Ensure the opcode index matches the main `README.md` (e.g., PASS_A is `11`, XNOR is `15`).
2. **Polarity**: Verify that subtraction (`SUB`) and comparison (`CMP`) handle 2's complement logic correctly.

---

## References

- [Vivado Simulation User Guide](https://www.xilinx.com/support/documentation/sw_manuals/xilinx2020_1/ug937-vivado-design-suite-simulation.pdf)
- [SystemVerilog Assertion Guide](https://www.verificationacademy.com/)
