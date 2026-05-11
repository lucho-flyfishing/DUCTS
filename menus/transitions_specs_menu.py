# transitions_specs_menu.py

from tkinter import Label, Button, Entry, Frame, LEFT, RIGHT, BOTH, X, TOP
import importlib
import inspect
from app_state import app_state


# Mapa del tipo de transición → archivo
TRANSITION_FILE_MAP = {
    1: "round_transition",
    2: "round_transition",  # reductor: misma tabla, primera columna < 1
    3: "round_rectangular_transition",
    4: "round_rectangular_transition",
    5: "rectangular_transition",
    6: "rectangular_pyramidal_transition",
    7: "rectangular_3_side_transition",
}


def transitions_specs_menu(W, go_back):
    # Limpiar ventana
    for widget in W.winfo_children():
        widget.destroy()

    # Obtener tipo de transición seleccionado
    selected_transition_value = app_state.selected_transition.get()
    filename = TRANSITION_FILE_MAP.get(selected_transition_value, None)

    if filename is None:
        Label(W, text="Error: Tipo de transición no válido", font=("Arial", 20, "bold")).pack()
        return

    # Importar módulo dinámico
    module = importlib.import_module(f"tables.{filename}")

    func_name = f"get_co_{filename}"
    calc_func = getattr(module, func_name)

    # Parámetros de la función
    sig = inspect.signature(calc_func)
    param_names = list(sig.parameters.keys())
    num_params = len(param_names)

    # Frame superior
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side=TOP, fill=X, pady=20)

    Label(
        top_frame,
        bg="gray5",
        fg="white",
        text=f"Transición seleccionada: {filename.replace('_', ' ').title()}",
        font=("Arial", 24, "bold")
    ).pack()

    # Nota extra para el reductor (opción 2)
    if selected_transition_value == 2:
        Label(
            top_frame,
            bg="gray5",
            fg="OrangeRed2",
            text="Nota: para un reductor ingrese un valor < 1 en la primera columna de la tabla.",
            font=("Arial", 14, "italic")
        ).pack(pady=4)

    Label(
        top_frame,
        bg="gray5",
        fg="white",
        text="Ingrese los valores para calcular Co",
        font=("Arial", 18)
    ).pack(pady=10)

    # Frame de parámetros dinámicos
    entries = []
    params_frame = Frame(W, bg='gray5')
    params_frame.pack(pady=20)

    for pname in param_names:
        row = Frame(params_frame, bg='gray5')
        row.pack(fill=X, pady=5)

        Label(
            row,
            text=pname.replace("_", "/") + ":",
            font=("Arial", 20),
            bg='gray5', fg='OrangeRed2',
        ).pack(side=LEFT, padx=10)

        entry = Entry(
            row,
            font=("Arial", 20),
            bg='white',
            fg='black',
            relief='solid',
            bd=2,
            highlightthickness=2,
            highlightbackground='white',
            highlightcolor='DeepSkyBlue2',
            insertbackground='black'
        )
        entry.pack(side=LEFT, padx=10)

        entries.append(entry)

    # Force visibility: focus first entry
    if entries:
        W.after(100, lambda: entries[0].focus_set())

    # -------------------------
    # Entry EXTRA → Nombre del fitting
    # -------------------------
    name_row = Frame(W, bg='gray5')
    name_row.pack(fill=X, pady=10)

    Label(
        name_row,
        text="Nombre / etiqueta del accesorio:",
        font=("Arial", 20),
        bg='gray5', fg='OrangeRed2',
    ).pack(padx=10)

    name_entry = Entry(
        name_row,
        bg='white',
        fg='black',
        relief='solid',
        bd=2,
        highlightthickness=2,
        highlightbackground='white',
        highlightcolor='DeepSkyBlue2',
        insertbackground='black',
        font=("Arial", 20),
        width=20
    )
    name_entry.pack(padx=10)

    # -------------------------
    # Guardar y calcular Co
    # -------------------------
    def save_values_and_compute():
        try:
            values = [float(e.get()) for e in entries]

            if len(values) != num_params:
                raise ValueError(
                    f"La función requiere {num_params} valores, pero ingresaste {len(values)}"
                )

            Co = calc_func(*values)

            nombre = name_entry.get().strip()
            if nombre == "":
                nombre = "Sin nombre"

            app_state.fittings.append([nombre, Co])

            Label(
                W,
                text=f"Co calculado = {Co:.4f}",
                font=("Arial", 18, "bold"),
                fg="blue"
            ).pack(pady=10)

            print("\nLista actual de fittings (nombre, Co):")
            for item in app_state.fittings:
                print(item)

        except Exception as e:
            Label(
                W,
                text=f"Error: {e}",
                font=("Arial", 16),
                fg="red"
            ).pack(pady=10)

    Button(
        W,
        text="Guardar valores",
        bg='White', fg='black',
        relief='raised',
        activebackground='DodgerBlue2',
        activeforeground='OrangeRed2',
        highlightbackground='OrangeRed2',
        font=('Arial', 20, 'bold'),
        command=save_values_and_compute
    ).pack(pady=20)

    # Navegación inferior
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill=X, pady=20)

    back_btn = Button(
        bottom_frame,
        text="Regresar",
        bg="white", fg="black",
        relief="raised",
        activebackground="DodgerBlue2",
        activeforeground="OrangeRed2",
        font=("Arial", 20, "bold"),
        command=lambda: go_back(W)
    )
    back_btn.pack(side=LEFT, padx=10, pady=10)