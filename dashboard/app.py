import streamlit as st
import pandas as pd
import folium
import sys
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(BASE_DIR)

from geopy.distance import geodesic
from streamlit_folium import st_folium

from utils.analytics import *
from utils.alerts import *
from utils.report_generator import *
from utils.playback import *
from utils.route_analytics import calculate_route_distance

from dashboard.utils.analytics import (
    vehicle_health,
    driver_risk,
    calculate_kpis
)

from dashboard.utils.alerts import (
    get_live_alerts
)

from dashboard.utils.report_generator import (
    generate_report
)

from dashboard.utils.playback import (
    create_route_map
)

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Vehicle Tracking & Theft Prevention System",
    layout="wide"
)

st.title(
    "🚗 Smart Vehicle Tracking & Theft Prevention Platform"
)

# =====================================
# CONFIG
# =====================================

SAFE_ZONE = (28.6139, 77.2090)

SAFE_RADIUS = 500

DATA_FOLDER = "data"

CSV_FILE = os.path.join(
    DATA_FOLDER,
    "vehicle_logs.csv"
)

# =====================================
# CREATE FOLDERS
# =====================================

os.makedirs(
    DATA_FOLDER,
    exist_ok=True
)

os.makedirs(
    "reports",
    exist_ok=True
)

# =====================================
# CREATE CSV IF NOT EXISTS
# =====================================

if not os.path.exists(CSV_FILE):

    pd.DataFrame(columns=[
        "Vehicle_ID",
        "Latitude",
        "Longitude",
        "Speed",
        "Engine_Status",
        "Lock_Status",
        "Alert"
    ]).to_csv(
        CSV_FILE,
        index=False
    )

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv(CSV_FILE)

# =====================================
# SIDEBAR
# =====================================

st.sidebar.header(
    "🚘 Vehicle Data Entry"
)

vehicle_id = st.sidebar.text_input(
    "Vehicle ID",
    "CAR001"
)

latitude = st.sidebar.number_input(
    "Latitude",
    value=28.6139,
    format="%.6f"
)

longitude = st.sidebar.number_input(
    "Longitude",
    value=77.2090,
    format="%.6f"
)

speed = st.sidebar.number_input(
    "Speed (km/h)",
    min_value=0.0,
    value=0.0
)

engine_status = st.sidebar.selectbox(
    "Engine Status",
    [
        "OFF",
        "ON"
    ]
)

lock_status = st.sidebar.selectbox(
    "Vehicle Lock",
    [
        "LOCKED",
        "UNLOCKED"
    ]
)

# =====================================
# SAVE DATA
# =====================================

if st.sidebar.button(
    "➕ Add Vehicle Data"
):

    current_location = (
        latitude,
        longitude
    )

    distance = geodesic(
        SAFE_ZONE,
        current_location
    ).meters

    alert = "SAFE"

    if distance > SAFE_RADIUS:

        alert = "⚠ Geofence Breach"

    if (
        lock_status == "LOCKED"
        and speed > 5
    ):

        alert = "🚨 Theft Detected"

    new_row = {
        "Vehicle_ID": vehicle_id,
        "Latitude": latitude,
        "Longitude": longitude,
        "Speed": speed,
        "Engine_Status": engine_status,
        "Lock_Status": lock_status,
        "Alert": alert
    }

    df = pd.concat(
        [
            df,
            pd.DataFrame([new_row])
        ],
        ignore_index=True
    )

    df.to_csv(
        CSV_FILE,
        index=False
    )

    st.sidebar.success(
        "Data Added Successfully"
    )

    st.rerun()

# =====================================
# NO DATA CHECK
# =====================================

if len(df) == 0:

    st.warning(
        "No vehicle data available."
    )

    st.stop()

# =====================================
# KPI SECTION
# =====================================
st.write(df.head())
st.write(df.columns)

total = df["Vehicle_ID"].nunique()

active_alerts = len(
    df[df["Alert"] != "SAFE"]
)

geofence_count = len(
    df[
        df["Alert"].astype(str).str.contains(
            "Geofence",
            na=False
        )
    ]
)

theft_count = len(
    df[
        df["Alert"].astype(str).str.contains(
            "Theft",
            na=False
        )
    ]
)


c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "🚗 Total Vehicles",
    total
)

c2.metric(
    "🚨 Active Alerts",
    active_alerts
)

c3.metric(
    "📍 Geofence Violations",
    geofence_count
)

c4.metric(
    "🔒 Theft Attempts",
    theft_count
)

st.divider()

latest = df.iloc[-1]
latest_alert = latest["Alert"]

if latest_alert == "SAFE":

    st.success(
        "✅ Vehicle operating normally"
    )

elif "Geofence" in latest_alert:

    st.warning(
        "⚠ Vehicle moved outside safe zone"
    )

elif "Theft" in latest_alert:

    st.error(
        "🚨 Theft attempt detected"
    )

# =====================================
# LATEST VEHICLE STATUS
# =====================================

latest = df.iloc[-1]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "🚗 Vehicle",
    latest["Vehicle_ID"]
)

col2.metric(
    "⚡ Speed",
    f"{latest['Speed']} km/h"
)

col3.metric(
    "🔧 Engine",
    latest["Engine_Status"]
)

col4.metric(
    "🚨 Alert",
    latest["Alert"]
)


# =====================================
# ALERT BANNER
# =====================================
latest = df.iloc[-1]
if latest["Alert"] == "SAFE":

    st.success(
        "✅ Vehicle operating normally"
    )

elif "Geofence" in str(latest["Alert"]):

    st.warning(
        "⚠ Vehicle moved outside safe zone"
    )

elif "Theft" in str(latest["Alert"]):

    st.error(
        "🚨 Theft attempt detected"
    )

# =====================================
# HEALTH SCORE
# =====================================

health = vehicle_health(
    latest["Speed"]
)

risk = driver_risk(
    latest["Speed"]
)
col1, col2 = st.columns(2)

with col1:

    st.subheader(
        "🩺 Vehicle Health Score"
    )

    st.metric(
        "Health Score",
        f"{health}%"
    )

    st.progress(
        health / 100
    )

with col2:

    st.subheader(
        "⚠ Driver Risk Score"
    )

    st.metric(
        "Risk Score",
        f"{risk}%"
    )

    st.progress(
        risk / 100
    )
    
# =====================================
# GOOGLE MAP LINK
# =====================================

maps_link = (
    f"https://maps.google.com/?q="
    f"{latest['Latitude']},"
    f"{latest['Longitude']}"
)

st.markdown(
    f"### 📍 [Open Current Location in Google Maps]({maps_link})"
)

# =====================================
# FLEET MAP
# =====================================

st.subheader(
    "🌍 Fleet Monitoring Map"
)

fleet_map = folium.Map(
    location=[28.6139, 77.2090],
    zoom_start=12
)

folium.Circle(
    SAFE_ZONE,
    radius=SAFE_RADIUS,
    popup="Safe Zone"
).add_to(fleet_map)

for _, row in df.iterrows():

    color = "green"

    if "Geofence" in row["Alert"]:
        color = "orange"

    if "Theft" in row["Alert"]:
        color = "red"

    folium.Marker(
        [
            row["Latitude"],
            row["Longitude"]
        ],
        popup=f"""
        Vehicle: {row['Vehicle_ID']}
        Speed: {row['Speed']}
        Alert: {row['Alert']}
        """,
        icon=folium.Icon(
            color=color
        )
    ).add_to(fleet_map)

st_folium(
    fleet_map,
    width=1200,
    height=550
)

st.divider()

# =====================================
# ROUTE PLAYBACK
# =====================================

st.subheader(
    "🛣 Route Playback"
)

vehicle_selected = st.selectbox(
    "Select Vehicle",
    sorted(
        df["Vehicle_ID"].unique()
    )
)

vehicle_df = df[
    df["Vehicle_ID"]
    == vehicle_selected
]

# -------------------------
# Route Distance Analytics
# -------------------------

distance = calculate_route_distance(
    vehicle_df
)

st.metric(
    "Total Route Distance",
    f"{distance} km"
)

if len(vehicle_df) > 1:

    route_map = create_route_map(
        vehicle_df
    )

    st_folium(
        route_map,
        width=1200,
        height=500
    )

else:

    st.info(
        "Need at least 2 points for route playback."
    )

st.divider()


# =====================================
# SPEED ANALYTICS
# =====================================

st.subheader(
    "📈 Vehicle Speed Analytics"
)

speed_df = vehicle_df[
    ["Speed"]
]

st.line_chart(speed_df)

st.divider()

# =====================================
# COMPLETE DATA TABLE
# =====================================

st.subheader(
    "📄 Vehicle History"
)

st.dataframe(
    df,
    use_container_width=True
)

# =====================================
# DOWNLOAD CSV
# =====================================

csv_data = df.to_csv(
    index=False
)

st.download_button(
    label="⬇ Download CSV",
    data=csv_data,
    file_name="vehicle_logs.csv",
    mime="text/csv"
)

# =====================================
# PDF REPORT
# =====================================

st.subheader(
    "📑 Report Generator"
)

if st.button(
    "Generate PDF Report"
):

    pdf_path = generate_report(df)

    with open(
        pdf_path,
        "rb"
    ) as file:

        st.download_button(
            label="⬇ Download PDF Report",
            data=file,
            file_name="Vehicle_Report.pdf",
            mime="application/pdf"
        )

    st.success(
        "PDF Generated Successfully!"
    )