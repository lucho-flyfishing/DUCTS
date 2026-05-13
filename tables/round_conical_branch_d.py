# round_conical_branch_d.py
# Tee, Diverging, Round, Conical Branch
# Jones and Sepsy 1969, Figure 12

# ---------------------------------------------------------
# CONSTANT GEOMETRY
# ---------------------------------------------------------
# Ac = As

# ---------------------------------------------------------
# TABLE: Branch, Cc,b
# Inputs:
#   Vb_Vs = V_b / V_s
# ---------------------------------------------------------

VB_VS_VALUES = [
    0.0, 0.2, 0.4, 0.6, 0.8,
    1.0, 1.2, 1.4, 1.6, 1.8, 2.0
]

CCB_VALUES = [
    1.0, 0.85, 0.74, 0.62, 0.52,
    0.42, 0.36, 0.32, 0.32, 0.37, 0.52
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

def get_ccb_round_conical_branch_d(Vb_Vs):

    return interpolate_1d(
        Vb_Vs,
        VB_VS_VALUES,
        CCB_VALUES
    )