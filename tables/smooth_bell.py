def get_co_smooth_bell(r_D):
    tabla = {
        0.00: 1.00,
        0.01: 0.87,
        0.02: 0.74,
        0.03: 0.61,
        0.04: 0.51,
        0.05: 0.40,
        0.06: 0.32,
        0.08: 0.20,
        0.10: 0.15,
        0.12: 0.10,
        0.16: 0.06,
        0.20: 0.03  # para ≥0.20
    }

    # Si r/D supera el rango de la tabla (≥0.20)
    if r_D >= 0.20:
        return tabla[0.20]

    # Obtener claves ordenadas
    valores_rD = sorted(tabla.keys())

    # Si está por debajo del primer valor
    if r_D <= valores_rD[0]:
        return tabla[valores_rD[0]]

    # Buscar intervalo para interpolar linealmente
    for i in range(len(valores_rD) - 1):
        r1, r2 = valores_rD[i], valores_rD[i + 1]
        if r1 <= r_D <= r2:
            Co1, Co2 = tabla[r1], tabla[r2]
            # Interpolación lineal
            Co = Co1 + (Co2 - Co1) * ((r_D - r1) / (r2 - r1))
            return Co

    # Valor por defecto (no debería llegar aquí)
    return None


r_bell = 2
D_bell = 5
r_bell__D_bell = r_bell / D_bell
result = get_co_smooth_bell(r_bell__D_bell)



