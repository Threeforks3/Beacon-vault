# Capsize in Open Water

A small vessel — kayak, canoe, skiff, sailboat — overturns in open water. Crew ends up in the water, possibly separated from the boat. The vessel may be partially submerged and difficult to spot from the air or surface.

> **[[Capsize in open water|Open Water Capsize]] — What to do immediately**
> - Stay with the vessel if possible — it's larger than you, easier to spot
> - Activate Beacon — attach to highest point on PFD or life raft
> - Keep the strobe clear of debris and spray
> - Conserve body heat — huddle with other survivors
> - The SOS pattern is visible from 2-3 nautical miles. SAR aircraft fly grid patterns. They will see it.

![[diagrams/capsize-rescue.html|Capsize rescue signal chain]]

## The Scenario

A human head in water is roughly 30cm in diameter. From 500ft, even in daylight, it's nearly invisible. At night, it's a negative space. A search aircraft at 90 knots covers 1.5 nautical miles per minute — it can fly directly overhead and miss you.

Typical sequence: vessel overturns → crew surfaces, locates each other → PFDs keep them alive but adrift → VHF radio submerged or unreachable → Coast Guard or local marine unit responds → search aircraft flies grid pattern looking for anything reflective or lit.

## Current Technologies & Practices

| Technology | Used By | Strengths | Gap |
|------------|---------|-----------|-----|
| Rescue 21 + SAROPS | USCG¹ | Triangulated fix, drift model, search pattern | Pattern dependent on mayday — no mayday, no triangulation trigger |
| EPIRB/PLB | COSPAS-SARSAT² | 406 MHz satellite alert with GPS fix | Point-in-time fix — if vessel sinks with EPIRB in bracket, no alert. If manually activated, position is where you WERE. Wind and current move you from that fix. No strobe for homing. |
| Strobe light | MRA, NASAR, ACA³ | Visible at night, recognized distress pattern | White only, no IR, ~8h runtime ceiling |
| Signal mirror | Universal | Daylight passive, infinite | Useless at night; requires sun at correct angle |
| VHF radio | USCG⁴ | Voice mayday, Rescue 21 fix | Submerged, dead battery, or unreachable in capsized vessel |
| AIS MOB | IMO SOLAS vessels⁵ | Local alarm + GPS position to plotter | $300+, recreational boaters exempt from carriage |

## The Gap

A capsize may not produce a mayday call. The vessel overturns suddenly — no time to radio. If no EPIRB is aboard or it sinks with the vessel, search begins only when the vessel is reported overdue. The search area is defined by last known position plus drift — potentially dozens of square miles. Crew in the water have no active signal. The search is looking for heads in water.

## Beacon Design Response

SOS strobe at maximum brightness. 360° hemispherical dome — visible from search aircraft above and surface vessels at water level. IP68 waterproof to 2 meters immersion. Enclosure displacement exceeds device weight — floats lens-up if torn from PFD. Bar-based attachment threads onto PFD webbing — one-hand detach lets you hold it overhead for maximum visibility. Tethered to PFD: bars may release under extreme force, tether retains. 26+ hour runtime spans multi-night operations. IR mode for NVG-equipped search aircraft.

## Coalition Footnotes

[¹] **USCG Rescue 21:** Triangulation requires a VHF transmission. Without a mayday, there is nothing to triangulate. Capsizes that produce no radio call enter the search pipeline only after overdue reporting — adding hours to the response timeline. [[USCG Rescue 21 and search patterns]]

[²] **COSPAS-SARSAT:** EPIRBs are vessel-mounted. If the vessel sinks with the EPIRB still in its bracket, no alert is generated. If manually activated by a crew member in the water, the fix is a GPS position at the moment of transmission — not a track. The victim drifts from that fix in wind and current. SAR arrives at the last known position and searches visually. No integrated strobe for terminal homing. [[COSPAS-SARSAT]]

[³] **ACA (American Canoe Association):** Paddlesports safety curriculum recommends whistle + signal mirror + light. Gap: no power-independent active strobe in standard paddler kit. [[SAR Coalition partner benefits]]

[⁴] **USCG:** Mayday on VHF Ch.16 triggers immediate SAR response. But a handheld VHF in a PFD pocket may be the only radio that survives — and range is limited to 2-5 nautical miles line-of-sight from water level. [[USCG SAR doctrine]]

[⁵] **IMO SOLAS:** AIS MOB devices required on SOLAS-class vessels only. Recreational vessels under 65ft exempt. The majority of capsizes occur on recreational vessels that carry no electronic distress signaling. [[IMO standards]]

[⁶] **USCG Sea School — Predicted Survival Time (Table 3-3):** In 50°F water, a person with flotation holding still survives 2.7 hours; in HELP posture, 4.0 hours. "Individuals should egress from the water as quickly as possible. A life raft or other floatation device should be used if available. Survival time will increase significantly once out of the water." The capsize victim's priority is getting OUT of the water — but until rescue arrives, the priority is being SEEN. [[USCG Sea School - Rescue and Survival Procedures]]

[⁷] **USCG Sea School — Datum Marker:** Coxswain SAR doctrine: "You will typically use a fender or life ring with a strobe light as your DMB." Expanding Square and Sector searches both instruct: "Datum should be marked with a buoy, life ring, strobe light, etc." The strobe is not just a victim signaling device — it is the USCG's standard tool for marking search pattern reference points. A victim with a strobe IS their own datum marker. [[USCG Sea School - Coxswain SAR Reference Guide]]

[⁸] **USCG Sea School — VDS Conservation:** "A distressed vessel has a limited number of VDS's, if any at all, and experienced mariners usually do not activate these signals until they actually see or hear an SRU." This operational reality means victims delay signaling until they perceive rescuers — potentially missing the search aircraft that flew overhead 10 minutes earlier. A 26-hour strobe eliminates the conservation calculus: activate immediately, remain visible continuously. [[USCG Sea School - Coxswain SAR Reference Guide]]

## Related

- [[Man overboard at night]] — single-person variant
- [[Paddlecraft separation]] — paddler separated from craft
- [[Waterproofing]] — IP68 design rationale
- [[Bar-based attachment]] — universal mounting
- [[Buoyancy]] — floatation design
- [[Battery life targets]] — runtime modeling
- [[USCG SAR doctrine]] — search patterns
