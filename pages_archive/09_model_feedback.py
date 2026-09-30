"""
Module 9 — Model Feedback Loop & Retraining Workflow
"""

import streamlit as st
import pandas as pd
from utils.data_loader import load_field_validations_data
from ml.train_recharge import train_ml_models
from utils.config import DEMO_DATA_DISCLAIMER

st.set_page_config(page_title="Model Feedback | SPRING-AI", layout="wide")

st.title("🔄 Module 9 — Model Feedback & Controlled Retraining")
st.caption("Comparison of AI predictions against ground-truthed field observations, validation accuracy evaluation, and retraining workflows.")

st.warning(f"⚠️ {DEMO_DATA_DISCLAIMER}")

df_val = load_field_validations_data()

st.markdown("""
```
AI Prediction
      ↓
Field Verification
      ↓
Actual Observation
      ↓
Comparison & Evaluation
      ↓
Updated Dataset
      ↓
Controlled Retraining Workflow
```
""")

# Validation Performance Metrics
if not df_val.empty:
    m1, m2, m3, m4 = st.columns(4)
    total_val = len(df_val)
    suitable_count = len(df_val[df_val["validation_status"] == "Suitable"])
    review_count = len(df_val[df_val["validation_status"] == "Needs Review"])
    accuracy_pct = round((suitable_count / total_val) * 100, 1)

    m1.metric("Field Validations Logged", f"{total_val}")
    m2.metric("Confirmed Suitable", f"{suitable_count}", f"{accuracy_pct}% Match Rate")
    m3.metric("Requires Review / Flagged", f"{review_count}")
    m4.metric("Model Feedback Precision", f"{accuracy_pct}%")

    st.markdown("---")

    st.subheader("📋 Logged Observations vs AI Predictions")
    st.dataframe(df_val, use_container_width=True, hide_index=True)
else:
    st.info("No field validation records logged yet.")

st.markdown("---")

# Controlled Retraining Trigger
st.subheader("⚙️ Controlled Model Retraining Workflow")
st.write("Triggering retraining incorporates newly logged field validations and updated spatial features into the Random Forest model.")

st.warning("⚠️ **Safety Notice**: Production models are NOT automatically updated without human-in-the-loop review.")

if st.button("🚀 Execute Model Retraining Workflow"):
    with st.spinner("Retraining Random Forest Model on updated datasets..."):
        train_ml_models()
    st.success("✅ Model retraining completed successfully! New model weights saved to `models/recharge_rf_model.pkl`.")
