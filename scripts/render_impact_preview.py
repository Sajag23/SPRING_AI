import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(13.333, 7.5), dpi=300)
ax.set_facecolor('white')
fig.patch.set_facecolor('white')

# 1. Header
oval = patches.Ellipse((1.3, 7.0), 1.8, 0.65, edgecolor='#0284C7', facecolor='white', linewidth=1.5)
ax.add_patch(oval)
ax.text(1.3, 7.0, 'SPRING AI', color='#182B49', fontsize=10, fontfamily='serif', weight='bold', ha='center', va='center')

ax.text(6.666, 7.0, 'IMPACT AND BENEFITS', color='#182B49', fontsize=22, fontfamily='serif', weight='bold', ha='center', va='center')
ax.text(12.8, 7.15, 'SMART INDIA HACKATHON', color='#182B49', fontsize=8, weight='bold', ha='right')
ax.text(12.8, 6.85, '2026', color='#0284C7', fontsize=12, weight='bold', ha='right')

# 2. Executive Summary Banner
banner = patches.FancyBboxPatch((2.0, 6.1), 9.333, 0.65, boxstyle="round,pad=0.03", edgecolor='#0284C7', facecolor='#E0F2FE', linewidth=1)
ax.add_patch(banner)
ax.text(6.666, 6.425, "Solar panels boomed because of rising electricity costs + government push.\nSimilarly, acute water scarcity + spring rejuvenation mandates are pushing SPRING AI forward.", color='#182B49', fontsize=8.5, weight='bold', ha='center', va='center')

# 3. Left Iceberg Model Box Representation
ib_box = patches.FancyBboxPatch((0.4, 0.85), 4.5, 5.0, boxstyle="round,pad=0.03", edgecolor='#0284C7', facecolor='#F0F9FF', linewidth=1.5)
ax.add_patch(ib_box)

# Waterline
ax.plot([0.4, 4.9], [4.5, 4.5], color='#38BDF8', linestyle='--', linewidth=2)
ax.text(0.6, 4.6, "Water Baseline Level", color='#0284C7', fontsize=7.5, weight='bold')

# Visible Tip
tip = patches.Polygon([[2.65, 4.5], [2.15, 5.5], [3.15, 4.5]], facecolor='#93C5FD', edgecolor='#1D4ED8')
ax.add_patch(tip)
ax.text(2.65, 4.95, "Visible Water Crisis\n& Field Surveys", color='#0F172A', fontsize=7, weight='bold', ha='center')

# Submerged Iceberg
submerged = patches.Polygon([[2.65, 4.5], [1.15, 1.2], [4.15, 1.2]], facecolor='#1D4ED8', alpha=0.85)
ax.add_patch(submerged)
ax.text(2.65, 3.7, "Untapped Recharge Potential\n(18.5 Billion Liters Water Storage)", color='white', fontsize=7.5, weight='bold', ha='center')
ax.text(2.65, 2.7, "Automated Slope >30° Safety Masks\n& MGNREGA Scheme Alignment", color='#E0F2FE', fontsize=7, ha='center')
ax.text(2.65, 1.7, "100+ Scheduled Tribal Districts Secured", color='#93C5FD', fontsize=7, weight='bold', ha='center')

# 4. Right Top: 5 Multi-Level Benefit Cards
rx = 5.1

cards_info = [
    ("• Household Level", "Lower water bills, 4.2M Liters annual water security, easy self-assessment GIS tool.", 5.1, 4.85, 3.7, 1.0),
    ("• Community Level", "Collective water conservation, secures 100+ Scheduled Tribal Districts & livelihoods.", 9.0, 4.85, 3.933, 1.0),
    ("• Regional Level", "Groundwater table rise (+1.2m), baseflow extension (+45 days), reduced flash runoff.", 5.1, 3.7, 3.7, 1.0),
    ("• Government Level", "Data-driven policymaking, easier monitoring of recharge mandates, MGNREGA budget optimization.", 9.0, 3.7, 3.933, 1.0),
    ("• Environmental / Long-Term", "Groundwater replenishment, climate change resilience, sustainable future mountain water resources.", 5.1, 2.55, 7.833, 0.95)
]

for title, desc, cx, cy, cw, ch in cards_info:
    cbox = patches.FancyBboxPatch((cx, cy), cw, ch, boxstyle="round,pad=0.03", edgecolor='#BAE6FD', facecolor='#EEF2FF', linewidth=1.2)
    ax.add_patch(cbox)
    ax.text(cx + 0.15, cy + ch - 0.25, title, color='#182B49', fontsize=9, fontfamily='serif', weight='bold', va='top')
    ax.text(cx + 0.3, cy + ch - 0.52, desc, color='#475569', fontsize=7.5, va='top')

# 5. Right Bottom: Value Chain
ax.text(9.0, 2.1, "Springshed Rejuvenation Value Chain", color='#182B49', fontsize=12, fontfamily='serif', weight='bold', ha='center')

vc_list = [
    ("Untapped Resource", "Springs Available in Mountain Belts"),
    ("AI Delineation", "Copernicus DEM & PRSI Scoring"),
    ("Field Sync", "Jal Sahi Mobile GIS App"),
    ("Govt / MGNREGA", "Itemized DPR Budget Sanction"),
    ("Sustainable Water", "+45 Days Extended Baseflow")
]

vw = 1.45
start_vx = 5.1
gap_v = 0.12

for idx, (vh, vd) in enumerate(vc_list):
    vx = start_vx + idx * (vw + gap_v)
    vbox = patches.FancyBboxPatch((vx, 0.45), vw, 1.4, boxstyle="round,pad=0.03", edgecolor='#0284C7', facecolor='white', linewidth=1.2)
    ax.add_patch(vbox)
    
    col = '#059669' if idx % 2 == 0 else '#0284C7'
    ax.text(vx + vw/2.0, 1.6, "◆", color=col, fontsize=12, ha='center', va='center')
    ax.text(vx + vw/2.0, 1.25, vh, color='#182B49', fontsize=7.5, weight='bold', ha='center', va='center')
    ax.text(vx + vw/2.0, 0.85, vd, color='#475569', fontsize=6.5, ha='center', va='center')

# 6. Footer
footer = patches.Rectangle((0, 0), 13.333, 0.4, facecolor='#0277BD', edgecolor='none')
ax.add_patch(footer)
ax.text(0.4, 0.2, '@SIH Idea submission- Template', color='white', fontsize=8.5, va='center')
ax.text(12.8, 0.2, '5', color='white', fontsize=9.5, weight='bold', va='center')

ax.set_xlim(0, 13.333)
ax.set_ylim(0, 7.5)
ax.axis('off')
plt.tight_layout()

out_img = "assets/exact_winning_impact_preview.png"
plt.savefig(out_img, bbox_inches='tight', facecolor='white')
print(f"Impact slide preview generated at {out_img}")
