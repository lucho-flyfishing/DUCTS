# round_tee.py
# Calculates loss coefficient C for Tee, Converging, Round (90°)
# Idelchik 1986 – Diagram 7-4
# No external libraries are used.

# -----------------------------
# DATA TABLES
# -----------------------------

# Ab/Ac column headings
AB_AC_VALUES = [0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1.0]

# Qs/Qc row headings
QS_QC_VALUES = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# Branch table C_c,b (same layout as previous Wye files)
C_CB_TABLE = [
    [-1.0, -1.0, -1.0, -0.90, -0.90, -0.90, -0.90],   # 0.0
    [0.40, -0.37, -0.51, -0.46, -0.50, -0.51, -0.52], # 0.1
    [3.8, 0.72, 0.17, -0.02, -0.14, -0.18, -0.24],    # 0.2
    [9.2, 2.3, 1.0, 0.44, 0.21, 0.11, -0.08],         # 0.3
    [16, 4.3, 2.1, 0.94, 0.54, 0.40, 0.32],           # 0.4
    [26, 6.8, 3.2, 1.1, 0.66, 0.49, 0.42],            # 0.5
    [37, 9.7, 4.7, 1.6, 0.92, 0.69, 0.57],            # 0.6
    [43, 13, 6.3, 2.1, 1.2, 0.88, 0.72],              # 0.7
    [65, 17, 7.9, 2.7, 1.5, 1.1, 0.86],               # 0.8
    [82, 21, 9.7, 3.4, 1.8, 1.2, 0.99],               # 0.9
    [101, 26, 12, 4.0, 2.1, 1.4, 1.1],                # 1.0
]

# Main table values depend ONLY on Qs/Qc:
QS_QC_VALUES_MAIN = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
C_CS_VALUES =       [0.0, 0.16, 0.27, 0.38, 0.46, 0.53, 0.57, 0.59, 0.60, 0.59, 0.55]

# -----------------------------
# Helper functions
# -----------------------------

def linear_interp(x, x0, x1, y0, y1):
    if x1 == x0:
        return y0
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

def bilinear_interp(x, y, x_vals, y_vals, table):
    # Find bounding x columns
    for i in range(len(x_vals) - 1):
        if x_vals[i] <= x <= x_vals[i+1]:
            x0_i = i
            x1_i = i + 1
            break
    else:
        return None

    # Find bounding y rows
    for j in range(len(y_vals) - 1):
        if y_vals[j] <= y <= y_vals[j+1]:
            y0_j = j
            y1_j = j + 1
            break
    else:
        return None

    Q11 = table[y0_j][x0_i]
    Q21 = table[y0_j][x1_i]
    Q12 = table[y1_j][x0_i]
    Q22 = table[y1_j][x1_i]

    R1 = linear_interp(x, x_vals[x0_i], x_vals[x1_i], Q11, Q21)
    R2 = linear_interp(x, x_vals[x0_i], x_vals[x1_i], Q12, Q22)

    return linear_interp(y, y_vals[y0_j], y_vals[y1_j], R1, R2)

# -----------------------------
# Public functions
# -----------------------------

def get_co_round_tee_branch(Qs_Qc, Ab_Ac):
    """
    Bilinear interpolation over (Ab/Ac , Qs/Qc)
    """
    return bilinear_interp(Ab_Ac, Qs_Qc, AB_AC_VALUES, QS_QC_VALUES, C_CB_TABLE)

def get_co_round_tee_main(Qs_Qc):
    """
    Linear interpolation only in Qs/Qc (single row table)
    """
    # Find bounding interval
    for i in range(len(QS_QC_VALUES_MAIN) - 1):
        if QS_QC_VALUES_MAIN[i] <= Qs_Qc <= QS_QC_VALUES_MAIN[i+1]:
            return linear_interp(Qs_Qc,
                                QS_QC_VALUES_MAIN[i], QS_QC_VALUES_MAIN[i+1],
                                C_CS_VALUES[i], C_CS_VALUES[i+1])
    return None
