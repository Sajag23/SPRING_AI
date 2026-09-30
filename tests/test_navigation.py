"""
Unit Tests for Navigation State & Portal Launcher Logic
"""

import unittest
import streamlit as st
from app import launch_portal_module1

class TestNavigation(unittest.TestCase):
    def test_launch_portal_module1(self):
        # Reset session state
        st.session_state["app_mode"] = "🌐 0. Platform Overview & Mission"
        st.session_state["master_nav_radio"] = "🌐 0. Platform Overview & Mission"

        # Mock st.rerun to prevent SystemExit / Streamlit rerun exception during test
        original_rerun = getattr(st, "rerun", None)
        st.rerun = lambda: None
        try:
            launch_portal_module1()
            expected = "🗺️ 1. Recharge Zone & Springshed Delineation"
            self.assertEqual(st.session_state["app_mode"], expected)
            self.assertNotIn("master_nav_radio", st.session_state)
        finally:
            if original_rerun:
                st.rerun = original_rerun

if __name__ == "__main__":
    unittest.main()
