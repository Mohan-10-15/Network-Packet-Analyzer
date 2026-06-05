from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QColor


class AlertsWidget(QTextEdit):

    def __init__(self):

        super().__init__()

        self.setReadOnly(True)

        self.setStyleSheet("""
            background:#1f1f1f;
            color:white;
            border-radius:10px;
            padding:10px;
        """)

    def add_alert(
        self,
        severity,
        text
    ):

        if severity == "CRITICAL":

            self.setTextColor(
                QColor(255, 0, 0)
            )

        elif severity == "HIGH":

            self.setTextColor(
                QColor(255, 140, 0)
            )

        elif severity == "MEDIUM":

            self.setTextColor(
                QColor(255, 255, 0)
            )

        else:

            self.setTextColor(
                QColor(0, 200, 255)
            )

        self.append(
            f"[{severity}] {text}"
        )