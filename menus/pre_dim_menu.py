from tkinter import Button, Label, Frame, StringVar
from app_state import app_state
import math

def pre_dim_menu(W, go_back, go_next):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    pre_result_main = Label(top_frame, text='Dimensionamiento preliminar del ramal principal '
                            'dadas las condiciones del aire', font=('Arial', 35), bg='gray5', fg='gray80')
    pre_result_main.pack(side='top', pady=1)
    
    
    #############################################################################################
    #calculos de los valores a mostrar en la pantalla de resultados
    selected =  app_state.selected_option.get()
    T = StringVar(value=app_state.get_temp)
    H = StringVar(value=app_state.get_alt)
    V = StringVar(value=app_state.velocity)

    main_branch_flowrate = app_state.flowrate_entries[app_state.main_branch.get() - 1]
    main_branch_length = app_state.length_entries[app_state.main_branch.get() - 1]
    
    # viscosidad
    
    if selected == 1 or selected == 2:

        T_K = float(T.get()) + 273.15
        mu_0 = 1.716e-5  # viscosidad de referencia en Pa·s
        T_0 = 273.15  # temperatura de referencia en k
        Su = 111  # constante Sutherlan en K
        
        mu = mu_0 * (T_K / T_0) ** 1.5 * (T_0 + Su) / (T_K + Su)  # formula viscosidad del aire
        viscosity = mu # en Pa·s
        app_state.viscosity = viscosity 

    else:
        
        T_K= (float(T.get()) - 32) * 5/9 + 273.1
        T_K= round(T_K, 2)
        
        mu0_si = 1.716e-5    
        T0 = 273.15          
        Su = 111.0            
        
        mu_si = mu0_si * ((T_K / T0) ** 1.5) * (T0 + Su) / (T_K + Su)
        
        mu_imperial = mu_si * 0.02088543423  
        viscosity = mu_imperial # en lb/(ft·s)
        app_state.viscosity = viscosity
        
    
    #presion
    
    P0 = 101325  # Pa
    factor = 0.0000225577
    exponent = 5.2559

    
    P_pa = P0 * (1 - factor * float(H.get())) ** exponent # Pa

    
    if selected == 1 or selected == 2: # conversion y redondeo
        
        P = round(P_pa, 2)  # Pa
    
    elif selected == 3:
        
        P = round(P_pa * 0.0001450377, 2)  # psi
    
    else:
        P = None

    
    app_state.P = P
    
    
    #densidad
    
    if selected == 1 or selected == 2:
        T_K = float(T.get()) + 273.15  # °C → K
        R = 287.05  # J/(kg·K) para aire seco
        rho = P / (R * T_K)  # kg/m³

    elif selected == 3:
        T_R = float(T.get()) + 459.67  # °F → °R
        pressure_lbft2 = P * 144  # psi → lb/ft²
        R = 53.35  # ft·lb/(lb·°R) para aire seco
        rho = pressure_lbft2 / (R * T_R)  # lb/ft³
        
    
    app_state.rho = rho
    
    
    # Perdida de presion y diametro
    if selected == 1:
        
        
            velocity =  float(V.get())# m/s
            Q = main_branch_flowrate / 1000  # L/s → m³/s
            diameter_m = math.sqrt((4 * Q) / (math.pi * velocity)) # m
            diameter = diameter_m * 1000  # m → mm
            
            
            epsilon = 1.5e-7  # rugosidad para materiales típicos de conductos en m
            
            
            D = diameter_m
            Re = (rho * velocity * D) / viscosity
            
            
            f = 0.25 / ( math.log10( (epsilon / (3.7 * D)) + (5.74 / Re**0.9) ) )**2  # factor de fricción para flujo turbulento
            
            
            # perdida de presion por unidad de longitud
            S = f * (1 / diameter_m) * (rho * velocity ** 2) / 2  # Pa por metro
            
            
    elif selected == 2:
        
        
            velocity = float(V.get())  # m/s
            Q = main_branch_flowrate  # m³/s
            diameter_m = math.sqrt((4 * Q) / (math.pi * velocity)) # m
            diameter = diameter_m * 1000  # m → mm
            
            
            epsilon = 1.5e-7  # rugosidad para materiales típicos de conductos en m
            
            
            D = diameter_m # m
            Re = (rho * velocity * D) / viscosity # Reynolds number
            
            
            f = 0.25 / ( math.log10( (epsilon / (3.7 * D)) + (5.74 / Re**0.9) ) )**2  # factor de fricción para flujo turbulento
            
            
            # perdida de presion por unidad de longitud
            S = f * (1 / D) * (rho * velocity ** 2) / 2  # Pa por metro
            
            
    elif selected == 3:
        
        
            velocity = float(V.get())  # fpm (feet per minute)
            Q_ft3s = main_branch_flowrate / 60  # CFM → ft³/s
            D_ft = math.sqrt((4 * Q_ft3s) / (math.pi * velocity))  # ft
            diameter_in = D_ft * 12  # ft → in
            diameter = diameter_in
            
            
            epsilon_in = 0.0005  # rugosidad en pulgadas
            epsilon_ft = epsilon_in / 12  # convertir in → ft
            density_ip = app_state.rho  # lb/ft³
            viscosity_ip = app_state.viscosity  # lb/ft·s
            
            
            D = D_ft  # ya en ft
            V_ft_s = velocity / 60  # convertir fpm → ft/s
            Re = (density_ip * V_ft_s * D) / viscosity_ip  # Reynolds number
            
            
            f_ip = 0.25 / (math.log10((epsilon_ft / (3.7 * D)) + (5.74 / Re**0.9))) ** 2 # factor de fricción para flujo turbulento
            
            
            # perdidas de presion por unidad de longitud
            S_ip = f_ip * (1 / D) * (density_ip * V_ft_s ** 2) / 2  # lb/ft² por ft
            S = S_ip / 5.202  # convertir lb/ft² → in.wg por ft
            
            
    else:
            diameter = None
            S = None
            
            
    def save_diameter_S():
        app_state.Re = Re
        app_state.diameter = diameter
        app_state.S = S
    
    
    print("Caudal ducto principal:", main_branch_flowrate)
    print("Longitud ducto principal:", main_branch_length)
    print("Viscosidad", app_state.viscosity)
    print("Presion", app_state.P)
    print("Densidad", app_state.rho)
    print("Reynolds", app_state.Re) 
    print("Diametro ducto principal:", diameter)
    print("Perdida de presion por longitud:", S)
    
    
    #############################################################################
    
    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(pady=20)
    
    if selected == 3:
        
        
        T_lbl = Label(middle_frame, text=f'Temperatura: {T.get()} °F', font=('Arial', 35), bg='gray5', fg='gray80')
        T_lbl.grid(row=0, column=0, pady=5, sticky='w')
        
        H_lbl = Label(middle_frame, text=f'Altitud: {H.get()} ft', font=('Arial', 35), bg='gray5', fg='gray80')
        H_lbl.grid(row=1, column=0, pady=5, sticky='w')
        
        V_lbl = Label(middle_frame, text=f'Velocidad: {V.get()} ft/s', font=('Arial', 35), bg='gray5', fg='gray80')
        V_lbl.grid(row=2, column=0, pady=5, sticky='w')
        
        F_lbl = Label(middle_frame, text=f'Caudal ramal principal: {main_branch_flowrate} cfm', 
                    font=('Arial', 35), bg='gray5', fg='gray80')
        F_lbl.grid(row=3, column=0, pady=5, sticky='w')
        
        L_lbl = Label(middle_frame, text=f'Longitud ramal principal: {main_branch_length} ft',
                    font=('Arial', 35), bg='gray5', fg='gray80')
        L_lbl.grid(row=4, column=0, pady=5, sticky='w')
        
        D_lbl = Label(middle_frame, text=f'Diámetro ramal principal: {round(diameter,2)} in',
                    font=('Arial', 35), bg='gray5', fg='OrangeRed2')
        D_lbl.grid(row=5, column=0, pady=5, sticky='w')
        
        S_lbl = Label(middle_frame, text=f'Pérdida de presión por longitud: {round(S,4)} in.wg/ft',
                    font=('Arial', 35), bg='gray5', fg='OrangeRed2')
        S_lbl.grid(row=6, column=0, pady=5, sticky='w')
        
        
    else:
        
        
        T_lbl = Label(middle_frame, text=f'Temperatura: {T.get()} °C', font=('Arial', 35), bg='gray5', fg='gray80')
        T_lbl.grid(row=0, column=0, pady=5, sticky='w')
        
        H_lbl = Label(middle_frame, text=f'Altitud: {H.get()} m', font=('Arial', 35), bg='gray5', fg='gray80')
        H_lbl.grid(row=1, column=0, pady=5, sticky='w')
        
        V_lbl = Label(middle_frame, text=f'Velocidad: {V.get()} m/s', font=('Arial', 35), bg='gray5', fg='gray80')
        V_lbl.grid(row=2, column=0, pady=5, sticky='w')
        
        F_lbl = Label(middle_frame, text=f'Caudal ramal principal: {main_branch_flowrate} L/s', 
                    font=('Arial', 35), bg='gray5', fg='gray80')
        F_lbl.grid(row=3, column=0, pady=5, sticky='w')
        
        L_lbl = Label(middle_frame, text=f'Longitud ramal principal: {main_branch_length} m',
                    font=('Arial', 35), bg='gray5', fg='gray80')
        L_lbl.grid(row=4, column=0, pady=5, sticky='w')
        
        D_lbl = Label(middle_frame, text=f'Diámetro ramal principal: {round(diameter,2)} mm',
                    font=('Arial', 35), bg='gray5', fg='OrangeRed2')
        D_lbl.grid(row=5, column=0, pady=5, sticky='w')
        
        S_lbl = Label(middle_frame, text=f'Pérdida de presión por longitud: {round(S,4)} Pa/m',
                    font=('Arial', 35), bg='gray5', fg='OrangeRed2')
        S_lbl.grid(row=6, column=0, pady=5, sticky='w')
        
        
    
    
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
    
    
    back_btn = Button(bottom_frame, text='Regresar y modificar valores', 
                    bg='White', fg='black',
                    relief='raised', 
                    activebackground='DodgerBlue2', 
                    activeforeground='OrangeRed2', 
                    font=('Arial', 20, 'bold'),
                    command=lambda: go_back(W))
    back_btn.pack(side='left', padx=10, pady=10)
    
    
    next_btn = Button(bottom_frame, text='Ir a correcciones y accesorios',
                    bg='White', fg='black',
                    relief='raised', 
                    activebackground='DodgerBlue2', 
                    activeforeground='OrangeRed2', 
                    font=('Arial', 20, 'bold'),
                    command=lambda: (save_diameter_S(), go_next(W)))
    next_btn.pack(side='right', padx=10, pady=10)