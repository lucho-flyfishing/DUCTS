from tkinter import Button, Label, Frame, StringVar
from app_state import app_state

def corrections_menu(W, go_back):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    pre_result_main = Label(top_frame, text='Menu de correciones', font=('Arial', 30), bg='gray12', fg='gray80')
    pre_result_main.pack(side='top', pady=1)

    test1 = Label(top_frame, text=f'diametro: {app_state.diameter} mm', font=('Arial', 20), bg='gray12', fg='gray80')
    test1.pack(side='top', pady=10)

    test2 = Label(top_frame, text=f'(pérdidas {app_state.S} mm)', 
                font=('Arial', 20), bg='gray12', fg='gray80')
    test2.pack(side='top', pady=10)
    
    
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
    
    back_btn = Button(bottom_frame, text='Volver', 
                    bg='White', fg='black',
                    relief='raised', 
                    activebackground='DodgerBlue2', 
                    activeforeground='OrangeRed2', 
                    font=('Arial', 20, 'bold'),
                    command=lambda: go_back(W))
    back_btn.pack(side='left', padx=10, pady=10)