from tkinter import Button, Label, Frame, StringVar
from app_state import app_state

def rectangular_eq_menu(W, go_back):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    pre_result_main = Label(top_frame, text='Rectangulares EQ', font=('Arial', 30), bg='gray12', fg='gray80')
    pre_result_main.pack(side='top', pady=1)
    
    
    middle_frame = Frame(W, bg='gray20')
    middle_frame.pack(side='top', fill='both', expand=True)
    
    
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
    
    back_btn = Button(bottom_frame, text='Regresar', 
                    bg='DarkSlateGray', fg='black', 
                    relief='raised', 
                    activebackground='SlateGray', 
                    activeforeground='white', 
                    highlightbackground='brown4', 
                    font=('Arial', 20, 'bold'),
                    command=lambda: go_back(W))
    back_btn.pack(padx=10, pady=10, anchor="w")