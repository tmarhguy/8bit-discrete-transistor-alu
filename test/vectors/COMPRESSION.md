# Test Vector Storage Optimization

## Problem
The `exhaustive.json` file containing 1,245,184 test vectors was **314MB** - far too large for efficient version control and CI/CD pipelines.

## Industry-Standard Solution: Gzip Compression

### Results
- **Original Size:** 314.4 MB (16.2M lines)
- **Compressed Size:** 7.6 MB  
- **Reduction:** 97.6%
- **Vectors:** 1,245,184 (verified)

### Implementation
1. **Compression Utility:** `tools/compress_test_vectors.py`
   - Converts `.json` → `.json.gz` using gzip
   - Verifies compressed file integrity
   - Industry best practice for large test suites

2. **Test Infrastructure Updates:**
   - `test/run_vectors.py` - Transparently loads both `.json` and `.json.gz`
   - Supports multiple formats: arrays, objects with `vectors` or `tests` keys
   - Zero code changes needed for existing tests

3. **Version Control:**
   - `.gitignore` excludes uncompressed `exhaustive.json`
   - Tracks compressed `exhaustive.json.gz` (7.6MB)
   - Reduces repository size by 306MB

### Usage
```bash
# Compress test vectors
python3 tools/compress_test_vectors.py

# Run tests (works with both formats)
python3 test/run_vectors.py test/vectors/exhaustive.json.gz
python3 test/run_vectors.py test/vectors/demo.json
```

### Alternative Formats Considered
| Format | Size Reduction | Speed | Complexity |
|--------|---------------|-------|------------|
| **gzip** (chosen) | 97.6% | Fast | Low |
| MessagePack | ~70% | 10x faster | Medium |
| Protocol Buffers | ~80% | Fast | High |
| SQLite | ~85% | Indexed queries | Medium |

**Why gzip?** 
- Best compression ratio
- Native Python support (no dependencies)
- Transparent to existing code
- Industry standard for test data

### Best Practices Applied
 Don't commit large generated files uncompressed  
 Use streaming/lazy loading for large datasets  
 Support multiple input formats for flexibility  
 Verify compressed data integrity  
 Document compression strategy in README
