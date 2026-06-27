# Man Overboard at Night

A person falls from a vessel into dark water. The vessel may not immediately know. They surface alone, drifting, with only what's attached to them.

## The Scenario

The critical factor: time. A person overboard at night is not just hard to find — they're drifting while the search area expands. Every minute without a signal means a larger search grid.

Cold water shock — gasp reflex, disorientation, rapid heat loss. In water below 15°C (59°F), functional swimming time is under 30 minutes. Hypothermia reduces the ability to wave, shout, or actively signal. The strobe must work without ongoing user action.

## Current Technologies & Practices

| Technology | Used By | Strengths | Gap |
|------------|---------|-----------|-----|
| Rescue 21 + SAROPS | USCG¹ | Triangulated mayday fix, drift modeling, optimized search pattern | Pattern converges on human lookouts — effective search width ~200yd daylight, ~0yd night |
| EPIRB/PLB | COSPAS-SARSAT² | GPS position, global satellite coverage | Minutes to alert, no continuous visual marking, requires registration |
| Strobe light | MRA, NASAR³ | Visible, waterproof, recognized pattern | White only, no IR, typical 8h ceiling |
| VHF radio | USCG Ch.16⁴ | Voice communication, Rescue 21 triangulation | Lost with vessel, submerged, dead battery |
| Search aircraft FLIR | USCG, CAP⁵ | Thermal detection from altitude | Water surface temperature masks body heat; spray degrades signature |
| Signal mirror | Universal | Daylight passive, infinite endurance | Useless at night; requires sun and skill |

## The Bottleneck

The entire search pipeline — triangulation, drift calculation, optimized search pattern — converges on human lookouts scanning water from a moving deck. The system is precise until the final step, which is visual acquisition of a 30cm target in moving water. At night, the search pattern covers miles while the effective visual swath is zero.

## Beacon Design Response

SOS strobe at 19,000+ mcd white + 850nm IR. The SOS pattern is internationally recognized — no navigation light, shore marker, or recreational light flashes SOS. 26h runtime from CR123A lithium. Bar-mounted to PFD webbing — rides at the highest point when floating. 360° dome visible from directly above (hoist operator perspective) and from surface vessels. Single-button press-and-hold activation — deliberate enough to prevent pocket activation, simple enough for cold, wet hands. Through-hole assembly survives water impact at terminal velocity. Stuck-button timeout prevents accidental drain.

**Beacon changes the search object.** The lookout is not searching for a human head. They are searching for an SOS strobe visible from 2-3 nautical miles at night. Effective search width goes from ~200 yards to ~6,000 yards. The search pattern is unchanged — probability of detection within it increases by orders of magnitude.

## Coalition Footnotes

[¹] **USCG Rescue 21:** Shore-based VHF direction-finding antenna arrays triangulate mayday transmissions. SAROPS calculates drift (wind, tide, current) based on time-to-on-scene. Surface unit drops datum marker, runs timed turns in standardized search pattern. Lookouts scan visually throughout. The entire system is engineered to put a vessel in the right place — but final acquisition is unaided human vision against water.

[²] **COSPAS-SARSAT:** MEOSAR detection in 5-10 minutes from activation. Requires registered beacon, unobstructed sky view, functional GPS lock. Position transmitted to rescue coordination center — not to on-scene assets directly. No continuous visual marking after alert.

[³] **MRA field equipment guide:** Minimum personal signaling kit = strobe + whistle + signal mirror. NASAR equivalent recommendations for ground and water search.

[⁴] **USCG:** VHF Ch.16 monitored continuously. Rescue 21 triangulation on transmission. MOB is typically separated from vessel and radio within seconds of fall.

[⁵] **Civil Air Patrol:** FLIR-equipped aircraft fly search grids. Thermal signature of human head in water is within 1-2°C of surrounding water — difficult discrimination in spray or chop.

[⁶] **USCG Sea School — Predicted Survival Time (Table 3-3):** In 50°F water: 1.5h floating without flotation, 4.0h in HELP posture or huddle with flotation. "Contrary to popular belief, the survivor should not swim around in efforts to keep warm. This will only increase the rate of heat loss and speed the onset of hypothermia." Core temperature at 95°F: mental confusion, impairment of rational thought, drowning possible. At 91°F: 50% do not survive. [[USCG Sea School - Rescue and Survival Procedures]]

[⁷] **USCG Sea School — Darkness Protocol:** "In hours of darkness, it becomes critical that the appropriate signaling devices are employed. During hours of darkness, flares and lights are crucial when these vessels are near." The USCG survival doctrine explicitly identifies darkness as the condition where active signaling becomes the critical survival factor. [[USCG Sea School - Rescue and Survival Procedures]]

[⁸] **USCG Sea School — Standard Strobe Spec:** The USCG-issued boat crew survival vest strobe: 50-70 flashes per minute, 8h minimum / 18h typical runtime, 2-5 mile visual range, white LED, hook-and-loop attachment to PFD or helmet. Beacon exceeds every parameter: SOS pattern (vs generic strobe), 26h runtime (vs 8h min), 850nm IR mode for NVG operations, bar-based attachment to any webbing (vs hook-and-loop to specific surfaces). [[USCG Sea School - Rescue and Survival Procedures]]

## Related

- [[Capsize in open water]] — multi-person variant
- [[Helicopter hoist]] — recovery phase
- [[Cold weather performance]] — battery and electronics in cold water
- [[One-hand activation]] — activation design
- [[Visibility range]] — tested distances
- [[USCG Rescue 21 and search patterns]] — full Rescue 21 operational pipeline
- [[USCG SAR doctrine]] — Coast Guard MOB response protocols
