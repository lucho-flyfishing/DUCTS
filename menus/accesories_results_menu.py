from tkinter import Button, Label, Frame
from app_state import app_state

def accesories_results_menu(W, go_back):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
    
    
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    results_main = Label(top_frame, text='resultados de accesorios', 
                            font=('Arial', 30), 
                            bg='gray5', 
                            fg='gray60')
    results_main.pack(side='top', pady=1)
    
    
    
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
