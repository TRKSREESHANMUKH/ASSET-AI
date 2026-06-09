import pandas as pd
from sklearn.linear_model import LinearRegression


def train_forecast_model(df: pd.DataFrame):
    df = df.copy()

    # Features
    X = df[[
    "prev_month_spend",
    "rolling_avg_3",
    "growth",
    "transaction_count"
]]

    # Target
    y = df["total_spend"]

    model = LinearRegression()
    model.fit(X, y)

    print("Forecast model trained")

    return model
