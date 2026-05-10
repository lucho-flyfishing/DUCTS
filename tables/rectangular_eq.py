def get_rectangular_eq(D, r, tol=1e-6, max_iter=100):
    """
    Calcula dimensiones rectangulares equivalentes (a, b)
    a partir de diámetro circular D y relación r = a/b.
    
    Parámetros:
        D : float  -> diámetro equivalente
        r : float  -> relación de aspecto (a/b)
    
    Retorna:
        (a, b)
    """
    
    # -----------------------------------------
    # Función a resolver: f(b) = 0
    # -----------------------------------------
    def f(b):
        a = r * b
        return 1.30 * ((a * b)**0.625) / ((a + b)**0.25) - D
    
    
    # -----------------------------------------
    # Intervalo inicial (heurístico robusto)
    # -----------------------------------------
    b_low = 1e-6
    b_high = D  # buen punto de partida físico
    
    
    # Asegurar que hay cambio de signo
    while f(b_high) < 0:
        b_high *= 2
    
    
    # -----------------------------------------
    # Método de bisección
    # -----------------------------------------
    for _ in range(max_iter):
        b_mid = (b_low + b_high) / 2
        f_mid = f(b_mid)
        
        if abs(f_mid) < tol:
            break
        
        if f_mid > 0:
            b_high = b_mid
        else:
            b_low = b_mid
    
    
    b = b_mid
    a = r * b
    
    return a, b