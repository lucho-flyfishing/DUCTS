# rectangular_mitered_elbow.py
# Calculates Co for Rectangular Mitered Elbows (Idelchik 1986, Diagram 6-5)

from app_state import app_state

# ------------------------------
# TABULATED C' VALUES (θ° vs H/W)
# ------------------------------

theta_values = [20, 30, 45, 60, 75, 90]

hw_values = [0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0]

c_prime_table = [
    [0.08, 0.08, 0.08, 0.07, 0.07, 0.07, 0.06, 0.06, 0.05, 0.05, 0.05],  # 20°
    [0.18, 0.17, 0.17, 0.16, 0.15, 0.15, 0.13, 0.13, 0.12, 0.12, 0.11],  # 30°
    [0.38, 0.37, 0.36, 0.34, 0.33, 0.31, 0.28, 0.27, 0.26, 0.25, 0.24],  # 45°
    [0.60, 0.59, 0.57, 0.55, 0.52, 0.49, 0.46, 0.43, 0.41, 0.39, 0.38],  # 60°
    [0.89, 0.87, 0.84, 0.81, 0.77, 0.73, 0.67, 0.63, 0.61, 0.58, 0.57],  # 75°
    [1.30, 1.30, 1.20, 1.20, 1.10, 1.10, 0.98, 0.92, 0.89, 0.85, 0.83],  # 90°
]

# ---------------------------------
# REYNOLDS CORRECTION FACTOR (K_Re)
# ---------------------------------

re_values = [1, 2, 3, 4, 6, 8, 10, 14]
k_re_values = [1.40, 1.26, 1.19, 1.14, 1.09, 1.06, 1.04, 1.00]


# ---------------------
# INTERPOLATION HELPERS
# ---------------------

def _find_bracket(values, x):
    """Return indices i, i+1 such that values[i] <= x <= values[i+1]."""
    if x <= values[0]:
        return 0, 0
    if x >= values[-1]:
        return len(values) - 1, len(values) - 1

    for i in range(len(values) - 1):
        if values[i] <= x <= values[i + 1]:
            return i, i + 1

    return len(values) - 1, len(values) - 1


def _linear_interpolate(x, x0, x1, y0, y1):
    """Simple linear interpolation."""
    if x1 == x0:
        return y0
    t = (x - x0) / (x1 - x0)
    return y0 * (1 - t) + y1 * t


def interpolate_1d(x, xp, fp):
    """Linear 1D interpolation with edge behavior."""
    if x <= xp[0]:
        return fp[0]
    if x >= xp[-1]:
        return fp[-1]

    i0, i1 = _find_bracket(xp, x)
    return _linear_interpolate(x, xp[i0], xp[i1], fp[i0], fp[i1])


def interpolate_2d(x, y, x_points, y_points, table):
    """
    Bilinear interpolation on 2D table:
    x = θ
    y = H/W
    """
    # Clamp
    if x <= x_points[0]:
        row_low = row_high = 0
    elif x >= x_points[-1]:
        row_low = row_high = len(x_points) - 1
    else:
        row_low, row_high = _find_bracket(x_points, x)

    # First interpolate each row in y
    row_interp_values = []
    for row_index in range(len(table)):
        row = table[row_index]
        i0, i1 = _find_bracket(y_points, y)
        val = _linear_interpolate(
            y,
            y_points[i0], y_points[i1],
            row[i0], row[i1]
        )
        row_interp_values.append(val)

    # Now interpolate between the two θ rows
    return _linear_interpolate(
        x,
        x_points[row_low], x_points[row_high],
        row_interp_values[row_low], row_interp_values[row_high]
    )


# -----------------------
# MAIN PUBLIC FUNCTION
# -----------------------

def get_co_rectangular_mitered_elbow(theta_deg, H_over_W):
    """
    Computes Co for Rectangular Mitered Elbow.

    Inputs:
        theta_deg (float): Angle in degrees
        H_over_W (float): H/W geometric ratio
        app_state.Re (float): Reynolds number

    Output:
        Co (float)
    """

    if app_state.Re is None:
        print("ERROR: app_state.Re is missing. Cannot compute K_Re.")
        return None

    # 1) C'
    c_prime = interpolate_2d(
        theta_deg,
        H_over_W,
        theta_values,
        hw_values,
        c_prime_table
    )

    # 2) Reynolds correction: Re × 10⁻⁴
    Re_scaled = app_state.Re / 1e4
    k_re = interpolate_1d(Re_scaled, re_values, k_re_values)

    # 3) Final loss coefficient Co
    Co = k_re * c_prime

    print(f"[DEBUG] Rectangular Mitered Elbow → θ={theta_deg}, H/W={H_over_W}")
    print(f"[DEBUG] C'={c_prime:.4f},  K_Re={k_re:.3f},  Co={Co:.4f}")

    return Co
