from tkinter import Button, Label, Frame
from app_state import app_state
from reportlab.lib.pagesizes import letter # importar libreria para crear el pdf
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle 
from reportlab.lib import colors


def corrections_menu(W, go_back, go_accesories_menu, go_roughness_menu, go_rectangular_eq_menu, go_branches_results_menu):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    pre_result_main = Label(top_frame, text='Menu de correciones', font=('Arial', 35), bg='gray5', fg='gray60')
    pre_result_main.pack(side='top', pady=1)
    
    
    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(expand=True, anchor='center')
    
    
    roughness_btn = Button(middle_frame, text='Correcion por rugosidad del material del ducto',
                        bg='white', fg='black', 
                        relief='raised', 
                        activebackground='DodgerBlue2',
                        activeforeground='OrangeRed2', 
                        font=('Arial', 25, 'bold'),
                        width=40,
                        command =lambda: go_roughness_menu(W))
    roughness_btn.pack(padx=5, pady=10, anchor='n')
    
    
    accesories_btn = Button(middle_frame, text='Calcular perdidas en accesorios', 
                            bg='white', fg='black', 
                            relief='raised', 
                            activebackground='DodgerBlue2', 
                            activeforeground='OrangeRed2', 
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command= lambda: go_accesories_menu(W))
    accesories_btn.pack(padx=5, pady=5)
    
    
    rectangular_eq_btn = Button(middle_frame, text='Ductos rectangulares equivalentes', 
                                bg='white', fg='black', 
                                relief='raised', 
                                activebackground='DodgerBlue2', 
                                activeforeground='OrangeRed2', 
                                font=('Arial', 25, 'bold'),
                                width=40,
                                command = lambda: go_rectangular_eq_menu(W))
    rectangular_eq_btn.pack(padx=5, pady=5)


    re_design_btn = Button(middle_frame, text='Volver a hacer el dimensionamiento preliminar', 
                            bg='white', fg='black', 
                            relief='raised', 
                            activebackground='DodgerBlue2', 
                            activeforeground='OrangeRed2', 
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command= lambda: go_back(W))
    re_design_btn.pack(padx=5, pady=5)


    branches_results_btn = Button(middle_frame, text='Resultados del dimensionamiento de ramalaes', 
                            bg='white', fg='black', 
                            relief='raised', 
                            activebackground='DodgerBlue2', 
                            activeforeground='OrangeRed2', 
                            font=('Arial', 25, 'bold'),
                            width=40,
                            command= lambda: go_branches_results_menu(W))
    branches_results_btn.pack(padx=5, pady=5)
    
    
    # Function to generate the PDF
    def generate_pdf():
        # PDF setup
        pdf_filename = app_state.filename.get() + ".pdf"
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

        # Header and footer text
        header = "A continuacion se muestran los resultados obtenidos del dimensionamiento de los ductos"
        footer = "[footer]"

        def draw_text(canvas, doc):
            width, height = letter
            canvas.drawString(80, height - 50, header)
            canvas.drawString(100, height - 700, footer)

        # Get data
        rows = app_state.duct_number.get()
        length_values = app_state.length_entries
        flowrate_values = app_state.flowrate_entries
        selected = app_state.selected_option.get()


        try:
            diameters_values = app_state.diameters_values
        except AttributeError:
            diameters_values = []

        try:
            S = app_state.S
        except AttributeError:
            S = []

        # Define header ONCE
        if selected == 1:
            data = [['Ramal', 'Caudal (L/s)', 'Longitud(m)',  'Pérdidas(Pa/m)', 'Diámetro(mm)']]
        elif selected == 2:
            data = [['Ramal', 'Caudal (m³/s)', 'Longitud(m)', 'Pérdidas(Pa/m)', 'Diámetro(mm)']]
        elif selected == 3:
            data = [['Ramal', 'Caudal (cfm)', 'Longitud(ft)', 'Pérdidas(inH20/ft)', 'Diámetro(in)']]

        # Build rows
        for i in range(rows):
            row_number = i
            flowrate = flowrate_values[i] 
            length = length_values[i]
            diameter = diameters_values[i]
            friction_loss = S[i] 


            row = [row_number, flowrate, length , friction_loss, diameter]
            data.append(row)

        # Create and style the table
        table = Table(data) 
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        # Build PDF
        doc.build([table], onFirstPage=draw_text)

        print(f"PDF '{pdf_filename}' created successfully!")

    pdf_btn = Button(middle_frame, text='Generar reporte en PDF',
                        bg='white', fg='black', 
                        relief='raised', 
                        activebackground='DodgerBlue2',
                        activeforeground='OrangeRed2', 
                        font=('Arial', 25, 'bold'),
                        width=40,
                        command=lambda: generate_pdf())
    pdf_btn.pack(padx=5, pady=5)
    
    
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
    
