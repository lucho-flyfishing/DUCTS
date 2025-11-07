from tkinter import Button, Label, Frame
from app_state import app_state
from PIL import Image, ImageTk
import resources  

def bells_menu(W, go_back):
    
    for widget in W.winfo_children():
        widget.destroy()
    
    
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    bells_lbl = Label(top_frame, text='Campanas', font=('Arial', 35), bg='gray5', fg='gray60')
    bells_lbl.pack(side='top', pady=1)
    
    
    middle_frame = Frame(W, bg='gray10')
    middle_frame.pack(expand=True, fill='both')
    
    
    bell_no_wall_img = resources.load_image("smooth_converging_bellmouth_without_end_wall.png",
                                    size=(300, 200))  
    bell_no_wall_lbl = Label(middle_frame, image=bell_no_wall_img, bg='gray5')
    bell_no_wall_lbl.image = bell_no_wall_img
    bell_no_wall_lbl.grid(row=0, column=0, padx=20, pady=20)

    bell_with_wall_img = resources.load_image("smooth_converging_bellmouth_with_wall.png",
                                    size=(300, 200))  
    bell_with_wall_lbl = Label(middle_frame, image=bell_with_wall_img, bg='gray5')
    bell_with_wall_lbl.image = bell_with_wall_img
    bell_with_wall_lbl.grid(row=0, column=1, padx=20, pady=20)
    
    
    conical_bell_no_wall_img = resources.load_image("conical_bell_no_wall.png",
                                    size=(350, 200))
    conical_bell_no_wall_lbl = Label(middle_frame, image=conical_bell_no_wall_img, bg='gray5')
    conical_bell_no_wall_lbl.image = conical_bell_no_wall_img
    conical_bell_no_wall_lbl.grid(row=0, column=2, padx=20, pady=20)
    
    conical_bell_with_wall_img = resources.load_image("conical_bell_with_end_wall.png",
                                    size=(350, 200))
    conical_bell_with_wall_lbl = Label(middle_frame, image=conical_bell_with_wall_img, bg='gray5')
    conical_bell_with_wall_lbl.image = conical_bell_with_wall_img
    conical_bell_with_wall_lbl.grid(row=0, column=3, padx=20, pady=20)
    
    
    
    
    
    
    
    
    
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