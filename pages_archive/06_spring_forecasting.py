"""
Module 6 — Spring Discharge Analysis & Trend Forecasting
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.data_loader import load_discharge_data, load_springs_data
from ml.forecasting import analyze_discharge_trend
from utils.config import DEMO_DATA_DISCLAIMER

st.set_page_config(page_title="Spring Forecasting | SPRING-AI", layout="wide")

st.title("📈 Module 6 — Spring Discharge & Rainfall Forecasting")
st.caption("Historical rainfall vs discharge correlation, seasonal trend analysis, and 6-month predictive flow extrapolation.")

st.warning(f"⚠️ {DEMO_DATA_DISCLAIMER}")

df_discharge = load_discharge_data()
df_springs = load_springs_data()

selected_spring_id = st.selectbox(
    "Select Spring to Analyze & Forecast:",
    options=df_springs["spring_id"] + " — " + df_springs["spring_name"]
)
sp_id = selected_spring_id.split(" — ")[0]

res = analyze_discharge_trend(df_discharge, sp_id)

if res is None:
    st.warning("⚠️ Time-series discharge data unavailable for this spring. Please select another spring.")
else:
    # Summary Metrics
    f1, f2, f3, f4, f5 = st.columns(5)
    f1.metric("Mean Discharge", f"{res['mean_discharge']} LPM")
    f2.metric("Peak Monsoon Flow", f"{res['max_discharge']} LPM")
    f3.metric("Lean Summer Flow", f"{res['min_discharge']} LPM")
    f4.metric("Rainfall Correlation", f"{res['rainfall_correlation']}", help="Pearson correlation (0 to 1)")
    f5.metric("Long-Term Trend", f"{res['trend_status']}")

    st.markdown("---")

    # Time Series Chart with 6-Month Forecast
    st.subheader("📉 36-Month Historical Flow & 6-Month Extrapolated Forecast")
    
    hist_df = res["historical_df"]
    fore_df = res["forecast_df"]

    fig = go.Figure()

    # Historical Discharge Line
    fig.add_trace(go.Scatter(
        x=hist_df["date"],
        y=hist_df["discharge_lpm"],
        mode="lines+markers",
        name="Historical Discharge (LPM)",
        line=dict(color="#3b82f6", width=2.5)
    ))

    # Forecast Line
    fig.add_trace(go.Scatter(
        x=fore_df["date"],
        y=fore_df["predicted_discharge_lpm"],
        mode="lines+markers",
        name="6-Month Trend Forecast (LPM)",
        line=dict(color="#ef4444", width=2.5, dash="dash")
    ))

    # Rainfall Bar Chart Overlay
    fig.add_trace(go.Bar(
        x=hist_df["date"],
        y=hist_df["rainfall_mm"] / 10,
        name="Rainfall (cm)",
        marker_color="rgba(16, 185, 129, 0.3)"
    ))

    fig.update_layout(
        title=f"Discharge Hydrograph & Forecast for {sp_id}",
        xaxis_title="Date",
        yaxis_title="Discharge (LPM) / Rainfall (cm)",
        legend=dict(x=0.01, y=0.99),
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info(
        "ℹ️ **Forecast Disclaimer**: Trend extrapolation assumes historical rainfall patterns persist. "
        "Forecast uncertainty increases with longer prediction horizons."
    )
