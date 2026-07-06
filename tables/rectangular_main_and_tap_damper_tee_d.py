# rectangular_main_and_tap_damper_tee_d.py
# Tee, Diverging, Rectangular Main and Tap, with Damper
# SMACNA 1981, Table 6-10R

# ---------------------------------------------------------
# CONSTANT GEOMETRY
# ---------------------------------------------------------
# Ac = As
#
# Main coefficient (Cc,s):
# See fitting 5-31

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
    [0.58, 0.58, 0.58, 0.58, 0.58, 0.58, 0.58, 0.58, 0.58],

    # Vb/Vc = 0.4
    [0.67, 0.64, 0.64, 0.64, 0.64, 0.64, 0.64, 0.64, 0.64],

    # Vb/Vc = 0.6
    [0.78, 0.76, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75],

    # Vb/Vc = 0.8
    [0.88, 0.98, 0.81, 1.01, 1.01, 1.01, 1.01, 1.01, 1.01],

    # Vb/Vc = 1.0
    [1.12, 1.05, 1.08, 1.18, 1.29, 1.29, 1.29, 1.29, 1.29],

    # Vb/Vc = 1.2
    [1.49, 1.48, 1.40, 1.51, 1.70, 1.91, 1.91, 1.91, 1.91],

    # Vb/Vc = 1.4
    [2.10, 2.21, 2.25, 2.29, 2.32, 2.48, 2.53, 2.53, 2.53],

    # Vb/Vc = 1.6
    [2.72, 3.30, 2.84, 3.09, 3.30, 3.19, 3.29, 3.16, 3.16],

    # Vb/Vc = 1.8
    [3.42, 4.58, 3.65, 3.92, 4.20, 4.15, 4.14, 4.10, 4.05],
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

def get_co_rectangular_main_and_tap_damper_tee_d_branch(Vb_Vc, Qb_Qc):

    return interpolate_2d(
        Vb_Vc,
        Qb_Qc,
        VB_VC_VALUES,
        QB_QC_VALUES,
        CCB_TABLE
    )