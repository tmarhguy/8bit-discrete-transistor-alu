# Test Vector Management

## Overview

This directory contains test vectors for the 8-bit ALU. We use industry-standard on-demand generation for exhaustive testing instead of storing large JSON files.

## Files

- `demo.json` - Sample test vectors (1,900 tests, 500KB)
- `BEST_PRACTICES.md` - Industry best practices for test vector management
- `COMPRESSION.md` - Historical notes on compression approaches

## On-Demand Generation (Recommended)

For exhaustive testing (1.2M+ vectors), we generate test vectors programmatically instead of storing them:

```bash
# Run exhaustive tests (generates 1,245,184 vectors on-the-fly)
./run_tests.sh exhaustive
```

**Benefits:**
- Zero storage (0 bytes vs 314MB JSON)
- Faster than loading files (no I/O overhead)
- Easy to modify test parameters
- Single source of truth (golden model in `test/exhaustive_vectors.py`)

## Implementation

The exhaustive test generator is located at:
- `test/exhaustive_vectors.py` - On-demand vector generator
- `tools/run_exhaustive_tests.py` - Test runner

**How it works:**
1. Generator yields 256×256 combinations for each of 19 operations
2. Each vector is computed using the golden model
3. Vectors are never stored - generated during test execution
4. Memory efficient: streaming/iterator pattern

## Quick Tests

For quick validation, use the demo vectors:

```bash
# Run demo tests (1,900 vectors from file)
./run_tests.sh quick
```

## Industry Standard

This approach is used by:
- Google Test (gtest) - Parametrized tests
- pytest - @pytest.mark.parametrize
- QuickCheck/Hypothesis - Property-based testing

All generate test cases programmatically rather than storing them.

## Migration from JSON

Previously, we stored exhaustive.json (314MB, 16M lines). This has been replaced with on-demand generation:

- Old: Load 314MB JSON file (5-10 seconds)
- New: Generate 1.2M vectors (1.3 seconds, 0 bytes storage)

See `BEST_PRACTICES.md` for detailed rationale.
