# 🚗 ParkPulse AI

### AI-Driven Parking Intelligence System for Smarter Traffic Enforcement

<p align="center">
  <img src="/Users/omraj/ParkPulseAI/Screenshots/Screenshot 2026-06-16 at 2.33.28 PM.png" />
  <img src="/Users/omraj/ParkPulseAI/Screenshots/Screenshot 2026-06-16 at 2.33.37 PM.png" />
  <img src="/Users/omraj/ParkPulseAI/Screenshots/Screenshot 2026-06-16 at 2.34.19 PM.png" />
  <img src="/Users/omraj/ParkPulseAI/Screenshots/Screenshot 2026-06-16 at 2.34.26 PM.png" />
  <img src="/Users/omraj/ParkPulseAI/Screenshots/Screenshot 2026-06-16 at 2.34.30 PM.png" />
  <img src="/Users/omraj/ParkPulseAI/Screenshots/Screenshot 2026-06-16 at 2.34.34 PM.png" />
  <img src="/Users/omraj/ParkPulseAI/Screenshots/Screenshot 2026-06-16 at 2.34.47 PM.png" />
  <img src=" /Users/omraj/ParkPulseAI/Screenshots/Screenshot 2026-06-16 at 2.34.52 PM.png" />          >

</p>


🎥 Demo Video

Watch the complete demonstration of ParkPulse AI here:

🔗 Google Drive Demo Link:
https://drive.google.com/file/d/1HpNxE8JZ2zkdDV1HuGh0x1HG2TCFq6bP/view?usp=sharing
---

## 📌 Problem Statement

### Poor Visibility on Parking-Induced Congestion

Illegal parking and spillover parking near commercial areas, metro stations, markets, and event zones choke carriageways and intersections.

### Current Challenges

* 🚓 Enforcement is patrol-based and reactive.
* 🗺️ No visibility into parking hotspots.
* 📊 No linkage between parking violations and congestion impact.
* 🚦 Difficult to prioritize enforcement zones.
* 👮 Limited resources lead to inefficient deployment.

---

# 💡 Our Solution

**ParkPulse AI** is an AI-powered parking intelligence platform that combines:

* Historical parking violation analytics
* Parking Impact Score (PIS)
* Hotspot heatmaps
* AI-driven recommendations
* YOLOv8 video analytics
* Traffic impact estimation using congestion proxies

to transform parking enforcement from **reactive policing to proactive intelligence**.

---

# 🏗️ System Architecture

```text
Historical Parking Data
        ↓
Hotspot Detection
        ↓
Parking Impact Score (PIS)
        ↓
Risk Categorization
        ↓
Enforcement Recommendations
        ↓
Interactive Dashboard
```

### AI Surveillance Pipeline

```text
Traffic Video
      ↓
YOLOv8 Vehicle Detection
      ↓
Multi-Object Tracking
      ↓
Illegal Parking Detection
      ↓
Queue Length Estimation
      ↓
Speed Estimation
      ↓
Delay Index Calculation
      ↓
Evidence Generation
```

---

# ✨ Key Features

## 📊 Historical Intelligence

* Bengaluru Parking Heatmap
* Top 20 Parking Hotspots
* Parking Impact Score (PIS)
* Risk Categorization
* Enforcement Recommendations

---

## 🤖 AI Surveillance

* YOLOv8 Vehicle Detection
* Multi-Object Tracking
* Illegal Parking Detection
* Evidence Snapshot Generation
* Annotated Video Output

---

## 🚦 Traffic Impact Estimation

* Queue Length Estimation
* Average Vehicle Speed
* Delay Index
* Congestion Proxy Metrics

---

## 🖥️ Interactive Dashboard

* React + Recharts Frontend
* Flipkart-inspired UI
* Heatmap Integration
* Video Playback
* Real-Time Metrics Visualization

---

# 📷 Dashboard Screenshots

> Replace the images below with your own screenshots.

## Dashboard Overview

```markdown
![Dashboard](screenshots/dashboard.png)
```

---

## Parking Heatmap

```markdown
![Heatmap](screenshots/heatmap.png)
```

---

## Top Hotspots

```markdown
![Hotspots](screenshots/hotspots.png)
```

---

## YOLO Detection

```markdown
![YOLO](screenshots/yolo_detection.png)
```

---

## Recommendations

```markdown
![Recommendations](screenshots/recommendations.png)
```

---

# 🎥 Demo

Demo Video:

```text
Add Google Drive / YouTube Link Here
```

The demo showcases:

* Parking hotspot analysis
* Parking Impact Scores
* Heatmap visualization
* AI surveillance
* Illegal parking detection
* Traffic impact estimation

---

# 📁 Project Structure

```text
PARKPULSEAI/
│
├── backend/              # FastAPI backend
├── data/                 # Input datasets
├── frontend/             # React frontend
├── models/               # ML models
├── notebooks/            # Analysis notebooks
├── outputs/              # Generated outputs
├── video/                # Sample videos
│
├── yolov8n.pt            # YOLO model
├── package.json
├── package-lock.json
├── README.md
│
└── node_modules/
```

---

# ⚙️ Installation

## Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn app:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

# ▶️ Running Historical Analytics

## Generate Heatmap

```bash
python backend/services/02_heatmap.py
```

---

## Generate Hotspots

```bash
python backend/services/03_smart_hotspots.py
```

---

## Calculate Parking Impact Score

```bash
python backend/services/04_parking_impact_score.py
```

---

## Generate Recommendations

```bash
python backend/services/05_recommendations.py
```

---

# 🤖 Running AI Surveillance

Place a video inside:

```text
video/sample_parking.mp4
```

Run:

```bash
python backend/services/06_video_detection.py
```

Outputs:

```text
outputs/
├── annotated_parking_fixed.mp4
├── traffic_metrics.txt
└── evidence/
```

---

# 📈 Parking Impact Score (PIS)

PIS prioritizes enforcement using:

* Parking Violation Density
* Diversity of Violation Types

Formula:

```text
PIS =
(0.7 × Violation Density)
+
(0.3 × Violation Diversity)
```

Risk Levels:

| Score | Risk     |
| ----- | -------- |
| ≥ 80  | Critical |
| 50–79 | High     |
| 20–49 | Moderate |
| < 20  | Low      |

---

# 🚦 Traffic Metrics

Since real traffic sensors were unavailable, ParkPulse AI estimates congestion impact using video-derived proxies.

## Queue Length

```text
Average vehicles present near hotspot
```

---

## Average Speed

```text
Vehicle movement estimated from tracking
```

---

## Delay Index

```text
Traffic slowdown indicator derived from speed reduction
```

---

# 🌍 Real-World Impact

ParkPulse AI enables:

* Faster identification of parking hotspots
* Targeted enforcement deployment
* Reduced congestion
* Improved road throughput
* Better utilization of traffic personnel

---

# 🚀 Future Scope

* Live CCTV Integration
* Automated Enforcement Alerts
* Multi-Camera Monitoring
* Smart City Dashboard Integration
* Cloud Deployment
* Predictive Congestion Forecasting

---

# 🛠️ Tech Stack

### Frontend

* React
* Axios
* Recharts
* React Icons

### Backend

* FastAPI
* Pandas
* Uvicorn

### AI & Computer Vision

* YOLOv8
* OpenCV
* Supervision

### Data Science

* NumPy
* Matplotlib
* Folium

---

Hackathon:

```text
Flipkart Gridlock Hackathon
```

---

# 📄 License

This project was developed for academic and hackathon purposes.

© 2026 ParkPulse AI Team

---

# 🏆 Conclusion

ParkPulse AI transforms fragmented parking violation records and surveillance feeds into actionable intelligence.

By combining historical analytics with AI-powered video understanding, the platform empowers authorities to move from reactive enforcement toward proactive congestion management for smarter cities.
