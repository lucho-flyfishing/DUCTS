# app_state.py
# Stores application-wide state variables (no Tkinter root here!)

class AppState:
    def __init__(self):
        self.filename = None
        self.duct_number = None
        self.main_branch = None
        self.selected_option = None
        self.flowrate_entries = []
        self.length_entries = []
        self.get_alt = None
        self.get_temp = None
        self.velocity = None
        self.viscosity = None
        self.P = None
        self.rho = None
        self.Re = None
        self.epsilon = None
        self.diameter = None
        self.diameters_values = []
        self.S = None
        self.selected_bell = None 
        self.selected_elbow = None
        self.selected_transition = None
        self.selected_junction = None
        self.selected_damper = None
        self.fittings = []
        self.r_bell = None 
        self.D_bell = None  
        self.Co_bell = None 


app_state = AppState()