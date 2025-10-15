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
from menus.results_menu import results_menu

def main():
    # Create the single root window
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

    # Define navigation
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
        velocity_entry_menu(W, go_back=go_to_velocity_range, go_next=go_to_results )
    
    def go_to_results(W):
        results_menu(W, go_back=go_to_velocity_entry)

    # Start with Start Menu
    go_to_start(W)

    # Run Tkinter loop
    W.mainloop()


if __name__ == "__main__":
    main()