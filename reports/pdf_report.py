from reportlab.lib.pagesizes import letter

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from database.db_manager import get_alerts

from analyzer.threat_engine import (
    get_risk_score,
    get_total_alerts,
    get_risk_level
)

from datetime import datetime


def generate_pdf():

    pdf = SimpleDocTemplate(
        "incident_report.pdf",
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    content = []

    # ==========================
    # TITLE PAGE
    # ==========================

    content.append(
        Paragraph(
            "Network Threat Detection & Traffic Intelligence Platform",
            styles["Title"]
        )
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    content.append(
        Paragraph(
            f"Generated: {datetime.now()}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    # ==========================
    # EXECUTIVE SUMMARY
    # ==========================

    content.append(
        Paragraph(
            "Executive Summary",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            f"Total Alerts: {get_total_alerts()}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Risk Score: {get_risk_score()}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Risk Level: {get_risk_level()}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(
            1,
            20
        )
    )

    content.append(
        PageBreak()
    )

    # ==========================
    # INCIDENT DETAILS
    # ==========================

    content.append(
        Paragraph(
            "Security Incidents",
            styles["Heading1"]
        )
    )

    content.append(
        Spacer(
            1,
            10
        )
    )

    alerts = get_alerts()

    if len(alerts) == 0:

        content.append(
            Paragraph(
                "No incidents detected.",
                styles["Normal"]
            )
        )

    else:

        for alert in alerts:

            incident_text = (
                f"<b>ID:</b> {alert[0]}<br/>"
                f"<b>Timestamp:</b> {alert[1]}<br/>"
                f"<b>Severity:</b> {alert[2]}<br/>"
                f"<b>Source IP:</b> {alert[3]}<br/>"
                f"<b>Event:</b> {alert[4]}"
            )

            content.append(
                Paragraph(
                    incident_text,
                    styles["Normal"]
                )
            )

            content.append(
                Spacer(
                    1,
                    10
                )
            )

    # ==========================
    # REPORT FOOTER
    # ==========================

    content.append(
        Spacer(
            1,
            20
        )
    )

    content.append(
        Paragraph(
            "End of Security Incident Report",
            styles["Heading2"]
        )
    )

    pdf.build(
        content
    )

    print(
        "Professional PDF report generated."
    )