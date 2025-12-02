# tables/round_rectangular_transition.py

# ---- TABLA DE Co PARA ROUND/RECTANGULAR TRANSITION ----
# Ejes:
# x = A1/Ao
# y = theta (grados)

co_table = {
    2:  {8: 0.14, 10: 0.15, 14: 0.20, 20: 0.25, 30: 0.30, 45: 0.33, 60: 0.33, 90: 0.33, 180: 0.30},
    4:  {8: 0.20, 10: 0.25, 14: 0.34, 20: 0.45, 30: 0.52, 45: 0.58, 60: 0.62, 90: 0.64, 180: 0.64},
    6:  {8: 0.21, 10: 0.30, 14: 0.42, 20: 0.53, 30: 0.63, 45: 0.72, 60: 0.78, 90: 0.79, 180: 0.79},
    10: {8: 0.24, 10: 0.30, 14: 0.43, 20: 0.53, 30: 0.64, 45: 0.75, 60: 0.84, 90: 0.89, 180: 0.88},
}

# ---- Interpolación lineal básica ----
def linear_interp(x, x1, x2, y1, y2):
    if x2 == x1:
        return y1
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)

# ---- Interpolación bilineal ----
def bilinear_lookup(x, y, table):
    xs = sorted(table.keys())
    ys = sorted(next(iter(table.values())).keys())

    # Limitar valores
    if x <= xs[0]: x = xs[0]
    if x >= xs[-1]: x = xs[-1]
    if y <= ys[0]: y = ys[0]
    if y >= ys[-1]: y = ys[-1]

    # Encontrar x1 y x2
    for i in range(len(xs)-1):
        if xs[i] <= x <= xs[i+1]:
            x1, x2 = xs[i], xs[i+1]
            break

    # Encontrar y1 y y2
    for j in range(len(ys)-1):
        if ys[j] <= y <= ys[j+1]:
            y1, y2 = ys[j], ys[j+1]
            break

    # Valores en esquinas
    Q11 = table[x1][y1]
    Q12 = table[x1][y2]
    Q21 = table[x2][y1]
    Q22 = table[x2][y2]

    # Interpolar primero en x
    R1 = linear_interp(x, x1, x2, Q11, Q21)
    R2 = linear_interp(x, x1, x2, Q12, Q22)

    # Interpolar final en y
    P = linear_interp(y, y1, y2, R1, R2)

    return P

# ---- FUNCIÓN PRINCIPAL ----
def get_co_round_rectangular_transition(area_ratio, theta_deg):
    """
    area_ratio = A1 / Ao
    theta_deg = ángulo θ en grados
    """
    return bilinear_lookup(area_ratio, theta_deg, co_table)
