# rectangular_tee.py
# Tee, Converging, Rectangular
# Idelchik 1986, Diagram 7-11

# ---------------------------------------------------------
# TABLE: Branch, Cc,b
# Inputs:
#   Ab_As = A_b / A_s
#   Ab_Ac = A_b / A_c
#   Qb_Qc = Q_b / Q_c
# ---------------------------------------------------------

QB_QC_VALUES = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

BRANCH_ROWS = [
    # Ab/As, Ab/Ac, Co values...
    [0.33, 0.25, -1.2, -0.40, 0.40, 1.6, 3.0, 4.8, 6.8, 8.9, 11],
    [0.50, 0.50, -0.50, -0.20, 0.0, 0.25, 0.45, 0.70, 1.0, 1.5, 2.0],
    [0.67, 0.50, -1.0, -0.60, -0.20, 0.10, 0.30, 0.60, 1.0, 1.5, 2.0],
    [1.00, 0.50, -2.2, -1.5, -0.95, -0.50, 0.0, 0.40, 0.80, 1.3, 1.9],
    [1.00, 1.00, -0.60, -0.30, -0.10, -0.04, 0.13, 0.21, 0.29, 0.36, 0.42],
    [1.33, 1.00, -1.2, -0.80, -0.40, -0.20, 0.0, 0.16, 0.24, 0.32, 0.38],
    [2.00, 1.00, -2.1, -1.4, -0.90, -0.50, -0.20, 0.0, 0.20, 0.25, 0.30],
]

# ---------------------------------------------------------
# TABLE: Main, Cc,s
# Inputs:
#   Ab_As = A_b / A_s
#   Ab_Ac = A_b / A_c
#   Qb_Qs = Q_b / Q_s
# ---------------------------------------------------------

QB_QS_VALUES = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

MAIN_ROWS = [
    # Ab/As, Ab/Ac, Co values...
    [0.33, 0.25, 0.30, 0.30, 0.20, -0.10, -0.45, -0.92, -1.5, -2.0, -2.6],
    [0.50, 0.50, 0.17, 0.16, 0.10, 0.0, -0.08, -0.18, -0.27, -0.37, -0.46],
    [0.67, 0.50, 0.27, 0.35, 0.32, 0.25, 0.12, -0.03, -0.23, -0.42, -0.58],
    [1.00, 0.50, 1.2, 1.1, 0.90, 0.65, 0.35, 0.0, -0.40, -0.80, -1.3],
    [1.00, 1.00, 0.18, 0.24, 0.27, 0.26, 0.23, 0.18, 0.10, 0.0, -0.12],
    [1.33, 1.00, 0.75, 0.36, 0.38, 0.35, 0.27, 0.18, 0.05, -0.08, -0.22],
    [2.00, 1.00, 0.80, 0.87, 0.80, 0.68, 0.55, 0.40, 0.25, 0.08, -0.10],
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


def interpolate_between_rows(target, row1, row2, values1, values2):

    if row2 == row1:
        return values1

    result = []

    for v1, v2 in zip(values1, values2):

        interp_value = v1 + (v2 - v1) * (target - row1) / (row2 - row1)

        result.append(interp_value)

    return result


# =========================================================
# BRANCH INTERPOLATION
# =========================================================

def get_ccb_rectangular_tee(Ab_As, Ab_Ac, Qb_Qc):

    rows = sorted(BRANCH_ROWS, key=lambda r: (r[0], r[1]))

    lower_row = rows[0]
    upper_row = rows[-1]

    for i in range(len(rows) - 1):

        current = rows[i]
        next_row = rows[i + 1]

        current_key = (current[0], current[1])
        next_key = (next_row[0], next_row[1])

        target_key = (Ab_As, Ab_Ac)

        if current_key <= target_key <= next_key:

            lower_row = current
            upper_row = next_row
            break

    lower_key = lower_row[0] + lower_row[1]
    upper_key = upper_row[0] + upper_row[1]
    target_key = Ab_As + Ab_Ac

    interpolated_values = interpolate_between_rows(
        target_key,
        lower_key,
        upper_key,
        lower_row[2:],
        upper_row[2:]
    )

    return interpolate_1d(
        Qb_Qc,
        QB_QC_VALUES,
        interpolated_values
    )


# =========================================================
# MAIN INTERPOLATION
# =========================================================

def get_ccs_rectangular_tee(Ab_As, Ab_Ac, Qb_Qs):

    rows = sorted(MAIN_ROWS, key=lambda r: (r[0], r[1]))

    lower_row = rows[0]
    upper_row = rows[-1]

    for i in range(len(rows) - 1):

        current = rows[i]
        next_row = rows[i + 1]

        current_key = (current[0], current[1])
        next_key = (next_row[0], next_row[1])

        target_key = (Ab_As, Ab_Ac)

        if current_key <= target_key <= next_key:

            lower_row = current
            upper_row = next_row
            break

    lower_key = lower_row[0] + lower_row[1]
    upper_key = upper_row[0] + upper_row[1]
    target_key = Ab_As + Ab_Ac

    interpolated_values = interpolate_between_rows(
        target_key,
        lower_key,
        upper_key,
        lower_row[2:],
        upper_row[2:]
    )

    return interpolate_1d(
        Qb_Qs,
        QB_QS_VALUES,
        interpolated_values
    )