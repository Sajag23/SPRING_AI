import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(13.333, 7.5), dpi=300)
ax.set_facecolor('white')
fig.patch.set_facecolor('white')

# 1. Header
oval = patches.Ellipse((1.3, 7.0), 1.8, 0.65, edgecolor='#0284C7', facecolor='white', linewidth=1.5)
ax.add_patch(oval)
ax.text(1.3, 7.0, 'SPRING AI', color='#182B49', fontsize=10, fontfamily='serif', weight='bold', ha='center', va='center')

ax.text(6.666, 7.0, 'RESEARCH AND REFERENCES', color='#182B49', fontsize=22, fontfamily='serif', weight='bold', ha='center', va='center')
ax.text(12.8, 7.15, 'SMART INDIA HACKATHON', color='#182B49', fontsize=8, weight='bold', ha='right')
ax.text(12.8, 6.85, '2026', color='#0284C7', fontsize=12, weight='bold', ha='right')

# 2. 4 Reference Cards (2x2 Grid)
xs = [0.4, 6.933]
ys = [3.9, 1.0]

categories = [
    ("🏛️ National Portals & Satellite Datasets", "#0284C7", [
        ("• Copernicus Open Access Hub (ESA): ", "30m Global DEM for catchment flow accumulation."),
        ("• Central Ground Water Board (CGWB): ", "National groundwater levels & aquifer maps."),
        ("• Geological Survey of India (GSI): ", "Lithology, rock permeability & formation maps."),
        ("• India Meteorological Dept (IMD): ", "High-res gridded rainfall & seasonal precipitation.")
    ]),
    ("📚 Academic & Scientific Literature", "#059669", [
        ("• NITI Aayog Report (2018): ", "Inventory and Revival of Springs in Himalayas."),
        ("• Hydrogeology Journal (Elsevier): ", "Groundwater Recharge Delineation via Remote Sensing."),
        ("• MoTA & Jal Shakti Guidelines: ", "8-Step Methodology for Springshed Management."),
        ("• ISRO Bhuvan Geo-Spatial Platform: ", "Land Use / Land Cover 1:50,000 spatial standards.")
    ]),
    ("📜 Regulatory & Scheme Frameworks", "#D97706", [
        ("• MGNREGA Operational Guidelines: ", "Schedule of rates for recharge structures."),
        ("• Jal Shakti Abhiyan Guidelines: ", "Specs for Staggered Trenches & Check Dams."),
        ("• NRSC Hydrological Manual: ", "Satellite-based flow routing protocols.")
    ]),
    ("🌐 Tech Stack & Open Source Libraries", "#7C3AED", [
        ("• GDAL / Rasterio & PyTorch: ", "Python spatial raster processing & DEM algorithms."),
        ("• PostGIS & Mapbox GL JS SDK: ", "Spatial indexing & vector tile rendering."),
        ("• SPRING AI Research Portal: ", "https://www.spring-ai.in/research-hub")
    ])
]

idx = 0
for r in range(2):
    for c in range(2):
        title, color, items = categories[idx]
        cx = xs[c]
        cy = ys[r]

        # Card Box
        card = patches.FancyBboxPatch((cx, cy), 6.0, 2.7, boxstyle="round,pad=0.03", edgecolor=color, facecolor='#F8FAFC', linewidth=1.5)
        ax.add_patch(card)

        # Banner Header
        banner = patches.Rectangle((cx, cy + 2.15), 6.0, 0.55, facecolor=color, edgecolor='none')
        ax.add_patch(banner)
        ax.text(cx + 0.2, cy + 2.425, title, color='white', fontsize=11, fontfamily='serif', weight='bold', va='center')

        # Items
        iy = cy + 1.95
        for head, desc in items:
            ax.text(cx + 0.2, iy, head, color='#182B49', fontsize=8.5, weight='bold', va='top')
            ax.text(cx + 2.4, iy, desc, color='#475569', fontsize=8, va='top')
            iy -= 0.45

        idx += 1

# 3. Footer
footer = patches.Rectangle((0, 0), 13.333, 0.4, facecolor='#0277BD', edgecolor='none')
ax.add_patch(footer)
ax.text(0.4, 0.2, '@SIH Idea submission- Template', color='white', fontsize=8.5, va='center')
ax.text(12.8, 0.2, '6', color='white', fontsize=9.5, weight='bold', va='center')

ax.set_xlim(0, 13.333)
ax.set_ylim(0, 7.5)
ax.axis('off')
plt.tight_layout()

out_img = "assets/exact_winning_research_preview.png"
plt.savefig(out_img, bbox_inches='tight', facecolor='white')
print(f"Research slide preview generated at {out_img}")
