from tkinter import Button, Label, Frame, Radiobutton
from app_state import app_state
import resources    

def elbows_menu(W, go_back, go_next):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')


    elbows_lbl = Label(top_frame, text='Codos', font=('Arial', 35), bg='gray5', fg='gray60')
    elbows_lbl.pack(side='top', pady=1)
    
    
    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(expand=True, fill='both')
    total_rows = 4
    total_cols = 4  
    
    for r in range(total_rows):
        middle_frame.rowconfigure(r, weight=1)
    
    for c in range(total_cols):
        middle_frame.columnconfigure(c, weight=1)
    
    radio_style = {
        "width": 50,
        "height": 1,
        "font": ("Arial", 10, "bold"),
        "fg": "OrangeRed2",   
        "activeforeground": "black",
        "activebackground": "OrangeRed2",
        "bg": "gray5",                               
    }
    
    
    def on_select():
        print("Selected elbow:", app_state.selected_elbow.get())
        
        
    Radiobutton(middle_frame, text="1. Codo de radio suave",
                variable=app_state.selected_elbow, value=1,
                command=on_select, **radio_style).grid(row=1, column=0, pady=5)
    
    
    smooth_r_elbow_img = resources.load_image("round_smooth_elbow.png", 
                                    size=(320, 350))  
    smooth_r_elbow_img_lbl = Label(middle_frame, image=smooth_r_elbow_img, bg='gray5')
    smooth_r_elbow_img_lbl.image = smooth_r_elbow_img
    smooth_r_elbow_img_lbl.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="2. Codo circular segmentado", 
                variable=app_state.selected_elbow, value=2,
                command=on_select, **radio_style).grid(row=1, column=1, pady=5)
    
    
    round_mitered_elbow_img = resources.load_image("round_mitered_elbow.png", 
                                    size=(320, 350))
    round_mitered_elbow_img_lbl = Label(middle_frame, image=round_mitered_elbow_img, bg='gray5')
    round_mitered_elbow_img_lbl.image = round_mitered_elbow_img
    round_mitered_elbow_img_lbl.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="3. Codo rectangular segmentado ",
                variable=app_state.selected_elbow, value=3,
                command=on_select, **radio_style).grid(row=1, column=2, pady=5)
    
    
    rectangular_mitered_elbow_img = resources.load_image("rectangular_mitered_elbow.png",
                                    size=(320, 350))
    rectangular_mitered_elbow_img_lbl = Label(middle_frame, image=rectangular_mitered_elbow_img, bg='gray5')
    rectangular_mitered_elbow_img_lbl.image = rectangular_mitered_elbow_img
    rectangular_mitered_elbow_img_lbl.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="4. Codo sin aletas radio suave",
                variable=app_state.selected_elbow, value=4,
                command=on_select, **radio_style).grid(row=1, column=3, pady=5)
    
    
    no_vanes_smooth_elbow_img = resources.load_image("no_vanes_smooth_elbow.png",
                                    size=(320, 350))
    no_vanes_smooth_elbow_img_lbl = Label(middle_frame, image=no_vanes_smooth_elbow_img, bg='gray5')
    no_vanes_smooth_elbow_img_lbl.image = no_vanes_smooth_elbow_img
    no_vanes_smooth_elbow_img_lbl.grid(row=0, column=3, padx=20, pady=10, sticky="nsew")
    
    
    
    Radiobutton(middle_frame, text="5. Codo sin aletas agudo",
                variable=app_state.selected_elbow, value=5,
                command=on_select, **radio_style).grid(row=3, column=0, pady=5)
    
    
    no_vanes_sharp_elbow_img = resources.load_image("no_vanes_sharp_elbow.png",
                                    size=(320, 350))
    no_vanes_sharp_elbow_img_lbl = Label(middle_frame, image=no_vanes_sharp_elbow_img, bg='gray5')
    no_vanes_sharp_elbow_img_lbl.image = no_vanes_sharp_elbow_img
    no_vanes_sharp_elbow_img_lbl.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="6. Codo en z 30 °",
                variable=app_state.selected_elbow, value=6,
                command=on_select, **radio_style).grid(row=3, column=1, pady=5)
    
    
    z_30_elbow_img = resources.load_image("z_30_elbow.png",
                                    size=(320, 350))
    z_30_elbow_img_lbl = Label(middle_frame, image=z_30_elbow_img, bg='gray5')
    z_30_elbow_img_lbl.image = z_30_elbow_img
    z_30_elbow_img_lbl.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="7. Codo circular de  3 , 4 y 5 piezas",
                variable=app_state.selected_elbow, value=7,
                command=on_select, **radio_style).grid(row=3, column=2, pady=5)
    
    
    round_3_4_5_pieces_elbow_img = resources.load_image("round_3_4_5_pieces_elbow.png",
                                    size=(320, 350))
    round_3_4_5_pieces_elbow_img_lbl = Label(middle_frame, image=round_3_4_5_pieces_elbow_img, bg='gray5')
    round_3_4_5_pieces_elbow_img_lbl.image = round_3_4_5_pieces_elbow_img
    round_3_4_5_pieces_elbow_img_lbl.grid(row=2, column=2, padx=20, pady=10, sticky="nsew")
    
    
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
    
    
    back_btn = Button(bottom_frame, text='Regresar', 
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