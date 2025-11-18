# z_30_elbow.py
# Elbow, 30° Z-Shaped, Round

from app_state import app_state


def linear_interp(x, xp, fp):
    """Interpolación lineal simple."""
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


def get_co_z_30_elbow(L_over_D):
    """
    Codo 30° Z-shaped Round.
    Parámetros:
    - L_over_D : relación L/D tomada del menú
    
    app_state.Re se usa automáticamente para la corrección.
    """

    # ---- Tabla C' para L/D ----
    # L/D:   0    0.5   1.0   1.5   2.0   2.5   3.0
    LD_vals =     [0,   0.5,  1.0,  1.5,  2.0,  2.5,  3.0]
    Cprime_vals = [0,   0.15, 0.15, 0.16, 0.16, 0.16, 0.16]

    Cprime = linear_interp(L_over_D, LD_vals, Cprime_vals)

    # ---- Corrección por Reynolds ----
    if app_state.Re is None:
        raise ValueError("Error: app_state.Re no ha sido calculado.")

    # Tabla en unidades Re × 10⁴
    Re_vals =  [1,    2,    3,    4,    6,    8,    10,   14]
    KRe_vals = [1.40, 1.26, 1.19, 1.14, 1.09, 1.06, 1.04, 1.00]

    Re_for_table = app_state.Re / 10_000

    KRe = linear_interp(Re_for_table, Re_vals, KRe_vals)

    # ---- Co final ----
    Co = KRe * Cprime
    return Co