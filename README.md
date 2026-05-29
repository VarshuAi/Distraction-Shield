# 🛡️ Distraction-Shield: High-Yield NEET 2026 Focus Engine

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge" />
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows Platform" />
  <img src="https://img.shields.io/badge/Security-UAC--Elevated-FF5722?style=for-the-badge&logo=shield&logoColor=white" alt="UAC Elevated" />
  <img src="https://img.shields.io/badge/UI-Rich%20CLI-00F2FE?style=for-the-badge" alt="Rich CLI" />
</div>

<br/>

> [!IMPORTANT]
> **This focus engine is custom-built to eliminate digital distractions and optimize active recall sessions leading up to the NEET examination on June 21st, 2026.**

---

## ⚡ Key Features

* **🛡️ Windows UAC Auto-Elevation**: The application modifies the Windows `hosts` file to block distracting domains. I programmed the script to **automatically request Windows Administrator permissions (UAC pop-up)** when launched—no complex manual command prompt setup required.
* **🔒 Strict Distraction Shielding**: Restricts access to a highly robust list of unproductive domains (YouTube, Instagram, Reddit, Facebook, Twitter/X, Discord, Twitch, Netflix).
* **🧬 High-Yield NEET Motivation Engine**: Every 5 minutes, the active console draws a beautifully styled panel displaying a highly targeted, expert-crafted study prompt or motivational quote covering **NCERT Biology facts, Physics formula tips, and Chemistry reaction mechanics**.
* **🔓 Failsafe System Restoration**: Built with a strict, hardware-level interruption hook. If the focus timer expires or if you force-abort the session using `Ctrl + C`, the application **instantly cleanses your hosts file**, restoring full website access immediately.
* **📊 Persistent Audit Logger**: Automatically logs the date, study category, duration, and completion status of every single session to a local `focus_history.csv` spreadsheet to track preparation consistency.

---

## 📁 Repository Structure

```text
Distraction-Shield/
│
├── shield.py           # Core application logic & auto-admin elevation
├── requirements.txt    # Python dependencies (Rich CLI)
├── README.md           # This premium documentation
└── focus_history.csv   # Local session log (auto-generated upon first run)
```

---

## 🚀 Installation & How to Run

Follow these simple steps in your **PowerShell** or **Command Prompt** to launch your focus shield:

### Step 1: Install Python Dependencies
```bash
pip install rich
```

### Step 2: Download this Repository & Enter the Directory
```bash
cd ~\Desktop\github-profile\distraction_shield
```

### Step 3: Launch the Focus Shield!
```bash
python shield.py
```

*Note: Windows will display a security pop-up requesting permission to run this Python script as Administrator. **Click "Yes"**, and your glowing study dashboard will boot up immediately!*

---

## 🚪 Exiting the Shield
* **To Abort Early**: Simply press **`Ctrl + C`** in your active terminal. The program will catch the interrupt, cleanly unlock all blocked websites, and exit safely.
* **On Session Completion**: The timer will end automatically, play a completion indicator, cleanly restore all website access, and close the session.

---
<div align="center">
  <sub>Custom-built for maximum focus and elite NEET 2026 preparation.</sub>
</div>
