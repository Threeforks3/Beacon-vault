---
title: "Swift Water Rescue"
type: scenario
tags:
  - scenario/water
  - scenario/land
  - scenario/day
  - scenario/night
  - source/nfpa
  - source/aca
  - source/uscg-sea-school
created: 2026-06-27
status: active
---

# Swift Water Rescue

Fast-moving water — river, flood channel, dam release — sweeps a victim downstream. They may be pinned against an obstacle, trapped in a hydraulic, or carried faster than they can self-rescue. Shore-based rescue teams must track the victim's position as they move downstream.

> **[[Swift water rescue|Swift Water]] — What to do immediately**
> - Activate Beacon — attach to PFD shoulder for maximum visibility above water
> - The strobe survives repeated submersion — IP68 waterproof to 2 meters
> - Shore-based rescuers track the flash pattern through spray and whitewater — continuous visual lock
> - Defensive swimming: feet up, facing downstream. The strobe on your PFD marks your position for throw-bag rescuers
> - Conserve energy. Do not fight the current — float feet-up, use the strobe to signal your position

![[diagrams/swiftwater-rescue.html|Swift water rescue signal chain]]

## The Scenario

Swift water is deceptive. Water moving at 6 knots exerts more force than a person can stand against. At 10 knots, it can sweep vehicles off roads. Victims are carried hundreds of yards per minute. Shore-based rescuers must track a moving target through spray, debris, and changing river features.

A victim's head in whitewater is intermittently visible. Between waves, spray, and debris, the rescuer loses visual contact constantly. If the victim goes under — trapped in a hydraulic or pinned on a strainer — the search transitions from tracking to recovery.

## Current Technologies & Practices

| Technology | Used By | Strengths | Gap |
|------------|---------|-----------|-----|
| Visual tracking | Swift water rescue teams¹ | No equipment needed, immediate | Victim submerged in whitewater is invisible; tracking lost between waves |
| Throw bag | Universal² | 50-75ft reach from shore | Requires victim to be conscious, oriented, and able to grab rope |
| Rescue PFD | Swift water teams, paddlers³ | Keeps victim afloat, high-visibility color | Passive — rescuers must see the PFD. Whitewater obscures intermittently |
| Night vision | SAR teams⁴ | Extends visual tracking into darkness | Spray and whitewater opaque to NVG at close range; IR strobe punches through |
| Helicopter | USCG, SAR⁵ | Aerial tracking, hoist extraction | Victim must be positively identified before hoist; rotor wash complicates scene |

## The Gap

Swift water rescue depends on continuous visual contact. Lose sight of the victim for 30 seconds and the search area has expanded hundreds of yards downstream. At night or in heavy spray, visual contact is impossible. An active strobe on the victim's PFD provides continuous positive position — the rescuer tracks the flash pattern even through spray and momentary submersion.

## Beacon Design Response

IP68 waterproofing handles repeated submersion in swift water. Bar-based closed-slot attachment stays on PFD webbing through hydraulic forces and debris impact. White LED at maximum brightness cuts through spray and whitewater. IR mode for helicopter NVG tracking from altitude — visible through rotor wash spray. Single-button activation usable with cold, wet, gloved hands. 26+ hour runtime — extends tracking window through multi-hour operations.

## Beacon Perspective

Beacon is a surface signal. In swift water, the surface is sometimes where you are, and sometimes not.

**Where Beacon falls short:** In aerated water — whitewater, hydraulic recirculation — bubbles scatter the strobe's light and reduce effective visibility compared to clear water. If the victim goes under a strainer, submerged log, or debris, the signal stops entirely — the lens is underwater. Beacon doesn't transmit a GPS track — it shows where you ARE at this moment, not where the current is taking you. Rescuers must maintain visual contact or reacquire. It's a point marker, not a tracking beacon.

Is there anything we're missing? Can you help us see what we may be missing?

*My mission is to be useful when human lives are in danger.*

## Coalition Footnotes

[¹] **Swift water rescue teams (NFPA 1006):** Technician-level training includes downstream victim tracking, throw bag deployment, and tethered swimmer rescue. Doctrine emphasizes maintaining visual contact. Gap acknowledged: no portable active strobe in standard swift water rescue kit. [[SAR Coalition partner benefits]]

[²] **ACA / American Whitewater:** Paddler safety curriculum includes throw bag use, self-rescue, and group rescue. Recommended equipment: PFD, helmet, throw bag, whistle. No strobe. Gap: paddler separated from group at dusk has no active signaling. [[SAR Coalition partner benefits]]

[³] **ASTM F2680:** Rescue PFD standard requires minimum 22 lbs buoyancy, high-visibility color, and reflective tape. Passive visibility only — works when rescuers are looking at you. Whitewater obscures intermittently.

[⁴] **SAR NVG operations:** Night vision extends tracking into darkness but whitewater spray creates near-field opacity at NVG wavelengths. IR strobe at 850nm penetrates spray better than visible light — a different detection modality that complements NVG.

[⁵] **USCG Helicopter Rescue:** Hoist from swift water requires positive visual ID. Rotor wash creates additional spray. IR strobe provides positive ID through spray at altitude. [[Helicopter hoist]]

## Related

- [[Man overboard at night]] — water rescue, different context
- [[Bar-based attachment]] — attachment force testing
- [[Waterproofing]] — IP68 design
- [[Impact resistance]] — debris impact survival
- [[IR beacon capability]] — NVG operations in degraded visual environments