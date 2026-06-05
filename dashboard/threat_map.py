from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem
)


class ThreatMap(QTableWidget):

    def __init__(self):

        super().__init__()

        self.setColumnCount(2)

        self.setHorizontalHeaderLabels(
            [
                "Location",
                "Threat Count"
            ]
        )

    def update_map(
        self,
        alerts
    ):

        location_counts = {}

        for alert in alerts:

            event = alert[4]

            if "Location:" in event:

                location = event.split(
                    "Location:"
                )[-1].strip()

                location_counts[
                    location
                ] = (
                    location_counts.get(
                        location,
                        0
                    ) + 1
                )

        self.setRowCount(
            len(location_counts)
        )

        row = 0

        for location, count in (
            location_counts.items()
        ):

            self.setItem(
                row,
                0,
                QTableWidgetItem(
                    location
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