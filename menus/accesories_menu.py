from tkinter import Button, Label, Frame, Radiobutton
from app_state import app_state

def accesories_menu(W, go_back):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
    
    
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    pre_result_main = Label(top_frame, text='Menu de accesorios', 
                            font=('Arial', 30), 
                            bg='gray5', 
                            fg='gray60')
    pre_result_main.pack(side='top', pady=1)
    
    
    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(side='top', fill='both', expand=True)
    
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
        print("Selected accesory:", app_state.selected_accesory.get())
        
    Radiobutton(middle_frame, text="1. Campanas",
                variable=app_state.selected_accesory, value=1,
                command=on_select, **radio_style).pack(pady=10)
    
    
    Radiobutton(middle_frame, text="2. Codos", 
                variable=app_state.selected_accesory, value=2,
                command=on_select, **radio_style).pack(pady=10)
    
    
    Radiobutton(middle_frame, text="3. Intersecciones ",
                variable=app_state.selected_accesory, value=3,
                command=on_select, **radio_style).pack(pady=10)
    
    Radiobutton(middle_frame, text="4. Transiciones",
                variable=app_state.selected_accesory, value=4,
                command=on_select, **radio_style).pack(pady=10)
    
    Radiobutton(middle_frame, text="5. Compuerta",
                variable=app_state.selected_accesory, value=5,
                command=on_select, **radio_style).pack(pady=10)

    
    
        
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
    
    
    back_btn = Button(bottom_frame, text='Regresar', 
                    bg='white', fg='black', 
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
                    command=lambda: on_select())
    next_btn.pack(side='right' , padx= 10, pady=10)
