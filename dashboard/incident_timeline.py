from PyQt6.QtWidgets import QListWidget


class IncidentTimeline(QListWidget):

    def __init__(self):

        super().__init__()

        self.setMinimumWidth(350)

    def update_incidents(
        self,
        alerts
    ):

        self.clear()

        for alert in alerts[:20]:

            timestamp = alert[1]
            severity = alert[2]
            event = alert[4]

            self.addItem(
                f"{timestamp} | {severity} | {event}"
            )