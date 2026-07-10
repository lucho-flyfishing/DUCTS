from tkinter import Tk, StringVar, IntVar, messagebox
from app_state import app_state

from menus.start_menu import start_menu
from menus.file_name_menu import file_name_menu
from menus.duct_number_menu import duct_number_menu
from menus.units_menu import units_menu
from menus.branch_features_menu import branch_features_menu
from menus.alt_temp_menu import alt_temp_menu
from menus.velocity_entry_menu import velocity_entry_menu
from menus.pre_dim_menu import pre_dim_menu
from menus.corrections_menu import corrections_menu
from menus.accesories_menu import accesories_menu
from menus.roughness_menu import roughness_menu
from menus.rectangular_eq_menu import rectangular_eq_menu
from menus.branches_results_menu import branches_results_menu
from menus.bells_menu import bells_menu
from menus.elbows_menu import elbows_menu
from menus.damper_menu import damper_menu   
from menus.transitions_menu import transitions_menu
from menus.junctions_menu import junctions_menu
from menus.diverging_junctions_menu import diverging_junctions_menu
from menus.bells_specs_menu import bells_specs_menu
from menus.elbows_specs_menu import elbows_specs_menu 
from menus.damper_specs_menu import damper_specs_menu
from menus.junctions_specs_menu import junctions_specs_menu
from menus.diverging_junctions_specs_menu import diverging_junctions_specs_menu
from menus.transitions_specs_menu import transitions_specs_menu
from menus.accesories_results_menu import accesories_results_menu




def main():
    
    W = Tk()
    W.geometry("1200x900")
    W.configure(bg="gray5")
    
    
    # Init app_state variables
    app_state.selected_option = StringVar(W)
    app_state.duct_number = IntVar(W)
    app_state.filename = StringVar(W)
    app_state.main_branch = IntVar(W)
    app_state.selected_option = IntVar(W)
    app_state.get_alt = StringVar(W)
    app_state.get_temp = StringVar(W)
    app_state.velocity = StringVar(W)
    app_state.viscosity = StringVar(W)
    app_state.P = StringVar(W)
    app_state.rho = StringVar(W)
    app_state.Re = StringVar(W)
    app_state.epsilon = StringVar(W)
    app_state.diameter = StringVar(W)
    app_state.S = StringVar(W)
    app_state.aspect_ratio = StringVar(W)
    app_state.selected_bell = IntVar(W)
    app_state.selected_elbow = IntVar(W)
    app_state.selected_transition = IntVar(W)
    app_state.selected_junction = IntVar(W)
    app_state.selected_diverging_junction = IntVar(W)
    app_state.selected_damper = IntVar(W)
    app_state.r_bell = IntVar(W)
    app_state.D_bell = IntVar(W)
    app_state.Co_bell = IntVar(W)

    # --- Track B --- which door was used to reach accesories_menu:
    # 'corrections' (Track A: sizing -> corrections -> accesorios) or
    # 'fittings'    (Track B: start -> Accesorios -> units -> alt_temp -> accesorios).
    # go_to_accesories_menu reads this to choose the correct "Regresar" target.
    app_state.accesories_entry = 'corrections'


    # --- Track B --- compute air density from units + altitude + temperature the
    # SAME way pre_dim_menu does, and store it in app_state.rho. The fittings menus
    # compute delta_p = Co * rho * V^2 / 2, so rho must exist even when the user
    # skips the sizing chain. pre_dim itself is left untouched.
    def compute_density_for_fittings():
        def _read(v):                       # handle StringVar or plain str
            return v.get() if hasattr(v, 'get') else v

        selected = app_state.selected_option.get()
        H_raw = _read(app_state.get_alt)
        T_raw = _read(app_state.get_temp)

        P0 = 101325.0
        factor = 0.0000225577
        exponent = 5.2559

        if selected == 3:
            H_m = float(H_raw) * 0.3048     # ft -> m
        else:
            H_m = float(H_raw)              # already m

        P_pa = P0 * (1 - factor * H_m) ** exponent

        if selected in (1, 2):
            P = round(P_pa, 2)              # Pa
            T_K = float(T_raw) + 273.15     # C -> K
            R = 287.05
            rho = P / (R * T_K)             # kg/m3
        else:  # selected == 3
            P = round(P_pa * 0.0001450377, 2)   # psi
            T_R = float(T_raw) + 459.67         # F -> R
            pressure_lbft2 = P * 144            # psi -> lb/ft2
            R = 53.35
            rho = pressure_lbft2 / (R * T_R)    # lb/ft3

        app_state.rho = rho
        print(f"[Accesorios] Densidad calculada: rho = {rho}")

    
    # navigation
    def go_to_start(W):
        # --- Track B --- the start screen now forks into two tracks
        start_menu(W, go_tramos=go_to_file_name, go_accesorios=go_to_units_fittings)
        
        
    def go_to_file_name(W):
        file_name_menu(W, go_back=go_to_start, go_next=go_to_duct_number)
        
        
    def go_to_duct_number(W):
        duct_number_menu(W, go_back=go_to_file_name, go_next=go_to_units)
        
        
    def go_to_units(W):
        units_menu(W, go_back=go_to_duct_number, go_next=go_to_branch_features)
        
    def go_to_branch_features(W):
        branch_features_menu(W, go_back=go_to_units, go_next=go_to_alt_temp)
        
        
    def go_to_alt_temp(W):
        alt_temp_menu(W, go_back=go_to_branch_features, go_next=go_to_velocity_entry)
    
    
    def go_to_velocity_entry(W):
        velocity_entry_menu(W, go_back=go_to_alt_temp, go_next=go_to_pre_dim )
    
    
    def go_to_pre_dim(W):
        pre_dim_menu(W, go_back=go_to_velocity_entry, go_next=go_to_corrections_menu)
    
    
    def go_to_corrections_menu(W):
        # --- Track B --- accesorios reached from here is the Track A door
        corrections_menu(W, go_back=go_to_pre_dim, go_accesories_menu=go_to_accesories_from_corrections,
                        go_roughness_menu=go_to_roughness_menu, go_rectangular_eq_menu=go_to_rectangular_eq_menu, 
                        go_branches_results_menu=go_to_branches_results_menu)
        
    def go_to_branches_results_menu(W):
        branches_results_menu(W, go_back=go_to_corrections_menu)   
    
    
    def go_to_roughness_menu(W):
        roughness_menu(W, go_back=go_to_corrections_menu, go_next=go_to_pre_dim)
    
    
    def go_to_rectangular_eq_menu(W):
        rectangular_eq_menu(W, go_back=go_to_corrections_menu)


    # --- Track B --- air-conditions front-end (reuses units_menu + alt_temp_menu
    # unchanged; just wired to different next/back targets than Track A)
    def go_to_units_fittings(W):
        units_menu(W, go_back=go_to_start, go_next=go_to_alt_temp_fittings)

    def go_to_alt_temp_fittings(W):
        alt_temp_menu(W, go_back=go_to_units_fittings, go_next=go_to_accesories_from_fittings)

    # --- Track B --- two doors into the same accesories_menu, each stamping the flag
    def go_to_accesories_from_corrections(W):
        app_state.accesories_entry = 'corrections'
        go_to_accesories_menu(W)

    def go_to_accesories_from_fittings(W):
        app_state.accesories_entry = 'fittings'
        try:
            compute_density_for_fittings()      # rho must exist before fittings run
        except (ValueError, TypeError):
            messagebox.showwarning(
                "Datos incompletos",
                "Ingrese una altitud y una temperatura válidas antes de continuar.")
            go_to_alt_temp_fittings(W)          # bounce back instead of crashing
            return
        go_to_accesories_menu(W)
    
    
    def go_to_accesories_menu(W):
        # --- Track B --- pick the "Regresar" target based on how we got here
        if getattr(app_state, 'accesories_entry', 'corrections') == 'fittings':
            back = go_to_alt_temp_fittings      # Track B: back through the air-conditions step
        else:
            back = go_to_corrections_menu       # Track A: back to the corrections hub
        accesories_menu(W, go_back=back, go_bells_menu=go_to_bells_menu,
                        go_elbows_menu=go_to_elbows_menu, go_damper_menu=go_to_damper_menu,
                        go_transitions_menu=go_to_transitions_menu, go_junctions_menu=go_to_junctions_menu, 
                        go_diverging_junctions_menu=go_to_diverging_junctions_menu, 
                        go_results_menu=go_to_results_menu)

    
    def go_to_bells_menu(W):
        bells_menu(W, go_back=go_to_accesories_menu, go_next=go_to_bells_specs_menu)
    
    def go_to_bells_specs_menu(W):
        bells_specs_menu(W, go_back=go_to_bells_menu)
    
    
    def go_to_elbows_menu(W):
        elbows_menu(W, go_back=go_to_accesories_menu, go_next=go_to_elbows_specs_menu)
        
    def go_to_elbows_specs_menu(W):
        elbows_specs_menu(W, go_back=go_to_elbows_menu)
    
    
    def go_to_damper_menu(W):
        damper_menu(W, go_back=go_to_accesories_menu, go_next=go_to_damper_specs_menu)
        
    def go_to_damper_specs_menu(W):
        damper_specs_menu(W, go_back=go_to_damper_menu)
    
    
    def go_to_transitions_menu(W):
        transitions_menu(W, go_back=go_to_accesories_menu, go_next=go_to_transitions_specs_menu)
    
    def go_to_transitions_specs_menu(W):
        transitions_specs_menu(W, go_back=go_to_transitions_menu)
    
    
    def go_to_junctions_menu(W):
        junctions_menu(W, go_back=go_to_accesories_menu, go_next=go_to_junctions_specs_menu)
        
    def go_to_junctions_specs_menu(W):
        junctions_specs_menu(W, go_back=go_to_junctions_menu)
    
    def go_to_diverging_junctions_menu(W):
        diverging_junctions_menu(W, go_back=go_to_accesories_menu, go_next=go_to_diverging_junctions_specs_menu)
        
    def go_to_diverging_junctions_specs_menu(W):
        diverging_junctions_specs_menu(W, go_back=go_to_diverging_junctions_menu)

    def go_to_results_menu(W):
        accesories_results_menu(W, go_back=go_to_accesories_menu)
    
    
    
    
    
    
    go_to_start(W)
    
    
    W.mainloop()
    
    
if __name__ == "__main__":
    main()