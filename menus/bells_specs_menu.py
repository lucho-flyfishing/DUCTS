# bell_specs_menu.py

from tkinter import Label, Button, Entry, Frame, LEFT, RIGHT, BOTH, X, TOP
import importlib
import inspect
from app_state import app_state


# Mapas del tipo de campana a su archivo correspondiente
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


def bells_specs_menu(W, go_back):
    # Limpia la ventana
    for widget in W.winfo_children():
        widget.destroy()

        selected_bell_value = app_state.selected_bell.get()

        filename = BELL_FILE_MAP.get(selected_bell_value, None)
    if filename is None:
        Label(W, text="Error: Tipo de campana no válido", font=("Arial", 20, "bold")).pack()
        return

    # Cargar módulo dinámico
    module = importlib.import_module(f"tables.{filename}")

    # Obtener la función get_co_xxx
    func_name = f"get_co_{filename}"
    calc_func = getattr(module, func_name)

    # Identificar cuantos parámetros requiere la función
    sig = inspect.signature(calc_func)
    param_names = list(sig.parameters.keys())
    num_params = len(param_names)

    # Crear frame superior
    top_frame = Frame(W)
    top_frame.pack(side=TOP, fill=X, pady=20)

    Label(top_frame, text=f"Campana seleccionada: {filename.replace('_',' ').title()}",
        font=("Arial", 24, "bold")).pack()

    Label(top_frame, text="Ingrese los valores para calcular Co",
        font=("Arial", 18)).pack(pady=10)

    # Contenedor para parámetros dinámicos
    entries = []
    params_frame = Frame(W)
    params_frame.pack(pady=20)

    # Crear un entry para cada parámetro requerido por la función
    for pname in param_names:
        row = Frame(params_frame)
        row.pack(fill=X, pady=5)

        Label(row, text=pname.replace("_", " ").title() + ":", 
            font=("Arial", 16)).pack(side=LEFT, padx=10)

        entry = Entry(row, font=("Arial", 16), width=10)
        entry.pack(side=LEFT, padx=10)

        entries.append(entry)

    # Función para guardar valores y calcular Co
    def save_values_and_compute():
        try:
            values = [float(e.get()) for e in entries]

            if len(values) != num_params:
                raise ValueError(
                    f"La función requiere {num_params} valores, pero ingresaste {len(values)}"
                )

            Co = calc_func(*values)

            # Guardar resultado en lista global
            app_state.fittings.append(Co)

            Label(W, text=f"Co calculado = {Co:.4f}",
                font=("Arial", 18, "bold"), fg="blue").pack(pady=10)

        except Exception as e:
            Label(W, text=f"Error: {e}", 
                font=("Arial", 16), fg="red").pack(pady=10)

    # Botón para guardar valores
    Button(W, text="Guardar valores",
        bg="DodgerBlue2", fg="white",
        font=("Arial", 18, "bold"),
        command=save_values_and_compute).pack(pady=20)

    # Frame inferior para navegación
    bottom_frame = Frame(W)
    bottom_frame.pack(side=TOP, fill=X, pady=20)

    # Botón Regresar
    back_btn = Button(bottom_frame, text="Regresar",
                    bg="white", fg="black",
                    relief="raised",
                    activebackground="DodgerBlue2",
                    activeforeground="OrangeRed2",
                    font=("Arial", 20, "bold"),
                    command=lambda: go_back(W))
    back_btn.pack(side=LEFT, padx=10, pady=10)

