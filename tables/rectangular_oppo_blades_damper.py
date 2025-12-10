"""
Rectangular Damper, Opposed Blades
Source: Idelchik et al. 1986

Inputs:
    L_R : float   → ratio L/R (sum of blade lengths / duct perimeter)
    theta : float → blade angle in degrees (0, 10, 20, 30, 40, 50, 60, 70)

Output:
    Co : float → loss coefficient
"""

# Supported table values
_LR_values = [0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.5]

_theta_values = [0, 10, 20, 30, 40, 50, 60, 70]

# Co table (rows = L/R, columns = theta)
_Co_table = {
    0.3: [0.52, 0.85, 2.1, 4.1, 9, 21, 73, 284],
    0.4: [0.52, 0.92, 2.2, 5.0, 11, 28, 100, 332],
    0.5: [0.52, 1.0,  2.3, 5.4, 13, 33, 122, 377],
    0.6: [0.52, 1.0,  2.3, 6.0, 14, 38, 148, 411],
    0.8: [0.52, 1.1,  2.4, 6.6, 18, 54, 188, 495],
    1.0: [0.52, 1.2,  2.7, 7.3, 21, 65, 245, 547],
    1.5: [0.52, 1.4,  3.2, 9.0, 28, 107, 361, 677],
}


def _interp_1d(x, x0, x1, y0, y1):
    """Linear interpolation helper."""
    if x1 == x0:
        return y0
    return y0 + (y1 - y0) * ((x - x0) / (x1 - x0))


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

    return y_table[x_list[-1]]


def get_co_rectangular_oppo_blades_damper(L_R: float, theta: float) -> float:
    """
    Returns Co for a rectangular opposed-blade damper.

    Bilinear interpolation:
    - First interpolate on L/R → row of Co(θ)
    - Then interpolate inside that row for the given θ
    """
    # Step 1: interpolate across L/R → row
    row = _interp_table(L_R, _LR_values, _Co_table)

    # Step 2: interpolate across theta
    if theta <= _theta_values[0]:
        return float(row[0])
    if theta >= _theta_values[-1]:
        return float(row[-1])

    for i in range(len(_theta_values) - 1):
        t0 = _theta_values[i]
        t1 = _theta_values[i + 1]

        if t0 <= theta <= t1:
            return float(_interp_1d(theta, t0, t1, row[i], row[i + 1]))

    return float(row[-1])
