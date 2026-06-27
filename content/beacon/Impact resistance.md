# Impact Resistance

Beacon is designed to survive the impacts its users survive. Drop from helicopter hoist height. Water impact at terminal velocity. Avalanche tumble. Mountain bike crash. The device continues signaling after the impact that incapacitated its user.

## Construction

**Through-hole assembly:** All components are through-hole, wave-soldered to a single PCB. No surface-mount components to shear under G-loading. The 5mm LED domes are inherently impact-resistant — a solid epoxy body bonded to the PCB through two leads.

**Polycarbonate cover:** Impact-rated polycarbonate absorbs and distributes impact energy without cracking. Unlike acrylic (brittle, shatters) or glass (heavy, shatters), polycarbonate deforms elastically and returns to shape.

**Single PCB:** No connectors to unseat, no ribbon cables to tear, no stacked boards to delaminate. One board, wave-soldered, everything mechanically continuous.

## Failure Modes

| Impact Type | Most Vulnerable Component | Mitigation |
|-------------|--------------------------|------------|
| Direct strike to dome | LED leads | Through-hole leads absorb flex; polycarbonate dome distributes force |
| Edge impact | PCB mounting | Board is mechanically constrained by enclosure geometry |
| Crush | Battery deformation | AAA steel jacket resists crush; enclosure collapses before battery shorts |
| Vibration | Solder joints | Through-hole joints have 10× the mechanical strength of SMD reflow joints |

## Testing Targets

- Drop from 100ft (helicopter hoist height) onto water: device survives and operates
- Drop from 6ft onto concrete (belt-height drop): cover may scratch, device operates
- 10G multi-axis tumble (avalanche simulation): no component separation
- Repeated impact in swift water against rocks: cover withstands without cracking

## Open Questions

- Has crush testing been performed with a hydraulic press to determine failure point?
- What is the failure mode at crush limit? (Short circuit? Open circuit? Fire risk?)
- Should an accelerometer-triggered activation be considered? (Auto-activate on impact)

## Related

- [[Bar-based attachment]] — keeps device with victim
- [[Avalanche burial]] — tumble forces
- [[Mountain bike crash]] — direct impact scenario
