from tkinter import Button, Label, Frame, messagebox, filedialog
from app_state import app_state
from reportlab.lib.pagesizes import letter  # libreria para crear el pdf
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def accesories_menu(W, go_back, go_bells_menu, go_elbows_menu, go_damper_menu,
                    go_transitions_menu, go_junctions_menu, go_results_menu):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()


    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')


    accesories__main = Label(top_frame, text='Menu de accesorios',
                            font=('Arial', 30),
                            bg='gray5',
                            fg='gray60')
    accesories__main.pack(side='top', pady=1)

    accesories_aux = Label(top_frame, text='Se ha concluido el calculo de perdidas en tramos rectos, a continuación \n'
                        ' se calcularan las perdidas por accesorios, cada accesorio se debe identificar \n'
                        ' con un codigo el cual se ingresa en el menu de cada accesorio',
                            font=('Arial', 20),
                            bg='gray5',
                            fg='gray60')
    accesories_aux.pack(side='top', pady=1)


    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(side='top', fill='both', expand=True)


    bells_btn = Button(middle_frame, text='1. Campanas',
                        bg='white', fg='black',
                        relief='raised',
                        activebackground='DodgerBlue2',
                        activeforeground='OrangeRed2',
                        font=('Arial', 25, 'bold'),
                        width=40,
                        command=lambda: go_bells_menu(W))
    bells_btn.pack(padx=5, pady=10, anchor='n')


    elbows_btn = Button(middle_frame, text='2. Codos',
                            bg='white', fg='black',
                            relief='raised',
                            activebackground='DodgerBlue2',
                            activeforeground='OrangeRed2',
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command=lambda: go_elbows_menu(W))
    elbows_btn.pack(padx=5, pady=5)

    damper_btn = Button(middle_frame, text='3. Dampers',
                            bg='white', fg='black',
                            relief='raised',
                            activebackground='DodgerBlue2',
                            activeforeground='OrangeRed2',
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command=lambda: go_damper_menu(W))
    damper_btn.pack(padx=5, pady=5)


    reducers_btn = Button(middle_frame, text='5. Transiciones',
                            bg='white', fg='black',
                            relief='raised',
                            activebackground='DodgerBlue2',
                            activeforeground='OrangeRed2',
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command=lambda: go_transitions_menu(W))
    reducers_btn.pack(padx=5, pady=5)


    #tees_btn = Button(middle_frame, text='6. Uniones - Empalmes',
                            #bg='white', fg='black',
                            #relief='raised',
                            #activebackground='DodgerBlue2',
                            #activeforeground='OrangeRed2',
                            #font=('Arial', 25, 'bold'),
                            #width=40,
                            #command= lambda: go_junctions_menu(W))
    #tees_btn.pack(padx=5, pady=5)

    results_btn = Button(middle_frame, text='6. Resultados de accesorios',
                            bg='white', fg='black',
                            relief='raised',
                            activebackground='DodgerBlue2',
                            activeforeground='OrangeRed2',
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command=lambda: go_results_menu(W))
    results_btn.pack(padx=5, pady=5)


    def generate_fittings_pdf():
        selected = app_state.selected_option.get()
        fittings = app_state.fittings   # each entry: [label, fitting_type, ΔP (Pa)]

        # Nothing to report yet
        if not fittings:
            messagebox.showwarning(
                "Sin accesorios",
                "No hay accesorios registrados para generar el reporte.")
            return

        # Header depends on unit system (same rule as accesories_results_menu)
        if selected in (1, 2):
            dp_header = 'ΔP (Pa)'
        else:
            dp_header = 'ΔP (inH₂O)'

        data = [['Etiqueta', 'Tipo de Accesorio', dp_header]]

        try:
            for fitting in fittings:
                label        = fitting[0]
                fitting_type = fitting[1]
                delta_p_pa   = float(fitting[2])

                # Unit conversion, identical to the on-screen results table
                if selected in (1, 2):
                    delta_p_display = f'{delta_p_pa:.4f}'
                else:
                    delta_p_display = f'{delta_p_pa * 0.00401463:.6f}'  # Pa -> inH₂O

                data.append([label, fitting_type, delta_p_display])
        except (ValueError, TypeError, IndexError) as e:
            messagebox.showerror(
                "Datos inválidos",
                f"No se pudieron leer los valores de los accesorios.\n{e}")
            return

        # Ask where to save
        default_name = (app_state.filename.get() or "reporte_accesorios") + ".pdf"
        pdf_filename = filedialog.asksaveasfilename(
            defaultextension=".pdf", initialfile=default_name,
            filetypes=[("PDF", "*.pdf")])
        if not pdf_filename:        # user cancelled
            return

        # Build the document
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
        styles = getSampleStyleSheet()
        header_text = ("A continuación se muestran las pérdidas de presión "
                       "calculadas para cada accesorio")

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

        story = [Paragraph(header_text, styles["Normal"]), Spacer(1, 18), table]

        try:
            doc.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)
        except PermissionError:
            messagebox.showerror(
                "Error", "No se pudo guardar el PDF. ¿Está abierto en otro programa?")
            return

        messagebox.showinfo("Listo", f"Reporte guardado en:\n{pdf_filename}")

    pdf_btn = Button(middle_frame, text='Generar reporte de accesorios en PDF',
                     bg='white', fg='black', relief='raised',
                     activebackground='DodgerBlue2', activeforeground='OrangeRed2',
                     font=('Arial', 25, 'bold'), width=40,
                     command=generate_fittings_pdf)
    pdf_btn.pack(padx=5, pady=5)


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