# Constitutive potential scan and core-scale status

Date: 18 October 2026

## Constitutive comparison

Two candidate potentials for the selector field u(r) were compared under the same static radial selector equation, source profile, and boundary conditions. Admissibility required N = e^{-u} > 0, N ≤ 1, and z = e^u - 1 ≥ 0.

- Double-well (exchange-symmetric quartic): 98 of 100 coarse combinations admissible; refined 20×20 grid over m ∈ [0.2, 1.2], u_★ ∈ [1.2, 4.5] produced 400 admissible solutions. Strongest core localization and redshift at small m and intermediate u_★; sharper threshold index at larger m.
- Exponential: all tested cases entered u < 0 over part of the domain, yielding N > 1 and z < 0. Excluded under the stated admissibility conditions.

The numerical scan therefore favors the double-well branch for physical admissibility in the present implementation. This is a constitutive selection within the model, not a derivation of the potential from the kinematic grammar.

## Core scale

The framework constants are c and G (via Newtonian normalization) and κ = c^{4}/(8π G). No ℏ appears. A Planck-length floor cannot be derived. Any core scale must be of the form s_{0} = a ξ with a a pure number, so z_max = 1/a. The choice a = 1 places the core surface at the Schwarzschild radius with z_max = 1 and v = √3 c / 2. This is a dimensionless choice, not a derivation.

## Status of open items

- Variational selector is the Euler–Lagrange equation of a scalar action; a single field equation containing V cannot constrain V.
- Cone curvature cannot supply a local potential (2D Einstein–Hilbert term is a total derivative).
- V must diverge as v → c (Lagrange multiplier of the speed bound). Form below the barrier remains a fork between double-well and exponential, distinguishable by presence or absence of a threshold.
- Lapse N = s/(s+ξ) is one of infinitely many interpolations between the same limits; N = e^{-ξ/s} is another and differs at O(1/s^{2}) in exterior load.
- Horizonlessness remains conditional on excision scale. Law 6 remains a free-fall gauge statement.

The constitutive scan narrows the phenomenological choice. It does not close the dynamical completion or select a unique transmission profile from the six laws.
