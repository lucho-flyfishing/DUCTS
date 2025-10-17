from tkinter import Frame, Label, Entry, Button
from app_state import app_state



def velocity_entry_menu(W, go_back, go_next):
    for widget in W.winfo_children():
        widget.destroy()
    
    
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    velocity_lbl = Label(top_frame, text=' Ingrese la velocidad de aire, '
                        'tenga en cuenta que debe ser la maxima \n velocidad ' 
                        'de todo el sistema',
                        font=('Arial', 30), bg='gray5', fg='gray80')
    velocity_lbl.pack(side='top', pady=1)
    
    
    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(pady=20)
    
    
    selected = app_state.selected_option.get()
    
    if selected == 1:
        velocity_unit_lbl  = Label(middle_frame, text='velocidad (m/s)', 
                                font=('Arial', 24), bg='gray5', fg='OrangeRed2')
        velocity_unit_lbl.grid(row=0, column=0, padx=5)
        
        
    elif selected == 2:
        velocity_unit_lbl = Label(middle_frame, text='velocidad (m/s)', 
                                font=('Arial', 24), bg='gray5', fg='OrangeRed2')
        velocity_unit_lbl.grid(row=0, column=0, padx=5)
        
        
    else:
        velocity_unit_lbl = Label(middle_frame, text='velocidad (fpm)', 
                                font=('Arial', 24), bg='gray5', fg='OrangeRed2')
        velocity_unit_lbl.grid(row=0, column=0, padx=5)
        
        
    velocity_entry = Entry(middle_frame, font=('Arial', 15),
                        bg='white', fg='gray', 
                        relief='solid', bd=2, 
                        highlightthickness=2, 
                        highlightbackground='black')
    velocity_entry.grid(row=0, column=1)
    
    
    v_placeholder = 'Escribe aquí...'
    velocity_entry.insert(0, v_placeholder)
    
    
    def on_focus_in(event):
        if velocity_entry.get() == v_placeholder:
            velocity_entry.delete(0, 'end')
            velocity_entry.config(fg='black')
            
            
    def on_focus_out(event):
        if velocity_entry.get() == '':
            velocity_entry.insert(0, v_placeholder)
            velocity_entry.config(fg='gray')
            
            
    velocity_entry.bind('<FocusIn>', on_focus_in)
    velocity_entry.bind('<FocusOut>', on_focus_out)
    
    
    velocity_entry.focus()
    
    
    def save_velocity():
        velocity = velocity_entry.get()
        app_state.velocity.set(velocity)
        print(f"Guardando velocidad: {app_state.velocity.get()}")
        
        
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
                    command=lambda: [save_velocity(), go_next(W)])
    next_btn.pack(side='right' , padx= 10, pady=10)