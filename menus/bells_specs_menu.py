from tkinter import Button, Label, Frame, Entry
from app_state import app_state
from tables.smooth_bell import get_co_smooth_bell


def bells_specs_menu(W, go_back):
    # Limpiar ventana
    for widget in W.winfo_children():
        widget.destroy()

    # ============================
    #         TOP FRAME
    # ============================
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

    # ============================
    #        MIDDLE FRAME
    # ============================
    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(expand=True, fill='both')

    # VARIABLES DEL USUARIO (value=1)
    if app_state.selected_bell.get() == 1:   #  <<<<<<<< CORRECCIÓN AQUÍ

        r_label = Label(
            middle_frame, text="Radio de entrada r (m):",
            font=("Arial", 20), bg='gray5', fg='gray90'
        )
        r_label.pack(pady=5)
        
        r_entry = Entry(middle_frame, font=("Arial", 20), justify="center")
        r_entry.pack(pady=5)

        D_label = Label(
            middle_frame, text="Diámetro hidráulico D (m):",
            font=("Arial", 20), bg='gray5', fg='gray90'
        )
        D_label.pack(pady=5)

        D_entry = Entry(middle_frame, font=("Arial", 20), justify="center")
        D_entry.pack(pady=5)

        def save_bell_values():
            try:
                app_state.r_bell = float(r_entry.get())
                app_state.D_bell = float(D_entry.get())

                # Calcular la relación adimensional r/D
                r_over_D = app_state.r_bell / app_state.D_bell

                # Llamar a la función que espera 1 argumento (r/D)
                app_state.Co_bell = get_co_smooth_bell(r_over_D)

                confirm_label.config(
                text=f"C₀ = {app_state.Co_bell:.3f} guardado correctamente",
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

        save_button = Button(
            middle_frame, text="Guardar Valores",
            bg='white', fg='black',
            relief='raised',
            activebackground='DodgerBlue2',
            activeforeground='OrangeRed2',
            font=('Arial', 22, 'bold'),
            command=save_bell_values
        )
        save_button.pack(pady=20)

        confirm_label = Label(
            middle_frame, text="", 
            font=("Arial", 18),
            bg="gray5", fg="lightgreen"
        )
        confirm_label.pack(pady=10)

    # ============================
    #       BOTTOM FRAME
    # ============================
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn = Button(
        bottom_frame, text='Regresar',
        bg='white', fg='black',
        relief='raised',
        activebackground='DodgerBlue2',
        activeforeground='OrangeRed2',
        font=('Arial', 20, 'bold'),
        command=lambda: go_back(W)
    )
    back_btn.pack(side='left', padx=10, pady=10)