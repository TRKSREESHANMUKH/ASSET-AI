import pandas as pd
from sklearn.linear_model import LogisticRegression


def train_risk_model(df: pd.DataFrame):
    df = df.copy()

    # Create target label
    df["risk"] = (df["total_spend"] > df["rolling_avg_3"]).astype(int)

    # Features
    X = df[["prev_month_spend", "rolling_avg_3", "growth"]]

    # Target
    y = df["risk"]

    model = LogisticRegression()
    model.fit(X, y)

    print(" Risk model trained")

    return model, df
