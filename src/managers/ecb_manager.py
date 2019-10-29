import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Dict

import requests


def currencies_per_day(reference_date: datetime) -> Dict:
    rates = requests.get(
        "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml"
    )

    # The real root of the rates are the third node of the xml
    rates_root = ET.fromstring(rates.content)[2]

    for cube in rates_root:
        if datetime.strptime(cube.attrib["time"], "%Y-%m-%d") == reference_date:
            break

    currencies = {"EUR": 1}

    for currency in cube:
        if "currency" in currency.attrib:
            currencies[currency.attrib["currency"]] = float(currency.attrib["rate"])

    return currencies
