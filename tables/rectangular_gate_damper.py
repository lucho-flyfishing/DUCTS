# rectangular_gate_damper.py
# Computes Co for a Rectangular Gate Damper
# Table based on H/W vs h/H (Idelchik)

# -------------------------------------------------------
# TABLE DEFINITION
# -------------------------------------------------------

# Rows: H/W ratios
H_over_W_values = [0.5, 1.0, 1.5, 2.0]

# Columns: h/H ratios
h_over_H_values = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# Co table: rows correspond to H/W; columns to h/H
Co_table = [
    [14, 6.9, 3.3, 1.7, 0.83, 0.32, 0.09],   # H/W = 0.5
    [19, 8.8, 4.5, 2.4, 1.2, 0.55, 0.17],   # H/W = 1.0
    [20, 9.1, 4.7, 2.7, 1.2, 0.47, 0.11],   # H/W = 1.5
    [18, 8.8, 4.5, 2.3, 1.1, 0.51, 0.13],   # H/W = 2.0
]


# -------------------------------------------------------
# 1D INTERPOLATION
# -------------------------------------------------------

def interp1d(x, xp, fp):
    """Simple linear interpolation without numpy."""
    if x <= xp[0]:
        return fp[0]
    if x >= xp[-1]:
        return fp[-1]

    for i in range(len(xp) - 1):
        if xp[i] <= x <= xp[i+1]:
            x0, x1 = xp[i], xp[i+1]
            y0, y1 = fp[i], fp[i+1]
            return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    return fp[-1]


# -------------------------------------------------------
# BILINEAR INTERPOLATION
# -------------------------------------------------------

def bilinear_interpolate(x, y, x_list, y_list, table):
    """
    Bilinear interpolation on a 2D table.
    
    x_list: rows axis (H/W)
    y_list: columns axis (h/H)
    """
    # Clamp x
    if x <= x_list[0]:
        x0_i = x1_i = 0
    elif x >= x_list[-1]:
        x0_i = x1_i = len(x_list) - 1
    else:
        for i in range(len(x_list) - 1):
            if x_list[i] <= x <= x_list[i+1]:
                x0_i, x1_i = i, i+1
                break

    # Clamp y
    if y <= y_list[0]:
        y0_j = y1_j = 0
    elif y >= y_list[-1]:
        y0_j = y1_j = len(y_list) - 1
    else:
        for j in range(len(y_list) - 1):
            if y_list[j] <= y <= y_list[j+1]:
                y0_j, y1_j = j, j+1
                break

    x0, x1 = x_list[x0_i], x_list[x1_i]
    y0, y1 = y_list[y0_j], y_list[y1_j]

    # Corner values
    Q11 = table[x0_i][y0_j]
    Q12 = table[x0_i][y1_j]
    Q21 = table[x1_i][y0_j]
    Q22 = table[x1_i][y1_j]

    # If no interpolation needed in x or y (clamped)
    if x0_i == x1_i and y0_j == y1_j:
        return float(Q11)

    if x0_i == x1_i:
        return float(Q11 + (Q12 - Q11) * (y - y0) / (y1 - y0))

    if y0_j == y1_j:
        return float(Q11 + (Q21 - Q11) * (x - x0) / (x1 - x0))

    # Full bilinear interpolation
    return float(
        Q11 * (x1 - x) * (y1 - y) +
        Q21 * (x - x0) * (y1 - y) +
        Q12 * (x1 - x) * (y - y0) +
        Q22 * (x - x0) * (y - y0)
        ) / ((x1 - x0) * (y1 - y0))


# -------------------------------------------------------
# MAIN FUNCTION
# -------------------------------------------------------

def get_co_rectangular_gate_damper(H_over_W, h_over_H):
    """
    Returns Co for a Rectangular Gate Damper.

    Parameters:
        H_over_W (float): Ratio of height to width.
        h_over_H (float): Blade height relative to duct height.

    Returns:
        float: interpolated Co.
    """
    return bilinear_interpolate(
        H_over_W,
        h_over_H,
        H_over_W_values,
        h_over_H_values,
        Co_table
    )
