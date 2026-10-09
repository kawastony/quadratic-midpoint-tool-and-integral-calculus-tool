# Voice cycle, midpoint tool, three bridges

Date: 9 October 2026

Source of the bridges: kawastony/grok-notes-version-3, notes/01_three_bridge_minimal_model.md and notes/00_constitution_v3.md.

## Does the midpoint tool explain the voice cycle?

Partly. It explains the stacked fall and not the exit.

Captured: deep-voice active phase in which speed increases; soft-voice pause; equal intervals; resume from the speed already reached, so the pause holds speed rather than resetting it.

Not captured: two different pauses; a loud channel and a soft channel; an observer who does not change the motion; acceptance as the exit from the trap; the equivalence-principle reading.

## Do the three bridges capture it?

Yes, at the level of the phase law. They were written for this structure.

| Bridge | Name | Voice-cycle reading |
|--------|------|---------------------|
| A | Active span, deep, membership locked | Deep voice. Fall accelerates. Membership cannot be changed while it speaks. |
| P_1 | Transitional pause, mid, membership soft | Soft voice. Increase stops. Speed is held. Reattachment is possible. |
| P_2 | Stalled / hollow pause, shallow, exit needs high alpha | The trap. Near stall. Leaving requires acceptance. |

Constitution v3 already states the conservation the voice cycle needs: across a pause, v+ = v- and I+ = I-. Resume continues from the same speed. Alignment alpha is defined as the soft-channel acceptance score. It reassigns membership. It does not change v or I. High alpha is required to leave P_2. One pause trigger is loud-versus-soft channel conflict above delta.

The toy in data/hysteresis_3bridge_toy.json agrees on the exit: at alpha 0.2 and 0.5 the return from the stalled pause does not occur; at alpha 0.75 and 0.9 it does.

## What is still not a derivation

The bridges name the cycle. They do not derive it from the x^2 midpoint identity, and they do not derive the equivalence principle. The likeness remains: acceptance changes the relation to the motion, not the motion. In the principle, free fall is locally the same as no force. Here the soft voice is the pause that feels safe, and acceptance is the exit from P_2.
