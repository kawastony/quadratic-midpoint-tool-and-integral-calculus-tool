# Carrier algebra

Date: 9 October 2026

Concept and algebra only. Not a claim that the derivation is closed.

## 1. Section measure

A cone of half-angle theta, generator coordinate s measured from the tip.

Strip, one transverse direction: width w(s) = alpha s. Measure grows as s. Conserved flux Q = w(s) g(s) gives

g(s) = Q / (alpha s).

Solid cone, two transverse directions: radius r(s) = s sin theta, area A(s) = pi r(s)^2 = pi sin^2(theta) s^2. Conserved flux Q = A(s) g(s) gives

g(s) = Q / (pi sin^2(theta) s^2).

Inverse-square holds only for the solid cone. The strip falls as 1/s. Fixed circumference kills the solid-cone falloff: if r is held fixed, A is constant and g does not fall. The elongating funnel with fixed mouth is the strip or the fixed-r case, not the inverse-square case, unless the stretch is allowed to open the radius.

## 2. Source coupling

The packet does not emit g by name. It emits the current I(t) = (Delta E / 2) sin(Delta E t), and the centroid acceleration a(t) = (d Delta E^2 / 2) cos(Delta E t). The coupling used here is that the active half injects its impulse into the cone flux,

Q = integral_0^{T/2} a(t) dt = d Delta E / 2 = 0.07084

at the locked point. That impulse is the source strength. The carrier then spreads it by the section law above.

## 3. Test body

On the generator the slow-motion law is

d^2 s / dt^2 = - partial_s Phi,   partial_s Phi = - g(s),

with g(s) from the section. In the weak-field form this is the spatial part of the geodesic equation for a static metric ds^2 = -(1 + 2 Phi) dt^2 + ds^2 + r(s)^2 dOmega^2. The second body accelerates because its coordinate acceleration is minus the gradient of the carrier potential, not because it is assigned the packet's centroid motion.

## 4. Oscillation and storage

The source alternates. The carrier stores the active-half impulse and does not reverse it on the return half. Rising half fills Q. Falling half is internal to the packet. The field g(s) is the stored flux divided by the section, so it stays one sign between cycles.

## 5. Depletion

Energy required to keep increasing the speed of a test mass m over a step Delta s is Delta E_req = m a Delta s. Depletion in the carrier is the loss of that budget. The rule used here is that the depletion rate and the acceleration budget are inverse,

D = C / (m a),

so a rising depletion is a falling acceleration, which is the falloff along s once a = g(s). Equivalently, where the speed is nonzero, a = (1/(m v)) dE/dt from the power ledger. Depletion along the cone is the same fact as g decreasing with section growth.
