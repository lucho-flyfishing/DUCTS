# smooth_r_elbow.py
# Elbow, Smooth Radius (Die Stamped), Round

def linear_interp(x, xp, fp):
    """Interpolación lineal simple equivalente a numpy.interp."""
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


def get_co_round_smooth_elbow(r_D, theta):
    """
    Calcula Co para un codo smooth radius redondo.
    Parámetros:
    - r_D : relación r/D
    - theta : ángulo en grados
    """

    # Tabla r/D → C'
    rd_vals = [0.5, 0.75, 1.0, 1.5, 2.0, 2.5]
    Cprime_vals = [0.71, 0.33, 0.22, 0.15, 0.13, 0.12]

    # Tabla theta → Kθ
    theta_vals = [0, 20, 30, 45, 60, 75, 90, 110, 130, 150, 180]
    Ktheta_vals = [0, 0.31, 0.45, 0.60, 0.78, 0.90, 1.00, 1.13, 1.20, 1.28, 1.40]

    # Interpolación
    Cprime = linear_interp(r_D, rd_vals, Cprime_vals)
    Ktheta = linear_interp(theta, theta_vals, Ktheta_vals)

    # Co final
    Co = Ktheta * Cprime
    return Co