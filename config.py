# config.py
"""
Configuration file for the Odisha Primary Health Coverage Analysis
Edit these variables as needed for local paths or to migrate between systems.
"""

import os

# === Core Data Directories ===
BASE_DIR = r"C:\Users\utkar\OneDrive\Desktop\ClimateXTelemedicine Odisha\Odisha_VScode\.venv\Primary Health Coverage Analysis_Odisha"
RAW_DATA_DIR = os.path.join(BASE_DIR, "Data", "Raw")
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, "Data", "Processed")
NOTEBOOKS_DIR = os.path.join(BASE_DIR, "Notebooks")
OUTPUTS_DIR = os.path.join(BASE_DIR, "Outputs")
VISUALIZATIONS_DIR = os.path.join(BASE_DIR, "Visualizations")

# === Notebook(s) ===
MASTER_NOTEBOOK = os.path.join(NOTEBOOKS_DIR, "01_JS_Coverage_Master_Report.ipynb")

# === Output Files ===
COMBINED_GEOJSON = os.path.join(OUTPUTS_DIR, "combined_phc_hsc_coverage_3km.geojson")
HSC_GEOJSON = os.path.join(OUTPUTS_DIR, "hsc_coverage_with_geometry.geojson")
PHC_GEOJSON = os.path.join(OUTPUTS_DIR, "phc_coverage_with_geometry.geojson")

# === Visualization Files ===
BUBBLE_CHART = os.path.join(VISUALIZATIONS_DIR, "district_bubble_chart_with_color@2x.png")
STACKED_BAR_CHART = os.path.join(VISUALIZATIONS_DIR, "district_stacked_bar@2x.jpeg")
UNCOVERED_BAR_CHART = os.path.join(VISUALIZATIONS_DIR, "district_uncovered_bar_chart@2x.jpeg")
PIE_CHART = os.path.join(VISUALIZATIONS_DIR, "statewide_pie_chart@2x.jpeg")

# === Main Policy Output ===
POLICY_PDF = os.path.join(BASE_DIR, "Odisha Facility Coverage.pptx.pdf")

# === Coverage Thresholds ===
PHC_COVERAGE_KM = 5
HSC_COVERAGE_KM = 3
COMBINED_COVERAGE_KM = 3

# === Unique ID Fields ===
FACILITY_ID_FIELD = "NIN"
VILLAGE_ID_FIELD = "LGD"

# === Utility Function Example ===
def ensure_dirs():
    """Ensure all output/visualization directories exist."""
    for d in [RAW_DATA_DIR, PROCESSED_DATA_DIR, NOTEBOOKS_DIR, OUTPUTS_DIR, VISUALIZATIONS_DIR]:
        os.makedirs(d, exist_ok=True)

# Usage: import config; config.ensure_dirs()