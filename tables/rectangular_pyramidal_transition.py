# rectangular_pyramidal_transition.py
# Cálculo de Co para "Transition, Rectangular, Pyramidal"
# Idelchik et al. 1986, Diagram 5-4
# Sin numpy, sin scipy. Interpolación bilineal manual.

def interp(x, x0, x1, q0, q1):
    """Interpolación lineal."""
    if x1 == x0:
        return q0
    return q0 + (q1 - q0) * (x - x0) / (x1 - x0)


def bilinear(x, y, x0, x1, y0, y1, q11, q12, q21, q22):
    """Interpolación bilineal."""
    r1 = interp(x, x0, x1, q11, q12)
    r2 = interp(x, x0, x1, q21, q22)
    return interp(y, y0, y1, r1, r2)


def get_neighbors(values, x):
    """Encuentra los dos valores vecinos para interpolación."""
    for i in range(len(values) - 1):
        if values[i] <= x <= values[i + 1]:
            return values[i], values[i + 1]
    if x <= values[0]:
        return values[0], values[0]
    if x >= values[-1]:
        return values[-1], values[-1]
    return values[0], values[0]


# -------------------------
# TABLA COMPLETA DE IDELCHIK
# -------------------------

AoA1_values = [0.06, 0.10, 0.25, 0.50, 1, 2, 4, 6, 10]

theta_values = [10, 15, 20, 30, 45, 60, 90, 120, 150, 180]

Co_table = {
    0.06: [0.26, 0.30, 0.44, 0.54, 0.53, 0.65, 0.77, 0.88, 0.95, 0.98],
    0.10: [0.24, 0.30, 0.43, 0.50, 0.53, 0.64, 0.75, 0.84, 0.89, 0.91],
    0.25: [0.20, 0.25, 0.34, 0.36, 0.45, 0.52, 0.58, 0.62, 0.64, 0.64],
    0.50: [0.14, 0.15, 0.20, 0.21, 0.25, 0.30, 0.33, 0.33, 0.33, 0.32],
    1.00: [0.0] * 10,
    2.00: [0.23, 0.22, 0.21, 0.20, 0.22, 0.20, 0.49, 0.74, 0.99, 1.10],
    4.00: [0.84, 0.68, 0.68, 0.64, 0.88, 1.10, 2.70, 4.30, 5.60, 6.60],
    6.00: [1.80, 1.50, 1.50, 1.40, 2.00, 2.50, 6.50, 10.00, 13.00, 15.00],
    10.0: [5.00, 5.00, 5.10, 5.00, 6.50, 8.00, 19.00, 29.00, 37.00, 43.00],
}


def get_co_rectangular_pyramidal_transition(AoA1, theta_deg):
    """Devuelve Co interpolado desde Idelchik (Transition, Rectangular, Pyramidal)."""
    x0, x1 = get_neighbors(AoA1_values, AoA1)
    y0, y1 = get_neighbors(theta_values, theta_deg)

    q11 = Co_table[x0][theta_values.index(y0)]
    q12 = Co_table[x0][theta_values.index(y1)]
    q21 = Co_table[x1][theta_values.index(y0)]
    q22 = Co_table[x1][theta_values.index(y1)]

    return bilinear(AoA1, theta_deg, x0, x1, y0, y1, q11, q12, q21, q22)