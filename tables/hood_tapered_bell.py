# tables/hood_tapered_bell.py
# Computes Co for tapered hoods (round or rectangular) using tabulated ASHRAE values.
# Pure Python version (no numpy, no scipy).


# ============================================================
#  ROUND HOOD TABLE
# ============================================================

theta_round = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180]

Co_round = [1.00, 0.11, 0.06, 0.09, 0.14, 0.18, 0.27, 0.32, 0.43, 0.50]


# ============================================================
#  RECTANGULAR / SQUARE HOOD TABLE
# ============================================================

theta_rect = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180]

Co_rect = [1.00, 0.19, 0.13, 0.16, 0.21, 0.27, 0.33, 0.43, 0.53, 0.62]


# ============================================================
#  LINEAR INTERPOLATION UTILITY
# ============================================================

def linear_interp(x, xp, fp):
    """
    Replacement for numpy/scipy interp1d.
    Performs linear interpolation or extrapolation.

    xp: list of x values (sorted)
    fp: list of corresponding y values
    """

    # Below minimum → extrapolate linearly
    if x <= xp[0]:
        x0, x1 = xp[0], xp[1]
        y0, y1 = fp[0], fp[1]
        return y0 + (x - x0) * (y1 - y0) / (x1 - x0)

    # Above maximum → extrapolate linearly
    if x >= xp[-1]:
        x0, x1 = xp[-2], xp[-1]
        y0, y1 = fp[-2], fp[-1]
        return y0 + (x - x0) * (y1 - y0) / (x1 - x0)

    # Find interval
    for i in range(len(xp) - 1):
        if xp[i] <= x <= xp[i + 1]:
            x0 = xp[i]
            x1 = xp[i + 1]
            y0 = fp[i]
            y1 = fp[i + 1]
            return y0 + (x - x0) * (y1 - y0) / (x1 - x0)

    # Should never happen
    return fp[-1]


# ============================================================
#  PUBLIC FUNCTION
# ============================================================

def get_co_hood_tapered_bell(theta, shape):
    """
    Returns Co for a tapered hood (round or rectangular).

    Parameters
    ----------
    theta : float
        Hood angle θ in degrees.

    shape : str
        "round"   → use round hood table
        "rect"    → use square/rectangular table

    Returns
    -------
    float : interpolated Co
    """

    shape = shape.lower().strip()

    if shape == "round":
        return float(linear_interp(theta, theta_round, Co_round))

    elif shape in ("rect", "rectangular", "square"):
        return float(linear_interp(theta, theta_rect, Co_rect))

    else:
        raise ValueError(
            f"Shape '{shape}' not recognized. Use 'round' or 'rect'."
        )
