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
        print("Selected junction:", app_state.selected_diverging_junction.get())
        
        

    Radiobutton(middle_frame, text="1. Y divergente rectangular y circular",
                variable=app_state.selected_diverging_junction, value=1,
                command=on_select, **radio_style).grid(row=1, column=0, pady=5)

    
    Radiobutton(middle_frame, text="2. T divergente ramal circular y principal rectangular",
                variable=app_state.selected_diverging_junction, value=2,
                command=on_select, **radio_style).grid(row=1, column=1, pady=5)

    
    Radiobutton(middle_frame, text="3. T divergente rectangular",
                variable=app_state.selected_diverging_junction, value=3,
                command=on_select, **radio_style).grid(row=1, column=2, pady=5)
    



    
    

    
    rectangular_and_round_wye_img = resources.load_image("rectangular_and_round_wye_d.png",
                                    size=(200, 200))
    rectangular_and_round_wye_img_lbl = Label(middle_frame, image=rectangular_and_round_wye_img, bg='gray5')
    rectangular_and_round_wye_img_lbl.image = rectangular_and_round_wye_img
    rectangular_and_round_wye_img_lbl.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
    
    rectangular_main_and_tap_tee_d_img = resources.load_image("rectangular_main_and_tap_tee_d.png",
                                    size=(200, 200))
    rectangular_main_and_tap_tee_d_img_lbl = Label(middle_frame, image=rectangular_main_and_tap_tee_d_img, bg='gray5')
    rectangular_main_and_tap_tee_d_img_lbl.image = rectangular_main_and_tap_tee_d_img
    rectangular_main_and_tap_tee_d_img_lbl.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

    rectangular_tee_d_img = resources.load_image("rectangular_tee_d.png",
                                    size=(200, 200))
    rectangular_tee_d_img_lbl = Label(middle_frame, image=rectangular_tee_d_img, bg='gray5')
    rectangular_tee_d_img_lbl.image = rectangular_tee_d_img
    rectangular_tee_d_img_lbl.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")


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