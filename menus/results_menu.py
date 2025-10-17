from tkinter import *

def results_menu(W, go_back):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    results_lbl = Label(top_frame, text='Resultados generados y guardados con éxito.', 
                        font=('Arial', 30), bg='gray5', fg='gray80')
    results_lbl.pack(pady=20)
    
    
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(pady=20)
    
    
    back_btn = Button(bottom_frame, text='Volver', 
                    bg='White', fg='black',
                    relief='raised', 
                    activebackground='DodgerBlue2', 
                    activeforeground='OrangeRed2', 
                    font=('Arial', 20, 'bold'),
                    command=lambda: go_back(W))
    back_btn.pack(side='left', padx=10, pady=10)