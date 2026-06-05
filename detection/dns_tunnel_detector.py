dns_tracker = {}

def detect_dns_tunnel(domain):

    if len(domain) > 60:
        return True

    return False