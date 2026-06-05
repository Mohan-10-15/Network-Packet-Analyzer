from PyQt6.QtWidgets import QProgressBar


class ThreatGauge(QProgressBar):

    def __init__(self):

        super().__init__()

        self.setMinimum(0)

        self.setMaximum(100)

        self.setValue(0)

        self.setMinimumHeight(
            35
        )

        self.setFormat(
            "Threat Score: %p%"
        )

        self.update_color(
            "#238636"
        )

    def update_color(
        self,
        color
    ):

        self.setStyleSheet(
            f"""
            QProgressBar{{
                background:#161b22;
                border:1px solid #30363d;
                border-radius:10px;
                text-align:center;
                color:white;
                font-weight:bold;
            }}

            QProgressBar::chunk{{
                background:{color};
                border-radius:10px;
            }}
            """
        )

    def update_score(
        self,
        risk_level
    ):

        mapping = {
            "LOW": (25, "#238636"),
            "MEDIUM": (50, "#d29922"),
            "HIGH": (75, "#fb8500"),
            "CRITICAL": (100, "#da3633")
        }

        value, color = mapping.get(
            risk_level,
            (0, "#238636")
        )

        self.setValue(
            value
        )

        self.update_color(
            color
        )