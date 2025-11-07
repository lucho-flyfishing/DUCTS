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


    smooth_img = resources.load_image("smooth.png",
                                    size=(300, 200))  
    smooth_img_lbl = Label(middle_frame, image=smooth_img, bg='gray5')
    smooth_img_lbl.image = smooth_img
    smooth_img_lbl.grid(row=0, column=0, padx=20, pady=20)

    smooth_wall_img = resources.load_image("smooth_wall.png",
                                    size=(300, 200))  
    smooth_wall_img_lbl = Label(middle_frame, image=smooth_wall_img, bg='gray5')
    smooth_wall_img_lbl.image = smooth_wall_img
    smooth_wall_img_lbl.grid(row=0, column=1, padx=20, pady=20)


    conical_img = resources.load_image("conical.png",
                                    size=(350, 200))
    conical_img_lbl = Label(middle_frame, image=conical_img, bg='gray5')
    conical_img_lbl.image = conical_img
    conical_img_lbl.grid(row=0, column=2, padx=20, pady=20)

    conical_wall_img = resources.load_image("conical_wall.png",
                                    size=(350, 200))
    conical_wall_img_lbl = Label(middle_frame, image=conical_wall_img, bg='gray5')
    conical_wall_img_lbl.image = conical_wall_img
    conical_wall_img_lbl.grid(row=0, column=3, padx=20, pady=20)

    
    
    
    
    
    
    
    
    
    
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