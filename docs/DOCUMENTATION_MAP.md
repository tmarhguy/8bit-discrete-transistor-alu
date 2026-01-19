# Documentation Map

**Complete navigation guide for the 8-bit discrete transistor ALU project documentation**

This document provides a comprehensive map of all project documentation, organized by purpose and audience.

---

## Quick Navigation

### For New Users

Start here to get up and running:

1. **[README.md](../README.md)** - Project overview and mission
2. **[GETTING_STARTED.md](GETTING_STARTED.md)** - Setup and installation
3. **[CLI_GUIDE.md](CLI_GUIDE.md)** - Command-line tool usage

### For Contributors

Essential reading for contributors:

1. **[CONTRIBUTING.md](../CONTRIBUTING.md)** - Contribution guidelines
2. **[ARCHITECTURE.md](ARCHITECTURE.md)** - System architecture
3. **[VERIFICATION.md](VERIFICATION.md)** - Testing methodology

### For Hardware Builders

Building the physical ALU:

1. **[GETTING_STARTED.md](GETTING_STARTED.md)** - Prerequisites and tools
2. **[build-notes/bom.md](build-notes/bom.md)** - Bill of materials
3. **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** - Common issues
4. **[DEBUGGING_GUIDE.md](DEBUGGING_GUIDE.md)** - Hardware debugging

---

## Documentation Hierarchy

```
cpu/
├── README.md                    # Project overview
├── meta/                # Project metadata
│   ├── CHANGELOG.md     # Version history
│   ├── CONTRIBUTING.md  # How to contribute
│   ├── JOURNEY.md       # Project story
│   └── TRANSISTOR_COUNT_REPORT.md # Detailed count
├── LICENSE              # MIT license
│
└── docs/
    ├── index.md                 # Documentation index
    ├── DOCUMENTATION_MAP.md     # This file
    ├── GLOSSARY.md              # Terms and acronyms
    │
    ├── GETTING_STARTED.md       # Setup guide
    ├── ARCHITECTURE.md          # System architecture
    ├── VERIFICATION.md          # Testing strategy
    ├── TROUBLESHOOTING.md       # Common issues
    ├── DEBUGGING_GUIDE.md       # Debugging procedures
    │
    ├── OPCODE_TABLE.md          # Operation reference
    ├── CLI_GUIDE.md             # CLI tool guide
    ├── POWER.md                 # Power analysis
    ├── MEDIA_INDEX.md           # Media catalog
    │
    ├── architecture/            # Architecture details
    │   ├── overview.md
    │   ├── control.md
    │   ├── flags.md
    │   └── schematics.md
    │
    ├── verification/            # Verification details
    │   ├── strategy.md
    │   ├── procedures.md
    │   ├── test-matrix.md
    │   ├── timing.md
    │   ├── opcode-status.md
    │   └── known-issues.md
    │
    └── build-notes/             # Build information
        ├── bom.md
        ├── bringup.md
        ├── decisions.md
        ├── release.md
        └── component_inventory.md
```

---

## Documentation by Purpose

### Understanding the Project

| Document | Purpose | Audience |
|----------|---------|----------|
| [README.md](../README.md) | Project overview, features, quick start | Everyone |
| [ARCHITECTURE.md](ARCHITECTURE.md) | System design and implementation | Technical |
| [HOW_IT_WORKS.md](../HOW_IT_WORKS.md) | Detailed operation explanation | Technical |

### Getting Started

| Document | Purpose | Audience |
|----------|---------|----------|
| [GETTING_STARTED.md](GETTING_STARTED.md) | Setup, installation, first steps | New users |
| [CLI_GUIDE.md](CLI_GUIDE.md) | Command-line tool usage | Users |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Common problems and solutions | All users |

### Technical Reference

| Document | Purpose | Audience |
|----------|---------|----------|
| [OPCODE_TABLE.md](OPCODE_TABLE.md) | Complete operation specifications | Developers |
| [POWER.md](POWER.md) | Transistor count and power analysis | Engineers |
| [FLAG_IMPLEMENTATION_GUIDE.md](FLAG_IMPLEMENTATION_GUIDE.md) | Flag generation details | Developers |

### Verification & Testing

| Document | Purpose | Audience |
|----------|---------|----------|
| [VERIFICATION.md](VERIFICATION.md) | Testing methodology and results | Developers |
| [sim/FPGA/README.md](../sim/FPGA/README.md) | FPGA Verilog Implementation | Developers |
| [test/README.md](../test/README.md) | Test suite documentation | Developers |
| [verification/test-matrix.md](verification/test-matrix.md) | Test coverage matrix | QA |

### Hardware Build

| Document | Purpose | Audience |
|----------|---------|----------|
| [build-notes/bom.md](build-notes/bom.md) | Bill of materials | Builders |
| [build-notes/bringup.md](build-notes/bringup.md) | Hardware bring-up procedure | Builders |
| [DEBUGGING_GUIDE.md](DEBUGGING_GUIDE.md) | Hardware debugging | Builders |

### Contributing

| Document | Purpose | Audience |
|----------|---------|----------|
| [CONTRIBUTING.md](../meta/CONTRIBUTING.md) | Contribution guidelines | Contributors |
| [CHANGELOG.md](../meta/CHANGELOG.md) | Version history | Contributors |
| [DOCUMENTATION_STYLE_GUIDE.md](DOCUMENTATION_STYLE_GUIDE.md) | Documentation standards | Contributors |

---

## Reading Paths by Role

### Role: Student / Learner

**Goal**: Understand how ALUs work from first principles

**Recommended path**:
1. [README.md](../README.md) - Overview
2. [HOW_IT_WORKS.md](../HOW_IT_WORKS.md) - Detailed explanation
3. [ARCHITECTURE.md](ARCHITECTURE.md) - System design
4. [GETTING_STARTED.md](GETTING_STARTED.md) - Try it yourself
5. [CLI_GUIDE.md](CLI_GUIDE.md) - Experiment with operations

### Role: Hardware Builder

**Goal**: Build the physical ALU

**Recommended path**:
1. [README.md](../README.md) - Project overview
2. [GETTING_STARTED.md](GETTING_STARTED.md) - Prerequisites
3. [build-notes/bom.md](build-notes/bom.md) - Order components
4. [build-notes/bringup.md](build-notes/bringup.md) - Assembly procedure
5. [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Common issues
6. [DEBUGGING_GUIDE.md](DEBUGGING_GUIDE.md) - Hardware debugging

### Role: Software Developer

**Goal**: Understand and modify the test framework

**Recommended path**:
1. [README.md](../README.md) - Project overview
2. [ARCHITECTURE.md](ARCHITECTURE.md) - System design
3. [VERIFICATION.md](VERIFICATION.md) - Testing methodology
4. [test/README.md](../test/README.md) - Test suite details
5. [CONTRIBUTING.md](../meta/CONTRIBUTING.md) - Contribution guidelines

### Role: Reviewer / Evaluator

**Goal**: Assess project quality and completeness

**Recommended path**:
1. [README.md](../README.md) - Project claims
2. [VERIFICATION.md](VERIFICATION.md) - Evidence of testing
3. [MEDIA_INDEX.md](MEDIA_INDEX.md) - Visual evidence
4. [ARCHITECTURE.md](ARCHITECTURE.md) - Technical depth
5. [CHANGELOG.md](../meta/CHANGELOG.md) - Development history

---

## Cross-Reference Matrix

### Architecture ↔ Verification

| Architecture Topic | Verification Document |
|-------------------|----------------------|
| Arithmetic Unit | [verification/procedures.md](verification/procedures.md) - Adder tests |
| Logic Unit | [verification/test-matrix.md](verification/test-matrix.md) - Logic tests |
| Flag Generation | [verification/procedures.md](verification/procedures.md) - Flag tests |
| Control Decoder | [verification/opcode-status.md](verification/opcode-status.md) - Opcode tests |

### Documentation ↔ Implementation

| Documentation | Implementation |
|--------------|----------------|
| [OPCODE_TABLE.md](OPCODE_TABLE.md) | `test/test_alu.py` - Golden model |
| [ARCHITECTURE.md](ARCHITECTURE.md) | `schematics/kicad/` - Hardware design |
| [VERIFICATION.md](VERIFICATION.md) | `test/` - Test suite |
| [CLI_GUIDE.md](CLI_GUIDE.md) | `alu_cli.py` - CLI tool |

---

## Documentation Status

### Complete 

- Project overview and mission
- Setup and installation guide
- Architecture documentation
- Verification methodology
- CLI tool guide
- Opcode reference
- Troubleshooting guide

### In Progress 

- Hardware debugging guide (this release)
- Documentation style guide (this release)
- Glossary (this release)

### Planned 

- Video tutorial series
- Interactive web demo
- [FPGA Implementation](../sim/FPGA/README.md) - Industry-grade Verilog implementation
- FPGA implementation guide
- Advanced optimization techniques

---

## Finding Specific Information

### How do I...

**...set up the project?**
→ [GETTING_STARTED.md](GETTING_STARTED.md)

**...run tests?**
→ [test/README.md](../test/README.md) or [VERIFICATION.md](VERIFICATION.md)

**...understand an operation?**
→ [OPCODE_TABLE.md](OPCODE_TABLE.md)

**...debug hardware?**
→ [TROUBLESHOOTING.md](TROUBLESHOOTING.md) or [DEBUGGING_GUIDE.md](DEBUGGING_GUIDE.md)

**...contribute code?**
→ [CONTRIBUTING.md](../meta/CONTRIBUTING.md)

**...find schematics?**
→ [architecture/schematics.md](architecture/schematics.md) or `schematics/` directory

**...understand transistor count?**
→ [POWER.md](POWER.md)

**...see test results?**
→ [VERIFICATION.md](VERIFICATION.md)

---

## External Resources

### Tools Documentation

- [Logisim Evolution](https://github.com/logisim-evolution/logisim-evolution) - Digital logic simulator
- [KiCad](https://docs.kicad.org/) - PCB design software
- [ngspice](http://ngspice.sourceforge.net/docs.html) - SPICE simulator

### Learning Resources

- [Digital Design Principles](https://www.nand2tetris.org/) - From NAND to Tetris
- [CMOS VLSI Design](http://cmosedu.com/) - Transistor-level design
- [Computer Architecture](https://www.coursera.org/learn/comparch) - System-level design

---

## Document Maintenance

### Updating Documentation

When making changes to the project:

1. **Update relevant documentation** - Keep docs in sync with code
2. **Update CHANGELOG.md** - Record all changes (in meta/)
3. **Update this map** - If adding new documents
4. **Run validation** - `python tools/validate_docs.py --full`

### Documentation Review Checklist

- [ ] All links work
- [ ] All media files exist
- [ ] Code examples execute correctly
- [ ] Version numbers are consistent
- [ ] Cross-references are accurate

---

## Getting Help

**Can't find what you're looking for?**

1. **Search**: Use GitHub's search or `grep` through docs
2. **Ask**: Open an issue on GitHub
3. **Contact**: Email tmarhguy@gmail.com

---

**Last Updated**: January 2026  
**Version**: 1.0  
**Maintainer**: Tyrone Marhguy
