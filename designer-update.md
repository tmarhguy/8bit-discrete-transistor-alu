![Status](https://img.shields.io/badge/status-optimization%20phase-orange)
![Architecture](https://img.shields.io/badge/architecture-fully%20discrete%20CMOS-blueviolet)
![Operations](https://img.shields.io/badge/ops-19-success)
![Transistors](https://img.shields.io/badge/transistors-3%2C488%2B-critical)
![License](https://img.shields.io/badge/license-MIT-green)

---

In a rather intentional turn of things, hoping to improve **fact and verifiability**, I will replace all black boxes with fully discrete parts. By that, I mean every mux and XOR gate will be designed directly with MOSFETs.

Currently, there are **624 discrete MOSFET components**, and an estimated **2,864 MOSFETs “hidden”** inside 74xx black-box muxes and XORs.

The initial choice of these 74xx ICs was to manage propagation delays—hence overall speed—and cost. Engineering, I’ve learned, without constraint is a mere fantasy; one the real world simply cannot afford.

Consider an 8-to-1, 2-bit mux: it costs at most **$2** as an IC, compared to a discrete implementation that would require on the order of **10² transistors**, each costing at least **$0.50** (if generosity is real).  

But to compromise such an intriguing pursuit of “discrete transistor” design—even once—for cost gives me pause. What’s the worst that could happen?

In light of this, all 74xx ICs will now be treated as **temporary black boxes** that *will be replaced*. Their only current purpose is to help design an MVP. Their existence sped up the process and early simulations for a first-time ALU sophomore designer.

But for facts and reference, this **will be a fully discrete transistor 8-bit ALU supporting 19 operations.**

Elegance will be compromised, but practicality is what the world we know was founded on. Besides, abstraction—when treated with proper respect—**facilitates rather than deceives** progress and truth.

---

### Why designing from the MOSFET level actually helps

Designing components from the MOSFET level to replace black boxes does an unrealized good.

Take a simple **2-to-1 mux**:

Using ready-made logic:
- You’d need **four 3-input AND gates**  
- Followed by **one 4-input OR gate**

Cost analysis:
- A 3-input AND requires **two AND gates**  
- Each AND = **6T**, so → **12T per 3-input AND**  
- Four of them → **48T**

For the OR stage:
- A 4-input OR needs **three OR gates**  
- Each OR = **6T**, so → **18T**

**Total using logic gates:**
> 48T + 18T = **66 transistors**

---

### MOSFET-level optimization

At the transistor level:

- A 3-input AND → **3-input NAND + inverter = 8T**
- Four of those → **32T**

For OR:
- A 4-input OR → **4-input NOR + inverter = 10T**

**Total:**
> 32T + 10T = **42 transistors**

That’s a **36% reduction**  
(4/11 fewer transistors).

By this design, I begin approaching a **more robust ALU** with:
- Lower transistor count  
- Less propagation delay  
- Better scalability for discrete logic

---

### But… not the final answer

Still, assuming this is a final solution is only **half—if not a quarter—of the picture.**

Transmission gates, from what I’ve read, offer a far more sane option than this pseudo-“VLSI” approach. A TG-based design cuts transistor counts even further—significantly so—even by rough mental math.

And that is precisely why I am **still in the optimization phase** of this project.
