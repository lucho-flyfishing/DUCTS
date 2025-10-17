from tkinter import Button, Label, Entry, Frame
from app_state import app_state

def file_name_menu(W, go_back, go_next):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    file_name_lbl = Label(W, text=('El programa va a crear un archivo con los resultados.\n'
                        'Introduzca el nombre con el que desea guardar \n el archivo y presione '
                        '“Guardar nombre del archivo”, \n luego presione “Siguiente”:'), 
                        font=('Arial', 26), bg='gray5', fg='gray60')
    file_name_lbl.pack(pady=1)
    
    
    file_name_entry = Entry(W, font=('Arial', 12), 
                            bg='white', fg='gray', 
                            relief='solid', bd=2, 
                            highlightthickness=2, 
                            highlightbackground='black')
    file_name_entry.pack(pady=5, ipady=5, ipadx=10)
    
    
    placeholder = 'Escribe aquí...'
    file_name_entry.insert(0, placeholder)
    
    
    def on_focus_in(event):
        if file_name_entry.get() == placeholder:
            file_name_entry.delete(0, 'end')
            file_name_entry.config(fg='black')

    def on_focus_out(event):
        if file_name_entry.get() == '':
            file_name_entry.insert(0, placeholder)
            file_name_entry.config(fg='gray')
            
            
    file_name_entry.bind('<FocusIn>', on_focus_in)
    file_name_entry.bind('<FocusOut>', on_focus_out)
    
    
    
    file_name_entry.focus()
    
    
    def save_filename():
        filename = file_name_entry.get()
        
        
        if filename == placeholder or filename.strip() == "":
            print("Nombre de archivo inválido.")
        else:
            app_state.filename.set(filename)
            print(f"Guardando como: {app_state.filename.get()}")
            
            
    save_btn = Button(W, text='Guardar nombre del archivo', 
                    bg='White', fg='black', 
                    relief='raised',
                    activebackground='DodgerBlue2', 
                    activeforeground='OrangeRed2',
                    highlightbackground='OrangeRed2',
                    font=('Arial', 20, 'bold'), 
                    command=save_filename)
    save_btn.pack(pady=10)
    
    
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
    
    
    next_btn = Button(bottom_frame, text='Siguiente',
                    bg='White', fg='black',
                    relief='raised',
                    activebackground='DodgerBlue2',
                    activeforeground='OrangeRed2',
                    font=('Arial', 20, 'bold'),
                    command=lambda: go_next(W))
    next_btn.pack(side='right' , padx= 10, pady=10)