import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_light_highlevel_architecture():
    os.makedirs("assets", exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(14, 7.5), dpi=300)
    ax.set_facecolor('#F8FAFC') # Clean light slate background
    fig.patch.set_facecolor('#F8FAFC')

    # Header Title Banner
    ax.text(7.0, 7.0, "SPRING AI — HIGH-LEVEL SYSTEM ARCHITECTURE", color='#0F172A', fontsize=18, fontfamily='serif', weight='bold', ha='center', va='center')
    ax.text(7.0, 6.6, "End-to-End GeoAI Pipeline from Satellite Data to Field Execution", color='#0284C7', fontsize=10, ha='center', va='center')

    # 4 Main High-Level Stage Columns
    stages = [
        {
            "num": "01", "name": "DATA INGESTION", "icon": "🛰️",
            "border": "#0284C7", "bg": "#FFFFFF", "pill_bg": "#E0F2FE", "head_color": "#0369A1",
            "items": [
                ("Copernicus DEM (30m)", "Terrain & Slope"),
                ("IMD Rainfall Data", "Gridded Hydro-Data"),
                ("GSI Lithology Maps", "Rock Infiltration"),
                ("CGWB Aquifer Wells", "Water Table Depth")
            ]
        },
        {
            "num": "02", "name": "CORE GEO-AI ENGINE", "icon": "⚙️",
            "border": "#D97706", "bg": "#FFFFFF", "pill_bg": "#FEF3C7", "head_color": "#B45309",
            "items": [
                ("30-Sec DEM Delineation", "3D Catchment Mapping"),
                ("PRSI Hydro-Scoring", "Multi-Criteria Matrix"),
                ("Structure Selector", "Trenches & Check Dams"),
                ("Slope >30° Safety Mask", "Landslide Risk Exclusion")
            ]
        },
        {
            "num": "03", "name": "CLOUD & BACKEND", "icon": "☁️",
            "border": "#7C3AED", "bg": "#FFFFFF", "pill_bg": "#F3E8FF", "head_color": "#6B21A8",
            "items": [
                ("FastAPI Microservices", "Async REST Endpoints"),
                ("PostGIS Spatial DB", "GeoJSON Vector Engine"),
                ("Offline Sync Pipeline", "Zero-Trust Field Buffer"),
                ("SpringBot Core Engine", "Voice & Language LLM")
            ]
        },
        {
            "num": "04", "name": "FIELD & MINISTRY APPS", "icon": "📱",
            "border": "#059669", "bg": "#FFFFFF", "pill_bg": "#D1FAE5", "head_color": "#047857",
            "items": [
                ("Interactive Web GIS", "Mapbox Analytics Dashboard"),
                ("Jal Sahi Mobile App", "Offline Field Verification"),
                ("1-Click MGNREGA DPR", "Automated PDF Dossier"),
                ("SpringBot Voice Assistant", "Local Dialect Support")
            ]
        }
    ]

    col_w = 2.9
    gap = 0.45
    start_x = 0.5

    for idx, stage in enumerate(stages):
        cx = start_x + idx * (col_w + gap)

        # Stage Outer Container Card
        card = patches.FancyBboxPatch((cx, 0.8), col_w, 5.3, boxstyle="round,pad=0.04", edgecolor=stage["border"], facecolor=stage["bg"], linewidth=1.8)
        ax.add_patch(card)

        # Stage Number Badge Circle
        num_circle = patches.Circle((cx + col_w/2.0, 5.7), 0.35, edgecolor=stage["border"], facecolor='#FFFFFF', linewidth=2)
        ax.add_patch(num_circle)
        ax.text(cx + col_w/2.0, 5.7, stage["num"], color='#0F172A', fontsize=12, weight='bold', ha='center', va='center')

        # Header Title Banner Pill
        head_pill = patches.FancyBboxPatch((cx + 0.15, 4.8), col_w - 0.3, 0.5, boxstyle="round,pad=0.03", edgecolor='none', facecolor=stage["pill_bg"])
        ax.add_patch(head_pill)
        ax.text(cx + col_w/2.0, 5.05, f"{stage['icon']}  {stage['name']}", color=stage["head_color"], fontsize=10.5, fontfamily='serif', weight='bold', ha='center', va='center')

        # Items list
        iy = 4.3
        for title, subtitle in stage["items"]:
            # Sub-item pill card
            sub_card = patches.FancyBboxPatch((cx + 0.15, iy - 0.65), col_w - 0.3, 0.7, boxstyle="round,pad=0.02", edgecolor='#E2E8F0', facecolor='#F8FAFC', linewidth=1.0)
            ax.add_patch(sub_card)

            ax.text(cx + col_w/2.0, iy - 0.28, title, color='#0F172A', fontsize=9, weight='bold', ha='center', va='center')
            ax.text(cx + col_w/2.0, iy - 0.50, subtitle, color='#475569', fontsize=7.5, ha='center', va='center')

            iy -= 0.88

        # Flow Arrow to Next Stage
        if idx < len(stages) - 1:
            ax.annotate('', xy=(cx + col_w + gap - 0.05, 3.4), xytext=(cx + col_w + 0.05, 3.4),
                        arrowprops=dict(facecolor=stage["border"], edgecolor=stage["border"], width=2.5, headwidth=8, headlength=8))

    # Bottom Footer Bar
    ax.plot([0.5, 13.5], [0.4, 0.4], color='#CBD5E1', linewidth=1)
    ax.text(0.5, 0.2, "SPRING AI — AI-Powered Springshed Rejuvenation System", color='#475569', fontsize=8.5, va='center')
    ax.text(13.5, 0.2, "Smart India Hackathon 2026", color='#0284C7', fontsize=8.5, weight='bold', ha='right', va='center')

    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    plt.tight_layout()

    out_path = "assets/spring_ai_high_level_architecture_light.png"
    plt.savefig(out_path, bbox_inches='tight', facecolor='#F8FAFC')
    print(f"Light Theme Architecture Diagram saved to {out_path}")

if __name__ == "__main__":
    generate_light_highlevel_architecture()
