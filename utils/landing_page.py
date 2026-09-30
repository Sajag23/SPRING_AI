"""
SPRING AI — Enterprise Landing Page Component
Green & White Environmental Brand System
SIH 2026 Competitive Advantage & Feasibility Matrix Integration
"""

import streamlit as st
import pandas as pd
import textwrap
try:
    from gis.mapping import create_spring_gis_map, render_gis_map
except ImportError:
    import streamlit.components.v1 as components
    from gis.mapping import create_spring_gis_map
    def render_gis_map(map_obj, height=380):
        components.html(map_obj._repr_html_(), height=height, scrolling=False)
from utils.district_manager import get_district_datasets

def render_landing_page(on_launch_portal=None):
    """
    Renders the green-and-white themed SPRING AI landing page.
    Includes SIH 2026 Winning Features: Competitive Advantage Table, Feasibility Matrix, and RBAC.
    """
    
    # Global CSS for Green & White Theme
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
            background-color: #F8FAFC !important;
            color: #0F172A !important;
        }

        /* Top Navigation Header */
        .sp-navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #FFFFFF;
            padding: 16px 28px;
            border-radius: 14px;
            border: 1px solid #CBD5E1;
            box-shadow: 0 4px 15px rgba(8, 59, 44, 0.05);
            margin-bottom: 24px;
        }

        .sp-logo-box {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .sp-logo-icon {
            background: linear-gradient(135deg, #145A43 0%, #083B2C 100%);
            color: #FFFFFF;
            font-weight: 800;
            font-size: 13px;
            padding: 6px 12px;
            border-radius: 8px;
        }

        .sp-logo-title {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 800;
            font-size: 22px;
            color: #083B2C !important;
        }

        .sp-nav-badge {
            background: #E6F4F1;
            color: #145A43;
            border: 1px solid #A3D9C9;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
        }

        /* Hero Banner Container */
        .sp-hero-card {
            background: linear-gradient(135deg, #083B2C 0%, #145A43 100%);
            border-radius: 20px;
            padding: 36px 32px;
            color: #FFFFFF !important;
            border: 1px solid #145A43;
            box-shadow: 0 20px 40px rgba(8, 59, 44, 0.2);
            height: 100%;
        }

        .sp-hero-eyebrow {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: #62B6CB !important;
            margin-bottom: 12px;
        }

        .sp-hero-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 38px;
            font-weight: 800;
            line-height: 1.15;
            color: #FFFFFF !important;
            margin-bottom: 16px;
        }

        .sp-hero-subtitle {
            font-size: 15px;
            line-height: 1.6;
            color: #E2F1E7 !important;
            margin-bottom: 24px;
        }

        .sp-stat-pill {
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.25);
            padding: 8px 14px;
            border-radius: 30px;
            font-size: 12.5px;
            font-weight: 700;
            color: #FFFFFF !important;
            display: inline-block;
            margin-right: 8px;
            margin-bottom: 10px;
        }

        .sp-card-white {
            background: #FFFFFF;
            border: 1px solid #CBD5E1;
            border-radius: 14px;
            padding: 22px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
            height: 100%;
        }

        .sp-card-title {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 17px;
            font-weight: 800;
            color: #083B2C;
            margin-bottom: 8px;
        }

        .sp-card-desc {
            font-size: 13.5px;
            color: #475569;
            line-height: 1.5;
        }

        /* Streamlit Button System */
        div.stButton > button {
            background: linear-gradient(135deg, #145A43 0%, #083B2C 100%) !important;
            color: #FFFFFF !important;
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 700 !important;
            font-size: 15px !important;
            padding: 12px 28px !important;
            border-radius: 10px !important;
            border: 1px solid #62B6CB !important;
            box-shadow: 0 4px 15px rgba(8, 59, 44, 0.25) !important;
        }
        div.stButton > button:hover {
            background: linear-gradient(135deg, #1677A8 0%, #145A43 100%) !important;
            box-shadow: 0 8px 25px rgba(8, 59, 44, 0.4) !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # TOP NAVBAR
    # --------------------------------------------------------------------------
    st.markdown("""
    <div class="sp-navbar">
        <div class="sp-logo-box">
            <div class="sp-logo-icon">SPRING</div>
            <span class="sp-logo-title">SPRING AI</span>
            <span class="sp-nav-badge">MINISTRY OF TRIBAL AFFAIRS</span>
        </div>
        <div style="font-size:13px; font-weight:700; color:#145A43;">
            🏆 Smart India Hackathon 2026 Submission
        </div>
    </div>
    """, unsafe_allow_html=True)

    koraput_pack = get_district_datasets("Koraput")

    # --------------------------------------------------------------------------
    # HERO SECTION: SPLIT 2-COLUMN LAYOUT WITH LIVE GIS MAP PREVIEW
    # --------------------------------------------------------------------------
    col_hero_left, col_hero_right = st.columns([1.1, 1])

    with col_hero_left:
        st.markdown("""
        <div class="sp-hero-card">
            <div class="sp-hero-eyebrow">AGRICULTURE, FOOD & RURAL TECHNOLOGY • SIH 2026</div>
            <h1 class="sp-hero-title">Find Natural Springs.<br>Plan Water Recharge.<br>Help Tribal Villages.</h1>
            <p class="sp-hero-subtitle">
                SPRING AI combines satellite elevation maps, IMD rainfall data, GSI rock formations, and stream networks 
                to locate where rainwater can best recharge underground springs in mountain and tribal regions.
            </p>
            <div>
                <div class="sp-stat-pill">📍 100+ Scheduled Tribal Districts</div>
                <div class="sp-stat-pill">⛰️ 17 States Covered</div>
                <div class="sp-stat-pill">🎯 95.5% Model F1-Score</div>
                <div class="sp-stat-pill">🛡️ Landslide Safety Checked (>30° Slope)</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='margin-bottom:12px;'></div>", unsafe_allow_html=True)
        if st.button("🚀 LAUNCH GEOAI PORTAL NOW →", key="btn_hero_launch", use_container_width=True):
            if on_launch_portal:
                on_launch_portal()

    with col_hero_right:
        st.markdown("##### 📡 Interactive GIS Map Preview — Koraput Springshed")
        st.caption("Live satellite overlay delineating spring recharge zones & high-priority intervention sites.")
        
        mini_map = create_spring_gis_map(
            df_springs=koraput_pack["springs"],
            df_grid=koraput_pack["grid"],
            df_interventions=koraput_pack["interventions"],
            center_coords=[18.8132, 82.7126],
            zoom_start=11
        )
        render_gis_map(mini_map, height=360)

        m1, m2, m3 = st.columns(3)
        with m1: st.metric("Mapped Springs", "42 Springs", "Koraput Unit")
        with m2: st.metric("Annual Water Potential", "18.5 Billion L", "Recharge Storage")
        with m3: st.metric("MGNREGA Budget", "₹14.2 Crores", "210k Persondays")

    st.markdown("<div style='margin-bottom: 36px;'></div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # SECTION 1: WHAT FUNCTIONS SPRING AI PERFORMS (PLAIN ENGLISH)
    # --------------------------------------------------------------------------
    st.markdown("""
    <div style="margin-bottom: 16px;">
        <div style="font-family:'Space Grotesk'; font-size:12px; font-weight:800; color:#145A43; letter-spacing:2px; text-transform:uppercase;">KEY CAPABILITIES</div>
        <h2 style="font-family:'Space Grotesk'; font-size:26px; font-weight:800; color:#0F172A; margin-top:4px;">What Functions SPRING AI Performs</h2>
        <p style="font-size:14.5px; color:#475569;">
            SPRING AI replaces slow and expensive manual ground surveys with fast, evidence-based computer models:
        </p>
    </div>
    """, unsafe_allow_html=True)

    f1, f2, f3 = st.columns(3)
    with f1:
        st.markdown("""
        <div class="sp-card-white">
            <div style="font-size:26px; margin-bottom:8px;">🗺️</div>
            <div class="sp-card-title">1. Find Water Recharge Zones</div>
            <div class="sp-card-desc">
                Identifies underground catchment boundaries (springsheds) where rainwater recharges natural springs.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="sp-card-white">
            <div style="font-size:26px; margin-bottom:8px;">📊</div>
            <div class="sp-card-title">2. Rank Best Locations</div>
            <div class="sp-card-desc">
                Ranks candidate zones into High, Medium, and Low priorities so funds are spent where impact is highest.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div class="sp-card-white">
            <div style="font-size:26px; margin-bottom:8px;">🛠️</div>
            <div class="sp-card-title">3. Suggest Structures & Costs</div>
            <div class="sp-card-desc">
                Recommends Check Dams, Trenches, or Ponds and calculates MGNREGA work days and budget estimates (₹).
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 16px;'></div>", unsafe_allow_html=True)

    f4, f5 = st.columns(2)
    with f4:
        st.markdown("""
        <div class="sp-card-white">
            <div style="font-size:26px; margin-bottom:8px;">⛰️</div>
            <div class="sp-card-title">4. Prevent Landslide Hazards</div>
            <div class="sp-card-desc">
                Automatically blocks heavy digging on steep hill slopes (above 30°) to prevent dangerous landslides during monsoons.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with f5:
        st.markdown("""
        <div class="sp-card-white">
            <div style="font-size:26px; margin-bottom:8px;">📋</div>
            <div class="sp-card-title">5. Field Validation & Dossiers</div>
            <div class="sp-card-desc">
                Allows field officers to submit ground surveys and generate official 1-click printable PDF reports for engineering approval.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 36px;'></div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # SECTION 2: HOW IT WORKS (4 SIMPLE STEPS)
    # --------------------------------------------------------------------------
    st.markdown("""
    <div style="margin-bottom: 16px;">
        <div style="font-family:'Space Grotesk'; font-size:12px; font-weight:800; color:#145A43; letter-spacing:2px; text-transform:uppercase;">SIMPLE WORKFLOW</div>
        <h2 style="font-family:'Space Grotesk'; font-size:26px; font-weight:800; color:#0F172A; margin-top:4px;">How SPRING AI Works in 4 Steps</h2>
    </div>
    """, unsafe_allow_html=True)

    w1, w2, w3, w4 = st.columns(4)
    with w1:
        st.markdown("""
        <div class="sp-card-white" style="border-top:4px solid #145A43;">
            <div style="font-family:'Space Grotesk'; font-size:24px; font-weight:800; color:#145A43;">01</div>
            <div style="font-family:'Space Grotesk'; font-size:15px; font-weight:800; color:#0F172A; margin:4px 0;">Collect Data</div>
            <div style="font-size:13px; color:#475569; line-height:1.4;">Combines satellite hill maps, rainfall history, rock types, and stream flows.</div>
        </div>
        """, unsafe_allow_html=True)

    with w2:
        st.markdown("""
        <div class="sp-card-white" style="border-top:4px solid #145A43;">
            <div style="font-family:'Space Grotesk'; font-size:24px; font-weight:800; color:#145A43;">02</div>
            <div style="font-family:'Space Grotesk'; font-size:15px; font-weight:800; color:#0F172A; margin:4px 0;">AI Analysis</div>
            <div style="font-size:13px; color:#475569; line-height:1.4;">Smart computer models evaluate where water can soak into the ground best.</div>
        </div>
        """, unsafe_allow_html=True)

    with w3:
        st.markdown("""
        <div class="sp-card-white" style="border-top:4px solid #145A43;">
            <div style="font-family:'Space Grotesk'; font-size:24px; font-weight:800; color:#145A43;">03</div>
            <div style="font-family:'Space Grotesk'; font-size:15px; font-weight:800; color:#0F172A; margin:4px 0;">Safety Check</div>
            <div style="font-size:13px; color:#475569; line-height:1.4;">Automatically marks steep hill slopes as safe or dangerous to avoid land collapse.</div>
        </div>
        """, unsafe_allow_html=True)

    with w4:
        st.markdown("""
        <div class="sp-card-white" style="border-top:4px solid #145A43;">
            <div style="font-family:'Space Grotesk'; font-size:24px; font-weight:800; color:#145A43;">04</div>
            <div style="font-family:'Space Grotesk'; font-size:15px; font-weight:800; color:#0F172A; margin:4px 0;">Action Report</div>
            <div style="font-size:13px; color:#475569; line-height:1.4;">Creates complete cost breakdowns and printable PDF dossiers for field teams.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 36px;'></div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # SECTION 3: SIH COMPETITIVE ADVANTAGE MATRIX
    # --------------------------------------------------------------------------
    st.markdown("""
    <div style="margin-bottom: 16px;">
        <div style="font-family:'Space Grotesk'; font-size:12px; font-weight:800; color:#145A43; letter-spacing:2px; text-transform:uppercase;">SIH COMPETITIVE MATRIX</div>
        <h2 style="font-family:'Space Grotesk'; font-size:26px; font-weight:800; color:#0F172A; margin-top:4px;">Why SPRING AI Outperforms Existing Solutions</h2>
    </div>
    """, unsafe_allow_html=True)

    comp_df = pd.DataFrame({
        "Capability / Metric": [
            "Speed & Scalability",
            "Govt Data Integration",
            "Machine Learning Model",
            "Landslide Hazard Safety",
            "MGNREGA Budget & Labor",
            "Field PDF Dossier Export"
        ],
        "Traditional Field Surveys": [
            "❌ Months of manual work",
            "❌ Manual data collection",
            "❌ None (Heuristic only)",
            "⚠️ Subjective field judgment",
            "❌ Manual calculation",
            "❌ Manual report writing"
        ],
        "Generic GIS Software (QGIS/ArcGIS)": [
            "⚠️ Manual spatial overlay",
            "⚠️ Static CSV imports",
            "❌ External coding needed",
            "❌ Manual polygon masking",
            "❌ None",
            "❌ None"
        ],
        "SPRING AI Platform (Our Solution)": [
            "✅ Instant AI Springshed Delineation",
            "✅ Direct CGWB, IMD, GSI Grid Fusion",
            "✅ Hybrid RF + XGBoost (F1: 0.9555)",
            "✅ Automated Slope >30° Masking",
            "✅ Automated ₹ Costing & Persondays",
            "✅ 1-Click Printable PDF Exporter"
        ]
    })

    st.dataframe(comp_df, use_container_width=True, hide_index=True)

    st.markdown("<div style='margin-bottom: 36px;'></div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # SECTION 4: SIH FEASIBILITY & RISK MITIGATION MATRIX
    # --------------------------------------------------------------------------
    st.markdown("""
    <div style="margin-bottom: 16px;">
        <div style="font-family:'Space Grotesk'; font-size:12px; font-weight:800; color:#145A43; letter-spacing:2px; text-transform:uppercase;">FEASIBILITY & VIABILITY</div>
        <h2 style="font-family:'Space Grotesk'; font-size:26px; font-weight:800; color:#0F172A; margin-top:4px;">Execution Challenges & Mitigation Strategy</h2>
    </div>
    """, unsafe_allow_html=True)

    feas_c1, feas_c2 = st.columns(2)

    with feas_c1:
        st.markdown("""
        <div class="sp-card-white">
            <h4 style="font-family:'Space Grotesk'; font-size:16px; font-weight:800; color:#083B2C; margin-bottom:10px;">
                1. Data Accuracy Challenge
            </h4>
            <p style="font-size:13px; color:#475569; line-height:1.5;">
                <b>Challenge:</b> Remote tribal hilly regions often lack ground weather stations.<br>
                <b>Mitigation Strategy:</b> Fuses satellite remote sensing (Copernicus DEM 30m, NASA POWER, IMD Pune Grid) 
                with on-ground field surveyor report ingestion.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='margin-bottom:12px;'></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="sp-card-white">
            <h4 style="font-family:'Space Grotesk'; font-size:16px; font-weight:800; color:#083B2C; margin-bottom:10px;">
                2. User Adoption & Digital Literacy
            </h4>
            <p style="font-size:13px; color:#475569; line-height:1.5;">
                <b>Challenge:</b> Field officers require simple, non-complex software.<br>
                <b>Mitigation Strategy:</b> Minimalist 1-click UI, clear visual maps, automated calculations, and 1-click printable PDF Dossiers.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with feas_c2:
        st.markdown("""
        <div class="sp-card-white">
            <h4 style="font-family:'Space Grotesk'; font-size:16px; font-weight:800; color:#083B2C; margin-bottom:10px;">
                3. High-Risk Construction Hazards
            </h4>
            <p style="font-size:13px; color:#475569; line-height:1.5;">
                <b>Challenge:</b> Heavy digging on steep slopes causes dangerous landslides during monsoons.<br>
                <b>Mitigation Strategy:</b> Automated Terrain Slope thresholding (>30°) strictly masks heavy excavation and recommends bio-vegetative alternatives.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='margin-bottom:12px;'></div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="sp-card-white">
            <h4 style="font-family:'Space Grotesk'; font-size:16px; font-weight:800; color:#083B2C; margin-bottom:10px;">
                4. Scheme & Budget Alignment
            </h4>
            <p style="font-size:13px; color:#475569; line-height:1.5;">
                <b>Challenge:</b> Water intervention proposals often stall due to lack of budget scheme alignment.<br>
                <b>Mitigation Strategy:</b> Direct MGNREGA cost structure (₹) and persondays estimation integrated into site recommendations.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-bottom: 36px;'></div>", unsafe_allow_html=True)

    # --------------------------------------------------------------------------
    # FOOTER & SECONDARY CTA
    # --------------------------------------------------------------------------
    st.markdown("""
    <div style="background: linear-gradient(135deg, #083B2C 0%, #145A43 100%); border-radius:18px; padding:32px; border:1px solid #145A43; text-align:center; color:#FFFFFF !important; box-shadow:0 15px 30px rgba(8,59,44,0.15);">
        <h2 style="font-family:'Space Grotesk'; font-size:24px; font-weight:800; color:#FFFFFF !important; margin-bottom:10px;">
            Ready to Explore the GeoAI Decision Portal?
        </h2>
        <p style="color:#E2F1E7 !important; font-size:14px; max-width:650px; margin:0 auto 20px auto;">
            Select any tribal district across 17 states to view live GIS maps, suitability heatmaps, and downloadable PDF dossiers.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_f_l, col_f_m, col_f_r = st.columns([1, 1.8, 1])
    with col_f_m:
        if st.button("🚀 LAUNCH PORTAL NOW →", key="btn_foot_launch", use_container_width=True):
            if on_launch_portal:
                on_launch_portal()

    st.markdown("""
    <div style="text-align:center; padding: 28px 0 12px 0; border-top: 1px solid #CBD5E1; margin-top: 40px; font-size: 12px; color: #64748B;">
        <b>SPRING AI</b> — Intelligent Spring Revival & Recharge Planning Platform © 2026 | Ministry of Tribal Affairs<br>
        <small>Data Sources: Central Ground Water Board (CGWB) • India Meteorological Department (IMD) • Geological Survey of India (GSI) • ISRO Bhuvan / Copernicus DEM 30m</small>
    </div>
    """, unsafe_allow_html=True)
