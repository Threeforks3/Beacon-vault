---
title: "Paddlecraft Separation"
type: scenario
tags:
  - scenario/water
  - scenario/day
  - source/uscg-sea-school
  - source/cospas-sarsat
  - source/mra
created: 2026-06-27
status: active
---

# Paddlecraft Separation

A paddler becomes separated from their craft — capsized in wind, swamped by wake, or ejected in current. The craft blows downwind faster than they can swim. They are now alone in the water with no buoyancy aid beyond their PFD.

> **[[Paddlecraft separation|Paddlecraft Separation]] — What to do immediately**
> - Activate Beacon immediately — your craft is drifting away and may be spotted first by SAR
> - Do not swim after the craft — you will exhaust yourself before catching it
> - Assume HELP posture — conserve heat, keep Beacon lens skyward
> - If in a group: raft up, keep Beacon on the highest point
> - The signal marks YOU, not your boat. SAR homes on the signal, not the empty hull.

![[diagrams/separation-rescue.html|Paddlecraft separation rescue chain]]

## The Scenario

Wind separates paddler from craft faster than most people realize. A kayak in 15 knots of wind drifts at 1-2 knots — faster than a person in a PFD can swim. Within minutes, the gap is irrecoverable. The craft is spotted from the air first — it's larger, more reflective. SAR arrives, finds an empty hull, and the search restarts from scratch.

The person in the water is now a 30cm target in a sea state. Without an active signal, they are functionally invisible. With wind chop, spray, and wave troughs, a visual search from the air is near-impossible outside of glassy-calm conditions.

## Current Technologies & Practices

| Technology | Used By | Strengths | Gap |
|------------|---------|-----------|-----|
| Rescue 21 + SAROPS | USCG¹ | Triangulated fix, drift model | Search centers on craft position — finds empty hull |
| EPIRB/PLB | COSPAS-SARSAT² | Satellite alert with GPS | Usually attached to vessel — drifts with craft, not person |
| PFD whistle | Universal | Audible close-range | 0.5 nm range maximum in calm conditions |
| Signal mirror | Universal | Daylight passive | Useless with sun behind clouds or at wrong angle |
| Strobe light | MRA, NASAR³ | Visible at night | Standard strobe 8h ceiling, no SOS pattern |

## The Bottleneck

SAR searches for the largest, most visible object — the craft. The paddler in the water is physically separated from it. By the time the empty hull is located and the search restarts, the victim has drifted further and the search area has expanded. The entire pipeline is optimized for finding boats, not people.

## Beacon Design Response

The Beacon is worn on the PFD — it stays with the person, not the craft. Bar-based attachment threads onto any PFD webbing. Tethered retention ensures it remains attached even under rough water conditions. When a paddler activates Beacon, the search target is the person — not the drifting hull. The strobe marks the victim's position from the moment of separation.

## Beacon Perspective

Beacon marks you, not your boat. That's the right target — but only if you can activate it.

**Where Beacon falls short:** If you're unconscious after the separation — head injury from capsize, cold shock incapacitation — Beacon can't activate itself. There's no accelerometer trigger, no water-contact sensor. In whitewater or rough seas, the strobe is intermittently submerged — visible between wave crests but not continuously. No satellite alert, no GPS transmission. Someone must report you overdue to start the search. Beacon makes you findable once SAR is looking — it doesn't notify them you're missing.

Is there anything we're missing? Can you help us see what we may be missing?

*My mission is to be useful when human lives are in danger.*

## Coalition Footnotes

[¹] **USCG Rescue 21:** SAROPS drift model centers on the reported vessel position. If the vessel is an empty kayak and the victim is a half-mile upwind, the search pattern is optimized for the wrong target. [[USCG Rescue 21 Search Patterns]]

[²] **COSPAS-SARSAT:** EPIRBs are bracket-mounted to vessels. A PLB carried on-person addresses this, but most paddlers carry neither. Beacon bridges the recreational gap. [[COSPAS-SARSAT]]

[³] **MRA field equipment guide:** Standard paddler signal kit = whistle + mirror + light. Separation scenarios highlight the need for person-mounted, not craft-mounted, signaling. [[Mountain Rescue Association]]

[⁴] **USCG — Datum Marker:** Coxswain SAR doctrine: the strobe IS the datum marker. A victim with a strobe in a separation scenario becomes their own reference point — the SAROPS drift model now works from the correct position because the signal is on the person, not the empty hull. [[USCG Coxswain SAR Reference]]

## Related

- [[Capsize in open water]] — multi-person capsize variant
- [[Man overboard at night]] — single-person nighttime separation
- [[Buoyancy]] — floatation design
- [[Bar-based attachment]] — universal mounting
- [[Visibility range]] — tested distances