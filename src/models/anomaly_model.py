import pandas as pd
from sklearn.ensemble import IsolationForest


def train_anomaly_model(df: pd.DataFrame):
    df = df.copy()

    # Ensure required columns exist
    if "amount" not in df.columns or "category" not in df.columns:
        raise ValueError("DataFrame must contain 'amount' and 'category' columns")

    # Clean amount
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"])

    # Encode category safely
    df["category"] = df["category"].fillna("Unknown")
    df["category_encoded"] = df["category"].astype("category").cat.codes

    # Feature set
    X = df[["amount", "category_encoded"]]

    # Train model
    model = IsolationForest(
        n_estimators=100,
        contamination=0.1,
        random_state=42
    )
    model.fit(X)

    print("Anomaly model trained successfully")

    return model, df


def predict_anomalies(model, df: pd.DataFrame):
    df = df.copy()

    if "category_encoded" not in df.columns:
        df["category_encoded"] = df["category"].astype("category").cat.codes

    X = df[["amount", "category_encoded"]]

    preds = model.predict(X)

    # Convert: 1 → 0 (normal), -1 → 1 (anomaly)
    df["anomaly"] = pd.Series(preds).map({1: 0, -1: 1})

    return df
