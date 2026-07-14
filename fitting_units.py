# fitting_units.py
# ---------------------------------------------------------------------------
# Unit handling shared by every fitting specs menu.
#
# The loss coefficient Co is dimensionless (the table functions take pure
# ratios), so the ONLY quantity that carries units in a fitting calculation is
# velocity, plus the pressure unit of the result. Density lives in app_state
# (kg/m3 in SI, lb/ft3 in imperial), set by pre_dim_menu / main.py so it's
# available even when the branches step is skipped.
#
# Strategy: always compute ΔP in Pa. In imperial the user types velocity in fpm
# and density is in lb/ft3, so both are converted to SI before applying the
# standard dynamic-pressure formula. The stored value is therefore ALWAYS Pa,
# which is exactly what accesories_menu's PDF and the results screen assume
# (they convert Pa -> inH2O for display). On-screen display here follows the
# same rule, so screen and PDF always agree.
#
# Reynolds number (INDEPENDENT fitting path):
#   Some fittings (rectangular/round elbows) apply a Reynolds correction KRe
#   and read app_state.Re. The branches flow computes Re/viscosity, but the
#   user can skip that flow, leaving app_state.viscosity empty. So the fitting
#   side does NOT depend on app_state.viscosity: compute_Re() derives the air
#   viscosity locally from the (shared, read-only) temperature entry via
#   Sutherland, in Pa·s. Nothing in the branches flow is touched, and no new
#   app_state variable is needed — Re still goes into app_state.Re, which the
#   table files already read and the elbow menu overwrites fresh each time.
# ---------------------------------------------------------------------------

from app_state import app_state

# --- conversion constants ---
FPM_TO_MS     = 0.3048 / 60.0     # feet/min -> m/s      (= 0.00508)
LBFT3_TO_KGM3 = 16.018463         # lb/ft3   -> kg/m3
PA_TO_INWG    = 0.00401463        # Pa       -> inH2O  (matches accesories_menu PDF)
IN_TO_M       = 0.0254            # inches   -> meters  (imperial duct dimensions)

# --- Sutherland constants for air (dynamic viscosity in Pa·s) ---
_MU_0 = 1.716e-5   # μ de referencia en Pa·s
_T_0  = 273.15     # temperatura de referencia en K
_SU   = 111.0      # constante de Sutherland en K


def _as_float(value, name="valor"):
    """
    Resuelve un número que puede venir como float/int normal o como variable
    de tkinter (StringVar/DoubleVar/IntVar). Lanza un error claro si falta.
    """
    if hasattr(value, "get"):          # variable de tkinter
        value = value.get()
    if value is None or value == "":
        raise ValueError(f"{name} no está definido (revisa el paso previo).")
    try:
        return float(value)
    except (TypeError, ValueError):
        raise ValueError(f"{name} no es un número válido: {value!r}")


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


def dim_unit():
    """Length unit for duct dimensions in the current system: 'in' or 'm'."""
    return "in" if _is_imperial() else "m"


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
    rho = _as_float(app_state.rho, "Densidad (ρ)")
    if _is_imperial():
        V_ms   = V_typed * FPM_TO_MS
        rho_si = rho * LBFT3_TO_KGM3
    else:
        V_ms   = V_typed
        rho_si = rho
    return Co * rho_si * (V_ms ** 2) / 2.0


def hydraulic_diameter_rect(H, W):
    """
    Hydraulic diameter of a rectangular duct: Dh = 2·H·W / (H + W).
    H and W must share the same length unit; the result comes out in that
    same unit (units are handled later by compute_Re).
    """
    if (H + W) == 0:
        raise ValueError("Dimensiones de ducto inválidas (H + W = 0).")
    return 2.0 * H * W / (H + W)


def _air_viscosity_pas():
    """
    Viscosidad dinámica del aire (μ) en Pa·s — calculada de forma INDEPENDIENTE
    para los fittings, a partir de la temperatura que el usuario ya ingresó.

    - Solo LEE la temperatura compartida (una entrada, no un cálculo), así que
      no se puede "romper" aunque se omitan los ramales.
    - NO usa app_state.viscosity ni toca el flujo de branches.
    - La viscosidad del aire depende solo de la temperatura (no de la presión/
      altitud), por eso basta Sutherland con T en Kelvin.

    >>> VERIFICAR 2 COSAS <<<
      1) app_state.get_temp debe ser el campo con la temperatura. Si en tu
         código se llama distinto, cambia SOLO esta línea.
      2) Unidad de la temperatura: se asume °C en SI y °F en imperial.
         Si tu entrada usa otra unidad, ajusta la conversión a Kelvin abajo.
    """
    T_typed = _as_float(app_state.get_temp, "Temperatura")

    if _is_imperial():
        T_K = (T_typed - 32.0) * 5.0 / 9.0 + 273.15   # °F -> K
    else:
        T_K = T_typed + 273.15                         # °C -> K

    if T_K <= 0:
        raise ValueError(f"Temperatura inválida: {T_typed}° -> {T_K:.1f} K")

    return _MU_0 * (T_K / _T_0) ** 1.5 * (_T_0 + _SU) / (T_K + _SU)


def compute_Re(V_typed, Dh_typed):
    """
    Reynolds number  Re = rho · V · Dh / mu   (dimensionless).

    Converts the typed velocity and hydraulic diameter to SI first:
      SI (1,2):  V in m/s,  Dh in m
      Imperial:  V in fpm,  Dh in in   -> converted to m/s and m
    Density (rho) comes from app_state (kg/m3 SI, lb/ft3 imperial).
    Viscosity (mu) is computed locally in Pa·s (see _air_viscosity_pas),
    independent of the branches flow.
    """
    rho = _as_float(app_state.rho, "Densidad (ρ)")
    mu  = _air_viscosity_pas()          # Pa·s, independiente de branches

    if mu <= 0:
        raise ValueError("Viscosidad (μ) debe ser mayor que cero.")

    if _is_imperial():
        V_ms   = V_typed * FPM_TO_MS
        rho_si = rho * LBFT3_TO_KGM3
        Dh_m   = Dh_typed * IN_TO_M
    else:
        V_ms   = V_typed
        rho_si = rho
        Dh_m   = Dh_typed

    return rho_si * V_ms * Dh_m / mu


def format_delta_p(delta_p_pa, prefix="ΔP"):
    """Display string for a stored Pa value, converted per unit system."""
    if _is_imperial():
        return f"{prefix} = {delta_p_pa * PA_TO_INWG:.6f} inH₂O"
    return f"{prefix} = {delta_p_pa:.4f} Pa"