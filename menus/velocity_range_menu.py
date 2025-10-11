from tkinter import Label, Button, Frame, Entry
from app_state import app_state

def velocity_range_menu(W, go_back):
    for widget in W.winfo_children():
        widget.destroy()
    
    Label  (W, text="Menú de rango de velocidad (a definir)",
        font=('Arial', 20, 'bold'),
        bg='grey12', fg='white').pack(pady=20)
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')
    
    back_btn = Button(bottom_frame, text='Regresar',
                    bg='White', fg='black',
                    relief='raised',
                    activebackground='DodgerBlue2',
                    activeforeground='OrangeRed2',
                    font=('Arial', 20, 'bold'),
                    command=lambda: go_back(W))
    back_btn.pack(side='left', padx=10, pady=10)

    