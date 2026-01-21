his update:

In a rather intentional turn of things, hoping to improve fact and verifiability, I will replace or black boxes with full discrete parts! By that I mean all muxes, xor gates will all be designed with MOSFETs. Currently, there are 624 discrete MOSFET components, and an estimated 2864 MOSFET components “hidden” in 74xx black box muxes and xors.

The initial choice of these 74xx ICs were to manage propagation delays, hence overall speed, and cost! Engineering I heard without constraint is a mere fantasy, one which the real world can’t afford!

Consider an 8to1 2 bit mux, which costs at most $2, compared to a discrete implementation that will cost of order 10^2 of transistors, each of which will cost at least $0.50, if generosity is a real thing.

But to compromise a rather intriguing pursuit of “discrete transistor”, a one time adventure for cost, makes me pause… What’s the worst that could happen? In light of this, all 74xx ICs will be treated as black boxes that will be replaced, and their only current purpose is to help design an MVP! Their existence sped up the process and initial simulations for a first timer ALU sophomore designer. But for facts and reference, this will be a fully discrete transistor 8bit ALU, that supports 19 operations.

Elegance will be compromised, but practicality is what the world we know was founded on! Besides, abstraction if treated with this presumed respect, facilitates than deceives progress and truth



Worth mentioning, designing components from MOSFET level to replace the black boxes here does perhaps an unrealized good. Consider building a 2 to 1 mux, I would need 4 of 3 input and gates followed by a 4 input or gate. Cost analysis, a 3 input and gate requires 2 and gates, that makes 12 MOSFETs (6T per and), so 48T in all. For a 4 input OR, 3 ORs are needed, also 3 * 6T.

In all using “ready gates”, you use 18 + 48 which is 66T.

However at the MOSFET level, you cut down a 3 in AND to a 3 in NAND plus an inverter, which is 8T. 4 of those are 32T! Again for 4 in or is 4in Nor plus inverter. This is 10T and not 18 as one is forced to use beyond MOSFET design.

By this, a mux is reduced to 42T, which is essentially 4/11 lower or 36% more savings! By this design, I begin to approach a more robust ALU with less count of transistors and thus less worry for propagation delay in the discrete setting.

Nonetheless, to assume this a final solution is only half if not a quarter of the picture. Transmission Gates as I read offer a much sane option than this pseudo-“VLSI” attempt! This TG attempt cuts down Transistor counts by as many as I can casually compute mentally as is, but it is considerably significant! This is the more reason why I am still in optimization phase of this project! 
