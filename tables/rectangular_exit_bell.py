"""
Exit, Rectangular, Two Sides Parallel, Diverging, Symmetrical
Idelchik et al. 1986 – Diagram 11-6
Interpolación bilineal sin numpy ni scipy
"""

# Independent variables
A1_over_A0_values = [2, 4, 6]
theta_values = [8, 10, 14, 20, 30, 45, 60]  # 60 representa ≥60°

# Co table (filas = A1/A0, columnas = θ)
Co_table = [
    [0.50, 0.51, 0.56, 0.63, 0.80, 0.96, 1.00],  # A1/A0 = 2
    [0.34, 0.38, 0.48, 0.63, 0.76, 0.91, 1.00],  # A1/A0 = 4
    [0.32, 0.34, 0.41, 0.56, 0.70, 0.84, 0.96],  # A1/A0 = 6
]


# ------------------------------
# Funciones internas auxiliares
# ------------------------------

def _find_bracketing_indices(values: list, x: float):
    """Regresa índices i, i+1 donde values[i] ≤ x ≤ values[i+1]."""
    # clamp automático
    if x <= values[0]:
        return 0, 0
    if x >= values[-1]:
        return len(values) - 1, len(values) - 1

    for i in range(len(values) - 1):
        if values[i] <= x <= values[i + 1]:
            return i, i + 1

    return len(values) - 1, len(values) - 1


def _bilinear_interpolation(A1_A0, theta):
    """Interpolación bilineal sobre la tabla."""
    # Ubicar índices vecinos
    i0, i1 = _find_bracketing_indices(A1_over_A0_values, A1_A0)
    j0, j1 = _find_bracketing_indices(theta_values, theta)

    x0, x1 = A1_over_A0_values[i0], A1_over_A0_values[i1]
    y0, y1 = theta_values[j0], theta_values[j1]

    # Pesos (evitar divisiones por cero)
    fx = (A1_A0 - x0) / (x1 - x0) if x1 != x0 else 0.0
    fy = (theta - y0) / (y1 - y0) if y1 != y0 else 0.0

    # Valores en esquinas
    Q11 = Co_table[i0][j0]
    Q12 = Co_table[i0][j1]
    Q21 = Co_table[i1][j0]
    Q22 = Co_table[i1][j1]

    # Fórmula bilineal
    return (
        Q11 * (1 - fx) * (1 - fy) +
        Q21 * fx * (1 - fy) +
        Q12 * (1 - fx) * fy +
        Q22 * fx * fy
    )


# ------------------------------
# Función pública
# ------------------------------

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

    # clamp manual
    A1_clamped = max(min(A1_A0, A1_over_A0_values[-1]), A1_over_A0_values[0])
    theta_clamped = max(min(theta, theta_values[-1]), theta_values[0])

    return float(_bilinear_interpolation(A1_clamped, theta_clamped))
