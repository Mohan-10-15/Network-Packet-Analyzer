import time

PORT_THRESHOLD = 5
TIME_WINDOW = 15

ip_port_tracker = {}

def detect_port_scan(
    source_ip,
    destination_port
):
    current_time = time.time()

    if source_ip not in ip_port_tracker:
        ip_port_tracker[source_ip] = []

    ip_port_tracker[source_ip].append(
        (
            destination_port,
            current_time
        )
    )

    ip_port_tracker[source_ip] = [
        item
        for item in ip_port_tracker[source_ip]
        if current_time - item[1]
        <= TIME_WINDOW
    ]

    unique_ports = set(
        port
        for port, _
        in ip_port_tracker[source_ip]
    )

    if len(unique_ports) >= PORT_THRESHOLD:
        print(
            f"[PORT SCAN] "
            f"{source_ip} "
            f"attempted "
            f"{len(unique_ports)} ports"
        )

        return True

    return False
