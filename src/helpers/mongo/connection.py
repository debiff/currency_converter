from mongoengine import register_connection
import os


def register() -> None:
    register_connection(
        "IGeniusTest",
        "IGeniusTest",
        username="",
        password="",
        host=os.environ["DB_NAME"],
        port=27017,
        authentication_source="admin",
    )
