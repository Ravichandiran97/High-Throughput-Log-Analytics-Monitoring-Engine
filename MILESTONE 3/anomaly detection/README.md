🧠 Anomaly Detection Pipeline (Milestone 3)

This project implements an anomaly detection workflow using **Isolation Forest** in Python.  
It simulates data, detects anomalies, visualizes results, and triggers alerts via email or Slack.  
All outputs are saved into separate files for reproducibility and auditing.

---
📂 Project Structure
```
anomaly_detection_pipeline/
│
├── data/
│   ├── 01_raw_data.csv          # simulated dataset
│   ├── 02_detection_results.csv # dataset with anomaly labels
│   ├── 03_anomalies.csv         # anomalies only
│   ├── 05_alert_log.txt         # alert messages
│
├── plots/
│   └── 04_anomaly_plot.png      # visualization
│
├── anomaly_pipeline.py          # main script
├── requirements.txt             # dependencies
└── README.md                    # documentation
```


## 📁 Output Files

- **01_raw_data.csv** → simulated dataset  
- **02_detection_results.csv** → dataset with anomaly labels (`1 = normal`, `-1 = anomaly`)  
- **03_anomalies.csv** → anomalies only  
- **04_anomaly_plot.png** → visualization of anomalies (red dots)  
- **05_alert_log.txt** → alert messages for each anomaly  

---

## 📬 Alerts

The pipeline includes optional alert functions:
- **Email alerts** via SMTP
- **Slack alerts** via webhook

To enable alerts:
- Set your email credentials in `send_email_alert()`
- Add your Slack webhook URL in `send_slack_alert()`

---

## 🎯 Next Steps (Milestone 4)

- Build a **Streamlit dashboard** to visualize anomalies interactively  
- Deploy the system locally or on cloud for real‑time monitoring  

---

## 📦 Requirements

See `requirements.txt` for dependencies:
```
numpy
pandas
matplotlib
scikit-learn
requests
```

---

## ✅ Summary

This pipeline:
- Generates or loads data  
- Detects anomalies with Isolation Forest  
- Saves results into reproducible files  
- Visualizes anomalies  
- Logs alerts for auditing  

It’s modular, reproducible, and GitHub‑ready.
