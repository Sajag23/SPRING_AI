"""
Module 1 — Executive Dashboard
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.data_loader import load_springs_data, load_environmental_grid, load_interventions_data, load_discharge_data
from gis.mapping import create_spring_gis_map, render_gis_map
from utils.config import DEMO_DATA_DISCLAIMER

st.set_page_config(page_title="Executive Dashboard | SPRING-AI", layout="wide")

st.title("📊 Module 1 — Executive Dashboard")
st.caption("Macro-level spring revival KPIs, interactive GIS spatial layers, and hydrogeological health distributions.")

st.warning(f"⚠️ {DEMO_DATA_DISCLAIMER}")

# Load Datasets
df_springs = load_springs_data()
df_grid = load_environmental_grid()
df_int = load_interventions_data()
df_discharge = load_discharge_data()

# KPI Cards Section
kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)

total_springs = len(df_springs)
declining_critical = len(df_springs[df_springs["seasonal_status"].isin(["Declining", "Critical"])])
high_recharge_area = len(df_grid[df_grid["recharge_suitability_target"] == 1])
high_priority_sites = len(df_int[df_int["priority_level"] == "HIGH"])
high_risk_sites = len(df_grid[df_grid["slope"] > 30])
avg_confidence = round(df_springs["confidence_score"].mean() * 100, 1)

with kpi1:
    st.metric("Total Springs", f"{total_springs}", help="Total registered springs in target tribal region")
with kpi2:
    st.metric("Requiring Attention", f"{declining_critical}", delta=f"{declining_critical/total_springs*100:.0f}%", delta_color="inverse")
with kpi3:
    st.metric("High Recharge Zone", f"{high_recharge_area} sq km", help="Grid cells with estimated recharge suitability > 52%")
with kpi4:
    st.metric("High Priority Sites", f"{high_priority_sites}", help="Intervention locations ranked HIGH priority")
with kpi5:
    st.metric("High Risk Zones", f"{high_risk_sites}", help="Areas with slope > 30° prone to landslide hazard")
with kpi6:
    st.metric("Avg Data Confidence", f"{avg_confidence}%", help="Average model/data confidence across region")

st.markdown("---")

# Main Interactive Map & Summary Panel
col_map, col_summary = st.columns([2.2, 1])

with col_map:
    st.subheader("🗺️ Interactive Regional GIS Map")
    st.caption("Toggle layers: Springs, Model Recharge Heatmap, Intervention Sites, and Landslide Risk Zones.")
    
    # Render Folium Map
    gis_map = create_spring_gis_map(
        df_springs=df_springs,
        df_grid=df_grid,
        df_interventions=df_int,
        show_heatmap=True
    )
    render_gis_map(gis_map, height=500)

with col_summary:
    st.subheader("📌 Selected Region Overview")
    st.markdown("**District:** Koraput | **State:** Odisha")
    st.markdown("**Target Population:** ~45,000 Tribal Inhabitants")
    st.markdown("**Primary Aquifer:** Fractured Granite-Gneiss & Weathered Sandstone")
    
    st.markdown("---")
    st.markdown("#### Quick Select Spring")
    selected_id = st.selectbox("Choose Spring to inspect:", df_springs["spring_id"] + " — " + df_springs["spring_name"])
    sp_id = selected_id.split(" — ")[0]
    sp_data = df_springs[df_springs["spring_id"] == sp_id].iloc[0]

    st.info(f"""
    **Spring ID:** {sp_data['spring_id']}  
    **Name:** {sp_data['spring_name']}  
    **Village:** {sp_data['village']}  
    **Discharge:** {sp_data['current_discharge_lpm']} LPM  
    **Health Status:** `{sp_data['seasonal_status']}`  
    **Recharge Probability:** `{sp_data['recharge_probability']*100:.0f}%`  
    **Confidence Level:** `{sp_data['confidence_score']*100:.0f}%`  
    """)

st.markdown("---")

# Analytical Charts Section
st.subheader("📈 Hydrogeological Analytics & Distributions")

c1, c2 = st.columns(2)

with c1:
    fig_health = px.pie(
        df_springs,
        names="seasonal_status",
        title="Spring Seasonal Health Distribution",
        color="seasonal_status",
        color_discrete_map={
            "Healthy": "#10b981",
            "Stable": "#3b82f6",
            "Declining": "#f59e0b",
            "Critical": "#ef4444",
            "Insufficient Data": "#6b7280"
        }
    )
    st.plotly_chart(fig_health, use_container_width=True)

with c2:
    fig_priority = px.bar(
        df_int,
        x="recommended_structure",
        color="priority_level",
        title="Candidate Interventions by Recommended Structure & Priority",
        labels={"recommended_structure": "Structure Type", "count": "Number of Sites"},
        color_discrete_map={"HIGH": "#047857", "MEDIUM": "#f59e0b", "LOW": "#dc2626"}
    )
    st.plotly_chart(fig_priority, use_container_width=True)
