# Regulatory

Beacon's regulatory landscape spans maritime (USCG), radio frequency (FCC), and product safety (UL) domains. Current assessment: the device is FCC §15.103(h) exempt (ATtiny404 internal 1 MHz oscillator — no intentional radiator classification) and falls under USCG self-certification for non-carriage equipment.

## Active Monitoring

Beacon's Regulatory Monitor Loop checks Federal Register feeds weekly for changes to:
- 46 CFR Part 161 (USCG electrical equipment)
- FCC Part 15 (intentional/unintentional radiators)
- UL standards for portable lighting / safety devices

## Key Findings

- **FCC:** §15.103(h) exemption confirmed — device operates at 1 MHz internal RC oscillator, well below intentional radiator thresholds. No certification required.
- **USCG:** Self-certification pathway confirmed under CG-ENG Policy Letter 03-18. Bench test plan drafted.
- **UL:** No specific standard identified for wearable electronic distress signals. UL 913 (intrinsically safe) may apply if Beacon is marketed for hazardous environments.

## Open Questions

- Does international distribution (EU, Canada) require additional certification?
- Is UL listing valuable for partner credibility even if not required?
- Does the bar-based attachment trigger any mechanical safety standard? (ASTM, etc.)

## Related

- [[USCG approval pathway]] — detailed analysis
- [[FCC]] — Part 15 exemption
- [[UL]] — product safety standards
