import numpy as np
from scipy.interpolate import RegularGridInterpolator

# Tabla de Co para Conical Converging Bellmouth, Rectangular
# Ángulos en grados:
angles = np.array([0, 10, 20, 30, 45, 60, 90, 120, 150, 180])

# L/D ratios:
L_over_D = np.array([0.025, 0.05, 0.10, 0.25, 0.60, 1.0])

# Matriz de Co (filas = L/D, columnas = ángulos)
co_matrix = np.array([
    [1.00, 0.96, 0.93, 0.90, 0.85, 0.80, 0.72, 0.64, 0.57, 0.50],
    [1.00, 0.93, 0.86, 0.80, 0.73, 0.67, 0.60, 0.56, 0.52, 0.50],
    [1.00, 0.80, 0.67, 0.55, 0.46, 0.41, 0.41, 0.43, 0.46, 0.50],
    [1.00, 0.68, 0.45, 0.30, 0.21, 0.17, 0.21, 0.28, 0.38, 0.50],
    [1.00, 0.46, 0.27, 0.18, 0.14, 0.13, 0.19, 0.27, 0.37, 0.50],
    [1.00, 0.32, 0.20, 0.14, 0.11, 0.10, 0.16, 0.24, 0.35, 0.50]
])

# Crear interpolador 2D
interpolator = RegularGridInterpolator(
    (L_over_D, angles),
    co_matrix,
    bounds_error=False,
    fill_value=None
)

def get_co_conical_bell(LD_value, angle_value):
    
    
    point = np.array([[LD_value, angle_value]])
    return float(interpolator(point)[0])