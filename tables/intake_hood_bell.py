import numpy as np
from scipy.interpolate import RegularGridInterpolator

"""
Tabla de C₀ para intake_hood_bell
Variables:
    θ (degrees)
    L/D (adimensional)
"""

# Valores de la tabla (filas = θ, columnas = L/D)
theta_values = np.array([0, 15])  # grados

LD_values = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 4.0])

# Matriz Co
Co_table = np.array([
    [2.63, 1.83, 1.53, 1.39, 1.31, 1.19, 1.08, 1.06, 1.00],  # θ = 0°
    [1.32, 0.77, 0.60, 0.48, 0.41, 0.30, 0.28, 0.25, 0.25],  # θ = 15°
])


# Interpolador
_co_interpolator = RegularGridInterpolator(
    (theta_values, LD_values),
    Co_table,
    bounds_error=False,
    fill_value=None
)


def get_co_intake_hood_bell(theta: float, L_D: float) -> float:
    """
    Obtiene C₀ para un intake_hood_bell usando interpolación bilineal
    Parámetros:
        theta (float): ángulo en grados
        L_D (float): relación L/D
    Retorna:
        float: valor interpolado de C₀
    """
    point = np.array([[theta, L_D]])
    return float(_co_interpolator(point))