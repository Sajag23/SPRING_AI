import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(13.333, 7.5), dpi=300)
ax.set_facecolor('white')
fig.patch.set_facecolor('white')

# 1. Header
ax.text(0.4, 7.0, 'SPRING AI', color='#D97706', fontsize=20, fontfamily='serif', weight='bold', va='center')
ax.text(6.666, 7.0, 'TECHNICAL APPROACH', color='#182B49', fontsize=22, fontfamily='serif', weight='bold', ha='center', va='center')
ax.text(12.8, 7.15, 'SMART INDIA HACKATHON', color='#182B49', fontsize=8, weight='bold', ha='right')
ax.text(12.8, 6.85, '2026', color='#0284C7', fontsize=12, weight='bold', ha='right')

# 2. Left Column: FLOW OF OUR SOLUTION
lx = 0.4
lw = 3.4

flow_pill = patches.FancyBboxPatch((lx, 6.1), lw, 0.45, boxstyle="round,pad=0.03", edgecolor='none', facecolor='#FED7AA')
ax.add_patch(flow_pill)
ax.text(lx + lw/2.0, 6.325, 'FLOW OF OUR SOLUTION', color='#182B49', fontsize=11, fontfamily='serif', weight='bold', ha='center', va='center')

steps = [
    ("Multi-Modal Data Integration", "(Copernicus DEM, IMD Rainfall, GSI Lithology)"),
    ("Catchment Feature Extraction", "(DEM Flow Accumulation & Slope Density)"),
    ("PRSI Index Calculation", "(Automated Multi-Criteria Hydro Scoring)"),
    ("Automated Safety Masking", "(Slope >30° Exclusion & Hazard Mask)"),
    ("Structure Recommendation", "(Staggered Trenches, Check Dams)"),
    ("1-Click MGNREGA DPR", "(PDF Dossier, GIS Dashboard & Alerts)")
]

y_start = 5.3
gap = 0.95
for idx, (st, sd) in enumerate(steps):
    sy = y_start - idx * gap
    box = patches.FancyBboxPatch((lx, sy), lw, 0.78, boxstyle="round,pad=0.03", edgecolor='#0284C7', facecolor='#103969', linewidth=1.2)
    ax.add_patch(box)
    ax.text(lx + lw/2.0, sy + 0.52, st, color='white', fontsize=8.5, weight='bold', ha='center', va='center')
    ax.text(lx + lw/2.0, sy + 0.25, sd, color='#BAE6FD', fontsize=7, ha='center', va='center')

# 3. Center Top: TECH STACK
cx = 4.1
cw = 4.5

tech_pill = patches.FancyBboxPatch((cx, 6.1), cw, 0.45, boxstyle="round,pad=0.03", edgecolor='none', facecolor='#BAE6FD')
ax.add_patch(tech_pill)
ax.text(cx + cw/2.0, 6.325, 'TECH STACK', color='#182B49', fontsize=11, fontfamily='serif', weight='bold', ha='center', va='center')

tech_container = patches.FancyBboxPatch((cx, 2.9), cw, 3.0, boxstyle="round,pad=0.03", edgecolor='#CBD5E1', facecolor='#F8FAFC', linewidth=1.2)
ax.add_patch(tech_container)

tech_info = [
    ("• Deployment & Cloud:", "Docker, Vercel, GCP / AWS Serverless Functions"),
    ("• Security & Auth:", "OAuth 2.0, JWT, Role-Based Access Control (RBAC)"),
    ("• Frontend & GIS UI:", "React.js, Mapbox GL JS, Leaflet.js, Tailwind CSS"),
    ("• Backend & Spatial DB:", "Python (FastAPI), PostGIS, PyTorch, GDAL")
]

ty = 5.5
for title, items in tech_info:
    ax.text(cx + 0.2, ty, title, color='#182B49', fontsize=9, weight='bold', va='top')
    ax.text(cx + 0.35, ty - 0.25, items, color='#0284C7', fontsize=8.5, va='top')
    ty -= 0.65

# 4. Right Top: PRSI FORMULA CALCULATION
rx = 8.8
rw = 4.133

prsi_pill = patches.FancyBboxPatch((rx, 6.1), rw, 0.45, boxstyle="round,pad=0.03", edgecolor='none', facecolor='#BBF7D0')
ax.add_patch(prsi_pill)
ax.text(rx + rw/2.0, 6.325, 'PRSI FORMULA CALCULATION', color='#182B49', fontsize=11, fontfamily='serif', weight='bold', ha='center', va='center')

prsi_container = patches.FancyBboxPatch((rx, 2.9), rw, 3.0, boxstyle="round,pad=0.03", edgecolor='#16A34A', facecolor='#F8FAFC', linewidth=1.2)
ax.add_patch(prsi_container)

ax.text(rx + 0.2, 5.6, "❏ PRSI Weighted Hydro-Geological Formula:", color='#182B49', fontsize=8.5, weight='bold')
ax.text(rx + rw/2.0, 5.15, "PRSI = 0.35(S) + 0.25(L) + 0.20(G) + 0.15(R) + 0.05(D)", color='#0284C7', fontsize=8.5, fontfamily='serif', weight='bold', ha='center')

weights_list = [
    "S = Slope Factor (35% weightage)",
    "L = Rock Lithology & Infiltration (25% weightage)",
    "G = Groundwater Depth (20% weightage)",
    "R = Rainfall Distribution (15% weightage)",
    "D = Drainage Density (5% weightage)"
]
wy = 4.6
for wtext in weights_list:
    ax.text(rx + 0.3, wy, f"• {wtext}", color='#0F172A', fontsize=7.5, va='top')
    wy -= 0.35

# 5. Bottom Right: ROLE BASED ACCESS CONTROL (RBAC)
rb_x = 4.1
rb_w = 8.833
rb_y = 2.25

rbac_pill = patches.FancyBboxPatch((rb_x, rb_y), rb_w, 0.45, boxstyle="round,pad=0.03", edgecolor='none', facecolor='#E9D5FF')
ax.add_patch(rbac_pill)
ax.text(rb_x + rb_w/2.0, rb_y + 0.225, 'ROLE BASED ACCESS CONTROL MATRIX', color='#182B49', fontsize=11, fontfamily='serif', weight='bold', ha='center', va='center')

# Matrix Header & Rows
rbac_headers = ["ROLE", "GIS MAPS", "PRSI", "REPORTS", "GW DATA", "FORECAST", "ALERTS", "OFFLINE SYNC", "RESEARCH"]
rbac_data = [
    ["MINISTRY OFFICER", "✔", "✔", "✔", "✔", "✔", "✔", "❌", "✔"],
    ["HYDROLOGIST / SCIENTIST", "✔", "✔", "✔", "✔", "✔", "✔", "❌", "✔"],
    ["DISTRICT OFFICER", "✔", "✔", "✔", "✔", "✔", "✔", "✔", "❌"],
    ["FIELD SURVEYOR (JAL SAHI)", "✔", "❌", "✔", "❌", "❌", "✔", "✔", "❌"]
]

col_widths = [1.833, 0.875, 0.875, 0.875, 0.875, 0.875, 0.875, 0.875, 0.875]
row_height = 0.38
start_y_table = rb_y - 0.45

# Draw Header Row
start_x = rb_x
for c_i, htxt in enumerate(rbac_headers):
    w = col_widths[c_i]
    r_hdr = patches.Rectangle((start_x, start_y_table), w, row_height, facecolor='#103969', edgecolor='#CBD5E1', linewidth=0.5)
    ax.add_patch(r_hdr)
    ax.text(start_x + w/2.0, start_y_table + row_height/2.0, htxt, color='white', fontsize=7, weight='bold', ha='center', va='center')
    start_x += w

# Draw Data Rows
for r_i, rvals in enumerate(rbac_data):
    start_x = rb_x
    curr_y = start_y_table - (r_i + 1) * row_height
    bgc = '#F8FAFC' if r_i % 2 == 0 else 'white'
    for c_i, val in enumerate(rvals):
        w = col_widths[c_i]
        r_cell = patches.Rectangle((start_x, curr_y), w, row_height, facecolor=bgc, edgecolor='#CBD5E1', linewidth=0.5)
        ax.add_patch(r_cell)
        
        fgc = '#16A34A' if val == '✔' else ('#DC2626' if val == '❌' else '#182B49')
        align = 'center' if c_i > 0 else 'left'
        tx_pos = start_x + w/2.0 if c_i > 0 else start_x + 0.1
        ax.text(tx_pos, curr_y + row_height/2.0, val, color=fgc, fontsize=7.5, weight='bold', ha=align, va='center')
        start_x += w

# 6. Footer
footer = patches.Rectangle((0, 0), 13.333, 0.4, facecolor='#0277BD', edgecolor='none')
ax.add_patch(footer)
ax.text(0.4, 0.2, '@SIH Idea submission- Template', color='white', fontsize=8.5, va='center')
ax.text(12.8, 0.2, '3', color='white', fontsize=9.5, weight='bold', va='center')

ax.set_xlim(0, 13.333)
ax.set_ylim(0, 7.5)
ax.axis('off')
plt.tight_layout()

out_img = "assets/exact_winning_technical_approach_preview.png"
plt.savefig(out_img, bbox_inches='tight', facecolor='white')
print(f"Technical Approach slide preview generated at {out_img}")
