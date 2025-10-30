from tkinter import Button, Label, Frame, StringVar
from app_state import app_state

def corrections_menu(W, go_back, go_accesories_menu, go_roughness_menu, go_rectangular_eq_menu):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    pre_result_main = Label(top_frame, text='Menu de correciones', font=('Arial', 30), bg='gray12', fg='gray80')
    pre_result_main.pack(side='top', pady=1)
    
    
    middle_frame = Frame(W, bg='gray20')
    middle_frame.pack(side='top', fill='both', expand=True)
    
    
    roughness_btn = Button(middle_frame, text='Correcion por rugosidad del material del ducto',
                        bg='DarkSlateGray', fg='black', 
                        relief='raised', 
                        activebackground='SlateGray',
                        activeforeground='white', 
                        highlightbackground='brown4', 
                        font=('Arial', 25, 'bold'),
                        command =lambda: go_roughness_menu(W))
    roughness_btn.pack(padx=5, pady=5, anchor="w", fill="x")
    
    
    accesories_btn = Button(middle_frame, text='Accesorios en el ducto', 
                            bg='DarkSlateGray', fg='black', 
                            relief='raised', 
                            activebackground='SlateGray', 
                            activeforeground='white', 
                            highlightbackground='brown4', 
                            font=('Arial', 25, 'bold'),
                            command= lambda: go_accesories_menu(W))
    accesories_btn.pack(padx=5, pady=5, anchor="w", fill="x")
    
    
    rectangular_eq_btn = Button(middle_frame, text='Ductos rectangulares equivalentes', 
                                bg='DarkSlateGray', fg='black', 
                                relief='raised', 
                                activebackground='SlateGray', 
                                activeforeground='white', 
                                highlightbackground='brown4', 
                                font=('Arial', 25, 'bold'),
                                command = lambda: go_rectangular_eq_menu(W))
    rectangular_eq_btn.pack(padx=5, pady=5, anchor="w", fill="x")
    
    
    pre_desing_btn = Button(middle_frame, text='Volver a hacer el dimensionamiento preliminar', 
                            bg='DarkSlateGray', fg='black', 
                            relief='raised', 
                            activebackground='SlateGray', 
                            activeforeground='white', 
                            highlightbackground='brown4', 
                            font=('Arial', 25, 'bold'),
                            command= lambda: go_back(W))
    pre_desing_btn.pack(padx=5, pady=5, anchor="w", fill="x")
    
    
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
    
