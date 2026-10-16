# Candidate B: quartic stiffening, first-pass analysis

Date: 16 October 2026

## Discrete law
kappa_d (u_{n+1} - 2 u_n + u_{n-1}) = (m^2 + lambda u_n^2) u_n - J_n.

## Continuum limit
kappa (u'' + 2/r u') = m^2 u + lambda u^3 - J(r).

## Weak field
For u << 1 the cubic term is negligible. Exterior recovers the screened Poisson equation. Unscreened limit gives u ~ 2GM/r, T ~ 1 - 2GM/r. Satisfies R3-R5.

## Center
Assume regular expansion u(r) = u_0 + u_2 r^2 + O(r^4). Substitution yields a relation between u_0, lambda, and the central load. For moderate loads u_0 remains finite. For extreme loads the cubic term can still allow large but finite u_0. No hard floor.

## Result
Candidate B stiffens the strong-field response and improves the chance of a regular center relative to pure elasticity. It does not produce a transmission floor. The jammed plateau remains an extra assumption. Energy-realizable and continuum-compatible. Minimal nonlinear extension.

## Next
Numerical integration of the continuum equation for increasing central load to map the u_0(J) curve and check for any effective saturation.
