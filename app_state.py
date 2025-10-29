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
        self.diameter = None
        self.S = None

app_state = AppState()