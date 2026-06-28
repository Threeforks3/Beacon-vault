---
title: "Battery Life Targets"
type: reference
tags:
  - beacon/design
  - power/battery
created: 2026-06-27
status: active
agent-note: true
agent-model: deepseek-v4-pro
agent-timestamp: 2026-06-27T14:00:00
---

# Battery Life Targets

Beacon's runtime is physics-governed — 2x AAA cell capacity divided by LED drive current. 26+ hours continuous SOS. Replaceable in seconds.

## Runtime Modeling

**Battery:** 2x AAA alkaline in series, 3.0V nominal. ~1,200mAh usable at 35mA drain.

**Load:** Two LEDs (white + IR) at 29mA each, interleaved operation — one LED on at any time, not simultaneous. Boost converter efficiency ~85%. Total average draw: ~35mA at 3.0V input.

**Runtime:** 1,200mAh / 35mA = 34 hours theoretical. Derate for voltage droop, temperature, and boost converter efficiency variation: 26+ hours conservative.

**Power budget analysis** (Gate G1, passed 2026-06-25): all parameters within MOSFET and boost converter operational limits. Peak switch current 464mA vs 600mA minimum spec — 77% margin.

## Scenario Mapping

| Runtime Need | Scenario | Beacon Coverage |
|-------------|----------|-----------------|
| 2 hours | Swift water rescue, helicopter hoist | 13× margin |
| 8 hours | Open water capsizes, man overboard | 3× margin |
| 24 hours | Flood rescues, oceanic ditching | Exceeds (26+) |
| 72 hours | Earthquake entrapment, extended blackout | Replaceable battery — carry spares |

## Replaceability

AAA is the most common battery in the world. Available at any gas station, supermarket, or convenience store. No proprietary battery, no charging infrastructure. In extended operations (multi-day flood rescue, oceanic search), carrying spare AAAs extends the signaling window indefinitely.

## Related

- Cold weather performance — alkaline vs lithium AAA
- [[Strobe vs Constant On]] — runtime impact of flash duty cycle