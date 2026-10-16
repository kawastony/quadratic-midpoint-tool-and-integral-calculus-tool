# Packing-bound derivation attempt

Date: 16 October 2026

## Setup
Shell index n, radius r_n, transmission T_n, strain u_n = -ln T_n.
Volume of shell n is fixed by the constitution (exact volume). Circumference of the deep end is fixed. Far end may adjust.

## Question
Do the fixed volume and fixed deep-end circumference imply a hard or soft upper bound on local strain u_n?

## Attempt
Fixed volume for a conical shell element: (1/3) π h (R_outer^{2} + R_outer R_inner + R_inner^{2}) = constant.
Fixed deep-end circumference: 2π R_deep = constant.
Elongation changes height h while the deep radius stays fixed. The far radius adjusts to keep volume exact.

Local strain u_n is defined from transmission, not directly from geometric compression. The constitution links transmission to cumulative shell attenuation, not to a packing density of an underlying material.

No relation of the form u_n ≤ u_star is forced. The geometric constraints determine how the far radius must change with h, but they do not bound the attenuation per shell. Transmission can in principle continue to drop without a geometric cutoff.

## Result
No-go. The volume and circumference constraints do not imply a packing bound on u. A saturating branch in V(u) remains an additional constitutive assumption, not a geometric necessity.

## Implication
Route 3 fails. The jammed plateau is not derived from the locked laws. It must be supplied by a material rule (Route 1 or 2) or retained as an effective input.
