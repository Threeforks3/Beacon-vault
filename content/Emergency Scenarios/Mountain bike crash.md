---
title: "Mountain Bike Crash"
type: scenario
tags:
  - scenario/land
  - source/imba
created: 2026-06-27
status: active
# Mountain Bike Crash

A mountain biker crashes on remote singletrack — broken collarbone, concussion, or too injured to ride out. No cell service. No one knows which trail they took. They're 10+ miles from the trailhead, possibly off the trail entirely.

> **[[Mountain bike crash|Bike Crash]] — What to do immediately**
> - Assess injuries before moving — spinal injuries are common in bike crashes
> - Activate Beacon — thread onto hydration pack strap or hang from a branch above your position
> - Stay on or near the trail if possible — SAR searches trail corridors first
> - The strobe is visible through partial canopy from aircraft — it's your best signal if you can't move
> - 26+ hour runtime spans the critical window: dusk → SAR activation at dawn → search grid in progress

![[diagrams/mtb-crash-rescue.html|Mountain bike crash rescue signal chain]]

## The Scenario

Mountain biking combines speed, isolation, and injury risk. A crash at 20+ mph in remote terrain can produce injuries that make self-extraction impossible. Even a sprained ankle means a 10-mile walk out becomes a multi-hour ordeal. Night falls. Temperature drops. The rider is stationary, in pain, difficult to spot from the air through tree canopy.

## Current Technologies & Practices

| Technology | Used By | Strengths | Gap |
|------------|---------|-----------|-----|
| Cell phone | Universal¹ | GPS location, camera, communication | No service on most trails. Battery drains fast in cold and with GPS use. Screen dies on impact |
| Trailforks / MTB Project | Mountain bikers² | Trail maps, route planning, offline maps | Shows where YOU are; doesn't signal anyone else. Phone-dependent |
| Riding buddy | Group riders³ | Immediate assistance, can ride out for help | Solo riders have no buddy. Separated group may not realize rider is missing |
| InReach / SPOT | Backcountry riders⁴ | Satellite SOS + two-way messaging | $300+ + subscription. Minority carry. Device may be in pack, not accessible after crash |
| Whistle | Race required⁵ | Audible signal, no battery | 0.1 mile range. Unconscious rider can't use it |

## The Gap

A solo mountain biker who crashes and can't self-extract has hours before anyone knows they're missing. Then hours more before SAR locates them. Through tree canopy at night, they're invisible. A strobe on their pack or person — activated with one hand after a crash — changes the search from "grid search 50 miles of singletrack" to "fly toward the flashing light."

## Beacon Design Response

Through-hole components wave-soldered to single PCB — no SMD to shear under crash G-loading. Polycarbonate cover absorbs impact without cracking. Bar-based attachment threads onto hydration pack shoulder strap or hip belt — stays with rider through crash. White SOS strobe visible through partial canopy at night. Under 70g — lighter than a spare tube. 26+ hour runtime. Single-button activation — usable one-handed after injury.

## Beacon Perspective

Beacon doesn't activate on impact. No accelerometer, no automatic trigger. If you're knocked unconscious, it stays dark.

**Where Beacon falls short:** In a crash with loss of consciousness, Beacon can't activate itself. It doesn't call 911. It doesn't transmit GPS coordinates. Someone must know your route and notice you're overdue. Under dense canopy, the strobe is visible from the air only through gaps — a helicopter might fly directly overhead and miss it if the canopy is solid. It's a visual signal, not a radio signal. Line-of-sight only.

Is there anything we're missing? Can you help us see what we may be missing?

*My mission is to be useful when human lives are in danger.*

## Coalition Footnotes

[¹] **IMBA (International Mountain Bicycling Association):** Trail advocacy and rider education. Ride preparation guidance includes tool kit, first aid, and communication device. Gap: no dedicated emergency signal in standard ride kit. Cell phone is default but unreliable in backcountry. [[SAR Coalition partner benefits]]

[²] **Trailforks / Outside Interactive:** Trail database used by majority of mountain bikers. Offline maps reduce navigation errors but don't solve the signaling problem. Integration opportunity: Beacon as recommended emergency equipment in trail database.

[³] **Group ride culture:** Riding in groups is standard safety practice. But group separation happens — faster riders ahead, mechanical issues, wrong turn at intersection. Rider left behind may not be missed until trailhead regroup — hours later.

[⁴] **Satellite messengers:** Growing adoption among enduro and backcountry riders. Same limitations as hunting use case: cost, subscription, device accessibility after crash. Beacon complements — no subscription, always on person, one-button activation when satellite messenger is in pack and unreachable.

[⁵] **Enduro / DH race requirements:** Whistle required for some race categories. Recognizes the communication gap but offers a tool with 0.1 mile effective range. Strobe provides 2+ mile visual range — orders of magnitude improvement.

## Related

- [[Wilderness lost hiker]] — similar terrain, different activity
- [[Impact resistance]] — crash survival
- [[Bar-based attachment]] — pack mounting
- [[One Hand Activation]] — post-crash usability