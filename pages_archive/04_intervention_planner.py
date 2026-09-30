"""
Module 4 — Intervention Site Prioritisation & Recommendation Engine
"""

import streamlit as st
import pandas as pd
from utils.data_loader import load_interventions_data, load_springs_data
from utils.scoring import evaluate_intervention_site
from reports.report_generator import generate_spring_pdf_report
from utils.config import DEMO_DATA_DISCLAIMER

st.set_page_config(page_title="Intervention Planner | SPRING-AI", layout="wide")

st.title("🛠️ Module 4 — Intervention Site Prioritisation")
st.caption("Ranked candidate locations for spring-revival interventions, rule-based structure matching, and PDF site inspection report generation.")

st.warning(f"⚠️ {DEMO_DATA_DISCLAIMER}")

df_int = load_interventions_data()
df_springs = load_springs_data()

# Filters
f_col1, f_col2, f_col3 = st.columns(3)
with f_col1:
    priority_filter = st.multiselect("Filter by Priority Level:", options=["HIGH", "MEDIUM", "LOW"], default=["HIGH", "MEDIUM"])
with f_col2:
    structure_filter = st.multiselect("Filter by Recommended Structure:", options=df_int["recommended_structure"].unique())
with f_col3:
    risk_filter = st.multiselect("Filter by Risk Status:", options=df_int["risk_status"].unique(), default=["Low", "Moderate"])

# Apply Filters
df_filtered = df_int.copy()
if priority_filter:
    df_filtered = df_filtered[df_filtered["priority_level"].isin(priority_filter)]
if structure_filter:
    df_filtered = df_filtered[df_filtered["recommended_structure"].isin(structure_filter)]
if risk_filter:
    df_filtered = df_filtered[df_filtered["risk_status"].isin(risk_filter)]

st.markdown(f"### Prioritised Candidate Sites ({len(df_filtered)} Matches)")

# Display Interactive Table
st.dataframe(
    df_filtered[[
        "site_id", "nearest_spring_id", "priority_level", "suitability_score",
        "recommended_structure", "slope", "risk_status", "existing_structure", "field_status"
    ]].sort_values("suitability_score", ascending=False),
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# Detailed Site Inspection Card
st.subheader("🔍 Site Deep-Dive & Rule Recommendation Engine")
selected_site_id = st.selectbox("Select Site ID for Detailed Engineering Evaluation:", df_int["site_id"])

site_info = df_int[df_int["site_id"] == selected_site_id].iloc[0]
spring_info = df_springs[df_springs["spring_id"] == site_info["nearest_spring_id"]].iloc[0]

eval_res = evaluate_intervention_site(site_info.to_dict())

s_c1, s_c2 = st.columns([1.5, 1])

with s_c1:
    st.markdown(f"### Site Details: `{site_info['site_id']}`")
    st.markdown(f"**Target Spring:** {spring_info['spring_name']} ({site_info['nearest_spring_id']})")
    st.markdown(f"**Latitude/Longitude:** {site_info['latitude']}° N, {site_info['longitude']}° E")
    st.markdown(f"**Elevation:** {site_info['elevation']} m | **Terrain Slope:** {site_info['slope']}°")
    
    st.info(f"""
    💡 **Indicative Intervention Recommendation:**  
    **{eval_res['indicative_recommendation']}**  

    *Priority Level:* **{eval_res['priority_level']}** ({eval_res['priority_score_pct']}% Score)  
    *Risk Status:* **{eval_res['risk_status']}**  
    """)

    st.caption(f"⚠️ {eval_res['disclaimer']}")

with s_c2:
    st.subheader("📄 Generate Site PDF Report")
    st.write("Export printable decision support report for field engineers & district authorities.")
    
    if st.button("📥 Download PDF Site Inspection Report"):
        pdf_path = f"reports/Report_{selected_site_id}.pdf"
        generate_spring_pdf_report(spring_info.to_dict(), site_info.to_dict(), pdf_path)
        
        with open(pdf_path, "rb") as file:
            st.download_button(
                label=" Click Here to Download PDF",
                data=file,
                file_name=f"SPRING_AI_Report_{selected_site_id}.pdf",
                mime="application/pdf"
            )
