from tkinter import Label, Button, Entry, Frame, LEFT, RIGHT, BOTH, X, TOP
import importlib
import inspect
from app_state import app_state



# =========================================================
# MAPA DE ARCHIVOS SEGÚN SELECCIÓN DEL USUARIO
# =========================================================
ELBOW_FILE_MAP = {
    1: "round_smooth_elbow",
    2: "round_mitered_elbow",
    3: "rectangular_mitered_elbow",
    4: "rect_no_vanes_elbow",     # ambos usan la misma función
    5: "rect_no_vanes_elbow",
    6: "z_30_elbow",
    7: "round_3_4_5_pieces_elbow"
}



def elbows_specs_menu(W, go_back):
    # Limpiar ventana
    for widget in W.winfo_children():
        widget.destroy()

    # Obtener tipo de campana seleccionado
    selected_elbow_value = app_state.selected_elbow.get()
    filename = ELBOW_FILE_MAP.get(selected_elbow_value, None)

    if filename is None:
        Label(W, text="Error: Tipo de codo no válido", font=("Arial", 20, "bold")).pack()
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
    top_frame = Frame(W)
    top_frame.pack(side=TOP, fill=X, pady=20)

    Label(
        top_frame,
        text=f"Codo seleccionada: {filename.replace('_',' ').title()}",
        font=("Arial", 24, "bold")
    ).pack()

    Label(
        top_frame,
        text="Ingrese los valores para calcular Co",
        font=("Arial", 18)
    ).pack(pady=10)

    # Frame de parámetros dinámicos
    entries = []
    params_frame = Frame(W)
    params_frame.pack(pady=20)

    # Crear dinámicamente las entradas según la función
    for pname in param_names:
        row = Frame(params_frame)
        row.pack(fill=X, pady=5)

        Label(
            row,
            text=pname.replace("_", "/") + ":",
            font=("Arial", 16)
        ).pack(side=LEFT, padx=10)

        entry = Entry(row, font=("Arial", 16), width=10)
        entry.pack(side=LEFT, padx=10)

        entries.append(entry)

    # -------------------------
    # Entry EXTRA → Nombre del fitting
    # -------------------------
    name_row = Frame(W)
    name_row.pack(fill=X, pady=10)

    Label(
        name_row,
        text="Nombre / etiqueta del accesorio:",
        font=("Arial", 16)
    ).pack(side=LEFT, padx=10)

    name_entry = Entry(name_row, font=("Arial", 16), width=20)
    name_entry.pack(side=LEFT, padx=10)

    # -------------------------
    # Guardar y calcular Co
    # -------------------------
    def save_values_and_compute():
        try:
            # Obtener valores numéricos
            values = [float(e.get()) for e in entries]

            if len(values) != num_params:
                raise ValueError(
                    f"La función requiere {num_params} valores, pero ingresaste {len(values)}"
                )

            # Calcular Co
            Co = calc_func(*values)

            # Obtener nombre
            nombre = name_entry.get().strip()
            if nombre == "":
                nombre = "Sin nombre"

            # Guardar como lista [nombre, Co]
            app_state.fittings.append([nombre, Co])

            # Mostrar Co en pantalla
            Label(
                W,
                text=f"Co calculado = {Co:.4f}",
                font=("Arial", 18, "bold"),
                fg="blue"
            ).pack(pady=10)

            # Imprimir en terminal
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

    # Botón de guardar
    Button(
        W,
        text="Guardar valores",
        bg="DodgerBlue2", fg="white",
        font=("Arial", 18, "bold"),
        command=save_values_and_compute
    ).pack(pady=20)

    # Navegación inferior
    bottom_frame = Frame(W)
    bottom_frame.pack(side=TOP, fill=X, pady=20)

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