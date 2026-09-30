"""
Unit Tests for SPRING-AI Data Loading & Validation
"""

import unittest
import pandas as pd
from utils.data_loader import load_springs_data, load_environmental_grid, load_discharge_data, load_interventions_data

class TestDataLoader(unittest.TestCase):
    def test_demo_data_loader_structure(self):
        df_springs = load_springs_data()
        self.assertIsInstance(df_springs, pd.DataFrame)
        self.assertIn("spring_id", df_springs.columns)

    def test_environmental_grid_structure(self):
        df_grid = load_environmental_grid()
        self.assertIsInstance(df_grid, pd.DataFrame)
        self.assertIn("slope", df_grid.columns)

    def test_discharge_data_structure(self):
        df_dis = load_discharge_data()
        self.assertIsInstance(df_dis, pd.DataFrame)
        self.assertIn("discharge_lpm", df_dis.columns)

    def test_interventions_data_structure(self):
        df_int = load_interventions_data()
        self.assertIsInstance(df_int, pd.DataFrame)
        self.assertIn("priority_level", df_int.columns)

    def test_district_manager_metrics_and_demographics(self):
        from utils.district_manager import get_district_datasets
        pack = get_district_datasets("Koraput District, Odisha")
        self.assertIn("tribal_demographics", pack)
        self.assertIn("water_metrics", pack)
        self.assertIn("financial_costing", pack)

        tribal = pack["tribal_demographics"]
        self.assertIn("tribes", tribal)
        self.assertGreater(tribal["st_pop_pct"], 0)

        water = pack["water_metrics"]
        self.assertGreater(water["storage_ml"], 0)
        self.assertGreater(water["catchment_sqkm"], 0)

        cost = pack["financial_costing"]
        self.assertGreater(cost["total_cost_lakhs"], 0)
        self.assertGreater(cost["mgnrega_persondays"], 0)

    def test_generate_district_executive_report(self):
        import os
        from utils.district_manager import get_district_datasets
        from reports.report_generator import generate_district_executive_report

        pack = get_district_datasets("Dindori District, MP")
        out_path = "reports/test_district_report.pdf"
        res_path = generate_district_executive_report(pack, out_path)
        self.assertTrue(os.path.exists(res_path))
        self.assertGreater(os.path.getsize(res_path), 500)

if __name__ == "__main__":
    unittest.main()

