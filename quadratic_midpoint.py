"""Exact midpoint identity for f(x) = x^2.

The derivative at the midpoint equals the sum of the boundary
coordinates, and equals the average of the boundary derivatives.
Symmetric pairs that share a sum share the midpoint reading.
"""


def f(x: float) -> float:
    return x * x


def df(x: float) -> float:
    return 2.0 * x


def midpoint_reading(x1: float, x2: float) -> dict:
    m = 0.5 * (x1 + x2)
    secant = (f(x2) - f(x1)) / (x2 - x1)
    return {
        "boundaries": (x1, x2),
        "sum": x1 + x2,
        "midpoint": m,
        "derivative_at_midpoint": df(m),
        "average_of_boundary_derivatives": 0.5 * (df(x1) + df(x2)),
        "secant": secant,
    }


def main() -> None:
    pairs = ((2.0, 4.0), (-1.0, 7.0), (0.0, 6.0), (2.5, 3.5))
    for x1, x2 in pairs:
        row = midpoint_reading(x1, x2)
        assert row["derivative_at_midpoint"] == row["sum"]
        assert row["derivative_at_midpoint"] == row["average_of_boundary_derivatives"]
        assert row["derivative_at_midpoint"] == row["secant"]
        print(
            f"boundaries {row['boundaries']}: "
            f"sum = midpoint slope = average slope = secant = {row['sum']}"
        )


if __name__ == "__main__":
    main()
