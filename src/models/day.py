from mongoengine import (
    Document,
    EmbeddedDocumentField,
    EmbeddedDocument,
    DateField,
    ListField,
    StringField,
    FloatField,
)


class Currency(EmbeddedDocument):

    name = StringField()
    amount = FloatField()

    @classmethod
    def create(cls, name, amount):  # TODO: typing
        obj = cls()

        obj.name = name
        obj.amount = amount

        return obj


class Day(Document):
    meta = {"db_alias": "IGeniusTest", "collection": "Currencies"}

    reference_date = DateField()
    currencies = ListField(EmbeddedDocumentField(Currency))

    @classmethod
    def create(cls, date, currencies):  # TODO: typing
        obj = cls()

        obj.reference_date = date
        obj.currencies = currencies

        return obj
