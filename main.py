from parse import parse_all_files, dump_output
from nlpapi import GoogleNLPService


def main():
    objects = parse_all_files()
    nlp = GoogleNLPService()
    for object in objects:
        print(object['text'])
        # analyze_sentiment(subtitle['text'])
        entities = nlp.analyze_entities(object['text'])
        extracted_entities = nlp.extract_entities(entities.entities)
        object['entities'] = extracted_entities
        print(extracted_entities)
    for object in objects:
        dump_output(object)


if __name__ == "__main__":
    main()
