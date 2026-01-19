# Media Assets - 8-Bit Discrete Transistor ALU

> Organized media library for the ALU project

This directory contains all visual evidence, documentation, and demonstration materials for the 8-bit discrete transistor ALU project.

---

## Directory Structure

```
media/
├── design/              # Design files and layouts
│   ├── vlsi/           # VLSI transistor-level layouts (4 files)
│   ├── electric/       # Electric VLSI design files (6 files)
│   └── kicad/          # KiCad schematic captures (4 files)
│
├── simulations/         # Simulation results and waveforms
│   ├── logisim/        # Logisim Evolution screenshots (2 files)
│   └── spice/          # SPICE simulation waveforms (16 files)
│
├── pcb/                 # PCB designs and renders
│   ├── layouts/        # PCB layout files (21 files)
│   └── renders/        # 3D PCB renders (7 files)
│
├── schematics/          # Circuit schematics
│   ├── boards/         # Complete board schematics (19 files)
│   ├── gates/          # Individual gate schematics (87 files)
│   └── modules/        # Module schematics (adder, mux, etc.) (5 files)
│
├── videos/              # Video demonstrations
│   ├── demos/          # Operation demos (7 videos)
│   └── process/        # Build process videos (9 videos)
│
├── photos/              # Physical hardware photos
│   ├── assembly/       # Assembly close-ups (2 photos)
│   └── hardware/       # Completed hardware (6 photos)
│
├── gates/               # Individual gate designs (15 files)
│   ├── and/            # AND gate files
│   ├── or/             # OR gate files
│   ├── nand/           # NAND gate files
│   ├── nor/            # NOR gate files
│   ├── xor/            # XOR gate files
│   ├── xnor/           # XNOR gate files
│   ├── not/            # NOT gate (inverter) files
│   └── adder/          # Full adder files
│
├── testing/             # Test screenshots and results (4 files)
├── timeline/            # Project timeline images (3 files)
└── misc/                # Miscellaneous files (6 files)
```

---

## File Statistics

**Total Files:** 223 media assets

| Category | Files | Description |
|----------|-------|-------------|
| **Design** | 14 | VLSI layouts, Electric designs, KiCad schematics |
| **Simulations** | 18 | Logisim screenshots, SPICE waveforms |
| **PCB** | 28 | PCB layouts and 3D renders |
| **Schematics** | 111 | Board, gate, and module schematics |
| **Videos** | 16 | Demos (7) + Process (9) |
| **Photos** | 8 | Assembly (2) + Hardware (6) |
| **Gates** | 15 | Individual gate design files |
| **Testing** | 4 | Test screenshots and results |
| **Timeline** | 3 | Project timeline images |
| **Misc** | 6 | Other assets |

---

##  Key Files

### Design Phase

**VLSI Transistor Layouts:**
- `design/vlsi/design_vlsi_inverter_mosfet.jpg` - NOT gate transistor layout
- `design/vlsi/design_vlsi_nand_mosfet.jpg` - NAND gate transistor layout
- `design/vlsi/design_vlsi_nor_mosfet.jpg` - NOR gate transistor layout
- `design/vlsi/design_vlsi_xor_mosfet.jpg` - XOR gate transistor layout

**Electric VLSI Designs:**
- `design/electric/design_electric_half_adder.png` - Half adder schematic
- `design/electric/design_electric_and.png` - AND gate design
- `design/electric/design_electric_or.png` - OR gate design
- `design/electric/design_electric_nand.png` - NAND gate design
- `design/electric/design_electric_xor.png` - XOR gate design
- `design/electric/design_electric_xnor.png` - XNOR gate design

**KiCad Schematics:**
- `design/kicad/design_kicad_alu_schematic.jpg` - Main ALU schematic
- `design/kicad/design_kicad_flags_schematic.jpg` - Flag generation schematic
- `design/kicad/design_kicad_control_schematic.jpg` - Control decoder schematic
- `design/kicad/design_kicad_alu_pcb_layout.png` - PCB layout

### Simulation Results

**Logisim:**
- `simulations/logisim/sim_logisim_evolution_full.png` - Complete ALU simulation
- `simulations/logisim/logism-evolution-full-circuit.png` - Full circuit view

**SPICE Waveforms:**
- `simulations/spice/*-spice*.png` - Gate-level SPICE simulations
- `simulations/spice/*electric-spice-schem-drc-check.png` - DRC verification

### PCB Files

**Layouts:**
- `pcb/layouts/pcb_add_sub.png` - Add/Sub unit PCB
- `pcb/layouts/pcb_flags.png` - Flag generation PCB
- `pcb/layouts/pcb_control.png` - Control decoder PCB
- `pcb/layouts/pcb_adder_8bit.png` - 8-bit adder PCB
- `pcb/layouts/pcb_led_panel_*.png` - LED panel PCBs (1-4)

**3D Renders:**
- `pcb/renders/alu-full-3d.png` - Complete ALU 3D render
- `pcb/renders/alu_full_3d.png` - Alternative 3D view
- `pcb/renders/unrouted_full_alu_monolithic.png` - Unrouted full ALU
- `pcb/renders/unrouted-pcb-ratnet-full-alu.png` - Ratsnest view

### Videos

**Demos (Operation Demonstrations):**
- `videos/demos/main-demo-logism-evolution-all-opcodes.mp4` - **Main demo (all 19 operations)**
- `videos/demos/sub-logism-demo-video.mp4` - Subtraction demo
- `videos/demos/testing_demo.mp4` - Testing demonstration
- `videos/demos/testing-demo.mp4` - Alternative testing demo
- `videos/demos/main_demo_inverter.mp4` - Inverter demo
- `videos/demos/logic-unit-sim-logism-evolution-fpga-export-sim.mp4` - Logic unit sim
- `videos/demos/logic_unit_sim_logism_evolution_fpga_export.mp4` - Logic unit export

**Process (Build Process):**
- `videos/process/nand_gate_full_flow.mp4` - NAND gate: transistor → PCB → testing
- `videos/process/half-adder-electric-vlsi-design.mp4` - Half adder design process
- `videos/process/design_electric_half_adder_video.mp4` - Electric design walkthrough
- `videos/process/kicad-8bit-nor-and spice simulation.mp4` - KiCad + SPICE workflow
- `videos/process/nand-gate-kicad-schematics-routing-3d.mp4` - NAND gate PCB process
- `videos/process/sim_ngspice_nor_kicad.mp4` - NOR gate SPICE simulation
- `videos/process/begining-routing-kicad-screenrecord.mp4` - PCB routing demo
- `videos/process/routing-demo.mp4` - Routing demonstration
- `videos/process/0001-0030.mp4` - Build sequence 1
- `videos/process/0001-0060.mp4` - Build sequence 2

### Photos

**Assembly Close-ups:**
- `photos/assembly/not_closeup_soldered_mosfets.jpg` - Hand-soldered MOSFETs
- `photos/assembly/not closeup soldered mosfets.jpg` - Alternative view

**Hardware:**
- `photos/hardware/alu_top.jpg` - **Complete ALU system (main photo)**
- `photos/hardware/not_demo_off_to_on.jpg` - NOT gate demo (OFF → ON)
- `photos/hardware/not_demo_on_to_off.jpg` - NOT gate demo (ON → OFF)
- `photos/hardware/not_demo_off to on.jpg` - Alternative demo
- `photos/hardware/not-demo-on to off.jpg` - Alternative demo
- `photos/hardware/begining-routing-kicad-screenrecord-Cover.jpg` - Routing cover

### Testing

- `testing/test_script_vector_screenshot.png` - **Test execution screenshot**
- `testing/test-script-vector-screenshot.png` - Alternative screenshot
- `testing/test_passed.png` - Test passed indicator
- `testing/test-passed.png` - Alternative indicator

### Timeline

- `timeline/process_timeline_01_mosfet_design.jpg` - Phase 1: MOSFET design
- `timeline/process_timeline_02_schematic.jpg` - Phase 2: Schematic capture
- `timeline/process_timeline_04_pcb_design.png` - Phase 4: PCB design

---

## Usage in Documentation

### README.md References

**Main image:**
```markdown
![Complete ALU System](media/photos/hardware/alu_top.jpg)
```

**Video links:**
```markdown
[![Watch Full Demo](media/photos/hardware/alu_top.jpg)](media/videos/demos/main-demo-logism-evolution-all-opcodes.mp4)
```

**Build gallery:**
- VLSI: `media/design/vlsi/design_vlsi_*.jpg`
- Simulations: `media/simulations/spice/*.png`
- Schematics: `media/schematics/boards/*.svg`
- PCB: `media/pcb/renders/*.png`
- Assembly: `media/photos/assembly/*.jpg`

### Video Demonstrations

**For quick demos:**
1. Main demo (all ops): `videos/demos/main-demo-logism-evolution-all-opcodes.mp4`
2. Subtraction: `videos/demos/sub-logism-demo-video.mp4`
3. Testing: `videos/demos/testing_demo.mp4`

**For technical deep-dives:**
1. NAND gate flow: `videos/process/nand_gate_full_flow.mp4`
2. SPICE simulation: `videos/process/sim_ngspice_nor_kicad.mp4`
3. PCB routing: `videos/process/routing-demo.mp4`

---

## File Naming Conventions

### Prefixes

- `design_vlsi_*` - VLSI transistor-level layouts
- `design_electric_*` - Electric VLSI design files
- `design_kicad_*` - KiCad schematic captures
- `sim_*` - Simulation results
- `pcb_*` - PCB layout files
- `schematic_*` - Circuit schematics
- `test_*` - Testing screenshots
- `process_timeline_*` - Timeline images

### Suffixes

- `*_mosfet.jpg` - Transistor-level designs
- `*_schematic.jpg` - Schematic captures
- `*_pcb*.png` - PCB layouts
- `*-spice*.png` - SPICE simulation results
- `*-demo*.mp4` - Demonstration videos
- `*_page-*.jpg` - Multi-page schematics

---

##  Maintenance

### Adding New Files

**Design files:**
- VLSI layouts → `design/vlsi/`
- Electric designs → `design/electric/`
- KiCad schematics → `design/kicad/`

**Simulation results:**
- Logisim screenshots → `simulations/logisim/`
- SPICE waveforms → `simulations/spice/`

**PCB files:**
- Layout PNGs → `pcb/layouts/`
- 3D renders → `pcb/renders/`

**Videos:**
- Operation demos → `videos/demos/`
- Build process → `videos/process/`

**Photos:**
- Assembly close-ups → `photos/assembly/`
- Completed hardware → `photos/hardware/`

### Updating README.md

When adding new key media files, update:
1. This README.md (media/README.md)
2. Main project README.md (../README.md)
3. MEDIA_INDEX.md (docs/MEDIA_INDEX.md)

---

## Quality Standards

**Images:**
- Format: PNG (screenshots, diagrams) or JPG (photos)
- Resolution: Minimum 1920×1080 for screenshots
- Photos: High resolution, well-lit, in-focus

**Videos:**
- Format: MP4 (H.264)
- Resolution: 1920×1080 minimum
- Length: 30 seconds to 2 minutes (demos), up to 5 minutes (process)
- Audio: Optional but recommended for narration

**File Sizes:**
- Images: < 5MB each
- Videos: < 50MB each (compress if needed)

---

##  Deprecated Files

**Old folder structure (removed):**
- `pcb photos/` → merged into `pcb/layouts/`
- `schematics photos jpg/` → merged into `schematics/boards/`
- `schematics photos svg/` → merged into `schematics/boards/`
- `schematics -gates-mux-adder/` → merged into `schematics/gates/` and `pcb/layouts/`

**Empty folders (removed):**
- `demo_videos/` → content moved to `videos/demos/`
- `renders/` → content moved to `pcb/renders/`
- `photos_build/` → content moved to `photos/assembly/`
- `waveforms/` → content moved to `simulations/spice/`
- `gifs/` → empty
- `images/` → empty
- `screenshots/` → empty

---

## Questions

**If you need specific media files:**
1. Check this README for file locations
2. Browse the organized folders
3. Search by filename pattern
4. Contact: tmarhguy@gmail.com | tmarhguy@seas.upenn.edu

---

**Last Updated:** January 16, 2026  
**Total Files:** 223 media assets  
**Total Size:** ~500MB  
**Organization:** Completed

---

**Related Documentation:**
- [Main README](../README.md) - Project overview
- [MEDIA_INDEX](../docs/MEDIA_INDEX.md) - Complete media catalog
- [ARCHITECTURE](../docs/ARCHITECTURE.md) - Technical details
