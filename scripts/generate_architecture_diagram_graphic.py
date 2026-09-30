import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_spring_ai_architecture_diagram():
    os.makedirs("assets", exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(14, 9), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#F8FAFC')

    # Title Banner
    title_box = patches.FancyBboxPatch((0.5, 8.2), 13.0, 0.65, boxstyle="round,pad=0.03", edgecolor='#0284C7', facecolor='#103969', linewidth=1.5)
    ax.add_patch(title_box)
    ax.text(7.0, 8.525, "SPRING AI — END-TO-END GEOAI SYSTEM ARCHITECTURE", color='white', fontsize=16, fontfamily='serif', weight='bold', ha='center', va='center')

    layers = [
        {
            "num": "LAYER 1", "title": "Data Sources & Ingestion", "color": "#2563EB", "bg": "#EFF6FF",
            "boxes": [
                ("Copernicus DEM (30m)", "Elevation & Slope"),
                ("IMD Hydromet API", "Gridded Rainfall"),
                ("GSI Bhukosh", "Lithology & Soil"),
                ("CGWB Aquifer Data", "Groundwater Depth")
            ]
        },
        {
            "num": "LAYER 2", "title": "Spatial Preprocessing Engine", "color": "#0284C7", "bg": "#F0F9FF",
            "boxes": [
                ("GDAL / Rasterio", "Coordinate Projection WGS84"),
                ("D8 Flow Accumulation", "3D Catchment Delineation"),
                ("Slope & Drainage Matrix", "Geomorphological Extraction"),
                ("Data Resampling", "Spatial Normalization")
            ]
        },
        {
            "num": "LAYER 3", "title": "Core Hydro-AI Model Engine", "color": "#D97706", "bg": "#FFFBEB",
            "boxes": [
                ("PRSI Weighted Formula", "0.35S + 0.25L + 0.20G + 0.15R + 0.05D"),
                ("PyTorch ML Classifier", "Suitability Pattern Scoring"),
                ("Structure Selector", "Trenches, Check Dams, Pits"),
                ("Runoff Yield Estimator", "Storage Potential Model")
            ]
        },
        {
            "num": "LAYER 4", "title": "Safety & Hazard Masking Engine", "color": "#DC2626", "bg": "#FEF2F2",
            "boxes": [
                ("Slope >30° Filter", "Landslide Risk Exclusion"),
                ("Eco-Forest Mask", "Regulatory Boundary Check"),
                ("Geological Fault Mask", "Structural Stability Check"),
                ("Zero-Hazard Validation", "Safe Site Designation")
            ]
        },
        {
            "num": "LAYER 5", "title": "Backend, Database & Sync Layer", "color": "#7C3AED", "bg": "#F5F3FF",
            "boxes": [
                ("FastAPI Microservices", "Async REST Endpoints"),
                ("PostGIS Spatial DB", "GeoJSON Spatial Indexing"),
                ("Offline Sync Engine", "SQLite Field Local Sync"),
                ("SpringBot Core", "Local Language LLM / Voice")
            ]
        },
        {
            "num": "LAYER 6", "title": "User Presentation & Field Output Layer", "color": "#059669", "bg": "#ECFDF5",
            "boxes": [
                ("Web GIS Dashboard", "Interactive Mapbox GL Maps"),
                ("Jal Sahi Mobile App", "Offline Field Verification"),
                ("MGNREGA DPR Generator", "1-Click PDF Cost Dossiers"),
                ("Ministry Alerts", "Spring Rejuvenation Insights")
            ]
        }
    ]

    y_positions = [7.1, 5.8, 4.5, 3.2, 1.9, 0.6]

    for idx, layer in enumerate(layers):
        ly = y_positions[idx]
        
        # Layer Header Box
        hdr_rect = patches.FancyBboxPatch((0.5, ly), 3.2, 0.95, boxstyle="round,pad=0.03", edgecolor=layer["color"], facecolor=layer["color"], linewidth=1.2)
        ax.add_patch(hdr_rect)
        ax.text(2.1, ly + 0.65, layer["num"], color='#BAE6FD' if layer["color"] != "#D97706" else "#FEF3C7", fontsize=9, weight='bold', ha='center', va='center')
        ax.text(2.1, ly + 0.3, layer["title"], color='white', fontsize=11, fontfamily='serif', weight='bold', ha='center', va='center')

        # Sub-boxes Container
        cont_rect = patches.FancyBboxPatch((3.8, ly), 9.7, 0.95, boxstyle="round,pad=0.03", edgecolor=layer["color"], facecolor=layer["bg"], linewidth=1.2)
        ax.add_patch(cont_rect)

        # 4 Sub-boxes inside each layer
        box_w = 2.25
        gap = 0.15
        for b_idx, (b_title, b_sub) in enumerate(layer["boxes"]):
            bx = 3.95 + b_idx * (box_w + gap)
            b_rect = patches.FancyBboxPatch((bx, ly + 0.1), box_w, 0.75, boxstyle="round,pad=0.03", edgecolor=layer["color"], facecolor='white', linewidth=1.0)
            ax.add_patch(b_rect)
            
            ax.text(bx + box_w/2.0, ly + 0.52, b_title, color='#0F172A', fontsize=8.5, weight='bold', ha='center', va='center')
            ax.text(bx + box_w/2.0, ly + 0.25, b_sub, color='#475569', fontsize=7.5, ha='center', va='center')

        # Connector Down Arrow (between layers)
        if idx < len(layers) - 1:
            ax.annotate('', xy=(8.65, y_positions[idx+1] + 0.95), xytext=(8.65, ly),
                        arrowprops=dict(facecolor=layer["color"], edgecolor=layer["color"], width=2.5, headwidth=8, headlength=8))

    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')
    plt.tight_layout()

    out_img = "assets/spring_ai_architecture_diagram.png"
    plt.savefig(out_img, bbox_inches='tight', facecolor='#F8FAFC')
    print(f"Spring AI Architecture Diagram saved to {out_img}")

if __name__ == "__main__":
    generate_spring_ai_architecture_diagram()
