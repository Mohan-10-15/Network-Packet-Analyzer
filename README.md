# Network Threat Detection & Traffic Intelligence Platform

## Overview

A professional cybersecurity monitoring platform developed using Python, Scapy, SQLite, PyQt6, and Threat Intelligence techniques.

The platform captures live network traffic, analyzes packets in real-time, detects suspicious activities, maps threats to the MITRE ATT&CK framework, performs GeoIP analysis, and presents results through a Security Operations Center (SOC) style dashboard.

---

## Features

### Network Monitoring
- Real-time packet capture using Scapy
- Protocol analysis (TCP, UDP, ICMP)
- Top Talkers analysis
- Protocol distribution analytics

### Threat Detection
- Port Scan Detection
- SYN Flood Detection
- ARP Spoof Detection
- DNS Tunnel Detection

### Threat Intelligence
- Known malicious IP detection
- MITRE ATT&CK technique mapping
- GeoIP country analysis

### Dashboard
- Real-time monitoring dashboard
- Threat Feed
- Incident Timeline
- Threat Heatmap
- Threat Map
- Executive Security Metrics

### Reporting
- SQLite alert storage
- Incident logging
- PDF security reports

---

## Technology Stack

| Component | Technology |
|------------|------------|
| Language | Python 3 |
| Packet Capture | Scapy |
| GUI | PyQt6 |
| Database | SQLite |
| Charts | Matplotlib |
| GeoIP | MaxMind GeoLite2 |
| Reporting | ReportLab |

---

## Architecture

```text
Network Interface
        ↓
Packet Capture Engine
        ↓
Protocol Decoder
        ↓
Threat Detection Engine
        ↓
Threat Intelligence
        ↓
MITRE ATT&CK Mapping
        ↓
SQLite Database
        ↓
SOC Dashboard
        ↓
PDF Reports
```

---

## Project Structure

```text
NetworkPacketAnalyzer-Pro
│
├── analyzer
├── capture
├── dashboard
├── database
├── detection
├── geoip
├── reports
├── logs
│
├── main.py
└── README.md
```

---

## Dashboard Components

### Security Operations Center Dashboard

- Executive Metrics
- Threat Gauge
- Threat Feed
- Threat Heatmap
- Threat Map
- Incident Timeline
- Protocol Analytics
- Alert Center

---

## MITRE ATT&CK Mapping

| Attack | MITRE Technique |
|----------|----------------|
| Port Scan | T1046 |
| SYN Flood | T1498 |
| ARP Spoof | T1557 |
| DNS Tunnel | T1071.004 |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/NetworkPacketAnalyzer-Pro.git
cd NetworkPacketAnalyzer-Pro
```

### Install Dependencies

```bash
pip install scapy
pip install pyqt6
pip install matplotlib
pip install reportlab
pip install geoip2
```

### Run Application

```bash
python main.py
```

---

## Screenshots

### Dashboard

Add dashboard screenshot here

### Threat Feed

Add threat feed screenshot here

### Threat Heatmap

Add heatmap screenshot here

### PDF Report

Add PDF report screenshot here

---

## Future Enhancements

- Machine Learning Threat Detection
- Threat Correlation Engine
- Web Dashboard
- SIEM Integration
- Real-Time Threat Intelligence Feeds
- Email Alerting
- Cloud Deployment

---

## Author

Mohanakrishnan C

Cybersecurity Enthusiast | Network Security | Threat Detection | SOC Engineering
