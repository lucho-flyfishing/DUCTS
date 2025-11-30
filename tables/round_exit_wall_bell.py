# round_exit_wall_bell.py
# Exit, Round, with End Wall Transition
# Idelchik 1986 – Diagram 5-8
# Interpolates Co as a function of L/D

# --------------------------
# Table data
# --------------------------

LD_values = [0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 14.0]

Co_values = [0.41, 0.32, 0.24, 0.20, 0.17, 0.15, 0.14, 0.12, 0.11, 0.11, 0.10]

# --------------------------
# Helper: manual 1D interpolation
# --------------------------

def interpolate_1d(x, xp, fp):
    """Linear 1D interpolation without numpy."""
    # left clamp
    if x <= xp[0]:
        return fp[0]
    # right clamp
    if x >= xp[-1]:
        return fp[-1]

    # find interval
    for i in range(len(xp) - 1):
        if xp[i] <= x <= xp[i+1]:
            x0, x1 = xp[i], xp[i+1]
            y0, y1 = fp[i], fp[i+1]
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    # fallback
    return fp[-1]

# --------------------------
# Main function
# --------------------------

def get_co_round_exit_wall_bell(L_D):
    """
    Computes Co for Exit, Round, with End Wall Transition.
    Interpolates based on L/D (Idelchik Diagram 5-8).

    Parameters:
        L_D (float): L/D geometric ratio.

    Returns:
        float: Co value.
    """

    return float(interpolate_1d(L_D, LD_values, Co_values))
