# tables/conical_wall_bell.py

import numpy as np
from scipy.interpolate import RegularGridInterpolator


# ---------------------------------------------
# TABLA ASHRAE - Co para Conical Wall Bellmouth
# ---------------------------------------------
# Ejes:
#   L/D  (filas)
#   theta (grados) (columnas)
# ---------------------------------------------

L_over_D_values = np.array([0.025, 0.05, 0.075, 0.10, 0.15, 0.60])

theta_values = np.array([0, 10, 20, 30, 45, 60, 90, 120, 150, 180])

# Matriz Co en el mismo orden:
# filas → L/D
# columnas → theta
co_matrix = np.array([
    [0.50, 0.47, 0.45, 0.43, 0.41, 0.40, 0.42, 0.44, 0.46, 0.50],  # L/D = 0.025
    [0.50, 0.45, 0.41, 0.36, 0.32, 0.30, 0.34, 0.39, 0.44, 0.50],  # L/D = 0.05
    [0.50, 0.42, 0.35, 0.30, 0.25, 0.23, 0.28, 0.35, 0.43, 0.50],  # L/D = 0.075
    [0.50, 0.39, 0.32, 0.25, 0.21, 0.18, 0.25, 0.33, 0.41, 0.50],  # L/D = 0.10
    [0.50, 0.37, 0.27, 0.20, 0.16, 0.15, 0.23, 0.31, 0.40, 0.50],  # L/D = 0.15
    [0.50, 0.27, 0.18, 0.13, 0.11, 0.12, 0.20, 0.30, 0.40, 0.50],  # L/D = 0.60
])


# Interpolador bilineal
interpolator = RegularGridInterpolator(
    (L_over_D_values, theta_values),
    co_matrix,
    bounds_error=False,
    fill_value=None
)


# ---------------------------------------------------
# FUNCIÓN PRINCIPAL
# ---------------------------------------------------
def get_co_conical_wall_bell(L_D: float, theta: float) -> float:
    """
    Calcula el coeficiente Co para una campana cónica con pared (Conical Wall Bellmouth)
    usando interpolación bilineal basada en la tabla ASHRAE.

    Parámetros:
        L_over_D : float
            Relación L/D (length / hydraulic diameter)
        theta_deg : float
            Ángulo del bisel o inclinación, en grados

    Retorna:
        float : valor interpolado de Co
    """

    point = np.array([[L_D, theta]])
    Co = interpolator(point)[0]

    return float(Co)