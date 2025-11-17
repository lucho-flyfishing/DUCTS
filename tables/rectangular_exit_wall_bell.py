import numpy as np
from scipy.interpolate import interp1d

# Data taken from Idelchik / ASHRAE diagram 5-10 (Exit, Rectangular, With Wall)
L_over_H_values = np.array([0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 14.0])
Co_values = np.array([0.53, 0.44, 0.35, 0.31, 0.28, 0.25, 0.24, 0.22, 0.20, 0.19, 0.19])

# Create 1D interpolation function for Co(L/H)
_co_interp = interp1d(
    L_over_H_values,
    Co_values,
    kind="linear",
    fill_value="extrapolate"
)

def get_co_rectangular_exit_wall_bell(L_H: float) -> float:
    """
    Returns interpolated Co for:
    - Exit, Rectangular, With Wall, Two Sides Parallel, Symmetrical, Diverging
    Based on Idelchik / ASHRAE diagram 5-10.
    """
    return float(_co_interp(L_H))