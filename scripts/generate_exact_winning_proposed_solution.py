import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def build_exact_winning_slide():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # Palette
    BG_COLOR = RGBColor(255, 255, 255)
    WHITE = RGBColor(255, 255, 255)
    NAVY_TITLE = RGBColor(24, 43, 73)        # #182B49
    BLUE_TEXT = RGBColor(2, 132, 199)        # #0284C7
    DARK_BLUE_TABLE = RGBColor(16, 57, 105)   # #103969
    HEADER_GREY = RGBColor(226, 232, 240)    # #E2E8F0
    TEXT_BLACK = RGBColor(15, 23, 42)        # #0F172A
    GREEN_ACCENT = RGBColor(16, 185, 129)    # #10B981
    GREEN_BG = RGBColor(220, 252, 231)        # #DCFCE7
    RED_BG = RGBColor(254, 226, 226)          # #FEE2E2
    RED_TEXT = RGBColor(220, 38, 38)          # #DC2626
    FOOTER_BLUE = RGBColor(2, 119, 189)       # #0277BD

    # 1. Background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_COLOR
    bg.line.fill.background()

    # 2. Header
    # Team Name / Logo (Top Left)
    logo_box = slide.shapes.add_textbox(Inches(0.4), Inches(0.15), Inches(2.2), Inches(0.6))
    tf_l = logo_box.text_frame
    p_l = tf_l.paragraphs[0]
    p_l.text = "SPRING AI"
    p_l.font.name = 'Georgia'
    p_l.font.size = Pt(22)
    p_l.font.bold = True
    p_l.font.color.rgb = RGBColor(217, 119, 6) # Amber color accent for brand

    # Center Header Title
    title_box = slide.shapes.add_textbox(Inches(2.7), Inches(0.15), Inches(7.5), Inches(0.6))
    tf_t = title_box.text_frame
    p_t = tf_t.paragraphs[0]
    p_t.text = "PROPOSED SOLUTION & UNIQUE FEATURES"
    p_t.font.name = 'Georgia'
    p_t.font.size = Pt(22)
    p_t.font.bold = True
    p_t.font.color.rgb = NAVY_TITLE
    p_t.alignment = PP_ALIGN.CENTER

    # Right SIH Badge
    sih_box = slide.shapes.add_textbox(Inches(10.5), Inches(0.1), Inches(2.4), Inches(0.7))
    tf_s = sih_box.text_frame
    p_s1 = tf_s.paragraphs[0]
    p_s1.text = "SMART INDIA HACKATHON"
    p_s1.font.name = 'Arial'
    p_s1.font.size = Pt(9)
    p_s1.font.bold = True
    p_s1.font.color.rgb = NAVY_TITLE
    p_s1.alignment = PP_ALIGN.RIGHT

    p_s2 = tf_s.add_paragraph()
    p_s2.text = "2026"
    p_s2.font.name = 'Arial'
    p_s2.font.size = Pt(13)
    p_s2.font.bold = True
    p_s2.font.color.rgb = BLUE_TEXT
    p_s2.alignment = PP_ALIGN.RIGHT

    # 3. Top Summary Banner (Dashed Border Box)
    summary_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.4), Inches(0.85), Inches(7.8), Inches(1.15))
    summary_box.fill.solid()
    summary_box.fill.fore_color.rgb = RGBColor(248, 250, 252)
    summary_box.line.color.rgb = NAVY_TITLE
    summary_box.line.width = Pt(1.5)

    tf_sum = summary_box.text_frame
    tf_sum.word_wrap = True
    p_sum = tf_sum.paragraphs[0]
    p_sum.text = "We propose, "
    p_sum.font.name = 'Arial'
    p_sum.font.size = Pt(10.5)
    p_sum.font.color.rgb = TEXT_BLACK
    
    # Run formatting
    r1 = p_sum.add_run()
    r1.text = "SPRING AI"
    r1.font.bold = True
    r1.font.color.rgb = BLUE_TEXT

    r2 = p_sum.add_run()
    r2.text = ", a one-stop platform for "

    r3 = p_sum.add_run()
    r3.text = "comprehensive hydro-geological springshed rejuvenation"
    r3.font.bold = True
    r3.font.color.rgb = BLUE_TEXT

    r4 = p_sum.add_run()
    r4.text = ", integrating "

    r5 = p_sum.add_run()
    r5.text = "Copernicus 30m DEM flow accumulation"
    r5.font.bold = True
    r5.font.color.rgb = TEXT_BLACK

    r6 = p_sum.add_run()
    r6.text = " with "

    r7 = p_sum.add_run()
    r7.text = "Potential Recharge Suitability Index (PRSI) modeling"
    r7.font.bold = True
    r7.font.color.rgb = BLUE_TEXT

    r8 = p_sum.add_run()
    r8.text = ". It seamlessly connects with major government groundwater data sources such as "

    r9 = p_sum.add_run()
    r9.text = "IMD, GSI (Geological Survey of India), CGWB (Central Ground Water Board)"
    r9.font.bold = True
    r9.font.color.rgb = BLUE_TEXT

    r10 = p_sum.add_run()
    r10.text = " and "

    r11 = p_sum.add_run()
    r11.text = "MGNREGA"
    r11.font.bold = True
    r11.font.color.rgb = BLUE_TEXT

    r12 = p_sum.add_run()
    r12.text = " etc."

    # 4. 6-Feature Grid (2 Columns x 3 Rows)
    card_w = Inches(3.8)
    card_h = Inches(1.5)
    xs = [Inches(0.4), Inches(4.4)]
    ys = [Inches(2.1), Inches(3.7), Inches(5.3)]

    cards = [
        # Row 1
        {
            "col": 0, "row": 0, "border_color": BLUE_TEXT,
            "head": "❏ Automated Hydro-Geological Catchment Delineation",
            "b1": "Programmatically applies ", "b2": "Copernicus 30m DEM & flow accumulation",
            "b3": " formulas, enabling ", "b4": "instant 30-sec springshed calculations", "b5": ", replacing months of manual field surveys."
        },
        {
            "col": 1, "row": 0, "border_color": GREEN_ACCENT,
            "head": "❏ Multi-Modal Data Fusion from National Portals",
            "b1": "Pulls up-to-date spatial data from ", "b2": "major government groundwater sources (GSI, IMD, CGWB)",
            "b3": " and satellite remote sensing for accurate ", "b4": "PRSI calculations", "b5": "."
        },
        # Row 2
        {
            "col": 0, "row": 1, "border_color": BLUE_TEXT,
            "head": "❏ AI-Based PRSI & Optimal Structure Recommendation",
            "b1": "Leverages AI & ML models to combine geo-tagged data into ", "b2": "PRSI suitability heatmaps",
            "b3": ", recommending optimal structures (", "b4": "Staggered Trenches, Percolation Pits, Check Dams", "b5": ")."
        },
        {
            "col": 1, "row": 1, "border_color": BLUE_TEXT,
            "head": "❏ Automated Hazard Masking & Safety Filter",
            "b1": "The system enforces automated slope safety constraints (", "b2": ">30° slope exclusion",
            "b3": ") & eco-sensitive masking to prevent ", "b4": "landslide risks and structural failures", "b5": "."
        },
        # Row 3
        {
            "col": 0, "row": 2, "border_color": BLUE_TEXT,
            "head": "❏ Offline Mobile GIS & Ground Verification App",
            "b1": "Enables Gram Panchayat Jal Sahi & Field Surveyors to perform ", "b2": "offline ground-truth mapping",
            "b3": " in remote tribal belts with ", "b4": "automated background cloud sync", "b5": "."
        },
        {
            "col": 1, "row": 2, "border_color": GREEN_ACCENT,
            "head": "❏ 1-Click MGNREGA Costing & DPR Dossier Generation",
            "b1": "AI-driven analysis automatically generates ", "b2": "itemized MGNREGA construction budgets",
            "b3": " and detailed ", "b4": "PDF project dossiers (DPR)", "b5": " for rapid administrative sanction."
        }
    ]

    for c in cards:
        cx = xs[c["col"]]
        cy = ys[c["row"]]

        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, card_w, card_h)
        box.fill.solid()
        box.fill.fore_color.rgb = RGBColor(255, 255, 255)
        box.line.color.rgb = c["border_color"]
        box.line.width = Pt(1.8)

        tf = box.text_frame
        tf.word_wrap = True
        
        # Header line
        p_head = tf.paragraphs[0]
        p_head.text = c["head"]
        p_head.font.name = 'Arial'
        p_head.font.size = Pt(10.5)
        p_head.font.bold = True
        p_head.font.color.rgb = TEXT_BLACK
        p_head.alignment = PP_ALIGN.CENTER
        p_head.space_after = Pt(3)

        # Body line
        p_body = tf.add_paragraph()
        p_body.alignment = PP_ALIGN.CENTER

        runs = [
            (c["b1"], False, TEXT_BLACK),
            (c["b2"], True, BLUE_TEXT),
            (c["b3"], False, TEXT_BLACK),
            (c["b4"], True, BLUE_TEXT),
            (c["b5"], False, TEXT_BLACK)
        ]
        for r_text, r_bold, r_col in runs:
            r = p_body.add_run()
            r.text = r_text
            r.font.name = 'Arial'
            r.font.size = Pt(9.5)
            r.font.bold = r_bold
            r.font.color.rgb = r_col

    # 5. Right Section — Unique Value Proposition Matrix & Extras
    rx = Inches(8.4)

    # Top Title Pill
    title_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, Inches(0.85), Inches(4.533), Inches(0.5))
    title_pill.fill.solid()
    title_pill.fill.fore_color.rgb = RGBColor(237, 233, 254) # Light purple
    title_pill.line.fill.background()
    tf_tp = title_pill.text_frame
    p_tp = tf_tp.paragraphs[0]
    p_tp.text = "Unique Value Proposition"
    p_tp.font.name = 'Georgia'
    p_tp.font.size = Pt(14)
    p_tp.font.bold = True
    p_tp.font.color.rgb = NAVY_TITLE
    p_tp.alignment = PP_ALIGN.CENTER

    # 4x4 Table
    table_shape = slide.shapes.add_table(5, 4, rx, Inches(1.45), Inches(4.533), Inches(3.8))
    table = table_shape.table
    table.columns[0].width = Inches(1.2)
    table.columns[1].width = Inches(1.0)
    table.columns[2].width = Inches(1.0)
    table.columns[3].width = Inches(1.333)

    # Table Header Row 0
    headers_row0 = ["Metric", "Existing Solutions", "Existing Solutions", "Our Solution"]
    # Table Subheader Row 1
    # We set custom cell text
    matrix_data = [
        # Row 0: Header
        [("Metric", DARK_BLUE_TABLE, WHITE, True), ("Existing Solutions", DARK_BLUE_TABLE, WHITE, True), ("Existing Solutions", DARK_BLUE_TABLE, WHITE, True), ("Our Solution", DARK_BLUE_TABLE, WHITE, True)],
        # Row 1: Subheader
        [("", DARK_BLUE_TABLE, WHITE, False), ("Manual Surveys", DARK_BLUE_TABLE, WHITE, True), ("Basic RS/GIS", DARK_BLUE_TABLE, WHITE, True), ("SPRING AI", DARK_BLUE_TABLE, WHITE, True)],
        # Row 2: Data 1
        [("Processing Speed", DARK_BLUE_TABLE, WHITE, True), ("❌ 6 Months", RED_BG, RED_TEXT, False), ("❌ 2-3 Wks", RED_BG, RED_TEXT, False), ("✔ 30-Sec AI Delineation", GREEN_BG, BLUE_TEXT, True)],
        # Row 3: Data 2
        [("Hydro-Geology Precision", DARK_BLUE_TABLE, WHITE, True), ("❌ Surface Only", RED_BG, RED_TEXT, False), ("Basic", RED_BG, RED_TEXT, False), ("✔ Full PRSI Model (Lithology+Soil)", GREEN_BG, BLUE_TEXT, True)],
        # Row 4: Data 3
        [("Landslide Masking", DARK_BLUE_TABLE, WHITE, True), ("❌ Risk Prone", RED_BG, RED_TEXT, False), ("❌ Manual Check", RED_BG, RED_TEXT, False), ("✔ Automated (>30° Slope Mask)", GREEN_BG, BLUE_TEXT, True)],
        # Row 5: Data 4
        [("Execution Dossier", DARK_BLUE_TABLE, WHITE, True), ("❌ Paper Draft", RED_BG, RED_TEXT, False), ("❌ None", RED_BG, RED_TEXT, False), ("✔ 1-Click MGNREGA DPR", GREEN_BG, BLUE_TEXT, True)]
    ]

    for r_idx, r_data in enumerate(matrix_data[1:], start=0):
        for c_idx, (cell_text, bg_col, text_col, is_bold) in enumerate(r_data):
            cell = table.cell(r_idx, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = bg_col
            tf_cell = cell.text_frame
            tf_cell.word_wrap = True
            p_c = tf_cell.paragraphs[0]
            p_c.text = cell_text
            p_c.font.name = 'Arial'
            p_c.font.size = Pt(8.5)
            p_c.font.bold = is_bold
            p_c.font.color.rgb = text_col
            p_c.alignment = PP_ALIGN.CENTER

    # Merge top header cells for Existing Solutions
    cell_a = table.cell(0, 1)
    cell_b = table.cell(0, 2)
    cell_a.merge(cell_b)

    # Dashed PRSI Score Formula Box
    prsi_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, Inches(5.35), Inches(4.533), Inches(0.75))
    prsi_box.fill.solid()
    prsi_box.fill.fore_color.rgb = RGBColor(248, 250, 252)
    prsi_box.line.color.rgb = BLUE_TEXT
    prsi_box.line.width = Pt(1.5)

    tf_p = prsi_box.text_frame
    tf_p.word_wrap = True
    p_prsi = tf_p.paragraphs[0]
    p_prsi.text = "UNIFIED PRSI SCORE: Uses a multi-index hydro-geological formula (Slope, Lithology, Rainfall, GW Depth) to deliver a unified, data-driven recharge score."
    p_prsi.font.name = 'Arial'
    p_prsi.font.size = Pt(8.5)
    p_prsi.font.bold = True
    p_prsi.font.color.rgb = TEXT_BLACK
    p_prsi.alignment = PP_ALIGN.CENTER

    # Dashed Chatbot Box
    bot_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, Inches(6.2), Inches(4.533), Inches(0.6))
    bot_box.fill.solid()
    bot_box.fill.fore_color.rgb = RGBColor(248, 250, 252)
    bot_box.line.color.rgb = BLUE_TEXT
    bot_box.line.width = Pt(1.5)

    tf_bot = bot_box.text_frame
    p_bot = tf_bot.paragraphs[0]
    p_bot.text = "🤖  AI-Driven Voice & Local Language Assistant — SpringBot"
    p_bot.font.name = 'Georgia'
    p_bot.font.size = Pt(11)
    p_bot.font.bold = True
    p_bot.font.color.rgb = NAVY_TITLE
    p_bot.alignment = PP_ALIGN.CENTER

    # 6. Footer Blue Bar
    footer_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(7.05), Inches(13.333), Inches(0.45))
    footer_bar.fill.solid()
    footer_bar.fill.fore_color.rgb = FOOTER_BLUE
    footer_bar.line.fill.background()

    tf_foot = footer_bar.text_frame
    p_foot_l = tf_foot.paragraphs[0]
    p_foot_l.text = "@SIH Idea submission- Template"
    p_foot_l.font.name = 'Arial'
    p_foot_l.font.size = Pt(11)
    p_foot_l.font.color.rgb = RGBColor(255, 255, 255)
    p_foot_l.alignment = PP_ALIGN.LEFT

    num_box = slide.shapes.add_textbox(Inches(12.2), Inches(7.05), Inches(1.0), Inches(0.45))
    tf_num = num_box.text_frame
    p_num = tf_num.paragraphs[0]
    p_num.text = "2"
    p_num.font.name = 'Arial'
    p_num.font.size = Pt(12)
    p_num.font.bold = True
    p_num.font.color.rgb = RGBColor(255, 255, 255)
    p_num.alignment = PP_ALIGN.RIGHT

    out_path = "SPRING_AI_Exact_Winning_Proposed_Solution.pptx"
    prs.save(out_path)
    print(f"Successfully generated exact winning proposed solution slide at: {os.path.abspath(out_path)}")

if __name__ == "__main__":
    build_exact_winning_slide()
