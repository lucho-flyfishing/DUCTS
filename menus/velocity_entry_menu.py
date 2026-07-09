from tkinter import Frame, Label, Entry, Button
from app_state import app_state


# ASHRAE Handbook – HVAC Applications 2015, Table 8, Section 48
# Main circular duct max velocities (m/s) by location and RC(N) level
ASHRAE_MAIN_CIRCULAR = {
    "Ducto vertical ó ducto sobre techo de panel yeso": {
        "Baja  (RC 25)":   12.7,
        "Media (RC 35)":   17.8,
        "Alta  (RC 45)":   25.4,
    },
    "Sobre techo acústico suspendido": {
        "Baja  (RC 25)":   10.2,
        "Media (RC 35)":   15.2,
        "Alta  (RC 45)":   22.9,
    },
    "Dentro de espacio ocupado": {
        "Baja  (RC 25)":    8.6,
        "Media (RC 35)":   13.2,
        "Alta  (RC 45)":   19.8,
    },
}

# Conversion factor m/s → fpm
MS_TO_FPM = 196.85


def velocity_entry_menu(W, go_back, go_next):
    for widget in W.winfo_children():
        widget.destroy()


    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')


    velocity_lbl = Label(top_frame, text=' Ingrese la velocidad de aire '
                        'del ramal principal:',
                        font=('Arial', 30), bg='gray5', fg='gray80')
    velocity_lbl.pack(side='top', pady=1)


    # ── ASHRAE reference widget ───────────────────────────────────────────────
    reference_frame = Frame(W, bg='gray5')
    reference_frame.pack(pady=(10, 0))

    ref_title = Label(reference_frame,
                    text='Velocidades máximas recomendadas — Ducto circular principal',
                    font=('Arial', 22, 'bold'), bg='gray5', fg='OrangeRed2')
    ref_title.grid(row=0, column=0, columnspan=5, pady=(0, 6))

    selected = app_state.selected_option.get()

    # Table header
    headers = ['Ubicación', 'Velocidad baja (RC 25)', 'Velocidad media (RC 35)', 'Velocidad alta (RC 45)']
    col_widths = [28, 22, 22, 22]
    for col, (h, w) in enumerate(zip(headers, col_widths)):
        Label(reference_frame, text=h, font=('Arial', 22, 'bold'),
            bg='gray15', fg='gray80', width=w, anchor='center',
            relief='flat', padx=4, pady=4
            ).grid(row=1, column=col, padx=1, pady=1)

    # Table rows
    for row_idx, (location, ranges) in enumerate(ASHRAE_MAIN_CIRCULAR.items(), start=2):
        Label(reference_frame, text=location, font=('Arial', 22),
            bg='gray12', fg='gray75', width=col_widths[0], anchor='w',
            padx=6, pady=3
            ).grid(row=row_idx, column=0, padx=1, pady=1)

        for col_idx, (range_label, max_vel_ms) in enumerate(ranges.items(), start=1):
            if selected == 3:           # imperial — show fpm
                display_val = f"{max_vel_ms * MS_TO_FPM:.0f} fpm"
            else:                       # metric — show m/s
                display_val = f"{max_vel_ms} m/s"

            Label(reference_frame, text=display_val, font=('Arial', 22, 'bold'),
                bg='gray12', fg='OrangeRed2', width=col_widths[col_idx],
                anchor='center', padx=4, pady=3
                ).grid(row=row_idx, column=col_idx, padx=1, pady=1)

    ref_note = Label(reference_frame,
                    text='Las velocidades recomendadas por “ASHRAE Handbook – HVAC Applications 2015 '
                        '/ Section 48 Noise and vibration control” se basan en criterios acústicos \n'
                        '· el RC(N): que aparece en la tabla es el criterio acústico del espacio de instalación'
                        '· para ramales: se usa el 80% de los valores anteriores',
                    font=('Arial', 12, 'italic'), bg='gray5', fg='gray55')
    ref_note.grid(row=5, column=0, columnspan=5, pady=(5, 0))
    # ── end reference widget ──────────────────────────────────────────────────


    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(pady=20)


    if selected == 1:
        velocity_unit_lbl  = Label(middle_frame, text='velocidad (m/s)',
                                font=('Arial', 24), bg='gray5', fg='OrangeRed2')
        velocity_unit_lbl.grid(row=0, column=0, padx=5)


    elif selected == 2:
        velocity_unit_lbl = Label(middle_frame, text='velocidad (m/s)',
                                font=('Arial', 24), bg='gray5', fg='OrangeRed2')
        velocity_unit_lbl.grid(row=0, column=0, padx=5)


    else:
        velocity_unit_lbl = Label(middle_frame, text='velocidad (fpm)',
                                font=('Arial', 24), bg='gray5', fg='OrangeRed2')
        velocity_unit_lbl.grid(row=0, column=0, padx=5)


    velocity_entry = Entry(middle_frame, font=('Arial', 15),
                        bg='white', fg='gray',
                        relief='solid', bd=2,
                        highlightthickness=2,
                        highlightbackground='black')
    velocity_entry.grid(row=0, column=1)


    v_placeholder = 'Escribe aquí...'
    velocity_entry.insert(0, v_placeholder)


    def on_focus_in(event):
        if velocity_entry.get() == v_placeholder:
            velocity_entry.delete(0, 'end')
            velocity_entry.config(fg='black')


    def on_focus_out(event):
        if velocity_entry.get() == '':
            velocity_entry.insert(0, v_placeholder)
            velocity_entry.config(fg='gray')


    velocity_entry.bind('<FocusIn>', on_focus_in)
    velocity_entry.bind('<FocusOut>', on_focus_out)


    velocity_entry.focus()


    def save_velocity():
        app_state.velocity = velocity_entry.get()
        print(f"Velocidad: {app_state.velocity}")

    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn = Button(bottom_frame, text='Volver',
                    bg='White', fg='black',
                    relief='raised',
                    activebackground='DodgerBlue2',
                    activeforeground='OrangeRed2',
                    font=('Arial', 20, 'bold'),
                    command=lambda: go_back(W))
    back_btn.pack(side='left', padx=10, pady=10)


    next_btn = Button(bottom_frame, text='Guardar y continuar',
                    bg='White', fg='black',
                    relief='raised',
                    activebackground='DodgerBlue2',
                    activeforeground='OrangeRed2',
                    font=('Arial', 20, 'bold'),
                    command=lambda: [save_velocity(), go_next(W)])
    next_btn.pack(side='right' , padx= 10, pady=10)