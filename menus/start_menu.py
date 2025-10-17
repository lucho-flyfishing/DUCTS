from tkinter import Button, Label
from app_state import app_state

def start_menu(W, go_next):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    lbl1 = Label(W, text='DIMENSIONAMIENTO DE DUCTOS \n DE AIRE ACONDICIONADO',
                font=('Arial', 30, 'bold'), bg='gray5', fg='Dark Orange')
    lbl1.pack(pady=1)
    
    
    lbl2 = Label(W, text='Con este programa usted podrá dimensionar ductos de ventilación \n'
                        'considerando las pérdidas debidas a la fricción en tramos rectos y \n'
                        'en accesorios. Solo es necesario conocer el caudal en los \n'
                        'ramales del sistema. Además, el programa presenta los ductos \n'
                        'rectangulares equivalentes.',
                font=('Arial', 26), bg='gray5', fg='gray60')
    lbl2.pack(pady=1)
    
    
    lbl3 = Label(W, text='(En los cálculos se incluyen las correcciones debidas a la altitud, \n'
                        'la temperatura y la rugosidad.)',
                font=('Arial', 16), bg='gray5', fg='gray60')
    lbl3.pack(pady=1)
    
    
    start_button = Button(W, text='Iniciar',
                        bg='White', fg='black',
                        relief='raised',
                        activebackground='DodgerBlue2',
                        activeforeground='OrangeRed2',
                        font=('Arial', 24, 'bold'),
                        command=lambda: go_next(W))
    start_button.pack(pady=30)
    
    
    lbl5 = Label(W, text='Desarrollado en la Universidad del Valle por Luis Jimenez',
                font=('Arial', 12, 'bold'), bg='gray5', fg='dark orange')
    lbl5.pack(side='bottom', pady=1)