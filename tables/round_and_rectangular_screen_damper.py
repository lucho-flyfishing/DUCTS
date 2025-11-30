"""
Round and Rectangular Screen Damper
Source: Standard HVAC loss coefficient tables

Inputs:
    n : float → free area ratio of screen (A1/Ao)
    A1_Ao : float → area ratio (A1/Ao)

Output:
    Co : float → loss coefficient
"""

# Table grid
_n_values = [0.2, 0.3, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 2.0, 2.5, 3.0, 4.0, 6.0]

_A1_Ao_values = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# Co table rows keyed by n
_Co_table = {
    0.2: [155, 75, 42, 24, 15, 8.0, 3.5, 0],
    0.3: [ 69, 33, 19, 11, 6.4, 3.6, 1.6, 0],
    0.4: [ 39, 19, 10, 6.1, 3.6, 2.0, 0.88, 0],
    0.6: [ 17, 8.3, 4.7, 2.7, 1.6, 0.89, 0.39, 0],
    0.8: [ 9.7, 4.7, 2.7, 1.5, 0.91, 0.50, 0.22, 0],
    1.0: [ 6.2, 3.0, 1.7, 0.97, 0.58, 0.32, 0.14, 0],
    1.2: [ 4.3, 2.1, 1.2, 0.67, 0.40, 0.22, 0.10, 0],
    1.4: [ 3.2, 1.5, 0.87, 0.49, 0.30, 0.16, 0.07, 0],
    1.6: [ 2.4, 1.2, 0.66, 0.38, 0.23, 0.12, 0.05, 0],
    2.0: [ 1.6, 0.75, 0.43, 0.24, 0.15, 0.08, 0.04, 0],
    2.5: [ 0.99, 0.48, 0.27, 0.16, 0.09, 0.05, 0.02, 0],
    3.0: [ 0.69, 0.33, 0.19, 0.11, 0.06, 0.04, 0.02, 0],
    4.0: [ 0.39, 0.19, 0.11, 0.06, 0.04, 0.02, 0.01, 0],
    6.0: [ 0.17, 0.08, 0.05, 0.03, 0.02, 0.01, 0,    0],
}


def _interp_1d(x, x0, x1, y0, y1):
    """Linear interpolation helper."""
    if x1 == x0:
        return y0
    return y0 + (y1 - y0) * ((x - x0) / (x1 - x0))


def _interp_table(x, x_list, y_table):
    """Interpolates row-wise (for n)."""
    if x <= x_list[0]:
        return y_table[x_list[0]]
    if x >= x_list[-1]:
        return y_table[x_list[-1]]

    for i in range(len(x_list) - 1):
        x0 = x_list[i]
        x1 = x_list[i + 1]
        if x0 <= x <= x1:
            row0 = y_table[x0]
            row1 = y_table[x1]
            return [
                _interp_1d(x, x0, x1, row0[j], row1[j])
                for j in range(len(row0))
            ]

    return y_table[x_list[-1]]


def get_co_round_rectangular_screen_damper(n: float, A1_Ao: float) -> float:
    """
    Returns Co for a round/rectangular screen damper.

    Bilinear interpolation:
    Step 1 → interpolate between table rows by n
    Step 2 → interpolate inside the row by A1/Ao
    """

    # Interpolate vertically (in n)
    row = _interp_table(n, _n_values, _Co_table)

    # Now interpolate horizontally (in A1/Ao)
    if A1_Ao <= _A1_Ao_values[0]:
        return float(row[0])
    if A1_Ao >= _A1_Ao_values[-1]:
        return float(row[-1])

    for i in range(len(_A1_Ao_values) - 1):
        x0 = _A1_Ao_values[i]
        x1 = _A1_Ao_values[i + 1]
        if x0 <= A1_Ao <= x1:
            return float(_interp_1d(A1_Ao, x0, x1, row[i], row[i + 1]))

    return float(row[-1])
