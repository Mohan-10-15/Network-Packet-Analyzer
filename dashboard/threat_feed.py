from PyQt6.QtWidgets import QListWidget


class ThreatFeed(QListWidget):

    def __init__(self):

        super().__init__()

    def update_feed(
        self,
        alerts
    ):

        self.clear()

        for alert in alerts:

            severity = alert[2]
            event = alert[4]

            self.addItem(
                f"[{severity}] {event}"
            )