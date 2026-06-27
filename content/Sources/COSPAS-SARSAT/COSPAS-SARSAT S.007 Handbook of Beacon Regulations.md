---
type: literature-note
tags:
  - source/cospas-sarsat
  - domain/satellite
  - domain/maritime
  - domain/aviation
  - equipment/beacon-types
created: 2026-06-27
status: active
source: "S.007-Issue2-Rev4-LATEST.pdf"
source-organization: "COSPAS-SARSAT"
source-date: "October 2022"
source-pages: "82 pages"
source-type: "International Standard"
agent-note: true
agent-model: deepseek-v4-pro
agent-timestamp: 2026-06-27T23:30:00
---

# COSPAS-SARSAT Handbook of Beacon Regulations (S.007)

**Source:** *Handbook of Beacon Regulations*, C/S S.007, Issue 2, Revision 4, October 2022. International Cospas-Sarsat Programme.

## Scope

This document summarizes regulations issued by Cospas-Sarsat Participants regarding the carriage of 406 MHz beacons. It covers EPIRBs (Emergency Position-Indicating Radio Beacons), ELTs (Emergency Locator Transmitters), and PLBs (Personal Locator Beacons).

## Three Beacon Types

The Cospas-Sarsat system recognizes three classes of 406 MHz distress beacon:

- **EPIRB** — Maritime. Linked to a vessel via MMSI or radio call sign. Mandated by SOLAS for certain vessels.
- **ELT** — Aviation. Linked to an aircraft via 24-bit address or registration marking. Mandated by ICAO.
- **PLB** — Personal. "Intended for use by an individual person (i.e., not necessarily linked to a ship or an aircraft like EPIRBs and ELTs). They can be used in any environment (e.g., on land, at sea and in aircraft)."

**Beacon relevance:** Beacon is closest to the PLB category — a personal signaling device for an individual, usable in any environment. However, Beacon operates in the visual/IR domain rather than 406 MHz radio. Beacon addresses the gap Cospas-Sarsat acknowledges: a 406 MHz alert brings rescuers to a GPS fix, but the victim drifts away from that fix. Beacon marks the victim's actual position with light.

## Critical Limitation

> No beacon transmits properly under water.

**Beacon relevance:** This single sentence from the international beacon authority validates Beacon's fundamental design premise. 406 MHz signals cannot transmit through water. A person in the water — the most common paddlesport emergency — cannot rely on satellite beacons for continuous position marking. Beacon's visual strobe operates above water (on the PFD shoulder), providing continuous position marking where RF beacons fail.

## False Activation Consequences

> Activating a 406 MHz beacon for even a very short time will generate a Cospas-Sarsat distress alert message that will be relayed to SAR services for their immediate action. Activating a beacon for reasons other than to indicate a distress situation or without the prior authorization from a Cospas-Sarsat MCC is considered an offence in many countries/territories of the world, and could result in prosecution.

**Beacon relevance:** 406 MHz beacons carry a heavy deterrent against false activation — criminal prosecution. This creates a psychological barrier: a person who is unsure whether their situation qualifies as "distress" may delay activation. Beacon has no such barrier. A strobe is a local visual signal — it does not trigger a satellite alert, does not involve law enforcement, and can be activated at any level of concern without consequences. This lowers the threshold for signaling and increases the likelihood of early activation.

## Self-Test Capability

> 406 MHz beacons are designed with a self-test capability for evaluating key performance characteristics. Initiating the beacon self-test function will not generate a distress alert in the Cospas-Sarsat System.

**Beacon relevance:** Self-test without false alert is a design requirement proven by 406 MHz beacons. Beacon's firmware should include a self-test mode (battery check, LED test) that does not produce an SOS pattern — matching the industry standard established by Cospas-Sarsat.

## Scale of the System

> There are more than two million Cospas-Sarsat 406 MHz distress beacons in operation.

**Beacon relevance:** The 406 MHz ecosystem is massive — over 2 million beacons worldwide. Beacon does not compete with this system; it complements it. The visual strobe addresses the gap between satellite fix and visual acquisition that 2 million beacons cannot close.

## Return Link Service (RLS)

> The Return Link Service (RLS) provides notification to a 406 MHz beacon that an alert transmitted by the beacon has been detected. This service is intended to provide acknowledgement of the reception of the alert message to persons in distress.

**Beacon relevance:** RLS provides psychological reassurance — "your alert was received." Beacon cannot provide this for satellite alerts (no 406 MHz integration), but its visual strobe provides a different form of reassurance: the user can see the light flashing and know the signal is active. For IR strobe, the reassurance comes from knowing SAR aircraft use IR detection.

## PLB Registration Requirements

> PLBs are intended for use by an individual person. Emergency contacts listed in the registration record of the PLB should speak the official language(s) associated with the country code of the beacon.

**Beacon relevance:** 406 MHz PLBs require registration — a bureaucratic step before the device works. Beacon requires no registration. Buy it, attach it, activate it. This is a meaningful market differentiation for casual outdoor users who would not register a PLB.

## Beacon Coding Complexity

The S.007 details multiple coding protocols (User Protocols and Location Protocols) across EPIRBs, ELTs, and PLBs — each with different country-specific requirements. This complexity is inherent to the 406 MHz system and is a barrier to adoption for recreational users.

**Beacon relevance:** Every coding protocol, every country-specific regulation, every registration requirement is friction that Beacon eliminates. Beacon has no coding, no protocols, no registration. It simply produces light in an internationally recognized distress pattern (SOS).

## Related

- [[COSPAS-SARSAT]] — organization page
- [[Man overboard at night]] — "no beacon transmits properly under water"
- [[Aircraft ditching]] — ELT regulations
- [[IMO standards]] — maritime beacon requirements
- [[ICAO SAR provisions]] — aviation beacon requirements
- [[Strobe vs Constant On]] — complement to satellite beacons
