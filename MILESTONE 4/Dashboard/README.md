# Anomaly Detection Dashboard – Milestone 4

## 📌 Project Overview
This project implements an anomaly detection pipeline with an interactive dashboard for monitoring, visualization, and reporting.  
Milestone 4 focuses on:
- Building interactive dashboards in Jupyter Notebook using Plotly and ipywidgets
- Exporting plots and filtered data
- Saving outputs (CSV, PNG, HTML, logs)
- Finalizing deployment with a shareable HTML report

---
 📂 Project Structure
```
├── data/
│   ├── 01_raw_data.csv
│   ├── 02_detection_results.csv
│   ├── 03_anomalies.csv
│   └── 08_filtered_anomalies.csv
├── plots/
│   ├── 04_anomaly_plot.png
│   ├── 06_dashboard_plot.png
│   └── 07_dashboard_plot.html
├── logs/
│   └── 05_alert_log.txt
├── reports/
│   └── Dashboard & Deployment.html
├── Dashboard/
│   └── config.yaml
├── README.md
└── requirements.txt
```

 ⚙️ Configuration
Settings are managed via `config.yaml`:
- **Thresholds** for anomaly detection
- **Alert channels** (email, Slack)
- **File paths** for data, plots, logs, and reports

Example:
```yaml
anomaly_detection:
  method: isolation_forest
  contamination: 0.05
  threshold_value: 50
```

---

## 🚀 Usage
 Explore the interactive dashboard and export results:
   - PNG plots
   - HTML plots
   - CSV filtered anomalies
   - HTML report (`Dashboard & Deployment.html`)

---

## 📊 Outputs
- **Data**: raw, detection results, anomalies, filtered anomalies  
- **Plots**: anomaly plot, dashboard plot (PNG + HTML)  
- **Logs**: alert log  
- **Reports**: notebook exported to HTML  
- **Docs**: README.md, requirements.txt, config.yaml  

---

## ✅ Milestone 4 Achievements
- Interactive anomaly detection dashboard
- Exported plots and reports
- Organized outputs for reproducibility
- GitHub‑ready documentation and structure

