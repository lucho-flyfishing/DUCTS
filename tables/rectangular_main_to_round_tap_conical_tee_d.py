# rectangular_main_to_round_tap_conical_tee_d.py
# Tee, Diverging, Rectangular Main to Round Tap (Conical)
# Inoue et al. 1980, Korst et al. 1950

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
# ---------------------------------------------------------

VB_VC_VALUES = [
    0.40,
    0.50,
    0.75,
    1.00,
    1.30,
    1.50,
]

CCB_VALUES = [
    0.80,
    0.83,
    0.90,
    1.00,
    1.10,
    1.40,
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

def get_co_rectangular_main_to_round_tap_conical_tee_d_branch(Vb_Vc):

    return interpolate_1d(
        Vb_Vc,
        VB_VC_VALUES,
        CCB_VALUES
    )