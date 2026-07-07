# rectangular_dovetail_wye.py
# Symmetrical Wye, Dovetail, Rectangular (Converging)
# Idelchik et al. 1986, Diagram 7-24

# ---------------------------------------------------------
# GEOMETRY
# ---------------------------------------------------------
# r/Wc = 1.5
# Q1b/Qc = Q2b/Qc = 0.5
#
# Returns:
#   Cc,1b or Cc,2b
# (Both branches are identical.)

# ---------------------------------------------------------
# TABLE
# ---------------------------------------------------------

AB_AC_VALUES = [
    0.5,
    1.0
]

CCB_VALUES = [
    0.23,
    0.07
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

def get_co_rectangular_dovetail_wye_branch(Ab_Ac):

    return interpolate_1d(
        Ab_Ac,
        AB_AC_VALUES,
        CCB_VALUES
    )