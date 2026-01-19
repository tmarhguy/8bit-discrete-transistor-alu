#!/usr/bin/env python3
"""
On-demand exhaustive test vector generator for ALU.

Industry best practice: Generate test vectors programmatically instead of
storing 314MB JSON files. This approach is used by Google, Meta, Microsoft, etc.

Benefits:
- Zero storage (0 bytes vs 314MB)
- Faster than loading JSON (no I/O overhead)
- Easy to modify test parameters
- Single source of truth (golden model)
"""

from typing import Iterator, Dict, Any, Tuple


# Opcode definitions (matches hardware implementation)
OPERATIONS = [
    ("ADD", "00000"),
    ("SUB", "00001"),
    ("INC_A", "00010"),
    ("DEC_A", "00011"),
    ("LSL", "00100"),
    ("LSR", "00101"),
    ("ASR", "00110"),
    ("REV_A", "00111"),
    ("NAND", "01000"),
    ("NOR", "01001"),
    ("XOR", "01010"),
    ("PASS_A", "01011"),
    ("PASS_B", "01100"),
    ("AND", "01101"),
    ("OR", "01110"),
    ("XNOR", "01111"),
    ("CMP", "10000"),
    ("NOT_A", "10001"),
    ("NOT_B", "10010"),
]


def compute_alu_operation(opcode: str, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
    """
    Golden model: compute expected ALU output.
    
    This is the SINGLE SOURCE OF TRUTH for ALU behavior.
    All test vectors are derived from this function.
    """
    op = int(opcode, 2)
    mask = 0xFF
    
    # Arithmetic operations
    if op == 0:  # ADD
        total = a + b
        result = total & mask
        carry = total > mask
        overflow = ((a & 0x80) == (b & 0x80)) and ((a & 0x80) != (result & 0x80))
    
    elif op == 1:  # SUB
        diff = a - b
        result = diff & mask
        carry = diff >= 0
        overflow = ((a & 0x80) != (b & 0x80)) and ((a & 0x80) != (result & 0x80))
    
    elif op == 2:  # INC_A
        total = a + 1
        result = total & mask
        carry = total > mask
        overflow = (a == 0x7F)
    
    elif op == 3:  # DEC_A
        diff = a - 1
        result = diff & mask
        carry = diff >= 0
        overflow = (a == 0x80)
    
    elif op == 4:  # LSL
        carry = bool(a & 0x80)
        result = (a << 1) & mask
        overflow = False
    
    elif op == 5:  # LSR
        carry = bool(a & 0x01)
        result = (a >> 1) & mask
        overflow = False
    
    elif op == 6:  # ASR
        carry = bool(a & 0x01)
        sign_bit = a & 0x80
        result = ((a >> 1) | sign_bit) & mask
        overflow = False
    
    elif op == 7:  # REV_A
        result = 0
        for i in range(8):
            if a & (1 << i):
                result |= (1 << (7 - i))
        carry = overflow = False
    
    # Logic operations (no carry/overflow)
    elif op == 8:  # NAND
        result = (~(a & b)) & mask
        carry = overflow = False
    
    elif op == 9:  # NOR
        result = (~(a | b)) & mask
        carry = overflow = False
    
    elif op == 10:  # XOR
        result = (a ^ b) & mask
        carry = overflow = False
    
    elif op == 11:  # PASS_A
        result = a & mask
        carry = overflow = False
    
    elif op == 12:  # PASS_B
        result = b & mask
        carry = overflow = False
    
    elif op == 13:  # AND
        result = (a & b) & mask
        carry = overflow = False
    
    elif op == 14:  # OR
        result = (a | b) & mask
        carry = overflow = False
    
    elif op == 15:  # XNOR
        result = (~(a ^ b)) & mask
        carry = overflow = False
    
    elif op == 16:  # CMP
        diff = a - b
        result = 0  # CMP returns 0
        carry = diff >= 0
        overflow = ((a & 0x80) != (b & 0x80)) and ((a & 0x80) != (diff & 0x80))
        # For CMP, flags are based on the comparison (diff), not the result (0)
        diff_masked = diff & mask
        zero = (diff_masked == 0)
        negative = (diff_masked & 0x80) != 0
        return result, {
            "carry": carry,
            "overflow": overflow,
            "zero": zero,
            "negative": negative
        }
    
    elif op == 17:  # NOT_A
        result = (~a) & mask
        carry = overflow = False
    
    elif op == 18:  # NOT_B
        result = (~b) & mask
        carry = overflow = False
    
    else:
        raise ValueError(f"Unsupported opcode: {opcode}")
    
    # Common flags (not used for CMP which returns early)
    zero = (result == 0)
    negative = (result & 0x80) != 0
    
    return result, {
        "carry": carry,
        "overflow": overflow,
        "zero": zero,
        "negative": negative
    }


def generate_exhaustive_vectors() -> Iterator[Dict[str, Any]]:
    """
    Generate all exhaustive test vectors on-the-fly.
    
    Yields 19 operations × 256 A values × 256 B values = 1,245,184 vectors
    Memory efficient: yields one vector at a time (streaming).
    """
    for op_name, opcode in OPERATIONS:
        # Exhaustive: all 256×256 combinations of A and B
        for a in range(256):
            for b in range(256):
                # Compute expected result and flags using golden model
                result, flags = compute_alu_operation(opcode, a, b)
                
                yield {
                    "test_name": f"{op_name}_{a:02X}_{b:02X}",
                    "opcode": opcode,
                    "A": a,
                    "B": b,
                    "expected_result": result,
                    "expected_flags": flags
                }


def count_vectors() -> int:
    """Count total number of exhaustive vectors."""
    return len(OPERATIONS) * 256 * 256


if __name__ == "__main__":
    # Demo: show that generation is instant
    import time
    
    print("Generating exhaustive test vectors on-the-fly...")
    start = time.time()
    
    count = 0
    for vector in generate_exhaustive_vectors():
        count += 1
        if count % 100000 == 0:
            print(f"  Generated {count:,} vectors...")
    
    elapsed = time.time() - start
    
    print(f"\nTotal: {count:,} vectors generated")
    print(f"Time: {elapsed:.2f} seconds")
    print(f"Storage: 0 bytes (vs 314MB JSON)")
    print(f"Speed: {count/elapsed:,.0f} vectors/second")
