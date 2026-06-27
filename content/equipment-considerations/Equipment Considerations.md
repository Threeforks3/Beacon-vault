# Equipment Considerations

Every design decision in Beacon traces to a scenario requirement. This section maps what we built to why we built it.

## Signal

- **[[Strobe vs constant-on]]** — Flash draws attention. Constant aids tracking. Beacon does both.
- **[[IR beacon capability]]** — Night vision compatibility for military/aviation SAR.
- **[[Visibility range]]** — Tested distances in daylight, dusk, and darkness.
- **[[Color selection]]** — Why white/IR over red/blue. International signal conventions.

## Power

- **[[Battery life targets]]** — Scenario-based runtime requirements (2hr, 8hr, 24hr).
- **[[Cold weather performance]]** — Lithium chemistry selection for sub-zero operation.
- **[[Battery accessibility]]** — Standard CR123A — available worldwide, even in remote areas.

## Physical

- **[[Waterproofing]]** — IP68 rating rationale. Immersion scenarios drive this.
- **[[Bar-based attachment]]** — Universal mounting architecture. Zero additional parts.
- **[[Impact resistance]]** — Drop-tested from helicopter hoist height.
- **[[Buoyancy]]** — Floats with PFD. Doesn't sink if detached.

## Usability

- **[[One-hand activation]]** — Designed for cold, wet, gloved hands.
- **[[Stuck-button timeout]]** — Prevents accidental drain in pack.
- **[[Attachment confidence]]** — Bar system tested to remain attached through avalanche and swift water.
