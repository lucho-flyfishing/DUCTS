from tkinter import Button, Label, Frame, StringVar, Entry
from app_state import app_state

def roughness_menu(W, go_back):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    pre_result_main = Label(top_frame, text='Menu de rugosidad', 
                            font=('Arial', 30),
                            bg='gray5',
                            fg='gray60')
    pre_result_main.pack(side='top', pady=1)
    
    
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    roughness_top_lbl = Label(top_frame, text='Hasta ahora se ha trabajado con una ' 
                            'rugosidad  de 0.0015 mm / 0.0000591 in \n Seleccione el factor ' 
                            'según el material del ducto', 
                            font=('Arial', 25), 
                            bg='gray5',
                            fg='gray60')
    roughness_top_lbl.pack(side='top', pady=1)
    
    
    middle_frame = Frame(W, bg='gray5',
                        highlightbackground="red",
                        highlightthickness=2)
    middle_frame.pack(expand=True)
    
    
    title_lbl = Label(middle_frame, text='Factores de rugosidad para el material del ducto',
                    borderwidth=2, 
                    relief="solid",
                    bg='gray5',
                    fg='gray60',
                    font=('Arial', 20, 'bold'))
    title_lbl.grid(row=0, column=0, columnspan=3, padx=5, pady=3, sticky="nsew")
    
    
    material_lbl = Label(middle_frame, text='Material',
                        font=('Arial', 15),
                        bg='gray5',
                        fg='gray60')
    material_lbl.grid(row=1, column=0, padx=5, pady=3, sticky="nsew")
    
    
    category_lbl = Label(middle_frame, text='Categoría',
                        font=('Arial', 15),
                        bg='gray5',
                        fg='gray60')
    category_lbl.grid(row=1, column=1, padx=5, pady=3, sticky="nsew")
    
    
    selected =  app_state.selected_option.get()
    
    if selected == 3:
    
        table1_roughness_imperial = [
            ["Acero al carbon sin recubrir","Lisa", 0.001181102],  
            ["Ducto plastico PVC", "Lisa",0.001181102],
            ["Aluminio","Lisa", 0.001181102],
            ["Acero galvanizado juntas longitudinales","Lisa", 0.001181102],   
            ["Acero galvanizado juntas en espiral","Medianamente Lisa",0.003543307],
            ["Laminas de acero galvanizado baño caliente juntas longitudinales","Promedio", 0.005905512],
            ["Ducto rigido en fibra de vidrio","Medianamente Rugosa", 0.0354331],  
            ["Recubrimiento de fibra de vidrio","Medianamente Rugosa", 0.0354331],
            ["Recubrimiento fibra de vidrio con aerosol","Rugosa", 0.11811],
            ["Ducto flexible metalico","Rugosa",0.11811],
            ["Ducto flexible en todo tipo de tejidos y alambre","Rugosa",0.11811],
            ["Concreto","Rugosa",0.11811]
        ]
    
    
        for i, row in enumerate(table1_roughness_imperial):
            for j, value in enumerate(row):
                label = Label(middle_frame,
                            text=value,
                            borderwidth=0.5,
                            relief="solid",
                            height=1)
                label.grid(row=i+2, column=j, padx=2, pady=2, sticky="nsew")
    
    
        roughness_imp_lbl = Label(middle_frame, text='Factor de Rugosidad (in)',
                                font=('Arial', 15),
                                bg='gray5',
                                fg='gray60')
        roughness_imp_lbl.grid(row=1, column=2, padx=5, pady=3, sticky="nsew")
    
    
    else:
        
        table2_roughness = [
            ["Acero al carbon sin recubrir","Lisa", 0.03],  
            ["Ducto plastico PVC", "Lisa", 0.03],
            ["Aluminio","Lisa", 0.03],
            ["Acero galvanizado juntas longitudinales","Lisa", 0.03],   
            ["Acero galvanizado juntas en espiral","Medianamente Lisa", 0.09],
            ["Laminas de acero galvanizado baño caliente juntas longitudinales","Promedio", 0.15],
            ["Ducto rigido en fibra de vidrio","Medianamente Rugosa", 0.9],  
            ["Recubrimiento de fibra de vidrio","Medianamente Rugosa", 0.9],
            ["Recubrimiento fibra de vidrio con aerosol","Rugosa", 3],
            ["Ducto flexible metalico","Rugosa", 3],
            ["Ducto flexible en todo tipo de tejidos y alambre","Rugosa", 3],
            ["Concreto","Rugosa", 3]
        ]
        
        
        for i, row in enumerate(table2_roughness):
            for j, value in enumerate(row):
                label = Label(middle_frame, text=value, 
                            borderwidth=0.5, 
                            relief="solid",
                            height=1)
                label.grid(row=i+2, column=j, padx=2, pady=2, sticky="nsew")
    
    
        roughness_lbl = Label(middle_frame, text='Factor de Rugosidad (mm)',
                            font=('Arial', 15), 
                            bg='gray5',
                            fg='gray60')
        roughness_lbl.grid(row=1, column=2, padx=5, pady=3, sticky="nsew")
    
    new_rough_lbl = Label(W, text=('introduzca el valor de rugosidad que desea utilizar para el cálculo \n'
                                'luego presione Siguiente'), 
                        font=('Arial', 26), 
                        bg='gray5', 
                        fg='gray60')
    new_rough_lbl.pack(pady=1)
    
    
    new_rough_entry = Entry(W, font=('Arial', 12), 
                            bg='white', fg='gray', 
                            relief='solid', bd=2, 
                            highlightthickness=2, 
                            highlightbackground='black')
    new_rough_entry.pack(pady=5, ipady=5, ipadx=10)
    
    
    
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
    
    
    back_btn = Button(bottom_frame, text='Regresar', 
                    bg='white', fg='black', 
                    relief='raised', 
                    activebackground='DodgerBlue2', 
                    activeforeground='OrangeRed2', 
                    highlightbackground='brown4', 
                    font=('Arial', 20, 'bold'),
                    command=lambda: go_back(W))
    back_btn.pack(padx=10, pady=10, anchor="w")