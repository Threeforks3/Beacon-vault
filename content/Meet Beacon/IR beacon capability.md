---
title: "IR Beacon Capability"
type: reference
tags: [beacon/capability, equipment/signal, technology/ir]
created: 2026-06-25
updated: 2026-06-27
status: active
agent-note: true
agent-model: deepseek-v4-pro
agent-timestamp: 2026-06-27T14:00:00
---

# IR Beacon Capability

Beacon emits on two channels simultaneously: visible white light for the naked eye, and 850nm near-infrared for electronic sensors. Silicon sees what the eye cannot. The IR signal is detected by night vision goggles, FLIR systems, digital cameras, smartphone sensors, drone cameras, security cameras, digital night scopes, and range finders — essentially every CCD and CMOS sensor fielded today. This turns every electronic eye in the area into a detection surface.

## Why IR Matters

**The NVG reality:** Coast Guard MH-60T Jayhawk crews fly with AN/AVS-9 night vision goggles. Military SAR helicopters use ANVIS-9. These systems are sensitive in the 600-900nm range — the TSHG6400's 850nm peak sits directly in their sweet spot.

**Visible vs IR tradeoff:** A white strobe is visible to the naked eye — good for surface vessels, ground teams, and civilian aircraft. But it also illuminates the scene, degrades the victim's night vision, and can be confused with other light sources. An IR strobe is invisible — it doesn't blind the victim, doesn't attract unwanted attention, and is uniquely identifiable as a distress signal through NVG. Beacon can do both.

**The detection advantage:** Through NVG, an IR strobe at 850nm appears as a brilliant flashing point source against a dark background. At 2-3 nautical miles from altitude, it's unmistakable. This provides early positive identification — search crews can acquire the victim before entering visual range, plan their approach, and reduce hover/search time.

## Technical

**LED:** Vishay TSHG6400, 5mm through-hole, 850nm peak wavelength, ±22° half-angle. Drive current: 29mA at 5.0V boost via 120Ω resistor.

**Visibility through obscurants:** IR penetrates light fog, dust, and snow better than visible light. This is why military systems use IR for target acquisition in degraded visual environments. For SAR, this means the IR strobe remains visible through rotor wash spray, snow dust, and light precipitation that scatters visible light.

**NVG compatibility:** Standard aviation NVG (AN/AVS-9, ANVIS-9) can be damaged by bright visible lights — they have automatic gain control, but a direct white strobe at close range can temporarily bloom the image. IR mode eliminates this risk: the strobe is bright through NVG but emits zero visible light. Crews can stare directly at the strobe for positive identification without degrading their night vision adaptation.

## Operational Use

- **Helicopter hoist:** Hoist operator acquires IR strobe through NVG before aircraft reaches hover position
- **Aircraft ditching:** Life raft IR strobe visible to search aircraft through NVG at extended range
- **Night overboard:** IR strobe on PFD is visible to Coast Guard NVG-equipped aircraft while the victim maintains dark adaptation
- **Avalanche:** IR penetrates snow dust that scatters visible light — surface marker visible through NVG from search aircraft

## Related

- [[IR detection surfaces]] — physics of CCD/CMOS sensitivity and sensor catalog
- [[Helicopter hoist]] — primary IR use case
- [[Aircraft ditching]] — oceanic IR search
- [[Strobe vs Constant On]] — signal pattern rationale
- [[Visibility range]] — tested distances for IR