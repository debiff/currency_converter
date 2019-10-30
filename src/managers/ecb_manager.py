import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Dict

import requests
from src.models.day import Currency, Day


def currencies_per_day(reference_date: datetime) -> Dict:

    day = Day.objects.get(reference_date=reference_date)

    currencies = {"EUR": float(1)}

    for currency in day.currencies:
        currencies[currency.name] = float(currency.amount)

    return currencies


def store_currencies() -> None:
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
