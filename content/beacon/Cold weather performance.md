# Cold Weather Performance

Beacon uses 2x AAA cells. The AAA form factor gives users a choice: alkaline for everyday low cost, or lithium AAA for extreme cold. The device itself works with either — the boost converter handles the full voltage range.

## Chemistry Options

**Alkaline (default):** -20°C to +54°C operating range. $0.50-1 per pair, available everywhere. Voltage droops below 0°C and cells fail completely around -18°C. For paddling, coastal, urban, and temperate scenarios — adequate and cheap.

**Lithium AAA (Energizer L92 or equivalent):** -40°C to +60°C. $3-4 per pair. Same form factor, same compartment, same device. Maintains nominal voltage across the full cold range. For avalanche, arctic, and winter backcountry — drop them in. Same chemistry used in avalanche transceivers.

This is the advantage of AAA over a soldered-in lithium pouch cell: the user decides based on their scenario. No SKU fragmentation, no "expedition edition." One device, user's choice of cells.

## Boost Converter Cold Margin

The TPS61070DDCR boost converter is specified to -40°C. Switching frequency and efficiency are flat across the temperature range. The 5.0V output rail stays within regulation even at cold-soak minimum input voltage.

## Enclosure

The sealed polycarbonate cover prevents condensation and ice formation on internal electronics. The LED dome is heated slightly by LED junction temperature during operation — preventing frost accumulation on the optical surface.

## Operational Context

- **Avalanche burial:** Victim entombed in snow at 0°C. Body heat keeps device near 0°C. Alkaline adequate. Lithium AAA recommended for multi-day backcountry tours where device may be cold-soaked in pack before activation.
- **Winter overboard:** Air temperature -20°C, water temperature 2°C. Device transitions from cold air to warmer water. Alkaline voltage recovers in water. Lithium AAA eliminates cold-air voltage sag.
- **Arctic expedition:** Multi-day operation below -20°C. Lithium AAA required.
- **Wilderness lost hiker:** Overnight at -10°C. Alkaline marginal — keep device in inner jacket pocket. Lithium AAA removes concern.

## Related

- [[Battery life targets]] — runtime modeling
- [[Battery accessibility]] — cell availability
- [[Avalanche burial]] — primary cold-weather scenario
