# 🚗 IoT Vehicle Tracking & Theft Prevention System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![IoT](https://img.shields.io/badge/IoT-GPS%20Tracking-green)
![Status](https://img.shields.io/badge/Project-Completed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

### Smart Fleet Monitoring, Geofencing & Vehicle Security Platform

An industry-oriented IoT-based Vehicle Tracking & Theft Prevention System designed for real-time fleet monitoring, GPS tracking, geofence violation detection, route playback, vehicle analytics, and theft alerts.

</div>

---

# 📌 Project Overview

Vehicle theft and inefficient fleet monitoring remain major challenges for logistics companies, ride-sharing services, school transportation systems, and personal vehicle owners.

This project provides a complete Vehicle Telematics Platform that enables:

✅ Real-Time Vehicle Tracking

✅ Geofence Monitoring

✅ Theft Detection

✅ Fleet Monitoring Dashboard

✅ Driver Risk Analysis

✅ Vehicle Health Scoring

✅ Route Playback Visualization

✅ PDF Report Generation

✅ Google Maps Integration

✅ Interactive Streamlit Dashboard

The system simulates an IoT-enabled vehicle monitoring ecosystem similar to solutions used by Uber, Ola, Rapido, Bosch Mobility, Fleet Complete, and Tata Telematics.

---

# 🎯 Problem Statement

Traditional vehicle security systems only provide alarms after a theft occurs.

Modern intelligent transportation systems require:

- Real-time location monitoring
- Geofence enforcement
- Theft prevention mechanisms
- Driver behavior analysis
- Fleet visibility
- Historical route tracking

This project addresses these challenges using GPS tracking and IoT-inspired cloud monitoring techniques.

---

# 🏗 System Architecture

```text
Vehicle GPS Coordinates
          │
          ▼
   ESP32 / Simulator
          │
          ▼
  Location Processing
          │
          ▼
   Geofence Engine
          │
          ▼
 Theft Detection Logic
          │
          ▼
 Analytics Engine
          │
          ▼
 Streamlit Dashboard
          │
          ▼
 Reports & Alerts
```

---

# 🔥 Key Features

## 🚗 Vehicle Tracking

- Real-time vehicle monitoring
- GPS coordinate tracking
- Multi-vehicle support
- Fleet visualization

---

## 🌍 Fleet Monitoring

Monitor multiple vehicles on a single map.

Features:

- Vehicle markers
- Status indicators
- Alert-based coloring
- Live fleet overview

---

## 📍 Geofence Detection

Detects when a vehicle exits the safe zone.

### Safe Zone

```text
Radius: 500 meters
```

Alerts:

```text
⚠ Geofence Breach
```

---

## 🚨 Theft Detection

If vehicle is:

```text
LOCKED
```

and speed becomes:

```text
> 5 km/h
```

System triggers:

```text
🚨 Theft Detected
```

---

## 🛣 Route Playback

Visualize vehicle movement history.

Features:

- Start Point
- End Point
- Route Path
- Checkpoints
- Route Distance

---

## 📊 Vehicle Health Score

Analyzes vehicle condition based on speed patterns.

Example:

| Speed | Health Score |
|---------|---------|
| 20 km/h | 100% |
| 60 km/h | 90% |
| 80 km/h | 75% |
| 100 km/h | 55% |

---

## ⚠ Driver Risk Score

Evaluates driving behavior.

Example:

| Speed | Risk |
|---------|---------|
| 20 km/h | 10% |
| 40 km/h | 25% |
| 60 km/h | 40% |
| 80 km/h | 60% |
| 100 km/h | 80% |

---

## 📄 Report Generation

Generate:

- Vehicle Reports
- Route Reports
- Alert Reports

Formats:

```text
CSV
PDF
```

---

# 🧠 Industry Applications

## 🚖 Ride Sharing Platforms

- Uber
- Ola
- Rapido

Use Cases:

- Driver monitoring
- Vehicle tracking
- Safety analytics

---

## 🚚 Logistics Companies

Use Cases:

- Fleet management
- Route optimization
- Theft prevention

---

## 🚌 School Transportation

Use Cases:

- Bus tracking
- Parent notifications
- Student safety

---

## 🚗 Personal Vehicles

Use Cases:

- Anti-theft monitoring
- Remote tracking
- Location history

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| Streamlit | Dashboard |
| Pandas | Data Processing |
| Folium | Interactive Maps |
| Geopy | Distance Calculation |
| ReportLab | PDF Reports |
| CSV Storage | Data Logging |

---

# 📂 Project Structure

```text
IoT-Vehicle-Tracking-Theft-Prevention-System/

│
├── dashboard/
│   └── app.py
│
├── utils/
│   ├── analytics.py
│   ├── alerts.py
│   ├── playback.py
│   ├── route_analytics.py
│   └── report_generator.py
│
├── data/
│   └── vehicle_logs.csv
│
├── reports/
│
├── images/
│   ├── dashboard.png
│   ├── fleet_map.png
│   ├── route_playback.png
│   ├── analytics.png
│   └── alerts.png
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/IoT-Vehicle-Tracking-Theft-Prevention-System.git
```

---

## Move Into Project

```bash
cd IoT-Vehicle-Tracking-Theft-Prevention-System
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📈 Dashboard Features

## KPI Cards

Displays:

- Total Vehicles
- Active Alerts
- Geofence Violations
- Theft Attempts

---

## Fleet Monitoring Map

Displays:

- Vehicle locations
- Geofence area
- Alert markers

---

## Route Playback

Displays:

- Vehicle route history
- Distance travelled
- Route checkpoints

---

## Analytics Panel

Displays:

- Vehicle Health Score
- Driver Risk Score
- Speed Trends

---

# 📷 Project Screenshots

## Dashboard Overview

<img width="1762" height="832" alt="P2 O s1" src="https://github.com/user-attachments/assets/cd88ad62-91f9-4e2a-9d90-f346ef500bf5" />

---

## Data Entry

<img width="422" height="873" alt="P2 O s2" src="https://github.com/user-attachments/assets/9819689e-ff71-4882-89be-1f38151d1faa" />

## Theft Detection

<img width="1482" height="860" alt="P2 O s3" src="https://github.com/user-attachments/assets/9d4c431f-9f79-4d73-8ae4-3987c1463338" />

## Fleet Monitoring

<img width="1560" height="902" alt="P2 O s4" src="https://github.com/user-attachments/assets/377b14a7-3f9f-4bfd-9009-63f77f27d990" />

---

## Route Playback

<img width="1807" height="886" alt="P2 O s5" src="https://github.com/user-attachments/assets/9e969010-26d2-4825-8eee-a04c47721fb8" />

---

## Analytics Dashboard

<img width="1557" height="688" alt="P2 O s6" src="https://github.com/user-attachments/assets/22405695-203c-4680-918c-d63df88b83a8" />

---

## Vehicle History

<img width="1793" height="852" alt="P2 O s7" src="https://github.com/user-attachments/assets/69fa8fe7-0b61-4843-a579-a7745c051f26" />

---

# 🧪 Sample Dataset

```csv
Vehicle_ID,Latitude,Longitude,Speed,Engine_Status,Lock_Status,Alert

CAR001,28.6139,77.2090,0,OFF,LOCKED,SAFE

CAR001,28.6145,77.2102,25,ON,UNLOCKED,SAFE

CAR001,28.6152,77.2118,40,ON,UNLOCKED,SAFE

CAR002,28.6208,77.2185,42,ON,UNLOCKED,⚠ Geofence Breach

CAR003,28.6321,77.2280,10,ON,LOCKED,🚨 Theft Detected
```

---

# 📊 Future Improvements

- Real GPS Integration
- ESP32 Support
- MQTT Communication
- Firebase Cloud Storage
- Mobile Application
- AI Driver Behavior Analysis
- Fuel Consumption Analytics
- Predictive Maintenance
- SOS Emergency System
- Live Vehicle Animation

---

# 🎓 Learning Outcomes

This project demonstrates:

- IoT System Design
- GPS Tracking Concepts
- Vehicle Telematics
- Fleet Monitoring
- Data Analytics
- Dashboard Development
- Geofencing Logic
- Theft Detection Systems
- Report Automation
- Software Engineering Practices

---

# 💼 Placement Relevance

Suitable for:

- IoT Engineer
- Embedded Systems Engineer
- Python Developer
- Data Analyst
- Smart Mobility Engineer
- Vehicle Telematics Engineer
- Software Developer Intern

---

# 👨‍💻 Author

**Shweta Singh**

B.Tech Electronics & Computer Engineering

IoT | Embedded Systems | Python | AI | Smart Mobility Solutions

---

# ⭐ If You Like This Project

Please consider giving this repository a Star ⭐

It motivates further development and helps others discover the project.
