"""
Configuration, Brand System & UI Theme Constants for SPRING-AI Platform
Modern GeoAI & Environmental Intelligence Aesthetic
"""

APP_TITLE = "SPRING-AI"
APP_TAGLINE = "Restoring Springs • Predicting Recharge • Strengthening Communities"
APP_SUBTITLE = "AI-powered geospatial decision support for spring revival and recharge planning in tribal and mountainous regions."
MINISTRY_TAG = "GeoAI Decision Support Platform"

DEMO_DATA_DISCLAIMER = (
    "DEMO & REAL DATASET NOTICE: All spatial layers combine satellite DEM (Bhuvan/Copernicus), "
    "precipitation, geology, and hydrogeological baselines across 100+ tribal districts in 17 states."
)

SCIENTIFIC_DISCLAIMER = (
    "IMPORTANT SCIENTIFIC DISCLAIMER: SPRING-AI provides decision-support estimates. "
    "AI predictions and recommendations must be clearly understood as model outputs and are not guaranteed ground truth. "
    "All outputs require appropriate field validation and expert hydrogeological assessment prior to engineering construction."
)

# Brand Color System
COLOR_PRIMARY_FOREST = "#12372A"
COLOR_SECONDARY_FOREST = "#1F5C45"
COLOR_WATER_BLUE = "#0284c7"
COLOR_SKY_BLUE = "#38bdf8"
COLOR_EARTH = "#8B6F47"
COLOR_SAND = "#D8C3A5"
COLOR_BG_LIGHT = "#f8fafc"
COLOR_BG_DARK = "#0f172a"

# Semantic Colors (WCAG Compliant)
COLOR_SUCCESS = "#10B981"
COLOR_WARNING = "#F59E0B"
COLOR_DANGER = "#EF4444"
COLOR_INFO = "#0284c7"

# Spring Health Diagnostics
COLOR_HEALTHY = "#10B981"
COLOR_STABLE = "#0284c7"
COLOR_DECLINING = "#F59E0B"
COLOR_CRITICAL = "#EF4444"
COLOR_INSUFFICIENT = "#6B7280"

# Feature definitions for ML Pipeline
FEATURE_COLS = [
    "elevation", "slope", "aspect", "rainfall", "drainage_density",
    "distance_to_drainage", "distance_to_spring", "fracture_density",
    "distance_to_fault", "land_use_code", "soil_permeability", "lithology_code"
]

FEATURE_LABELS = {
    "elevation": "Elevation (m MSL)",
    "slope": "Terrain Slope (°)",
    "aspect": "Slope Aspect (°)",
    "rainfall": "Annual Precipitation (mm)",
    "drainage_density": "Drainage Density (km/km²)",
    "distance_to_drainage": "Distance to Stream (m)",
    "distance_to_spring": "Distance to Spring (m)",
    "fracture_density": "Fracture Density (km/km²)",
    "distance_to_fault": "Distance to Fault Line (m)",
    "land_use_code": "Land Use / Cover Class",
    "soil_permeability": "Soil Permeability Index (1-5)",
    "lithology_code": "Geological Lithology Class"
}

JALSETU_LOGO_SVG = """
<svg width="36" height="36" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="50" cy="50" r="46" stroke="#0284c7" stroke-width="4" stroke-dasharray="8 4" opacity="0.6"/>
    <path d="M20 75L50 25L80 75H20Z" fill="#0f172a"/>
    <path d="M40 75L62 38L85 75H40Z" fill="#059669" opacity="0.85"/>
    <path d="M50 42C50 42 38 58 38 65C38 71.6 43.4 77 50 77C56.6 77 62 71.6 62 65C62 58 50 42 50 42Z" fill="#0284c7"/>
</svg>
"""
