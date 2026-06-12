import sqlite3

conn = sqlite3.connect(
    "database/vehicle.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tracking(

id INTEGER PRIMARY KEY,
timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
latitude REAL,
longitude REAL,
status TEXT,
alert TEXT
)
""")

conn.commit()

def save_record(
        lat,
        lon,
        status,
        alert):

    cursor.execute("""
    INSERT INTO tracking(
    latitude,
    longitude,
    status,
    alert)

    VALUES(?,?,?,?)
    """,
    (
        lat,
        lon,
        status,
        alert
    ))

    conn.commit()