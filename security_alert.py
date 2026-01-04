import os
import socket
import requests
from dotenv import load_dotenv

# --- Load Environment Variables ---
load_dotenv("bottokens.env")   

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
MESSAGE = os.getenv("MESSAGE", "Unauthorized connection detected!")
PORT = int(os.getenv("PORT", 2222))   # default port is 2222


# --- Safety Checks ---
if not TOKEN or not CHAT_ID:
    raise SystemExit(
        "\n[ERROR] Missing TOKEN or CHAT_ID.\n"
        "Create a bottokens.env file with:\n"
        "TOKEN=your_bot_token\n"
        "CHAT_ID=your_chat_id\n"
    )


# --- Telegram Alert Function ---
def send_telegram_alert(text: str):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }

    try:
        response = requests.post(url, data=payload, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to send Telegram alert: {e}")
        return False

    return True


# --- Honeypot Server ---
def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(("0.0.0.0", PORT))
    except OSError:
        raise SystemExit(f"[ERROR] Port {PORT} is already in use. Try another port.")

    server.listen(5)

    print(f"[-] Honeypot active on port {PORT}")
    send_telegram_alert(f"🛡 Sentinel-SSH active.\nListening on port {PORT}...")

    while True:
        client, addr = server.accept()
        attacker_ip = addr[0]

        print(f"[!] Connection detected from: {attacker_ip}")

        alert_msg = (
            "🚨 ALERT: Unauthorized connection detected\n"
            f"🌍 IP: {attacker_ip}\n"
            f"🔌 Port: {PORT}"
        )

        send_telegram_alert(alert_msg)
        client.close()


if __name__ == "__main__":
    start_honeypot()
