# Sentinel-SSH: Real-Time Honeypot & Alerting
A lightweight Python-based honeypot designed to detect unauthorized connection attempts and send instant alerts via Telegram.

## Features
**Real-Time Monitoring:** Listens on a dedicated "trap" port (Port 2222).
**Instant Alerting:** Sends the attacker's IP address directly to your phone via Telegram Bot API.
**Background Persistence:** Runs as a systemd service to stay active 24/7.
**Security First:** Uses `.env` files to keep API tokens hidden and safe.

## Tech Stack
**Language:** Python 3
**OS:** Ubuntu Linux
**Libraries:** `socket`, `requests`, `python-dotenv`

## Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ziyan/Sentinel-SSH.git](https://github.com/ziyan/Sentinel-SSH.git)
   cd Sentinel-SSH