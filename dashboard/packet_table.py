from PyQt6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem
)

class PacketTable(QTableWidget):

    def __init__(self):
        super().__init__()

        self.setColumnCount(2)

        self.setHorizontalHeaderLabels(
            [
                "Source IP",
                "Packets"
            ]
        )

    def update_table(self, ip_stats):

        self.setRowCount(
            len(ip_stats)
        )

        for row, (
            ip,
            count
        ) in enumerate(
            ip_stats.items()
        ):

            self.setItem(
                row,
                0,
                QTableWidgetItem(ip)
            )

            self.setItem(
                row,
                1,
                QTableWidgetItem(
                    str(count)
                )
            )