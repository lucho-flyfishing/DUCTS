from tkinter import Button, Label, Frame, Radiobutton
from app_state import app_state
import resources

def damper_menu(W, go_back):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')


    dampers_lbl = Label(top_frame, text='Dampers', font=('Arial', 35), bg='gray5', fg='gray60')
    dampers_lbl.pack(side='top', pady=1)

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
        print("Selected damper:", app_state.selected_damper.get())
        
        
    Radiobutton(middle_frame, text="1. Damper mariposa circular",
                variable=app_state.selected_damper, value=1,
                command=on_select, **radio_style).grid(row=1, column=0, pady=5)
    
    
    round_butterfly_damper_img = resources.load_image("round_butterfly_damper.png",
                                    size=(300, 200))
    round_butterfly_damper_img_lbl = Label(middle_frame, image=round_butterfly_damper_img, 
                                        bg='gray5')
    round_butterfly_damper_img_lbl.image = round_butterfly_damper_img
    round_butterfly_damper_img_lbl.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="2. Damper mariposa rectangular",
                variable=app_state.selected_damper, value=2,
                command=on_select, **radio_style).grid(row=1, column=1, pady=5)
    
    
    rectangular_butterfly_damper_img = resources.load_image("rectangular_butterfly_damper.png",
                                        size=(300, 200))
    rectangular_butterfly_damper_img_lbl = Label(middle_frame, image=rectangular_butterfly_damper_img, 
                                                bg='gray5')
    rectangular_butterfly_damper_img_lbl.image = rectangular_butterfly_damper_img
    rectangular_butterfly_damper_img_lbl.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="3. Damper compuerta rectangular",
                variable=app_state.selected_damper, value=3,
                command=on_select, **radio_style).grid(row=1, column=2, pady=5)
    
    
    rectangular_gate_damper_img = resources.load_image("rectangular_gate_damper.png",
                                        size=(300, 200))
    rectangular_gate_damper_img_lbl = Label(middle_frame, image=rectangular_gate_damper_img, bg='gray5')
    rectangular_gate_damper_img_lbl.image = rectangular_gate_damper_img
    rectangular_gate_damper_img_lbl.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="4. Damper compuerta circular",
                variable=app_state.selected_damper, value=4,
                command=on_select, **radio_style).grid(row=1, column=3, pady=5)
    
    
    round_gate_damper_img = resources.load_image("round_gate_damper.png",
                                    size=(300, 200))
    round_gate_damper_img_lbl = Label(middle_frame, image=round_gate_damper_img, bg='gray5')
    round_gate_damper_img_lbl.image = round_gate_damper_img
    round_gate_damper_img_lbl.grid(row=0, column=3, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="5. Damper recangular de aspas en paralelo",
                variable=app_state.selected_damper, value=5,
                command=on_select, **radio_style).grid(row=3, column=0, pady=5)
    
    
    rectangular_parallel_blades_damper_img = resources.load_image("rectangular_parallel_blades_damper.png",
                                                size=(300, 200))
    rectangular_parallel_blades_damper_img_lbl = Label(middle_frame, image=rectangular_parallel_blades_damper_img, 
                                                    bg='gray5')
    rectangular_parallel_blades_damper_img_lbl.image = rectangular_parallel_blades_damper_img
    rectangular_parallel_blades_damper_img_lbl.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="6. Damper rectangular de aspas opuestas",
                variable=app_state.selected_damper, value=6,
                command=on_select, **radio_style).grid(row=3, column=1, pady=5)
    
    rectangular_oppo_blades_damper_img = resources.load_image("rectangular_oppo_blades_damper.png",
                                                size=(300, 200))
    rectangular_oppo_blades_damper_img_lbl = Label(middle_frame, image=rectangular_oppo_blades_damper_img, 
                                                    bg='gray5')
    rectangular_oppo_blades_damper_img_lbl.image = rectangular_oppo_blades_damper_img
    rectangular_oppo_blades_damper_img_lbl.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")
    
    
    
    Radiobutton(middle_frame, text="7. Damper circular y rectangular de malla",
                variable=app_state.selected_damper, value=7,
                command=on_select, **radio_style).grid(row=3, column=2, pady=5)
    
    
    round_and_rectangular_screen_damper_img = resources.load_image("round_and_rectangular_screen_damper.png",
                                                size=(300, 200))
    round_and_rectangular_screen_damper_img_lbl = Label(middle_frame, 
                                                    image=round_and_rectangular_screen_damper_img,
                                                    bg='gray5')
    round_and_rectangular_screen_damper_img_lbl.image = round_and_rectangular_screen_damper_img
    round_and_rectangular_screen_damper_img_lbl.grid(row=2, column=2, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="8. Damper circular y rectangular perforado",
                variable=app_state.selected_damper, value=8,
                command=on_select, **radio_style).grid(row=3, column=3, pady=5)
    
    
    thick_perforated_damper_img = resources.load_image("thick_perforated_damper.png",
                                        size=(300, 200))
    thick_perforated_damper_img_lbl = Label(middle_frame, image=thick_perforated_damper_img, bg='gray5')
    thick_perforated_damper_img_lbl.image = thick_perforated_damper_img
    thick_perforated_damper_img_lbl.grid(row=2, column=3, padx=20, pady=10, sticky="nsew")
    
    
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