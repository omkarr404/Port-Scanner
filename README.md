
# 🛡️ Port Scanner GUI

A user-friendly Python-based **Port Scanner** with a graphical interface built using Tkinter. This tool allows users to scan custom port ranges on any IP or domain, view results in real time, and generate a **PDF report** of open ports.

---

## 🚀 Features

- ✅ Easy-to-use graphical user interface (Tkinter)
- 🎯 Custom port range input
- 📈 Real-time progress bar during scanning
- 🛑 Stop scan anytime and generate partial report
- 📄 PDF report generation (via `fpdf`)
- 💡 Works with both IP addresses and domain names
- ⚡ Lightweight and fast

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
````

---

## 🔧 How to Run

```bash
python gui_port_scanner.py
```

---

## 📝 Output

* All scan reports are saved automatically in the `scan_reports/` folder.
* Reports are generated in **PDF format** after scan completion or cancellation.

---

## 📌 Example Usage

1. Enter a domain or IP (e.g., `scanme.nmap.org`)
2. Enter a port range (e.g., `1` to `1000`)
3. Click **Start Scan**
4. Click **Stop and Generate PDF** if you want to end early
5. The PDF report will be saved in the `scan_reports/` folder

---

## ⚠️ Legal Disclaimer

> Only scan IP addresses or domains that you **own** or have **explicit permission** to scan. Unauthorized port scanning is illegal and may violate cybersecurity laws.

---

## 🖼️ Screenshots (Optional)

> Add screenshots of your GUI and generated PDF here if you like.

---

## 👤 Author

**Omkar Sawant**
🔗 [GitHub Profile](https://github.com/omkarr404)

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use, modify, and distribute.

---


---

### ✅ Bonus Tip

Also create a `requirements.txt` file with:

```

fpdf

```

Let me know if you want me to also generate a banner image (`.png`) or GitHub project logo!
```
