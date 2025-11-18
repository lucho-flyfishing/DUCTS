# round_mitered_elbow.py
# Elbow, Mitered, Round (Idelchik et al. 1986)

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


def get_co_round_mitered_elbow(theta):
    """
    Codo mitered redondo.
    Parámetros:
    - theta : ángulo del codo en grados

    app_state.Re se usa automáticamente para la corrección.
    """

    # ---- Tabla C' (solo depende de theta) ----
    theta_vals = [20, 30, 45, 60, 75, 90]
    Cprime_vals = [0.08, 0.16, 0.34, 0.55, 0.81, 1.20]

    Cprime = linear_interp(theta, theta_vals, Cprime_vals)

    # ---- Tabla corrección Reynolds ----
    # Re en tabla viene como: 1, 2, 3, 4, 6, 8, 10, >=14  (x 10⁴)
    Re_vals = [1, 2, 3, 4, 6, 8, 10, 14]
    KRe_vals = [1.40, 1.26, 1.19, 1.14, 1.09, 1.06, 1.04, 1.00]

    # Convertimos Re real al formato de la tabla
    # La tabla está en unidades "x 10⁴"
    if app_state.Re is None:
        raise ValueError("Error: app_state.Re no ha sido calculado.")

    Re_for_table = app_state.Re / 10_000

    KRe = linear_interp(Re_for_table, Re_vals, KRe_vals)

    # ---- Co final ----
    Co = KRe * Cprime
    return Co