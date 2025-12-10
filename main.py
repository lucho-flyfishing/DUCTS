from tkinter import Tk, StringVar, IntVar
from app_state import app_state

from menus.start_menu import start_menu
from menus.file_name_menu import file_name_menu
from menus.duct_number_menu import duct_number_menu
from menus.units_menu import units_menu
from menus.branch_features_menu import branch_features_menu
from menus.alt_temp_menu import alt_temp_menu
from menus.velocity_range_menu import velocity_range_menu
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
from menus.bells_specs_menu import bells_specs_menu
from menus.elbows_specs_menu import elbows_specs_menu 
from menus.damper_specs_menu import damper_specs_menu




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
    app_state.diameter = StringVar(W)
    app_state.S = StringVar(W)
    app_state.selected_bell = IntVar(W)
    app_state.selected_elbow = IntVar(W)
    app_state.selected_transition = IntVar(W)
    app_state.selected_junction = IntVar(W)
    app_state.selected_damper = IntVar(W)
    app_state.r_bell = IntVar(W)
    app_state.D_bell = IntVar(W)
    app_state.Co_bell = IntVar(W)

    
    
    # navigation
    def go_to_start(W):
        start_menu(W, go_next=go_to_file_name)
        
        
    def go_to_file_name(W):
        file_name_menu(W, go_back=go_to_start, go_next=go_to_duct_number)
        
        
    def go_to_duct_number(W):
        duct_number_menu(W, go_back=go_to_file_name, go_next=go_to_units)
        
        
    def go_to_units(W):
        units_menu(W, go_back=go_to_duct_number, go_next=go_to_branch_features)
        
    def go_to_branch_features(W):
        branch_features_menu(W, go_back=go_to_units, go_next=go_to_alt_temp)
        
        
    def go_to_alt_temp(W):
        alt_temp_menu(W, go_back=go_to_branch_features, go_next=go_to_velocity_range)
    
    
    def go_to_velocity_range(W):
        velocity_range_menu(W, go_back=go_to_alt_temp, go_next=go_to_velocity_entry)
    
    
    def go_to_velocity_entry(W):
        velocity_entry_menu(W, go_back=go_to_velocity_range, go_next=go_to_pre_dim )
    
    
    def go_to_pre_dim(W):
        pre_dim_menu(W, go_back=go_to_velocity_entry, go_next=go_to_corrections_menu)
    
    
    def go_to_corrections_menu(W):
        corrections_menu(W, go_back=go_to_pre_dim, go_accesories_menu=go_to_accesories_menu,
                        go_roughness_menu=go_to_roughness_menu, go_rectangular_eq_menu=go_to_rectangular_eq_menu, 
                        go_branches_results_menu=go_to_branches_results_menu)
        
    def go_to_branches_results_menu(W):
        branches_results_menu(W, go_back=go_to_corrections_menu)   
    
    
    def go_to_roughness_menu(W):
        roughness_menu(W, go_back=go_to_corrections_menu)
    
    
    def go_to_rectangular_eq_menu(W):
        rectangular_eq_menu(W, go_back=go_to_corrections_menu)
    
    
    def go_to_accesories_menu(W):
        accesories_menu(W, go_back=go_to_corrections_menu, go_bells_menu=go_to_bells_menu,
                        go_elbows_menu=go_to_elbows_menu, go_damper_menu=go_to_damper_menu,
                        go_transitions_menu=go_to_transitions_menu, go_junctions_menu=go_to_junctions_menu)
    
    
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
        transitions_menu(W, go_back=go_to_accesories_menu)
    
    
    def go_to_junctions_menu(W):
        junctions_menu(W, go_back=go_to_accesories_menu)
    
    
    
    
    
    
    go_to_start(W)
    
    
    W.mainloop()
    
    
if __name__ == "__main__":
    main()