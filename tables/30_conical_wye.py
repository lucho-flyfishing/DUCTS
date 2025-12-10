# wye_30.py
# Calculates loss coefficient C for Converging Wye (30°)
# Idelchik Diagram 7-4 / SMACNA
# No external libraries are used.

# -----------------------------
# DATA TABLES
# -----------------------------

# --- Column Headings (Flow Ratios) ---
# For Branch Table Top (Qb/Qs) and Main Table (Qb/Qc)
Q_RATIOS_2_0 = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]

# --- 1. BRANCH TABLE (Top Section: C_c,b vs Qb/Qs) ---
# Rows are identified by (As/Ac, Ab/Ac)
BRANCH_QS_ROWS_HEAD = [
    (0.3, 0.2), (0.3, 0.3),
    (0.4, 0.2), (0.4, 0.3), (0.4, 0.4),
    (0.5, 0.2), (0.5, 0.3), (0.5, 0.4), (0.5, 0.5),
    (0.6, 0.2), (0.6, 0.3), (0.6, 0.4), (0.6, 0.5), (0.6, 0.6)
]

BRANCH_TABLE_QB_QS = [
    [-2.4, -0.11, 1.8, 3.4, 4.8, 6.0, 7.1, 8.0, 8.9, 9.7],     # 0.3, 0.2
    [-2.8, -1.3, 0.14, 0.72, 1.4, 2.0, 2.4, 2.8, 3.2, 3.5],    # 0.3, 0.3
    [-1.4, 0.61, 2.3, 3.8, 5.2, 6.3, 7.3, 8.3, 9.1, 9.8],      # 0.4, 0.2
    [-1.8, -0.54, 0.42, 1.2, 1.8, 2.3, 2.7, 3.1, 3.4, 3.7],    # 0.4, 0.3
    [-1.9, -0.89, -0.17, 0.36, 0.76, 1.1, 1.3, 1.5, 1.7, 1.9], # 0.4, 0.4
    [-0.82, 0.97, 2.6, 4.0, 5.3, 6.4, 7.4, 8.3, 9.1, 9.9],     # 0.5, 0.2
    [-1.2, -0.15, 0.71, 1.4, 2.0, 2.5, 2.9, 3.3, 3.6, 3.9],    # 0.5, 0.3
    [-1.4, -0.54, 0.06, 0.50, 0.85, 1.1, 1.3, 1.5, 1.7, 1.8],  # 0.5, 0.4
    [-1.4, -0.66, -0.15, 0.21, 0.48, 0.68, 0.84, 0.97, 1.1, 1.2], # 0.5, 0.5
    [-0.52, 1.2, 2.7, 4.1, 5.3, 6.4, 7.4, 8.3, 9.1, 9.9],      # 0.6, 0.2
    [-0.93, 0.06, 0.85, 1.5, 2.1, 2.6, 3.0, 3.4, 3.7, 4.0],    # 0.6, 0.3
    [-1.1, -0.37, 0.16, 0.55, 0.86, 1.1, 1.3, 1.4, 1.6, 1.8],  # 0.6, 0.4
    [-1.1, -0.49, -0.06, 0.25, 0.48, 0.66, 0.79, 0.90, 1.0, 1.1], # 0.6, 0.5
    [-1.2, -0.55, -0.15, 0.12, 0.31, 0.45, 0.56, 0.65, 0.71, 0.77]# 0.6, 0.6
]

# --- 2. BRANCH TABLE (Bottom Section: C_c,b vs Qb/Qc) ---
# Used typically for larger As/Ac ratios (0.8 - 1.0)
BRANCH_QC_ROWS_HEAD = [
    (0.8, 0.2), (0.8, 0.3), (0.8, 0.4), (0.8, 0.5), (0.8, 0.6), (0.8, 0.7), (0.8, 0.8),
    (1.0, 0.2), (1.0, 0.3), (1.0, 0.4), (1.0, 0.5), (1.0, 0.6), (1.0, 0.8), (1.0, 1.0)
]

BRANCH_TABLE_QB_QC = [
    [-0.27, 1.3, 2.7, 4.0, 5.2, 6.3, 7.3, 8.2, 9.0, 9.7],    # 0.8, 0.2
    [-0.67, 0.18, 0.90, 1.5, 2.0, 2.5, 2.9, 3.3, 3.6, 4.0],  # 0.8, 0.3
    [-0.85, -0.27, 0.16, 0.49, 0.75, 0.97, 1.2, 1.3, 1.4, 1.6], # 0.8, 0.4
    [-0.90, -0.40, -0.07, 0.18, 0.36, 0.50, 0.61, 0.70, 0.78, 0.84], # 0.8, 0.5
    [-0.92, -0.46, -0.16, 0.04, 0.18, 0.29, 0.37, 0.44, 0.49, 0.53], # 0.8, 0.6
    [-0.93, -0.49, -0.21, -0.03, 0.10, 0.19, 0.25, 0.30, 0.34, 0.37], # 0.8, 0.7
    [-0.93, -0.50, -0.24, -0.07, 0.05, 0.13, 0.19, 0.23, 0.27, 0.29], # 0.8, 0.8
    [-0.26, 1.2, 2.6, 3.9, 5.1, 6.1, 7.1, 8.0, 8.8, 9.5],    # 1.0, 0.2
    [-0.65, 0.12, 0.79, 1.4, 1.9, 2.4, 2.8, 3.1, 3.5, 3.8],  # 1.0, 0.3
    [-0.83, -0.34, 0.04, 0.33, 0.58, 0.78, 0.95, 1.1, 1.2, 1.3], # 1.0, 0.4
    [-0.89, -0.48, -0.20, 0, 0.15, 0.27, 0.37, 0.45, 0.51, 0.57], # 1.0, 0.5
    [-0.91, -0.54, -0.31, -0.14, -0.03, 0.06, 0.12, 0.18, 0.22, 0.25], # 1.0, 0.6
    [-0.91, -0.59, -0.38, -0.25, -0.16, -0.10, -0.06, -0.03, -0.01, 0.01], # 1.0, 0.8
    [-0.93, -0.60, -0.40, -0.28, -0.20, -0.14, -0.11, -0.08, -0.07, -0.06] # 1.0, 1.0
]

# --- 3. MAIN TABLE (C_c,s vs Qb/Qc) ---
MAIN_ROWS_HEAD = [
    (0.3, 0.2), (0.3, 0.3),
    (0.4, 0.2), (0.4, 0.3), (0.4, 0.4),
    (0.5, 0.2), (0.5, 0.3), (0.5, 0.4), (0.5, 0.5),
    (0.6, 0.2), (0.6, 0.3), (0.6, 0.4), (0.6, 0.5), (0.6, 0.6),
    (0.8, 0.2), (0.8, 0.3), (0.8, 0.4), (0.8, 0.5), (0.8, 0.6), (0.8, 0.7), (0.8, 0.5),
    (1.0, 0.2), (1.0, 0.3), (1.0, 0.4), (1.0, 0.5), (1.0, 0.6), (1.0, 0.8), (1.0, 1.0)
]

MAIN_TABLE_QB_QC = [
    [4.5, 2.8, 1.5, 0.56, -0.17, -0.74, -1.2, -1.6, -1.9, -2.1],    # 0.3, 0.2
    [4.6, 3.1, 2.0, 1.2, 0.57, 0.08, -0.30, -0.62, -0.89, -1.1],    # 0.3, 0.3
    [1.6, 0.85, 0.16, -0.43, -0.92, -1.3, -1.7, -1.9, -2.2, -2.4],  # 0.4, 0.2
    [1.7, 1.1, 0.58, 0.13, -0.24, -0.56, -0.82, -1.1, -1.3, -1.4],  # 0.4, 0.3
    [1.8, 1.3, 0.80, 0.42, 0.11, -0.15, -0.37, -0.55, -0.72, -0.86],# 0.4, 0.4
    [0.67, 0.18, -0.33, -0.79, -1.2, -1.5, -1.8, -2.1, -2.3, -2.5], # 0.5, 0.2
    [0.75, 0.42, 0.07, -0.25, -0.54, -0.80, -1.0, -1.2, -1.4, -1.5],# 0.5, 0.3
    [0.80, 0.55, 0.28, 0.03, -0.20, -0.40, -0.57, -0.73, -0.86, -0.98], # 0.5, 0.4
    [0.82, 0.62, 0.41, 0.20, 0.02, -0.15, -0.29, -0.42, -0.53, -0.63],  # 0.5, 0.5
    [0.26, -0.11, -0.54, -0.95, -1.3, -1.6, -1.9, -2.1, -2.4, -2.5],    # 0.6, 0.2
    [0.34, 0.13, -0.14, -0.42, -0.67, -0.90, -0.11, -0.13, -0.14, -0.16], # 0.6, 0.3
    [0.39, 0.25, 0.06, -0.14, -0.33, -0.51, -0.66, -0.80, -0.93, -1.0],   # 0.6, 0.4
    [0.41, 0.32, 0.18, 0.03, -0.12, -0.26, -0.38, -0.50, -0.60, -0.69],   # 0.6, 0.5
    [0.43, 0.37, 0.26, 0.14, 0.02, -0.09, -0.19, -0.29, -0.37, -0.45],    # 0.6, 0.6
    [-0.01, -0.30, -0.67, -1.1, -1.4, -1.7, -2.0, -2.2, -2.4, -2.6],      # 0.8, 0.2
    [0.07, -0.07, -0.29, -0.58, -0.76, -0.97, -1.2, -1.3, -1.5, -1.6],    # 0.8, 0.3
    [0.11, 0.05, -0.09, -0.26, -0.42, -0.58, -0.72, -0.85, -0.97, -1.1],  # 0.8, 0.4
    [0.14, 0.12, 0.03, -0.09, -0.21, -0.34, -0.45, -0.55, -0.64, -0.73],  # 0.8, 0.5
    [0.15, 0.17, 0.11, 0.02, -0.07, -0.17, -0.26, -0.34, -0.42, -0.49],   # 0.8, 0.6
    [0.17, 0.21, 0.17, 0.11, 0.03, -0.05, -0.12, -0.19, -0.26, -0.32],    # 0.8, 0.7
    [0.17, 0.23, 0.22, 0.17, 0.11, 0.05, -0.02, -0.07, -0.13, -0.18],     # 0.8, 0.8
    [-0.05, -0.33, -0.70, -1.1, -1.4, -1.7, -2.0, -2.2, -2.4, -2.6],      # 1.0, 0.2
    [0.03, -0.10, -0.31, -0.55, -0.78, -0.98, -1.2, -1.3, -1.5, -1.6],    # 1.0, 0.3
    [0.07, 0.02, -0.12, -0.28, -0.44, -0.59, -0.73, -0.86, -0.98, -1.1],  # 1.0, 0.4
    [0.09, 0.09, 0.01, -0.11, -0.23, -0.35, -0.46, -0.56, -0.65, -0.74],  # 1.0, 0.5
    [0.11, 0.14, 0.09, 0, -0.09, -0.18, -0.27, -0.35, -0.43, -0.50],      # 1.0, 0.6
    [0.13, 0.20, 0.19, 0.15, 0.09, 0.03, -0.03, -0.08, -0.14, -0.19],     # 1.0, 0.8
    [0.14, 0.24, 0.25, 0.24, 0.20, 0.16, 0.12, 0.08, 0.04, 0]             # 1.0, 1.0
]

# -----------------------------
# Helper functions
# -----------------------------

def linear_interp(x, x0, x1, y0, y1):
    if x1 == x0:
        return y0
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

def interp_2d_irregular(as_ac, ab_ac, q_val, row_headers, q_headers, data_table):
    """
    Interpolates a table where rows are defined by tuples (As/Ac, Ab/Ac)
    and columns are defined by flow ratio Q.
    1. Interpolates Q (columns) for all relevant rows.
    2. Interpolates Ab/Ac (inner geometry).
    3. Interpolates As/Ac (outer geometry).
    """

    # 1. Identify unique As/Ac values available in the table
    available_as = sorted(list(set(r[0] for r in row_headers)))
    
    # Find bounding As/Ac
    as_idx = -1
    for i in range(len(available_as) - 1):
        if available_as[i] <= as_ac <= available_as[i+1]:
            as_idx = i
            break
    
    if as_idx == -1:
        # Out of bounds or exact match end
        if as_ac < available_as[0]: as_targets = [available_as[0]]
        elif as_ac > available_as[-1]: as_targets = [available_as[-1]]
        else: as_targets = [as_ac] # Should not happen with logic above
    else:
        as_targets = [available_as[as_idx], available_as[as_idx+1]]

    results_per_as = []

    for target_as in as_targets:
        # Get all rows belonging to this As/Ac
        subset_rows = []
        for idx, (r_as, r_ab) in enumerate(row_headers):
            if r_as == target_as:
                subset_rows.append((r_ab, idx))
        
        subset_rows.sort(key=lambda x: x[0]) # Sort by Ab/Ac

        if not subset_rows:
            continue

        # Find bounding Ab/Ac within this As/Ac group
        ab_vals = [x[0] for x in subset_rows]
        ab_idx = -1
        for i in range(len(ab_vals) - 1):
            if ab_vals[i] <= ab_ac <= ab_vals[i+1]:
                ab_idx = i
                break
        
        # Select rows to interpolate
        if ab_idx != -1:
            rows_to_use = [subset_rows[ab_idx], subset_rows[ab_idx+1]]
        else:
            # Clamp to nearest
            if ab_ac < ab_vals[0]: rows_to_use = [subset_rows[0]]
            else: rows_to_use = [subset_rows[-1]]

        # Interpolate Q (columns) for these specific rows
        q_results = []
        for r_ab, table_row_idx in rows_to_use:
            # Column interpolation logic
            row_data = data_table[table_row_idx]
            # Find Q bounds
            c_val = None
            for k in range(len(q_headers) - 1):
                if q_headers[k] <= q_val <= q_headers[k+1]:
                    c_val = linear_interp(q_val, q_headers[k], q_headers[k+1], 
                                        row_data[k], row_data[k+1])
                    break
            if c_val is None:
                # Clamp Q
                if q_val < q_headers[0]: c_val = row_data[0]
                else: c_val = row_data[-1]
            
            q_results.append((r_ab, c_val))

        # Interpolate Ab/Ac
        if len(q_results) == 1:
            final_c_for_as = q_results[0][1]
        else:
            final_c_for_as = linear_interp(ab_ac, 
                                        q_results[0][0], q_results[1][0], 
                                        q_results[0][1], q_results[1][1])
        
        results_per_as.append((target_as, final_c_for_as))

    # Finally, interpolate As/Ac
    if len(results_per_as) == 1:
        return results_per_as[0][1]
    else:
        return linear_interp(as_ac, 
                            results_per_as[0][0], results_per_as[1][0], 
                            results_per_as[0][1], results_per_as[1][1])


# -----------------------------
# Public functions
# -----------------------------

def get_wye_30_branch(Qs, Qc, Qb, As, Ac, Ab):
    """
    Calculates Branch Coefficient C_c,b.
    Automatically selects between Top Table (Qb/Qs) and Bottom Table (Qb/Qc)
    based on As/Ac ratio availability.
    """
    as_ac = As / Ac
    ab_ac = Ab / Ac
    
    # Decide which table to use based on As/Ac range
    # Top table covers As/Ac 0.3 - 0.6
    # Bottom table covers As/Ac 0.8 - 1.0
    
    if as_ac <= 0.65:
        # Use Top Table (Qb/Qs based)
        if Qs == 0: return None # Avoid division by zero
        q_ratio = Qb / Qs
        return interp_2d_irregular(as_ac, ab_ac, q_ratio, 
                                BRANCH_QS_ROWS_HEAD, Q_RATIOS_2_0, BRANCH_TABLE_QB_QS)
    else:
        # Use Bottom Table (Qb/Qc based)
        if Qc == 0: return None
        q_ratio = Qb / Qc
        return interp_2d_irregular(as_ac, ab_ac, q_ratio, 
                                BRANCH_QC_ROWS_HEAD, Q_RATIOS_2_0, BRANCH_TABLE_QB_QC)

def get_wye_30_main(Qc, Qb, As, Ac, Ab):
    """
    Calculates Main Coefficient C_c,s based on Qb/Qc.
    """
    as_ac = As / Ac
    ab_ac = Ab / Ac
    if Qc == 0: return None
    q_ratio = Qb / Qc
    
    return interp_2d_irregular(as_ac, ab_ac, q_ratio, 
                            MAIN_ROWS_HEAD, Q_RATIOS_2_0, MAIN_TABLE_QB_QC)