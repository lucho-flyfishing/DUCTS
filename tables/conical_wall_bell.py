# tables/conical_wall_bell.py

# ---------------------------------------------
# TABLA ASHRAE - Co para Conical Wall Bellmouth
# ---------------------------------------------
# Ejes:
#   L/D  (filas)
#   theta (grados) (columnas)
# ---------------------------------------------

L_over_D_values = [0.025, 0.05, 0.075, 0.10, 0.15, 0.60]

theta_values = [0, 10, 20, 30, 45, 60, 90, 120, 150, 180]

# Matriz Co en el mismo orden:
# filas → L/D
# columnas → theta
co_matrix = [
    [0.50, 0.47, 0.45, 0.43, 0.41, 0.40, 0.42, 0.44, 0.46, 0.50],  # L/D = 0.025
    [0.50, 0.45, 0.41, 0.36, 0.32, 0.30, 0.34, 0.39, 0.44, 0.50],  # L/D = 0.05
    [0.50, 0.42, 0.35, 0.30, 0.25, 0.23, 0.28, 0.35, 0.43, 0.50],  # L/D = 0.075
    [0.50, 0.39, 0.32, 0.25, 0.21, 0.18, 0.25, 0.33, 0.41, 0.50],  # L/D = 0.10
    [0.50, 0.37, 0.27, 0.20, 0.16, 0.15, 0.23, 0.31, 0.40, 0.50],  # L/D = 0.15
    [0.50, 0.27, 0.18, 0.13, 0.11, 0.12, 0.20, 0.30, 0.40, 0.50],  # L/D = 0.60
]


# -------------------------------------------
# Utilidades de interpolación
# -------------------------------------------

def interpolate_2d(x, y, x_vals, y_vals, table):
    """Interpolación bilineal manual, equivalente a RegularGridInterpolator."""
    
    # Clamp en X
    if x <= x_vals[0]:
        x = x_vals[0]
    if x >= x_vals[-1]:
        x = x_vals[-1]

    # Clamp en Y
    if y <= y_vals[0]:
        y = y_vals[0]
    if y >= y_vals[-1]:
        y = y_vals[-1]

    # Buscar intervalo en X
    for i in range(len(x_vals) - 1):
        if x_vals[i] <= x <= x_vals[i + 1]:
            x0_i = i
            break

    # Buscar intervalo en Y
    for j in range(len(y_vals) - 1):
        if y_vals[j] <= y <= y_vals[j + 1]:
            y0_j = j
            break

    # Extraer puntos del grid
    Q11 = table[x0_i][y0_j]
    Q12 = table[x0_i][y0_j + 1]
    Q21 = table[x0_i + 1][y0_j]
    Q22 = table[x0_i + 1][y0_j + 1]

    x0 = x_vals[x0_i]
    x1 = x_vals[x0_i + 1]
    y0 = y_vals[y0_j]
    y1 = y_vals[y0_j + 1]

    # Pesos
    tx = (x - x0) / (x1 - x0) if x1 != x0 else 0
    ty = (y - y0) / (y1 - y0) if y1 != y0 else 0

    # Fórmula bilineal
    return (
        Q11 * (1 - tx) * (1 - ty) +
        Q21 * tx * (1 - ty) +
        Q12 * (1 - tx) * ty +
        Q22 * tx * ty
    )


# ---------------------------------------------------
# FUNCIÓN PRINCIPAL (MISMO NOMBRE Y ARGUMENTOS)
# ---------------------------------------------------
def get_co_conical_wall_bell(L_D: float, theta: float) -> float:
    """
    Calcula el coeficiente Co para una campana cónica con pared (Conical Wall Bellmouth)
    usando interpolación bilineal basada en tabla ASHRAE.
    """

    return float(
        interpolate_2d(
            L_D,
            theta,
            L_over_D_values,
            theta_values,
            co_matrix
        )
    )
