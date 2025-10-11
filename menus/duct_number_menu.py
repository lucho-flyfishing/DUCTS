from tkinter import Button, Label, Entry, Frame
from app_state import app_state

def duct_number_menu(W, go_back, go_next):
        # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
    
    #top frame for the menu title
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    # Title for the duct information menu
    duct_info_tittle = Label(top_frame, text='Complete la información sobre los ramales '
                            'del sistema, luego presione " Siguiente".', 
                            font=('Arial', 30, 'bold'), bg='gray5', fg='gray60')
    duct_info_tittle.pack(pady=10)
    
    # Entry for branch number and main branch
    # Middle frame to hold entry fields
    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(expand=True)

    duct_number_lbl = Label(middle_frame, text='Número de ramales del ducto. ',
                            font=('Arial', 26), bg='gray5', fg='OrangeRed2')
    duct_number_lbl.pack(pady=1)

    duct_number_entry = Entry(middle_frame, font=('Arial', 15),
                            bg='white', fg='gray5', 
                            relief='solid', bd=2, 
                            highlightthickness=2,
                            highlightbackground='black')
    duct_number_entry.pack(pady=20, ipady=5, ipadx=10)

    main_branch_lbl = Label(middle_frame, text='Número de ramal que va a usar como ducto principal:',
                            font=('Arial', 26), bg='gray5', fg='OrangeRed2')
    main_branch_lbl.pack(pady=5)

    main_branch_entry = Entry(middle_frame, font=('Arial', 15),
                            bg='white', fg='gray5',
                            relief='solid', bd=2,
                            highlightthickness=2, 
                            highlightbackground='black')
    main_branch_entry.pack(pady=20, ipady=5, ipadx=10)

    # Placeholder text for duct number
    duct_number_placeholder = 'Escribe aquí...'
    duct_number_entry.insert(0, duct_number_placeholder)

    # Functions to handle placeholder behavior
    def on_focus_in(event):
        if duct_number_entry.get() == duct_number_placeholder:
            duct_number_entry.delete(0, 'end')
            duct_number_entry.config(fg='black')

    def on_focus_out(event):
        if duct_number_entry.get() == '':
            duct_number_entry.insert(0, duct_number_placeholder)
            duct_number_entry.config(fg='gray')

    # Bind focus events
    duct_number_entry.bind('<FocusIn>', on_focus_in)
    duct_number_entry.bind('<FocusOut>', on_focus_out)

    # Auto-focus for caret visibility
    duct_number_entry.focus()

    # Function to save duct number using app_state
    def save_duct_number():
        value = duct_number_entry.get()  # Get the user input

        if value == duct_number_placeholder:
            app_state.duct_number.set(0)  # Avoid saving placeholder
        else:
            try:
                app_state.duct_number.set(int(value))  # Convert and store in app_state
            except ValueError:
                print("Error: Ingrese un número válido")  # Handle invalid input

        print(f'El número de ductos es: {app_state.duct_number.get()}')  # Verify it's working
    
    #funcion to save the main branch number
    def save_main_branch():
        value = main_branch_entry.get()
        if value == 'Escribe aquí...':
            app_state.main_branch.set(0)
        else:
            try:
                app_state.main_branch.set(int(value))
            except ValueError:
                print("Error: Ingrese un número válido")
        print(f'El ducto principal es el número: {app_state.main_branch.get()}')  # Verify it's working
    # Button to save the duct number and main branch
        
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn = Button(bottom_frame, text='Volver',
                    bg='White', fg='black',
                    relief='raised', 
                    activebackground='DodgerBlue2', 
                    activeforeground='OrangeRed2', 
                    font=('Arial', 20, 'bold'), 
                    command = lambda: go_back(W))
    back_btn.pack (side='left', padx=10, pady=10)

    next_btn = Button(bottom_frame, text='Siguiente',
                    bg='White', fg='black', 
                    relief='raised', 
                    activebackground='DodgerBlue2', 
                    activeforeground='OrangeRed2',  
                    font=('Arial', 20, 'bold'), 
                    command=lambda: [save_duct_number(), save_main_branch(), go_next(W)])
    next_btn.pack(side='right' , padx= 10, pady=10)
    
