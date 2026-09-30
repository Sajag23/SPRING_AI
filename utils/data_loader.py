"""
Data Loader Utility for SPRING-AI Platform
Loads Real NASA Climate Datasets, Real Satellite Elevation Data, Springs Data, Environmental Grid Features, and Interventions.
"""

import os
import pandas as pd
import streamlit as st

DATA_DIR = "data/demo"
REAL_DIR = "data/real"

@st.cache_data
def load_springs_data(data_dir=DATA_DIR):
    path = os.path.join(data_dir, "springs.csv")
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame(columns=["spring_id", "spring_name", "latitude", "longitude", "elevation", "village", "district", "state", "spring_type", "current_discharge_lpm", "seasonal_status", "recharge_probability", "confidence_score", "landslide_risk"])

@st.cache_data
def load_environmental_grid(data_dir=DATA_DIR):
    path = os.path.join(data_dir, "environmental_features.csv")
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame(columns=["location_id", "latitude", "longitude", "elevation", "slope", "aspect", "rainfall", "drainage_density", "distance_to_drainage", "distance_to_spring", "fracture_density", "distance_to_fault", "land_use_code", "soil_permeability", "lithology_code", "landslide_risk_code", "recharge_suitability_target", "synthetic_suitability_score"])

@st.cache_data
def load_discharge_data(data_dir=DATA_DIR):
    path = os.path.join(data_dir, "discharge.csv")
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame(columns=["spring_id", "date", "rainfall_mm", "discharge_lpm", "temperature_c", "season"])

@st.cache_data
def load_interventions_data(data_dir=DATA_DIR):
    path = os.path.join(data_dir, "interventions.csv")
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame(columns=["site_id", "latitude", "longitude", "nearest_spring_id", "elevation", "slope", "recommended_structure", "priority_level", "suitability_score", "confidence_score", "risk_status", "existing_structure", "field_status"])

@st.cache_data
def load_real_nasa_climate_data(real_dir=REAL_DIR):
    path = os.path.join(real_dir, "real_nasa_climate_koraput.csv")
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame()

@st.cache_data
def load_real_elevation_villages(real_dir=REAL_DIR):
    path = os.path.join(real_dir, "real_elevation_villages_koraput.csv")
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame()

def load_field_validations_data(data_dir=DATA_DIR):
    path = os.path.join(data_dir, "field_validations.csv")
    if os.path.exists(path):
        return pd.read_csv(path)
    return pd.DataFrame()

def save_field_validation(new_record, data_dir=DATA_DIR):
    path = os.path.join(data_dir, "field_validations.csv")
    if os.path.exists(path):
        df = pd.read_csv(path)
        df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
    else:
        df = pd.DataFrame([new_record])
    df.to_csv(path, index=False)
    return df

def ingest_custom_ground_report(report_dict, dist_pack):
    """
    Ingests custom on-ground field assessment report data submitted by villagers or engineers.
    Updates the springs and interventions datasets in dist_pack, re-scoring GeoAI recharge predictions.
    """
    if not isinstance(report_dict, dict) or not dist_pack:
        return dist_pack

    df_springs = dist_pack["springs"]
    cfg = dist_pack["config"]

    sp_id = report_dict.get("spring_id", f"{cfg['district'][:3].upper()}-SPR-GROUND")
    sp_name = report_dict.get("spring_name", f"{cfg['district']} Field Assessed Spring")
    lat = float(report_dict.get("latitude", cfg["center_coords"][0]))
    lon = float(report_dict.get("longitude", cfg["center_coords"][1]))
    discharge = float(report_dict.get("observed_discharge_lpm", 12.0))
    slope = float(report_dict.get("observed_slope", 15.0))
    notes = report_dict.get("field_notes", "Ingested ground assessment report.")

    status = "Critical" if discharge < 8 else ("Declining" if discharge < 18 else "Healthy")
    risk_status = "High" if slope > 30 else ("Moderate" if slope > 18 else "Low")
    recharge_prob = round(min(0.95, max(0.45, 0.90 - (slope / 100.0) + (discharge / 100.0))), 2)

    new_spring_row = {
        "spring_id": sp_id,
        "spring_name": sp_name,
        "latitude": round(lat, 5),
        "longitude": round(lon, 5),
        "elevation": round(report_dict.get("elevation", 750.0), 1),
        "village": report_dict.get("village", cfg.get("villages", ["Ground Site"])[0]),
        "district": cfg["district"],
        "state": cfg["state"],
        "spring_type": report_dict.get("spring_type", "Fracture Spring"),
        "current_discharge_lpm": discharge,
        "seasonal_status": status,
        "recharge_probability": recharge_prob,
        "confidence_score": 0.94,
        "landslide_risk": risk_status,
        "govt_datasource": f"Ground Report ({report_dict.get('surveyor_name', 'Villager/Engineer')})"
    }

    existing = df_springs[df_springs["spring_id"] == sp_id]
    if not existing.empty:
        idx = existing.index[0]
        for k, v in new_spring_row.items():
            df_springs.at[idx, k] = v
    else:
        df_springs = pd.concat([pd.DataFrame([new_spring_row]), df_springs], ignore_index=True)

    dist_pack["springs"] = df_springs

    val_record = {
        "validation_id": f"VAL-GROUND-{len(load_field_validations_data())+1:03d}",
        "site_id": sp_id,
        "observer_name": report_dict.get("surveyor_name", "Villager/Engineer"),
        "observed_slope_deg": slope,
        "validation_status": "Ground Assessment Ingested",
        "notes": f"{notes} | Ground Discharge: {discharge} LPM | Status: {status}"
    }
    save_field_validation(val_record)

    return dist_pack

