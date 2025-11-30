# Tabla de Co para Conical Converging Bellmouth, Rectangular

angles = [0, 10, 20, 30, 45, 60, 90, 120, 150, 180]

L_over_D = [0.025, 0.05, 0.10, 0.25, 0.60, 1.0]

co_matrix = [
    [1.00, 0.96, 0.93, 0.90, 0.85, 0.80, 0.72, 0.64, 0.57, 0.50],
    [1.00, 0.93, 0.86, 0.80, 0.73, 0.67, 0.60, 0.56, 0.52, 0.50],
    [1.00, 0.80, 0.67, 0.55, 0.46, 0.41, 0.41, 0.43, 0.46, 0.50],
    [1.00, 0.68, 0.45, 0.30, 0.21, 0.17, 0.21, 0.28, 0.38, 0.50],
    [1.00, 0.46, 0.27, 0.18, 0.14, 0.13, 0.19, 0.27, 0.37, 0.50],
    [1.00, 0.32, 0.20, 0.14, 0.11, 0.10, 0.16, 0.24, 0.35, 0.50]
]


def interpolate_1d(x, xp, fp):
    """Interpolación lineal 1D."""
    # Si está fuera del rango, clamp
    if x <= xp[0]:
        return fp[0]
    if x >= xp[-1]:
        return fp[-1]

    # Buscar intervalo
    for i in range(len(xp) - 1):
        if xp[i] <= x <= xp[i+1]:
            x0, x1 = xp[i], xp[i+1]
            y0, y1 = fp[i], fp[i+1]

            # Interpolación lineal
            t = (x - x0) / (x1 - x0)
            return y0 + t * (y1 - y0)


def interpolate_2d(x, y, x_vals, y_vals, table):
    """Interpolación bilineal."""
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

    # Encuentra intervalo en X
    for i in range(len(x_vals) - 1):
        if x_vals[i] <= x <= x_vals[i+1]:
            x0_i = i
            break

    # Encuentra intervalo en Y
    for j in range(len(y_vals) - 1):
        if y_vals[j] <= y <= y_vals[j+1]:
            y0_j = j
            break

    # Valores del grid más cercano
    Q11 = table[x0_i][y0_j]
    Q12 = table[x0_i][y0_j+1]
    Q21 = table[x0_i+1][y0_j]
    Q22 = table[x0_i+1][y0_j+1]

    x0 = x_vals[x0_i]
    x1 = x_vals[x0_i+1]
    y0 = y_vals[y0_j]
    y1 = y_vals[y0_j+1]

    # Coeficientes de interpolación
    tx = (x - x0) / (x1 - x0) if x1 != x0 else 0
    ty = (y - y0) / (y1 - y0) if y1 != y0 else 0

    # Bilinear
    return (
        Q11 * (1 - tx) * (1 - ty) +
        Q21 * tx * (1 - ty) +
        Q12 * (1 - tx) * ty +
        Q22 * tx * ty
    )


def get_co_conical_bell(L_D, theta):

    return interpolate_2d(
        L_D, theta,
        L_over_D, angles,
        co_matrix
    )
