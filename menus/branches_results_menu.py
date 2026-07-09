from tkinter import Button, Label, Frame, StringVar, Canvas, Scrollbar
from app_state import app_state
import math


def solve_diameter_equal_friction(Q, S, rho, viscosity, epsilon):
    """
    Iterative solver for duct diameter using equal friction method.
    Given flowrate Q (m³/s), target friction rate S (Pa/m),
    air density rho (kg/m³), dynamic viscosity (Pa·s), roughness epsilon (m).
    Returns diameter in meters.
    """
    # Initial guess from simplified formula (ignore friction factor, assume f~0.015)
    f_guess = 0.02
    D = ((8 * f_guess * rho * Q**2) / (math.pi**2 * S)) ** (1/5)

    for _ in range(50):  # iterate until convergence
        V = (4 * Q) / (math.pi * D**2)
        Re = (rho * V * D) / viscosity
        if Re < 1:
            break
        f = 0.25 / (math.log10((epsilon / (3.7 * D)) + (5.74 / Re**0.9)))**2
        D_new = ((8 * f * rho * Q**2) / (math.pi**2 * S)) ** (1/5)
        if abs(D_new - D) < 1e-9:
            break
        D = D_new

    return D


def solve_diameter_equal_friction_ip(Q_ft3s, S_inwg_ft, density_ip, viscosity_ip, epsilon_ft):
    """
    Iterative solver for duct diameter — imperial units.
    Q_ft3s: ft³/s, S_inwg_ft: inH₂O/ft, density_ip: lb/ft³,
    viscosity_ip: lb/(ft·s), epsilon_ft: ft.
    Returns diameter in feet.
    """
    S_lbft2_ft = S_inwg_ft * 5.202  # convert inH₂O/ft → lb/ft² per ft
    # BUG 2 FIX: en unidades US la ec. de Darcy y Reynolds requieren la densidad en
    # slug/ft³ (la viscosidad ya viene en base slug). density_ip llega en lb-masa/ft³.
    density_slug = density_ip / 32.174  # lb-masa/ft³ → slug/ft³

    f_guess = 0.02
    D = ((8 * f_guess * density_slug * Q_ft3s**2) / (math.pi**2 * S_lbft2_ft)) ** (1/5)

    for _ in range(50):
        V = (4 * Q_ft3s) / (math.pi * D**2)
        Re = (density_slug * V * D) / viscosity_ip
        if Re < 1:
            break
        f = 0.25 / (math.log10((epsilon_ft / (3.7 * D)) + (5.74 / Re**0.9)))**2
        D_new = ((8 * f * density_slug * Q_ft3s**2) / (math.pi**2 * S_lbft2_ft)) ** (1/5)
        if abs(D_new - D) < 1e-9:
            break
        D = D_new

    return D


def branches_results_menu(W, go_back):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()


    selected       = app_state.selected_option.get()
    flowrate_values = app_state.flowrate_entries
    length_values   = app_state.length_entries
    density        = float(app_state.rho)
    viscosity      = float(app_state.viscosity)
    main_branch    = app_state.main_branch.get()

    # S from the main branch (set in pre_dim_menu) — design friction rate for all branches
    S_main = float(app_state.S)

    # La rugosidad ya se coacciona a float/None en pre_dim_menu, pero si esta pantalla
    # se alcanza sin pasar por alli, epsilon podria seguir siendo un StringVar. Se
    # normaliza aqui para que los defaults por unidad de abajo funcionen sin error.
    if isinstance(app_state.epsilon, StringVar):
        val = app_state.epsilon.get().strip()
        app_state.epsilon = float(val) if val else None

    diameters_values = []
    delta_p_values   = []
    velocity_values  = []


    for i in range(len(flowrate_values)):
        flow_value   = flowrate_values[i]
        length_value = length_values[i]

        if selected == 1:
            Q       = flow_value / 1000          # L/s → m³/s
            # rugosidad: valor del usuario (mm → m) o default 1.5e-4 m (≈0.15 mm).
            # Misma fuente que pre_dim_menu para mantener el mismo material.
            epsilon = 1.5e-4 if app_state.epsilon is None else app_state.epsilon / 1000  # m

            D_m       = solve_diameter_equal_friction(Q, S_main, density, viscosity, epsilon)
            diameters = D_m * 1000               # m → mm
            velocity  = float(app_state.velocity) if (i + 1) == main_branch else (4 * Q) / (math.pi * D_m**2)  # m/s

        elif selected == 2:
            Q       = flow_value                 # already m³/s
            # rugosidad: valor del usuario (mm → m) o default 1.5e-4 m (≈0.15 mm)
            epsilon = 1.5e-4 if app_state.epsilon is None else app_state.epsilon / 1000  # m

            D_m       = solve_diameter_equal_friction(Q, S_main, density, viscosity, epsilon)
            diameters = D_m * 1000               # m → mm
            velocity  = float(app_state.velocity) if (i + 1) == main_branch else (4 * Q) / (math.pi * D_m**2)  # m/s

        elif selected == 3:
            Q_ft3s       = flow_value / 60       # CFM → ft³/s
            # rugosidad: valor del usuario ya en pulgadas, o default 0.0059 in.
            # 0.0059 in ≡ 0.15 mm ≡ 1.5e-4 m: es el MISMO default fisico que en SI,
            # expresado en la unidad que consume el solver imperial (NO usar 1.5e-4
            # aqui: 1.5e-4 in ≈ 0.0038 mm, ~40x mas liso).
            epsilon_in   = 0.0059 if app_state.epsilon is None else app_state.epsilon  # in
            epsilon_ft   = epsilon_in / 12       # in → ft
            density_ip   = density               # lb/ft³
            viscosity_ip = viscosity             # lb/(ft·s)

            D_ft      = solve_diameter_equal_friction_ip(Q_ft3s, S_main, density_ip, viscosity_ip, epsilon_ft)
            diameters = D_ft * 12                # ft → in
            velocity  = float(app_state.velocity) if (i + 1) == main_branch else ((4 * Q_ft3s) / (math.pi * D_ft**2)) * 60  # fpm

        else:
            diameters = None
            velocity  = None

        delta_p = S_main * length_value if diameters is not None else None

        diameters_values.append(diameters)
        delta_p_values.append(delta_p)
        velocity_values.append(velocity)

        print("Diametro calculado para el ramal", i + 1, ":", diameters, "| Velocidad:", velocity)


    app_state.diameters_values = diameters_values
    app_state.delta_p_values   = delta_p_values
    app_state.velocity_values  = velocity_values


    # ── S label ───────────────────────────────────────────────────────────────
    if selected in (1, 2):
        s_text = f'Tasa de fricción de diseño (S): {round(S_main, 4)} Pa/m'
    else:
        s_text = f'Tasa de fricción de diseño (S): {round(S_main, 6)} inH₂O/ft'

    Label(W, text=s_text,
          font=('Arial', 16, 'bold'),
          bg='gray5', fg='gray60'
          ).pack(pady=(15, 2))

    Label(W, text='Todos los ramales se dimensionan con esta misma tasa (método de igual fricción)',
          font=('Arial', 11, 'italic'),
          bg='gray5', fg='gray50'
          ).pack(pady=(0, 10))

    # ── Results table ─────────────────────────────────────────────────────────
    title_lbl = Label(W, text='Resultados del dimensionamiento de ramales',
                      font=('Arial', 22, 'bold'), bg='gray5', fg='OrangeRed2')
    title_lbl.pack(pady=(5, 5))

    table_container = Frame(W, bg='gray5')
    table_container.pack(fill='both', expand=True, pady=5)

    canvas = Canvas(table_container, bg='gray5', highlightthickness=0, bd=0)
    scrollbar = Scrollbar(table_container, orient='vertical', command=canvas.yview,
                          bg='gray30', troughcolor='gray12',
                          activebackground='DodgerBlue2',
                          highlightthickness=0, bd=0, width=14)
    canvas.configure(yscrollcommand=scrollbar.set, yscrollincrement=34)

    canvas.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')

    table_frame = Frame(canvas, bg='gray5')
    canvas.create_window((0, 0), window=table_frame, anchor='nw')

    def _update_scrollregion(event):
        canvas.configure(scrollregion=canvas.bbox('all'))
    table_frame.bind('<Configure>', _update_scrollregion)

    def _on_mousewheel(event):
        if event.num == 4 or event.delta > 0:
            canvas.yview_scroll(-1, 'units')
        elif event.num == 5 or event.delta < 0:
            canvas.yview_scroll(1, 'units')

    def _bind_mousewheel(event):
        canvas.bind_all('<MouseWheel>', _on_mousewheel)
        canvas.bind_all('<Button-4>', _on_mousewheel)
        canvas.bind_all('<Button-5>', _on_mousewheel)

    def _unbind_mousewheel(event):
        canvas.unbind_all('<MouseWheel>')
        canvas.unbind_all('<Button-4>')
        canvas.unbind_all('<Button-5>')

    canvas.bind('<Enter>', _bind_mousewheel)
    canvas.bind('<Leave>', _unbind_mousewheel)

    if selected == 1:
        col_headers = ['Ramal', 'Caudal (L/s)', 'Longitud (m)', 'Velocidad (m/s)', 'ΔP (Pa)', 'Diámetro (mm)']
    elif selected == 2:
        col_headers = ['Ramal', 'Caudal (m³/s)', 'Longitud (m)', 'Velocidad (m/s)', 'ΔP (Pa)', 'Diámetro (mm)']
    else:
        col_headers = ['Ramal', 'Caudal (cfm)', 'Longitud (ft)', 'Velocidad (fpm)', 'ΔP (inH₂O)', 'Diámetro (in)']

    col_widths = [18, 18, 18, 18, 20, 18]

    # Header row
    for col, (header, width) in enumerate(zip(col_headers, col_widths)):
        Label(table_frame, text=header,
              font=('Arial', 12, 'bold'),
              bg='gray15', fg='gray90',
              width=width, anchor='center',
              relief='flat', padx=4, pady=6
              ).grid(row=0, column=col, padx=1, pady=1)

    # Data rows
    for i in range(len(flowrate_values)):
        is_main = (main_branch == i + 1)

        name_fg = 'OrangeRed2' if is_main else 'gray80'
        val_fg  = 'OrangeRed2' if is_main else 'gray70'
        tag     = ' (Principal)' if is_main else ''

        row_data = [
            f'Ramal {i + 1}{tag}',
            f'{flowrate_values[i]:.2f}',
            f'{length_values[i]:.2f}',
            f'{velocity_values[i]:.2f}',
            f'{delta_p_values[i]:.4f}',
            f'{diameters_values[i]:.1f}',
        ]

        for col, (value, width) in enumerate(zip(row_data, col_widths)):
            fg = name_fg if col == 0 else val_fg
            Label(table_frame, text=value,
                  font=('Arial', 12),
                  bg='gray12', fg=fg,
                  width=width, anchor='center',
                  relief='flat', padx=4, pady=5
                  ).grid(row=i + 1, column=col, padx=1, pady=1)

    # ── end results table ─────────────────────────────────────────────────────


    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn = Button(bottom_frame, text='Regresar y modificar valores',
                    bg='White', fg='black',
                    relief='raised',
                    activebackground='DodgerBlue2',
                    activeforeground='OrangeRed2',
                    font=('Arial', 20, 'bold'),
                    command=lambda: go_back(W))
    back_btn.pack(side='left', padx=10, pady=10)