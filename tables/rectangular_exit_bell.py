import numpy as np
from scipy.interpolate import RegularGridInterpolator

# -----------------------------------------
# Data for: Exit, Rectangular, Two Sides Parallel, Diverging, Symmetrical
# Idelchik et al. 1986 – Diagram 11-6
# -----------------------------------------

# Independent variables
A1_over_A0_values = np.array([2, 4, 6])
theta_values = np.array([8, 10, 14, 20, 30, 45, 60])  # using 60 for ≥60

# Co table
Co_table = np.array([
    # θ =  8     10     14     20     30     45     ≥60
    [0.50, 0.51, 0.56, 0.63, 0.80, 0.96, 1.00],  # A1/A0 = 2
    [0.34, 0.38, 0.48, 0.63, 0.76, 0.91, 1.00],  # A1/A0 = 4
    [0.32, 0.34, 0.41, 0.56, 0.70, 0.84, 0.96]   # A1/A0 = 6
])

# Interpolator setup
_interpolator = RegularGridInterpolator(
    (A1_over_A0_values, theta_values),
    Co_table,
    bounds_error=False,
    fill_value=None
)

def get_co_rectangular_exit_bell(A1_A0, theta):
    """
    Returns the Co value for a Rectangular Exit Bell (Two Sides Parallel Diverging).

    Parameters
    ----------
    A1_A0 : float
        Ratio A1/A0.
    theta : float
        Divergence angle in degrees.

    Returns
    -------
    float
        Bilinearly interpolated Co value.
    """

    # Clamp values outside table range
    A1_clamped = np.clip(A1_A0, A1_over_A0_values[0], A1_over_A0_values[-1])
    theta_clamped = np.clip(theta, theta_values[0], theta_values[-1])

    Co = _interpolator([[A1_clamped, theta_clamped]])[0]
    return float(Co)