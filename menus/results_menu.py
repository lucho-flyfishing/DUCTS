from tkinter import Button, Label, Frame, StringVar
from app_state import app_state

def results_menu(W, go_back):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    pre_result_main = Label(top_frame, text='Dimensionamiento preliminar, del ramal principal '
                            'dadas las condiciones del aire', font=('Arial', 30), bg='gray12', fg='gray80')
    pre_result_main.pack(side='top', pady=1)
    
    
    
    #calculos de los valores a mostrar en la pantalla de resultados
    selected =  app_state.selected_option.get()
    T = StringVar(value=app_state.get_temp)
    H = StringVar(value=app_state.get_alt)
    V = StringVar(value=app_state.velocity)

    main_branch_flowrate = app_state.flowrate_entries[app_state.main_branch.get() - 1]
    main_branch_length = app_state.length_entries[app_state.main_branch.get() - 1]
    
    # visocity
    
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
        
    
    #density
    
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
        
    #store the density value in app_state
    app_state.rho = rho


    print("Caudal ducto principal:", main_branch_flowrate)
    print("Longitud ducto principal:", main_branch_length)
    print("Viscosidad", app_state.viscosity)
    print("Presion", app_state.P)
    print("Densidad", app_state.rho)

    #############################################################################
    
    middle_frame = Frame(W, bg='gray12')
    middle_frame.pack(pady=20)
    
    if selected == 3:
        T_lbl = Label(middle_frame, text=f'Temperatura: {T.get()} °F', font=('Arial', 20), bg='gray12', fg='gray80')
        T_lbl.grid(row=0, column=0, pady=5)

        H_lbl = Label(middle_frame, text=f'Altitud: {H.get()} ft', font=('Arial', 20), bg='gray12', fg='gray80')
        H_lbl.grid(row=1, column=0, pady=5)

        V_lbl = Label(middle_frame, text=f'Velocidad: {V.get()} ft/s', font=('Arial', 20), bg='gray12', fg='gray80')
        V_lbl.grid(row=2, column=0, pady=5)
        
        F_lbl = Label(middle_frame, text=f'Caudal ramal principal: {main_branch_flowrate} cfm', 
                    font=('Arial', 20), bg='gray12', fg='gray80')
        F_lbl.grid(row=3, column=0, pady=5)
        
        L_lbl = Label(middle_frame, text=f'Longitud ramal principal: {main_branch_length} ft',
                    font=('Arial', 20), bg='gray12', fg='gray80')
        L_lbl.grid(row=4, column=0, pady=5)
        
    else:

        T_lbl = Label(middle_frame, text=f'Temperatura: {T.get()} °C', font=('Arial', 20), bg='gray12', fg='gray80')
        T_lbl.grid(row=0, column=0, pady=5)

        H_lbl = Label(middle_frame, text=f'Altitud: {H.get()} m', font=('Arial', 20), bg='gray12', fg='gray80')
        H_lbl.grid(row=1, column=0, pady=5)

        V_lbl = Label(middle_frame, text=f'Velocidad: {V.get()} m/s', font=('Arial', 20), bg='gray12', fg='gray80')
        V_lbl.grid(row=2, column=0, pady=5)
        
        F_lbl = Label(middle_frame, text=f'Caudal ramal principal: {main_branch_flowrate} L/s', 
                    font=('Arial', 20), bg='gray12', fg='gray80')
        F_lbl.grid(row=3, column=0, pady=5)
        
        L_lbl = Label(middle_frame, text=f'Longitud ramal principal: {main_branch_length} m',
                    font=('Arial', 20), bg='gray12', fg='gray80')
        L_lbl.grid(row=4, column=0, pady=5)
        
        
    
    
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(pady=20)
    
    
    back_btn = Button(bottom_frame, text='Volver', 
                    bg='White', fg='black',
                    relief='raised', 
                    activebackground='DodgerBlue2', 
                    activeforeground='OrangeRed2', 
                    font=('Arial', 20, 'bold'),
                    command=lambda: go_back(W))
    back_btn.pack(side='left', padx=10, pady=10)