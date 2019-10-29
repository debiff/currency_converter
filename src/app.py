from flask import Flask
from flask_restful import Api


def create_app():
    app = Flask(__name__)
    api = Api(app)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
