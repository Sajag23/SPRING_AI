import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_creative_highlevel_architecture():
    os.makedirs("assets", exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(14, 7.5), dpi=300)
    ax.set_facecolor('#0F172A') # Dark Navy modern tech theme background
    fig.patch.set_facecolor('#0F172A')

    # Header Title Banner
    ax.text(7.0, 7.0, "SPRING AI — HIGH-LEVEL SYSTEM ARCHITECTURE", color='white', fontsize=18, fontfamily='serif', weight='bold', ha='center', va='center')
    ax.text(7.0, 6.6, "End-to-End GeoAI Pipeline from Satellite Data to Field Execution", color='#38BDF8', fontsize=10, ha='center', va='center')

    # 4 Main High-Level Stage Columns
    stages = [
        {
            "num": "01", "name": "DATA INGESTION", "icon": "🛰️",
            "border": "#38BDF8", "bg": "#1E293B", "head_color": "#38BDF8",
            "items": [
                ("Copernicus DEM (30m)", "Terrain & Slope"),
                ("IMD Rainfall Data", "Gridded Hydro-Data"),
                ("GSI Lithology Maps", "Rock Infiltration"),
                ("CGWB Aquifer Wells", "Water Table Depth")
            ]
        },
        {
            "num": "02", "name": "CORE GEO-AI ENGINE", "icon": "⚙️",
            "border": "#F59E0B", "bg": "#1E293B", "head_color": "#F59E0B",
            "items": [
                ("30-Sec DEM Delineation", "3D Catchment Mapping"),
                ("PRSI Hydro-Scoring", "Multi-Criteria Matrix"),
                ("Structure Selector", "Trenches & Check Dams"),
                ("Slope >30° Safety Mask", "Landslide Risk Exclusion")
            ]
        },
        {
            "num": "03", "name": "CLOUD & BACKEND", "icon": "☁️",
            "border": "#A855F7", "bg": "#1E293B", "head_color": "#A855F7",
            "items": [
                ("FastAPI Microservices", "Async REST Endpoints"),
                ("PostGIS Spatial DB", "GeoJSON Vector Engine"),
                ("Offline Sync Pipeline", "Zero-Trust Field Buffer"),
                ("SpringBot Core Engine", "Voice & Language LLM")
            ]
        },
        {
            "num": "04", "name": "FIELD & MINISTRY APPS", "icon": "📱",
            "border": "#10B981", "bg": "#1E293B", "head_color": "#10B981",
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
        card = patches.FancyBboxPatch((cx, 0.8), col_w, 5.3, boxstyle="round,pad=0.04", edgecolor=stage["border"], facecolor=stage["bg"], linewidth=2.0)
        ax.add_patch(card)

        # Stage Number Badge Circle
        num_circle = patches.Circle((cx + col_w/2.0, 5.7), 0.35, edgecolor=stage["border"], facecolor='#0F172A', linewidth=2)
        ax.add_patch(num_circle)
        ax.text(cx + col_w/2.0, 5.7, stage["num"], color='white', fontsize=12, weight='bold', ha='center', va='center')

        # Header Title
        ax.text(cx + col_w/2.0, 5.0, f"{stage['icon']}  {stage['name']}", color=stage["head_color"], fontsize=11, fontfamily='serif', weight='bold', ha='center', va='center')
        ax.plot([cx + 0.3, cx + col_w - 0.3], [4.7, 4.7], color=stage["border"], linewidth=1.5, linestyle='--')

        # Items list
        iy = 4.3
        for title, subtitle in stage["items"]:
            # Sub-item pill card
            sub_card = patches.FancyBboxPatch((cx + 0.15, iy - 0.65), col_w - 0.3, 0.7, boxstyle="round,pad=0.02", edgecolor='#334155', facecolor='#0F172A', linewidth=1.0)
            ax.add_patch(sub_card)

            ax.text(cx + col_w/2.0, iy - 0.28, title, color='white', fontsize=9, weight='bold', ha='center', va='center')
            ax.text(cx + col_w/2.0, iy - 0.50, subtitle, color='#94A3B8', fontsize=7.5, ha='center', va='center')

            iy -= 0.88

        # Flow Arrow to Next Stage
        if idx < len(stages) - 1:
            ax.annotate('', xy=(cx + col_w + gap - 0.05, 3.4), xytext=(cx + col_w + 0.05, 3.4),
                        arrowprops=dict(facecolor=stage["border"], edgecolor=stage["border"], width=3, headwidth=9, headlength=9))

    # Bottom Footer Bar
    ax.plot([0.5, 13.5], [0.4, 0.4], color='#334155', linewidth=1)
    ax.text(0.5, 0.2, "SPRING AI — AI-Powered Springshed Rejuvenation System", color='#94A3B8', fontsize=8.5, va='center')
    ax.text(13.5, 0.2, "Smart India Hackathon 2026", color='#38BDF8', fontsize=8.5, weight='bold', ha='right', va='center')

    ax.set_xlim(0, 14)
    ax.set_ylim(0, 7.5)
    ax.axis('off')
    plt.tight_layout()

    out_path = "assets/spring_ai_high_level_architecture.png"
    plt.savefig(out_path, bbox_inches='tight', facecolor='#0F172A')
    print(f"High-level Architecture Diagram saved to {out_path}")

if __name__ == "__main__":
    generate_creative_highlevel_architecture()
