from datetime import datetime


def valid_date(date: str) -> datetime:
    """

    :param date:
    :return:
    """
    date = datetime.strptime(date, "%Y-%m-%d")

    if date.weekday() is 5 or date.weekday() is 6:
        raise ValueError("The date must be a weekday")

    if date > datetime.today():
        raise ValueError("The date cannot be greater than today")

    return date
