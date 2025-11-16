from tkinter import Button, Label, Frame, Entry
from app_state import app_state
from tables.smooth_bell import get_co_smooth_bell


def bells_specs_menu(W, go_back):
    
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    main_label = Label(
        top_frame,
        text='Introduzca los valores de la campana',
        font=('Arial', 30),
        bg='gray5',
        fg='gray60'
    )
    main_label.pack(side='top', pady=1)
    
    
    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(expand=True, fill='both')
    
    
    if app_state.selected_bell.get() == 1: 
        
        
        r_label = Label(
            middle_frame, text="Radio de entrada r (m):",
            font=("Arial", 20), bg='gray5', fg='gray90'
        )
        r_label.pack(pady=5)
        
        r_entry = Entry(
            middle_frame,
            bg='white', fg='gray5',
            relief='solid', bd=2,
            highlightthickness=2,
            highlightbackground='black',
            font=('Arial', 15)
        )
        r_entry.pack(pady=5)

        D_label = Label(
            middle_frame, text="Diámetro hidráulico D (m):",
            font=("Arial", 20), bg='gray5', fg='gray90'
        )
        D_label.pack(pady=5)

        D_entry = Entry(
            middle_frame,                             
            bg='white', fg='gray5',
            relief='solid', bd=2,
            highlightthickness=2,
            highlightbackground='black',
            font=('Arial', 15)
        )
        D_entry.pack(pady=5)
        
        
        fit_code_label = Label(
            middle_frame, text="Elija un nombre o código para el accesorio:",
            font=("Arial", 20), bg='gray5', fg='gray90'
        )
        fit_code_label.pack(pady=5)
        
        
        fit_code_entry = Entry(
            middle_frame,                             
            bg='white', fg='gray5',
            relief='solid', bd=2,
            highlightthickness=2,
            highlightbackground='black',
            font=('Arial', 15)
        )
        fit_code_entry.pack(pady=5)
        
        
        def save_bell_values():
            try:
                app_state.r_bell = float(r_entry.get())
                app_state.D_bell = float(D_entry.get())
                
                r_over_D = app_state.r_bell / app_state.D_bell
                
                app_state.Co_bell = get_co_smooth_bell(r_over_D)
                
                confirm_label.config(
                    text=f"C₀ = {app_state.Co_bell:.3f} calculado correctamente",
                    fg="lightgreen"
                )

            except ZeroDivisionError:
                confirm_label.config(
                    text="Error: D no puede ser 0.",
                    fg="red"
                )
            except ValueError:
                confirm_label.config(
                    text="Error: introduzca valores numéricos válidos.",
                    fg="red"
                )


        
        def save_fitting():
            code = fit_code_entry.get().strip()

            if code == "":
                confirm_label.config(
                    text="Debe ingresar un nombre/código para guardar el accesorio.",
                    fg="red"
                )
                return

            
            app_state.fittings.append({
                "type": "smooth_bell",
                "code": code,
                "r": app_state.r_bell,
                "D": app_state.D_bell,
                "r_over_D": app_state.r_bell / app_state.D_bell,
                "Co": app_state.Co_bell
            })

            confirm_label.config(
                text=f"Accesorio '{code}' guardado en app_state.fittings",
                fg="lightblue"
            )


        
        save_button = Button(
            middle_frame,
            text="Guardar Valores",
            bg='white', fg='black',
            relief='raised',
            activebackground='DodgerBlue2',
            activeforeground='OrangeRed2',
            font=('Arial', 22, 'bold'),
            command=lambda: (save_bell_values(), save_fitting())
        )
        save_button.pack(pady=20)


        confirm_label = Label(
            middle_frame,
            text="", 
            font=("Arial", 18),
            bg="gray5",
            fg="lightgreen"
        )
        confirm_label.pack(pady=10)
        
        
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
    
    
    back_btn = Button(
        bottom_frame,
        text='Regresar',
        bg='white', fg='black',
        relief='raised',
        activebackground='DodgerBlue2',
        activeforeground='OrangeRed2',
        font=('Arial', 20, 'bold'),
        command=lambda: go_back(W)
    )
    back_btn.pack(side='left', padx=10, pady=10)