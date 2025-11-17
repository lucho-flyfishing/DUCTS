from tkinter import Label, Button, Frame, Entry
from app_state import app_state
import importlib


def bell_specs_menu(W, go_back):

    # --- LIMPIAR VENTANA ---
    for widget in W.winfo_children():
        widget.destroy()

    # --- MAPA ARCHIVOS ---
    BELL_FILE_MAP = {
        1: "smooth_bell",
        2: "smooth_wall_bell",
        3: "conical_bell",
        4: "conical_wall_bell",
        5: "round_exit_bell",
        6: "round_exit_wall_bell",
        7: "rectangular_exit_bell",
        8: "rectangular_exit_wall_bell",
        9: "intake_hood_bell",
        10: "hood_tapered_bell"
    }

    # --- ETIQUETAS DE PARÁMETROS ---
    PARAM_LABELS = {
        "smooth_bell": ["Radio de entrada (r)", "Diámetro hidráulico (d)"],
        "smooth_wall_bell": ["Radio de entrada (r)", "Diámetro hidráulico (d)"],
        "conical_bell": ["Diámetro menor (d1)", "Diámetro mayor (d2)", "Ángulo (°)"],
        "conical_wall_bell": ["Diámetro menor (d1)", "Diámetro mayor (d2)", "Ángulo (°)"],
        "round_exit_bell": ["Radio de salida (r)", "Diámetro (d)"],
        "round_exit_wall_bell": ["Radio de salida (r)", "Diámetro (d)"],
        "rectangular_exit_bell": ["Lado mayor (a)", "Lado menor (b)"],
        "rectangular_exit_wall_bell": ["Lado mayor (a)", "Lado menor (b)"],
        "intake_hood_bell": ["Altura (H)", "Ancho (W)", "Profundidad (L)"],
        "hood_tapered_bell": ["Altura (H)", "Ancho (W)", "Longitud del Taper (L)"]
    }

    selected = app_state.selected_bell.get()
    bell_file = BELL_FILE_MAP.get(selected)

    if bell_file is None:
        return

    # --- FRAMES ---
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')

    Label(
        top_frame,
        text="Introduzca los valores del accesorio",
        font=('Arial', 28),
        bg='gray5',
        fg='gray60'
    ).pack(pady=10)

    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(expand=True)

    # --- PARÁMETROS ---
    entries = []
    for label in PARAM_LABELS[bell_file]:
        lbl = Label(middle_frame, text=label + ":", font=("Arial", 20), bg='gray5', fg='gray90')
        lbl.pack(pady=5)

        entry = Entry(middle_frame, bg='white', fg='gray5',
                    relief='solid', bd=2, highlightthickness=2,
                    highlightbackground='black', font=('Arial', 16))
        entry.pack(pady=5)

        entries.append(entry)

    confirm_label = Label(middle_frame, text="", font=("Arial", 18), bg="gray5")
    confirm_label.pack(pady=10)

    # --- CALCULAR ---
    def calculate_and_save():
        try:
            params = [float(e.get()) for e in entries]

            module = importlib.import_module(f"tables.{bell_file}")
            func = getattr(module, f"get_co_{bell_file}")
            Co_value = func(*params)

            # Guardar accesorio
            if not hasattr(app_state, "fittings"):
                app_state.fittings = []

            app_state.fittings.append({
                "type": bell_file,
                "params": params,
                "Co": Co_value
            })

            confirm_label.config(
                text=f"C₀ = {Co_value:.3f} guardado correctamente",
                fg="lightgreen"
            )

        except ValueError:
            confirm_label.config(
                text="Error: ingrese valores numéricos válidos.",
                fg="red"
            )

    Button(
        middle_frame, text="Guardar Valores",
        bg='white', fg='black',
        relief='raised',
        activebackground='DodgerBlue2',
        activeforeground='OrangeRed2',
        font=('Arial', 22, 'bold'),
        command=calculate_and_save
    ).pack(pady=20)

    # --- NAVEGACIÓN (ESTÁNDAR) ---
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

