# gui_port_scanner.py

import tkinter as tk
from tkinter import ttk, scrolledtext
from threading import Thread
from scanner_core import run_scan, stop_scan

scan_thread = None

def start_scan_thread():
    global scan_thread
    progress_bar["value"] = 0
    output.delete(1.0, tk.END)
    scan_thread = Thread(target=start_scan)
    scan_thread.start()

def start_scan():
    target = entry.get()
    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        output.insert(tk.END, "❌ Invalid port range.\n")
        return

    if not target:
        output.insert(tk.END, "❌ Please enter a domain or IP\n")
        return

    output.insert(tk.END, f"\n🔍 Starting scan for {target} (Ports {start_port}-{end_port})\n")
    output.see(tk.END)

    def update_gui(line):
        output.insert(tk.END, line + "\n")
        output.see(tk.END)

    def update_progress(val):
        progress_bar["value"] = val

    result = run_scan(target, start_port, end_port, update_gui, update_progress)
    progress_bar["value"] = 100
    output.insert(tk.END, "\n✅ Scan completed!\n📄 Report saved in scan_reports folder.\n")
    output.see(tk.END)

def cancel_scan():
    stop_scan()
    output.insert(tk.END, "⛔ Scan stopped by user. Generating PDF report...\n")
    output.see(tk.END)

# GUI setup
root = tk.Tk()
root.title("🛡️ Port Scanner GUI")
root.geometry("600x650")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Enter Website / IP:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack()

frame_ports = tk.Frame(root, bg="#f0f0f0")
frame_ports.pack(pady=5)

tk.Label(frame_ports, text="Start Port:", bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=0, padx=5)
start_port_entry = tk.Entry(frame_ports, width=10)
start_port_entry.insert(0, "1")
start_port_entry.grid(row=0, column=1)

tk.Label(frame_ports, text="End Port:", bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=2, padx=5)
end_port_entry = tk.Entry(frame_ports, width=10)
end_port_entry.insert(0, "1024")
end_port_entry.grid(row=0, column=3)

frame_buttons = tk.Frame(root, bg="#f0f0f0")
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Start Scan", command=start_scan_thread, bg="#007acc", fg="white", font=("Arial", 12)).grid(row=0, column=0, padx=10)
tk.Button(frame_buttons, text="Stop and Generate PDF", command=cancel_scan, bg="#cc0000", fg="white", font=("Arial", 12)).grid(row=0, column=1, padx=10)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=10)

output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=25, font=("Courier", 10))
output.pack(padx=10, pady=10)

root.mainloop()
