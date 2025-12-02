# tables/round_transition.py

# ---- TABLA DE Co PARA ROUND TRANSITION ----
# Ejes:
# x = Ao/A1
# y = theta (grados)

co_table = {
    0.06: {10: 0.21, 15: 0.29, 20: 0.38, 30: 0.60, 45: 0.84, 60: 0.88, 90: 0.88, 120: 0.88, 150: 0.88, 180: 0.88},
    0.10: {10: 0.21, 15: 0.28, 20: 0.38, 30: 0.59, 45: 0.76, 60: 0.80, 90: 0.83, 120: 0.84, 150: 0.83, 180: 0.83},
    0.25: {10: 0.16, 15: 0.22, 20: 0.30, 30: 0.46, 45: 0.61, 60: 0.64, 90: 0.63, 120: 0.64, 150: 0.62, 180: 0.62},
    0.50: {10: 0.11, 15: 0.13, 20: 0.19, 30: 0.33, 45: 0.33, 60: 0.32, 90: 0.31, 120: 0.31, 150: 0.30, 180: 0.30},
    1.00: {10: 0,    15: 0,    20: 0,    30: 0,    45: 0,    60: 0,    90: 0,    120: 0,    150: 0,    180: 0},
    2.00: {10: 0.20, 15: 0.20, 20: 0.20, 30: 0.20, 45: 0.22, 60: 0.24, 90: 0.48, 120: 0.72, 150: 0.96, 180: 1.00},
    4.00: {10: 0.80, 15: 0.64, 20: 0.64, 30: 0.64, 45: 0.88, 60: 1.10, 90: 2.70, 120: 4.30, 150: 5.60, 180: 6.60},
    6.00: {10: 1.60, 15: 1.40, 20: 1.40, 30: 1.40, 45: 2.00, 60: 2.50, 90: 6.50, 120: 10.0, 150: 14.0, 180: 16.0},
    10.0: {10: 5.00, 15: 5.00, 20: 5.00, 30: 5.00, 45: 6.50, 60: 10.0, 90: 19.0, 120: 27.0, 150: 37.0, 180: 43.0},
}

# ---- Interpolación lineal básica ----
def linear_interp(x, x1, x2, y1, y2):
    if x2 == x1:
        return y1
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)

# ---- Interpolación bilineal en la tabla ----
def bilinear_lookup(x, y, table):
    xs = sorted(table.keys())
    ys = sorted(next(iter(table.values())).keys())

    # Limitar dentro de la tabla
    if x <= xs[0]: x = xs[0]
    if x >= xs[-1]: x = xs[-1]
    if y <= ys[0]: y = ys[0]
    if y >= ys[-1]: y = ys[-1]

    # Encontrar x1, x2
    for i in range(len(xs)-1):
        if xs[i] <= x <= xs[i+1]:
            x1, x2 = xs[i], xs[i+1]
            break

    # Encontrar y1, y2
    for j in range(len(ys)-1):
        if ys[j] <= y <= ys[j+1]:
            y1, y2 = ys[j], ys[j+1]
            break

    # Valores en los 4 puntos
    Q11 = table[x1][y1]
    Q12 = table[x1][y2]
    Q21 = table[x2][y1]
    Q22 = table[x2][y2]

    # Interpolar en x
    R1 = linear_interp(x, x1, x2, Q11, Q21)
    R2 = linear_interp(x, x1, x2, Q12, Q22)

    # Interpolar final en y
    P = linear_interp(y, y1, y2, R1, R2)

    return P

# ---- FUNCIÓN PRINCIPAL ----
def get_co_round_transition(area_ratio, theta_deg):
    """
    area_ratio = Ao / A1
    theta_deg = θ en grados
    """
    return bilinear_lookup(area_ratio, theta_deg, co_table)
