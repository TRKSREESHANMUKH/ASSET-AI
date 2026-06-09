# A.S.S.E.T

## AI Powered System for Spending Evaluation, Prediction and Trend Analysis

Most expense trackers tell users where their money went.

A.S.S.E.T attempts to answer a more valuable question:

**Where is the money likely to go next?**

A.S.S.E.T is an intelligent financial analytics platform that transforms raw transaction data into actionable insights through expense forecasting, overspending risk assessment, anomaly detection, behavioral analysis, and financial health scoring.

The project combines machine learning, data engineering, and behavioral analytics to help understand not only past spending patterns but also future financial trends.

---

## Why I Built This

While exploring personal finance applications, I noticed that most expense tracking tools focus on recording transactions rather than understanding financial behavior.

I wanted to build a system capable of answering questions such as:

Will I overspend next month?

Are there unusual transactions hidden in my spending history?

How stable are my spending habits?

Is my financial behavior improving or becoming more risky over time?

Can machine learning generate meaningful financial insights automatically?

This project is my attempt to move beyond bookkeeping and build a system that interprets financial behavior.

---

## Core Capabilities

### Expense Forecasting

Predicts future spending using historical expense patterns and engineered behavioral features.

### Risk Assessment

Identifies the probability of overspending based on previous spending behavior.

### Anomaly Detection

Detects unusual transactions using Isolation Forest to identify potential outliers in spending activity.

### Behavioral Analytics

Measures spending volatility and category drift to understand changes in financial habits.

### Financial Health Scoring

Generates a consolidated score based on spending stability, behavioral patterns, anomalies, and overspending risk.

### AI Generated Financial Insights

Automatically produces human readable financial reports with recommendations and observations.

---

## System Architecture

```text
Raw Transactions
        │
        ▼
 Data Cleaning
        │
        ▼
 Monthly Aggregation
        │
        ▼
 Feature Engineering
        │
        ├─────────────► Forecasting Model
        │
        ├─────────────► Risk Prediction Model
        │
        ├─────────────► Anomaly Detection Model
        │
        ▼
 Behavioral Analytics
        │
        ▼
 Financial Health Score
        │
        ▼
 AI Insight Generation
```

---

## Key Results

Forecasted future monthly expenses using machine learning.

Classified overspending risk from historical behavior.

Detected anomalous transactions using Isolation Forest.

Measured spending volatility and category drift.

Generated an overall Financial Health Score.

Produced automated financial insight reports.

---

## Challenges Faced

Handling missing and inconsistent transaction data.

Engineering meaningful behavioral features from raw expenses.

Combining multiple analytical outputs into a single health score.

Ensuring consistency between individual model outputs and pipeline results.

Designing interpretable financial insights rather than only predictive outputs.

---

## What I Learned

End to end machine learning pipeline development.

Feature engineering for financial data.

Forecasting and classification model design.

Anomaly detection using Isolation Forest.

Behavioral analytics and financial metric design.

Modular software architecture for AI projects.

Version control and project management using Git and GitHub.

---

## Future Improvements

Interactive Streamlit dashboard.

Real time transaction monitoring.

Personalized financial recommendations.

Category wise budget optimization.

Multi user support.

Advanced forecasting models.

Explainable AI based recommendations.

---

## Technology Stack

Python

Pandas

NumPy

Scikit-Learn

Matplotlib

Google Colab

Git

GitHub

---

## Repository Structure

```text
ASSET-AI/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── notebooks/
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── metrics/
│   ├── insights/
│   └── pipeline.py
│
├── app/
│   └── streamlit_app.py
│
└── README.md
```

---

## Author

**Thota Ramakrishna Sree Shanmukh**  
Artificial Intelligence and Data Science
