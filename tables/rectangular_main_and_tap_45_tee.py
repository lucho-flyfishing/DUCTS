# rectangular_main_and_tap_45_tee.py
# Converging, Rectangular Main and Tap (45° Entry)
# SMACNA 1981, Table 9F

# ---------------------------------------------------------
# CONSTANT GEOMETRY
# ---------------------------------------------------------
# Ab/As = 0.5
# As/Ac = 1.0
# Ab/Ac = 0.5
#
# L = 0.25 W, 3 in. minimum

# ---------------------------------------------------------
# TABLE: Branch, Cc,b
# Inputs:
#   Vc_fpm = main duct velocity [fpm]
#   Qb_Qc = Q_b / Q_c
# ---------------------------------------------------------

QB_QC_VALUES = [
    0.1, 0.2, 0.3, 0.4, 0.5,
    0.6, 0.7, 0.8, 0.9, 1.0
]

# Vc < 1200 fpm
CCB_LOW_VELOCITY = [
    -0.83, -0.68, -0.30, 0.28, 0.55,
    1.03, 1.50, 1.93, 2.50, 3.03
]

# Vc > 1200 fpm
CCB_HIGH_VELOCITY = [
    -0.72, -0.52, -0.23, 0.34, 0.76,
    1.14, 1.83, 2.01, 2.90, 3.63
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

def get_ccb_rectangular_main_and_tap_45_tee(Vc_fpm, Qb_Qc):

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