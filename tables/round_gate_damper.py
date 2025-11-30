# round_gate_damper.py
# Computes Co for a Round Gate Damper
# Based on Idelchik 1986, Diagram 9-5

# -------------------------------------------------------
# TABLE: Co vs h/D
# -------------------------------------------------------

h_over_D_values = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

Co_values = [35.0, 10.0, 4.6, 2.1, 0.98, 0.44, 0.17, 0.06]


# -------------------------------------------------------
# Manual 1D interpolation
# -------------------------------------------------------

def interpolate_1d(x, xp, fp):
    """Simple linear interpolation without numpy."""
    if x <= xp[0]:
        return fp[0]
    if x >= xp[-1]:
        return fp[-1]

    for i in range(len(xp) - 1):
        if xp[i] <= x <= xp[i+1]:
            x0, x1 = xp[i], xp[i+1]
            y0, y1 = fp[i], fp[i+1]
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    return fp[-1]


# -------------------------------------------------------
# MAIN FUNCTION
# -------------------------------------------------------

def get_co_round_gate_damper(h_over_D):
    """
    Computes Co for a Round Gate Damper.

    Parameter:
        h_over_D : float
            Ratio h/D from the diagram.

    Returns:
        float : Co
    """

    return float(interpolate_1d(h_over_D, h_over_D_values, Co_values))
