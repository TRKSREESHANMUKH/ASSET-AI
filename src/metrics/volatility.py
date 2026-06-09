import pandas as pd
import numpy as np


def compute_volatility(df: pd.DataFrame):
    df = df.copy()

    spend = df["total_spend"]

    mean = spend.mean()
    std = spend.std()

    if mean == 0:
        return 0

    # Coefficient of variation
    cv = std / mean

    # Normalize to 0–1 range (soft cap)
    normalized = np.tanh(cv)

    return normalized
