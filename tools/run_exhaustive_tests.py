#!/usr/bin/env python3
"""
Exhaustive ALU Test Runner - On-Demand Generation
Runs 1.2M+ test vectors without loading any files.
"""

import sys
from pathlib import Path

# Add test directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "test"))

from exhaustive_vectors import generate_exhaustive_vectors, count_vectors
sys.path.insert(0, str(Path(__file__).parent.parent / "tools"))
from run_tests import SimulatedALUHardware, OpcodeStats, print_header, print_table_header, print_row

def main():
    print_header()
    print("Running EXHAUSTIVE tests (1,245,184 vectors generated on-demand)")
    
    hw = SimulatedALUHardware()
    total_vectors = count_vectors()
    op_stats = {}
    
    total_passed = 0
    total_failed = 0
    update_interval = max(1, total_vectors // 1000)
    
    sys.stdout.write(f"Executing {total_vectors:,} tests...\n")
    
    for i, test in enumerate(generate_exhaustive_vectors()):
        code = str(test.get("opcode", "UNKNOWN")).strip()
        name = hw.get_op_name(code)
        
        if code not in op_stats:
            op_stats[code] = OpcodeStats(code, name)
        
        passed, _ = hw.evaluate(test)
        if passed:
            op_stats[code].passed += 1
            total_passed += 1
        else:
            op_stats[code].failed += 1
            total_failed += 1
        
        if (i + 1) % update_interval == 0 or (i + 1) == total_vectors:
            percent = ((i + 1) / total_vectors) * 100
            sys.stdout.write(f"\rProgress: {percent:5.1f}% | {i+1:,}/{total_vectors:,}")
            sys.stdout.flush()
    
    sys.stdout.write("\n\n")
    
    # Print Report Table
    print_table_header()
    sorted_codes = sorted(op_stats.keys())
    for code in sorted_codes:
        stats = op_stats[code]
        print_row(code, stats.name, stats.passed + stats.failed, stats.passed, stats.failed)
    print("\n")
    
    # Final Summary
    print(f"{'='*80}")
    print(f"{'FINAL SUMMARY':^80}")
    print(f"{'='*80}")
    print(f"Total Tests Run: {total_passed + total_failed:,}")
    print(f"Passed:          {total_passed:,} ({(total_passed/(total_passed+total_failed) if total_passed+total_failed else 0)*100:.1f}%)")
    print(f"Failed:          {total_failed:,}")
    print(f"{'='*80}\n")
    
    return 0 if total_failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
