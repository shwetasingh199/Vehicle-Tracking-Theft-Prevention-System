from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(df):

    filename = "reports/vehicle_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "Vehicle Tracking Report",
            styles["Title"]
        )
    )

    for _, row in df.iterrows():

        text = (
            f"Vehicle: {row['Vehicle_ID']} | "
            f"Speed: {row['Speed']} | "
            f"Alert: {row['Alert']}"
        )

        elements.append(
            Paragraph(
                text,
                styles["Normal"]
            )
        )

    doc.build(elements)

    return filename