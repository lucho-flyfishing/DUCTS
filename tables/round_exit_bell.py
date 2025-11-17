"""
Table and interpolation for ROUND EXIT BELL
Source: ASHRAE – A1/A0 vs θ table for exit bells.
Rows: A1/A0 ratios
Columns: θ in degrees
Values: Co
"""

import numpy as np
from scipy.interpolate import RegularGridInterpolator

# --------------------------
# Table definition
# --------------------------

# A1/A0 values (rows)
A_RATIO = np.array([2, 4, 6, 10, 16])

# θ values (columns)
THETA_DEG = np.array([8, 10, 14, 20, 30, 45, 60])

# Co table
CO_VALUES = np.array([
    [0.36, 0.33, 0.37, 0.51, 0.90, 1.00, 1.00],   # A1/A0 = 2
    [0.24, 0.21, 0.28, 0.40, 0.70, 0.99, 1.00],   # 4
    [0.20, 0.19, 0.26, 0.37, 0.67, 0.99, 1.00],   # 6
    [0.18, 0.16, 0.24, 0.36, 0.68, 0.99, 1.00],   # 10
    [0.16, 0.16, 0.20, 0.36, 0.66, 0.99, 1.00],   # 16
])

# --------------------------
# Interpolator
# --------------------------

interpolator = RegularGridInterpolator(
    (A_RATIO, THETA_DEG),
    CO_VALUES,
    bounds_error=False,
    fill_value=None  # allow extrapolation (we clamp manually)
)

# --------------------------
# Main function
# --------------------------

def get_co_round_exit_bell(a_ratio: float, theta_deg: float) -> float:
    """
    Interpolate Co for a ROUND EXIT BELL.

    Parameters:
        a_ratio (float): A1/A0 ratio.
        theta_deg (float): Divergence angle θ in degrees.

    Returns:
        float: Co value (interpolated).
    """

    # Clamp to table limits
    a_clamped = np.clip(a_ratio, A_RATIO.min(), A_RATIO.max())
    t_clamped = np.clip(theta_deg, THETA_DEG.min(), THETA_DEG.max())

    point = np.array([a_clamped, t_clamped])

    co = interpolator(point)

    return float(co)