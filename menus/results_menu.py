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

    print("Caudal ducto principal:", main_branch_flowrate)
    print("Longitud ducto principal:", main_branch_length)

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