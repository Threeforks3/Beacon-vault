# USCG Rescue 21 and Search Patterns

Operational contribution from USCG surface search perspective. Describes the search planning pipeline and where the visual acquisition bottleneck occurs.

## Rescue 21

Rescue 21 is the Coast Guard's coastal VHF radio direction-finding system. Shore-based antenna arrays triangulate a mayday transmission to produce a position fix. This fix is at a specific moment in time — when the radio was keyed.

## The Drift Calculation

From the Rescue 21 fix, SAROPS calculates drift: wind, tide, current, sea state. The critical multiplier is **time** — how long until a surface unit can get on scene. Every minute of transit time increases the search area.

## Search Pattern Execution

A datum marker is dropped at the calculated drift point. The surface unit then runs timed turns forming standardized search patterns (expanding square, sector search, parallel track). Pattern selection is a function of time-to-on-scene and search object size.

## The Lookout Bottleneck

SAR lookouts on deck scan visually throughout the pattern. The entire system — triangulation, drift modeling, optimized pattern — converges on human eyes trying to acquire a target measured in centimeters in moving water.

- **Daylight, calm:** Human head visible at ~200 yards from a small boat deck
- **Daylight, 3-foot seas:** Visible intermittently at ~50-100 yards — lost in troughs
- **Night:** Effectively zero without active signaling. Search pattern covers miles; effective visual swath is zero.

## The Beacon Effect

Beacon changes the search object. The lookout is not searching for a human head. They are searching for an SOS strobe:

- White LED at 19,000+ mcd: visible from 2-3 nautical miles at night
- 850nm IR: visible through NVG at extended range, penetrates spray and light fog
- 360° dome: visible regardless of victim orientation
- 26-hour runtime: still flashing when the surface unit arrives, even after extended transit

**Effective search width goes from ~200 yards to ~6,000 yards.** The search pattern is unchanged — the probability of detection within it increases by orders of magnitude.

## Open Questions for USCG Partners

- At what range can a lookout positively identify an SOS strobe vs a navigation light?
- Does IR acquisition through NVG change search pattern selection? (Earlier acquisition = different pattern optimization)
- What is the current probability of detection for a person in water without active signaling vs with a strobe? (SAROPS has these numbers)
- Can Rescue 21 direction-finding be supplemented by an IR-strobe-equipped target during SAREX?

## Related

- [[USCG SAR doctrine]]
- [[Man overboard at night]]
- [[Capsize in open water]]
- [[IR beacon capability]]
- [[Visibility range]]
