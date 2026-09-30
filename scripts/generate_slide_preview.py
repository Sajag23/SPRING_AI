import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(13.333, 7.5), dpi=300)
ax.set_facecolor('#F8FAFC')
fig.patch.set_facecolor('#F8FAFC')

# Header
# Team Oval
oval = patches.Ellipse((1.3, 7.0), 1.8, 0.7, edgecolor='#2563EB', facecolor='white', linewidth=2)
ax.add_patch(oval)
ax.text(1.3, 7.0, 'Your Team\nName', color='#0F172A', fontsize=9, ha='center', va='center', weight='bold')

# Center Header Title
ax.text(6.666, 7.1, 'SPRING AI', color='#0F172A', fontsize=22, ha='center', va='center', weight='bold', fontfamily='serif')
ax.text(6.666, 6.7, 'AI-Driven Springshed Rejuvenation & Hydro-Geological Planning System', color='#475569', fontsize=8, ha='center', va='center')

# SIH Logo Badge
sih_box = patches.FancyBboxPatch((10.8, 6.6), 2.1, 0.75, boxstyle="round,pad=0.03", edgecolor='#CBD5E1', facecolor='white', linewidth=1.5)
ax.add_patch(sih_box)
ax.text(11.85, 7.1, 'SMART INDIA HACKATHON', color='#0F172A', fontsize=8, ha='center', va='center', weight='bold')
ax.text(11.85, 6.8, '2026', color='#2563EB', fontsize=12, ha='center', va='center', weight='bold')

# Main Section Title
ax.text(0.5, 6.1, '• Proposed Solution (Describe your Idea/Solution/Prototype)', color='#2563EB', fontsize=15, weight='bold')
ax.plot([0.5, 9.8], [5.95, 5.95], color='#2563EB', linewidth=2)

cards = [
    {
        "x": 0.5, "title": "💡 Detailed Explanation", "color": "#2563EB",
        "pill": "⚡ 30-Sec Delineation Engine",
        "bullets": [
            ("• Multi-Modal Data Fusion", "Copernicus DEM, IMD Rainfall, GSI Lithology & Sentinel-2."),
            ("• 30-Sec DEM Delineation", "Automates 3D catchment boundary & recharge mapping."),
            ("• PRSI Hydro-Geology Engine", "Scores pixel suitability for groundwater recharge structures."),
            ("• Offline App & 1-Click DPR", "Field verification GIS app generating MGNREGA dossiers.")
        ]
    },
    {
        "x": 4.8, "title": "🎯 Problem Addressed", "color": "#059669",
        "pill": "🌊 +45 Days Baseflow Extension",
        "bullets": [
            ("• Eliminates Survey Delays", "Cuts 6-month manual ground mapping down to instant AI."),
            ("• Prevents Structure Failure", "Uses subsurface lithology & soil infiltration rate."),
            ("• Landslide Safety Masking", "Automated safety mask excludes steep terrain (>30° slope)."),
            ("• Secures Tribal Water", "Extends spring baseflow (+45d) across 100+ Tribal Districts.")
        ]
    },
    {
        "x": 9.1, "title": "⚡ Innovation & Uniqueness", "color": "#D97706",
        "pill": "🚀 First-in-India GeoAI Matrix",
        "bullets": [
            ("• Proprietary PRSI Formula", "Multi-criteria hydro-geological decision matrix."),
            ("• Automated Safety Masking", "Hardcoded hazard & eco-sensitive constraint filtering."),
            ("• Zero-Trust Offline Sync", "Enables remote field workers to capture data without internet."),
            ("• Satellite-to-DPR Pipeline", "End-to-end automation from raw DEM to MGNREGA budget.")
        ]
    }
]

for card in cards:
    cx = card["x"]
    # Outer Card
    rect = patches.FancyBboxPatch((cx, 0.9), 3.75, 4.8, boxstyle="round,pad=0.05", edgecolor='#CBD5E1', facecolor='white', linewidth=1.5)
    ax.add_patch(rect)

    # Banner Top
    banner = patches.Rectangle((cx, 5.1), 3.75, 0.6, facecolor=card["color"], edgecolor='none')
    ax.add_patch(banner)
    ax.text(cx + 1.875, 5.4, card["title"], color='white', fontsize=11, weight='bold', ha='center', va='center')

    # Bullets
    y_curr = 4.85
    for b_head, b_desc in card["bullets"]:
        ax.text(cx + 0.2, y_curr, b_head, color='#0F172A', fontsize=9, weight='bold', va='top')
        ax.text(cx + 0.35, y_curr - 0.22, b_desc, color='#475569', fontsize=7.5, va='top')
        y_curr -= 0.95

    # Pill
    pill_box = patches.FancyBboxPatch((cx + 0.3, 1.05), 3.15, 0.45, boxstyle="round,pad=0.03", edgecolor=card["color"], facecolor='#F1F5F9', linewidth=1.2)
    ax.add_patch(pill_box)
    ax.text(cx + 1.875, 1.275, card["pill"], color=card["color"], fontsize=8.5, weight='bold', ha='center', va='center')

# Footer Bar
footer = patches.Rectangle((0, 0), 13.333, 0.5, facecolor='#0277BD', edgecolor='none')
ax.add_patch(footer)
ax.text(0.4, 0.25, '@SIH Idea submission- Template', color='white', fontsize=9, va='center')
ax.text(12.8, 0.25, '2', color='white', fontsize=10, weight='bold', va='center')

ax.set_xlim(0, 13.333)
ax.set_ylim(0, 7.5)
ax.axis('off')
plt.tight_layout()

out_img = "assets/proposed_solution_slide_preview.png"
plt.savefig(out_img, bbox_inches='tight', facecolor='#F8FAFC')
print(f"Slide preview image generated at {out_img}")
