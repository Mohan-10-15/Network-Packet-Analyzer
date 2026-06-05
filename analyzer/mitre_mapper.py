MITRE_MAP = {
    "Port Scan Detected":
        "T1046 - Network Service Discovery",

    "Possible SYN Flood":
        "T1498 - Network Denial of Service",

    "ARP Spoofing Detected":
        "T1557 - Adversary-in-the-Middle",

    "Possible DNS Tunnel":
        "T1071.004 - DNS Protocol"
}


def map_attack(event):

    return MITRE_MAP.get(
        event,
        "Unknown Technique"
    )