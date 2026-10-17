# TCV L-H diagnostic results status

Date: 17 October 2026

## Population-level markers (fixed-window pre/post)

- **Wtot** (stored energy): strongest symmetric marker.
  - L→H (n=43): positive in 35/43 (81%), p ≈ 2.1e-5.
  - H→L (n=144): negative in 129/144 (90%), p ≈ 4.3e-24.
- **dW/dt**: strong for L→H (37/43 positive, p ≈ 8.2e-7); not robust for H→L under present windows (sign fraction ~51%, p=0.40).
- **PSOL_RT**: no robust universal pre/post sign shift in either direction.

## Onset timing attempts

- Threshold-style dW/dt rise detection is boundary-censored. Windows of 50, 100, and 200 ms show pile-up at the horizon. The method supplies a lower bound, not a resolved onset time.
- Piecewise-linear breakpoint fits on Wtot: high-quality subset (R² > 0.95, m2 > m1) yields 13 of 31 candidates. Median lead relative to label t0 ≈ -10 ms. Wilcoxon p = 0.080. Suggestive of near-coincident or modestly pre-label slope change in clean events; not statistically significant.

## Status

The diagnostic ranks observables by robustness on labeled TCV transitions. Wtot is the primary population-level marker. Derivative and breakpoint methods are useful for characterizing dynamics in subsets but do not yet establish a resolved precursor or a universal onset clock. No independent edge diagnostics (shear, turbulence, pedestal) were coupled. The result is empirical ranking, not a derived dynamical law.
