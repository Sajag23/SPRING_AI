# SPRING-AI — AI-Based Spring Revival & Recharge Planning System

**Ministry of Tribal Affairs — AI/ML Geospatial Decision Support System Prototype**

> **Geospatial intelligence for identifying probable recharge zones, prioritising spring-revival interventions, and supporting field-based water resource management in tribal and hilly areas.**

---

## 📌 Project Overview

In hilly and tribal regions across India (such as the Eastern Ghats, Western Ghats, Northeast, and Himalayan belts), natural springs (*Dhara*, *Jharna*, or *Naula*) are the primary lifeline for drinking water, domestic use, and hill agriculture. 

However, identifying a spring's underlying recharge zone—the uphill area where rainfall sinks into fractured rock layers and feeds the spring—is difficult through surface observation alone. Traditional hydrogeological field surveys are time-consuming and expensive to scale across thousands of remote tribal hamlets.

**SPRING-AI** is a scientifically cautious, technology-enabled decision-support platform designed to:
1. **Delineate Probable Recharge Zones / Springsheds** using DEM elevation, geological fractures, rainfall, and land-use data.
2. **Compute Recharge Suitability Probabilities** using Random Forest and XGBoost machine learning models combined with hydrogeological rule frameworks.
3. **Prioritise Candidate Intervention Locations** and recommend site-appropriate water conservation structures (e.g. Staggered Contour Trenches, Loose Boulder Check Dams, Percolation Ponds).
4. **Enforce Environmental & Landslide Risk Masking** to prohibit heavy recharge interventions on steep slopes (>30°–35°).
5. **Incorporate Field Verification & Ground-Truthing Data** to create a continuous model feedback and controlled retraining loop.

---

## ⚠️ Synthetic Demonstration Data Disclaimer

```
SYNTHETIC DEMONSTRATION DATA — NOT REAL FIELD MEASUREMENTS.
All geographical coordinates, spring names, discharge trends, and environmental variables
used in this demonstration are generated realistically for testing purposes.
```

**Scientific Boundary Notice**: Predictions are presented as **model-estimated recharge suitability decision-support estimates**, NOT as guaranteed underground flow paths. All recommendations require field and engineering verification prior to construction.

---

## 🏗️ System Architecture

```
                                  SPRING-AI PIPELINE
                                  
   DATA INGESTION               GEOSPATIAL AI ENGINE              DECISION SUPPORT PORTAL
+-------------------+        +------------------------+        +---------------------------+
| - DEM (Copernicus)|        | - Random Forest Model  |        | - Executive Dashboard     |
| - GSI Geology     | ------>| - XGBoost Regressor    | ------>| - Interactive Folium Map  |
| - IMD Rainfall    |        | - Hydro-Rule Engine    |        | - Spring Explorer         |
| - Fracture Buffer |        | - Landslide Risk Mask  |        | - PDF Report Generator    |
| - Sentinel LULC   |        | - Data Confidence Metric|       | - Field Validation Logger |
+-------------------+        +------------------------+        +---------------------------+
```

---

## 🚀 Installation & Running Instructions

### 1. Prerequisites
- Python 3.9+ installed
- `pip` package manager

### 2. Clone / Navigate to Project Directory
```bash
cd C:\Users\dhank\.gemini\antigravity\scratch\spring-ai
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train Demonstration Model & Generate Data
```bash
python ml/train_recharge.py
```

### 5. Launch Application
```bash
streamlit run app.py
```
Open your browser to `http://localhost:8501`.

---

## 🧪 Running Automated Unit Tests
```bash
python -m pytest tests/
```

---

## 🎬 5–10 Minute Demo Workflow Sequence

Follow these steps to demonstrate the full capabilities of the platform:

1. **Open Landing Page (`app.py`)**: Review header disclaimers, Ministry badge, and system capabilities.
2. **Module 1 — Executive Dashboard (`01_dashboard.py`)**: View total springs, declining status count, high recharge area, and interactive Folium GIS map with togglable heatmap overlays.
3. **Module 2 — Spring Explorer (`02_spring_explorer.py`)**: Select a spring (e.g. `SPR-001`) to inspect elevation, current discharge, seasonal health, and 36-month hydrograph.
4. **Module 3 — AI Recharge Analysis (`03_recharge_analysis.py`)**: Adjust slope and fracture density sliders in the interactive simulator to see real-time suitability score changes and Random Forest feature importance.
5. **Module 4 — Intervention Planner (`04_intervention_planner.py`)**: View candidate sites ranked by priority. Click "Download PDF Site Inspection Report" to generate a printable report.
6. **Module 5 — Risk Analysis (`05_risk_analysis.py`)**: Inspect the landslide hazard mask displaying steep slope (>30°) zones where recharge interventions are prohibited.
7. **Module 6 — Spring Forecasting (`06_spring_forecasting`)**: Review rainfall vs discharge correlation and the 6-month predictive flow extrapolation.
8. **Module 7 — Field Validation (`07_field_validation.py`)**: Submit a new field observation entry logged by a Jal Sai or engineer.
9. **Module 8 — Data Management (`08_data_management.py`)**: Check system data confidence and layer completeness breakdown.
10. **Module 9 — Model Feedback (`09_model_feedback.py`)**: Review field accuracy vs predictions and trigger the controlled model retraining workflow.
11. **Module 10 — Methodology (`10_methodology.py`)**: Review architectural pipelines, scientific rules, and test the Spring-AI Assistant.

---

## 📄 License & Attribution

Developed for the **Ministry of Tribal Affairs**.  
Built with Streamlit, Scikit-Learn, Folium, Plotly, and FPDF2.
