from collections import Counter

from analyzer.threat_engine import (
    get_risk_score
)


def get_executive_metrics(alerts):

    metrics = {
        "top_threat": "None",
        "top_country": "Unknown",
        "highest_severity": "LOW",
        "risk_score": get_risk_score(),
        "total_alerts": len(alerts)
    }

    if not alerts:
        return metrics

    threat_counter = Counter()
    country_counter = Counter()

    severity_rank = {
        "LOW": 1,
        "MEDIUM": 2,
        "HIGH": 3,
        "CRITICAL": 4
    }

    highest = "LOW"

    for alert in alerts:

        severity = alert[2]
        event = alert[4]

        if severity_rank.get(
            severity,
            0
        ) > severity_rank.get(
            highest,
            0
        ):
            highest = severity

        if "Port Scan" in event:
            threat_counter["Port Scan"] += 1

        elif "SYN Flood" in event:
            threat_counter["SYN Flood"] += 1

        elif "ARP Spoof" in event:
            threat_counter["ARP Spoof"] += 1

        elif "DNS Tunnel" in event:
            threat_counter["DNS Tunnel"] += 1

        if "Location:" in event:

            country = (
                event.split(
                    "Location:"
                )[-1]
                .strip()
            )

            country_counter[
                country
            ] += 1

    if threat_counter:

        metrics["top_threat"] = (
            threat_counter.most_common(1)[0][0]
        )

    if country_counter:

        metrics["top_country"] = (
            country_counter.most_common(1)[0][0]
        )

    metrics["highest_severity"] = highest

    return metrics