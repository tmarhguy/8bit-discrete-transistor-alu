import machine
import time

# ==========================================
# 8-Bit Discrete ALU Hardware Test Script
# For Raspberry Pi Pico / RP2040
# ==========================================

# ------------------------------------------
# Pin Configuration (Adjust as needed)
# ------------------------------------------

# Output Pins (Pico -> ALU Inputs)
A_PINS = [0, 1, 2, 3, 4, 5, 6, 7]         # A[0]..A[7]
B_PINS = [8, 9, 10, 11, 12, 13, 14, 15]   # B[0]..B[7]
FUNC_PINS = [16, 17, 18, 19, 20]          # FUNC[0]..FUNC[4]

# Input Pins (ALU Outputs -> Pico)
OUT_PINS = [21, 22, 23, 24, 25, 26, 27, 28] # OUT[0]..OUT[7]

# Control
DELAY_US = 500  # Propagation delay wait time (should be > 400ns)

# ------------------------------------------
# Initialization
# ------------------------------------------

a_gpio = [machine.Pin(p, machine.Pin.OUT) for p in A_PINS]
b_gpio = [machine.Pin(p, machine.Pin.OUT) for p in B_PINS]
func_gpio = [machine.Pin(p, machine.Pin.OUT) for p in FUNC_PINS]

out_gpio = [machine.Pin(p, machine.Pin.IN) for p in OUT_PINS]

# ------------------------------------------
# Helper Functions
# ------------------------------------------

def set_inputs(a, b, func):
    """Set ALU inputs via GPIO"""
    # Set A bus
    for i in range(8):
        val = (a >> i) & 1
        a_gpio[i].value(val)
        
    # Set B bus
    for i in range(8):
        val = (b >> i) & 1
        b_gpio[i].value(val)
        
    # Set Function bus
    for i in range(5):
        val = (func >> i) & 1
        func_gpio[i].value(val)

def read_output():
    """Read ALU output via GPIO"""
    result = 0
    for i in range(8):
        result |= (out_gpio[i].value() << i)
    return result

def run_test(name, opcode, a, b, expected):
    """Run a single test case"""
    set_inputs(a, b, opcode)
    time.sleep_us(DELAY_US) # Wait for signals to propagate
    actual = read_output()
    
    if actual == expected:
        return True, actual
    else:
        return False, actual

# ------------------------------------------
# Test Sequences
# ------------------------------------------

def run_smoke_test():
    """Run basic sanity checks"""
    print("=== Running Smoke Test ===")
    
    tests = [
        # Name, Opcode, A, B, Expected
        ("ADD_ZERO", 0b00000, 0, 0, 0),
        ("ADD_ONE",  0b00000, 1, 1, 2),
        ("ADD_MAX",  0b00000, 255, 0, 255),
        ("AND_MASK", 0b01101, 0xFF, 0x0F, 0x0F),
        ("XOR_INV",  0b01010, 0xAA, 0x55, 0xFF),
    ]
    
    passed = 0
    for t in tests:
        name, op, a, b, exp = t
        success, act = run_test(name, op, a, b, exp)
        
        status = "PASS" if success else f"FAIL (Got {act}, Exp {exp})"
        print(f"Test {name}: {status}")
        if success: passed += 1
            
    print(f"Smoke Test: {passed}/{len(tests)} Passed\n")

# ------------------------------------------
# Main Loop
# ------------------------------------------

if __name__ == "__main__":
    print("Initializing ALU Hardware Test Interface...")
    time.sleep(1)
    
    while True:
        print("\nOptions:")
        print("1. Run Smoke Test")
        print("2. Manual Input")
        print("3. Loop Random Inputs (Stress Test)")
        
        choice = input("Select option: ")
        
        if choice == "1":
            run_smoke_test()
            
        elif choice == "2":
            try:
                op = int(input("Opcode (0-31): "))
                a = int(input("A (0-255): "))
                b = int(input("B (0-255): "))
                set_inputs(a, b, op)
                time.sleep_us(DELAY_US)
                res = read_output()
                print(f"Output: {res} (0x{res:02X})")
            except ValueError:
                print("Invalid input")

        elif choice == "3":
            print("Running random stress test... Ctrl+C to stop")
            import random
            count = 0
            errors = 0
            try:
                while True:
                    a = random.getrandbits(8)
                    b = random.getrandbits(8)
                    # Test ADD (Opcode 0)
                    success, act = run_test("RND", 0, a, b, (a+b)&0xFF)
                    if not success:
                        print(f"FAIL: {a} + {b} = {act} (Exp {(a+b)&0xFF})")
                        errors += 1
                    count += 1
                    if count % 1000 == 0:
                        print(f"{count} tests, {errors} errors")
            except KeyboardInterrupt:
                print("Stopped.")
