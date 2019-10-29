from flask import Flask
from flask_restful import Api

from src.apis.convert import Convert


def create_app():
    app = Flask(__name__)
    api = Api(app)

    # Binding routes
    api.add_resource(Convert, "/convert/<string:src_currency>/<string:dest_currency>")

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
