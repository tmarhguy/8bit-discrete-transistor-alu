# Industry-Standard Test Vector Management

## The Problem
Storing 1.2M+ exhaustive test vectors as JSON creates massive files:
- **314MB** uncompressed
- **16.2M lines** of JSON
- Slow to load (seconds)
- Bloats repository
- Difficult to review/diff

## Industry Best Practice: **Don't Store Them**

### Solution: On-Demand Generation
```python
# Instead of loading 314MB of JSON...
for vector in generate_exhaustive_vectors():
    test_alu(vector)
```

### Why This is Better

| Approach | Storage | Load Time | Maintainability |
|----------|---------|-----------|-----------------|
| **JSON file** | 314MB | 5-10s | Hard to modify |
| **Gzip JSON** | 7.6MB | 3-5s + decompress | Still large |
| **On-demand**  | **0 bytes** | **Instant** | **Easy** |

### Real-World Examples

**Google Test (gtest)**
```cpp
// Generate test cases programmatically
INSTANTIATE_TEST_SUITE_P(
    ExhaustiveALU,
    ALUTest,
    testing::Combine(
        testing::Range(0, 256),  // A
        testing::Range(0, 256),  // B
        testing::Values(ADD, SUB, AND, OR...)
    )
);
```

**pytest (Python)**
```python
@pytest.mark.parametrize("a,b", 
    [(a, b) for a in range(256) for b in range(256)])
def test_alu_add(a, b):
    assert alu.add(a, b) == golden_model(a, b)
```

**Industry Standard: Property-Based Testing**
- **Hypothesis** (Python)
- **QuickCheck** (Haskell)
- **fast-check** (JavaScript)

These frameworks **generate millions of test cases** without storing any of them.

## Implementation

### 1. Generator Function (Recommended)
```python
def generate_exhaustive_vectors():
    """Yields 1.2M+ vectors on-the-fly"""
    for op in OPERATIONS:
        for a in range(256):
            for b in range(256):
                yield compute_test_vector(op, a, b)
```

**Benefits:**
- Zero storage
- Faster than JSON loading
- Memory efficient (streaming)
- Easy to modify test parameters
- Single source of truth (golden model)

### 2. Compressed Binary (If Storage Needed)
For CI caching or offline testing:

**NumPy `.npz` (Best for numerical data)**
```python
import numpy as np

# Save (one-time)
np.savez_compressed('vectors.npz',
    A=np.array([...]),
    B=np.array([...]),
    opcodes=np.array([...]),
    results=np.array([...]))

# Load (instant)
data = np.load('vectors.npz')
```

**Size:** ~5-10MB (vs 314MB JSON)  
**Load time:** <100ms (vs 5-10s JSON)

### 3. SQLite Database (For Complex Queries)
```python
import sqlite3

# One-time setup
conn = sqlite3.connect('test_vectors.db')
conn.execute('''CREATE TABLE vectors (
    id INTEGER PRIMARY KEY,
    opcode TEXT,
    a INTEGER,
    b INTEGER,
    result INTEGER,
    flags INTEGER
)''')

# Query specific tests
cursor.execute('SELECT * FROM vectors WHERE opcode = ? AND a > ?', 
               ('ADD', 128))
```

**Size:** ~20-30MB with indexes  
**Benefits:** Queryable, indexed, fast random access

## Recommendation for This Project

### For Development/CI: **On-Demand Generation**
```bash
# test/test_alu_exhaustive.py
python3 test/test_alu_exhaustive.py  # Generates all vectors on-the-fly
```

### For Archival (Optional): **NumPy .npz**
```bash
# One-time: save compressed binary
python3 tools/save_vectors_npz.py

# Fast loading when needed
python3 test/load_from_npz.py
```

## Migration Path

1.  **Keep `demo.json`** (500KB, good for quick tests)
2.  **Delete `exhaustive.json`** (314MB, regenerate on-demand)
3.  **Use generator** in test suite
4. ️ **Optional:** Create `.npz` for CI caching

## Files to Update

- `test/test_alu.py` - Use generator instead of loading JSON
- `run_tests.sh` - Remove exhaustive.json dependency
- `.gitignore` - Remove exhaustive.json entry (not needed)
- `README.md` - Document on-demand generation approach

## Summary

**Industry Standard:** Generate test vectors programmatically, don't store them.

**Your Project:**
- 1.2M vectors × 0 bytes = **0MB storage**
- Faster execution (no I/O overhead)
- Easier maintenance (modify generator, not 16M lines of JSON)
- Professional approach used by Google, Meta, Microsoft, etc.
