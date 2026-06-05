mac_ip_map = {}

def detect_arp_spoof(ip, mac):

    if ip in mac_ip_map:

        if mac_ip_map[ip] != mac:
            return True

    mac_ip_map[ip] = mac

    return False