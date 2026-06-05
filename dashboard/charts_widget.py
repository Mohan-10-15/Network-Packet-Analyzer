from matplotlib.figure import Figure

def create_protocol_chart(protocols):

    fig = Figure(figsize=(5,4))

    ax = fig.add_subplot(111)

    labels = []
    values = []

    for proto, count in protocols.items():

        if count > 0:

            labels.append(proto)
            values.append(count)

    if len(values) == 0:

        values = [1]
        labels = ["No Data"]

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%"
    )

    ax.set_title(
        "Protocol Distribution"
    )

    return fig


def create_ip_chart(ip_stats):

    fig = Figure(figsize=(5,4))

    ax = fig.add_subplot(111)

    sorted_ips = sorted(
        ip_stats.items(),
        key=lambda x: x[1],
        reverse=True
    )

    top_ips = sorted_ips[:10]

    labels = [x[0] for x in top_ips]

    values = [x[1] for x in top_ips]

    ax.bar(
        labels,
        values
    )

    ax.set_title(
        "Top Source IPs"
    )

    ax.tick_params(
        axis='x',
        rotation=45
    )

    return fig