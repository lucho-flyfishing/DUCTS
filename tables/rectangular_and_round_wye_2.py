# rectangular_and_round_wye.py
# Wye, Rectangular and Round (Converging)
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
    45
]

QB_QC_VALUES = [
    0.0,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1.0
]

CCB_TABLE = [

    # θ = 15°
    [
        -2.6,
        -1.9,
        -1.3,
        -0.77,
        -0.30,
         0.10,
         0.41,
         0.67,
         0.85,
         0.97,
         1.00
    ],

    # θ = 30°
    [
        -2.1,
        -1.5,
        -1.0,
        -0.53,
        -0.10,
         0.28,
         0.69,
         0.91,
         1.10,
         1.40,
         1.60
    ],

    # θ = 45°
    [
        -1.3,
        -0.93,
        -0.55,
        -0.16,
         0.20,
         0.56,
         0.92,
         1.30,
         1.60,
         2.00,
         2.30
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

def get_co_rectangular_and_round_wye_2_branch(theta, Qb_Qc):

    return interpolate_2d(
        theta,
        Qb_Qc,
        THETA_VALUES,
        QB_QC_VALUES,
        CCB_TABLE
    )