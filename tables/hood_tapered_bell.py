# tables/hood_tapered_bell.py
# Computes Co for tapered hoods (round or rectangular) using tabulated ASHRAE values.
# Uses linear interpolation.

import numpy as np
from scipy.interpolate import interp1d


# ============================================================
#  ROUND HOOD TABLE
# ============================================================

# Angles (degrees)
theta_round = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180], dtype=float)

# Corresponding Co values
Co_round = np.array([1.00, 0.11, 0.06, 0.09, 0.14, 0.18, 0.27, 0.32, 0.43, 0.50], dtype=float)

# Interpolator
_interp_round = interp1d(
    theta_round,
    Co_round,
    kind="linear",
    fill_value="extrapolate",
    bounds_error=False
)


# ============================================================
#  RECTANGULAR / SQUARE HOOD TABLE
# ============================================================

theta_rect = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180], dtype=float)

Co_rect = np.array([1.00, 0.19, 0.13, 0.16, 0.21, 0.27, 0.33, 0.43, 0.53, 0.62], dtype=float)

_interp_rect = interp1d(
    theta_rect,
    Co_rect,
    kind="linear",
    fill_value="extrapolate",
    bounds_error=False
)


# ============================================================
#  PUBLIC FUNCTION
# ============================================================

def get_co_hood_tapered_bell(theta, shape):
    """
    Returns Co for a tapered hood (round or rectangular).

    Parameters
    ----------
    theta : float
        Hood angle θ in degrees.

    shape : str
        "round"   → use round hood table
        "rect"    → use square/rectangular table

    Returns
    -------
    float : interpolated Co
    """

    shape = shape.lower().strip()

    if shape == "round":
        return float(_interp_round(theta))

    elif shape in ("rect", "rectangular", "square"):
        return float(_interp_rect(theta))

    else:
        raise ValueError(
            f"Shape '{shape}' not recognized. Use 'round' or 'rect'."
        )