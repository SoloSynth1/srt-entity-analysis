import json

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account


class GoogleNLPService:

    def __init__(self, service_account_file='./key/credentials.json'):
        self.service_account_file = service_account_file
        self.credentials = service_account.Credentials.from_service_account_file(self.service_account_file)
        self.client = language.LanguageServiceClient(credentials=self.credentials)
        self.ENCODING_TYPE = enums.EncodingType.UTF8
        self.ENTITY_ENUM_TYPE = {
            0: "UNKNOWN",
            1: "PERSON",
            2: "LOCATION",
            3: "ORGANIZATION",
            4: "EVENT",
            5: "WORK_OF_ART",
            6: "CONSUMER_GOOD",
            7: "OTHER",
            9: "PHONE_NUMBER",
            10: "ADDRESS",
            11: "DATE",
            12: "NUMBER",
            13: "PRICE",
        }

    def document_from_text(self, text):
        return types.Document(content=text, type=enums.Document.Type.PLAIN_TEXT)

    def analyze_sentiment(self, text):
        document = self.document_from_text(text)
        response = self.client.analyze_sentiment(document=document, encoding_type=self.ENCODING_TYPE)
        return response

    def analyze_syntax(self, text):
        document = self.document_from_text(text)
        response = self.client.analyze_syntax(document, encoding_type=self.ENCODING_TYPE)
        return response

    def analyze_entities(self, text):
        document = self.document_from_text(text)
        response = self.client.analyze_entities(document, encoding_type=self.ENCODING_TYPE)
        return response

    def analyze_entity_sentiment(self, text):
        document = self.document_from_text(text)
        response = self.client.analyze_entity_sentiment(document, encoding_type=self.ENCODING_TYPE)
        return response

    def extract_entities(self, entities):
        words = []
        for entity in entities:
            word = {
                "name": entity.name,
                "type": self.ENTITY_ENUM_TYPE[entity.type],
                "salience": entity.salience,
            }
            words.append(word)
        return words


if __name__ == "__main__":
    print(enums.Entity.Type.EVENT, enums.Entity.Type.EVENT.value)
    print(enums.Entity.Type.ADDRESS, enums.Entity.Type.ADDRESS.value)
    print(enums.Entity.Type.CONSUMER_GOOD, enums.Entity.Type.CONSUMER_GOOD.value)
    print(enums.Entity.Type.DATE, enums.Entity.Type.DATE.value)
    print(enums.Entity.Type.LOCATION, enums.Entity.Type.LOCATION.value)
    print(enums.Entity.Type.NUMBER, enums.Entity.Type.NUMBER.value)
    print(enums.Entity.Type.ORGANIZATION, enums.Entity.Type.ORGANIZATION.value)
    print(enums.Entity.Type.OTHER, enums.Entity.Type.OTHER.value)
    print(enums.Entity.Type.PERSON, enums.Entity.Type.PERSON.value)
    print(enums.Entity.Type.PHONE_NUMBER, enums.Entity.Type.PHONE_NUMBER.value)
    print(enums.Entity.Type.PRICE, enums.Entity.Type.PRICE.value)
    print(enums.Entity.Type.UNKNOWN, enums.Entity.Type.UNKNOWN.value)
    print(enums.Entity.Type.WORK_OF_ART, enums.Entity.Type.WORK_OF_ART.value)