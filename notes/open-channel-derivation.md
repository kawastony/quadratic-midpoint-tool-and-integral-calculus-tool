# Open-channel depletion derivation attempt

Date: 16 October 2026

## Hypothesis
Each shell has N_star transmissive microchannels. Let N_n be the number remaining open. Define the consumed fraction
phi_n = 1 - N_n / N_star.
Identify the strain with the consumed fraction: u_n = u_star * phi_n, so 0 <= u_n < u_star.

## Counting
Suppose the number of accessible microstates for a shell scales as
Omega_n proportional to (1 - phi_n)^mu = (1 - u_n / u_star)^mu.
The configurational free-energy cost is then
F_n = -ln Omega_n = -mu ln(1 - u_n / u_star) + const.

## Elastic branch
Add the weak-field quadratic term by hand (or from a separate harmonic expansion of residual channels):
V(u) = (m^2 / 2) u^2 - mu ln(1 - u / u_star) - (mu / u_star) u.
The linear subtraction enforces V'(0) = 0.

## Result
The logarithmic barrier is recovered from a microstate counting assumption. The assumption itself (Omega proportional to remaining open channels to a power) is not derived from the locked laws. It is a statistical hypothesis placed on top of the shell product.

## Status
Toy derivation of the functional form of Candidate C. The capacity ceiling is introduced by the finite number of channels, not forced by the kinematic constitution. The locked laws remain unchanged. The barrier is an additional constitutive axiom.
