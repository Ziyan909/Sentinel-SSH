# 🔐 Sentinel-SSH  
_A lightweight Python honeypot that detects unauthorized SSH-style connection attempts and sends instant alerts via Telegram._

Sentinel-SSH is designed as a **defensive security project** to help developers and students understand attacker activity on exposed ports.  
It simulates a service running on a custom “trap” port — when a connection attempt is made, the attacker’s IP is logged and an alert is pushed to your Telegram bot in real-time.

---

## ✨ Features

- **🛰 Real-Time Monitoring**  
  Listens continuously on a decoy port (default: `2222`) to detect inbound connection attempts.

- **⚡ Instant Telegram Alerts**  
  Sends attacker details to your Telegram bot the moment activity is detected.

- **🔐 Secret-Safe Design**  
  API keys and bot tokens are stored securely in a `.env` file — **never hard-coded.**

- **🧠 Simple & Lightweight**  
  Pure Python — no heavy dependencies or complex setup required.

- **🛡 Learning-Focused**  
  Built to demonstrate how honeypots detect malicious scanning & probing activity.

---

## 🏗 Tech Stack

| Component | Used |
|----------|------|
| Language | Python 3 |
| OS | Ubuntu Linux |
| Libraries | `socket`, `requests`, `python-dotenv` |

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Ziyan909/Sentinel-SSH.git
cd Sentinel-SSH
