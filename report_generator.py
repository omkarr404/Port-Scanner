# report_generator.py

from fpdf import FPDF

def generate_pdf_report(target, ip, open_ports, start_time, end_time, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)

    pdf.cell(0, 10, f"Port Scan Report for {target} ({ip})", ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.ln(10)

    pdf.cell(0, 10, f"Scan started: {start_time}", ln=True)
    pdf.cell(0, 10, f"Scan finished: {end_time}", ln=True)
    pdf.ln(5)

    if open_ports:
        pdf.cell(0, 10, f"Open Ports:", ln=True)
        for port in open_ports:
            pdf.cell(0, 10, f" - Port {port}", ln=True)
    else:
        pdf.cell(0, 10, "No open ports found.", ln=True)

    pdf.output(filename)
