from tkinter import Button, Label, Frame
from app_state import app_state

def tees_menu(W, go_back):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')


    tees_lbl = Label(top_frame, text='Tees', font=('Arial', 35), bg='gray5', fg='gray60')
    tees_lbl.pack(side='top', pady=1)

    middle_frame = Frame(W, bg='gray10')
    middle_frame.pack(expand=True, fill='both')
    
    
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