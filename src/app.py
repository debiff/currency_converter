from flask import Flask
from flask_restful import Api

from src.apis.convert import Convert
from src.helpers.mongo import connection

from src.managers import ecb_manager


def create_app() -> Flask:
    app = Flask(__name__)
    api = Api(app)
    # Binding routes
    api.add_resource(Convert, "/convert/<string:src_currency>/<string:dest_currency>")

    return app


app = create_app()


@app.before_first_request
def before_first_request_func() -> None:
    connection.register()
    ecb_manager.store_currencies()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
