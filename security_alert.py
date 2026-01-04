import os
import socket
from dotenv import load_dotenv
import requests

load_dotenv("bottokens.env")

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
MESSAGE = "It's Working huh"

def send_telegram_alert(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    
    response = requests.post(url, data=payload)
    return response.json()

print(send_telegram_alert(MESSAGE))

def start_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("0.0.0.0", 2222))
    
    server.listen(5)
    print("[-] Honeypot is active... ")
    send_telegram_alert(" Sentinel-SSH: Honeypot is now LIVE and monitoring port 2222.")

    while True:
        client, addr = server.accept()
        attacker_ip = addr[0]
        
        print(f"[!] Someone just Knocked ip: {attacker_ip}")
        
        alert_msg = f" ALERT: Unauthorized connection attempt detected!\nIP: {attacker_ip}\nPort: 2222"
        send_telegram_alert(alert_msg)
        
        client.close()

start_honeypot()