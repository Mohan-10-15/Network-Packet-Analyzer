from database.db_manager import add_alert

from analyzer.threat_intelligence import (
    check_ip_reputation
)

from analyzer.mitre_mapper import (
    map_attack
)

from analyzer.geoip_lookup import (
    get_country
)

risk_score = 0

total_alerts = 0

SEVERITY_SCORES = {
    "LOW": 10,
    "MEDIUM": 20,
    "HIGH": 40,
    "CRITICAL": 60
}


def raise_alert(
    severity,
    source_ip,
    event
):

    global risk_score
    global total_alerts

    score = SEVERITY_SCORES.get(
        severity,
        0
    )

    country = get_country(
        source_ip
    )

    if check_ip_reputation(
        source_ip
    ):

        score += 50

        event = (
            f"{event} "
            f"[Known Malicious IP]"
        )

    mitre_id = map_attack(
        event.replace(
            " [Known Malicious IP]",
            ""
        )
    )

    event_details = (
        f"{event} | "
        f"{mitre_id} | "
        f"Location: {country}"
    )

    risk_score += score

    total_alerts += 1

    add_alert(
        severity,
        source_ip,
        event_details
    )

    print(
        f"[{severity}] "
        f"{event_details} "
        f"({source_ip})"
    )


def get_risk_score():

    return risk_score


def get_total_alerts():

    return total_alerts


def get_risk_level():

    score = risk_score

    if score < 50:

        return "LOW"

    elif score < 100:

        return "MEDIUM"

    elif score < 200:

        return "HIGH"

    return "CRITICAL"


def reset_risk_score():

    global risk_score
    global total_alerts

    risk_score = 0
    total_alerts = 0