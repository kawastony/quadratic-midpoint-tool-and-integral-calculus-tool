# Map and gravity calculation

Date: 9 October 2026

## What the tool captures

The quadratic midpoint tool and the integral ledger capture the stacked fall: active increase, pause that holds speed, resume from that speed. They do not capture bridge P_2, alignment alpha, or the observer. Those stay in grok-notes-version-3.

## Map

| Voice cycle | Tool |
|-------------|------|
| Person, unmoved by the voices | Midpoint, held fixed |
| Deep voice, active | Boundaries closing; speed of the fall increases |
| Soft voice, pause | Boundaries held; closing speed zero; fall speed unchanged |
| Equal intervals | Active duration = pause duration = tau |
| Next deep voice continues from the speed already reached | v is not reset; the next active phase adds to it |
| Two voices | The two boundaries. For f(x)=x^2 their slope average equals the midpoint slope |
| Observer, acceptance, exit from the trap | Not in the tool |

## Calculation the map allows

Half-width w. Midpoint slope stays 6 while the boundaries move. Accumulated change across the interval:

integral from 3-w to 3+w of 2x dx = 12 w.

Equal phases, duration tau. On an active phase the closing speed is u and the fall gains

Delta v = integral_0^tau a(t) dt.

On the pause, a = 0, so v+ = v-. After n active phases with the same a,

v_n = n a tau.

Distance fallen through n equal pairs, active then pause:

s_n = n (v_0 tau + (1/2) a tau^2) + n v_pause_average tau,

with the pause carrying the speed left by the preceding active phase. Speed stacks. Distance stacks faster than a single constant acceleration.

If the narrative's "increasing even more" is kept, a itself grows by phase. Then v_n is no longer n a tau, and the motion is not constant g.

## Gravity

Constant gravitational acceleration is the special case a = g on every active phase and a = 0 on every pause. Nothing in the midpoint identity forces a = g. The integral of the midpoint slope over the gap is 12w, which shrinks as the boundaries close. The integral of closing speed is a distance. The energy of a fixed-time elongation grows as L^2. None of these equals g, and none recovers v_inf = (Lambda_*^2 G M mu)^(1/4), 18.7 eV, or the z ~ 0.35 freeze.

The equivalence-principle likeness is outside this calculation. Acceptance would have to change the relation to v without changing v. The tool has no such variable. Alpha in the three-bridge note is that variable, and it was not derived from the midpoint.
