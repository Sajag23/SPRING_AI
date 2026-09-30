"""
Spring Discharge Time-Series Analysis & Forecasting Module
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def analyze_discharge_trend(df_discharge, spring_id):
    """
    Analyzes historical discharge for a specific spring and builds a short-term trend forecast.
    """
    sub_df = df_discharge[df_discharge["spring_id"] == spring_id].sort_values("date").copy()
    if sub_df.empty:
        return None

    sub_df["date"] = pd.to_datetime(sub_df["date"])
    sub_df["time_idx"] = np.arange(len(sub_df))

    # Basic stats
    mean_discharge = sub_df["discharge_lpm"].mean()
    max_discharge = sub_df["discharge_lpm"].max()
    min_discharge = sub_df["discharge_lpm"].min()
    
    # Rainfall correlation
    corr = sub_df["rainfall_mm"].corr(sub_df["discharge_lpm"])

    # Trend fitting
    X = sub_df[["time_idx"]]
    y = sub_df["discharge_lpm"]
    model = LinearRegression()
    model.fit(X, y)
    slope = model.coef_[0]

    trend_status = "Declining" if slope < -0.15 else ("Increasing" if slope > 0.15 else "Stable")

    # Forecast next 6 months
    future_time = np.arange(len(sub_df), len(sub_df) + 6).reshape(-1, 1)
    future_preds = model.predict(future_time)
    future_preds = np.maximum(future_preds, 0.5) # Non-negative flow

    last_date = sub_df["date"].max()
    future_dates = pd.date_range(start=last_date + pd.Timedelta(days=30), periods=6, freq="ME")

    forecast_df = pd.DataFrame({
        "date": future_dates.strftime("%Y-%m-%d"),
        "predicted_discharge_lpm": np.round(future_preds, 2),
        "confidence_level": "Medium (Linear Extrapolation)"
    })

    return {
        "spring_id": spring_id,
        "mean_discharge": round(float(mean_discharge), 2),
        "max_discharge": round(float(max_discharge), 2),
        "min_discharge": round(float(min_discharge), 2),
        "rainfall_correlation": round(float(corr), 3),
        "trend_status": trend_status,
        "slope": round(float(slope), 4),
        "historical_df": sub_df,
        "forecast_df": forecast_df
    }
