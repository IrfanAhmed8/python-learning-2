from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def generate_pdf_report(date, walk, water, sleep, feedback_lines, output_path='data/report.pdf'):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    c.setFont("Helvetica", 14)
    y = height - 50

    c.drawString(50, y, "📊 Health Report")
    y -= 30
    c.setFont("Helvetica", 12)

    c.drawString(50, y, f"📅 Date: {date}")
    y -= 20
    c.drawString(50, y, f"🚶 Walked: {walk} km")
    y -= 20
    c.drawString(50, y, f"💧 Water: {water} litres")
    y -= 20
    c.drawString(50, y, f"😴 Sleep: {sleep} hours")
    y -= 30

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "📝 Feedback:")
    y -= 20
    c.setFont("Helvetica", 12)

    for line in feedback_lines:
        if y < 50:  # Add new page if content reaches bottom
            c.showPage()
            y = height - 50
        c.drawString(60, y, f"- {line}")
        y -= 20

    c.save()
    print("✅ PDF report saved to 'data/report.pdf'")
