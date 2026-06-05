import ipaddress
import geoip2.database

reader = geoip2.database.Reader(
    "geoip/GeoLite2-Country.mmdb"
)


def get_country(ip):

    try:

        address = ipaddress.ip_address(ip)

        if address.is_private:

            return "Local Network"

        response = reader.country(ip)

        return (
            response.country.name
            or "Unknown"
        )

    except:

        return "Unknown"