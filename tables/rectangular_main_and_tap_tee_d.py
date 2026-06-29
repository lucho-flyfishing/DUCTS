# rectangular_main_and_tap_tee_d.py
# Tee, Diverging, Rectangular Main and Tap
# SMACNA 1981, Table 10Q

# ---------------------------------------------------------
# CONSTANT GEOMETRY
# ---------------------------------------------------------
# Ac = As
#
# Main coefficient (Cc,s):
# See fitting 5-23

# ---------------------------------------------------------
# TABLE: Branch, Cc,b
# Inputs:
#   Vb_Vc = Vb / Vc
#   Qb_Qc = Qb / Qc
# ---------------------------------------------------------

VB_VC_VALUES = [
    0.2, 0.4, 0.6, 0.8,
    1.0, 1.2, 1.4, 1.6, 1.8
]

QB_QC_VALUES = [
    0.1, 0.2, 0.3, 0.4,
    0.5, 0.6, 0.7, 0.8, 0.9
]

# Missing values are repeated so interpolation remains valid.

CCB_TABLE = [

    # Vb/Vc = 0.2
    [1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03, 1.03],

    # Vb/Vc = 0.4
    [1.04, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01],

    # Vb/Vc = 0.6
    [1.11, 1.03, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05, 1.05],

    # Vb/Vc = 0.8
    [1.16, 1.21, 1.17, 1.12, 1.12, 1.12, 1.12, 1.12, 1.12],

    # Vb/Vc = 1.0
    [1.38, 1.40, 1.30, 1.36, 1.27, 1.27, 1.27, 1.27, 1.27],

    # Vb/Vc = 1.2
    [1.52, 1.61, 1.68, 1.91, 1.47, 1.66, 1.66, 1.66, 1.66],

    # Vb/Vc = 1.4
    [1.79, 2.01, 1.90, 2.31, 2.28, 2.20, 1.95, 1.95, 1.95],

    # Vb/Vc = 1.6
    [2.07, 2.28, 2.13, 2.71, 2.99, 2.81, 2.09, 2.20, 2.20],

    # Vb/Vc = 1.8
    [2.32, 2.54, 2.64, 3.09, 3.72, 2.48, 2.21, 2.57, 2.32],
]


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


def interpolate_2d(x, y, x_values, y_values, table):

    interpolated_rows = []

    for row in table:

        interpolated_rows.append(
            interpolate_1d(y, y_values, row)
        )

    return interpolate_1d(
        x,
        x_values,
        interpolated_rows
    )


# =========================================================
# BRANCH COEFFICIENT
# =========================================================

def get_ccb_rectangular_main_and_tap_tee_d(Vb_Vc, Qb_Qc):

    return interpolate_2d(
        Vb_Vc,
        Qb_Qc,
        VB_VC_VALUES,
        QB_QC_VALUES,
        CCB_TABLE
    )