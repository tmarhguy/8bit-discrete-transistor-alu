# Design Decisions

This document tracks key design decisions made during the ALU development.

## Architecture Decisions

### 2's Complement Subtraction

Chose XOR-based design for subtraction over MUX array, resulting in 30% reduction in transistor count.

### Control Signal Encoding

Implemented 5-bit FUNC[4:0] opcode with global inversion bit, enabling 19 implemented operations efficiently.

