---
title: "IR Detection Surfaces"
type: reference
tags: [equipment/ir, physics/sensors, technology/detection]
created: 2026-06-27
status: active
agent-note: true
agent-model: deepseek-v4-pro
agent-timestamp: 2026-06-27T14:00:00
---

# IR Detection Surfaces

Beacon emits 850nm near-infrared from Vishay TSHG6400 LEDs. The 850nm wavelength was chosen for NVG compatibility, but the detection surface is far larger than aviation night vision. Silicon photodiodes — the foundation of every CCD and CMOS image sensor — are sensitive from roughly 350nm to 1100nm, peaking near 850nm. Beacon sits at their sweet spot.

## Why Silicon Sees 850nm

**Bandgap physics**: Silicon has a bandgap of 1.12 eV. Any photon with energy above 1.12 eV can generate an electron-hole pair in silicon. 850nm photons carry 1.46 eV — well above the threshold. This is not a specialty property of night vision sensors. It is fundamental. Every silicon imager sees 850nm.

**Consumer IR-cut filters**: Digital cameras and phones place an IR-cut filter over the sensor to improve color accuracy in visible light. These filters are not opaque — they attenuate IR but don't block it. At 850nm, typical consumer IR-cut filters pass 1-15% of incident light. An LED emitting 35 milliwatts of IR reaches the sensor at hundreds of microwatts — orders of magnitude above the sensor noise floor.

**The phone camera test**: Open your phone camera. Point a TV remote at it. Press a button. The remote's 940nm LED — *farther* from silicon's peak than Beacon's 850nm — produces a visible purple-white flash through the camera. Beacon is brighter, at a wavelength silicon sees more efficiently.

## Detection Surface Catalog

| Sensor Type | 850nm Sensitivity | Deployment | Detection Range (est.) |
|------------|-------------------|------------|------------------------|
| AN/AVS-9 NVG (USCG MH-60T) | Peak sensitivity at ~800nm | Aviation SAR | 3+ km |
| ANVIS-9 NVG (military SAR) | Peak sensitivity at ~800nm | Military SAR | 3+ km |
| FLIR thermal (MWIR) | Low at 850nm | Aviation/law enforcement | Not optimized for 850nm |
| Smartphone camera (any) | Attenuated by IR-cut filter | Ubiquitous | 500m+ (clear air) |
| Consumer drone camera | Attenuated by IR-cut filter | Growing rapidly | 500m+ |
| Security camera (IR mode) | High — IR-cut removed at night | Shorelines, marinas, trailheads | 1km+ |
| Digital night scope (Gen 2/3) | Full sensitivity | Hunters, law enforcement | 2km+ |
| Digital camera (no IR-cut) | Full sensitivity | Astrophotography, modified cameras | 3km+ |
| Laser range finder sensor | High at 850nm (same wavelength) | Military, surveying | In-band detection |

## Operational Implications

**Not just aircraft**: The NVG-equipped helicopter is the gold standard, but it is also the rarest detection surface. A capsized kayaker at night is far more likely to be within range of a phone camera, a marina security camera, or a recreational drone than directly under a Coast Guard flight path.

**Redundancy through ubiquity**: Every additional detection surface is an independent chance of being found. The person on shore scanning with their phone. The fishing boat's onboard camera system. The trailhead security camera recording the parking lot. The hunter's digital scope sweeping a hillside. None of these replace the Coast Guard. All of them reduce the time to detection.

**No additional hardware**: The detection surface exists whether or not anyone planned for it. Beacon requires no paired receiver. No app. No base station. It exploits a physical property of silicon that every camera manufacturer already ships.

## Limitations

- **Atmospheric absorption**: Water vapor absorbs IR. In heavy fog or rain, IR range is reduced but not eliminated — IR penetrates light obscurants better than visible light due to longer wavelength.
- **Consumer IR-cut variability**: Phone cameras vary in IR sensitivity by manufacturer and model year. Modern phones with stronger IR-cut filters will see Beacon at shorter range.
- **Not thermal**: Beacon is near-infrared, not thermal (MWIR/LWIR). It does not produce a heat signature detectable by true thermal imagers.
- **Directional**: TSHG6400 has a ±22° half-angle. The IR beam is moderately directional — not isotropic.

## Related

- [[IR beacon capability]] — operational use across scenarios
- [[Visibility range]] — tested distances
- [[Beacon]] — full product specification
- [[Strobe vs Constant On]] — signal pattern rationale