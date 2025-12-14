from tkinter import Button, Label, Frame, Radiobutton
from app_state import app_state
import resources

def transitions_menu(W, go_back):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()
        
        
    top_frame = Frame(W, bg='gray5')
    top_frame.pack(side='top', fill='x')
    
    
    reducers_lbl = Label(top_frame, text='Transiciones', 
                            font=('Arial', 35), bg='gray5', fg='gray60')
    reducers_lbl.pack(side='top', pady=1)
    
    
    middle_frame = Frame(W, bg='gray5')
    middle_frame.pack(expand=True, fill='both')
    
    total_rows = 5  
    total_cols = 3 
    
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
        print("Selected transition:", app_state.selected_transition.get())
        
        
    Radiobutton(middle_frame, text="1. Transición circular",
                variable=app_state.selected_transition, value=1,
                command=on_select, **radio_style).grid(row=1, column=0, pady=5)
    
    
    round_transition_img = resources.load_image("round_transition.png", 
                                    size=(350, 220))  
    round_transition_img_lbl = Label(middle_frame, image=round_transition_img, bg='gray5')
    round_transition_img_lbl.image = round_transition_img  
    round_transition_img_lbl.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="2. Transicion circular reductora", 
                variable=app_state.selected_elbow, value=2,
                command=on_select, **radio_style).grid(row=1, column=1, pady=5)
    
    
    round_reducer_transition_img = resources.load_image("round_reducer_transition.png",
                                    size=(350, 220))
    round_reducer_transition_img_lbl = Label(middle_frame, image=round_reducer_transition_img, bg='gray5')
    round_reducer_transition_img_lbl.image = round_reducer_transition_img
    round_reducer_transition_img_lbl.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="3. Transición circular a rectangular", 
                variable=app_state.selected_transition, value=3,
                command=on_select, **radio_style).grid(row=1, column=2, pady=5)
    
    
    round_rectangular_transition_img = resources.load_image("round_rectangular_transition.png",
                                    size=(350, 220))
    round_rectangular_transition_img_lbl = Label(middle_frame, image=round_rectangular_transition_img, bg='gray5')
    round_rectangular_transition_img_lbl.image = round_rectangular_transition_img
    round_rectangular_transition_img_lbl.grid(row=0, column=2, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="4. Transición rectangular a circular",
                variable=app_state.selected_transition, value=4,
                command=on_select, **radio_style).grid(row=3, column=0, pady=5)
    
    
    rectangular_round_transition_img = resources.load_image("rectangular_round_transition.png",
                                    size=(350, 220))
    rectangular_round_transition_img_lbl = Label(middle_frame, image=rectangular_round_transition_img, bg='gray5')
    rectangular_round_transition_img_lbl.image = rectangular_round_transition_img
    rectangular_round_transition_img_lbl.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="5. Transición rectangular",
                variable=app_state.selected_transition, value=5,
                command=on_select, **radio_style).grid(row=3, column=1, pady=5)
    
    rectangular_transition_img = resources.load_image("rectangular_transition.png",
                                    size=(350, 220))
    rectangular_transition_img_lbl = Label(middle_frame, image=rectangular_transition_img, bg='gray5')
    rectangular_transition_img_lbl.image = rectangular_transition_img
    rectangular_transition_img_lbl.grid(row=2, column=1, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="6. Transición rectangular piramidal",
                variable=app_state.selected_transition, value=6,
                command=on_select, **radio_style).grid(row=3, column=2, pady=5)
    
    
    rectangular_pyramidal_transition_img = resources.load_image("rectangular_pyramidal_transition.png",
                                    size=(350, 220))
    rectangular_pyramidal_transition_img_lbl = Label(middle_frame, image=rectangular_pyramidal_transition_img, bg='gray5')
    rectangular_pyramidal_transition_img_lbl.image = rectangular_pyramidal_transition_img
    rectangular_pyramidal_transition_img_lbl.grid(row=2, column=2, padx=20, pady=10, sticky="nsew")
    
    
    Radiobutton(middle_frame, text="7. Transición rectangular 3 lados",
                variable=app_state.selected_transition, value=7,
                command=on_select, **radio_style).grid(row=5, column=0, pady=5)
    
    
    rectangular_3_sides_transition_img = resources.load_image("rectangular_3_side_transition.png",
                                    size=(350, 220))
    rectangular_3_sides_transition_img_lbl = Label(middle_frame, image=rectangular_3_sides_transition_img, bg='gray5')
    rectangular_3_sides_transition_img_lbl.image = rectangular_3_sides_transition_img
    rectangular_3_sides_transition_img_lbl.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")



    
    

    
    

    

    
    

    
    




    
    
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