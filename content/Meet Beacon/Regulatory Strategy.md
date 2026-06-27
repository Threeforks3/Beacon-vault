---
title: "Regulatory Strategy"
type: permanent-note
tags: [beacon/identity, beacon/regulatory]
created: 2026-06-27
status: evergreen
---

# Regulatory Strategy

Every electronic device that emits a signal faces a regulatory path. Beacon chose its path deliberately — not by avoiding regulation, but by designing to qualify for exemptions where possible and meeting standards where required.

## The 1 MHz Decision

Beacon's processor runs at 1 MHz. That's slow by modern standards — a typical microcontroller runs at 8, 16, or 20 MHz. The decision was regulatory, not technical.

FCC Part 15 governs unintentional radiators — devices that emit radio frequency energy as a byproduct of operation. Below a certain clock speed threshold, devices qualify for exemption under §15.103(h). At 1 MHz, Beacon falls comfortably within that exemption.

The alternative path — formal FCC testing — costs $5,000 to $13,000 for a device in this category. For a product targeting a $25 crowdfunding price point, that's prohibitive. The 1 MHz clock eliminates that cost without compromising functionality. The SOS timing is software-driven via delay loops; 1 MHz provides more than enough resolution for the required flash patterns.

## LED Visibility Standards

The SOS strobe adheres to 46 CFR 161.013-7, which specifies the flash rate for distress signals: 4.3 cycles per minute. Each SOS cycle is 14 seconds with a 3-second inter-cycle gap. The white LED was selected to deliver 28.2 candela minimum at 20mA — exceeding the visibility requirements for a personal distress signal at the target range of 2+ nautical miles.

Luminosity drove the LED selection, not cost. The Cree C503D-WAN was the unanimous choice across 16 independent studies — no other LED in its class delivered the required brightness at the power budget available.

## IR — Exceeding Requirements

There is no regulatory requirement for infrared signaling on a personal distress device. Beacon includes it anyway. USCG and Civil Air Patrol search aircraft fly with AN/AVS-9 night vision goggles as standard equipment. An 850nm IR strobe is invisible to the naked eye but unmistakable through NVG — it preserves the crew's night adaptation while providing an active target.

The IR LED (Vishay TSHG6400, 850nm, ±22° half-angle) was selected for wider beam coverage than the narrower ±15° alternatives. A wider beam means less precision required from the person holding it — the signal reaches the aircraft even if Beacon isn't perfectly oriented.

## The Path Not Taken

Beacon does not include a 406 MHz transmitter, GPS receiver, or VHF radio. Each of those would trigger a different regulatory regime: COSPAS-SARSAT type approval for EPIRBs/PLBs, FCC licensing for transmitters, and significantly higher per-unit cost. Those capabilities are valuable — they're also well-served by existing products. Beacon focuses on the last mile: the visual terminal homing signal that works after the satellite fix and radio call have done their job.

## CE and International

CE marking for the European market is deferred to production. The design targets Class 1 (no radio transmitter) under the Radio Equipment Directive, which simplifies the conformity assessment path. The 1 MHz clock and lack of intentional radiator place Beacon in the least burdensome category for most international markets.
