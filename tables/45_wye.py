# fortyfive_wye.py
# Calculates loss coefficient C for 45° wye (branch and main)
# Tables extracted from Idelchik 1986 – Diagram 7-2
# No external libraries are used.

# -----------------------------
# DATA TABLES (hard-coded)
# -----------------------------

# Rows = Qb/Qc
# Columns = Ab/Ac

AB_AC_VALUES = [0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1.0]

QB_QC_VALUES = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# -----------------------------
# Branch table C_cb
# -----------------------------
C_CB_TABLE = [
    [-1.0, -1.0, -1.0, -0.90, -0.90, -0.80, -0.90],  # Qb/Qc = 0.0
    [0.24, -0.45, -0.56, -0.50, -0.52, -0.53, -0.53],  # 0.1
    [3.2, 0.54, -0.02, -0.14, -0.21, -0.23, -0.23],    # 0.2
    [8.0, 1.6, 0.60, 0.23, 0.06, -0.0, -0.02],         # 0.3
    [14, 3.2, 1.3, 0.52, 0.25, 0.18, 0.15],            # 0.4
    [22, 5.0, 2.1, 0.65, 0.25, 0.23, 0.22],            # 0.5
    [32, 8.3, 3.2, 0.90, 0.81, 0.63, 0.51],            # 0.6
    [43, 9.2, 3.9, 1.2, 0.56, 0.39, 0.33],             # 0.7
    [56, 12, 4.9, 1.5, 0.66, 0.39, 0.36],              # 0.8
    [71, 15, 6.2, 1.8, 0.72, 0.44, 0.35],              # 0.9
    [87, 19, 7.4, 2.0, 0.78, 0.44, 0.32],              # 1.0
]

# -----------------------------
# Main table C_cs
# -----------------------------
C_CS_TABLE = [
    [0, 0, 0, 0, 0, 0, 0],           # 0.0
    [0.05, 0.12, 0.17, 0.22, 0.27, 0.29, 0.31],  # 0.1
    [-0.20, -0.17, 0.02, 0.17, 0.22, 0.27, 0.31],  # 0.2
    [-0.76, -0.13, 0.08, 0.12, 0.23, 0.32, 0.40],  # 0.3
    [-1.7, -0.50, -0.12, 0.08, 0.36, 0.46, 0.41],   # 0.4
    [-2.8, -1.4, -0.73, -0.19, 0.16, 0.34, 0.40],   # 0.5
    [-3.5, -1.7, -0.87, -0.35, 0.10, 0.29, 0.32],   # 0.6
    [-6.1, -2.6, -1.4, -0.80, 0.25, 0.08, 0.25],    # 0.7
    [-8.1, -3.2, -1.8, -1.3, -0.55, -0.07, 0.06],   # 0.8
    [-10, -4.8, -2.8, -1.9, -0.88, -0.40, -0.18],   # 0.9
    [-13, -6.1, -3.7, -2.6, -1.4, -0.77, -0.42],    # 1.0
]

# -----------------------------
# Helper function: linear interpolation
# -----------------------------
def linear_interp(x, x0, x1, y0, y1):
    if x1 == x0:
        return y0
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

# -----------------------------
# Helper function: bilinear interpolation
# -----------------------------
def bilinear_interp(x, y, x_vals, y_vals, table):
    # find bounding indices for x
    for i in range(len(x_vals) - 1):
        if x_vals[i] <= x <= x_vals[i+1]:
            x0_i = i
            x1_i = i + 1
            break
    else:
        return None

    # find bounding indices for y
    for j in range(len(y_vals) - 1):
        if y_vals[j] <= y <= y_vals[j+1]:
            y0_j = j
            y1_j = j + 1
            break
    else:
        return None

    # get four surrounding points
    Q11 = table[y0_j][x0_i]
    Q21 = table[y0_j][x1_i]
    Q12 = table[y1_j][x0_i]
    Q22 = table[y1_j][x1_i]

    # interpolate in x direction
    R1 = linear_interp(x, x_vals[x0_i], x_vals[x1_i], Q11, Q21)
    R2 = linear_interp(x, x_vals[x0_i], x_vals[x1_i], Q12, Q22)

    # interpolate in y direction
    return linear_interp(y, y_vals[y0_j], y_vals[y1_j], R1, R2)

# -----------------------------
# PUBLIC FUNCTIONS
# -----------------------------

def get_co_45_wye_branch(Qb_Qc, Ab_Ac):
    return bilinear_interp(Ab_Ac, Qb_Qc, AB_AC_VALUES, QB_QC_VALUES, C_CB_TABLE)

def get_co_45_wye_main(Qb_Qc, Ab_Ac):
    return bilinear_interp(Ab_Ac, Qb_Qc, AB_AC_VALUES, QB_QC_VALUES, C_CS_TABLE)
