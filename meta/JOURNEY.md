# The Journey: From 3AM Thoughts to 3,488 Transistors

> *"It's 3am, and I think: what if I woke up in a medieval time before computers existed? Can I trust myself to build the first ALU from the very bare level: discrete transistors?"*

This project didn't start as a homework assignment. It started in my solo dorm room, born from a noisy brain at 3 AM and a hypothetical survival scenario.

## The Medieval Hypothesis

If I were transported back in time, could I restart the digital age? It's a question of fundamental understanding. Not using chips, not using standard libraries, but using the raw physics of switching.

To validate this hypothesis, I had to move from theoretical models to physical atoms. This meant sourcing discrete components and fabricating custom PCBs even for the simplest gates.

| DigiKey Component Order | JLCPCB Prototype Order |
| :---: | :---: |
| ![DigiKey Order](../media/gates/not/not_mosfet_order_digikey.png) | ![JLCPCB Order](../media/gates/not/not_pcb_order_jlcpcb.png) |
| *Procuring BSS138/BSS84 MOSFETs for early logic validation* | *Initial manufacture of the 1-bit Sample Inverter PCB* |

There was only one way to find out. Lucky for me, being a Computer Engineering sophomore at Penn means I have the license to do exactly this—to dive as deep as I want into both hardware and software.

## 100+ Hours in Solitude

I spent my winter break not relaxing, but locked in.

- **The Process**: I began designing schematics for inverters, NANDs, NORs, XNORs—notting them, combining them, proving them.
- **The Rigor**: I verified SPICE directives for each design in ngspice (Electric VLSI). I recreated them in KiCad. I tested and retested because, in my medieval timeline, a mistake would be "expensive."
- **The Scale**: I went from single gates to bigger blocks—half adders, full adders, then 8-bit versions.

A standard ALU needs a control signal, so I designed a decoder to convert 5-bit opcodes. This took days to weeks of pure "lock-in." It's funny, but I loved it. 15-hour days felt too easy. It was like a hardware hackathon that no one forced me into.

## 1.25 Million Realities

I didn't want to just build *an* ALU; I wanted to build *the* ALU.

To ensure absolute rigor, I designed an FPGA-rendered version and tested every possible input combination.

- **256** (Input A) × **256** (Input B) × **19** (Opcodes)
- **1,247,084 test cases.**
- **100% pass rate across all 19 operations.**

They all passed.

## Conclusion

Now I can go to sleep knowing that if I appeared in medieval times, even solo, computers would be invented long before cars and quarter zips.

Maybe we wouldn't use SPICE or UVM testing rigor. Maybe we'd just use a simple audible continuity tester—like the one I built at 13 with two nails, a beeper, and wires from an old cassette player. But it would be enough.

Make no mistake: I can now "smell" any logic gate configuration from a mile away.

*This project is the physical manifestation of that obsession. Enjoy the journey.*

---
*By Tyrone Marhguy, Computer Engineering, UPenn*
