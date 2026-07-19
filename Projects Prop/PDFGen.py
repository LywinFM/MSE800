try:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import inch
except ImportError as e:
    raise ImportError("ReportLab is not installed. Install it using `pip install reportlab` to generate PDFs.") from e

def create_pdf_report(filename):
    # Create a PDF canvas
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(1 * inch, height - 1 * inch, "Monthly Performance Report")

    # Subtitle
    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, height - 1.3 * inch, "Generated using Python and ReportLab")

    # Body text
    text = c.beginText(1 * inch, height - 2 * inch)
    text.setFont("Helvetica", 11)
    lines = [
        "Summary:",
        "This report outlines the key performance indicators for the month.",
        "",
        "Highlights:",
        "- Sales increased by 12%",
        "- Customer satisfaction improved",
        "- System uptime maintained at 99.9%",
        "",
        "Next Steps:",
        "- Expand automation",
        "- Improve onboarding workflow",
        "- Continue monitoring KPIs"
    ]

    for line in lines:
        text.textLine(line)

    c.drawText(text)

    # Finish the PDF
    c.showPage()
    c.save()

    print(f"PDF report '{filename}' created successfully.")

# Run the function
create_pdf_report("monthly_report.pdf")
