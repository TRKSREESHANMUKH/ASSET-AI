import pandas as pd

# Data
from src.data.cleaner import clean_data
from src.data.transformer import transform_to_monthly

# Features
from src.features.feature_engineering import create_features

# Models
from src.models.forecasting import train_forecast_model
from src.models.risk_model import train_risk_model
from src.models.anomaly_model import (
    train_anomaly_model,
    predict_anomalies
)

# Metrics
from src.metrics.volatility import compute_volatility
from src.metrics.drift import compute_category_drift
from src.metrics.scoring import financial_health_score

# Insights
from src.insights.ai_insight_generator import generate_insight


def run_pipeline(raw_df: pd.DataFrame):

    print("\n==============================")
    print(" AI Expense Intelligence System")
    print("==============================")

    # -----------------------------------
    # CLEANING
    # -----------------------------------
    clean_df = clean_data(raw_df)

    clean_df["Month"] = (
        clean_df["Date"]
        .dt.to_period("M")
        .astype(str)
    )

    print("\n Data cleaned")

    # -----------------------------------
    # TRANSFORMATION
    # -----------------------------------
    monthly_df = transform_to_monthly(clean_df)

    print(" Monthly transformation completed")

    # -----------------------------------
    # FEATURES
    # -----------------------------------
    features_df = create_features(
        monthly_df,
        clean_df
    )

    print(" Features created")

    # -----------------------------------
    # FORECAST MODEL
    # -----------------------------------
    forecast_model = train_forecast_model(features_df)

    print(" Forecast model ready")

    # -----------------------------------
    # RISK MODEL
    # -----------------------------------
    risk_model, risk_df = train_risk_model(features_df)

    print(" Risk model ready")

    # -----------------------------------
    # ANOMALY MODEL
    # -----------------------------------
    anomaly_model, clean_df = train_anomaly_model(clean_df)

    clean_df = predict_anomalies(
        anomaly_model,
        clean_df
    )

    print(" Anomaly detection completed")

    # -----------------------------------
    # METRICS
    # -----------------------------------
    volatility = compute_volatility(features_df)

    drift = compute_category_drift(features_df)

    anomaly_rate = clean_df["anomaly"].mean()

    print(" Behavioral metrics computed")

    # -----------------------------------
    # NEXT MONTH FORECAST
    # -----------------------------------
    last_row = features_df.iloc[-1]

    next_input = pd.DataFrame([{
        "prev_month_spend": last_row["total_spend"],
        "rolling_avg_3": last_row["rolling_avg_3"],
        "growth": last_row["growth"],
        "transaction_count": last_row["transaction_count"]
    }])

    predicted_spend = forecast_model.predict(
        next_input
    )[0]

    # -----------------------------------
    # RISK PREDICTION
    # -----------------------------------
    risk_X = risk_df[[
        "prev_month_spend",
        "rolling_avg_3",
        "growth"
    ]]

    risk_predictions = risk_model.predict(risk_X)

    latest_risk = risk_predictions[-1]

    health_score = financial_health_score(
      volatility,
      drift,
      latest_risk,
      anomaly_rate
    )

    # -----------------------------------
    # INSIGHT GENERATION
    # -----------------------------------
    insight = generate_insight(
        predicted_spend=predicted_spend,
        volatility=volatility,
        drift=drift,
        risk_prediction=latest_risk,
        health_score=health_score
    )

    print(insight)

    print("\n Pipeline execution completed")

    return {
        "clean_df": clean_df,
        "monthly_df": monthly_df,
        "features_df": features_df,
        "forecast_model": forecast_model,
        "risk_model": risk_model,
        "anomaly_model": anomaly_model,
        "volatility": volatility,
        "drift": drift,
        "insight": insight,
        "health_score": health_score,
    }
