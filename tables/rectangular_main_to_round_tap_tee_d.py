# rectangular_main_to_round_tap_tee_d.py
# Tee, Diverging, Rectangular Main to Round Tap
# SMACNA 1981, Table 6-10T

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
#   Qb_Qs = Qb / Qs
# ---------------------------------------------------------

VB_VC_VALUES = [
    0.2, 0.4, 0.6, 0.8,
    1.0, 1.2, 1.4, 1.6, 1.8
]

QB_QS_VALUES = [
    0.1, 0.2, 0.3, 0.4, 0.5,
    0.6, 0.7, 0.8, 0.9
]

# Each row corresponds to a Vb/Vc value.
# Missing values at the end of each row are repeated so interpolation
# remains valid inside the available domain.

CCB_TABLE = [

    # Vb/Vc = 0.2
    [1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00],

    # Vb/Vc = 0.4
    [1.01, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07, 1.07],

    # Vb/Vc = 0.6
    [1.14, 1.10, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08, 1.08],

    # Vb/Vc = 0.8
    [1.18, 1.31, 1.12, 1.13, 1.13, 1.13, 1.13, 1.13, 1.13],

    # Vb/Vc = 1.0
    [1.30, 1.38, 1.20, 1.23, 1.26, 1.26, 1.26, 1.26, 1.26],

    # Vb/Vc = 1.2
    [1.46, 1.58, 1.45, 1.31, 1.39, 1.48, 1.48, 1.48, 1.48],

    # Vb/Vc = 1.4
    [1.70, 1.82, 1.65, 1.51, 1.56, 1.64, 1.71, 1.71, 1.71],

    # Vb/Vc = 1.6
    [1.93, 2.06, 2.00, 1.85, 1.70, 1.76, 1.80, 1.88, 1.88],

    # Vb/Vc = 1.8
    [2.06, 2.17, 2.10, 2.13, 2.06, 1.98, 1.99, 2.00, 2.07],
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

def get_co_rectangular_main_to_round_tap_tee_d_branch(Vb_Vc, Qb_Qs):

    return interpolate_2d(
        Vb_Vc,
        Qb_Qs,
        VB_VC_VALUES,
        QB_QS_VALUES,
        CCB_TABLE
    )