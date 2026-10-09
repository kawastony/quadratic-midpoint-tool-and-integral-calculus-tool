# What integral calculus sees

Date: 9 October 2026

Integral calculus on these dynamics shows three different ledgers, and none of them is a constant gravity.

## Quadratic interval

The midpoint slope stays \(6\) while the boundaries close. The integral across that interval does not stay \(6\). With the midpoint at \(3\) and half-width \(w\),

\[
\int_{3-w}^{3+w} 2x\,\mathrm dx = 12w.
\]

That is the midpoint slope times the width. As the boundaries come together, \(w\to 0\) and the area under the derivative collapses to \(0\). The slope reading is unchanged. The accumulated change in \(x^2\) across the interval vanishes in proportion to the gap.

Integrating the constant midpoint slope in time, instead of across the gap, only gives \(6t\): a clock, not a well.

## Closing speed

The closing speed integrates to a distance. If the boundaries approach the midpoint at speed \(u\),

\[
\int u\,\mathrm dt
\]

is how far they have come together. It becomes an acceleration only after differentiating \(u\), not by integrating it. The integral of the closing speed is the shrinkage of the interval.

## Fixed arrival time

The fixed arrival time is already an integral constraint,

\[
T=\int_0^{L}\frac{\mathrm dx}{v(x)}.
\]

Holding \(T\) fixed while \(L\) grows forces the average speed to be \(L/T\). The integral of velocity over one trip equals the current length,

\[
\int_0^{T} v\,\mathrm dt = L,
\]

so each longer funnel shows a larger distance covered in the same time. The integral of acceleration over that trip is only the net gain in speed, \(v_{\mathrm{end}}-v_{\mathrm{start}}\). On a pause, with a launch speed already equal to \(L/T\), that gain is zero: the integral of acceleration during the run is \(0\). The nonzero impulse sits between pauses, where the launch speed has to be raised from \(L/T\) to \(L'/T\),

\[
\int a\,\mathrm dt = \frac{L'-L}{T}.
\]

## Energy

Volume is fixed, so a faster stream in the same volume carries kinetic energy proportional to \(v^2\), hence to \(L^2\). The work integral of pressure times wall speed has to supply that increase if the liquid is ideal; it is paid by whatever is stretching the funnel. Viscous dissipation shows up as a separate positive integral, \(\int \tau:\nabla v\,\mathrm dV\), and that term is a loss. The gravitational term appears only if the stretch is vertical, as \(\int \rho g\,\Delta h\,\mathrm dV\), and it does not grow like \(L^2\) merely because the arrival time was held fixed.

The integrals show a shrinking area under a constant midpoint slope, a closing distance, a rising trip length in a fixed time, and an energy cost that grows like \(L^2\) as the funnel elongates without bound. They do not show a constant \(g\).
