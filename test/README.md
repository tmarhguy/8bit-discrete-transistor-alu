# ALU Test Suite

> Industry-Standard Testing Framework for 8-bit ALU

---

## Quick Start

### Fastest Way (No Dependencies Required)

**Quick Test (1,900 tests):**
```bash
# From project root
./run_tests.sh

# Or
python3 test/test_alu.py

# Or
make test-quick
```

**Exhaustive Test (1,247,084 tests):**
```bash
# From project root
./run_tests.sh exhaustive
```

**Output (Exhaustive):**

```
Summary: 1247084 passed, 0 failed
Success Rate: 100.0%
Duration: 9.3 seconds

Per-operation: 65,636 tests × 19 operations = 1,247,084 total
```

**Output (Quick):**

```
Summary: 1900 passed, 0 failed
Success Rate: 100.0%
Duration: < 1 second
```

---

## Test Suite Overview

This directory contains the complete verification framework for the 8-bit discrete transistor ALU.

### Test Coverage

| Category | Tests | Coverage | Status |
|----------|-------|----------|--------|
| Arithmetic | 8 operations | 100% |  |
| Logic | 8 operations | 100% |  |
| Special | 3 operations | 100% |  |
| **Total** | **19 operations** | **100%** | **** |

---

## Test Methods

### Method 1: Shell Script (Recommended)

```bash
./run_tests.sh              # Quick mode: 1,900 tests
./run_tests.sh exhaustive   # Exhaustive mode: 1,247,084 tests
./run_tests.sh pytest       # With pytest (requires install)
./run_tests.sh verbose      # Verbose output
./run_tests.sh coverage     # With coverage report
./run_tests.sh install      # Install dependencies
./run_tests.sh help         # Show help
```

### Method 2: Direct Python Execution

```bash
# Quick test (no dependencies)
python3 test/test_alu.py

# With pytest (requires pytest)
cd test && pytest test_alu.py -v

# Specific operation
pytest test_alu.py -k "ADD" -v

# With coverage
pytest test_alu.py --cov --cov-report=html
```

---

## Test Vector Format

Test vectors are stored in **JSON format** for easy parsing and automation.

### Example Test Vector

```json
{
  "test_name": "ADD_01",
  "A": 42,
  "B": 23,
  "opcode": "00000",
  "expected_result": 65,
  "expected_flags": {
    "carry": false,
    "overflow": false,
    "zero": false,
    "negative": false
  }
}
```

### Fields

- **test_name**: Unique identifier for the test
- **A**: First operand (0-255)
- **B**: Second operand (0-255)
- **opcode**: 5-bit operation code (matches `spec/opcode/opcode_table.md`)
- **expected_result**: Expected 8-bit output
- **expected_flags**: Expected flag states

---

## Test Categories

### Arithmetic Operations

**File**: `vectors/arithmetic.json`

**Coverage**:
- ADD, SUB operations
- INC, DEC operations
- Shift operations (LSL, LSR, ASR)
- Bit reversal (REV)

**Edge cases**:
- Overflow conditions
- Underflow conditions
- Zero results
- Maximum values

### Logic Operations

**File**: `vectors/logic.json`

**Operations**:
- Base gates: NAND, NOR, XOR
- Derived gates: AND, OR, XNOR
- Pass-through: PASS A, PASS B
- Inversion: NOT A, NOT B

### Special Operations

**File**: `vectors/special.json`

**Operations**:
- CMP (comparison with flags)
- Control operations

---

## Test Execution

### Quick Test (1,900 tests)

**Purpose**: Fast validation during development

**Coverage**: 100 tests per operation × 19 operations = 1,900 tests

**Execution time**: < 1 second

**Use cases**:
- Pre-commit validation
- Quick sanity checks
- CI/CD fast path

### Exhaustive Test (1,247,084 tests)

**Purpose**: Comprehensive validation

**Coverage**: 65,636 tests per operation × 19 operations = 1,247,084 tests

**Execution time**: ~9.3 seconds

**Use cases**:
- Pre-release validation
- Regression testing
- Hardware validation

---

## Test Results

### Expected Output Format

```
╔════════════════════════════════════════════════════════════════════════════╗
║                          ALU TEST RUNNER                                   ║
╚════════════════════════════════════════════════════════════════════════════╝

=== Running Quick Tests (No Dependencies) ===

================================================================================
Running ALU Tests (unittest mode)
================================================================================

================================================================================
Results: 1900 passed, 0 failed out of 1900 total
Success Rate: 100.0%
================================================================================
```

### Interpreting Results

- **All tests passing**: ALU implementation is correct
- **Some tests failing**: Check specific operation implementation
- **All tests failing**: Check test framework setup

---

## Continuous Integration

### GitHub Actions

The test suite is integrated with GitHub Actions for automated testing on every commit.

**Workflow**: `.github/workflows/ci.yml`

```yaml
name: ALU Verification
on: [push, pull_request]
jobs:
  verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run quick tests
        run: ./run_tests.sh
      - name: Run exhaustive tests
        run: ./run_tests.sh exhaustive
```

---

## Troubleshooting

### Tests Not Running

**Issue**: `./run_tests.sh: Permission denied`

**Solution**:
```bash
chmod +x run_tests.sh
```

### Import Errors

**Issue**: `ModuleNotFoundError: No module named 'test_alu'`

**Solution**:
```bash
# Ensure you're in project root
cd /path/to/cpu

# Run from root
./run_tests.sh
```

### Test Failures

**Issue**: Specific tests failing

**Debug steps**:
1. Run single operation: `pytest test_alu.py -k "ADD" -v`
2. Check implementation in `test_alu.py`
3. Compare with Logisim simulation
4. Verify opcode mapping

---

## Related Documentation

- [VERIFICATION.md](../docs/VERIFICATION.md) - Complete verification strategy
- [OPCODE_TABLE.md](../docs/OPCODE_TABLE.md) - Operation specifications
- [ARCHITECTURE.md](../docs/ARCHITECTURE.md) - System architecture

---

**Last Updated**: January 2026  
**Version**: 1.0  
**Test Status**: 1,247,084/1,247,084 passing (100%)
