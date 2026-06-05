from detection.port_scan_detector import detect_port_scan
from detection.syn_flood_detector import detect_syn_flood
from detection.arp_spoof_detector import detect_arp_spoof
from detection.dns_tunnel_detector import detect_dns_tunnel

from analyzer.threat_engine import raise_alert

packet_counter = 0

protocol_stats = {
    "TCP": 0,
    "UDP": 0,
    "ICMP": 0,
    "OTHER": 0
}

ip_stats = {}

detected_sources = set()


def decode_packet(packet):

    global packet_counter

    packet_counter += 1

    source_ip = packet.get(
        "src",
        "Unknown"
    )

    protocol = packet.get(
        "protocol",
        "OTHER"
    )

    protocol_stats[protocol] = (
        protocol_stats.get(
            protocol,
            0
        ) + 1
    )

    ip_stats[source_ip] = (
        ip_stats.get(
            source_ip,
            0
        ) + 1
    )

    destination_port = packet.get(
        "dst_port",
        0
    )

    # ==========================
    # PORT SCAN DETECTION
    # ==========================

    if detect_port_scan(
        source_ip,
        destination_port
    ):

        event_id = (
            source_ip,
            "PORT_SCAN"
        )

        if event_id not in detected_sources:

            detected_sources.add(
                event_id
            )

            raise_alert(
                "HIGH",
                source_ip,
                "Port Scan Detected"
            )

    # ==========================
    # SYN FLOOD DETECTION
    # ==========================

    tcp_flags = packet.get(
        "flags",
        ""
    )

    if protocol == "TCP":

        if "S" in tcp_flags:

            if detect_syn_flood(
                source_ip
            ):

                event_id = (
                    source_ip,
                    "SYN_FLOOD"
                )

                if event_id not in detected_sources:

                    detected_sources.add(
                        event_id
                    )

                    raise_alert(
                        "CRITICAL",
                        source_ip,
                        "Possible SYN Flood"
                    )

    # ==========================
    # ARP SPOOF DETECTION
    # ==========================

    src_mac = packet.get(
        "src_mac"
    )

    if src_mac:

        if detect_arp_spoof(
            source_ip,
            src_mac
        ):

            event_id = (
                source_ip,
                "ARP_SPOOF"
            )

            if event_id not in detected_sources:

                detected_sources.add(
                    event_id
                )

                raise_alert(
                    "CRITICAL",
                    source_ip,
                    "ARP Spoofing Detected"
                )

    # ==========================
    # DNS TUNNEL DETECTION
    # ==========================

    dns_query = packet.get(
        "dns_query"
    )

    if dns_query:

        if detect_dns_tunnel(
            dns_query
        ):

            event_id = (
                source_ip,
                "DNS_TUNNEL"
            )

            if event_id not in detected_sources:

                detected_sources.add(
                    event_id
                )

                raise_alert(
                    "HIGH",
                    source_ip,
                    "Possible DNS Tunnel"
                )


def get_statistics():

    return {
        "packets": packet_counter,
        "protocols": protocol_stats,
        "ips": ip_stats
    }


def get_protocol_stats():

    return protocol_stats


def get_top_talkers():

    return sorted(
        ip_stats.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]