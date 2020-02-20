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
            8: "PHONE_NUMBER",
            9: "ADDRESS",
            10: "DATE",
            11: "NUMBER",
            12: "PRICE",
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
    nlp = GoogleNLPService()
    with open("./subtitle/0adba949ed305baf9499481b3fe591b59da3744f.json", "r") as f:
        subtitle = json.loads(f.read())
        print(subtitle['text'])
        # analyze_sentiment(subtitle['text'])
        entities = nlp.analyze_entities(subtitle['text'])
        extracted_entities = nlp.extract_entities(entities.entities)
        subtitle['entities'] = extracted_entities
        print(subtitle)
