from scapy.all import sniff, IP, TCP, ICMP
from datetime import datetime

LOG_FILE = "python_ids_alerts.log"

def log_alert(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert = f"[{time}] {message}"
    print(alert)
    with open(LOG_FILE, "a") as f:
        f.write(alert + "\n")

def detect_packet(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst

        if ICMP in packet:
            log_alert(f"ICMP Ping Detected | Source: {src} → Destination: {dst}")

        if TCP in packet and packet[TCP].flags == "S":
            log_alert(f"TCP SYN Scan Detected | Source: {src} → Destination: {dst}")

print("Python-based IDS Started...")
print("Monitoring network traffic...\n")

sniff(prn=detect_packet, store=False)
