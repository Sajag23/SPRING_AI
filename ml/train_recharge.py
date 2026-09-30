"""
Machine Learning Model Training & Synthetic Data Generator for SPRING-AI
Generates demo datasets, trains Random Forest & XGBoost models, and saves model artifacts.
"""

import os
import json
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score, f1_score
from sklearn.preprocessing import StandardScaler
import joblib

def generate_synthetic_data(output_dir="data/demo", num_springs=50, num_grid_points=1200):
    os.makedirs(output_dir, exist_ok=True)
    np.random.seed(42)

    # Base coordinates for a tribal region (e.g. Koraput / Eastern Ghats, Odisha)
    base_lat = 18.8100
    base_lon = 82.7100

    # 1. Generate Springs Data
    springs = []
    spring_statuses = ["Healthy", "Stable", "Declining", "Critical", "Insufficient Data"]
    villages = ["Pottangi", "Semiliguda", "Lamtaput", "Nandapur", "Dasamantapur", "Laxmipur", "Bandhugaon", "Narayanpatna"]
    districts = ["Koraput"]
    states = ["Odisha"]

    for i in range(1, num_springs + 1):
        lat = base_lat + np.random.uniform(-0.25, 0.25)
        lon = base_lon + np.random.uniform(-0.25, 0.25)
        elevation = np.random.uniform(600, 1400)
        current_discharge = np.round(np.random.gamma(shape=3.0, scale=8.0), 2)
        status = np.random.choice(spring_statuses, p=[0.25, 0.35, 0.20, 0.15, 0.05])
        
        springs.append({
            "spring_id": f"SPR-{i:03d}",
            "spring_name": f"Jharna {i} ({np.random.choice(['Upper', 'Lower', 'Mukhya', 'Bara'])})",
            "latitude": round(lat, 5),
            "longitude": round(lon, 5),
            "elevation": round(elevation, 1),
            "village": np.random.choice(villages),
            "district": districts[0],
            "state": states[0],
            "spring_type": np.random.choice(["Gravity Depression", "Contact Spring", "Fracture Spring", "Fault Spring"]),
            "current_discharge_lpm": current_discharge, # Litres Per Minute
            "seasonal_status": status,
            "recharge_probability": round(np.random.uniform(0.45, 0.95), 2),
            "confidence_score": round(np.random.uniform(0.60, 0.90), 2),
            "landslide_risk": np.random.choice(["Low", "Moderate", "High"], p=[0.6, 0.3, 0.1])
        })
    df_springs = pd.DataFrame(springs)
    df_springs.to_csv(os.path.join(output_dir, "springs.csv"), index=False)

    # 2. Generate Environmental Grid Features for Recharge Zone Modeling
    grid_features = []
    for i in range(1, num_grid_points + 1):
        lat = base_lat + np.random.uniform(-0.30, 0.30)
        lon = base_lon + np.random.uniform(-0.30, 0.30)
        elevation = np.random.uniform(500, 1500)
        slope = np.random.uniform(1.0, 45.0)
        aspect = np.random.uniform(0, 360)
        rainfall = np.random.uniform(1100, 1800)
        drainage_density = np.random.uniform(0.5, 4.5)
        dist_drainage = np.random.uniform(20, 1200)
        dist_spring = np.random.uniform(50, 3000)
        fracture_density = np.random.uniform(0.1, 3.5)
        dist_fault = np.random.uniform(10, 2500)
        land_use_code = np.random.choice([0, 1, 2, 3, 4], p=[0.35, 0.25, 0.20, 0.15, 0.05])
        soil_perm = np.random.choice([1, 2, 3, 4, 5], p=[0.10, 0.25, 0.35, 0.20, 0.10])
        lithology_code = np.random.choice([0, 1, 2, 3, 4], p=[0.40, 0.20, 0.25, 0.10, 0.05])

        # Hydrogeological rule logic for synthetic ground truth target:
        # High recharge probability occurs at: moderate slope (5-25 deg), high fracture density, permeable soil, high rainfall, close fault proximity
        suitability_score = (
            (1.0 if 5 <= slope <= 25 else 0.3) * 0.25 +
            (fracture_density / 3.5) * 0.25 +
            (soil_perm / 5.0) * 0.20 +
            (1.0 - min(dist_fault, 2000)/2000) * 0.15 +
            (rainfall / 1800) * 0.15
        )
        is_suitable = 1 if suitability_score > 0.52 else 0

        grid_features.append({
            "location_id": f"LOC-{i:04d}",
            "latitude": round(lat, 5),
            "longitude": round(lon, 5),
            "elevation": round(elevation, 1),
            "slope": round(slope, 1),
            "aspect": round(aspect, 1),
            "rainfall": round(rainfall, 1),
            "drainage_density": round(drainage_density, 2),
            "distance_to_drainage": round(dist_drainage, 1),
            "distance_to_spring": round(dist_spring, 1),
            "fracture_density": round(fracture_density, 2),
            "distance_to_fault": round(dist_fault, 1),
            "land_use_code": land_use_code,
            "soil_permeability": soil_perm,
            "lithology_code": lithology_code,
            "landslide_risk_code": 2 if slope > 35 else (1 if slope > 22 else 0),
            "recharge_suitability_target": is_suitable,
            "synthetic_suitability_score": round(float(suitability_score), 3)
        })

    df_grid = pd.DataFrame(grid_features)
    df_grid.to_csv(os.path.join(output_dir, "environmental_features.csv"), index=False)

    # 3. Generate Time-Series Spring Discharge Data (36 Months)
    dates = pd.date_range(start="2023-01-01", periods=36, freq="ME")
    discharge_records = []
    for sp in df_springs["spring_id"].iloc[:15]: # Top 15 springs for detailed time series
        base_flow = np.random.uniform(10, 40)
        for date in dates:
            month = date.month
            # Monsoon (June-Sept) rainfall spike
            if month in [6, 7, 8, 9]:
                monthly_rainfall = np.random.uniform(250, 450)
                discharge = base_flow * np.random.uniform(2.5, 4.0)
            elif month in [10, 11]:
                monthly_rainfall = np.random.uniform(40, 120)
                discharge = base_flow * np.random.uniform(1.5, 2.2)
            else:
                monthly_rainfall = np.random.uniform(0, 30)
                discharge = base_flow * np.random.uniform(0.5, 1.1)
            
            discharge_records.append({
                "spring_id": sp,
                "date": date.strftime("%Y-%m-%d"),
                "rainfall_mm": round(monthly_rainfall, 1),
                "discharge_lpm": round(discharge, 2),
                "temperature_c": round(np.random.uniform(18, 34), 1),
                "season": "Monsoon" if month in [6,7,8,9] else ("Post-Monsoon" if month in [10,11] else "Dry Summer")
            })
    df_discharge = pd.DataFrame(discharge_records)
    df_discharge.to_csv(os.path.join(output_dir, "discharge.csv"), index=False)

    # 4. Generate Candidate Interventions
    interventions = []
    types = ["Staggered Contour Trench (SCT)", "Loose Boulder Check Dam (LBCD)", "Percolation Pond", "Recharge Pit with Shaft", "Vegetative Bio-Fencing"]
    for i in range(1, 30):
        lat = base_lat + np.random.uniform(-0.20, 0.20)
        lon = base_lon + np.random.uniform(-0.20, 0.20)
        slope = np.random.uniform(4, 28)
        risk = "Low" if slope < 18 else ("Moderate" if slope < 25 else "High")
        itype = types[0] if slope > 15 else (types[1] if slope > 8 else types[2])
        score = round(np.random.uniform(0.65, 0.94), 2)
        
        interventions.append({
            "site_id": f"INT-{i:03d}",
            "latitude": round(lat, 5),
            "longitude": round(lon, 5),
            "nearest_spring_id": f"SPR-{(i % num_springs) + 1:03d}",
            "elevation": round(np.random.uniform(700, 1300), 1),
            "slope": round(slope, 1),
            "recommended_structure": itype,
            "priority_level": "HIGH" if score > 0.82 else ("MEDIUM" if score > 0.70 else "LOW"),
            "suitability_score": score,
            "confidence_score": round(np.random.uniform(0.68, 0.88), 2),
            "risk_status": risk,
            "existing_structure": np.random.choice(["None", "Dilapidated Check Dam", "Natural Stream"], p=[0.7, 0.15, 0.15]),
            "field_status": np.random.choice(["Proposed", "Field Verified", "Under Construction", "Needs Review"], p=[0.5, 0.25, 0.1, 0.15])
        })
    df_int = pd.DataFrame(interventions)
    df_int.to_csv(os.path.join(output_dir, "interventions.csv"), index=False)

    # 5. Generate Field Validation Records
    validations = [
        {
            "validation_id": "VAL-001",
            "site_id": "INT-001",
            "spring_id": "SPR-001",
            "date": "2026-08-15",
            "observer_name": "Ramesh Kumar (Jal Sai)",
            "observed_slope_deg": 14.2,
            "observed_geology": "Fractured Granite",
            "observed_soil": "Permeable Gravelly Loam",
            "existing_structure": "None",
            "validation_status": "Suitable",
            "notes": "Good catchment area with high infiltration potential. Recommended SCT construction.",
            "discharge_impact_observed": "N/A (Pre-construction)"
        },
        {
            "validation_id": "VAL-002",
            "site_id": "INT-005",
            "spring_id": "SPR-003",
            "date": "2026-09-02",
            "observer_name": "Dr. Anita Roy (Hydrogeologist)",
            "observed_slope_deg": 29.5,
            "observed_geology": "Sheared Slate",
            "observed_soil": "Thin Stony Soil",
            "existing_structure": "Natural Stream",
            "validation_status": "Needs Review",
            "notes": "Slope exceeds safe threshold for heavy percolation. Risk of local soil creep.",
            "discharge_impact_observed": "N/A"
        }
    ]
    df_val = pd.DataFrame(validations)
    df_val.to_csv(os.path.join(output_dir, "field_validations.csv"), index=False)

    print(f"Generated synthetic demo data at '{output_dir}'.")

def train_ml_models(data_dir="data/demo", model_dir="models"):
    os.makedirs(model_dir, exist_ok=True)
    grid_path = os.path.join(data_dir, "environmental_features.csv")
    if not os.path.exists(grid_path):
        generate_synthetic_data(data_dir)

    df = pd.read_csv(grid_path)
    feature_cols = [
        "elevation", "slope", "aspect", "rainfall", "drainage_density",
        "distance_to_drainage", "distance_to_spring", "fracture_density",
        "distance_to_fault", "land_use_code", "soil_permeability", "lithology_code"
    ]

    X = df[feature_cols]
    y = df["recharge_suitability_target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train Random Forest
    rf_model = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)
    rf_model.fit(X_train_scaled, y_train)

    y_pred = rf_model.predict(X_test_scaled)
    y_prob = rf_model.predict_proba(X_test_scaled)[:, 1]

    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_prob)

    # Feature Importance
    importances = rf_model.feature_importances_
    feat_imp = {col: round(float(imp), 4) for col, imp in zip(feature_cols, importances)}

    # Save artifacts
    joblib.dump(rf_model, os.path.join(model_dir, "recharge_rf_model.pkl"))
    joblib.dump(scaler, os.path.join(model_dir, "scaler.pkl"))

    metrics = {
        "model_type": "RandomForestClassifier",
        "f1_score": round(float(f1), 4),
        "roc_auc": round(float(roc_auc), 4),
        "feature_importances": feat_imp,
        "num_training_samples": len(X_train),
        "is_synthetic_model": True
    }

    with open(os.path.join(model_dir, "metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)

    with open(os.path.join(model_dir, "feature_names.json"), "w") as f:
        json.dump(feature_cols, f, indent=2)

    print(f"Model successfully trained! F1-Score: {f1:.4f}, ROC-AUC: {roc_auc:.4f}")

if __name__ == "__main__":
    generate_synthetic_data()
    train_ml_models()
