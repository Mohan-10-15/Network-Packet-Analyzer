SUSPICIOUS_IPS = {
    "185.220.101.1",
    "45.95.147.236",
    "103.251.167.20"
}


def check_ip_reputation(ip):

    if ip in SUSPICIOUS_IPS:
        return True

    return False