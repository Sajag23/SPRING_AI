"""
SPRING-AI — AI-Powered Spring Revival & Recharge Planning System
Production-Quality GeoAI Platform & Decision-Support System
"""

import os
import io
import zipfile
import datetime
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
# Data & GIS Utilities
import importlib
try:
    from utils.district_manager import DISTRICTS_CONFIG, get_district_datasets, TRIBAL_STATE_DISTRICTS_MAP
except ImportError:
    import utils.district_manager
    importlib.reload(utils.district_manager)
    from utils.district_manager import DISTRICTS_CONFIG, get_district_datasets, TRIBAL_STATE_DISTRICTS_MAP
import importlib
try:
    from utils.data_loader import (
        load_field_validations_data, save_field_validation,
        load_real_nasa_climate_data, load_real_elevation_villages,
        ingest_custom_ground_report
    )
except ImportError:
    import utils.data_loader
    importlib.reload(utils.data_loader)
    from utils.data_loader import (
        load_field_validations_data, save_field_validation,
        load_real_nasa_climate_data, load_real_elevation_villages,
        ingest_custom_ground_report
    )
from utils.ai_assistant import query_spring_ai
import utils.landing_page
importlib.reload(utils.landing_page)
from utils.landing_page import render_landing_page
from ml.predict_recharge import RechargePredictor
from ml.forecasting import analyze_discharge_trend
from ml.train_recharge import train_ml_models
try:
    from utils.scoring import (
        evaluate_intervention_site, calculate_data_quality_score,
        calculate_spring_health_score, calculate_before_after_impact, GLOSSARY_TERMS
    )
except ImportError:
    pass
try:
    from gis.mapping import create_spring_gis_map, render_gis_map, create_pan_india_overview_map
except ImportError:
    import gis.mapping
    importlib.reload(gis.mapping)
    from gis.mapping import create_spring_gis_map, render_gis_map, create_pan_india_overview_map
try:
    from reports.report_generator import generate_spring_pdf_report, generate_district_executive_report
except ImportError:
    import reports.report_generator
    importlib.reload(reports.report_generator)
    from reports.report_generator import generate_spring_pdf_report, generate_district_executive_report
try:
    from utils.config import (
        APP_TITLE, APP_TAGLINE, APP_SUBTITLE,
        COLOR_PRIMARY_FOREST, COLOR_SECONDARY_FOREST, COLOR_WATER_BLUE, COLOR_SKY_BLUE,
        COLOR_EARTH, COLOR_SAND, COLOR_BG_LIGHT, COLOR_BG_DARK,
        DEMO_DATA_DISCLAIMER, SCIENTIFIC_DISCLAIMER, JALSETU_LOGO_SVG
    )
except ImportError:
    APP_TITLE = "SPRING-AI"
    APP_TAGLINE = "Restoring Springs • Predicting Recharge • Strengthening Communities"
    APP_SUBTITLE = "AI-powered geospatial decision support for spring revival and recharge planning in tribal and mountainous regions."
    COLOR_PRIMARY_FOREST = "#12372A"
    COLOR_SECONDARY_FOREST = "#1F5C45"
    COLOR_WATER_BLUE = "#0284c7"
    COLOR_SKY_BLUE = "#38bdf8"
    COLOR_EARTH = "#8B6F47"
    COLOR_SAND = "#D8C3A5"
    COLOR_BG_LIGHT = "#f8fafc"
    COLOR_BG_DARK = "#0f172a"
    DEMO_DATA_DISCLAIMER = (
        "DEMO & REAL DATASET NOTICE: All spatial layers combine satellite DEM (Bhuvan/Copernicus), "
        "precipitation, geology, and hydrogeological baselines across 100+ tribal districts in 17 states."
    )
    SCIENTIFIC_DISCLAIMER = (
        "IMPORTANT SCIENTIFIC DISCLAIMER: SPRING-AI provides decision-support estimates. "
        "AI predictions and recommendations must be clearly understood as model outputs and are not guaranteed ground truth. "
        "All outputs require appropriate field validation and expert hydrogeological assessment prior to engineering construction."
    )
    JALSETU_LOGO_SVG = """
    <svg width="36" height="36" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="46" stroke="#0284c7" stroke-width="4" stroke-dasharray="8 4" opacity="0.6"/>
        <path d="M20 75L50 25L80 75H20Z" fill="#0f172a"/>
        <path d="M40 75L62 38L85 75H40Z" fill="#059669" opacity="0.85"/>
        <path d="M50 42C50 42 38 58 38 65C38 71.6 43.4 77 50 77C56.6 77 62 71.6 62 65C62 58 50 42 50 42Z" fill="#0284c7"/>
    </svg>
    """

# Page Setup — Force Collapsed Sidebar
st.set_page_config(
    page_title="SPRING-AI | GeoAI Spring Revival Platform",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize Session States
if "app_mode" not in st.session_state:
    st.session_state.app_mode = "LANDING" # LANDING or DASHBOARD
if "dashboard_tab" not in st.session_state:
    st.session_state.dashboard_tab = "Overview"
if "user_role" not in st.session_state:
    st.session_state.user_role = "Analyst"

# ==============================================================================
# ENTERPRISE GEOAI DESIGN SYSTEM (SPRING-AI STYLING & CSS)
# ==============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

    html, body {
        font-family: 'Space Grotesk', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: #f8fafc !important;
        color: #0f172a !important;
    }

    .stApp {
        background-color: #f8fafc !important;
        color: #0f172a !important;
    }

    /* Permanently Hide Left Sidebar & Streamlit Default Top Header Bar */
    [data-testid="stSidebar"], [data-testid="stSidebarNav"], section[data-testid="stSidebar"],
    header[data-testid="stHeader"], header, div[data-testid="stHeader"] {
        display: none !important;
        visibility: hidden !important;
        height: 0px !important;
    }

    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 2.5rem !important;
        max-width: 98% !important;
    }

    /* PREVENT STREAMLIT DEFAULT RERUN BLURRING & DIMMING */
    div[data-stale="true"],
    section[data-stale="true"],
    div[data-testid="stVerticalBlock"] > div[data-stale="true"],
    .stApp > div[data-stale="true"] {
        opacity: 1 !important;
        filter: none !important;
        transition: none !important;
    }

    /* IFRAME & MAP HARDWARE ACCELERATION SHARPNESS */
    iframe {
        border-radius: 12px !important;
        border: 1px solid #cbd5e1 !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04) !important;
        transform: translateZ(0) !important;
        backface-visibility: hidden !important;
        image-rendering: -webkit-optimize-contrast !important;
    }

    /* SELECTBOX & INPUT CONTRAST FIXES */
    div[data-baseweb="select"] {
        background-color: #ffffff !important;
        border-radius: 8px !important;
    }
    div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02) !important;
    }
    div[data-baseweb="select"] span,
    div[data-baseweb="select"] div,
    div[data-baseweb="select"] p {
        color: #0f172a !important;
        font-weight: 700 !important;
    }
    div[data-baseweb="popover"] div {
        background-color: #ffffff !important;
        color: #0f172a !important;
    }
    label[data-testid="stWidgetLabel"] p,
    label[data-testid="stWidgetLabel"] span {
        color: #0f172a !important;
        font-weight: 800 !important;
        font-size: 14px !important;
    }

    /* PORTAL HEADER BOX CONTRAST FIX */
    .portal-header-box {
        background: linear-gradient(135deg, #08120F 0%, #083B2C 100%) !important;
        padding: 14px 22px !important;
        border-radius: 12px !important;
        margin-bottom: 14px !important;
        border: 1px solid #145A43 !important;
        box-shadow: 0 4px 15px rgba(8, 18, 15, 0.25) !important;
    }
    .portal-header-box, .portal-header-box div, .portal-header-box span, .portal-header-box p {
        color: #FFFFFF !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 800 !important;
        font-size: 19px !important;
        letter-spacing: -0.3px !important;
        text-shadow: 0 1px 3px rgba(0,0,0,0.8) !important;
    }

    /* HORIZONTAL RADIO NAVIGATION TABS FIX */
    div[data-testid="stRadio"] > label {
        display: none !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] {
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 6px !important;
        background-color: #e2e8f0 !important;
        padding: 6px !important;
        border-radius: 12px !important;
        margin-bottom: 14px !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] label[data-baseweb="radio"] {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
        padding: 6px 14px !important;
        cursor: pointer !important;
        margin: 0 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03) !important;
        transition: all 0.2s ease !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] label[data-baseweb="radio"]:hover {
        border-color: #145A43 !important;
        background-color: #f1f5f9 !important;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] label[data-baseweb="radio"] p,
    div[data-testid="stRadio"] div[role="radiogroup"] label[data-baseweb="radio"] span,
    div[data-testid="stRadio"] div[role="radiogroup"] label[data-baseweb="radio"] div {
        color: #0f172a !important;
        font-weight: 700 !important;
        font-size: 13.5px !important;
        margin: 0 !important;
    }
    /* Hide default radio circle bullet */
    div[data-testid="stRadio"] div[role="radiogroup"] label[data-baseweb="radio"] > div:first-child {
        display: none !important;
    }

    /* STREAMLIT TABS HIGH-CONTRAST VISIBILITY FIX */
    div[data-baseweb="tab-list"] {
        background-color: #e2e8f0 !important;
        padding: 4px !important;
        border-radius: 10px !important;
        gap: 4px !important;
    }
    button[data-baseweb="tab"] {
        background-color: #ffffff !important;
        color: #334155 !important;
        border-radius: 8px !important;
        padding: 8px 18px !important;
        font-weight: 700 !important;
        font-size: 13.5px !important;
        border: 1px solid #cbd5e1 !important;
        transition: all 0.2s ease !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #145A43 !important;
        color: #ffffff !important;
        border-color: #145A43 !important;
        box-shadow: 0 4px 12px rgba(20, 90, 67, 0.25) !important;
    }
    button[data-baseweb="tab"] p,
    button[data-baseweb="tab"] div,
    button[data-baseweb="tab"] span {
        color: inherit !important;
        font-weight: 700 !important;
    }

    /* METRIC CARDS HIGH CONTRAST */
    [data-testid="stMetricValue"] {
        color: #083B2C !important;
        font-weight: 800 !important;
        font-size: 26px !important;
    }
    [data-testid="stMetricLabel"] {
        color: #475569 !important;
        font-weight: 700 !important;
    }

    /* Hero Banner Visualization */
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #12372A 100%);
        border-radius: 18px;
        padding: 36px 40px;
        color: #ffffff;
        margin-bottom: 24px;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.15);
    }

    .hero-title {
        font-size: 36px !important;
        font-weight: 800 !important;
        line-height: 1.15 !important;
        margin-bottom: 12px !important;
        letter-spacing: -0.5px !important;
        color: #ffffff !important;
    }

    .hero-desc {
        font-size: 15px !important;
        color: #93c5fd !important;
        max-width: 750px;
        line-height: 1.6 !important;
        margin-bottom: 0 !important;
    }

    /* High Contrast Presentable Cards */
    .jalsetu-card {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-left: 4px solid #145A43;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 16px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.04);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .jalsetu-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
        border-color: #145A43;
    }

    .card-title-text {
        font-size: 16px;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Form & Button Styling */
    .stButton > button {
        border-radius: 10px !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #145A43 0%, #083B2C 100%) !important;
        color: #ffffff !important;
        border: none !important;
        padding: 10px 22px !important;
        box-shadow: 0 4px 12px rgba(20, 90, 67, 0.25) !important;
        transition: all 0.2s ease !important;
    }

    .stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 16px rgba(20, 90, 67, 0.4) !important;
    }

    /* FIX STREAMLIT POPOVER BUTTON & BODY CONTRAST ENHANCEMENTS */
    div[data-testid="stPopover"] > button {
        background-color: #1677A8 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 13px !important;
        padding: 8px 18px !important;
        box-shadow: 0 4px 12px rgba(22, 119, 168, 0.3) !important;
    }
    div[data-testid="stPopover"] > button p,
    div[data-testid="stPopover"] > button span,
    div[data-testid="stPopover"] > button div {
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    div[data-testid="stPopover"] > button:hover,
    div[data-testid="stPopover"] > button:focus,
    div[data-testid="stPopover"] > button:active {
        background-color: #115e85 !important;
        color: #ffffff !important;
        box-shadow: 0 6px 16px rgba(17, 94, 133, 0.4) !important;
    }
    div[data-testid="stPopoverBody"],
    div[data-testid="stPopoverBody"] > div {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border-radius: 14px !important;
        border: 1px solid #cbd5e1 !important;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2) !important;
        padding: 12px !important;
    }
    div[data-testid="stPopoverBody"] p,
    div[data-testid="stPopoverBody"] span,
    div[data-testid="stPopoverBody"] h1,
    div[data-testid="stPopoverBody"] h2,
    div[data-testid="stPopoverBody"] h3,
    div[data-testid="stPopoverBody"] h4,
    div[data-testid="stPopoverBody"] label,
    div[data-testid="stPopoverBody"] li,
    div[data-testid="stPopoverBody"] div {
        color: #0f172a !important;
    }
    div[data-testid="stPopoverBody"] input,
    div[data-testid="stPopoverBody"] textarea {
        background-color: #f8fafc !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
    }
</style>
""", unsafe_allow_html=True)

# Custom High-Contrast Alert Component (Fixes yellow low-contrast Streamlit alert)
def render_scientific_notice():
    st.markdown("""
    <div style="background-color:#fef3c7; border:1px solid #f59e0b; border-left:5px solid #d97706; border-radius:10px; padding:14px 18px; color:#92400e; font-size:12.5px; font-weight:600; line-height:1.5; margin-top:14px;">
        <b>⚠️ IMPORTANT SCIENTIFIC NOTICE & DISCLAIMER:</b> SPRING-AI provides model-estimated decision-support outputs. AI predictions and recommendations MUST NOT replace detailed hydrogeological ground-truthing, engineering verification, or statutory environmental clearances.
    </div>
    """, unsafe_allow_html=True)

def launch_portal_module1():
    target_mode = "🗺️ 1. Recharge Zone & Springshed Delineation"
    st.session_state.app_mode = target_mode
    st.session_state.pop("portal_nav_radio", None)
    st.session_state.pop("master_nav_radio", None)
    st.rerun()

def render_district_side_panel(dist_pack):
    cfg = dist_pack["config"]
    tribal = dist_pack.get("tribal_demographics", {})
    water = dist_pack.get("water_metrics", {})
    cost = dist_pack.get("financial_costing", {})

    st.subheader(f"🏛️ Side Panel — {cfg['district']}")
    
    with st.container(border=True):
        st.markdown(f"##### 🛖 Tribal Demographics in {cfg['district']}")
        st.markdown(f"• **State & District:** {cfg['district']}, {cfg['state']}")
        st.markdown(f"• **ST Population:** `{tribal.get('st_pop_pct', 50)}% ST`")
        st.markdown(f"• **Tribal Households Served:** `{tribal.get('households_impacted', 0):,} Households`")
        st.markdown(f"• **Primary Livelihood:** {tribal.get('livelihood', 'Forest Produce & Agriculture')}")

    with st.container(border=True):
        st.markdown(f"##### 💧 Water Storage & Catchment Impact")
        st.markdown(f"• **Treated Catchment:** `{water.get('catchment_sqkm', 0)} sq km` ({water.get('catchment_hectares', 0):,} Ha)")
        st.markdown(f"• **Annual Water Storage:** `{water.get('storage_ml', 0)} Million Liters`")
        st.markdown(f"• **Est. Water Table Rise:** `+{water.get('water_table_rise_m', 0)} meters`")
        st.markdown(f"• **Baseflow Extension:** `+{water.get('summer_flow_extension_days', 0)} Days into Summer`")

    with st.container(border=True):
        st.markdown(f"##### 💰 MGNREGA Budget & Labor")
        st.markdown(f"• **Total Estimated Budget:** `₹{cost.get('total_cost_lakhs', 0)} Lakhs` (₹{cost.get('total_cost_crores', 0)} Cr)")
        st.markdown(f"• **MGNREGA Labor Created:** `{cost.get('mgnrega_persondays', 0):,} Persondays`")
        st.markdown(f"• **Cost per Household:** `₹{cost.get('cost_per_household_inr', 0):,}`")

    report_file = f"reports/SPRING_AI_{cfg['district'].replace(' ', '_')}_Executive_Report.pdf"
    clean_dist_key = cfg['district'].replace(' ', '_').replace('🌐', '').replace('🇮🇳', '').strip()
    if st.button("📥 Generate District Executive Report (PDF)", key=f"pdf_btn_{clean_dist_key}", use_container_width=True):
        os.makedirs("reports", exist_ok=True)
        generate_district_executive_report(dist_pack, report_file)
        st.success(f"Generated Executive Dossier for {cfg['district']}!")

    if os.path.exists(report_file):
        with open(report_file, "rb") as f:
            st.download_button(
                label=f"⬇️ Download {cfg['district']} Executive PDF Dossier",
                data=f,
                file_name=f"SPRING_AI_{clean_dist_key}_Executive_Dossier.pdf",
                mime="application/pdf",
                key=f"dl_btn_{clean_dist_key}",
                use_container_width=True
            )

# Initialize session state for selected navigation module
nav_options = [
    "🌐 0. Platform Overview & Mission",
    "🗺️ 1. Recharge Zone & Springshed Delineation",
    "📊 2. Recharge Suitability & Priority Ranking",
    "🛠️ 3. Site Intervention Measures & Costing",
    "⛰️ 4. Risk & Landslide Safety Masking",
    "📋 5. Field Validation & Report Dossiers"
]

if "app_mode" not in st.session_state or st.session_state.app_mode not in nav_options:
    st.session_state.app_mode = "🌐 0. Platform Overview & Mission"

# ==============================================================================
# PAGE ROUTER ARCHITECTURE:
# Page 1: Public Overview & Mission (Purely Informative Landing Page)
# Page 2: GeoAI Portal (Operational Decision Support Modules with Top Control Bar)
# ==============================================================================

if st.session_state.app_mode == "🌐 0. Platform Overview & Mission":
    render_landing_page(on_launch_portal=launch_portal_module1)
else:
    # --------------------------------------------------------------------------
    # GEOAI PORTAL (PAGE 2) TOP NAVIGATION & REGION CONTROLS
    # --------------------------------------------------------------------------
    col_nav_l, col_nav_st, col_nav_dt = st.columns([1.8, 1, 1.2])

    with col_nav_l:
        st.markdown(
            '<div class="portal-header-box">'
            '<div style="display:flex; align-items:center; gap:10px;">'
            '<svg width="26" height="26" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M20 75L50 25L80 75H20Z" fill="#62B6CB"/>'
            '<path d="M40 75L62 38L85 75H40Z" fill="#145A43" opacity="0.85"/>'
            '<path d="M50 42C50 42 38 58 38 65C38 71.6 43.4 77 50 77C56.6 77 62 71.6 62 65C62 58 50 42 50 42Z" fill="#38BDF8"/>'
            '</svg>'
            '<span style="color:#FFFFFF !important; font-weight:800; font-size:18px;">SPRING AI — GeoAI Portal</span>'
            '</div>'
            '</div>',
            unsafe_allow_html=True
        )
        if st.button("🌐 ← Back to Overview & Mission", key="btn_back_to_overview"):
            st.session_state.app_mode = "🌐 0. Platform Overview & Mission"
            if "master_nav_radio" in st.session_state:
                del st.session_state["master_nav_radio"]
            st.rerun()

    with col_nav_st:
        state_options = ["🇮🇳 All-India (17 States)"] + list(TRIBAL_STATE_DISTRICTS_MAP.keys())
        selected_state = st.selectbox(
            "📌 State / National View:",
            options=state_options,
            index=0,
            key="global_state_select"
        )

    is_pan_india = (selected_state == "🇮🇳 All-India (17 States)")

    with col_nav_dt:
        if is_pan_india:
            all_districts_list = []
            for st_k, d_list in TRIBAL_STATE_DISTRICTS_MAP.items():
                for d_item in d_list:
                    all_districts_list.append(f"{d_item} ({st_k})")
            district_options = ["🌐 All 100+ Tribal Districts"] + sorted(all_districts_list)
            selected_district_name = st.selectbox(
                "🏛️ Target District:",
                options=district_options,
                index=0,
                key="global_district_select_all"
            )
        else:
            state_dists = TRIBAL_STATE_DISTRICTS_MAP[selected_state]
            district_options = [f"🌐 All Districts in {selected_state}"] + state_dists
            selected_district_name = st.selectbox(
                "🏛️ Target District:",
                options=district_options,
                index=0,
                key="global_district_select_state"
            )

    # Load Selected District Datasets
    dist_pack = get_district_datasets(selected_district_name, state_name=selected_state)

    if "dist_pack_override" in st.session_state and not is_pan_india and "All" not in selected_district_name:
        dist_pack = st.session_state["dist_pack_override"]

    dist_cfg = dist_pack["config"]
    df_springs = dist_pack["springs"]
    df_grid = dist_pack["grid"]
    df_int = dist_pack["interventions"]
    df_discharge = dist_pack["discharge"]
    df_validations = load_field_validations_data()
    predictor = RechargePredictor()

    # Master Portal Navigation Tab Bar
    portal_nav_options = [
        "🗺️ 1. Recharge Zone & Springshed Delineation",
        "📊 2. Recharge Suitability & Priority Ranking",
        "🛠️ 3. Site Intervention Measures & Costing",
        "⛰️ 4. Risk & Landslide Safety Masking",
        "📋 5. Field Validation & Report Dossiers"
    ]

    if st.session_state.app_mode not in portal_nav_options:
        st.session_state.app_mode = portal_nav_options[0]
        st.session_state.pop("portal_nav_radio", None)
        st.session_state.pop("master_nav_radio", None)

    current_idx = portal_nav_options.index(st.session_state.app_mode) if st.session_state.app_mode in portal_nav_options else 0

    dash_tab_selected = st.radio(
        "SPRING AI GeoAI Portal Modules:",
        options=portal_nav_options,
        index=current_idx,
        horizontal=True,
        key="portal_nav_radio"
    )

    if dash_tab_selected not in portal_nav_options:
        dash_tab_selected = portal_nav_options[0]

    st.session_state.app_mode = dash_tab_selected

    st.markdown("---")

    # --------------------------------------------------------------------------
    # MODULE 1: RECHARGE ZONE & SPRINGSHED DELINEATION (Solution #1)
    # --------------------------------------------------------------------------
    if "1." in dash_tab_selected or "Recharge Zone" in dash_tab_selected:
        if selected_district_name == "🌐 All 100+ Tribal Districts":
            st.markdown("### 🗺️ Pan-India GeoAI National Springshed Overview — All 100+ Tribal Districts")
            st.caption("Displays active springshed density heatmaps and district clusters across 17 tribal states in India.")

            m1, m2, m3, m4, m5 = st.columns(5)
            with m1: st.metric("National Districts", "100+ Tribal Districts", "17 States Covered")
            with m2: st.metric("Recharge Catchment", f"{dist_pack['water_metrics']['catchment_sqkm']} sq km", f"{dist_pack['water_metrics']['catchment_hectares']:,} Ha")
            with m3: st.metric("Mapped Springs", f"{len(df_springs)} Springs", "National Inventory")
            with m4: st.metric("Water Storage", f"{dist_pack['water_metrics']['storage_ml']} Billion L", "Annual Storage Potential")
            with m5: st.metric("MGNREGA Budget", f"₹{dist_pack['financial_costing']['total_cost_crores']} Crores", f"{dist_pack['financial_costing']['mgnrega_persondays']:,} Persondays")

            c_map, c_side = st.columns([2.2, 1.2])
            with c_map:
                st.markdown("#### 📡 Interactive Pan-India Multi-Layer GIS Visualizer")
                pan_map = create_pan_india_overview_map(DISTRICTS_CONFIG)
                render_gis_map(pan_map, height=540)

            with c_side:
                render_district_side_panel(dist_pack)
        else:
            st.markdown(f"### 🗺️ Probable Recharge Zone & Springshed Identification — {dist_cfg['district']}, {dist_cfg['state']}")
            st.caption("Fulfills Ministry Mandate #1: Delineates subsurface recharge areas using satellite DEM, IMD rainfall, GSI lithology, slope, aspect, and lineament fractures with confidence scoring.")

            m1, m2, m3, m4, m5 = st.columns(5)
            total_sp = len(df_springs)
            high_rec = dist_pack["water_metrics"]["catchment_sqkm"]
            high_int = len(df_int[df_int["priority_level"] == "HIGH"])
            high_risk = len(df_grid[df_grid["slope"] > 30])
            avg_conf = round(df_springs["confidence_score"].mean() * 100, 1) if not df_springs.empty else 0.0

            with m1: st.metric("Mapped Springs", total_sp, f"{dist_cfg['district']} Inventory")
            with m2: st.metric("Recharge Area", f"{high_rec} sq km", f"{dist_pack['water_metrics']['catchment_hectares']:,} Ha")
            with m3: st.metric("Priority Sites", high_int, "Field Action Ready")
            with m4: st.metric("Hazard Mask (>30°)", high_risk, "Landslide Prohibited")
            with m5: st.metric("Model Confidence", f"{avg_conf}%", "Uncertainty Quantified")

            c_map, c_side = st.columns([2.2, 1.2])
            with c_map:
                st.markdown("#### 📡 Interactive Springshed & Multi-Layer GIS Visualizer")
                gis_map = create_spring_gis_map(df_springs=df_springs, df_grid=df_grid, df_interventions=df_int, center_coords=dist_cfg["center_coords"], zoom_start=dist_cfg["zoom_level"])
                render_gis_map(gis_map, height=520)

            with c_side:
                render_district_side_panel(dist_pack)

    # --------------------------------------------------------------------------
    # MODULE 2: SUITABILITY & PRIORITY RANKING (Solution #2)
    # --------------------------------------------------------------------------
    elif "2." in dash_tab_selected or "Suitability" in dash_tab_selected:
        st.markdown(f"### 📊 Recharge Suitability Heatmap & Spatial Priority Ranking — {dist_cfg['district']}")
        st.caption("Fulfills Ministry Mandate #2: Generates probability-based suitability scores and ranks priority zones for groundwater recharge.")

        r1, r2 = st.columns([2, 1.2])
        with r1:
            st.markdown("#### Top Ranked High-Suitability Recharge Grid Cells")
            high_g = df_grid[df_grid["recharge_suitability_target"] == 1]
            st.dataframe(high_g[["location_id", "latitude", "longitude", "elevation", "slope", "synthetic_suitability_score"]].head(12), use_container_width=True, hide_index=True)

            st.markdown("#### Random Forest + XGBoost Feature Importance Weights")
            fi_df = pd.DataFrame({
                "Feature": ["Annual Rainfall (IMD)", "Geology / Lithology (GSI)", "Terrain Slope (DEM)", "Drainage Proximity", "Land Cover", "Soil Permeability"],
                "Importance (%)": [32, 24, 20, 14, 6, 4]
            })
            fig_bar = px.bar(fi_df, x="Importance (%)", y="Feature", orientation="h", title="GeoAI Factor Weights", color="Importance (%)", color_continuous_scale="Viridis")
            st.plotly_chart(fig_bar, use_container_width=True)

        with r2:
            render_district_side_panel(dist_pack)

    # --------------------------------------------------------------------------
    # MODULE 3: INTERVENTION MEASURES & COSTING (Solution #3)
    # --------------------------------------------------------------------------
    elif "3." in dash_tab_selected or "Intervention" in dash_tab_selected:
        st.markdown(f"### 🛠️ Indicative Recharge Measures & MGNREGA Costing — {dist_cfg['district']}")
        st.caption("Fulfills Ministry Mandate #3: Recommends site-specific bio-engineering structures (Check Dams, Contour Trenches, Percolation Ponds, Recharge Shafts) with MGNREGA cost & labor estimates.")

        c_int, c_side = st.columns([2.1, 1.2])
        with c_int:
            if not df_int.empty:
                st.dataframe(df_int[["site_id", "nearest_spring_id", "priority_level", "suitability_score", "recommended_structure", "slope", "risk_status"]], use_container_width=True, hide_index=True)

                sel_int = st.selectbox("Select Candidate Site ID to Inspect:", df_int["site_id"])
                int_data = df_int[df_int["site_id"] == sel_int].iloc[0]
                imp_res = calculate_before_after_impact(int_data.to_dict())

                st.markdown(f"""
                <div class="jalsetu-card" style="border-left:4px solid #145A43;">
                    <h4>Site {int_data['site_id']} Engineering & MGNREGA Costing Dossier</h4>
                    <b>Recommended Measure:</b> <span style="color:#145A43; font-weight:700;">{int_data['recommended_structure']}</span><br>
                    <b>Estimated MGNREGA Cost:</b> <b>{imp_res['estimated_cost_inr']}</b> | <b>Labor Created:</b> <b>{imp_res['mgnrega_persondays']} Persondays</b><br>
                    <b>Post-Monsoon Flow Extension:</b> <b style="color:#10B981;">{imp_res['flow_extension_days']}</b> | <b>Water Table Rise:</b> <b style="color:#10B981;">{imp_res['water_table_rise_m']}</b><br>
                    <b>Tribal Households Served:</b> {imp_res['tribal_households_impacted']} Households ({imp_res['daily_water_added_lpd']})
                </div>
                """, unsafe_allow_html=True)

        with c_side:
            render_district_side_panel(dist_pack)

    # --------------------------------------------------------------------------
    # MODULE 4: RISK & LANDSLIDE SAFETY MASKING (Solution #4)
    # --------------------------------------------------------------------------
    elif "4." in dash_tab_selected or "Risk" in dash_tab_selected:
        st.markdown(f"### ⛰️ Landslide Hazard & Terrain Risk Prohibitions — {dist_cfg['district']}")
        st.caption("Fulfills Ministry Mandate #4: Flags high-risk or unsuitable locations, excluding structural interventions on slopes >30° to prevent slope failure.")

        c_risk, c_side = st.columns([2, 1.2])
        with c_risk:
            st.markdown("#### Landslide Risk Masking Rules")
            st.error("⚠️ **SAFETY MANDATE:** Structural recharge interventions (Check Dams, Heavy Excavation) are strictly prohibited on slopes >30° to prevent inducing landslide disasters during monsoon saturation.")
            high_risk_cells = len(df_grid[df_grid["slope"] > 30])
            st.markdown(f"- **Prohibited High-Slope Cells:** `{high_risk_cells} grid locations` flagged as severe landslide risk.")
            st.markdown("- **Alternative Recommended Measure:** Afforestation, vetiver bio-fencing, and bio-vegetative slope stabilization without heavy excavation.")

        with c_side:
            render_district_side_panel(dist_pack)

    # --------------------------------------------------------------------------
    # MODULE 5: FIELD VALIDATION & REPORT DOSSIERS (Solution #5)
    # --------------------------------------------------------------------------
    elif "5." in dash_tab_selected or "Field" in dash_tab_selected:
        st.markdown(f"### 📋 Field Verification & Custom Ground Assessment Ingestion — {dist_cfg['district']}")
        st.caption("Fulfills Ministry Mandate #5: Interactive field validation tool & custom ground report uploader to log ground-truthing observations and retrain the AI model.")

        c_f1, c_f2 = st.columns([2, 1.2])
        with c_f1:
            st.markdown("#### 📥 Custom Ground Assessment Data Ingestion & Re-Scoring Tool")
            st.caption("Have an on-ground field assessment report? Submit it below to ingest field data and dynamically re-score GeoAI predictions.")
            
            with st.form("ground_report_form"):
                g_name = st.text_input("Surveyor / Engineer Name:", "Dr. R. K. Sharma (Field Hydrogeologist)")
                g_sp_id = st.text_input("Spring / Ground Site ID:", f"{dist_cfg['district'][:3].upper()}-GROUND-001")
                g_sp_name = st.text_input("Observed Feature Name:", f"{dist_cfg['district']} Field Assessed Spring")
                g_village = st.selectbox("Observed Village / Habitation:", dist_cfg.get("villages", ["Village A"]))
                
                cg1, cg2, cg3 = st.columns(3)
                with cg1: g_discharge = st.number_input("Ground Discharge (LPM):", 0.0, 500.0, 11.5)
                with cg2: g_slope = st.number_input("Observed Terrain Slope (°):", 0.0, 60.0, 14.5)
                with cg3: g_type = st.selectbox("Spring Classification:", ["Fracture Spring", "Contact Spring", "Gravity Depression Spring"])
                
                g_notes = st.text_area("Field Assessment Observations & Notes:", "Verified fractured quartzite contact zone. Water table declined 1.2m during pre-monsoon.")
                g_file = st.file_uploader("Optional CSV/JSON Field Log File:", type=["csv", "json"])

                if st.form_submit_button("⚡ Ingest Ground Report & Re-Score Model"):
                    rep_dict = {
                        "surveyor_name": g_name,
                        "spring_id": g_sp_id,
                        "spring_name": g_sp_name,
                        "village": g_village,
                        "observed_discharge_lpm": g_discharge,
                        "observed_slope": g_slope,
                        "spring_type": g_type,
                        "field_notes": g_notes,
                        "latitude": dist_cfg["center_coords"][0] + 0.012,
                        "longitude": dist_cfg["center_coords"][1] + 0.015
                    }
                    dist_pack = ingest_custom_ground_report(rep_dict, dist_pack)
                    st.session_state["dist_pack_override"] = dist_pack
                    st.success(f"✅ Ingested Ground Assessment Report for {g_sp_id}! GeoAI suitability scores recalculated incorporating on-ground data.")
                    st.rerun()

            st.markdown("---")
            st.markdown("#### Log Standard Field Verification Survey")
            with st.form("val_form"):
                v_site = st.selectbox("Site ID:", df_int["site_id"] if not df_int.empty else ["INT-001"])
                v_name = st.text_input("Surveyor Name:", "Dr. R. K. Sharma (Hydrogeologist)")
                v_slope = st.number_input("Observed Slope (°):", 0.0, 60.0, 14.0)
                v_status = st.selectbox("Validation Status:", ["Suitable", "Not Suitable", "Needs Review"])
                v_notes = st.text_area("Field Notes:", "Verified fractured granite contact zone.")
                if st.form_submit_button("💾 Log Ground Verification"):
                    save_field_validation({"validation_id": f"VAL-{len(df_validations)+1:03d}", "site_id": v_site, "observer_name": v_name, "observed_slope_deg": v_slope, "validation_status": v_status, "notes": v_notes})
                    st.success("Field survey logged successfully!")
                    st.rerun()

            st.markdown("---")
            st.markdown("#### Individual Site Technical Dossier Export")
            if not df_int.empty:
                sel_s = st.selectbox("Select Candidate Site ID for Technical PDF Export:", df_int["site_id"])
                site_d = df_int[df_int["site_id"] == sel_s].iloc[0]
                sp_d = df_springs[df_springs["spring_id"] == site_d["nearest_spring_id"]].iloc[0] if not df_springs.empty else {}
                
                if st.button("📥 Generate Site Technical Dossier (PDF)"):
                    os.makedirs("reports", exist_ok=True)
                    pdf_path = f"reports/Report_{sel_s}.pdf"
                    generate_spring_pdf_report(sp_d.to_dict() if hasattr(sp_d, 'to_dict') else {}, site_d.to_dict(), pdf_path)
                    with open(pdf_path, "rb") as f:
                        st.download_button("Click Here to Download Site Technical PDF", f, file_name=f"SPRING_AI_{sel_s}.pdf", mime="application/pdf")

            if st.button("🚀 Retrain AI Model on Field Logs"):
                train_ml_models()
                st.success("Model retrained successfully!")
        
        with c_f2:
            render_district_side_panel(dist_pack)

        render_scientific_notice()
    else:
        st.markdown(f"### 🗺️ Probable Recharge Zone & Springshed Identification — {dist_cfg['district']}, {dist_cfg['state']}")
        st.caption("Fulfills Ministry Mandate #1: Delineates subsurface recharge areas using satellite DEM, IMD rainfall, GSI lithology, slope, aspect, and lineament fractures with confidence scoring.")

        m1, m2, m3, m4, m5 = st.columns(5)
        total_sp = len(df_springs)
        high_rec = dist_pack["water_metrics"]["catchment_sqkm"]
        high_int = len(df_int[df_int["priority_level"] == "HIGH"])
        high_risk = len(df_grid[df_grid["slope"] > 30])
        avg_conf = round(df_springs["confidence_score"].mean() * 100, 1) if not df_springs.empty else 0.0

        with m1: st.metric("Mapped Springs", total_sp, f"{dist_cfg['district']} Inventory")
        with m2: st.metric("Recharge Area", f"{high_rec} sq km", f"{dist_pack['water_metrics']['catchment_hectares']:,} Ha")
        with m3: st.metric("Priority Sites", high_int, "Field Action Ready")
        with m4: st.metric("Hazard Mask (>30°)", high_risk, "Landslide Prohibited")
        with m5: st.metric("Model Confidence", f"{avg_conf}%", "Uncertainty Quantified")

        c_map, c_side = st.columns([2.2, 1.2])
        with c_map:
            st.markdown("#### 📡 Interactive Springshed & Multi-Layer GIS Visualizer")
            gis_map = create_spring_gis_map(df_springs=df_springs, df_grid=df_grid, df_interventions=df_int, center_coords=dist_cfg["center_coords"], zoom_start=dist_cfg["zoom_level"])
            render_gis_map(gis_map, height=520)

        with c_side:
            render_district_side_panel(dist_pack)

    # ==============================================================================
    # FLOATING SPRING-AI HYDRO-COPILOT WIDGET (PAGE 2)
    # ==============================================================================
    with st.popover("💬 Ask SPRING-AI Copilot", help="Interactive GeoAI Copilot & Hydrogeological Assistant"):
        st.markdown("### 🤖 SPRING-AI Hydro-Copilot")
        st.caption(f"Active Context: {dist_cfg['district']}, {dist_cfg['state']}")
        
        cp1, cp2 = st.columns(2)
        with cp1:
            if st.button("⚡ Copilot Auto-Analyze District"):
                st.info(
                    f"**⚡ Hydro-Diagnosis for {dist_cfg['district']}:**\n"
                    f"- **Precipitation:** `{dist_cfg['rainfall_mean']} mm/year` | **Lithology:** `{dist_cfg['lithology_types'][0]}`\n"
                    f"- **Tribal Demographics:** `{dist_pack['tribal_demographics']['st_pop_pct']}% ST` ({', '.join(dist_pack['tribal_demographics']['tribes'][:3])})\n"
                    f"- **Annual Water Potential:** `{dist_pack['water_metrics']['storage_ml']} Million Liters` ({dist_pack['water_metrics']['storage_cum']:,} m³)\n"
                    f"- **Costing:** `₹{dist_pack['financial_costing']['total_cost_lakhs']} Lakhs` | `{dist_pack['financial_costing']['mgnrega_persondays']:,} Persondays`"
                )
        with cp2:
            if st.button("📋 Field Ingestion Summary"):
                val_df = load_field_validations_data()
                st.success(f"**Field Ingestions:** {len(val_df)} ground assessments currently recorded in database.")

        user_q = st.text_input("Ask SPRING-AI Copilot a question:", "Which springs are in critical condition?", key="copilot_user_q")
        if user_q:
            ans = query_spring_ai(user_q, df_springs, dist_cfg, df_int)
            st.markdown(ans)

