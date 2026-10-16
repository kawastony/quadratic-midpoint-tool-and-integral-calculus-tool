# u-z coupling comparison

Date: 16 October 2026

## Target
Synthetic coordination Z from published O’Hern / Majmudar square-root scaling above Zc = 6.

## Results
| Model | RMSE | Best params |
|-------|------|-------------|
| UZ-1 smooth power | 0.191 | z0=6, a=2, m=1.5 |
| UZ-2 delayed | 0.257 | z0=6, a=2, m=1, uc=0.03 |
| UZ-3 logistic | 0.489 | z0=5.5, dz=2, k=50, uc=0.02 |

## Verdict
On this synthetic continuous rise, UZ-1 (smooth power law) has the lowest RMSE. The delayed threshold (UZ-2) is not required to match the published square-root scaling once the isostatic jump has already occurred. The logistic form over-smoothes the onset.

## Interpretation
For the post-jamming continuous rise, smooth coupling is sufficient. The discontinuous onset itself remains a Tier 2 feature outside the continuous bridge laws. Protocol dependence and true experimental noise are not tested here.
