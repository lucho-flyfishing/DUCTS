import numpy as np
from scipy.interpolate import interp1d

# Data for "Exit, Round, with End Wall Transition"
# Source: Idelchik et al. 1986, Diagram 5-8
# θ = optimum angle (table provides θ but it is NOT an input — only L/D matters)

# L/D values from table
LD_values = np.array([0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 14.0])

# Corresponding Co values
Co_values = np.array([0.41, 0.32, 0.24, 0.20, 0.17, 0.15, 0.14, 0.12, 0.11, 0.11, 0.10])

# Create interpolation function
_co_interpolator = interp1d(
    LD_values,
    Co_values,
    kind="linear",
    bounds_error=False,
    fill_value=(Co_values[0], Co_values[-1])
)

def get_co_round_exit_wall_bell(L_over_D):
    """
    Returns the Co value for a Round Exit with End Wall Transition.
    Interpolates based on L/D.

    Parameters
    ----------
    L_over_D : float
        The L/D ratio.

    Returns
    -------
    float
        Interpolated Co value.
    """
    return float(_co_interpolator(L_over_D))