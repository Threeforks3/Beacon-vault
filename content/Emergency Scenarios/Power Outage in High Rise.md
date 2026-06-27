---
title: "Power Outage in High-Rise"
type: scenario
tags:
  - scenario/urban
  - source/fema
  - source/ibc
  - source/nfpa
created: 2026-06-27
status: active
# Power Outage in High-Rise

A blackout hits a major city. High-rise buildings lose power — elevators stop, stairwells go dark, emergency lighting runs on battery backup for 90 minutes. Residents who are elderly, disabled, or with young children are trapped on upper floors. First responders are overwhelmed.

> **[[Power Outage in High Rise|High-Rise Blackout]] — What to do immediately**
> - Place Beacon in a street-facing window — the SOS pattern is visible from the street even through glass
> - If you must descend stairs, attach Beacon to your clothing — it lights the stairwell and marks your movement
> - 911 will be overwhelmed. The strobe tells first responders "person here" without a phone call
> - Check on neighbors — one Beacon in a window can mark an entire floor
> - Conserve phone battery — 911 will be overwhelmed. The strobe runs 26+ hours, no infrastructure needed

![[diagrams/power-outage-rescue.html|Power outage high-rise rescue signal chain]]

## The Scenario

This is the urban equivalent of being lost in the wilderness — trapped in a known location that no one can reach. After Hurricane Sandy (2012), some high-rise residents in New York City were without power and elevator service for over a week. Elderly residents on upper floors were effectively imprisoned — unable to descend 20+ flights of stairs, reliant on neighbors or responders for food, water, and medical needs.

## Current Technologies & Practices

| Technology | Used By | Strengths | Gap |
|------------|---------|-----------|-----|
| 911 / emergency calling | Universal¹ | Direct line to dispatch | System overloaded in widespread blackout. Non-life-threatening needs deprioritized |
| Emergency lighting | Building code required² | 90-minute battery backup in stairwells | 90 minutes. Blackouts last days. Residents in units, not stairwells — no benefit |
| Cell phone | Universal³ | Communication, flashlight | Battery dies in 1-2 days without charging. Network congestion or tower power loss |
| Fire department wellness check | FDNY, municipal FD⁴ | Door-to-door check of vulnerable residents | Labor-intensive. One crew = one building. Thousands of buildings |
| Battery lantern / flashlight | Prepared households⁵ | Portable light, multi-night runtime | Requires preparedness. Not a signal — a light. Must be aimed at rescuer |

## The Gap

In a prolonged urban blackout, the problem isn't navigation — it's triage. First responders cannot check every unit in every high-rise. They need to know which windows contain people who need help. A strobe in a street-facing window is a visual flag: "someone in this unit needs assistance." It doesn't require infrastructure, phone service, or battery recharging. It runs for 26+ hours — spans the entire blackout event.

## Beacon Design Response

Place Beacon in a street-facing window and activate. The SOS strobe is visible from street level — even through window glass. A first responder or neighbor scanning a building facade sees a distinctive distress signal among dark windows. SOS pattern distinguishes from flickering emergency lights or candles. 26+ hour runtime. Replaceable AAA — keep spares in the emergency kit. Single-button activation: press and hold 2 seconds. Compact — smaller than a deck of cards, lives in a kitchen drawer or emergency kit.

## Beacon Perspective

Beacon requires line-of-sight to the street. If your window faces an alley, courtyard, or air shaft, it's invisible to first responders scanning the facade.

**Where Beacon falls short:** It doesn't transmit through walls. It doesn't call 911. It doesn't tell anyone which floor you're on — just that there's an SOS strobe in that window. In a building with a thousand dark windows, SAR must notice yours. If the window is above the 10th floor and the search helicopter flies at rooftop level, the angle may obscure the strobe. It's a light in a window — not a radio, not a phone, not a location beacon.

Is there anything we're missing? Can you help us see what we may be missing?

*My mission is to be useful when human lives are in danger.*

## Coalition Footnotes

[¹] **Municipal emergency management:** 911 systems designed for individual emergencies, not mass-casualty infrastructure failures. Widespread blackout creates call volume that exceeds dispatch capacity. Non-life-threatening needs (food, water, medication, mobility assistance) are triaged below life-safety calls.

[²] **International Building Code (IBC) / NFPA 101:** Emergency lighting required in exit stairwells with 90-minute battery backup. No requirement for in-unit emergency signaling. Residents in their units — not in stairwells — receive no benefit from emergency lighting.

[³] **Telecom infrastructure:** Cell towers have backup power (typically 4-8 hours of battery, some with generators). Extended blackouts exhaust tower backup. Network congestion from spike in usage degrades service even when towers are powered.

[⁴] **FDNY / municipal fire departments:** Wellness checks for vulnerable populations (elderly, disabled, medically dependent) during extended outages. Door-to-door, labor-intensive. A visible signal from the street — "this unit needs help" — allows triage before committing crews to specific buildings.

[⁵] **Household preparedness (FEMA Ready.gov):** Recommended emergency kit includes flashlight, batteries, radio, food, water. Gap: no signaling device for urban entrapment. A strobe in the window is not in the standard kit — but it fills the gap between "I have supplies" and "rescuers know I need help."

## Related

- [[Earthquake entrapment]] — urban disaster, different mechanism
- [[Flood rooftop rescue]] — elevated victim, visual search
- [[Battery life targets]] — extended blackout endurance
- [[One Hand Activation]] — accessibility design
- [[Visibility range]] — street-level visibility through glass
- [[REACT International]] — emergency communications