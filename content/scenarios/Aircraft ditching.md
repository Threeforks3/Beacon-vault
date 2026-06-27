# Aircraft Ditching

An aircraft — small private plane, commercial airliner, or military helicopter — makes an emergency water landing. Survivors may be in life rafts, in the water, or clinging to debris. The search area can span dozens of square miles.

## The Scenario

Surviving a ditching is the first half. Being FOUND in open water, possibly miles from the last known position, is the second half. ELTs activate on impact but 121.5/406 MHz beacons can fail on water impact or be submerged with the aircraft.

A life raft drifts at 1-3 knots in wind. After 6 hours, search radius is 6-18 nautical miles. After 24 hours, it's 24-72 nautical miles. Without an active signal ON the raft, search aircraft look for a 2-meter orange raft in a circle 50 miles across.

## Current Technologies & Practices

| Technology | Used By | Strengths | Gap |
|------------|---------|-----------|-----|
| ELT 406 MHz | COSPAS-SARSAT, ICAO¹ | Automatic activation on impact, satellite detection | May fail on water impact; submerged with aircraft if it sinks |
| 121.5 MHz homing | USCG, CAP² | Direction-finding by search aircraft | Satellite monitoring discontinued 2009; being phased out |
| Life raft equipment kit | IMO SOLAS³ | Strobe, mirror, dye marker, whistle | Small raft strobes are low-power; dye marker disperses in hours |
| Search aircraft FLIR | USCG, CAP, military⁴ | Wide-area thermal scanning | Raft and survivors at water temperature — low thermal contrast |
| NVG visual search | USCG, military⁵ | Crew night vision scanning | Passive — requires something TO see. An IR strobe provides active target |

## The Gap

COSPAS-SARSAT gets searchers to within 1-3 nautical miles. Then what? The raft is invisible at night. The strobes in standard raft equipment kits are small, low-power, and short-runtime. Search aircraft crews scan dark water with NVG looking for a passive target. An active IR strobe changes the equation — the raft announces its position continuously.

## Beacon Design Response

Beacon is a complement to ELT, not a replacement. The 406 MHz ELT gets searchers to the general area. Beacon's SOS strobe gets them to the exact raft location. 26+ hour runtime. IR mode for NVG-equipped search aircraft — invisible to naked eye, unmistakable through NVG. IP68 to 2 meters salt water immersion. Bar-based attachment pre-threads onto raft D-rings or grab lines during pre-flight safety brief. Gold-plated contacts resist salt water corrosion. Floats lens-up independently — continues signaling even if separated from raft.

## Coalition Footnotes

[¹] **COSPAS-SARSAT / ICAO:** 406 MHz ELT required on most aircraft under ICAO Annex 6. Satellite detection in <5 minutes with GPS-encoded position. But water impact is the highest failure mode — antenna submersion, airframe shielding, or battery disconnect. [[COSPAS-SARSAT]] [[ICAO SAR provisions]]

[²] **USCG / CAP:** 121.5 MHz homing uses aircraft-mounted direction finders. Being phased out — COSPAS-SARSAT ended satellite processing of 121.5 MHz in 2009. Some USCG aircraft retain capability but it's no longer primary. [[USCG SAR doctrine]]

[³] **IMO SOLAS:** Life raft equipment standards (SOLAS Chapter III) require a waterproof electric torch, signaling mirror, and whistle. No requirement for a dedicated distress strobe with IR capability. Strobe in raft canopy is low-power and typically alkaline-battery limited. [[IMO standards]]

[⁴] **USCG / CAP / Military:** FLIR systems detect temperature differences. Survivors in water or on a raft present minimal thermal contrast against the water surface. Active IR strobe at 850nm is a bright point source through FLIR — unambiguous.

[⁵] **USCG Air Station Clearwater:** MH-60T crews fly with AN/AVS-9 NVG as standard night equipment. An IR strobe visible through NVG provides positive visual identification before the aircraft reaches hover position. [[USCG approval pathway]]

## Related

- [[Helicopter hoist]] — recovery from water
- [[IR beacon capability]] — NVG/FLIR compatibility
- [[Battery life targets]] — oceanic endurance
- [[Buoyancy]] — independent floatation
- [[Waterproofing]] — salt water protection
- [[IMO standards]] — international maritime signal requirements
- [[COSPAS-SARSAT]] — satellite SAR system
