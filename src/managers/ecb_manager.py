import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Dict

import requests
from src.models.day import Currency, Day


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


def store_currencies():
    rates = requests.get(
        "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml"
    )

    # The real root of the rates are the third node of the xml
    rates_root = ET.fromstring(rates.content)[2]

    day_list = []

    for cube in rates_root:
        day_list.append(cube)

    for day in day_list:
        if Day.objects(reference_date=day.attrib["time"]).count() == 0:
            currencies_list = []
            for currency in day:
                currencies_list.append(
                    Currency(
                        currency.attrib["currency"], float(currency.attrib["rate"])
                    )
                )
            Day(day.attrib["time"], currencies_list).save()
