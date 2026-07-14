# elbow_specs_menu.py

from tkinter import Label, Button, Entry, Frame, OptionMenu, StringVar, LEFT, RIGHT, BOTH, X, TOP
import importlib
import inspect
from app_state import app_state
from fitting_units import (
    velocity_label, compute_delta_p_pa, format_delta_p, vel_unit, rho_unit,
    dim_unit, compute_Re, hydraulic_diameter_rect,
)


# =========================================================
# MAPA DE ARCHIVOS SEGÚN SELECCIÓN DEL USUARIO
# =========================================================
ELBOW_FILE_MAP = {
    1: "round_smooth_elbow",
    2: "round_mitered_elbow",
    3: "rectangular_mitered_elbow",
    4: "rect_no_vanes_elbow",
    5: "rect_no_vanes_elbow",
    6: "z_30_elbow",
    7: "round_3_4_5_pieces_elbow"
}

# =========================================================
# NOMBRE A MOSTRAR
# Las opciones 4 y 5 comparten el mismo archivo, así que mostramos
# un nombre específico (en vez del nombre de archivo) para que el
# usuario confirme cuál eligió. Coincide con las etiquetas del menú.
# =========================================================
ELBOW_DISPLAY_NAME = {
    4: "Codo sin aletas radio suave",
    5: "Codo sin aletas agudo",
}

# =========================================================
# PARÁMETROS QUE SE MUESTRAN COMO DROPDOWN (OptionMenu)
# en lugar de una caja de texto.
# =========================================================
DROPDOWN_PARAMS = {
    "número_piezas": {
        "options": ["3", "4", "5"],
        "values": {"3": 3, "4": 4, "5": 5},
    },
}

# =========================================================
# PARÁMETROS AUTOMÁTICOS  (NO se le piden al usuario)
# Su valor se deduce de la selección del codo.
#   Opción 4  "radio suave" -> use_Ktheta = True   (Co = Kθ · KRe · C'o)
#   Opción 5  "agudo/sharp"  -> use_Ktheta = False  (Co =      KRe · C'o)
# =========================================================
AUTO_PARAMS = {
    "use_Ktheta": {
        4: True,
        5: False,
    },
}

# =========================================================
# CORRECCIÓN DE REYNOLDS  (KRe)
# Solo algunos codos la usan (leen app_state.Re). Para esos pedimos
# la dimensión física mínima y calculamos Dh y luego Re = ρ·V·Dh/μ,
# aquí mismo (independiente de la parte de ramales/branches).
#
# ¿Cómo saber cuáles agregar? En tu proyecto corre:
#       grep -rl "app_state.Re" tables/
# y pon esos nombres de archivo aquí.
#
# Formas soportadas:
#   "rectangular": pide W (ancho). H sale del ratio H/W ya ingresado.
#                  Dh = 2·H·W / (H + W)   ->  "ratio_param" = nombre del
#                  parámetro H/W en la firma de la función.
#   "round":       pide D (diámetro).  Dh = D
#
# NOTA: verifica los codos redondos/segmentados con el grep de arriba
#       y agrégalos según corresponda.
# =========================================================
REYNOLDS_FITTINGS = {
    "rect_no_vanes_elbow":       {"shape": "rectangular", "ratio_param": "H_W"},
    "rectangular_mitered_elbow": {"shape": "rectangular", "ratio_param": "H_W"},
    "round_mitered_elbow":       {"shape": "round"},   # solo pide D -> Dh = D
    "z_30_elbow":                {"shape": "round"},   # codo en Z redondo -> Dh = D
}


def elbows_specs_menu(W, go_back):
    # Limpiar ventana
    for widget in W.winfo_children():
        widget.destroy()

    # Obtener tipo de codo seleccionado
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

    # Nombre a mostrar (más claro que el nombre de archivo cuando
    # dos selecciones comparten el mismo archivo)
    display_name = ELBOW_DISPLAY_NAME.get(
        selected_elbow_value,
        filename.replace('_', ' ').title()
    )

    # ¿Este codo necesita corrección de Reynolds?
    re_cfg = REYNOLDS_FITTINGS.get(filename)

    # Frame superior
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side=TOP, fill=X, pady=20)

    Label(
        top_frame,
        text=f"Codo seleccionado: {display_name}",
        bg='gray5',
        fg='white',
        font=("Arial", 24, "bold")
    ).pack()

    Label(
        top_frame,
        text="Ingrese los valores para calcular ΔP",
        bg='gray5',
        fg='white',
        font=("Arial", 18)
    ).pack(pady=10)

    # Frame de parámetros dinámicos
    value_getters = []    # una función por parámetro, EN ORDEN de la firma
    numeric_entries = []  # solo para poner el foco en la primera caja
    params_frame = Frame(W, bg='gray5')
    params_frame.pack(pady=20)

    # Entradas dinámicas según firma de la función (para Co)
    for pname in param_names:

        # ---- Parámetro automático: sin casilla, valor según selección ----
        if pname in AUTO_PARAMS:
            mapping = AUTO_PARAMS[pname]
            if selected_elbow_value in mapping:
                auto_value = mapping[selected_elbow_value]
            else:
                default = sig.parameters[pname].default
                auto_value = None if default is inspect.Parameter.empty else default
            value_getters.append(lambda av=auto_value: av)
            continue

        row = Frame(params_frame, bg='gray5')
        row.pack(fill=X, pady=5)

        config = DROPDOWN_PARAMS.get(pname)

        Label(
            row,
            text=pname.replace("_", "/") + ":",
            font=("Arial", 20),
            bg='gray5', fg='OrangeRed2',
        ).pack(side=LEFT, padx=10)

        if config:
            # Parámetro tipo dropdown → OptionMenu
            options = config["options"]
            value_map = config.get("values", {opt: opt for opt in options})

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

            value_getters.append(lambda v=var, vm=value_map: vm[v.get()])
        else:
            # Parámetro numérico → Entry normal
            entry = Entry(
                row,
                font=("Arial", 20),
                width=10,
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

            numeric_entries.append(entry)
            value_getters.append(lambda e=entry: float(e.get()))

    # -------------------------
    # (Solo si aplica) Dimensión física para el número de Reynolds
    # Rectangular -> pide W ; Round -> pide D
    # -------------------------
    dim_entry = None
    if re_cfg is not None:
        dim_row = Frame(params_frame, bg='gray5')
        dim_row.pack(fill=X, pady=5)

        if re_cfg["shape"] == "round":
            dim_label = f"D - diámetro ducto ({dim_unit()}):"
        else:
            dim_label = f"W - ancho ducto ({dim_unit()}):"

        Label(
            dim_row,
            text=dim_label,
            font=("Arial", 20),
            bg='gray5', fg='OrangeRed2',
        ).pack(side=LEFT, padx=10)

        dim_entry = Entry(
            dim_row,
            font=("Arial", 20),
            width=10,
            bg='white', fg='black',
            relief='solid', bd=2,
            highlightthickness=2,
            highlightbackground='white',
            highlightcolor='DeepSkyBlue2',
            insertbackground='black'
        )
        dim_entry.pack(side=LEFT, padx=10)

    # -------------------------
    # Entry → Velocidad
    # -------------------------
    vel_row = Frame(params_frame, bg='gray5')
    vel_row.pack(fill=X, pady=5)

    Label(
        vel_row,
        text=velocity_label(),
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
        bg='gray5',
        fg='OrangeRed2',
        font=("Arial", 20)
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

    # Focus primera caja de texto numérica (los dropdowns no son Entry)
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
            # 1) Valores de los parámetros del codo (orden de la firma)
            values = [get() for get in value_getters]

            # 2) Velocidad
            V = float(vel_entry.get())

            # 3) Si el codo usa KRe, calcular Re AHORA (la función lee
            #    app_state.Re). Independiente de la parte de ramales.
            Re_value = None
            if re_cfg is not None:
                if re_cfg["shape"] == "round":
                    Dh = float(dim_entry.get())                 # Dh = D
                else:
                    W_dim = float(dim_entry.get())              # ancho real
                    H_W = values[param_names.index(re_cfg["ratio_param"])]
                    H_dim = H_W * W_dim                         # alto real
                    Dh = hydraulic_diameter_rect(H_dim, W_dim)  # Dh = 2HW/(H+W)

                Re_value = compute_Re(V, Dh)
                app_state.Re = Re_value                          # float en app_state

            # 4) Coeficiente Co
            Co = calc_func(*values)

            # 5) Densidad (solo para mostrar) y ΔP
            rho = app_state.rho
            delta_p = compute_delta_p_pa(Co, V)

            # Etiqueta
            label = name_entry.get().strip()
            if label == "":
                label = "Sin nombre"

            # Tipo de fitting (nombre claro; distingue 4 vs 5)
            fitting_type = display_name

            # Guardar [etiqueta, tipo, ΔP en Pa]
            app_state.fittings.append([label, fitting_type, delta_p])

            # Mostrar resultado (Pa en SI, inH2O en imperial)
            Label(
                result_frame,
                text=format_delta_p(delta_p),
                font=("Arial", 18, "bold"),
                bg='gray5',
                fg='DeepSkyBlue2'
            ).pack(pady=5)

            # Detalle (incluye Re si se calculó)
            detail = f"(Co = {Co:.4f}  |  V = {V} {vel_unit()}  |  ρ = {rho} {rho_unit()}"
            if Re_value is not None:
                detail += f"  |  Re = {Re_value:,.0f}"
            detail += ")"

            Label(
                result_frame,
                text=detail,
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