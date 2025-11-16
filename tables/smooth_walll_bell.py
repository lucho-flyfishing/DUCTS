

def get_co_smooth_wall_bell(r_over_D: float) -> float:
    
    
    table = [
        (0.00, 0.50),
        (0.01, 0.44),
        (0.02, 0.37),
        (0.03, 0.31),
        (0.04, 0.26),
        (0.05, 0.22),
        (0.06, 0.20),
        (0.08, 0.15),
        (0.10, 0.12),
        (0.12, 0.09),
        (0.16, 0.06),
        (0.20, 0.03),  
    ]
    
    
    if r_over_D <= table[0][0]:
        return table[0][1]
    
    
    if r_over_D >= table[-1][0]:
        return table[-1][1]
    
    
    for i in range(len(table) - 1):
        x0, y0 = table[i]
        x1, y1 = table[i + 1]
        
        
        if x0 <= r_over_D <= x1:
            
            t = (r_over_D - x0) / (x1 - x0)
            return y0 + t * (y1 - y0)
        
        
    return table[-1][1]