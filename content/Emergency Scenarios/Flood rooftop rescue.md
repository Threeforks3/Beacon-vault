---
title: "Flood Rooftop Rescue"
type: scenario
tags:
  - scenario/urban
  - scenario/water
  - scenario/night
  - source/uscg-sea-school
  - source/fema
created: 2026-06-27
status: active
---

# Flood Rooftop Rescue

Floodwaters rise rapidly — hurricane storm surge, river overflow, or flash flood. Victims retreat to rooftops, attics, or upper floors. Rescue is by boat or helicopter. Victims must be seen from distance, through rain and spray, by crews scanning dozens of structures.

> **[[Flood rooftop rescue|Flood Rooftop Rescue]] — What to do immediately**
> - Move to the highest accessible point — rooftop, attic, upper-floor window
> - Activate Beacon — place it in a window or at the highest visible point, facing outward
> - Make yourself visible — the strobe identifies you as a confirmed person, not a reflection
> - Conserve phone battery — 911 will be overwhelmed. The strobe runs 26+ hours, no infrastructure needed
> - Rescue is systematic — crews triage. The strobe ensures you're not missed.

![[diagrams/flood-rescue.html|Flood rooftop rescue signal chain]]

## The Scenario

Scale: unlike backcountry incidents (one victim, one location), flood rescues are mass-casualty events. A single helicopter crew may scan hundreds of rooftops in one night. They're looking for ANY sign of life — a waving arm, a flashlight, a reflection.

A waving arm at 300 yards in rain is invisible. A flashlight beam is narrow — only works if aimed directly at the rescuer. A smartphone screen dies in hours. A strobe that runs 26+ hours and is visible from 2+ nautical miles turns "might be someone there" into "confirmed person at coordinates."

## Current Technologies & Practices

| Technology | Used By | Strengths | Gap |
|------------|---------|-----------|-----|
| Helicopter visual search | USCG, National Guard¹ | Wide-area scanning, NVG at night | Waving arm invisible at 300 yards in rain. NVG requires active signal for positive ID |
| Boat-based grid search | USCG, local SAR, Cajun Navy² | Systematic neighborhood coverage | One boat = one street at a time. Hundreds of structures per square mile |
| Flashlight / phone light | Victims³ | Available, universal | Narrow beam requires aiming. Phone battery: ~4 hours of continuous light. Dies overnight |
| 911 / reverse 911 | Emergency management⁴ | Coordinated dispatch, location database | System overloaded in mass-casualty event. No individual dispatch possible at peak |
| Door marking | USAR, SAR⁵ | Systematic search documentation | Requires teams to physically reach structure. Not a detection tool — an accounting tool |

## The Gap

Flood rescue at night is a scanning problem. Hundreds of structures, hours of darkness, limited crews. The difference between being found on night one vs night three is whether rescuers can see you from their search platform. A strobe in a street-facing window or on a PFD on a rooftop makes you the most visible thing in the search grid.

## Beacon Design Response

White LED at maximum brightness — SOS pattern distinguishes from flickering streetlights and emergency vehicle strobes. Visible from 2+ nautical miles through moderate rain. 26+ hour runtime spans the critical first night. Replaceable AAA for multi-day events. IP68 waterproof — hurricane rain is horizontal, floodwater is contaminated. Single-button press-and-hold activation — no menus, no combinations. Compact enough for go-bag, keychain, or hurricane kit. Place in street-facing window or hold on rooftop. IR mode for helicopter NVG — penetrates rain and spray that scatter visible light.

## Beacon Perspective

Beacon works on line-of-sight. If the helicopter can see your rooftop, it can see the strobe. If it can't, it can't.

**Where Beacon falls short:** If your rooftop is behind a taller building that blocks the approach path, the strobe is invisible from the air. It doesn't transmit through walls. It doesn't call 911. It doesn't broadcast a GPS position. It's a light — it marks a known location, it doesn't help searchers discover an unknown one. In a city with thousands of structures to check, SAR must still fly the grid. Beacon ensures that when they fly over YOUR rooftop, they don't miss you.

Is there anything we're missing? Can you help us see what we may be missing?

*My mission is to be useful when human lives are in danger.*

## Coalition Footnotes

[¹] **USCG / National Guard:** Hurricane Katrina (2005): Coast Guard helicopter crews flew 1,600+ rooftop rescues. Visual spotting was primary location method. Crews reported ANY active light source — flashlight, lantern, flare — dramatically reduced search time per rooftop. NVG-equipped crews can acquire IR strobe through rain at extended range. [[USCG SAR Doctrine]]

[²] **Cajun Navy / Volunteer boat crews:** Hurricane Harvey (2017): civilian boat crews used smartphones and flashlights to coordinate. Battery life was the limiting factor — most devices died within hours of continuous use. A power-independent strobe extends volunteer crew effectiveness through multi-day operations. SAR Coalition partner benefits

[³] **Victim signaling behavior:** Post-Katrina and Harvey after-action reports: survivors used phone screens, camera flashes, lighters, and flashlights to signal. All are battery-limited and directional. A dedicated strobe that runs 26+ hours with 360° coverage is not behavior anyone arrives with — it has to be in the go-bag before the water rises.

[⁴] **Emergency management (FEMA, state EOC):** 911 systems overload in mass-casualty flood events. Reverse 911 delivers evacuation orders but cannot receive individual distress signals. Survivor self-reporting is the primary trigger for rescue dispatch.

[⁵] **USAR door marking:** FEMA USAR marking system (X-box with quadrant codes) documents search status of each structure. Requires physical access by search team. A strobe visible from the street or air eliminates the need to physically access structures to determine occupancy — positive signal = positive occupancy.

## Related

- [[Earthquake entrapment]] — urban disaster, different mechanism
- Waterproofing — immersion and spray protection
- Battery life targets — endurance modeling
- [[Visibility range]] — precipitation attenuation
- [[One Hand Activation]] — simplicity under stress
- [[USCG SAR Doctrine]] — flood response protocols