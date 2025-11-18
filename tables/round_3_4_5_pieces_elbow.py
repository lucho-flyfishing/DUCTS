# round_3_4_5_pieces_elbow.py
# Elbows; 5-, 4-, and 3-Pieces, Round


def linear_interp(x, xp, fp):
    """Interpolación lineal simple (sin numpy)."""
    if x <= xp[0]:
        return fp[0]
    if x >= xp[-1]:
        return fp[-1]

    for i in range(len(xp) - 1):
        if xp[i] <= x <= xp[i+1]:
            x0, x1 = xp[i], xp[i+1]
            y0, y1 = fp[i], fp[i+1]
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    return fp[-1]


def get_co_round_3_4_5_pieces_elbow(num_pieces, r_D, theta):
    """
    Calcula Co para codos de 3, 4 o 5 piezas.
    Parámetros:
    - num_pieces : número de piezas (3, 4, 5)
    - r_D : relación r/D
    - theta : ángulo en grados
    """

    if num_pieces not in [3, 4, 5]:
        raise ValueError("num_pieces debe ser 3, 4 o 5.")

    # Tabla r/D en columnas
    rd_vals = [0.75, 1.0, 1.5, 2.0]

    # Filas de la tabla C'o
    Cprime_table = {
        5: [0.46, 0.33, 0.24, 0.19],
        4: [0.50, 0.37, 0.27, 0.24],
        3: [0.54, 0.42, 0.34, 0.33],
    }

    Cprime_vals = Cprime_table[num_pieces]

    # Interpolación para C'
    Cprime = linear_interp(r_D, rd_vals, Cprime_vals)

    # Tabla de corrección angular Kθ
    theta_vals = [0, 20, 30, 45, 60, 75, 90, 110, 130, 150, 180]
    Ktheta_vals = [0, 0.31, 0.45, 0.60, 0.78, 0.90, 1.00, 1.13, 1.20, 1.28, 1.40]

    # Interpolación para Kθ
    Ktheta = linear_interp(theta, theta_vals, Ktheta_vals)

    # Co final
    Co = Ktheta * Cprime
    return Co