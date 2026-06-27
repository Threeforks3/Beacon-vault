# Cold Weather Performance

Beacon is designed to operate from -40°C to +60°C. The CR123A lithium chemistry, sealed enclosure, and thermal design ensure cold-weather operation where alkaline batteries fail completely.

## Chemistry Selection

**Lithium vs Alkaline:** Alkaline batteries lose voltage rapidly below 0°C and fail completely at -18°C. Lithium chemistry (Li/MnO2 in CR123A) maintains nominal voltage to -40°C. This is the same chemistry used in avalanche transceivers — proven in backcountry winter conditions.

**Cold-soak behavior:** When a lithium cell is cold-soaked at -30°C, initial voltage droops by 10-15% for the first few minutes of discharge. The cell self-heats under load (internal resistance × current²) and voltage recovers to near-nominal within 5-10 minutes of activation. Beacon's boost converter maintains regulation through the initial voltage droop.

**Boost converter cold margin:** The TPS61070DDCR boost converter is specified to -40°C. Switching frequency and efficiency are flat across the temperature range. The 5.0V output rail stays within regulation even at cold-soak minimum input voltage.

## Enclosure

The sealed polycarbonate cover prevents condensation and ice formation on internal electronics. The LED dome is heated slightly by LED junction temperature during operation — preventing frost accumulation on the optical surface.

## Operational Context

- **Avalanche burial:** Victim entombed in snow at 0°C. Device operates at full brightness.
- **Winter overboard:** Air temperature -20°C, water temperature 2°C. Thermal shock from air to water does not affect operation.
- **Arctic expedition:** Multi-day operation at -30°C. Lithium chemistry maintains voltage throughout.
- **Wilderness lost hiker:** Overnight at -10°C. Battery self-heating under load provides additional margin.

## Related

- [[Battery life targets]] — runtime modeling
- [[Avalanche burial]] — primary cold-weather scenario
