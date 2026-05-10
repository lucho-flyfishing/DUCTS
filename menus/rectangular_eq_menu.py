from tkinter import Button, Label, Frame
from app_state import app_state
from tables.rectangular_eq import get_rectangular_eq


def rectangular_eq_menu(W, go_back):
    # Clear window
    for widget in W.winfo_children():
        widget.destroy()
    
    
    # -------------------------
    # TOP FRAME
    # -------------------------
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    title = Label(top_frame,
                  text='Rectangulares EQ',
                  font=('Arial', 30),
                  bg='gray5',
                  fg='gray60')
    title.pack(side='top', pady=1)
    
    
    # -------------------------
    # MIDDLE FRAME
    # -------------------------
    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(pady=10)
    
    
    # -------------------------
    # BOTTOM FRAME
    # -------------------------
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
    
    
    # -------------------------
    # DATA
    # -------------------------
    diameters_values = app_state.diameters_values
    selected = app_state.selected_option.get()
    
    
    # -------------------------
    # UNITS
    # -------------------------
    if selected == 3:
        unit = "in"
    else:
        unit = "mm"
    
    
    # -------------------------
    # HEADERS
    # -------------------------
    headers = [
        "Ramal",
        f"Diámetro ({unit})",
        "Eq 1:1",
        "Eq 2:1",
        "Eq 3:1",
        "Eq 4:1"
    ]
    
    for col, text in enumerate(headers):
        Label(
            middle_frame,
            text=text,
            bg="gray10",
            fg="white",
            font=("Arial", 22, "bold"),
            padx=10,
            pady=5
        ).grid(row=0, column=col, sticky="nsew")
    
    
    # -------------------------
    # BODY TABLE
    # -------------------------
    ratios = [1, 2, 3, 4]
    
    for i, D in enumerate(diameters_values):
        
        row = i + 1
        
        # Ramal
        Label(
            middle_frame,
            text=str(i + 1),
            bg="gray5",
            fg="white",
            font=("Arial", 13)
        ).grid(row=row, column=0)
        
        # Diámetro
        Label(
            middle_frame,
            text=f"{round(D, 2)} {unit}",
            bg="gray5",
            fg="white",
            font=("Arial", 13)
        ).grid(row=row, column=1)
        
        
        # Equivalentes rectangulares
        for j, r in enumerate(ratios):
            
            a, b = get_rectangular_eq(D, r)
            
            text = f"{round(a, 1)} x {round(b, 1)} {unit}"
            
            Label(
                middle_frame,
                text=text,
                bg="gray5",
                fg="white",
                font=("Arial", 13)
            ).grid(row=row, column=j + 2)
    
    
    # -------------------------
    # BACK BUTTON
    # -------------------------
    back_btn = Button(
        bottom_frame,
        text='Regresar',
        bg='white',
        fg='black',
        relief='raised',
        activebackground='DodgerBlue2',
        activeforeground='OrangeRed2',
        font=('Arial', 20, 'bold'),
        command=lambda: go_back(W)
    )
    
    back_btn.pack(padx=10, pady=10, anchor="w")