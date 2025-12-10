# round_butterfly_damper.py
# Calculates Co for a Round Butterfly Damper using bilinear interpolation.
# Table derived from Idelchik (Butterfly Valve, Round)

# No NumPy used → fully compatible with PyInstaller/Nuitka

# -------------------------------------------------------------
# TABULATED VALUES OF Co BASED ON (D/Do) vs θ (degrees)
# -------------------------------------------------------------

theta_values = [0, 10, 20, 30, 40, 50, 60, 70, 75, 80, 85]

ddo_values = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

co_table = [
    [0.19, 0.27, 0.37, 0.49, 0.61, 0.74, 0.86, 0.96, 0.99, 1.00, 1.00],  # D/Do = 0.5
    [0.19, 0.32, 0.48, 0.69, 0.94, 1.20, 1.50, 1.70, 1.80, 1.90, 1.90],  # 0.6
    [0.19, 0.37, 0.64, 1.00, 1.50, 2.10, 2.80, 3.50, 3.70, 3.90, 4.10],  # 0.7
    [0.19, 0.45, 0.87, 1.60, 2.60, 4.10, 6.10, 8.40, 9.40, 10.0, 10.0],   # 0.8
    [0.19, 0.54, 1.20, 2.50, 5.00, 9.60, 17.0, 30.0, 38.0, 45.0, 50.0],  # 0.9
    [0.19, 0.67, 1.80, 4.40, 11.0, 32.0, 113.0, None, None, None, None], # 1.0
]

# -------------------------------------------------------------
# SIMPLE MANUAL INTERPOLATORS (NO NUMPY)
# -------------------------------------------------------------

def interp_1d(x, xp, fp):
    """Linear interpolation with clamping and handling missing values."""
    # Clamp
    if x <= xp[0]:
        return fp[0]
    if x >= xp[-1]:
        return fp[-1]

    # Find interval
    for i in range(len(xp)-1):
        if xp[i] <= x <= xp[i+1]:
            x0, x1 = xp[i], xp[i+1]
            f0, f1 = fp[i], fp[i+1]

            # For None → treat as last valid value (flat)
            if f0 is None:
                f0 = f1
            if f1 is None:
                f1 = f0

            # Linear interpolation
            t = (x - x0) / (x1 - x0)
            return f0 + t * (f1 - f0)

    return fp[-1]


def interp_2d(x, y, x_points, y_points, table):
    """Bilinear interpolation for Co(D/Do, θ)."""

    # Clamp values
    x = max(min(x, x_points[-1]), x_points[0])
    y = max(min(y, y_points[-1]), y_points[0])

    # 1) Interpolate over θ for each row (fixed D/Do)
    co_at_theta = []
    for row in table:
        co_at_theta.append(interp_1d(y, y_points, row))

    # 2) Interpolate over D/Do
    return interp_1d(x, x_points, co_at_theta)


# -------------------------------------------------------------
# PUBLIC FUNCTION
# -------------------------------------------------------------

def get_co_round_butterfly_damper(D_Do, theta):
    """
    Computes Co for a Round Butterfly Damper.

    Inputs:
        D_Do (float): Ratio D/Do (0.5 - 1.0)
        theta (float): Blade angle in degrees (0 - 85)
        app_state: Not used for this fitting, included for consistency

    Output:
        Co (float)
    """

    Co = interp_2d(
        D_Do,
        theta,
        ddo_values,
        theta_values,
        co_table
    )

    print(f"[DEBUG] Round Butterfly Damper → D/Do={D_Do}, θ={theta}")
    print(f"[DEBUG] Co = {Co}")

    return Co
