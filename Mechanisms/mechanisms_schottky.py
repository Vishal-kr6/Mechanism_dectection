import numpy as np

def is_schottky(V, I, r2_th=0.98):
    X = np.sqrt(V)
    Y = np.log(I / V)
    coeffs = np.polyfit(X, Y, 1)
    pred = np.polyval(coeffs, X)
    r2 = 1 - np.sum((Y - pred) ** 2) / np.sum((Y - np.mean(Y)) ** 2)
    if r2 > r2_th:
        return True, coeffs[0], r2
    return False, coeffs[0], r2
