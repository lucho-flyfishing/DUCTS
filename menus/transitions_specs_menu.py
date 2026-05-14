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
        text="Ingrese los valores para calcular ΔP",
        font=("Arial", 18)
    ).pack(pady=10)

    # Frame de parámetros dinámicos
    entries = []
    params_frame = Frame(W, bg='gray5')
    params_frame.pack(pady=20)

    # Entradas dinámicas según firma de la función (para Co)
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

    # -------------------------
    # Entry → Velocidad
    # -------------------------
    vel_row = Frame(params_frame, bg='gray5')
    vel_row.pack(fill=X, pady=5)

    Label(
        vel_row,
        text="V (m/s):",
        font=("Arial", 20),
        bg='gray5', fg='OrangeRed2',
    ).pack(side=LEFT, padx=10)

    vel_entry = Entry(
        vel_row,
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
    vel_entry.pack(side=LEFT, padx=10)

    # -------------------------
    # Entry → Etiqueta del accesorio
    # -------------------------
    name_row = Frame(W, bg='gray5')
    name_row.pack(fill=X, pady=10)

    Label(
        name_row,
        text="Etiqueta del accesorio:",
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

    # Focus primer entry
    if entries:
        W.after(100, lambda: entries[0].focus_set())

    # -------------------------
    # Calcular y guardar
    # -------------------------
    def save_values_and_compute():
        # Limpiar resultados anteriores
        for widget in result_frame.winfo_children():
            widget.destroy()

        try:
            # Valores para Co
            values = [float(e.get()) for e in entries]

            if len(values) != num_params:
                raise ValueError(
                    f"La función requiere {num_params} valores, pero ingresaste {len(values)}"
                )

            # Calcular Co
            Co = calc_func(*values)

            # Velocidad
            V = float(vel_entry.get())

            # Densidad desde app_state
            rho = app_state.rho

            # Calcular ΔP
            delta_p = Co * rho * (V ** 2) / 2

            # Etiqueta
            label = name_entry.get().strip()
            if label == "":
                label = "Sin nombre"

            # Tipo de fitting
            fitting_type = filename.replace('_', ' ').title()

            # Guardar [etiqueta, tipo, ΔP]
            app_state.fittings.append([label, fitting_type, delta_p])

            # Mostrar resultado
            Label(
                result_frame,
                text=f"ΔP = {delta_p:.4f} Pa",
                font=("Arial", 18, "bold"),
                bg='gray5',
                fg='DeepSkyBlue2'
            ).pack(pady=5)

            Label(
                result_frame,
                text=f"(Co = {Co:.4f}  |  V = {V} m/s  |  ρ = {rho} kg/m³)",
                font=("Arial", 14),
                bg='gray5',
                fg='gray60'
            ).pack()

            # Imprimir en terminal
            print("\nLista actual de fittings:")
            for item in app_state.fittings:
                print(item)

        except Exception as e:
            Label(
                result_frame,
                text=f"Error: {e}",
                font=("Arial", 16),
                bg='gray5',
                fg='red'
            ).pack(pady=10)

    # Botón guardar
    Button(
        W,
        text="Guardar y calcular ΔP",
        bg='White', fg='black',
        relief='raised',
        activebackground='DodgerBlue2',
        activeforeground='OrangeRed2',
        highlightbackground='OrangeRed2',
        font=('Arial', 20, 'bold'),
        command=save_values_and_compute
    ).pack(pady=20)

    # Frame para mostrar resultado (se limpia en cada cálculo)
    result_frame = Frame(W, bg='gray5')
    result_frame.pack(pady=10)

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