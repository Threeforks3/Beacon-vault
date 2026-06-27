---
title: "Wilderness Lost Hiker"
type: scenario
tags:
  - scenario/land
  - scenario/night
  - source/mra
  - source/nasar
  - source/cap
  - source/uscg-sea-school
  - source/cospas-sarsat
  - source/bsa
created: 2026-06-27
status: active
---

# Wilderness Lost Hiker

A hiker, hunter, or backpacker is off-trail in remote terrain — no cell service, no trail markings, possibly injured. Daylight is fading. SAR has been notified, but the search area spans hundreds of square miles of forest, mountain, or desert.

> **[[Wilderness lost hiker|Lost Hiker]] — What to do immediately**
> - Stop moving. Stay put. "Hug a tree" — SAR searches from last known position outward
> - Activate Beacon — hang it from a branch, pack, or tent line at the highest visible point
> - The strobe penetrates partial canopy. At night, it's visible from 2+ miles from aircraft through tree gaps
> - Do not exhaust yourself shouting — the strobe does the signaling
> - 26+ hour runtime spans the critical window: dusk → SAR activation at dawn → search grid in progress

![[diagrams/lost-hiker-rescue.html|Lost hiker rescue signal chain]]

## The Scenario

The most common SAR mission type. Lost-person searches account for the majority of SAR callouts in every jurisdiction. Most resolve within 24 hours. The ones that don't — multi-day grid searches — are the ones where the victim had no way to signal.

A lost hiker without a signaling device relies on: shouting (range: 0.1 mile in forest), campfire (2-3 miles from air in clear conditions, dangerous in fire season), waving (invisible under canopy), signal mirror (requires direct sunlight — useless at night and under canopy).

## Current Technologies & Practices

| Technology | Used By | Strengths | Gap |
|------------|---------|-----------|-----|
| Ground search teams | MRA, NASAR¹ | Grid search, K9, tracking | Labor-intensive, slow. One team covers ~1 sq mile per day in dense terrain |
| Search aircraft (fixed-wing) | CAP, USCG² | Wide-area visual scanning | Looking for color and movement through canopy gaps — passive target |
| Helicopter FLIR | USCG, CAP, NPS³ | Thermal scanning from altitude | Tree canopy blocks IR; body heat indistinguishable from sun-warmed rocks by afternoon |
| Cell phone | Universal⁴ | Two-way communication, GPS coordinates | No service in wilderness search areas; battery dies in hours |
| Whistle | MRA recommended⁵ | Audible signal, lightweight, passive | Range 0.1 mile in forest; requires conscious, active victim |
| Signal mirror | Universal | Daylight passive, infinite endurance | Requires direct sunlight; useless at night, under canopy, in overcast |
| Personal Locator Beacon | COSPAS-SARSAT⁶ | 406 MHz satellite alert with GPS fix | Point-in-time fix — victim moves after activation. No strobe for homing. SAR gets within 1-3 NM, still must search visually. $250+, single-use mentality keeps it in pack. |

## The Gap

A lost hiker at night is invisible. Ground teams search by grid — slow, methodical, and dependent on the victim being in the grid cell being searched right now. A strobe visible from the air through canopy gaps changes the search from "grid until you stumble on them" to "fly toward the flashing light." The standard advice — hug a tree — becomes advice backed by a 2+ mile beacon hung from that tree.

## Beacon Design Response

Under 70g with 2x AAA — lighter than a multi-tool. 26+ hour continuous SOS spans the critical window: lost at dusk → SAR activation at dawn → search grid in progress → found. White LED at maximum brightness punches through partial canopy. SOS pattern distinguishable from campfire glimmer at 2+ miles. 2x AAA (alkaline standard, lithium optional for extreme cold). Bar-based attachment threads onto pack shoulder strap, belt loop, or hung from branch for elevated positioning. Single-button activation — the last thing a hypothermic hiker needs is a complex interface.

## Beacon Perspective

Beacon makes you findable. It doesn't tell anyone you need finding.

**Where Beacon falls short:** Beacon doesn't transmit GPS coordinates. It doesn't call for help. It's a visual signal — someone must already be searching. Under dense triple-canopy forest with no gaps to the sky, the strobe from above is invisible — it's visible only from ground level within the forest. A PLB or satellite messenger can send an SOS with your coordinates from anywhere with sky view — Beacon can't. They're complementary, not competing: the PLB starts the search, Beacon finishes it.

Is there anything we're missing? Can you help us see what we may be missing?

*My mission is to be useful when human lives are in danger.*

## Coalition Footnotes

[¹] **MRA (Mountain Rescue Association):** Volunteer mountain rescue teams in the US and Canada. Ground search is primary mission. Recommended personal equipment includes whistle, light source, extra clothing. Gap: recommended light source is a headlamp — directional, short-runtime, not designed for signaling. [[Mountain Rescue Association]]

[²] **CAP (Civil Air Patrol):** Fixed-wing search aircraft fly contour grids at 1,000-3,000ft AGL. Visual acquisition of a human figure through canopy is the primary detection method. An active strobe visible through canopy gaps dramatically increases detection probability. [[Civil Air Patrol]]

[³] **NPS (National Park Service):** 3,400+ SAR incidents in national parks annually. Most common: day hiker off trail. Most common missing equipment: light source. NPS helicopter operations include FLIR search — thermal signature of stationary human through canopy is minimal. Active strobe provides complementary detection modality. [[SAR Coalition partner benefits]]

[⁴] **Universal:** Cell phone is the default emergency device for most hikers. Relies on infrastructure that doesn't exist in wilderness search areas. Battery life is the second failure mode — GPS + screen use drains battery in hours. Beacon: power-independent, no infrastructure, 26+ hours.

[⁵] **BSA Outdoor Ethics / 10 Essentials:** Scouts are taught to carry flashlight and whistle. Gap: neither is visible from search aircraft. The 10 Essentials don't include a dedicated emergency strobe. [[SAR Coalition partner benefits]]

[⁶] **COSPAS-SARSAT:** PLBs transmit a 406 MHz distress signal with GPS position to the satellite network. The fix is a single point in time — the victim's location when the alert was sent. In water, a person drifts. On land, a lost hiker keeps walking. SAR arrives in the general area (1-3 NM) and must then search visually. PLBs have no integrated strobe — they alert, they don't home. Beacon closes the last mile: the satellite fix gets SAR nearby, the strobe gets them to you. [[COSPAS-SARSAT]]

## Related

- [[Avalanche burial]] — winter backcountry variant
- [[Mountain bike crash]] — similar terrain, different mechanism
- [[Hunting accident]] — wilderness with firearm involvement
- [[Cold weather performance]] — battery and electronics
- [[Bar-based attachment]] — pack mounting
- [[Mountain Rescue Association]] — wilderness SAR protocols