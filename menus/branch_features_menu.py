from tkinter import Label, Button, Frame, Entry
from app_state import app_state

def branch_features_menu(W, go_back, go_next):
    for widget in W.winfo_children():
        widget.destroy()
    
    def save_branch_data():
        """Save the flow rate and length for each branch in app_state."""
        app_state.flowrate_entries = []  # Reset stored values
        app_state.length_entries = []

        for i in range(app_state.duct_number.get()):
            try:
                flowrate = float(flowrate_entries[i].get())
                length = float(length_entries[i].get())
                app_state.flowrate_entries.append(flowrate)
                app_state.length_entries.append(length)
            except ValueError:
                print(f"Error: Ingrese valores válidos en el Ramal {i+1}")

        print("Caudales guardados:", app_state.flowrate_entries)
        print("Longitudes guardadas:", app_state.length_entries)

    # Function placeholder for the next menu
    def branches_features():
        for widget in W.winfo_children():
            widget.destroy()
        # Aquí va el siguiente menú o pantalla
        Label(W, text="Siguiente pantalla (a definir)", 
            font=('Arial', 20, 'bold'),
            bg='grey12', fg='white').pack(pady=20)

    # Header label
    Label(W, text="Ingrese los valores de caudal y longitud de ramal", 
        font=('Arial', 30, 'bold'),
        bg='grey5', fg='grey80').pack(pady=10)

    selected = app_state.selected_option.get()
    duct_number = app_state.duct_number.get()

    # Frame to hold entry fields
    middle_frame = Frame(W, bg='grey5')
    middle_frame.pack(pady=10)

    # Header Labels depending on selected units
    headers = {
        1: ("Caudal (L/s)", "Longitud (m)"),
        2: ("Caudal (m³/h)", "Longitud (m)"),
        3: ("Caudal (cfm)", "Longitud (ft)")
    }
    
    if selected in headers:
        Label(middle_frame, text=headers[selected][0],
            font=('Arial', 16,'bold'),
            bg='grey5', fg='grey80').grid(row=0, column=1, padx=5, pady=5)
        Label(middle_frame, text=headers[selected][1],
            font=('Arial', 16,'bold'),
            bg='grey5', fg='grey80').grid(row=0, column=2, padx=5, pady=5)

    # Create input fields for each branch
    flowrate_entries = []
    length_entries = []
    placeholder = 'Escribe aquí...'

    for i in range(duct_number):
        if app_state.main_branch.get() == i + 1:
            Label(middle_frame, text=f'Ramal {i+1} (Principal):',
                font=('Arial', 14),
                bg='grey5', fg='OrangeRed2').grid(row=i+1, column=0, padx=3, pady=1)
        else:
            Label(middle_frame, text=f'Ramal {i+1}:', 
                font=('Arial', 14), 
                bg='grey5', fg='grey80').grid(row=i+1, column=0, padx=3, pady=1)

        # Flowrate entry with placeholder
        flowrate_entry = Entry(middle_frame, font=('Arial', 12),
                            width=10, bg='grey40', fg='gray80')
        flowrate_entry.grid(row=i+1, column=1, padx=5, pady=1)
        flowrate_entries.append(flowrate_entry)

        def on_focus_in(event, entry=flowrate_entry):
            if entry.get() == placeholder:
                entry.delete(0, 'end')
                entry.config(fg='black')

        def on_focus_out(event, entry=flowrate_entry):
            if entry.get() == '':
                entry.insert(0, placeholder)
                entry.config(fg='gray')
                
        # Bind focus events
        flowrate_entry.bind('<FocusIn>', on_focus_in)
        flowrate_entry.bind('<FocusOut>', on_focus_out)
        
        # Auto-focus for caret visibility
        flowrate_entry.focus()

        # Length entry
        length_entry = Entry(middle_frame, font=('Arial', 12),
                            width=10, bg='grey40', fg='gray80')
        length_entry.grid(row=i+1, column=2, padx=5, pady=1)
        length_entries.append(length_entry)

    # Bottom buttons
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

    next_btn = Button(bottom_frame, text="Guardar y Continuar", 
                    bg='White', fg='black',
                    relief='raised', 
                    activebackground='DodgerBlue2', 
                    activeforeground='OrangeRed2', 
                    font=('Arial', 20, 'bold'),
                    command=lambda: [save_branch_data(), go_next(W)])
    next_btn.pack(side='right', padx=10, pady=10)


    

