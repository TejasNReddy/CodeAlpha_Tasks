# Network Intrusion Detection System (NIDS)

This project implements a **Network Intrusion Detection System (NIDS)** using **Snort** and a **Python-based IDS** as part of the **CodeAlpha Cyber Security Internship – Task 4**.

---

## 🔐 What is an IDS?
An Intrusion Detection System monitors network traffic to identify suspicious or malicious activity and generates alerts for potential attacks.

---

## 🛠 Tools & Technologies
- Ubuntu 24.04 LTS
- Snort (Primary NIDS)
- Python 3
- Scapy
- Nmap (for testing)

---

## ⚙️ System Architecture
- Snort monitors live network traffic using custom detection rules
- Alerts are generated for ICMP pings and TCP SYN scans
- Logs are stored for analysis
- A Python-based IDS is implemented to understand packet-level detection logic

---

## 🧪 Detection Rules
- ICMP Ping Detection
- TCP SYN Scan (Nmap)
- HTTP Traffic Monitoring

---

## 🚨 Response Mechanism
Upon detection of suspicious activity, the attacker IP can be blocked using firewall rules:
```bash
sudo ufw deny from <attacker-ip>
