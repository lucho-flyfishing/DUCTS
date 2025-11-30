"""
Exit, Rectangular, With Wall, Two Sides Parallel, Symmetrical, Diverging
Idelchik / ASHRAE diagram 5-10
Interpolación lineal sin numpy ni scipy
"""

# Tabla original
L_over_H_values = [0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 14.0]
Co_values =       [0.53, 0.44, 0.35, 0.31, 0.28, 0.25, 0.24, 0.22, 0.20, 0.19, 0.19]


def _find_bracket(values: list, x: float):
    """Devuelve índices i, i+1 tales que values[i] ≤ x ≤ values[i+1]."""
    if x <= values[0]:
        return 0, 0
    if x >= values[-1]:
        return len(values) - 1, len(values) - 1

    for i in range(len(values) - 1):
        if values[i] <= x <= values[i + 1]:
            return i, i + 1

    return len(values) - 1, len(values) - 1


def _linear_interpolate(x, x0, x1, y0, y1):
    """Interpolación lineal simple."""
    if x1 == x0:
        return y0
    t = (x - x0) / (x1 - x0)
    return y0 * (1 - t) + y1 * t


def get_co_rectangular_exit_wall_bell(L_H: float) -> float:
    """
    Returns interpolated Co for:
    - Exit, Rectangular, With Wall, Two Sides Parallel, Symmetrical, Diverging
    Based on Idelchik / ASHRAE diagram 5-10.

    Parámetro:
        L_H (float): relación L/H
    Retorna:
        float: Co interpolado
    """
    # Clamp interno
    if L_H <= L_over_H_values[0]:
        return float(Co_values[0])
    if L_H >= L_over_H_values[-1]:
        return float(Co_values[-1])

    i0, i1 = _find_bracket(L_over_H_values, L_H)

    x0 = L_over_H_values[i0]
    x1 = L_over_H_values[i1]
    y0 = Co_values[i0]
    y1 = Co_values[i1]

    return float(_linear_interpolate(L_H, x0, x1, y0, y1))
