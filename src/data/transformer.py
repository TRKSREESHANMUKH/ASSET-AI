import pandas as pd

def transform_to_monthly(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    monthly_total = df.groupby("Month")["amount"].sum().reset_index()
    monthly_total.rename(columns={"amount": "total_spend"}, inplace=True)

    category_pivot = df.pivot_table(
        index="Month",
        columns="category",
        values="amount",
        aggfunc="sum",
        fill_value=0
    ).reset_index()

    monthly_df = pd.merge(monthly_total, category_pivot, on="Month")

    print(" Monthly transformation done")

    return monthly_df
