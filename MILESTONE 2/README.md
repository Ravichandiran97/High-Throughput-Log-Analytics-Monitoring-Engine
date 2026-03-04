# Milestone 2: Log Ingestion & Distributed Parsing System

## 📌 Objective
Develop a reproducible pipeline that ingests synthetic logs, parses them using **Dask** and **Ray**, and validates throughput performance.  
This milestone demonstrates ingestion, distributed parsing, and benchmarking.

---

## 📂 Repository Structure
```
log-analytics-engine/
├── data_generation/        # Synthetic log generator notebook
├── ingestion/              # (Optional) ingestion helper script
├── parsers/                # Dask & Ray parsing notebooks
├── validation/             # Throughput validation notebook + screenshots
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

---

## ⚙️ Workflow

### 1. Log Generation
- Synthetic logs created in `data_generation/log_generator.ipynb`.
- Example output: `sample_logs.csv`.

### 2. Ingestion
- Logs ingested either:
  - Directly in notebooks (`dd.read_csv("sample_logs.csv")`), or
  - Via helper functions in `ingestion/ingest_logs.py`.

### 3. Distributed Parsing
- **Dask**:
  ```python
  import dask.dataframe as dd
  logs_dask = dd.read_csv("sample_logs.csv")
  parsed_dask = logs_dask[["Timestamp", "Level", "Message"]]
  parsed_dask.head()
  ```
- **Ray**:
  ```python
  import ray, pandas as pd
  ray.shutdown()
  ray.init(local_mode=True, ignore_reinit_error=True)

  @ray.remote
  def parse_chunk(file_path):
      df = pd.read_csv(file_path)
      return df[["Timestamp", "Level", "Message"]]

  futures = [parse_chunk.remote("sample_logs.csv")]
  results = ray.get(futures)
  parsed_ray = pd.concat(results)
  parsed_ray.head()
  ```

### 4. Throughput Validation
- Compare performance of Dask vs Ray:
  ```python
  import time

  # Dask throughput
  start = time.time()
  count_dask = parsed_dask.count().compute()
  end = time.time()
  print(f"Dask throughput: {count_dask} logs in {end-start:.2f} seconds")

  # Ray throughput
  start = time.time()
  count_ray = len(parsed_ray)
  end = time.time()
  print(f"Ray throughput: {count_ray} logs in {end-start:.2f} seconds")
  ```

---

## 📊 Validation Evidence
Screenshots stored in `validation/screenshots/`:
- **Dask parsing output** (`parsed_dask.head()`)
- **Ray parsing output** (`parsed_ray.head()`)
- **Throughput results** (Dask vs Ray)

---

## 📦 Requirements
Dependencies listed in `requirements.txt`:
```
dask[complete]
ray
pandas
pyarrow
fastparquet
```

---

## ✅ Deliverables
- End‑to‑end ingestion + parsing pipeline
- Throughput validation notebook
- Screenshots for evidence
- Organized repo structure
- Documentation (this README)

---

## 🚀 Next Milestone
Milestone 3 will extend this pipeline to **real‑time log streaming and monitoring**, integrating ingestion with live sources (e.g., Kafka) and scaling distributed parsing.
```
