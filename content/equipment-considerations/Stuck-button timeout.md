# Stuck-Button Timeout

If Beacon's activation button is held down continuously — compressed in a packed bag, jammed against equipment, or pinned under debris — the device will eventually deactivate to prevent battery drain. This is the stuck-button timeout.

## Behavior

**Normal activation:** Press and hold 2 seconds → device activates → SOS strobe begins.

**Stuck-button detection:** After 30 minutes of continuous button press, the firmware assumes the button is mechanically stuck. The device deactivates and enters lockout — it will not reactivate until the button is released and pressed again.

**Rationale:** A Beacon accidentally activated in a pack will drain its battery in 26+ hours. The stuck-button timeout prevents a single accidental activation from consuming the entire battery. The 30-minute window provides margin: a user deliberately holding the button (injured, unable to release) gets 30 minutes of signaling. After that, the device conserves remaining battery for intentional reactivation.

## Firmware Implementation

The ATtiny404 monitors the button GPIO pin. A timer increments while the pin is held low (pressed). At the 30-minute threshold, the device enters deep sleep. The button must transition high (released) before a new press is recognized.

This is one of the earliest firmware changes needed before breadboard testing — see Beacon pending item #78.

## Open Questions

- Is 30 minutes the right threshold? Shorter prevents more drain. Longer provides more margin for users who can't release.
- Should there be a low-battery override? (If battery is critically low, maybe signal until dead regardless of button state)
- Can the timeout be user-configurable? (Different missions, different priorities)

## Related

- [[One-hand activation]] — button interface design
- [[Battery life targets]] — what's at stake if timeout fails
