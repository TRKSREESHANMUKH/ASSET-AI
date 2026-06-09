def generate_insight(
    predicted_spend,
    volatility,
    drift,
    risk_prediction,
    health_score
):
    insight = f"""

================ AI FINANCIAL INSIGHT REPORT ================

 Predicted Next Month Spend
 ------------------------------------------------------------
 ₹ {predicted_spend:.2f}

 Financial Health Score
 ------------------------------------------------------------
 {health_score}/100

"""

    if health_score >= 85:
        grade = "Excellent"
    elif health_score >= 70:
        grade = "Good"
    elif health_score >= 50:
        grade = "Average"
    else:
        grade = "Poor"

    insight += " Grade : " + grade + "\n\n"

    insight += f"""
 Spending Volatility Analysis
 ------------------------------------------------------------
 Volatility Score : {volatility:.3f}
"""

    if volatility < 0.3:
        insight += " Spending pattern is stable.\n"
    elif volatility < 0.6:
        insight += " Spending pattern shows moderate fluctuations.\n"
    else:
        insight += " Spending behavior is highly volatile.\n"

    insight += f"""

 Category Drift Analysis
 ------------------------------------------------------------
 Drift Score : {drift:.3f}
"""

    if drift < 0.2:
        insight += " Spending categories are consistent with past behavior.\n"
    elif drift < 0.5:
        insight += " Spending categories are moderately changing.\n"
    else:
        insight += " Significant shift detected in spending behavior.\n"

    insight += f"""

 Overspending Risk Assessment
 ------------------------------------------------------------
"""

    if risk_prediction == 1:
        insight += " High likelihood of overspending next month.\n"
    else:
        insight += " Overspending risk appears low.\n"

    insight += """

 Recommendation
 ------------------------------------------------------------
 Maintain controlled spending habits and monitor category wise expenses regularly.

==============================================================
"""

    return insight
