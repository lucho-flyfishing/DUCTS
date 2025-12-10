
from tkinter import Button, Label, Frame, StringVar
from app_state import app_state
import math


def branches_results_menu(W, go_back):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
    
    
    selected =  app_state.selected_option.get()
    flowrate_values = app_state.flowrate_entries
    length_values = app_state.length_entries
    V = float(app_state.velocity)           
    density = float(app_state.rho)         
    viscosity = float(app_state.viscosity)



    # lists to store the results of diameter and friction loss per length
    diameters_values = []
    
    
    for i in range(len(flowrate_values)): # Loop through each branch to calculate diameter and friction loss
        flow_value = flowrate_values[i]
        length_value = length_values[i]

        if selected == 1:
            velocity =  float(V)
            Q = flow_value / 1000  # L/s → m³/s
            diameter_m = math.sqrt((4 * Q) / (math.pi * velocity)) # m
            diameters = diameter_m * 1000  # m → mm
            
            epsilon = 1.5e-6 # roughness for typical duct materials in m
            
            D = diameter_m
            Re = (density * velocity * D) / viscosity

            # Friction factor (turbulent, Swamee-Jain approximation)
            f = 0.25 / ( math.log10( (epsilon / (3.7 * D)) + (5.74 / Re**0.9) ) )**2  # friction factor for turbulent flow

            S = f * (1 / diameter_m) * (density * velocity ** 2) / 2  # Pa per meter

        elif selected == 2:
            velocity =  float(V)  # m/s
            Q = flow_value  # m³/s
            diameter_m = math.sqrt((4 * Q) / (math.pi * velocity)) # m
            diameters = diameter_m * 1000  # m → mm
            
            epsilon = 1.5e-6  # roughness for typical duct materials in m
            
            D = diameter_m # already in m
            Re = (density * velocity * D) / viscosity # Reynolds number

            # Friction factor (turbulent, Swamee-Jain approximation)
            f = 0.25 / ( math.log10( (epsilon / (3.7 * D)) + (5.74 / Re**0.9) ) )**2  # friction factor for turbulent flow

            # Friction loss per unit length
            S = f * (1 / D) * (density * velocity ** 2) / 2  # Pa per meter

        elif selected == 3:
            velocity =  float(V)  # fpm (feet per minute)
            Q_ft3s = flow_value / 60  # CFM → ft³/s
            D_ft = math.sqrt((4 * Q_ft3s) / (math.pi * velocity))  # ft
            diameter_in = D_ft * 12  # ft → in
            diameters = diameter_in

            epsilon_in = 0.0000591  # typical roughness in inches
            epsilon_ft = epsilon_in / 12  # convert in → ft
            density_ip = app_state.density  # lb/ft³
            viscosity_ip = app_state.viscosity  # lb/ft·s

            D = D_ft  # already in ft
            V_ft_s = velocity / 60  # convert fpm → ft/s
            Re = (density_ip * V_ft_s * D) / viscosity_ip  # Reynolds number

            # Friction factor (turbulent, Swamee-Jain approximation)
            f_ip = 0.25 / (math.log10((epsilon_ft / (3.7 * D)) + (5.74 / Re**0.9))) ** 2

            # Friction loss per unit length
            S_ip = f_ip * (1 / D) * (density_ip * V_ft_s ** 2) / 2  # lb/ft² per ft
            S = S_ip / 5.202  # convert lb/ft² → in.wg per ft

        else:
            diameters = None

        diameters_values.append(diameters)

        
        app_state.diameters_values = diameters_values  # Store the diameter values in app_state

        print("Diametro calculado para el ramal", i+1, ":", diameters)
        

        
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