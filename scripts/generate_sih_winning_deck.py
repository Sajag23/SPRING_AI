"""
SPRING AI — Winning Grade SIH 2026 Presentation Generator
Generates high-resolution PNG diagram graphics (Iceberg, Flow Ribbon, Architecture)
and compiles a 16:9 Widescreen PowerPoint Presentation Deck (.pptx)
matching the exact SIH 2025 Winner Deck Format (#Team KIS easyRWH & GritForce AquaRoot).
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

os.makedirs("assets", exist_ok=True)

# -----------------------------------------------------------------------------
# 1. GENERATE GRAPHIC DIAGRAM ASSETS (MATPLOTLIB & PIL)
# -----------------------------------------------------------------------------

def generate_flow_ribbon_image():
    """Generates a high-res 6-step curved flow ribbon diagram graphic."""
    fig, ax = plt.subplots(figsize=(10, 2.5), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#F8FAFC')

    steps = [
        ("01 Data Fusion", "#2563EB"),
        ("02 Delineation", "#059669"),
        ("03 PRSI Scoring", "#D97706"),
        ("04 Safety Mask", "#DC2626"),
        ("05 Costing", "#7C3AED"),
        ("06 PDF Dossier", "#083B2C")
    ]

    x_coords = np.linspace(0.8, 9.2, len(steps))
    y_coords = 1.2 + 0.3 * np.sin(np.linspace(0, np.pi, len(steps)))

    # Draw Connecting Wave Line
    t = np.linspace(0.8, 9.2, 200)
    wave = 1.2 + 0.3 * np.sin(np.pi * (t - 0.8) / 8.4)
    ax.plot(t, wave, color='#CBD5E1', linewidth=4, zorder=1)

    for i, (label, color) in enumerate(steps):
        cx, cy = x_coords[i], y_coords[i]
        circle = plt.Circle((cx, cy), 0.55, color=color, zorder=2)
        ax.add_patch(circle)
        ax.text(cx, cy, label.split(' ')[0], color='white', weight='bold', fontsize=11, ha='center', va='center', zorder=3)
        ax.text(cx, cy - 0.8, ' '.join(label.split(' ')[1:]), color='#0F172A', weight='bold', fontsize=9.5, ha='center', va='top', zorder=3)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 2.2)
    ax.axis('off')
    plt.tight_layout()
    out_path = "assets/flow_ribbon.png"
    plt.savefig(out_path, bbox_inches='tight', facecolor='#F8FAFC')
    plt.close()

def generate_iceberg_graphic():
    """Generates a high-res Iceberg diagram graphic for Impact & Value Chain."""
    fig, ax = plt.subplots(figsize=(6, 4.5), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')

    # Water Line
    ax.axhline(2.8, color='#38BDF8', linewidth=3, linestyle='--')
    ax.text(0.2, 2.9, 'Water Baseline Level', color='#0284C7', weight='bold', fontsize=8)

    # Tip of Iceberg (Above Water)
    tip = patches.Polygon([[3, 2.8], [4, 4.2], [5, 2.8]], color='#93C5FD', alpha=0.9)
    ax.add_patch(tip)
    ax.text(4, 3.4, 'Visible Water Crisis\n& Field Surveys', color='#0F172A', weight='bold', fontsize=8, ha='center')

    # Submerged Iceberg (Below Water)
    submerged = patches.Polygon([[3, 2.8], [1.5, 0.4], [6.5, 0.4], [5, 2.8]], color='#1D4ED8', alpha=0.85)
    ax.add_patch(submerged)
    ax.text(4, 2.0, 'Untapped Springshed Recharge Potential\n(18.5 Billion Liters Water Storage)', color='white', weight='bold', fontsize=8.5, ha='center')
    ax.text(4, 1.2, 'Automated Slope >30° Safety Prohibitions\n& MGNREGA Scheme Budget Alignment', color='#E0F2FE', weight='bold', fontsize=7.5, ha='center')
    ax.text(4, 0.6, '100+ Scheduled Tribal Districts Secured', color='#93C5FD', weight='bold', fontsize=7.5, ha='center')

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 4.5)
    ax.axis('off')
    plt.tight_layout()
    out_path = "assets/iceberg_graphic.png"
    plt.savefig(out_path, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close()

def generate_architecture_graphic():
    """Generates a high-res 6-layer architecture pipeline diagram."""
    fig, ax = plt.subplots(figsize=(6, 4.5), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')

    layers = [
        ("01 Data Sources", "Copernicus 30m DEM, IMD Rainfall, GSI Lithology", "#2563EB"),
        ("02 Feature Fusion", "Slope (°), Aspect, Fractures, Stream Order", "#059669"),
        ("03 GeoAI ML Core", "Random Forest + XGBoost (F1: 0.9555)", "#D97706"),
        ("04 Safety Filter", "Slope >30° Landslide Safety Prohibitions", "#DC2626"),
        ("05 Decision Portal", "Interactive Folium Canvas & District Aggregator", "#7C3AED"),
        ("06 Field Output", "1-Click Official Executive PDF Dossier Exporter", "#083B2C")
    ]

    for i, (title, desc, color) in enumerate(layers):
        y = 4.0 - i * 0.65
        rect = patches.FancyBboxPatch((0.5, y - 0.25), 5.0, 0.5, boxstyle="round,pad=0.08", color=color, alpha=0.9)
        ax.add_patch(rect)
        ax.text(0.7, y, title, color='white', weight='bold', fontsize=8.5, va='center')
        ax.text(2.6, y, desc, color='white', fontsize=7.5, va='center')

    ax.set_xlim(0, 6)
    ax.set_ylim(0, 4.5)
    ax.axis('off')
    plt.tight_layout()
    out_path = "assets/architecture_graphic.png"
    plt.savefig(out_path, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close()

print("Generating graphics...")
generate_flow_ribbon_image()
generate_iceberg_graphic()
generate_architecture_graphic()
print("Graphic diagram assets generated successfully!")

# -----------------------------------------------------------------------------
# 2. BUILD PPTX PRESENTATION MATCHING SIH WINNER FORMAT (#Team KIS & GritForce)
# -----------------------------------------------------------------------------

def build_winning_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    NAVY = RGBColor(15, 23, 42)         # #0F172A
    FOREST = RGBColor(8, 59, 44)        # #083B2C
    MINT = RGBColor(16, 185, 129)       # #10B981
    BLUE = RGBColor(37, 99, 235)        # #2563EB
    LIGHT_BG = RGBColor(248, 250, 252)  # #F8FAFC
    WHITE = RGBColor(255, 255, 255)
    RED_ACCENT = RGBColor(225, 29, 72)  # #E11D48
    BORDER_COLOR = RGBColor(203, 213, 225)

    blank_layout = prs.slide_layouts[6]

    # Helper: Winning Header (Team Logo Left, Title Center, SIH Logo Right)
    def add_winner_header(slide, title_text, slide_num):
        # Header background
        h_bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
        h_bg.fill.solid()
        h_bg.fill.fore_color.rgb = NAVY
        h_bg.line.fill.background()

        # Team KIS Badge on Top Left
        team_b = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.4), Inches(0.18), Inches(0.8), Inches(0.8))
        team_b.fill.solid()
        team_b.fill.fore_color.rgb = FOREST
        team_b.line.color.rgb = MINT
        team_b.line.width = Pt(2)
        tb_tf = team_b.text_frame
        p_tb = tb_tf.paragraphs[0]
        p_tb.text = "SPRING\nAI"
        p_tb.font.name = 'Space Grotesk'
        p_tb.font.size = Pt(8.5)
        p_tb.font.bold = True
        p_tb.font.color.rgb = WHITE
        p_tb.alignment = PP_ALIGN.CENTER

        # Slide Title
        tbox = slide.shapes.add_textbox(Inches(1.4), Inches(0.2), Inches(8.2), Inches(0.8))
        tf = tbox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = 'Space Grotesk'
        p.font.size = Pt(26)
        p.font.bold = True
        p.font.color.rgb = WHITE

        # SIH 2026 Tag on Right
        sih_b = slide.shapes.add_textbox(Inches(9.5), Inches(0.2), Inches(3.4), Inches(0.7))
        sih_tf = sih_b.text_frame
        p_sih = sih_tf.paragraphs[0]
        p_sih.text = f"SMART INDIA HACKATHON 2026  |  0{slide_num}"
        p_sih.font.name = 'Space Grotesk'
        p_sih.font.size = Pt(11)
        p_sih.font.bold = True
        p_sih.font.color.rgb = MINT
        p_sih.alignment = PP_ALIGN.RIGHT

    # =========================================================================
    # SLIDE 1: PROPOSED SOLUTION & UNIQUE FEATURES (#Team KIS Slide 1 Format)
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    add_winner_header(slide1, "PROPOSED SOLUTION & UNIQUE FEATURES", 1)

    # One-line Solution Banner
    pitch_b = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.3), Inches(11.733), Inches(0.75))
    pitch_b.fill.solid()
    pitch_b.fill.fore_color.rgb = FOREST
    pitch_b.line.color.rgb = MINT
    pitch_tf = pitch_b.text_frame
    pitch_tf.word_wrap = True
    pp = pitch_tf.paragraphs[0]
    pp.text = "SPRING AI is a one-stop geospatial decision-support platform for comprehensive spring revival & recharge planning, integrating satellite remote sensing with ground hydrogeology baselines across 100+ Scheduled Tribal Districts."
    pp.font.name = 'Plus Jakarta Sans'
    pp.font.size = Pt(12)
    pp.font.bold = True
    pp.font.color.rgb = WHITE
    pp.alignment = PP_ALIGN.CENTER

    # Left: 6 Feature Cards Grid (2x3)
    feat_w = Inches(3.2)
    feat_h = Inches(1.8)
    feat_x0 = Inches(0.8)
    feat_y0 = Inches(2.2)

    features_list = [
        ("Automated PRSI Computation", "Applies multi-criteria weighted overlay for recharge suitability."),
        ("Real-Time Government Fusion", "Pulls satellite DEM 30m, IMD rainfall & GSI rock formations."),
        ("Geo-Intelligent Mapping", "Hardware-accelerated Folium canvas with Esri Satellite HD."),
        ("Landslide Hazard Masking", "Strictly prohibits heavy digging on slopes >30° for safety."),
        ("MGNREGA Costing Engine", "Calculates site structure costs (₹) & persondays labor."),
        ("1-Click PDF Dossiers", "Produces official printable Executive Field Reports for engineers.")
    ]

    for idx, (ftitle, fdesc) in enumerate(features_list):
        row = idx // 2
        col = idx % 2
        fx = feat_x0 + col * (feat_w + Inches(0.2))
        fy = feat_y0 + row * (feat_h + Inches(0.15))

        fbox = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, fx, fy, feat_w, feat_h)
        fbox.fill.solid()
        fbox.fill.fore_color.rgb = WHITE
        fbox.line.color.rgb = BLUE
        fbox.line.width = Pt(1.5)
        ftf = fbox.text_frame
        ftf.word_wrap = True

        pt = ftf.paragraphs[0]
        pt.text = f"❏ {ftitle}"
        pt.font.name = 'Space Grotesk'
        pt.font.size = Pt(11.5)
        pt.font.bold = True
        pt.font.color.rgb = BLUE

        pd = ftf.add_paragraph()
        pd.text = fdesc
        pd.font.name = 'Plus Jakarta Sans'
        pd.font.size = Pt(9.5)
        pd.font.color.rgb = NAVY

    # Right: Unique Value Proposition Matrix Table (#Team KIS Format)
    tbl_box = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.7), Inches(2.2), Inches(4.8), Inches(4.8))
    tbl_box.fill.solid()
    tbl_box.fill.fore_color.rgb = LIGHT_BG
    tbl_box.line.color.rgb = FOREST
    tbl_box.line.width = Pt(2)
    tbl_tf = tbl_box.text_frame
    tbl_tf.word_wrap = True

    ptbl_h = tbl_tf.paragraphs[0]
    ptbl_h.text = "UNIQUE VALUE PROPOSITION MATRIX"
    ptbl_h.font.name = 'Space Grotesk'
    ptbl_h.font.size = Pt(13)
    ptbl_h.font.bold = True
    ptbl_h.font.color.rgb = FOREST
    ptbl_h.alignment = PP_ALIGN.CENTER

    comp_items = [
        ("Capability", "Manual Survey", "Generic GIS", "SPRING AI"),
        ("Govt API Integration", "❌ None", "⚠️ Static", "✅ Direct Fusion"),
        ("AI ML Model", "❌ None", "❌ None", "✅ Hybrid RF+XGB"),
        ("Landslide Mask (>30°)", "⚠️ Subjective", "❌ Manual", "✅ Automated"),
        ("MGNREGA Costing", "❌ Manual", "❌ None", "✅ Automated ₹"),
        ("Field PDF Dossier", "❌ Slow", "❌ None", "✅ 1-Click Export")
    ]

    for item in comp_items:
        p = tbl_tf.add_paragraph()
        p.text = f"{item[0]:<18} | {item[1]:<10} | {item[3]}"
        p.font.name = 'Plus Jakarta Sans'
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = NAVY

    # =========================================================================
    # SLIDE 2: SOLUTION OVERVIEW & PROCESS RIBBON (#Team KIS Slide 2 Format)
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_winner_header(slide2, "SOLUTION OVERVIEW & PROCESS RIBBON", 2)

    # Top Description Ribbon Box
    desc_b = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.3), Inches(11.733), Inches(0.65))
    desc_b.fill.solid()
    desc_b.fill.fore_color.rgb = LIGHT_BG
    desc_b.line.color.rgb = BLUE
    dtf = desc_b.text_frame
    dtf.word_wrap = True
    pdt = dtf.paragraphs[0]
    pdt.text = "SPRING AI simplifies usability, turning complex multi-modal satellite remote sensing into an easy 1-click digital tool for decision-makers and field engineering teams."
    pdt.font.name = 'Plus Jakarta Sans'
    pdt.font.size = Pt(11.5)
    pdt.font.bold = True
    pdt.font.color.rgb = NAVY

    # Embedded Graphic Image: Flow Ribbon Diagram
    if os.path.exists("assets/flow_ribbon.png"):
        slide2.shapes.add_picture("assets/flow_ribbon.png", Inches(0.8), Inches(2.1), Inches(11.733), Inches(2.3))

    # Bottom Left Box: Usability & Action
    u_box = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.5), Inches(5.6), Inches(2.5))
    u_box.fill.solid()
    u_box.fill.fore_color.rgb = WHITE
    u_box.line.color.rgb = BLUE
    u_tf = u_box.text_frame
    u_tf.word_wrap = True

    pu_h = u_tf.paragraphs[0]
    pu_h.text = "USABILITY & ACTIONABLE ACCESS"
    pu_h.font.name = 'Space Grotesk'
    pu_h.font.size = Pt(13)
    pu_h.font.bold = True
    pu_h.font.color.rgb = BLUE

    u_items = [
        "Simplifies Usability: Converts complex GIS overlays into clear visual heatmaps.",
        "Empowers Field Officers: Instant ground assessment & site recommendations.",
        "Enables Action: Direct MGNREGA cost & labor persondays estimation."
    ]
    for item in u_items:
        p = u_tf.add_paragraph()
        p.text = f"• {item}"
        p.font.name = 'Plus Jakarta Sans'
        p.font.size = Pt(10.5)
        p.font.color.rgb = NAVY

    # Bottom Right Box: Key Solution Features
    kf_box = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.5), Inches(5.7), Inches(2.5))
    kf_box.fill.solid()
    kf_box.fill.fore_color.rgb = WHITE
    kf_box.line.color.rgb = FOREST
    kf_tf = kf_box.text_frame
    kf_tf.word_wrap = True

    pkf_h = kf_tf.paragraphs[0]
    pkf_h.text = "KEY SOLUTION FEATURES"
    pkf_h.font.name = 'Space Grotesk'
    pkf_h.font.size = Pt(13)
    pkf_h.font.bold = True
    pkf_h.font.color.rgb = FOREST

    kf_items = [
        "→ Feasibility check for recharge structures based on local rainfall & slope.",
        "→ Calculates runoff capacity & suggests pit/trench dimensions.",
        "→ Provides data on principal aquifer depth using satellite models.",
        "→ Generates detailed cost estimation & 1-click printable PDF dossiers."
    ]
    for item in kf_items:
        p = kf_tf.add_paragraph()
        p.text = item
        p.font.name = 'Plus Jakarta Sans'
        p.font.size = Pt(10.5)
        p.font.color.rgb = NAVY

    # =========================================================================
    # SLIDE 3: TECHNICAL APPROACH & DIAGRAMS (#Team KIS Slide 3 Format)
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_winner_header(slide3, "TECHNICAL APPROACH & INFRASTRUCTURE", 3)

    # Left: Tech Stack Box
    ts_b = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.4), Inches(4.5), Inches(5.5))
    ts_b.fill.solid()
    ts_b.fill.fore_color.rgb = LIGHT_BG
    ts_b.line.color.rgb = BLUE
    ts_b.line.width = Pt(2)
    ts_tf = ts_b.text_frame
    ts_tf.word_wrap = True

    pts_h = ts_tf.paragraphs[0]
    pts_h.text = "TECH STACK & INTEGRATIONS"
    pts_h.font.name = 'Space Grotesk'
    pts_h.font.size = Pt(14)
    pts_h.font.bold = True
    pts_h.font.color.rgb = BLUE

    ts_pills = [
        ("Frontend", "Python 3.10+ • Streamlit Framework"),
        ("GIS Canvas", "Folium • Leaflet.js • Bhuvan HD"),
        ("AI / ML", "Scikit-Learn • XGBoost (F1: 0.9555)"),
        ("Data APIs", "Copernicus DEM 30m • IMD • GSI"),
        ("Reporting", "FPDF2 PDF Executive Exporter")
    ]
    for cat, val in ts_pills:
        p = ts_tf.add_paragraph()
        p.text = f"• {cat}:  {val}"
        p.font.name = 'Plus Jakarta Sans'
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = NAVY

    # Right: Embedded Architecture Graphic Image
    if os.path.exists("assets/architecture_graphic.png"):
        slide3.shapes.add_picture("assets/architecture_graphic.png", Inches(5.6), Inches(1.4), Inches(6.9), Inches(5.5))

    # =========================================================================
    # SLIDE 4: ANALYTICS & ROLE-BASED ACCESS (GritForce Slide 4 Format)
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_winner_header(slide4, "ANALYTICS ENGINE & ROLE-BASED ACCESS", 4)

    # Top Right: Mathematical PRSI Formula Box
    formula_b = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.4), Inches(11.733), Inches(1.8))
    formula_b.fill.solid()
    formula_b.fill.fore_color.rgb = LIGHT_BG
    formula_b.line.color.rgb = FOREST
    formula_b.line.width = Pt(2)
    ftf = formula_b.text_frame
    ftf.word_wrap = True

    pf_h = ftf.paragraphs[0]
    pf_h.text = "PROBABILISTIC RECHARGE SUITABILITY INDEX (PRSI) FORMULATION"
    pf_h.font.name = 'Space Grotesk'
    pf_h.font.size = Pt(14)
    pf_h.font.bold = True
    pf_h.font.color.rgb = FOREST

    pf_eq = ftf.add_paragraph()
    pf_eq.text = "PRSI = 0.32(Rainfall) + 0.24(Geology) + 0.20(Slope) + 0.14(Fractures) + 0.06(LULC) + 0.04(Soil)"
    pf_eq.font.name = 'Space Grotesk'
    pf_eq.font.size = Pt(13)
    pf_eq.font.bold = True
    pf_eq.font.color.rgb = BLUE

    pf_rule = ftf.add_paragraph()
    pf_rule.text = "Safety Mask Rule: If Terrain Slope S > 30° ⇒ PRSI ≡ 0 (Prohibits heavy structural excavation to prevent landslides)."
    pf_rule.font.name = 'Plus Jakarta Sans'
    pf_rule.font.size = Pt(11)
    pf_rule.font.color.rgb = RED_ACCENT
    pf_rule.font.bold = True

    # Bottom: Role-Based Access Table (RBAC)
    rbac_b = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.4), Inches(11.733), Inches(3.6))
    rbac_b.fill.solid()
    rbac_b.fill.fore_color.rgb = WHITE
    rbac_b.line.color.rgb = BLUE
    rbac_b.line.width = Pt(1.5)
    rtf = rbac_b.text_frame
    rtf.word_wrap = True

    pr_h = rtf.paragraphs[0]
    pr_h.text = "ROLE-BASED ACCESS CONTROL (RBAC) MATRIX"
    pr_h.font.name = 'Space Grotesk'
    pr_h.font.size = Pt(14)
    pr_h.font.bold = True
    pr_h.font.color.rgb = BLUE

    rbac_rows = [
        ("ROLE", "GIS MAPS", "PRSI SCORES", "COSTING", "SAFETY MASK", "GROUND LOGS", "PDF DOSSIER"),
        ("MINISTRY / POLICY MAKER", "✓", "✓", "✓", "✓", "✗", "✓"),
        ("HYDROLOGIST / SCIENTIST", "✓", "✓", "✓", "✓", "✓", "✓"),
        ("FIELD ENGINEER / OFFICER", "✓", "✗", "✓", "✓", "✓", "✓"),
        ("COMMUNITY / PUBLIC", "✓", "✓", "✗", "✓", "✗", "✗")
    ]
    for row in rbac_rows:
        p = rtf.add_paragraph()
        p.text = f"{row[0]:<28} | {row[1]:<8} | {row[2]:<10} | {row[3]:<8} | {row[4]:<10} | {row[5]:<10} | {row[6]}"
        p.font.name = 'Plus Jakarta Sans'
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = NAVY

    # =========================================================================
    # SLIDE 5: FEASIBILITY AND VIABILITY (#Team KIS Slide 5 Format)
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_winner_header(slide5, "FEASIBILITY AND VIABILITY MATRIX", 5)

    # Left Column: 3 Pillars (Feasibility, Challenges, Strategy)
    f_col = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.4), Inches(6.8), Inches(5.5))
    f_col.fill.solid()
    f_col.fill.fore_color.rgb = WHITE
    f_col.line.color.rgb = BLUE
    f_col.line.width = Pt(2)
    ftf = f_col.text_frame
    ftf.word_wrap = True

    p1 = ftf.paragraphs[0]
    p1.text = "1. Feasibility"
    p1.font.name = 'Space Grotesk'
    p1.font.size = Pt(13)
    p1.font.bold = True
    p1.font.color.rgb = BLUE

    items1 = [
        "Technically → Existing satellite APIs, GIS mapping, and ML algorithms.",
        "Economically → Promotes cost savings, water security & MGNREGA alignment.",
        "Socially → Solves summer water scarcity in Scheduled Tribal regions."
    ]
    for item in items1:
        p = ftf.add_paragraph()
        p.text = f"• {item}"
        p.font.name = 'Plus Jakarta Sans'
        p.font.size = Pt(10)
        p.font.color.rgb = NAVY

    p2 = ftf.add_paragraph()
    p2.text = "\n2. Challenges vs. Strategy"
    p2.font.name = 'Space Grotesk'
    p2.font.size = Pt(13)
    p2.font.bold = True
    p2.font.color.rgb = RED_ACCENT

    items2 = [
        "Data Accuracy → Fuse satellite APIs (IMD, GSI, DEM) + ground log validation.",
        "User Adoption → Minimalist 1-click UI & 1-click printable PDF Dossiers.",
        "Terrain Hazards → Slope >30° thresholding masks dangerous excavation.",
        "Regulatory Barriers → Partner with Ministry & align with MGNREGA scheme."
    ]
    for item in items2:
        p = ftf.add_paragraph()
        p.text = f"• {item}"
        p.font.name = 'Plus Jakarta Sans'
        p.font.size = Pt(10)
        p.font.color.rgb = NAVY

    # Right Column: Stack of 8 Green Feasible Solution Pills (#Team KIS Format)
    pills_b = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.8), Inches(1.4), Inches(4.7), Inches(5.5))
    pills_b.fill.solid()
    pills_b.fill.fore_color.rgb = LIGHT_BG
    pills_b.line.color.rgb = FOREST
    pills_b.line.width = Pt(2)
    ptf = pills_b.text_frame
    ptf.word_wrap = True

    pp_h = ptf.paragraphs[0]
    pp_h.text = "OUR FEASIBLE SOLUTION PILLARS"
    pp_h.font.name = 'Space Grotesk'
    pp_h.font.size = Pt(13)
    pp_h.font.bold = True
    pp_h.font.color.rgb = FOREST
    pp_h.alignment = PP_ALIGN.CENTER

    pills_list = [
        "✓ Transparent comparison of structure options.",
        "✓ Map-based input + auto data fetch.",
        "✓ Smart PRSI assessment with detailed report.",
        "✓ Verified MGNREGA budget & persondays.",
        "✓ End-to-end flow: Ingest → PRSI → Mask → PDF.",
        "✓ Vernacular & English PDF report support.",
        "✓ Water storage capacity estimates (18.5B L).",
        "✓ Upfront cost vs long-term water security."
    ]
    for pill in pills_list:
        p = ptf.add_paragraph()
        p.text = pill
        p.font.name = 'Plus Jakarta Sans'
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = FOREST

    # =========================================================================
    # SLIDE 6: IMPACT AND BENEFITS (#Team KIS Slide 6 Format)
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_winner_header(slide6, "IMPACT AND BENEFITS (ICEBERG MODEL)", 6)

    # Top Analogy Banner
    an_b = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.3), Inches(11.733), Inches(0.65))
    an_b.fill.solid()
    an_b.fill.fore_color.rgb = LIGHT_BG
    an_b.line.color.rgb = BLUE
    atf = an_b.text_frame
    atf.word_wrap = True
    pat = atf.paragraphs[0]
    pat.text = "Solar panels boomed because of rising electricity costs + govt push. Similarly, water scarcity + recharge mandates are pushing springshed revival forward."
    pat.font.name = 'Plus Jakarta Sans'
    pat.font.size = Pt(11.5)
    pat.font.bold = True
    pat.font.color.rgb = NAVY

    # Left: Embedded Iceberg Graphic Image
    if os.path.exists("assets/iceberg_graphic.png"):
        slide6.shapes.add_picture("assets/iceberg_graphic.png", Inches(0.8), Inches(2.1), Inches(5.8), Inches(4.8))

    # Right: Multi-Tier Impact Breakdown Cards
    imp_b = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.1), Inches(5.7), Inches(4.8))
    imp_b.fill.solid()
    imp_b.fill.fore_color.rgb = WHITE
    imp_b.line.color.rgb = FOREST
    imp_b.line.width = Pt(2)
    itf = imp_b.text_frame
    itf.word_wrap = True

    pi_h = itf.paragraphs[0]
    pi_h.text = "MULTI-TIER BENEFIT BREAKDOWN"
    pi_h.font.name = 'Space Grotesk'
    pi_h.font.size = Pt(14)
    pi_h.font.bold = True
    pi_h.font.color.rgb = FOREST

    tiers = [
        ("Household Level", "Lower water bills, 4.2M Liters annual water security."),
        ("Community Level", "Secures 100+ Scheduled Tribal Districts & livelihoods."),
        ("Regional Level", "Groundwater table rise (+1.2m) & baseflow extension (+45 days)."),
        ("Ministry Level", "Data-driven policymaking & MGNREGA budget optimization."),
        ("Environmental", "Long-term groundwater replenishment & climate resilience.")
    ]

    for title, desc in tiers:
        p = itf.add_paragraph()
        p.text = f"• {title}:  {desc}"
        p.font.name = 'Plus Jakarta Sans'
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = NAVY

    out_path = "SPRING_AI_SIH_2026_Final_Winner_Deck.pptx"
    prs.save(out_path)
    print(f"Successfully generated winning-format PowerPoint presentation at {os.path.abspath(out_path)}")

if __name__ == "__main__":
    build_winning_deck()
