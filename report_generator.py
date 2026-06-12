from reportlab.platypus import *

from reportlab.lib.styles import getSampleStyleSheet

import sqlite3

doc = SimpleDocTemplate(
"reports/location_report.pdf"
)

styles = getSampleStyleSheet()

story = []

story.append(
Paragraph(
"Vehicle Tracking Report",
styles["Title"]
)
)

conn = sqlite3.connect(
"database/vehicle.db"
)

cursor = conn.cursor()

cursor.execute(
"SELECT * FROM tracking"
)

for row in cursor.fetchall():

    story.append(
        Paragraph(
        str(row),
        styles["Normal"]
        )
    )

doc.build(story)