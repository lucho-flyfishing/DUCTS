from tkinter import Button, Label, Frame, StringVar
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
                            'rugosidad #### \n Seleccione el material del ducto', 
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
            ["Lisa", 0.00118],  
            ["Lisa", 0.00118],
            ["Lisa", 0.00118],
            ["Lisa", 0.00118],   
            ["Medianamente Lisa", 0.00354],
            ["Promedio", 0.00591],
            ["Promedio", 0.00591],  
            ["Medianamente Rugosa", 0.03543],
            ["Medianamente Rugosa", 0.03543],
            ["Rugosa", 0.11811],
            ["Medianamente Rugosa", 0.03543],
            ["Rugosa", 0.11811],
            ["Rugosa", 0.11811],
            ["Rugosa", 0.11811],
            ["Rugosa", 0.11811],
        ]
    
    
        for i, row in enumerate(table1_roughness_imperial):
            for j, value in enumerate(row):
                label = Label(middle_frame,
                            text=value,
                            borderwidth=1,
                            relief="solid",
                            width=16,
                            height=1)
                label.grid(row=i+2, column=j+1, padx=2, pady=2)
    
    
        roughness_imp_lbl = Label(middle_frame, text='Factor de Rugosidad (in)',
                                font=('Arial', 15),
                                bg='gray5',
                                fg='gray60')
        roughness_imp_lbl.grid(row=1, column=2, padx=5, pady=3, sticky="nsew")
    
    
    else:
        
        table2_roughness = [
            ["Lisa", 0.03],  
            ["Lisa", 0.03],
            ["Lisa", 0.03],
            ["Lisa", 0.03],   
            ["Medianamente Lisa", 0.09],
            ["Promedio", 0.15],
            ["Promedio", 0.15],  
            ["Medianamente Rugosa", 0.9],
            ["Medianamente Rugosa", 0.9],
            ["Rugosa", 3],
            ["Medianamente Rugosa", 0.9],
            ["Rugosa", 3],
            ["Rugosa", 3],
            ["Rugosa", 3],
            ["Rugosa", 3]
        ]
        
        
        for i, row in enumerate(table2_roughness):
            for j, value in enumerate(row):
                label = Label(middle_frame, text=value, 
                            borderwidth=1, 
                            relief="solid",
                            width=16, height=1)
                label.grid(row=i+2, column=j+1, padx=2, pady=2)
    
    
        roughness_lbl = Label(middle_frame, text='Factor de Rugosidad (mm)',
                            font=('Arial', 15), 
                            bg='gray5',
                            fg='gray60')
        roughness_lbl.grid(row=1, column=2, padx=5, pady=3, sticky="nsew")
    
    
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