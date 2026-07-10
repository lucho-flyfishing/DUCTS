# junctions_specs_menu.py

from tkinter import Label, Button, Entry, Frame, OptionMenu, StringVar, LEFT, X, TOP
import importlib
import inspect
from app_state import app_state
from fitting_units import velocity_label, compute_delta_p_pa, format_delta_p, vel_unit, rho_unit


# =========================================================
# MAPA DE ARCHIVOS SEGÚN SELECCIÓN DEL USUARIO
# =========================================================
JUNCTION_FILE_MAP = {
    1: "30_wye",
    2: "45_wye",
    3: "round_tee",
    4: "30_conical_wye",
    5: "45_conical_wye",
    6: "rectangular_tee",
    7: "round_tap_rectangular_main_tee",
    8: "rectangular_main_and_tap_tee",
    9: "rectangular_and_round_wye_2",
    10: "rectangular_dovetail_wye",
}

# String params → rendered as dropdowns instead of text entries
DROPDOWN_PARAMS = {
    # Add any string params here if needed in the future
}


def junctions_specs_menu(W, go_back):
    # Limpiar ventana
    for widget in W.winfo_children():
        widget.destroy()

    # Obtener tipo de unión seleccionado
    selected_junction_value = app_state.selected_junction.get()
    filename = JUNCTION_FILE_MAP.get(selected_junction_value, None)

    if filename is None:
        Label(W, text="Error: Tipo de unión no válido", font=("Arial", 20, "bold")).pack()
        return

    # Importar módulo dinámico
    module = importlib.import_module(f"tables.{filename}")

    # Verificar qué funciones existen en el módulo
    has_branch = hasattr(module, f"get_co_{filename}_branch")
    has_main   = hasattr(module, f"get_co_{filename}_main")

    if not has_branch and not has_main:
        Label(W, text=f"Error: No se encontraron funciones para {filename}",
              font=("Arial", 18), fg='red').pack(pady=20)
        return

    branch_func   = getattr(module, f"get_co_{filename}_branch") if has_branch else None
    main_func     = getattr(module, f"get_co_{filename}_main")   if has_main   else None

    # Parámetros de cada función disponible
    branch_params = list(inspect.signature(branch_func).parameters.keys()) if has_branch else []
    main_params   = list(inspect.signature(main_func).parameters.keys())   if has_main   else []

    # Unión de parámetros — sin duplicados, orden preservado
    all_params = list(dict.fromkeys(branch_params + main_params))

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
        text="Ingrese los valores para calcular ΔP",
        font=("Arial", 18)
    ).pack(pady=10)

    # -------------------------
    # Entradas dinámicas (unión de params)
    # -------------------------
    entries     = {}   # param_name → widget
    param_types = {}   # param_name → "numeric" | "string"

    params_frame = Frame(W, bg='gray5')
    params_frame.pack(pady=10)

    for pname in all_params:
        row = Frame(params_frame, bg='gray5')
        row.pack(fill=X, pady=5)

        Label(
            row,
            text=pname.replace("_", "/") + ":",
            font=("Arial", 20),
            bg='gray5', fg='OrangeRed2',
        ).pack(side=LEFT, padx=10)

        if pname in DROPDOWN_PARAMS:
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
            entries[pname]     = var
            param_types[pname] = "string"
        else:
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
            entries[pname]     = entry
            param_types[pname] = "numeric"

    # -------------------------
    # Velocidades (solo las necesarias)
    # -------------------------
    vel_frame = Frame(W, bg='gray5')
    vel_frame.pack(pady=5)

    vb_entry = vs_entry = None

    if has_branch:
        vb_row = Frame(vel_frame, bg='gray5')
        vb_row.pack(fill=X, pady=5)
        Label(vb_row, text=velocity_label("V_b", "Velocidad ramal"),
              font=("Arial", 20), bg='gray5', fg='OrangeRed2').pack(side=LEFT, padx=10)
        vb_entry = Entry(vb_row, font=("Arial", 20), bg='white', fg='black',
                         relief='solid', bd=2, highlightthickness=2,
                         highlightbackground='white', highlightcolor='DeepSkyBlue2',
                         insertbackground='black')
        vb_entry.pack(side=LEFT, padx=10)

    if has_main:
        vs_row = Frame(vel_frame, bg='gray5')
        vs_row.pack(fill=X, pady=5)
        Label(vs_row, text=velocity_label("V_s", "Velocidad principal"),
              font=("Arial", 20), bg='gray5', fg='OrangeRed2').pack(side=LEFT, padx=10)
        vs_entry = Entry(vs_row, font=("Arial", 20), bg='white', fg='black',
                         relief='solid', bd=2, highlightthickness=2,
                         highlightbackground='white', highlightcolor='DeepSkyBlue2',
                         insertbackground='black')
        vs_entry.pack(side=LEFT, padx=10)

    # -------------------------
    # Etiquetas (solo las necesarias)
    # -------------------------
    labels_frame = Frame(W, bg='gray5')
    labels_frame.pack(pady=5)

    branch_label_entry = main_label_entry = None

    if has_branch:
        branch_label_row = Frame(labels_frame, bg='gray5')
        branch_label_row.pack(fill=X, pady=5)
        Label(branch_label_row, text="Etiqueta ramal:",
              font=("Arial", 20), bg='gray5', fg='OrangeRed2').pack(side=LEFT, padx=10)
        branch_label_entry = Entry(branch_label_row, font=("Arial", 20), bg='white', fg='black',
                                   relief='solid', bd=2, highlightthickness=2,
                                   highlightbackground='white', highlightcolor='DeepSkyBlue2',
                                   insertbackground='black', width=20)
        branch_label_entry.pack(side=LEFT, padx=10)

    if has_main:
        main_label_row = Frame(labels_frame, bg='gray5')
        main_label_row.pack(fill=X, pady=5)
        Label(main_label_row, text="Etiqueta principal:",
              font=("Arial", 20), bg='gray5', fg='OrangeRed2').pack(side=LEFT, padx=10)
        main_label_entry = Entry(main_label_row, font=("Arial", 20), bg='white', fg='black',
                                 relief='solid', bd=2, highlightthickness=2,
                                 highlightbackground='white', highlightcolor='DeepSkyBlue2',
                                 insertbackground='black', width=20)
        main_label_entry.pack(side=LEFT, padx=10)

    # Focus primer entry numérico
    numeric_entries = [entries[p] for p in all_params if param_types[p] == "numeric"]
    if numeric_entries:
        W.after(100, lambda: numeric_entries[0].focus_set())

    # -------------------------
    # Calcular y guardar
    # -------------------------
    def save_values_and_compute():
        for widget in result_frame.winfo_children():
            widget.destroy()

        try:
            # Construir dict de valores
            value_dict = {}
            for pname in all_params:
                if param_types[pname] == "string":
                    value_dict[pname] = entries[pname].get()
                else:
                    value_dict[pname] = float(entries[pname].get())

            rho          = app_state.rho
            fitting_type = filename.replace('_', ' ').title()

            if has_branch:
                branch_args    = [value_dict[p] for p in branch_params]
                Co_branch      = branch_func(*branch_args)
                V_b            = float(vb_entry.get())
                delta_p_branch = compute_delta_p_pa(Co_branch, V_b)   # Pa
                label_b        = branch_label_entry.get().strip() or "Sin nombre (ramal)"
                app_state.fittings.append([label_b, fitting_type + " (ramal)", delta_p_branch])

                Label(result_frame,
                      text=format_delta_p(delta_p_branch, "ΔP ramal"),
                      font=("Arial", 18, "bold"), bg='gray5', fg='DeepSkyBlue2').pack(pady=3)
                Label(result_frame,
                      text=f"(Co = {Co_branch:.4f}  |  V_b = {V_b} {vel_unit()}  |  ρ = {rho} {rho_unit()})",
                      font=("Arial", 14), bg='gray5', fg='gray60').pack()

            if has_main:
                main_args    = [value_dict[p] for p in main_params]
                Co_main      = main_func(*main_args)
                V_s          = float(vs_entry.get())
                delta_p_main = compute_delta_p_pa(Co_main, V_s)       # Pa
                label_s      = main_label_entry.get().strip() or "Sin nombre (principal)"
                app_state.fittings.append([label_s, fitting_type + " (principal)", delta_p_main])

                Label(result_frame,
                      text=format_delta_p(delta_p_main, "ΔP principal"),
                      font=("Arial", 18, "bold"), bg='gray5', fg='DeepSkyBlue2').pack(pady=3)
                Label(result_frame,
                      text=f"(Co = {Co_main:.4f}  |  V_s = {V_s} {vel_unit()}  |  ρ = {rho} {rho_unit()})",
                      font=("Arial", 14), bg='gray5', fg='gray60').pack()

            # Terminal
            print("\nLista actual de fittings:")
            for item in app_state.fittings:
                print(item)

        except Exception as e:
            Label(result_frame, text=f"Error: {e}",
                  font=("Arial", 16), bg='gray5', fg='red').pack(pady=10)

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

    # Frame resultado
    result_frame = Frame(W, bg='gray5')
    result_frame.pack(pady=10)

    # Navegación inferior
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill=X, pady=20)

    Button(
        bottom_frame,
        text="Regresar",
        bg="white", fg="black",
        relief="raised",
        activebackground="DodgerBlue2",
        activeforeground="OrangeRed2",
        font=("Arial", 20, "bold"),
        command=lambda: go_back(W)
    ).pack(side=LEFT, padx=10, pady=10)