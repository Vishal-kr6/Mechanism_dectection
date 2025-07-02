import numpy as np
from mechanisms.ohmic import is_ohmic
from mechanisms.sclc import is_sclc
from mechanisms.schottky import is_schottky
from mechanisms.poole_frenkel import is_poole_frenkel
from mechanisms.fowler_nordheim import is_fn_tunneling
from mechanisms.direct_tunneling import is_direct_tunneling

def classify_mechanism(logV, logI, V, I):
    # Ohmic
    found, slope, r2 = is_ohmic(logV, logI)
    if found:
        return "Ohmic", slope, r2
    # SCLC
    found, slope, r2 = is_sclc(logV, logI)
    if found:
        return "SCLC", slope, r2
    # Schottky
    found, slope, r2 = is_schottky(V, I)
    if found:
        return "Schottky or Poole-Frenkel", slope, r2
    # FN
    found, slope, r2 = is_fn_tunneling(V, I)
    if found:
        return "Fowler-Nordheim Tunneling", slope, r2
    # Direct tunneling
    found, slope, r2 = is_direct_tunneling(V, I)
    if found:
        return "Direct Tunneling", slope, r2
    return "Unknown or Mixed Mechanism", None, None