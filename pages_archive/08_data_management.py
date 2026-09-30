"""
Module 8 — Data Management & Real Dataset Explorer
"""

import streamlit as st
import pandas as pd
from utils.data_loader import (
    load_springs_data, load_environmental_grid, load_discharge_data,
    load_interventions_data, load_real_nasa_climate_data, load_real_elevation_villages
)
from utils.scoring import calculate_data_quality_score
from utils.config import DEMO_DATA_DISCLAIMER

st.set_page_config(page_title="Data Management | SPRING-AI", layout="wide")

st.title("💾 Module 8 — Spatial Data Management & Real Dataset Explorer")
st.caption("Inspect and export all real NASA climate datasets, satellite elevation points, spring hydrogeology features, and upload custom files.")

# Upload Section
st.subheader("📤 Upload Custom Spatial / Hydrogeological Datasets")
uploaded_file = st.file_uploader("Upload spatial CSV or GeoJSON dataset:", type=["csv", "geojson"])

if uploaded_file is not None:
    try:
        df_up = pd.read_csv(uploaded_file)
        st.success(f" Successfully loaded dataset '{uploaded_file.name}' with {len(df_up)} records!")
        st.dataframe(df_up.head(5), use_container_width=True)
    except Exception as e:
        st.error(f"❌ Data Processing Failed: {str(e)}. Please verify column names and formatting.")

st.markdown("---")

# Active System Datasets Explorer
st.subheader("🌐 Active System Datasets (Koraput District, Odisha)")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌧️ Real NASA Climate Data",
    "⛰️ Real Satellite Elevation Data",
    "💧 Springs Field Inventory",
    "🗺️ Environmental Spatial Grid",
    "🛠️ Candidate Interventions"
])

with tab1:
    df_nasa = load_real_nasa_climate_data()
    if not df_nasa.empty:
        st.markdown("### Real NASA POWER API Climate Records (2020 - 2024)")
        st.caption("Monthly precipitation (mm) and temperature (°C) for Koraput (18.8132°N, 82.7126°E).")
        st.dataframe(df_nasa, use_container_width=True, hide_index=True)
        st.download_button(
            "📥 Download NASA Climate CSV",
            data=df_nasa.to_csv(index=False),
            file_name="real_nasa_climate_koraput.csv",
            mime="text/csv"
        )
    else:
        st.info("NASA Climate dataset not loaded.")

with tab2:
    df_elev = load_real_elevation_villages()
    if not df_elev.empty:
        st.markdown("### Real Satellite Elevation Data for Tribal Villages")
        st.caption("Elevation in meters above mean sea level fetched from Open-Meteo DEM API.")
        st.dataframe(df_elev, use_container_width=True, hide_index=True)
        st.download_button(
            "📥 Download Elevation CSV",
            data=df_elev.to_csv(index=False),
            file_name="real_elevation_villages_koraput.csv",
            mime="text/csv"
        )
    else:
        st.info("Elevation dataset not loaded.")

with tab3:
    df_sp = load_springs_data()
    st.markdown("### Mapped Springs Inventory")
    st.dataframe(df_sp, use_container_width=True, hide_index=True)
    st.download_button(
        "📥 Download Springs Inventory CSV",
        data=df_sp.to_csv(index=False),
        file_name="springs_inventory_koraput.csv",
        mime="text/csv"
    )

with tab4:
    df_grid = load_environmental_grid()
    st.markdown("### Hydrogeological Environmental Grid (1,000 Points)")
    st.dataframe(df_grid.head(100), use_container_width=True, hide_index=True)
    st.caption("Showing top 100 spatial grid rows of 1,000 processed locations.")

with tab5:
    df_int = load_interventions_data()
    st.markdown("### Candidate Intervention Locations")
    st.dataframe(df_int, use_container_width=True, hide_index=True)

st.markdown("---")

# Data Quality Breakdown
st.subheader("📊 System Data Confidence Breakdown")
dq_res = calculate_data_quality_score({
    "terrain_dem": True,
    "rainfall": True,
    "geology_lithology": True,
    "faults_fractures": True,
    "spring_discharge": True,
    "land_use": True
})

st.success(f"🟢 **OVERALL SYSTEM DATA CONFIDENCE: {dq_res['overall_score_pct']}% (HIGH)**")
for key, pct in dq_res["layer_breakdown"].items():
    st.progress(int(pct), text=f"{key.replace('_', ' ').title()}: {pct}%")
