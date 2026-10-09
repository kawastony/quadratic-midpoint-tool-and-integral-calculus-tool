"""Constitution tool.

The story is the law. Active acceleration is gravity.
Pause holds speed. The observer does not change either.
"""


def cycle(n, g, tau, alpha, alpha_exit=1.0):
    """n equal pairs of deep voice then soft voice.

    a = g on the active phase, 0 on the pause.
    tau is the shared duration.
    alpha is acceptance. It does not enter v or g.
    Exit opens only if alpha reaches alpha_exit.
    """
    v = 0.0
    s = 0.0
    rows = []
    for k in range(1, n + 1):
        s += v * tau + 0.5 * g * tau * tau
        v += g * tau
        rows.append({"phase": "deep", "k": k, "v": v, "s": s, "a": g})
        s += v * tau
        rows.append({"phase": "soft", "k": k, "v": v, "s": s, "a": 0.0})
    return {
        "v": v,
        "s": s,
        "g": g,
        "tau": tau,
        "alpha": alpha,
        "exits": alpha >= alpha_exit,
        "rows": rows,
    }


def main():
    g = 9.81
    tau = 1.0
    for alpha in (0.0, 1.0):
        out = cycle(3, g, tau, alpha)
        print(
            f"alpha={alpha}: v={out['v']:.2f} m/s after 3 deep voices, "
            f"s={out['s']:.2f} m, exit={out['exits']}"
        )
        for row in out["rows"]:
            print(
                f"  {row['phase']} {row['k']}: a={row['a']}, "
                f"v={row['v']:.2f}, s={row['s']:.2f}"
            )


if __name__ == "__main__":
    main()
