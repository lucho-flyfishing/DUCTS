from tkinter import Button, Label, Frame
from app_state import app_state


def accesories_results_menu(W, go_back):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()


    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')

    results_main = Label(top_frame, text='resultados de accesorios',
                         font=('Arial', 30),
                         bg='gray5',
                         fg='gray60')
    results_main.pack(side='top', pady=1)


    # ── Calculations ──────────────────────────────────────────────────────────
    selected = app_state.selected_option.get()
    V        = float(app_state.velocity)
    rho      = float(app_state.rho)
    fittings = app_state.fittings   # each entry: [nombre, Co, duct_num]

    if selected in (1, 2):
        Pv = 0.5 * rho * V ** 2     # Pa
    else:
        Pv = (V / 4005) ** 2        # in w.g.  (V in fpm, standard air)

    # ── Results table ─────────────────────────────────────────────────────────
    table_frame = Frame(W, bg='gray5')
    table_frame.pack(pady=15)

    if selected in (1, 2):
        col_headers = ['Ramal', 'Accesorio', 'ΔP (Pa)']
    else:
        col_headers = ['Ramal', 'Accesorio', 'ΔP (inH₂O)']

    col_widths = [12, 35, 18]

    # Header row
    for col, (header, width) in enumerate(zip(col_headers, col_widths)):
        Label(table_frame, text=header,
              font=('Arial', 12, 'bold'),
              bg='gray15', fg='gray90',
              width=width, anchor='center',
              relief='flat', padx=4, pady=6
              ).grid(row=0, column=col, padx=1, pady=1)

    # Data rows
    for i, fitting in enumerate(fittings):
        nombre   = fitting[0]
        Co       = fitting[1]
        duct_num = fitting[2] if fitting[2] is not None else '—'

        delta_p  = Co * Pv

        row_data = [
            str(duct_num),
            nombre,
            f'{delta_p:.4f}',
        ]

        for col, (value, width) in enumerate(zip(row_data, col_widths)):
            Label(table_frame, text=value,
                  font=('Arial', 12),
                  bg='gray12', fg='gray70',
                  width=width, anchor='center',
                  relief='flat', padx=4, pady=5
                  ).grid(row=i + 1, column=col, padx=1, pady=1)

    # ── end results table ─────────────────────────────────────────────────────


    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn = Button(bottom_frame, text='Regresar',
                      bg='white', fg='black',
                      relief='raised',
                      activebackground='DodgerBlue2',
                      activeforeground='OrangeRed2',
                      font=('Arial', 20, 'bold'),
                      command=lambda: go_back(W))
    back_btn.pack(side='left', padx=10, pady=10)