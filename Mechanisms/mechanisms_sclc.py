import numpy as np

def is_sclc(logV, logI, tol=0.2, r2_th=0.98):
    coeffs = np.polyfit(logV, logI, 1)
    slope = coeffs[0]
    pred = np.polyval(coeffs, logV)
    r2 = 1 - np.sum((logI - pred) ** 2) / np.sum((logI - np.mean(logI)) ** 2)
    if abs(slope - 2) < tol and r2 > r2_th:
        return True, slope, r2
    return False, slope, r2
