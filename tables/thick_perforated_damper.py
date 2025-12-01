# Thick Perforated Damper
# Co = f(t/d , n)
# Interpolación bilineal manual

# Valores de t/d (filas)
t_over_d_values = [0.015, 0.2, 0.4, 0.6]

# Valores de n (columnas)
n_values = [0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90]

# Tabla Co (filas = t/d, columnas = n)
co_table = [
    [52, 30, 18, 8.3, 4.0, 2.0, 0.97, 0.42, 0.13],  # t/d = 0.015
    [48, 28, 17, 7.7, 3.8, 1.9, 0.91, 0.40, 0.13],  # t/d = 0.20
    [46, 27, 17, 7.4, 3.6, 1.8, 0.88, 0.39, 0.13],  # t/d = 0.40
    [42, 24, 15, 6.6, 3.2, 1.6, 0.80, 0.36, 0.13],  # t/d = 0.60
]


def _interp_1d(x, x_list, y_list):
    """Interpolación lineal sencilla."""
    if x <= x_list[0]:
        return y_list[0]
    if x >= x_list[-1]:
        return y_list[-1]

    for i in range(len(x_list) - 1):
        x0, x1 = x_list[i], x_list[i+1]
        if x0 <= x <= x1:
            y0, y1 = y_list[i], y_list[i+1]
            t = (x - x0) / (x1 - x0)
            return y0 + t * (y1 - y0)


def get_co_thick_perforated_damper(t_over_d, n):
    """
    Interpolación bilineal manual para obtener Co.
    Parámetros:
        t_over_d : relación t/d
        n : free area ratio
    """

    # 1) Interpolar en columnas para cada fila (t/d fijo)
    row_results = []
    for row in co_table:
        row_results.append(_interp_1d(n, n_values, row))

    # 2) Con esos valores, interpolar ahora entre filas según t/d
    Co = _interp_1d(t_over_d, t_over_d_values, row_results)

    return Co
