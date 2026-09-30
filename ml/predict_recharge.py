"""
Inference & Hybrid Recharge Scoring Engine for SPRING-AI
Combines Machine Learning predictions with Hydrogeological Rule-Based Factors and computes Confidence Scores.
"""

import os
import json
import numpy as np
import pandas as pd
import joblib

class RechargePredictor:
    def __init__(self, model_dir="models"):
        self.model_path = os.path.join(model_dir, "recharge_rf_model.pkl")
        self.scaler_path = os.path.join(model_dir, "scaler.pkl")
        self.metrics_path = os.path.join(model_dir, "metrics.json")
        self.feature_names_path = os.path.join(model_dir, "feature_names.json")

        if os.path.exists(self.model_path) and os.path.exists(self.scaler_path):
            self.model = joblib.load(self.model_path)
            self.scaler = joblib.load(self.scaler_path)
            with open(self.metrics_path, "r") as f:
                self.metrics = json.load(f)
            with open(self.feature_names_path, "r") as f:
                self.feature_names = json.load(f)
        else:
            self.model = None
            self.scaler = None
            self.metrics = {}
            self.feature_names = []

    def predict_point(self, input_dict):
        """
        Calculates hybrid recharge suitability score and confidence for a single location.
        """
        # 1. Feature array extraction
        feat_array = []
        for feat in self.feature_names:
            feat_array.append(input_dict.get(feat, 0.0))

        feat_vector = np.array(feat_array).reshape(1, -1)

        # 2. ML Model Prediction
        if self.model is not None and self.scaler is not None:
            scaled_feat = self.scaler.transform(feat_vector)
            ml_prob = float(self.model.predict_proba(scaled_feat)[0, 1])
        else:
            ml_prob = 0.50 # Fallback

        # 3. Rule-Based Hydrogeological Scoring
        slope = input_dict.get("slope", 15.0)
        fracture_density = input_dict.get("fracture_density", 1.0)
        dist_fault = input_dict.get("distance_to_fault", 1000.0)
        soil_perm = input_dict.get("soil_permeability", 3.0)
        rainfall = input_dict.get("rainfall", 1200.0)

        # Hydrogeological rule checks
        slope_score = 1.0 if (5 <= slope <= 25) else (0.4 if slope < 5 else 0.1)
        frac_score = min(fracture_density / 3.0, 1.0)
        fault_score = max(0.0, 1.0 - (dist_fault / 2000.0))
        soil_score = soil_perm / 5.0
        rain_score = min(rainfall / 1600.0, 1.0)

        hydro_rule_score = (
            0.30 * frac_score +
            0.25 * slope_score +
            0.20 * fault_score +
            0.15 * soil_score +
            0.10 * rain_score
        )

        # 4. Hybrid Suitability Score (0% - 100%)
        hybrid_score = round(float((0.55 * ml_prob + 0.45 * hydro_rule_score) * 100), 1)

        # 5. Data Confidence Indicator (0% - 100%)
        # Confidence increases if critical variables (fracture_density, fault distance) are provided
        confidence = 60.0
        if "fracture_density" in input_dict: confidence += 15.0
        if "distance_to_fault" in input_dict: confidence += 10.0
        if "soil_permeability" in input_dict: confidence += 10.0
        if "elevation" in input_dict: confidence += 5.0
        confidence = round(min(confidence, 95.0), 1)

        # 6. Feature Contribution / Explainability
        contributions = {
            "Positive Factors": [],
            "Negative / Constraint Factors": []
        }

        if 5 <= slope <= 25:
            contributions["Positive Factors"].append(f"Favourable Slope ({slope:.1f}°)")
        else:
            contributions["Negative / Constraint Factors"].append(f"Suboptimal Slope ({slope:.1f}°)")

        if fracture_density > 1.5:
            contributions["Positive Factors"].append(f"High Rock Fracture Density ({fracture_density:.1f} km/km²)")
        else:
            contributions["Negative / Constraint Factors"].append(f"Low Fracture Density ({fracture_density:.1f} km/km²)")

        if dist_fault < 800:
            contributions["Positive Factors"].append(f"Proximity to Geological Fault Line ({dist_fault:.0f} m)")

        if rainfall > 1300:
            contributions["Positive Factors"].append(f"High Annual Precipitation ({rainfall:.0f} mm)")

        if slope > 35:
            contributions["Negative / Constraint Factors"].append(f"CRITICAL: High Slope Landslide Hazard Zone ({slope:.1f}°)")

        return {
            "model_estimated_recharge_suitability_pct": hybrid_score,
            "data_confidence_pct": confidence,
            "ml_model_probability": round(ml_prob, 3),
            "hydrogeological_rule_score": round(hydro_rule_score, 3),
            "explainability": contributions
        }

    def predict_dataframe(self, df):
        """
        Batch prediction for a dataframe of locations.
        """
        results = []
        for idx, row in df.iterrows():
            res = self.predict_point(row.to_dict())
            results.append(res["model_estimated_recharge_suitability_pct"])
        df_copy = df.copy()
        df_copy["model_estimated_recharge_suitability_pct"] = results
        return df_copy
