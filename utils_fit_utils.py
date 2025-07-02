import numpy as np

def linear_fit(X, Y):
    coeffs = np.polyfit(X, Y, 1)
    pred = np.polyval(coeffs, X)
    r2 = 1 - np.sum((Y - pred) ** 2) / np.sum((Y - np.mean(Y)) ** 2)
    return coeffs, r2