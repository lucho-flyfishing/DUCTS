# bell_specs_menu.py

from tkinter import Label, Button, Entry, Frame, OptionMenu, StringVar, LEFT, RIGHT, BOTH, X, TOP
import importlib
import inspect
from app_state import app_state


# Mapa del tipo de campana → archivo
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
    10: "hood_tapered_bell",
}

# Params that are strings → rendered as dropdowns instead of text entries
DROPDOWN_PARAMS = {
    "forma": ["round", "rect"],
}


def bells_specs_menu(W, go_back):
    # Limpiar ventana
    for widget in W.winfo_children():
        widget.destroy()

    # Obtener tipo de campana seleccionado
    selected_bell_value = app_state.selected_bell.get()
    filename = BELL_FILE_MAP.get(selected_bell_value, None)

    if filename is None:
        Label(W, text="Error: Tipo de campana no válido", font=("Arial", 20, "bold")).pack()
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
        text=f"Campana seleccionada: {filename.replace('_', ' ').title()}",
        font=("Arial", 24, "bold")
    ).pack()

    Label(
        top_frame,
        bg="gray5",
        fg="white",
        text="Ingrese los valores para calcular ΔP",
        font=("Arial", 18)
    ).pack(pady=10)

    # Frame de parámetros dinámicos
    entries = []
    param_types = []   # "numeric" or "string" — tells save_values_and_compute how to parse
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

        if pname in DROPDOWN_PARAMS:
            # String param → OptionMenu, no typing needed
            options = DROPDOWN_PARAMS[pname]
            var = StringVar(W)
            var.set(options[0])
            menu = OptionMenu(row, var, *options)
            menu.config(
                font=("Arial", 18),
                bg='white', fg='black',
                activebackground='DeepSkyBlue2',
                activeforeground='white',
                relief='solid',
                bd=2,
                width=10
            )
            menu["menu"].config(font=("Arial", 16), bg='white', fg='black')
            menu.pack(side=LEFT, padx=10)
            entries.append(var)
            param_types.append("string")
        else:
            # Numeric param → regular Entry
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
            param_types.append("numeric")

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

    # Focus first numeric entry
    numeric_entries = [e for e, t in zip(entries, param_types) if t == "numeric"]
    if numeric_entries:
        W.after(100, lambda: numeric_entries[0].focus_set())

    # -------------------------
    # Calcular y guardar
    # -------------------------
    def save_values_and_compute():
        # Limpiar resultados anteriores
        for widget in result_frame.winfo_children():
            widget.destroy()

        try:
            # Parse each param according to its type
            values = []
            for e, t in zip(entries, param_types):
                if t == "string":
                    values.append(e.get())          # string as-is
                else:
                    values.append(float(e.get()))   # numeric

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