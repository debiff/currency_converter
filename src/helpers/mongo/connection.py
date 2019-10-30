from mongoengine import register_connection


def register():
    register_connection(
        "IGeniusTest",
        "IGeniusTest",
        username="",
        password="",
        host="db",
        port=27017,
        authentication_source="admin",
    )
