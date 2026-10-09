# From packet v to g

Date: 9 October 2026

Newton's formula is not used. G is not inserted. The mass and the radius are not assigned to its slots.

v is the wall mass. It enters only by fixing the split,

Delta E(v) = A(v) exp(-2 v d),

A(v) = 4^v Gamma(v+1/2) / (sqrt(pi) Gamma(v)).

At v = 1 the formula gives A = 2 and Delta E = 0.03663. The locked numerical split at d = 2 is 0.07084. The acceleration below uses the locked split.

The transfer moves the centroid,

x(t) = -(d/2) cos(Delta E t).

There is movement, so there is a speed,

v_speed(t) = (d Delta E / 2) sin(Delta E t).

The speed changes, so the integral tool gives the acceleration,

a(t) = d v_speed / dt = (d Delta E(v)^2 / 2) cos(Delta E t).

The integral of a from the wall to the quarter-clock equals the speed gained there, 0.0501. That check closes.

The midpoint tool reads the same a on a short window of the rising half, where the sine is locally quadratic. It confirms the value. It is not a second source.

At the start of the deep voice, cos = 1, so

a(v) = d Delta E(v)^2 / 2 = 0.00502

in packet units, at the locked point.

The constitution sets this active acceleration equal to gravity:

g(v) = d [A(v) exp(-2 v d)]^2 / 2.

The soft half holds no new gain: the speed is falling back, and the pause reading is the return, not a second constant. Acceptance does not change v or Delta E, so it does not change g.

This uses v to calculate a, and names that a as g. It does not produce a kilogram, a metre, or Newton's G.
