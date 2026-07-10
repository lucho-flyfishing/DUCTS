from tkinter import Button, Label, Frame
from app_state import app_state

def start_menu(W, go_tramos, go_accesorios):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()


    lbl1 = Label(W, text='DIMENSIONAMIENTO DE DUCTOS',
                font=('Arial', 30, 'bold'), bg='gray5', fg='Dark Orange')
    lbl1.pack(pady=1)


    lbl2 = Label(W, text='Este programa dimensiona ductos de aire mediante equal-friction method \n'
                        'y calcula las pérdidas de presión por accesorios.',
                font=('Arial', 26), bg='gray5', fg='gray60')
    lbl2.pack(pady=1)


    lbl3 = Label(W, text='(En los cálculos se incluyen las correcciones debidas a la altitud, \n'
                        'la temperatura y la rugosidad.)',
                font=('Arial', 16), bg='gray5', fg='gray60')
    lbl3.pack(pady=1)


    choose_lbl = Label(W, text='¿Qué desea calcular?',
                    font=('Arial', 20, 'bold'), bg='gray5', fg='gray80')
    choose_lbl.pack(pady=(30, 5))


    buttons_frame = Frame(W, bg='gray5')
    buttons_frame.pack(pady=10)


    tramos_button = Button(buttons_frame, text='Tramos rectos',
                        bg='White', fg='black',
                        relief='raised',
                        activebackground='DodgerBlue2',
                        activeforeground='OrangeRed2',
                        font=('Arial', 24, 'bold'),
                        width=18,
                        command=lambda: go_tramos(W))
    tramos_button.pack(side='left', padx=20)


    accesorios_button = Button(buttons_frame, text='Accesorios',
                        bg='White', fg='black',
                        relief='raised',
                        activebackground='DodgerBlue2',
                        activeforeground='OrangeRed2',
                        font=('Arial', 24, 'bold'),
                        width=18,
                        command=lambda: go_accesorios(W))
    accesorios_button.pack(side='left', padx=20)


    lbl5 = Label(W, text='Desarrollado en la Universidad del Valle por Luis Jimenez',
                font=('Arial', 12, 'bold'), bg='gray5', fg='dark orange')
    lbl5.pack(side='bottom', pady=1)