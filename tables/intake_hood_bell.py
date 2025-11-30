"""
Tabla de C₀ para intake_hood_bell
Variables:
    θ (degrees)
    L/D (adimensional)
"""

# Valores de la tabla (filas = θ, columnas = L/D)
theta_values = [0, 15]  # grados

LD_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 4.0]

# Matriz Co en formato lista de listas
Co_table = [
    [2.63, 1.83, 1.53, 1.39, 1.31, 1.19, 1.08, 1.06, 1.00],  # θ = 0°
    [1.32, 0.77, 0.60, 0.48, 0.41, 0.30, 0.28, 0.25, 0.25],  # θ = 15°
]


def _find_bracketing_indices(values: list, x: float):
    """Retorna los índices i, i+1 tales que values[i] <= x <= values[i+1]."""
    # clamp
    if x <= values[0]:
        return 0, 0
    if x >= values[-1]:
        return len(values) - 1, len(values) - 1

    for i in range(len(values) - 1):
        if values[i] <= x <= values[i + 1]:
            return i, i + 1

    return len(values) - 1, len(values) - 1  # fallback seguro


def _bilinear_interpolation(theta, L_D):
    """Interpolación bilineal manual en la tabla."""
    # Encontrar índices en theta y L/D
    i0, i1 = _find_bracketing_indices(theta_values, theta)
    j0, j1 = _find_bracketing_indices(LD_values, L_D)

    t0, t1 = theta_values[i0], theta_values[i1]
    l0, l1 = LD_values[j0], LD_values[j1]

    # Si estamos justo en un valor exacto
    if i0 == i1 and j0 == j1:
        return Co_table[i0][j0]

    # Pesos de interpolación
    # Evitar divisiones por cero
    if t1 != t0:
        ft = (theta - t0) / (t1 - t0)
    else:
        ft = 0.0

    if l1 != l0:
        fl = (L_D - l0) / (l1 - l0)
    else:
        fl = 0.0

    # Valores en las esquinas
    Q11 = Co_table[i0][j0]
    Q12 = Co_table[i0][j1]
    Q21 = Co_table[i1][j0]
    Q22 = Co_table[i1][j1]

    # Interpolación bilineal estándar
    return (
        Q11 * (1 - ft) * (1 - fl) +
        Q21 * ft * (1 - fl) +
        Q12 * (1 - ft) * fl +
        Q22 * ft * fl
    )


def get_co_intake_hood_bell(theta: float, L_D: float) -> float:
    """
    Obtiene C₀ para un intake_hood_bell usando interpolación bilineal (sin numpy ni scipy)
    """
    # clamp suave para evitar extrapolación peligrosa
    theta_clamped = max(min(theta, theta_values[-1]), theta_values[0])
    LD_clamped = max(min(L_D, LD_values[-1]), LD_values[0])

    return float(_bilinear_interpolation(theta_clamped, LD_clamped))
