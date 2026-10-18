# BETAN late-window slope and curvature feature analysis

Date: 18 October 2026

## Feature table

302 shots, all status_feat = ok. Columns include euler_slope, group (neutral/positive/negative), and derived statistics (euler_mean, euler_std, euler_max, burst counts, z_end, etc.).

## Group counts (from prior window analysis)

- neutral: 146
- positive: 88
- negative: 68

Thresholds based on IQR of euler_slope.

## Top differentiating features (gold vs rest)

Gold defined as positive-slope group. Largest standardized differences:

- euler_slope / euler_slope_raw: abs_std_diff_d ≈ 1.39
- euler_max: ≈ 0.96
- euler_std: ≈ 0.95
- euler_mean: ≈ 0.84

Other features (z_end, frac_down, std_ratio) show smaller differences (≈ 0.25 or less).

## Median values by group

- euler_slope: negative ≈ -1.11, neutral ≈ -0.06, positive ≈ 1.39
- euler_max and euler_std higher in positive group
- z_end similar across groups (≈ 0.92–1.11)

## Interpretation status

The late-window slope on BETAN stratifies shots. Curvature traces show sparse spikes rather than smooth sustained curvature. Interior-versus-edge refinements reduce sensitivity to terminal artifacts. These are empirical rankings of response features on labeled windows. They do not establish a derived dynamical law, a topological transition, or a predictive disruption model. The kinematic grammar remains unchanged; the numbers come from the data.

## Framework connection (as used)

Midpoint identity and curvature remainder have been used as diagnostics on time series. On linear segments the remainder is zero by construction. Non-zero spikes flag localized deviations. This is consistent with using the tool to characterize regimes, not to select a new geometric shape.
