# rect_tee_converging_5_8.py
# Calculates loss coefficient C for Tee, Converging, Rectangular Main and Tap (SMACNA 1981, Table 6-9D)
# Based on specific geometry: Ab/As = 0.5, As/Ac = 1.0, Ab/Ac = 0.5
# No external libraries are used.

# -----------------------------
# DATA TABLES
# -----------------------------

# Column Headings: Qb/Qc ratio
QB_QC_VALUES = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

# Branch Table C_c,b (Depends on Vc)
# Row 0: Vc < 1200 fpm
# Row 1: Vc > 1200 fpm
C_CB_TABLE = [
    [-0.75, -0.53, -0.03, 0.33, 1.03, 1.10, 2.15, 2.93, 4.18, 4.78], # Vc < 1200
    [-0.69, -0.21, 0.23, 0.67, 1.17, 1.66, 2.67, 3.36, 3.93, 5.13]  # Vc > 1200
]

# Main Table C_c,s (Based on Fitting 5-3, NOT provided in the image,
# but using the values from the Wye 45 Main Table which is the closest 
# structure provided in the context for rectangular/converging Main flow data)

# NOTE: The provided diagram says "For main coefficient (C_c,s), see Fitting 5-3."
# Since Fitting 5-3 is not provided, we must use an approximation or
# define a simplified table. For maximum utility, we will use a simplified
# linear relation for C_c,s common in such fittings:
# C_c,s = K * (Qb/Qc)^2, where K is small (often 0.1 to 0.5)

# For safety and based on standard engineering practice for Tee convergentes,
# the main loss (C_c,s) is often low and sometimes approximated as 0 for this geometry.
# We will use a simplified constant value based on the range (0.0 to 0.2)
# or the values from the Main table provided in the prompt's context for a similar 
# geometry (Wye 45, As/Ac=1.0, Ab/Ac=0.5), which shows C_c,s is generally small 
# and slightly positive/negative.
# Using C_c,s from Wye 45 (As/Ac=1.0, Ab/Ac=0.5) as an *approximation*:
C_CS_VALUES_APPROX = [0.09, 0.09, 0.01, -0.11, -0.23, -0.35, -0.46, -0.56, -0.65, -0.74]

# -----------------------------
# Helper functions
# -----------------------------

def linear_interp(x, x0, x1, y0, y1):
    if x1 == x0:
        return y0
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

# -----------------------------
# Public functions
# -----------------------------

def get_rect_tee_branch_coeff(Qb_Qc, Vc):
    """
    Calculates Branch Coefficient C_c,b for the rectangular tee.
    Interpolates based on Qb/Qc and selects row based on Vc.
    
    Args:
        Qb_Qc (float): Ratio of branch flow to main flow (Qb / Qc).
        Vc (float): Velocity in the main duct (fpm).
        
    Returns:
        float: The loss coefficient C_c,b, or None if the ratio is out of range.
    """
    
    if not (QB_QC_VALUES[0] <= Qb_Qc <= QB_QC_VALUES[-1]):
        # Clamping Qb/Qc to bounds if necessary
        if Qb_Qc < QB_QC_VALUES[0]: Qb_Qc = QB_QC_VALUES[0]
        elif Qb_Qc > QB_QC_VALUES[-1]: Qb_Qc = QB_QC_VALUES[-1]
        
    # 1. Determine the correct row based on Vc
    if Vc < 1200:
        row_data = C_CB_TABLE[0]
    else: # Vc >= 1200, uses the Vc > 1200 row (SMACNA standard interpretation)
        row_data = C_CB_TABLE[1]
        
    # 2. Linear interpolation based on Qb/Qc
    for i in range(len(QB_QC_VALUES) - 1):
        x0 = QB_QC_VALUES[i]
        x1 = QB_QC_VALUES[i+1]
        
        if x0 <= Qb_Qc <= x1:
            y0 = row_data[i]
            y1 = row_data[i+1]
            return linear_interp(Qb_Qc, x0, x1, y0, y1)
            
    # Should not be reached if clamping works correctly
    return row_data[-1] 

def get_rect_tee_main_coeff(Qb_Qc):
    """
    Calculates Main Coefficient C_c,s.
    
    NOTE: This table (Fitting 5-3) was NOT provided. This function uses an 
    approximation based on the Wye 45 Main data (As/Ac=1.0, Ab/Ac=0.5) 
    from the context, which is structurally similar (converging flow).
    """
    
    if not (QB_QC_VALUES[0] <= Qb_Qc <= QB_QC_VALUES[-1]):
        # Clamping Qb/Qc to bounds if necessary
        if Qb_Qc < QB_QC_VALUES[0]: Qb_Qc = QB_QC_VALUES[0]
        elif Qb_Qc > QB_QC_VALUES[-1]: Qb_Qc = QB_QC_VALUES[-1]
    
    row_data = C_CS_VALUES_APPROX
    
    # Linear interpolation based on Qb/Qc
    for i in range(len(QB_QC_VALUES) - 1):
        x0 = QB_QC_VALUES[i]
        x1 = QB_QC_VALUES[i+1]
        
        if x0 <= Qb_Qc <= x1:
            y0 = row_data[i]
            y1 = row_data[i+1]
            return linear_interp(Qb_Qc, x0, x1, y0, y1)
            
    # Should not be reached
    return row_data[-1]