# Odisha Primary Health Coverage Analysis & Mobile Health Unit Policy Recommendations

**Prepared for:** Joint Secretary (eHealth), Ministry of Health & Family Welfare, Government of India\
**Lead Author:** Utkarsh Agarwal, Intelehealth

---

## Why This Project?

Despite increased investment in rural health infrastructure, many villages in Odisha still fall outside the effective reach of government Primary Health Centres (PHCs) and Health Sub-Centres (HSCs). This project provides a granular, reproducible analysis to answer:

- Which villages are uncovered if we look only at PHCs?
- Which villages are uncovered if we look only at HSCs?
- Which villages remain uncovered even if we combine both PHCs and HSCs within a 3 km buffer?
- Where should Mobile Health Units (MHUs) be deployed for the greatest impact?

---

## Analytical Logic: Three Coverage Definitions

### 1. **PHC-Only Coverage**

- A village is considered **covered** if there is a PHC within 5 km of its centroid.
- Output: `phc_coverage_with_geometry.geojson`

### 2. **HSC-Only Coverage**

- A village is considered **covered** if there is an HSC within 3 km of its centroid.
- Output: `hsc_coverage_with_geometry.geojson`

### 3. **Combined Coverage (Aggregate, 3 km Rule)**

- A village is considered **covered** if *either* a PHC or HSC is within 3 km of its centroid (most inclusive, “universal access” metric).
- Output: `combined_phc_hsc_coverage_3km.geojson`

Villages are flagged “uncovered” if they don’t meet any of the above criteria, depending on the metric used. All three outputs are mapped and analyzed.

---

## Step-by-Step Analysis

### 1. Data Preparation

- Merge and clean official government and ESRI datasets (villages/facilities) using unique codes (LGD for villages, NIN for facilities).
- Geolocate, deduplicate, and check all records for accuracy.

### 2. Coverage Calculations (All Three Modes)

- For every village:
  - Calculate distance to all PHCs and HSCs.
  - Apply each definition:
    - PHC: covered if within 5 km of a PHC.
    - HSC: covered if within 3 km of an HSC.
    - Combined: covered if either facility is within 3 km (aggregate).
- Create binary “covered/uncovered” flags for each mode, for every village.

### 3. Output & Visualization

- Separate GeoJSONs for each definition (PHC-only, HSC-only, Combined 3 km)
- District/state tables showing % of villages covered/uncovered for all three rules
- Bar, pie, and bubble charts visualizing each scenario
- Maps highlighting gaps, with cluster analysis for MHU targeting

### 4. Policy Translation

- **PHC-only:** Shows service gaps if PHCs are sole access point (often too conservative)
- **HSC-only:** More local, shows gaps for “last-mile” access
- **Combined 3 km (Aggregate):** Realistic, ambitious “universal” metric—ideal for setting government benchmarks and for prioritizing MHUs
- **All outputs are included in the slide deck and ready for government/NGO use**

---

## Folder Structure

```
Primary Health Coverage Analysis_Odisha/
├── Data/
│   ├── Processed/
│   └── Raw/
├── Notebooks/
│   └── 01_JS_Coverage_Master_Report.ipynb
├── Outputs/
│   ├── combined_phc_hsc_coverage_3km.geojson    # Combined aggregate output
│   ├── hsc_coverage_with_geometry.geojson       # HSC-only output
│   └── phc_coverage_with_geometry.geojson       # PHC-only output
├── Visualizations/
│   ├── district_bubble_chart_with_color@2x.png
│   ├── district_stacked_bar@2x.jpeg
│   ├── district_uncovered_bar_chart@2x.jpeg
│   └── statewide_pie_chart@2x.jpeg
├── Odisha Facility Coverage.pptx.pdf
```

---

## Outputs Provided

- `phc_coverage_with_geometry.geojson`: PHC 5 km rule—who is covered just by PHCs?
- `hsc_coverage_with_geometry.geojson`: HSC 3 km rule—who is covered just by HSCs?
- `combined_phc_hsc_coverage_3km.geojson`: Aggregate “combined” rule—who is covered by *either* within 3 km?
- District/state summary charts for each mode
- Slide deck for high-level policy and operational meetings

---

## Why Provide All Three?

- **PHC-only** is the government’s main formal network but may miss many last-mile villages.
- **HSC-only** gives a sharper picture of “doorstep” access.
- **Combined 3 km** is the universal, human-rights–oriented benchmark for the SDG era—useful for rapid policy action and MHU deployment.

---

## For Policymakers, Researchers, NGOs

- All code and logic are fully reproducible and transparent.
- Every coverage scenario is mapped, visualized, and available for integration with time/distance/cost models and future telemedicine expansion.
- Directly supports focused MHU rollout and last-mile universal access strategies.

---

## License & Credits

MIT or CC-BY 4.0 (as applicable)

- Analysis: Utkarsh Agarwal, Intelehealth
- Data: ESRI India, MoHFW (HMIS), GADM

**Contact:** Utkarsh Agarwal, Intelehealth [[your.email@provider.com](mailto\:your.email@provider.com)]

