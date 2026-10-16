# Minimal mathematics

Date: 16 October 2026

## Variables
- J0: load
- u: response (strain / optical depth)
- u★: capacity ceiling
- J0*: crossover load

## Candidate A
V(u) = (1/2) m^{2} u^{2}
Equilibrium: m^{2} u0 = J0
Unbounded linear response. No hard ceiling.

## Candidate B
V(u) = (1/2) m^{2} u^{2} + (λ/4) u^{4}
Equilibrium: m^{2} u0 + λ u0^{3} = J0
Sublinear stiffening. No hard ceiling.

## Candidate C
V(u) = (1/2) m^{2} u^{2} - μ ln(1 - u/u★) - (μ/u★) u
Domain 0 ≤ u < u★
V' diverges as u → u★⁻
Equilibrium forces u0 → u★ from below as J0 → ∞
Incremental slope Δu0/ΔJ0 → 0

## Definitions
- Plateau: Δu/ΔJ0 → 0 while u bounded by u★
- Ceiling: u★
- Crossover: load scale where saturation becomes visible
- Incremental collapse: vanishing derivative of response with respect to load

Only C yields the plateau class.
