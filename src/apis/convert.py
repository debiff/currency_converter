from typing import Tuple, Dict

from flask_restful import Resource, reqparse

from src.helpers.flask.validator import valid_date
from src.managers import conversion_manager


class Convert(Resource):
    """
    Manage the conversion between a currency and another with respect to the euro's value.
    """

    def __init__(self):
        super(Convert, self).__init__()
        self.reqparse = reqparse.RequestParser()

        self.reqparse.add_argument(
            "amount",
            type=float,
            required=True,
            help="No amount provided",
            location="args",
        )
        self.reqparse.add_argument(
            "reference_date", type=valid_date, default="", location="args"
        )

    def get(self, src_currency: str, dest_currency: str) -> Tuple[Dict, int]:
        """

        :param src_currency: str
        :param dest_currency: str

        :return:
        """
        args = self.reqparse.parse_args()

        amount = args["amount"]
        reference_date = args["reference_date"]

        if amount < 0:
            return {"message": "Amount must be greater than 0"}, 400

        try:
            amount, currency = conversion_manager.convert(
                amount, src_currency, dest_currency, reference_date
            )
        except ValueError as error:
            return {"message": error}, 400

        return {"amount": amount, "currency": currency}, 200
