# Dynamical Closure Test Results — 2026-10-21

## Analytic Source-Free Branch

Closed-form solution for the homogeneous equation u'' = -2/r u' + 2 (u')^2 yields:

| a | r_surf | r_ph | b_c |
|---|--------|------|-----|
| 0.1 | 1.1 | 1.6371 | 2.7571 |
| 0.2 | 1.2 | 1.7529 | 2.9461 |
| 0.3 | 1.3 | 1.8526 | 3.1081 |
| 0.4 | 1.4 | 1.9397 | 3.2492 |
| 0.5 | 1.5 | 2.0168 | 3.3738 |
| 0.6 | 1.6 | 2.0860 | 3.4851 |
| 0.7 | 1.7 | 2.1486 | 3.5858 |
| 0.8 | 1.8 | 2.2059 | 3.6776 |
| 0.9 | 1.9 | 2.2587 | 3.7620 |
| 1.0 | 2.0 | 2.3077 | 3.8402 |

(xi=1, rmax=20). These are the photon-sphere critical impact parameters. Source-free scalar moves b_c downward from the cone value of 4.

## Dynamical Test of Fitted S(u, u')

- Target profile: u = cone_u + A*(xi/r) with A_star ≈ 0.6528, giving target b_min ≈ 5.400.
- Polynomial fit (degree 3, Ridge) of reverse-engineered S on (u, u') along the target branch has low residual on the branch.
- Quick dynamical integration starting from the *target* initial conditions (u(rmin), u'(rmin)) under the fitted S(u,u') law:
  - Solve succeeds.
  - Dynamical b_min ≈ 3.024.
  - Δb_c ≈ -2.376 (relaxes toward source-free values).
  - max |u - u_target| ≈ 0.60.

**Conclusion:** The regression fit S ≈ S(u, u') describes the source *along the target trajectory* extremely well, but does not dynamically sustain that trajectory. The flow under the fitted law drifts away from the target and settles near the source-free branch.

This confirms that a fit inferred from a single 1-D trajectory in (u, u') space is not a closed constitutive law. Locality in (u, u') is insufficient for dynamical reproduction of the target-hitting profile.

## Implications for the Paper

- Reverse-engineered target-hitting profiles exist and are regular.
- Purely local S(u) fails dynamically (prior result).
- Enriched descriptive fits S(u, r) or S(u, u') improve regression quality dramatically.
- However, even the best descriptive S(u, u') does not close the dynamics when used as an ODE right-hand side.
- Therefore the compact-object completion requires structure beyond a low-order local function of (u, u') fitted on one branch. Explicit radial dependence, auxiliary fields, or non-local constitutive structure remain open.

Honest claim: the missing source is smooth and of non-negligible amplitude near the photon sphere, but is not captured by simple polynomial closures in the scalar state variables alone.
