from scapy.all import sniff
from analyzer.protocol_decoder import decode_packet


def process_packet(packet):

    try:

        pkt = {}

        if packet.haslayer("Ether"):

            pkt["src_mac"] = packet["Ether"].src
            pkt["dst_mac"] = packet["Ether"].dst

        if packet.haslayer("IP"):

            pkt["src"] = packet["IP"].src
            pkt["dst"] = packet["IP"].dst

            if packet.haslayer("TCP"):

                pkt["protocol"] = "TCP"

                pkt["src_port"] = packet["TCP"].sport
                pkt["dst_port"] = packet["TCP"].dport

                pkt["flags"] = str(
                    packet["TCP"].flags
                )

            elif packet.haslayer("UDP"):

                pkt["protocol"] = "UDP"

                pkt["src_port"] = packet["UDP"].sport
                pkt["dst_port"] = packet["UDP"].dport

            elif packet.haslayer("ICMP"):

                pkt["protocol"] = "ICMP"

            else:

                pkt["protocol"] = "OTHER"

        if packet.haslayer("DNS"):

            try:

                pkt["dns_query"] = str(
                    packet["DNS"].qd.qname.decode()
                )

            except:

                pass

        decode_packet(pkt)

    except Exception as e:

        print(
            f"Capture Error: {e}"
        )


def start_capture():

    sniff(
        prn=process_packet,
        store=False
    )