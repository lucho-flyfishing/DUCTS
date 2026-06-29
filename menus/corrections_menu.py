from tkinter import Button, Label, Frame, messagebox, filedialog
from app_state import app_state
from reportlab.lib.pagesizes import letter  # libreria para crear el pdf
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def _num(x):
    """Coerce a Tk variable, an Entry widget, or a plain value to float.

    flowrate_entries / length_entries may hold numbers OR Tk widgets;
    this works for all of them (Entry.get(), StringVar.get(), DoubleVar.get(),
    or a bare float).
    """
    if hasattr(x, "get"):
        x = x.get()
    return float(x)


def corrections_menu(W, go_back, go_accesories_menu, go_roughness_menu,
                     go_rectangular_eq_menu, go_branches_results_menu):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()

    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')

    pre_result_main = Label(top_frame, text='Menu de correciones',
                            font=('Arial', 35), bg='gray5', fg='gray60')
    pre_result_main.pack(side='top', pady=1)

    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(expand=True, anchor='center')

    branches_results_btn = Button(middle_frame, text='Resultados del dimensionamiento de ramales',
                                bg='white', fg='black',
                                relief='raised',
                                activebackground='DodgerBlue2',
                                activeforeground='OrangeRed2',
                                font=('Arial', 25, 'bold'),
                                width=40,
                                command=lambda: go_branches_results_menu(W))
    branches_results_btn.pack(padx=5, pady=5)

    roughness_btn = Button(middle_frame, text='Correcion por rugosidad del material del ducto',
                                bg='white', fg='black',
                                relief='raised',
                                activebackground='DodgerBlue2',
                                activeforeground='OrangeRed2',
                                font=('Arial', 25, 'bold'),
                                width=40,
                                command=lambda: go_roughness_menu(W))
    roughness_btn.pack(padx=5, pady=10, anchor='n')

    rectangular_eq_btn = Button(middle_frame, text='Ductos rectangulares equivalentes',
                                bg='white', fg='black',
                                relief='raised',
                                activebackground='DodgerBlue2',
                                activeforeground='OrangeRed2',
                                font=('Arial', 25, 'bold'),
                                width=40,
                                command=lambda: go_rectangular_eq_menu(W))
    rectangular_eq_btn.pack(padx=5, pady=5)

    re_design_btn = Button(middle_frame, text='Volver a hacer el dimensionamiento preliminar',
                            bg='white', fg='black',
                            relief='raised',
                            activebackground='DodgerBlue2',
                            activeforeground='OrangeRed2',
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command=lambda: go_back(W))
    re_design_btn.pack(padx=5, pady=5)

    accesories_btn = Button(middle_frame, text='Calcular perdidas en accesorios',
                            bg='white', fg='black',
                            relief='raised',
                            activebackground='DodgerBlue2',
                            activeforeground='OrangeRed2',
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command=lambda: go_accesories_menu(W))
    accesories_btn.pack(padx=5, pady=5)

    def generate_pdf():
        rows = app_state.duct_number.get()
        selected = app_state.selected_option.get()

        flowrate_values = app_state.flowrate_entries
        length_values = app_state.length_entries
        diameters_values = getattr(app_state, "diameters_values", [])

        # Shared design values (same for every branch) -> shown once on top.
        S = getattr(app_state, "S", None)            # friction rate
        temperature = getattr(app_state, "get_temp", None)

        # Make sure per-branch results actually exist before building anything.
        if (len(diameters_values) < rows or
                len(flowrate_values) < rows or
                len(length_values) < rows):
            messagebox.showwarning(
                "Sin resultados",
                "Primero debes calcular los diámetros antes de generar el reporte.")
            return

        # --- Per-branch table (no Pérdidas column: that value is the same for all) ---
        headers = {
            1: ['Ramal', 'Caudal (L/s)',  'Longitud (m)',  'Diámetro (mm)'],
            2: ['Ramal', 'Caudal (m³/s)', 'Longitud (m)',  'Diámetro (mm)'],
            3: ['Ramal', 'Caudal (cfm)',  'Longitud (ft)', 'Diámetro (in)'],
        }
        data = [headers.get(selected, headers[1])]

        try:
            for i in range(rows):
                data.append([
                    i + 1,
                    f"{_num(flowrate_values[i]):.2f}",
                    f"{_num(length_values[i]):.2f}",
                    f"{_num(diameters_values[i]):.1f}",
                ])
        except (ValueError, TypeError) as e:
            messagebox.showerror(
                "Datos inválidos",
                f"No se pudieron leer los valores de los ramales.\n{e}")
            return

        # --- Shared parameters block (label + value pairs) ---
        # Units follow the selected system (3 = imperial).
        fric_unit = "inH₂O/ft" if selected == 3 else "Pa/m"
        temp_unit = "°F" if selected == 3 else "°C"

        params = []
        if S is not None:
            try:
                params.append(("Pérdida de carga de diseño",
                               f"{_num(S):.3f} {fric_unit}"))
            except (ValueError, TypeError):
                pass
        if temperature is not None:
            try:
                params.append(("Temperatura", f"{_num(temperature):.1f} {temp_unit}"))
            except (ValueError, TypeError):
                pass

        # To add more shared values, append another tuple here, e.g. altitude:
        # altitude = getattr(app_state, "get_alt", None)
        # if altitude is not None:
        #     alt_unit = "ft" if selected == 3 else "m"
        #     params.append(("Altitud", f"{_num(altitude):.0f} {alt_unit}"))

        # --- Ask where to save ---
        default_name = (app_state.filename.get() or "reporte") + ".pdf"
        pdf_filename = filedialog.asksaveasfilename(
            defaultextension=".pdf", initialfile=default_name,
            filetypes=[("PDF", "*.pdf")])
        if not pdf_filename:        # user cancelled
            return

        # --- Build the document ---
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
        styles = getSampleStyleSheet()
        header_text = ("A continuación se muestran los resultados obtenidos "
                       "del dimensionamiento de los ductos")

        def draw_footer(canvas, doc):
            canvas.setFont("Helvetica", 9)
            canvas.drawString(72, 36, "[footer]")   # ~0.5 in from bottom

        table = Table(data, repeatRows=1)            # repeat header if it spills to page 2
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR',  (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN',      (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME',   (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        story = [Paragraph(header_text, styles["Normal"]), Spacer(1, 12)]
        if params:
            param_table = Table([[f"{label}:", value] for label, value in params],
                                hAlign='LEFT')
            param_table.setStyle(TableStyle([
                ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),  # bold labels
                ('ALIGN',    (0, 0), (0, -1), 'LEFT'),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ]))
            story.append(param_table)
            story.append(Spacer(1, 18))
        story.append(table)

        try:
            doc.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)
        except PermissionError:
            messagebox.showerror(
                "Error", "No se pudo guardar el PDF. ¿Está abierto en otro programa?")
            return

        messagebox.showinfo("Listo", f"Reporte guardado en:\n{pdf_filename}")

    pdf_btn = Button(middle_frame, text='Generar reporte de resultados en PDF',
                     bg='white', fg='black', relief='raised',
                     activebackground='DodgerBlue2', activeforeground='OrangeRed2',
                     font=('Arial', 25, 'bold'), width=40,
                     command=generate_pdf)
    pdf_btn.pack(padx=5, pady=5)

    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
    
