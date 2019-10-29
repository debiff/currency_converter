import pytest
from pytest_bdd import scenarios, given, then

from src.app import create_app


@pytest.fixture
def app():
    _app = create_app()
    return _app


@pytest.fixture
def client(app):
    _client = app.test_client()
    return _client


CONVERTERS = {"amount": float, "srcCurrency": str, "destCurrency": str, "result": float}

scenarios("../features/convert.feature", example_converters=CONVERTERS)


@given(
    'the convert API service is queried to convert "<amount>" "<src_currency>" in "<dst_currency>" '
    'in data "<reference_date>"'
)
def converter_response(app, client, amount, src_currency, dst_currency, reference_date):
    return client.get(
        "/converter/{}/{}?amount={}&reference_date={}".format(
            src_currency, dst_currency, amount, reference_date
        )
    )


@then('the response status code is "200"')
def converter_code(converter_response):
    assert converter_response.status_code == 200


@then('the response contains the amount converted "<result>"')
def converter_amount(converter_response, result):
    assert converter_response.json["amount"] == result
