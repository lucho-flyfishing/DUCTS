from tkinter import Label, Button, Frame, Entry
from app_state import app_state

def alt_temp_menu(W, go_back, go_next):
    for widget in W.winfo_children():
        widget.destroy()
    
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    alt_temp_lbl = Label(top_frame, text=' Ingrese la altitud y '
                        'temperatura del \n lugar de la instalación',
                        font=('Arial', 30), bg='gray5', fg='gray80')
    alt_temp_lbl.pack(side='top', pady=1)
    
    
    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(pady=20)

    selected = app_state.selected_option.get()
    
    if selected == 3:

        temp_lbl = Label(middle_frame, text='Temperatura (F°)', 
                        font=('Arial', 25, 'bold'), 
                        bg='gray5', fg='OrangeRed2')
        temp_lbl.grid(row=1, column=0)
        
        temp_entry = Entry(middle_frame, font=('Arial', 15), 
                        bg='white', fg='gray', 
                        relief='solid', bd=2, 
                        highlightthickness=2, 
                        highlightbackground='black')
        temp_entry.grid(row=1, column=1)
    
        alt_lbl = Label(middle_frame, text='Altitud (ft)', 
                        font=('Arial', 25, 'bold'),
                        bg='gray5', fg='OrangeRed2')
        alt_lbl.grid(row=0, column=0)
        alt_entry = Entry(middle_frame, font=('Arial', 15), 
                        bg='white', fg='gray', 
                        relief='solid', bd=2, 
                        highlightthickness=2, 
                        highlightbackground='black')
        alt_entry.grid(row=0, column=1)
    
    else:
        temp_lbl = Label(middle_frame, text='Temperatura (C°)', 
                        font=('Arial', 25, 'bold'), 
                        bg='gray5', fg='OrangeRed2')
        temp_lbl.grid(row=1, column=0)
        
        temp_entry = Entry(middle_frame, font=('Arial', 15),
                        bg='white', fg='gray',
                        relief='solid', bd=2,
                        highlightthickness=2,
                        highlightbackground='black')
        temp_entry.grid(row=1, column=1)
    
        alt_lbl = Label(middle_frame, text='Altitud (m)',
                        font=('Arial', 25, 'bold'),
                        bg='gray5', fg='OrangeRed2')
        alt_lbl.grid(row=0, column=0)
        
        alt_entry = Entry(middle_frame, font=('Arial', 15),
                        bg='white', fg='gray',
                        relief='solid', bd=2,
                        highlightthickness=2,
                        highlightbackground='black')
        alt_entry.grid(row=0, column=1)
        
        
    def get_values():
        app_state.get_alt = alt_entry.get()
        app_state.get_temp = temp_entry.get()
        print(f"Altitud: {app_state.get_alt}, Temperatura: {app_state.get_temp}") 

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
    
    next_btn = Button(bottom_frame, text='Guardar y continuar',
                    bg='White', fg='black',
                    relief='raised', 
                    activebackground='DodgerBlue2', 
                    activeforeground='OrangeRed2', 
                    font=('Arial', 20, 'bold'),
                    command=lambda: [get_values(), go_next(W)])
    next_btn.pack(side='right', padx=10, pady=10)