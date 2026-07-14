# accesories_results_menu.py

from tkinter import Button, Label, Frame, Canvas, Scrollbar
from app_state import app_state


def accesories_results_menu(W, go_back):
    # Limpiar ventana
    for widget in W.winfo_children():
        widget.destroy()

    # Frame superior
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')

    Label(
        top_frame,
        text='Resultados de Accesorios',
        font=('Arial', 30),
        bg='gray5',
        fg='gray60'
    ).pack(side='top', pady=10)

    # ── Datos ─────────────────────────────────────────────────────────────────
    selected = app_state.selected_option.get()
    fittings = app_state.fittings   # each entry: [label, fitting_type, ΔP (Pa)]

    # ── Tabla de resultados (scrolleable) ─────────────────────────────────────
    table_container = Frame(W, bg='gray5')
    table_container.pack(fill='both', expand=True, pady=15)

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

    # Encabezados según unidades
    if selected in (1, 2):
        dp_header = 'ΔP (Pa)'
    else:
        dp_header = 'ΔP (inH₂O)'

    col_headers = ['Etiqueta', 'Tipo de Accesorio', dp_header]
    col_widths   = [20, 35, 18]

    # Fila de encabezados
    for col, (header, width) in enumerate(zip(col_headers, col_widths)):
        Label(
            table_frame,
            text=header,
            font=('Arial', 12, 'bold'),
            bg='gray15', fg='gray90',
            width=width, anchor='center',
            relief='flat', padx=4, pady=6
        ).grid(row=0, column=col, padx=1, pady=1)

    # Filas de datos
    if not fittings:
        Label(
            table_frame,
            text='No hay accesorios registrados.',
            font=('Arial', 14),
            bg='gray5', fg='gray60'
        ).grid(row=1, column=0, columnspan=3, pady=20)
    else:
        for i, fitting in enumerate(fittings):
            label        = fitting[0]
            fitting_type = fitting[1]
            delta_p_pa   = fitting[2]

            # Conversión de unidades si es necesario
            if selected in (1, 2):
                delta_p_display = f'{delta_p_pa:.4f}'
            else:
                delta_p_display = f'{delta_p_pa * 0.00401463:.6f}'  # Pa → inH₂O

            row_data = [label, fitting_type, delta_p_display]

            for col, (value, width) in enumerate(zip(row_data, col_widths)):
                Label(
                    table_frame,
                    text=value,
                    font=('Arial', 12),
                    bg='gray12', fg='gray70',
                    width=width, anchor='center',
                    relief='flat', padx=4, pady=5
                ).grid(row=i + 1, column=col, padx=1, pady=1)

    # ── Navegación inferior ───────────────────────────────────────────────────
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')

    Button(
        bottom_frame,
        text='Regresar',
        bg='white', fg='black',
        relief='raised',
        activebackground='DodgerBlue2',
        activeforeground='OrangeRed2',
        font=('Arial', 20, 'bold'),
        command=lambda: go_back(W)
    ).pack(side='left', padx=10, pady=10)