from tkinter import Button, Label, Frame, Radiobutton
from app_state import app_state
import resources

from tkinter import Button, Label, Frame, Radiobutton
from app_state import app_state
import resources


def diverging_junctions_menu(W, go_back):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')


    tees_lbl = Label(top_frame, text='Uniones divergentes', font=('Arial', 35), bg='gray5', fg='gray60')
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
        print("Selected junction:", app_state.selected_diverging_junction.get())
        
        
    
    
    Radiobutton(middle_frame, text="1. T circular con ramal cónico",
                variable=app_state.selected_diverging_junction, value=1,
                command=on_select, **radio_style).grid(row=1, column=0, pady=5)

    
    Radiobutton(middle_frame, text="2. Y circular de 45° con ramal cónico",
                variable=app_state.selected_diverging_junction, value=2,
                command=on_select, **radio_style).grid(row=1, column=1, pady=5)

    
    Radiobutton(middle_frame, text="3. T circular con ramal a 90° y codo de 90°",
                variable=app_state.selected_diverging_junction, value=3,
                command=on_select, **radio_style).grid(row=1, column=2, pady=5)
    
    
    Radiobutton(middle_frame, text="4. T circular con ramal a 90° y codo de 45°",
                variable=app_state.selected_diverging_junction, value=4,
                command=on_select, **radio_style).grid(row=1, column=3, pady=5)
    
    
    Radiobutton(middle_frame, text="5. T rectangular ",
                variable=app_state.selected_diverging_junction, value=5,
                command=on_select, **radio_style).grid(row=3, column=0, pady=5)
    
    
    Radiobutton(middle_frame, text="6. Y circular o rectangular ",
                variable=app_state.selected_diverging_junction, value=6,
                command=on_select, **radio_style).grid(row=3, column=1, pady=5)
    
    
    Radiobutton(middle_frame, text="7. T con principal rectangular y ramal circular ",
                variable=app_state.selected_diverging_junction, value=7,
                command=on_select, **radio_style).grid(row=3, column=2, pady=5)
    
    
    Radiobutton(middle_frame, text="8. T con principal rectangular y ramal circular cónico ",
                variable=app_state.selected_diverging_junction, value=8,
                command=on_select, **radio_style).grid(row=3, column=3, pady=5)
    
    Radiobutton(middle_frame, text="9. T con principal y ramal rectangular ",
                variable=app_state.selected_diverging_junction, value=9,
                command=on_select, **radio_style).grid(row=5, column=0, pady=5)
    

    round_conical_branch_tee_d_img = resources.load_image("round_conical_branch_tee_d.png",
                                    size=(200, 200))
    round_conical_branch_tee_d_img_lbl = Label(middle_frame, image=round_conical_branch_tee_d_img, bg='gray5')
    round_conical_branch_tee_d_img_lbl.image = round_conical_branch_tee_d_img
    round_conical_branch_tee_d_img_lbl.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
    
    
    _45_round_conical_branch_wye_d_img = resources.load_image("45_round_conical_branch_wye_d.png",
                                    size=(200, 200))
    _45_round_conical_branch_wye_d_img_lbl = Label(middle_frame, image=_45_round_conical_branch_wye_d_img, bg='gray5')
    _45_round_conical_branch_wye_d_img_lbl.image = _45_round_conical_branch_wye_d_img
    _45_round_conical_branch_wye_d_img_lbl.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")
    
    
    _45_round_conical_branch_wye_d_img = resources.load_image("90_round_branch_to_main_with_45_elbow_tee_d.png",
                                    size=(200, 200))
    _45_round_conical_branch_wye_d_img_lbl = Label(middle_frame, image=_45_round_conical_branch_wye_d_img, bg='gray5')
    _45_round_conical_branch_wye_d_img_lbl.image = _45_round_conical_branch_wye_d_img
    _45_round_conical_branch_wye_d_img_lbl.grid(row=0, column=3, padx=20, pady=10, sticky="nsew")
    
    
    _90_round_conical_branch_tee_d_img = resources.load_image("90_round_branch_to_main_with_90_elbow_tee_d.png",
                                    size=(200, 200))
    _90_round_conical_branch_tee_d_img_lbl = Label(middle_frame, image=_90_round_conical_branch_tee_d_img, bg='gray5')
    _90_round_conical_branch_tee_d_img_lbl.image = _90_round_conical_branch_tee_d_img
    _90_round_conical_branch_tee_d_img_lbl.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")
    
    

    
    
    rectangular_tee_d_img = resources.load_image("rectangular_tee_d.png", 
                                    size=(200, 200))
    rectangular_tee_d_img_lbl = Label(middle_frame, image=rectangular_tee_d_img, bg='gray5')
    rectangular_tee_d_img_lbl.image = rectangular_tee_d_img
    rectangular_tee_d_img_lbl.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
    
    
    rectangular_and_round_wye_d_img = resources.load_image("rectangular_and_round_wye_d.png",
                                    size=(200, 200))
    rectangular_and_round_wye_d_img_lbl = Label(middle_frame, image=rectangular_and_round_wye_d_img, bg='gray5')
    rectangular_and_round_wye_d_img_lbl.image = rectangular_and_round_wye_d_img
    rectangular_and_round_wye_d_img_lbl.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")
    
    
    rectangular_main_to_round_tap_tee_d_img = resources.load_image("rectangular_main_to_round_tap_tee_d.png",
                                    size=(200, 200))
    rectangular_main_to_round_tap_tee_d_img_lbl = Label(middle_frame, image=rectangular_main_to_round_tap_tee_d_img, bg='gray5')
    rectangular_main_to_round_tap_tee_d_img_lbl.image = rectangular_main_to_round_tap_tee_d_img
    rectangular_main_to_round_tap_tee_d_img_lbl.grid(row=2, column=2, padx=20, pady=10, sticky="nsew")
    
    
    rectangular_main_to_round_tap_conical_tee_d_img = resources.load_image("rectangular_main_to_round_tap_conical_tee_d.png",
                                    size=(200, 200))
    rectangular_main_to_round_tap_conical_tee_d_img_lbl = Label(middle_frame, image=rectangular_main_to_round_tap_conical_tee_d_img, bg='gray5')
    rectangular_main_to_round_tap_conical_tee_d_img_lbl.image = rectangular_main_to_round_tap_conical_tee_d_img
    rectangular_main_to_round_tap_conical_tee_d_img_lbl.grid(row=2, column=3, padx=20, pady=10, sticky="nsew")


    rectangular_main_and_tap_tee_d_img = resources.load_image("rectangular_main_and_tap_tee_d.png",
                                    size=(200, 200))
    rectangular_main_and_tap_tee_d_img_lbl = Label(middle_frame, image=rectangular_main_and_tap_tee_d_img, bg='gray5')
    rectangular_main_and_tap_tee_d_img_lbl.image = rectangular_main_and_tap_tee_d_img
    rectangular_main_and_tap_tee_d_img_lbl.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")
    
    
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