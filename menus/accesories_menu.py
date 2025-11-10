from tkinter import Button, Label, Frame
from app_state import app_state

def accesories_menu(W, go_back, go_bells_menu, go_elbows_menu, go_damper_menu,
                    go_diffusers_menu, go_transitions_menu, go_junctions_menu):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
    
    
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    pre_result_main = Label(top_frame, text='Menu de accesorios', 
                            font=('Arial', 30), 
                            bg='gray5', 
                            fg='gray60')
    pre_result_main.pack(side='top', pady=1)
    
    
    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(side='top', fill='both', expand=True)
    
    
    bells_btn = Button(middle_frame, text='1. Campanas',
                        bg='white', fg='black', 
                        relief='raised', 
                        activebackground='DodgerBlue2',
                        activeforeground='OrangeRed2', 
                        font=('Arial', 25, 'bold'),
                        width=40,
                        command =lambda: go_bells_menu(W))
    bells_btn.pack(padx=5, pady=10, anchor='n')
    
    
    elbows_btn = Button(middle_frame, text='2. Codos', 
                            bg='white', fg='black', 
                            relief='raised', 
                            activebackground='DodgerBlue2', 
                            activeforeground='OrangeRed2', 
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command= lambda: go_elbows_menu(W))
    elbows_btn.pack(padx=5, pady=5)
    
    damper_btn = Button(middle_frame, text='3. Dampers', 
                            bg='white', fg='black',
                            relief='raised',
                            activebackground='DodgerBlue2',
                            activeforeground='OrangeRed2',
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command= lambda: go_damper_menu(W))
    damper_btn.pack(padx=5, pady=5)
    
    
    diffuser_btn = Button(middle_frame, text='4. Difusores - Rejillas',
                            bg='white', fg='black',
                            relief='raised',
                            activebackground='DodgerBlue2',
                            activeforeground='OrangeRed2',
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command= lambda: go_diffusers_menu(W))
    diffuser_btn.pack(padx=5, pady=5)
    
    
    reducers_btn = Button(middle_frame, text='5. Transiciones',
                            bg='white', fg='black',
                            relief='raised',
                            activebackground='DodgerBlue2',
                            activeforeground='OrangeRed2',
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command= lambda: go_transitions_menu(W))
    reducers_btn.pack(padx=5, pady=5)
    
    
    tees_btn = Button(middle_frame, text='6. Uniones - Empalmes',
                            bg='white', fg='black',
                            relief='raised',
                            activebackground='DodgerBlue2',
                            activeforeground='OrangeRed2',
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command= lambda: go_junctions_menu(W))
    tees_btn.pack(padx=5, pady=5)
    
    
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
    
    
    back_btn = Button(bottom_frame, text='Regresar', 
                    bg='white', fg='black', 
                    relief='raised', 
                    activebackground='DodgerBlue2', 
                    activeforeground='OrangeRed2',
                    font=('Arial', 20, 'bold'),
                    command=lambda: go_back(W))
    back_btn.pack(side='left', padx=10, pady=10)


