import sys
import threading

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QTabWidget
)

from PyQt6.QtCore import QTimer

from matplotlib.backends.backend_qtagg import (
    FigureCanvasQTAgg as FigureCanvas
)

from capture.packet_capture import start_capture

from analyzer.protocol_decoder import (
    get_statistics,
    get_protocol_stats
)

from analyzer.threat_engine import (
    get_total_alerts,
    get_risk_level
)

from database.db_manager import (
    get_alerts
)

from reports.pdf_report import (
    generate_pdf
)

from dashboard.packet_table import PacketTable
from dashboard.alerts_widget import AlertsWidget
from dashboard.status_widget import StatusWidget
from dashboard.threat_feed import ThreatFeed
from dashboard.threat_gauge import ThreatGauge
from dashboard.threat_map import ThreatMap
from dashboard.threat_heatmap import ThreatHeatmap
from dashboard.incident_timeline import IncidentTimeline
from dashboard.kpi_card import KPICard

from dashboard.executive_metrics import (
    get_executive_metrics
)

from dashboard.charts_widget import (
    create_protocol_chart,
    create_ip_chart
)


class Dashboard(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Network Security Operations Center"
        )

        self.resize(
            1800,
            1000
        )

        self.protocol_canvas = None
        self.ip_canvas = None

        self.init_ui()

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.refresh_dashboard
        )

        self.timer.start(
            2000
        )

    def init_ui(self):

        main_layout = QVBoxLayout()

        title = QLabel(
            "Network Threat Detection & Traffic Intelligence Platform"
        )

        title.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
            color:#00ff99;
            padding:10px;
        """)

        main_layout.addWidget(title)

        # KPI CARDS

        cards_layout = QHBoxLayout()

        self.packet_card = KPICard(
            "📦 Packets"
        )

        self.alert_card = KPICard(
            "🚨 Alerts"
        )

        self.risk_card = KPICard(
            "⚠ Risk"
        )

        self.country_card = KPICard(
            "🎯 Top Threat"
        )

        cards_layout.addWidget(
            self.packet_card
        )

        cards_layout.addWidget(
            self.alert_card
        )

        cards_layout.addWidget(
            self.risk_card
        )

        cards_layout.addWidget(
            self.country_card
        )

        main_layout.addLayout(
            cards_layout
        )

        # STATUS

        self.status_widget = StatusWidget()

        main_layout.addWidget(
            self.status_widget
        )

        # THREAT GAUGE

        self.threat_gauge = ThreatGauge()

        main_layout.addWidget(
            self.threat_gauge
        )

        # BUTTONS

        button_layout = QHBoxLayout()

        self.start_btn = QPushButton(
            "Start Monitoring"
        )

        self.start_btn.clicked.connect(
            self.start_monitoring
        )

        self.report_btn = QPushButton(
            "Generate PDF Report"
        )

        self.report_btn.clicked.connect(
            self.export_report
        )

        button_layout.addWidget(
            self.start_btn
        )

        button_layout.addWidget(
            self.report_btn
        )

        main_layout.addLayout(
            button_layout
        )

        # CHARTS

        self.chart_layout = QHBoxLayout()

        main_layout.addLayout(
            self.chart_layout
        )

        # TABS

        self.tabs = QTabWidget()

        self.packet_table = PacketTable()

        self.alert_widget = AlertsWidget()

        self.threat_feed = ThreatFeed()

        self.timeline = IncidentTimeline()

        self.heatmap = ThreatHeatmap()

        self.threat_map = ThreatMap()

        self.tabs.addTab(
            self.packet_table,
            "Packets"
        )

        self.tabs.addTab(
            self.alert_widget,
            "Alerts"
        )

        self.tabs.addTab(
            self.threat_feed,
            "Threat Feed"
        )

        self.tabs.addTab(
            self.timeline,
            "Timeline"
        )

        self.tabs.addTab(
            self.heatmap,
            "Heatmap"
        )

        self.tabs.addTab(
            self.threat_map,
            "Threat Map"
        )

        main_layout.addWidget(
            self.tabs
        )

        self.setLayout(
            main_layout
        )

        self.setStyleSheet("""
    QWidget{
        background:#0d1117;
        color:white;
    }

    QPushButton{
        background:#238636;
        color:white;
        padding:10px;
        border:none;
        border-radius:8px;
        font-weight:bold;
    }

    QPushButton:hover{
        background:#2ea043;
    }

    QTabWidget::pane{
        border:1px solid #30363d;
        background:#161b22;
    }

    QTabBar::tab{
        background:#161b22;
        color:white;
        padding:12px;
        min-width:140px;
        border:1px solid #30363d;
        border-radius:6px;
    }

    QTabBar::tab:selected{
        background:#238636;
    }
""")
    def start_monitoring(self):

        thread = threading.Thread(
            target=start_capture,
            daemon=True
        )

        thread.start()

    def export_report(self):

        generate_pdf()

        QMessageBox.information(
            self,
            "Success",
            "Incident Report Generated"
        )

    def update_charts(self):

        stats = get_statistics()

        protocols = get_protocol_stats()

        ip_stats = stats["ips"]

        if self.protocol_canvas:

            self.chart_layout.removeWidget(
                self.protocol_canvas
            )

            self.protocol_canvas.deleteLater()

        if self.ip_canvas:

            self.chart_layout.removeWidget(
                self.ip_canvas
            )

            self.ip_canvas.deleteLater()

        protocol_fig = create_protocol_chart(
            protocols
        )

        ip_fig = create_ip_chart(
            ip_stats
        )

        self.protocol_canvas = FigureCanvas(
            protocol_fig
        )

        self.ip_canvas = FigureCanvas(
            ip_fig
        )

        self.chart_layout.addWidget(
            self.protocol_canvas
        )

        self.chart_layout.addWidget(
            self.ip_canvas
        )

    def refresh_dashboard(self):

        stats = get_statistics()

        risk = get_risk_level()

        self.packet_card.set_value(
            str(stats["packets"])
        )

        self.alert_card.set_value(
            str(get_total_alerts())
        )

        self.risk_card.set_value(
            risk
        )

        self.risk_card.set_risk_color(
            risk
        )    
        self.status_widget.update_status(
            risk
        )

        self.threat_gauge.update_score(
            risk
        )

        self.packet_table.update_table(
            stats["ips"]
        )

        alerts = get_alerts()

        metrics = get_executive_metrics(
            alerts
        )

        self.country_card.set_value(
            metrics["top_threat"]
        )

        self.alert_widget.clear()

        for alert in alerts:

            severity = alert[2]

            message = (
                f"{alert[4]} "
                f"({alert[3]})"
            )

            self.alert_widget.add_alert(
                severity,
                message
            )

        self.threat_feed.update_feed(
            alerts
        )

        self.timeline.update_incidents(
            alerts
        )

        self.heatmap.update_heatmap(
            alerts
        )

        self.threat_map.update_map(
            alerts
        )

        self.update_charts()


def launch_dashboard():

    app = QApplication(
        sys.argv
    )

    dashboard = Dashboard()

    dashboard.show()

    sys.exit(
        app.exec()
    )