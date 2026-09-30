"""
Rule Engine & Scoring Algorithms for SPRING-AI
Calculates Intervention Priorities, Structure Recommendations, Spring Health Scores,
Before/After Impact Projections, Cost Estimations, and Data Quality Metrics.
"""

def evaluate_intervention_site(site_dict):
    """
    Calculates intervention priority score, indicative structure recommendation, and risk level.
    """
    slope = site_dict.get("slope", 10.0)
    suitability = site_dict.get("suitability_score", 0.75)
    if suitability > 1.0: # If passed as percentage 0-100
        suitability /= 100.0

    soil_perm = site_dict.get("soil_permeability", 3)
    existing = site_dict.get("existing_structure", "None")

    # 1. Indicative Structure Recommendation
    if slope > 35:
        recommendation = "No Structural Intervention — High Landslide Risk Zone (Requires Vegetative Bio-Stabilisation Only)"
        risk = "Critical"
        priority = "LOW"
    elif 15 <= slope <= 35:
        recommendation = "Staggered Contour Trenches (SCT) & Bio-Fencing"
        risk = "Moderate" if slope > 25 else "Low"
        priority = "HIGH" if suitability > 0.75 else "MEDIUM"
    elif 5 <= slope < 15:
        recommendation = "Loose Boulder Check Dam (LBCD) / Gabion Check Dam"
        risk = "Low"
        priority = "HIGH" if suitability > 0.70 else "MEDIUM"
    else: # < 5 degrees
        recommendation = "Percolation Pond / Artificial Recharge Pit with Shaft"
        risk = "Low"
        priority = "HIGH" if suitability > 0.65 else "MEDIUM"

    if existing != "None" and priority == "HIGH":
        recommendation += f" (Note: Repair/Augment Existing '{existing}')"

    # Priority score numeric
    priority_score = round(min(suitability * 100.0, 99.0), 1)

    return {
        "indicative_recommendation": recommendation,
        "priority_level": priority,
        "priority_score_pct": priority_score,
        "risk_status": risk,
        "disclaimer": "Indicative recommendation — requires field and engineering verification."
    }

def calculate_spring_health_score(spring_row):
    """
    Computes a 0-100 Health Diagnostic Score and Water Quality Index for a given spring.
    """
    discharge = spring_row.get("current_discharge_lpm", 15.0)
    status = spring_row.get("seasonal_status", "Stable")
    recharge_prob = spring_row.get("recharge_probability", 0.70)
    
    # Flow score component (40%)
    flow_score = min(100.0, (discharge / 30.0) * 100.0) * 0.40
    
    # Stability score component (30%)
    status_weights = {"Healthy": 100, "Stable": 80, "Declining": 45, "Critical": 20, "Perennial": 95}
    stability_score = status_weights.get(status, 60) * 0.30
    
    # Recharge potential component (30%)
    recharge_score = (recharge_prob * 100.0) * 0.30
    
    health_score = round(flow_score + stability_score + recharge_score, 1)
    
    # Water Quality Index (Simulated baseline based on spring type)
    ph = round(6.8 + (health_score / 100.0) * 0.8, 2)
    ec = int(180 + (100 - health_score) * 2.5)
    turbidity = round(1.2 + (100 - health_score) * 0.05, 1)
    
    return {
        "health_score": health_score,
        "health_rating": "🟢 Healthy" if health_score >= 75 else ("🟡 Vulnerable" if health_score >= 50 else "🔴 Critical"),
        "ph_level": ph,
        "ec_us_cm": ec,
        "turbidity_ntu": turbidity,
        "water_quality_status": "🟢 Safe Drinking Water" if ph >= 6.5 and ph <= 8.5 and ec < 500 else "🟡 Treatment Advisory"
    }

def calculate_before_after_impact(site_dict):
    """
    Calculates estimated hydrogeological impact and MGNREGA cost/labor breakdown post-intervention.
    """
    rec_struct = site_dict.get("recommended_structure", "Staggered Contour Trenches")
    slope = site_dict.get("slope", 12.0)
    
    if "Check Dam" in rec_struct:
        cost_inr = 185000
        persondays = 420
        flow_extension_days = 75
        water_table_rise_m = 3.2
        storage_cu_m = 1200
        households_served = 140
    elif "Trench" in rec_struct:
        cost_inr = 95000
        persondays = 260
        flow_extension_days = 60
        water_table_rise_m = 2.1
        storage_cu_m = 850
        households_served = 90
    elif "Percolation" in rec_struct or "Pond" in rec_struct:
        cost_inr = 240000
        persondays = 580
        flow_extension_days = 90
        water_table_rise_m = 4.5
        storage_cu_m = 2500
        households_served = 210
    else:
        cost_inr = 45000
        persondays = 110
        flow_extension_days = 30
        water_table_rise_m = 0.8
        storage_cu_m = 300
        households_served = 35

    return {
        "estimated_cost_inr": f"₹{cost_inr:,}",
        "mgnrega_persondays": persondays,
        "flow_extension_days": f"+{flow_extension_days} Days into Summer",
        "water_table_rise_m": f"+{water_table_rise_m} meters",
        "storage_capacity_cum": f"{storage_cu_m:,} m³",
        "tribal_households_impacted": households_served,
        "daily_water_added_lpd": f"{households_served * 120:,} Liters/Day",
        "distance_saved_km": "1.8 km/day for tribal women"
    }

def calculate_data_quality_score(datasets_available):
    """
    Computes data completeness and overall data confidence score based on uploaded layers.
    """
    weights = {
        "terrain_dem": 0.25,
        "rainfall": 0.20,
        "geology_lithology": 0.20,
        "faults_fractures": 0.15,
        "spring_discharge": 0.10,
        "land_use": 0.10
    }

    score = 0.0
    details = {}
    for key, weight in weights.items():
        is_present = datasets_available.get(key, True)
        pct = 100.0 if is_present else 0.0
        score += weight * pct
        details[key] = round(pct, 0)

    overall_level = "HIGH" if score >= 80 else ("MEDIUM" if score >= 50 else "LOW")

    return {
        "overall_score_pct": round(score, 1),
        "confidence_level": overall_level,
        "layer_breakdown": details
    }

GLOSSARY_TERMS = {
    "Dhara / Jharna": "Traditional natural spring in tribal hilly regions where groundwater discharges naturally onto the surface.",
    "Springshed": "The specific surface and subsurface land area that contributes recharge water to a spring.",
    "Lithology": "The physical characteristics of rock formations (e.g. Quartzite, Granite, Gneiss) determining water infiltration.",
    "Lineament": "Linear geological features such as fault lines and fracture zones that act as natural underground water channels.",
    "Baseflow": "The portion of spring flow coming from deep groundwater storage rather than direct surface runoff.",
    "LPM": "Liters Per Minute — units used to measure natural spring discharge flow rate.",
    "MSL": "Mean Sea Level — reference altitude used for mountain elevation measurements in meters."
}
