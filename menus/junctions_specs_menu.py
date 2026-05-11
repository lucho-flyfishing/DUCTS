# junctions_specs_menu.py

from tkinter import Label, Button, Entry, Frame, LEFT, RIGHT, BOTH, X, TOP
import importlib
import inspect
from app_state import app_state


# Mapa del tipo de unión → archivo
JUNCTIONS_FILE_MAP = {
    1:  "30_wye",
    2:  "45_wye",
    3:  "round_tee",
    4:  "30_conical_wye",
    5:  "45_conical_wye",
    6:  "rectangular_tee",
    7:  "round_tap_rectangular_main_tee",
    8:  "rectangular_main_and_tap_tee",
    9:  "rectangular_and_round_wye_d",
    10: "rectangular_main_and_tap_tee_d",
    11: "rectangular_tee_d",
}


def junctions_specs_menu(W, go_back):
    # Limpiar ventana
    for widget in W.winfo_children():
        widget.destroy()

    # Obtener tipo de unión seleccionado
    selected_junction_value = app_state.selected_junction.get()
    filename = JUNCTIONS_FILE_MAP.get(selected_junction_value, None)

    if filename is None:
        Label(W, text="Error: Tipo de unión no válido", font=("Arial", 20, "bold")).pack()
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
        text=f"Unión seleccionada: {filename.replace('_', ' ').title()}",
        font=("Arial", 24, "bold")
    ).pack()

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
    # Entry EXTRA → Número de ramal del accesorio
    # -------------------------
    duct_row = Frame(W, bg='gray5')
    duct_row.pack(fill=X, pady=10)

    Label(
        duct_row,
        text="Número de ramal al que pertenece el accesorio:",
        font=("Arial", 20),
        bg='gray5', fg='OrangeRed2',
    ).pack(padx=10)

    duct_number_entry = Entry(
        duct_row,
        bg='white',
        fg='black',
        relief='solid',
        bd=2,
        highlightthickness=2,
        highlightbackground='white',
        highlightcolor='DeepSkyBlue2',
        insertbackground='black',
        font=("Arial", 20),
        width=10
    )
    duct_number_entry.pack(padx=10)


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

            # Get duct number
            duct_num_str = duct_number_entry.get().strip()
            duct_num = int(duct_num_str) if duct_num_str else None

            # Save as [nombre, Co, duct_number]
            app_state.fittings.append([nombre, Co, duct_num])

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