import pandas as pd


def create_features(df: pd.DataFrame, transaction_df: pd.DataFrame):
    df = df.copy()

    # Previous month spend
    df["prev_month_spend"] = df["total_spend"].shift(1)

    # Rolling average
    df["rolling_avg_3"] = (
        df["total_spend"]
        .rolling(window=3)
        .mean()
    )

    # Growth rate
    df["growth"] = df["total_spend"].pct_change()

    # Transaction count per month
    transaction_counts = (
        transaction_df.groupby("Month")
        .size()
        .values
    )

    df["transaction_count"] = transaction_counts

    # Fill missing values
    df = df.fillna(0)

    print("Features created")

    return df
