"""
Unit Tests for Intervention Rule Matching & Risk Analysis
"""

import unittest
from utils.scoring import evaluate_intervention_site, calculate_data_quality_score

class TestScoring(unittest.TestCase):
    def test_landslide_risk_inhibition(self):
        high_slope_site = {
            "slope": 40.0,
            "suitability_score": 0.85,
            "soil_permeability": 3,
            "existing_structure": "None"
        }
        eval_res = evaluate_intervention_site(high_slope_site)
        self.assertEqual(eval_res["risk_status"], "Critical")
        self.assertEqual(eval_res["priority_level"], "LOW")
        self.assertIn("High Landslide Risk", eval_res["indicative_recommendation"])

    def test_contour_trench_recommendation(self):
        mod_slope_site = {
            "slope": 18.0,
            "suitability_score": 0.88,
            "soil_permeability": 4,
            "existing_structure": "None"
        }
        eval_res = evaluate_intervention_site(mod_slope_site)
        self.assertEqual(eval_res["priority_level"], "HIGH")
        self.assertIn("Contour Trenches", eval_res["indicative_recommendation"])

    def test_data_quality_score(self):
        datasets = {
            "terrain_dem": True,
            "rainfall": True,
            "geology_lithology": True,
            "faults_fractures": False,
            "spring_discharge": True,
            "land_use": False
        }
        dq = calculate_data_quality_score(datasets)
        self.assertIn(dq["confidence_level"], ["HIGH", "MEDIUM", "LOW"])
        self.assertTrue(0.0 <= dq["overall_score_pct"] <= 100.0)

if __name__ == "__main__":
    unittest.main()
