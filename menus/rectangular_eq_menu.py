from tkinter import Button, Label, Frame, Canvas, Scrollbar
from app_state import app_state
from tables.rectangular_eq import get_rectangular_eq


# Colors for the selectable Eq cells
CELL_BG = "gray5"
CELL_FG = "white"
HOVER_BG = "gray25"
SELECTED_BG = "DodgerBlue2"
SELECTED_FG = "white"


def rectangular_eq_menu(W, go_back):
    # Clear window
    for widget in W.winfo_children():
        widget.destroy()


    # -------------------------
    # TOP FRAME
    # -------------------------
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')

    title = Label(top_frame,
                  text='En la siguiente tabla se muestran los equivalentes rectangulares para cada \n '
                       'diámetro de ducto circular, considerando diferentes relaciones de aspecto \n'
                       '(ancho:alto). Haz clic en el valor que quieras usar para cada ducto; ese \n'
                       'será el que se incluya en el PDF.',
                  font=('Arial', 15),
                  bg='gray5',
                  fg='gray60')
    title.pack(side='top', pady=1)


    # -------------------------
    # BOTTOM FRAME
    # packed BEFORE the scrollable area so it reserves its space
    # at the bottom first
    # -------------------------
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')


    # -------------------------
    # SCROLLABLE MIDDLE FRAME
    # -------------------------
    scroll_container = Frame(W, bg='gray5')
    scroll_container.pack(side='top', fill='both', expand=True, padx=10, pady=10)

    canvas = Canvas(scroll_container, bg='gray5', highlightthickness=0)
    scrollbar = Scrollbar(scroll_container, orient='vertical', command=canvas.yview)
    middle_frame = Frame(canvas, bg='gray5')

    middle_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas_window = canvas.create_window((0, 0), window=middle_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side='left', fill='both', expand=True)
    scrollbar.pack(side='right', fill='y')

    def _resize_inner(event):
        canvas.itemconfig(canvas_window, width=event.width)

    canvas.bind('<Configure>', _resize_inner)

    def _on_mousewheel(event):
        if event.num == 4:
            canvas.yview_scroll(-1, 'units')
        elif event.num == 5:
            canvas.yview_scroll(1, 'units')
        else:
            canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')

    canvas.bind_all('<MouseWheel>', _on_mousewheel)
    canvas.bind_all('<Button-4>', _on_mousewheel)
    canvas.bind_all('<Button-5>', _on_mousewheel)


    # -------------------------
    # BACK BUTTON (also releases the global mousewheel binding)
    # -------------------------
    def _handle_back():
        canvas.unbind_all('<MouseWheel>')
        canvas.unbind_all('<Button-4>')
        canvas.unbind_all('<Button-5>')
        go_back(W)

    back_btn = Button(
        bottom_frame,
        text='Regresar',
        bg='white',
        fg='black',
        relief='raised',
        activebackground='DodgerBlue2',
        activeforeground='OrangeRed2',
        font=('Arial', 20, 'bold'),
        command=_handle_back
    )

    back_btn.pack(padx=10, pady=10, anchor="w")


    # -------------------------
    # DATA
    # -------------------------
    diameters_values = app_state.diameters_values
    selected = app_state.selected_option.get()


    # -------------------------
    # UNITS
    # -------------------------
    if selected == 3:
        unit = "in"
    else:
        unit = "mm"


    # -------------------------
    # SELECTION STATE (app_state)
    # -------------------------
    if not hasattr(app_state, "rectangular_eq_selection"):
        app_state.rectangular_eq_selection = {}

    for i in range(len(diameters_values)):
        app_state.rectangular_eq_selection.setdefault(i, 1)


    # -------------------------
    # HEADERS
    # -------------------------
    ratios = [1, 2, 3, 4, 5]

    headers = ["Ramal", f"Diámetro ({unit})"] + [f"Eq {r}:1" for r in ratios]

    # Aspect ratio group label spanning the EQ columns
    Label(
        middle_frame,
        text="Relación de aspecto (ancho:alto)",
        bg="gray20",
        fg="yellow",
        font=("Arial", 13, "italic"),
    ).grid(row=0, column=2, columnspan=len(ratios), sticky="nsew", padx=2, pady=(0, 2))

    for col, text in enumerate(headers):
        Label(
            middle_frame,
            text=text,
            bg="gray10",
            fg="white",
            font=("Arial", 22, "bold"),
            padx=10,
            pady=5
        ).grid(row=1, column=col, sticky="nsew")


    # -------------------------
    # BODY TABLE
    # -------------------------
    cell_widgets = {}  # ramal index -> {ratio: label widget}

    def refresh_row(row_index):
        current = app_state.rectangular_eq_selection.get(row_index, 1)
        for ratio, widget in cell_widgets[row_index].items():
            if ratio == current:
                widget.config(bg=SELECTED_BG, fg=SELECTED_FG, font=("Arial", 13, "bold"))
            else:
                widget.config(bg=CELL_BG, fg=CELL_FG, font=("Arial", 13, "normal"))

    def make_select_handler(row_index, ratio):
        def handler(event=None):
            app_state.rectangular_eq_selection[row_index] = ratio
            refresh_row(row_index)
        return handler

    def make_hover_handlers(row_index, ratio):
        def on_enter(event):
            if app_state.rectangular_eq_selection.get(row_index, 1) != ratio:
                cell_widgets[row_index][ratio].config(bg=HOVER_BG)

        def on_leave(event):
            if app_state.rectangular_eq_selection.get(row_index, 1) != ratio:
                cell_widgets[row_index][ratio].config(bg=CELL_BG)

        return on_enter, on_leave

    for i, D in enumerate(diameters_values):

        row = i + 2  # shifted down by 1 to account for the label row

        # Ramal
        Label(
            middle_frame,
            text=str(i + 1),
            bg="gray5",
            fg="white",
            font=("Arial", 13)
        ).grid(row=row, column=0)

        # Diámetro
        Label(
            middle_frame,
            text=f"{round(D, 2)} {unit}",
            bg="gray5",
            fg="white",
            font=("Arial", 13)
        ).grid(row=row, column=1)


        # Equivalentes rectangulares (clickable)
        cell_widgets[i] = {}

        for j, r in enumerate(ratios):

            a, b = get_rectangular_eq(D, r)
            text = f"{round(a, 1)} x {round(b, 1)} {unit}"

            cell = Label(
                middle_frame,
                text=text,
                bg=CELL_BG,
                fg=CELL_FG,
                font=("Arial", 13),
                cursor="hand2",
                padx=8,
                pady=4
            )
            cell.grid(row=row, column=j + 2, sticky="nsew")

            cell.bind("<Button-1>", make_select_handler(i, r))

            on_enter, on_leave = make_hover_handlers(i, r)
            cell.bind("<Enter>", on_enter)
            cell.bind("<Leave>", on_leave)

            cell_widgets[i][r] = cell

        refresh_row(i)