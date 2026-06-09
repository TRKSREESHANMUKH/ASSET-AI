
def financial_health_score(
    volatility,
    drift,
    risk,
    anomaly_rate
):

    score = 100

    score -= volatility * 20
    score -= drift * 15
    score -= risk * 10
    score -= anomaly_rate * 5

    score = max(0, min(100, score))

    return round(score, 2)
