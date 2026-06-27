---
title: "Man Overboard at Night"
type: scenario
tags:
  - scenario/water
  - scenario/night
  - source/uscg-sea-school
  - source/cospas-sarsat
  - source/mra
  - source/nasar
  - source/cap
created: 2026-06-27
status: active
# Man Overboard at Night

A person falls from a vessel into dark water. The vessel may not immediately know. They surface alone, drifting, with only what's attached to them.

> **[[Man overboard at night|Night Man Overboard]] — What to do immediately**
> - Stay with flotation — do not swim, it accelerates heat loss
> - Activate Beacon — press and hold 2 seconds, place at highest point on PFD
> - Conserve energy — assume HELP posture (Heat Escape Lessening Position)
> - Orient the strobe skyward — search aircraft approach from above
> - Stay calm — the strobe is visible from 2-3 nautical miles. They are looking for you.

![[diagrams/mob-rescue.html|Man overboard rescue chain]]

![[diagrams/night-operations.html|Night operations rescue chain]]

## The Scenario

The critical factor: time. A person overboard at night is not just hard to find — they're drifting while the search area expands. Every minute without a signal means a larger search grid.

Cold water shock — gasp reflex, disorientation, rapid heat loss. In water below 15°C (59°F), functional swimming time is under 30 minutes. Hypothermia reduces the ability to wave, shout, or actively signal. The strobe must work without ongoing user action.

## Current Technologies & Practices

| Technology | Used By | Strengths | Gap |
|------------|---------|-----------|-----|
| Rescue 21 + SAROPS | USCG¹ | Triangulated mayday fix, drift modeling, optimized search pattern | Pattern converges on human lookouts — effective search width ~200yd daylight, ~0yd night |
| EPIRB/PLB | COSPAS-SARSAT² | 406 MHz satellite alert with GPS fix | Point-in-time fix — victim drifts. No strobe for terminal homing. SAR arrives at last known position, must search visually for a head in the water. |
| Strobe light | MRA, NASAR³ | Visible, waterproof, recognized pattern | White only, no IR, typical 8h ceiling |
| VHF radio | USCG Ch.16⁴ | Voice communication, Rescue 21 triangulation | Lost with vessel, submerged, dead battery |
| Search aircraft FLIR | USCG, CAP⁵ | Thermal detection from altitude | Water surface temperature masks body heat; spray degrades signature |
| Signal mirror | Universal | Daylight passive, infinite endurance | Useless at night; requires sun and skill |

## The Bottleneck

The entire search pipeline — triangulation, drift calculation, optimized search pattern — converges on human lookouts scanning water from a moving deck. The system is precise until the final step, which is visual acquisition of a 30cm target in moving water. At night, the search pattern covers miles while the effective visual swath is zero.

## Beacon Design Response

SOS strobe at 19,000+ mcd white + 850nm IR. The SOS pattern is internationally recognized — no navigation light, shore marker, or recreational light flashes SOS. 26h runtime from 2x AAA alkaline. Bar-mounted to PFD webbing — rides at the highest point when floating. 360° dome visible from directly above (hoist operator perspective) and from surface vessels. Single-button press-and-hold activation — deliberate enough to prevent pocket activation, simple enough for cold, wet hands. Through-hole assembly survives water impact at terminal velocity. Stuck-button timeout prevents accidental drain.

**Beacon changes the search object.** The lookout is not searching for a human head. They are searching for an SOS strobe visible from 2-3 nautical miles at night. Effective search width goes from ~200 yards to ~6,000 yards. The search pattern is unchanged — probability of detection within it increases by orders of magnitude.

## Beacon Perspective

Beacon changes what searchers are looking for. It doesn't tell them where to start looking.

**Where Beacon falls short:** Beacon has no EPIRB, no PLB, no satellite transmitter. It doesn't call the Coast Guard. It doesn't broadcast a GPS position. The search must be triggered by someone who knows you're missing. In sea state 4+, the strobe is intermittently underwater — from the air, it's a signal that blinks between wave crests depending on timing. Dense fog attenuates the strobe to close range. What Beacon does: when SAR is searching the right area, it replaces "find a head in dark water" with "fly toward the SOS strobe." It closes the last mile — it doesn't start the first one.

Is there anything we're missing? Can you help us see what we may be missing?

*My mission is to be useful when human lives are in danger.*

## Coalition Footnotes

[¹] **USCG Rescue 21:** Shore-based VHF direction-finding antenna arrays triangulate mayday transmissions. SAROPS calculates drift (wind, tide, current) based on time-to-on-scene. Surface unit drops datum marker, runs timed turns in standardized search pattern. Lookouts scan visually throughout. The entire system is engineered to put a vessel in the right place — but final acquisition is unaided human vision against water.

[²] **COSPAS-SARSAT:** MEOSAR satellites detect 406 MHz alerts in under 10 minutes. The fix is a GPS position at the moment of transmission — an accurate snapshot, not a moving track. In wind and current, a person in the water drifts away from that fix within minutes. SAR aircraft arrive at the last known position and must visually search. PLBs/EPIRBs have no integrated strobe — they alert the network, they don't home the helicopter. Beacon closes the last mile: the fix gets them nearby, the strobe brings them to you. [[COSPAS-SARSAT]]

[³] **MRA field equipment guide:** Minimum personal signaling kit = strobe + whistle + signal mirror. NASAR equivalent recommendations for ground and water search.

[⁴] **USCG:** VHF Ch.16 monitored continuously. Rescue 21 triangulation on transmission. MOB is typically separated from vessel and radio within seconds of fall.

[⁵] **Civil Air Patrol:** FLIR-equipped aircraft fly search grids. Thermal signature of human head in water is within 1-2°C of surrounding water — difficult discrimination in spray or chop.

[⁶] **USCG — Predicted Survival Time (Table 3-3):** In 50°F water: 1.5h floating without flotation, 4.0h in HELP posture or huddle with flotation. "Contrary to popular belief, the survivor should not swim around in efforts to keep warm. This will only increase the rate of heat loss and speed the onset of hypothermia." Core temperature at 95°F: mental confusion, impairment of rational thought, drowning possible. At 91°F: 50% do not survive. [[USCG Rescue and Survival Procedures]]

[⁷] **USCG — Darkness Protocol:** "In hours of darkness, it becomes critical that the appropriate signaling devices are employed. During hours of darkness, flares and lights are crucial when these vessels are near." The USCG survival doctrine explicitly identifies darkness as the condition where active signaling becomes the critical survival factor. [[USCG Rescue and Survival Procedures]]

[⁸] **USCG — Standard Strobe Spec:** The USCG-issued boat crew survival vest strobe: 50-70 flashes per minute, 8h minimum / 18h typical runtime, 2-5 mile visual range, white LED, hook-and-loop attachment to PFD or helmet. Beacon exceeds every parameter: SOS pattern (vs generic strobe), 26h runtime (vs 8h min), 850nm IR mode for NVG operations, bar-based attachment to any webbing (vs hook-and-loop to specific surfaces). [[USCG Rescue and Survival Procedures]]

## Related

- [[Capsize in open water]] — multi-person variant
- [[Paddlecraft separation]] — craft drifts away, paddler remains
- [[Helicopter hoist]] — recovery phase
- [[Cold weather performance]] — battery and electronics in cold water
- [[One Hand Activation]] — activation design
- [[Visibility range]] — tested distances
- [[USCG Rescue 21 Search Patterns]] — full Rescue 21 operational pipeline
- [[USCG SAR Doctrine]] — Coast Guard MOB response protocols