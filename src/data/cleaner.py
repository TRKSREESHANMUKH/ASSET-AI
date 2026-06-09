import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Convert Date
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])

    # Filter expenses only
    df = df[df["type"] == "EXPENSE"]

    # Drop unnecessary columns
    cols_to_drop = [
        "transfer-amount", "transfer-currency",
        "to-account", "receive-amount",
        "receive-currency", "due-date", "id"
    ]
    df = df.drop(columns=cols_to_drop, errors="ignore")

    # Fix category
    df["category"] = df["category"].fillna("Unknown")

    # Fix amount
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"])

    print(" Data cleaned")

    return df
