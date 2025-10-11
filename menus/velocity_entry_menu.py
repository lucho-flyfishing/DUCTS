from tkinter import Frame, Label, Entry, Button
from app_state import app_state


    
def velocity_entry_menu(W, go_back):
    for widget in W.winfo_children():
        widget.destroy()
    
    
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    velocity_lbl = Label(top_frame, text=' Ingrese la velocidad de aire '
                        'en cada ramal (m/s o ft/min)',
                        font=('Arial', 30), bg='gray5', fg='gray80')
    velocity_lbl.pack(side='top', pady=1)
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')
    
    back_btn = Button(bottom_frame, text='Atrás', 
                    bg='gray20', fg='white',
                    font=('Arial', 16),
                    command=lambda: [go_back(W)])
    back_btn.pack(side='left', padx=10, pady=10)