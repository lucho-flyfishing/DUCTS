"""
ASHRAE Velocity Ranges for Main Circular Ducts
Based on ASHRAE Handbook – HVAC Applications 2015, Table 8, Section 48
RC(N) mapping:
  Low    = RC 25  (quiet spaces: theaters, bedrooms, libraries)
  Medium = RC 35  (offices, restaurants, general commercial)
  High   = RC 45  (mechanical rooms, warehouses, stores)
"""

# Data: {location: {range_label: max_velocity_m/s}}
ASHRAE_MAIN_CIRCULAR = {
    "In shaft / above drywall ceiling": {
        "Low  (RC 25)":    12.7,
        "Medium (RC 35)":  17.8,
        "High (RC 45)":    25.4,
    },
    "Above suspended acoustic ceiling": {
        "Low  (RC 25)":    10.2,
        "Medium (RC 35)":  15.2,
        "High (RC 45)":    22.9,
    },
    "Duct within occupied space": {
        "Low  (RC 25)":     8.6,
        "Medium (RC 35)":  13.2,
        "High (RC 45)":    19.8,
    },
}

def print_chart():
    col_loc   = 36
    col_range = 18
    col_vel   = 14

    header_loc   = "Installation Location"
    header_range = "Speed Range"
    header_vel   = "Max Velocity (m/s)"

    divider = "=" * (col_loc + col_range + col_vel + 4)
    row_sep = "-" * (col_loc + col_range + col_vel + 4)

    print()
    print(divider)
    print("  ASHRAE — MAX AIRFLOW VELOCITIES | MAIN CIRCULAR DUCT")
    print(divider)
    print(f"  {'Installation Location':<{col_loc}} {'Speed Range':<{col_range}} {'Max Velocity (m/s)':>{col_vel}}")
    print(row_sep)

    for location, ranges in ASHRAE_MAIN_CIRCULAR.items():
        first = True
        for range_label, max_vel in ranges.items():
            loc_str = location if first else ""
            print(f"  {loc_str:<{col_loc}} {range_label:<{col_range}} {max_vel:>{col_vel}.1f}")
            first = False
        print(row_sep)

    print()
    print("  Notes:")
    print("  · RC(N) = Room Criteria Noise — acoustic design target for the served space.")
    print("  · Low  (RC 25): theaters, bedrooms, libraries, conference rooms.")
    print("  · Medium (RC 35): private offices, restaurants, general commercial.")
    print("  · High (RC 45): stores, cafeterias, industrial, mechanical rooms.")
    print("  · Values are maximum ceilings. Equal-friction velocity must stay below these.")
    print("  · Branch ducts: use ~80% of the main duct value for the same location/range.")
    print()
    print(divider)
    print()

if __name__ == "__main__":
    print_chart()