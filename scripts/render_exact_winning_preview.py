import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(13.333, 7.5), dpi=300)
ax.set_facecolor('white')
fig.patch.set_facecolor('white')

# 1. Header
ax.text(0.4, 7.0, 'SPRING AI', color='#D97706', fontsize=20, fontfamily='serif', weight='bold', va='center')
ax.text(6.666, 7.0, 'PROPOSED SOLUTION & UNIQUE FEATURES', color='#182B49', fontsize=20, fontfamily='serif', weight='bold', ha='center', va='center')

# Right Emblem
ax.text(12.8, 7.15, 'SMART INDIA HACKATHON', color='#182B49', fontsize=8, weight='bold', ha='right')
ax.text(12.8, 6.85, '2026', color='#0284C7', fontsize=12, weight='bold', ha='right')

# 2. Top Dashed Summary Box
summary_bg = patches.FancyBboxPatch((0.4, 5.5), 7.6, 1.1, boxstyle="round,pad=0.03", edgecolor='#182B49', facecolor='#F8FAFC', linewidth=1.5, linestyle='--')
ax.add_patch(summary_bg)

summary_text = (
    "We propose, SPRING AI, a one-stop destination for comprehensive hydro-geological springshed rejuvenation,\n"
    "integrating Copernicus 30m DEM flow accumulation with Potential Recharge Suitability Index (PRSI) modeling.\n"
    "It seamlessly connects with major government groundwater data sources such as IMD, GSI, CGWB & MGNREGA etc."
)
ax.text(0.5, 6.05, summary_text, color='#0F172A', fontsize=8, va='center', fontfamily='sans-serif', linespacing=1.4)

# 3. 6 Feature Cards Grid (2 cols x 3 rows)
xs = [0.4, 4.3]
ys = [3.9, 2.3, 0.7]

cards_data = [
    # Row 1
    ("❏ Automated Catchment Delineation", "Applies Copernicus 30m DEM & flow accumulation formulas,\nenabling instant 30-sec springshed calculations.", "#0284C7"),
    ("❏ Multi-Modal Data Fusion", "Pulls up-to-date spatial data from major government sources\n(GSI, IMD, CGWB) & Sentinel satellite remote sensing.", "#10B981"),
    # Row 2
    ("❏ AI-Based PRSI Recommendation", "Combines geo-tagged data into PRSI suitability heatmaps,\nrecommending Staggered Trenches, Percolation Pits & Check Dams.", "#0284C7"),
    ("❏ Automated Hazard Safety Filter", "Enforces slope safety constraints (>30° slope exclusion)\n& eco-sensitive masking to prevent landslide risks.", "#0284C7"),
    # Row 3
    ("❏ Offline Mobile GIS Verification", "Enables Gram Panchayat Jal Sahi & Field Surveyors to perform\noffline ground-truth mapping with auto cloud sync.", "#0284C7"),
    ("❏ 1-Click MGNREGA DPR Dossiers", "Automatically generates itemized MGNREGA construction budgets\nand detailed PDF project dossiers (DPR) for rapid sanction.", "#10B981")
]

idx = 0
for r in range(3):
    for c in range(2):
        head, body, bcolor = cards_data[idx]
        cx = xs[c]
        cy = ys[r]

        card_box = patches.FancyBboxPatch((cx, cy), 3.7, 1.45, boxstyle="round,pad=0.03", edgecolor=bcolor, facecolor='white', linewidth=1.5)
        ax.add_patch(card_box)

        ax.text(cx + 1.85, cy + 1.2, head, color='#0F172A', fontsize=8.5, weight='bold', ha='center', va='center')
        ax.text(cx + 1.85, cy + 0.6, body, color='#475569', fontsize=7.5, ha='center', va='center', linespacing=1.3)

        idx += 1

# 4. Right Section — Unique Value Proposition Table & Extra Boxes
rx = 8.3

# Title Pill
title_pill = patches.FancyBboxPatch((rx, 6.1), 4.6, 0.5, boxstyle="round,pad=0.03", edgecolor='none', facecolor='#EDE9FE')
ax.add_patch(title_pill)
ax.text(rx + 2.3, 6.35, 'Unique Value Proposition', color='#182B49', fontsize=12, fontfamily='serif', weight='bold', ha='center', va='center')

# Matrix Header & Table Rows
cell_data = [
    # Header 0
    [("Metric", "#103969", "white"), ("Existing Solutions", "#103969", "white"), ("Existing Solutions", "#103969", "white"), ("Our Solution", "#103969", "white")],
    # Header 1
    [("", "#103969", "white"), ("Manual Surveys", "#103969", "white"), ("Basic RS/GIS", "#103969", "white"), ("SPRING AI", "#103969", "white")],
    # Row 1
    [("Processing Speed", "#103969", "white"), ("❌ 6 Months", "#FEE2E2", "#DC2626"), ("❌ 2-3 Wks", "#FEE2E2", "#DC2626"), ("✔ 30-Sec AI", "#DCFCE7", "#0284C7")],
    # Row 2
    [("Hydro-Geology", "#103969", "white"), ("❌ Surface Only", "#FEE2E2", "#DC2626"), ("Basic", "#FEE2E2", "#DC2626"), ("✔ Full PRSI", "#DCFCE7", "#0284C7")],
    # Row 3
    [("Landslide Mask", "#103969", "white"), ("❌ Risk Prone", "#FEE2E2", "#DC2626"), ("❌ Manual", "#FEE2E2", "#DC2626"), ("✔ Automated", "#DCFCE7", "#0284C7")],
    # Row 4
    [("DPR Dossier", "#103969", "white"), ("❌ Paper Draft", "#FEE2E2", "#DC2626"), ("❌ None", "#FEE2E2", "#DC2626"), ("✔ 1-Click PDF", "#DCFCE7", "#0284C7")]
]

col_w = [1.1, 1.0, 1.0, 1.5]
row_h = 0.55
start_y = 5.4

for r_i, row in enumerate(cell_data):
    start_x = rx
    y_pos = start_y - (r_i * row_h)
    for c_i, (txt, bgc, fgc) in enumerate(row):
        w = col_w[c_i]
        c_rect = patches.Rectangle((start_x, y_pos), w, row_h, facecolor=bgc, edgecolor='#E2E8F0', linewidth=0.8)
        ax.add_patch(c_rect)
        ax.text(start_x + (w/2.0), y_pos + (row_h/2.0), txt, color=fgc, fontsize=7.5, weight='bold', ha='center', va='center')
        start_x += w

# PRSI Score Box
prsi_box = patches.FancyBboxPatch((rx, 1.3), 4.6, 0.75, boxstyle="round,pad=0.03", edgecolor='#0284C7', facecolor='#F8FAFC', linewidth=1.5, linestyle='--')
ax.add_patch(prsi_box)
ax.text(rx + 2.3, 1.675, "UNIFIED PRSI SCORE: Uses a multi-index hydro-geological formula\n(Slope, Lithology, Rainfall, GW Depth) to deliver a unified recharge score.", color='#0F172A', fontsize=7.5, weight='bold', ha='center', va='center')

# Bot Box
bot_box = patches.FancyBboxPatch((rx, 0.55), 4.6, 0.6, boxstyle="round,pad=0.03", edgecolor='#0284C7', facecolor='#F8FAFC', linewidth=1.5, linestyle='--')
ax.add_patch(bot_box)
ax.text(rx + 2.3, 0.85, "🤖  AI-Driven Voice & Local Language Assistant — SpringBot", color='#182B49', fontsize=9.5, fontfamily='serif', weight='bold', ha='center', va='center')

# 5. Footer Blue Bar
footer = patches.Rectangle((0, 0), 13.333, 0.4, facecolor='#0277BD', edgecolor='none')
ax.add_patch(footer)
ax.text(0.4, 0.2, '@SIH Idea submission- Template', color='white', fontsize=8.5, va='center')
ax.text(12.8, 0.2, '2', color='white', fontsize=9.5, weight='bold', va='center')

ax.set_xlim(0, 13.333)
ax.set_ylim(0, 7.5)
ax.axis('off')
plt.tight_layout()

out_img = "assets/exact_winning_proposed_solution_preview.png"
plt.savefig(out_img, bbox_inches='tight', facecolor='white')
print(f"Exact winning slide preview image generated at {out_img}")
