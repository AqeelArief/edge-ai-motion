# Edge AI Motion Anomaly Detection

## Project Overview
This project explores how **Edge AI systems** can process motion (accelerometer-style) data locally to detect unusual or risky movement while minimizing the amount of data sent to a server.

Instead of transmitting all raw sensor data, the system learns patterns of “normal” motion on-device and only sends **summarized information or alerts** when something out of the ordinary occurs. This approach mirrors real-world applications in wearables, health monitoring, and IoT devices.

---

## Motivation
Many devices such as smartwatches and fitness trackers continuously collect motion data. Sending all of this raw data to the cloud:
- wastes bandwidth
- increases latency
- raises privacy concerns

This project demonstrates how **edge-based processing** can reduce data transmission while still identifying important events like sudden impacts or abnormal motion.

---

## System Pipeline
The project follows an end-to-end pipeline:

1. **Raw Data Ingestion**
   - Accelerometer-style data with x, y, and z axes
   - Each row represents a moment in time

2. **Windowing & Feature Extraction**
   - Data is grouped into short time windows
   - Each window is summarized using statistical features such as:
     - mean acceleration
     - maximum acceleration

3. **Anomaly Detection**
   - Windows are evaluated against a threshold
   - Unusual motion patterns are flagged as alerts

4. **Edge Decision Logic**
   - Normal motion → no data sent
   - Anomalous motion → alert generated
   - This simulates efficient edge-device behavior

---

## Files in This Repository

- `explore_data.py`  
  Loads and inspects raw motion data to understand its structure and basic statistics.

- `window_data.py`  
  Breaks motion data into time windows and computes summary statistics for each window.

- `edge_pipeline.py`  
  Combines windowing, feature extraction, and anomaly detection into a single end-to-end edge AI pipeline.

- `motion_data.csv`  
  Sample motion dataset used to simulate accelerometer readings.

---

## Key Concepts Demonstrated
- Edge AI vs cloud-based processing
- Time-series windowing
- Feature extraction from sensor data
- Anomaly detection using statistical thresholds
- Data efficiency and system-level design

---

## Potential Extensions
- Replace threshold-based logic with a lightweight machine learning model
- Apply the pipeline to real wearable or workout data
- Visualize motion patterns and anomalies
- Deploy logic on a microcontroller or mobile device

---

