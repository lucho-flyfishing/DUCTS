from tkinter import Label, Button, Frame, Entry
from app_state import app_state

def velocity_range_menu(W, go_back, go_next):
    for widget in W.winfo_children():
        widget.destroy()
    
    #altitude and temperature menu interface
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    ASHRAE_vel_rec_lbl = Label(top_frame, text='Cualquier sistema de ductos puede ' 
                            'diseñarse con ciertos valores máximos admisibles '
                            'para la velocidad del flujo de aire utilizando '
                            'los criterios \n de diseño. A continuación se '
                            'presentan las velocidades de aire recomendadas '
                            'según los criterios de diseño establecidos por ASHRAE,'
                            '\n con el objetivo de garantizar niveles de ruido '
                            'aceptables y un funcionamiento eficiente de los sistemas '
                            'de climatización', 
                            font=('Arial', 17, 'bold'), bg='gray5', fg='gray60')
    ASHRAE_vel_rec_lbl.pack(side='top', pady=1)

    middle_frame = Frame(W, bg='gray5',highlightbackground="Dark Orange", highlightthickness=2)
    middle_frame.pack(expand=True)
    
    selected = app_state.selected_option.get()
    if selected == 3:
    #  VELOCITY RANGE MENU FOR IMPERIAL UNITS
    # table 1 velocities for the main duct
    # Create a table to display the recommended air velocities
        
        table1_main_duct_fpm = [
            [45, 3503.94, 5000.0],   # In shaft or above drywall ceiling
            [35, 2500.0, 3503.94],
            [25, 1692.91, 2500.0],
            [45, 2500.0, 4507.87],   # Above suspended acoustic ceiling
            [35, 1751.97, 2992.13],
            [25, 1200.79, 2007.87],
            [45, 2007.87, 3897.64],  # Duct located within occupied space
            [35, 1456.69, 2598.43],
            [25, 944.88, 1692.91]
        ]

        for i, row in enumerate(table1_main_duct_fpm):
            for j, value in enumerate(row):
                label =Label(middle_frame, text=value, borderwidth=1, relief="solid", width=10, height=1)
                label.grid(row=i+3, column=j+1, padx=2, pady=2)

        #table 1 titles
        max_V_main = Label(middle_frame, text='Velocidad máxima del flujo de aire del conducto '
                        'principal para alcanzar los criterios de diseño acústico', 
                        font=('Arial', 20, 'bold'),  borderwidth=2, relief="solid",bg='gray5', fg='OrangeRed2')
        max_V_main.grid(row=0, column=0, columnspan=4, padx=5, pady=3, sticky="nsew")

        max_vel_lbl = Label(middle_frame, text='Velocidad máxima del flujo de aire (fpm)',
                            font=('Arial', 17, 'bold'), bg='gray5', fg='Dark Orange')
        max_vel_lbl.grid(row=1, column=2, columnspan=4, padx=3, pady=5, sticky="nsew")

        main_duct_lbl = Label(middle_frame, text='Ubicación del ducto principal',
                            font=('Arial', 17, 'bold'), bg='gray5', fg='OrangeRed2')
        main_duct_lbl.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        design_RC_lbl = Label(middle_frame, text='Criterio de diseño', 
                            font=('Arial', 17, 'bold'), bg='gray5', fg='Dark Orange')
        design_RC_lbl.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        rect_duct_lbl = Label(middle_frame, text='Ducto rectangular', 
                            font=('Arial', 17, 'bold'), bg='gray5', fg='Dark Orange')
        rect_duct_lbl.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

        circ_duct_lbl = Label(middle_frame, text='Ducto circular', 
                            font=('Arial', 17, 'bold'), bg='gray5', fg='Dark Orange')
        circ_duct_lbl.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

        drywall_duct_lbl = Label(middle_frame, text='En espacio vacío o sobre techo de placas de yeso', 
                                font=('Arial', 16), borderwidth=2, relief="solid", bg='gray5', fg='gray60')
        drywall_duct_lbl.grid(row=3, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        suspended_duct_lbl = Label(middle_frame, text='Sobre techo acústico suspendido', 
                                font=('Arial', 16), bg='gray5', borderwidth=2, relief="solid", fg='gray60')
        suspended_duct_lbl.grid(row=6, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        occupied_space_duct_lbl = Label(middle_frame, text='Conducto situado dentro de un espacio ocupado', 
                                        font=('Arial', 16), bg='gray5', borderwidth=2, relief="solid", fg='gray60')
        occupied_space_duct_lbl.grid(row=9, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")
        
        table2_branch_duct_fpm = [
            [45, 2795.28, 3996.06],   # In shaft or above drywall ceiling
            [35, 2007.87, 2795.28],
            [25, 1358.27, 2007.87],
            [45, 2007.87, 3602.36],   # Above suspended acoustic ceiling
            [35, 1397.64, 2401.57],
            [25, 964.57, 1614.17],
            [45, 1614.17, 3110.24],   # Duct located within occupied space
            [35, 1161.42, 2086.61],
            [25, 748.03, 1358.27]
        ]

        for i, row in enumerate(table2_branch_duct_fpm):
            for j, value in enumerate(row):
                label = Label(middle_frame, text=value, borderwidth=1, relief="solid", width=10, height=1)
                label.grid(row=i+15, column=j+1, padx=2, pady=2)

        # table 2 titles
        max_V_branch = Label(middle_frame, text='Velocidad máxima del flujo de aire en los ramales '
                            'para alcanzar los criterios de diseño acústico', 
                            font=('Arial', 20, 'bold'), borderwidth=2, relief="solid", bg='gray5', fg='OrangeRed2')
        max_V_branch.grid(row=12, column=0, columnspan=4, padx=3, pady=5, sticky="nsew")
        
        max_vel_branch_lbl = Label(middle_frame, text='Velocidad máxima del flujo de aire (fpm)', 
                                font=('Arial', 17,'bold'), bg='gray5', fg='Dark Orange')
        max_vel_branch_lbl.grid(row=13, column=2, columnspan=4, padx=3, pady=5, sticky="nsew")
        
        branch_duct_lbl = Label(middle_frame, text='Ubicación del ramal', 
                                font=('Arial', 17, 'bold'), bg='gray5', fg='OrangeRed2')
        branch_duct_lbl.grid(row=14, column=0, padx=5, pady=5, sticky="nsew")
        
        branch_design_RC_lbl = Label(middle_frame, text='Criterio de diseño', 
                                    font=('Arial', 17, 'bold'), bg='gray5', fg='Dark Orange')
        branch_design_RC_lbl.grid(row=14, column=1, padx=5, pady=5, sticky="nsew")
        
        branch_rect_duct_lbl = Label(middle_frame, text='Ducto rectangular', 
                                    font=('Arial', 17, 'bold'), bg='gray5', fg='Dark Orange')
        branch_rect_duct_lbl.grid(row=14, column=2, padx=5, pady=5, sticky="nsew")
        
        branch_circ_duct_lbl = Label(middle_frame, text='Ducto circular', 
                                    font=('Arial', 17, 'bold'), bg='gray5', fg='Dark Orange')
        branch_circ_duct_lbl.grid(row=14, column=3, padx=5, pady=5, sticky="nsew")

        branch_drywall_duct_lbl = Label(middle_frame, text='En espacio vacío o sobre techo de placas de yeso', 
                                        font=('Arial', 16), borderwidth=2, relief="solid", bg='gray5', fg='gray60')
        branch_drywall_duct_lbl.grid(row=15, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        branch_suspended_duct_lbl = Label(middle_frame, text='Sobre techo acústico suspendido', 
                                        font=('Arial', 16), borderwidth=2, relief="solid", bg='gray5', fg='gray60')
        branch_suspended_duct_lbl.grid(row=18, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        branch_occupied_space_duct_lbl = Label(middle_frame, text='Conducto situado dentro de un espacio ocupado', 
                                            font=('Arial', 16), borderwidth=2, relief="solid", bg='gray5', fg='gray60')
        branch_occupied_space_duct_lbl.grid(row=21, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        note_lbl = Label(middle_frame, text='Los ductos secundarios deben tener velocidades de flujo de aire de '
                        'aproximadamente del 80% de los valores indicados para el ducto principal.', 
                        font=('Arial', 14), bg='gray5', fg='OrangeRed2')
        note_lbl.grid(row=24, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
    # VELOCITY RANGE MENU FOR METRIC UNITS
    else:
        table1_main_duct = [
            [45, 17.8, 25.4],  # In shaft or above drywall ceiling
            [35, 12.7, 17.8],
            [25, 8.6, 12.7],
            [45, 12.7, 22.9],  # Above suspended acoustic ceiling
            [35, 8.9, 15.2],
            [25, 6.1, 10.2],
            [45, 10.2, 19.8],  # Duct located within occupied space
            [35, 7.4, 13.2],
            [25, 4.8, 8.6]
        ]

        for i, row in enumerate(table1_main_duct):
            for j, value in enumerate(row):
                label =Label(middle_frame, text=value, borderwidth=1, relief="solid", width=10, height=1)
                label.grid(row=i+3, column=j+1, padx=2, pady=2)

        #table 1 titles
        max_V_main = Label(middle_frame, text='Velocidad máxima del flujo de aire del conducto '
                        'principal para alcanzar los criterios de diseño acústico', 
                        font=('Arial', 20, 'bold'),  borderwidth=2, relief="solid",bg='gray5', fg='OrangeRed2')
        max_V_main.grid(row=0, column=0, columnspan=4, padx=5, pady=3, sticky="nsew")

        max_vel_lbl = Label(middle_frame, text='Velocidad máxima del flujo de aire (m/s)', 
                            font=('Arial', 17, 'bold'), bg='gray5', fg='Dark Orange')
        max_vel_lbl.grid(row=1, column=2, columnspan=4, padx=3, pady=5, sticky="nsew")

        main_duct_lbl = Label(middle_frame, text='Ubicación del ducto principal', 
                            font=('Arial', 17, 'bold'), bg='gray5', fg='OrangeRed2')
        main_duct_lbl.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        design_RC_lbl = Label(middle_frame, text='Criterio de diseño', 
                            font=('Arial', 17, 'bold'), bg='gray5', fg='Dark Orange')
        design_RC_lbl.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        rect_duct_lbl = Label(middle_frame, text='Ducto rectangular', 
                            font=('Arial', 17, 'bold'), bg='gray5', fg='Dark Orange')
        rect_duct_lbl.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

        circ_duct_lbl = Label(middle_frame, text='Ducto circular', 
                            font=('Arial', 17, 'bold'), bg='gray5', fg='Dark Orange')
        circ_duct_lbl.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

        drywall_duct_lbl = Label(middle_frame, text='En espacio vacío o sobre techo de placas de yeso', 
                                font=('Arial', 16), borderwidth=2, relief="solid", bg='gray5', fg='gray60')
        drywall_duct_lbl.grid(row=3, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        suspended_duct_lbl = Label(middle_frame, text='Sobre techo acústico suspendido', 
                                font=('Arial', 16), borderwidth=2, relief="solid", bg='gray5', fg='gray60')
        suspended_duct_lbl.grid(row=6, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        occupied_space_duct_lbl = Label(middle_frame, text='Conducto situado dentro de un espacio ocupado', 
                                        font=('Arial', 16), borderwidth=2, relief="solid", bg='gray5', fg='gray60')
        occupied_space_duct_lbl.grid(row=9, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")
        
        # Table 2: Branch duct airflow velocities [RC(N), Rectangular, Circular]
        table2_branch_duct = [
            [45, 14.2, 20.3],  # In shaft or above drywall ceiling
            [35, 10.2, 14.2],
            [25, 6.9, 10.2],
            [45, 10.2, 18.3],  # Above suspended acoustic ceiling
            [35, 7.1, 12.2],
            [25, 4.9, 8.2],
            [45, 8.2, 15.8],   # Duct located within occupied space
            [35, 5.9, 10.6],
            [25, 3.8, 6.9]
        ]

        for i, row in enumerate(table2_branch_duct):
            for j, value in enumerate(row):
                label = Label(middle_frame, text=value, borderwidth=1, relief="solid", width=10, height=1)
                label.grid(row=i+15, column=j+1, padx=2, pady=2)

        # table 2 titles
        max_V_branch = Label(middle_frame, text='Velocidad máxima del flujo de aire en los ramales ' 
                            'para alcanzar los criterios de diseño acústico', 
                            font=('Arial', 20, 'bold'), borderwidth=2, relief="solid", bg='gray5', fg='OrangeRed2')
        max_V_branch.grid(row=12, column=0, columnspan=4, padx=3, pady=5, sticky="nsew")
        
        max_vel_branch_lbl = Label(middle_frame, text='Velocidad máxima del flujo de aire (m/s)',
                                font=('Arial', 17,'bold'), bg='gray5', fg='Dark Orange')
        max_vel_branch_lbl.grid(row=13, column=2, columnspan=4, padx=3, pady=5, sticky="nsew")
        
        branch_duct_lbl = Label(middle_frame, text='Ubicación del ramal', 
                                font=('Arial', 17, 'bold'), bg='gray5', fg='OrangeRed2')
        branch_duct_lbl.grid(row=14, column=0, padx=5, pady=5, sticky="nsew")
        
        branch_design_RC_lbl = Label(middle_frame, text='Criterio de diseño', 
                                    font=('Arial', 17, 'bold'), bg='gray5', fg='Dark Orange')
        branch_design_RC_lbl.grid(row=14, column=1, padx=5, pady=5, sticky="nsew")
        
        branch_rect_duct_lbl = Label(middle_frame, text='Ducto rectangular', 
                                    font=('Arial', 17, 'bold'), bg='gray5', fg='Dark Orange')
        branch_rect_duct_lbl.grid(row=14, column=2, padx=5, pady=5, sticky="nsew")
        
        branch_circ_duct_lbl = Label(middle_frame, text='Ducto circular', 
                                    font=('Arial', 17, 'bold'), bg='gray5', fg='Dark Orange')
        branch_circ_duct_lbl.grid(row=14, column=3, padx=5, pady=5, sticky="nsew")
        
        branch_drywall_duct_lbl = Label(middle_frame, text='En espacio vacío o sobre techo de placas de yeso', 
                                        font=('Arial', 16), borderwidth=2, relief="solid", bg='gray5', fg='gray60')
        branch_drywall_duct_lbl.grid(row=15, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        branch_suspended_duct_lbl = Label(middle_frame, text='Sobre techo acústico suspendido', 
                                    font=('Arial', 16),borderwidth=2, relief="solid", bg='gray5', fg='gray60')
        branch_suspended_duct_lbl.grid(row=18, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        branch_occupied_space_duct_lbl = Label(middle_frame, text='Conducto situado dentro de un espacio ocupado', 
                                            font=('Arial', 16), borderwidth=2, relief="solid", bg='gray5', fg='gray60')
        branch_occupied_space_duct_lbl.grid(row=21, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        note_lbl = Label(middle_frame, text='Los ductos secundarios deben tener velocidades de flujo de aire de '
                        'aproximadamente del 80% de los valores indicados para el ducto principal.', 
                        font=('Arial', 14), bg='gray5', fg='OrangeRed2')
        note_lbl.grid(row=24, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

    
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
        
    back_btn = Button(bottom_frame, text='Regresar',
                    bg='White', fg='black',
                    relief='raised',
                    activebackground='DodgerBlue2',
                    activeforeground='OrangeRed2',
                    font=('Arial', 20, 'bold'),
                    command=lambda: go_back(W))
    back_btn.pack(side='left', padx=10, pady=10)
    
    next_btn = Button(bottom_frame, text='Siguiente',
                    bg='White', fg='black',
                    relief='raised',
                    activebackground='DodgerBlue2',
                    activeforeground='OrangeRed2',
                    font=('Arial', 20, 'bold'),
                    command=lambda: go_next(W))
    next_btn.pack(side='right', padx=10, pady=10)

    