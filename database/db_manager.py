import sqlite3

connection = sqlite3.connect(
    "security.db",
    check_same_thread=False
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    severity TEXT,
    source_ip TEXT,
    event TEXT
)
""")

connection.commit()

def add_alert(
    severity,
    source_ip,
    event
):
    cursor.execute(
        """
        INSERT INTO alerts(
            timestamp,
            severity,
            source_ip,
            event
        )
        VALUES(
            datetime('now'),
            ?,
            ?,
            ?
        )
        """,
        (
            severity,
            source_ip,
            event
        )
    )

    connection.commit()

def get_alerts():
    cursor.execute("""
    SELECT *
    FROM alerts
    ORDER BY id DESC
    LIMIT 50
    """)

    return cursor.fetchall()