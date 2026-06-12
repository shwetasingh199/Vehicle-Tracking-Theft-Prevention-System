from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/locations")

def get_locations():

    conn = sqlite3.connect(
        "database/vehicle.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tracking"
    )

    data = cursor.fetchall()

    return data