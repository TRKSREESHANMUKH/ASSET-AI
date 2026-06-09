import pandas as pd
import numpy as np


def compute_category_drift(df: pd.DataFrame):
    df = df.copy()

    # Identify category columns
    exclude_cols = [
        "Month", "total_spend",
        "prev_month_spend", "rolling_avg_3", "growth", "transaction_count","predicted_spend"
    ]

    category_cols = [col for col in df.columns if col not in exclude_cols]

    # Convert to proportions
    df_prop = df[category_cols].div(df["total_spend"], axis=0).fillna(0)

    # Current distribution
    current = df_prop.iloc[-1]

    # Historical average
    historical = df_prop.mean()

    # L1 distance (bounded 0–2)
    drift = np.abs(current - historical).sum()

    # Normalize to 0–1
    normalized_drift = drift / 2

    return normalized_drift
