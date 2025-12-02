# rectangular_transition.py
# Cálculo de Co para "Transition, Rectangular, Two Sides Parallel, Symmetrical"
# Idelchik et al. 1986, Diagram 5-2
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
# TABLA DE IDELCHIK COMPLETA
# -------------------------

AoA1_values = [0.06, 0.10, 0.25, 0.50, 1, 2, 4, 6, 10]

theta_values = [10, 15, 30, 45, 60, 90, 120, 150, 180]

Co_table = {
    0.06: [0.26, 0.27, 0.40, 0.56, 0.71, 0.86, 1.00, 0.99, 0.98],
    0.10: [0.24, 0.26, 0.36, 0.53, 0.69, 0.82, 0.93, 0.92, 0.91],
    0.25: [0.17, 0.19, 0.22, 0.42, 0.60, 0.68, 0.70, 0.67, 0.66],
    0.50: [0.14, 0.13, 0.15, 0.24, 0.35, 0.37, 0.38, 0.36, 0.35],
    1.00: [0.0] * 9,
    2.00: [0.23, 0.20, 0.20, 0.20, 0.24, 0.28, 0.54, 0.78, 1.10],
    4.00: [0.81, 0.64, 0.64, 0.64, 0.88, 1.10, 2.80, 5.70, 6.60],
    6.00: [1.80, 1.40, 1.40, 1.40, 2.00, 2.50, 6.60, 10.00, 13.00],
    10.0: [5.00, 5.00, 5.00, 5.00, 6.50, 8.00, 19.0, 29.0, 43.0],
}


def get_co_rectangular_transition(AoA1, theta_deg):
    """Devuelve Co interpolado desde Idelchik."""
    x0, x1 = get_neighbors(AoA1_values, AoA1)
    y0, y1 = get_neighbors(theta_values, theta_deg)

    q11 = Co_table[x0][theta_values.index(y0)]
    q12 = Co_table[x0][theta_values.index(y1)]
    q21 = Co_table[x1][theta_values.index(y0)]
    q22 = Co_table[x1][theta_values.index(y1)]

    return bilinear(AoA1, theta_deg, x0, x1, y0, y1, q11, q12, q21, q22)
