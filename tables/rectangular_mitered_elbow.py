# rectangular_mitered_elbow.py
# Calculates Co for Rectangular Mitered Elbows (Idelchik 1986, Diagram 6-5)

import numpy as np
from app_state import app_state

# ------------------------------
# TABULATED C' VALUES (θ° vs H/W)
# ------------------------------

theta_values = np.array([20, 30, 45, 60, 75, 90])

hw_values = np.array([0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0])

c_prime_table = np.array([
    [0.08, 0.08, 0.08, 0.07, 0.07, 0.07, 0.06, 0.06, 0.05, 0.05, 0.05],  # 20°
    [0.18, 0.17, 0.17, 0.16, 0.15, 0.15, 0.13, 0.13, 0.12, 0.12, 0.11],  # 30°
    [0.38, 0.37, 0.36, 0.34, 0.33, 0.31, 0.28, 0.27, 0.26, 0.25, 0.24],  # 45°
    [0.60, 0.59, 0.57, 0.55, 0.52, 0.49, 0.46, 0.43, 0.41, 0.39, 0.38],  # 60°
    [0.89, 0.87, 0.84, 0.81, 0.77, 0.73, 0.67, 0.63, 0.61, 0.58, 0.57],  # 75°
    [1.30, 1.30, 1.20, 1.20, 1.10, 1.10, 0.98, 0.92, 0.89, 0.85, 0.83],  # 90°
])

# ---------------------------------
# REYNOLDS CORRECTION FACTOR (K_Re)
# ---------------------------------

re_values = np.array([1, 2, 3, 4, 6, 8, 10, 14])

k_re_values = np.array([1.40, 1.26, 1.19, 1.14, 1.09, 1.06, 1.04, 1.00])


def interpolate_1d(x, xp, fp):
    """Linear 1D interpolation with edge handling."""
    if x <= xp[0]:
        return fp[0]
    if x >= xp[-1]:
        return fp[-1]
    return np.interp(x, xp, fp)


def interpolate_2d(x, y, x_points, y_points, table):
    """
    Bilinear interpolation:
    x = θ
    y = H/W
    """
    # Clamp values to domain
    x = max(min(x, x_points[-1]), x_points[0])
    y = max(min(y, y_points[-1]), y_points[0])

    # Interpolate across θ rows first
    c_at_hw = np.array([
        np.interp(y, y_points, row) for row in table
    ])

    # Final interpolation across θ
    return np.interp(x, x_points, c_at_hw)


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

    # 1) Interpolate C'
    c_prime = interpolate_2d(
        theta_deg,
        H_over_W,
        theta_values,
        hw_values,
        c_prime_table
    )

    # 2) Compute K_Re from Re×10⁻⁴
    Re_scaled = app_state.Re / 1e4
    k_re = interpolate_1d(Re_scaled, re_values, k_re_values)

    # 3) Final Co
    Co = k_re * c_prime

    print(f"[DEBUG] Rectangular Mitered Elbow → θ={theta_deg}, H/W={H_over_W}")
    print(f"[DEBUG] C'={c_prime:.4f},  K_Re={k_re:.3f},  Co={Co:.4f}")

    return Co
