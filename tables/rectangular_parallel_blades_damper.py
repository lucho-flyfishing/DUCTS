"""
Rectangular Damper, Parallel Blades
Source: Idelchik et al. 1986, Diagram 9-5 (Brown and Fellows 1957)

Inputs:
    L_R : float   → ratio L/R  (sum of blade lengths / duct perimeter)
    theta : float → blade angle in degrees (0, 10, 20, 30, 40, 50, 60, 70)

Output:
    Co : float    → loss coefficient
"""

# Supported table values
_LR_values = [0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.5]

_theta_values = [0, 10, 20, 30, 40, 50, 60, 70]

# Co matrix (rows = L/R, columns = theta)
# From the table in Idelchik.
_Co_table = {
    0.3: [0.52, 0.79, 1.4, 2.3, 5.0, 9, 14, 32],
    0.4: [0.52, 0.85, 1.5, 2.4, 5.0, 9, 16, 38],
    0.5: [0.52, 0.92, 1.5, 2.4, 5.0, 9, 18, 45],
    0.6: [0.52, 0.92, 1.5, 2.4, 5.4, 9, 21, 45],
    0.8: [0.52, 0.92, 1.5, 2.5, 5.4, 9, 22, 55],
    1.0: [0.52, 1.0,  1.6, 2.6, 5.4, 10, 24, 65],
    1.5: [0.52, 1.0,  1.6, 2.7, 5.4, 10, 28, 102],
}


def _interp_1d(x, x0, x1, y0, y1):
    """Linear interpolation helper."""
    if x1 == x0:
        return y0
    return y0 + (y1 - y0) * ( (x - x0) / (x1 - x0) )


def _interp_table(x, x_list, y_table):
    """
    Interpolates in 1D for x.
    x_list must be sorted.
    """
    if x <= x_list[0]:
        return y_table[x_list[0]]

    if x >= x_list[-1]:
        return y_table[x_list[-1]]

    for i in range(len(x_list) - 1):
        x0 = x_list[i]
        x1 = x_list[i + 1]

        if x0 <= x <= x1:
            y0 = y_table[x0]
            y1 = y_table[x1]

            return [
                _interp_1d(x, x0, x1, y0[j], y1[j])
                for j in range(len(y0))
            ]

    # Should never reach here
    return y_table[x_list[-1]]


def get_co_rectangular_parallel_blades_damper(L_R: float, theta: float) -> float:
    """
    Returns Co for a rectangular parallel-blade damper.

    Performs bilinear interpolation:
    - First interpolate on L/R between table rows.
    - Then interpolate on θ between table columns.
    """
    # Step 1: interpolate across L/R → get a row of Co(θ)
    row = _interp_table(L_R, _LR_values, _Co_table)

    # Step 2: interpolate across θ inside that row
    # clamp theta to min/max
    if theta <= _theta_values[0]:
        return float(row[0])
    if theta >= _theta_values[-1]:
        return float(row[-1])

    # find bounding angles
    for i in range(len(_theta_values) - 1):
        t0 = _theta_values[i]
        t1 = _theta_values[i + 1]

        if t0 <= theta <= t1:
            return float(_interp_1d(theta, t0, t1, row[i], row[i + 1]))

    # safety fallback
    return float(row[-1])
