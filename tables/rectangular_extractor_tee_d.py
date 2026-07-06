# rectangular_extractor_tee_d.py
# Tee, Diverging, Rectangular, with Extractor
# SMACNA 1981, Table 6-10S

# ---------------------------------------------------------
# CONSTANT GEOMETRY
# ---------------------------------------------------------
# Ac = As

# ---------------------------------------------------------
# MAIN COEFFICIENT (Cc,s)
# ---------------------------------------------------------

VB_VC_MAIN = [
    0.2, 0.4, 0.6, 0.8,
    1.0, 1.2, 1.4, 1.6, 1.8
]

CCS_VALUES = [
    0.03, 0.04, 0.07, 0.12,
    0.13, 0.14, 0.27, 0.30, 0.25
]

# ---------------------------------------------------------
# BRANCH COEFFICIENT (Cc,b)
# ---------------------------------------------------------

VB_VC_VALUES = [
    0.2, 0.4, 0.6, 0.8,
    1.0, 1.2, 1.4, 1.6, 1.8
]

QB_QC_VALUES = [
    0.1, 0.2, 0.3, 0.4,
    0.5, 0.6, 0.7, 0.8, 0.9
]

# Missing values are repeated to complete each row.

CCB_TABLE = [

    # Vb/Vc = 0.2
    [0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60, 0.60],

    # Vb/Vc = 0.4
    [0.62, 0.69, 0.69, 0.69, 0.69, 0.69, 0.69, 0.69, 0.69],

    # Vb/Vc = 0.6
    [0.74, 0.80, 0.82, 0.82, 0.82, 0.82, 0.82, 0.82, 0.82],

    # Vb/Vc = 0.8
    [0.99, 1.10, 0.95, 0.90, 0.90, 0.90, 0.90, 0.90, 0.90],

    # Vb/Vc = 1.0
    [1.48, 1.12, 1.41, 1.24, 1.21, 1.21, 1.21, 1.21, 1.21],

    # Vb/Vc = 1.2
    [1.91, 1.33, 1.43, 1.52, 1.55, 1.64, 1.64, 1.64, 1.64],

    # Vb/Vc = 1.4
    [2.47, 1.67, 1.70, 2.04, 1.86, 1.98, 2.47, 2.47, 2.47],

    # Vb/Vc = 1.6
    [3.17, 2.40, 2.33, 2.53, 2.31, 2.51, 3.13, 3.25, 3.25],

    # Vb/Vc = 1.8
    [3.85, 3.37, 2.89, 3.23, 3.09, 3.03, 3.30, 3.74, 4.11],
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
# MAIN COEFFICIENT
# =========================================================

def get_co_rectangular_extractor_tee_d_main(Vb_Vc):

    return interpolate_1d(
        Vb_Vc,
        VB_VC_MAIN,
        CCS_VALUES
    )


# =========================================================
# BRANCH COEFFICIENT
# =========================================================

def get_co_rectangular_extractor_tee_d_branch(Vb_Vc, Qb_Qc):

    return interpolate_2d(
        Vb_Vc,
        Qb_Qc,
        VB_VC_VALUES,
        QB_QC_VALUES,
        CCB_TABLE
    )