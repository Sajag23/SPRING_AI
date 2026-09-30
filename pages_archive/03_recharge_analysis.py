"""
Module 3 — AI Recharge Zone Identification
"""

import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data_loader import load_environmental_grid, load_springs_data
from ml.predict_recharge import RechargePredictor
from gis.mapping import create_spring_gis_map, render_gis_map
from utils.config import DEMO_DATA_DISCLAIMER, SCIENTIFIC_DISCLAIMER

st.set_page_config(page_title="AI Recharge Zone Analysis | SPRING-AI", layout="wide")

st.title("🧠 Module 3 — AI Recharge Zone Identification")
st.caption("Spatial feature extraction, Random Forest / XGBoost recharge suitability estimation, feature importance, and model explainability.")

st.warning(f"⚠️ {DEMO_DATA_DISCLAIMER}")

df_grid = load_environmental_grid()
df_springs = load_springs_data()
predictor = RechargePredictor()

st.markdown("""
> [!NOTE]
> **Model-Estimated Recharge Suitability**: The suitability score (0–100%) represents a probabilistic estimate of groundwater infiltration potential based on integrated terrain, fracture density, rainfall, and geological data. It does NOT represent guaranteed hydrogeological subsurface flow lines.
""")

# Interactive Single Point Inference Playground
st.subheader("🔍 Interactive Spatial Point Predictor & Feature Simulator")

with st.expander("🛠️ Adjust Hydrogeological Parameters to Test ML Prediction", expanded=True):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        elevation = st.slider("Elevation (m)", 400, 1600, 950)
        slope = st.slider("Terrain Slope (°)", 1.0, 45.0, 14.2)
        aspect = st.slider("Aspect (°)", 0, 360, 180)
    with c2:
        rainfall = st.slider("Annual Rainfall (mm)", 800, 2200, 1450)
        drainage_density = st.slider("Drainage Density (km/km²)", 0.2, 5.0, 2.1)
        dist_drainage = st.slider("Distance to Stream (m)", 10, 2000, 350)
    with c3:
        fracture_density = st.slider("Fracture Density (km/km²)", 0.0, 4.0, 2.2)
        dist_fault = st.slider("Distance to Fault Line (m)", 10, 3000, 450)
        soil_perm = st.selectbox("Soil Permeability Index (1-5)", [1, 2, 3, 4, 5], index=3)
    with c4:
        land_use = st.selectbox("Land Use Classification", [0, 1, 2, 3, 4], format_func=lambda x: ["Dense Forest", "Open Forest", "Agricultural", "Barren/Scrub", "Settlement"][x])
        lithology = st.selectbox("Lithology Class", [0, 1, 2, 3, 4], format_func=lambda x: ["Weathered Granite", "Hard Sandstone", "Schist & Gneiss", "Basalt", "Limestone"][x])
        dist_spring = st.slider("Distance to Spring (m)", 50, 4000, 600)

input_sample = {
    "elevation": elevation,
    "slope": slope,
    "aspect": aspect,
    "rainfall": rainfall,
    "drainage_density": drainage_density,
    "distance_to_drainage": dist_drainage,
    "distance_to_spring": dist_spring,
    "fracture_density": fracture_density,
    "distance_to_fault": dist_fault,
    "land_use_code": land_use,
    "soil_permeability": soil_perm,
    "lithology_code": lithology
}

res = predictor.predict_point(input_sample)

# Display Results
res_col1, res_col2, res_col3 = st.columns(3)
with res_col1:
    st.metric(
        "Model-Estimated Recharge Suitability",
        f"{res['model_estimated_recharge_suitability_pct']}%",
        help="Model probability combined with hydrogeological rule factors"
    )
with res_col2:
    st.metric(
        "Data Confidence Score",
        f"{res['data_confidence_pct']}%",
        help="Confidence derived from completeness of spatial input layers"
    )
with res_col3:
    st.metric(
        "ML Model Probability",
        f"{res['ml_model_probability']*100:.1f}%",
        help="Pure Random Forest classifier probability"
    )

# Explainability breakdown
st.markdown("#### 💡 Explainable AI — Contributing Factors")
exp_col1, exp_col2 = st.columns(2)
with exp_col1:
    st.success("**Positive Contributing Factors:**\n\n" + "\n".join([f"✓ {item}" for item in res["explainability"]["Positive Factors"]]))
with exp_col2:
    if res["explainability"]["Negative / Constraint Factors"]:
        st.error("**Negative / Constraint Factors:**\n\n" + "\n".join([f"⚠️ {item}" for item in res["explainability"]["Negative / Constraint Factors"]]))
    else:
        st.info("No major negative terrain or risk constraints identified.")

st.markdown("---")

# Feature Importance Chart
st.subheader("📊 Global Model Feature Importance (Random Forest)")
if predictor.metrics and "feature_importances" in predictor.metrics:
    fi_dict = predictor.metrics["feature_importances"]
    df_fi = pd.DataFrame({"Feature": list(fi_dict.keys()), "Importance": list(fi_dict.values())}).sort_values("Importance", ascending=True)
    
    fig_fi = px.bar(
        df_fi,
        x="Importance",
        y="Feature",
        orientation="h",
        title="Key Spatial Variables Driving Recharge Predictions",
        color="Importance",
        color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig_fi, use_container_width=True)

st.markdown("---")

# GIS Heatmap View
st.subheader("🗺️ Regional Recharge Heatmap & Grid Distribution")
m_heat = create_spring_gis_map(
    df_springs=df_springs,
    df_grid=df_grid,
    show_heatmap=True
)
render_gis_map(m_heat, height=450)
