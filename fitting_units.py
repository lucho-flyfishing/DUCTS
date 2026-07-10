# fitting_units.py
# ---------------------------------------------------------------------------
# Unit handling shared by every fitting specs menu.
#
# The loss coefficient Co is dimensionless (the table functions take pure
# ratios), so the ONLY quantity that carries units in a fitting calculation is
# velocity, plus the pressure unit of the result. Density lives in app_state
# (kg/m3 in SI, lb/ft3 in imperial), set by pre_dim_menu / the accesorios
# density step.
#
# Strategy: always compute ΔP in Pa. In imperial the user types velocity in fpm
# and density is in lb/ft3, so both are converted to SI before applying the
# standard dynamic-pressure formula. The stored value is therefore ALWAYS Pa,
# which is exactly what accesories_menu's PDF and the results screen assume
# (they convert Pa -> inH2O for display). On-screen display here follows the
# same rule, so screen and PDF always agree.
# ---------------------------------------------------------------------------

from app_state import app_state

# --- conversion constants ---
FPM_TO_MS     = 0.3048 / 60.0     # feet/min -> m/s      (= 0.00508)
LBFT3_TO_KGM3 = 16.018463         # lb/ft3   -> kg/m3
PA_TO_INWG    = 0.00401463        # Pa       -> inH2O  (matches accesories_menu PDF)


def _is_imperial():
    return app_state.selected_option.get() == 3


def vel_unit():
    """Velocity unit string for the current system: 'fpm' or 'm/s'."""
    return "fpm" if _is_imperial() else "m/s"


def rho_unit():
    """Density unit string for the current system."""
    return "lb/ft³" if _is_imperial() else "kg/m³"


def dp_unit():
    """Pressure unit string for the current system."""
    return "inH₂O" if _is_imperial() else "Pa"


def velocity_label(symbol="V", extra=""):
    """
    Ready-made label for a velocity entry.
      velocity_label()                          -> 'V (m/s):'  or 'V (fpm):'
      velocity_label('V_b', 'Velocidad ramal')  -> 'V_b - Velocidad ramal (fpm):'
    """
    prefix = symbol if not extra else f"{symbol} - {extra}"
    return f"{prefix} ({vel_unit()}):"


def compute_delta_p_pa(Co, V_typed):
    """
    ΔP in Pa from a loss coefficient and the velocity the user typed.
      SI (1,2):  V in m/s, rho in kg/m3   -> Pa directly.
      Imperial:  V in fpm, rho in lb/ft3  -> convert both to SI, then Pa.
    Always returns Pa so storage stays consistent for the PDF / results layer.
    """
    rho = app_state.rho
    if _is_imperial():
        V_ms   = V_typed * FPM_TO_MS
        rho_si = rho * LBFT3_TO_KGM3
    else:
        V_ms   = V_typed
        rho_si = rho
    return Co * rho_si * (V_ms ** 2) / 2.0


def format_delta_p(delta_p_pa, prefix="ΔP"):
    """Display string for a stored Pa value, converted per unit system."""
    if _is_imperial():
        return f"{prefix} = {delta_p_pa * PA_TO_INWG:.6f} inH₂O"
    return f"{prefix} = {delta_p_pa:.4f} Pa"