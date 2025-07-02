import pandas as pd

def load_iv_data(filepath):
    df = pd.read_csv(filepath)
    V = df["V"].values
    I = df["I"].values
    return V, I
