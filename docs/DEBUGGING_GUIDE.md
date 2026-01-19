# Hardware Debugging Guide

**Systematic debugging procedures for the 8-bit discrete transistor ALU**

This guide provides step-by-step debugging workflows for hardware issues, from power-on problems to complex signal integrity issues.

---

## Table of Contents

- [Debugging Philosophy](#debugging-philosophy)
- [Essential Tools](#essential-tools)
- [Systematic Debugging Workflow](#systematic-debugging-workflow)
- [Power System Debugging](#power-system-debugging)
- [Gate-Level Debugging](#gate-level-debugging)
- [Subsystem Debugging](#subsystem-debugging)
- [Signal Integrity Issues](#signal-integrity-issues)
- [Common Failure Modes](#common-failure-modes)
- [Case Studies](#case-studies)

---

## Debugging Philosophy

### Divide and Conquer

1. **Isolate the problem** - Narrow down to specific subsystem
2. **Test known-good inputs** - Start with simple, predictable cases
3. **Work bottom-up** - Verify gates before testing complete operations
4. **Document findings** - Record measurements and observations

### Scientific Method

1. **Observe** - What is the actual behavior?
2. **Hypothesize** - What could cause this?
3. **Test** - Design experiment to confirm/reject hypothesis
4. **Iterate** - Repeat until root cause found

---

## Essential Tools

### Required Equipment

| Tool | Purpose | Typical Use |
|------|---------|-------------|
| **Multimeter** | DC voltage, continuity | Power rails, solder joints |
| **Oscilloscope** | Waveforms, timing | Propagation delay, signal integrity |
| **Logic Analyzer** | Multi-channel digital | Bus activity, timing relationships |
| **Power Supply** | Regulated 5V | System power with current limiting |

### Optional but Helpful

- **Thermal Camera** - Locate hot spots (shorts, incorrect components)
- **Function Generator** - Generate test patterns
- **Logic Probe** - Quick logic level checks
- **Magnifying Glass** - Inspect solder joints

---

## Systematic Debugging Workflow

### Step 1: Visual Inspection

**Before applying power:**

```
 Check all solder joints (shiny, smooth)
 Look for bridges between pins
 Verify component orientation (ICs, transistors, capacitors)
 Check for missing components
 Inspect for physical damage
```

**Common issues found**:
- Cold solder joints (dull, grainy)
- Solder bridges (especially on fine-pitch ICs)
- Reversed polarized components
- Wrong component values

### Step 2: Continuity Testing

**Power off, measure resistance:**

```bash
# VCC to GND should be > 1kΩ (no shorts)
Multimeter: Resistance mode
Red probe: VCC
Black probe: GND
Expected: > 1kΩ

# Critical signal paths
Test: Input pins to IC pins
Expected: < 1Ω (good connection)
```

**Red flags**:
- VCC to GND < 100Ω → Short circuit
- Signal path > 10Ω → Poor connection

### Step 3: Power-On Test

**Apply power with current limiting:**

```bash
# Initial power-on
1. Set power supply to 5.0V, 100mA current limit
2. Connect power
3. Observe current draw
4. Measure voltages at test points
```

**Expected behavior**:
- Current draw: 50-150mA (idle)
- VCC at ICs: 4.75-5.25V
- No hot components
- No smoke or burning smell

**If excessive current**:
- Power off immediately
- Check for shorts with thermal camera
- Inspect recent solder work

### Step 4: Functional Testing

**Test subsystems independently:**

```
1. Test individual gates (NOT, NAND, NOR)
2. Test full adder (8 input combinations)
3. Test arithmetic unit (simple ADD)
4. Test logic unit (simple AND)
5. Test complete operations
```

---

## Power System Debugging

### Problem: No Power

**Symptoms**:
- No LEDs light up
- Multimeter reads 0V at VCC

**Debug procedure**:

```bash
# 1. Check power supply
Measure at supply output: Should be 5.0V
If not: Check supply settings, fuse, connections

# 2. Check power connector
Measure at board power input: Should be 5.0V
If not: Check connector, wiring, polarity

# 3. Check power distribution
Measure at various VCC points: Should be 4.75-5.25V
If not: Check for broken traces, poor solder joints
```

### Problem: Voltage Drop

**Symptoms**:
- VCC at far end of board < 4.75V
- Erratic behavior under load

**Debug procedure**:

```bash
# Measure IR drop
1. Measure VCC at power input: Record value
2. Measure VCC at far end: Record value
3. Calculate drop: Input - Far end

Acceptable: < 0.25V drop
If > 0.25V:
  - Check trace width (should be ≥ 1mm for power)
  - Add bulk capacitors
  - Improve ground plane
```

### Problem: Excessive Current Draw

**Symptoms**:
- Current > 500mA (expected: 50-150mA)
- Components get hot

**Debug procedure**:

```bash
# Locate short circuit
1. Power off
2. Use thermal camera or finger to find hot spot
3. Inspect area around hot component
4. Check for:
   - Solder bridges
   - Reversed transistors
   - Shorted traces
   - Wrong component values
```

---

## Gate-Level Debugging

### Testing Individual Gates

**NOT Gate Test**:

```bash
# Setup
Input: Connect to 0V (GND) or 5V (VCC)
Output: Measure with multimeter

# Test cases
Input = 0V → Output should be ~5V
Input = 5V → Output should be ~0V

# Acceptable ranges
Logic 0: < 0.5V
Logic 1: > 4.5V
```

**NAND Gate Test**:

```bash
# Truth table verification
A=0, B=0 → OUT=1 (5V)
A=0, B=1 → OUT=1 (5V)
A=1, B=0 → OUT=1 (5V)
A=1, B=1 → OUT=0 (0V)

# If all outputs are same:
- Check input connections
- Verify transistor orientation
- Test transistors individually
```

### Oscilloscope Measurements

**Propagation Delay**:

```bash
# Setup
Ch1: Input signal (trigger)
Ch2: Output signal
Timebase: 50ns/div

# Measure
1. Apply step input (0V → 5V)
2. Trigger on rising edge of input
3. Measure time to output change
4. Compare with expected delay

Expected for single gate: 5-20ns
If > 50ns: Check for excessive capacitance
```

**Signal Integrity**:

```bash
# Check for ringing, overshoot
1. Zoom in on transitions
2. Look for oscillations
3. Measure overshoot amplitude

Acceptable overshoot: < 10% of VCC
If excessive:
  - Add series termination resistor
  - Reduce trace length
  - Add decoupling capacitors
```

---

## Subsystem Debugging

### Arithmetic Unit

**Problem**: Incorrect addition results

**Debug workflow**:

```bash
# Test 1: Single-bit adder
A=0, B=0, Cin=0 → Sum=0, Cout=0
A=0, B=1, Cin=0 → Sum=1, Cout=0
A=1, B=0, Cin=0 → Sum=1, Cout=0
A=1, B=1, Cin=0 → Sum=0, Cout=1
(test all 8 combinations)

# Test 2: Carry chain
Input: A=0xFF, B=0x01 (should overflow)
Expected: Sum=0x00, Cout=1

# Scope carry propagation
Ch1: A[0] (trigger)
Ch2: FA0.Cout
Ch3: FA7.Cout
Measure: Carry ripple time (~400ns)

# If carry doesn't propagate:
- Check carry chain connections
- Verify full adder outputs
- Test individual full adders
```

**Problem**: Subtraction doesn't work

**Debug workflow**:

```bash
# Test XOR array
M=0 (ADD mode): B should pass unchanged
M=1 (SUB mode): B should be inverted

# Scope B and B'
Ch1: B[0]
Ch2: B'[0] (after XOR)
Ch3: M (control signal)

When M=0: B' should equal B
When M=1: B' should equal ~B

# If XOR not working:
- Check M signal reaches XOR gates
- Verify XOR gate implementation
- Test XOR gates individually
```

### Logic Unit

**Problem**: All logic operations give same result

**Debug workflow**:

```bash
# Test operation selection
Set A=0xFF, B=0x0F

Expected results:
NAND: 0xF0
NOR:  0x00
XOR:  0xF0
AND:  0x0F
OR:   0xFF

# If all same:
- Check LOGIC_SEL control signals
- Verify MUX connections
- Test MUX with known inputs

# Scope control signals
Ch1: LOGIC_SEL[0]
Ch2: LOGIC_SEL[1]
Ch3: LOGIC_SEL[2]
Ch4: MUX output

# Verify MUX truth table
```

### Flag Generation

**Problem**: EQUAL flag always wrong

**Debug workflow**:

```bash
# Test equality detection
A=42, B=42 → EQUAL should be 1
A=42, B=43 → EQUAL should be 0

# Scope XOR array
For each bit i:
  Ch1: A[i]
  Ch2: B[i]
  Ch3: XOR[i] (should be 0 when A[i]==B[i])

# Check NOR gate
All XOR outputs should feed into NOR
NOR output = EQUAL flag

# If not working:
- Verify all 8 XOR gates
- Check NOR gate inputs
- Test NOR gate separately
```

---

## Signal Integrity Issues

### Problem: Intermittent Failures

**Symptoms**:
- Works sometimes, fails randomly
- Behavior changes with temperature
- Touching board affects operation

**Debug procedure**:

```bash
# Check solder joints
1. Visual inspection with magnification
2. Reflow suspect joints
3. Test continuity before/after reflow

# Check for floating inputs
1. Add pull-down resistors (10kΩ) to all inputs
2. Verify all control signals are driven
3. Check for unconnected pins

# Check power supply noise
1. Scope VCC with AC coupling
2. Look for noise spikes
3. Add more decoupling capacitors if needed
```

### Problem: Timing Violations

**Symptoms**:
- Works at low speed, fails at high speed
- Glitches on outputs

**Debug procedure**:

```bash
# Measure critical path delay
1. Identify longest path (usually ripple-carry)
2. Scope input and output
3. Measure propagation time
4. Compare with specification

# If too slow:
- Check for excessive capacitance
- Verify transistor types (2N7000 vs BS250)
- Reduce trace lengths
- Add buffers if needed

# Check for race conditions
1. Scope multiple signals simultaneously
2. Look for hazards (glitches)
3. Add synchronization if needed
```

---

## Common Failure Modes

### Reversed Transistors

**Symptoms**:
- Gate doesn't work
- Transistor gets hot
- Incorrect logic levels

**Identification**:
```bash
# NMOS (2N7000) correct orientation:
Source → GND
Drain → Output
Gate → Input

# PMOS (BS250) correct orientation:
Source → VCC
Drain → Output
Gate → Input

# Test in-circuit:
Measure voltage at each pin
Compare with expected values
```

**Fix**: Desolder and reinstall correctly

### Cold Solder Joints

**Symptoms**:
- Intermittent connections
- Noise on signals
- Continuity test fails randomly

**Identification**:
```bash
# Visual inspection:
Good joint: Shiny, smooth, concave fillet
Bad joint: Dull, grainy, convex blob

# Electrical test:
Wiggle component while measuring continuity
If resistance changes: Cold joint
```

**Fix**: Reflow with fresh solder and flux

### Missing Pull-Resistors

**Symptoms**:
- Floating inputs
- Erratic behavior
- Noise sensitivity

**Identification**:
```bash
# Check input voltages
Undriven input should be at defined level
If floating between 0V and 5V: Missing pull resistor

# Add pull-down:
10kΩ resistor from input to GND
```

---

## Case Studies

### Case Study 1: Adder Not Working

**Problem**: ADD operation returns 0 for all inputs

**Debug process**:
1. Tested individual full adders → All working
2. Checked carry chain → FA0.Cout not connected to FA1.Cin
3. Fixed connection → ADD working
4. Verified with test vectors → All passing

**Lesson**: Always verify connections between stages

### Case Study 2: Intermittent Logic Operations

**Problem**: Logic operations work sometimes, fail randomly

**Debug process**:
1. Scoped control signals → LOGIC_SEL floating
2. Added pull-down resistors → Still intermittent
3. Checked solder joints → Found cold joint on control decoder
4. Reflowed joint → Problem solved

**Lesson**: Intermittent issues often indicate poor connections

### Case Study 3: Excessive Power Consumption

**Problem**: Current draw 800mA (expected 150mA)

**Debug process**:
1. Used thermal camera → Found hot PMOS transistor
2. Measured voltages → Gate at 5V (should be 0V for off)
3. Traced signal → Control signal inverted
4. Fixed control logic → Current normal

**Lesson**: Thermal imaging quickly locates problems

---

## Quick Reference

### Voltage Levels

| Signal | Logic 0 | Logic 1 |
|--------|---------|---------|
| CMOS output | < 0.5V | > 4.5V |
| CMOS input threshold | < 1.5V | > 3.5V |

### Typical Delays

| Component | Delay |
|-----------|-------|
| Inverter | 5-10ns |
| 2-input gate | 10-20ns |
| Full adder | 40-60ns |
| 8-bit adder | 350-450ns |

### Test Points

**Critical signals to scope**:
1. VCC, GND (power integrity)
2. A[0], B[0] (inputs)
3. FA0.Cout, FA7.Cout (carry chain)
4. MUX_OUT[0] (datapath)
5. OUT[0] (final output)

---

## Related Documentation

- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Common issues and solutions
- [GETTING_STARTED.md](GETTING_STARTED.md) - Setup and assembly
- [ARCHITECTURE.md](ARCHITECTURE.md) - System design
- [VERIFICATION.md](VERIFICATION.md) - Test procedures

---

**Last Updated**: January 2026  
**Version**: 1.0  
**Author**: Tyrone Marhguy
