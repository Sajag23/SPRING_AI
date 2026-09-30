"""
Module 2 — Spring Explorer
"""

import streamlit as st
import plotly.express as px
from utils.data_loader import load_springs_data, load_discharge_data
from gis.mapping import create_spring_gis_map, render_gis_map
from utils.config import DEMO_DATA_DISCLAIMER

st.set_page_config(page_title="Spring Explorer | SPRING-AI", layout="wide")

st.title("💧 Module 2 — Spring Explorer")
st.caption("Detailed hydrogeological metadata, seasonal discharge hydrographs, elevation profiles, and health indicators for individual springs.")

st.warning(f"⚠️ {DEMO_DATA_DISCLAIMER}")

df_springs = load_springs_data()
df_discharge = load_discharge_data()

# Search & Filter Controls
col_f1, col_f2, col_f3 = st.columns(3)
with col_f1:
    village_filter = st.multiselect("Filter by Village:", options=df_springs["village"].unique())
with col_f2:
    status_filter = st.multiselect("Filter by Seasonal Health:", options=df_springs["seasonal_status"].unique())
with col_f3:
    spring_search = st.selectbox("Select Spring to Inspect:", options=df_springs["spring_id"] + " — " + df_springs["spring_name"])

# Apply Filters
df_filtered = df_springs.copy()
if village_filter:
    df_filtered = df_filtered[df_filtered["village"].isin(village_filter)]
if status_filter:
    df_filtered = df_filtered[df_filtered["seasonal_status"].isin(status_filter)]

selected_id = spring_search.split(" — ")[0]
spring_info = df_springs[df_springs["spring_id"] == selected_id].iloc[0]

st.markdown("---")

# Main Inspection Header
col_details, col_map = st.columns([1.5, 1.5])

with col_details:
    st.subheader(f"📌 {spring_info['spring_name']} ({spring_info['spring_id']})")
    
    status_color = {
        "Healthy": "🟢",
        "Stable": "🔵",
        "Declining": "🟡",
        "Critical": "🔴",
        "Insufficient Data": "⚪"
    }.get(spring_info["seasonal_status"], "🔵")

    st.markdown(f"### Health Status: {status_color} `{spring_info['seasonal_status']}`")
    st.caption("Basis of Classification: Historical discharge trends, summer dry-period flow, and community reports.")

    m1, m2, m3 = st.columns(3)
    m1.metric("Elevation", f"{spring_info['elevation']} m")
    m2.metric("Discharge (Current)", f"{spring_info['current_discharge_lpm']} LPM")
    m3.metric("Recharge Prob.", f"{spring_info['recharge_probability']*100:.0f}%")

    st.markdown(f"""
    * **Village:** {spring_info['village']}
    * **District:** {spring_info['district']} ({spring_info['state']})
    * **Coordinates:** {spring_info['latitude']}° N, {spring_info['longitude']}° E
    * **Geological Spring Type:** {spring_info['spring_type']}
    * **Model Confidence Score:** {spring_info['confidence_score']*100:.0f}%
    * **Landslide Susceptibility:** `{spring_info['landslide_risk']}`
    """)

with col_map:
    st.subheader("📍 Spring Location & Local Area")
    m = create_spring_gis_map(
        df_springs=df_springs,
        selected_spring_id=selected_id,
        center_coords=[spring_info["latitude"], spring_info["longitude"]],
        zoom_start=13,
        show_heatmap=False
    )
    render_gis_map(m, height=320)

st.markdown("---")

# Time-Series Discharge Chart
st.subheader("📉 Historical Discharge & Monthly Hydrograph")
sp_discharge = df_discharge[df_discharge["spring_id"] == selected_id].sort_values("date")

if not sp_discharge.empty:
    fig_ts = px.line(
        sp_discharge,
        x="date",
        y="discharge_lpm",
        title=f"Monthly Discharge (LPM) for {spring_info['spring_id']} (2023 - 2025)",
        markers=True,
        line_shape="spline",
        labels={"date": "Date", "discharge_lpm": "Discharge (Litres / Min)"}
    )
    fig_ts.add_bar(
        x=sp_discharge["date"],
        y=sp_discharge["rainfall_mm"] / 10, # Scaled rainfall overlay
        name="Rainfall (cm)"
    )
    st.plotly_chart(fig_ts, use_container_width=True)
else:
    st.info("ℹ️ Long-term monthly discharge monitoring data unavailable for this specific spring. Basic discharge field estimates logged.")
