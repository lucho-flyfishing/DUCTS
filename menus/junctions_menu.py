from tkinter import Button, Label, Frame, Radiobutton
from app_state import app_state
import resources

def junctions_menu(W, go_back):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')


    tees_lbl = Label(top_frame, text='Uniones - Empalmes', font=('Arial', 35), bg='gray5', fg='gray60')
    tees_lbl.pack(side='top', pady=1)

    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(expand=True, fill='both')
    total_rows = 5  
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
        print("Selected junction:", app_state.selected_junction.get())
        
        
    Radiobutton(middle_frame, text="1. Y 30° convergente ",
                variable=app_state.selected_junction, value=1,
                command=on_select, **radio_style).grid(row=1, column=0, pady=5)
    
    
    Radiobutton(middle_frame, text="2. Y 45° convergente", 
                variable=app_state.selected_junction, value=2,
                command=on_select, **radio_style).grid(row=1, column=1, pady=5)

    Radiobutton(middle_frame, text="3. T circular ",
                variable=app_state.selected_junction, value=3,
                command=on_select, **radio_style).grid(row=1, column=2, pady=5)

    
    Radiobutton(middle_frame, text="4. Y 30° pricipal conico",
                variable=app_state.selected_junction, value=4,
                command=on_select, **radio_style).grid(row=1, column=3, pady=5)

    
    Radiobutton(middle_frame, text="5. Y 45° principal conico",
                variable=app_state.selected_junction, value=5,
                command=on_select, **radio_style).grid(row=3, column=0, pady=5)

    
    Radiobutton(middle_frame, text="6. T rectangular",
                variable=app_state.selected_junction, value=6,
                command=on_select, **radio_style).grid(row=3, column=1, pady=5)

    Radiobutton(middle_frame, text="7. T Ramal circular y principal rectangular°",
                variable=app_state.selected_junction, value=7,
                command=on_select, **radio_style).grid(row=3, column=2, pady=5)

    
    Radiobutton(middle_frame, text="8. T Ramal y principal rectangular",
                variable=app_state.selected_junction, value=8,
                command=on_select, **radio_style).grid(row=3, column=3, pady=5)

    Radiobutton(middle_frame, text="9. Y divergente rectangular y circular",
                variable=app_state.selected_junction, value=9,
                command=on_select, **radio_style).grid(row=5, column=0, pady=5)

    
    Radiobutton(middle_frame, text="10. T divergente ramal circular y principal rectangular",
                variable=app_state.selected_junction, value=10,
                command=on_select, **radio_style).grid(row=5, column=1, pady=5)

    
    Radiobutton(middle_frame, text="11. T divergente rectangular",
                variable=app_state.selected_junction, value=11,
                command=on_select, **radio_style).grid(row=5, column=2, pady=5)

    
    


    wye_30_img = resources.load_image("30_wye.png",
                                    size=(200, 200))
    wye_30_img_lbl = Label(middle_frame, image=wye_30_img, bg='gray5')
    wye_30_img_lbl.image = wye_30_img
    wye_30_img_lbl.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
    
    wye_45_img = resources.load_image("45_wye.png",
                                    size=(200, 200))
    wye_45_img_lbl = Label(middle_frame, image=wye_45_img, bg='gray5')
    wye_45_img_lbl.image = wye_45_img
    wye_45_img_lbl.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

    round_tee_img = resources.load_image("round_tee.png",
                                    size=(200, 200))
    round_tee_img_lbl = Label(middle_frame, image=round_tee_img, bg='gray5')
    round_tee_img_lbl.image = round_tee_img
    round_tee_img_lbl.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")
    
    wye_30_conical_img = resources.load_image("30_conical_wye.png",
                                    size=(200, 200))
    wye_30_conical_img_lbl = Label(middle_frame, image=wye_30_conical_img, bg='gray5')
    wye_30_conical_img_lbl.image = wye_30_conical_img
    wye_30_conical_img_lbl.grid(row=0, column=3, padx=20, pady=10, sticky="nsew")
    
    wye_45_conical_img = resources.load_image("45_conical_wye.png",
                                    size=(200, 200))
    wye_45_conical_img_lbl = Label(middle_frame, image=wye_45_conical_img, bg='gray5')
    wye_45_conical_img_lbl.image = wye_45_conical_img
    wye_45_conical_img_lbl.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
    
    
    rectangular_tee_img = resources.load_image("rectangular_tee.png",
                                    size=(200, 200))
    rectangular_tee_img_lbl = Label(middle_frame, image=rectangular_tee_img, bg='gray5')
    rectangular_tee_img_lbl.image = rectangular_tee_img
    rectangular_tee_img_lbl.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")


    round_tap_rectangular_main_img = resources.load_image("round_tap_rectangular_main_tee.png",
                                    size=(200, 200))
    round_tap_rectangular_main_img_lbl = Label(middle_frame, image=round_tap_rectangular_main_img, bg='gray5')
    round_tap_rectangular_main_img_lbl.image = round_tap_rectangular_main_img
    round_tap_rectangular_main_img_lbl.grid(row=2, column=2, padx=20, pady=10, sticky="nsew")


    rectangular_tap_rectangular_main_img = resources.load_image("rectangular_main_and_tap_tee.png",
                                    size=(200, 200))
    rectangular_tap_rectangular_main_img_lbl = Label(middle_frame, image=rectangular_tap_rectangular_main_img, bg='gray5')
    rectangular_tap_rectangular_main_img_lbl.image = rectangular_tap_rectangular_main_img
    rectangular_tap_rectangular_main_img_lbl.grid(row=2, column=3, padx=20, pady=10, sticky="nsew")
    
    rectangular_and_round_wye_img = resources.load_image("rectangular_and_round_wye_d.png",
                                    size=(200, 200))
    rectangular_and_round_wye_img_lbl = Label(middle_frame, image=rectangular_and_round_wye_img, bg='gray5')
    rectangular_and_round_wye_img_lbl.image = rectangular_and_round_wye_img
    rectangular_and_round_wye_img_lbl.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")
    
    rectangular_main_and_tap_tee_d_img = resources.load_image("rectangular_main_and_tap_tee_d.png",
                                    size=(200, 200))
    rectangular_main_and_tap_tee_d_img_lbl = Label(middle_frame, image=rectangular_main_and_tap_tee_d_img, bg='gray5')
    rectangular_main_and_tap_tee_d_img_lbl.image = rectangular_main_and_tap_tee_d_img
    rectangular_main_and_tap_tee_d_img_lbl.grid(row=4, column=1, padx=20, pady=10, sticky="nsew")

    rectangular_tee_d_img = resources.load_image("rectangular_tee_d.png",
                                    size=(200, 200))
    rectangular_tee_d_img_lbl = Label(middle_frame, image=rectangular_tee_d_img, bg='gray5')
    rectangular_tee_d_img_lbl.image = rectangular_tee_d_img
    rectangular_tee_d_img_lbl.grid(row=4, column=2, padx=20, pady=10, sticky="nsew")


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