---
title: "Coastal Fog Navigation"
type: scenario
tags:
  - scenario/water
  - scenario/day
  - source/uscg-sea-school
  - source/imo
  - source/aca
created: 2026-06-27
status: active
---

# Coastal Fog Navigation

Thick fog rolls in along a coastline. Vessels — commercial fishing boats, recreational sailboats, kayaks — are navigating by GPS but invisible to each other. A vessel in distress or adrift is a collision hazard and a search challenge.

> **[[Coastal fog navigation|Coastal Fog]] — What to do immediately**
> - Activate Beacon — the wide hemispherical beam cuts through fog better than a narrow beam
> - The SOS pattern distinguishes you from navigation lights — other vessels will recognize a distress signal
> - Sound signals are unreliable in fog — the strobe provides a second signaling modality
> - 360° coverage means you're visible regardless of vessel orientation
> - Conserve phone battery — 911 will be overwhelmed. The strobe runs 26+ hours, no infrastructure needed

![[diagrams/coastal-fog-rescue.html|Coastal fog rescue signal chain]]

## The Scenario

Fog is the most dangerous weather condition for maritime navigation — more lethal than storms, more disorienting than darkness. Sound is unreliable (fog distorts and reflects sound waves). Radar shows large vessels but misses kayaks and small craft. AIS is only on commercial vessels. A small craft in fog is invisible until collision is imminent — and invisible to SAR assets if they capsize or lose power.

## Current Technologies & Practices

| Technology | Used By | Strengths | Gap |
|------------|---------|-----------|-----|
| Radar | Commercial vessels, USCG¹ | Detects large targets through fog | Misses kayaks, SUPs, small sailboats — no radar signature |
| AIS | IMO SOLAS vessels² | Vessel identity + GPS position broadcast | Recreational vessels exempt; no distress signaling function |
| Sound signals | USCG Navigation Rules³ | Horn/whistle required on all vessels | Fog distorts sound — direction unreliable at distance |
| GPS/chartplotter | Recreational boaters⁴ | Own-position awareness, route tracking | Shows where YOU are; doesn't show others where you are |
| VHF radio | USCG, all vessels⁵ | Voice communication, mayday, Rescue 21 triangulation | Requires functioning radio, antenna, and battery |

## The Gap

In fog, a small vessel is invisible to radar and AIS. Sound signals are unreliable. If the vessel loses power — engine failure, capsize, dead battery — it has no active signal at all. It becomes a silent, invisible object adrift in a shipping lane or search area.

## Beacon Design Response

Domed lens produces wide hemispherical beam — diffuse enough to minimize backscatter in fog, bright enough to be visible from surface vessels. SOS pattern distinguishes it from navigation lights. 360° coverage regardless of vessel orientation. 26+ hour runtime spans persistent fog events. Waterproof to IP68. Manual activation — works without vessel power.

## Beacon Perspective

Fog attenuates light exponentially. Beacon's visible range drops from miles to hundreds of yards in dense fog. It's a close-range terminal homing signal in these conditions — not a long-range detection tool.

**Where Beacon falls short:** No radar reflector. No AIS transmitter. It doesn't make a kayak visible to ship radar — only to human eyes. In thick fog, line-of-sight is short and the strobe won't reach a vessel that isn't already close. A VHF radio with DSC can alert every vessel in range — Beacon can't. It's a visual signal, and fog is the condition that most aggressively defeats visual signals.

Is there anything we're missing? Can you help us see what we may be missing?

*My mission is to be useful when human lives are in danger.*

## Coalition Footnotes

[¹] **USCG Vessel Traffic Service:** Radar surveillance of major ports and shipping lanes. X-band and S-band radar detect vessels >20ft reliably. Kayaks, SUPs, and small sailboats have radar cross-sections smaller than sea clutter — invisible to VTS radar. [[USCG SAR Doctrine]]

[²] **IMO SOLAS:** AIS carriage required on vessels >300 GT internationally, >65ft in US. Creates a two-tier visibility system: commercial vessels see each other; recreational vessels see neither each other nor commercial traffic. [[IMO standards]]

[³] **USCG Navigation Rules:** Rule 35 — sound signals in restricted visibility. Power-driven vessel underway: one prolonged blast every 2 minutes. But sound propagation in fog is unpredictable — refraction layers bend sound, creating shadow zones. [[USCG SAR Doctrine]]

[⁴] **ACA / Paddlesports:** Recreational paddlers navigate by GPS and visual reference. In fog, GPS provides position but not collision avoidance. Paddler is invisible to other vessels and cannot see them approaching. [[SAR Coalition partner benefits]]

[⁵] **USCG:** VHF Ch.16 monitored continuously. Rescue 21 triangulation on transmission. But small craft in fog may not recognize distress in time to radio, or may lose electrical power before transmitting. [[USCG Rescue 21 Search Patterns]]

## Related

- [[Capsize in open water]] — vessel distress scenario
- [[Visibility range]] — fog attenuation
- [[Waterproofing]] — moisture protection
- [[Strobe vs Constant On]] — signal pattern rationale
- [[USCG SAR Doctrine]] — maritime SAR protocols