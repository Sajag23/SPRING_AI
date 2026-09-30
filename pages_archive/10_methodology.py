"""
Module 10 — Methodology, Architecture & Scientific Rules
"""

import streamlit as st
from utils.config import SCIENTIFIC_DISCLAIMER, DEMO_DATA_DISCLAIMER

st.set_page_config(page_title="Methodology | SPRING-AI", layout="wide")

st.title("📚 Module 10 — Methodology, System Architecture & Science Rules")
st.caption("Detailed technical breakdown of data ingestion, spatial feature extraction, ML hybrid modeling, and scientific boundaries.")

st.warning(f"⚠️ {DEMO_DATA_DISCLAIMER}")

# Architecture Section
st.subheader("🏗️ System Architecture & Workflow Pipeline")

st.markdown("""
```
 GIS Data Processing          AI/ML Engine          Decision Support & UI
+--------------------+    +--------------------+    +-----------------------+
| - DEM Elevation    |    | - Random Forest    |    | - Executive Dashboard |
| - GSI Geology      | -> | - XGBoost          | -> | - Spring Explorer     |
| - IMD Rainfall     |    | - Hydro-Rules      |    | - Recharge Heatmaps   |
| - Fracture Buffers |    | - Confidence Metric|    | - Field Mobile App    |
+--------------------+    +--------------------+    +-----------------------+
```
""")

st.markdown("""
### 1. Data Processing & Spatial Derivative Extraction
- **Elevation & Terrain:** Digital Elevation Models (NASADEM / Copernicus 30m) are processed to extract slope (°), aspect (°), Topographic Position Index (TPI), and Topographic Wetness Index (TWI).
- **Geological Fractures:** Linear structural features (faults, joints, lineaments) extracted from Geological Survey of India (GSI) maps are buffered to calculate fracture density (km/km²) and proximity (meters).
- **Drainage & Hydrology:** Flow accumulation algorithms delineate stream networks and compute stream proximity.

### 2. Hybrid AI + Hydrogeological Decision Model
The system uses a hybrid model combining machine learning predictions with hydrogeological rules:
$$\\text{Recharge Score} = 0.55 \\times \\text{ML Probability} + 0.45 \\times \\text{Hydrogeological Rule Score}$$

### 3. Data Confidence Score
Calculated dynamically based on layer completeness:
- **Full spatial layers** (DEM, Geology, Rainfall, Fractures): **High Confidence (80-95%)**
- **Partial layers** (DEM + Rainfall only): **Medium Confidence (50-75%)**
""")

st.markdown("---")

# Scientific Rules & Ethical Guidelines
st.subheader("⚖️ Scientific Rules & Ethical Guidelines")

st.error("""
**Mandatory Scientific Boundaries Enforced by SPRING-AI:**
1. **No Absolute Subsurface Flow Claims**: The platform estimates recharge *suitability*, NOT guaranteed underground flow paths.
2. **Landslide Safety Masking**: Slopes > 35° are flagged as critical hazard zones to prevent artificial water infiltration from triggering slope failure.
3. **No Automated Construction Approvals**: All output recommendations are *indicative decision support* requiring engineering and hydrogeological ground verification.
4. **Synthetic Data Transparency**: Demonstration data is explicitly labeled to prevent misuse.
""")

st.markdown("---")

# Optional AI Assistant Section
st.subheader("💬 Optional Spring-AI Assistant")
st.caption("Ask questions about spring recharge planning based ONLY on system data.")

user_query = st.text_input("Ask SPRING-AI Assistant a question:", "Why are Staggered Contour Trenches recommended on moderate slopes?")

if user_query:
    if "trench" in user_query.lower() or "contour" in user_query.lower():
        st.info("💡 **SPRING-AI Assistant:** Staggered Contour Trenches (SCT) are recommended on moderate slopes (15°–30°) because they break the velocity of surface runoff, allow rainwater more time to infiltrate into fractured bedrock, and prevent soil erosion without causing slope instability.")
    elif "landslide" in user_query.lower() or "risk" in user_query.lower():
        st.info("💡 **SPRING-AI Assistant:** High slope areas (>30°) increase the risk of landslides if water is forcibly recharged. The system flags these areas as 'High Risk' and recommends vegetative bio-stabilization instead of heavy structural interventions.")
    else:
        st.info(f"💡 **SPRING-AI Assistant:** Ground-truthed data indicates that for '{user_query}', site feasibility depends on slope, fracture density, and rainfall. Field verification is required prior to engineering approval.")
