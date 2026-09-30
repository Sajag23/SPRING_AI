import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_complete_master_deck():
    master_prs = Presentation()
    master_prs.slide_width = Inches(13.333)
    master_prs.slide_height = Inches(7.5)

    # List of individual slide presentations to combine
    slide_files = [
        "SPRING_AI_Exact_Winning_Proposed_Solution.pptx",     # Slide 2
        "SPRING_AI_Exact_Winning_Technical_Approach.pptx",    # Slide 3
        "SPRING_AI_Exact_Winning_Feasibility.pptx",           # Slide 4
        "SPRING_AI_Exact_Winning_Impact.pptx",                # Slide 5
        "SPRING_AI_Exact_Winning_Research.pptx"               # Slide 6
    ]

    # Combine slides
    for s_file in slide_files:
        if os.path.exists(s_file):
            sub_prs = Presentation(s_file)
            for slide in sub_prs.slides:
                # Add blank slide to master
                blank_layout = master_prs.slide_layouts[6]
                new_slide = master_prs.slides.add_slide(blank_layout)

                # Copy all shapes from source slide to target slide
                for shape in slide.shapes:
                    if shape.has_text_frame:
                        # Add textbox / shape copy
                        new_shape = new_slide.shapes.add_shape(
                            shape.auto_shape_type if hasattr(shape, 'auto_shape_type') and shape.auto_shape_type else MSO_SHAPE.RECTANGLE,
                            shape.left, shape.top, shape.width, shape.height
                        )
                        new_shape.fill.solid()
                        if hasattr(shape.fill, 'fore_color') and shape.fill.fore_color and hasattr(shape.fill.fore_color, 'rgb'):
                            new_shape.fill.fore_color.rgb = shape.fill.fore_color.rgb
                        else:
                            new_shape.fill.background()

                        if hasattr(shape.line, 'color') and shape.line.color and hasattr(shape.line.color, 'rgb'):
                            new_shape.line.color.rgb = shape.line.color.rgb
                        else:
                            new_shape.line.fill.background()

                        # Copy text
                        tf_new = new_shape.text_frame
                        tf_new.word_wrap = shape.text_frame.word_wrap
                        for p_idx, p_old in enumerate(shape.text_frame.paragraphs):
                            p_new = tf_new.paragraphs[0] if p_idx == 0 else tf_new.add_paragraph()
                            p_new.text = p_old.text
                            p_new.alignment = p_old.alignment
                            if len(p_old.runs) > 0 and hasattr(p_old.runs[0].font, 'color') and hasattr(p_old.runs[0].font.color, 'rgb'):
                                for r_old in p_old.runs:
                                    r_new = p_new.add_run()
                                    r_new.text = r_old.text
                                    r_new.font.name = r_old.font.name
                                    r_new.font.size = r_old.font.size
                                    r_new.font.bold = r_old.font.bold
                                    if hasattr(r_old.font.color, 'rgb') and r_old.font.color.rgb:
                                        r_new.font.color.rgb = r_old.font.color.rgb

    out_file = "SPRING_AI_SIH_2026_MASTER_WINNING_DECK.pptx"
    master_prs.save(out_file)
    print(f"Master presentation with all slides saved to: {os.path.abspath(out_file)}")

if __name__ == "__main__":
    build_complete_master_deck()
