import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_exact_winning_research():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # Colors
    BG_COLOR = RGBColor(255, 255, 255)
    WHITE = RGBColor(255, 255, 255)
    NAVY_TITLE = RGBColor(24, 43, 73)        # #182B49
    BLUE_TEXT = RGBColor(2, 132, 199)        # #0284C7
    DARK_BLUE_HEADER = RGBColor(16, 57, 105) # #103969
    CARD_BG = RGBColor(248, 250, 252)        # #F8FAFC
    BORDER_GREY = RGBColor(203, 213, 225)    # #CBD5E1
    TEXT_BLACK = RGBColor(15, 23, 42)        # #0F172A
    GRAY_TEXT = RGBColor(71, 85, 105)        # #475569
    FOOTER_BLUE = RGBColor(2, 119, 189)       # #0277BD
    EMERALD = RGBColor(5, 150, 105)         # #059669
    AMBER = RGBColor(217, 119, 6)           # #D97706
    PURPLE = RGBColor(124, 58, 237)         # #7C3AED

    # 1. Background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_COLOR
    bg.line.fill.background()

    # 2. Header
    # Left Oval Logo Box
    oval = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.4), Inches(0.2), Inches(1.8), Inches(0.65))
    oval.fill.solid()
    oval.fill.fore_color.rgb = WHITE
    oval.line.color.rgb = BLUE_TEXT
    oval.line.width = Pt(1.5)
    tf_ov = oval.text_frame
    p_ov = tf_ov.paragraphs[0]
    p_ov.text = "SPRING AI"
    p_ov.font.name = 'Georgia'
    p_ov.font.size = Pt(11)
    p_ov.font.bold = True
    p_ov.font.color.rgb = NAVY_TITLE
    p_ov.alignment = PP_ALIGN.CENTER

    # Center Header Title
    title_box = slide.shapes.add_textbox(Inches(2.5), Inches(0.15), Inches(7.8), Inches(0.6))
    tf_t = title_box.text_frame
    p_t = tf_t.paragraphs[0]
    p_t.text = "RESEARCH AND REFERENCES"
    p_t.font.name = 'Georgia'
    p_t.font.size = Pt(24)
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

    # -------------------------------------------------------------------------
    # 3. 4-CATEGORY VISUAL REFERENCE CARDS (2x2 GRID)
    # -------------------------------------------------------------------------
    card_w = Inches(6.0)
    card_h = Inches(2.7)
    xs = [Inches(0.4), Inches(6.933)]
    ys = [Inches(1.0), Inches(3.9)]

    categories = [
        {
            "col": 0, "row": 0, "color": BLUE_TEXT,
            "title": "🏛️  National Portals & Satellite Datasets",
            "items": [
                ("Copernicus Open Access Hub (ESA)", "30m Global DEM for catchment flow accumulation & slope mapping."),
                ("Central Ground Water Board (CGWB / INGRES)", "National groundwater levels, aquifer maps & recharge norms."),
                ("Geological Survey of India (GSI Bhukosh)", "Lithology, rock permeability & subsurface formation maps."),
                ("India Meteorological Dept (IMD Hydromet)", "High-resolution gridded rainfall & seasonal precipitation data.")
            ]
        },
        {
            "col": 1, "row": 0, "color": EMERALD,
            "title": "📚  Academic & Scientific Literature",
            "items": [
                ("NITI Aayog Report (2018)", "Inventory and Revival of Springs in Himalayas for Water Security."),
                ("Hydrogeology Journal (Elsevier 2022)", "Potential Groundwater Recharge Delineation via Remote Sensing & AHP."),
                ("MoTA & Jal Shakti Guidelines (2020)", "8-Step Methodology for Springshed Management in Mountainous Belts."),
                ("ISRO Bhuvan Geo-Spatial Platform", "Land Use / Land Cover (LULC) 1:50,000 spatial mapping standards.")
            ]
        },
        {
            "col": 0, "row": 1, "color": AMBER,
            "title": "📜  Regulatory & Scheme Frameworks",
            "items": [
                ("MGNREGA Operational Guidelines (MoRD)", "Itemized schedule of rates for water conservation & recharge structures."),
                ("Jal Shakti Abhiyan Guidelines", "Technical specs for Staggered Trenches, Percolation Pits & Check Dams."),
                ("NRSC Hydrological Modeling Manual", "Satellite-based flow routing protocols & hydro-geological scoring.")
            ]
        },
        {
            "col": 1, "row": 1, "color": PURPLE,
            "title": "🌐  Technology & Open Source Libraries",
            "items": [
                ("GDAL / Rasterio & PyTorch", "Python spatial raster processing & DEM flow direction algorithms."),
                ("PostGIS & Mapbox GL JS SDK", "Spatial indexing, fast vector tile rendering & geo-queries."),
                ("SPRING AI Research Portal", "https://www.spring-ai.in/research-hub — Model docs & data specs.")
            ]
        }
    ]

    for cat in categories:
        cx = xs[cat["col"]]
        cy = ys[cat["row"]]

        # Outer Card Box
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, card_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = cat["color"]
        card.line.width = Pt(1.5)

        # Header Bar
        hbar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, cx, cy, card_w, Inches(0.55))
        hbar.fill.solid()
        hbar.fill.fore_color.rgb = cat["color"]
        hbar.line.fill.background()

        tf_hb = hbar.text_frame
        p_hb = tf_hb.paragraphs[0]
        p_hb.text = cat["title"]
        p_hb.font.name = 'Georgia'
        p_hb.font.size = Pt(12)
        p_hb.font.bold = True
        p_hb.font.color.rgb = WHITE
        p_hb.alignment = PP_ALIGN.LEFT

        # Content Text Box
        cbox = slide.shapes.add_textbox(cx + Inches(0.15), cy + Inches(0.6), card_w - Inches(0.3), card_h - Inches(0.65))
        tf_c = cbox.text_frame
        tf_c.word_wrap = True

        for i_idx, (i_head, i_desc) in enumerate(cat["items"]):
            p_i = tf_c.paragraphs[0] if i_idx == 0 else tf_c.add_paragraph()
            p_i.text = f"• {i_head}: "
            p_i.font.name = 'Arial'
            p_i.font.size = Pt(9.5)
            p_i.font.bold = True
            p_i.font.color.rgb = NAVY_TITLE

            r_d = p_i.add_run()
            r_d.text = i_desc
            r_d.font.bold = False
            r_d.font.color.rgb = GRAY_TEXT

            p_i.space_after = Pt(3)

    # 4. Footer Blue Bar
    footer_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(7.05), Inches(13.333), Inches(0.45))
    footer_bar.fill.solid()
    footer_bar.fill.fore_color.rgb = FOOTER_BLUE
    footer_bar.line.fill.background()

    tf_foot = footer_bar.text_frame
    p_foot_l = tf_foot.paragraphs[0]
    p_foot_l.text = "@SIH Idea submission- Template"
    p_foot_l.font.name = 'Arial'
    p_foot_l.font.size = Pt(11)
    p_foot_l.font.color.rgb = WHITE
    p_foot_l.alignment = PP_ALIGN.LEFT

    num_box = slide.shapes.add_textbox(Inches(12.2), Inches(7.05), Inches(1.0), Inches(0.45))
    tf_num = num_box.text_frame
    p_num = tf_num.paragraphs[0]
    p_num.text = "6"
    p_num.font.name = 'Arial'
    p_num.font.size = Pt(12)
    p_num.font.bold = True
    p_num.font.color.rgb = WHITE
    p_num.alignment = PP_ALIGN.RIGHT

    out_path = "SPRING_AI_Exact_Winning_Research.pptx"
    prs.save(out_path)
    print(f"Successfully generated exact winning Research slide at: {os.path.abspath(out_path)}")

if __name__ == "__main__":
    build_exact_winning_research()
