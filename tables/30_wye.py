# tables/wye_30.py
# Wye 30°, Converging (Idelchik et al. 1986, Diagram 7-1)
# Dos tablas: Cc_branch (ramal) y Cc_main (ducto principal)
# Entrada:
#   Ab_Ac : Ab / Ac (área ramal / área conducto principal)
#   Qb_Qc : Qb / Qc (flujo ramal sobre flujo conducto principal)
#
# Todas las interpolaciones son lineales / bilineales manuales (sin numpy / scipy).

# --- Ejes de la tabla
AB_AC_VALUES = [0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1.0]   # columnas (Ab/Ac)
QB_QC_VALUES = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]  # filas (Qb/Qc)


# --- Tabla: Cc_branch (ramal) ---
# Filas por Qb/Qc, columnas por Ab/Ac
CC_BRANCH_TABLE = [
    [-1.0, -1.0, -1.0, -0.9, -0.9, -0.9, -0.9],   # Qb/Qc = 0.0
    [ 0.21, -0.46, -0.57, -0.51, -0.53, -0.54, -0.54],  # 0.1
    [ 3.10,  0.37, -0.06, -0.16,  0.23, -0.24, -0.28],  # 0.2
    [ 7.60,  1.50,  0.50,  0.15,  0.04, -0.06, -0.08],  # 0.3
    [14.00,  3.00,  1.20,  0.42,  0.19,  0.03,  0.12],  # 0.4
    [21.00,  4.60,  1.80,  0.53,  0.24,  0.19,  0.15],  # 0.5
    [30.00,  6.40,  2.60,  0.77,  0.35,  0.25,  0.17],  # 0.6
    [41.00,  8.50,  3.40,  0.99,  0.42,  0.28,  0.22],  # 0.7
    [54.00, 12.00,  4.20,  1.20,  0.47,  0.29,  0.25],  # 0.8
    [58.00, 14.00,  5.30,  1.40,  0.49,  0.29,  0.22],  # 0.9
    [84.00, 17.00,  6.30,  1.40,  0.49,  0.21,  0.15],  # 1.0
]


# --- Tabla: Cc_main (ducto principal) ---
# Filas por Qb/Qc, columnas por Ab/Ac
CC_MAIN_TABLE = [
    [ 0.00,   0.00,   0.00,   0.00,   0.00,   0.00,   0.00 ],   # 0.0
    [ 0.01,   0.02,   0.11,   0.13,   0.15,   0.16,   0.17 ],   # 0.1
    [-0.33,   0.01,   0.13,   0.19,   0.24,   0.27,   0.29 ],   # 0.2
    [-1.10,  -0.25,  -0.01,   0.10,   0.22,   0.30,   0.35 ],   # 0.3
    [-2.20,  -0.75,  -0.30,  -0.05,   0.17,   0.26,   0.36 ],   # 0.4
    [-3.60,  -1.40,  -0.70,  -0.35,   0.02,   0.21,   0.32 ],   # 0.5
    [-5.40,  -2.40,  -1.30,  -0.70,  -0.20,   0.06,   0.25 ],   # 0.6
    [-7.60,  -3.40,  -2.00,  -1.20,  -0.50,  -0.15,   0.10 ],   # 0.7
    [-10.0,  -4.60,  -2.70,  -1.80,  -0.90,  -0.43,  -0.15 ],   # 0.8
    [-13.0,  -6.20,  -3.70,  -2.60,  -1.40,  -0.80,  -0.45 ],   # 0.9
    [-16.0,  -7.70,  -4.80,  -3.40,  -1.90,  -1.20,  -0.75 ],   # 1.0
]


# -------------------------
# UTIL: INTERPOLACIONES
# -------------------------
def _lin_interp(x, x0, x1, y0, y1):
    """Linear interpolation (handles x0==x1)."""
    if x1 == x0:
        return y0
    t = (x - x0) / (x1 - x0)
    return y0 + t * (y1 - y0)


def _find_bracketing_indices(grid, x):
    """Return (i0, i1) indices such that grid[i0] <= x <= grid[i1].
       If x is outside grid, returns (0,0) or (n-1,n-1) to clamp.
    """
    if x <= grid[0]:
        return 0, 0
    if x >= grid[-1]:
        return len(grid) - 1, len(grid) - 1
    for i in range(len(grid) - 1):
        if grid[i] <= x <= grid[i + 1]:
            return i, i + 1
    # fallback
    return 0, 0


def _bilinear_from_table(x, y, x_grid, y_grid, table):
    """
    Bilinear interpolation lookup for table given as list-of-rows:
      - table[row_index][col_index]
    x_grid: columns (Ab/Ac)
    y_grid: rows (Qb/Qc)
    x corresponds to Ab/Ac, y corresponds to Qb/Qc
    """
    # find bracketing indices for x (columns) and y (rows)
    ix0, ix1 = _find_bracketing_indices(x_grid, x)
    iy0, iy1 = _find_bracketing_indices(y_grid, y)

    # corner values
    Q11 = table[iy0][ix0]  # (y0, x0)
    Q12 = table[iy0][ix1]  # (y0, x1)
    Q21 = table[iy1][ix0]  # (y1, x0)
    Q22 = table[iy1][ix1]  # (y1, x1)

    x0 = x_grid[ix0]; x1 = x_grid[ix1]
    y0 = y_grid[iy0]; y1 = y_grid[iy1]

    # if either axis is clamped (i0==i1 or j0==j1) the linear helpers handle it
    R1 = _lin_interp(x, x0, x1, Q11, Q12)  # along x at y0
    R2 = _lin_interp(x, x0, x1, Q21, Q22)  # along x at y1

    P = _lin_interp(y, y0, y1, R1, R2)      # along y between R1 and R2
    return P


# -------------------------
# API: funciones expuestas
# -------------------------
def get_co_wye_30_branch(Ab_Ac, Qb_Qc):
    """
    Co for the branch of a 30° Wye (Cc,b).
    Inputs:
      Ab_Ac : Ab / Ac (float)
      Qb_Qc : Qb / Qc (float)
    Returns:
      float: interpolated Cc for branch
    """
    return _bilinear_from_table(Ab_Ac, Qb_Qc, AB_AC_VALUES, QB_QC_VALUES, CC_BRANCH_TABLE)


def get_co_wye_30_main(Ab_Ac, Qb_Qc):
    """
    Co for the main (straight) duct of a 30° Wye (Cc,s).
    Inputs:
      Ab_Ac : Ab / Ac (float)
      Qb_Qc : Qb / Qc (float)
    Returns:
      float: interpolated Cc for main
    """
    return _bilinear_from_table(Ab_Ac, Qb_Qc, AB_AC_VALUES, QB_QC_VALUES, CC_MAIN_TABLE)
