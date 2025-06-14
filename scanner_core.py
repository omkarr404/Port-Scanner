# scanner_core.py

import socket
from datetime import datetime
from report_generator import generate_pdf_report
import os

scan_running = True

def stop_scan():
    global scan_running
    scan_running = False

def run_scan(target, start_port, end_port, update_gui=None, update_progress=None):
    global scan_running
    scan_running = True

    os.makedirs("scan_reports", exist_ok=True)
    result_lines = []
    open_ports = []

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        return f"❌ Could not resolve domain."

    total_ports = end_port - start_port + 1
    scanned_ports = 0

    start_time = datetime.now()
    result_lines.append(f"🔎 Scanning {target} ({ip})")
    result_lines.append(f"⏱️ Started: {start_time}")
    result_lines.append(f"📌 Port range: {start_port} - {end_port}")
    result_lines.append("-" * 50)

    for port in range(start_port, end_port + 1):
        if not scan_running:
            result_lines.append("⛔ Scan cancelled by user.")
            break
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                msg = f"[+] Port {port} is OPEN"
                result_lines.append(msg)
                open_ports.append(port)
                if update_gui:
                    update_gui(msg)
            s.close()
        except Exception:
            continue

        scanned_ports += 1
        if update_progress:
            progress = int((scanned_ports / total_ports) * 100)
            update_progress(progress)

    end_time = datetime.now()
    result_lines.append("-" * 50)
    result_lines.append(f"✅ Scan Finished at: {end_time}")
    result_lines.append(f"⏳ Duration: {end_time - start_time}")
    if scan_running:
        result_lines.append("✅ Full port range scanned successfully!")

    # Generate PDF only (no txt file)
    filename_base = f"scan_reports/scan_report_{target.replace('.', '_')}"
    generate_pdf_report(target, ip, open_ports, start_time, end_time, filename_base + ".pdf")

    return "\n".join(result_lines)
