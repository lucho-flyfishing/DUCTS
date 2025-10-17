from tkinter import  Label, Radiobutton, Frame, Button
from app_state import app_state

def units_menu(W, go_back, go_next):
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame (W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    units_opt_lbl = Label(top_frame, bg='gray5', fg='gray60', 
                        text='El programa permite escoger entre '
                        'tres sistemas \n de unidades. Seleccione '
                        'las unidades para: caudal, \n pérdidas, '
                        'diámetro y velocidad, respectivamente.',
                        font=('Arial', 30))
    units_opt_lbl.pack(side='top', pady=1)
    
    
    guide_lbl = Label(top_frame, bg='gray5', fg='gray60', 
                    text='(haga clic en una de las opciones, ' 
                    'luego presione siguiente)',
                    font=('Arial', 18))
    guide_lbl.pack(side='top', pady=1)
    
    
    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(expand=True)
    
    
    unidades_lbl = Label(middle_frame, bg='gray5', fg='gray60',
                        text='UNIDADES', 
                        font=('Arial', 25, 'bold'))
    unidades_lbl.pack(pady=10)
    
    
    radio_style = {
        "width": 30,
        "height": 1,
        "font": ("Arial", 25, "bold"),
        "fg": "OrangeRed2",   
        "activeforeground": "black",
        "activebackground": "OrangeRed2",
        "bg": "gray5",                  
        "relief": "raised"              
    }

    def on_select():
        print("Selected option:", app_state.selected_option.get())
        
    Radiobutton(middle_frame, text="1. L/s    :   Pa/m   : mm : m/s : m",
                variable=app_state.selected_option, value=1,
                command=on_select, **radio_style).pack(pady=10)
    
    
    Radiobutton(middle_frame, text="2. m³/s :   Pa/m   : mm : m/s : m", 
                variable=app_state.selected_option, value=2,
                command=on_select, **radio_style).pack(pady=10)
    
    
    Radiobutton(middle_frame, text="3. cfm    : inH20/ft : in : fpm : ft",
                variable=app_state.selected_option, value=3,
                command=on_select, **radio_style).pack(pady=10)
    
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')
    
    
    back_btn = Button(bottom_frame, text='Volver', 
                    bg='White', fg='black',
                    relief='raised', 
                    activebackground='DodgerBlue2', 
                    activeforeground='OrangeRed2', 
                    font=('Arial', 20, 'bold'),
                    command=lambda: go_back(W))
    back_btn.pack(side='left', padx=10, pady=10)
    
    
    next_btn = Button(bottom_frame, text='Siguiente',
                    bg='White', fg='black',
                    relief='raised',
                    activebackground='DodgerBlue2',
                    activeforeground='OrangeRed2',
                    font=('Arial', 20, 'bold'),
                    command=lambda: [on_select(), go_next(W)])
    next_btn.pack(side='right' , padx= 10, pady=10)



    

