from PyQt6.QtWidgets import QLabel


class StatusWidget(QLabel):

    def __init__(self):

        super().__init__()

        self.setText(
            "SYSTEM STATUS: SECURE"
        )

        self.setStyleSheet("""
            background:#1f1f1f;
            color:#00ff99;
            font-size:18px;
            padding:15px;
            border-radius:10px;
        """)

    def update_status(
        self,
        risk_level
    ):

        if risk_level == "LOW":

            self.setText(
                "SYSTEM STATUS: SECURE"
            )

        elif risk_level == "MEDIUM":

            self.setText(
                "SYSTEM STATUS: WARNING"
            )

        elif risk_level == "HIGH":

            self.setText(
                "SYSTEM STATUS: DANGER"
            )

        else:

            self.setText(
                "SYSTEM STATUS: CRITICAL"
            )