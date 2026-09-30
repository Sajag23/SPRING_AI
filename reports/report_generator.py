"""
PDF & Scientific Report Generator for JALSETU AI Platform
Produces official publication-ready decision support PDF dossiers.
"""

import os
from fpdf import FPDF
from utils.config import SCIENTIFIC_DISCLAIMER, DEMO_DATA_DISCLAIMER

class PDFReport(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(18, 55, 42) # Primary Forest #12372A
        self.cell(0, 10, 'SPRING-AI - Spring Revival & Recharge Planning Dossier', border=0, new_x='LMARGIN', new_y='NEXT', align='C')
        self.set_font('Helvetica', 'I', 9)
        self.set_text_color(22, 119, 168) # Water Blue #1677A8
        self.cell(0, 5, 'AI-Powered Geospatial Decision Support for Tribal & Mountainous Regions', border=0, new_x='LMARGIN', new_y='NEXT', align='C')
        self.set_draw_color(18, 55, 42)
        self.line(10, 26, 200, 26)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()} | SPRING-AI Decision Support Estimate - Requires Field Validation', border=0, new_x='RIGHT', new_y='TOP', align='C')

def generate_spring_pdf_report(spring_data, site_data=None, output_path="reports/spring_report.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # 1. Executive Summary & Study Area
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(18, 55, 42) # Forest Green
    sp_name = str(spring_data.get('spring_name', 'N/A')).replace('—', '-').replace('–', '-')
    sp_id = str(spring_data.get('spring_id', 'N/A')).replace('—', '-').replace('–', '-')
    pdf.cell(0, 8, f"1. Target Spring Profile: {sp_name} ({sp_id})", border=0, new_x='LMARGIN', new_y='NEXT')
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(95, 6, f"Village: {spring_data.get('village', 'N/A')}", border=0, new_x='RIGHT', new_y='TOP')
    pdf.cell(95, 6, f"District: {spring_data.get('district', 'N/A')}", border=0, new_x='LMARGIN', new_y='NEXT')
    pdf.cell(95, 6, f"Latitude: {spring_data.get('latitude', 'N/A')} N", border=0, new_x='RIGHT', new_y='TOP')
    pdf.cell(95, 6, f"Longitude: {spring_data.get('longitude', 'N/A')} E", border=0, new_x='LMARGIN', new_y='NEXT')
    pdf.cell(95, 6, f"Elevation: {spring_data.get('elevation', 'N/A')} m MSL", border=0, new_x='RIGHT', new_y='TOP')
    pdf.cell(95, 6, f"Spring Type: {spring_data.get('spring_type', 'N/A')}", border=0, new_x='LMARGIN', new_y='NEXT')
    pdf.cell(95, 6, f"Current Discharge: {spring_data.get('current_discharge_lpm', 'N/A')} LPM", border=0, new_x='RIGHT', new_y='TOP')
    pdf.cell(95, 6, f"Seasonal Status: {spring_data.get('seasonal_status', 'N/A')}", border=0, new_x='LMARGIN', new_y='NEXT')
    pdf.ln(4)

    # 2. AI Model Recharge Suitability & Factors
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(18, 55, 42)
    pdf.cell(0, 8, "2. GeoAI Model Recharge Suitability Assessment", border=0, new_x='LMARGIN', new_y='NEXT')
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(30, 41, 59)
    prob_pct = float(spring_data.get('recharge_probability', 0.8)) * 100
    conf_pct = float(spring_data.get('confidence_score', 0.75)) * 100
    
    pdf.cell(95, 6, f"Probable Recharge Suitability: {prob_pct:.1f}%", border=0, new_x='RIGHT', new_y='TOP')
    pdf.cell(95, 6, f"Model Confidence Score: {conf_pct:.1f}%", border=0, new_x='LMARGIN', new_y='NEXT')
    pdf.cell(95, 6, f"Landslide Hazard Status: {spring_data.get('landslide_risk', 'Low (Safe Slope)')}", border=0, new_x='LMARGIN', new_y='NEXT')
    pdf.ln(4)

    # 3. Recommended Water Conservation Interventions
    if site_data:
        pdf.set_font("Helvetica", "B", 12)
        pdf.set_text_color(18, 55, 42)
        pdf.cell(0, 8, "3. Prioritised Artificial Recharge Interventions", border=0, new_x='LMARGIN', new_y='NEXT')
        
        pdf.set_font("Helvetica", "", 10)
        s_id = str(site_data.get('site_id', 'INT-001')).replace('—', '-').replace('–', '-')
        rec_str = str(site_data.get('recommended_structure', 'Staggered Contour Trench')).replace('—', '-').replace('–', '-')
        pdf.cell(95, 6, f"Prioritised Site ID: {s_id}", border=0, new_x='RIGHT', new_y='TOP')
        pdf.cell(95, 6, f"Priority Level: {site_data.get('priority_level', 'HIGH')}", border=0, new_x='LMARGIN', new_y='NEXT')
        pdf.multi_cell(0, 6, f"Recommended Engineering Measure: {rec_str}")
        pdf.ln(4)

    # 4. Mandatory Disclaimers & Field Validation Notice
    pdf.ln(4)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(220, 38, 38)
    pdf.cell(0, 6, "SCIENTIFIC LIMITATIONS & FIELD VALIDATION REQUIREMENT:", border=0, new_x='LMARGIN', new_y='NEXT')
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(80, 80, 80)
    clean_disc = SCIENTIFIC_DISCLAIMER.replace('—', '-').replace('–', '-')
    clean_demo = DEMO_DATA_DISCLAIMER.replace('—', '-').replace('–', '-')
    pdf.multi_cell(0, 4, clean_disc)
    pdf.ln(2)
    pdf.multi_cell(0, 4, clean_demo)

    pdf.output(output_path)
    return output_path

def generate_district_executive_report(dist_pack, output_path="reports/district_executive_report.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    cfg = dist_pack.get("config", {})
    tribal = dist_pack.get("tribal_demographics", {})
    water = dist_pack.get("water_metrics", {})
    cost = dist_pack.get("financial_costing", {})

    # 1. District Profile & Hydrogeology
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(18, 55, 42)
    pdf.cell(0, 8, f"1. District Springshed Profile: {cfg.get('district', 'N/A')}, {cfg.get('state', 'N/A')}", border=0, new_x='LMARGIN', new_y='NEXT')

    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(30, 41, 59)
    pdf.cell(95, 6, f"State: {cfg.get('state', 'N/A')}", border=0, new_x='RIGHT', new_y='TOP')
    pdf.cell(95, 6, f"Governing Agency: {cfg.get('govt_agency', 'CGWB & IMD')}", border=0, new_x='LMARGIN', new_y='NEXT')
    pdf.cell(95, 6, f"Mean Precipitation: {cfg.get('rainfall_mean', 'N/A')} mm", border=0, new_x='RIGHT', new_y='TOP')
    pdf.cell(95, 6, f"Elevation Range: {cfg.get('elev_range', [0,0])[0]}-{cfg.get('elev_range', [0,0])[1]}m MSL", border=0, new_x='LMARGIN', new_y='NEXT')
    litho_str = ", ".join(cfg.get("lithology_types", ["Hard Rock"]))[:60]
    pdf.set_x(10)
    pdf.multi_cell(0, 6, f"Primary Lithology: {litho_str}")
    pdf.ln(4)

    # 2. Tribal Demographics & Habitations
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(18, 55, 42)
    pdf.cell(0, 8, "2. Census ST Demographics & Tribal Community Profile", border=0, new_x='LMARGIN', new_y='NEXT')

    pdf.set_font("Helvetica", "", 10)
    tribes_str = ", ".join(tribal.get("tribes", ["Tribal Communities"]))
    pdf.cell(95, 6, f"Scheduled Tribe Population: {tribal.get('st_pop_pct', 50)}%", border=0, new_x='RIGHT', new_y='TOP')
    pdf.cell(95, 6, f"Tribal Households Served: {tribal.get('households_impacted', 0):,}", border=0, new_x='LMARGIN', new_y='NEXT')
    pdf.set_x(10)
    pdf.multi_cell(0, 6, f"Tribes Living in Region: {tribes_str}")
    pdf.set_x(10)
    pdf.multi_cell(0, 6, f"Primary Livelihood Base: {tribal.get('livelihood', 'Agriculture & NTFP')}")
    pdf.ln(4)

    # 3. Hydrological Catchment & Water Storage Impact
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(18, 55, 42)
    pdf.cell(0, 8, "3. Estimated Water Storage Potential & Catchment Impact", border=0, new_x='LMARGIN', new_y='NEXT')

    pdf.set_font("Helvetica", "", 10)
    pdf.cell(95, 6, f"Treated Catchment Area: {water.get('catchment_sqkm', 0)} sq km ({water.get('catchment_hectares', 0):,} Hectares)", border=0, new_x='RIGHT', new_y='TOP')
    pdf.cell(95, 6, f"Annual Storage Potential: {water.get('storage_ml', 0)} Million Liters ({water.get('storage_cum', 0):,} m3)", border=0, new_x='LMARGIN', new_y='NEXT')
    pdf.cell(95, 6, f"Estimated Water Table Rise: +{water.get('water_table_rise_m', 0)} meters", border=0, new_x='RIGHT', new_y='TOP')
    pdf.cell(95, 6, f"Summer Baseflow Extension: +{water.get('summer_flow_extension_days', 0)} Days", border=0, new_x='LMARGIN', new_y='NEXT')
    pdf.cell(95, 6, f"Daily Water Augmentation: {water.get('daily_water_added_lpd', 'N/A')}", border=0, new_x='LMARGIN', new_y='NEXT')
    pdf.ln(4)

    # 4. Financial Budget & MGNREGA Labor Generation
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(18, 55, 42)
    pdf.cell(0, 8, "4. Financial Budget Estimates & MGNREGA Labor Generation", border=0, new_x='LMARGIN', new_y='NEXT')

    pdf.set_font("Helvetica", "", 10)
    pdf.cell(95, 6, f"Total Estimated Budget: INR {cost.get('total_cost_lakhs', 0)} Lakhs (INR {cost.get('total_cost_crores', 0)} Crores)", border=0, new_x='RIGHT', new_y='TOP')
    pdf.cell(95, 6, f"MGNREGA Labor Generation: {cost.get('mgnrega_persondays', 0):,} Persondays", border=0, new_x='LMARGIN', new_y='NEXT')
    pdf.cell(95, 6, f"Estimated Investment per Household: INR {cost.get('cost_per_household_inr', 0):,}", border=0, new_x='LMARGIN', new_y='NEXT')
    pdf.ln(4)

    # 5. Scientific Limitations & Field Validation
    pdf.ln(4)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(220, 38, 38)
    pdf.cell(0, 6, "SCIENTIFIC LIMITATIONS & FIELD VALIDATION MANDATE:", border=0, new_x='LMARGIN', new_y='NEXT')
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(80, 80, 80)
    pdf.set_x(10)
    pdf.multi_cell(0, 4, SCIENTIFIC_DISCLAIMER.replace('—', '-').replace('–', '-'))
    pdf.ln(2)
    pdf.set_x(10)
    pdf.multi_cell(0, 4, DEMO_DATA_DISCLAIMER.replace('—', '-').replace('–', '-'))

    pdf.output(output_path)
    return output_path

