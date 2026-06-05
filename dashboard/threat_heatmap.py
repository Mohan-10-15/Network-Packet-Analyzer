from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem
)


class ThreatHeatmap(QTableWidget):

    def __init__(self):

        super().__init__()

        self.setColumnCount(2)

        self.setHorizontalHeaderLabels(
            [
                "Threat Type",
                "Count"
            ]
        )

    def update_heatmap(
        self,
        alerts
    ):

        threat_counts = {}

        for alert in alerts:

            event = alert[4]

            if "Port Scan" in event:

                threat = "Port Scan"

            elif "SYN Flood" in event:

                threat = "SYN Flood"

            elif "ARP Spoof" in event:

                threat = "ARP Spoof"

            elif "DNS Tunnel" in event:

                threat = "DNS Tunnel"

            else:

                threat = "Other"

            threat_counts[threat] = (
                threat_counts.get(
                    threat,
                    0
                ) + 1
            )

        self.setRowCount(
            len(threat_counts)
        )

        row = 0

        for threat, count in (
            sorted(
                threat_counts.items(),
                key=lambda x: x[1],
                reverse=True
            )
        ):

            self.setItem(
                row,
                0,
                QTableWidgetItem(
                    threat
                )
            )

            self.setItem(
                row,
                1,
                QTableWidgetItem(
                    str(count)
                )
            )

            row += 1