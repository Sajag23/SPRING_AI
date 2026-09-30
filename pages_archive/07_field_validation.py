"""
Module 7 — Field Validation & Observation Logger
"""

import streamlit as st
import datetime
from utils.data_loader import load_interventions_data, load_springs_data, load_field_validations_data, save_field_validation
from utils.config import DEMO_DATA_DISCLAIMER

st.set_page_config(page_title="Field Validation | SPRING-AI", layout="wide")

st.title("📋 Module 7 — Field Validation & Ground-Truthing")
st.caption("Offline-capable observation logging for Jal Sais, hydrogeologists, and field engineers to verify AI recommendations.")

st.warning(f"⚠️ {DEMO_DATA_DISCLAIMER}")

df_int = load_interventions_data()
df_springs = load_springs_data()
df_validations = load_field_validations_data()

# Form Submission Section
st.subheader("📝 Submit New Field Verification Entry")

with st.form("field_validation_form"):
    c1, c2, c3 = st.columns(3)
    with c1:
        site_id = st.selectbox("Select Candidate Site ID:", df_int["site_id"])
        observer_name = st.text_input("Observer Name / Role:", "Ramesh Kumar (Jal Sai)")
        date_val = st.date_input("Verification Date:", datetime.date.today())
    with c2:
        observed_slope = st.number_input("Field Observed Slope (°):", 0.0, 60.0, 14.5)
        observed_geology = st.selectbox("Observed Lithology / Rock Type:", ["Fractured Granite", "Weathered Sandstone", "Hard Schist", "Massive Basalt", "Other"])
        observed_soil = st.selectbox("Observed Soil Type:", ["Permeable Gravelly Loam", "Stony Sandy Clay", "Dense Unweathered Clay", "Deep Alluvium"])
    with c3:
        existing_struct = st.text_input("Existing Water Structure (if any):", "None")
        validation_status = st.selectbox("Field Feasibility Status:", ["Suitable", "Not Suitable", "Needs Review"])
        photo_upload = st.file_uploader("Upload Geotagged Site Photo (Optional):", type=["jpg", "png"])

    notes = st.text_area("Field Hydrogeological Observations & Local Notes:", "Site has excellent catchment topography with visible fracture orientation feeding the lower spring.")

    submitted = st.form_submit_button("💾 Submit Field Validation Entry")

    if submitted:
        spring_id = df_int[df_int["site_id"] == site_id]["nearest_spring_id"].iloc[0]
        val_id = f"VAL-{len(df_validations) + 1:03d}"
        
        new_record = {
            "validation_id": val_id,
            "site_id": site_id,
            "spring_id": spring_id,
            "date": date_val.strftime("%Y-%m-%d"),
            "observer_name": observer_name,
            "observed_slope_deg": observed_slope,
            "observed_geology": observed_geology,
            "observed_soil": observed_soil,
            "existing_structure": existing_struct,
            "validation_status": validation_status,
            "notes": notes,
            "discharge_impact_observed": "Logged"
        }
        save_field_validation(new_record)
        st.success(f"✅ Field Validation Entry '{val_id}' successfully saved!")
        st.rerun()

st.markdown("---")

# Field Validation Log Table
st.subheader("📜 Historical Field Verification Logbook")
df_val_current = load_field_validations_data()
if not df_val_current.empty:
    st.dataframe(df_val_current, use_container_width=True, hide_index=True)
else:
    st.info("No field validation records logged yet.")
