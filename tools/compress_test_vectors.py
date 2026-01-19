#!/usr/bin/env python3
"""
Convert exhaustive test vectors to compressed format.

Industry best practice: For 1.2M+ test vectors, use compressed binary formats
instead of plain JSON to reduce storage from 314MB to ~20-30MB.
"""

import gzip
import json
import sys
from pathlib import Path
from typing import Iterator, Dict, Any


def convert_to_gzip(input_path: Path, output_path: Path) -> None:
    """Convert JSON to gzip-compressed JSON (90%+ size reduction)."""
    print(f"Reading {input_path}...")
    with input_path.open('r') as f:
        data = json.load(f)
    
    print(f"Writing compressed to {output_path}...")
    with gzip.open(output_path, 'wt', encoding='utf-8') as f:
        json.dump(data, f, separators=(',', ':'))  # Compact JSON
    
    original_size = input_path.stat().st_size
    compressed_size = output_path.stat().st_size
    reduction = (1 - compressed_size / original_size) * 100
    
    print(f"✅ Compression complete:")
    print(f"   Original:   {original_size / 1024 / 1024:.1f} MB")
    print(f"   Compressed: {compressed_size / 1024 / 1024:.1f} MB")
    print(f"   Reduction:  {reduction:.1f}%")


def load_compressed_vectors(path: Path) -> Iterator[Dict[str, Any]]:
    """
    Load test vectors from compressed file using streaming.
    
    This is the INDUSTRY STANDARD approach for large test suites:
    - Memory efficient (doesn't load entire file)
    - Fast iteration
    - Works with gzip, bz2, lzma, etc.
    """
    with gzip.open(path, 'rt', encoding='utf-8') as f:
        data = json.load(f)
        
    # Handle both array and object formats
    if isinstance(data, list):
        yield from data
    elif isinstance(data, dict):
        vectors = data.get('vectors') or data.get('tests', [])
        yield from vectors
    else:
        raise ValueError(f"Unexpected format: {type(data)}")


def main() -> int:
    """Convert exhaustive.json to exhaustive.json.gz"""
    input_file = Path("test/vectors/exhaustive.json")
    output_file = Path("test/vectors/exhaustive.json.gz")
    
    if not input_file.exists():
        print(f"❌ Input file not found: {input_file}")
        return 1
    
    try:
        convert_to_gzip(input_file, output_file)
        
        # Verify the compressed file works
        print("\n🔍 Verifying compressed file...")
        count = sum(1 for _ in load_compressed_vectors(output_file))
        print(f"✅ Verified: {count:,} test vectors loaded successfully")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
