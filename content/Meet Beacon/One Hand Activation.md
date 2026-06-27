---
title: "One-Hand Activation"
type: reference
tags:
  - beacon/design
  - interface/button
created: 2026-06-27
status: active
agent-note: true
agent-model: deepseek-v4-pro
agent-timestamp: 2026-06-27T14:00:00
# One-Hand Activation

Beacon uses a single-button press-and-hold interface. Press and hold for 2 seconds to activate. The button is tactile — a raised dome findable by feel in complete darkness, through gloves, with cold or wet hands.

## Design Constraints

**Who activates it:** The victim, who may be hypothermic, injured, exhausted, panicked, or unfamiliar with the device. A SAR professional might activate it in seconds. A civilian in their first emergency might take minutes. The interface must work for both.

**Under what conditions:** Darkness, cold water, gloved hands, high stress, possibly one-handed (the other hand injured or occupied). No screens to read, no sequences to memorize, no modes to cycle through accidentally.

**Failure modes:** Accidental activation in a pack drains the battery. Failure to activate when needed costs lives. The 2-second press-and-hold balances these: deliberate enough to prevent pocket activation, simple enough that a panicked user can discover it by feel.

## Tactile Design

The button is a raised dome — the only protrusion on an otherwise smooth cover surface. A user running their thumb across the device in darkness finds the button immediately. No other controls exist — there is only one thing to press.

The press force is calibrated for deliberate activation: firm enough to prevent accidental press, light enough for cold-weakened fingers. Glove compatibility tested with: neoprene paddling gloves, ski gloves, USCG rescue gloves, bare cold-wet hands.

## Stuck-Button Timeout

If the button is held down continuously (e.g., compressed in a packed bag), Beacon activates normally. After 30 minutes of continuous button press, the firmware enters timeout — the device deactivates and will not reactivate until the button is released and pressed again. This prevents accidental battery drain during storage or transport.

## Open Questions

- What activation method do SAR professionals prefer for rapid deployment?
- Should there be a "panic mode" — one-tap activation — for life-critical scenarios?
- Is 2 seconds the right hold time? (Field testing with cold-water subjects would validate)

## Related

- [[Stuck-button timeout]] — accidental drain prevention
- [[Battery life targets]] — runtime implications of early activation