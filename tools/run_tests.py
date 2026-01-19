#!/usr/bin/env python3
"""
ALU Test Runner
Executes JSON test vectors against the software Golden Model.
Features:
- Live progress updates
- Opcode-level statistics
- Hardware emulation using ALU8Bit model
"""

import argparse
import json
import sys
import time
import threading
import itertools
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Tuple, Any

# --- UI Utilities ---

class Spinner:
    """Animated loading spinner for endless tasks."""
    def __init__(self, message: str = "Processing"):
        self.message = message
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self._spin)

    def start(self):
        self.stop_event.clear()
        self.thread.start()

    def stop(self):
        self.stop_event.set()
        self.thread.join()
        sys.stdout.write(f"\r{self.message}... Done!   \n")
        sys.stdout.flush()

    def _spin(self):
        spinner_chars = itertools.cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
        while not self.stop_event.is_set():
            sys.stdout.write(f"\r{next(spinner_chars)} {self.message}...")
            sys.stdout.flush()
            time.sleep(0.1)

def print_header():
    print(f"\n{'='*80}")
    print(f"{'ALU TEST EXECUTION (Golden Model)':^80}")
    print(f"{'='*80}\n")

def print_table_header():
    print(f"{'Opcode':<10} | {'Operation':<10} | {'Tests':<10} | {'Passed':<10} | {'Failed':<10} | {'Status'}")
    print(f"{'-'*11}+{'-'*12}+{'-'*12}+{'-'*12}+{'-'*12}+{'-'*10}")

def print_row(opcode, operation, total, passed, failed):
    status = "PASS" if failed == 0 else "FAIL"
    print(f"{opcode:<10} | {operation:<10} | {total:<10,} | {passed:<10,} | {failed:<10,} | {status}")

# --- Hardware Model ---

class ALU8Bit:
    """Software simulation of 8-bit ALU (Golden Model)"""
    
    def __init__(self):
        self.width = 8
        self.mask = (1 << self.width) - 1
        
    def _flags(self, result: int, carry: bool = False, overflow: bool = False) -> Dict[str, bool]:
        result_8bit = result & self.mask
        return {
            'carry': carry,
            'zero': result_8bit == 0,
            'overflow': overflow,
            'negative': bool(result_8bit & 0x80)
        }
    
    def add(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        result = a + b
        carry = result > self.mask
        overflow = ((a & 0x80) == (b & 0x80)) and ((a & 0x80) != (result & 0x80))
        return result & self.mask, self._flags(result, carry, overflow)
    
    def sub(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        result = a - b
        carry = result >= 0
        overflow = ((a & 0x80) != (b & 0x80)) and ((a & 0x80) != (result & 0x80))
        return result & self.mask, self._flags(result, carry, overflow)
    
    def inc_a(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        result = a + 1
        carry = result > self.mask
        overflow = (a == 0x7F)
        return result & self.mask, self._flags(result, carry, overflow)
    
    def dec_a(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        result = a - 1
        carry = result >= 0
        overflow = (a == 0x80)
        return result & self.mask, self._flags(result, carry, overflow)
    
    def lsl(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        carry = bool(a & 0x80)
        result = (a << 1) & self.mask
        return result, self._flags(result, carry, False)
    
    def lsr(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        carry = bool(a & 0x01)
        result = (a >> 1) & self.mask
        return result, self._flags(result, carry, False)
    
    def asr(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        carry = bool(a & 0x01)
        sign_bit = a & 0x80
        result = ((a >> 1) | sign_bit) & self.mask
        return result, self._flags(result, carry, False)
    
    def rev_a(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        result = 0
        for i in range(8):
            if a & (1 << i):
                result |= (1 << (7 - i))
        return result, self._flags(result, False, False)
    
    def nand(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        result = (~(a & b)) & self.mask
        return result, self._flags(result, False, False)
    
    def nor(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        result = (~(a | b)) & self.mask
        return result, self._flags(result, False, False)
    
    def xor(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        result = (a ^ b) & self.mask
        return result, self._flags(result, False, False)
    
    def pass_a(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        return a, self._flags(a, False, False)
    
    def pass_b(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        return b, self._flags(b, False, False)
    
    def and_op(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        result = (a & b) & self.mask
        return result, self._flags(result, False, False)
    
    def or_op(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        result = (a | b) & self.mask
        return result, self._flags(result, False, False)
    
    def xnor(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        result = (~(a ^ b)) & self.mask
        return result, self._flags(result, False, False)
    
    def cmp(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        result = a - b
        carry = result >= 0
        overflow = ((a & 0x80) != (b & 0x80)) and ((a & 0x80) != (result & 0x80))
        return 0, self._flags(result, carry, overflow)
    
    def not_a(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        result = (~a) & self.mask
        return result, self._flags(result, False, False)
    
    def not_b(self, a: int, b: int) -> Tuple[int, Dict[str, bool]]:
        result = (~b) & self.mask
        return result, self._flags(result, False, False)

class SimulatedALUHardware:
    def __init__(self):
        self.alu = ALU8Bit()
        self.ops = {
            "00000": ("ADD", self.alu.add),
            "00001": ("SUB", self.alu.sub),
            "00010": ("INC_A", self.alu.inc_a),
            "00011": ("DEC_A", self.alu.dec_a),
            "00100": ("LSL", self.alu.lsl),
            "00101": ("LSR", self.alu.lsr),
            "00110": ("ASR", self.alu.asr),
            "00111": ("REV_A", self.alu.rev_a),
            "01000": ("NAND", self.alu.nand),
            "01001": ("NOR", self.alu.nor),
            "01010": ("XOR", self.alu.xor),
            "01011": ("PASS_A", self.alu.pass_a),
            "01100": ("PASS_B", self.alu.pass_b),
            "01101": ("AND", self.alu.and_op),
            "01110": ("OR", self.alu.or_op),
            "01111": ("XNOR", self.alu.xnor),
            "10000": ("CMP", self.alu.cmp),
            "10001": ("NOT_A", self.alu.not_a),
            "10010": ("NOT_B", self.alu.not_b),
        }

    def evaluate(self, test: Dict[str, Any]) -> Tuple[bool, str]:
        opcode = str(test.get("opcode", "")).strip()
        
        # Fallback for old vectors without opcode
        if opcode not in self.ops:
            op_name = test.get("operation", "").upper()
            for k, (name, _) in self.ops.items():
                if name == op_name:
                    opcode = k
                    break
        
        if opcode not in self.ops:
            return False, f"Unknown Opcode: {opcode}"

        _, func = self.ops[opcode]
        
        try:
            actual_result, actual_flags = func(int(test["A"]), int(test["B"]))
        except Exception as e:
            return False, str(e)

        # Verify Result
        if actual_result != int(test.get("expected_result", 0)):
            return False, f"Result Mismatch: Exp {test['expected_result']} vs Act {actual_result}"

        # Verify Flags
        exp_flags = test.get("expected_flags", {})
        for flag, exp_val in exp_flags.items():
            if bool(exp_val) != actual_flags.get(flag, False):
                return False, f"Flag '{flag}' Mismatch"
        
        return True, "Pass"

    def get_op_name(self, opcode):
        if opcode in self.ops:
            return self.ops[opcode][0]
        return "UNKNOWN"

# --- Main Logic ---

@dataclass
class OpcodeStats:
    opcode: str
    name: str
    passed: int = 0
    failed: int = 0

def load_vectors(path: Path) -> List[Dict[str, Any]]:
    # Spinner handles the delay visualization
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
        if isinstance(data, dict) and "tests" in data:
            return data["tests"]
        if isinstance(data, list):
            return data
        raise ValueError("Invalid JSON format")

def main():
    parser = argparse.ArgumentParser(description="Run ALU test vectors.")
    parser.add_argument("--vectors-dir", default="test", help="Directory containing JSON vectors.")
    # output-dir argument removed intentionally
    args = parser.parse_args()

    vectors_dir = Path(args.vectors_dir)
    vector_files = sorted(vectors_dir.glob("*.json"))
    
    if not vector_files:
        print("No test vectors found!")
        return 1

    print_header()
    hw = SimulatedALUHardware()
    
    total_passed = 0
    total_failed = 0
    
    for vector_file in vector_files:
        print(f"Testing File: {vector_file.name}")
        
        # 1. Load Data
        spinner = Spinner(f"Loading {vector_file.name}")
        spinner.start()
        try:
            vectors = load_vectors(vector_file)
        except Exception as e:
            spinner.stop()
            print(f"❌ Failed to load {vector_file.name}: {e}")
            continue
        spinner.stop()
        
        # 2. Run Tests
        # We process all tests, grouping results by opcode for reporting
        op_stats: Dict[str, OpcodeStats] = {}
        
        total_vectors = len(vectors)
        update_interval = max(1, total_vectors // 1000)
        sys.stdout.write(f"Executing {total_vectors:,} tests...\n")
        
        for i, test in enumerate(vectors):
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
        
        sys.stdout.write("\n")

        # 3. Print Report Table
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
