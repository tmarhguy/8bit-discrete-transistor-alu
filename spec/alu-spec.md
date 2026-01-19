# ALU Specification

This document defines the complete specification for the 8-bit discrete transistor ALU.

## Overview

The ALU implements 19 operations on 8-bit operands, supporting arithmetic, logic, shift, and comparison operations.

## Inputs

- `A[7:0]` - 8-bit operand A
- `B[7:0]` - 8-bit operand B
- `FUNC[4:0]` - 5-bit operation selector (Opcode)
- `M` - ADD/SUB mode (0=ADD, 1=SUB)
- `INV_OUT` - Global post-mux inversion bit

## Outputs

- `OUT[7:0]` - 8-bit result
- `C_OUT` - Carry/Borrow output
- `Z_FLAG` - Zero flag
- `N_FLAG` - Negative flag

## Operations

See [opcode_table.md](opcode/opcode_table.md) for complete operation list.
