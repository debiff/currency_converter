from datetime import datetime
from typing import Tuple

from src.managers import ecb_manager


def convert(
    amount: float, src_currency: str, dest_currency: str, reference_date: datetime
) -> Tuple[float, str]:
    """

    :param amount:
    :param src_currency:
    :param dest_currency:
    :param reference_date:
    :return:
    """
    currencies_list = ecb_manager.currencies_per_day(reference_date)

    if src_currency not in currencies_list or dest_currency not in currencies_list:
        raise ValueError("SrcCurrency or DestCurrency not found")

    amount_in_euro = amount / currencies_list[src_currency]
    converted_amount = round(amount_in_euro * currencies_list[dest_currency], 2)

    return converted_amount, dest_currency
