"""
Unit Tests for Machine Learning Training & Inference Engine
"""

import unittest
import os
from ml.train_recharge import train_ml_models
from ml.predict_recharge import RechargePredictor

class TestMLPipeline(unittest.TestCase):
    def test_ml_training_and_prediction(self):
        train_ml_models()
        self.assertTrue(os.path.exists("models/recharge_rf_model.pkl"))

        predictor = RechargePredictor()
        sample_input = {
            "elevation": 900.0,
            "slope": 12.0,
            "aspect": 180.0,
            "rainfall": 1400.0,
            "drainage_density": 2.1,
            "distance_to_drainage": 300.0,
            "distance_to_spring": 500.0,
            "fracture_density": 2.5,
            "distance_to_fault": 400.0,
            "land_use_code": 1,
            "soil_permeability": 4,
            "lithology_code": 0
        }

        result = predictor.predict_point(sample_input)
        self.assertIn("model_estimated_recharge_suitability_pct", result)
        self.assertIn("data_confidence_pct", result)
        self.assertTrue(0.0 <= result["model_estimated_recharge_suitability_pct"] <= 100.0)
        self.assertTrue(0.0 <= result["data_confidence_pct"] <= 100.0)

if __name__ == "__main__":
    unittest.main()
