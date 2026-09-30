import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(13.333, 7.5), dpi=300)
ax.set_facecolor('white')
fig.patch.set_facecolor('white')

# 1. Header
oval = patches.Ellipse((1.3, 7.0), 1.8, 0.65, edgecolor='#0284C7', facecolor='white', linewidth=1.5)
ax.add_patch(oval)
ax.text(1.3, 7.0, 'SPRING AI', color='#182B49', fontsize=10, fontfamily='serif', weight='bold', ha='center', va='center')

ax.text(6.666, 7.0, 'FEASIBILITY AND VIABILITY', color='#182B49', fontsize=22, fontfamily='serif', weight='bold', ha='center', va='center')
ax.text(12.8, 7.15, 'SMART INDIA HACKATHON', color='#182B49', fontsize=8, weight='bold', ha='right')
ax.text(12.8, 6.85, '2026', color='#0284C7', fontsize=12, weight='bold', ha='right')

# 2. Left Container & Numbered Nodes (Feasibility, Challenges, Strategy)
lx = 0.4
lw = 8.2
lh = 5.6
ly = 0.95

# Outer Box
rect = patches.FancyBboxPatch((lx, ly), lw, lh, boxstyle="round,pad=0.03", edgecolor='#0284C7', facecolor='#F8FAFC', linewidth=1.5)
ax.add_patch(rect)

# Vertical connecting line
ax.plot([lx + 0.45, lx + 0.45], [ly + 0.5, ly + 5.0], color='#0284C7', linewidth=2.5, zorder=2)

sections = [
    ("1", "Feasibility", 5.2, [
        ("Technically → ", "Existing satellite APIs (Copernicus DEM, IMD, GSI) & custom PRSI algorithms."),
        ("Economically → ", "Optimizes MGNREGA budgets, saves millions in manual surveys."),
        ("Socially → ", "Solves drinking water scarcity across 100+ Scheduled Tribal Districts.")
    ]),
    ("2", "Challenges", 3.4, [
        ("Data Accuracy → ", "Remote tribal mountain terrain data & local rainfall observations may be sparse."),
        ("User Adoption → ", "Low digital literacy among Gram Panchayat field surveyors (Jal Sahi)."),
        ("Ground Truth Reliability → ", "Risk of unverified field reports or incorrect GPS site coordinates.")
    ]),
    ("3", "Strategy", 1.6, [
        ("Data Accuracy → ", "Multi-satellite validation (Sentinel-2, Copernicus DEM) + local interpolation."),
        ("User Adoption → ", "Voice-assisted AI (SpringBot in tribal languages) & offline-first sync."),
        ("Ground Truth Reliability → ", "Geo-tagged photo proof, auto-GPS timestamping & 2-tier approval.")
    ])
]

for num, title, sy, bullets in sections:
    # Circle Node
    circ = patches.Circle((lx + 0.45, sy + 0.3), 0.3, edgecolor='#0284C7', facecolor='white', linewidth=2, zorder=3)
    ax.add_patch(circ)
    ax.text(lx + 0.45, sy + 0.3, num, color='#182B49', fontsize=12, fontfamily='serif', weight='bold', ha='center', va='center', zorder=4)

    # Title Tag Box
    t_box = patches.Rectangle((lx + 0.9, sy + 0.1), 1.8, 0.42, facecolor='#103969', edgecolor='none', zorder=3)
    ax.add_patch(t_box)
    ax.text(lx + 1.8, sy + 0.31, title, color='white', fontsize=11, fontfamily='serif', weight='bold', ha='center', va='center', zorder=4)

    # Bullets
    by = sy - 0.05
    for lead, body in bullets:
        ax.text(lx + 0.95, by, "• ", color='#182B49', fontsize=8.5, weight='bold', va='top')
        ax.text(lx + 1.15, by, lead, color='#0F172A', fontsize=8.5, weight='bold', va='top')
        ax.text(lx + 2.45, by, body, color='#475569', fontsize=8, va='top')
        by -= 0.35

# 3. Right Column: OUR FEASIBLE SOLUTION (8 Pills)
rx = 8.8
rw = 4.133
ry = 0.95

ax.text(rx + rw/2.0, 6.35, "Our Feasible Solution", color='#182B49', fontsize=14, fontfamily='serif', weight='bold', ha='center')

pills_list = [
    "Transparent MGNREGA itemized cost estimation.",
    "Map-based DEM input + auto satellite data fetch.",
    "Smart hydro-geological assessment with detailed PDF DPR.",
    "Verified government structure catalog (Check Dams, Trenches).",
    "End-to-end service flow — DEM Delineation → PRSI → DPR.",
    "Voice & Local Tribal Language support (SpringBot).",
    "Offline-first mobile GIS sync for remote tribal belts.",
    "Runoff & water storage capacity estimates (+45d baseflow)."
]

py_start = 5.7
gap_p = 0.62
for idx, ptxt in enumerate(pills_list):
    py = py_start - idx * gap_p
    pbox = patches.FancyBboxPatch((rx, py), rw, 0.52, boxstyle="round,pad=0.03", edgecolor='#86EFAC', facecolor='#DCFCE7', linewidth=1.2)
    ax.add_patch(pbox)
    ax.text(rx + rw/2.0, py + 0.26, ptxt, color='#182B49', fontsize=8.5, weight='bold', ha='center', va='center')

# Bottom URL Banner
url_box = patches.FancyBboxPatch((lx, 0.52), 12.533, 0.35, boxstyle="round,pad=0.03", edgecolor='#0284C7', facecolor='#E0F2FE', linewidth=1)
ax.add_patch(url_box)
ax.text(6.666, 0.695, "https://www.spring-ai.in/assessment", color='#0284C7', fontsize=9.5, weight='bold', ha='center', va='center')

# 4. Footer
footer = patches.Rectangle((0, 0), 13.333, 0.4, facecolor='#0277BD', edgecolor='none')
ax.add_patch(footer)
ax.text(0.4, 0.2, '@SIH Idea submission- Template', color='white', fontsize=8.5, va='center')
ax.text(12.8, 0.2, '4', color='white', fontsize=9.5, weight='bold', va='center')

ax.set_xlim(0, 13.333)
ax.set_ylim(0, 7.5)
ax.axis('off')
plt.tight_layout()

out_img = "assets/exact_winning_feasibility_preview.png"
plt.savefig(out_img, bbox_inches='tight', facecolor='white')
print(f"Feasibility slide preview generated at {out_img}")
