"""
Module 5 — Environmental & Landslide Risk Analysis Engine
"""

import streamlit as st
import plotly.express as px
from utils.data_loader import load_environmental_grid, load_interventions_data
from gis.mapping import create_spring_gis_map, render_gis_map
from utils.config import DEMO_DATA_DISCLAIMER

st.set_page_config(page_title="Risk Analysis | SPRING-AI", layout="wide")

st.title("⚠️ Module 5 — Environmental & Landslide Risk Analysis")
st.caption("Identification of high-slope landslide hazard zones, unstable rock formations, and unsuitable recharge locations.")

st.warning(f"⚠️ {DEMO_DATA_DISCLAIMER}")

df_grid = load_environmental_grid()
df_int = load_interventions_data()

st.markdown("""
> [!CAUTION]
> **Safety First Protocol**: Artificial groundwater recharge interventions (e.g. heavy percolation tanks or unlined trenches) on slopes exceeding 30°–35° can increase pore water pressure and trigger catastrophic slope collapse or soil creep. The system automatically masks and flags high-risk locations.
""")

# Risk Breakdown Metrics
r1, r2, r3, r4 = st.columns(4)
high_slope_count = len(df_grid[df_grid["slope"] > 30])
mod_slope_count = len(df_grid[(df_grid["slope"] >= 20) & (df_grid["slope"] <= 30)])
safe_slope_count = len(df_grid[df_grid["slope"] < 20])
flagged_interventions = len(df_int[df_int["risk_status"] == "High"])

with r1:
    st.metric("Landslide Hazard Zones (Slope > 30°)", f"{high_slope_count}", "CRITICAL RISK", delta_color="inverse")
with r2:
    st.metric("Moderate Slope Zones (20°-30°)", f"{mod_slope_count}", "REQUIRES BIO-ENGINEERING")
with r3:
    st.metric("Low Slope Zones (< 20°)", f"{safe_slope_count}", "SAFE FOR STRUCTURES")
with r4:
    st.metric("High-Risk Candidate Sites", f"{flagged_interventions}", "FLAGGED IN PLANNER", delta_color="inverse")

st.markdown("---")

c_map, c_chart = st.columns([2, 1])

with c_map:
    st.subheader("🗺️ Spatial Risk Mask Overlay")
    st.caption("Red markers denote grid areas with steep terrain (>30°) where structural recharge intervention is prohibited.")
    
    m_risk = create_spring_gis_map(
        df_grid=df_grid,
        show_heatmap=False
    )
    render_gis_map(m_risk, height=450)

with c_chart:
    st.subheader("📉 Terrain Slope Distribution")
    fig_slope = px.histogram(
        df_grid,
        x="slope",
        nbins=25,
        title="Grid Cell Slope Angle Count",
        labels={"slope": "Slope Angle (°)", "count": "Grid Cells"},
        color_discrete_sequence=["#ef4444"]
    )
    fig_slope.add_vline(x=30, line_dash="dash", line_color="red", annotation_text="Danger Threshold (>30°)")
    st.plotly_chart(fig_slope, use_container_width=True)

st.markdown("---")

# Flagged High Risk Sites Table
st.subheader("🚫 Unsuitable / High-Risk Locations Table")
st.caption("Locations marked 'INSUFFICIENT DATA' or 'CRITICAL LANDSLIDE RISK' require mandatory hydrogeological ground verification.")

high_risk_df = df_grid[df_grid["slope"] > 30][["location_id", "latitude", "longitude", "elevation", "slope", "rainfall"]].head(20)
high_risk_df["Risk Category"] = "HIGH LANDSLIDE HAZARD"
high_risk_df["Recommended Action"] = "Prohibit Water Accumulation — Bio-Stabilisation Only"

st.dataframe(high_risk_df, use_container_width=True, hide_index=True)
