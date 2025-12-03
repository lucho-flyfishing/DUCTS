# Transition, Rectangular, Three Sides Straight
# Co vs Ao/A1 vs theta (deg)
# No external libraries are used.

def linear_interpolate(x, x0, x1, y0, y1):
    """Simple linear interpolation."""
    if x1 == x0:
        return y0
    return y0 + (y1 - y0) * ( (x - x0) / (x1 - x0) )


# ============================
# TABLA Co
# ============================
AOA1_VALUES = [0.06, 0.1, 0.25, 0.5, 1, 2, 4, 6, 10]

THETA_VALUES = [10, 15, 20, 30, 45, 60, 90]

CO_TABLE = [
    [0.26, 0.27, 0.40, 0.56, 0.71, 0.86, 1.00],  # Ao/A1 = 0.06
    [0.24, 0.26, 0.36, 0.53, 0.69, 0.82, 0.93],  # 0.1
    [0.17, 0.19, 0.22, 0.42, 0.60, 0.68, 0.70],  # 0.25
    [0.14, 0.13, 0.15, 0.24, 0.35, 0.37, 0.38],  # 0.5
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],   # 1
    [0.23, 0.20, 0.20, 0.20, 0.24, 0.28, 0.54],  # 2
    [0.81, 0.64, 0.64, 0.64, 0.88, 1.1,  2.8 ],  # 4
    [1.8,  1.4,  1.4,  1.4,  2.0,  2.5,  6.6 ],  # 6
    [5.0,  5.0,  5.0,  5.0,  6.5,  8.0,  19  ],  # 10
]


def interpolate_2d(Ao_A1, theta):
    """
    Bilinear interpolation over the Co table.
    Ao_A1: ratio Ao/A1 (float)
    theta: angle in degrees (float)
    """

    # ----- Buscar índices para Ao/A1 -----
    for i in range(len(AOA1_VALUES) - 1):
        if AOA1_VALUES[i] <= Ao_A1 <= AOA1_VALUES[i+1]:
            i0 = i
            i1 = i + 1
            break
    else:
        # Fuera de rango: clamp
        if Ao_A1 <= AOA1_VALUES[0]:
            i0 = i1 = 0
        else:
            i0 = i1 = len(AOA1_VALUES) - 1

    # ----- Buscar índices para theta -----
    for j in range(len(THETA_VALUES) - 1):
        if THETA_VALUES[j] <= theta <= THETA_VALUES[j+1]:
            j0 = j
            j1 = j + 1
            break
    else:
        # Fuera de rango: clamp
        if theta <= THETA_VALUES[0]:
            j0 = j1 = 0
        else:
            j0 = j1 = len(THETA_VALUES) - 1

    # Valores de la tabla para bilinear interpolation
    Q11 = CO_TABLE[i0][j0]
    Q12 = CO_TABLE[i0][j1]
    Q21 = CO_TABLE[i1][j0]
    Q22 = CO_TABLE[i1][j1]

    # Interpolación en AOA1
    R1 = linear_interpolate(Ao_A1, AOA1_VALUES[i0], AOA1_VALUES[i1], Q11, Q21)
    R2 = linear_interpolate(Ao_A1, AOA1_VALUES[i0], AOA1_VALUES[i1], Q12, Q22)

    # Interpolación final en θ
    P = linear_interpolate(theta, THETA_VALUES[j0], THETA_VALUES[j1], R1, R2)

    return P



# ============================
# API PRINCIPAL
# ============================

def get_co_rectangular_3_side_transition(Ao_A1, theta):
    """
    Return the Co value for:
    Transition, Rectangular, Three Sides Straight.

    Inputs:
        Ao_A1 → ratio Ao/A1
        theta → degrees
    """
    return interpolate_2d(Ao_A1, theta)