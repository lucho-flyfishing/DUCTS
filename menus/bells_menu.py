from tkinter import Button, Label, Frame, Radiobutton
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
    
    
    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(expand=True, fill='both')
    total_rows = 5   # You use rows 0, 1, 2, and 4 (so up to 5)
    total_cols = 4   # You use columns 0–3

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
        print("Selected bell:", app_state.selected_bell.get())
        
    Radiobutton(middle_frame, text="1. Campana de entrada de radio suave sin pared terminal",
                variable=app_state.selected_bell, value=1,
                command=on_select, **radio_style).grid(row=1, column=0, pady=10)
    
    
    Radiobutton(middle_frame, text="2. Campana de entrada de radio suave con pared terminal", 
                variable=app_state.selected_bell, value=2,
                command=on_select, **radio_style).grid(row=1, column=1, pady=10)
    
    
    Radiobutton(middle_frame, text="3. Campana cónica sin pared terminal",
                variable=app_state.selected_bell, value=3,
                command=on_select, **radio_style).grid(row=1, column=2, pady=10)
    
    Radiobutton(middle_frame, text="4. Campana cónica con pared terminal",
                variable=app_state.selected_bell, value=3,
                command=on_select, **radio_style).grid(row=1, column=2, pady=10)


    smooth_img = resources.load_image("smooth.png", size=(300, 200))  
    smooth_img_lbl = Label(middle_frame, image=smooth_img, bg='gray5')
    smooth_img_lbl.image = smooth_img
    smooth_img_lbl.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    
    
    smooth_wall_img = resources.load_image("smooth_wall.png",
                                    size=(300, 200))  
    smooth_wall_img_lbl = Label(middle_frame, image=smooth_wall_img, bg='gray5')
    smooth_wall_img_lbl.image = smooth_wall_img
    smooth_wall_img_lbl.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
    
    
    conical_img = resources.load_image("conical.png",
                                    size=(350, 200))
    conical_img_lbl = Label(middle_frame, image=conical_img, bg='gray5')
    conical_img_lbl.image = conical_img
    conical_img_lbl.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")
    
    
    conical_wall_img = resources.load_image("conical_wall.png",
                                    size=(350, 200))
    conical_wall_img_lbl = Label(middle_frame, image=conical_wall_img, bg='gray5')
    conical_wall_img_lbl.image = conical_wall_img
    conical_wall_img_lbl.grid(row=0, column=3, padx=20, pady=20, sticky="nsew")
    
    
    exit_round_img = resources.load_image("exit_round.png",
                                    size=(300, 200))
    exit_round_img_lbl = Label(middle_frame, image=exit_round_img, bg='gray5')
    exit_round_img_lbl.image = exit_round_img
    exit_round_img_lbl.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
    
    
    exit_round_wall_img = resources.load_image("exit_round_wall.png",
                                    size=(300, 200))
    exit_round_wall_img_lbl = Label(middle_frame, image=exit_round_wall_img, bg='gray5')
    exit_round_wall_img_lbl.image = exit_round_wall_img
    exit_round_wall_img_lbl.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")
    
    exit_rect_img = resources.load_image("exit_rectangular.png",
                                    size=(350, 200))
    exit_rect_img_lbl = Label(middle_frame, image=exit_rect_img, bg='gray5')
    exit_rect_img_lbl.image = exit_rect_img
    exit_rect_img_lbl.grid(row=2, column=2, padx=20, pady=20, sticky="nsew")
    
    exit_rect_wall_img = resources.load_image("exit_rectangular_wall.png",
                                    size=(350, 200))
    exit_rect_wall_img_lbl = Label(middle_frame, image=exit_rect_wall_img, bg='gray5')
    exit_rect_wall_img_lbl.image = exit_rect_wall_img
    exit_rect_wall_img_lbl.grid(row=2, column=3, padx=20, pady=20, sticky="nsew") 
    
    intake_hood_img = resources.load_image("intake_hood.png",
                                    size=(300, 200))
    intake_hood_img_lbl = Label(middle_frame, image=intake_hood_img, bg='gray5')
    intake_hood_img_lbl.image = intake_hood_img
    intake_hood_img_lbl.grid(row=4, column=0, padx=20, pady=20, sticky="nsew")
    
    hood_tapered_img = resources.load_image("hood_tapered.png",
                                    size=(300, 200))
    hood_tapered_img_lbl = Label(middle_frame, image=hood_tapered_img, bg='gray5')
    hood_tapered_img_lbl.image = hood_tapered_img
    hood_tapered_img_lbl.grid(row=4, column=1, padx=20, pady=20, sticky="nsew")
    
    
    
    
    
    
    bottom_frame = Frame(W, bg='gray5')
    bottom_frame.pack(side='bottom', fill='x')
    
    
    back_btn = Button(bottom_frame, text='Regresar',
        bg='white', fg='black',
        relief='raised',
        activebackground='DodgerBlue2',
        activeforeground='OrangeRed2',
        font=('Arial', 20, 'bold'),
        command=lambda: go_back(W))
    back_btn.pack(side='left', padx=10, pady=10)#