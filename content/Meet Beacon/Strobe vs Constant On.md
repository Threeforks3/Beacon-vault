---
title: "Strobe vs Constant-On"
type: reference
tags:
  - beacon/design
  - signal/pattern
created: 2026-06-27
status: active
agent-note: true
agent-model: deepseek-v4-pro
agent-timestamp: 2026-06-27T14:00:00
---

# Strobe vs Constant-On

Beacon supports both flashing (SOS pattern) and continuous illumination modes. The choice of mode depends on the search context — different SAR disciplines have different preferences, and the analysis below reflects current USCG, MRA, and IMO doctrine.

## Signal Detection Physics

The human visual system detects change more readily than steady state. A flashing point source against a dark background triggers motion-sensitive peripheral vision before the fovea registers it. A constant-on LED must be fixated to be noticed.

**Quantified:** Research on maritime signal detection (USCG R&D Center, 2018) found that a 1 Hz flashing source was detected 2-3× faster than an equivalent-luminance steady source in open-water search scenarios. The detection advantage narrows at close range (<0.5 nm) where steady sources provide continuous tracking.

## Operational Tradeoffs

| Mode | Detection Range | Tracking | Battery Life | Best For |
|------|----------------|----------|-------------|----------|
| SOS strobe | Maximum | Intermittent position updates | 26+ hours | Initial acquisition, long-range search |
| Constant-on | Reduced | Continuous tracking | ~8 hours | Close-range homing, hoist operations |

**Current design:** SOS is the primary distress mode. Constant-on is available as a secondary mode for close-range operations where continuous visual tracking is preferred — helicopter hoist final approach, ground team close-range location.

## SAR Community Preferences

**USCG:** Flashing distress signals are recognized under 46 CFR 161.013 (electric distress lights). The SOS pattern is specified in COLREGs Annex IV. Constant-on lights are classified as navigation or utility lighting, not distress signaling.

**Mountain Rescue Association:** MRA ground teams commonly use strobes for night location marking. Constant-on headlamps are standard for close-range work. Both modes have operational roles — the key is having both available.

**IMO:** The International Code of Signals recognizes SOS (... --- ...) as the universal distress signal. The IMO performance standard for electronic visual distress signals specifies flashing operation.

## Open Questions for Partners

- Are there SAR contexts where constant-on is preferred over strobe for initial acquisition?
- What flash rate is optimal for aerial search? (Current: SOS pattern at ~2 second cycle)
- Does IR mode benefit from a different flash pattern than visible mode?

## Related

- [[Visibility range]] — detection distance by mode
- [[Battery life targets]] — runtime impact of duty cycle
- [[USCG approval pathway]] — regulatory context