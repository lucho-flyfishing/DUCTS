# rectangular_butterfly_damper.py
# Computes Co for a Rectangular Butterfly Damper
# Based on Idelchik 1986, Diagram 9-17

# -------------------------------------------------------
# TABLE: Co values as a function of Type, H/W, and θ (deg)
# -------------------------------------------------------

# θ values (columns)
theta_values = [0, 10, 20, 30, 40, 50, 60, 65, 70]

# Rows represent:
# TYPE 1, H/W < 0.25
# TYPE 1, 0.25–1.0
# TYPE 2, H/W > 1.0

damper_table = {
    1: {
        "ranges": [(0.0, 0.25), (0.25, 1.0)],
        "Co": [
            # Type 1, H/W < 0.25
            [0.04, 0.30, 1.10, 3.00, 8.00, 23.0, 60.0, 100.0, 190.0],
            # Type 1, 0.25–1.0
            [0.08, 0.33, 1.20, 3.30, 9.00, 26.0, 70.0, 128.0, 210.0]
        ]
    },

    2: {
        "ranges": [(1.0, 9999.0)],  # H/W > 1.0
        "Co": [
            [0.13, 0.35, 1.30, 3.60, 10.0, 29.0, 80.0, 155.0, 230.0]
        ]
    }
}

# -------------------------------------------------------
# 1D interpolation (manual)
# -------------------------------------------------------

def interpolate_1d(x, xp, fp):
    """Linear interpolation without numpy."""
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
# Helper: find row based on H/W
# -------------------------------------------------------

def get_co_rectangular_butterfly_damper(TYPE, H_W):
    """
    Determines which row of the damper table applies.
    Returns (row_index).
    """

    ranges = damper_table[TYPE]["ranges"]

    for i, (low, high) in enumerate(ranges):
        if low <= H_W < high:
            return i

    # If H/W is exactly 1.0 for Type 1, choose the second row
    if TYPE == 1 and H_W == 1.0:
        return 1

    # Clamp to last row in unexpected cases
    return len(ranges)
