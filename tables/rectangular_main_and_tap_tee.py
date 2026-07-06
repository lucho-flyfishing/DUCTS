# rectangular_main_and_tap_tee.py
# Tee, Converging, Rectangular Main and Tap
# SMACNA 1981, Table 6-9D

# ---------------------------------------------------------
# CONSTANT GEOMETRY
# ---------------------------------------------------------
# Ab/As = 0.5
# As/Ac = 1.0
# Ab/Ac = 0.5
#
# Main coefficient (Cc,s):
# See fitting 5-3

# ---------------------------------------------------------
# TABLE: Branch, Cc,b
# Inputs:
#   Vc category (<1200 or >1200 fpm)
#   Qb/Qc
# ---------------------------------------------------------

QB_QC_VALUES = [
    0.1, 0.2, 0.3, 0.4, 0.5,
    0.6, 0.7, 0.8, 0.9, 1.0
]

CCB_TABLE = {
    "low": [      # Vc < 1200 fpm
        -0.75,
        -0.53,
        -0.03,
         0.33,
         1.03,
         1.10,
         2.15,
         2.93,
         4.18,
         4.78,
    ],

    "high": [     # Vc > 1200 fpm
        -0.69,
        -0.21,
         0.23,
         0.67,
         1.17,
         1.66,
         2.67,
         3.36,
         3.93,
         5.13,
    ]
}


# =========================================================
# BASIC INTERPOLATION
# =========================================================

def interpolate_1d(x, xp, fp):

    if x <= xp[0]:
        return fp[0]

    if x >= xp[-1]:
        return fp[-1]

    for i in range(len(xp) - 1):

        if xp[i] <= x <= xp[i + 1]:

            x1 = xp[i]
            x2 = xp[i + 1]

            y1 = fp[i]
            y2 = fp[i + 1]

            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)


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

# =========================================================
# BRANCH COEFFICIENT
# =========================================================

def get_co_rectangular_main_and_tap_tee_branch(Vc, Qb_Qc):

    if Vc < 1200:
        table = CCB_TABLE["low"]
    else:
        table = CCB_TABLE["high"]

    return interpolate_1d(
        Qb_Qc,
        QB_QC_VALUES,
        table
    )

# =========================================================
# MAIN COEFFICIENT
# =========================================================
    
def get_co_rectangular_main_and_tap_tee_main(Qs_Qc):
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
