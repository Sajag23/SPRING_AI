"""
Unit Tests for Ask SPRING-AI Natural Language Query Assistant
"""

import unittest
import pandas as pd
from utils.ai_assistant import query_spring_ai
from utils.district_manager import DISTRICTS_CONFIG, get_district_datasets

class TestAIAssistant(unittest.TestCase):

    def setUp(self):
        data_dict = get_district_datasets("Koraput District, Odisha")
        self.dist_cfg = data_dict["config"]
        self.df_springs = data_dict["springs"]
        self.df_interventions = data_dict["interventions"]

    def test_empty_query(self):
        res = query_spring_ai("", self.df_springs, self.dist_cfg)
        self.assertIn("Please type a question", res)

    def test_critical_springs_query(self):
        res = query_spring_ai("Which springs are in critical condition?", self.df_springs, self.dist_cfg)
        self.assertIn("Critical & Declining Springs", res)

    def test_healthy_springs_query(self):
        res = query_spring_ai("Show me healthy high flow springs", self.df_springs, self.dist_cfg)
        self.assertIn("Healthy & Stable Springs", res)

    def test_interventions_query(self):
        res = query_spring_ai("What structures and cost estimates for check dams?", self.df_springs, self.dist_cfg)
        self.assertIn("Recharge Structure & Engineering Guidelines", res)

    def test_specific_spring_query(self):
        res = query_spring_ai("Tell me about KOR-SPR-001", self.df_springs, self.dist_cfg)
        self.assertIn("Spring Details", res)

    def test_water_quality_query(self):
        res = query_spring_ai("What is the WQI and drinking water quality?", self.df_springs, self.dist_cfg)
        self.assertIn("Water Quality Index", res)

    def test_ml_model_query(self):
        res = query_spring_ai("How does the ML algorithm predict recharge?", self.df_springs, self.dist_cfg)
        self.assertIn("Machine Learning Architecture", res)

if __name__ == "__main__":
    unittest.main()
