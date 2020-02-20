import json
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = './key/credentials.json'

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE)

# Instantiates a client
client = language.LanguageServiceClient(credentials=credentials)


def analyze_sentiment(text):
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    response = client.analyze_sentiment(document=document)
    print(response)
    sentiment = response.document_sentiment

    print('Text: {}'.format(text))
    print('Sentiment Score: {}, Magnitude: {}'.format(sentiment.score, sentiment.magnitude))


def analyze_syntax(text):
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_syntax(document, encoding_type=encoding_type)
    print(response)


if __name__ == "__main__":
    # with open("./subtitle/0c82ac666286fe7d62712b8bfa5fc8a284a6066d.json", "r") as f:
    #     subtitle = json.loads(f.read())
    #     # analyze_sentiment(subtitle['text'])
    #     analyze_syntax(subtitle['text'])
    byte_str = b'\357\274\210\346\211\200\346\234\211\347\227\205\346\210\277\350\254\235\347\265\225\346\216\242\350\250\252\357\274\214\345\244\232\350\254\235\345\220\210\344\275\234\357\274\211'
    print(byte_str.decode('utf-8'))
