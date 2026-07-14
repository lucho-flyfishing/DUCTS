# rectangular_and_round_wye_d.py
# Wye, Rectangular and Round (Diverging)
# Idelchik et al. 1986, Diagram 7-30

# ---------------------------------------------------------
# GEOMETRY
# ---------------------------------------------------------
# A1b = A2b
# Ac = A1b + A2b
#
# Returns Cc,1b or Cc,2b
# (Both branches use the same table.)

# ---------------------------------------------------------
# TABLE
# ---------------------------------------------------------

THETA_VALUES = [
    15,
    30,
    45,
    60,
    90
]

VB_VC_VALUES = [
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.8,
    1.0,
    1.2,
    1.4,
    1.6,
    1.8,
    2.0
]

CCB_TABLE = [

    # θ = 15°
    [
        0.81,
        0.65,
        0.51,
        0.38,
        0.28,
        0.20,
        0.11,
        0.06,
        0.14,
        0.30,
        0.51,
        0.76,
        1.00
    ],

    # θ = 30°
    [
        0.84,
        0.69,
        0.56,
        0.44,
        0.34,
        0.26,
        0.19,
        0.15,
        0.15,
        0.30,
        0.51,
        0.76,
        1.00
    ],

    # θ = 45°
    [
        0.87,
        0.74,
        0.63,
        0.54,
        0.45,
        0.38,
        0.29,
        0.24,
        0.23,
        0.30,
        0.51,
        0.76,
        1.00
    ],

    # θ = 60°
    [
        0.90,
        0.82,
        0.79,
        0.66,
        0.59,
        0.53,
        0.43,
        0.36,
        0.33,
        0.39,
        0.51,
        0.76,
        1.00
    ],

    # θ = 90°
    [
        1.00,
        1.00,
        1.00,
        1.00,
        1.00,
        1.00,
        1.00,
        1.00,
        1.00,
        1.00,
        1.00,
        1.00,
        1.00
    ]
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

def get_co_rectangular_and_round_wye_2_d_branch(theta, Vb_Vc):

    return interpolate_2d(
        theta,
        Vb_Vc,
        THETA_VALUES,
        VB_VC_VALUES,
        CCB_TABLE
    )