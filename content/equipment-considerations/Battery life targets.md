# Battery Life Targets

Beacon's runtime is physics-governed — CR123A lithium cell capacity divided by LED drive current. 26+ hours continuous SOS from a single cell. Replaceable in seconds.

## Runtime Modeling

**Battery:** CR123A lithium, 1,550mAh nominal capacity at 3.0V nominal.

**Load:** Two LEDs (white + IR) at 29mA each, interleaved operation — one LED on at any time, not simultaneous. Boost converter efficiency ~85%. Total average draw: ~35mA at 3.0V input.

**Runtime:** 1,550mAh / 35mA = 44 hours theoretical. Derate for voltage droop, temperature, and boost converter efficiency variation: 26+ hours conservative.

**Power budget analysis** (Gate G1, passed 2026-06-25): all parameters within MOSFET and boost converter operational limits. Peak switch current 464mA vs 600mA minimum spec — 77% margin.

## Scenario Mapping

| Runtime Need | Scenario | Beacon Coverage |
|-------------|----------|-----------------|
| 2 hours | Swift water rescue, helicopter hoist | 13× margin |
| 8 hours | Open water capsizes, man overboard | 3× margin |
| 24 hours | Flood rescues, oceanic ditching | Exceeds (26+) |
| 72 hours | Earthquake entrapment, extended blackout | Replaceable battery — carry spares |

## Replaceability

CR123A is the most common lithium primary cell in emergency equipment. Available at any hardware store, outdoor retailer, or online. No proprietary battery, no charging infrastructure. In extended operations (multi-day flood rescue, oceanic search), carrying spare CR123As extends the signaling window indefinitely.

## Related

- [[Cold weather performance]] — lithium chemistry advantage
- [[Strobe vs constant-on]] — runtime impact of flash duty cycle
