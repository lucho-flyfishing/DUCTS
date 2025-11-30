# round_exit_bell.py
# Computes Co for Round Exit Bell (ASHRAE)

# -------------------------
# Table definition
# -------------------------

A_RATIO = [2, 4, 6, 10, 16]  # rows
THETA_DEG = [8, 10, 14, 20, 30, 45, 60]  # columns

CO_VALUES = [
    [0.36, 0.33, 0.37, 0.51, 0.90, 1.00, 1.00],  # A1/A0 = 2
    [0.24, 0.21, 0.28, 0.40, 0.70, 0.99, 1.00],  # 4
    [0.20, 0.19, 0.26, 0.37, 0.67, 0.99, 1.00],  # 6
    [0.18, 0.16, 0.24, 0.36, 0.68, 0.99, 1.00],  # 10
    [0.16, 0.16, 0.20, 0.36, 0.66, 0.99, 1.00],  # 16
]

# -------------------------
# Helper interpolation functions
# -------------------------

def interpolate_1d(x, xp, fp):
    """Simple linear interpolation for 1D arrays."""
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


def bilinear_interpolate(x, y, X, Y, table):
    """
    Bilinear interpolation:
    x = A1/A0
    y = theta
    """

    # 1) clamp values
    if x < X[0]: x = X[0]
    if x > X[-1]: x = X[-1]
    if y < Y[0]: y = Y[0]
    if y > Y[-1]: y = Y[-1]

    # 2) find bounding A_RATIO indices
    for i in range(len(X) - 1):
        if X[i] <= x <= X[i+1]:
            x0_i = i
            x1_i = i + 1
            break

    # 3) interpolate in Y (theta) for both bounding rows
    row0 = table[x0_i]
    row1 = table[x1_i]

    c0 = interpolate_1d(y, Y, row0)
    c1 = interpolate_1d(y, Y, row1)

    # 4) final interpolation between rows
    X0, X1 = X[x0_i], X[x1_i]
    return c0 + (c1 - c0) * (x - X0) / (X1 - X0)

# -------------------------
# Main function
# -------------------------

def get_co_round_exit_bell(A1_A0: float, theta: float) -> float:
    """
    Computes Co for a Round Exit Bell.
    Inputs:
        A1_A0 (float)
        theta (float): degrees
    Output:
        Co (float)
    """

    return float(bilinear_interpolate(
        A1_A0,
        theta,
        A_RATIO,
        THETA_DEG,
        CO_VALUES
    ))
