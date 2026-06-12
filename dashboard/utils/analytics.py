import pandas as pd

def vehicle_health(speed):

    health = 100

    if speed > 40:
        health -= 10

    if speed > 60:
        health -= 15

    if speed > 80:
        health -= 20

    if speed > 100:
        health -= 30

    return max(health, 0)


def driver_risk(speed):

    if speed <= 20:
        return 10

    elif speed <= 40:
        return 25

    elif speed <= 60:
        return 40

    elif speed <= 80:
        return 60

    elif speed <= 100:
        return 80

    else:
        return 100
    
def calculate_kpis(df):

    total_vehicles = df["Vehicle_ID"].nunique()

    active_alerts = len(
        df[df["Alert"] != "SAFE"]
    )

    geofence_count = len(
        df[
            df["Alert"].astype(str).str.contains(
                "Geofence",
                case=False,
                na=False
            )
        ]
    )

    theft_count = len(
        df[
            df["Alert"].astype(str).str.contains(
                "Theft",
                case=False,
                na=False
            )
        ]
    )

    return (
        total_vehicles,
        active_alerts,
        geofence_count,
        theft_count
    )