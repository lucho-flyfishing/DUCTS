# round_tap_rectangular_main_tee.py
# Tee, Converging, Round Tap to Rectangular Main
# SMACNA 1981, Table 6-9C

# ---------------------------------------------------------
# CONSTANT GEOMETRY
# ---------------------------------------------------------
# Ab/As = 0.5
# As/Ac = 1.0
# Ab/Ac = 0.5

# ---------------------------------------------------------
# TABLE: Branch, Cc,b
# Inputs:
#   Vc_fpm = main duct velocity [fpm]
#   Qb_Qc = Q_b / Q_c
# ---------------------------------------------------------

QB_QC_VALUES = [0.1, 0.2, 0.3, 0.4, 0.5,
                0.6, 0.7, 0.8, 0.9, 1.0]

# Vc < 1200 fpm
CCB_LOW_VELOCITY = [
    -0.63, -0.55, 0.13, 0.23, 0.78,
    1.30, 1.93, 3.10, 4.88, 5.60
]

# Vc > 1200 fpm
CCB_HIGH_VELOCITY = [
    -0.49, -0.21, 0.23, 0.60, 1.27,
    2.06, 2.75, 3.70, 4.93, 5.95
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


# =========================================================
# BRANCH COEFFICIENT
# =========================================================

def get_co_round_tap_rectangular_main_tee_branch(Vc_fpm, Qb_Qc):

    # Select velocity row
    if Vc_fpm < 1200:
        values = CCB_LOW_VELOCITY
    else:
        values = CCB_HIGH_VELOCITY

    return interpolate_1d(
        Qb_Qc,
        QB_QC_VALUES,
        values
    )