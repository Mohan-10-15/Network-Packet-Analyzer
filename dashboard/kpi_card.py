from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt


class KPICard(QLabel):

    def __init__(
        self,
        title,
        value="0"
    ):

        super().__init__()

        self.title = title

        self.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.setMinimumHeight(
            100
        )

        self.set_value(
            value
        )

        self.setStyleSheet("""
            QLabel{
                background:#161b22;
                border:1px solid #30363d;
                border-radius:15px;
                color:white;
                font-weight:bold;
                padding:10px;
            }
        """)

    def set_value(
        self,
        value
    ):

        self.setText(
            f"""
            <div style='font-size:15px;color:#8b949e'>
            {self.title}
            </div>

            <div style='font-size:28px;
                        font-weight:bold;
                        color:white'>
            {value}
            </div>
            """
        )

    def set_risk_color(
        self,
        risk
    ):

        colors = {
            "LOW": "#238636",
            "MEDIUM": "#d29922",
            "HIGH": "#fb8500",
            "CRITICAL": "#da3633"
        }

        color = colors.get(
            risk,
            "#161b22"
        )

        self.setStyleSheet(
            f"""
            QLabel{{
                background:{color};
                border-radius:15px;
                color:white;
                font-weight:bold;
                padding:10px;
            }}
            """
        )