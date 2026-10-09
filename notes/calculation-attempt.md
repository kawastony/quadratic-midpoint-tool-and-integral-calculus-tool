# Calculation attempt

Date: 9 October 2026

Same targets as the paper appendices, recomputed from the quadratic-midpoint dynamic. The dynamic supplies a midpoint, a closing interval, a fixed volume, a fixed circumference, and a fixed arrival time. It does not supply cone angles, a baryonic mass, a SPARC sample, a redshift, or a compactification scale. Those paper inputs were not invented in order to force a match.

## What the new dynamic actually evaluates

For f(x) = x^2, midpoint 3, half-width w:

integral from 3-w to 3+w of 2x dx = 12 w.

At the boundaries used in the record: w = 4 gives area 48; w = 1 gives area 12. The slope reading stays 6. The accumulated change shrinks with the gap.

Fixed arrival time T, length L, volume held fixed:

v = L/T
specific kinetic energy = (1/2) (L/T)^2

So doubling L at fixed T doubles speed and quadruples kinetic energy. The impulse required between pauses is (L' - L)/T. None of these expressions contains G, M, or an angle.

## Paper targets, and whether this dynamic reaches them

1. Flat rotation curve, Paper 9 Appendix A.1: v_inf = (Lambda_*^2 G M mu)^(1/4). The new dynamic gives v = L/T. Matching a galactic speed requires putting the mass into T or L by hand. Example only: 200 km/s across 10 kpc is a transit time of about 4.9 x 10^7 years. That is a unit conversion, not a derivation of the quarter-power law. Not reproduced.

2. Gas-disk MAE, 0.080 to 0.051 dex. No SPARC residuals live in the midpoint dynamic. Not reproduced.

3. Freeze at z ~ 0.35 and the Planck densities. The paper integrates a winding equation with H(t) and Omega_DM already in it. The new dynamic has an active phase and a pause, but no redshift. Not reproduced.

4. Mediator mass 18.7 eV. Paper 9 Appendix A.4 inserts c_twist ~ 0.00725, mu_compact ~ 1.6 PeV, and f_epsilon from psi_1, psi_2. The midpoint dynamic has no energy scale. Not reproduced.

5. Dark hierarchy. Paper 9 Appendix A.5 states psi_1 = 58.74 deg, psi_2 = 82.80 deg, and Lambda_dark / Lambda_QCD = sin(psi_2)/sin(psi_1) ~ 3.138, then Lambda_dark = 659 MeV and M_B^dark = 957 MeV. Recomputed from those angles, sin(82.80 deg)/sin(58.74 deg) = 1.161, not 3.138. The factor 659/3.138 ~ 210 MeV is the QCD scale they divided by, so 3.138 was not produced by the sine of the stated angles. The midpoint boundaries 2 and 4, or -1 and 7, do not generate either number. Not reproduced. The paper statement also does not check out on its own inputs.

6. Dark Shield 10^-2 to 10^-3, and epsilon_H less than or about 10^-10 GeV. Both are loop and charge-cancellation claims in Paper 9 Appendices A.6 and A.7. No charge or loop is defined by the closing interval. Not reproduced.

7. Pause scale r_p = 1/mu, and multiplicity n = 8 from N_wind = 10.28 with an image factor 2 (Paper 25 Appendices B and C). The new pause is a phase of the elongation, not an inverse length, and it does not count windings. Not reproduced.

## Result

The new dynamic reproduces its own identities: midpoint slope 6, area 12w, speed L/T, energy growing as L^2. It does not reproduce the paper outputs. The paper outputs that were checked depend on cone angles, a mass, a Hubble history, or an inserted scale. One stated paper identity, the sine ratio 3.138, is not recovered from the angles written next to it.
