# rect_no_vanes_elbow.py
# Elbow Without Vanes, Rectangular (Smooth radius & Sharp Heel)
# Ambos accesorios usan EXACTAMENTE la misma tabla.

from app_state import app_state


def linear_interp(x, xp, fp):
    """Interpolación lineal simple 1D."""
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


def bilinear_interp(x, y, x_vals, y_vals, table):
    """Interpolación bilineal para la tabla C' (r/W vs H/W)."""
    # Interpola primero en x para cada fila
    row_interp = []
    for row in table:
        row_interp.append(linear_interp(x, x_vals, row))

    # Luego interpola entre esos resultados en y
    return linear_interp(y, y_vals, row_interp)


def get_co_rect_no_vanes_elbow(r_over_W, H_over_W, theta_deg, use_Ktheta=True):
    """
    Codo rectangular sin aletas (smooth o sharp throat).
    
    Parámetros:
    - r_over_W : r/W
    - H_over_W : H/W
    - theta_deg : ángulo
    - use_Ktheta : True = smooth radius, False = sharp heel
    """

    # ===============================
    # TABLA PRINCIPAL DE C'
    # ===============================

    H_over_W_vals = [0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0]

    r_over_W_vals = [0.5, 0.75, 1.0, 1.5, 2.0]

    Cprime_table = [
        [1.3, 1.3, 1.2, 1.2, 1.1, 1.0, 1.0, 1.1, 1.1, 1.2, 1.2],   # r/W = 0.5
        [0.57, 0.52, 0.48, 0.44, 0.40, 0.39, 0.39, 0.40, 0.42, 0.43, 0.44], # r/W = 0.75
        [0.27, 0.25, 0.23, 0.21, 0.19, 0.18, 0.18, 0.19, 0.20, 0.21, 0.21], # r/W = 1.0
        [0.22, 0.20, 0.19, 0.17, 0.15, 0.14, 0.14, 0.15, 0.16, 0.17, 0.17], # r/W = 1.5
        [0.20, 0.18, 0.16, 0.15, 0.14, 0.13, 0.13, 0.14, 0.14, 0.15, 0.15], # r/W = 2.0
    ]

    Cprime = bilinear_interp(r_over_W, H_over_W, H_over_W_vals, r_over_W_vals, Cprime_table)

    # ===================================
    # FACTOR ANGULAR (solo smooth radius)
    # ===================================

    if use_Ktheta:
        theta_vals = [0, 20, 30, 45, 60, 75, 90, 110, 130, 150, 180]
        Ktheta_vals = [0, 0.31, 0.45, 0.60, 0.78, 0.90, 1.00, 1.13, 1.20, 1.28, 1.40]
        Ktheta = linear_interp(theta_deg, theta_vals, Ktheta_vals)
    else:
        Ktheta = 1.0  # sharp throat heel no usa Kθ

    # ===================================
    # CORRECCIÓN POR REYNOLDS
    # ===================================

    if app_state.Re is None:
        raise ValueError("Error: app_state.Re no ha sido calculado.")

    Re_tab =  [1,   2,    3,    4,    6,    8,    10,   14,   20]   # Re × 10⁴
    # r/W < 0.75 usa tabla de 0.5
    if r_over_W <= 0.75:
        KRe_vals = [1.40, 1.26, 1.19, 1.14, 1.09, 1.06, 1.04, 1.00, 1.00]
    else:
        KRe_vals = [2.00, 1.77, 1.64, 1.56, 1.46, 1.38, 1.30, 1.15, 1.00]

    Re_for_table = app_state.Re / 10_000
    KRe = linear_interp(Re_for_table, Re_tab, KRe_vals)

    # ===============================
    # RESULTADO FINAL
    # ===============================

    Co = Cprime * KRe * Ktheta
    return Co