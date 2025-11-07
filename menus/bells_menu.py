from tkinter import Button, Label, Frame
from app_state import app_state
from PIL import Image, ImageTk
import resources  # ✅ importa resources desde el nivel principal (funciona si ducts es el package principal)

def bells_menu(W, go_back):
    # Limpiar la ventana
    for widget in W.winfo_children():
        widget.destroy()
        
    # ---- TOP FRAME ----
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    pre_result_main = Label(top_frame, text='Campanas', font=('Arial', 35), bg='gray5', fg='gray60')
    pre_result_main.pack(side='top', pady=1)
    
    # ---- MIDDLE FRAME ----
    middle_frame = Frame(W, bg='gray10')
    middle_frame.pack(expand=True, fill='both')

    # 👉 Cargar imagen desde resources.py (carpeta /images)
    img_campana = resources.load_image("smooth_converging_bellmouth_without_end_wall.png", size=(300, 200))  # cambia el nombre según tu archivo
    img_label = Label(middle_frame, image=img_campana, bg='gray10')
    img_label.image = img_campana  # evita que se borre de memoria
    img_label.pack(pady=20)

    # ---- BOTTOM FRAME ----
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
    
    back_btn = Button(
        bottom_frame, text='Regresar',
        bg='white', fg='black',
        relief='raised',
        activebackground='DodgerBlue2',
        activeforeground='OrangeRed2',
        font=('Arial', 20, 'bold'),
        command=lambda: go_back(W)
    )
    back_btn.pack(side='left', padx=10, pady=10)