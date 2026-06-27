---
title: "Avalanche Burial"
type: scenario
tags:
  - scenario/land
  - scenario/snow
  - scenario/night
  - source/mra
  - source/aiare
  - source/recco
created: 2026-06-27
status: active
---

# Avalanche Burial

A backcountry skier, snowboarder, or snowmobiler is caught in an avalanche, carried downhill, and buried under snow. Time to live is measured in minutes. The victim is invisible from the surface.

> **[[Avalanche burial|Avalanche Burial]] — What to do immediately**
> - If you have an airbag, deploy it — stay on the surface if possible
> - Activate Beacon before impact if time allows — the strobe survives the ride
> - Create an air pocket in front of your face as the snow settles
> - If any equipment remains above the surface, the strobe marks your position
> - Companion rescue: transceiver search gets within 2-3m. The strobe provides the visual pinpoint when you break through.

![[diagrams/avalanche-rescue.html|Avalanche burial rescue signal chain]]

## The Scenario

The 15-minute window: survival probability drops sharply after 15 minutes of burial. After 35 minutes, survival is below 30%. Leading cause of death is asphyxiation — not trauma, not hypothermia. Speed of recovery is everything.

Avalanche transceivers (457 kHz) require the rescuer to have a compatible device, be within range, and know how to search. RECCO reflectors are passive — require a RECCO detector typically only carried by organized rescue and helicopters. An active strobe adds a complementary layer of detection.

## Current Technologies & Practices

| Technology | Used By | Strengths | Gap |
|------------|---------|-----------|-----|
| Avalanche transceiver (457 kHz) | Backcountry users, ski patrol¹ | Companion rescue in minutes, industry standard | Requires rescuer with compatible device + training. Buried deeper than 2m = signal weakens |
| RECCO reflector | Backcountry users² | Passive, no battery, helicopter-detectable | Requires RECCO detector — only carried by organized rescue. No companion rescue capability |
| Avalanche airbag | Backcountry users³ | Keeps victim near surface, reduces burial depth | Doesn't signal. Deployment is not guaranteed |
| Probe + shovel | Universal⁴ | Pinpoints burial depth, extraction | Requires transceiver or RECCO to get within probe range first |
| K9 search | Ski patrol, SAR⁵ | Scent detection, independent of electronics | Dogs and handlers not always immediately available. Time-critical scenario |
| Helicopter RECCO search | SAR, ski patrol⁶ | Wide-area detection from altitude | RECCO detector range ~200m from helicopter. Requires flyover of burial zone |
| Organised rescue | MRA, ski patrol⁷ | Systematic search, K9, RECCO | Response time 30+ minutes — outside the 15-minute survival window |

## The Gap

Avalanche rescue is layered: transceiver for companion rescue (minutes), RECCO for organized rescue (30+ minutes), K9 for extended search. Missing: a surface marker that works if any equipment remains above snow. If the victim's pack, ski pole, or any attached equipment stays above the surface, an active strobe turns that debris into a beacon visible to search aircraft with NVG — even through suspended snow dust.

## Beacon Design Response

2x AAA (alkaline standard, lithium AAA optional for -40°C — same form factor). Bar-based one-hand-detach with tether backup: bars may release under extreme tumble, tether retains. Through-hole components wave-soldered to single PCB — no SMD to shear under G-loading. Polycarbonate cover absorbs impact without cracking. 5mm LED domes inherently impact-resistant. IR strobe visible through NVG in snow dust conditions where white light scatters. Beacon is an ADDITIONAL layer — transceiver gets within 2-3 meters, probe pinpoints, strobe confirms when rescuers break through. Surface marking: if any attached equipment remains above snow, the strobe provides active signal to search aircraft.

## Beacon Perspective

Beacon is an additional layer in the avalanche rescue chain — the fourth after transceiver, RECCO, and K9. It won't replace any of them.

**Where Beacon falls short:** Beacon has no 457 kHz transceiver and no RECCO reflector. It doesn't help companion rescuers pinpoint burial depth — the transceiver does that. If Beacon is buried under 2m of snow with no equipment above the surface, it's invisible. There's no RF beacon, no RECCO reflector, no signal that penetrates consolidated avalanche debris. It only helps if it stays above the surface, or if rescuers are close enough to see the strobe through gaps in the snow.

Is there anything we're missing? Can you help us see what we may be missing?

*My mission is to be useful when human lives are in danger.*

## Coalition Footnotes

[¹] **AIARE / AAA:** Avalanche transceiver (457 kHz) is the standard companion rescue tool. All backcountry users expected to carry transceiver + probe + shovel. Industry standard: 3-antenna digital transceivers with marking function for multiple burials. Range: ~60m. Training required for effective search. [[Mountain Rescue Association]]

[²] **RECCO:** Passive reflector integrated into clothing and equipment. No battery. Detected by helicopter-mounted RECCO SAR detector at ~200m range. Limitation: requires organized rescue with detector — no companion rescue capability. Adopted by major outdoor brands (Patagonia, Arc'teryx, etc.).

[³] **Avalanche airbag manufacturers (ABS, BCA, Mammut):** Keeps victim near surface through inverse segregation — larger volume rises in flowing snow. Does not signal. Deployment reliability variable. Adds weight and cost.

[⁴] **Universal backcountry standard:** Probe for depth confirmation after transceiver search, shovel for extraction. Neither provides signaling. Beacon is a signaling complement to the probe/shovel — not a replacement.

[⁵] **SAR K9:** Avalanche dogs can search large areas quickly. Independent of electronics. Limitation: availability. Not every ski area or backcountry zone has immediate dog access. Time-critical scenario demands multiple detection layers.

[⁶] **Helicopter RECCO:** Organized rescue deploys RECCO detector on helicopter long-line. Effective for wide-area search. Detection range ~200m. Requires flyover of burial zone — if search area is misidentified, detector won't find victim.

[⁷] **MRA / Ski Patrol:** Organized avalanche rescue response. Systematic probe line search. Time to on-scene: 30+ minutes for backcountry, faster for in-bounds. Outside the 15-minute companion rescue window — emphasizes why companion rescue is primary. [[Mountain Rescue Association]]

## Related

- [[Cold weather performance]] — battery chemistry selection
- [[Bar-based attachment]] — multi-axis force testing
- [[IR beacon capability]] — NVG compatibility through snow dust
- [[Impact resistance]] — drop and crush testing
- [[Wilderness lost hiker]] — non-avalanche backcountry scenarios
- [[Mountain Rescue Association]] — backcountry SAR protocols