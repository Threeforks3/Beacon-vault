---
title: "Color Selection"
type: reference
tags:
  - beacon/design
  - enclosure/color
created: 2026-06-27
status: active
agent-note: true
agent-model: deepseek-v4-pro
agent-timestamp: 2026-06-27T14:00:00
# Color Selection

Beacon uses white light for visible signaling. No red, no blue, no green. The choice is driven by international signal conventions and SAR operational doctrine.

## Rationale

**White is the international distress color.** COLREGs specifies white for distress signaling. Red is port navigation. Green is starboard. Blue is reserved for law enforcement in many jurisdictions. Using white eliminates ambiguity.

**White maximizes luminous efficacy.** White LEDs (Cree C503D-WAN) produce more perceived brightness per watt than colored alternatives. For a battery-constrained device, white provides the longest visibility range per milliamp-hour.

**IR is the second color.** 850nm infrared is invisible to the naked eye but unmistakable through night vision. It's not a "color" in the visible sense but serves as a second signaling channel for NVG-equipped search assets.

## Open Questions

- Would a red option serve any SAR context? (Some jurisdictions use red for emergency vehicles)
- Does white create confusion with recreational lighting? (Campers, boaters, cyclists all use white lights)
- Should the IR LED have a different flash pattern to distinguish it from the white LED through NVG?

## Related

- [[Strobe vs Constant On]] — flash pattern
- [[IR beacon capability]] — second channel
- [[Visibility range]] — white vs colored range testing