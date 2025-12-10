from tkinter import Button, Label, Frame
from app_state import app_state

def corrections_menu(W, go_back, go_accesories_menu, go_roughness_menu, go_rectangular_eq_menu, go_branches_results_menu):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    pre_result_main = Label(top_frame, text='Menu de correciones', font=('Arial', 35), bg='gray5', fg='gray60')
    pre_result_main.pack(side='top', pady=1)
    
    
    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(expand=True, anchor='center')
    
    
    roughness_btn = Button(middle_frame, text='Correcion por rugosidad del material del ducto',
                        bg='white', fg='black', 
                        relief='raised', 
                        activebackground='DodgerBlue2',
                        activeforeground='OrangeRed2', 
                        font=('Arial', 25, 'bold'),
                        width=40,
                        command =lambda: go_roughness_menu(W))
    roughness_btn.pack(padx=5, pady=10, anchor='n')
    
    
    accesories_btn = Button(middle_frame, text='Calcular perdidas en accesorios', 
                            bg='white', fg='black', 
                            relief='raised', 
                            activebackground='DodgerBlue2', 
                            activeforeground='OrangeRed2', 
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command= lambda: go_accesories_menu(W))
    accesories_btn.pack(padx=5, pady=5)
    
    
    rectangular_eq_btn = Button(middle_frame, text='Ductos rectangulares equivalentes', 
                                bg='white', fg='black', 
                                relief='raised', 
                                activebackground='DodgerBlue2', 
                                activeforeground='OrangeRed2', 
                                font=('Arial', 25, 'bold'),
                                width=40,
                                command = lambda: go_rectangular_eq_menu(W))
    rectangular_eq_btn.pack(padx=5, pady=5)


    re_design_btn = Button(middle_frame, text='Volver a hacer el dimensionamiento preliminar', 
                            bg='white', fg='black', 
                            relief='raised', 
                            activebackground='DodgerBlue2', 
                            activeforeground='OrangeRed2', 
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command= lambda: go_back(W))
    re_design_btn.pack(padx=5, pady=5)


    branches_results_btn = Button(middle_frame, text='Resultados del dimensionamiento de ramalaes', 
                            bg='white', fg='black', 
                            relief='raised', 
                            activebackground='DodgerBlue2', 
                            activeforeground='OrangeRed2', 
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command= lambda: go_branches_results_menu(W))
    branches_results_btn.pack(padx=5, pady=5)

    pdf_btn = Button(middle_frame, text='Generar reporte en PDF',
                        bg='white', fg='black', 
                        relief='raised', 
                        activebackground='DodgerBlue2',
                        activeforeground='OrangeRed2', 
                        font=('Arial', 25, 'bold'),
                        width=40,)
    pdf_btn.pack(padx=5, pady=5)
    
    
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
    
